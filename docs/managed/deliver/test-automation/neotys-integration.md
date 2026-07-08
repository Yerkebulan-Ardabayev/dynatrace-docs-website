---
title: NeoLoad
source: https://docs.dynatrace.com/managed/deliver/test-automation/neotys-integration
---

# NeoLoad

# NeoLoad

* Published Feb 08, 2022

NeoLoad is an automated performance testing platform helping enterprise organizations to implement continuous testing and end to end testing. NeoLoad has a bi-directional integration with Dynatrace to precisely analyze how the whole application and its ecosystem is behaving under load. If you're both a Dynatrace and NeoLoad user, you will have get the KPIs to analyze and make automated decisions. NeoLoad supports the full range of mobile, web, and packaged applications.

At the end of each NeoLoad test, a Dynatrace event is created for each monitored service. NeoLoad also sends the global statistics of the test to Dynatrace so that they can be used as custom metrics in Dynatrace dashboards.

## Dynatrace prerequisites

Before you set the integration on the NeoLoad side, make sure you meet the following prerequisites on the Dynatrace side.

### API token

NeoLoad integration requires a [Dynatrace API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the following permissions:

| API v1 | API v2 |
| --- | --- |
| **Access problem and event feed, metrics and topology** | **Read metrics** |
| **Capture Request Data** | **Read entities** |
| **Read configuration** | **Write entities** |
| **Write configuration** |  |
| **Data ingest** |  |

### Tagging

Each service you want to retrieve the NeoLoad data on needs to be [tagged](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically."). You will add respective tags when setting up integration on the NeoLoad side.

## Set up NeoLoad

See [Enable the integration of Dynatrace﻿](https://documentation.tricentis.com/neoload/9.0/en/WebHelp/#5896_1.htm) in NeoLoad docs for detailed instructions on how to set the integration up in NeoLoad.

## Analyze results in Dynatrace

The traffic created by NeoLoad is identified by NeoLoad-added `X-Dynatrace-Test` header, so that you can easily isolate the traffic coming from NeoLoad. You can search for NeoLoad metrics in [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") by filtering for `custom:neoload`.

## Related topics

* [Dynatrace and load testing tools integration](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Capture request attributes based on web request data](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.")
* [Filter monitoring data via request attributes](/managed/observe/application-observability/services/request-attributes/filter-monitoring-data-via-request-attributes "Use request attributes to filter your monitoring data and narrow down service analysis scope.")