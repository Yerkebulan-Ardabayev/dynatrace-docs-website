---
title: Tags and management zones for Azure integration
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/tags-and-management-zones-azure
scraped: 2026-03-02T21:17:10.782245
---

# Теги и зоны управления для интеграции с Azure

# Теги и зоны управления для интеграции с Azure

* Latest Dynatrace
* How-to guide
* 5 мин. чтения
* Обновлено 14 октября 2024 г.

Для организации облачных сущностей в вашей среде и упрощения их поиска вы можете использовать теги и базовые свойства экземпляров, импортированные из облака, а также теги и зоны управления, назначенные в Dynatrace. Теги и зоны управления применяются к облачным сущностям так же, как и к другим сущностям, но лучше всего применять их через [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка entity selector для конечных точек Environment API.").

## Облачные сущности в вашей среде

Вы можете просматривать все облачные сущности в вашей среде, используя их идентификатор или тип из [типов облачных сущностей](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.") через [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Настройка entity selector для конечных точек Environment API."), так же как и для других сущностей. Вы также можете исследовать все доступные свойства и взаимосвязи для каждого отдельного ресурса или типа.

Вы также можете просматривать их метрики, используя entity selector как часть [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Настройка metric selector для Metric v2 API."), например, в [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения нужной аналитики.").

Типы облачных сущностей

Чтобы узнать больше об облачных сущностях Dynatrace и проверить, у каких из них можно импортировать теги из облака, см. [Облачные сервисы с соответствующими типами сущностей Dynatrace](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.").

## Добавление автоматически применяемого тега к облачным сущностям

Выполните следующие шаги для автоматического применения тега к облачным сущностям. Чтобы узнать больше о тегах, см. [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.").

1. Перейдите в **Settings** > **Tags** > **Automatically applied tags**.
2. Выберите **Create tag** и введите имя нового тега в поле **Tag name**.
3. Выберите **Add a new rule**.
4. Необязательно **Optional tag value**. Это значение появляется рядом с именем тега, для которого указано правило, после `:` и используется для предоставления более точной информации на основе конкретного правила. Обратите внимание, что для правил на основе entity selector это значение не может быть извлечено из самой сущности с помощью заполнителей.
5. В списке **Rule type** выберите тип **Entity selector**.
6. Используйте один из фрагментов кода из [примеров](#entity-selector-examples) и адаптируйте его с вашими собственными значениями для применения тегов к облачным сущностям, соответствующим вашему [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Настройка entity selector для конечных точек Environment API.").
7. Выберите **Preview** для проверки результатов, возвращаемых конкретным entity selector.
8. Выберите **Save changes**.

Пример правила на основе entity selector

![Entity selector для очередей](https://dt-cdn.net/images/queue-entity-selector-1688-9b93f73016.png)

## Добавление облачных сущностей в существующие зоны управления

Выполните следующие шаги для добавления облачных сущностей в существующие зоны управления. Чтобы узнать больше о зонах управления, см. [Настройка зон управления](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа к ним.").

1. Перейдите в **Settings** > **Preferences** > **Management zones**.
2. Отредактируйте существующую зону управления и выберите **Add a new rule**.
3. В списке **Rule applies to** выберите **Entity selector**.
4. Используйте один из фрагментов кода из [примеров](#entity-selector-examples) и адаптируйте его с вашими собственными значениями для добавления в зону управления облачных сущностей, соответствующих [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector#tag "Настройка entity selector для конечных точек Environment API.").
5. Выберите **Preview** для проверки результатов, возвращаемых конкретным entity selector.
6. Выберите **Save changes**.

Пример зоны управления на основе entity selector

![Зона управления для очередей](https://dt-cdn.net/images/queue-management-zone-1688-12745271e1.png)

## Примеры entity selector для сущностей Azure

Вы можете использовать приведённые ниже примеры и [типы облачных сущностей](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics#cloud-entity-types "Мониторинг сервисов Azure с помощью Dynatrace и просмотр доступных метрик.") в соответствии с вашими потребностями.

Регионы

Группы ресурсов

Подписки

Теги

Другие свойства

Типы облачных сервисов не встроенные

```
type(CUSTOM_DEVICE), customDeviceSource("AZURE"), customProperties("Region:South Africa North")
```

```
type(CUSTOM_DEVICE), customDeviceSource("AZURE"), not(customProperties("Region:South Africa North"))
```

```
type(cloud:azure:batch:account), customDeviceSource("AZURE"), customProperties("Region:South Africa North")
```

Типы встроенных облачных сервисов

```
type(AZURE_STORAGE_ACCOUNT), toRelationship.isSiteOf(type(AZURE_REGION), entityName(northeurope))
```

Типы облачных сервисов не встроенные

```
type(CUSTOM_DEVICE),customProperties("Resource group:test-rg3")
```

```
type(cloud:azure:batch:account),customProperties("Resource group:test-rg3")
```

Типы встроенных облачных сервисов

```
type(AZURE_STORAGE_ACCOUNT), azureResourceGroupName("cloud-test-rg-westeurope")
```

Типы облачных сервисов не встроенные

```
type(CUSTOM_DEVICE),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

```
type(CUSTOM_DEVICE),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),azureSubscriptionUuid("d1234e5f-de67-4db2-ad02-d89d2a1234f5"))
```

```
type(cloud:azure:batch:account),fromRelationships.belongsTo(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

Типы встроенных облачных сервисов

```
type(AZURE_STORAGE_ACCOUNT),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Team-Product"))
```

```
type(AZURE_STORAGE_ACCOUNT),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),azureSubscriptionUuid("d1234e5f-de67-4db2-ad02-d89d2a1234f5"))
```

Не встроенные облачные сервисы

```
type(CUSTOM_DEVICE),tag([AZURE]environment:DEV)
```

```
type(CUSTOM_DEVICE),tag([AZURE]owner:TeamA)
```

Не встроенный облачный сервис -- конкретный тип сервиса

```
type(cloud:azure:batch:account),tag([AZURE]environment:DEV)
```

Встроенные облачные сервисы

```
type(AZURE_STORAGE_ACCOUNT),tag([AZURE]environment:DEV)
```

```
type(AZURE_VM),tag([AZURE]owner:TeamA)
```

Теги на родительском ресурсе для сервиса Azure, не имеющего собственных тегов

```
type(AZURE_SERVICE_BUS_TOPIC), toRelationship.isAzrServiceBusNamespaceOfQueue(type(AZURE_SERVICE_BUS_NAMESPACE),tag("[Azure]tagOnParent:valueOnParent"))
```

Не встроенные облачные сервисы

```
type(CUSTOM_DEVICE),customProperties("Resource group:new-resources")
```

```
type(CUSTOM_DEVICE),customDeviceSource("AZURE"),dnsNames(ademotestlab.file.core.windows.net)
```

```
type(CUSTOM_DEVICE),customDeviceSource("AZURE"), ipAddress(172.0.0.202)
```

Не встроенный облачный сервис -- конкретный тип сервиса

```
type(cloud:azure:storage:storageaccounts:file),customProperties("Resource group:new-resources")
```

```
type(cloud:azure:storage:storageaccounts:file),dnsNames(ademodevtestlab5563.file.core.windows.net)
```

```
type("cloud:azure:network:loadbalancers:standard"),ipAddress(10.237.0.223)
```

```
type(cloud:azure:storage:storageaccounts),not(customProperties.exists("Secondary region"))
```

```
type(cloud:azure:storage:storageaccounts:file),customProperties("Status of primary region:available")
```

Встроенные облачные сервисы

```
type(AZURE_STORAGE_ACCOUNT), azureStorageAccountSecondaryRegion.exists()
```

```
type(AZURE_STORAGE_ACCOUNT), dnsNames("csb10030000ab28bff8.blob.core.windows.net")
```

```
type(AZURE_SERVICE_BUS_TOPIC), azureServiceBusMaxSizeMb("1024")
```

Виртуальные машины

Функции

Сервисы

Группы процессов и хосты

```
type("AZURE_VM"), dnsNames("ag-vm.eastus.cloudapp.azure.com")
```

Виртуальные машины Azure с установленным OneAgent

```
type("AZURE_VM"), toRelationship.runsOn(type(HOST))
```

Виртуальные машины Azure без установленного OneAgent

```
type("AZURE_VM"), not(toRelationship.runsOn(type(HOST)))
```

Azure Functions, работающие на App Service Plan с установленным расширением сайта OneAgent

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(HOST))
```

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP_INSTANCE))
```

```
type("AZURE_FUNCTION_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP))
```

Azure Functions, работающие на App Service Plan без установленного расширения сайта OneAgent

```
type("AZURE_FUNCTION_APP"),not(sku("Dynamic")),not(fromRelationships.isPgAppOf(type(HOST)))
```

```
type("AZURE_FUNCTION_APP"),sku("Standard"),not(fromRelationships.isPgAppOf(type(HOST)))
```

Azure Functions, инструментированные библиотеками Dynatrace OpenTelemetry (ODIN)

```
type(AZURE_FUNCTION_APP), toRelationship.runsOn(type("SERVICE"))
```

Azure Functions, работающие на плане Consumption, инструментированные библиотеками Dynatrace OpenTelemetry (ODIN)

```
type(AZURE_FUNCTION_APP), sku("Dynamic"), toRelationship.runsOn(type("SERVICE"))
```

Azure Functions, работающие на плане Consumption, не инструментированные библиотеками Dynatrace OpenTelemetry (ODIN)

```
type(AZURE_FUNCTION_APP), sku("Dynamic"), not(toRelationship.runsOn(type("SERVICE")))
```

App Services с установленным OneAgent

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(HOST))
```

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP_INSTANCE))
```

```
type("AZURE_WEB_APP"),fromRelationships.isPgAppOf(type(PROCESS_GROUP))
```

App Services без установленного OneAgent

```
type("AZURE_WEB_APP"),not(fromRelationships.isPgAppOf(type(HOST)))
```

Сервисы, которые также мониторятся интеграцией Azure -- для Function Apps на App Service Plan

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP)))
```

```
type(SERVICE), fromRelationships.runsOn(type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnProcessGroupInstance(type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP), entityName("funcapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),tag("[Azure]environment:DEV")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription"))))
```

Сервисы, которые также мониторятся интеграцией Azure -- для Function Apps, инструментированных библиотеками Dynatrace OpenTelemetry (ODIN)

```
type(SERVICE), fromRelationship.runsOn(type("AZURE_FUNCTION_APP"))
```

Сервисы, которые также мониторятся интеграцией Azure -- для Function Apps, работающих на плане Consumption, инструментированных библиотеками Dynatrace OpenTelemetry (ODIN)

```
type(SERVICE), fromRelationship.runsOn(type("AZURE_FUNCTION_APP"), sku("Dynamic"))
```

Сервисы, которые также мониторятся интеграцией Azure -- для Web Apps

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP)))
```

```
type(SERVICE), fromRelationships.runsOn(type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnProcessGroupInstance(type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP), entityName("webapp-name")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP),tag("[Azure]environment:DEV")))
```

```
type(SERVICE), fromRelationships.runsOnOsi(type(HOST), toRelationships.isPgAppOf(type(AZURE_WEB_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription"))))
```

Группы процессов и хосты, также мониторируемые интеграцией Azure

```
type(HOST), fromRelationships.runsOn(type(AZURE_VM),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(HOST), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP_INSTANCE), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type(AZURE_SUBSCRIPTION),entityName("Cloud Dev Subcription")))
```

```
type(PROCESS_GROUP), toRelationships.isPgAppOf(type(AZURE_FUNCTION_APP),fromRelationships.isAccessibleBy(type("AZURE_SUBSCRIPTION"),entityName("Cloud Dev Subcription")))
```

## Связанные темы

* [Зоны управления](/docs/manage/identity-access-management/permission-management/management-zones "Узнайте о концепциях зон управления, как определять зоны управления и как использовать их максимально эффективно.")
* [Теги и зоны управления для очередей](/docs/observe/infrastructure-observability/queues/configuration/tags-and-management-zones "Автоматическое применение тегов к очередям и организация их в зоны управления.")
* [Настройка зон управления](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Создание зон управления и назначение прав доступа к ним.")
* [Определение и применение тегов](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.")
* [Наблюдаемость инфраструктуры](/docs/observe/infrastructure-observability "Инфраструктура приложений, включая облачные и контейнерные платформы, которые Dynatrace может мониторить")
