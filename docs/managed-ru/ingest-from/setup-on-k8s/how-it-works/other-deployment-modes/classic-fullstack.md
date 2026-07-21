---
title: Классический мониторинг Full-Stack
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack
---

# Классический мониторинг Full-Stack

# Классический мониторинг Full-Stack

* Чтение: 2 мин
* Опубликовано 31 окт. 2024 г.

Классический мониторинг Full-Stack объединяет мониторинг хостов и приложений для сред Kubernetes. Инструментированные поды сохраняют свою связь с хостами, что обеспечивает сбор метрик хостов.

Дополнительную информацию можно найти в разделе [`.spec.oneAgent.classicFullStack`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") документации по DynaKube.

## Возможности

* Инструментированные поды сохраняют таксономическую связь с хостами и метриками хостов. OneAgent дополняет модули кода обнаружением OOM, мониторингом дисков и хранилища, мониторингом сети и другими возможностями.
* Этот комплексный подход включает мониторинг кластера Kubernetes, распределённую трассировку, изоляцию доменов сбоев и глубокую аналитику на уровне кода с использованием единой конфигурации развёртывания для всех кластеров.

## Ограничения

Классический режим Full-Stack не поддерживается при использовании [платформенного токена](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

Существует зависимость запуска между контейнером, в котором развёрнут OneAgent, и контейнером приложения, который нужно инструментировать (например, контейнеры с включённым глубоким мониторингом процессов). Контейнер OneAgent должен быть запущен, а процесс `oneagenthelper` должен работать до запуска контейнера приложения, чтобы обеспечить корректную инструментацию.

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/манифесты в рамках базовой установки. Дополнительную информацию можно найти в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") управляет автоматическим развёртыванием, конфигурацией и жизненным циклом компонентов Dynatrace в среде Kubernetes.
* [Вебхук Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") проверяет определения DynaKube, преобразует определения с более старыми версиями API и внедряет конфигурации в поды.

### Компоненты, управляемые Operator

Следующие компоненты развёртываются при применении DynaKube с полным стеком наблюдаемости:

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") собирает метрики хостов с узлов Kubernetes.
* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") направляет данные наблюдаемости в кластер Dynatrace и отслеживает API Kubernetes.

![classic-full-stack](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-37-54-pm-2354-6d55b949e0.png)

classic-full-stack

Для классического внедрения full-stack требуется *доступ на запись* из пода OneAgent к файловой системе узла Kubernetes для обнаружения новых развёрнутых контейнеров и внедрения в них.