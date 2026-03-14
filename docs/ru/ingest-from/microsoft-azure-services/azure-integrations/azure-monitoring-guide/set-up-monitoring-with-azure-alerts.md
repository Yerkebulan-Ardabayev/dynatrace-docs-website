---
title: Настройка уведомлений мониторинга с помощью Azure Monitor alerts
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts
scraped: 2026-03-06T21:32:17.117243
---

# Настройка уведомлений мониторинга с помощью оповещений Azure Monitor


* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 5 мин
* Обновлено 28 января 2026 г.

После [настройки интеграции Azure Monitor](../azure-monitoring-guide.md "Настройка и конфигурация мониторинга Azure в Dynatrace.") вы можете приступить к настройке уведомлений мониторинга с помощью оповещений Azure Monitor.

Оповещения Azure Monitor — это единый центр уведомлений для всех типов важных условий, обнаруженных в данных мониторинга Azure. Интеграция оповещений Azure Monitor позволяет получать оповещения, которые автоматически преобразуются в события, используемые Dynatrace Intelligence для более глубокого анализа.

Чтобы настроить уведомления мониторинга с помощью оповещений Azure Monitor, выполните следующие шаги.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание API-токена**](set-up-monitoring-with-azure-alerts.md#step-1 "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка одного или нескольких выделенных ActiveGate**](set-up-monitoring-with-azure-alerts.md#step-2 "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка оповещений Azure Monitor через вебхук**](set-up-monitoring-with-azure-alerts.md#step-3 "Интеграция с оповещениями Azure Monitor и поддерживаемые типы оповещений Azure Monitor")

## Шаг 1 Создание API-токена

Чтобы сгенерировать API-токен

1. Перейдите в **Access Tokens**.
2. Выберите **Generate new token**.
3. Введите имя для вашего токена.
4. Найдите и выберите область доступа **Ingest metrics**.
5. Выберите **Generate token**.
6. Выберите **Copy**, чтобы скопировать сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

Вы можете назначить несколько разрешений одному токену или сгенерировать несколько токенов, каждый с различными уровнями доступа, и использовать их соответствующим образом. Ознакомьтесь с политиками безопасности вашей организации для получения лучших практик.

## Шаг 2 Настройка одного или нескольких выделенных ActiveGate

ActiveGate, выделенный для приёма оповещений Azure Monitor, не обязательно должен быть тем же ActiveGate, который выполняет интеграцию Azure Monitor. Это может быть любой другой [ActiveGate с поддержкой мониторинга Azure](../../../dynatrace-activegate/configuration/configure-activegate.md#azure_mod "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями.").

Чтобы настроить выделенный ActiveGate для приёма оповещений Azure Monitor:

1. Настройте действительный TLS-сертификат (не самоподписанный сертификат) для ActiveGate, чтобы обеспечить связь по HTTPS. Убедитесь, что корневой сертификат принимается Azure. Подробнее см. [как настроить пользовательский SSL-сертификат для ActiveGate](../../../dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate.md "Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").
2. Добавьте следующие строки в файл `custom.properties` вашего ActiveGate и перезапустите ActiveGate после применения конфигурации.

   ```
   [azure_monitoring]


   event_servlet = true
   ```
3. Предоставьте доступ к ActiveGate для IP-адресов источника оповещений Azure Monitor.

Подробнее см. [диапазоны IP-адресов источника](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) в документации Azure.

## Шаг 3 Настройка оповещений Azure Monitor через вебхук

В настоящее время события/оповещения, принимаемые через вебхук оповещений Azure Monitor, не потребляют DDU, хотя это может измениться в будущем.

Оповещения Azure Monitor, принимаемые через вебхуки, настраиваются в ваших правилах оповещений Azure.
Оповещения сопоставляются с ближайшей известной соответствующей сущностью. Это означает, что они либо сопоставляются со связанной сущностью ресурса Azure, либо, в качестве запасного варианта, с подпиской Azure ресурса.

Чтобы настроить оповещения Azure Monitor через вебхук, необходимо создать правило оповещения и группу действий, которая будет запускать вебхук.

1. На портале Azure перейдите в **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.
2. Выберите **Scope** > **Select scope**.
3. Отфильтруйте и выберите ресурс, который вы хотите мониторить, а затем выберите **Done**.
4. Выберите **Condition** > **Add condition**.
5. Отфильтруйте, выберите и настройте тип сигнала, который будет запускать ваше оповещение.
6. Выберите **Next: Actions** > **Create action group**.
7. Введите **subscription** (подписку), которая будет управлять развёрнутыми ресурсами и затратами, **resource group** (группу ресурсов), к которой принадлежит подписка, и имя (а также отображаемое имя) для **action group** (группы действий).
8. Выберите **Actions** и введите следующие значения:

   * Для **Action type** выберите **Webhook** и введите имя.
   * Для **URI** введите `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, обязательно заменив `<YOUR_ACTIVEGATE_ADDRESS>` и `<YOUR_API_TOKEN>` на ваши собственные значения.
9. Оставьте общую схему оповещений отключённой, а затем выберите **OK**.

Общая схема оповещений не поддерживается.

10. Выберите **Review and create** > **Create**.

После создания группы действий вы можете просматривать и редактировать её в **Alerts** > **Action groups**.

Подробнее см. [правила вебхуков в документации Azure](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).

## Типы оповещений

Поддерживаются следующие типы оповещений.

### Оповещения по метрикам

Оповещения по метрикам дополняют интеграцию Dynatrace с метриками Azure Monitor.

Оповещения по метрикам позволяют получать события на основе метрик без необходимости отправки метрик в Dynatrace. Это полезно для снижения нагрузки на API и сеть, особенно в случаях, когда метрика может не понадобиться (например, для построения графиков).

Тип события определяется на основе **Severity** (серьёзности) оповещения:

* **Sev-0 (Critical)**: `ERROR_EVENT`
* **Sev-1 (Error)**: `PERFORMANCE_EVENT`
* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`
* **Default (Informational)**: `CUSTOM_ANNOTATION`

### Оповещения журнала активности

Dynatrace поддерживает три типа уведомлений об активности.

#### Состояние ресурса журнала активности

Тип события определяется на основе **Level** (уровня) серьёзности:

* **Critical**: `AVAILABILITY_EVENT`
* **Error**: `AVAILABILITY_EVENT`
* **Default**: `CUSTOM_ANNOTATION`

Подробнее см. [Настройка оповещений о состоянии ресурсов с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) в документации Azure.

#### Состояние сервиса журнала активности

Тип события определяется на основе **IncidentType**

* Случай **ActionRequired**: `ERROR_EVENT`
* Случай **Incident** или **Security**:

  + Уровень **Error**: `ERROR_EVENT`
  + Уровень **Info** или **Warning**: `CUSTOM_ANNOTATION`
* Случай **Maintenance** или **Information**: `CUSTOM_ANNOTATION`

Анализ первопричин

События с `Properties.stage=RCA` пропускаются. Стадия RCA для состояния сервиса не поддерживается.

Подробнее см. [Создание оповещений журнала активности для уведомлений сервиса с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) в документации Azure.

#### Административные действия журнала активности

* **Default**: `CUSTOM_ANNOTATION`

## Связанные темы

* [Интеграции Microsoft Azure](../../azure-integrations.md "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry.")
* [Категории событий](../../../../dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories.md "Узнайте о различных категориях событий и поддерживаемых типах событий, а также об уровнях их серьёзности и логике их создания.")
