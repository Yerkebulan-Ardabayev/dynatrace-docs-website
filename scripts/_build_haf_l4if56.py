# -*- coding: utf-8 -*-
"""L4-IF.56 builder: setup-on-k8s/guides/high-availability batch (3 files).

Derives RU from EN line-by-line (code-fence-aware) to guarantee:
- line-parity (EN line count == RU line count),
- byte-identical code fences / blank lines / source: / scraped:,
- URL identity (all link/anchor targets copied verbatim inside translated lines),
- LF line endings (RU canon),
- clean RU (no em-dash, no scraping mojibake â / BOM).

Translation map keys are the STRIPPED EN line; leading indentation is re-applied
from the EN line, so nested list markers keep their exact whitespace. Any prose
line missing from the map raises -> catches leftover-EN.
"""

import os
import re

# Scraping mojibake: UTF-8 BOM mis-decoded as Latin-1 (ï»¿ = U+00EF U+00BB U+00BF)
# plus a stray real BOM. Stripped from both EN lookup key and RU output so the
# match is mojibake-insensitive and the RU stays clean.
MOJI_RE = re.compile("[﻿ï»¿]")

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
SUB = "ingest-from/setup-on-k8s/guides/high-availability"

# ----------------------------------------------------------------------------
# Per-file translation maps: stripped EN line -> stripped RU line.
# ----------------------------------------------------------------------------
TRANS = {
    "api-request-threshold.md": {
        "title: Configure minimum time between requests": "title: Настройка минимального интервала между запросами",
        "# Configure minimum time between requests": "# Настройка минимального интервала между запросами",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "Dynatrace Operator version 1.2.0+": "Dynatrace Operator версии 1.2.0+",
        "In Dynatrace Operator version 0.11.0 until 1.2.0, this configuration was "
        "set using the annotation feature.dynatrace.com/dynatrace-api-request-threshold.": "В версиях Dynatrace Operator с 0.11.0 до 1.2.0 эта конфигурация "
        "задавалась с помощью аннотации feature.dynatrace.com/dynatrace-api-request-threshold.",
        "Dynatrace Operator makes regular calls to Dynatrace to gather the "
        "information necessary to function properly.": "Dynatrace Operator регулярно обращается к Dynatrace, чтобы собирать "
        "информацию, необходимую для корректной работы.",
        "The minimum time between requests from the Dynatrace Operator, which was "
        "previously hard coded to 15 minutes to reduce network load, can now be configured.": "Минимальный интервал между запросами от Dynatrace Operator, ранее "
        "жёстко заданный как 15 минут для снижения нагрузки на сеть, теперь можно настроить.",
        "To set this time (in minutes), set the field `dynatraceApiRequestThreshold`.": "Чтобы задать этот интервал (в минутах), укажите поле `dynatraceApiRequestThreshold`.",
        "The Operator makes three different types of requests for:": "Operator выполняет три различных типа запросов:",
        "* ActiveGate connection details": "* сведения о подключении ActiveGate",
        "* OneAgent connection details": "* сведения о подключении OneAgent",
        "* Token scope verification": "* проверка области действия токена",
        "The specified interval is counted independently for each of these request types.": "Указанный интервал отсчитывается независимо для каждого из этих типов запросов.",
    },
    "priority.md": {
        "title: Use priorityClass for critical Dynatrace components": "title: Использование priorityClass для критически важных компонентов Dynatrace",
        "# Use priorityClass for critical Dynatrace components": "# Использование priorityClass для критически важных компонентов Dynatrace",
        "* 1-min read": "* Чтение: 1 мин",
        "* Published Jul 28, 2023": "* Опубликовано 28 июля 2023 г.",
        "Starting with Dynatrace Operator version 0.8.0+, a `priorityClass` object "
        "is created by default when installing the Dynatrace Operator. This priority "
        "class is initially set to a high value to ensure that the components that "
        "use it have a higher priority than other pods, and that critical components "
        "like the CSI driver are scheduled by Kubernetes. For details, see the "
        "[Kubernetes documentation on PriorityClass﻿]"
        "(https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass).": "Начиная с Dynatrace Operator версии 0.8.0+, при установке Dynatrace "
        "Operator по умолчанию создаётся объект `priorityClass`. Этому классу "
        "приоритета изначально присваивается высокое значение, чтобы компоненты, "
        "которые его используют, имели более высокий приоритет, чем другие поды, "
        "и чтобы такие критически важные компоненты, как CSI-драйвер, "
        "планировались Kubernetes. Подробнее см. [документацию Kubernetes по "
        "PriorityClass]"
        "(https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass).",
        "You can change the default value of this parameter according to your "
        "environment and the individual use of priority classes within your cluster. "
        "Be aware that lowering the default value might impact the scheduling of the "
        "pods created by Dynatrace. `priorityClass` is used on the CSI driver pods by "
        "default, but it can also be used on OneAgent pods (see the `priorityClassName` "
        "parameter in [DynaKube parameters]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"List the available parameters for setting up Dynatrace Operator on Kubernetes.")).': "Вы можете изменить значение этого параметра по умолчанию в соответствии "
        "с вашей средой и индивидуальным использованием классов приоритета в "
        "вашем кластере. Учтите, что понижение значения по умолчанию может "
        "повлиять на планирование подов, создаваемых Dynatrace. По умолчанию "
        "`priorityClass` применяется к подам CSI-драйвера, но его также можно "
        "использовать для подов OneAgent (см. параметр `priorityClassName` в "
        "разделе [Параметры DynaKube]"
        "(/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "
        '"Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")).',
    },
    "high-availability.md": {
        "title: Configure high availability for Dynatrace Operator webhook": "title: Настройка высокой доступности для вебхука Dynatrace Operator",
        "# Configure high availability for Dynatrace Operator webhook": "# Настройка высокой доступности для вебхука Dynatrace Operator",
        "* 1-min read": "* Чтение: 1 мин",
        "* Updated on Feb 27, 2026": "* Обновлено 27 февраля 2026 г.",
        "## Configure high availability": "## Настройка высокой доступности",
        "Dynatrace Operator version 1.9.0+": "Dynatrace Operator версии 1.9.0+",
        "You can customize the `replicas`, `topologySpreadConstraints`, and "
        "`podDisruptionBudget` values independently:": "Вы можете настраивать значения `replicas`, `topologySpreadConstraints` "
        "и `podDisruptionBudget` независимо друг от друга:",
        "The examples below use Helm values. If you deploy using manifests, you can "
        "achieve the same by adjusting the corresponding sections in your deployment "
        "manifest directly.": "В примерах ниже используются значения Helm. Если вы развёртываете с "
        "помощью манифестов, того же можно добиться, напрямую изменив "
        "соответствующие разделы в вашем манифесте развёртывания.",
        "You must keep `highAvailability` set to `true` (the default value) for the "
        "`replicas`, `topologySpreadConstraints`, and `podDisruptionBudget` values to "
        "take effect. If you set `highAvailability` to `false`, these fields are "
        "ignored. This ensures backward compatibility for users who previously "
        "disabled the high availability mode.": "Чтобы значения `replicas`, `topologySpreadConstraints` и "
        "`podDisruptionBudget` вступили в силу, необходимо оставить "
        "`highAvailability` в значении `true` (значение по умолчанию). Если "
        "задать для `highAvailability` значение `false`, эти поля игнорируются. Это "
        "обеспечивает обратную совместимость для пользователей, которые ранее "
        "отключали режим высокой доступности.",
        "### Changes to topology spread constraints": "### Изменения в ограничениях распределения по топологии",
        "The default `topologySpreadConstraints` is now `whenUnsatisfiable: "
        "ScheduleAnyway` instead of the previous `whenUnsatisfiable: DoNotSchedule`. "
        "This change makes scheduling less aggressive, so the webhook pods can still "
        "be scheduled in environments where only a few nodes (one or two) are "
        "available. Previously, `DoNotSchedule` could prevent pods from being "
        "scheduled if the topology constraints couldn't be fully satisfied.": "Теперь значением по умолчанию для `topologySpreadConstraints` является "
        "`whenUnsatisfiable: ScheduleAnyway` вместо прежнего `whenUnsatisfiable: "
        "DoNotSchedule`. Это изменение делает планирование менее агрессивным, "
        "поэтому поды вебхука по-прежнему могут планироваться в средах, где "
        "доступно лишь несколько узлов (один или два). Раньше значение "
        "`DoNotSchedule` могло препятствовать планированию подов, если "
        "ограничения топологии не удавалось полностью удовлетворить.",
        "## Legacy `highAvailability` Helm value (**deprecated**)": "## Прежнее значение Helm `highAvailability` (**устарело**)",
        "Dynatrace Operator version 0.6.0+": "Dynatrace Operator версии 0.6.0+",
        "Starting with Operator version 1.9.0, the `highAvailability` value is "
        "deprecated in favor of the `replicas`, `topologySpreadConstraints`, and "
        "`podDisruptionBudget` values. See [Configure high availability]"
        "(#configure-high-availability) for the recommended approach.": "Начиная с версии Operator 1.9.0, значение `highAvailability` устарело "
        "в пользу значений `replicas`, `topologySpreadConstraints` и "
        "`podDisruptionBudget`. Рекомендуемый подход см. в разделе [Настройка "
        "высокой доступности](#configure-high-availability).",
        "The legacy `highAvailability` Helm value offered the following capabilities:": "Прежнее значение Helm `highAvailability` предоставляло следующие возможности:",
        "* Increases replicas to two replicas for webhook deployment.": "* Увеличивает число реплик до двух для развёртывания вебхука.",
        "* Adds [pod topology spread constraints﻿](https://dt-url.net/xc03ysw):": "* Добавляет [ограничения распределения подов по топологии](https://dt-url.net/xc03ysw):",
        "+ Pods are spread across different nodes, with the nodes in different zones where possible.": "+ Поды распределяются по разным узлам, причём узлы по возможности находятся в разных зонах.",
        "+ Multiple pods are allowed in the same zone.": "+ В одной зоне допускается несколько подов.",
        "* Adds [pod disruption budget﻿](https://dt-url.net/m303yfk):": "* Добавляет [бюджет прерывания работы подов](https://dt-url.net/m303yfk):",
        "+ It restricts graceful shutdowns of the webhook pod if it's the last remaining pod.": "+ Он ограничивает корректное завершение работы пода вебхука, если это последний оставшийся под.",
    },
}


