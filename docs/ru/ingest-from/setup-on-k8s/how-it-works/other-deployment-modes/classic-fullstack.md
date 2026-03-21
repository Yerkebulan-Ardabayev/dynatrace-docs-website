---
title: Мониторинг Classic Full-Stack
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack
scraped: 2026-03-05T21:26:07.681929
---

# Classic Full-Stack monitoring


* Latest Dynatrace
* 2-min read

Classic Full-Stack monitoring интегрирует мониторинг хостов и приложений для сред Kubernetes. Инструментированные поды сохраняют свою связь с хостами, что позволяет собирать метрики хостов.

Дополнительную информацию см. в разделе [`.spec.oneAgent.classicFullStack`](../../reference/dynakube-parameters.md "List the available parameters for setting up Dynatrace Operator on Kubernetes.") документации DynaKube.

## Возможности

* Инструментированные поды сохраняют таксономическую связь с хостами и метриками хостов. OneAgent дополняет кодовые модули обнаружением OOM, мониторингом дисков и хранилищ, мониторингом сети и многим другим.
* Этот универсальный подход включает мониторинг кластера Kubernetes, распределённую трассировку, изоляцию домена сбоев и глубокое понимание на уровне кода с использованием единой конфигурации развёртывания для всех ваших кластеров.

## Ограничения

Существует зависимость запуска между контейнером, в котором развёрнут OneAgent, и контейнером приложения, подлежащего инструментированию (например, контейнеры с включённым глубоким мониторингом процессов). Контейнер OneAgent должен быть запущен, и процесс `oneagenthelper` должен выполняться до запуска контейнера приложения, чтобы обеспечить корректное инструментирование.

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/манифесты в рамках базовой установки. Подробную информацию см. в соответствующих разделах:

* [Dynatrace Operator](../components/dynatrace-operator.md#operator "Components of Dynatrace Operator") управляет автоматическим развёртыванием, конфигурацией и жизненным циклом компонентов Dynatrace в вашей среде Kubernetes.
* [Веб-хук Dynatrace Operator](../components/dynatrace-operator.md#webhook "Components of Dynatrace Operator") проверяет определения DynaKube, конвертирует определения со старыми версиями API и внедряет конфигурации в поды.

### Компоненты, управляемые оператором

Следующие компоненты развёртываются путём применения DynaKube с наблюдаемостью полного стека:

* [Dynatrace OneAgent](../../../dynatrace-oneagent.md "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") собирает метрики хостов с узлов Kubernetes.
* [Dynatrace ActiveGate](../../../dynatrace-activegate.md "Understand the basic concepts related to ActiveGate.") маршрутизирует данные наблюдаемости в кластер Dynatrace и осуществляет мониторинг Kubernetes API.

![classic-full-stack](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-37-54-pm-2354-6d55b949e0.png)

Внедрение Classic full-stack требует *доступа на запись* от пода OneAgent в файловую систему узла Kubernetes для обнаружения и внедрения в новые развёрнутые контейнеры.
