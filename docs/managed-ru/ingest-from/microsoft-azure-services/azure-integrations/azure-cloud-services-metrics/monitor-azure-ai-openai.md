---
title: Azure OpenAI
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-ai-openai
scraped: 2026-05-12T11:27:17.792778
---

# Azure OpenAI

# Azure OpenAI

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 25 марта 2024 г.

Dynatrace версии 1.272+Environment ActiveGate версии 1.195+

Dynatrace получает метрики из Azure Metrics API для OpenAI. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/azure-enable-service-monitoring "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса предусмотрен предустановленный дашборд, он появится на вашей странице **Dashboards** с набором всех рекомендуемых метрик. Искать конкретные дашборды можно с помощью фильтрации по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.  
Чтобы убрать дашборд из списка, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

Clone hide azure

## Доступные метрики

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| SuccessRate | Уровень доступности | API name, Operation name, Ratelimit key, Region | Процент | Применимо |
| BlockedCalls | Заблокированные вызовы | API name, Operation name, Ratelimit key, Region | Количество | Применимо |
| ClientErrors | Клиентские ошибки | API name, Operation name, Ratelimit key, Region | Количество | Применимо |
| DataIn | Входящие данные | API name, Operation name, Region | Байт | Применимо |
| DataOut | Исходящие данные | API name, Operation name, Region | Байт | Применимо |
| GeneratedTokens | Количество сгенерированных токенов завершения | API name, Model deployment name, Model name, Region, Usage channel | Количество | Применимо |
| Latency | Задержка | API name, Operation name, Ratelimit key, Region | Миллисекунда | Применимо |
| FineTunedTrainingHours | Обработанные часы тонкой настройки обучения | API name, Model deployment name, Model name, Region, Usage channel | Количество | Применимо |
| TokenTransaction | Обработанные токены инференса | API name, Model deployment name, Model name, Region, Usage channel | Количество | Применимо |
| ProcessedPromptTokens | Обработанные токены промпта | API name, Model deployment name, Model name, Region, Usage channel | Количество | Применимо |
| Ratelimit | Ограничение частоты запросов | Ratelimit key, Region | Количество | Применимо |
| ServerErrors | Количество ошибок сервера | API name, Operation name, Ratelimit key, Region | Количество | Применимо |
| SuccessfulCalls | Количество успешных вызовов | API name, Operation name, Ratelimit key, Region | Количество | Применимо |
| TotalCalls | Количество вызовов | API name, Operation name, Ratelimit key, Region | Количество | Применимо |
| TotalErrors | Количество ошибок | API name, Operation name, Ratelimit key, Region | Количество | Применимо |