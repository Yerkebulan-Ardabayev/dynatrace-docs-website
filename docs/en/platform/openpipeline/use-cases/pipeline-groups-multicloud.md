---
title: Configure multi-cloud ingest governance with pipeline groups
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/pipeline-groups-multicloud
scraped: 2026-02-28T21:12:34.178319
---

# Configure multi-cloud ingest governance with pipeline groups

# Configure multi-cloud ingest governance with pipeline groups

* Latest Dynatrace
* Tutorial
* 18-min read
* Published Feb 26, 2026

This tutorial explains how to create and manage pipeline groups using the Settings API, enabling consistent ingest governance in multiâcloud environments. It demonstrates how to enforce global and cloudâspecific processing logic, restrict sensitive stagesâsuch as permissionsâand ensure that each team operates within clearly defined responsibilities.

By structuring pipelines through mandatory and restrited stages, pipeline groups provide a scalable, centralized approach to managing large sets of pipelines across multiâcloud environments.

![Example pipeline groups for Aws and Azure log processing](https://dt-cdn.net/images/pipeline-group-tutorial-aws-azure-75a041547a.svg)

## Who is this for?

Administrators, SREs, and engineers automating ingest governance at scale.

## What will you learn?

In this tutorial, you'll learn how to:

* Create pipeline groups via the Settings API to manage over 30 pipelines for AWS and Azure log processing.
* Add member pipelines for cloudâ and team-specific workloads.
* Configure composition pipelines that enforce the responsibilities of admin, midâlevel, and dev teams.
* Restrict sensitive stagesâsuch as cost allocation, permissions, and storageâwhich are centrally governed by the admin and midâlevel teams.
* Apply pipeline groups to multiâcloud deployments where consistent ingest governance is required across AWS and Azure, while enabling teams to manage their respective processing and extraction stages.

## Before you begin

### Prerequisites

Required permissions: `settings:objects:read` and `settings:objects:write` with `builtin:openpipeline.<configuration-scope>.pipeline-groups` scope.

Show Settings API schemas

* [Settings API - Pipeline Groups configuration (events) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-pipeline-groups "View builtin:openpipeline.events.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (bizevents) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-pipeline-groups "View builtin:openpipeline.bizevents.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (spans) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-pipeline-groups "View builtin:openpipeline.spans.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (logs) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-pipeline-groups "View builtin:openpipeline.logs.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (davis.problems) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-pipeline-groups "View builtin:openpipeline.davis.problems.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (metrics) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-pipeline-groups "View builtin:openpipeline.metrics.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (security.events) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-pipeline-groups "View builtin:openpipeline.security.events.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (events.security) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-pipeline-groups "View builtin:openpipeline.events.security.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (davis.events) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-pipeline-groups "View builtin:openpipeline.davis.events.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (events.sdlc) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-pipeline-groups "View builtin:openpipeline.events.sdlc.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (system.events) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-pipeline-groups "View builtin:openpipeline.system.events.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (usersessions) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-pipeline-groups "View builtin:openpipeline.usersessions.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")
* [Settings API - Pipeline Groups configuration (user.events) schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-pipeline-groups "View builtin:openpipeline.user.events.pipeline-groups settings schema table of your monitoring environment via the Dynatrace API.")

### Prior knowledge

* You know how to create pipelines via the [Settings API](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-pipelines "View builtin:openpipeline.logs.pipelines settings schema table of your monitoring environment via the Dynatrace API.").
* You know how to [set access control in OpenPipeline](/docs/platform/openpipeline/getting-started/set-access-control "Distribute OpenPipeline ingest source and pipeline management via owner-based access control.").
* You are familiar with [pipeline groups](/docs/platform/openpipeline/concepts/pipeline-groups "Understand how restricting and mandating configurations for pipeline groups via Settings API works.") and [pipeline group limits](/docs/platform/openpipeline/reference/limits#pipeline-groups "Reference limits of Dynatrace OpenPipeline.").

## Configure pipeline groups

In this tutorial, we'll create two pipeline groups, one per cloud provider, each executing a series of composition pipelines and member pipelines. The following table illustrates the scenario that the tutorial aims to achieve.

### 1. Create composition pipelines

1. Define a custom pipeline with the composition role (`"groupRole": "compositionPipeline"` and `"routing": "notRoutable"`) via JSON.

   The composition pipelines in this tutorial are five custom pipelines, defined as follows.

   * A global pipeline called **Global cost center and bucket assignment** that will be used by both groups (AWS pipelines and Azure pipelines) to assign buckets and `dt.cost.cost_center`. It's owned and accessed by the admin team only.

     JSON example

     ```
     {



     "schemaId": "builtin:openpipeline.logs.pipelines",



     "value": {



     "customId": "global-cost-and-bucket",



     "displayName": "Global cost center and bucket assignment",



     "groupRole": "compositionPipeline",



     "routing": "notRoutable",



     "costAllocation": {



     "processors": [



     {



     "type": "costAllocation",



     "id": "cost-allocation-global",



     "description": "Assign global dt.cost.cost_center",



     "enabled": true,



     "matcher": "true",



     "costAllocation": {



     "value": {



     "type": "constant",



     "constant": "CC-GLOBAL-0001"



     }



     }



     }



     ]



     },



     "storage": {



     "processors": [



     {



     "type": "bucketAssignment",



     "id": "bucket-assignment-logs-aws-global",



     "description": "Assign AWS logs to global AWS bucket",



     "enabled": true,



     "matcher": "matchesValue(cloud.provider, \"aws\")",



     "sampleData": "{\"cloud.provider\":\"aws\"}",



     "bucketAssignment": {



     "bucketName": "logs-global-aws-90d"



     }



     },



     {



     "type": "bucketAssignment",



     "id": "bucket-assignment-logs-azure-global",



     "description": "Assign Azure logs to global Azure bucket",



     "enabled": true,



     "matcher": "matchesValue(cloud.provider, \"azure\")",



     "sampleData": "{\"cloud.provider\":\"azure\"}",



     "bucketAssignment": {



     "bucketName": "logs-global-azure-90d"



     }



     }



     ]



     }



     }



     }
     ```
   * Two cloud-specific processing pipelines called **AWS processing** and **Azure processing** to normalize incoming logs from the respective cloud provide and extract metrics, Davis events, and business events. They're managed by several people within the business unit; specificically, they're owned by the mid-level team and accessed by some senior dev team leads.

     JSON example

     AWS

     Azure

     ```
     {



     "schemaId": "builtin:openpipeline.logs.pipelines",



     "value": {



     "customId": "aws-processing",



     "displayName": "AWS processing",



     "groupRole": "compositionPipeline",



     "routing": "notRoutable",



     "processing": {



     "processors": [



     {



     "type": "fieldsAdd",



     "id": "aws-add-provider",



     "description": "Normalize cloud provider",



     "enabled": true,



     "matcher": "true",



     "fieldsAdd": {



     "fields": [



     { "name": "cloud.provider", "value": "aws" }



     ]



     }



     },



     {



     "type": "dql",



     "id": "aws-parse-common",



     "description": "Parse level and requestId from content when present",



     "enabled": true,



     "matcher": "true",



     "sampleData": "{\"content\":\"2025-10-01T10:00:00Z [ERROR] req=abcd-1234 Something failed\",\"service.name\":\"ordersvc\"}",



     "dql": {



     "script": "parse content, \"'[' UPPER:loglevel ']' ' req=' LD:aws.request_id\""



     }



     },



     {



     "type": "drop",



     "id": "aws-drop-elb-health",



     "description": "Drop ELB healthcheck noise",



     "enabled": true,



     "matcher": "matchesValue(content, \"ELB-HealthChecker*\")",



     "sampleData": "{\"content\":\"ELB-HealthChecker 200\"}"



     }



     ]



     },



     "metricExtraction": {



     "processors": [



     {



     "type": "counterMetric",



     "id": "aws-error-counter",



     "description": "Count ERROR logs by service and account",



     "enabled": true,



     "matcher": "matchesValue(loglevel, \"ERROR\")",



     "sampleData": "{\"loglevel\":\"ERROR\",\"service.name\":\"ordersvc\",\"aws.account.id\":\"123456789012\"}",



     "counterMetric": {



     "metricKey": "custom.aws.log.error.count",



     "dimensions": [



     {



     "extractionType": "field",



     "sourceFieldName": "service.name",



     "destinationFieldName": "service"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "aws.account.id",



     "destinationFieldName": "account"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "loglevel"



     }



     ]



     }



     }



     ]



     },



     "davis": {



     "processors": [



     {



     "type": "davis",



     "id": "aws-davis-event",



     "description": "Create Davis problem for ERROR/FATAL AWS logs",



     "enabled": true,



     "matcher": "alert.trigger == true",



     "sampleData": "{\"cloud.provider\":\"aws\",\"service.name\":\"ordersvc\",\"aws.account.id\":\"123456789012\",\"aws.request_id\":\"abcd-1234\",\"dt.source_entity\":\"HOST-1234567890\",\"content\":\"[ERROR] req=abcd-1234 Something failed\"}",



     "davis": {



     "properties": [



     { "key": "event.type", "value": "CUSTOM_ALERT" },



     { "key": "event.name", "value": "AWS log error in {service.name}" },



     { "key": "event.description", "value": "{cloud.provider} error in {service.name} (account:{aws.account.id}, request:{aws.request_id}).{content}" },



     { "key": "dt.source_entity", "value": "{dt.source_entity}" }



     ]



     }



     }



     ]



     },



     "dataExtraction": {



     "processors": [



     {



     "type": "bizevent",



     "id": "aws-bizevent-error",



     "description": "Extract a business event for ERROR/FATAL AWS logs",



     "enabled": true,



     "matcher": "matchesValue(loglevel, \"ERROR\") OR matchesValue(loglevel, \"FATAL\")",



     "sampleData": "{\"cloud.provider\":\"aws\",\"service.name\":\"ordersvc\",\"aws.account.id\":\"123456789012\",\"aws.request_id\":\"abcd-1234\",\"loglevel\":\"ERROR\",\"content\":\"[ERROR] req=abcd-1234 Checkout failed\"}",



     "bizevent": {



     "eventProvider": {



     "type": "constant",



     "constant": "logs"



     },



     "eventType": {



     "type": "constant",



     "constant": "BUSINESS_ERROR"



     },



     "fieldExtraction": {



     "type": "include",



     "include": [



     {



     "extractionType": "field",



     "sourceFieldName": "cloud.provider"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "service.name"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "aws.account.id"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "aws.request_id"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "loglevel"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "content"



     }



     ]



     }



     }



     }



     ]



     }



     }



     }
     ```

     ```
     {



     "schemaId": "builtin:openpipeline.logs.pipelines",



     "value": {



     "customId": "azure-processing",



     "displayName": "Azure processing",



     "groupRole": "compositionPipeline",



     "routing": "notRoutable",



     "processing": {



     "processors": [



     {



     "type": "fieldsAdd",



     "id": "azure-add-provider",



     "description": "Normalize cloud provider",



     "enabled": true,



     "matcher": "true",



     "fieldsAdd": {



     "fields": [



     { "name": "cloud.provider", "value": "azure" }



     ]



     }



     },



     {



     "type": "dql",



     "id": "azure-parse-common",



     "description": "Parse level and operationId from content when present",



     "enabled": true,



     "matcher": "true",



     "sampleData": "{\"content\":\"2025-10-01 10:00:00 Error opId=efgh-5678 Failure\",\"service.name\":\"inventorysvc\"}",



     "dql": {



     "script": "parse content, \"UPPER:loglevel ' opId=' LD:azure.operation_id\""



     }



     },



     {



     "type": "drop",



     "id": "azure-drop-noise",



     "description": "Drop noisy platform heartbeat logs",



     "enabled": true,



     "matcher": "matchesValue(content, \"Heartbeat*\")",



     "sampleData": "{\"content\":\"Heartbeat OK\"}"



     }



     ]



     },



     "metricExtraction": {



     "processors": [



     {



     "type": "counterMetric",



     "id": "azure-error-counter",



     "description": "Count Error logs by service and resource group",



     "enabled": true,



     "matcher": "matchesValue(loglevel, \"ERROR\") OR matchesValue(loglevel, \"Error\")",



     "sampleData": "{\"loglevel\":\"Error\",\"service.name\":\"inventorysvc\",\"azure.resource.group\":\"rg-observability\"}",



     "counterMetric": {



     "metricKey": "custom.azure.log.error.count",



     "dimensions": [



     {



     "extractionType": "field",



     "sourceFieldName": "service.name",



     "destinationFieldName": "service"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "azure.resource.group",



     "destinationFieldName": "resource_group"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "loglevel"



     }



     ]



     }



     }



     ]



     },



     "davis": {



     "processors": [



     {



     "type": "davis",



     "id": "azure-davis-event",



     "description": "Create Davis problem for Error/ERROR/FATAL Azure logs",



     "enabled": true,



     "matcher": "alert.trigger == true",



     "sampleData": "{\"cloud.provider\":\"azure\",\"service.name\":\"inventorysvc\",\"azure.resource.group\":\"rg-observability\",\"azure.operation_id\":\"efgh-5678\",\"dt.source_entity\":\"HOST-0987654321\",\"content\":\"Error opId=efgh-5678 Failure\"}",



     "davis": {



     "properties": [



     { "key": "event.type", "value": "CUSTOM_ALERT" },



     { "key": "event.name", "value": "Azure log error in {service.name}" },



     { "key": "event.description", "value": "{cloud.provider} error in {service.name} (resource_group:{azure.resource.group}, operation:{azure.operation_id}).{content}" },



     { "key": "dt.source_entity", "value": "{dt.source_entity}" }



     ]



     }



     }



     ]



     },



     "dataExtraction": {



     "processors": [



     {



     "type": "bizevent",



     "id": "azure-bizevent-error",



     "description": "Extract a business event for Error/ERROR/FATAL Azure logs",



     "enabled": true,



     "matcher": "matchesValue(loglevel, \"ERROR\") OR matchesValue(loglevel, \"Error\") OR matchesValue(loglevel, \"FATAL\")",



     "sampleData": "{\"cloud.provider\":\"azure\",\"service.name\":\"inventorysvc\",\"azure.resource.group\":\"rg-observability\",\"azure.operation_id\":\"efgh-5678\",\"loglevel\":\"Error\",\"content\":\"Error opId=efgh-5678 Failure during stock update\"}",



     "bizevent": {



     "eventProvider": {



     "type": "constant",



     "constant": "logs"



     },



     "eventType": {



     "type": "constant",



     "constant": "BUSINESS_ERROR"



     },



     "fieldExtraction": {



     "type": "include",



     "include": [



     {



     "extractionType": "field",



     "sourceFieldName": "cloud.provider"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "service.name"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "azure.resource.group"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "azure.operation_id"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "loglevel"



     },



     {



     "extractionType": "field",



     "sourceFieldName": "content"



     }



     ]



     }



     }



     }



     ]



     }



     }



     }
     ```

* Two cloud-specific cost and permission assignment pipelines called **AWS cost and permission assignment** and **Azure cost and permission assignment** to set `dt.cost.product` and security context for the respective cloud provider. They're owned and accessed by the mid-level team only.

  JSON example

  AWS

  Azure

  ```
  {



  "schemaId": "builtin:openpipeline.logs.pipelines",



  "value": {



  "customId": "aws-cost-and-permissions",



  "displayName": "AWS cost and permission assignment",



  "groupRole": "compositionPipeline",



  "routing": "notRoutable",



  "productAllocation": {



  "processors": [



  {



  "type": "productAllocation",



  "id": "aws-product-allocation",



  "description": "Set dt.cost.product for AWS",



  "enabled": true,



  "matcher": "matchesValue(cloud.provider, \"aws\")",



  "sampleData": "{\"cloud.provider\":\"aws\"}",



  "productAllocation": {



  "value": {



  "type": "constant",



  "constant": "prod-aws-observability"



  }



  }



  }



  ]



  },



  "securityContext": {



  "processors": [



  {



  "type": "securityContext",



  "id": "aws-security-context",



  "description": "Restrict access to mid-level team only (AWS logs)",



  "enabled": true,



  "matcher": "true",



  "securityContext": {



  "value": {



  "type": "constant",



  "constant": "security:mid-level:aws-logs"



  }



  }



  }



  ]



  }



  }



  }
  ```

  ```
  {



  "schemaId": "builtin:openpipeline.logs.pipelines",



  "value": {



  "customId": "azure-cost-and-permissions",



  "displayName": "Azure cost and permission assignment",



  "groupRole": "compositionPipeline",



  "routing": "notRoutable",



  "productAllocation": {



  "processors": [



  {



  "type": "productAllocation",



  "id": "azure-product-allocation",



  "description": "Set dt.cost.product for Azure",



  "enabled": true,



  "matcher": "matchesValue(cloud.provider, \"azure\")",



  "sampleData": "{\"cloud.provider\":\"azure\"}",



  "productAllocation": {



  "value": {



  "type": "constant",



  "constant": "prod-azure-observability"



  }



  }



  }



  ]



  },



  "securityContext": {



  "processors": [



  {



  "type": "securityContext",



  "id": "azure-security-context",



  "description": "Restrict access to mid-level team only (Azure logs)",



  "enabled": true,



  "matcher": "true",



  "securityContext": {



  "value": {



  "type": "constant",



  "constant": "security:mid-level:azure-logs"



  }



  }



  }



  ]



  }



  }



  }
  ```
* Use the [`POST /api/v2/settings/objects`](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request with the pipeline schema of the configuration scope (`builtin:openpipeline.<configuration.scope>.pipelines`).

### 2. Create member pipelines

1. To create a member pipeline, create a custom pipeline with the member role (`"groupRole": "memberPipeline"` and `"routing": "routable"`). Use the OpenPipeline settings Web UI or the [`POST /api/v2/settings/objects`](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request with the pipeline schema of the configuration scope (`builtin:openpipeline.<configuration.scope>.pipelines`).

   JSON example

   The following JSON contains an example of the member pipeline structure.

   ```
   {



   "schemaId": "builtin:openpipeline.logs.pipelines",



   "value": {



   "displayName": "AWS Web Frontend",



   "customId": "aws-web-frontend",



   "groupRole": "memberPipeline",



   "routing": "routable",



   "processing": {



   "processors": [



   {



   "type": "fieldsAdd",



   "id": "web-tags",



   "matcher": "true",



   "description": "Add team and product tags for the web frontend",



   "enabled": true,



   "fieldsAdd": {



   "fields": [



   { "name": "dt.owner", "value": "team-web" },



   { "name": "deployment.release_product", "value": "easytrade" },



   { "name": "deployment.release_stage", "value": "prod" }



   ]



   }



   },



   {



   "type": "dql",



   "id": "web-parse-http",



   "matcher": "true",



   "description": "Parse HTTP logs for the web frontend",



   "enabled": true,



   "dql": {



   "script": "parse content, \"TIMESTAMP:timestamp ' ' UPPER:http.method ' ' LD:url.path ' status=' INT:http.status_code ' duration_ms=' INT:duration.ms ' ua=' LD:user_agent\""



   }



   },



   {



   "type": "drop",



   "id": "drop-health",



   "description": "Drop health and readiness checks for the web frontend",



   "enabled": true,



   "matcher": "matchesPhrase(url.path, \"/health\") or matchesPhrase(url.path, \"/ready\")"



   }



   ]



   }



   }



   }
   ```
2. Create the associated route. Use the OpenPipeline settings Web UI or the [`POST /api/v2/settings/objects`](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request with the route schema of the configuration scope (`builtin:openpipeline.<configuration.scope>.routing`).

   JSON example

   The following JSON contains an example of a route structure.

   ```
   {



   "schemaId": "builtin:openpipeline.logs.routing",



   "value": {



   "routingEntries": [



   {



   "enabled": true,



   "pipelineType": "custom",



   "pipelineId": "<aws-web-frontend-object-id>",



   "matcher": "cloud.service.name == \"astroshop-web-frontend\"",



   "description": "Route AstroShop Web Frontend logs to the Web Frontend member pipeline"



   }



   ]



   }



   }
   ```

In this tutorial, the following member pipelines exist.

AWS

Azure

### 3. Create pipeline groups

1. Define two pipeline groups, one for AWS (`AWS pipelines`) and one for Azure (`Azure pipelines`).

   The groups process logs of the respective cloud provider following the same structure. Each group references the following pipelines:

   1. **Global cost and bucket** pipeline: Defines Cost allocation and Storage stages.
   2. **AWS processing** and **Azure processing** pipelines: Define Processing, Metric Extraction, Davis, and Data Extraction stages.
   3. **AWS cost and permission assignment** and **Azure cost and permission assignment** pipelines: Define Product allocation and Security context stages.
   4. Member pipeline (placeholder): Defines Processing stage.

   The groups execute first the composition pipelines (1, 2, 3). They mandate the Cost allocation, Storage, Processing, Metric Extraction, Davis, Data Extraction, Product allocation, and Security context stages in this order. Then, the member pipelines add transformations in the Processing stage.

   JSON example

   AWS

   Azure

   ```
   {



   "schemaId": "builtin:openpipeline.logs.pipeline-groups",



   "value": {



   "displayName": "AWS Pipeline Group",



   "memberPipelines": [



   "<xx000x-web-frontend-object-id>",



   "<xx000x-trade-service-object-id>",



   "<xx000x-portfolio-service-object-id>",



   "<xx000x-account-service-object-id>",



   "<xx000x-quote-service-object-id>",



   "<xx000x-order-service-object-id>",



   "<xx000x-notification-service-object-id>",



   "<xx000x-risk-analytics-service-object-id>",



   "<xx000x-audit-logging-service-object-id>",



   "<xx000x-api-gateway-object-id>",



   "<xx000x-s3-buckets-object-id>",



   "<xx000x-rds-aurora-databases-object-id>",



   "<xx000x-dynamodb-tables-object-id>",



   "<xx000x-lambda-functions-object-id>",



   "<xx000x-ecs-eks-services-object-id>",



   "<xx000x-monitoring-logging-agents-object-id>"



   ],



   "memberStages": {



   "type": "include",



   "include": ["processing"]



   },



   "composition": [



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<xx000x-global-cost-bucket-object-id>",



   "stages": {



   "type": "include",



   "include": ["costAllocation", "storage"]



   }



   },



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<xx000x-aws-processing-object-id>",



   "stages": {



   "type": "include",



   "include": ["processing", "metricExtraction", "davis", "dataExtraction"]



   }



   },



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<xx000x-aws-cost-permissions-object-id>",



   "stages": {



   "type": "include",



   "include": ["productAllocation", "securityContext"]



   }



   },



   {



   "isPipelinePlaceholder": true



   }



   ]



   }



   }
   ```

   ```
   {



   "schemaId": "builtin:openpipeline.logs.pipeline-groups",



   "value": {



   "displayName": "Azure Pipeline Group",



   "memberPipelines": [



   "<yy111y-web-frontend-object-id>",



   "<yy111y-product-catalog-service-object-id>",



   "<yy111y-order-service-object-id>",



   "<yy111y-inventory-service-object-id>",



   "<yy111y-user-account-service-object-id>",



   "<yy111y-cart-service-object-id>",



   "<yy111y-payment-gateway-integration-object-id>",



   "<yy111y-review-&amp;-rating-service-object-id>",



   "<yy111y-recommendation-engine-object-id>",



   "<yy111y-notification-service-object-id>",



   "<yy111y-shipping-service-object-id>",



   "<yy111y-image-processing-service-object-id>",



   "<yy111y-api-gateway-object-id>",



   "<yy111y-azure-sql-storage-accounts-object-id>",



   "<yy111y-azure-functions-logic-apps-object-id>",



   "<yy111y-monitoring-logging-agents-object-id>"



   ],



   "memberStages": {



   "type": "include",



   "include": ["processing"]



   },



   "composition": [



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<yy111y-global-cost-bucket-object-id>",



   "stages": {



   "type": "include",



   "include": ["productAllocation", "storage"]



   }



   },



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<yy111y-azure-processing-object-id>",



   "stages": {



   "type": "include",



   "include": ["processing", "metricExtraction", "davis", "dataExtraction"]



   }



   },



   {



   "isPipelinePlaceholder": false,



   "pipelineId": "<yy111y-azure-cost-permissions-object-id>",



   "stages": {



   "type": "include",



   "include": ["productAllocation", "securityContext"]



   }



   },



   {



   "isPipelinePlaceholder": true



   }



   ]



   }



   }
   ```
2. Use the [`POST /api/v2/settings/objects`](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request with the pipeline group schema of the configuration scope (`builtin:openpipeline.<configuration.scope>.pipeline-groups`).

## Congratulations!

You now have a complete API-based workflow to manage pipeline groups, enforce global governance, and scale pipeline operations across AWS and Azure environments.

You can create new member pipelines and then add them to the group any time. Use the [`PUT /api/v2/settings/objects/{objectId}`](/docs/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") request with the pipeline group schema of the configuration scope (`builtin:openpipeline.<configuration-scope>.pipeline-groups`).

Once the request is successfull, the `memberPipelines` field of the pipeline group lists the member pipeline IDs.

## Related topics

* [OpenPipeline pipeline groups](/docs/platform/openpipeline/concepts/pipeline-groups "Understand how restricting and mandating configurations for pipeline groups via Settings API works.")