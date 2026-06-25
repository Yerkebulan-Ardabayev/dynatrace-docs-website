---
title: Ограничение вызовов API к Azure
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure
scraped: 2026-05-12T12:31:22.309320
---

# Ограничение вызовов API к Azure

# Ограничение вызовов API к Azure

* Пояснение
* Чтение: 3 мин
* Обновлено 9 октября 2025 г.

При мониторинге крупных сред Azure (тысячи ресурсов на подписку Azure) существует риск достижения лимитов регулирования Azure API. Следуйте этому руководству, чтобы ограничить вызовы API к Azure и обеспечить полноценный мониторинг Azure.

## Лимиты регулирования Azure

Существует два типа регулируемых запросов Azure, которые необходимо принимать во внимание:

1. [Регулируемые запросы в Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits): Azure регулирует операции чтения на уровне подписки и тенанта.

   * Dynatrace использует запросы Azure Resource Manager для сбора встроенных сервисов и метрик для всех сервисов.
2. [Регулируемые запросы в Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)

   * Dynatrace использует запросы Azure Resource Graph для сбора всех сервисов, не являющихся встроенными.

## Механизм защиты Dynatrace от регулирования Azure

По умолчанию Dynatrace собирает ресурсы и метрики Azure каждые 5 минут, чтобы не выполнять вызовы API ежеминутно. Частота опроса зависит от лимита регулирования Azure.

Dynatrace рассчитывает, сколько запросов необходимо отправить в Azure в течение предстоящего часа. Если ожидаемое число запросов превышает настроенный лимит регулирования (12 000 запросов/час), Dynatrace изменяет частоту опроса, чтобы собирать данные с интервалом не более 15 минут.

## Как избежать регулирования Azure

Для обеспечения полноценного мониторинга Dynatrace важно не превышать лимиты регулирования Azure. Чтобы уменьшить количество вызовов API к Azure, можно выполнить одно из следующих действий.

* Скорректировать конфигурацию Azure service principal в соответствии со своей средой на стороне Azure.
* Ограничить количество отслеживаемых ресурсов с помощью мониторинга по тегам на стороне Dynatrace.

Подробности см. ниже.

### Конфигурация Azure service principal

Существует три варианта настройки [Azure service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) в зависимости от среды Azure.

* Рекомендуется: один Azure service principal - одна подписка Azure

  + Лимит регулирования: 12 000 запросов/час на подписку Azure
* Одна большая подписка Azure, превышающая лимит регулирования

  Распределите мониторинг между Azure service principals:

  + Можно создать несколько Azure service principals для одной подписки Azure, задав для каждого service principal параметр `--scope` в виде отдельных групп ресурсов Azure.
    Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.

    ```
    az ad sp create-for-rbac --name <YourServicePrincipalName> --role reader --scopes /subscriptions/<YourSubscriptionID>/resourceGroups/<YourResourceGroupID> --query "{ClientID:appId,TenantID:tenant,SecretKey:password}"
    ```

    Обязательно замените заполнители (`<...>`) своими значениями:

    - `<YourServicePrincipalName>` - имя service principal, который будет создан для доступа Dynatrace к Azure.
    - `<YourSubscriptionID>` - имя подписки, которую нужно отслеживать.
    - `<YourResourceGroupID>` - имя конкретной группы ресурсов, которую нужно отслеживать.
  + Можно создать несколько Azure service principals, задав параметр `--scope` на уровне подписки, и добавить несколько учётных данных в Dynatrace для мониторинга одной подписки Azure, но разных сервисов.

    Например:

    - Один для мониторинга сервиса `Azure Virtual machines (built-in)`
    - Другой для мониторинга `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services` и `Azure Storage File Services`, но не `Azure Virtual machines (built-in)`.

    Помните, что набор отслеживаемых сервисов должен быть разным для каждых учётных данных и не должен оставаться в конфигурации по умолчанию. В противном случае значения метрик для пересекающихся сервисов могут оказаться некорректными.
* (не рекомендуется) Один Azure service principal - множество подписок Azure

  Если первый вариант не подходит, настройте Azure service principal для мониторинга до двадцати подписок Azure.

  Помните, что количество вызовов API зависит от размера подписок Azure. Если интеграция Dynatrace для мониторинга Azure работает некорректно, рассмотрите возможность уменьшения числа подписок на один Azure service principal.

### Ограничение отслеживаемых ресурсов с помощью мониторинга по тегам - конфигурация Dynatrace

Если не нужно отслеживать все ресурсы Azure в подписках, можно использовать мониторинг по тегам для уменьшения вызовов Azure API.

При большом количестве подписок мониторинга по тегам может быть недостаточно для предотвращения регулирования, поэтому всё равно необходимо подготовить надлежащую [конфигурацию Azure service principal](#service-principal).

* Мониторинг по тегам в основном позволяет ограничить вызовы для метрик и вложенных ресурсов (например, Microsoft.ServiceBus/namespaces/queues для всех ресурсов типа Microsoft.ServiceBus/namespaces).
* Вызовы для ресурсов верхнего уровня по-прежнему выполняются для каждой подписки.

Можно выбрать отслеживаемые ресурсы на основе существующих тегов Azure, которые Dynatrace автоматически импортирует из экземпляров сервисов.
Чтобы выполнять мониторинг ресурсов на основе тегов

1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.
2. На странице обзора Azure выберите значок **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для нужного экземпляра Azure.
3. Установите для параметра **Resources to be monitored** значение **Monitor resources selected by tags**.
4. Введите пары ключ/значение для определения ресурсов, которые нужно исключить из мониторинга или включить в него.
   Можно ввести несколько пар ключ/значение: каждый раз при вводе пары появляется новая пустая строка для редактирования.
5. Нажмите **Save** для сохранения конфигурации.

   Чтобы автоматически импортировать теги Azure в Dynatrace, включите **Capture Azure tags automatically**.

## Связанные темы

* [Мониторинг Microsoft Azure](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с Dynatrace")