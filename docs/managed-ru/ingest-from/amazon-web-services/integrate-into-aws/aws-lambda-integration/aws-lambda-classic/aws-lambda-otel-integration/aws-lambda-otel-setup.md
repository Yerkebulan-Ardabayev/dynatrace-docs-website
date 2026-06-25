---
title: Мониторинг AWS Lambda с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup
scraped: 2026-05-12T12:10:10.459384
---

# Мониторинг AWS Lambda с OpenTelemetry

# Мониторинг AWS Lambda с OpenTelemetry

* Практическое руководство
* Чтение: 3 мин
* Обновлено 22 января 2026 г.

Dynatrace предоставляет расширения для OpenTelemetry в AWS Lambda, такие как экспортёры, дополнительную инструментацию и вспомогательные библиотеки, чтобы упростить мониторинг AWS Lambda.

Список языкоспецифичных пакетов, которые можно использовать совместно с нативными OpenTelemetry SDK и API или с AWS Distribution for OpenTelemetry, см. в разделе [Трассировка .NET Lambda-функций](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Трассировка AWS Lambda-функций на runtime .NET").

## Предварительные условия

* Dynatrace версии 1.240+
* OneAgent версии 1.193+ для всех OneAgent-агентов, участвующих в трассировке
* В Dynatrace перейдите в **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

## Установка

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Выбор решения для мониторинга и метода конфигурации**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#choose-config-method "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry")[![Шаг 2 необязательный](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 необязательный")

**Указание API-эндпоинта Dynatrace**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#specify-endpoint "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Применение конфигурации к AWS Lambda-функции**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#apply-config "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Инструментация кода функции**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup#instrument-code "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry")

## Шаг 1 Выбор решения для мониторинга и метода конфигурации

Параметры конфигурации, относящиеся к Lambda layers, здесь не применяются.

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **AWS Lambda**.

3. На странице **Enable Monitoring for AWS Lambda Functions** установите **Select a runtime** в значение **.NET**.

   Параметр **Monitoring solution** автоматически выставляется в **AWS Lambda OpenTelemetry package**.
4. Установите **Select a configuration method** на предпочтительный метод конфигурации. Убедитесь, что заданы все свойства для выбранного метода конфигурации.

## Шаг 2 необязательный Указание API-эндпоинта Dynatrace Необязательно

Если вы не хотите использовать публичный API-эндпоинт Dynatrace по умолчанию, укажите кастомный API-эндпоинт Dynatrace, на который вы хотите получать данные мониторинга.

Чтобы уменьшить сетевую задержку, обычно Dynatrace ActiveGate разворачивают рядом (в том же регионе) с AWS Lambda-функцией, которую вы хотите мониторить.

### Шаг 3 Применение конфигурации к AWS Lambda-функции

Чтобы применить конфигурацию, выберите один из вариантов ниже в зависимости от выбранного метода конфигурации.

Configure with JSON file

Скопируйте JSON-сниппет в файл `dtconfig.json`, расположенный в корневой папке развёртывания вашей AWS Lambda Functions.

Configure with environment variables

На странице **Enable Monitoring for AWS Lambda Functions**, в блоке **Use the following values to define environment variables for your AWS Lambda function**, приведён сниппет со всеми необходимыми переменными окружения. Убедитесь, что вы добавили эти переменные окружения и их значения в конфигурацию вашей Lambda-функции. Подробнее см. [Configuring environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-config).

## Шаг 4 Инструментация кода функции

Добавление необходимых API-вызовов для мониторинга вызовов функции через OpenTelemetry зависит от языка и соответствующей дистрибуции OpenTelemetry.

Подробные инструкции для различных языков, поддерживаемых Dynatrace, см. в разделе [Трассировка .NET Lambda-функций](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Трассировка AWS Lambda-функций на runtime .NET").

## Известные ограничения

Инструментация Dynatrace не захватывает IP-адреса исходящих HTTP-запросов. Если вызванный сервис не мониторится Dynatrace, это приводит к **unmonitored hosts**.