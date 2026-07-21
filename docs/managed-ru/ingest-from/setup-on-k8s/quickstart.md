---
title: Быстрый старт
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/quickstart
---

# Быстрый старт

# Быстрый старт

* Чтение 2 мин
* Обновлено 18 дек. 2024 г.

Эта страница поможет установить компоненты Dynatrace в течение минуты на кластере Kubernetes, чтобы быстро получить пользу от платформы наблюдаемости и аналитики Dynatrace.

Предварительные требования

Перед установкой Dynatrace на кластере Kubernetes убедись, что выполнены следующие требования:

* CLI `kubectl` подключён к кластеру Kubernetes, который нужно мониторить.
* Есть достаточные привилегии на мониторируемом кластере для выполнения команд `kubectl` или `oc`. Если не используется роль кластера `cluster-admin`, см. [права доступа для развёртывания](/managed/ingest-from/setup-on-k8s/reference/security#deployment-permissions "Эта страница содержит обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых прав доступа") для необходимых разрешений.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик (egress) для подов Dynatrace (по умолчанию: пространство имён Dynatrace) до URL среды Dynatrace.

  + Для Dynatrace Managed можно опционально использовать URL кластера ActiveGate.
* Для OpenShift Dedicated нужна [роль cluster-admin﻿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm Используй [Helm версии 3﻿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформы](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") Kubernetes/OpenShift и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

## Развёртывание Dynatrace Operator

Получить аналитику и практические ответы по платформе Kubernetes, а также по контейнеризованным приложениям можно, [развернув Dynatrace для полной наблюдаемости Kubernetes](/managed/ingest-from/setup-on-k8s/deployment#fullObs "Развёртывание Dynatrace Operator на Kubernetes") в режиме cloud-native full-stack.

1. Перейди в **Kubernetes**.
2. Выбери **Connect automatically via Dynatrace Operator**.
3. Следуй инструкциям на экране.

![quickstart](https://dt-cdn.net/images/quickstart-2nd-gen-2976-cd3bfad512.png)

quickstart

## Узнать больше

[### Режим развёртывания

Определи рекомендуемый режим развёртывания для нужной конфигурации на основе требований.](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes")[### Интеграции

Используй компоненты с открытым исходным кодом для приёма дополнительных сигналов наблюдаемости в Dynatrace.](/managed/ingest-from/setup-on-k8s/extend-observability-k8s "Как приём данных можно расширить с помощью компонентов с открытым исходным кодом")[### Как это работает

Ознакомься с компонентами Dynatrace, которые развёртываются в кластере Kubernetes.](/managed/ingest-from/setup-on-k8s/how-it-works "Подробное описание того, как работает развёртывание на Kubernetes.")[### Руководства

Узнай, как настроить Dynatrace Operator для поддержки конкретных сценариев использования.](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев использования")[### Получить практические ответы

Начни анализировать кластеры Kubernetes и контейнеризованные приложения с помощью Dynatrace и получай пользу от практических ответов.](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")

## Связанные темы

* [Мониторинг кластера и рабочих нагрузок Kubernetes﻿](https://www.dynatrace.com/technologies/kubernetes-monitoring/)