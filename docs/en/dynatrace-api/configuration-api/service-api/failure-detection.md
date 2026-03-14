---
title: Failure detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/failure-detection
scraped: 2026-03-05T21:31:58.735333
---

# Failure detection API


* Reference
* Published Jan 11, 2021

[### List all parameter sets

Get an overview of all parameter sets for failure detection rules.](failure-detection/parameter-set/get-all.md "View all failure detection parameter sets of your monitoring environment via the Dynatrace API.")[### View a parameter set

View the configuration of all parameter sets for failure detection rules.](failure-detection/parameter-set/get-parameter-set.md "View a failure detection parameter set via the Dynatrace API.")

[### Create a parameter set

Create a new parameter set for failure detection rules.](failure-detection/parameter-set/post-parameter-set.md "Create a failure detection parameter set via the Dynatrace API.")

### Edit a parameter set

* [Update an existing parameter set](failure-detection/parameter-set/put-parameter-set.md "Edit a failure detection parameter set via the Dynatrace API.") for failure detection rules.
* [Change the ID](failure-detection/parameter-set/change-id.md "Change the ID of a failure detection parameter set via the Dynatrace API.") of a parameter set.

[### Delete a parameter set

Delete a parameter set for failure detection rules.](failure-detection/parameter-set/delete-parameter-set.md "Delete a failure detection parameter set via the Dynatrace API.")

[### List all rules

Get an overview of all failure detection rules.](failure-detection/detection-rules/get-all.md "View all failure detection rules of your monitoring environment via the Dynatrace API.")[### View a rule

View the configuration of a failure detection rule.](failure-detection/detection-rules/get-rule.md "View a failure detection rule via the Dynatrace API.")[### Reorder rules

Failure detection rules are evaluated one after another. The first matching rule is applied, and further processing stops.

Reorder the rules to achieve the order of evaluation you need.](failure-detection/detection-rules/reorder-rules.md "Change the order of failure detection rules via the Dynatrace API.")[### Create a rule

Create a new failure detection rule.](failure-detection/detection-rules/post-rule.md "Create a failure detection rule via the Dynatrace API.")

### Edit a rule

* [Update an existing](failure-detection/detection-rules/put-rule.md "Edit a failure detection rule via the Dynatrace API.") failure detection rule.
* [Change the ID](failure-detection/detection-rules/change-id.md "Change the ID of a failure detection rule via the Dynatrace API.") of a rule.

[### Delete a rule

Delete a failure detection rule you don't need anymore.](failure-detection/detection-rules/delete-rule.md "Delete a failure detection rule via the Dynatrace API.")

## Related topics

* [Configure service failure detection](../../../observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection.md "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")