---
title: "Tags and metadata"
source: https://docs.dynatrace.com/docs/manage/tags-and-metadata
updated: 2026-02-09
---

# Tags and metadata

# Tags and metadata

* Explanation
* 1-min read
* Published Jul 19, 2017

[Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") automatically discovers components in your environment, such as process groups, services and real user applications. Not only can these entities be auto-discovered, their underlying technologies can also be accurately identified (for example, Apache HTTP server, IBM WebSphere, and much more). As part of this auto-detection, Dynatrace discovers network topology as well. Once traffic is monitored, Dynatrace detects also load balancers and proxies. Moreover, Dynatrace supports 3rd party integrations, thus augmenting this data with topology and monitoring information from AWS, VMware, Azure, OpenStack, and more.

Managing such a huge amount of information, however, and organizing such large monitoring environments is a real challenge. To effectively cope with this challenge, Dynatrace supports tags and metadata. Tags and metadata enable you to organize your monitored environments in a meaningful way. Tags in Dynatrace are basically labels or markers while metadata are key/value pairs that are inherent to any monitored entity. Metadata are mainly used for defining extra information for entities while tags are used for organizing entities. You can also create tags based on metadata. In general, although tags and metadata are closely related, they are different concepts and are created and used in a different way.

## Basic concepts

[#### Tags versus metadata

Understand the difference between tags and metadata in Dynatrace.

* Explanation

Read this explanation](/docs/manage/tags-and-metadata/basic-concepts/tags-vs-metadata)[#### Best practices and recommendations for tagging

Learn when it's recommended to use tags that leverage auto-detected metadata, as well as best practices for enriching Dynatrace monitoring with additional metadata.

* Explanation

Read this explanation](/docs/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging)[#### Best practices for scaling tagging and management-zone rules

Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.

* Explanation

Read this explanation](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale)

## Setup

[#### Define and apply tags

Find out how to define and apply tags manually and automatically.

* How-to guide

Read this guide](/docs/manage/tags-and-metadata/setup/how-to-define-tags)[#### Define tags based on environment variables

Find out how Dynatrace enables you to define tags based on environment variables.

* How-to guide

Read this guide](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables)

## Reference

[#### Regular expressions in Dynatrace

Learn how to use regular expressions in the context of Dynatrace.

* Explanation

Read this explanation](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace)

## Use cases

[#### Organize Cloud Foundry deployments by tags

Automatically organize and filter all your monitored applications by applying tags from your Cloud Foundry environment.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/organize-cf-deployments-by-tags)[#### Organize Kubernetes/OpenShift deployments by tags

Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments)[#### Organize Kubernetes/OpenShift deployments by tags

Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments)[#### Define tags and metadata for hosts

Learn how to tag and set additional properties for a monitored host.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts)[#### Define your own process group metadata

Configure your own process-related metadata based on the unique needs of your organization or environment.

* How-to guide

Read this guide](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata)
