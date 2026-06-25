# -*- coding: utf-8 -*-
"""Merge L4-IF.50 batch (2 standard AWS streaming/messaging files: Amazon MQ
(ActiveMQ + RabbitMQ), Amazon EMR (Elastic MapReduce)) translations into the
shared cumulative dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Same mechanism as L4-IF.45-49: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. asciinorm
also folds markdown escapes (\\_ \\*) and curly/dash punctuation. Any skeleton key
left without a translation, or any translation matching no skeleton key, is
reported (self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if50.json")


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

# ---- intros (both form V1) ----
for name in ["Amazon MQ", "Amazon EMR"]:
    RU[en_v1(name)] = ru_v1(name)

# ---- Amazon MQ (ActiveMQ + RabbitMQ) ----
RU.update(
    {
        "# Amazon MQ monitoring": "# Мониторинг Amazon MQ",
        "`Broker` is the main dimension.": "Основное измерение: `Broker`.",
        # --- ActiveMQ ---
        "### ActiveMQ": "### ActiveMQ",
        "The number of consumers subscribed to the destination": "Количество потребителей, подписанных на место назначения",
        "The number of earned CPU credits that an instance has accrued since it was launched or started (including the number of launch credits)": "Количество заработанных кредитов CPU, которые экземпляр накопил с момента его запуска или старта (включая количество кредитов запуска)",
        "The percentage of allocated Amazon EC2 compute units that the broker currently uses": "Процент выделенных вычислительных единиц Amazon EC2, которые в данный момент использует брокер",
        "The current number of active connections on the current broker": "Текущее количество активных подключений на текущем брокере",
        "The number of messages acknowledged by consumers, per minute": "Количество сообщений, подтверждённых потребителями, в минуту",
        "The number of messages sent to consumers, per minute": "Количество сообщений, отправленных потребителям, в минуту",
        "The number of messages sent to the destination, per minute": "Количество сообщений, отправленных в место назначения, в минуту",
        "The end-to-end latency from when a message arrives at a broker until it is delivered to a consumer": "Сквозная задержка от момента поступления сообщения на брокер до момента его доставки потребителю",
        "The total number of connections, active and inactive, that have been established on the broker": "Общее количество подключений, активных и неактивных, установленных на брокере",
        "The number of messages that couldn't be delivered because they expired, per minute": "Количество сообщений, которые не удалось доставить из-за истечения их срока действия, в минуту",
        "The percentage of the ActiveMQ JVM memory limit that the broker currently uses": "Процент лимита памяти JVM ActiveMQ, который в данный момент использует брокер",
        "The number of messages sent to consumers that have not been acknowledged": "Количество сообщений, отправленных потребителям, которые не были подтверждены",
        "The number of inactive durable topic subscribers, up to a maximum of 2000": "Количество неактивных устойчивых подписчиков топика, до максимума в 2000",
        "The percentage of disk space used by the job scheduler store": "Процент дискового пространства, используемого хранилищем планировщика задач",
        "The number of journal files that will be replayed after a clean shutdown": "Количество файлов журнала, которые будут воспроизведены после штатного завершения работы",
        "The number of journal files that will be replayed after an unclean shutdown": "Количество файлов журнала, которые будут воспроизведены после нештатного завершения работы",
        "The percentage of the memory limit that the destination currently uses.": "Процент лимита памяти, который в данный момент использует место назначения.",
        "The volume of incoming traffic for the broker": "Объём входящего трафика брокера",
        "The volume of outgoing traffic for the broker": "Объём исходящего трафика брокера",
        "The total number of transactions in progress": "Общее количество выполняемых транзакций",
        "The number of producers for the destination": "Количество производителей для места назначения",
        "The number of messages in the queue. This metric applies only to queues.": "Количество сообщений в очереди. Эта метрика применяется только к очередям.",
        "The number of messages that have been received from the remote broker for a duplex network connector": "Количество сообщений, полученных от удалённого брокера для дуплексного сетевого коннектора",
        "The percent used by the storage limit. If this reaches 100, the broker will refuse messages.": "Процент, использованный от лимита хранилища. Если он достигнет 100, брокер начнёт отклонять сообщения.",
        "The percentage of available temporary storage used by non-persistent messages": "Процент доступного временного хранилища, используемого непостоянными сообщениями",
        "The number of message consumers subscribed to destinations on the current broker": "Количество потребителей сообщений, подписанных на места назначения на текущем брокере",
        "The total number of messages that have been consumed by clients": "Общее количество сообщений, потреблённых клиентами",
        "The total number of messages that have been sent to the broker": "Общее количество сообщений, отправленных на брокер",
        "The number of messages stored on the broker": "Количество сообщений, хранящихся на брокере",
        "The number of message producers active on destinations on the current broker": "Количество производителей сообщений, активных на местах назначения на текущем брокере",
        # --- RabbitMQ ---
        "### RabbitMQ": "### RabbitMQ",
        "The rate at which messages are being acknowledged by consumers.": "Скорость, с которой сообщения подтверждаются потребителями.",
        "The total number of channels established on the broker.": "Общее количество каналов, установленных на брокере.",
        "The rate at which the RabbitMQ server is confirming published messages.": "Скорость, с которой сервер RabbitMQ подтверждает опубликованные сообщения.",
        "The total number of connections established on the broker.": "Общее количество подключений, установленных на брокере.",
        "The total number of consumers connected to the broker.": "Общее количество потребителей, подключённых к брокеру.",
        "The total number of exchanges configured on the broker.": "Общее количество обменников, настроенных на брокере.",
        "The total number of messages in the queues.": "Общее количество сообщений в очередях.",
        "The total number of ready messages in the queues.": "Общее количество готовых сообщений в очередях.",
        "The total number of unacknowledged messages in the queues.": "Общее количество неподтверждённых сообщений в очередях.",
        "The rate at which messages are published to the broker.": "Скорость, с которой сообщения публикуются на брокере.",
        "The total number of queues configured on the broker.": "Общее количество очередей, настроенных на брокере.",
        "The disk limit for a RabbitMQ node.": "Дисковый лимит для узла RabbitMQ.",
        "Number of file descriptors used.": "Количество используемых файловых дескрипторов.",
        # source quirk: SystemCpuUtilization keeps the trailing period (ActiveMQ CpuUtilization has none) -> distinct key
        "The percentage of allocated Amazon EC2 compute units that the broker currently uses.": "Процент выделенных вычислительных единиц Amazon EC2, которые в данный момент использует брокер.",
    }
)

# ---- Amazon EMR (Elastic MapReduce) ----
RU.update(
    {
        "# Amazon EMR (Elastic MapReduce) monitoring": "# Мониторинг Amazon EMR (Elastic MapReduce)",
        "`JobFlowId` is the main dimension.": "Основное измерение: `JobFlowId`.",
        "The number of applications submitted to YARN that have completed": "Количество приложений, отправленных в YARN, которые завершились",
        "The number of applications submitted to YARN that have failed to complete": "Количество приложений, отправленных в YARN, которые не удалось завершить",
        "The number of applications submitted to YARN that have been killed": "Количество приложений, отправленных в YARN, которые были принудительно завершены",
        "The number of applications submitted to YARN that are in a Pending state": "Количество приложений, отправленных в YARN, которые находятся в состоянии ожидания (Pending)",
        "The number of applications submitted to YARN that are running": "Количество приложений, отправленных в YARN, которые выполняются",
        "The number of applications submitted to YARN": "Количество приложений, отправленных в YARN",
        "Shows if the last backup failed. Set to `0` by default and updated to `1` if the previous backup attempt failed. This metric is only reported for HBase clusters.": "Показывает, завершилось ли последнее резервное копирование неудачей. По умолчанию установлено в `0` и обновляется до `1`, если предыдущая попытка резервного копирования завершилась неудачей. Эта метрика регистрируется только для кластеров HBase.",
        "The amount of remaining HDFS disk capacity": "Объём оставшейся дисковой ёмкости HDFS",
        "The number of resource containers allocated by the resource manager": "Количество контейнеров ресурсов, выделенных менеджером ресурсов",
        "The ratio (in numbers) of pending containers to containers allocated (`ContainerPendingRatio` = `ContainerPending` / `ContainerAllocated`). If `ContainerAllocated` = `0`, then `ContainerPendingRatio` = `ContainerPending`.": "Соотношение (в числах) ожидающих контейнеров к выделенным контейнерам (`ContainerPendingRatio` = `ContainerPending` / `ContainerAllocated`). Если `ContainerAllocated` = `0`, то `ContainerPendingRatio` = `ContainerPending`.",
        "The number of containers in the queue that have not yet been allocated": "Количество контейнеров в очереди, которые ещё не были выделены",
        "The number of containers reserved": "Количество зарезервированных контейнеров",
        "The number of core nodes waiting to be assigned (pending requests)": "Количество основных узлов, ожидающих назначения (ожидающие запросы)",
        "The number of working core nodes": "Количество работающих основных узлов",
        "The number of blocks that HDFS reports as corrupted": "Количество блоков, которые HDFS сообщает как повреждённые",
        "The status of block replication: blocks being replicated, age of replication requests, and unsuccessful replication requests": "Состояние репликации блоков: реплицируемые блоки, возраст запросов на репликацию и неуспешные запросы на репликацию",
        "The number of bytes read from HDFS": "Количество байт, прочитанных из HDFS",
        "The number of bytes written to HDFS": "Количество байт, записанных в HDFS",
        "The percentage of HDFS storage currently used": "Процент хранилища HDFS, используемого в данный момент",
        "Indicates that a cluster is no longer performing work, but is still alive and accruing charges. Set to `1` if no tasks are running and no jobs are running, and to `0` otherwise. This value is checked at five-minute intervals and a value of `1` indicates only that the cluster was idle when checked, not that it was idle for the entire five minutes.": "Указывает, что кластер больше не выполняет работу, но всё ещё активен и продолжает накапливать расходы. Устанавливается в `1`, если не выполняется ни одна задача и ни одно задание, и в `0` в противном случае. Это значение проверяется с интервалом в пять минут, и значение `1` указывает лишь на то, что кластер простаивал в момент проверки, а не на то, что он простаивал в течение всех пяти минут.",
        "The number of jobs in the cluster that have failed": "Количество заданий в кластере, которые завершились неудачей",
        "The number of jobs in the cluster that are currently running": "Количество заданий в кластере, которые выполняются в данный момент",
        "The percentage of data nodes that are receiving work from Hadoop": "Процент узлов данных, получающих работу от Hadoop",
        "The percentage of task trackers that are functional": "Процент трекеров задач, которые функционируют",
        "The number of nodes presently running MapReduce tasks or jobs. Equivalent to YARN metric `mapred.resourcemanager.NoOfActiveNodes`": "Количество узлов, на которых в настоящее время выполняются задачи или задания MapReduce. Эквивалентно метрике YARN `mapred.resourcemanager.NoOfActiveNodes`",
        "The number of nodes allocated to MapReduce applications that have been marked in a **Decommissioned** state": "Количество узлов, выделенных приложениям MapReduce, которые были помечены в состояние **Decommissioned**",
        "The number of nodes allocated to MapReduce that have been marked in a **Lost** state": "Количество узлов, выделенных MapReduce, которые были помечены в состояние **Lost**",
        "The number of nodes available to MapReduce that have been rebooted and marked in a **Rebooted** state": "Количество узлов, доступных MapReduce, которые были перезагружены и помечены в состояние **Rebooted**",
        "The number of nodes presently available to MapReduce jobs": "Количество узлов, доступных в настоящее время заданиям MapReduce",
        "The number of nodes available to MapReduce jobs marked in an **Unhealthy** state": "Количество узлов, доступных заданиям MapReduce, помеченных в состояние **Unhealthy**",
        "The unused map task capacity. This is calculated as the maximum number of map tasks for a given cluster, less the total number of map tasks currently running in that cluster.": "Неиспользуемая ёмкость задач map. Вычисляется как максимальное количество задач map для данного кластера за вычетом общего количества задач map, выполняющихся в этом кластере в данный момент.",
        "The number of remaining map tasks for each job": "Количество оставшихся задач map для каждого задания",
        "The number of running map tasks for each job": "Количество выполняющихся задач map для каждого задания",
        "The amount of memory allocated to the cluster": "Объём памяти, выделенной кластеру",
        "The amount of memory available for allocation": "Объём памяти, доступной для выделения",
        "The amount of memory reserved for allocation": "Объём памяти, зарезервированной для выделения",
        "The total amount of memory in the cluster": "Общий объём памяти в кластере",
        "The number of blocks in which HDFS has no replicas. These might be corrupt blocks.": "Количество блоков, для которых у HDFS нет реплик. Это могут быть повреждённые блоки.",
        "The amount of time it took the previous backup to complete. This metric is set regardless of whether the last completed backup succeeded or failed. While the backup is ongoing, this metric returns the number of minutes after the backup started. This metric is only reported for HBase clusters.": "Количество времени, которое потребовалось предыдущему резервному копированию для завершения. Эта метрика устанавливается независимо от того, завершилось ли последнее резервное копирование успешно или неудачей. Пока резервное копирование выполняется, эта метрика возвращает количество минут с момента начала резервного копирования. Эта метрика регистрируется только для кластеров HBase.",
        "The number of blocks marked for deletion": "Количество блоков, помеченных для удаления",
        "Unused reduce task capacity. This is calculated as the maximum reduce task capacity for a given cluster, less the number of reduce tasks currently running in that cluster.": "Неиспользуемая ёмкость задач reduce. Вычисляется как максимальная ёмкость задач reduce для данного кластера за вычетом количества задач reduce, выполняющихся в этом кластере в данный момент.",
        "The number of remaining reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated.": "Количество оставшихся задач reduce для каждого задания. Если у вас установлен планировщик и выполняется несколько заданий, создаётся несколько графиков.",
        "The number of running reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated.": "Количество выполняющихся задач reduce для каждого задания. Если у вас установлен планировщик и выполняется несколько заданий, создаётся несколько графиков.",
        "The ratio of the total map tasks remaining to the total map slots available in the cluster": "Соотношение общего количества оставшихся задач map к общему количеству доступных слотов map в кластере",
        "The number of bytes read from Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on EMR.": "Количество байт, прочитанных из Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется к другим рабочим нагрузкам в EMR.",
        "The number of bytes written to Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on EMR.": "Количество байт, записанных в Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется к другим рабочим нагрузкам в EMR.",
        "The number of task nodes waiting to be assigned (pending requests)": "Количество узлов задач, ожидающих назначения (ожидающие запросы)",
        "The number of working task nodes": "Количество работающих узлов задач",
        "The number of elapsed minutes after the last successful HBase backup started on your cluster. This metric is only reported for HBase clusters.": "Количество прошедших минут с момента начала последнего успешного резервного копирования HBase на вашем кластере. Эта метрика регистрируется только для кластеров HBase.",
        "The total number of concurrent data transfers": "Общее количество одновременных передач данных",
        "The number of blocks that need to be replicated one or more times": "Количество блоков, которые необходимо реплицировать один или несколько раз",
        # source quirk: EN typo "he percentage" (missing T) -> normal RU grammar (canon L4-IF.45)
        "he percentage of remaining memory available to YARN (`YARNMemoryAvailablePercentage` = `MemoryAvailableMB` / `MemoryTotalMB`)": "Процент оставшейся памяти, доступной для YARN (`YARNMemoryAvailablePercentage` = `MemoryAvailableMB` / `MemoryTotalMB`)",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon MQ monitoring": "Мониторинг Amazon MQ",
    "Amazon EMR (Elastic MapReduce) monitoring": "Мониторинг Amazon EMR (Elastic MapReduce)",
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
