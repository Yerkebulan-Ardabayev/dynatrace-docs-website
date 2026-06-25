---
title: Configure minimum time between requests
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/api-request-threshold
scraped: 2026-05-12T12:09:33.527764
---

# Configure minimum time between requests

# Configure minimum time between requests

* 1-min read
* Published Jul 28, 2023

Dynatrace Operator version 1.2.0+

In Dynatrace Operator version 0.11.0 until 1.2.0, this configuration was set using the annotation feature.dynatrace.com/dynatrace-api-request-threshold.

Dynatrace Operator makes regular calls to Dynatrace to gather the information necessary to function properly.

The minimum time between requests from the Dynatrace Operator, which was previously hard coded to 15 minutes to reduce network load, can now be configured.

To set this time (in minutes), set the field `dynatraceApiRequestThreshold`.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



dynatraceApiRequestThreshold: 15



...
```

The Operator makes three different types of requests for:

* ActiveGate connection details
* OneAgent connection details
* Token scope verification

The specified interval is counted independently for each of these request types.