---
title: Классические (ранее «встроенные») метрики AWS
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics
scraped: 2026-03-04T21:29:09.114692
---

# Классические (ранее «встроенные») метрики AWS


* Classic
* Справочник
* Чтение: 1 мин.
* Обновлено 29 января 2024 г.

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических (ранее «встроенных») сервисов AWS на облачные сервисы](aws-migration-guide.md "Миграция классических сервисов AWS на их новые версии.").

В таблице ниже перечислены все метрики AWS, которые Dynatrace собирает по умолчанию при включении [мониторинга AWS](../../../../observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring.md "Мониторинг AWS с помощью Dynatrace").

Все остальные метрики, собираемые Dynatrace для настраиваемых сервисов AWS, см. на страницах [облачных сервисов](../aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик.").

| Ключ метрики | Название | Единица измерения | Агрегации |
| --- | --- | --- | --- |
| builtin:cloud.aws.alb.connections.active | Количество активных соединений ALB | Count | autoavgmaxmin |
| builtin:cloud.aws.alb.connections.new | Количество новых соединений ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.alb.http4xx | Количество ошибок 4XX ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.alb.http5xx | Количество ошибок 5XX ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.target.http4xx | Количество целевых ошибок 4XX ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.target.http5xx | Количество целевых ошибок 5XX ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.rejCon | Количество отклонённых соединений ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.targConn | Количество ошибок целевых соединений ALB | Count | autovalue |
| builtin:cloud.aws.alb.errors.tlsNeg | Количество ошибок согласования TLS клиента ALB | Count | autovalue |
| builtin:cloud.aws.alb.bytes | Количество обработанных байт ALB | Count | autovalue |
| builtin:cloud.aws.alb.lcus | Количество потреблённых LCU ALB | Count | autovalue |
| builtin:cloud.aws.alb.requests | Количество запросов ALB | Count | autovalue |
| builtin:cloud.aws.alb.respTime | Время ответа цели ALB | Second | autoavgmaxmin |
| builtin:cloud.aws.asg.running | Количество работающих экземпляров EC2 (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.asg.stopped | Количество остановленных экземпляров EC2 (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.asg.terminated | Количество завершённых экземпляров EC2 (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.running | Количество работающих экземпляров EC2 (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.stopped | Количество остановленных экземпляров EC2 (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.terminated | Количество завершённых экземпляров EC2 (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.dynamo.capacityUnits.consumed.read | Потреблённые единицы ёмкости чтения DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.consumed.write | Потреблённые единицы ёмкости записи DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.provisioned.read | Выделенные единицы ёмкости чтения DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.provisioned.write | Выделенные единицы ёмкости записи DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.read | Единицы ёмкости чтения DynamoDB % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.dynamo.capacityUnits.write | Единицы ёмкости записи DynamoDB % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.dynamo.errors.system | Количество запросов DynamoDB с кодом состояния HTTP 500 | Count | autovalue |
| builtin:cloud.aws.dynamo.errors.user | Количество запросов DynamoDB с кодом состояния HTTP 400 | Count | autovalue |
| builtin:cloud.aws.dynamo.requests.latency | Задержка успешных запросов DynamoDB для операции | Millisecond | autoavgmaxmin |
| builtin:cloud.aws.dynamo.requests.returnedItems | Количество элементов, возвращённых операцией DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.requests.throttled | Количество регулируемых запросов DynamoDB для операции | Count | autovalue |
| builtin:cloud.aws.dynamo.throttledEvents.read | Количество регулируемых событий чтения DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.throttledEvents.write | Количество регулируемых событий записи DynamoDB | Count | autovalue |
| builtin:cloud.aws.dynamo.tables | Количество таблиц для AvailabilityZone | Count | autoavgmaxmin |
| builtin:cloud.aws.ebs.latency.read | Задержка чтения тома EBS | Second | autoavgmaxmin |
| builtin:cloud.aws.ebs.latency.write | Задержка записи тома EBS | Second | autoavgmaxmin |
| builtin:cloud.aws.ebs.ops.consumed | Потреблённые OPS тома EBS | Per second | autovalue |
| builtin:cloud.aws.ebs.ops.read | OPS чтения тома EBS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.ops.write | OPS записи тома EBS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.percent | Пропускная способность тома EBS % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.read | Пропускная способность чтения тома EBS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.write | Пропускная способность записи тома EBS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.idleTime | Время простоя тома EBS % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ebs.queue | Длина очереди тома EBS | Count | autoavgmaxmin |
| builtin:cloud.aws.ec2.cpu.usage | Использование CPU EC2 % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.readOps | IOPS чтения хранилища экземпляра EC2 | Per second | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.readRate | Скорость чтения хранилища экземпляра EC2 | kB/s | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.writeOps | IOPS записи хранилища экземпляра EC2 | Per second | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.writeRate | Скорость записи хранилища экземпляра EC2 | kB/s | autoavgmaxmin |
| builtin:cloud.aws.ec2.net.rx | Скорость получения сетевых данных EC2 | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.ec2.net.tx | Скорость передачи сетевых данных EC2 | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.elb.errors.backend.connection | Ошибки бэкенд-соединений CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http2xx | Количество бэкенд-ошибок 2XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http3xx | Количество бэкенд-ошибок 3XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http4xx | Количество бэкенд-ошибок 4XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http5xx | Количество бэкенд-ошибок 5XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.elb.http4xx | Количество ошибок 4XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.elb.http5xx | Количество ошибок 5XX CLB | Count | autovalue |
| builtin:cloud.aws.elb.errors.frontend | Процент ошибок фронтенда CLB | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.elb.hosts.healthy | Количество здоровых хостов CLB | Count | autoavgmaxmin |
| builtin:cloud.aws.elb.hosts.unhealthy | Количество нездоровых хостов CLB | Count | autoavgmaxmin |
| builtin:cloud.aws.elb.latency | Задержка CLB | Second | autoavgmaxmin |
| builtin:cloud.aws.elb.reqCompl | Количество выполненных запросов CLB | Count | autovalue |
| builtin:cloud.aws.lambda.concExecutions | Количество параллельных выполнений LambdaFunction | Count | autoavgcountmaxminsum |
| builtin:cloud.aws.lambda.duration | Время выполнения кода LambdaFunction | Millisecond | autoavgcountmaxminsum |
| builtin:cloud.aws.lambda.errors | Количество неудачных вызовов LambdaFunction с кодом состояния HTTP 4XX | Count | autovalue |
| builtin:cloud.aws.lambda.errorsRate | Доля неудачных вызовов LambdaFunction ко всем вызовам % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.lambda.invocations | Количество вызовов LambdaFunction | Count | autovalue |
| builtin:cloud.aws.lambda.provConcExecutions | Количество выделенных параллельных выполнений LambdaFunction | Count | autovalue |
| builtin:cloud.aws.lambda.provConcInvocations | Количество вызовов с выделенной параллельностью LambdaFunction | Count | autovalue |
| builtin:cloud.aws.lambda.provConcSpilloverInvocations | Количество вызовов с переполнением выделенной параллельности LambdaFunction | Count | autovalue |
| builtin:cloud.aws.lambda.throttlers | Количество регулируемых вызовов LambdaFunction | Count | autovalue |
| builtin:cloud.aws.nlb.flow.active | Количество активных потоков NLB | Count | autoavgmaxmin |
| builtin:cloud.aws.nlb.flow.new | Количество новых потоков NLB | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.client | Количество сбросов клиента NLB | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.elb | Количество сбросов NLB | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.target | Количество сбросов цели NLB | Count | autovalue |
| builtin:cloud.aws.nlb.bytes | Количество обработанных байт NLB | Count | autovalue |
| builtin:cloud.aws.nlb.lcus | Количество потреблённых LCU NLB | Count | autovalue |
| builtin:cloud.aws.rds.cpu.usage | Использование CPU RDS % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.rds.latency.read | Задержка чтения RDS | Second | autoavgmaxmin |
| builtin:cloud.aws.rds.latency.write | Задержка записи RDS | Second | autoavgmaxmin |
| builtin:cloud.aws.rds.memory.freeable | Доступная память RDS | Byte | autoavgmaxmin |
| builtin:cloud.aws.rds.memory.swap | Использование swap RDS | Byte | autoavgmaxmin |
| builtin:cloud.aws.rds.net.rx | Пропускная способность получения сети RDS | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.net.tx | Пропускная способность передачи сети RDS | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.ops.read | IOPS чтения RDS | Per second | autoavgmaxmin |
| builtin:cloud.aws.rds.ops.write | IOPS записи RDS | Per second | autoavgmaxmin |
| builtin:cloud.aws.rds.throughput.read | Пропускная способность чтения RDS | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.throughput.write | Пропускная способность записи RDS | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.connections | Соединения RDS | Count | autoavgmaxmin |
| builtin:cloud.aws.rds.free | Свободное пространство хранилища RDS % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.rds.restarts | Перезапуски RDS | Count | autovalue |