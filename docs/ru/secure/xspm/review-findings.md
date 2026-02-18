---
title: Review findings
source: https://www.dynatrace.com/docs/secure/xspm/review-findings
scraped: 2026-02-18T05:57:55.613260
---

# Review findings

# Review findings

* Latest Dynatrace
* How-to guide
* Updated on Oct 13, 2025

To efficiently manage and analyze security and compliance findings, you can [filter](#filter) and [sort](#sort) results to prioritize the most relevant findings.

## Filter

Select which information is to be displayed.

### Filter by standard

You have two options:

From Overview

From Assessment results

1. Go to the **Overview** page.
2. From the list of available compliance standard cards, select the one you're interested in. This will navigate you to the **Assessment results** page, filtered by the respective standard.

![filter by standard](https://dt-cdn.net/images/2024-11-10-11-32-31-1491-79379f31bf.png)

1. Go to the **Assessment results** page.
2. In the filter bar, select a **Standard** (short form) and/or a **Standard name** (full name of the standard) to focus your results.

![filter by standard](https://dt-cdn.net/images/2025-10-13-15-28-08-1920-94cd4524a0.png)

### Filter by system

You have two options:

From Overview

From Assessment results

1. Go to the **Overview** page.
2. In the **My systems** table, look for and select the system you're interested in. This will navigate you to the **Assessment results** page, filtered by the respective system.

![filter by system](https://dt-cdn.net/images/2024-11-10-12-06-27-860-9e7c4d01d1.png)

Only systems on which Security Posture Management is enabled can be selected.

1. Go to the **Assessment results** page.
2. In the **System** filter, select the system you're interested in.

   ![filter by system](https://dt-cdn.net/images/2025-10-13-15-34-33-1357-5c705ed4d4.png)

   Only systems on which Security Posture Management is enabled are displayed.
3. Select **Update** next to the systems filter bar to update results based on your selection.

### Filter by assessment view

On the **Assessment results** page, use the **Assessment view** filter to control the scope of displayed rules:

* **Complete results**: Displays all rules assessed for the selected systems, including those marked `Not relevant`.
* **Recommended**: Displays only the results which are relevant to your environment: `Failed`, `Manual`, or `Passed`.

![assessment view filter](https://dt-cdn.net/images/2025-10-13-14-37-49-1920-1a11441c0c.png)

### Filter by results, severity and rule

On the **Assessment results** page, filter for the options you're interested in:

* [Result](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Failed`, `Manual`, `Passed`, `Not relevant`)
* [Severity](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Critical`, `High`, `Medium`, `Low`)
* Rule (full or partial match of the rule name)

Filters can be combined.

![combined filters](https://dt-cdn.net/images/2025-10-13-15-38-12-1920-a0e9d073f1.png)

## Sort

On the **Overview** and the **Assessment results** pages, select any of the columns with a sorter symbol  to change the order of results to ascending or descending based on that criteria.

![sorting](https://dt-cdn.net/images/2024-11-10-11-16-35-579-3bd762be27.png)

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")