---
title: Organize Cloud Foundry deployments by tags
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/organize-cf-deployments-by-tags
---

# Organize Cloud Foundry deployments by tags

# Organize Cloud Foundry deployments by tags

* How-to guide
* 3-min read
* Published Sep 21, 2017

Dynatrace provides the ability to define tags for CloudFoundry application process groups and services via any user-provided Dynatrace [Cloud Foundry service﻿](https://docs.run.pivotal.io/devguide/services/) that’s bound to your application. This enables you to automatically organize and filter all monitored Cloud Foundry application components.

## Recommendation

Defining tags in the environment itself has its uses. However, we don't recommend it as a general purpose solution. The reason is that this is cumbersome and requires a lot of preplanning. Making changes later isn't easy either. Use it with caution.

We recommend that you define additional metadata at the deployed system. For CloudFoundry apps this can also be done via a user-provided Dynatrace [Cloud Foundry service﻿](https://docs.run.pivotal.io/devguide/services/) that’s bound to your application.

This enables you to use [automated tagging rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and will apply almost immediately without any change to the monitored environment or applications.

## Define Cloud Foundry service tags for multiple applications

To define Dynatrace tags, you can leverage one or more Cloud Foundry service instances that have the name `dynatrace` as a substring. For example:

```
cf cups dynatrace-tags -p '{ "tag key": "tag value", "tag key": "tag value"}'
```

You’re prompted automatically to provide values for certain tags (for example, `tag:region>eu-central-1`). Dynatrace supports both Cloud Foundry labels and Cloud Foundry key-value tags. For example, the tag `tanzu` in the example above is used to label all applications running within a VMware Tanzu environment—so this tag doesn’t include a value. The key-value tag `region` in the example holds the region of the AWS account that was used to deploy the Cloud Foundry environment.

You can easily update your user-provided Cloud Foundry services with new values (for example, `tag:region>eu-west-2`) or additional tags:

```
cf uups dynatrace-tags -p "tag:tanzu, tag:region, tag:newtag"
```

To exploit the service instance `dynatrace-tags` above, you must bind the instance to your application (for example, `spring-music`):

```
cf bs spring-music dynatrace-tags
```

## Define tags for specific Cloud Foundry applications

Additionally, Dynatrace automatically detects tags that are provided to applications via [Cloud Foundry environment variables﻿](https://docs.pivotal.io/pivotalcf/1-12/devguide/deploy-apps/manifest.html#env-block). For instance, you can provide the environment variable `DT_TAGS` in the environment block of your application manifest but you can also set `DT_TAGS` using the `cf` command `set-env`:

```
---



applications:



- name: spring-music



memory: 1G



random-route: true



path: build/libs/spring-music.jar



services:



- dynatrace-service



env:



DT_TAGS: hotfix
```

```
cf set-env spring-music DT_TAGS "hotfix"
```

Both examples above attach the tag `hotfix` to all monitored processes that are related to the application `spring-music`.

## Leverage Cloud Foundry tags in your Dynatrace environment

Cloud Foundry tags are searchable via Dynatrace search. This allows you to easily find and inspect the monitoring results of related processes that are running in your Cloud Foundry environment.

Cloud Foundry tags also integrate seamlessly with Dynatrace filters. For example, you can easily filter technologies or problems using Cloud Foundry tags. You can also leverage Cloud Foundry tags when setting up fine-grained [problem alerting profiles](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").

## Limitations

Dynatrace buildpack integration for IBM WebSphere Liberty can currently only support a single service instance that uses the name `dynatrace` as a substring. However, you can easily provide tags when creating this single service instance for Dynatrace:

```
cf cups dynatrace-service -p "environmentid, apitoken, tag:tanzu, tag:region"
```

If you already have a service instance for Dynatrace in place you can update it with new values or additional tags:

```
cf uups dynatrace-service -p "environmentid, apitoken, tag:tanzu, tag:region, tag:newtag"
```

For further details on creating a user-provided service for Dynatrace see [How do I monitor Cloud Foundry applications?](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

The Dynatrace Node.js, Java, PHP, and Staticfile buildpack integrations allow you to leverage not only one, but several service instances to define Dynatrace tags.

## Related topics

* [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")