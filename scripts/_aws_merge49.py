# -*- coding: utf-8 -*-
"""Merge L4-IF.49 batch (5 standard AWS storage/network files: EBS (new), S3,
Storage Gateway, Transit Gateway, Elasticsearch Service (ES)) translations into
the shared cumulative dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Same mechanism as L4-IF.45/46/47/48: translations keyed by an ASCII-normalized
form of the EN text, matched against the real skeleton keys programmatically.
asciinorm also folds markdown escapes (\\_ \\*) and curly/dash punctuation. Any
skeleton key left without a translation, or any translation matching no skeleton
key, is reported (self-validation against typos). Asserts: no em-dash, no
mojibake in RU. Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if49.json")


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


# ---- intro template (verbatim shipped canon V1, service name swapped) ----
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

# ---- intros (all form V1) ----
for name in [
    "Amazon EBS",
    "Amazon Simple Storage Service (Amazon S3)",
    "AWS Storage Gateway",
    "AWS Transit Gateway",
    "Amazon Elasticsearch Service (ES)",
]:
    RU[en_v1(name)] = ru_v1(name)

# ---- EBS (new) ----
RU.update(
    {
        "# Amazon EBS (Elastic Block Store) monitoring": "# Мониторинг Amazon EBS (Elastic Block Store)",
        "* Updated on Apr 08, 2025": "* Обновлено 8 апреля 2025 г.",
        "This service monitors a part of Amazon EBS (AWS/EBS). While you have this service configured, you can't have Amazon EBS (built-in) service turned on.": "Этот сервис отслеживает часть Amazon EBS (AWS/EBS). Пока этот сервис настроен, нельзя включить сервис Amazon EBS (built-in).",
        "`VolumeId` is the main dimension.": "Основное измерение: `VolumeId`.",
        "Provides information about the percentage of I/O credits (for `gp2`) or throughput credits (for `st1` and `sc1`) remaining in the burst bucket.": "Предоставляет информацию о проценте кредитов ввода-вывода (для `gp2`) или кредитов пропускной способности (для `st1` и `sc1`), оставшихся в корзине всплеска.",
        "Provides information about the percentage of throughput credits remaining in the burst bucket.": "Предоставляет информацию о проценте кредитов пропускной способности, оставшихся в корзине всплеска.",
        "Provides information about the percentage of I/O credits remaining in the burst bucket.": "Предоставляет информацию о проценте кредитов ввода-вывода, оставшихся в корзине всплеска.",
        "Bytes read from all EBS volumes attached to the instance in a specified period of time.": "Количество байт, прочитанных со всех томов EBS, подключённых к экземпляру, за указанный период времени.",
        "Completed read operations from all Amazon EBS volumes attached to the instance in a specified period of time.": "Количество завершённых операций чтения со всех томов Amazon EBS, подключённых к экземпляру, за указанный период времени.",
        "Bytes written to all EBS volumes attached to the instance in a specified period of time.": "Количество байт, записанных на все тома EBS, подключённые к экземпляру, за указанный период времени.",
        # source quirk: ReadOps says "Amazon EBS volumes", WriteOps says "EBS volumes" (no "Amazon") -> mirror EN
        "Completed write operations to all EBS volumes attached to the instance in a specified period of time.": "Количество завершённых операций записи на все тома EBS, подключённые к экземпляру, за указанный период времени.",
        "The number of volume create credits available. This metric is reported per snapshot per Availability Zone.": "Количество доступных кредитов создания тома. Эта метрика регистрируется для каждого моментального снимка в каждой зоне доступности.",
        "The maximum number of volume create credits that can be accumulated. This metric is reported per snapshot per Availability Zone.": "Максимальное количество кредитов создания тома, которое может быть накоплено. Эта метрика регистрируется для каждого моментального снимка в каждой зоне доступности.",
        "The total amount of read and write operations (normalized to 256K capacity units) consumed in a specified period of time.": "Общее количество операций чтения и записи (нормализованных к единицам ёмкости по 256 КБ), потреблённых за указанный период времени.",
        "The total number of seconds in a specified period of time when no read or write operations were submitted.": "Общее количество секунд за указанный период времени, когда не было отправлено ни одной операции чтения или записи.",
        "The number of read and write operation requests waiting to be completed in a specified period of time.": "Количество запросов на операции чтения и записи, ожидающих завершения за указанный период времени.",
        "Provides information on the read operations in a specified period of time.": "Предоставляет информацию об операциях чтения за указанный период времени.",
        "The total number of read operations in a specified period of time.": "Общее количество операций чтения за указанный период времени.",
        "The percentage of I/O operations per second (IOPS) delivered of the total IOPS provisioned for an Amazon EBS volume.": "Процент операций ввода-вывода в секунду (IOPS), обеспеченных от общего числа IOPS, подготовленных для тома Amazon EBS.",
        "The total number of seconds spent by all read operations that completed in a specified period of time.": "Общее количество секунд, затраченных всеми операциями чтения, завершившимися за указанный период времени.",
        "The total number of seconds spent by all write operations that completed in a specified period of time.": "Общее количество секунд, затраченных всеми операциями записи, завершившимися за указанный период времени.",
        "Provides information on the write operations in a specified period of time.": "Предоставляет информацию об операциях записи за указанный период времени.",
        "The total number of write operations in a specified period of time.": "Общее количество операций записи за указанный период времени.",
    }
)

# ---- S3 ----
RU.update(
    {
        "# Amazon S3 (Simple Storage Service) monitoring": "# Мониторинг Amazon S3 (Simple Storage Service)",
        "* A request metrics filter for the buckets you want to monitor. For more information, see [Creating a request metrics filter for an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/configure-metrics.html) in [AWS documentation](https://dt-url.net/aw030yi).": "* Фильтр метрик запросов для корзин, которые требуется отслеживать. Дополнительные сведения см. в разделе [Создание фильтра метрик запросов для корзины S3](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/configure-metrics.html) в [документации AWS](https://dt-url.net/aw030yi).",
        "To monitor S3 metrics, you need to select **Amazon S3 service**, otherwise Amazon S3 (built-in) will provide only a basic count of S3 buckets in your account.": "Чтобы отслеживать метрики S3, нужно выбрать **Amazon S3 service**, иначе Amazon S3 (built-in) предоставит только базовый подсчёт корзин S3 в вашем аккаунте.",
        "By default, request metrics **aren't** reported. To have them reported, you need to enable them in the **AWS S3** console.": "По умолчанию метрики запросов **не** регистрируются. Чтобы они регистрировались, необходимо включить их в консоли **AWS S3**.",
        "`BucketName` is the main dimension.": "Основное измерение: `BucketName`.",
        "The total number of HTTP requests made to an Amazon S3 bucket, regardless of type": "Общее количество HTTP-запросов к корзине Amazon S3, независимо от типа",
        "The number of bytes downloaded for requests made to an Amazon S3 bucket, where the response includes a body": "Количество байт, скачанных по запросам к корзине Amazon S3, для которых ответ содержит тело",
        "The number of bytes uploaded that contain a request body, made to an Amazon S3 bucket": "Количество отправленных байт, содержащих тело запроса, для запросов к корзине Amazon S3",
        "The number of HTTP DELETE requests made for objects in an Amazon S3 bucket (includes Delete multiple objects requests).": "Количество HTTP-запросов DELETE к объектам в корзине Amazon S3 (включая запросы на удаление нескольких объектов).",
        "Per request, the time from when the Amazon S3 bucket receives the complete request to when the response starts to be returned": "Время от момента получения корзиной Amazon S3 полного запроса до момента начала возврата ответа, в расчёте на один запрос",
        "The number of HTTP GET requests made for objects in an Amazon S3 bucket (doesn't include list operations)": "Количество HTTP-запросов GET к объектам в корзине Amazon S3 (не включает операции получения списка)",
        "The number of HTTP HEAD requests made to an Amazon S3 bucket": "Количество HTTP-запросов HEAD к корзине Amazon S3",
        "The number of HTTP requests that list the contents of a bucket": "Количество HTTP-запросов, возвращающих содержимое корзины",
        "The number of HTTP POST requests made to an Amazon S3 bucket": "Количество HTTP-запросов POST к корзине Amazon S3",
        "The number of HTTP PUT requests made for objects in an Amazon S3 bucket": "Количество HTTP-запросов PUT к объектам в корзине Amazon S3",
        "The number of Amazon S3 SelectObjectContent requests made for objects in an Amazon S3 bucket": "Количество запросов Amazon S3 SelectObjectContent к объектам в корзине Amazon S3",
        "The number of bytes of data returned with Amazon S3 SelectObjectContent requests in an Amazon S3 bucket": "Количество байт данных, возвращённых по запросам Amazon S3 SelectObjectContent в корзине Amazon S3",
        "The number of bytes of data scanned with Amazon S3 SelectObjectContent requests in an Amazon S3 bucket": "Количество байт данных, просканированных по запросам Amazon S3 SelectObjectContent в корзине Amazon S3",
        "The time per request, starting from the first byte received to the last byte sent to an Amazon S3 bucket. This includes the time taken to receive the request body and send the response body, which is not included in FirstByteLatency.": "Время на один запрос, отсчитываемое от первого полученного байта до последнего байта, отправленного в корзину Amazon S3. Включает время на получение тела запроса и отправку тела ответа, которое не учитывается в FirstByteLatency.",
        "The number of HTTP 4xx client error status code requests made to an Amazon S3 bucket with a value of either 0 or 1. The average statistic shows the error rate, and the sum statistic shows the count of that type of error, during each period.": "Количество запросов к корзине Amazon S3 с кодом состояния ошибки клиента HTTP 4xx, со значением 0 или 1. Статистика average показывает частоту ошибок, а статистика sum показывает количество ошибок этого типа за каждый период.",
        "The number of HTTP 5xx server error status code requests made to an Amazon S3 bucket with a value of either 0 or 1. The average statistic shows the error rate, and the sum statistic shows the count of that type of error, during each period.": "Количество запросов к корзине Amazon S3 с кодом состояния ошибки сервера HTTP 5xx, со значением 0 или 1. Статистика average показывает частоту ошибок, а статистика sum показывает количество ошибок этого типа за каждый период.",
    }
)

# ---- Storage Gateway ----
RU.update(
    {
        "# AWS Storage Gateway monitoring": "# Мониторинг AWS Storage Gateway",
        "* 6-min read": "* Чтение: 6 мин",
        "`GatewayName` is the main dimension.": "Основное измерение: `GatewayName`.",
        "The total number of bytes available in the gateway's cache storage": "Общее количество байт, доступных в кэш-хранилище шлюза",
        "Percentage of application reads served from the cache": "Процент операций чтения приложений, обслуженных из кэша",
        # source quirk: em-dash mis-scraped; key uses ASCII hyphen (asciinorm folds), value avoids em-dash (rule 0)
        "Percentage of the cache that is dirty-that is, it contains content that has not been uploaded to AWS": "Процент кэша, являющегося «грязным», то есть содержащего данные, которые ещё не были выгружены в AWS",
        "Percentage of the gateway's cache storage being used": "Процент используемого кэш-хранилища шлюза",
        "The total number of bytes being used in the gateway's cache storage": "Общее количество байт, используемых в кэш-хранилище шлюза",
        "The total number of bytes that the gateway sent to the cloud during the reporting period. This metric includes the activity of all the volumes on the gateway.": "Общее количество байт, отправленных шлюзом в облако за отчётный период. Эта метрика включает активность всех томов на шлюзе.",
        "The total number of bytes that the gateway sent to the cloud during the reporting period": "Общее количество байт, отправленных шлюзом в облако за отчётный период",
        "The latency in downloading the data from the cloud to the gateway": "Задержка при скачивании данных из облака на шлюз",
        "The number of files for which metadata was fetched": "Количество файлов, для которых были получены метаданные",
        "Percentage of time that the gateway is waiting on a response from the local disk": "Процент времени, в течение которого шлюз ожидает ответа от локального диска",
        "Amount of RAM provisioned to the gateway VM, in bytes": "Объём ОЗУ, выделенного виртуальной машине шлюза, в байтах",
        "Amount of RAM currently in use by the gateway VM, in bytes": "Объём ОЗУ, используемого в данный момент виртуальной машиной шлюза, в байтах",
        "The number of NFS session that are active on the gateway": "Количество сеансов NFS, активных на шлюзе",
        "The number of bytes waiting to be written to AWS, sampled at the end of the reporting period for all volumes in the gateway": "Количество байт, ожидающих записи в AWS, замеренное в конце отчётного периода по всем томам шлюза",
        "The total number of bytes read from your on-premises applications in the reporting period for all volumes in the gateway": "Общее количество байт, прочитанных из ваших локальных приложений за отчётный период по всем томам шлюза",
        "The total number of milliseconds spent on read operations from your on-premises applications in the reporting period for all volumes in the gateway": "Общее количество миллисекунд, затраченных на операции чтения из ваших локальных приложений за отчётный период по всем томам шлюза",
        "The number of Server Message Block (SMB) version 1 sessions that are active on the gateway": "Количество сеансов Server Message Block (SMB) версии 1, активных на шлюзе",
        "The number of SMB version 2 sessions that are active on the gateway": "Количество сеансов SMB версии 2, активных на шлюзе",
        "The number of SMB version 3 sessions that are active on the gateway": "Количество сеансов SMB версии 3, активных на шлюзе",
        "The time since the last available recovery point": "Время, прошедшее с момента последней доступной точки восстановления",
        "The total size of the cache in bytes": "Общий размер кэша в байтах",
        "Percentage of the gateway's upload buffer used": "Процент использования буфера выгрузки шлюза",
        "The total number of bytes being used in the gateway's upload buffer": "Общее количество байт, используемых в буфере выгрузки шлюза",
        "Percentage of CPU time spent on gateway processing, averaged across all cores": "Процент времени CPU, затраченного на обработку шлюзом, усреднённый по всем ядрам",
        "The total amount of unused space in the gateway's working storage": "Общий объём неиспользуемого пространства в рабочем хранилище шлюза",
        # source quirk: WriteBytes says "to ... applications", WriteTime says "from ... applications" (EN inconsistent) -> mirror each
        "The total number of bytes written to your on-premises applications in the reporting period for all volumes in the gateway": "Общее количество байт, записанных в ваши локальные приложения за отчётный период по всем томам шлюза",
        "The total number of milliseconds spent on write operations from your on-premises applications in the reporting period for all volumes in the gateway": "Общее количество миллисекунд, затраченных на операции записи из ваших локальных приложений за отчётный период по всем томам шлюза",
    }
)

# ---- Transit Gateway ----
RU.update(
    {
        "# AWS Transit Gateway monitoring": "# Мониторинг AWS Transit Gateway",
        "TransitGateway is a cross-account service, meaning multiple accounts may monitor one TransitGateway. Dynatrace keeps metrics separate for each monitored account that monitors the same TransitGateway instance.": "TransitGateway является межаккаунтным сервисом: один экземпляр TransitGateway могут отслеживать несколько аккаунтов. Dynatrace хранит метрики раздельно для каждого отслеживаемого аккаунта, который отслеживает один и тот же экземпляр TransitGateway.",
        "`TransitGateway` is the main dimension.": "Основное измерение: `TransitGateway`.",
        "The number of bytes dropped because they matched a black hole route": "Количество байт, отброшенных из-за соответствия маршруту чёрной дыры",
        "The number of bytes dropped because they did not match a route": "Количество байт, отброшенных из-за несоответствия ни одному маршруту",
        "The number of bytes received by the transit gateway": "Количество байт, полученных транзитным шлюзом",
        "The number of packets sent by the transit gateway": "Количество пакетов, отправленных транзитным шлюзом",
        "The number of `IGMP Join` messages received by the transit gateway": "Количество сообщений `IGMP Join`, полученных транзитным шлюзом",
        "The number of `IGMP Query` messages received by the transit gateway": "Количество сообщений `IGMP Query`, полученных транзитным шлюзом",
        "The number of `IGMP Leave` messages received by the transit gateway": "Количество сообщений `IGMP Leave`, полученных транзитным шлюзом",
        "The number of multicast bytes received by the transit gateway": "Количество многоадресных байт, полученных транзитным шлюзом",
        "The number of multicast bytes sent from the transit gateway": "Количество многоадресных байт, отправленных транзитным шлюзом",
        "The number of multicast packets dropped": "Количество отброшенных многоадресных пакетов",
        "The number of multicast packets received by the transit gateway": "Количество многоадресных пакетов, полученных транзитным шлюзом",
        "The number of multicast packets sent by the transit gateway": "Количество многоадресных пакетов, отправленных транзитным шлюзом",
        "The number of multicast domains configured on the transit gateway": "Количество многоадресных доменов, настроенных на транзитном шлюзе",
        "The number of multicast group members configured on the transit gateway": "Количество членов многоадресных групп, настроенных на транзитном шлюзе",
        "The number of packets dropped because they matched a black hole route": "Количество пакетов, отброшенных из-за соответствия маршруту чёрной дыры",
        "The number of packets dropped because they did not match a route": "Количество пакетов, отброшенных из-за несоответствия ни одному маршруту",
        "The number of packets received by the transit gateway": "Количество пакетов, полученных транзитным шлюзом",
    }
)

# ---- Elasticsearch Service (ES) ----
RU.update(
    {
        "# Amazon ES (Elasticsearch Service) monitoring": "# Мониторинг Amazon ES (Elasticsearch Service)",
        "The number of failed automated snapshots for the cluster. A value of `1` indicates that no automated snapshot of the domain has been taken for the last 36 hours.": "Количество неудавшихся автоматических моментальных снимков кластера. Значение `1` указывает на то, что за последние 36 часов не было создано ни одного автоматического моментального снимка домена.",
        "The remaining CPU credits available for data nodes in the cluster. A CPU credit provides the performance of a full CPU core for one minute. This metric is available only for the T2 instance types.": "Оставшиеся кредиты CPU, доступные для узлов данных в кластере. Кредит CPU обеспечивает производительность полного ядра CPU в течение одной минуты. Эта метрика доступна только для типов экземпляров T2.",
        "The percentage of CPU usage for data nodes in the cluster. Maximum shows the node with the highest CPU usage. Average represents all nodes in the cluster. This metric is also available for individual nodes.": "Процент использования CPU узлами данных в кластере. Maximum показывает узел с наибольшим использованием CPU. Average представляет все узлы в кластере. Эта метрика также доступна для отдельных узлов.",
        "Indicates whether your cluster is accepting or blocking incoming write requests. A value of `0` means that the cluster is accepting requests. A value of `1` means that the cluster is blocking requests.": "Указывает, принимает или блокирует ваш кластер входящие запросы на запись. Значение `0` означает, что кластер принимает запросы. Значение `1` означает, что кластер блокирует запросы.",
        "A value of `1` indicates that all index shards are allocated to nodes in the cluster": "Значение `1` указывает на то, что все шарды индексов размещены на узлах в кластере",
        "A value of `1` indicates that the primary and replica shards for at least one index aren't allocated to nodes in the cluster": "Значение `1` указывает на то, что первичные шарды и шарды-реплики хотя бы для одного индекса не размещены на узлах в кластере",
        "A value of `1` indicates that the primary shards for all indices are allocated to nodes in the cluster, but replica shards for at least one index aren't allocated to nodes in the cluster": "Значение `1` указывает на то, что первичные шарды для всех индексов размещены на узлах в кластере, но шарды-реплики хотя бы для одного индекса не размещены на узлах в кластере",
        "The total used space for the cluster": "Общее используемое пространство кластера",
        "The total number of documents marked for deletion across all data nodes in the cluster. These documents no longer appear in search results, but Elasticsearch only removes deleted documents from disk during segment merges. This metric increases after delete requests and decreases after segment merges.": "Общее количество документов, помеченных для удаления, по всем узлам данных в кластере. Эти документы больше не появляются в результатах поиска, но Elasticsearch удаляет удалённые документы с диска только во время слияний сегментов. Эта метрика увеличивается после запросов на удаление и уменьшается после слияний сегментов.",
        "The number of pending input and output (I/O) requests for an EBS volume": "Количество ожидающих запросов ввода-вывода (I/O) для тома EBS",
        "The number of requests made to the Elasticsearch cluster": "Количество запросов к кластеру Elasticsearch",
        "The free space for data nodes in the cluster": "Свободное пространство для узлов данных в кластере",
        "The number of HTTP requests made to the Elasticsearch cluster that included an invalid (or missing) host header": "Количество HTTP-запросов к кластеру Elasticsearch, содержавших недопустимый (или отсутствующий) заголовок host",
        "The maximum percentage of the Java heap used for all data nodes in the cluster": "Максимальный процент кучи Java, используемой всеми узлами данных в кластере",
        "A value of `1` indicates that the KMS customer master key used to encrypt data at rest has been disabled": "Значение `1` указывает на то, что главный ключ клиента KMS, используемый для шифрования данных в состоянии покоя, был отключён",
        "A value of `1` indicates that the KMS customer master key used to encrypt data at rest has been deleted or revoked its grants to Amazon ES": "Значение `1` указывает на то, что главный ключ клиента KMS, используемый для шифрования данных в состоянии покоя, был удалён или его разрешения для Amazon ES были отозваны",
        "A health check for Kibana. A value of `1` indicates normal behavior. A value of `0` indicates that Kibana is inaccessible. In most cases, the health of Kibana mirrors the health of the cluster.": "Проверка работоспособности Kibana. Значение `1` указывает на нормальное поведение. Значение `0` указывает на то, что Kibana недоступна. В большинстве случаев работоспособность Kibana отражает работоспособность кластера.",
        "The remaining CPU credits available for dedicated master nodes in the cluster. A CPU credit provides the performance of a full CPU core for one minute.": "Оставшиеся кредиты CPU, доступные для выделенных мастер-узлов в кластере. Кредит CPU обеспечивает производительность полного ядра CPU в течение одной минуты.",
        "The maximum percentage of CPU resources used by the dedicated master nodes": "Максимальный процент ресурсов CPU, используемых выделенными мастер-узлами",
        "The maximum percentage of the Java heap used for all dedicated master nodes in the cluster": "Максимальный процент кучи Java, используемой всеми выделенными мастер-узлами в кластере",
        # source quirk: malformed code-span `/\_cluster/health/`` (stray double backtick + escaped underscore) mirrored byte-for-byte
        "A health check for MasterNotDiscovered exceptions. A value of `1` indicates normal behavior. A value of `0` indicates that `/\\_cluster/health/`` is failing.": "Проверка работоспособности для исключений MasterNotDiscovered. Значение `1` указывает на нормальное поведение. Значение `0` указывает на то, что `/\\_cluster/health/`` не работает.",
        "The number of nodes in the Amazon ES cluster, including dedicated master nodes and UltraWarm nodes": "Количество узлов в кластере Amazon ES, включая выделенные мастер-узлы и узлы UltraWarm",
        "The number of input and output (I/O) operations per second for read operations on EBS volumes": "Количество операций ввода-вывода (I/O) в секунду для операций чтения на томах EBS",
        "The latency for read operations on EBS volumes": "Задержка операций чтения на томах EBS",
        "The throughput for read operations on EBS volumes": "Пропускная способность операций чтения на томах EBS",
        "The total number of searchable documents across all data nodes in the cluster": "Общее количество документов, доступных для поиска, по всем узлам данных в кластере",
        "The number of input and output (I/O) operations per second for write operations on EBS volumes": "Количество операций ввода-вывода (I/O) в секунду для операций записи на томах EBS",
        "The latency for write operations on EBS volumes": "Задержка операций записи на томах EBS",
        "The throughput for write operations on EBS volumes": "Пропускная способность операций записи на томах EBS",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon EBS (Elastic Block Store) monitoring": "Мониторинг Amazon EBS (Elastic Block Store)",
    "Amazon S3 (Simple Storage Service) monitoring": "Мониторинг Amazon S3 (Simple Storage Service)",
    "AWS Storage Gateway monitoring": "Мониторинг AWS Storage Gateway",
    "AWS Transit Gateway monitoring": "Мониторинг AWS Transit Gateway",
    "Amazon ES (Elasticsearch Service) monitoring": "Мониторинг Amazon ES (Elasticsearch Service)",
}


def main():
    # guard: no em-dash, no mojibake in any RU value
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
    for k in skel:  # k = real skeleton key (byte-identical with EN source)
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
