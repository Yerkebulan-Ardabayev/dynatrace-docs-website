---
title: Billing report
source: https://www.dynatrace.com/docs/license/billing-reports
scraped: 2026-02-18T05:39:11.888661
---

# Billing report

# Billing report

* Latest Dynatrace
* Explanation
* 1-min read
* Published Nov 15, 2023

Your DPS Billing report gives you all the details of your DPS budget state for each day of the current period. It shows which costs were booked on which day with regards to their booking date. There is a difference between the consumption date and the booking date: consumption always occurs when Dynatrace capabilities are used. Booking occurs when consumption is recognized and deducted from your DPS annual commitment. Therefore, the booking date can differ from the consumption date.

To access the billing report in the Dynatrace web UI, go to **Subscription** > **Billing report**.

![DPS billing reports](https://dt-cdn.net/images/billingreport-1913-1256f12b00.png)

The Billing report consists of the following charts:

1. **Booked costs to date:** This chart displays the accumulated costs per booking day. It also shows the annual minimum commitment of your subscription.
2. **Booked costs per day:** This chart shows the costs booked for each individual day. It does not contain the accumulated budget state. This chart helps you identify variations in daily costs.

The API for the Dynatrace Platform Subscription allows access to the underlying data of this view. Please read the API documentation for further details.

## Related topics

* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")