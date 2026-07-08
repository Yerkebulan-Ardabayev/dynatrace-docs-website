---
title: Application Security monitoring (ASUs)
source: https://docs.dynatrace.com/managed/license/classic-licensing/application-security-units
---

# Application Security monitoring (ASUs)

# Application Security monitoring (ASUs)

* 6-min read
* Published Nov 30, 2021

## Application Security

[Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.") helps you to visualize, analyze, and monitor security vulnerabilities in your environment that are related to third-party libraries at runtime.

### Application Security units

Dynatrace Application Security is licensed based on the consumption of Application Security units (ASUs). The number of Application Security units that an environment consumes is based on the servers that run applications, which are monitored with Application Security.

There are multiple factors that influence the consumption of ASUs:

* The amount of RAM that a monitored server has (see the weighting table below)
* The number of hours that the server runs
* The Application Security capabilities that are enabled on the server

### Application Security capabilities

Currently, Application Security provides two capabilities:

* Runtime Vulnerability Analytics
* Runtime Application Protection

### How capabilities affect monitoring consumption

Each capability consumes 1 ASU per hour multiplied by the RAM weight (See the weighting table for details).

Runtime Application Protection (RAP) relies on Runtime Vulnerability Assessment (RVA) to evaluate the vulnerability that an attack is based on. Therefore, a server with Runtime Application Protection enabled always consumes ASUs for both RVA and RAP.

| Host size(based on RAM GiB) | Runtime Vulnerability Analytics(Application Security units per hour) | Runtime Vulnerability Analytics & Runtime Application Protection(Application Security units per hour) |
| --- | --- | --- |
| 1.6 GiB | 0.10 | 0.20 |
| 4 GiB | 0.25 | 0.50 |
| 8 GiB | 0.50 | 1 |
| 16 GiB | 1 | 2 |
| 32 GiB | 2 | 4 |
| 48 GiB | 3 | 6 |
| 64 GiB | 4 | 8 |
| 80 GiB | 5 | 10 |
| N × 16 | N | N × 2 |

#### Example

Say that an environment consists of

* 1 server with 32 GiB RAM running RVA and RAP
* 1 server with 32 GiB RAM running RVA
* 1 server with 4 GiB RAM running RVA
* 1 server with 32 GiB RAM to handle load spikes running RVA and RAP

If the first three servers in the list run 24x7, they will consume 54,750 Application Security units per year. When the environment is no longer able to handle the load, an additional server with 32 GiB RAM running RVA and RAP spins up to handle the spikes. This server runs a total of 250 hours during the year, so the consumption is increased by 1,000 ASUs.

This is calculated based on the following:

* One of the 32 GiB RAM servers is running RVA and RAP and consumes 35,040 ASUs per year.  
  `4 ASUs for RVA and RAP for a 32 GiB host × 24 (hours) × 365 (days)`
* The other 32 GiB RAM server is running only RVA and consumes 17,520 ASUs per year.  
  `2 ASUs for RVA for a 32 GiB host × 24 (hours) × 365 (days)`
* The 4 GiB RAM server runs only RVA and consumes 2,190 ASUs per year.  
  `0.25 ASUs for RVA for a 4 GiB host × 24 (hours) × 365 (days)`
* When the environment is no longer able to handle the load, an additional server with 32 GiB RAM running RVA and RAP spins up to handle the spikes, but it only runs a total of 250 hours during the year. So, the consumption is increased by 1,000 ASUs.  
  `4 ASUs for RVA and RAP for a 32 GiB host × 250 (hours)`

### Combine Application Security monitoring with Full-Stack and Infrastructure Monitoring

Application Security units are consumed concurrently with host units for both Full-Stack and Infrastructure Monitoring. For example, you can monitor the security of a host that runs on a Tomcat server that's monitored with Dynatrace Infrastructure Monitoring only, rather than Full-Stack Monitoring. This approach provides you with Dynatrace Application Security insights, but you won't benefit from improved prioritization based on your topology or the deeper performance insights that are provided with Full-Stack Monitoring mode.

The allocation of Application Security units is only applicable to hosts that run supported technologies. Contact a Dynatrace product expert via live chat to learn more.

## Runecast Security Posture Management (SPM)

The licenses listed here are unrelated to the Application Security Monitoring ASUs; there is no prerequisite of licensing Application Security Monitoring ASUs to consume Security Posture Mangement (SPM). For details on DPS SPM pricing, see [Application Security (DPS)](/managed/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

Runecast® Security Posture Management (SPM) provides continuous monitoring and automated assessment for VMware® and cloud environments. With insights into configuration, compliance issues, and exposure risk assessment, customers can maintain a strong security posture.

### Runecast Security Posture Management (SPM) capabilities

Runecast Security Posture Management (SPM) provides the following capabilities:

* VMware SPM (VSPM)
* Cloud SPM (CSPM)

### Runecast Security Posture Management (SPM) units of measure

Runecast Security Posture Management (SPM) is licensed based on SKUs. The number of SKUs that an environment consumes is based on the following units of measure:

* The unit of measure for VSPM is CPU sockets per year (CPU sockets of the licensed VMware® ESXi hosts), regardless of the number of cores or VMs.
* The unit of measure for CSPM is hosts per year, where a host in the CSPM context applies for compute, database, and function resources. You can enable CSPM on the cloud on a per-account basis.

The licenses are structured as concurrent annual units. Unused licenses don't roll over to subsequent periods. To extend your licensed CPU sockets and/or hosts, you need to purchase additional licenses.

#### VSPM calculation example

Suppose you purchase a license for 20 CPU sockets, starting on January 1st. VSPM checks are initiated and run continuously. After six months, you add 10 more CPU sockets to your environment and purchase an additional license for these new sockets, with a start date of July 1st.

The initial license for 20 CPU sockets expires 12 months after the initial purchase, on December 31st of the same year.

* The 20 CPU sockets have become unlicensed and cannot be checked until renewed.
* The second license continues to cover the remaining 10 CPU sockets until its expiration on June 30th of the following year.

#### CSPM calculation example

Suppose you purchase a subscription for 20 AWS billable assets (EC2 instances and Lambda functions), starting on January 1. CSPM checks are initiated and run continuously.
After six months, you decide to add 10 more hosts to your environment and purchase an additional license for these new hosts, with a start date of July 1.
In this case, you would need to apply a new license for 30 billable assets, replacing your current subscription.

The license for the original 20 hosts expires 12 months after the initial purchase, on December 31st.

* The 20 hosts have become unlicensed and cannot be checked until renewed.
* The second license continues to cover the remaining 10 hosts until its expiration on June 30th of the following year.

![cspm](https://dt-cdn.net/images/20250417-112010-1102-2d970d5643.png)

cspm

### View your license

You can view details about your current, expired, and upcoming licenses on the [licensing portal﻿](https://dt-url.net/bj03ua2) (after logging in to your profile, you can see your licenses on the left).

![view your licenses](https://dt-cdn.net/images/20250417-112053-1648-8c741dda54.png)

view your licenses

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)
* [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")