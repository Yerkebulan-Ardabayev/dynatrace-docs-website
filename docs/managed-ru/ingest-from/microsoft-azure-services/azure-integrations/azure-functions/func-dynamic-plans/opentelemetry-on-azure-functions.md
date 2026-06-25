---
title: Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions
scraped: 2026-05-12T12:04:42.016451
---

# Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption

# Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption

* Практическое руководство
* Чтение: 3 мин
* Обновлено 31 марта 2025 г.

Dynatrace версии 1.240+ OneAgent версии 1.193+

Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов Azure Functions.
Для этого Dynatrace предоставляет пакеты для конкретных языков, например [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` для .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace."), которые можно использовать совместно со стандартными SDK и API OpenTelemetry.

## Установка

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Активация функции OneAgent**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#oneagent-feature "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Выбор метода настройки**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#choose-config-method "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3 необязательный")

**Указание эндпоинта Dynatrace API**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#specify-endpoint "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Применение настроек к приложению функции**](#apply-config)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Инструментирование кода функции**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#instrument-code "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace.")

### Шаг 1. Активация функции OneAgent

Откройте **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

### Шаг 2. Выбор метода настройки

1. В Dynatrace введите **Deploy OneAgent** в строке **Search** и выберите приложение.
2. В разделе **Download Dynatrace OneAgent** выберите **Set up** > **Azure Functions**.
3. На странице **Enable Monitoring for Azure Functions** в разделе **How will you configure your Azure Functions?** выберите нужный метод настройки из выпадающего меню.

### Шаг 3 (необязательно). Указание эндпоинта Dynatrace API

Если не нужно использовать стандартный публичный эндпоинт Dynatrace, укажите пользовательский эндпоинт Dynatrace API для получения данных мониторинга.

Для снижения сетевой задержки рекомендуется развернуть Dynatrace ActiveGate рядом с монитируемой Azure Function (в том же регионе).

### Шаг 4. Применение настроек к приложению функции

Чтобы применить настройки, выберите один из вариантов ниже в зависимости от метода настройки.

Настройка с помощью файла JSON

Настройка с помощью переменных окружения

Скопируйте фрагмент JSON в файл `dtconfig.json`, расположенный в корневой папке развёртывания Azure Functions.

На странице **Enable Monitoring for Azure Functions** в разделе **Use the following values to configure your monitored Azure Functions** содержится фрагмент со всеми необходимыми переменными окружения. Добавьте эти переменные и их значения в настройки приложения функции:

1. В Azure Portal перейдите к приложению функции.
2. В **Settings** выберите **Configuration**.
3. Отредактируйте существующие переменные окружения, чтобы их имена и значения совпадали с указанными в [Dynatrace](#variables-dynatrace), или, если в приложении функции нет существующих переменных, выберите **New application setting** и добавьте имена и значения всех переменных из [Dynatrace](#variables-dynatrace).

Настройки, не указанные в Dynatrace, оставьте без изменений.

### Шаг 5. Инструментирование кода функции

Добавление необходимых вызовов API для мониторинга вызовов функций через OpenTelemetry зависит от используемого языка и соответствующего дистрибутива OpenTelemetry:

* **.NET (C#):** [Трассировка Azure Functions на .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace.")
* **Node.js (Javascript):** [Трассировка Azure Functions на Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Мониторинг Azure Functions с OpenTelemetry для Node.js и Dynatrace.")
* **Python:** [Трассировка Azure Functions на Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Мониторинг Azure Functions с OpenTelemetry для Python и Dynatrace.")

## Известные ограничения

Интеграция Dynatrace с Azure Functions не захватывает IP-адреса исходящих HTTP-запросов. Если вызываемый сервис не отслеживается через Dynatrace OneAgent, это приводит к появлению **неотслеживаемых хостов**.

## Связанные темы

* [Мониторинг Azure Functions на App Service Plan для Windows](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions через расширение Azure site extension.")
* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")