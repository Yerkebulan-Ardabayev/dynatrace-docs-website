---
title: Service detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/detection-rules
scraped: 2026-02-25T21:25:33.630403
---

# Service detection API

# Service detection API

* Reference
* Published Jun 19, 2019

The **Rule-based service detection** API enables you to manage the configuration of service detection rules.

### List all

Get an overview of all service detection rules for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-all "View all service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-all "View all service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-all "View all service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-all "View all service detection rules for external and opaque web services via the Dynatrace API.")

### View a rule

Get parameters of a service detection rule for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/get-a-rule "View a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/get-a-rule "View a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/get-a-rule "View a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/get-rule "View a service detection rule for external and opaque web services via the Dynatrace API.")

### Reorder rules

Service detection rules are evaluated one after another. The first matching rule is applied and further processing stops. Reorder service detection rules to achieve the order of evaluation you need.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/reorder-rules "Reorder service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/reorder-rules "Reorder service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/reorder-rules "Reorder service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/reorder-rules "Reorder service detection rules for external and opaque web services via the Dynatrace API.")

### Create a rule

Create a new service detection rule for:

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/post-a-rule "Create a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/post-a-rule "Create a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/post-a-rule "Create a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/post-rule "Create a service detection rule for external and opaque web services via the Dynatrace API.")

### Edit a rule

Update an existing service detection rule or create a new rule with the specified ID.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/put-a-rule "Edit a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/put-a-rule "Edit a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/put-a-rule "Edit a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/put-rule "Edit a service detection rule for external and opaque web services via the Dynatrace API.")

### Delete a rule

Delete a service detection rule you don't need anymore.

* [Full web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-request/del-a-rule "Delete a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-request/del-a-rule "Delete a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/full-web-service/del-a-rule "Delete a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](/docs/dynatrace-api/configuration-api/service-api/detection-rules/opaque-web-service/delete-rule "Delete a service detection rule for external and opaque web services via the Dynatrace API.")

## Related topics

* [Service Detection v1](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")