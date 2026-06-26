---
title: Миграция с классических сервисов AWS (ранее «встроенных») на облачные сервисы
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide
scraped: 2026-05-12T11:29:34.423156
---

# Миграция с классических сервисов AWS (ранее «встроенных») на облачные сервисы

# Миграция с классических сервисов AWS (ранее «встроенных») на облачные сервисы

* Практическое руководство
* Чтение: 9 мин
* Обновлено 27 июня 2024 г.

На странице обзора AWS можно получить доступ к классическим сервисам и облачным сервисам Dynatrace для мониторинга AWS. Оба типа сервисов используют одни и те же ресурсы AWS. Однако классические сервисы применяют предопределённый набор метрик, поэтому настройка отслеживаемых метрик или определение уже отслеживаемых не поддерживается.

## Классические сервисы и облачные сервисы

Как упомянуто выше, классические сервисы и облачные сервисы используют одни и те же ресурсы AWS. Однако облачные сервисы поддерживают более широкий набор параметров конфигурации: новые метрики и настраиваемые отслеживаемые метрики. Для расширения возможностей настройки начато следующее:

* Добавление новых сервисов в раздел **Облачные сервисы**, чтобы можно было выбирать нужные метрики для отслеживания.
* Добавление новых метрик для облачных сервисов: они не только настраиваемы, но и позволяют отслеживать значительно больше данных, чем прежде.
* Замена классических сервисов на облачные с расширенными параметрами настройки метрик.

