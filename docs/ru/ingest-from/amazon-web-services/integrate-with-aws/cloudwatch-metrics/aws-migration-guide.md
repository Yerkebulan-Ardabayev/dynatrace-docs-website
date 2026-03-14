---
title: Миграция с классических (ранее «встроенных») сервисов AWS на облачные сервисы
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide
scraped: 2026-03-06T21:27:57.370633
---

# Миграция с классических (ранее «встроенных») сервисов AWS на облачные сервисы


* Classic
* Практическое руководство
* 9 минут чтения
* Обновлено 27 июня 2024 г.

На странице обзора AWS можно получить доступ к классическим сервисам и облачным сервисам Dynatrace для мониторинга AWS. Оба типа сервисов используют одни и те же ресурсы AWS. Однако классические сервисы используют предопределённый набор метрик, поэтому настройка отслеживаемых метрик или определение уже отслеживаемых метрик не поддерживается.

## Классические сервисы и облачные сервисы

Как уже упоминалось, классические сервисы и облачные сервисы используют одни и те же ресурсы AWS. Однако облачные сервисы поддерживают более широкий спектр параметров конфигурации, таких как новые метрики и настраиваемые отслеживаемые метрики. Чтобы предоставить вам больше возможностей для настройки, мы начали следующее:

* Добавление новых сервисов в раздел **Cloud services**, чтобы вы могли настраивать отслеживаемые метрики.
* Добавление дополнительных метрик для облачных сервисов: они не только настраиваемые, но и позволяют отслеживать значительно больше, чем прежде.
* Замена классических сервисов облачными сервисами с расширенными возможностями настройки метрик.

