---
title: Экспорт данных лицензии
source: https://docs.dynatrace.com/managed/managed-cluster/operation/export-license-data
scraped: 2026-05-12T11:24:07.831735
---

# Экспорт данных лицензии

# Экспорт данных лицензии

* Updated on Nov 25, 2025

Экспорт данных лицензии позволяет экспортировать необработанные сведения о почасовом использовании лицензии во всех ваших средах за указанный период. Обратите внимание, что это использование не соответствует оплачиваемому потреблению в рамках [классического лицензирования Dynatrace](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."). Для развёртываний Managed в офлайн-режиме он служит входными данными для биллинга.

Для экспорта данных лицензии:

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Licensing** и выберите **Export license data**.
3. Задайте временной период для экспорта.
4. Выберите **Export**.

Экспортированный ZIP-файл включает:

* ZIP-файл с файлами данных лицензии в формате JSON
* Файл подписи
* Файл журнала с информацией о создании и экспорте ZIP-файла

Файлы JSON содержат следующую информацию:

### ConsumptionExport

| Название свойства | Описание |
| --- | --- |
| clusterUuid | Идентификатор кластера |
| timeFrameStart | Начало временного периода экспорта данных потребления |
| timeFrameEnd | Конец временного периода экспорта данных потребления |
| environmentBillingEntries | Список объектов **EnvironmentUsage** |

### EnvironmentUsage

| Название свойства | Описание |
| --- | --- |
| environmentUuid | Идентификатор среды |
| visits | Количество потреблённых пользовательских сеансов |
| mobileSessions | Количество потреблённых мобильных пользовательских сеансов |
| totalRUMUserPropertiesUsed | Количество заданных свойств пользовательских сеансов |
| newProblems | Не используется, устарело |
| hostUsages | Список объектов **HostUsage** |
| downloads | Не используется, устарело |
| syntheticUsages | Не используется, устарело |
| syntheticBillingUsage | Список объектов **SyntheticUsage** |
| customMetrics | Список объектов **CustomMetricsUsage** |
| davisDataUnits | Список объектов **DDUUsage** |
| trial | Признак тестовой среды |
| logStorageUsageBytes | Использование хранилища Log Monitoring в байтах |
| logUploadVolumeBytes | Объём загрузки Log Monitoring в байтах |
| sessionReplays | Количество потреблённых записей пользовательских сеансов |
| mobileSessionReplays | Количество потреблённых записей мобильных пользовательских сеансов |

### HostUsage

| Название свойства | Описание |
| --- | --- |
| osiId | Идентификатор кластера |
| hostName | Не используется |
| hostCategory | Устарело |
| agentUsages | Список объектов **AgentUsage** |
| infrastructureOnly | Признак работы в режиме Infrastructure Monitoring |
| paas | Признак приложения PaaS |
| passMemoryLimit | Ограничение RAM приложения PaaS в байтах; для не-PaaS приложений — null |
| vendorTypeId | Идентификатор вендора PaaS. Для не-PaaS приложений — null |
| hostMemoryBytes | Объём RAM хоста в байтах |
| premiumLogAnalytics | Признак включения Premium Log Monitoring на хосте |
| hasContainers | Признак хоста виртуализации (например, Docker-хоста) |

### AgentUsage

| Название свойства | Описание |
| --- | --- |
| networkTraffic | Не используется, устарело |
| agentId | Уникальный идентификатор модуля OneAgent |
| agentTypeId | Идентификатор типа модуля OneAgent; 1 для модуля ОС |
| agentUsageRecords | Список объектов **AgentUsageRecord** |

### AgentUsageRecord

| Название свойства | Описание |
| --- | --- |
| startTime | Время начала работы модуля OneAgent в рамках временного периода ConsumptionExport |
| endTime | Время окончания работы агента в рамках временного периода ConsumptionExport |

### SyntheticUsage

| Название свойства | Описание |
| --- | --- |
| monitorTypeId | Идентификатор типа Synthetic-монитора; 1 для браузерного, 2 для HTTP |
| testId | Уникальный идентификатор Synthetic-монитора |
| publicExecutions | Количество выполнений из публичных местоположений |
| privateExecutions | Количество выполнений из приватных местоположений |

### CustomMetricsUsage

| Название свойства | Описание |
| --- | --- |
| source | Имя источника определения пользовательской метрики (например, `JMX`) |
| total | Количество определений пользовательских метрик |

### DDUUsage

| Название свойства | Описание |
| --- | --- |
| pool | Название пула DDU (например, «Metrics») |
| total | Количество потреблённых единиц данных Davis (Davis Data Units) |