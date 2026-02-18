---
title: Tags and management zones for AWS integration
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/tags-and-management-zones-aws
scraped: 2026-02-17T05:04:07.494866
---

# Tags and management zones for AWS integration

# Tags and management zones for AWS integration

* How-to guide
* 4-min read
* Updated on Feb 20, 2024

To organize cloud entities in your environment and simplify searches for them, you can use tags and basic instance properties imported from the cloud, as well as tags and management zones assigned in Dynatrace. Tags and management zones are applied to cloud entities just as they are for other entities, but they are best applied via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Cloud entities in your environment

You can browse all cloud entites in your environment using their ID or type from [cloud entity types](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.") via the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."), just as for other entities. You can also explore all available properties and relationships available for each individual resource or type.

You can also browse their metrics using entity selector as part of [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."), e.g. in [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

Cloud entity types

To learn more about Dynatrace cloud entities and to check which ones can have tags imported from the cloud, see [Cloud services with their respective Dynatrace entity types](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.").

## Add an automatically applied tag to cloud entities

Follow the steps below to automatically apply a tag to cloud entities. To learn more about tags, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

1. Go to **Settings** > **Tags** > **Automatically applied tags**.
2. Select **Create tag** and type a name for the new tag in the **Tag name** field.
3. Select **Add a new rule**.
4. Optional **Optional tag value**. This value appears next to the tag name that the rule is specified for, after a `:`, and is used to provide more precise information based on the individual rule. Note that for rules based on the entity selector, this value cannot be extracted from the entity itself using placeholders.
5. From the **Rule type** list, choose the **Entity selector** type.
6. Use one of the code snippets from the [examples](#entity-selector-examples) and adapt it with your own values to apply tags to cloud entities matching your [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").
7. Select **Preview** to verify the results returned by the specific entity selector.
8. Select **Save changes**.

Example of a rule-based entity selector

![Queue entity selector](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Add cloud entities to existing management zones

Follow the steps below to add cloud entities to existing management zones. To learn more about management zones, see [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.").

1. Go to **Settings** > **Preferences** > **Management zones**.
2. Edit an existing management zone and select **Add a new rule**.
3. In the **Rule applies to** list, choose the **Entity selector**.
4. Use one of the code snippets from the [examples](#entity-selector-examples) and adapt it with your own values to add to the management zone cloud entities matching the [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints.").
5. Select **Preview** to verify the results returned by the specific entity selector.
6. Select **Save changes**.

Example of a management zone based on the entity selector

![Management zone for queues](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Entity selector examples for AWS entities

You can use the examples below and [cloud entity types](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.") to suit your own needs.

Regions and zones

AWS account

Tags

Other properties

Non-built-in cloud services types

```
type(CUSTOM_DEVICE), customDeviceSource("AWS"), customProperties("REGION_NAME:af-south-1")
```

Non-built-in cloud service - specific service type: Lambda

```
type(cloud:aws:lambda), customProperties("REGION_NAME:us-east-1")
```

Lambda (built-in) in region

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),regionName("us-east-1"))
```

Lambda (built-in) in availability zones

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),entityName("us-east-1a"))
```

```
type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))
```

Non-built-in cloud services

```
type(CUSTOM_DEVICE),tag([AWS]environment:dev)
```

```
type(CUSTOM_DEVICE),tag([AWS]owner:TeamA)
```

Non-built-in cloud service - specific service type

```
type(cloud:aws:s3),tag([AWS]environment:dev)
```

```
type(cloud:aws:lambda),tag([AWS]environment:dev)
```

Built-in cloud services

```
type(AWS_LAMBDA_FUNCTION),tag([AWS]environment:dev)
```

```
type(EC2_INSTANCE),tag([AWS]owner:TeamA)
```

```
type(RELATIONAL_DATABASE_SERVICE),tag([AWS]owner:TeamA)
```

Non-built-in cloud services

```
type(CUSTOM_DEVICE),arn("arn:aws:s3:::simple-storage-dev")
```

```
type(CUSTOM_DEVICE),customDeviceSource("AWS"), ipAddress(172.0.0.202)
```

```
type(CUSTOM_DEVICE),customDeviceSource("AWS"), ipAddress(172.0.0.202)
```

Non-built-in cloud service - specific service type

```
type(cloud:aws:api_gateway),customProperties("ApiId:9a8b7cd6ef")
```

Built-in cloud services

```
type("EC2_INSTANCE"),ipAddress("3.123.987.65")
```

```
type("RELATIONAL_DATABASE_SERVICE"),arn("arn:aws:rds:us-east-1:908070605040:db:database-1-instance-1")
```

```
type("RELATIONAL_DATABASE_SERVICE"),rdsEngine("aurora-mysql")
```

EC2

Lambda

Services

Process groups and hosts

```
type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))
```

```
type(EC2_INSTANCE),tag([AWS]owner:TeamA)
```

EC2s with OneAgent installed

```
type(EC2_INSTANCE),toRelationships.runsOn(type(HOST))
```

EC2s without OneAgent installed

```
type(EC2_INSTANCE),not(toRelationships.runsOn(type(HOST)))
```

Lambda properties

```
type(cloud:aws:lambda), customProperties("REGION_NAME:us-east-1")
```

```
type(cloud:aws:lambda), customProperties("Runtime:python3.8")
```

```
type(cloud:aws:lambda), customProperties("Version:$LATEST")
```

Lambda (built-in) in region

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),regionName("us-east-1"))
```

Lambda (built-in) in availability zones

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),entityName("us-east-1a"))
```

Lambdas with OneAgent installed

```
type(cloud:aws:lambda),toRelationships.runsOn(type(SERVICE))
```

Lambdas without OneAgent installed

```
type(cloud:aws:lambda),not(toRelationships.runsOn(type(SERVICE)))
```

Lambda (built-in) with OneAgent installed

```
type(AWS_LAMBDA_FUNCTION),toRelationships.runsOn(type(SERVICE))
```

Lambdas (built-in) without OneAgent installed

```
type(AWS_LAMBDA_FUNCTION),not(toRelationships.runsOn(type(SERVICE)))
```

Services also monitored by AWS integration

EC2

```
type(SERVICE),fromRelationships.runsOnHost(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

Lambda

```
type(SERVICE),fromRelationships.runsOn(type(cloud:aws:lambda),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS)))
```

Lambda (built-in)

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS)))
```

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION), entityId("AWS_LAMBDA_FUNCTION-60AAABCDF1234B3A"))
```

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION),tag([AWS]Environment:DEV))
```

Process groups and hosts also monitored by AWS integration

```
type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040")))
```

```
type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

```
type(PROCESS_GROUP),fromRelationships.runsOn(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

## Related topics



* [Management zones](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Queue tags and management zones](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Automatically apply tags to queues and organize them into management zones.")
* [Set up management zones](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")
* [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Infrastructure Observability](/docs/observe/infrastructure-observability "The application infrastructure, including cloud and container platforms, that Dynatrace can monitor")