---
title: "Agent Next Steps"
description: "Ideas of what to do with your agent"
date: "May 10 2026"
---

Since setting up my [Nanobot agent](nanobot-setup.md) I've been giving it increasingly more complex tasks and ran into a few limitations. Here are the problems and solutions I've discovered.

## Email as a Channel != Email as a Tool

It was very easy to connect Nanobot to its own `agent@ai.voytov.com` email account, but I quickly realized that it treats incoming emails as instructions (prompts) that require an immediate response - over email. What I wanted to do was to sign up the bot for a bunch of museum email newsletters, and for the bot to summarize new interesting events to me on Telegram. So totally different paradigm. I modified the default email channel to ignore any emails other than from me, and then created a [simple IMAP MCP server](https://github.com/ivoytov/imap-mcp) that allows it send/read its own emails and then summarize them to me at a pre-scheduled time.

## Web Search Sucks

By default, Nanobot comes configured with DuckDuckGo, and the results from searches leave a lot to be desired. I've been a paying customer of [Kagi Search](kagi.com) and I found they have an unpublished alpha of API search. I emailed support and quickly got enabled for the alpha, and it's been much better results.

## Web Browsing Sucks

I work at Rockefeller Center, and the landlord has a website portal where they post events and announcements. I wanted my agent to login to this portal and summarize anything interesting or relevant to me, like changes in bike room policies. This webpage was heavy on JavaScript, and the built-in web fetch tool or even `curl` was not going to cut it. So I added this section to my Docker compose file:

```
browserless:
    image: ghcr.io/browserless/chromium:latest
    restart: unless-stopped
    # We do NOT map ports to the host (e.g., no "3000:3000").
    # This keeps Browserless completely hidden from the public internet.
    # It is only accessible to 'nanobot-gateway' via the internal Docker network.
    environment:
      - TOKEN=<YOUR_TOKEN> # Prevents unauthorized access
      - MAX_CONCURRENT_SESSIONS=5 # Adjust based on your Hetzner VPS RAM (assume ~500MB per session)
      - MAX_QUEUE_LENGTH=10
      - CONNECTION_TIMEOUT=60000 # 60 seconds
    deploy:
      resources:
        limits:
          memory: 2G # IMPORTANT: Put a hard cap so Chrome doesn't crash your whole VPS
```

Now your agent can write Puppeteer/Playwright scripts that use this headless browser located at `ws://browserless:3000/?token=<YOUR_TOKEN>` to interact with the web, login to websites, and even do things for you. 

For security purposes, I only let the agent access websites that I don't care about. I pass in credentials to the agent using an environment variable, and I tell it to never store the credentials in git - yes, you should tell it to use a git repo for its scripts - but ultimately you have to assume that a nefarious actor could get it to reveal them.

## Access Unpublished HTTP APIs

There are some sites that hate bots. One of them is [surfline.com](surfline.com). So instead of fighting it, I created a quick and dirty [surfline MCP](https://github.com/ivoytov/surfline-mcp) that uses their unpublished HTTP API to get surf forecasts for the Rockaways in NYC. Then you can plug this MCP into your agent, and it can directly fetch the wave forecast without any trouble.