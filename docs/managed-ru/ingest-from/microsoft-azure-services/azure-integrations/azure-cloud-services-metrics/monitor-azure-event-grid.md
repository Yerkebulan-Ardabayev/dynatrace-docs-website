---
title: Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid
scraped: 2026-05-12T11:26:36.705921
---

# Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)

# Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 27 июля 2020 г.

Dynatrace получает метрики из Azure Metrics API для Azure Event Grid (Domain Topics, Topics, System Topics). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по различным измерениям и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные условия

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

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

![Eventgrid dash](https://dt-cdn.net/images/domain-dashboard-2831-82aa7e47f2.png)

Eventgrid dash

![Topics](https://dt-cdn.net/images/topic-dashboard-1850-f3c283d392.png)

Topics

![System](https://dt-cdn.net/images/system-dashboard-1805-f6d8b147c2.png)

System

## Доступные метрики

### Azure Event Grid Domain Topics

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество недоставленных событий, соответствующих этой подписке на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, DeadLetterReason | Количество |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, Error, ErrorType | Количество | Применимо |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Topic, EventSubscriptionName, DomainEventSubscriptionName | Количество | Применимо |
| DestinationProcessingDurationInMs | Длительность обработки в назначении в миллисекундах | Topic, EventSubscriptionName, DomainEventSubscriptionName | Миллисекунда | Применимо |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, DropReason | Количество | Применимо |
| MatchedEventCount | Общее количество событий, сопоставленных с этой подпиской на события | Topic, EventSubscriptionName, DomainEventSubscriptionName | Количество | Применимо |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Topic, ErrorType, Error | Количество | Применимо |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Topic | Количество | Применимо |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах |  | Миллисекунда | Применимо |

### Azure Event Grid Topics

| Имя | Описание | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество недоставленных событий, соответствующих этой подписке на события | Количество | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Количество | Error, ErrorType, EventSubscriptionName | Применимо |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Количество | EventSubscriptionName | Применимо |
| DestinationProcessingDurationInMs | Длительность обработки в назначении в миллисекундах | Миллисекунда | EventSubscriptionName | Применимо |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Количество | DropReason, EventSubscriptionName | Применимо |
| MatchedEventCount | Общее количество событий, сопоставленных с этой подпиской на события | Количество | EventSubscriptionName | Применимо |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Количество | ErrorType, Error | Применимо |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Количество |  | Применимо |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах | Миллисекунда |  | Применимо |
| UnmatchedEventCount | Общее количество событий, не соответствующих ни одной подписке на события для этого топика | Количество |  | Применимо |

### Azure Event Grid System Topics

| Имя | Описание | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество недоставленных событий, соответствующих этой подписке на события | Количество | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Количество | Error, ErrorType, EventSubscriptionName | Применимо |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Количество | EventSubscriptionName | Применимо |
| DestinationProcessingDurationInMs | Длительность обработки в назначении в миллисекундах | Миллисекунда | EventSubscriptionName | Применимо |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Количество | DropReason, EventSubscriptionName | Применимо |
| MatchedEventCount | Общее количество событий, сопоставленных с этой подпиской на события | Количество | EventSubscriptionName | Применимо |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Количество | ErrorType, Error | Применимо |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Количество |  | Применимо |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах | Миллисекунда |  | Применимо |
| UnmatchedEventCount | Общее количество событий, не соответствующих ни одной подписке на события для этого топика | Количество |  | Применимо |