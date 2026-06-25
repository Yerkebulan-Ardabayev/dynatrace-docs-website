# -*- coding: utf-8 -*-
"""Merge L4-IF.54 batch (AWS broken-header: dynamodb-new, rds-new, trusted-advisor,
glue) prose/Description translations into the shared cumulative dicts.

Same mechanism as L4-IF.45-53: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. Self-validation
reports any uncovered skeleton key or unused translation. Asserts: no em-dash, no
mojibake in RU.

Canon: the metric tables use COLMAP_OVERRIDE signatures registered in
_build_aws_l4if54.py (Name=EN findability, Description->TRANS, Unit->UNIT,
Statistics/Dimensions=EN, Recommended->APPLIC). Intro is form V1. Several rds-new
EN Description cells are TRUNCATED in the source (".. available for basic", ".. and
Amazon RDS", ".. MariaDB instances,") -> mirrored faithfully (no_unverified_claims),
not completed. Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if54.json")


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

# ---- H1 headings (X monitoring -> # Мониторинг X) ----
RU["# Amazon DynamoDB monitoring"] = "# Мониторинг Amazon DynamoDB"
RU["# Amazon RDS (Relational Database Service) monitoring"] = (
    "# Мониторинг Amazon RDS (Relational Database Service)"
)
RU["# AWS Trusted Advisor monitoring"] = "# Мониторинг AWS Trusted Advisor"
RU["# AWS Glue monitoring"] = "# Мониторинг AWS Glue"

# ---- intro (form V1); DynamoDB intro already shipped in L4-IF.53 ----
RU[en_v1("Amazon RDS")] = ru_v1("Amazon RDS")
RU[en_v1("AWS Trusted Advisor")] = ru_v1("AWS Trusted Advisor")
RU[en_v1("AWS Glue")] = ru_v1("AWS Glue")

# ---- read-time + main-dimension ----
RU["* 31-min read"] = "* Чтение: 31 мин"
RU["`TableName` is the main dimension."] = "Основное измерение: `TableName`."
RU["`JobName` is the main dimension."] = "Основное измерение: `JobName`."

# ---- new-service migration warning (canon: azure storage-account L4-IF.42) ----
RU.update(
    {
        "This service monitors a part of Amazon DynamoDB (AWS/DynamoDB). While you have this service configured, you can't have Amazon Dynamo Database (built-in) service turned on.": "Этот сервис отслеживает часть Amazon DynamoDB (AWS/DynamoDB). Пока этот сервис настроен, вы не можете включить сервис Amazon Dynamo Database (built-in).",
        "This service monitors a part of Amazon RDS (AWS/RDS). While you have this service configured, you can't have Amazon RDS (built-in) service turned on.": "Этот сервис отслеживает часть Amazon RDS (AWS/RDS). Пока этот сервис настроен, вы не можете включить сервис Amazon RDS (built-in).",
    }
)

# ---- DynamoDB metric descriptions ----
RU.update(
    {
        "The number of read capacity units consumed over the specified time period for both provisioned and on-demand capacity, so you can track how much of your throughput is used.": "Количество единиц ёмкости чтения, потреблённых за указанный период времени как для подготовленной ёмкости, так и для ёмкости по требованию, что позволяет отслеживать, какая часть пропускной способности используется.",
        "The percentage of provisioned read capacity utilized by the highest provisioned read table or global secondary index of an account.": "Процент подготовленной ёмкости чтения, используемой таблицей или глобальным вторичным индексом с наибольшей подготовленной ёмкостью чтения в аккаунте.",
        "The latency of successful requests to DynamoDB or Amazon DynamoDB Streams during the specified time period.": "Задержка успешных запросов к DynamoDB или Amazon DynamoDB Streams за указанный период времени.",
        "The number of items returned by Query, Scan or ExecuteStatement (select) operations during the specified time period.": "Количество элементов, возвращённых операциями Query, Scan или ExecuteStatement (select) за указанный период времени.",
        "The percentage of provisioned read capacity units utilized by an account.": "Процент подготовленных единиц ёмкости чтения, используемых аккаунтом.",
        "The percentage of provisioned write capacity utilized by the highest provisioned write table or global secondary index of an account.": "Процент подготовленной ёмкости записи, используемой таблицей или глобальным вторичным индексом с наибольшей подготовленной ёмкостью записи в аккаунте.",
        "The maximum number of write capacity units that can be used by a table or global secondary index of an account.": "Максимальное количество единиц ёмкости записи, которое может использовать таблица или глобальный вторичный индекс аккаунта.",
        "The maximum number of read capacity units that can be used by an account.": "Максимальное количество единиц ёмкости чтения, которое может использовать аккаунт.",
        "The number of write capacity units consumed over the specified time period for both provisioned and on-demand capacity, so you can track how much of your throughput is used.": "Количество единиц ёмкости записи, потреблённых за указанный период времени как для подготовленной ёмкости, так и для ёмкости по требованию, что позволяет отслеживать, какая часть пропускной способности используется.",
        "The maximum number of read capacity units that can be used by a table or global secondary index of an account.": "Максимальное количество единиц ёмкости чтения, которое может использовать таблица или глобальный вторичный индекс аккаунта.",
        "The number of provisioned read capacity units for a table or a global secondary index.": "Количество подготовленных единиц ёмкости чтения для таблицы или глобального вторичного индекса.",
        "The number of provisioned write capacity units for a table or a global secondary index.": "Количество подготовленных единиц ёмкости записи для таблицы или глобального вторичного индекса.",
        "The percentage of provisioned write capacity units utilized by an account.": "Процент подготовленных единиц ёмкости записи, используемых аккаунтом.",
        "The maximum number of write capacity units that can be used by an account.": "Максимальное количество единиц ёмкости записи, которое может использовать аккаунт.",
        "The elapsed time since a record yet to be replicated to the Kinesis data stream first appeared in the DynamoDB table.": "Время, прошедшее с момента, когда запись, ещё не реплицированная в поток данных Kinesis, впервые появилась в таблице DynamoDB.",
        "The number of failed attempts to perform conditional writes.": "Количество неудачных попыток выполнить условную запись.",
        "The number of records that DynamoDB failed to replicate to your Kinesis data stream.": "Количество записей, которые DynamoDB не удалось реплицировать в ваш поток данных Kinesis.",
        "The number of write capacity units consumed when adding a new global secondary index to a table.": "Количество единиц ёмкости записи, потреблённых при добавлении нового глобального вторичного индекса в таблицу.",
        "The percentage of completion when a new global secondary index is being added to a table.": "Процент выполнения при добавлении нового глобального вторичного индекса в таблицу.",
        "The number of write throttle events that occur when adding a new global secondary index to a table.": "Количество событий регулирования записи, возникающих при добавлении нового глобального вторичного индекса в таблицу.",
        "The number of item updates that are written to one replica table, but that have not yet been written to another replica in the global table.": "Количество обновлений элементов, которые записаны в одну реплику таблицы, но ещё не записаны в другую реплику в глобальной таблице.",
        "Requests to DynamoDB that exceed the provisioned read capacity units for a table or a global secondary index.": "Запросы к DynamoDB, превышающие подготовленные единицы ёмкости чтения для таблицы или глобального вторичного индекса.",
        "The elapsed time between an updated item appearing in the DynamoDB stream for one replica table, and that item appearing in another replica in the global table.": "Время между появлением обновлённого элемента в потоке DynamoDB для одной реплики таблицы и появлением этого элемента в другой реплике в глобальной таблице.",
        "The number of bytes returned by GetRecords operations (Amazon DynamoDB Streams) during the specified time period.": "Количество байт, возвращённых операциями GetRecords (Amazon DynamoDB Streams) за указанный период времени.",
        "The number of stream records returned by GetRecords operations (Amazon DynamoDB Streams) during the specified time period.": "Количество записей потока, возвращённых операциями GetRecords (Amazon DynamoDB Streams) за указанный период времени.",
        "The requests to DynamoDB or Amazon DynamoDB Streams that generate an HTTP 500 status code during the specified time period.": "Запросы к DynamoDB или Amazon DynamoDB Streams, генерирующие код состояния HTTP 500 за указанный период времени.",
        "The number of items deleted by Time to Live (TTL) during the specified time period.": "Количество элементов, удалённых механизмом Time to Live (TTL) за указанный период времени.",
        "The number of records that were throttled by your Kinesis data stream due to insufficient Kinesis Data Streams capacity.": "Количество записей, подвергнутых регулированию вашим потоком данных Kinesis из-за недостаточной ёмкости Kinesis Data Streams.",
        "Requests to DynamoDB that exceed the provisioned throughput limits on a resource (such as a table or an index).": "Запросы к DynamoDB, превышающие подготовленные лимиты пропускной способности для ресурса (например, таблицы или индекса).",
        "Rejected item-level requests due to transactional conflicts between concurrent requests on the same items.": "Отклонённые запросы на уровне элементов из-за транзакционных конфликтов между параллельными запросами к одним и тем же элементам.",
        "Requests to DynamoDB or Amazon DynamoDB Streams that generate an HTTP 400 status code during the specified time period.": "Запросы к DynamoDB или Amazon DynamoDB Streams, генерирующие код состояния HTTP 400 за указанный период времени.",
        "Requests to DynamoDB that exceed the provisioned write capacity units for a table or a global secondary index.": "Запросы к DynamoDB, превышающие подготовленные единицы ёмкости записи для таблицы или глобального вторичного индекса.",
    }
)

# ---- RDS metric descriptions (4 EN cells truncated in source -> mirrored) ----
RU.update(
    {
        "The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic": "Процент кредитов ввода-вывода, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна для basic",
        "The amount of swap space used on the DB instance.": "Объём пространства подкачки, используемого на экземпляре БД.",
        "The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS": "Исходящий (передаваемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS",
        "The average number of bytes read from disk per second.": "Среднее количество байт, прочитанных с диска в секунду.",
        "The number of outstanding I/Os (read/write requests) waiting to access the disk.": "Количество необработанных операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску.",
        "The amount of disk space occupied by binary logs. If automatic backups are enabled for MySQL and MariaDB instances,": "Объём дискового пространства, занятого бинарными логами. Если для экземпляров MySQL и MariaDB включено автоматическое резервное копирование,",
        "The number of client network connections to the database instance.": "Количество клиентских сетевых подключений к экземпляру базы данных.",
        "The amount of available storage space.": "Объём доступного дискового пространства.",
        "The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available": "Процент кредитов пропускной способности, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна",
        "The percentage of CPU utilization.": "Процент использования CPU.",
        "The number of attempts to connect to an instance, whether successful or not.": "Количество попыток подключения к экземпляру, как успешных, так и неуспешных.",
        "The average amount of time taken per disk I/O operation.": "Среднее время, затрачиваемое на одну операцию ввода-вывода диска.",
        "The amount of available random access memory.": "Объём доступной оперативной памяти.",
        "The average number of disk read I/O operations per second.": "Среднее количество операций ввода-вывода чтения с диска в секунду.",
        "The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS": "Входящий (принимаемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS",
        "The average number of bytes written to disk per second.": "Среднее количество байт, записанных на диск в секунду.",
        "The average number of disk write I/O operations per second.": "Среднее количество операций ввода-вывода записи на диск в секунду.",
        "The percent of General Purpose SSD (gp2) burst-bucket I/O credits available.": "Процент доступных кредитов ввода-вывода корзины всплеска для General Purpose SSD (gp2).",
    }
)

# ---- Trusted Advisor prose ----
RU.update(
    {
        "For AWS Trusted Advisor, there are no instances (custom devices) on the custom device group overview page. The service metrics are under the **Further details** section of the custom device group overview page.": "Для AWS Trusted Advisor на странице обзора группы пользовательских устройств нет экземпляров (пользовательских устройств). Метрики сервиса находятся в разделе **Further details** страницы обзора группы пользовательских устройств.",
        "AWS Trusted Advisor CloudWatch metrics are available **only** for Business and Enterprise Support plans.": "Метрики CloudWatch AWS Trusted Advisor доступны **только** для планов поддержки Business и Enterprise.",
    }
)

# ---- Glue prose + metric descriptions ----
RU.update(
    {
        "To ingest additional observability metrics": "Чтобы принимать дополнительные метрики наблюдаемости",
        "1. In the AWS Console, go to **Job details** section.": "1. В консоли AWS перейдите в раздел **Job details**.",
        "2. Enable the **Job observability metrics** option.": "2. Включите опцию **Job observability metrics**.",
        "The number of bytes read from all data sources by all completed Spark tasks running in all executors": "Количество байт, прочитанных из всех источников данных всеми завершёнными задачами Spark, выполняющимися во всех исполнителях",
        "The ETL elapsed time in milliseconds (doesn't include the job bootstrap times)": "Прошедшее время ETL в миллисекундах (не включает время начальной загрузки задания)",
        "The number of completed stages in a job": "Количество завершённых этапов в задании",
        "The number of completed tasks in a job": "Количество завершённых задач в задании",
        "The number of failed tasks in a job": "Количество неуспешных задач в задании",
        "The number of tasks killed in a job": "Количество принудительно завершённых задач в задании",
        "The number of records read from all data sources by all completed Spark tasks running in all executors": "Количество записей, прочитанных из всех источников данных всеми завершёнными задачами Spark, выполняющимися во всех исполнителях",
        "The number of bytes written by all executors to shuffle data between them since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes written for this purpose during the previous minute)": "Количество байт, записанных всеми исполнителями для перемешивания данных между ними с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, записанных для этой цели за предыдущую минуту)",
        "The number of bytes read by all executors to shuffle data between them since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes read for this purpose during the previous minute)": "Количество байт, прочитанных всеми исполнителями для перемешивания данных между ними с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, прочитанных для этой цели за предыдущую минуту)",
        "The number of megabytes of disk space used across all executors": "Количество мегабайт дискового пространства, используемого по всем исполнителям",
        "The number of actively running job executors": "Количество активно работающих исполнителей задания",
        "The number of maximum (actively running and pending) job executors needed to satisfy the current load": "Максимальное количество исполнителей задания (активно работающих и ожидающих), необходимых для обработки текущей нагрузки",
        "The fraction of memory used by the JVM heap (scale: `0`-`1`) for this driver": "Доля памяти, используемой кучей JVM (шкала: `0`-`1`), для этого драйвера",
        "The fraction of memory used by the JVM heap (scale: `0`-`1`) for all executors": "Доля памяти, используемой кучей JVM (шкала: `0`-`1`), для всех исполнителей",
        "The number of memory bytes used by the JVM heap for the driver": "Количество байт памяти, используемых кучей JVM для драйвера",
        "The number of memory bytes used by the JVM heap for all executors": "Количество байт памяти, используемых кучей JVM для всех исполнителей",
        "The number of bytes read from Amazon S3 by the driver since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes read during the previous minute)": "Количество байт, прочитанных из Amazon S3 драйвером с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, прочитанных за предыдущую минуту)",
        "The number of bytes read from Amazon S3 by all executors since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes read during the previous minute)": "Количество байт, прочитанных из Amazon S3 всеми исполнителями с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, прочитанных за предыдущую минуту)",
        "The number of bytes written to Amazon S3 by the driver since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes written during the previous minute)": "Количество байт, записанных в Amazon S3 драйвером с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, записанных за предыдущую минуту)",
        "The number of bytes written to Amazon S3 by all executors since the previous report (aggregated by the AWS Glue metrics dashboard as the number of bytes written during the previous minute)": "Количество байт, записанных в Amazon S3 всеми исполнителями с момента предыдущего отчёта (агрегируется дашбордом метрик AWS Glue как количество байт, записанных за предыдущую минуту)",
        "The fraction of CPU system load used (scale: `0`-`1`) by the driver": "Доля используемой системной нагрузки CPU (шкала: `0`-`1`) драйвером",
        "The fraction of CPU system load used (scale: `0`-`1`) by all executors": "Доля используемой системной нагрузки CPU (шкала: `0`-`1`) всеми исполнителями",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon DynamoDB monitoring": "Мониторинг Amazon DynamoDB",
    "Amazon RDS (Relational Database Service) monitoring": "Мониторинг Amazon RDS (Relational Database Service)",
    "AWS Trusted Advisor monitoring": "Мониторинг AWS Trusted Advisor",
    "AWS Glue monitoring": "Мониторинг AWS Glue",
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
