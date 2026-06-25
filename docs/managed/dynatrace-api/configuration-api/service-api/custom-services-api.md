---
title: Custom services API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api
scraped: 2026-05-12T11:04:39.391431
---

# Custom services API

# Custom services API

* Reference
* Published Oct 22, 2018

The **Custom services** API enables you to manage the custom service detection rules.

[### List all

Get an overview of all custom service rules.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/get-all "View all custom service rules of your environment via the Dynatrace API.")[### View a rule

Get parameters of a custom service rule by its ID.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/get-rule "View a custom service rule via the Dynatrace API.")[### Reorder rules

Custom service rules are evaluated one after another. The first matching rule is applied, and further processing stops.

Reorder custom service rules to achieve the order of evaluation you need.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/reorder-rules "Change the order of custom service rules via the Dynatrace API.")[### Create a rule

Create a new rule with the exact parameters you need.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/post-rule "Create a custom service rule via the Dynatrace API.")[### Edit a rule

Update an existing custom service rule or create a new rule with the specified ID.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/put-rule "Edit a custom service rule via the Dynatrace API.")[### Delete a rule

Delete a rule you don't need anymore.](/managed/dynatrace-api/configuration-api/service-api/custom-services-api/del-rule "Delete a custom service rule via the Dynatrace API.")

## Related topics

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.")