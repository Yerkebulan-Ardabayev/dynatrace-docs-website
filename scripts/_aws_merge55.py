# -*- coding: utf-8 -*-
"""Merge L4-IF.55 batch (AWS iot.md, broken/mislabeled-header) prose/Description
translations into the shared cumulative dicts.

Same mechanism as L4-IF.45-54. Self-validation reports uncovered skeleton keys or
unused translations. Asserts: no em-dash, no mojibake in RU.

Canon: status codes (`CANCELED`/`FAILED`/`IN_PROGRESS`/`QUEUED`/`REJECTED`/
`REMOVED`/`SUCCESS`), MQTT message types (`CONNECT`/`PUBLISH`/`SUBSCRIBE`/
`UNSUBSCRIBE`), dimension names (`JobId`/`Protocol`/`RuleName`/`ActionType`) and
shadow ops (`DeleteThingShadow`/`GetThingShadow`/`UpdateThingShadow`) stay EN in
backticks. message broker->брокер сообщений, dimension->измерение, contains->
содержит, throttled->подвергнутых регулированию, log events->события журнала,
topic->топик, job execution->выполнение задания. Intro form V1. Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if55.json")


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


# helper: status-change / status-is job-execution sentences (highly repetitive)
def changed_to(st):
    return (
        "The number of job executions whose status has changed to `%s` within a time period "
        "that is determined by CloudWatch. The `JobId` dimension contains the ID of the job."
        % st
    )


def ru_changed_to(st):
    return (
        "Количество выполнений задания, статус которых изменился на `%s` в течение периода времени, "
        "определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания."
        % st
    )


def status_is(st):
    return (
        "The total number of job executions whose status is `%s` for the given job. "
        "The `JobId` dimension contains the ID of the job." % st
    )


def ru_status_is(st):
    return (
        "Общее количество выполнений задания со статусом `%s` для данного задания. "
        "Измерение `JobId` содержит идентификатор задания." % st
    )


RU = {}

# ---- title / H1 / intro ----
RU["# AWS IoT monitoring"] = "# Мониторинг AWS IoT"
RU[en_v1("AWS IoT")] = ru_v1("AWS IoT")

# ---- job-execution status sentences (CANCELED/FAILED/IN_PROGRESS/QUEUED/REJECTED/REMOVED/SUCCESS) ----
for st in [
    "CANCELED",
    "FAILED",
    "IN_PROGRESS",
    "QUEUED",
    "REJECTED",
    "REMOVED",
    "SUCCESS",
]:
    RU[changed_to(st)] = ru_changed_to(st)
    RU[status_is(st)] = ru_status_is(st)

# ---- connection / publish / subscribe / unsubscribe / shadow / rules descriptions ----
RU.update(
    {
        "The number of client errors generated while executing the job. The `JobId` dimension contains the ID of the job.": "Количество клиентских ошибок, возникших при выполнении задания. Измерение `JobId` содержит идентификатор задания.",
        # CONNECT
        "The number of connection requests that could not be authorized by the message broker. The `Protocol` dimension contains the protocol used to send the `CONNECT` message.": "Количество запросов на подключение, которые не удалось авторизовать брокеру сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`.",
        "The number of connection requests rejected because the MQTT message did not meet the requirements defined in AWS IoT quotas. The `Protocol` dimension contains the protocol used to send the `CONNECT` message.": "Количество запросов на подключение, отклонённых из-за того, что сообщение MQTT не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`.",
        "The number of connection requests that failed because an internal error occurred. The `Protocol` dimension contains the protocol used to send the `CONNECT` message.": "Количество запросов на подключение, которые завершились неудачей из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`.",
        "The number of successful connections to the message broker. The `Protocol` dimension contains the protocol used to send the `CONNECT` message.": "Количество успешных подключений к брокеру сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`.",
        "The number of connection requests that were throttled because the account exceeded the allowed connect request rate. The `Protocol` dimension contains the protocol used to send the `CONNECT` message.": "Количество запросов на подключение, подвергнутых регулированию из-за того, что аккаунт превысил допустимую частоту запросов на подключение. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`.",
        # shadow ops
        "The number of `DeleteThingShadow` requests processed successfully. The `Protocol` dimension contains the protocol used to make the request.": "Количество запросов `DeleteThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса.",
        "The number of `GetThingShadow` requests processed successfully. The `Protocol` dimension contains the protocol used to make the request.": "Количество запросов `GetThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса.",
        "The number of `UpdateThingShadow` requests processed successfully. The `Protocol` dimension contains the protocol used to make the request.": "Количество запросов `UpdateThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса.",
        # rule actions
        "The number of failed rule action invocations. The `RuleName` dimension contains the name of the rule that specifies the action. The `ActionType` dimension contains the type of action that was invoked.": "Количество неуспешных вызовов действий правила. Измерение `RuleName` содержит имя правила, задающего действие. Измерение `ActionType` содержит тип вызванного действия.",
        "The number of successful rule action invocations. The `RuleName` dimension contains the name of the rule that specifies the action. The `ActionType` dimension contains the type of action that was invoked.": "Количество успешных вызовов действий правила. Измерение `RuleName` содержит имя правила, задающего действие. Измерение `ActionType` содержит тип вызванного действия.",
        # log events
        "The singular batch of log events that has failed to publish due to throttling errors": "Отдельный пакет событий журнала, который не удалось опубликовать из-за ошибок регулирования",
        "The number of log events within the batch that have failed to publish due to throttling errors": "Количество событий журнала в пакете, которые не удалось опубликовать из-за ошибок регулирования",
        # rules engine / parse / topic
        "The number of JSON parse errors that occurred in messages published on a topic on which a rule is listening. The `RuleName` dimension contains the name of the rule.": "Количество ошибок разбора JSON, возникших в сообщениях, опубликованных в топике, который прослушивает правило. Измерение `RuleName` содержит имя правила.",
        "The number of ping messages received by the message broker. The `Protocol` dimension contains the protocol used to send the ping message.": "Количество ping-сообщений, полученных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки ping-сообщения.",
        "The number of messages throttled by the rules engine because of malicious behavior or because the number of messages exceeds the rules engine's throttle limit. The `RuleName` dimension contains the name of the rule to be triggered.": "Количество сообщений, подвергнутых регулированию механизмом правил из-за вредоносного поведения или из-за того, что количество сообщений превышает лимит регулирования механизма правил. Измерение `RuleName` содержит имя правила, которое должно быть запущено.",
        "The rule to be triggered could not be found. The `RuleName` dimension contains the name of the rule.": "Не удалось найти правило, которое должно быть запущено. Измерение `RuleName` содержит имя правила.",
        "The number of AWS IoT rules executed": "Количество выполненных правил AWS IoT",
        "The number of incoming messages published on a topic on which a rule is listening. The `RuleName` dimension contains the name of the rule.": "Количество входящих сообщений, опубликованных в топике, который прослушивает правило. Измерение `RuleName` содержит имя правила.",
        # PUBLISH
        "The number of publish requests the message broker was unable to authorize. The `Protocol` dimension contains the protocol used to publish the message.": "Количество запросов на публикацию, которые брокер сообщений не смог авторизовать. Измерение `Protocol` содержит протокол, использованный для публикации сообщения.",
        "The number of publish requests rejected by the message broker because the message did not meet the requirements defined in AWS IoT quotas. The `Protocol` dimension contains the protocol used to publish the message.": "Количество запросов на публикацию, отклонённых брокером сообщений из-за того, что сообщение не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для публикации сообщения.",
        "The number of publish requests the message broker failed to process because an internal error occurred. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, которые брокер сообщений не смог обработать из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        "The number of publish requests successfully processed by the message broker. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        "The number of publish request that were throttled because the client exceeded the allowed inbound message rate. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, подвергнутых регулированию из-за того, что клиент превысил допустимую частоту входящих сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        "The number of publish requests made by the message broker that could not be authorized by AWS IoT. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, сделанных брокером сообщений, которые не удалось авторизовать в AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        "The number of publish requests made by the message broker that were rejected because the message did not meet the requirements defined in AWS IoT quotas. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, сделанных брокером сообщений, которые были отклонены из-за того, что сообщение не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        "The number of publish requests successfully made by the message broker. The `Protocol` dimension contains the protocol used to send the `PUBLISH` message.": "Количество запросов на публикацию, успешно сделанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`.",
        # SUBSCRIBE
        "The number of subscription requests made by a client that could not be authorized. The `Protocol` dimension contains the protocol used to send the `SUBSCRIBE` message.": "Количество запросов на подписку, сделанных клиентом, которые не удалось авторизовать. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`.",
        "The number of subscribe requests that were rejected because the `SUBSCRIBE` message did not meet the requirements defined in AWS IoT quotas. The `Protocol` dimension contains the protocol used to send the `SUBSCRIBE` message.": "Количество запросов на подписку, отклонённых из-за того, что сообщение `SUBSCRIBE` не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`.",
        "The number of subscribe requests that were rejected because an internal error occurred. The `Protocol` dimension contains the protocol used to send the `SUBSCRIBE` message.": "Количество запросов на подписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`.",
        "The number of subscribe requests that were successfully processed by the message broker. The `Protocol` dimension contains the protocol used to send the `SUBSCRIBE` message.": "Количество запросов на подписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`.",
        "The number of subscribe requests that were throttled because the client exceeded the allowed subscribe request rate. The `Protocol` dimension contains the protocol used to send the `SUBSCRIBE` message.": "Количество запросов на подписку, подвергнутых регулированию из-за того, что клиент превысил допустимую частоту запросов на подписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`.",
        # UNSUBSCRIBE
        "The number of unsubscribe requests that were rejected because the `UNSUBSCRIBE` message did not meet the requirements defined in AWS IoT quotas. The `Protocol` dimension contains the protocol used to send the `UNSUBSCRIBE` message.": "Количество запросов на отписку, отклонённых из-за того, что сообщение `UNSUBSCRIBE` не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`.",
        "The number of unsubscribe requests that were rejected because an internal error occurred. The `Protocol` dimension contains the protocol used to send the `UNSUBSCRIBE` message.": "Количество запросов на отписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`.",
        "The number of unsubscribe requests that were successfully processed by the message broker. The `Protocol` dimension contains the protocol used to send the `UNSUBSCRIBE` message.": "Количество запросов на отписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`.",
        "The number of unsubscribe requests that were rejected because the client exceeded the allowed unsubscribe request rate. The `Protocol` dimension contains the protocol used to send the `UNSUBSCRIBE` message.": "Количество запросов на отписку, отклонённых из-за того, что клиент превысил допустимую частоту запросов на отписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`.",
    }
)

ADD_TITLES = {"AWS IoT monitoring": "Мониторинг AWS IoT"}


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
