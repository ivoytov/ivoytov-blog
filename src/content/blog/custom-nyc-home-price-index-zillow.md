---
title: "Custom NYC Home Price Index: A Flexible Alternative to Zillow"
description: "A transparent repeat-sales model for anyone who needs NYC housing signals they can audit."
pubDate: "Jun 03 2025"
heroImage: "/NYCHome.jpg"
---

Zillow's dashboards are fine if you only need a headline number. I wanted something I could interrogate, remix, and extend, so I published my own repeat-sales toolkit for New York City. You can explore the live chart at [ivoytov.github.io/manhattan](https://ivoytov.github.io/manhattan/) and read the code at [github.com/ivoytov/manhattan](https://github.com/ivoytov/manhattan/blob/master/repeat_sales_index.jl).

## What the Code Does

1. **Ingests & cleans** two decades of NYC sales data, standardizing columns and filtering impossible prices or obvious duplicates.  
2. **Builds unique IDs** for each property (block/lot/apartment) so repeat transactions line up across time.  
3. **Flags outliers** using log price deltas adjusted for the time between sales.  
4. **Runs a repeat-sales regression** with time based weights to estimate period over period price moves.  
5. **Slices the index** by borough, neighborhood, property type, and price tier so you can zoom into the segments you actually trade.

## How It Differs From Zillow's ZHVI

- Data comes straight from NYC public records, not a black box AVM.  
- Methodology is a transparent repeat-sales regression, similar to Case-Shiller.  
- Segmentation is unlimited — if you can define the cohort, you can model it.  
- Every transformation is auditable, so you can rerun the exact pipeline later.

## Why It's More Customizable

- Adjust filters (price bands, property buckets, time windows) with a quick edit.  
- Swap in your own residual weighting or regression approach.  
- Change the reporting cadence to weekly, monthly, or custom periods.  
- Fork it for your favorite borough or roll it forward as new deeds drop.

## Use Cases

- Policy analysis across boroughs or income bands.  
- Hyper local investor updates for clients or LPs.  
- Academic housing studies that require reproducible methods.  
- Automated reporting in research decks or newsletters.

## Grab the Code

Everything lives in a single Julia project. Clone it, tweak the thresholds, and send a PR if you find a smarter way to normalize the data. I am always up for ideas on segmentation, visualization, or alternative weighting schemes.
