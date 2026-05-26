---
title: 我的 RSS 与书签工作流
categories:
- chores
date: "2026-5-26"
tags:
- RSS
- bookmark
---



# 我的 RSS 工作流



我使用 RSS 订阅我喜欢的源，并依赖 [Karakeep](https://karakeep.app/) 来管理书签。为了简化这个流程，我将 [Miniflux](https://miniflux.app/) 与 Karakeep 进行了同步集成，这样我在 RSS 阅读器中保存的任何文章都会自动保存为书签。此外，我还将 Miniflux 与 Telegram 进行了集成，以便轻松地与朋友分享文章。

```mermaid
graph TD
    A[RSS 订阅源] -->|1. 定期自动获取| B(Miniflux 阅读器)

    B -->|2. 新文章到达| H[触发 Telegram 机器人]
    H -->|3. 自动发布| G[(Telegram 频道)]
    
    B -->|4. 用户阅读并加星| C[文章加星]
    C -->|5. 同步集成| E[(Karakeep 书签)]

```
