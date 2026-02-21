---
title: Data centers
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/infrastructure-and-operations/data-centers
scraped: 2026-02-21T21:10:27.075950
---

# Data centers

# Data centers

* Latest Dynatrace
* Explanation
* 2-min read
* Published Nov 26, 2025

The  **Data centers** view in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** monitors the health and performance of your data centers and availability zones.

Select a data center to view all monitored hosts within it.

## Overview

Here's what each column in the  **Data centers** view stands for.

* **Data center**: The name or identifier of the data center or availability zone.
* **Type**: The type of data center, such as:

  + AWS Availability Zone
  + GCP zone
  + Azure Region
  + Geo Location Site
* **Hosts**:

  + **Total**: The total number of hosts in the data center.
  + **Unhealthy**: The number of hosts experiencing issues. Critical hosts are marked with red emphasis.
  + **Monitored**: The percentage of hosts actively monitored within the data center. Lower than 100% means Dynatrace identified unmonitored instances based on host connections.
* **Location**: The geographic name of the data center location.

## Use cases

* Identify critical issues

  Check the **Unhealthy** column and apply the Critical alert filter to quickly find data centers with problems. Selecting the alert indicator will take you to a filtered host list, focusing on the affected systems.
* Monitor coverage

  Review the **Monitored** column to ensure comprehensive tracking of all hosts. If you notice gaps in monitoring, you can use ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** to extend your oversight and achieve full coverage.