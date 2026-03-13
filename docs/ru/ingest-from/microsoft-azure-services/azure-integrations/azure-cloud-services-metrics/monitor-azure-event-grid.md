---
title: Azure Event Grid (Domain Topics, Topics, System Topics) monitoring
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-event-grid
scraped: 2026-03-06T21:26:06.933213
---

# Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)

# Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 27, 2020

Dynatrace получает метрики из Azure Metrics API для Azure Event Grid (Domain Topics, Topics, System Topics). Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на дашбордах.

## Предварительные требования

* Dynatrace версии 1.199+
* Environment ActiveGate версии 1.195+

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../azure-monitoring-guide/azure-enable-service-monitoring.md "Включение мониторинга Azure в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** содержит список всех экземпляров (пользовательских устройств), принадлежащих группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Если для сервиса доступен предустановленный дашборд, вы получите предустановленный дашборд для соответствующего сервиса, содержащий все рекомендуемые метрики, на странице **Dashboards**. Вы можете искать определенные дашборды, фильтруя по **Preset**, а затем по **Name**.

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учетных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учетные данные, перейдите в **Settings** > **Cloud and virtualization** > **Azure**, выберите нужный экземпляр Azure, затем выберите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но вы можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню обзора (**...**) и выберите **Clone**.
Чтобы убрать дашборд из списка дашбордов, вы можете его скрыть. Чтобы скрыть дашборд, откройте меню обзора (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide azure](https://dt-cdn.net/images/2020-12-10-14-35-42-1473-23fe220b09.png)

![Eventgrid dash](https://dt-cdn.net/images/domain-dashboard-2831-82aa7e47f2.png)

![Topics](https://dt-cdn.net/images/topic-dashboard-1850-f3c283d392.png)

![System](https://dt-cdn.net/images/system-dashboard-1805-f6d8b147c2.png)

## Доступные метрики

### Azure Event Grid Domain Topics

| Название | Описание | Измерения | Единица | Рекомендуемая |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество событий, помещенных в очередь недоставленных сообщений, соответствующих этой подписке на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, DeadLetterReason | Count |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, Error, ErrorType | Count | Applicable |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| DestinationProcessingDurationInMs | Длительность обработки в месте назначения в миллисекундах | Topic, EventSubscriptionName, DomainEventSubscriptionName | MilliSecond | Applicable |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Topic, EventSubscriptionName, DomainEventSubscriptionName, DropReason | Count | Applicable |
| MatchedEventCount | Общее количество событий, соответствующих этой подписке на события | Topic, EventSubscriptionName, DomainEventSubscriptionName | Count | Applicable |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Topic, ErrorType, Error | Count | Applicable |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Topic | Count | Applicable |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах |  | MilliSecond | Applicable |

### Azure Event Grid Topics

| Название | Описание | Единица | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество событий, помещенных в очередь недоставленных сообщений, соответствующих этой подписке на события | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Длительность обработки в месте назначения в миллисекундах | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Общее количество событий, соответствующих этой подписке на события | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Count |  | Applicable |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах | MilliSecond |  | Applicable |
| UnmatchedEventCount | Общее количество событий, не соответствующих ни одной из подписок на события для этого топика | Count |  | Applicable |

### Azure Event Grid System Topics

| Название | Описание | Единица | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- |
| DeadLetteredCount | Общее количество событий, помещенных в очередь недоставленных сообщений, соответствующих этой подписке на события | Count | DeadLetterReason, EventSubscriptionName |  |
| DeliveryAttemptFailCount | Общее количество событий, которые не удалось доставить в эту подписку на события | Count | Error, ErrorType, EventSubscriptionName | Applicable |
| DeliverySuccessCount | Общее количество событий, доставленных в эту подписку на события | Count | EventSubscriptionName | Applicable |
| DestinationProcessingDurationInMs | Длительность обработки в месте назначения в миллисекундах | MilliSecond | EventSubscriptionName | Applicable |
| DroppedEventCount | Общее количество отброшенных событий, соответствующих этой подписке на события | Count | DropReason, EventSubscriptionName | Applicable |
| MatchedEventCount | Общее количество событий, соответствующих этой подписке на события | Count | EventSubscriptionName | Applicable |
| PublishFailCount | Общее количество событий, которые не удалось опубликовать в этот топик | Count | ErrorType, Error | Applicable |
| PublishSuccessCount | Общее количество событий, опубликованных в этот топик | Count |  | Applicable |
| PublishSuccessLatencyInMs | Задержка успешной публикации в миллисекундах | MilliSecond |  | Applicable |
| UnmatchedEventCount | Общее количество событий, не соответствующих ни одной из подписок на события для этого топика | Count |  | Applicable |
