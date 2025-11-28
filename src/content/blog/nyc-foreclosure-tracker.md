---
title: "NYC Foreclosure Tracker"
description: "forqloz compresses hours of foreclosure auction research into a single weekly digest."
pubDate: "Jun 19 2025"
heroImage: "/nyc.png"
---

I get asked all the time how I stay on top of New York City foreclosure auctions. The honest answer used to be: lots of spreadsheets, half broken county sites, and way too much time. I built [forqloz](https://ivoytov.github.io/forqloz) so I could stop hunting and start evaluating deals.

## Why I Built It

- Public notices are scattered across borough specific PDFs and email lists. 
- Data is rarely normalized, so matching properties over time is tedious.
- Investors want to scan both past and upcoming auctions to size trends, not click through dozens of tabs.

## What forqloz Delivers

- A clean, filterable map of past and scheduled auctions, refreshed every week.
- Exportable tables (CSV/JSON) so you can blend the feed with your own underwriting model.
- Quick links back to the underlying notices plus my own annotations on quirks I am tracking.

![Map preview from the tool](/nyc.png)

The project is free, open, and intentionally lightweight so you can hack on top of it. Try it, send feedback, or fork it if you want a version tuned to your workflow.
