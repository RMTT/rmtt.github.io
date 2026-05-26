{
  description = "Hugo development environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            hugo
            git
            python3
            python3Packages.cloudflare
          ];

          shellHook = ''
            echo "Hugo development environment loaded."
            echo "Hugo version: $(hugo version)"
            echo "Python environment loaded (with latest cloudflare SDK from PyPI)."
          '';
        };
      }
    );
}
