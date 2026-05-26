import os
import re
import argparse
import mimetypes
import urllib.request
import urllib.error


def get_content_type(file_path):
    return mimetypes.guess_type(file_path)[0] or "application/octet-stream"


def upload_image_r2(image_path, post_dir_name, api_token, account_id, bucket_name, public_url_base):
    """Uploads an image to Cloudflare R2 using the Cloudflare API via HTTP PUT and returns the public URL."""
    print(f"  Uploading {image_path} to R2...")

    file_name = os.path.basename(image_path)
    object_name = f"posts/{post_dir_name}/{file_name}"

    content_type = get_content_type(image_path)

    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/r2/buckets/{bucket_name}/objects/{object_name}"

    try:
        with open(image_path, 'rb') as f:
            body = f.read()

        req = urllib.request.Request(url, data=body, method='PUT')
        req.add_header('Authorization', f'Bearer {api_token}')
        req.add_header('Content-Type', content_type)

        with urllib.request.urlopen(req) as response:
            if response.status not in (200, 201):
                raise Exception(f"HTTP {response.status}: {response.read().decode('utf-8')}")

    except urllib.error.HTTPError as e:
        raise Exception(f"Failed to upload to R2 (HTTP {e.code}): {e.read().decode('utf-8')}")
    except Exception as e:
        raise Exception(f"Failed to upload to R2: {e}")

    public_url_base = public_url_base.rstrip('/')
    if not public_url_base.startswith(('http://', 'https://')):
        public_url_base = f"https://{public_url_base}"
        
    return f"{public_url_base}/{object_name}"


def process_markdown_file(md_path, api_token, account_id, bucket_name, public_url_base):
    """Processes a single markdown file: uploads local images and replaces URLs."""
    md_dir = os.path.dirname(md_path)
    post_dir_name = os.path.basename(md_dir)

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    local_images_to_delete = []

    def replacer(match):
        alt_text = match.group(1)
        img_path = match.group(2)

        if img_path.startswith(("http://", "https://")):
            return match.group(0)

        full_img_path = os.path.join(md_dir, img_path)

        if not os.path.exists(full_img_path):
            print(f"  Warning: Local image not found: {full_img_path}")
            return match.group(0)

        try:
            url = upload_image_r2(
                full_img_path,
                post_dir_name,
                api_token,
                account_id,
                bucket_name,
                public_url_base,
            )
            print(f"  Success: Uploaded to {url}")
            local_images_to_delete.append(full_img_path)
            return f"![{alt_text}]({url})"
        except Exception as e:
            print(f"  Error uploading {full_img_path}: {e}")
            return match.group(0)

    pattern = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated markdown file: {md_path}")

    for img in set(local_images_to_delete):
        if os.path.exists(img):
            os.remove(img)
            print(f"  Deleted local photo: {img}")


def main():
    parser = argparse.ArgumentParser(
        description="Scan markdown files, upload local photos to Cloudflare R2, and delete local photos."
    )
    parser.add_argument(
        "--dir",
        default=os.getenv("POSTS_DIR", "content/posts"),
        help="Directory containing markdown posts (default: content/posts)",
    )
    parser.add_argument(
        "--account-id",
        default=os.getenv("CLOUDFLARE_ACCOUNT_ID"),
        required=not os.getenv("CLOUDFLARE_ACCOUNT_ID"),
        help="Cloudflare Account ID (env: CLOUDFLARE_ACCOUNT_ID)",
    )
    parser.add_argument(
        "--api-token",
        default=os.getenv("CLOUDFLARE_API_TOKEN"),
        required=not os.getenv("CLOUDFLARE_API_TOKEN"),
        help="Cloudflare API Token (env: CLOUDFLARE_API_TOKEN)",
    )
    parser.add_argument(
        "--bucket",
        default=os.getenv("R2_BUCKET"),
        required=not os.getenv("R2_BUCKET"),
        help="R2 Bucket Name (env: R2_BUCKET)",
    )
    parser.add_argument(
        "--public-url",
        default=os.getenv("R2_PUBLIC_URL"),
        required=not os.getenv("R2_PUBLIC_URL"),
        help="Base URL for the public bucket (env: R2_PUBLIC_URL)",
    )
    args = parser.parse_args()

    posts_dir = args.dir
    if not os.path.exists(posts_dir):
        print(f"Error: Directory {posts_dir} does not exist.")
        return

    # Cloudflare API token is used directly now

    print(f"Scanning directory: {posts_dir}")
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith(".md") or file.endswith(".mdx"):
                md_path = os.path.join(root, file)
                print(f"\nProcessing {md_path}")
                process_markdown_file(
                    md_path, args.api_token, args.account_id, args.bucket, args.public_url
                )

    print("\nProcess completed.")


if __name__ == "__main__":
    main()
