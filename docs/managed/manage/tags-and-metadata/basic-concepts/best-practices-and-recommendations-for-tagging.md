---
title: Best practices and recommendations for tagging
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging
---

# Best practices and recommendations for tagging

# Best practices and recommendations for tagging

* Explanation
* 5-min read
* Published May 03, 2018

Tagging is a powerful mechanism. However, to reap its benefits, tagging should be used carefully and in a meaningful way. To guide you towards this end, we provide you with specific recommendations and best practices, which are described below. With [auto-tagging based on metadata](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), tags can be generated automatically and assigned to monitored entities with the specific metadata values that Dynatrace detects automatically.

In addition to automatic tagging rules, Dynatrace supports definition of tags through system environment variables and manual tagging. For manual tagging the [POST tags request](/managed/dynatrace-api/environment-api/custom-tags/post-tags "Assign custom tags to monitored entities via Dynatrace API.") of the Custom tags API comes handy, as it enables you to assign a tag to a large set of entities.

## Host metadata and tagging

It's possible to [define tags](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-tag-configuration-file "Learn how to tag and set additional properties for a monitored host.") as well as [additional metadata](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-metadata-configuration-file "Learn how to tag and set additional properties for a monitored host.") for each of the hosts.

It's recommended that you define additional metadata at the deployed system of a host. You should send as much extra metadata as you can. This extra data can be used by Dynatrace to define tags, management zones, or dynamically within charts, dashboards, and more. It's recommended also that you standardize some metadata about your organization. You can save them into the respective config file in an automated fashion during the deployment procedure.

Important aspects to standardize are:

* Owner/team/business unit/line of business
* Environment: staging/production
* Version (if applicable)
* Importance/severity (relevant for problem alerting profiles)

For host tags, it's recommended that you not define tags at the deployed system. The reason is that this is cumbersome and requires a lot of preplanning. It's also hard to change. Only do this when what you want to tag rarely changes and you need to create a filter globally (possible example: importance/severity). Another case would be if your way of working requires you to define tags during deployment time in an automated fashion.

## Application metadata and tagging

What's recommended for hosts is also valid for applications and processes. Typically, you should think about additional metadata and standard metadata and not about tags.

For applications like WebSphere or Tomcat, you should use the [environment variable](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") `DT_CUSTOM_PROP` to define your metadata. This variable needs to be present at the application startup. For WebSphere, you can do this in the WebSphere console in the JVM section. For Tomcat and others, simply define it as part of the startup script.

With Kubernetes, use [Kubernetes annotations](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.") to define your metadata. Dynatrace will pick up all annotations automatically. The same is true for [AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources."). Dynatrace will also pick up AWS tags, but in this case as tags not as metadata. Of course, you can still use them to define additional tags or use them for any other purpose.

To define [Dynatrace tags for Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/organize-cf-deployments-by-tags "Automatically organize and filter all your monitored applications by applying tags from your Cloud Foundry environment."), you can leverage one or more Cloud Foundry service instances that have the name `dynatrace` as a substring.

## Automated tagging

It's recommended that you configure [automated tagging rules](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically."), based on existing or custom metadata, to define your filter sets for charts, alerting, and more. These tags and rules can be changed and adapted any time and will apply almost immediately without any change to the monitored environment or applications.

## CMDB, API and automation

If you have a CMDB where you want to define and maintain your tags, you can do so and use the API to synchronize those tags with Dynatrace. This means you can define tags and assign them to entities via the API. This should be used for common tags that you already maintain in a location outside of Dynatrace.

## Management zones

[Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") are an important concept in Dynatrace and of high importance in large environments, as they can make large organizations work. Management zones are based on the same idea as automated tags, but designed for the explicit purpose of defining groups of entities that either belong together or have common security levels.

It's recommended that you define zones for all teams that specify what they are supposed to view and the different lines of business. It also makes sense to add different zones for different support teams, so that the large amount of data is consumable and so that security layers are introduced. Every user can have access to multiple zones. Zones can overlap, so you don't need to worry about assigning one entity to a specific zone. Shared entities can therefore be in many or all zones.

The best way to create management zones is to define rules based on your entities metadata (including custom metadata). However, if you want to maintain your management zones outside of Dynatrace, you can also base them on tags.

## Problems, management zones, and tags

[Problems](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.") can also be filtered by tags. This basically means that one can focus on problems related to entities with a specific tag. This is also how notification integration can leverage tags. One can define to only send problems that concern entities with a certain tag to a specific [notification integration](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.").

## Naming rules and naming conventions

Dynatrace automatically provides names, but they don’t enable you to quickly identify where an application or service belongs to. To achieve this, it's recommended that you use [service naming rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Use naming rules to customize and enhance the automated naming of your services.") and [process group naming rules](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming"). This can be done in Dynatrace using metadata imported from the monitored applications.

It's highly recommended that you prefix process groups and applications with a designation related to business units (`BU` or `LOB`) or other owner designation. Such naming standard will be applied automatically to new and existing entities and can be enhanced in the future based on newly arising needs. This is also one of the reasons why it makes sense to define a minimal set of metadata that every application can provide.