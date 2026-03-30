---
title: Примечания к выпуску Dynatrace Operator версии 1.7.0
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-0
scraped: 2026-03-03T21:28:05.786009
---

**Дата выпуска:** 8 сентября 2025

> Рекомендуется обновиться до версии 1.7.1 для получения важных исправлений.

## Объявления

- **Сокращение монтирований** — уменьшено количество томов для инжекции модулей кода. Бинарные файлы OneAgent теперь в режиме только для чтения.
- **Управление размером эфемерных томов** через аннотации рабочих нагрузок.
- **Расширены разрешения ClusterRole `dynatrace-kubernetes-monitoring`** — добавлены: `customresourcedefinitions`, `ingresses`, `networkpolicies`, `endpointslices`, `horizontalpodautoscalers` (get/list/watch).

## Новые функции

- Сокращены OAuth-области для EdgeConnect provisioner (settings:object:write/read только для K8s-автоматизации)
- Настраиваемые `livenessProbe` для CSI-драйвера через Helm
- Предупреждение при `telemetryIngest` без указания `imageRef` (станет обязательным)
- Область `entities.read` больше не требуется; `settings.read`/`settings.write` стали необязательными

## Исправления

- Корректное удаление TLS-секрета при отключении ActiveGate
- `.spec.templates.logMonitoring.resources` применяется к init и основному контейнерам
- Валидация протоколов в `.spec.apiServer` EdgeConnect
- Обновления `.version` корректно применяются при отключенном `.autoUpdate`
- Замены для CSI liveness probe и node driver registrar (отключаемые через Helm)
- Исправлено переключение OTel endpoint при удалении ActiveGate
- Исправлены дублирующиеся имена портов в DaemonSet CSI
- Исправлен `runAsNonRoot` init-контейнера в OpenShift
- Прокси-настройки из `.spec.proxy` применяются к LogMonitoring
- Сетевая зона `.spec.networkZone` распространяется на LogMonitoring DaemonSet

## Известные проблемы

- Ложноположительные "Host is unavailable" при автомасштабировании
- OneAgent < 1.317 несовместим с сокращенными монтированиями

## Устаревание

- Helm-репо `dynatrace/helm-charts` устарел
- DynaKube API: `v1beta1`/`v1beta2` удалены; `v1beta3` будет удалена в 1.8.0
- Поле `.autoUpdate` устарело
- CSI sidecar бинарные файлы устарели
- OpenShift 4.10/4.11 больше не поддерживаются
- Событие "Mark for Termination" устарело (заменено событиями доступности в OneAgent 1.301)

## Обновление с версии 1.6

DynaKube API `v1beta1`/`v1beta2` не поддерживаются. Обновите манифесты до `v1beta5` перед обновлением.
