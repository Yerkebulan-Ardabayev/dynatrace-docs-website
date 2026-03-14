---
title: Service detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/detection-rules
scraped: 2026-03-06T21:22:36.788501
---

# Service detection API


* Reference
* Published Jun 19, 2019

The **Rule-based service detection** API enables you to manage the configuration of service detection rules.

### List all

Get an overview of all service detection rules for:

* [Full web requests](detection-rules/full-web-request/get-all.md "View all service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/get-all.md "View all service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/get-all.md "View all service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/get-all.md "View all service detection rules for external and opaque web services via the Dynatrace API.")

### View a rule

Get parameters of a service detection rule for:

* [Full web requests](detection-rules/full-web-request/get-a-rule.md "View a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/get-a-rule.md "View a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/get-a-rule.md "View a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/get-rule.md "View a service detection rule for external and opaque web services via the Dynatrace API.")

### Reorder rules

Service detection rules are evaluated one after another. The first matching rule is applied and further processing stops. Reorder service detection rules to achieve the order of evaluation you need.

* [Full web requests](detection-rules/full-web-request/reorder-rules.md "Reorder service detection rules for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/reorder-rules.md "Reorder service detection rules for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/reorder-rules.md "Reorder service detection rules for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/reorder-rules.md "Reorder service detection rules for external and opaque web services via the Dynatrace API.")

### Create a rule

Create a new service detection rule for:

* [Full web requests](detection-rules/full-web-request/post-a-rule.md "Create a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/post-a-rule.md "Create a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/post-a-rule.md "Create a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/post-rule.md "Create a service detection rule for external and opaque web services via the Dynatrace API.")

### Edit a rule

Update an existing service detection rule or create a new rule with the specified ID.

* [Full web requests](detection-rules/full-web-request/put-a-rule.md "Edit a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/put-a-rule.md "Edit a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/put-a-rule.md "Edit a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/put-rule.md "Edit a service detection rule for external and opaque web services via the Dynatrace API.")

### Delete a rule

Delete a service detection rule you don't need anymore.

* [Full web requests](detection-rules/full-web-request/del-a-rule.md "Delete a service detection rule for full web requests via the Dynatrace API.")
* [Opaque web requests](detection-rules/opaque-web-request/del-a-rule.md "Delete a service detection rule for opaque and external web requests via the Dynatrace API.")
* [Full web services](detection-rules/full-web-service/del-a-rule.md "Delete a service detection rule for full web services via the Dynatrace API.")
* [Opaque web services](detection-rules/opaque-web-service/delete-rule.md "Delete a service detection rule for external and opaque web services via the Dynatrace API.")

## Related topics

* [Service Detection v1](../../../observe/application-observability/services/service-detection/service-detection-v1.md "Find out how Dynatrace Service Detection v1 detects and names different types of services.")