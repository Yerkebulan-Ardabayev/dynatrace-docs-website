---
title: Full-stack observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack
scraped: 2026-03-05T21:25:24.269087
---

# Полноуровневая наблюдаемость

# Полноуровневая наблюдаемость

* Latest Dynatrace
* 3-min read
* Published Oct 31, 2024

Полноуровневая наблюдаемость объединяет мониторинг инфраструктуры и приложений в средах Kubernetes. Эта конфигурация включает внедрение Dynatrace OneAgent и обеспечивает видимость как производительности кластера, так и поведения приложений.

Дополнительную информацию смотрите в разделе [`.spec.oneAgent.cloudNativeFullStack`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") документации DynaKube.

## Возможности

* Предлагает функциональность, аналогичную классическому полноуровневому внедрению.
* Использует мутирующие веб-хуки для внедрения кодовых модулей в Pod-ы приложений.
* Обеспечивает обогащение данных для сред Kubernetes через [файлы обогащения](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

### Текущие ограничения

* Диагностические файлы (архивы поддержки) для Pod-ов приложений пока не поддерживаются.
* Правила мониторинга контейнеров не поддерживаются (параметр выбора меток DynaKube предоставляет аналогичную функциональность).
* [Статический мониторинг Go](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Learn the limitations for Go support and their workarounds.") поддерживается частично.
* Архивы поддержки OneAgent, например журналы кодовых модулей, можно собирать из отслеживаемого процесса/Pod-а с помощью пункта меню **Run OneAgent Diagnostics** на странице конкретного процесса. Если архив поддержки OneAgent недоступен, это означает одно из следующего:

  + В Pod приложения не был внедрён кодовый модуль.
  + Возникла проблема при создании архива поддержки OneAgent.

## Развёртываемые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты разворачиваются через Helm/манифесты в рамках базовой установки. Дополнительную информацию смотрите в соответствующих разделах:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") управляет автоматическим развёртыванием, конфигурацией и жизненным циклом компонентов Dynatrace в среде Kubernetes.
* [Веб-хук Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") проверяет определения DynaKube, конвертирует определения со старыми версиями API и внедряет конфигурации в Pod-ы.
* [CSI Driver Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") развёртывается как DaemonSet и предоставляет доступное для записи хранилище томов для бинарных файлов OneAgent, чтобы минимизировать использование сети и хранилища.

### Компоненты, управляемые Operator

Следующие компоненты развёртываются при применении DynaKube с полноуровневой наблюдаемостью:

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") собирает метрики хоста с узлов Kubernetes.
* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") маршрутизирует данные наблюдаемости в кластер Dynatrace и отслеживает Kubernetes API.
* Кодовые модули Dynatrace внедряются в ваше приложение для обеспечения глубокого мониторинга и наблюдаемости.

![cloud-native](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-40-02-pm-2352-4cba84df51.png)
