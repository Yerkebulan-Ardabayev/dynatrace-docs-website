---
title: Order-of-magnitude notation
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/dynatrace-ui/order-of-magnitude-notation
scraped: 2026-05-12T11:13:09.477379
---

# Order-of-magnitude notation

# Order-of-magnitude notation

* Explanation
* 2-min read
* Published Dec 19, 2025

Dynatrace displays metric values using order-of-magnitude notation derived from the [International System of Units (SI)ï»¿](https://dt-url.net/os03419).

## Notation

Examples of order-of-magnitude notation in Dynatrace:

| Notation | Factor | Meaning |
| --- | --- | --- |
| k | 10^3 | kilo, thousand |
| M | 10^6 | mega, million |
| G | 10^9 | giga, billion |
| T | 10^12 | tera, trillion |

## Examples

### Metrics browser

In this example from the [Metrics browser](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), you can see values displayed in millions. This is order-of-magnitude notation (`7.5M` means "about 7.5 million" and not "exactly 7.5 million").

The order of magnitude here is selected automatically based on the size of the values. For example, the same metric measured over a shorter timeframe might be displayed in `k` values instead of `M`.

![Example order-of-magnitude values in the metrics browser.](https://dt-cdn.net/images/magnitude-metrics-browser-1284-02225955bf.png)

Example order-of-magnitude values in the metrics browser.

### Data Explorer and dashboard tiles

In [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), you can allow Dynatrace to automatically select an order of magnitude as it does in the **Metrics browser**, but Data Explorer also lets you specify an order of magnitude that overrides the automatic selection: set **Unit** to display a selected metric's values in a specific order of magnitude.

![Data Explorer Unit setting](https://dt-cdn.net/images/explorer-set-unit-296-7dfcc5b953.png)

Data Explorer Unit setting

The three tiles below are identical except that **Unit** was set to different values when configuring them in Data Explorer. From left to right:

* **Auto**âwith **Unit** set to `Auto` for the first tile, Dynatrace automatically selects an appropriate order of magnitude for values: `1.32M` (approximately 1.32 million), `428k` (approximately 428 thousand), etc.
* **k (thousand)**âwith **Unit** set to `k (thousand)` for the second tile, Dynatrace expresses each value in thousands.
* **M (million)**âwith **Unit** set to `M (million)` for the third tile, Dynatrace expresses each value in millions.

![Tiles with different Unit settings](https://dt-cdn.net/images/dashboard-tiles-unit-examples-1006-61e950f821.png)

Tiles with different Unit settings

In **Advanced mode**, you can use `:setUnit(<unit>)` to select from a wider range of units.

In addition, you can use the **Format** setting to specify the number of decimal places to display: `0`, `0.0`, `0.00`, `0.000`.