![AWS E2E Cloud services infographic](https://dt-cdn.net/images/aws-e2e-cloud-services-infographic-988-0482402cdd.png)

AWS E2E Cloud services infographic

Если используются классические сервисы, рекомендуется перейти на облачные, чтобы воспользоваться расширенными возможностями настройки.

AWS Lambda

Если используется интеграция OneAgent для Lambda, рекомендуется выполнить миграцию Lambda. Начиная с Dynatrace версии 1.283, данные нового сервиса Lambda отображаются вместе с данными OneAgent на [странице сервиса Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг функций Lambda, написанных на Python, Node.js и Java.").

## Последствия миграции

Несмотря на то что классические и облачные сервисы отслеживают одни и те же ресурсы AWS, в Dynatrace они обрабатываются как два разных объекта.

* У них разные идентификаторы объектов и ключи метрик.
* Из-за различий в реализации они могут обнаруживать разное количество экземпляров. Облачные сервисы отображают только экземпляры с метриками.
* Данные для каждого типа объектов Dynatrace собираются и хранятся отдельно.
* ![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Критическое изменение. Необходимо адаптировать конфигурацию дашбордов, оповещений и зон управления с учётом идентификатора объекта или [ключей метрик отслеживаемого типа сервиса](#metrics).

Сейчас можно выбрать классический или облачный сервис для сохранения исторических данных, однако следует учитывать следующее:

* Исторические данные хранятся в классических сервисах. При возврате к классическому сервису отслеживаемые данные будут содержать пробелы за период, когда ресурсы отслеживались через облачный сервис.
* Нельзя одновременно включить оба сервиса. Несмотря на то что в Dynatrace это два разных сервиса, устаревшая и новая версии отслеживают один и тот же ресурс AWS. При одновременном включении двух версий плата за опрос одних и тех же данных будет начислена дважды.
* При включении новой версии классическая отключается автоматически, и наоборот.
* Прямая связь отсутствует между:

  + объектами с историческими и новыми данными;
  + данными облачного сервиса и данными OneAgent для непрозрачного **Amazon RDS**: они не привязаны к новой странице облачного сервиса с метриками CloudWatch.
* Журналы из [Amazon Data Firehose](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция Amazon Data Firehose позволяет напрямую принимать облачные журналы без дополнительной инфраструктуры и с большей пропускной способностью.") в **Amazon RDS** по-прежнему привязаны к историческим данным и объекту `RELATIONAL_DATABASE_SERVICE`.
* События или проблемы, которые автоматически обнаруживались на исторических (классических) данных, могут не создаваться автоматически. Правила оповещения не предусмотрены для следующих облачных сервисов:

  + **Amazon RDS**
  + **Amazon EBS**
  + **AWS Lambda**: [предустановленная конфигурация метрических событий](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting "Настройка метрических событий для оповещений.") предоставляется, но требует ручного включения.

Для мониторинга облачных сервисов необходимо настроить [Environment ActiveGate](https://dt-url.net/sc0396g).

## Изменения в интерфейсе

После настройки новой версии сервиса страница обзора AWS изменяется.

Рассмотрим пример для **Amazon EBS**.

* Если настроен устаревший сервис **Amazon EBS (классический)**, раздел **Тома EBS** страницы обзора AWS выглядит следующим образом.

  ![EBS volumes section 1](https://dt-cdn.net/images/ebs-volumes-section-1-1413-72a6702912.png)

  EBS volumes section 1
* Если настроен облачный сервис **Amazon EBS**, раздел **Тома EBS** страницы обзора AWS выглядит следующим образом.

  ![EBS volumes section 2](https://dt-cdn.net/images/ebs-volumes-section-2-1444-bab960de18.png)

  EBS volumes section 2
* Выберите **Облачные сервисы**, чтобы открыть новые страницы обзора сервисов.

  ![Amazon EBS](https://dt-cdn.net/images/amazon-ebs-1444-ac20e76566.png)

  Amazon EBS
* Кроме того, метрики облачных сервисов можно настроить через веб-интерфейс.

  ![AWS Settings Manage services](https://dt-cdn.net/images/aws-settings-manage-services-1378-2e4d62f377.png)

  AWS Settings Manage services

  ![Settings Amazon EBS](https://dt-cdn.net/images/settings-amazon-ebs-1379-58ec3b97d6.png)

  Settings Amazon EBS

## Облачные сервисы и соответствующие им классические сервисы

| Новый облачный сервис | Старый классический сервис |
| --- | --- |
| [Amazon EC2 Auto Scaling](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling "Мониторинг Amazon EC2 Auto Scaling и просмотр доступных метрик.") | [Amazon EC2 Auto Scaling (классический)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin "Мониторинг Amazon EC2 Auto Scaling и просмотр доступных метрик.") |
| [Amazon DynamoDB](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb-new "Мониторинг Amazon DynamoDB и просмотр доступных метрик.") | [Amazon DynamoDB (классический)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamo-db-builtin "Мониторинг Amazon DynamoDB и просмотр доступных метрик.") |
| [Amazon EBS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-ebs-new "Мониторинг Amazon EBS и просмотр доступных метрик.") | [Amazon EBS (классический)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-block-store-ebs-builtin "Мониторинг Amazon Elastic Block Store и просмотр доступных метрик.") |
| [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lambda-new "Мониторинг AWS Lambda и просмотр доступных метрик.") | [AWS Lambda (классический)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin "Мониторинг AWS Lambda (встроенного) и просмотр доступных метрик.") |
| [Amazon RDS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new "Мониторинг Amazon RDS и просмотр доступных метрик.") | [Amazon RDS (классический)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-builtin "Мониторинг Amazon RDS и просмотр доступных метрик.") |

## Миграция метрик

Ниже приведены таблицы с метриками классических сервисов и соответствующими им метриками облачных сервисов. Пустые ячейки означают отсутствие идентичной соответствующей метрики.

Префикс `ext:` используется метриками из [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace.") и [расширений ActiveGate](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace."), а также [классическими метриками для интеграции с AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интеграция метрик из Amazon CloudWatch.").

Несмотря на схожесть названий, метрики интеграции AWS **не** основаны на расширениях.

### Amazon Auto Scaling группа

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество запущенных экземпляров EC2 (ASG) | builtin:cloud.aws.asg.running | - | - |
| Количество остановленных экземпляров EC2 (ASG) | builtin:cloud.aws.asg.stopped | - | - |
| Количество завершённых экземпляров EC2 (ASG) | builtin:cloud.aws.asg.terminated | - | - |

### Amazon DynamoDB

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Единицы ёмкости чтения DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.consumed.read | ConsumedReadCapacityUnits Sum | ext:cloud.aws.dynamodb.consumedReadCapacityUnitsSum ext:cloud.aws.dynamodb.consumedReadCapacityUnitsByGlobalSecondaryIndexName |
| Единицы ёмкости записи DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.consumed.write | ConsumedWriteCapacityUnits Sum | ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSum ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSumByGlobalSecondaryIndexName |
| Выделенные единицы ёмкости чтения DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.provisioned.read | ProvisionedReadCapacityUnits Sum | ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSum ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSumByGlobalSecondaryIndexName |
| Выделенные единицы ёмкости записи DynamoDB | builtin:cloud.aws.dynamo.capacityUnits.provisioned.write | ProvisionedWriteCapacityUnits Sum | ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSum ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSumByGlobalSecondaryIndexName |
| Единицы ёмкости чтения DynamoDB, % | builtin:cloud.aws.dynamo.capacityUnits.read | *calculated* | 100 \* ext:cloud.aws.dynamodb.consumedReadCapacityUnitsSum / ext:cloud.aws.dynamodb.provisionedReadCapacityUnitsSum |
| Единицы ёмкости записи DynamoDB, % | builtin:cloud.aws.dynamo.capacityUnits.write | *calculated* | 100 \* ext:cloud.aws.dynamodb.consumedWriteCapacityUnitsSum / ext:cloud.aws.dynamodb.provisionedWriteCapacityUnitsSum |
| Количество запросов DynamoDB с кодом HTTP 500 | builtin:cloud.aws.dynamo.errors.system | SystemErrors Sum (by Operation) | ext:cloud.aws.dynamodb.SystemErrorsSumByOperation |
| Количество запросов DynamoDB с кодом HTTP 400 | builtin:cloud.aws.dynamo.errors.user | UserErrors Sum (by Region) | ext:cloud.aws.dynamodb.UserErrorsSum |
| Задержка успешных запросов DynamoDB для операции | builtin:cloud.aws.dynamo.requests.latency | SuccessfulRequestLatency (by Operation) | ext:cloud.aws.dynamodb.successfulRequestLatencyByOperation |
| Количество элементов, возвращённых операцией DynamoDB | builtin:cloud.aws.dynamo.requests.returnedItems | ReturnedItemCount Sum (by Operation) | ext:cloud.aws.dynamodb.returnedItemCountSumByOperation |
| Количество регулируемых запросов DynamoDB для операции | builtin:cloud.aws.dynamo.requests.throttled | ThrottledRequests Sum (by Operation) | ext:cloud.aws.dynamodb.ThrottledRequestsSumByOperation |
| Количество событий регулирования чтения DynamoDB | builtin:cloud.aws.dynamo.throttledEvents.read | ReadThrottleEvents Sum | ext:cloud.aws.dynamodb.ReadThrottleEventsSum ext:cloud.aws.dynamodb.ReadThrottleEventsSumByGlobalSecondaryIndexName |
| Количество событий регулирования записи DynamoDB | builtin:cloud.aws.dynamo.throttledEvents.write | WriteThrottleEvents Sum | ext:cloud.aws.dynamodb.WriteThrottleEventsSum ext:cloud.aws.dynamodb.WriteThrottleEventsSumByGlobalSecondaryIndexName |
| Количество таблиц для зоны доступности | builtin:cloud.aws.dynamo.tables | - | - |

### Amazon EBS

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Задержка чтения тома EBS | builtin:cloud.aws.ebs.latency.read | - | - |
| Задержка записи тома EBS | builtin:cloud.aws.ebs.latency.write | - | - |
| Потреблённые операции ввода-вывода тома EBS | builtin:cloud.aws.ebs.ops.consumed | VolumeConsumedReadWriteOps Sum | ext:cloud.aws.ebs.volumeConsumedReadWriteOps |
| Операции чтения тома EBS | builtin:cloud.aws.ebs.ops.read | VolumeReadOps Sum | ext:cloud.aws.ebs.volumeReadOpsSum |
| Операции записи тома EBS | builtin:cloud.aws.ebs.ops.write | VolumeWriteOps Sum | ext:cloud.aws.ebs.volumeWriteOpsSum |
| Пропускная способность тома EBS, % | builtin:cloud.aws.ebs.throughput.percent | VolumeThroughputPercentage | ext:cloud.aws.ebs.volumeThroughputPercentage |
| Пропускная способность чтения тома EBS | builtin:cloud.aws.ebs.throughput.read | *calculated* | ext:cloud.aws.ebs.volumeReadBytes / ext:cloud.aws.ebs.volumeTotalReadTime |
| Пропускная способность записи тома EBS | builtin:cloud.aws.ebs.throughput.write | *calculated* | ext:cloud.aws.ebs.volumeWriteBytes / ext:cloud.aws.ebs.volumeTotalWriteTime |
| Время простоя тома EBS, % | builtin:cloud.aws.ebs.idleTime | - | - |
| Длина очереди тома EBS | builtin:cloud.aws.ebs.queue | VolumeQueueLength Sum | ext:cloud.aws.ebs.volumeQueueLengthSum |

### AWS Lambda

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Количество параллельных выполнений LambdaFunction | builtin:cloud.aws.lambda.concExecutions | ConcurrentExecutions Sum | ext:cloud.aws.lambda.concurrentExecutionsSum ext:cloud.aws.lambda.concurrentExecutionsSumByResource ext:cloud.aws.lambda.concurrentExecutionsSumByRegion |
| Время выполнения кода LambdaFunction | builtin:cloud.aws.lambda.duration | Duration | ext:cloud.aws.lambda.duration ext:cloud.aws.lambda.durationByResource ext:cloud.aws.lambda.durationByRegion |
| Количество неудачных вызовов LambdaFunction с кодом HTTP 4XX | builtin:cloud.aws.lambda.errors | Errors Sum | ext:cloud.aws.lambda.errorsSum ext:cloud.aws.lambda.errorsSumByResource ext:cloud.aws.lambda.errorsSumByRegion |
| Доля неудачных вызовов LambdaFunction от всех вызовов, % | builtin:cloud.aws.lambda.errorsRate | *calculated* | 100 \* ext:cloud.aws.lambda.errorsSum / ext:cloud.aws.lambda.invocationsSum |
| Количество вызовов функции LambdaFunction | builtin:cloud.aws.lambda.invocations | Invocations Sum | ext:cloud.aws.lambda.invocationsSum ext:cloud.aws.lambda.invocationsSumByResource ext:cloud.aws.lambda.invocationsSumByRegion |
| Количество выделенных параллельных выполнений LambdaFunction | builtin:cloud.aws.lambda.provConcExecutions | ProvisionedConcurrentExecutions Sum | ext:cloud.aws.lambda.provisionedConcurrentExecutionsSum ext:cloud.aws.lambda.provisionedConcurrentExecutionsSumByResource ext:cloud.aws.lambda.provisionedConcurrentExecutionsSumByRegion |
| Количество вызовов выделенной конкурентности LambdaFunction | builtin:cloud.aws.lambda.provConcInvocations | ProvisionedConcurrencyInvocations Sum | ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSum ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSumByResource ext:cloud.aws.lambda.provisionedConcurrencyInvocationsSumByRegion |
| Количество вызовов переполнения выделенной конкурентности LambdaFunction | builtin:cloud.aws.lambda.provConcSpilloverInvocations | ProvisionedConcurrencySpilloverInvocations Sum | ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSum ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSumByResource ext:cloud.aws.lambda.provisionedConcurrencySpilloverInvocationsSumByRegion |
| Количество регулируемых вызовов функции LambdaFunction | builtin:cloud.aws.lambda.throttlers | Throttles Sum | ext:cloud.aws.lambda.throttlesSum ext:cloud.aws.lambda.throttlesSumByResource ext:cloud.aws.lambda.throttlesSumByRegion |

### Amazon RDS

| Название метрики классического сервиса | Ключ метрики классического сервиса | Название метрики облачного сервиса | Ключ метрики облачного сервиса |
| --- | --- | --- | --- |
| Использование ЦП RDS, % | builtin:cloud.aws.rds.cpu.usage | CPUUtilization | ext:cloud.aws.rds.cpuUtilization ext:cloud.aws.rds.cpuUtilizationByRegionDatabaseClass ext:cloud.aws.rds.cpuUtilizationByRegionDBClusterIdentifier ext:cloud.aws.rds.cpuUtilizationByRegion ext:cloud.aws.rds.cpuUtilizationByRegionEngineName ext:cloud.aws.rds.cpuUtilizationByRegionDBClusterIdentifierRole |
| Задержка чтения RDS | builtin:cloud.aws.rds.latency.read | ReadLatency | ext:cloud.aws.rds.readLatency ext:cloud.aws.rds.readLatencyByRegionDatabaseClass ext:cloud.aws.rds.readLatencyByRegionDBClusterIdentifier ext:cloud.aws.rds.readLatencyByRegion ext:cloud.aws.rds.readLatencyByRegionEngineName ext:cloud.aws.rds.readLatencyByRegionDBClusterIdentifierRole |
| Задержка записи RDS | builtin:cloud.aws.rds.latency.write | WriteLatency | ext:cloud.aws.rds.writeLatency ext:cloud.aws.rds.writeLatencyByRegionDatabaseClass ext:cloud.aws.rds.writeLatencyByRegionDBClusterIdentifier ext:cloud.aws.rds.writeLatencyByRegion ext:cloud.aws.rds.writeLatencyByRegionEngineName ext:cloud.aws.rds.writeLatencyByRegionDBClusterIdentifierRole |
| Доступная память RDS | builtin:cloud.aws.rds.memory.freeable | FreeableMemory | ext:cloud.aws.rds.freeableMemory ext:cloud.aws.rds.freeableMemoryByRegionDatabaseClass ext:cloud.aws.rds.freeableMemoryByRegionDBClusterIdentifier ext:cloud.aws.rds.freeableMemoryByRegion ext:cloud.aws.rds.freeableMemoryByRegionEngineName ext:cloud.aws.rds.freeableMemoryByRegionDBClusterIdentifierRole |
| Использование файла подкачки RDS | builtin:cloud.aws.rds.memory.swap | SwapUsage | ext:cloud.aws.rds.swapUsage ext:cloud.aws.rds.swapUsageByRegionDatabaseClass ext:cloud.aws.rds.swapUsageByRegionDBClusterIdentifier ext:cloud.aws.rds.swapUsageByRegion ext:cloud.aws.rds.swapUsageByRegionEngineName ext:cloud.aws.rds.swapUsageByRegionDBClusterIdentifierRole |
| Пропускная способность получения по сети RDS | builtin:cloud.aws.rds.net.rx | NetworkReceiveThroughput | ext:cloud.aws.rds.networkReceiveThroughput ext:cloud.aws.rds.networkReceiveThroughputByRegionDatabaseClass ext:cloud.aws.rds.networkReceiveThroughputByRegionDBClusterIdentifier ext:cloud.aws.rds.networkReceiveThroughputByRegion ext:cloud.aws.rds.networkReceiveThroughputByRegionEngineName ext:cloud.aws.rds.networkReceiveThroughputByRegionDBClusterIdentifierRole |
| Пропускная способность передачи по сети RDS | builtin:cloud.aws.rds.net.tx | NetworkTransmitThroughput | ext:cloud.aws.rds.networkTransmitThroughput ext:cloud.aws.rds.networkTransmitThroughputByRegionDatabaseClass ext:cloud.aws.rds.networkTransmitThroughputByRegionDBClusterIdentifier ext:cloud.aws.rds.networkTransmitThroughputByRegion ext:cloud.aws.rds.networkTransmitThroughputByRegionEngineName ext:cloud.aws.rds.networkTransmitThroughputByRegionDBClusterIdentifierRole |
| IOPS чтения RDS | builtin:cloud.aws.rds.ops.read | ReadIOPS | ext:cloud.aws.rds.readIOPS ext:cloud.aws.rds.readIOPSByRegionDatabaseClass ext:cloud.aws.rds.readIOPSByRegion ext:cloud.aws.rds.readIOPSByRegionEngineName |
| IOPS записи RDS | builtin:cloud.aws.rds.ops.write | WriteIOPS | ext:cloud.aws.rds.writeIOPS ext:cloud.aws.rds.writeIOPSByRegionDatabaseClass ext:cloud.aws.rds.writeIOPSByRegion ext:cloud.aws.rds.writeIOPSByRegionEngineName |
| Пропускная способность чтения RDS | builtin:cloud.aws.rds.throughput.read | ReadThroughput | ext:cloud.aws.rds.readThroughput ext:cloud.aws.rds.readThroughputByRegionDatabaseClass ext:cloud.aws.rds.readThroughputByRegion ext:cloud.aws.rds.readThroughputByRegionEngineName |
| Пропускная способность записи RDS | builtin:cloud.aws.rds.throughput.write | WriteThroughput | ext:cloud.aws.rds.writeThroughput ext:cloud.aws.rds.writeThroughputByRegionDatabaseClass ext:cloud.aws.rds.writeThroughputByRegion ext:cloud.aws.rds.writeThroughputByRegionEngineName |
| Соединения RDS | builtin:cloud.aws.rds.connections | DatabaseConnections Sum | ext:cloud.aws.rds.databaseConnectionsSumByRegionDatabaseClass ext:cloud.aws.rds.databaseConnectionsSumByRegionDBClusterIdentifier ext:cloud.aws.rds.databaseConnectionsSumByRegion ext:cloud.aws.rds.databaseConnectionsSumByRegionEngineName ext:cloud.aws.rds.databaseConnectionsSumByRegionDBClusterIdentifierRole |
| Свободное место RDS, % | builtin:cloud.aws.rds.free | - | - |
| Перезапуски RDS | builtin:cloud.aws.rds.restarts | - | - |