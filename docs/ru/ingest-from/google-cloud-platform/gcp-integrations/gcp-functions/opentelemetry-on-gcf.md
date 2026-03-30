---
title: Настройка мониторинга OpenTelemetry для Google Cloud Functions
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf
scraped: 2026-03-06T21:29:42.968498
---

* Latest Dynatrace
* How-to guide

Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов Google Cloud Functions.

Для этого Dynatrace предоставляет специфичные для языков пакеты, такие как `@dynatrace/opentelemetry-gcf` для Node.js, `dynatrace-opentelemetry-gcf` для Python и `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` для .NET, которые могут использоваться в сочетании со стандартными SDK и API OpenTelemetry.

## Предварительные требования

* Dynatrace версии 1.240+
* OneAgent версии 1.193+ для всех экземпляров OneAgent, участвующих в трассировке
* Перейдите в **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

## Установка

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Выберите метод конфигурации**](opentelemetry-on-gcf.md#choose-config-method "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Укажите конечную точку API Dynatrace**](opentelemetry-on-gcf.md#specify-endpoint "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Примените конфигурацию к вашей Google Cloud функции**](opentelemetry-on-gcf.md#apply-config "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Инструментируйте код функции**](opentelemetry-on-gcf.md#instrument-code "Мониторинг Google Cloud Functions с OpenTelemetry и Dynatrace.")

## Шаг 1 Выберите метод конфигурации

1. В Dynatrace выполните **Search** для приложения **Deploy OneAgent** и выберите его.
2. В разделе **Download Dynatrace OneAgent** выберите **Set up** > **Google Cloud Functions**.
3. На странице **Enable Monitoring for Google Cloud Functions** в разделе **How will you configure your Google Cloud Functions?** выберите предпочтительный метод из выпадающего меню. Убедитесь, что вы задали все свойства для выбранного метода, прежде чем копировать сгенерированные фрагменты конфигурации.

## Шаг 2 (необязательный) Укажите конечную точку API Dynatrace

Если вы не хотите использовать конечную точку Dynatrace по умолчанию, укажите пользовательскую конечную точку API Dynatrace, на которую вы хотите получать данные мониторинга.

Для уменьшения сетевой задержки обычно развёртывают Dynatrace ActiveGate рядом (в том же регионе) с Google Cloud функцией, которую вы хотите мониторить.

### Шаг 3 Примените конфигурацию к вашей Google Cloud функции

Конфигурация с помощью JSON-файла

Скопируйте JSON-фрагмент в файл с именем `dtconfig.json`, расположенный в корневой папке вашего развёртывания Google Cloud Functions.

Конфигурация с помощью переменных окружения

На странице **Enable Monitoring for Google Cloud Functions** в разделе **Use the following values to configure your monitored Google Cloud Functions** находится фрагмент со всеми необходимыми переменными окружения. Обязательно добавьте эти переменные окружения и их значения в конфигурацию вашей Google Cloud функции. Подробности см. в разделе [Использование переменных окружения](https://cloud.google.com/functions/docs/configuring/env-var).

## Шаг 4 Инструментируйте код функции

Добавление необходимых вызовов API для мониторинга вызовов функций через OpenTelemetry зависит от языка программирования и соответствующего дистрибутива OpenTelemetry:

* **Node.js:** Интеграция с Google Cloud Functions для Node.js
* **Python:** Интеграция с Google Cloud Functions для Python
* **Go:** Интеграция с Google Cloud Functions для GoLang
* **.NET:** Интеграция с Google Cloud Functions для .NET

## Известные ограничения

Интеграция Dynatrace с Google Cloud Functions не записывает IP-адреса исходящих HTTP-запросов. Если вызываемый сервис не мониторится с помощью Dynatrace OneAgent, это приводит к появлению **немониторируемых хостов**.

## Связанные темы

* Настройка Dynatrace в Google Cloud
* Матрица поддержки платформ и возможностей OneAgent
* [Мониторинг Google Cloud](https://www.dynatrace.com/technologies/google-cloud-monitoring/)
