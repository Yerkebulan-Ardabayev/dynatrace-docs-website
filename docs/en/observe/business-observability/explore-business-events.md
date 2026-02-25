---
title: Explore Business Events
source: https://www.dynatrace.com/docs/observe/business-observability/explore-business-events
scraped: 2026-02-25T21:18:07.603639
---

# Explore Business Events

# Explore Business Events

* Latest Dynatrace
* App
* 2-min read
* Published Apr 25, 2023

About the app

![Explore Business Events](https://dt-cdn.net/images/biz-events-512-68c4be09db.png "Explore Business Events") **Explore Business Events** is a central repository of resources related to business events, including blog posts, documentation, direct product links and other applications relevant to business analysis, such as [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."). It was designed to:

* Take you through the Dynatrace business analysis process end-to-end, starting from business event capture, through processing, and analyzing, to displaying final results on dashboards.
* Help you understand business analytics use cases and address your specific use case.

Prerequisites

### Permissions

The following table describes the required permissions.

storage:bizevents:read

Is required to read bizevents from Grail

storage:buckets:read

Is required to read system data from Grail

settings:objects:read

Is required to read OneAgent rules

settings:objects:write

Is required to write OneAgent rules

settings:schemas:read

Is required to read OneAgent rules schema

app-settings:objects:read

Is required to read configurations in app settings

storage:filter-segments:read

Read filter segments

storage:events:write

Required for workflow action

state:app-states:read

Is required to read app states

state:app-states:write

Is required to write app states

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

![Explore business events](https://dt-cdn.net/hub/Explore_business_events_2.png)

1 of 1Explore business events

## Process flow

The Business event process in Dynatrace consists of three main steps: Capture and Process, Analyze, and Create Dashboards. To see a use case covering all steps, go to [Business events use case](/docs/observe/business-observability/end-to-end-example "How to capture and process business events.").

### Capture and process

Displays all links relevant to business event capture and processing. To see a real-life scenario for capturing and processing business event data, go to [the capture section of the end-to-end use case](/docs/observe/business-observability/end-to-end-example#create-a-capture-rule "How to capture and process business events.").

### Analyze

Provides you with links to two places where you can run your DQL queries: Notebooks and the **Logs and event viewer**.

* To see examples of simple and advanced DQL queries for business analysis, go to [Analysis and examples](/docs/observe/business-observability/bo-analysis "Analyze and present business event data.").
* To see the analysis performed as part of the use case, go to [Use case analysis part](/docs/observe/business-observability/end-to-end-example#analyze-your-data-with-dql "How to capture and process business events.").

### Visualize

Provides you with links to places where dashboards can be created. To see an example dashboard created as part of the use case, go to [the end-to-end use case](/docs/observe/business-observability/end-to-end-example#display-your-results "How to capture and process business events.").

## Dynatrace resources for business events

* Blog posts supplement the documentation with real-life examples, use cases and how-to guides.
* Dynatrace live chat and the Dynatrace Community are interactive platforms that provide answers to your questions in real time and offer collaboration possibilities.
* Direct product links save your time and help you arrive exactly in the place a certain process step takes place, for example at the **Capture business events with OneAgent** product page.
* [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") is used to query and analyze your business events, in [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."), and the **Logs and event viewer**.
* Custom dashboards transform complex data from your queries into easy-to-follow visualizations.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Understand the Dynatrace business analysis process end-to-end.](https://www.dynatrace.com/hub/detail/explore-business-events/?internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [View a blog post on business analytics.ï»¿](https://www.dynatrace.com/news/blog/dynatrace-enhances-business-observability/)
* [View the Dynatrace website devoted to business analytics.ï»¿](https://www.dynatrace.com/platform/business-observability/)
* [View the Dynatrace Query Language hub](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")