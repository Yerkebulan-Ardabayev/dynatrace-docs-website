---
title: Ingest Microsoft Entra ID sign-in logs
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id
scraped: 2026-03-06T21:23:43.477598
---

# Приём логов входа Microsoft Entra ID

# Приём логов входа Microsoft Entra ID

* Latest Dynatrace
* Руководство
* Обновлено 25 августа 2025 г.

Принимайте логи входа Microsoft Entra ID и анализируйте их в Dynatrace.

## Начало работы

### Обзор

Далее вы узнаете, как принимать логи входа из вашего экземпляра [Microsoft Entra ID](https://www.microsoft.com/en-us/security/business/identity-access/microsoft-entra-id) в Grail и отслеживать их на платформе Dynatrace.

### Сценарии использования

С помощью полученных данных вы можете использовать платформу Dynatrace для мониторинга активности входов в Microsoft Entra ID и доступа к критически важным приложениям организации, выявляя аномалии и опережая потенциальные угрозы. Подробнее см. [Мониторинг подозрительной активности входов с помощью Dynatrace](../../use-cases/monitor-sign-in-activity.md "Анализ подозрительного и вредоносного поведения при входе с помощью Dynatrace.").

### Требования

* Включите пересылку логов входа Entra ID в Dynatrace одним из следующих способов:

  + **Вариант 1**: [Пересылка логов Azure](../../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md "Используйте пересылку логов Azure для приёма логов Azure.")
  + **Вариант 2**: [Нативный сервис Azure Dynatrace](../../../ingest-from/microsoft-azure-services/azure-platform/azure-native-integration.md "Настройка среды Dynatrace SaaS с использованием Azure Marketplace.")
* Разрешения:

  + Для запроса принятых логов: `storage:logs:read`.

## Активация и настройка

Чтобы настроить мониторинг логов входа Microsoft Entra ID, выполните следующие шаги.

1. Настройка встроенного процессора OpenPipeline

1. В Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** и выберите **Logs**.
2. Перейдите в **Pipelines** и выберите  **Pipeline**.
3. В разделе **Processing** выберите **Processor** > **Technology bundle** > **Azure Entra ID Audit Logs**.
4. Нажмите **Choose**.
5. Введите имя для вашего конвейера Azure и нажмите **Save**.
6. В разделе **Dynamic routing** выберите  **Dynamic route**.
7. Введите следующее условие соответствия:

   ```
   matchesValue(cloud.provider, "azure") AND



   matchesPhrase(content, "\"SignInLogs\"")
   ```
8. Выберите только что созданный конвейер, введите имя для динамического маршрута и нажмите **Add**.

2. Проверка конфигурации

Проверьте конфигурацию, выполнив следующий запрос в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитикой данных наблюдаемости в едином совместном настраиваемом рабочем пространстве."):

```
fetch logs



| filter cloud.provide == "azure"



AND isNotNull(audit.action)



AND isNotNull(authentication.is_multifactor)
```

3. Визуализация результатов с помощью нашего примера дашборда

1. Загрузите наш [пример дашборда с GitHub](https://dt-url.net/ur03wvb).
2. Откройте [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени."), выберите ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, затем выберите загруженный файл.

## Подробности

### Как это работает

Существуют два способа включить пересылку логов входа Entra ID в Dynatrace:

* **Вариант 1**: Через [пересылку логов Azure](../../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md "Используйте пересылку логов Azure для приёма логов Azure.")
* **Вариант 2**: Через [нативный сервис Azure Dynatrace](../../../ingest-from/microsoft-azure-services/azure-platform/azure-native-integration.md "Настройка среды Dynatrace SaaS с использованием Azure Marketplace.")

Подробности описаны ниже.

Через пересылку логов Azure

Через нативный сервис Azure Dynatrace

![mechanism1](https://dt-cdn.net/images/image-20250508-154953-2812-e26b3cab6c.png)

1. Логи принимаются в Dynatrace

1. Microsoft Entra ID непрерывно экспортирует логи входа в [Azure Event Hubs](https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-about).
2. Приложение [Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp) предварительно обрабатывает логи и отправляет их в Dynatrace, используя выделенную [конечную точку приёма логов](../../../dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs.md "Отправка пользовательских логов в Dynatrace через Log Monitoring API v2.") [OpenPipeline](../../../platform/openpipeline.md "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.").

2. Логи обрабатываются и сохраняются в Grail

1. Полученные данные сопоставляются с [семантическим словарём Dynatrace](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.").
2. Данные хранятся в [Grail](../../../platform/grail.md "Информация о том, какие данные Dynatrace можно запрашивать и как это делать.") в унифицированном формате в бакете по умолчанию `default_logs`. Подробнее см. [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, включающей бакеты, таблицы и представления.").

![mechanism2](https://dt-cdn.net/images/image-20250508-154902-2731-fc140d187d.png)

1. Логи принимаются в Dynatrace

Логи входа Microsoft Entra ID собираются, обрабатываются и отправляются в Dynatrace с помощью ресурса Dynatrace Native Service.

2. Логи обрабатываются и сохраняются в Grail

1. Полученные данные сопоставляются с [семантическим словарём Dynatrace](../../../semantic-dictionary/model/security-events.md#vulnerability-finding-events "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.").
2. Данные хранятся в [Grail](../../../platform/grail.md "Информация о том, какие данные Dynatrace можно запрашивать и как это делать.") в унифицированном формате в бакете по умолчанию `default_logs`. Подробнее см. [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, включающей бакеты, таблицы и представления.").

### Лицензирование и стоимость

Информацию о тарификации см. в [Events на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление Dynatrace Events на базе Grail в модели подписки Dynatrace Platform.").

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабирование обработки данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями семантического словаря, связанными с событиями безопасности.")