![AWS E2E Cloud services infographic](https://dt-cdn.net/images/aws-e2e-cloud-services-infographic-988-0482402cdd.png)

Если вы используете классические сервисы, рекомендуем перейти на облачные сервисы, чтобы воспользоваться расширенным набором настраиваемых параметров конфигурации.

AWS Lambda

Если вы используете интеграцию OneAgent для ваших функций Lambda, рекомендуем выполнить миграцию Lambda. Начиная с версии Dynatrace 1.283, данные нового сервиса Lambda отображаются вместе с данными OneAgent на [странице сервиса Lambda](../../integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension.md "Мониторинг функций Lambda, написанных на Python, Node.js и Java.").

## Влияние миграции

Несмотря на то что классические сервисы и облачные сервисы отслеживают одни и те же ресурсы AWS на стороне Dynatrace, они отслеживаются как две разные сущности.

* У них разные идентификаторы сущностей и ключи метрик.
* В связи с различными реализациями они могут обнаруживать разное количество экземпляров. Облачные сервисы отображают только экземпляры с метриками.
* Данные для каждого типа сущностей Dynatrace собираются и хранятся отдельно.
* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Критическое изменение Необходимо адаптировать конфигурацию дашбордов, оповещений и Management Zone на основе идентификатора сущности или [ключей метрик с типом отслеживаемого сервиса](#metrics).

В настоящее время у вас есть возможность выбрать между классическим и облачным сервисом для сохранения исторических данных, однако следует учитывать следующее:

* Исторические данные сохраняются в классических сервисах. При переключении обратно в отслеживаемых данных будут пробелы за период, в течение которого ресурсы отслеживались через облачный сервис.
* Нельзя одновременно включить оба варианта. Несмотря на то что в Dynatrace это два разных сервиса, устаревшая и новая версии отслеживают один и тот же ресурс AWS. При одновременном включении двух версий с вас будет взиматься двойная плата за опрос одних и тех же данных дважды.
* При включении новой версии классическая версия отключается автоматически, и наоборот.
* Отсутствует прямая связь между

  + Сущностями, содержащими исторические и новые данные.
  + Данными облачного сервиса и данными OneAgent для непрозрачного **Amazon RDS** — не связан со страницей нового облачного сервиса с метриками CloudWatch.
* Журналы из [Amazon Data Firehose](../aws-logs-ingest/lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет принимать облачные журналы напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.") в **Amazon RDS** по-прежнему привязываются к историческим данным и сущности `RELATIONAL_DATABASE_SERVICE`.
* События или проблемы, которые могли бы автоматически обнаруживаться в исторических (классических) данных, могут не генерироваться автоматически. Правила оповещений не предусмотрены для следующих облачных сервисов:

  + **Amazon RDS**
  + **Amazon EBS**
  + **AWS Lambda** — предусмотрена [предустановленная конфигурация событий метрик](aws-set-up-metric-events-for-alerting.md "Настройка и конфигурация событий метрик для оповещений."), но её необходимо включить вручную.

Для мониторинга облачных сервисов необходимо настроить [Environment ActiveGate](https://dt-url.net/sc0396g).

## Изменения в пользовательском интерфейсе

Страница обзора AWS изменится после настройки новой версии сервиса.

Для примера рассмотрим **Amazon EBS**.

* Если настроен устаревший сервис **Amazon EBS (classic)**, вот как выглядит раздел **EBS volumes** на странице обзора AWS.

  ![EBS volumes section 1](https://dt-cdn.net/images/ebs-volumes-section-1-1413-72a6702912.png)
* Если настроен облачный сервис **Amazon EBS**, вот как выглядит раздел **EBS volumes** на странице обзора AWS.

  ![EBS volumes section 2](https://dt-cdn.net/images/ebs-volumes-section-2-1444-bab960de18.png)
* Нажмите **Cloud services** для перехода на новые страницы обзора сервисов.

  ![Amazon EBS](https://dt-cdn.net/images/amazon-ebs-1444-ac20e76566.png)
* Кроме того, метрики облачных сервисов можно настраивать через веб-интерфейс.

  ![AWS Settings Manage services](https://dt-cdn.net/images/aws-settings-manage-services-1378-2e4d62f377.png)

  ![Settings Amazon EBS](https://dt-cdn.net/images/settings-amazon-ebs-1379-58ec3b97d6.png)

## Облачные сервисы и соответствующие им классические сервисы

| Новый облачный сервис | Старый классический сервис |
| --- | --- |
| [Amazon EC2 Auto Scaling](cloudwatch-ec2/ec2-auto-scaling.md "Мониторинг Amazon EC2 Auto Scaling и просмотр доступных метрик.") | [Amazon EC2 Auto Scaling (classic)](cloudwatch-ec2/ec2-auto-scaling-builltin.md "Мониторинг Amazon EC2 Auto Scaling и просмотр доступных метрик.") |
| [Amazon DynamoDB](../aws-all-services/aws-service-dynamodb-new.md "Мониторинг Amazon DynamoDB и просмотр доступных метрик.") | [Amazon DynamoDB (classic)](../aws-all-services/aws-service-dynamo-db-builtin.md "Мониторинг Amazon DynamoDB и просмотр доступных метрик.") |
| [Amazon EBS](../aws-all-services/aws-service-ebs-new.md "Мониторинг Amazon EBS и просмотр доступных метрик.") | [Amazon EBS (classic)](../aws-all-services/aws-service-elastic-block-store-ebs-builtin.md "Мониторинг Amazon Elastic Block Store и просмотр доступных метрик.") |
| [AWS Lambda](../aws-all-services/aws-service-lambda-new.md "Мониторинг AWS Lambda и просмотр доступных метрик.") | [AWS Lambda (classic)](aws-lambda-cloudwatch-metrics/lambda-builtin.md "Мониторинг AWS Lambda (встроенный) и просмотр доступных метрик.") |
| [Amazon RDS](../aws-all-services/aws-service-relational-database-service-rds-new.md "Мониторинг Amazon RDS и просмотр доступных метрик.") | [Amazon RDS (classic)](../aws-all-services/aws-service-relational-database-service-rds-builtin.md "Мониторинг Amazon RDS и просмотр доступных метрик.") |

## Миграция метрик

Ниже приведены таблицы с метриками классических сервисов и соответствующими метриками облачных сервисов. Пустые ячейки указывают на отсутствие идентичной соответствующей метрики.

Подробнее о доступе к ним в Grail можно узнать на этой [странице](../../../../analyze-explore-automate/metrics/built-in-metrics-on-grail.md "Ознакомьтесь с аналогами классических встроенных метрик, поддерживаемых на Grail.").

Префикс `ext:` используется метриками из [расширений OneAgent](../../../extensions/develop-your-extensions.md "Разработка собственных расширений в Dynatrace.") и [расширений ActiveGate](../../../extensions/develop-your-extensions.md "Разработка собственных расширений в Dynatrace."), а также [классическими метриками для интеграции AWS](../cloudwatch-metrics.md "Интеграция метрик из Amazon CloudWatch.").

Несмотря на схожесть наименований, метрики интеграции AWS **не** основаны на расширениях.

### Amazon Auto Scaling Group

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество работающих экземпляров EC2 (ASG) | builtin:cloud.aws.asg.running | - | - |
| Количество остановленных экземпляров EC2 (ASG) | builtin:cloud.aws.asg.stopped | - | - |
| Количество завершённых экземпляров EC2 (ASG) | builtin:cloud.aws.asg.terminated | - | - |

### Amazon DynamoDB

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Единицы ёмкости чтения DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.consumed.read | ConsumedReadCapacityUnits Sum | ext:cloud.aws.dynamodb.consumedReadCapacityUnitsSum ext:cloud.aws.dynamodb.consumedReadCapacityUnitsByGlobalSecondaryIndexName |
| Единицы ёмкости записи DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.consumed.write | ConsumedWriteCapacityUnits Sum | ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSum ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSumByGlobalSecondaryIndexName |
| Подготовленные единицы ёмкости чтения DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.provisioned.read | ProvisionedReadCapacityUnits Sum | ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSum ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSumByGlobalSecondaryIndexName |
| Подготовленные единицы ёмкости записи DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.provisioned.write | ProvisionedWriteCapacityUnits Sum | ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSum ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSumByGlobalSecondaryIndexName |
| Единицы ёмкости чтения DynamoDB % | builtin:cloud.aws.dynamo.capacityUnits.read | *вычисляемое* | 100 \* ext:cloud.aws.dynamodb.consumedReadCapacityUnitsSum / ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSum |
| Единицы ёмкости записи DynamoDB % | builtin:cloud.aws.dynamo.capacityUnits.write | *вычисляемое* | 100 \* ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSum / ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSum |
| Количество запросов DynamoDB с кодом HTTP 500 | builtin:cloud.aws.dynamo.errors.system | SystemErrors Sum (by Operation) | ext:cloud.aws.dynamodb.SystemErrorsSumByOperation |
| Количество запросов DynamoDB с кодом HTTP 400 | builtin:cloud.aws.dynamo.errors.user | UserErrors Sum (by Region) | ext:cloud.aws.dynamodb.UserErrorsSum |
| Количество успешных запросов DynamoDB с задержкой по операции | builtin:cloud.aws.dynamo.requests.latency | SuccessfulRequestLatency (by Operation) | ext:cloud.aws.dynamodb.successfulRequestLatencyByOperation |
| Количество элементов, возвращённых операцией DynamoDB | builtin:cloud.aws.dynamo.requests.returnedItems | ReturnedItemCount Sum (by Operation) | ext:cloud.aws.dynamodb.returnedItemCountSumByOperation |
| Количество ограниченных запросов DynamoDB по операции | builtin:cloud.aws.dynamo.requests.throttled | ThrottledRequests Sum (by Operation) | ext:cloud.aws.dynamodb.ThrottledRequestsSumByOperation |
| Количество событий ограничения чтения DynamoDB | builtin:cloud.aws.dynamo.throttledEvents.read | ReadThrottleEvents Sum | ext:cloud.aws.dynamodb.ReadThrottleEventsSum ext:cloud.aws.dynamodb.ReadThrottleEventsSumByGlobalSecondaryIndexName |
| Количество событий ограничения записи DynamoDB | builtin:cloud.aws.dynamo.throttledEvents.write | WriteThrottleEvents Sum | ext:cloud.aws.dynamodb.WriteThrottleEventsSum ext:cloud.aws.dynamodb.WriteThrottleEventsSumByGlobalSecondaryIndexName |
| Количество таблиц для AvailabilityZone | builtin:cloud.aws.dynamo.tables | - | - |

### Amazon EBS

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Задержка чтения тома EBS | builtin:cloud.aws.ebs.latency.read | - | - |
| Задержка записи тома EBS | builtin:cloud.aws.ebs.latency.write | - | - |
| Потреблённые операции ввода-вывода тома EBS | builtin:cloud.aws.ebs.ops.consumed | VolumeConsumedReadWriteOps Sum | ext:cloud.aws.ebs.volumeConsumedReadWriteOps |
| Операции чтения тома EBS | builtin:cloud.aws.ebs.ops.read | VolumeReadOps Sum | ext:cloud.aws.ebs.volumeReadOpsSum |
| Операции записи тома EBS | builtin:cloud.aws.ebs.ops.write | VolumeWriteOps Sum | ext:cloud.aws.ebs.volumeWriteOpsSum |
| Пропускная способность тома EBS % | builtin:cloud.aws.ebs.throughput.percent | VolumeThroughputPercentage | ext:cloud.aws.ebs.volumeThroughputPercentage |
| Пропускная способность чтения тома EBS | builtin:cloud.aws.ebs.throughput.read | *вычисляемое* | ext:cloud.aws.ebs.volumeReadBytes / ext:cloud.aws.ebs.volumeTotalReadTime |
| Пропускная способность записи тома EBS | builtin:cloud.aws.ebs.throughput.write | *вычисляемое* | ext:cloud.aws.ebs.volumeWriteBytes / ext:cloud.aws.ebs.volumeTotalWriteTime |
| Время простоя тома EBS % | builtin:cloud.aws.ebs.idleTime | - | - |
| Длина очереди тома EBS | builtin:cloud.aws.ebs.queue | VolumeQueueLength Sum | ext:cloud.aws.ebs.volumeQueueLengthSum |

### AWS Lambda

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество параллельных выполнений LambdaFunction | builtin:cloud.aws.lambda.concExecutions | ConcurrentExecutions Sum | ext:cloud.aws.lambda.concurrentExecutionsSum ext:cloud.aws.lambda.concurrentExecutionsSumByResource ext:cloud.aws.lambda.concurrentExecutionsSumByRegion |
| Время выполнения кода LambdaFunction. | builtin:cloud.aws.lambda.duration | Duration | ext:cloud.aws.lambda.duration ext:cloud.aws.lambda.durationByResource ext:cloud.aws.lambda.durationByRegion |
| Количество неудачных вызовов LambdaFunction с кодом HTTP 4XX | builtin:cloud.aws.lambda.errors | Errors Sum | ext:cloud.aws.lambda.errorsSum ext:cloud.aws.lambda.errorsSumByResource ext:cloud.aws.lambda.errorsSumByRegion |
| Доля неудачных вызовов LambdaFunction от общего числа вызовов % | builtin:cloud.aws.lambda.errorsRate | *вычисляемое* | 100 \* ext:cloud.aws.lambda.errorsSum / ext:cloud.aws.lambda.invocationsSum |
| Количество вызовов LambdaFunction | builtin:cloud.aws.lambda.invocations | Invocations Sum | ext:cloud.aws.lambda.invocationsSum ext:cloud.aws.lambda.invocationsSumByResource ext:cloud.aws.lambda.invocationsSumByRegion |
| Количество подготовленных параллельных выполнений LambdaFunction | builtin:cloud.aws.lambda.provConcExecutions | ProvisionedConcurrentExecutions Sum | ext:cloud.aws.lambda.provisionedConcurrentExecutionsSum ext:cloud.aws.lambda.provisionedConcurrentExecutionsSumByResource ext:cloud.aws.lambda.provisionedConcurrentExecutionsSumByRegion |
| Количество вызовов с подготовленным параллелизмом LambdaFunction | builtin:cloud.aws.lambda.provConcInvocations | ProvisionedConcurrencyInvocations Sum | ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSum ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSumByResource ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSumByRegion |
| Количество вызовов с переполнением подготовленного параллелизма LambdaFunction | builtin:cloud.aws.lambda.provConcSpilloverInvocations | ProvisionedConcurrencySpilloverInvocations Sum | ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSum ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSumByResource ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSumByRegion |
| Количество ограниченных вызовов функции LambdaFunction | builtin:cloud.aws.lambda.throttlers | Throttles Sum | ext:cloud.aws.lambda.throttlesSum ext:cloud.aws.lambda.throttlesSumByResource ext:cloud.aws.lambda.throttlesSumByRegion |

### Amazon RDS

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Использование ЦП RDS % | builtin:cloud.aws.rds.cpu.usage | CPUUtilization | ext:cloud.aws.rds.cpuUtilization ext:cloud.aws.rds.cpuUtilizationByRegionDatabaseClass ext:cloud.aws.rds.cpuUtilizationByRegionDBClusterIdentifier ext:cloud.aws.rds.cpuUtilizationByRegion ext:cloud.aws.rds.cpuUtilizationByRegionEngineName ext:cloud.aws.rds.cpuUtilizationByRegionDBClusterIdentifierRole |
| Задержка чтения RDS | builtin:cloud.aws.rds.latency.read | ReadLatency | ext:cloud.aws.rds.readLatency ext:cloud.aws.rds.readLatencyByRegionDatabaseClass ext:cloud.aws.rds.readLatencyByRegionDBClusterIdentifier ext:cloud.aws.rds.readLatencyByRegion ext:cloud.aws.rds.readLatencyByRegionEngineName ext:cloud.aws.rds.readLatencyByRegionDBClusterIdentifierRole |
| Задержка записи RDS | builtin:cloud.aws.rds.latency.write | WriteLatency | ext:cloud.aws.rds.writeLatency ext:cloud.aws.rds.writeLatencyByRegionDatabaseClass ext:cloud.aws.rds.writeLatencyByRegionDBClusterIdentifier ext:cloud.aws.rds.writeLatencyByRegion ext:cloud.aws.rds.writeLatencyByRegionEngineName ext:cloud.aws.rds.writeLatencyByRegionDBClusterIdentifierRole |
| Свободная память RDS | builtin:cloud.aws.rds.memory.freeable | FreeableMemory | ext:cloud.aws.rds.freeableMemory ext:cloud.aws.rds.freeableMemoryByRegionDatabaseClass ext:cloud.aws.rds.freeableMemoryByRegionDBClusterIdentifier ext:cloud.aws.rds.freeableMemoryByRegion ext:cloud.aws.rds.freeableMemoryByRegionEngineName ext:cloud.aws.rds.freeableMemoryByRegionDBClusterIdentifierRole |
| Использование swap-памяти RDS | builtin:cloud.aws.rds.memory.swap | SwapUsage | ext:cloud.aws.rds.swapUsage ext:cloud.aws.rds.swapUsageByRegionDatabaseClass ext:cloud.aws.rds.swapUsageByRegionDBClusterIdentifier ext:cloud.aws.rds.swapUsageByRegion ext:cloud.aws.rds.swapUsageByRegionEngineName ext:cloud.aws.rds.swapUsageByRegionDBClusterIdentifierRole |
| Пропускная способность приёма по сети RDS | builtin:cloud.aws.rds.net.rx | NetworkReceiveThroughput | ext:cloud.aws.rds.networkReceiveThroughput ext:cloud.aws.rds.networkReceiveThroughputByRegionDatabaseClass ext:cloud.aws.rds.networkReceiveThroughputByRegionDBClusterIdentifier ext:cloud.aws.rds.networkReceiveThroughputByRegion ext:cloud.aws.rds.networkReceiveThroughputByRegionEngineName ext:cloud.aws.rds.networkReceiveThroughputByRegionDBClusterIdentifierRole |
| Пропускная способность передачи по сети RDS | builtin:cloud.aws.rds.net.tx | NetworkTransmitThroughput | ext:cloud.aws.rds.networkTransmitThroughput ext:cloud.aws.rds.networkTransmitThroughputByRegionDatabaseClass ext:cloud.aws.rds.networkTransmitThroughputByRegionDBClusterIdentifier ext:cloud.aws.rds.networkTransmitThroughputByRegion ext:cloud.aws.rds.networkTransmitThroughputByRegionEngineName ext:cloud.aws.rds.networkTransmitThroughputByRegionDBClusterIdentifierRole |
| IOPS чтения RDS | builtin:cloud.aws.rds.ops.read | ReadIOPS | ext:cloud.aws.rds.readIOPS ext:cloud.aws.rds.readIOPSByRegionDatabaseClass ext:cloud.aws.rds.readIOPSByRegion ext:cloud.aws.rds.readIOPSByRegionEngineName |
| IOPS записи RDS | builtin:cloud.aws.rds.ops.write | WriteIOPS | ext:cloud.aws.rds.writeIOPS ext:cloud.aws.rds.writeIOPSByRegionDatabaseClass ext:cloud.aws.rds.writeIOPSByRegion ext:cloud.aws.rds.writeIOPSByRegionEngineName |
| Пропускная способность чтения RDS | builtin:cloud.aws.rds.throughput.read | ReadThroughput | ext:cloud.aws.rds.readThroughput ext:cloud.aws.rds.readThroughputByRegionDatabaseClass ext:cloud.aws.rds.readThroughputByRegion ext:cloud.aws.rds.readThroughputByRegionEngineName |
| Пропускная способность записи RDS | builtin:cloud.aws.rds.throughput.write | WriteThroughput | ext:cloud.aws.rds.writeThroughput ext:cloud.aws.rds.writeThroughputByRegionDatabaseClass ext:cloud.aws.rds.writeThroughputByRegion ext:cloud.aws.rds.writeThroughputByRegionEngineName |
| Соединения RDS | builtin:cloud.aws.rds.connections | DatabaseConnections Sum | ext:cloud.aws.rds.databaseConnectionsSumByRegionDatabaseClass ext:cloud.aws.rds.databaseConnectionsSumByRegionDBClusterIdentifier ext:cloud.aws.rds.databaseConnectionsSumByRegion ext:cloud.aws.rds.databaseConnectionsSumByRegionEngineName ext:cloud.aws.rds.databaseConnectionsSumByRegionDBClusterIdentifierRole |
| Свободное пространство хранилища RDS % | builtin:cloud.aws.rds.free | - | - |
| Перезапуски RDS | builtin:cloud.aws.rds.restarts | - | - |
