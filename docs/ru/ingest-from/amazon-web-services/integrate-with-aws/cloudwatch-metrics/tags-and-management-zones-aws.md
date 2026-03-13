---
title: Tags and management zones for AWS integration
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/tags-and-management-zones-aws
scraped: 2026-03-02T21:30:15.566087
---

# Теги и зоны управления для интеграции с AWS

# Теги и зоны управления для интеграции с AWS

* Практическое руководство
* Чтение: 4 мин
* Обновлено 20 февраля 2024

Для организации облачных сущностей в вашей среде и упрощения их поиска вы можете использовать теги и базовые свойства экземпляров, импортированные из облака, а также теги и зоны управления, назначенные в Dynatrace. Теги и зоны управления применяются к облачным сущностям так же, как и к другим сущностям, но лучше всего их применять через [селектор сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

## Облачные сущности в вашей среде

Вы можете просматривать все облачные сущности в вашей среде, используя их ID или тип из [типов облачных сущностей](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.") через [селектор сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."), так же как и для других сущностей. Вы также можете изучить все доступные свойства и связи для каждого отдельного ресурса или типа.

Вы также можете просматривать их метрики, используя селектор сущностей как часть [селектора метрик](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API."), например, в [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

Типы облачных сущностей

Чтобы узнать больше об облачных сущностях Dynatrace и проверить, какие из них могут иметь теги, импортированные из облака, см. [Облачные сервисы с соответствующими типами сущностей Dynatrace](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.").

## Добавление автоматически применяемого тега к облачным сущностям

Выполните следующие шаги для автоматического применения тега к облачным сущностям. Чтобы узнать больше о тегах, см. [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

1. Перейдите в **Settings** > **Tags** > **Automatically applied tags**.
2. Нажмите **Create tag** и введите имя нового тега в поле **Tag name**.
3. Нажмите **Add a new rule**.
4. Необязательно **Optional tag value**. Это значение отображается рядом с именем тега, для которого указано правило, после `:`, и используется для предоставления более точной информации на основе конкретного правила. Обратите внимание, что для правил на основе селектора сущностей это значение не может быть извлечено из самой сущности с помощью заполнителей.
5. Из списка **Rule type** выберите тип **Entity selector**.
6. Используйте один из фрагментов кода из [примеров](#entity-selector-examples) и адаптируйте его с вашими собственными значениями для применения тегов к облачным сущностям, соответствующим вашему [селектору сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").
7. Нажмите **Preview**, чтобы проверить результаты, возвращаемые конкретным селектором сущностей.
8. Нажмите **Save changes**.

Пример правила на основе селектора сущностей

![Queue entity selector](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Добавление облачных сущностей в существующие зоны управления

Выполните следующие шаги для добавления облачных сущностей в существующие зоны управления. Чтобы узнать больше о зонах управления, см. [Настройка зон управления](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.").

1. Перейдите в **Settings** > **Preferences** > **Management zones**.
2. Отредактируйте существующую зону управления и нажмите **Add a new rule**.
3. В списке **Rule applies to** выберите **Entity selector**.
4. Используйте один из фрагментов кода из [примеров](#entity-selector-examples) и адаптируйте его с вашими собственными значениями для добавления облачных сущностей, соответствующих [селектору сущностей](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Configure the entity selector for Environment API endpoints."), в зону управления.
5. Нажмите **Preview**, чтобы проверить результаты, возвращаемые конкретным селектором сущностей.
6. Нажмите **Save changes**.

Пример зоны управления на основе селектора сущностей

![Management zone for queues](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Примеры селекторов сущностей для сущностей AWS

Вы можете использовать приведённые ниже примеры и [типы облачных сущностей](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services#cloud-entity-types "Monitor all AWS cloud services with Dynatrace and view available metrics.") в соответствии со своими потребностями.

Регионы и зоны

Аккаунт AWS

Теги

Другие свойства

Небазовые типы облачных сервисов

```
type(CUSTOM_DEVICE), customDeviceSource("AWS"), customProperties("REGION_NAME:af-south-1")
```

Небазовый облачный сервис — конкретный тип сервиса: Lambda

```
type(cloud:aws:lambda), customProperties("REGION_NAME:us-east-1")
```

Lambda (базовый) в регионе

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),regionName("us-east-1"))
```

Lambda (базовый) в зонах доступности

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),entityName("us-east-1a"))
```

```
type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))
```

Небазовые облачные сервисы

```
type(CUSTOM_DEVICE),tag([AWS]environment:dev)
```

```
type(CUSTOM_DEVICE),tag([AWS]owner:TeamA)
```

Небазовый облачный сервис — конкретный тип сервиса

```
type(cloud:aws:s3),tag([AWS]environment:dev)
```

```
type(cloud:aws:lambda),tag([AWS]environment:dev)
```

Базовые облачные сервисы

```
type(AWS_LAMBDA_FUNCTION),tag([AWS]environment:dev)
```

```
type(EC2_INSTANCE),tag([AWS]owner:TeamA)
```

```
type(RELATIONAL_DATABASE_SERVICE),tag([AWS]owner:TeamA)
```

Небазовые облачные сервисы

```
type(CUSTOM_DEVICE),arn("arn:aws:s3:::simple-storage-dev")
```

```
type(CUSTOM_DEVICE),customDeviceSource("AWS"), ipAddress(172.0.0.202)
```

```
type(CUSTOM_DEVICE),customDeviceSource("AWS"), ipAddress(172.0.0.202)
```

Небазовый облачный сервис — конкретный тип сервиса

```
type(cloud:aws:api_gateway),customProperties("ApiId:9a8b7cd6ef")
```

Базовые облачные сервисы

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

Сервисы

Группы процессов и хосты

```
type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))
```

```
type(EC2_INSTANCE),tag([AWS]owner:TeamA)
```

EC2 с установленным OneAgent

```
type(EC2_INSTANCE),toRelationships.runsOn(type(HOST))
```

EC2 без установленного OneAgent

```
type(EC2_INSTANCE),not(toRelationships.runsOn(type(HOST)))
```

Свойства Lambda

```
type(cloud:aws:lambda), customProperties("REGION_NAME:us-east-1")
```

```
type(cloud:aws:lambda), customProperties("Runtime:python3.8")
```

```
type(cloud:aws:lambda), customProperties("Version:$LATEST")
```

Lambda (базовый) в регионе

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),regionName("us-east-1"))
```

Lambda (базовый) в зонах доступности

```
type(AWS_LAMBDA_FUNCTION),toRelationships.isSiteOf(type(AWS_AVAILABILITY_ZONE),entityName("us-east-1a"))
```

Lambda с установленным OneAgent

```
type(cloud:aws:lambda),toRelationships.runsOn(type(SERVICE))
```

Lambda без установленного OneAgent

```
type(cloud:aws:lambda),not(toRelationships.runsOn(type(SERVICE)))
```

Lambda (базовый) с установленным OneAgent

```
type(AWS_LAMBDA_FUNCTION),toRelationships.runsOn(type(SERVICE))
```

Lambda (базовый) без установленного OneAgent

```
type(AWS_LAMBDA_FUNCTION),not(toRelationships.runsOn(type(SERVICE)))
```

Сервисы, также мониторящиеся через интеграцию с AWS

EC2

```
type(SERVICE),fromRelationships.runsOnHost(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

Lambda

```
type(SERVICE),fromRelationships.runsOn(type(cloud:aws:lambda),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS)))
```

Lambda (базовый)

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS)))
```

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION), entityId("AWS_LAMBDA_FUNCTION-60AAABCDF1234B3A"))
```

```
type(SERVICE),fromRelationships.runsOn(type(AWS_LAMBDA_FUNCTION),tag([AWS]Environment:DEV))
```

Группы процессов и хосты, также мониторящиеся через интеграцию с AWS

```
type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040")))
```

```
type(PROCESS_GROUP_INSTANCE),fromRelationships.isProcessOf(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

```
type(PROCESS_GROUP),fromRelationships.runsOn(type(HOST),fromRelationships.runsOn(type(EC2_INSTANCE),fromRelationships.isAccessibleBy(type(AWS_CREDENTIALS),awsAccountId("908070605040"))))
```

## Связанные темы

* [Зоны управления](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Теги и зоны управления для очередей](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Automatically apply tags to queues and organize them into management zones.")
* [Настройка зон управления](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.")
* [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Мониторинг инфраструктуры](/docs/observe/infrastructure-observability "The application infrastructure, including cloud and container platforms, that Dynatrace can monitor")
