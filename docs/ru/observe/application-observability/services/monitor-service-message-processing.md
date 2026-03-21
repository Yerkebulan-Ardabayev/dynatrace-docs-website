---
title: Мониторинг обработки сообщений сервисом
source: https://www.dynatrace.com/docs/observe/application-observability/services/monitor-service-message-processing
scraped: 2026-03-06T21:18:27.453892
---

# Мониторинг обработки сообщений сервисами


* Учебное руководство
* 3 мин. чтения

Современные распределённые системы в значительной мере опираются на асинхронное взаимодействие через очереди сообщений и стриминговые платформы. Понимание потоков сообщений, пропускной способности и сбоев обработки критически важно для обеспечения надёжности системы.

Мониторинг обработки сообщений сервисами в Dynatrace решает эту задачу, обеспечивая всестороннюю видимость транзакций на основе сообщений в архитектуре микросервисов, помогая отслеживать пропускную способность, выявлять узкие места и устранять проблемы обработки.

## Что такое мониторинг обработки сообщений сервисами?

В Dynatrace обработка сообщений означает любую транзакцию, связанную с очередями сообщений или стриминговыми платформами, такими как Kafka, RabbitMQ, ActiveMQ и AWS SQS. Это включает сообщения, публикуемые в топиках, получаемые из очередей и обрабатываемые потребляющими сервисами.

Мониторинг обработки сообщений сервисами помогает понять, как сообщения перемещаются по распределённым системам, обнаруживать узкие места в обработке и выявлять сбои в асинхронных паттернах взаимодействия.

Доступ к мониторингу обработки сообщений сервисами можно получить непосредственно через ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, а также через пользовательские панели мониторинга и оповещения, настроенные для отслеживания метрик сообщений.

Эта функция предназначена для SRE, разработчиков и инженеров платформ, которым необходима видимость асинхронных паттернов взаимодействия и работоспособности обработки сообщений.

Мониторинг обработки сообщений сервисами обеспечивает:

* Отслеживание в реальном времени скоростей публикации, получения и обработки сообщений
* Выявление узких мест в обработке и задержек в очередях
* Отслеживание потоков сообщений между продюсирующими и потребляющими сервисами
* Мониторинг частоты ошибок при сбоях обработки сообщений
* Сопоставление инфраструктурных зависимостей для платформ обмена сообщениями
* Интеграция с распределёнными трассировками для анализа первопричин

## Справочник метрик

Dynatrace предоставляет четыре основные метрики для мониторинга обработки сообщений:

| Метрика | Описание | Единица |
| --- | --- | --- |
| `dt.service.messaging.publish.count` | Сообщения, отправленные в очереди/топики | count |
| `dt.service.messaging.receive.count` | Сообщения, полученные из очередей/топиков | count |
| `dt.service.messaging.process.count` | Успешно обработанные сообщения | count |
| `dt.service.messaging.process.failure_count` | Сообщения, обработка которых завершилась ошибкой | count |

### Ключевые измерения

| Измерение | Описание | Примеры значений |
| --- | --- | --- |
| `messaging.destination.name` | Имя очереди или топика | `authorQueue`, `orderEvents` |
| `dt.entity.service` | Идентификатор сервиса | `spring-kafka-producer` |
| `messaging.system` | Платформа обмена сообщениями | `kafka`, `rabbitmq`, `aws_sqs` |
| `aws.account.id` | Идентификатор учётной записи AWS | `123456789012` |
| `aws.region` | Регион AWS | `us-east-1` |
| `k8s.cluster.name` | Имя кластера Kubernetes | `prod-cluster` |
| `k8s.namespace.name` | Пространство имён Kubernetes | `payment-services` |

## Начало работы

Чтобы начать мониторинг обработки сообщений сервисами:

1. Перейдите в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, выберите вкладку **Explorer** и нажмите **Message processing**.
2. Выберите сервис и очередь/топик, которые хотите отслеживать.
3. Просматривайте **Publish rate**, **Receive rate** и **Process rate** на временных диаграммах.
4. Определяйте задержку, сравнивая скорости получения и обработки.
5. Детализируйте распределённые трассировки для расследования конкретных сбоев сообщений.

## Примеры запросов

Мониторинг пропускной способности обмена сообщениями сервисов:

```
timeseries throughput = sum(dt.service.messaging.process.count),


by: {dt.smartscape.service}


| lookup [smartscapeNodes "SERVICE" | fields name,id],


sourceField:dt.smartscape.service, lookupField:id


| fieldsAdd `Service` = lookup.name, dt.smartscape.service


| summarize throughput = sum(throughput[]),


by: { timeframe, interval, `Service`, dt.smartscape.service }
```

Расчёт частоты сбоев обмена сообщениями сервисов:

```
timeseries { throughput = sum(dt.service.messaging.process.count),


failure_count = sum(dt.service.messaging.process.failure_count) },


by: {dt.smartscape.service}, nonempty:true, union:true


| lookup [ smartscapeNodes "SERVICE" | fields name, id],


sourceField:dt.smartscape.service, lookupField:id


| fieldsAdd `Service` = lookup.name, dt.smartscape.service


| summarize failure_rate = sum((failure_count[] / throughput[]) * 100),


by: { timeframe, interval, `Service`, dt.smartscape.service }
```
