---
title: Service Detection v1
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1
scraped: 2026-05-12T11:18:39.429314
---

# Service Detection v1

# Service Detection v1

* Overview
* 1-min read
* Updated on Aug 06, 2025

Service Detection v1 (SDv1) — это механизм обнаружения сервисов для сервисов, инструментированных OneAgent, в Dynatrace.

Он предоставляет возможности обнаружения на основе типов сервисов, специфичных для технологий, каждый из которых имеет собственные правила обнаружения и параметры настройки. Эти возможности включают:

* **Service type recognition**: Идентификация различных типов сервисов.
* **Custom detection rules**: Тонкая настройка способа обнаружения и группировки сервисов.
* **Request naming**: Отслеживание ключевых бизнес-транзакций.
* **Failure detection**: Определение ошибок и проблемных запросов.

Для поддержки OpenTelemetry см. [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Узнайте, как обнаруживать, именовать и разбивать сервисы из span'ов OpenTelemetry и OneAgent."), который поддерживает обнаружение сервисов через атрибуты ресурсов OTel.

## Типы сервисов

SDv1 может обнаруживать следующие типы сервисов:

* **Web request services**: Приложения, развёрнутые через веб-серверы или веб-контейнеры.
* **Web services**: Как определено WSDL.
* **Database services**: Приложения, выполняющие запросы к базам данных.
* **Messaging services**: Слушатели очередей и тем в приложениях.
* **Remoting services**: RMI и RPC-коммуникации.
* **Background activity services**: Потоки, работающие в фоновом режиме.
* **Custom services**: Пользовательская инструментация для нестандартных технологий.

## Параметры настройки

С помощью SDv1 можно настроить описанные ниже параметры.

### Правила обнаружения сервисов

* Объединение приложений в один сервис.
* Разделение сервисов на основе шаблонов URL.
* Создание правил для немониторируемых хостов.
* Исправление проблем с именованием веб-серверов.

Подробности см. в разделе [Правила обнаружения сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Используйте правила обнаружения для настройки и улучшения автоматического обнаружения ваших сервисов.").

### Именование сервисов

* Встроенные правила определяют именование «из коробки».
* Пользовательские правила именования сервисов позволяют создавать собственные стандарты именования.
* Форматы имён сервисов с заполнителями для согласованных соглашений об именовании.

Дополнительные сведения см. в разделе [Правила именования сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Используйте правила именования для настройки и улучшения автоматического именования ваших сервисов.").

### Именование запросов

* Определение способа отображения запросов в вашем окружении.
* Создание понятных имён для бизнес-транзакций.
* Отслеживание операций на детальном уровне.

Подробности см. в разделе [Настройка именования запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Настройте именование запросов и определите операции, предлагаемые вашими сервисами.").

### Обнаружение сбоев

* Настройка параметров обнаружения ошибок глобально или для отдельных сервисов.
* Определение пользовательских правил ошибок.
* Обработка HTTP-ошибок и исключений в соответствии с вашими потребностями.

Дополнительные сведения см. в разделе [Настройка обнаружения сбоев сервиса](/managed/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Узнайте, какие типы ошибок сервисов Dynatrace обнаруживает автоматически, и узнайте, как настроить параметры обнаружения сбоев в соответствии с вашими конкретными требованиями.").

## Связанные темы

* [Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Узнайте, как обнаруживать, именовать и разбивать сервисы из span'ов OpenTelemetry и OneAgent.")
* [API обнаружения сервисов](/managed/dynatrace-api/configuration-api/service-api/detection-rules "Узнайте, что предлагает Dynatrace API конфигурации правил обнаружения сервисов.")
* [Обнаружение группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения группы процессов.")