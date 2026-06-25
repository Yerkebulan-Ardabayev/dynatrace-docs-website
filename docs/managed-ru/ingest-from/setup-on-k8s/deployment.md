---
title: Развёртывание
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment
scraped: 2026-05-12T11:11:02.252135
---

# Развёртывание

# Развёртывание

* Чтение: 6 мин
* Обновлено 28 января 2026 г.

Dynatrace предлагает гибкий подход к observability в Kubernetes: вы можете выбирать тот уровень observability, который нужен для ваших кластеров Kubernetes. На этой странице приведён обзор и пошаговое руководство по рекомендуемым опциям, покрывающим ваши потребности в observability для Kubernetes.
Все варианты развёртывания на этой странице используют [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). Отдельную документацию и опции для основных дистрибутивов Kubernetes см. в разделе [Дистрибутивы](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Обзор различных конфигураций для всех основных дистрибутивов Kubernetes.").

## Варианты observability

### Full Kubernetes observability

Получите мгновенные инсайты по здоровью Kubernetes и готовое распределённое трассирование и аналитику для ваших нагрузок.

#### Варианты развёртывания

* Рекомендуется: [разверните Dynatrace Operator в режиме cloud-native full-stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Разверните Dynatrace Operator в режиме cloud-native full-stack в Kubernetes")
* [Разверните Dynatrace Operator в режиме classic full-stack](/managed/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Разверните Dynatrace Operator в режиме classic full-stack в Kubernetes")  
  Ограничения: существует зависимость запуска между контейнером, в котором развёрнут OneAgent, и контейнерами приложений, которые нужно инструментировать (например, контейнерами с включённым deep process monitoring). Контейнер OneAgent должен быть запущен, а процесс oneagenthelper должен работать до старта контейнера приложения, чтобы приложение было корректно инструментировано.

Другая опция

* Deprecated: [Ручной rollout OneAgent через DaemonSet](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Разверните, обновите и удалите OneAgent DaemonSet в Kubernetes.") (не основан на Dynatrace Operator)

### Kubernetes observability

Понимайте и устраняйте проблемы со здоровьем ваших кластеров Kubernetes.

#### Развёртывание

[Разверните Dynatrace Operator для Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed "Разверните Dynatrace Operator для Kubernetes observability.")

### Application observability

Повышайте надёжность и производительность нагрузок за счёт автоматического распределённого трассирования и видимости на уровне кода.

#### Развёртывание

[Разверните Dynatrace Operator в режиме application monitoring](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Разверните Dynatrace Operator в режиме application monitoring в Kubernetes")

Другие опции

Следующие опции мониторинга приложений не основаны на Dynatrace Operator:

* [Pod-runtime injection](/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime "Внедряйте code modules Dynatrace в контейнер во время его развёртывания.")
* [Build-time injection](/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime "Внедряйте code modules Dynatrace в контейнер во время сборки для каждого нового развёртывания Pod.")

Для архитектуры S390x поддерживаются инъекции [pod runtime](/managed/ingest-from/setup-on-k8s/deployment/other/pod-runtime "Внедряйте code modules Dynatrace в контейнер во время его развёртывания.") и [container build-time](/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime "Внедряйте code modules Dynatrace в контейнер во время сборки для каждого нового развёртывания Pod.").

## Развёртывание из Marketplaces

Dynatrace поддерживает развёртывание Dynatrace Operator из следующих маркетплейсов:

* [OpenShift OperatorHub](/managed/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub "Разверните Dynatrace Operator в OpenShift через OperatorHub.")
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Узнать больше

[### Как это работает

Ознакомьтесь с компонентами Dynatrace, которые разворачиваются в вашем кластере Kubernetes.](/managed/ingest-from/setup-on-k8s/how-it-works "Подробное описание того, как работает развёртывание в Kubernetes.")[### Руководства

Узнайте, как настроить Dynatrace Operator под конкретные сценарии использования.](/managed/ingest-from/setup-on-k8s/guides "Подробное описание вариантов установки и настройки для конкретных сценариев")[### Справочник

Справочник API и варианты конфигурации для всех компонентов Dynatrace в вашем кластере Kubernetes.](/managed/ingest-from/setup-on-k8s/reference "Содержит справочную страницу с вариантами конфигурации для каждого компонента Dynatrace")[### Release notes Dynatrace Operator

См. release notes для Dynatrace Operator.](/managed/whats-new/dynatrace-operator "Release notes для Dynatrace Operator")
