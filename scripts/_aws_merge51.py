# -*- coding: utf-8 -*-
"""Merge L4-IF.51 batch (Amazon MSK / Kafka) translations into the shared
cumulative dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Same mechanism as L4-IF.45-50: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. Any skeleton
key left without a translation, or any translation matching no skeleton key, is
reported (self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if51.json")


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

# ---- intro (form V1) + heading + date + main-dimension line ----
RU[en_v1("Amazon MSK (Kafka)")] = ru_v1("Amazon MSK (Kafka)")
RU["# Amazon MSK (Kafka) monitoring"] = "# Мониторинг Amazon MSK (Kafka)"
RU["* Updated on May 19, 2025"] = "* Обновлено 19 мая 2025 г."
RU["`Cluster Name` is the main dimension."] = "Основное измерение: `Cluster Name`."

# ---- metric descriptions (62 unique) ----
RU.update(
    {
        "Only one controller per cluster should be active at any given time.": "В любой момент времени активным должен быть только один контроллер на кластер.",
        "The number of bytes per second received from clients": "Количество байт в секунду, полученных от клиентов",
        "The number of bytes per second sent to clients": "Количество байт в секунду, отправленных клиентам",
        "The number of earned credits": "Количество заработанных кредитов",
        "The number of used credits": "Количество использованных кредитов",
        "The percentage of CPU idle time": "Процент времени простоя CPU",
        "The percentage of CPU in kernel space": "Процент CPU в пространстве ядра",
        "The percentage of CPU in user space": "Процент CPU в пользовательском пространстве",
        "The mean time in milliseconds that the consumer request is processed at the leader": "Среднее время в миллисекундах, в течение которого запрос потребителя обрабатывается на лидере",
        "The mean time in milliseconds that the consumer request waits in the request queue": "Среднее время в миллисекундах, в течение которого запрос потребителя ожидает в очереди запросов",
        "The mean time in milliseconds that the consumer request waits in the response queue": "Среднее время в миллисекундах, в течение которого запрос потребителя ожидает в очереди ответов",
        "The mean total time in milliseconds that consumers spend on fetching data from the broker": "Среднее суммарное время в миллисекундах, которое потребители тратят на извлечение данных из брокера",
        "The mean time in milliseconds that the follower request is processed at the leader": "Среднее время в миллисекундах, в течение которого запрос фолловера обрабатывается на лидере",
        "The mean time in milliseconds that the follower request waits in the request queue": "Среднее время в миллисекундах, в течение которого запрос фолловера ожидает в очереди запросов",
        "The mean time in milliseconds that the follower request waits in the response queue": "Среднее время в миллисекундах, в течение которого запрос фолловера ожидает в очереди ответов",
        "The mean time in milliseconds for the follower to send a response": "Среднее время в миллисекундах, за которое фолловер отправляет ответ",
        "The mean total time in milliseconds that followers spend on fetching data from the broker": "Среднее суммарное время в миллисекундах, которое фолловеры тратят на извлечение данных из брокера",
        "The number of fetch message conversions per second for the broker": "Количество преобразований сообщений при извлечении в секунду для брокера",
        "The mean total time in milliseconds that messages being fetched spend converting": "Среднее суммарное время в миллисекундах, которое извлекаемые сообщения тратят на преобразование",
        "The number of throttled bytes per second": "Количество байт в секунду, подвергнутых регулированию",
        "The number of messages in the throttle queue": "Количество сообщений в очереди регулирования",
        "The average fetch throttle time in milliseconds": "Среднее время регулирования извлечения в миллисекундах",
        "Total number of partitions across all brokers in the cluster": "Общее количество партиций на всех брокерах в кластере",
        "Total number of topics across all brokers in the cluster": "Общее количество топиков на всех брокерах в кластере",
        "The percentage of disk space used for application logs": "Процент дискового пространства, используемого для журналов приложения",
        "The percentage of disk space used for data logs": "Процент дискового пространства, используемого для журналов данных",
        "The number of leader replicas": "Количество реплик-лидеров",
        "The size in bytes of buffered memory for the broker": "Размер в байтах буферизованной памяти для брокера",
        "The size in bytes of cached memory for the broker": "Размер в байтах кэшированной памяти для брокера",
        "The size in bytes of memory that is free and available for the broker": "Размер в байтах памяти, свободной и доступной для брокера",
        "The size in bytes of memory that is in use for the broker": "Размер в байтах памяти, используемой брокером",
        "The number of incoming messages per second for the broker": "Количество входящих сообщений в секунду для брокера",
        "The maximum offset lag across all partitions in a topic": "Максимальное отставание смещения по всем партициям в топике",
        "The average percentage of the time the network processors are idle": "Средний процент времени, в течение которого сетевые процессоры простаивают",
        "The number of dropped receive packages": "Количество отброшенных пакетов при приёме",
        "The number of network receive errors for the broker": "Количество сетевых ошибок приёма для брокера",
        "The number of packets received by the broker": "Количество пакетов, полученных брокером",
        "The number of dropped transmit packages": "Количество отброшенных пакетов при передаче",
        "The number of network transmit errors for the broker": "Количество сетевых ошибок передачи для брокера",
        "The number of packets transmitted by the broker": "Количество пакетов, переданных брокером",
        "Total number of partitions that are offline in the cluster": "Общее количество партиций, находящихся офлайн в кластере",
        "The number of partitions for the broker": "Количество партиций для брокера",
        "The number of produce message conversions per second for the broker": "Количество преобразований сообщений при записи в секунду для брокера",
        "The mean time in milliseconds spent on message format conversions": "Среднее время в миллисекундах, затраченное на преобразование формата сообщений",
        "The mean time in milliseconds that request messages spend in the queue": "Среднее время в миллисекундах, в течение которого сообщения запросов находятся в очереди",
        "The mean time in milliseconds that response messages spend in the queue": "Среднее время в миллисекундах, в течение которого сообщения ответов находятся в очереди",
        "The mean time in milliseconds spent on sending response messages": "Среднее время в миллисекундах, затраченное на отправку сообщений ответов",
        "The average produce throttle time in milliseconds": "Среднее время регулирования записи в миллисекундах",
        "The mean produce time in milliseconds": "Среднее время записи в миллисекундах",
        "The mean number of request bytes for the broker": "Среднее количество байт запросов для брокера",
        "The average time in milliseconds spent in broker network and I/O threads to process requests that are exempt from throttling": "Среднее время в миллисекундах, проведённое в сетевых потоках и потоках ввода-вывода брокера для обработки запросов, освобождённых от регулирования",
        "The average percentage of the time the request handler threads are idle": "Средний процент времени, в течение которого потоки обработчика запросов простаивают",
        "The average request throttle time in milliseconds": "Среднее время регулирования запросов в миллисекундах",
        "The average time in milliseconds spent in broker network and I/O threads to process requests": "Среднее время в миллисекундах, проведённое в сетевых потоках и потоках ввода-вывода брокера для обработки запросов",
        "The percentage of the root disk used by the broker": "Процент корневого диска, используемого брокером",
        "The aggregated offset lag for all the partitions in a topic": "Совокупное отставание смещения по всем партициям в топике",
        "The size in bytes of swap memory that is available for the broker": "Размер в байтах памяти подкачки, доступной для брокера",
        "The size in bytes of swap memory that is in use for the broker": "Размер в байтах памяти подкачки, используемой брокером",
        "The number of under minIsr partitions for the broker": "Количество партиций ниже minIsr для брокера",
        "The number of under-replicated partitions for the broker": "Количество партиций с недостаточной репликацией для брокера",
        "Mean latency in milliseconds for ZooKeeper requests from broker": "Средняя задержка в миллисекундах для запросов ZooKeeper от брокера",
        "Connection status of broker's ZooKeeper session which may be one of the following: `NOT_CONNECTED`: `0.0`, `ASSOCIATING`: `0.1`, `CONNECTING`: `0.5`, `CONNECTEDREADONLY`: `0.8`, `CONNECTED`: `1.0`, `CLOSED`: `5.0`, `AUTH_FAILED`: `10.0`.": "Статус подключения сеанса ZooKeeper брокера, который может принимать одно из следующих значений: `NOT_CONNECTED`: `0.0`, `ASSOCIATING`: `0.1`, `CONNECTING`: `0.5`, `CONNECTEDREADONLY`: `0.8`, `CONNECTED`: `1.0`, `CLOSED`: `5.0`, `AUTH_FAILED`: `10.0`.",
    }
)

# ---- frontmatter title (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon MSK (Kafka) monitoring": "Мониторинг Amazon MSK (Kafka)",
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
