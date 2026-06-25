---
title: Full-stack observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack
scraped: 2026-05-12T11:23:40.767870
---

# Full-stack observability

# Full-stack observability

* Чтение: 3 мин
* Опубликовано 31 октября 2024 г.

Full-stack observability объединяет мониторинг инфраструктуры и приложений в окружениях Kubernetes. Эта конфигурация включает инъекцию Dynatrace OneAgent и предоставляет инсайты как по производительности кластера, так и по поведению приложений.

Дополнительную информацию см. в разделе [`.spec.oneAgent.cloudNativeFullStack`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") DynaKube.

## Возможности

* Предлагает функциональность, аналогичную инъекции classic full-stack.
* Использует мутирующие вебхуки для внедрения code modules в Pod приложений.
* Включает обогащение данных для окружений Kubernetes с помощью [файлов обогащения](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

### Текущие ограничения

* Диагностические файлы (архивы поддержки) для Pod приложений пока не поддерживаются.
* Правила мониторинга контейнеров не поддерживаются (параметр label selector в DynaKube предоставляет аналогичную функциональность).
* [Статический мониторинг Go](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Узнайте об ограничениях поддержки Go и способах их обхода.") поддерживается частично.
* Архивы поддержки OneAgent, например логи code modules, можно собрать с мониторируемого процесса/Pod с помощью пункта меню **Run OneAgent Diagnostics** на странице конкретного процесса. Если архив поддержки OneAgent недоступен, это означает одно из следующего:

  + В Pod приложения не был внедрён ни один code module.
  + Возникла проблема при создании архива поддержки OneAgent.

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/Manifests в рамках базовой установки. Подробнее см. в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Компоненты Dynatrace Operator") управляет автоматическим развёртыванием, настройкой и жизненным циклом компонентов Dynatrace в вашем окружении Kubernetes.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Компоненты Dynatrace Operator") проверяет определения DynaKube, конвертирует определения с устаревшими версиями API и внедряет конфигурации в Pod.
* [Dynatrace Operator CSI Driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Компоненты Dynatrace Operator") развёртывается как DaemonSet, предоставляет хранилище томов с возможностью записи для двоичных файлов OneAgent, чтобы минимизировать использование сети и хранилища.

### Компоненты под управлением оператора

Следующие компоненты развёртываются путём применения DynaKube с full-stack observability:

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции OneAgent и узнайте, как устанавливать и эксплуатировать OneAgent на различных платформах.") собирает метрики хостов с узлов Kubernetes.
* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.") маршрутизирует данные observability в кластер Dynatrace и отслеживает Kubernetes API.
* В ваше приложение внедряются code modules Dynatrace для обеспечения deep monitoring и observability.

![cloud-native](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-40-02-pm-2352-4cba84df51.png)

cloud-native