---
title: Настройка уведомлений мониторинга с Azure Monitor alerts
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts
scraped: 2026-05-12T11:38:14.632026
---

# Настройка уведомлений мониторинга с Azure Monitor alerts

# Настройка уведомлений мониторинга с Azure Monitor alerts

* Практическое руководство
* Чтение: 5 мин
* Обновлено 28 января 2026 г.

После [настройки интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Настройка и конфигурирование мониторинга Azure в Dynatrace.") можно приступить к настройке уведомлений мониторинга с Azure Monitor alerts.

Azure Monitor alerts, единый центр уведомлений для всех типов важных условий, обнаруженных в данных мониторинга Azure. Интеграция Azure Monitor alerts позволяет принимать оповещения, которые автоматически преобразуются в события, используемые Davis AI для более глубокого анализа.

Чтобы настроить уведомления мониторинга с Azure Monitor alerts, выполните следующие шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Создание API-токена**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-1 "Интеграция с Azure Monitor alerts и поддерживаемые типы оповещений Azure Monitor")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка одного или нескольких выделенных ActiveGates**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-2 "Интеграция с Azure Monitor alerts и поддерживаемые типы оповещений Azure Monitor")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Настройка Azure Monitor alerts через webhook**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-3 "Интеграция с Azure Monitor alerts и поддерживаемые типы оповещений Azure Monitor")

## Шаг 1. Создание API-токена

Чтобы создать API-токен

1. Откройте **Access Tokens**.
2. Нажмите **Generate new token**.
3. Введите имя для токена.
4. Найдите и выберите область **Ingest metrics**.
5. Нажмите **Generate token**.
6. Нажмите **Copy**, чтобы скопировать созданный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Одному токену можно назначить несколько разрешений или создать несколько токенов с разными уровнями доступа и использовать их соответствующим образом. Ознакомьтесь с политиками безопасности своей организации для получения рекомендаций.

## Шаг 2. Настройка одного или нескольких выделенных ActiveGates

ActiveGate, выделенный для приёма Azure Monitor alerts, не обязан совпадать с ActiveGate, выполняющим интеграцию с Azure Monitor. Это может быть любой другой [ActiveGate с поддержкой мониторинга Azure](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований.").

Чтобы настроить выделенный ActiveGate для приёма Azure Monitor alerts:

1. Настройте действительный TLS-сертификат (не самоподписанный) для ActiveGate для обмена данными по HTTPS. Убедитесь, что корневой сертификат принят Azure. Подробнее см. в разделе [о настройке пользовательского SSL-сертификата для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").
2. Добавьте следующие строки в файл `custom.properties` своего ActiveGate и перезапустите ActiveGate после применения конфигурации.

   ```
   [azure_monitoring]



   event_servlet = true
   ```
3. Предоставьте ActiveGate доступ к IP-адресам источника Azure Monitor alerts.

Подробнее см. в разделе [диапазоны IP-адресов источника](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) в документации Azure.

## Шаг 3. Настройка Azure Monitor alerts через webhook

В настоящее время события/оповещения, поступающие через webhook Azure Monitor alerts, не потребляют DDU, хотя в будущем это может измениться.

Azure Monitor alerts, принимаемые через webhooks, настраиваются в правилах оповещений Azure.
Оповещения сопоставляются с наиболее близкой известной сущностью. Это означает, что они либо сопоставляются с соответствующей сущностью ресурса Azure, либо, в качестве запасного варианта, с подпиской Azure для данного ресурса.

Чтобы настроить Azure Monitor alerts через webhook, нужно создать правило оповещения и группу действий, которая будет запускать webhook.

1. В Azure Portal откройте **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.
2. Выберите **Scope** > **Select scope**.
3. Отфильтруйте и выберите ресурс для мониторинга, затем нажмите **Done**.
4. Выберите **Condition** > **Add condition**.
5. Отфильтруйте, выберите и настройте тип сигнала, который будет запускать оповещение.
6. Выберите **Next: Actions** > **Create action group**.
7. Введите **subscription**, которая будет управлять развёрнутыми ресурсами и расходами, **resource group**, к которой относится подписка, а также имя (и отображаемое имя) для **action group**.
8. Выберите **Actions** и введите следующие значения:

   * Для **Action type** выберите **Webhook** и введите имя.
   * Для **URI** введите `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, заменив `<YOUR_ACTIVEGATE_ADDRESS>` и `<YOUR_API_TOKEN>` своими значениями.
9. Оставьте общую схему оповещений отключённой и нажмите **OK**.

Общая схема оповещений не поддерживается.

10. Нажмите **Review and create** > **Create**.

После создания группы действий её можно просмотреть и изменить в **Alerts** > **Action groups**.

Подробнее см. в разделе [Правила Webhook в документации Azure](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).

## Типы оповещений

Поддерживаются следующие типы оповещений.

### Метрические оповещения

Метрические оповещения дополняют интеграцию Dynatrace с метриками Azure Monitor.

Метрические оповещения позволяют получать события на основе метрик без необходимости передавать метрики в Dynatrace. Это помогает снизить нагрузку на API и сеть, особенно в случаях, когда метрика не нужна (например, для построения графиков).

Тип события определяется на основе **Severity** оповещения:

* **Sev-0 (Critical)**: `ERROR_EVENT`
* **Sev-1 (Error)**: `PERFORMANCE_EVENT`
* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`
* **Default (Informational)**: `CUSTOM_ANNOTATION`

### Оповещения журнала активности

Dynatrace поддерживает три типа уведомлений об активности.

#### Работоспособность ресурса в журнале активности

Тип события определяется на основе **Level** серьёзности:

* **Critical**: `AVAILABILITY_EVENT`
* **Error**: `AVAILABILITY_EVENT`
* **Default**: `CUSTOM_ANNOTATION`

Подробнее см. в разделе [Настройка оповещений о работоспособности ресурса с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) в документации Azure.

#### Работоспособность сервиса в журнале активности

Тип события определяется на основе **IncidentType**

* Case **ActionRequired**: `ERROR_EVENT`
* Case **Incident** or **Security**:

  + Level **Error**: `ERROR_EVENT`
  + Level **Info** or **Warning**: `CUSTOM_ANNOTATION`
* Case **Maintenance** or **Information**: `CUSTOM_ANNOTATION`

Анализ первопричины

События с `Properties.stage=RCA` пропускаются. Стадия RCA для работоспособности сервиса не поддерживается.

Подробнее см. в разделе [Создание оповещений журнала активности об уведомлениях сервиса с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) в документации Azure.

#### Административные записи журнала активности

* **Default**: `CUSTOM_ANNOTATION`

## Связанные темы

* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")
* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Узнайте о различных категориях событий и поддерживаемых типах событий, их уровнях серьёзности и логике их возникновения.")