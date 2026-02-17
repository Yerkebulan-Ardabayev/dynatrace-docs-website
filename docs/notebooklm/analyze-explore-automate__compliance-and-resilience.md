# Dynatrace Documentation: analyze-explore-automate/compliance-and-resilience

Generated: 2026-02-17

Files combined: 1

---


## Source: compliance-assistant.md


---
title: Compliance Assistant
source: https://www.dynatrace.com/docs/analyze-explore-automate/compliance-and-resilience/compliance-assistant
scraped: 2026-02-17T04:58:18.366546
---

# Compliance Assistant

# Compliance Assistant

* Latest Dynatrace
* App
* 3-min read
* Updated on Jan 28, 2026
* Preview

About the app

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** collects information from various sources and applications to maintain real-time visibility into the status of compliance across critical applications and systems.

It leverages the Dynatrace platform's observability, security, and other capabilities, enhanced by Dynatrace Intelligence, to bolster its operational resilience and security posture.

Prerequisites

## Set up sources and applications

* To take full advantage of ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, see [Prerequisites](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management#prereq "Configure and enable Security Posture Management in Kubernetes.") and how to [Get started](/docs/secure/xspm#start "Detect, manage, and take action on security and compliance findings.").
* Set up [Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Set up [Dynatrace Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
* [Install](/docs/manage/hub#install "See the information about Dynatrace Hub.") ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** supports you in achieving and managing compliance with regulations and certifications out-of-the-box, starting with [DORA (Digital Operational Resilience Act)](#dora).

![Compliance Assistant overview](https://dt-cdn.net/hub/Compliance_Assistant_Preview_qb0fIUx.png)

1 of 1

## Navigate Compliance Assistant

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** provides the following interactions:

* Open reporting template
  Select  **ICT incident reporting notebook** in the upper-right corner of the page to access an incident reporting template in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

  Note that this is a [ready-made document](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Use ready-made documents right out of the box.").
* Open DORA regulation

  Within each widget, you can find a chapter from DORA regulation to which it refers.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Explore in Dynatrace Hub

Manage compliance with automated checks and incident handling out-of-the-box.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/compliance-assistant/?query=compl&filter=all)

To help achieve a strong DORA compliance posture, Dynatrace:

* Consolidates data from across the Dynatrace security and observability platform to create a comprehensive compliance overview in line with Chapters of DORA.
* Maintains real-time visibility into compliance status across monitored systems.
* Supports reporting of incidents as required by DORA.

## DORA compliance

DORA is an EU regulation that enhances the digital operational resilience of the financial sector. It strives to ensure financial entities can withstand and recover from severe operational disruptions, including cyber-attacks.

## ICT configuration compliance

ICT configuration compliance widget gathers information from **Runecast** and **Security Posture Management** to continuously scan configurations and get an overview of how they meet DORA requirements.

## ICT vulnerabilities

ICT vulnerabilities gathers information from ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** (with `Risk level` filter applied).

## Incidents ICT critical services

Incidents ICT critical services widget gathers information from:

* **Attacks** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks")âif there's a security incident, helps detect and classify an attack on your environment in real time.
* **Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new")âif there's a resilience incident, analyzes abnormal system behavior and performance problems detected by Dynatrace Intelligence.
* Use [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") to conveniently filter observability and security incidents impacting a critical service under DORA.

**ICT vulnerabilities** widget shows you most recent resilience and security incidents, but you can view all ICT Observability in **Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") and view all ICT Security incidents in **Attacks** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks").

## ICT Monitoring Coverage

ICT Monitoring Coverage widget gather information from:

* ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**âprevents unexpected outages by detecting and remediating monitoring coverage gaps.

## Use cases

Compliance Assistant enables you to easily achieve and manage your DORA compliance:

* Maintain real-time visibility into the status of DORA compliance across critical applications and systems.
* Consolidate insights from across the Dynatrace platform streamlined to specific regulatory requirements displayed in a tailored view.
* Identify critical incidents and support your team with timely and accurate reporting per DORA requirements.
* Automate reporting by providing automated workflows and templates as prescribed by regulators.


---