def read_lf(p):
    with open(p, "r", encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def build(fname):
    en_path = os.path.join(BASE, "managed", SUB, fname)
    ru_path = os.path.join(BASE, "managed-ru", SUB, fname)
    en_lines = read_lf(en_path).split("\n")
    tmap = {MOJI_RE.sub("", k): v for k, v in TRANS[fname].items()}
    out = []
    in_fence = False
    for ln in en_lines:
        stripped = MOJI_RE.sub("", ln.strip())
        if stripped.startswith("```"):
            in_fence = not in_fence
            out.append(ln)
            continue
        if in_fence:
            out.append(ln)
            continue
        if stripped == "":
            out.append(ln)
            continue
        if stripped == "---":
            out.append(ln)
            continue
        if stripped.startswith("source:") or stripped.startswith("scraped:"):
            out.append(ln)
            continue
        if stripped in tmap:
            indent = ln[: len(ln) - len(ln.lstrip())]
            out.append(indent + tmap[stripped])
            continue
        raise SystemExit(f"[{fname}] UNTRANSLATED: {ln!r}")

    assert len(out) == len(en_lines), f"{fname}: parity {len(out)} != {len(en_lines)}"
    os.makedirs(os.path.dirname(ru_path), exist_ok=True)
    with open(ru_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out))
    print(f"OK  {fname}: {len(out)} lines -> {ru_path}")


if __name__ == "__main__":
    for fn in TRANS:
        build(fn)
