---
title: My RSS and Bookmarks Workflow
categories:
- chores
date: "2026-05-26"
tags:
- RSS
- bookmark
---



# My RSS Workflow



I use RSS to subscribe to my favorite feeds and reliance on [Karakeep](https://karakeep.app/) for bookmarking. To streamline this, I sync [Miniflux](https://miniflux.app/) with Karakeep so that any saved items in my RSS reader are automatically saved as bookmarks. Additionally, I’ve integrated Miniflux with Telegram to easily share interesting articles with my friends.

```mermaid
graph TD
    A[RSS Feed Sources] -->|1. Auto-fetch periodically| B(Miniflux Reader)

    B -->|2. New Article Arrives| H[Trigger Telegram Bot]
    H -->|3. Auto-post| G[(Telegram Channel)]
    
    B -->|4. User Reads & Stars| C[Star Article]
    C -->|5. Sync Integration| E[(Karakeep Bookmarks)]

```

