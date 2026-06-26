---
title: Настройка мониторинга OpenTelemetry для Google Cloud Functions
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf
scraped: 2026-05-12T12:08:53.505820
---

# Настройка мониторинга OpenTelemetry для Google Cloud Functions

# Настройка мониторинга OpenTelemetry для Google Cloud Functions

* Практическое руководство
* Чтение: 2 мин
* Обновлено 31 марта 2025 г.

Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов Google Cloud Functions.

Для этого Dynatrace предоставляет пакеты для конкретных языков: [`@dynatrace/opentelemetry-gcf` для Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с OpenTelemetry для Node.js и Dynatrace."), [`dynatrace-opentelemetry-gcf` для Python](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Мониторинг Google Cloud Functions с OpenTelemetry для Python и Dynatrace.") и [`Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` для .NET](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Мониторинг Google Cloud Functions с OpenTelemetry для .NET и Dynatrace."), которые можно использовать совместно со стандартными OpenTelemetry SDK и API.

## Предварительные требования

* Dynatrace версии 1.240+
* OneAgent версии 1.193+ для всех OneAgent, участвующих в трассировке
* Перейдите в **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

## Установка

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Выберите метод конфигурации**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#choose-config-method "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Шаг 2 необязательный](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 необязательный")

**Укажите эндпоинт API Dynatrace**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#specify-endpoint "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Примените конфигурацию к функции Google Cloud**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#apply-config "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Инструментируйте код функции**](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf#instrument-code "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")

## Шаг 1 Выбор метода конфигурации

1. В Dynatrace выполните поиск приложения **Deploy OneAgent** и выберите его.
2. В разделе **Download Dynatrace OneAgent** выберите **Set up** > **Google Cloud Functions**.
3. На странице **Enable Monitoring for Google Cloud Functions**, в разделе **How will you configure your Google Cloud Functions?**, выберите нужный метод из выпадающего меню. Перед копированием сгенерированных фрагментов конфигурации убедитесь, что заданы все свойства для выбранного метода.

## Шаг 2 (необязательно) Укажите эндпоинт API Dynatrace

Если использовать стандартный публичный эндпоинт Dynatrace не нужно, укажите пользовательский эндпоинт API Dynatrace для получения данных мониторинга.

Для снижения сетевой задержки рекомендуется развёртывать Dynatrace ActiveGate рядом с отслеживаемой функцией Google Cloud (в том же регионе).

### Шаг 3 Применение конфигурации к функции Google Cloud

Конфигурация с помощью JSON-файла

Скопируйте фрагмент JSON в файл `dtconfig.json`, расположенный в корневой папке развёртывания Google Cloud Functions.

Конфигурация с помощью переменных окружения

На странице **Enable Monitoring for Google Cloud Functions**, в разделе **Use the following values to configure your monitored Google Cloud Functions**, содержится фрагмент со всеми необходимыми переменными окружения. Обязательно добавьте эти переменные и их значения в конфигурацию функции Google Cloud. Подробнее см. [Using environment variables](https://cloud.google.com/functions/docs/configuring/env-var).

## Шаг 4 Инструментирование кода функции

Добавление необходимых API-вызовов для мониторинга вызовов функции через OpenTelemetry зависит от языка и соответствующего дистрибутива OpenTelemetry:

* **Node.js:** [Интеграция на Google Cloud Functions Node.js](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Мониторинг Google Cloud Functions с OpenTelemetry для Node.js и Dynatrace.")
* **Python:** [Интеграция на Google Cloud Functions Python](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-python "Мониторинг Google Cloud Functions с OpenTelemetry для Python и Dynatrace.")
* **Go:** [Интеграция на Google Cloud Functions GoLang](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-go "Мониторинг Google Cloud Functions с OpenTelemetry для Go и Dynatrace.")
* **.NET:** [Интеграция на Google Cloud Functions .NET](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet "Мониторинг Google Cloud Functions с OpenTelemetry для .NET и Dynatrace.")

## Известные ограничения

Интеграция Dynatrace для Google Cloud Functions не фиксирует IP-адреса исходящих HTTP-запросов. Если вызываемый сервис не отслеживается Dynatrace OneAgent, это приводит к появлению **немониторируемых хостов**.

## Связанные темы

* [Настройка Dynatrace в Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживает OneAgent на различных операционных системах и платформах.")
* [Google Cloud monitoring](https://www.dynatrace.com/technologies/google-cloud-monitoring/)