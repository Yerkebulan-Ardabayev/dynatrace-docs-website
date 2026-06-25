# -*- coding: utf-8 -*-
"""Merge L4-IF.47 batch (6 standard AWS DB-family files: Aurora, DocumentDB,
DynamoDB Accelerator (DAX), ElastiCache, Keyspaces (Cassandra), Neptune)
translations into the shared cumulative dicts (_aws_trans_l4if43.json +
_aws_titles_l4if43.json).

Same mechanism as L4-IF.45/46: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. asciinorm
also folds markdown escapes (\\_ \\*) and curly punctuation so RU keys can be
written with plain ASCII underscores/quotes (the STORED key stays the real
skeleton key, byte-identical with the EN source). Any skeleton key left without a
translation, or any translation matching no skeleton key, is reported
(self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if47.json")


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


# ---- intro templates (verbatim shipped canon, service name swapped) ----
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


def en_v2(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view graphs per service instance, with a set of dimensions, and create custom graphs "
        "that you can pin to your dashboards." % s
    )


def ru_v2(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать графики по каждому экземпляру сервиса с набором измерений и создавать "
        "собственные графики, которые можно закреплять на дашбордах." % s
    )


RU = {}

# intros: V1 for all except DocumentDB (V2)
for svc in [
    "Amazon Aurora",
    "Amazon DynamoDB Accelerator (DAX)",
    "Amazon ElastiCache",
    "Amazon Keyspaces",
    "Amazon Neptune",
]:
    RU[en_v1(svc)] = ru_v1(svc)
RU[en_v2("Amazon DocumentDB")] = ru_v2("Amazon DocumentDB")

# H1 headings (body, with leading "# ")
RU.update(
    {
        "# Amazon Aurora monitoring": "# Мониторинг Amazon Aurora",
        "# Amazon DocumentDB (with MongoDB compatibility) monitoring": "# Мониторинг Amazon DocumentDB (with MongoDB compatibility)",
        "# Amazon DynamoDB Accelerator (DAX) monitoring": "# Мониторинг Amazon DynamoDB Accelerator (DAX)",
        "# Amazon ElastiCache monitoring": "# Мониторинг Amazon ElastiCache",
        "# Amazon Keyspaces (Cassandra) monitoring": "# Мониторинг Amazon Keyspaces (Cassandra)",
        "# Amazon Neptune monitoring": "# Мониторинг Amazon Neptune",
    }
)

# read-time bullets
RU.update(
    {
        "* 22-min read": "* Чтение: 22 мин",
        "* 7-min read": "* Чтение: 7 мин",
        "* 12-min read": "* Чтение: 12 мин",
        "* 13-min read": "* Чтение: 13 мин",
        "* 11-min read": "* Чтение: 11 мин",
    }
)

# main-dimension notes
for dim in ["DBClusterIdentifier", "ClusterId", "CacheClusterId", "Keyspace"]:
    RU["`%s` is the main dimension." % dim] = "Основное измерение: `%s`." % dim

# ---- special prose ----
RU.update(
    {
        "This service monitors Amazon RDS clusters. You can find the already monitored resources on the AWS overview page in the **Cloud services** section.": "Этот сервис отслеживает кластеры Amazon RDS. Уже отслеживаемые ресурсы можно найти на странице обзора AWS в разделе **Cloud services**.",
        "To monitor RDS instances instead, check the Amazon RDS and the **RDS** section on the AWS overview page.": "Чтобы вместо этого отслеживать экземпляры RDS, см. Amazon RDS и раздел **RDS** на странице обзора AWS.",
        "Only metrics from `AWS/DocDB` namespace are supported.": "Поддерживаются только метрики из пространства имён `AWS/DocDB`.",
        "* Any version of ActiveGate in both Dynatrace SaaS and Managed deployments.": "* Любая версия ActiveGate в развёртываниях Dynatrace SaaS и Managed.",
        "* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.": "* Чтобы отключить мониторинг встроенных сервисов, требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.",
        "* There is no API for this service. Tagging is available on the custom devices (keyspaces) as it uses a separate Amazon API.": "* Для этого сервиса нет API. Тегирование доступно на пользовательских устройствах (keyspaces), так как используется отдельный API Amazon.",
        'For role-based access (whether in a [SaaS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#role-based-access "Connect your Amazon account with Dynatrace Managed and start monitoring.") deployment), you need an ActiveGate installed on an Amazon EC2 host.': 'Для доступа на основе ролей (в развёртывании [SaaS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Приём метрик Amazon CloudWatch.") или [Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#role-based-access "Подключите аккаунт Amazon к Dynatrace Managed и начните мониторинг.")) требуется ActiveGate, установленный на хосте Amazon EC2.',
    }
)

# ---- Aurora metric cells ----
RU.update(
    {
        "The average number of current transactions executing on an Aurora database instance per second": "Среднее количество текущих транзакций, выполняемых на экземпляре базы данных Aurora, в секунду",
        "The amount of time a replica DB cluster running on Aurora with MySQL compatibility lags behind the source DB cluster": "Время, на которое реплика кластера БД, работающая на Aurora с совместимостью MySQL, отстаёт от исходного кластера БД",
        "The maximum amount of lag between the primary instance and each Aurora DB instance in the DB cluster": "Максимальная величина отставания между первичным экземпляром и каждым экземпляром БД Aurora в кластере БД",
        "For an Aurora replica, the amount of lag when replicating updates from the primary instance": "Для реплики Aurora: величина отставания при репликации обновлений с первичного экземпляра",
        "The number of backtrack change records created over 5 minutes for your DB cluster": "Количество записей изменений backtrack, созданных за 5 минут для вашего кластера БД",
        "The number of backtrack change records used by your DB cluster": "Количество записей изменений backtrack, использованных вашим кластером БД",
        "The difference between the target backtrack window and the actual backtrack window": "Разница между целевым окном backtrack и фактическим окном backtrack",
        "The number of times that the actual backtrack window is smaller than the target backtrack window for a given period of time": "Количество случаев, когда фактическое окно backtrack меньше целевого окна backtrack за заданный период времени",
        "The amount of disk space occupied by binary logs on the primary instance": "Объём дискового пространства, занятого двоичными журналами на первичном экземпляре",
        "The average number of transactions in the database that are blocked per second": "Среднее количество транзакций в базе данных, заблокированных в секунду",
        "The percentage of requests that are served by the buffer cache": "Процент запросов, обслуженных буферным кэшем",
        "The number of CPU credits that an instance has accumulated, reported at 5-minute intervals. This metric applies only to `db.t2.small` and `db.t2.medium` instances. You can use this metric to determine how long an Aurora MySQL DB instance can burst beyond its baseline performance level at a given rate.": "Количество кредитов CPU, накопленных экземпляром; регистрируется с интервалом в 5 минут. Эта метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. С помощью этой метрики можно определить, как долго экземпляр БД Aurora MySQL может работать в режиме всплеска сверх базового уровня производительности при заданной интенсивности.",
        "The number of CPU credits consumed during the specified period, reported at 5-minute intervals. This metric applies only to `db.t2.small` and `db.t2.medium` instances. This metric measures the amount of time during which physical CPUs have been used for processing instructions by virtual CPUs allocated to the Aurora MySQL DB instance.": "Количество кредитов CPU, израсходованных за указанный период; регистрируется с интервалом в 5 минут. Эта метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. Эта метрика измеряет количество времени, в течение которого физические CPU использовались для обработки инструкций виртуальными CPU, выделенными экземпляру БД Aurora MySQL.",
        "The percentage of CPU used by an Aurora DB instance": "Процент CPU, используемого экземпляром БД Aurora",
        "The latency for commit operations": "Задержка операций фиксации",
        "The average number of commit operations per second": "Среднее количество операций фиксации в секунду",
        "The latency for data definition language (DDL) requests such as example, create, alter, and drop requests": "Задержка запросов языка определения данных (DDL), например запросов create, alter и drop",
        "The average number of DDL requests per second": "Среднее количество запросов DDL в секунду",
        "The latency for inserts, updates, and deletes": "Задержка операций вставки, обновления и удаления",
        "The average number of inserts, updates, and deletes per second": "Среднее количество операций вставки, обновления и удаления в секунду",
        "The number of connections to an Aurora DB instance": "Количество подключений к экземпляру БД Aurora",
        "The average number of deadlocks in the database per second": "Среднее количество взаимоблокировок в базе данных в секунду",
        "The latency for delete queries": "Задержка запросов удаления",
        "The average number of delete queries per second": "Среднее количество запросов удаления в секунду",
        "The number of outstanding read/write requests waiting to access the disk": "Количество незавершённых запросов чтения/записи, ожидающих доступа к диску",
        "The amount of time that the instance has been running": "Время работы экземпляра",
        "The amount of local storage available for each DB instance.": "Объём локального хранилища, доступного для каждого экземпляра БД.",
        "The amount of available random access memory": "Объём доступной оперативной памяти",
        "The latency for insert queries": "Задержка запросов вставки",
        "The average number of insert queries per second": "Среднее количество запросов вставки в секунду",
        "The average number of failed login attempts per second": "Среднее количество неудачных попыток входа в секунду",
        "The age of the oldest unvacuumed transaction ID in transactions. If this value reaches `2`,`146`,`483`,`648` (2^31 - 1,000,000), the database is forced into read-only mode, to avoid transaction ID wraparound.": "Возраст самого старого неочищенного идентификатора транзакции, в транзакциях. Если это значение достигает `2`,`146`,`483`,`648` (2^31 - 1 000 000), база данных принудительно переводится в режим только для чтения во избежание зацикливания идентификаторов транзакций.",
        "The amount of network throughput received from clients by each instance in the Aurora MySQL DB cluster. This throughput doesn't include network traffic between instances in the Aurora DB cluster and the cluster volume.": "Объём сетевой пропускной способности, полученной от клиентов каждым экземпляром в кластере БД Aurora MySQL. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД Aurora и томом кластера.",
        "The amount of network throughput both received from and transmitted to clients by each instance in the Aurora MySQL DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.": "Объём сетевой пропускной способности, как полученной от клиентов, так и переданной им каждым экземпляром в кластере БД Aurora MySQL. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера.",
        "The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.": "Объём сетевой пропускной способности, отправленной клиентам каждым экземпляром в кластере БД Aurora. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера.",
        "The average number of queries executed per second": "Среднее количество запросов, выполненных в секунду",
        "The lag when replicating updates from the primary RDS PostgreSQL instance to other nodes in the cluster": "Отставание при репликации обновлений с первичного экземпляра RDS PostgreSQL на другие узлы в кластере",
        "The average number of disk I/O operations per second": "Среднее количество дисковых операций ввода-вывода в секунду",
        "The average amount of time taken per disk I/O operation": "Среднее время, затрачиваемое на одну дисковую операцию ввода-вывода",
        "The percentage of requests that are served by the resultset cache": "Процент запросов, обслуженных кэшем результирующих наборов",
        "The latency for select queries": "Задержка запросов выборки",
        "The average number of select queries per second": "Среднее количество запросов выборки в секунду",
        "The amount of swap space used on the Aurora PostgreSQL DB instance": "Объём пространства подкачки, используемого на экземпляре БД Aurora PostgreSQL",
        "The amount of disk space consumed by transaction logs on the Aurora PostgreSQL DB instance. This metric is only generated when Aurora PostgreSQL is using logical replication or AWS Database Migration Service. By default, Aurora PostgreSQL uses log records, not transaction logs. When transaction logs aren't in use, the value for this metric is -1.": "Объём дискового пространства, занятого журналами транзакций на экземпляре БД Aurora PostgreSQL. Эта метрика формируется только тогда, когда Aurora PostgreSQL использует логическую репликацию или AWS Database Migration Service. По умолчанию Aurora PostgreSQL использует записи журнала, а не журналы транзакций. Когда журналы транзакций не используются, значение этой метрики равно -1.",
        "The latency for update queries": "Задержка запросов обновления",
        "The average number of update queries per second": "Среднее количество запросов обновления в секунду",
        "The amount of storage used by your Aurora DB instance. This value affects the cost of the Aurora DB cluster.": "Объём хранилища, используемого вашим экземпляром БД Aurora. Это значение влияет на стоимость кластера БД Aurora.",
        "The number of billed read I/O operations from a cluster volume within a 5-minute interval": "Количество оплачиваемых операций ввода-вывода чтения из тома кластера за 5-минутный интервал",
        "The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals": "Количество дисковых операций ввода-вывода записи в том кластера; регистрируется с интервалом в 5 минут",
        "The average number of bytes written to disk": "Среднее количество байт, записанных на диск",
    }
)

# ---- DocumentDB metric cells ----
RU.update(
    {
        "The total amount of backup storage in GiB used to support the point-in-time restore feature within the Amazon DocumentDB's retention window": "Общий объём хранилища резервных копий в ГиБ, используемого для поддержки функции восстановления на момент времени в пределах окна хранения Amazon DocumentDB",
        "The percentage of CPU used by an instance": "Процент CPU, используемого экземпляром",
        "The amount of storage used by your cluster to store the change stream log in megabytes": "Объём хранилища, используемого вашим кластером для хранения журнала потока изменений, в мегабайтах",
        "The maximum amount of lag, in milliseconds, between the primary instance and each Amazon DocumentDB instance in the cluster": "Максимальная величина отставания в миллисекундах между первичным экземпляром и каждым экземпляром Amazon DocumentDB в кластере",
        "The minimum amount of lag, in milliseconds, between the primary instance and each replica instance in the cluster": "Минимальная величина отставания в миллисекундах между первичным экземпляром и каждым экземпляром реплики в кластере",
        "The amount of lag, in milliseconds, when replicating updates from the primary instance to a replica instance": "Величина отставания в миллисекундах при репликации обновлений с первичного экземпляра на экземпляр реплики",
        "The number of connections open on an instance taken at a one-minute frequency": "Количество подключений, открытых на экземпляре, измеряемое с частотой раз в минуту",
        "The amount of time, in seconds, that the instance has been running": "Время работы экземпляра в секундах",
        "The amount of storage available to each instance for temporary tables and logs": "Объём хранилища, доступного каждому экземпляру для временных таблиц и журналов",
        "The amount of available random access memory, in bytes": "Объём доступной оперативной памяти в байтах",
        "The amount of network throughput, in bytes per second, received from clients by each instance in the cluster": "Объём сетевой пропускной способности в байтах в секунду, полученной от клиентов каждым экземпляром в кластере",
        "The amount of network throughput, in bytes per second, both received from and transmitted to clients by each instance in the Amazon DocumentDB cluster": "Объём сетевой пропускной способности в байтах в секунду, как полученной от клиентов, так и переданной им каждым экземпляром в кластере Amazon DocumentDB",
        "The amount of network throughput, in bytes per second, sent to clients by each instance in the cluster": "Объём сетевой пропускной способности в байтах в секунду, отправленной клиентам каждым экземпляром в кластере",
        "The total amount of backup storage in GiB consumed by all snapshots for a given Amazon DocumentDB cluster outside its backup retention window": "Общий объём хранилища резервных копий в ГиБ, занятого всеми снимками для данного кластера Amazon DocumentDB за пределами окна хранения резервных копий",
        "The amount of swap space used on the instance": "Объём пространства подкачки, используемого на экземпляре",
        "The total amount of backup storage in GiB for which you are billed for a given Amazon DocumentDB cluster": "Общий объём хранилища резервных копий в ГиБ, за который начисляется плата для данного кластера Amazon DocumentDB",
        "The amount of storage used by your cluster in bytes": "Объём хранилища, используемого вашим кластером, в байтах",
        "The average number of billed read I/O operations from a cluster volume, reported at 5-minute intervals": "Среднее количество оплачиваемых операций ввода-вывода чтения из тома кластера; регистрируется с интервалом в 5 минут",
        "The average number of billed write I/O operations from a cluster volume, reported at 5-minute intervals": "Среднее количество оплачиваемых операций ввода-вывода записи из тома кластера; регистрируется с интервалом в 5 минут",
        "The average amount of time, in milliseconds, taken per disk I/O operation": "Среднее время в миллисекундах, затрачиваемое на одну дисковую операцию ввода-вывода",
    }
)

# ---- DynamoDB Accelerator (DAX) metric cells (node or cluster) ----
RU.update(
    {
        "The number of BatchGetItem requests handled by the node or cluster": "Количество запросов BatchGetItem, обработанных узлом или кластером",
        "The number of BatchWriteItem requests handled by the node or cluster": "Количество запросов BatchWriteItem, обработанных узлом или кластером",
        "The percentage of CPU utilization of the node or cluster": "Процент загрузки CPU узла или кластера",
        "The number of simultaneous connections made by clients to the node or cluster": "Количество одновременных подключений, установленных клиентами к узлу или кластеру",
        "The number of DeleteItem requests handled by the node or cluster": "Количество запросов DeleteItem, обработанных узлом или кластером",
        "Total number of requests that resulted in a user error reported by the node or cluster. Requests that were throttled by the node or cluster are included.": "Общее количество запросов, приведших к пользовательской ошибке, зарегистрированных узлом или кластером. Включаются запросы, подвергнутые регулированию узлом или кластером.",
        "An approximation of the amount of data cached in the item cache and the query cache by the node or cluster": "Приблизительный объём данных, кэшированных в кэше элементов и кэше запросов узлом или кластером",
        "The amount of data that was evicted by the node or cluster to make room for newly requested data": "Объём данных, вытесненных узлом или кластером для освобождения места под вновь запрошенные данные",
        "Total number of requests that resulted in an error reported by the node or cluster": "Общее количество запросов, приведших к ошибке, зарегистрированных узлом или кластером",
        "Total number of requests that resulted in an internal error reported by the node or cluster": "Общее количество запросов, приведших к внутренней ошибке, зарегистрированных узлом или кластером",
        "The number of GetItem requests handled by the node or cluster": "Количество запросов GetItem, обработанных узлом или кластером",
        "The number of times an item was returned from the cache by the node or cluster": "Количество случаев, когда элемент был возвращён из кэша узлом или кластером",
        "The number of times an item was not in the node or cluster cache, and had to be retrieved from DynamoDB": "Количество случаев, когда элемент отсутствовал в кэше узла или кластера и его пришлось извлекать из DynamoDB",
        "The number of bytes received on all network interfaces by the node or cluster": "Количество байт, полученных на всех сетевых интерфейсах узлом или кластером",
        "The number of bytes sent out on all network interfaces by the node or cluster. This metric identifies the volume of outgoing traffic in terms of the number of bytes on a single node or cluster.": "Количество байт, отправленных на всех сетевых интерфейсах узлом или кластером. Эта метрика определяет объём исходящего трафика в виде количества байт на одном узле или кластере.",
        "The number of packets received on all network interfaces by the node or cluster": "Количество пакетов, полученных на всех сетевых интерфейсах узлом или кластером",
        "The number of packets sent out on all network interfaces by the node or cluster. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single node or cluster.": "Количество пакетов, отправленных на всех сетевых интерфейсах узлом или кластером. Эта метрика определяет объём исходящего трафика в виде количества пакетов на одном узле или кластере.",
        "The number of PutItem requests handled by the node or cluster": "Количество запросов PutItem, обработанных узлом или кластером",
        "The number of times a query result was returned from the node or cluster cache": "Количество случаев, когда результат запроса был возвращён из кэша узла или кластера",
        "The number of times a query result was not in the node or cluster cache, and had to be retrieved from DynamoDB": "Количество случаев, когда результат запроса отсутствовал в кэше узла или кластера и его пришлось извлекать из DynamoDB",
        "The number of query requests handled by the node or cluster": "Количество запросов query, обработанных узлом или кластером",
        "The number of times a scan result was returned from the node or cluster cache": "Количество случаев, когда результат сканирования был возвращён из кэша узла или кластера",
        "The number of times a scan result was not in the node or cluster cache, and had to be retrieved from DynamoDB": "Количество случаев, когда результат сканирования отсутствовал в кэше узла или кластера и его пришлось извлекать из DynamoDB",
        "The number of scan requests handled by the node or cluster": "Количество запросов scan, обработанных узлом или кластером",
        "Total number of requests throttled by the node or cluster": "Общее количество запросов, подвергнутых регулированию узлом или кластером",
        "Total number of requests handled by the node or cluster": "Общее количество запросов, обработанных узлом или кластером",
        "The number of TransactGetItems requests handled by the node or cluster": "Количество запросов TransactGetItems, обработанных узлом или кластером",
        "The number of TransactWriteItems requests handled by the node or cluster": "Количество запросов TransactWriteItems, обработанных узлом или кластером",
        "The number of UpdateItem requests handled by the node or cluster": "Количество запросов UpdateItem, обработанных узлом или кластером",
    }
)

# ---- ElastiCache metric cells (Redis / Memcached) ----
RU.update(
    {
        "The number of value reallocations per minute performed by the active defragmentation process. This is derived from `active_defrag_hits` statistic.": "Количество перераспределений значений в минуту, выполненных процессом активной дефрагментации. Вычисляется на основе статистики `active_defrag_hits`.",
        "The number of bytes that have been read from the network by the cache node": "Количество байт, прочитанных из сети узлом кэша",
        "The number of bytes used to store cache items": "Количество байт, используемых для хранения элементов кэша",
        "The total number of bytes allocated by Redis for all purposes, including the dataset, buffers, and so on. This is derived from used_memory statistic.": "Общее количество байт, выделенных Redis для всех целей, включая набор данных, буферы и т. д. Вычисляется на основе статистики used_memory.",
        "The number of bytes currently used by hash tables": "Количество байт, используемых в настоящее время хеш-таблицами",
        "The number of bytes that have been written to the network by the cache node": "Количество байт, записанных в сеть узлом кэша",
        "The percentage of CPU utilization for the entire host": "Процент загрузки CPU для всего хоста",
        "The number of successful read-only key lookups in the main dictionary. This is derived from keyspace_hits statistic.": "Количество успешных операций поиска ключей только для чтения в основном словаре. Вычисляется на основе статистики keyspace_hits.",
        "The number of unsuccessful read-only key lookups in the main dictionary. This is derived from keyspace_misses statistic.": "Количество неуспешных операций поиска ключей только для чтения в основном словаре. Вычисляется на основе статистики keyspace_misses.",
        "The number of CAS (check and set) requests the cache has received where the CAS value did not match the CAS value stored": "Количество запросов CAS (check and set), полученных кэшем, в которых значение CAS не совпало с сохранённым значением CAS",
        "The number of CAS requests the cache has received where the requested key was found and the CAS value matched": "Количество запросов CAS, полученных кэшем, в которых запрошенный ключ был найден и значение CAS совпало",
        "The number of CAS requests the cache has received where the key requested was not found": "Количество запросов CAS, полученных кэшем, в которых запрошенный ключ не был найден",
        "The cumulative number of config get requests": "Накопительное количество запросов config get",
        "The cumulative number of config set requests": "Накопительное количество запросов config set",
        "The number of flush commands the cache has received": "Количество команд flush, полученных кэшем",
        "The number of get commands the cache has received": "Количество команд get, полученных кэшем",
        "The number of set commands the cache has received": "Количество команд set, полученных кэшем",
        "The cumulative number of touch requests": "Накопительное количество запросов touch",
        "The current number of configurations stored": "Текущее количество сохранённых конфигураций",
        "A count of the number of connections connected to the cache at an instant in time. ElastiCache uses two to three of the connections to monitor the cluster.": "Количество подключений, установленных к кэшу в определённый момент времени. ElastiCache использует два-три из этих подключений для мониторинга кластера.",
        "A count of the number of items currently stored in the cache": "Количество элементов, хранящихся в кэше в настоящее время",
        "The number of decrement requests the cache has received where the requested key was found": "Количество запросов decrement, полученных кэшем, в которых запрошенный ключ был найден",
        "The number of decrement requests the cache has received where the requested key was not found": "Количество запросов decrement, полученных кэшем, в которых запрошенный ключ не был найден",
        "The number of delete requests the cache has received where the requested key was found": "Количество запросов delete, полученных кэшем, в которых запрошенный ключ был найден",
        "The number of delete requests the cache has received where the requested key was not found.": "Количество запросов delete, полученных кэшем, в которых запрошенный ключ не был найден.",
        "Provides CPU utilization of the Redis engine thread": "Предоставляет данные о загрузке CPU потоком движка Redis",
        "The number of valid items evicted from the least recently used cache (LRU) which were never touched after being set": "Количество действительных элементов, вытесненных из кэша наименее недавно использовавшихся (LRU), к которым ни разу не обращались после установки",
        "The number of non-expired items the cache evicted to allow space for new writes": "Количество неистёкших элементов, вытесненных кэшем для освобождения места под новые записи",
        "The number of expired items reclaimed from the LRU which were never touched after being set": "Количество истёкших элементов, освобождённых из LRU, к которым ни разу не обращались после установки",
        "The amount of free memory available on the host. This is derived from the RAM, buffers, and cache that the OS reports as freeable.": "Объём свободной памяти, доступной на хосте. Вычисляется на основе ОЗУ, буферов и кэша, которые ОС сообщает как освобождаемые.",
        "The number of get requests the cache has received where the key requested was found": "Количество запросов get, полученных кэшем, в которых запрошенный ключ был найден",
        "The number of get requests the cache has received where the key requested was not found": "Количество запросов get, полученных кэшем, в которых запрошенный ключ не был найден",
        "The total number of read-only type commands. This is derived from the Redis commandstats statistic by summing all of the read-only type commands (get, hget, scard, lrange, and so on).": "Общее количество команд типа «только чтение». Вычисляется на основе статистики Redis commandstats путём суммирования всех команд типа «только чтение» (get, hget, scard, lrange и т. д.).",
        "The total number of commands that are hash-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more hashes (hget, hkeys, hvals, hdel, and so on).": "Общее количество команд, основанных на хешах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими хешами (hget, hkeys, hvals, hdel и т. д.).",
        "The total number of HyperLogLog-based commands": "Общее количество команд на основе HyperLogLog",
        "The number of increment requests the cache has received where the key requested was found": "Количество запросов increment, полученных кэшем, в которых запрошенный ключ был найден",
        "The number of increment requests the cache has received where the key requested was not found": "Количество запросов increment, полученных кэшем, в которых запрошенный ключ не был найден",
        "The total number of commands that are key-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more keys across multiple data structures (del, expire, rename, and so on).": "Общее количество команд, основанных на ключах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими ключами в разных структурах данных (del, expire, rename и т. д.).",
        "The number of keys being tracked by Redis key tracking as a percentage of tracking-table-max-keys. Key tracking is used to aid client-side caching and notifies clients when keys are modified.": "Количество ключей, отслеживаемых механизмом отслеживания ключей Redis, в процентах от tracking-table-max-keys. Отслеживание ключей помогает кэшированию на стороне клиента и уведомляет клиентов об изменении ключей.",
        "The total number of commands that are list-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more lists (lindex, lrange, lpush, ltrim, and so on).": "Общее количество команд, основанных на списках. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими списками (lindex, lrange, lpush, ltrim и т. д.).",
        "The number of bytes the host has read from the network": "Количество байт, прочитанных хостом из сети",
        "The number of bytes sent out on all network interfaces by the instance": "Количество байт, отправленных на всех сетевых интерфейсах экземпляром",
        "The number of new connections the cache has received. This is derived from the memcached total_connections statistic by recording the change in total_connections across a period of time.": "Количество новых подключений, полученных кэшем. Вычисляется на основе статистики memcached total_connections путём фиксации изменения total_connections за период времени.",
        "The number of new items the cache has stored. This is derived from the memcached total_items statistic by recording the change in total_items across a period of time.": "Количество новых элементов, сохранённых кэшем. Вычисляется на основе статистики memcached total_items путём фиксации изменения total_items за период времени.",
        "The number of expired items the cache evicted to allow space for new writes": "Количество истёкших элементов, вытесненных кэшем для освобождения места под новые записи",
        "For nodes in a replicated configuration, ReplicationBytes reports the number of bytes that the primary is sending to all of its replicas. This metric is representative of the write load on the replication group. This is derived from the master_repl_offset statistic.": "Для узлов в реплицированной конфигурации ReplicationBytes сообщает количество байт, которые первичный узел отправляет всем своим репликам. Эта метрика отражает нагрузку записи на группу репликации. Вычисляется на основе статистики master_repl_offset.",
        "This metric is only applicable for a node running as a read replica. It represents how far behind, in seconds, the replica is in applying changes from the primary node.": "Эта метрика применима только к узлу, работающему как реплика чтения. Она показывает, насколько (в секундах) реплика отстаёт в применении изменений с первичного узла.",
        "This binary metric returns 1 whenever a background save (forked or forkless) is in progress, and 0 otherwise.": "Эта двоичная метрика возвращает 1, когда выполняется фоновое сохранение (с ответвлением процесса или без него), и 0 в противном случае.",
        "The total number of commands that are set-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more sets (scard, sdiff, sadd, sunion, and so on).": "Общее количество команд, основанных на множествах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими множествами (scard, sdiff, sadd, sunion и т. д.).",
        "The total number of write types of commands. This is derived from the Redis commandstats statistic by summing all of the mutative types of commands that operate on data (set, hset, sadd, lpop, and so on).": "Общее количество команд типа «запись». Вычисляется на основе статистики Redis commandstats путём суммирования всех изменяющих типов команд, работающих с данными (set, hset, sadd, lpop и т. д.).",
        "The total number of slab pages that have been moved": "Общее количество перемещённых страниц slab",
        "The total number of commands that are sorted set-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more sorted sets (zcount, zrange, zrank, zadd, and so on).": "Общее количество команд, основанных на упорядоченных множествах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими упорядоченными множествами (zcount, zrange, zrank, zadd и т. д.).",
        "The total number of commands that are string-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more strings (strlen, setex, setrange, and so on).": "Общее количество команд, основанных на строках. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одной или несколькими строками (strlen, setex, setrange и т. д.).",
        "The amount of swap used on the host": "Объём пространства подкачки, используемого на хосте",
        "The number of keys that have been touched and were given a new expiration time": "Количество ключей, к которым обратились и которым было задано новое время истечения",
        "The number of items that have been touched, but were not found": "Количество элементов, к которым обратились, но которые не были найдены",
        "The amount of memory not used by data. This is derived from the Memcached statistics limit_maxbytes and bytes by subtracting bytes from limit_maxbytes.": "Объём памяти, не используемой данными. Вычисляется на основе статистик Memcached limit_maxbytes и bytes путём вычитания bytes из limit_maxbytes.",
    }
)

# ---- Keyspaces (Cassandra) metric cells ----
RU.update(
    {
        "The maximum number of read capacity units that can be used by an account": "Максимальное количество единиц ёмкости чтения, которые может использовать аккаунт",
        "The maximum number of read capacity units that can be used by a table of an account": "Максимальное количество единиц ёмкости чтения, которые может использовать таблица аккаунта",
        "The maximum number of write capacity units that can be used by a table of an account": "Максимальное количество единиц ёмкости записи, которые может использовать таблица аккаунта",
        "The maximum number of write capacity units that can be used by an account": "Максимальное количество единиц ёмкости записи, которые может использовать аккаунт",
        "The percentage of provisioned read capacity units utilized by an account": "Процент подготовленных единиц ёмкости чтения, использованных аккаунтом",
        "The percentage of provisioned write capacity units utilized by an account": "Процент подготовленных единиц ёмкости записи, использованных аккаунтом",
        "The number of failed lightweight transaction (LWT) write requests": "Количество неудачных запросов записи облегчённых транзакций (LWT)",
        "The number of read capacity units consumed over the specified time period": "Количество единиц ёмкости чтения, израсходованных за указанный период времени",
        "The number of write capacity units consumed over the specified time period": "Количество единиц ёмкости записи, израсходованных за указанный период времени",
        "The percentage of provisioned read capacity units utilized by the highest provisioned read table of an account": "Процент подготовленных единиц ёмкости чтения, использованных таблицей аккаунта с наибольшим объёмом подготовленной ёмкости чтения",
        "The percentage of provisioned write capacity utilized by the highest provisioned write table of an account": "Процент подготовленной ёмкости записи, использованной таблицей аккаунта с наибольшим объёмом подготовленной ёмкости записи",
        "The number of provisioned read capacity units for a table": "Количество подготовленных единиц ёмкости чтения для таблицы",
        "The number of provisioned write capacity units for a table": "Количество подготовленных единиц ёмкости записи для таблицы",
        "The number of rows returned by SELECT operations during the specified time period": "Количество строк, возвращённых операциями SELECT за указанный период времени",
        "The successful requests to Amazon Keyspaces during the specified time period": "Успешные запросы к Amazon Keyspaces за указанный период времени",
        "The requests to Amazon Keyspaces that generate a ServerError during the specified time period": "Запросы к Amazon Keyspaces, генерирующие ошибку ServerError, за указанный период времени",
        "Requests to Amazon Keyspaces that generate an `InvalidRequest` error during the specified time period": "Запросы к Amazon Keyspaces, генерирующие ошибку `InvalidRequest`, за указанный период времени",
    }
)

# ---- Neptune metric cells ----
RU.update(
    {
        "The total amount of backup storage, in bytes, used to support from the Neptune DB cluster's backup retention window": "Общий объём хранилища резервных копий в байтах, используемого для поддержки окна хранения резервных копий кластера БД Neptune",
        "The percentage of CPU utilization": "Процент загрузки CPU",
        "For a read replica, the amount of lag when replicating updates from the primary instance, in milliseconds": "Для реплики чтения: величина отставания при репликации обновлений с первичного экземпляра, в миллисекундах",
        "The maximum amount of lag between the primary instance and each Neptune DB instance in the DB cluster, in milliseconds": "Максимальная величина отставания между первичным экземпляром и каждым экземпляром БД Neptune в кластере БД, в миллисекундах",
        "The minimum amount of lag between the primary instance and each Neptune DB instance in the DB cluster, in milliseconds": "Минимальная величина отставания между первичным экземпляром и каждым экземпляром БД Neptune в кластере БД, в миллисекундах",
        "The amount of time that the instance has been running, in seconds": "Время работы экземпляра, в секундах",
        "The amount of available RAM, in bytes": "Объём доступной оперативной памяти, в байтах",
        "Number of requests per second to the Gremlin engine": "Количество запросов в секунду к движку Gremlin",
        "The number of open WebSocket connections to Neptune": "Количество открытых подключений WebSocket к Neptune",
        "Number of loader requests per second": "Количество запросов загрузчика в секунду",
        "The number of requests waiting in the input queue pending execution. Neptune starts throttling requests when they exceed the maximum queue capacity": "Количество запросов, ожидающих выполнения во входной очереди. Neptune начинает регулировать запросы, когда они превышают максимальную ёмкость очереди",
        "The incoming (receive) network traffic on the DB instance, including both customer database traffic and Neptune traffic used for monitoring and replication, in bytes/second": "Входящий (принимаемый) сетевой трафик на экземпляре БД, включая как трафик клиентской базы данных, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду",
        "The amount of network throughput both received from and transmitted to clients by each instance in the Neptune DB cluster, in bytes per second. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume.": "Объём сетевой пропускной способности, как полученной от клиентов, так и переданной им каждым экземпляром в кластере БД Neptune, в байтах в секунду. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера.",
        "The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Neptune traffic used for monitoring and replication, in bytes/second": "Исходящий (передаваемый) сетевой трафик на экземпляре БД, включая как трафик клиентской базы данных, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду",
        "The number of transactions successfully committed per second": "Количество транзакций, успешно зафиксированных в секунду",
        "The number of transactions opened on the server per second": "Количество транзакций, открытых на сервере в секунду",
        "The number of transactions per second rolled back on the server because of errors": "Количество транзакций в секунду, откатанных на сервере из-за ошибок",
        "The total amount of backup storage consumed by all snapshots for a Neptune DB cluster outside its backup retention window, in bytes": "Общий объём хранилища резервных копий, занятого всеми снимками для кластера БД Neptune за пределами окна хранения резервных копий, в байтах",
        "The number of requests per second to the SPARQL engine": "Количество запросов в секунду к движку SPARQL",
        "The total amount of backup storage for which you are billed for a given Neptune DB cluster, in bytes": "Общий объём хранилища резервных копий, за который начисляется плата для данного кластера БД Neptune, в байтах",
        "The total number per second of requests that errored out because of client-side issues": "Общее количество запросов в секунду, завершившихся ошибкой из-за проблем на стороне клиента",
        "The total number of requests per second to the server from all sources": "Общее количество запросов в секунду к серверу из всех источников",
        "The total number per second of requests that errored out on the server because of internal failures": "Общее количество запросов в секунду, завершившихся ошибкой на сервере из-за внутренних сбоев",
        "The total amount of storage allocated to your Neptune DB cluster, in bytes. This is the amount of storage for which you are billed. It is the maximum amount of storage allocated to your DB cluster at any point in its existence, not the amount you are currently using.": "Общий объём хранилища, выделенного вашему кластеру БД Neptune, в байтах. Это объём хранилища, за который начисляется плата. Это максимальный объём хранилища, выделенный вашему кластеру БД в любой момент его существования, а не объём, который вы используете в настоящее время.",
        "The amount of storage used by your Neptune DB instance, in bytes.": "Объём хранилища, используемого вашим экземпляром БД Neptune, в байтах.",
        "The remaining available space for the cluster volume, as measured in bytes": "Оставшееся доступное пространство для тома кластера, измеряемое в байтах",
        "The average number of billed read I/O operations from a cluster volume, reported at 5-minute intervals.": "Среднее количество оплачиваемых операций ввода-вывода чтения из тома кластера; регистрируется с интервалом в 5 минут.",
        "The average number of write disk I/O operations to the cluster volume, reported at 5-minute intervals": "Среднее количество дисковых операций ввода-вывода записи в том кластера; регистрируется с интервалом в 5 минут",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon Aurora monitoring": "Мониторинг Amazon Aurora",
    "Amazon DocumentDB (with MongoDB compatibility) monitoring": "Мониторинг Amazon DocumentDB (with MongoDB compatibility)",
    "Amazon DynamoDB Accelerator (DAX) monitoring": "Мониторинг Amazon DynamoDB Accelerator (DAX)",
    "Amazon ElastiCache monitoring": "Мониторинг Amazon ElastiCache",
    "Amazon Keyspaces (Cassandra) monitoring": "Мониторинг Amazon Keyspaces (Cassandra)",
    "Amazon Neptune monitoring": "Мониторинг Amazon Neptune",
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
            print("  MISS:", k[:110])
    if unused_mine:
        print(f"--- UNUSED my translations ({len(unused_mine)}) ---")
        for k in unused_mine:
            print("  EXTRA:", k[:110])
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

    merge(TRANS_P, add_trans)
    merge(TITLE_P, ADD_TITLES)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
