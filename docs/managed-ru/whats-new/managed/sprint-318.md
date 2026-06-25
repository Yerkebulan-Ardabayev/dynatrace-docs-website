---
title: Заметки о выпуске Dynatrace Managed версии 1.318
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-318
scraped: 2026-05-12T11:08:01.177938
---

# Заметки о выпуске Dynatrace Managed версии 1.318

# Заметки о выпуске Dynatrace Managed версии 1.318

* Заметки о выпуске
* 10-min read
* Updated on Aug 19, 2025
* Rollout start on Jul 7, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.318.

## Новые функции и улучшения

Application Observability | Service detection

### Настраиваемые сервисы и конечные точки для приложений с Service Detection v2 (SDv2)

Service Detection v2 (SDv2), развитие Service Detection v1, позволяет настраивать сервисы, конечные точки и обнаружение сбоев в соответствии с бизнес-потребностями. SDv2 гармонизирует сервисы OneAgent и OpenTelemetry с целью обеспечения одинаковой функциональности для всех данных трасс.

В данном первоначальном выпуске поддерживаются сервисы OpenTelemetry, а Adobe Experience Manager поддерживается как первая технология OneAgent.

![Adobe Experience Manager](https://dt-cdn.net/images/adobe-experience-manager-1737-7f7de41e91.png)

Adobe Experience Manager

SDv2 работает на основе единого набора правил, основанных на атрибутах ресурсов. Базовые правила настраиваемы, и для добавления контекста к сервисам можно использовать любой атрибут ресурса.

SDv2 также вводит концепцию конечных точек, представляющих собой развитие ключевых требований. Конечные точки позволяют понять взаимодействия приложений и обнаруживать аномалии с использованием базовых метрик.

![Настройки Service Detection v2](https://dt-cdn.net/images/sdv2-config-1609-2032994dc6.png)

Настройки Service Detection v2

Подробнее о SDv2 см. в разделе [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

Platform

### Учитывающий стойки статус работоспособности в premium HA

Для кластеров Managed новее версии 1.302 в развёртывании Premium High Availability отработка отказа DC запускается только в том случае, если неработоспособные узлы охватывают более одной стойки.

Application Observability | Distributed Traces

### Улучшенная визуализация атрибутов в представлении отдельной трассировки

Теперь атрибуты используют всё доступное горизонтальное пространство экрана до тех пор, пока пространство не будет полностью занято или не будут отображены все атрибуты.

![Улучшенная визуализация атрибутов для представления отдельной трассировки](https://dt-cdn.net/images/solution-proposal-1-b0f77a2221.gif)

Улучшенная визуализация атрибутов для представления отдельной трассировки

Log Monitoring

### Сбор и анализ структурированных данных из журналов событий Windows

OneAgent версии 1.317+

Теперь можно собирать структурированные данные из журналов событий Windows и анализировать их с помощью Dynatrace Managed. Для включения перейдите в **Settings** > **Log Monitoring** > **Log module feature flags** и включите **Support for structured data in Windows Event Logs**.

При включении структурированные данные собираются из журналов событий Windows из ветки «User Data» или, если она недоступна, из ветки «Event Data» и её подветок. Собранные данные передаются в виде атрибутов вместе с записанным содержимым.

Имена атрибутов формируются на основе доступной информации, например имён тегов или значения поля имени. Если имена тегов повторяются, а поле имени пустое, к имени тега добавляется порядковый номер.

Подветки без значений и теги с меткой «Binary» опускаются.

Settings

### Исправлено некорректное расположение кнопок при настройке определений Java-сервисов

Исправлена проблема, при которой кнопки отображались за пределами экрана при настройке определений Java-сервисов на определённых размерах дисплея.

Platform

### Улучшенная стабильность восстановления Cassandra

При ручном выполнении операции восстановления Cassandra по какой-либо причине теперь она выполняется таблица за таблицей во избежание слишком большой нагрузки на весь кластер.

Platform

### Обновление Cassandra до версии 4.1.9

В рамках данного выпуска узлы Cassandra обновляются до версии 4.1.9 для получения исправлений ошибок и уязвимостей безопасности.

Вмешательство пользователя или время простоя не требуются; обновление должно выполняться посредством поэтапного (rolling) обновления в рамках обычных обновлений версии.

Digital Experience | Synthetic

### Прекращение поддержки и замена метрик состояния работоспособности Location и Node

Следующие метрики состояния работоспособности Location и Node объявлены устаревшими и заменены новыми метриками самомониторинга.

| Устаревшая метрика | Заменяющая метрика |
| --- | --- |
| `builtin:synthetic.location.health_status` | `dsfm:synthetic.location.health_status` |
| `builtin:synthetic.location.node.component.healthStatus` | `dsfm:synthetic.location.node.component.health_status` |

Licensing

### Сглажен граничный случай в классическом лицензировании

Версия кластера 1.318.84+: для редких случаев классического лицензирования с мониторингом только приложений изменено требование в пользу клиентов. Система выставления счетов за единицы хоста теперь несколько раз пытается запросить лимит памяти PaaS для кратко существующих хостов, прежде чем использовать память хоста.

## Несовместимые изменения

Platform | Mission Control

### Обновление шифров Mission Control

Список шифров Mission Control сокращён, принимаются только следующие:

```
TLS_AES_128_GCM_SHA256
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
ECDHE-ECDSA-AES128-GCM-SHA256
ECDHE-RSA-AES128-GCM-SHA256
ECDHE-ECDSA-AES256-GCM-SHA384
ECDHE-RSA-AES256-GCM-SHA384
```

Убедитесь, что все устанавливаемые подключения к Mission Control поддерживают эти шифры. Если они не поддерживают перечисленные шифры, подключение к Mission Control установлено не будет.

Infrastructure Observability | Hosts

### Улучшенное разбиение процессов Oracle Net Listener по имени слушателя

Исправлена проблема, при которой процессы Oracle Net Listener не разбивались по имени, когда службы ОС не собирались на Windows. Кроме того, теперь используется правильное имя слушателя вместо имени домашнего каталога Oracle.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.317](/managed/whats-new/dynatrace-api/sprint-317 "Changelog for Dynatrace API version 1.317")
* [Журнал изменений Dynatrace API версии 1.318](/managed/whats-new/dynatrace-api/sprint-318 "Changelog for Dynatrace API version 1.318")

## Поддержка операционных систем

### Предстоящие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление поставщика](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление поставщика](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление поставщика](https://aws.amazon.com/linux/)

### Прошедшие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы больше не поддерживаются с 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Объявление поставщика](https://wiki.debian.org/DebianReleases)

## Исправленные ошибки