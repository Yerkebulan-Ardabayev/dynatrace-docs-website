---
title: Kubernetes credentials API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api
---

# Kubernetes credentials API

# Kubernetes credentials API

* Reference
* Published Jun 27, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes`) and the [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`) schemas instead.

[### List all credentials

Get an overview of all Kubernetes credentials stored in your environment.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-all "View all Kubernetes credentials of your monitoring environment via the Dynatrace API.")[### View credentials

Get the configuration of credentials by configuration ID.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-credentials "View a Kubernetes credentials configuration via the Dynatrace API.")

[### Create credentials

Create a new credentials configuration with the exact parameters you need.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/post-new-credentials "Create a Kubernetes credentials configuration via the Dynatrace API.")[### Edit credentials

Update an existing configuration of Kubernetes credentials. You can also create new credentials with the specified ID.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/put-credentials "Update a Kubernetes credentials configuration via the Dynatrace API.")[### Delete credentials

Delete credentials configuration you no longer need.](/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/delete-credentials "Delete a Kubernetes credentials configuration via the Dynatrace API.")

## Related topics

* [Explore Kubernetes in Dynatrace Hub﻿](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)