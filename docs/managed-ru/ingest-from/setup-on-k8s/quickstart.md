---
title: Быстрый старт
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/quickstart
scraped: 2026-05-12T11:11:16.232515
---

# Быстрый старт

# Быстрый старт

* Чтение: 2 мин
* Обновлено 18 декабря 2024 г.

Эта страница поможет вам за минуту установить компоненты Dynatrace в вашем кластере Kubernetes, чтобы быстро начать пользоваться платформой observability и аналитики Dynatrace.

Предварительные требования

Перед установкой Dynatrace в кластере Kubernetes убедитесь, что вы соответствуете следующим требованиям:

* Ваш CLI `kubectl` подключён к кластеру Kubernetes, который вы хотите мониторить.
* У вас достаточно прав на отслеживаемом кластере для запуска команд `kubectl` или `oc`.

### Настройка и конфигурация кластера

* Необходимо разрешить исходящий трафик для подов Dynatrace (по умолчанию: пространство имён Dynatrace) к URL вашего окружения Dynatrace.

  + Для Dynatrace Managed дополнительно можно использовать URL Cluster ActiveGate.
* Для OpenShift Dedicated необходима [роль cluster-adminï»¿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Установка Helm: используйте [Helm версии 3ï»¿](https://dt-url.net/n5036j1).

### Поддерживаемые версии

См. поддерживаемые [версии платформ](/managed/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы") и [дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.") Kubernetes/OpenShift.

## Разверните Dynatrace Operator

Вы получите инсайты и actionable answers по вашей платформе Kubernetes, а также по вашим контейнерным приложениям, [развернув Dynatrace для Full Kubernetes Observability](/managed/ingest-from/setup-on-k8s/deployment#fullObs "Разверните Dynatrace Operator в Kubernetes") в режиме cloud-native full-stack.

1. Перейдите в **Kubernetes**.
2. Выберите **Connect automatically via Dynatrace Operator**.
3. Следуйте инструкциям на экране.

![quickstart](https://dt-cdn.net/images/quickstart-2nd-gen-2976-cd3bfad512.png)

quickstart

## Узнать больше

[### Режим развёртывания

Определите рекомендуемый режим развёртывания для вашей установки с учётом ваших требований.](/managed/ingest-from/setup-on-k8s/deployment "Разверните Dynatrace Operator в Kubernetes")[### Интеграции

Используйте open source компоненты для приёма дополнительных сигналов observability в Dynatrace.](/managed/ingest-from/setup-on-k8s/extend-observability-k8s "Как расширить приём данных с помощью open source компонентов")[### Как это работает

Ознакомьтесь с компонентами Dynatrace, которые разворачиваются в вашем кластере Kubernetes.](/managed/ingest-from/setup-on-k8s/how-it-works "Подробное описание того, как работает развёртывание в Kubernetes.")[### Руководства

Узнайте, как настроить Dynatrace Operator под конкретные сценарии использования.](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев")[### Получите actionable answers

Начните анализировать ваши кластеры Kubernetes и контейнерные приложения с Dynatrace и пользуйтесь actionable answers.](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")

## Связанные темы

* [Мониторинг кластеров и нагрузок Kubernetesï»¿](https://www.dynatrace.com/technologies/kubernetes-monitoring/)
