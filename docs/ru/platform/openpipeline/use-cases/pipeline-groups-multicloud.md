---
title: Настройка управления приёмом данных в мультиоблачной среде с помощью групп конвейеров
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/pipeline-groups-multicloud
scraped: 2026-03-06T21:16:05.385634
---

* Актуальная версия Dynatrace

В этом руководстве объясняется, как создавать и управлять группами конвейеров с помощью Settings API, обеспечивая согласованное управление приёмом данных в мультиоблачных средах. Оно демонстрирует, как применять глобальную и облачно-специфичную логику обработки, ограничивать чувствительные этапы — такие как разрешения — и гарантировать, что каждая команда работает в рамках чётко определённых обязанностей.

Структурируя конвейеры через обязательные и ограниченные этапы, группы конвейеров обеспечивают масштабируемый и централизованный подход к управлению большими наборами конвейеров в мультиоблачных средах.

![Пример групп конвейеров для обработки логов AWS и Azure](https://dt-cdn.net/images/pipeline-group-tutorial-aws-azure-75a041547a.svg)

## Для кого это руководство?

Администраторы, SRE-инженеры и инженеры, автоматизирующие управление приёмом данных в масштабе.

## Чему вы научитесь?

В этом руководстве вы узнаете, как:

* Создавать группы конвейеров через Settings API для управления более чем 30 конвейерами для обработки логов AWS и Azure.
* Добавлять участвующие конвейеры для облачно- и командно-специфичных рабочих нагрузок.
* Настраивать композиционные конвейеры, которые определяют обязанности команд администраторов, среднего уровня и разработчиков.
* Ограничивать чувствительные этапы — такие как распределение затрат, разрешения и хранение — которые централизованно управляются командами администраторов и среднего уровня.
* Применять группы конвейеров к мультиоблачным развёртываниям, где требуется согласованное управление приёмом данных в AWS и Azure, позволяя командам управлять собственными этапами обработки и извлечения.

## Перед началом

### Необходимые условия

Необходимые разрешения: `settings:objects:read` и `settings:objects:write` с областью `builtin:openpipeline.<configuration-scope>.pipeline-groups`.

Показать схемы Settings API

* Settings API — таблица схемы конфигурации Pipeline Groups (events)
* Settings API — таблица схемы конфигурации Pipeline Groups (bizevents)
* Settings API — таблица схемы конфигурации Pipeline Groups (spans)
* Settings API — таблица схемы конфигурации Pipeline Groups (logs)
* Settings API — таблица схемы конфигурации Pipeline Groups (davis.problems)
* Settings API — таблица схемы конфигурации Pipeline Groups (metrics)
* Settings API — таблица схемы конфигурации Pipeline Groups (security.events)
* Settings API — таблица схемы конфигурации Pipeline Groups (events.security)
* Settings API — таблица схемы конфигурации Pipeline Groups (davis.events)
* Settings API — таблица схемы конфигурации Pipeline Groups (events.sdlc)
* Settings API — таблица схемы конфигурации Pipeline Groups (system.events)
* Settings API — таблица схемы конфигурации Pipeline Groups (usersessions)
* Settings API — таблица схемы конфигурации Pipeline Groups (user.events)

### Предварительные знания

* Вы знаете, как создавать конвейеры через Settings API.
* Вы знаете, как настроить контроль доступа в OpenPipeline.
* Вы знакомы с группами конвейеров и [лимитами групп конвейеров](../reference/limits.md#pipeline-groups "Справочные лимиты Dynatrace OpenPipeline.").

## Настройка групп конвейеров

В этом руководстве мы создадим две группы конвейеров, по одной на облачного провайдера, каждая из которых выполняет серию композиционных конвейеров и участвующих конвейеров. Следующая таблица иллюстрирует сценарий, который данное руководство стремится реализовать.

### 1. Создание композиционных конвейеров

1. Определите пользовательский конвейер с ролью composition (`"groupRole": "compositionPipeline"` и `"routing": "notRoutable"`) через JSON.

   Композиционные конвейеры в этом руководстве — это пять пользовательских конвейеров, определённых следующим образом.

   * Глобальный конвейер под названием **Global cost center and bucket assignment**, который будет использоваться обеими группами (конвейеры AWS и конвейеры Azure) для назначения бакетов и `dt.cost.cost_center`. Он принадлежит и доступен только команде администраторов.

     Пример JSON

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
   * Два облачно-специфичных конвейера обработки под названиями **AWS processing** и **Azure processing** для нормализации входящих логов от соответствующего облачного провайдера и извлечения метрик, событий Davis и бизнес-событий. Ими управляют несколько человек в бизнес-подразделении; в частности, они принадлежат команде среднего уровня и доступны некоторым старшим руководителям команд разработчиков.

     Пример JSON

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

* Два облачно-специфичных конвейера назначения затрат и разрешений под названиями **AWS cost and permission assignment** и **Azure cost and permission assignment** для установки `dt.cost.product` и контекста безопасности для соответствующего облачного провайдера. Они принадлежат и доступны только команде среднего уровня.

  Пример JSON

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
* Используйте запрос `POST /api/v2/settings/objects` со схемой конвейера для области конфигурации (`builtin:openpipeline.<configuration.scope>.pipelines`).


### 2. Создание участвующих конвейеров

1. Чтобы создать участвующий конвейер, создайте пользовательский конвейер с ролью member (`"groupRole": "memberPipeline"` и `"routing": "routable"`). Используйте веб-интерфейс настроек OpenPipeline или запрос `POST /api/v2/settings/objects` со схемой конвейера для области конфигурации (`builtin:openpipeline.<configuration.scope>.pipelines`).

   Пример JSON

   Следующий JSON содержит пример структуры участвующего конвейера.

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
2. Создайте связанный маршрут. Используйте веб-интерфейс настроек OpenPipeline или запрос `POST /api/v2/settings/objects` со схемой маршрута для области конфигурации (`builtin:openpipeline.<configuration.scope>.routing`).

   Пример JSON

   Следующий JSON содержит пример структуры маршрута.

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

В этом руководстве существуют следующие участвующие конвейеры.

AWS

Azure

### 3. Создание групп конвейеров

1. Определите две группы конвейеров: одну для AWS (`AWS pipelines`) и одну для Azure (`Azure pipelines`).

   Группы обрабатывают логи соответствующего облачного провайдера по одной и той же структуре. Каждая группа ссылается на следующие конвейеры:

   1. Конвейер **Global cost and bucket**: Определяет этапы Cost allocation и Storage.
   2. Конвейеры **AWS processing** и **Azure processing**: Определяют этапы Processing, Metric Extraction, Dynatrace Intelligence и Data Extraction.
   3. Конвейеры **AWS cost and permission assignment** и **Azure cost and permission assignment**: Определяют этапы Product allocation и Security context.
   4. Участвующий конвейер (заполнитель): Определяет этап Processing.

   Группы сначала выполняют композиционные конвейеры (1, 2, 3). Они обязывают выполнять этапы Cost allocation, Storage, Processing, Metric Extraction, Dynatrace Intelligence, Data Extraction, Product allocation и Security context в указанном порядке. Затем участвующие конвейеры добавляют преобразования на этапе Processing.

   Пример JSON

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
2. Используйте запрос `POST /api/v2/settings/objects` со схемой группы конвейеров для области конфигурации (`builtin:openpipeline.<configuration.scope>.pipeline-groups`).

## Поздравляем!

Теперь у вас есть полный рабочий процесс на основе API для управления группами конвейеров, обеспечения глобального управления и масштабирования операций конвейеров в средах AWS и Azure.

Вы можете создавать новые участвующие конвейеры и затем добавлять их в группу в любое время. Используйте запрос `PUT /api/v2/settings/objects/{objectId}` со схемой группы конвейеров для области конфигурации (`builtin:openpipeline.<configuration-scope>.pipeline-groups`).

После успешного выполнения запроса поле `memberPipelines` группы конвейеров будет содержать идентификаторы участвующих конвейеров.

## Связанные темы

* Группы конвейеров OpenPipeline
