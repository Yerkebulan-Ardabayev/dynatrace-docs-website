---
title: Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions
scraped: 2026-03-06T21:27:46.855290
---

# Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption

# Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Mar 31, 2025

Dynatrace version 1.240+ OneAgent version 1.193+

Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов Azure Functions.
Для этого Dynatrace предоставляет языково-специфичные пакеты, такие как [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` для .NET](opentelemetry-on-azure-functions-dotnet.md "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace."), которые можно использовать в сочетании с SDK и API OpenTelemetry по умолчанию.

## Установка

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Активируйте функцию OneAgent**](opentelemetry-on-azure-functions.md#oneagent-feature "Мониторинг Azure Functions на плане consumption с OpenTelemetry и Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Выберите метод конфигурации**](opentelemetry-on-azure-functions.md#choose-config-method "Мониторинг Azure Functions на плане consumption с OpenTelemetry и Dynatrace.")[![Шаг 3 (необязательный)](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3 (необязательный)")

**Укажите конечную точку API Dynatrace**](opentelemetry-on-azure-functions.md#specify-endpoint "Мониторинг Azure Functions на плане consumption с OpenTelemetry и Dynatrace.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Примените конфигурацию к вашему приложению-функции**](#apply-config)[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Инструментируйте код функции**](opentelemetry-on-azure-functions.md#instrument-code "Мониторинг Azure Functions на плане consumption с OpenTelemetry и Dynatrace.")

### Шаг 1: Активируйте функцию OneAgent

Перейдите в **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

### Шаг 2: Выберите метод конфигурации

1. В Dynatrace используйте **Search**, чтобы найти приложение **Deploy OneAgent**, и выберите его.
2. В разделе **Download Dynatrace OneAgent** выберите **Set up** > **Azure Functions**.
3. На странице **Enable Monitoring for Azure Functions** в разделе **How will you configure your Azure Functions?** выберите предпочтительный метод конфигурации из выпадающего меню.

### Шаг 3 (необязательный): Укажите конечную точку API Dynatrace

Если вы не хотите использовать публичную конечную точку Dynatrace по умолчанию, укажите пользовательскую конечную точку API Dynatrace, на которую вы хотите получать данные мониторинга.

Для снижения сетевой задержки обычно развёртывается ActiveGate Dynatrace близко к (в том же регионе, что и) Azure Function, которую вы хотите мониторить.

### Шаг 4: Примените конфигурацию к вашему приложению-функции

Чтобы применить конфигурацию, выберите один из вариантов ниже в зависимости от вашего метода конфигурации.

Конфигурация с JSON-файлом

Конфигурация с переменными окружения

Скопируйте JSON-фрагмент в файл с именем `dtconfig.json`, расположенный в корневой папке вашего развёртывания Azure Functions.

На странице **Enable Monitoring for Azure Functions** в разделе **Use the following values to configure your monitored Azure Functions** находится фрагмент со всеми необходимыми переменными окружения. Обязательно добавьте эти переменные окружения и их значения в конфигурацию вашего приложения-функции:

1. В Azure Portal перейдите к вашему приложению-функции.
2. В разделе **Settings** выберите **Configuration**.
3. Отредактируйте существующие переменные окружения так, чтобы имена и значения соответствовали указанным в [Dynatrace](#variables-dynatrace), или, если у вашего приложения-функции нет существующих переменных, выберите **New application setting** и добавьте имена и значения для всех переменных из [Dynatrace](#variables-dynatrace).

Оставьте настройки, не указанные Dynatrace, без изменений.

### Шаг 5: Инструментируйте код функции

Добавление необходимых вызовов API для мониторинга вызовов функций через OpenTelemetry зависит от языка и его соответствующего дистрибутива OpenTelemetry:

* **.NET (C#):** [Трассировка Azure Functions, написанных на .NET](opentelemetry-on-azure-functions-dotnet.md "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace.")
* **Node.js (Javascript):** [Трассировка Azure Functions, написанных на Node.js](opentelemetry-on-azure-functions-nodejs.md "Мониторинг Azure Functions с OpenTelemetry для Node.js и Dynatrace.")
* **Python:** [Трассировка Azure Functions, написанных на Python](opentelemetry-on-azure-functions-python.md "Мониторинг Azure Functions с OpenTelemetry для Python и Dynatrace.")

## Известные ограничения

Интеграция Dynatrace Azure Functions не захватывает IP-адреса исходящих HTTP-запросов. Если вызываемый сервис не мониторится с помощью Dynatrace OneAgent, это приведёт к появлению **немониторируемых хостов**.

## Связанные темы

* [Мониторинг Azure Functions на плане App Service для Windows](../integrate-oneagent-on-azure-functions.md "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions с использованием расширения сайта Azure.")
* [Настройка Dynatrace в Microsoft Azure](../../../../microsoft-azure-services.md "Настройте и сконфигурируйте мониторинг для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](../../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
