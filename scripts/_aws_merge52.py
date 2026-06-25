# -*- coding: utf-8 -*-
"""Merge L4-IF.52 batch (Amazon Kinesis: Data Analytics, Data Firehose, Data
Streams (KDS), Video Streams) translations into the shared cumulative dicts.

Same mechanism as L4-IF.45-51: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. Any skeleton
key left without a translation, or any translation matching no skeleton key, is
reported (self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Product-name sub-headings (### ...) map to themselves (identity, EN canon, like
### ActiveMQ / ### Amazon SageMaker Endpoints). Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if52.json")


def asciinorm(s):
    for a, b in [
        ("’", "'"),
        ("‘", "'"),
        ("“", '"'),
        ("”", '"'),
        ("…", "..."),
        ("–", "-"),
        ("—", "-"),
        ("×", "x"),
        ("\\_", "_"),
        ("\\*", "*"),
    ]:
        s = s.replace(a, b)
    return s


def en_v1(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view metrics for each service instance, split metrics into multiple dimensions, "
        "and create custom charts that you can pin to your dashboards." % s
    )


def ru_v1(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений "
        "и создавать собственные графики, которые можно закреплять на дашбордах." % s
    )


RU = {}

# ---- intro (form V1) + heading + read-time + date ----
RU[en_v1("Amazon Kinesis")] = ru_v1("Amazon Kinesis")
RU[
    "# Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams) monitoring"
] = "# Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)"
RU["* 33-min read"] = "* Чтение: 33 мин"
RU["* Updated on Jan 10, 2025"] = "* Обновлено 10 января 2025 г."

# ---- product-name sub-headings: identity (EN canon) ----
for h in [
    "### Amazon Kinesis Data Analytics",
    "### Amazon Data Firehose",
    "### Amazon Kinesis Data Streams (KDS)",
    "### Amazon Kinesis Video Streams",
]:
    RU[h] = h

# ---- per-table main-dimension lines ----
RU["`Application` is the main dimension."] = "Основное измерение: `Application`."
RU["`DeliveryStreamName` is the main dimension."] = (
    "Основное измерение: `DeliveryStreamName`."
)
RU["`StreamName` is the main dimension."] = "Основное измерение: `StreamName`."

# ---- Amazon Kinesis Data Analytics (Flink) descriptions ----
RU.update(
    {
        "The number of bytes read (per input stream) or written (per output stream).": "Количество прочитанных байт (на входной поток) или записанных (на выходной поток).",
        "The number of records returned by a Lambda function that were marked with `Dropped` status.": "Количество записей, возвращённых функцией Lambda и помеченных статусом `Dropped`.",
        "The time taken for each AWS Lambda function invocation performed by Kinesis Data Analytics.": "Время, затраченное на каждый вызов функции AWS Lambda, выполненный Kinesis Data Analytics.",
        "The sum of bytes of the records returned by a Lambda function that were marked with `OK` status.": "Сумма байт записей, возвращённых функцией Lambda и помеченных статусом `OK`.",
        "The number of records returned by a Lambda function that were marked with `OK` status.": "Количество записей, возвращённых функцией Lambda и помеченных статусом `OK`.",
        "The number of records returned by a Lambda function that were marked with `ProcessingFailed` status.": "Количество записей, возвращённых функцией Lambda и помеченных статусом `ProcessingFailed`.",
        "The number of successful Lambda invocations by Kinesis Data Analytics.": "Количество успешных вызовов Lambda, выполненных Kinesis Data Analytics.",
        "The number of Kinesis Processing Units that are used to run your stream processing application.": "Количество единиц обработки Kinesis, используемых для запуска вашего приложения потоковой обработки.",
        "The time taken for each Lambda function invocation performed by Kinesis Data Analytics.": "Время, затраченное на каждый вызов функции Lambda, выполненный Kinesis Data Analytics.",
        "Indicates how far behind from the current time an application is reading from the streaming source.": "Показывает, насколько относительно текущего времени приложение отстаёт при чтении из потокового источника.",
        "The number of records read (per input stream) or written (per output stream).": "Количество прочитанных записей (на входной поток) или записанных (на выходной поток).",
        "The number of successful deliveries. Every successful delivery attempt to the destination configured for your application is marked with `1`. Every failed delivery attempt is marked with `0`.": "Количество успешных доставок. Каждая успешная попытка доставки в место назначения, настроенное для вашего приложения, помечается значением `1`. Каждая неудачная попытка доставки помечается значением `0`.",
        "The time (in milliseconds) this task or operator is back pressured per second.": "Время (в миллисекундах), в течение которого эта задача или оператор находится под обратным давлением, в секунду.",
        "The time (in milliseconds) this task or operator is busy (neither idle nor back pressured) per second. Can be NaN, if the value could not be calculated.": "Время (в миллисекундах), в течение которого эта задача или оператор занят (не простаивает и не находится под обратным давлением), в секунду. Может быть NaN, если значение не удалось вычислить.",
        "The average number of bytes consumed per second for a topic.": "Среднее количество байт, потребляемых в секунду для топика.",
        "The total number of offset commit failures to Kafka, if offset committing and checkpointing are enabled.": "Общее количество неудачных фиксаций смещения в Kafka, если включены фиксация смещения и создание контрольных точек.",
        "The total number of successful offset commits to Kafka, if offset committing and checkpointing are enabled.": "Общее количество успешных фиксаций смещения в Kafka, если включены фиксация смещения и создание контрольных точек.",
        "The last successfully committed offsets to Kafka, for each partition. A particular partition's metric can be specified by topic name and partition id.": "Последние успешно зафиксированные смещения в Kafka для каждой партиции. Метрику конкретной партиции можно указать по имени топика и id партиции.",
        "Overall percentage of CPU utilization across task manager containers in Flink application cluster.": "Общий процент использования CPU по контейнерам менеджеров задач в кластере приложения Flink.",
        "Overall percentage of disk utilization across task manager containers in Flink application cluster.": "Общий процент использования диска по контейнерам менеджеров задач в кластере приложения Flink.",
        "Overall percentage of memory utilization across task manager containers in Flink application cluster.": "Общий процент использования памяти по контейнерам менеджеров задач в кластере приложения Flink.",
        "Overall percentage of CPU utilization across task managers.": "Общий процент использования CPU по менеджерам задач.",
        "The last watermark this application/operator/task/thread has received.": "Последний водяной знак, полученный этим приложением/оператором/задачей/потоком.",
        "The consumer's current read offset, for each partition. A particular partition's metric can be specified by topic name and partition id.": "Текущее смещение чтения потребителя для каждой партиции. Метрику конкретной партиции можно указать по имени топика и id партиции.",
        "The last watermark this application/operator/task/thread has emitted.": "Последний водяной знак, отправленный этим приложением/оператором/задачей/потоком.",
        "For jobs currently in a failing/recovering situation, the time elapsed during this outage.": "Для заданий, в данный момент находящихся в состоянии сбоя/восстановления, время, прошедшее в течение этого перебоя в работе.",
        "The total number of times this job has fully restarted since it was submitted. This metric does not measure fine-grained restarts.": "Общее количество полных перезапусков этого задания с момента его отправки. Эта метрика не учитывает точечные перезапуски.",
        "Overall heap memory utilization across task managers.": "Общее использование памяти кучи по менеджерам задач.",
        "The time (in milliseconds) this task or operator is idle (has no data to process) per second. Idle time excludes back pressured time, so if the task is back pressured it is not idle.": "Время (в миллисекундах), в течение которого эта задача или оператор простаивает (нет данных для обработки), в секунду. Время простоя не включает время под обратным давлением, поэтому если задача находится под обратным давлением, она не простаивает.",
        "The time it took to complete the last checkpoint.": "Время, которое потребовалось для завершения последней контрольной точки.",
        "The total size of the last checkpoint": "Общий размер последней контрольной точки",
        "The total number of records this application, operator or task has received per second.": "Общее количество записей, полученных этим приложением, оператором или задачей в секунду.",
        "The total number of records this application, operator, or task has received.": "Общее количество записей, полученных этим приложением, оператором или задачей.",
        "The total number of records this application, operator or task has emitted per second.": "Общее количество записей, отправленных этим приложением, оператором или задачей в секунду.",
        "The total number of records this application, operator or task has emitted.": "Общее количество записей, отправленных этим приложением, оператором или задачей.",
        "The number of times checkpointing has failed.": "Количество случаев сбоя при создании контрольных точек.",
        "The total number of old garbage collection operations that have occurred across all task managers.": "Общее количество операций сборки мусора старого поколения, произошедших по всем менеджерам задач.",
        "The total time spent performing old garbage collection operations.": "Общее время, затраченное на выполнение операций сборки мусора старого поколения.",
        "The maximum lag in terms of number of records for any partition in this window": "Максимальное отставание по числу записей для любой партиции в этом окне",
        "The time that the job has been running without interruption.": "Время, в течение которого задание выполнялось без прерываний.",
    }
)

# ---- Amazon Data Firehose descriptions ----
RU.update(
    {
        "The number of bytes delivered to Amazon S3 for backup over the specified time period. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled.": "Количество байт, доставленных в Amazon S3 для резервного копирования за указанный период времени. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3.",
        "Age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to the Amazon S3 bucket for backup. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled.": "Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в корзину Amazon S3 для резервного копирования. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3.",
        "The number of records delivered to Amazon S3 for backup over the specified time period. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled.": "Количество записей, доставленных в Amazon S3 для резервного копирования за указанный период времени. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3.",
        "Sum of successful Amazon S3 put commands for backup over sum of all Amazon S3 backup put commands. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled.": "Сумма успешных команд put в Amazon S3 для резервного копирования относительно суммы всех команд put резервного копирования в Amazon S3. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3.",
        "When the data source is a Kinesis data stream, this metric indicates the number of bytes read from that data stream. This number includes rereads due to failovers.": "Когда источником данных является поток данных Kinesis, эта метрика показывает количество байт, прочитанных из этого потока данных. Это число включает повторные чтения из-за отработки отказа.",
        "When the data source is a Kinesis data stream, this metric indicates the number of records read from that data stream. This number includes rereads due to failovers.": "Когда источником данных является поток данных Kinesis, эта метрика показывает количество записей, прочитанных из этого потока данных. Это число включает повторные чтения из-за отработки отказа.",
        "The number of bytes indexed to Amazon ES over the specified time period": "Количество байт, проиндексированных в Amazon ES за указанный период времени",
        "The number of records indexed to Amazon ES over the specified time period": "Количество записей, проиндексированных в Amazon ES за указанный период времени",
        "The sum of the successfully indexed records over the sum of records that were attempted": "Сумма успешно проиндексированных записей относительно суммы записей, по которым была предпринята попытка",
        "The number of bytes copied to Amazon Redshift over the specified time period": "Количество байт, скопированных в Amazon Redshift за указанный период времени",
        "The number of records copied to Amazon Redshift over the specified time period": "Количество записей, скопированных в Amazon Redshift за указанный период времени",
        "The sum of successful Amazon Redshift `COPY` commands over the sum of all Amazon Redshift `COPY` commands": "Сумма успешных команд `COPY` в Amazon Redshift относительно суммы всех команд `COPY` в Amazon Redshift",
        "The number of bytes delivered to Amazon S3 over the specified time period": "Количество байт, доставленных в Amazon S3 за указанный период времени",
        "The age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to the S3 bucket.": "Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в корзину S3.",
        "The number of records delivered to Amazon S3 over the specified time period": "Количество записей, доставленных в Amazon S3 за указанный период времени",
        "The sum of successful Amazon S3 put commands over the sum of all Amazon S3 put commands": "Сумма успешных команд put в Amazon S3 относительно суммы всех команд put в Amazon S3",
        "The number of bytes delivered to Splunk over the specified time period": "Количество байт, доставленных в Splunk за указанный период времени",
        "The approximate duration it takes to receive an acknowledgment from Splunk after Amazon Data Firehose sends it data": "Приблизительная продолжительность получения подтверждения от Splunk после того, как Amazon Data Firehose отправляет ему данные",
        "Age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to Splunk.": "Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в Splunk.",
        "The number of records delivered to Splunk over the specified time period": "Количество записей, доставленных в Splunk за указанный период времени",
        "The time taken per `DescribeDeliveryStream` operation, measured over the specified time period": "Время, затраченное на одну операцию `DescribeDeliveryStream`, измеренное за указанный период времени",
        "The total number of `DescribeDeliveryStream` requests": "Общее количество запросов `DescribeDeliveryStream`",
        "The time it takes for each Lambda function invocation performed by Amazon Data Firehose": "Время, затрачиваемое на каждый вызов функции Lambda, выполненный Amazon Data Firehose",
        "The sum of the successful Lambda function invocations over the sum of the total Lambda function invocations": "Сумма успешных вызовов функции Lambda относительно суммы всех вызовов функции Lambda",
        "The size of the records that could not be converted": "Размер записей, которые не удалось преобразовать",
        "The number of records that could not be converted": "Количество записей, которые не удалось преобразовать",
        "The number of bytes ingested successfully into the delivery stream over the specified time period after throttling": "Количество байт, успешно принятых в поток доставки за указанный период времени после регулирования",
        "The number of records ingested successfully into the delivery stream over the specified time period after throttling": "Количество записей, успешно принятых в поток доставки за указанный период времени после регулирования",
        "When the data source is a Kinesis data stream, this metric indicates the number of milliseconds that the last read record is behind the newest record in the Kinesis data stream": "Когда источником данных является поток данных Kinesis, эта метрика показывает количество миллисекунд, на которое последняя прочитанная запись отстаёт от новейшей записи в потоке данных Kinesis",
        "The time taken per `ListDeliveryStream` operation, measured over the specified time period": "Время, затраченное на одну операцию `ListDeliveryStream`, измеренное за указанный период времени",
        "The total number of `ListFirehose` requests": "Общее количество запросов `ListFirehose`",
        "The number of bytes put to the Amazon Data Firehose delivery stream using `PutRecordBatch` over the specified time period": "Количество байт, помещённых в поток доставки Amazon Data Firehose с помощью `PutRecordBatch` за указанный период времени",
        "The time taken per `PutRecordBatch` operation, measured over the specified time period": "Время, затраченное на одну операцию `PutRecordBatch`, измеренное за указанный период времени",
        "The total number of records from `PutRecordBatch` operations": "Общее количество записей из операций `PutRecordBatch`",
        "The total number of `PutRecordBatch` requests": "Общее количество запросов `PutRecordBatch`",
        "The number of bytes put to the Amazon Data Firehose delivery stream using `PutRecord` over the specified time period": "Количество байт, помещённых в поток доставки Amazon Data Firehose с помощью `PutRecord` за указанный период времени",
        "The time taken per `PutRecord` operation, measured over the specified time period": "Время, затраченное на одну операцию `PutRecord`, измеренное за указанный период времени",
        "The total number of `PutRecord` requests, which is equal to the total number of records from `PutRecord` operations": "Общее количество запросов `PutRecord`, которое равно общему количеству записей из операций `PutRecord`",
        "The size of the successfully converted records": "Размер успешно преобразованных записей",
        "The number of successfully converted records": "Количество успешно преобразованных записей",
        "The number of successfully processed bytes over the specified time period": "Количество успешно обработанных байт за указанный период времени",
        "The number of successfully processed records over the specified time period": "Количество успешно обработанных записей за указанный период времени",
        "The total number of times the `DescribeStream` operation is throttled when the data source is a Kinesis data stream": "Общее количество случаев регулирования операции `DescribeStream`, когда источником данных является поток данных Kinesis",
        "The total number of times the `GetRecords` operation is throttled when the data source is a Kinesis data stream": "Общее количество случаев регулирования операции `GetRecords`, когда источником данных является поток данных Kinesis",
        "The total number of times the `GetShardIterator` operation is throttled when the data source is a Kinesis data stream": "Общее количество случаев регулирования операции `GetShardIterator`, когда источником данных является поток данных Kinesis",
        "The time taken per `UpdateDeliveryStream` operation, measured over the specified time period": "Время, затраченное на одну операцию `UpdateDeliveryStream`, измеренное за указанный период времени",
        "The total number of `UpdateDeliveryStream` requests": "Общее количество запросов `UpdateDeliveryStream`",
    }
)

# ---- Amazon Kinesis Data Streams (KDS) descriptions ----
RU.update(
    {
        "The number of bytes retrieved from the Kinesis stream, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes in a single `GetRecords` operation for the stream in the specified time period.": "Количество байт, извлечённых из потока Kinesis, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты в одной операции `GetRecords` для потока за указанный период времени.",
        "The age of the last record in all `GetRecords` calls made against a Kinesis stream, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream.": "Возраст последней записи во всех вызовах `GetRecords`, выполненных к потоку Kinesis, измеренный за указанный период времени. Возраст представляет собой разницу между текущим временем и моментом, когда последняя запись вызова `GetRecords` была записана в поток. Статистики Minimum и Maximum можно использовать для отслеживания прогресса потребительских приложений Kinesis. Значение `0` означает, что считываемые записи полностью догнали поток.",
        "The time taken per GetRecords operation, measured over the specified time period": "Время, затраченное на одну операцию GetRecords, измеренное за указанный период времени",
        "The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single `GetRecords` operation for the stream in the specified time period.": "Количество записей, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи в одной операции `GetRecords` для потока за указанный период времени.",
        "The number of successful `GetRecords` operations per stream, measured over the specified time period": "Количество успешных операций `GetRecords` на поток, измеренное за указанный период времени",
        "The number of bytes successfully put to the Kinesis stream over the specified time period. This metric includes bytes from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the bytes in a single put operation for the stream in the specified time period.": "Количество байт, успешно помещённых в поток Kinesis за указанный период времени. Эта метрика включает байты из операций `PutRecord` и `PutRecords`. Статистики Minimum, Maximum и Average представляют байты в одной операции put для потока за указанный период времени.",
        "The number of records successfully put to the Kinesis stream over the specified time period. This metric includes record counts from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the records in a single put operation for the stream in the specified time period.": "Количество записей, успешно помещённых в поток Kinesis за указанный период времени. Эта метрика включает количество записей из операций `PutRecord` и `PutRecords`. Статистики Minimum, Maximum и Average представляют записи в одной операции put для потока за указанный период времени.",
        "The age of the last record in all `GetRecords` calls made against a shard, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream.": "Возраст последней записи во всех вызовах `GetRecords`, выполненных к шарду, измеренный за указанный период времени. Возраст представляет собой разницу между текущим временем и моментом, когда последняя запись вызова `GetRecords` была записана в поток. Статистики Minimum и Maximum можно использовать для отслеживания прогресса потребительских приложений Kinesis. Значение `0` означает, что считываемые записи полностью догнали поток.",
        "The number of bytes retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period.": "Количество байт, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты, возвращённые в одной операции `GetRecords` или опубликованные в одном событии `SubscribeToShard` для шарда за указанный период времени.",
        "The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period.": "Количество записей, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи, возвращённые в одной операции `GetRecords` или опубликованные в одном событии `SubscribeToShard` для шарда за указанный период времени.",
        "The number of bytes put to the Kinesis stream using the `PutRecord` operation over the specified time period": "Количество байт, помещённых в поток Kinesis с помощью операции `PutRecord` за указанный период времени",
        "The number of successful `PutRecord` operations per Kinesis stream, measured over the specified time period. Average reflects the percentage of successful writes to a stream.": "Количество успешных операций `PutRecord` на поток Kinesis, измеренное за указанный период времени. Average отражает процент успешных записей в поток.",
        "The number of bytes put to the Kinesis stream using the `PutRecords` operation over the specified time period": "Количество байт, помещённых в поток Kinesis с помощью операции `PutRecords` за указанный период времени",
        "The time taken per `PutRecords` operation, measured over the specified time period": "Время, затраченное на одну операцию `PutRecords`, измеренное за указанный период времени",
        "The number of successful records in a `PutRecords` operation per Kinesis stream, measured over the specified time period": "Количество успешных записей в операции `PutRecords` на поток Kinesis, измеренное за указанный период времени",
        "The number of `PutRecords` operations where at least one record succeeded, per Kinesis stream, measured over the specified time period": "Количество операций `PutRecords`, в которых успешно выполнена хотя бы одна запись, на поток Kinesis, измеренное за указанный период времени",
        "The number of `GetRecords` calls throttled for the stream over the specified time period": "Количество вызовов `GetRecords`, подвергнутых регулированию для потока за указанный период времени",
        "The number of bytes received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes published in a single event for the specified time period.": "Количество байт, полученных из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты, опубликованные в одном событии за указанный период времени.",
        "The difference between the current time and when the last record of the `SubscribeToShard` event was written to the stream": "Разница между текущим временем и моментом, когда последняя запись события `SubscribeToShard` была записана в поток",
        "The number of records received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single event for the specified time period.": "Количество записей, полученных из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи в одном событии за указанный период времени.",
        "This metric is emitted every time an event is published successfully. Only emitted when there's an active subscription.": "Эта метрика отправляется каждый раз при успешной публикации события. Отправляется только при наличии активной подписки.",
        "This metric is emitted when a new subscription attempt fails because there already is an active subscription by the same consumer or if you exceed the number of calls per second allowed for this operation": "Эта метрика отправляется, когда новая попытка подписки завершается неудачей, потому что уже существует активная подписка от того же потребителя, или если превышено допустимое для этой операции количество вызовов в секунду",
        "The number of records rejected due to throttling for the stream over the specified time period. This metric includes throttling from `PutRecord` and `PutRecords` operations.": "Количество записей, отклонённых из-за регулирования для потока за указанный период времени. Эта метрика включает регулирование из операций `PutRecord` и `PutRecords`.",
    }
)

# ---- Amazon Kinesis Video Streams descriptions ----
RU.update(
    {
        "Latency of the `GetHLSMasterPlaylist` API calls for the given stream name": "Задержка вызовов API `GetHLSMasterPlaylist` для данного имени потока",
        "Number of `GetHLSMasterPlaylist` API requests for a given stream": "Количество запросов API `GetHLSMasterPlaylist` для данного потока",
        "The rate of success, `1` being the value for every successful request, and `0` the value for every failure": "Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою",
        "Latency of the `GetHLSMediaPlaylist` API calls for the given stream name": "Задержка вызовов API `GetHLSMediaPlaylist` для данного имени потока",
        "Number of `GetHLSMediaPlaylist` API requests for a given stream": "Количество запросов API `GetHLSMediaPlaylist` для данного потока",
        "Latency of the `GetHLSStreamingSessionURL` API calls for the given stream name": "Задержка вызовов API `GetHLSStreamingSessionURL` для данного имени потока",
        "Number of `GetHLSStreamingSessionURL` API requests for a given stream": "Количество запросов API `GetHLSStreamingSessionURL` для данного потока",
        "Latency of the `GetMP4InitFragment` API calls for the given stream name": "Задержка вызовов API `GetMP4InitFragment` для данного имени потока",
        "Number of `GetMP4InitFragment` API requests for a given stream": "Количество запросов API `GetMP4InitFragment` для данного потока",
        "Latency of the `GetMP4MediaFragment` API calls for the given stream name": "Задержка вызовов API `GetMP4MediaFragment` для данного имени потока",
        "Total number of bytes sent out from the service as part of the `GetMP4MediaFragment` API for a given stream": "Общее количество байт, отправленных из сервиса в рамках API `GetMP4MediaFragment` для данного потока",
        "Number of `GetMP4MediaFragment` API requests for a given stream": "Количество запросов API `GetMP4MediaFragment` для данного потока",
        "The number of connections that were not successfully established": "Количество соединений, которые не удалось успешно установить",
        "Total number of bytes sent out from the service as part of the `GetMediaForFragmentList` API for a given stream": "Общее количество байт, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока",
        "Total number of fragments sent out from the service as part of the `GetMediaForFragmentList` API for a given stream": "Общее количество фрагментов, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока",
        "Total number of frames sent out from the service as part of the `GetMediaForFragmentList` API for a given stream": "Общее количество кадров, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока",
        "Number of `GetMediaForFragmentList` API requests for a given stream": "Количество запросов API `GetMediaForFragmentList` для данного потока",
        "Time difference between the current server timestamp and the server timestamp of the last fragment sent": "Разница во времени между текущей серверной меткой времени и серверной меткой времени последнего отправленного фрагмента",
        "Total number of bytes sent out from the service as part of the `GetMedia` API for a given stream": "Общее количество байт, отправленных из сервиса в рамках API `GetMedia` для данного потока",
        "Number of fragments sent while doing `GetMedia` for the stream": "Количество фрагментов, отправленных при выполнении `GetMedia` для потока",
        "Number of frames sent during `GetMedia` on the given stream": "Количество кадров, отправленных во время `GetMedia` для данного потока",
        "Number of `GetMedia` API requests for a given stream": "Количество запросов API `GetMedia` для данного потока",
        "Latency of the `ListFragments` API calls for the given stream name": "Задержка вызовов API `ListFragments` для данного имени потока",
        "The total number of connections to the service host": "Общее количество подключений к хосту сервиса",
        "Time difference between when the first byte of a new fragment is received by Kinesis Video Streams and when the `Buffering ACK` is sent for the fragment": "Разница во времени между моментом, когда первый байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Buffering ACK`",
        "Errors while establishing `PutMedia` connection for the stream": "Ошибки при установлении соединения `PutMedia` для потока",
        "Number of Error ACKs sent while doing `PutMedia` for the stream": "Количество подтверждений Error ACK, отправленных при выполнении `PutMedia` для потока",
        "Time difference between when the first and last bytes of a fragment are received by Kinesis Video Streams": "Разница во времени между моментом, когда первый и последний байты фрагмента получены Kinesis Video Streams",
        "Time taken from when the complete fragment data is received and archived": "Время с момента получения и архивирования полных данных фрагмента",
        "Number of bytes received as part of `PutMedia` for the stream": "Количество байт, полученных в рамках `PutMedia` для потока",
        "Number of complete fragments received as part of `PutMedia` for the stream": "Количество полных фрагментов, полученных в рамках `PutMedia` для потока",
        "Number of complete frames received as part of `PutMedia` for the stream": "Количество полных кадров, полученных в рамках `PutMedia` для потока",
        "Time difference between the request and the HTTP response from `InletService` while establishing the connection": "Разница во времени между запросом и HTTP-ответом от `InletService` при установлении соединения",
        "Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Persisted ACK` is sent for the fragment": "Разница во времени между моментом, когда последний байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Persisted ACK`",
        "Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Received ACK` is sent for the fragment": "Разница во времени между моментом, когда последний байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Received ACK`",
        "Number of `PutMedia` API requests for a given stream": "Количество запросов API `PutMedia` для данного потока",
    }
)

# ---- frontmatter title (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams) monitoring": "Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)",
}


def main():
    bad = []
    for k, v in list(RU.items()) + list(ADD_TITLES.items()):
        if "—" in v:
            bad.append("EM-DASH: " + v[:60])
        if "â" in v or "﻿" in v:
            bad.append("MOJIBAKE/BOM: " + v[:60])
    if bad:
        for b in bad:
            print("  GUARD-FAIL:", b)
        return 1

    skel = json.load(open(SKEL_P, encoding="utf-8"))
    norm2ru = {asciinorm(k): v for k, v in RU.items()}
    if len(norm2ru) != len(RU):
        print("  WARN: asciinorm collision in RU keys")
    add_trans = {}
    unmatched_skel = []
    used = set()
    for k in skel:
        ak = asciinorm(k)
        if ak in norm2ru:
            add_trans[k] = norm2ru[ak]
            used.add(ak)
        else:
            unmatched_skel.append(k)
    unused_mine = [k for k in norm2ru if k not in used]

    print(f"skeleton keys: {len(skel)} | matched: {len(add_trans)}")
    if unmatched_skel:
        print(f"--- UNMATCHED skeleton keys ({len(unmatched_skel)}) ---")
        for k in unmatched_skel:
            print("  MISS:", k[:115])
    if unused_mine:
        print(f"--- UNUSED my translations ({len(unused_mine)}) ---")
        for k in unused_mine:
            print("  EXTRA:", k[:115])
    if unmatched_skel:
        print("ABORT: not all skeleton keys covered; fix before merging.")
        return 1

    def merge(path, add):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        before = len(d)
        d.update(add)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        print(
            f"{os.path.basename(path)}: {before} -> {len(d)} (+{len(d) - before} net; {len(add)} offered)"
        )

    if "--write" in sys.argv:
        merge(TRANS_P, add_trans)
        merge(TITLE_P, ADD_TITLES)
        print("done")
    else:
        print("DRY-OK (pass --write to merge into dicts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
