---
title: Guardian execution context
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/execution-context
scraped: 2026-03-01T21:18:16.226869
---

# Guardian execution context

# Guardian execution context

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Sep 29, 2023

Your Continuous Integration (CI) tool, for example, Jenkins, can [send business events to Dynatrace](/docs/observe/business-observability/bo-api-ingest "Set up authentication for and ingest business events via API."). These events can then trigger Site Reliability Guardian validations in a workflow.

Disclaimer

The following steps use business events to integrate into a CI/CD pipeline and fetch validation results. This approach is valid for now, but we plan a new event kind for events occurring during the software development lifecycle of a software component. This new event kind will replace business events in the future.

If you want to filter the Site Reliability Guardian validation events based on the source trigger, the created business events must contain context information from the external tool. The context information can be carried by an externalId, a version number, a build number, or any parameter that lets you identify the tool.

## Context propagation

To propagate the execution context, the event triggering a workflow execution must contain the `execution_context` field, as in the example below.

```
{



"timeframe.to": "2023-03-08T06:29:08.809Z",



"timeframe.from": "2023-03-08T05:29:08.809Z",



"errors": "[]",



"status": "fail",



"event.id": "d08a70d8-f6de-4d0d-bd34-5d416a20ba6a",



"timestamp": 1678256963078000000,



"event.kind": "BIZ_EVENT",



"event.type": "guardian.validation.triggered",



"tag.stage": "hardening",



"tag.service": "carts",



"event.provider": "Jenkins",



"dt.system.bucket": "default_bizevents_short"



"execution_context": {



"buildId": "4711",



"version": "0.1.0"



}



}
```

The context execution is propagated to the guardian validation business event. The `guardian.validation.started`, `guardian.validation.finished`, and `guardian.validation.objective` events contain the propagated `execution_context` field.

## Query your guardian data using execution context

This DQL shows you the first `guardian.validation.objective` business event with a specific guardian ID and parses the execution context field to extract a specific value from the event JSON.

```
fetch bizevents |



filter event.type == "guardian.validation.objective" AND guardian.id == "vu9U3hXa3q0AAAABADFhcHA6ZHluYXRyYWNlLnNpdGUucmVsaWFiaWxpdHkuZ3VhcmRpYW46Z3VhcmRpYW5zAAZ0ZW5hbnQABnRlbmFudAAkMWNiZDVkYWYtZThhNi0zMDkxLWFkOGQtMmU5NDNmNWJmZWJmvu9U3hXa3q0" |



limit 1 |



parse execution_context, "JSON:parsed_execution_context"
```

This DQL shows you all `guardian.validation.finished` business events where the execution context is defined by `buildid` equal to `4711`.

```
fetch bizevents



| filter event.type == "guardian.validation.finished"



| parse execution_context, "JSON:parsed_execution_context"



| filter parsed_execution_context[buildId] == "4711"
```