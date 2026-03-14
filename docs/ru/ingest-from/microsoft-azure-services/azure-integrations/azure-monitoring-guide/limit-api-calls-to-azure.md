---
title: Ограничение вызовов API к Azure
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure
scraped: 2026-03-03T21:32:29.510104
---

# Ограничение API-вызовов к Azure


* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Oct 09, 2025

При мониторинге крупных сред Azure (тысячи ресурсов на подписку Azure) существует риск достижения лимитов троттлинга Azure API со стороны Dynatrace. Следуйте этому руководству, чтобы ограничить API-вызовы к Azure и обеспечить полноценный мониторинг Azure.

## Лимиты троттлинга Azure

Существует два типа троттлируемых запросов Azure, которые необходимо учитывать:

1. [Троттлируемые запросы в Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits) — Azure троттлирует операции чтения на уровне подписки и тенанта.

   * Dynatrace использует запросы Azure Resource Manager для сбора встроенных сервисов и метрик для всех сервисов.
2. [Троттлируемые запросы в Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)

   * Dynatrace использует запросы Azure Resource Graph для сбора всех сервисов, которые не являются встроенными.

## Механизм защиты от троттлинга Dynatrace Azure

Dynatrace собирает ресурсы и метрики Azure каждые 5 минут по умолчанию, чтобы избежать API-вызовов каждую минуту. Однако частота опроса зависит от лимита троттлинга Azure.

Dynatrace рассчитывает, сколько запросов необходимо отправить в Azure в течение следующего часа. Если количество ожидаемых запросов превышает настроенный лимит троттлинга (12 000 запросов/час), Dynatrace изменяет частоту опроса для сбора данных с интервалом не более 15 минут.

## Как избежать троттлинга Azure

Для обеспечения полноценного мониторинга Dynatrace важно избегать лимитов троттлинга Azure. Чтобы уменьшить количество API-вызовов к Azure, вы можете выполнить одно из следующих действий.

* Настроить конфигурацию Azure service principal в соответствии с вашей средой на стороне Azure.
* Ограничить количество отслеживаемых ресурсов с помощью мониторинга по тегам на стороне Dynatrace.

Подробности см. ниже.

### Конфигурация Azure service principal

У вас есть три варианта настройки [Azure service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) в зависимости от вашей среды Azure.

* Рекомендуется: Один Azure service principal — одна подписка Azure

  + Лимит троттлинга: 12 000 запросов/час на подписку Azure
* Одна большая подписка Azure, превышающая лимит троттлинга

  Разделите мониторинг между несколькими Azure service principal:

  + Вы можете создать несколько Azure service principal для одной подписки Azure, установив `--scope` каждого service principal на отдельные группы ресурсов Azure.
    Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

    ```
    az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID>/resourceGroups/<YourResourceGroupID> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
    ```

    Обязательно замените заполнители (`<...>`) вашими значениями:

    - `<YourServicePrincipalName>` — имя service principal, который будет создан для доступа Dynatrace к Azure.
    - `<YourSubscriptionID>` — имя подписки, которую вы хотите отслеживать.
    - `<YourResourceGroupID>` — имя конкретной группы ресурсов, которую вы хотите отслеживать.
  + Вы можете создать несколько Azure service principal, установив `--scope` на уровень подписки, и добавить несколько учётных данных для мониторинга одной и той же подписки Azure в Dynatrace, но с разными сервисами.

    Например:

    - Один отслеживает сервис `Azure Virtual machines (built-in)`
    - Другой отслеживает `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services` и `Azure Storage File Services`, но не отслеживает `Azure Virtual machines (built-in)`.

    Помните, что область отслеживаемых сервисов должна быть различной для каждых учётных данных и не должна оставаться с конфигурацией по умолчанию. В противном случае значения метрик для пересекающихся сервисов могут быть некорректными.
* (не рекомендуется) Один Azure service principal — много подписок Azure

  Если первый вариант не подходит для вашей ситуации, настройте Azure service principal для мониторинга до двадцати подписок Azure.

  Помните, что количество API-вызовов зависит от размера ваших подписок Azure. Если вы заметили, что интеграция Dynatrace для мониторинга Azure работает некорректно, рассмотрите возможность уменьшения количества подписок на один Azure service principal.

### Ограничение отслеживаемых ресурсов с помощью мониторинга на основе тегов — конфигурация Dynatrace

Если вам не нужно отслеживать все ресурсы Azure в ваших подписках, вы можете использовать мониторинг по тегам для уменьшения количества API-вызовов к Azure.

Если у вас много подписок, мониторинг на основе тегов может быть недостаточным для избежания троттлинга, и вам следует подготовить надлежащую [конфигурацию Azure service principal](#service-principal).

* Мониторинг по тегам в основном позволяет ограничить вызовы для метрик и подресурсов (например, Microsoft.ServiceBus/namespaces/queues для всех ресурсов типа Microsoft.ServiceBus/namespaces).
* Вызовы для ресурсов верхнего уровня по-прежнему необходимо выполнять для каждой подписки.

Вы можете выбрать мониторинг ресурсов на основе существующих тегов Azure, так как Dynatrace автоматически импортирует их из экземпляров сервисов.
Чтобы настроить мониторинг ресурсов на основе тегов:

1. Перейдите в **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure выберите значок **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для экземпляра Azure.
3. Установите **Resources to be monitored** на **Monitor resources selected by tags**.
4. Введите пары ключ/значение для идентификации ресурсов, которые нужно исключить из мониторинга или включить в мониторинг.
   Вы можете ввести несколько пар ключ/значение: каждый раз при вводе пары отображается ещё одна пустая строка для редактирования по мере необходимости.
5. Выберите **Save** для сохранения конфигурации.

   Чтобы автоматически импортировать теги Azure в Dynatrace, включите **Capture Azure tags automatically**.

## Связанные темы

* [Мониторинг Microsoft Azure](../../../../observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring.md "Мониторинг Azure с помощью Dynatrace")
