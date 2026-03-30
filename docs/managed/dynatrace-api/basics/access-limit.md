---
title: "Dynatrace API - Access limit"
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/access-limit
updated: 2026-02-09
---

Read access to the Dynatrace API is free of charge on a fair use model. You're charged for defining and pushing new custom metrics through the Dynatrace API on a per-metric, per-month basis.

For detailed information about custom metric ingestion and how this affects your consumption of Dynatrace monitoring, see the relevant page for your license model.

* Dynatrace Platform Subscription: Unavailable in Dynatrace Managed
* Dynatrace classic license: DDUs for metrics

## Payload limit

The payload size is limited to 1 MB. Exceptions are:

* Configuration API Mobile Symbolication APIâyou can upload a symbol file of up to 100 MiB compressed; the uncompressed file must not exceed 500 MiB.
* Configuration API Extensions APIâyou can upload extension ZIP files up to 50 MB.
* Configuration API Plugins APIâyou can upload plugin ZIP files up to 50 MB.
* Log Ingestion API Log Monitoring APIâthe maximum payload size of a single request is 10 MB.
* OpenTelemetry trace ingest API Ingestion API into Dynatrace.")âthe maximum payload size of a single request is 8 MB.
* OpenTelemetry metrics ingest API Ingestion API into Dynatrace.")âthe maximum payload size of a single request is 4 MB.
* OpenTelemetry logs ingest API Ingestion API into Dynatrace.")âthe maximum payload size of a single request is 2 MB.

## Request throttling

Every environment has a limited thread pool (with a queue) for request processing. You reach the limit when both thread pool and its queue are full or the request times out in the queue (timeout is 10 seconds). When you reach the limit, your requests return the response code 429.

This approach enables you to execute a high number of cheap requests without hitting the limit, and it protects your environment from being overloaded by many expensive requests.
