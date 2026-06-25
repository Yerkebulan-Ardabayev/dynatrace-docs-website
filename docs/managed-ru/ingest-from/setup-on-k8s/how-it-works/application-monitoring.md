---
title: Application observability
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/application-monitoring
scraped: 2026-05-12T11:23:30.246439
---

# Application observability

# Application observability

* Чтение: 3 мин
* Обновлено 4 мая 2026 г.

Application observability фокусируется на мониторинге метрик уровня приложений путём внедрения code modules в Pod приложений. Этот режим предлагает несколько стратегий инъекции (автоматическую, во время выполнения и во время сборки) для сбора метрик, специфичных для приложений. Для получения инсайтов на уровне инфраструктуры сочетайте его с [мониторингом платформы Kubernetes](/managed/ingest-from/setup-on-k8s/how-it-works/kubernetes-monitoring "Подробное описание мониторинга платформы Kubernetes с помощью Dynatrace Operator.").

Дополнительную информацию см. в разделе [`.spec.oneAgent.applicationMonitoring`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") DynaKube.

## Автоматическая инъекция

Стратегию автоматической инъекции можно использовать для Pod приложений. Dynatrace внедряет code modules в Pod с помощью admission controller Kubernetes. Этот подход позволяет собирать метрики, специфичные для приложений, и отслеживать метрики уровня контейнеров.

### Возможности

* Dynatrace внедряет code modules в Pod с помощью admission controller Kubernetes.
* Получите детальный контроль над инструментированными Pod с помощью namespace и аннотаций.
* Направляйте метрики Pod в разные окружения Dynatrace в пределах одного кластера Kubernetes.
* [Включите обогащение данных для окружений Kubernetes](/managed/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

### Текущие ограничения

* Диагностические файлы (архивы поддержки) для Pod приложений пока не поддерживаются.
* [Статический мониторинг Go](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Узнайте об ограничениях поддержки Go и способах их обхода.") поддерживается частично.

При развёртывании в режиме application monitoring code modules Dynatrace отслеживают процессы внутри контейнера, включая метрики диска, CPU и сети. Метрики хостов не отслеживаются. Без [мониторинга платформы Kubernetes](#kubernetes-monitoring) топология ограничена Pod и контейнерами.

### Развёрнутые ресурсы

Следующие компоненты развёртываются через Helm/Manifests в рамках базовой установки. Подробнее см. в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Компоненты Dynatrace Operator") управляет автоматическим развёртыванием, настройкой и жизненным циклом компонентов Dynatrace в вашем окружении Kubernetes.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Компоненты Dynatrace Operator") проверяет определения DynaKube, конвертирует определения с устаревшими версиями API и внедряет конфигурации в Pod.
* [Dynatrace Operator CSI Driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Компоненты Dynatrace Operator") Необязательно, развёртывается как DaemonSet, предоставляет хранилище томов с возможностью записи для двоичных файлов OneAgent, чтобы минимизировать использование сети и хранилища.

Следующий компонент развёртывается путём применения DynaKube с Application observability:

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.") маршрутизирует данные observability в кластер Dynatrace.
* В ваше приложение внедряются code modules Dynatrace для обеспечения deep monitoring и observability.

![auto-injection](https://dt-cdn.net/images/screenshot-2024-01-31-at-3-23-56-pm-2358-6db693bc75.png)

auto-injection

## Инъекция во время выполнения Pod

Application monitoring можно использовать для Pod приложений. Pod OneAgent не устанавливаются, а собирать метрики хостов с узлов Kubernetes невозможно.

### Возможности

* В Pod внедряются code modules Dynatrace с помощью init-контейнеров Kubernetes.
* Разные образы контейнеров могут иметь отдельные конфигурации для разных окружений Dynatrace.

### Ограничения

Поскольку Dynatrace Operator не задействован, автоматическая инъекция, настройка и обогащение не выполняются. Необходимо вручную корректировать ваши рабочие нагрузки Kubernetes.

![PodRuntime Illustration](https://cdn.bfldr.com/B686QPH3/as/2jr3k4q567mf434ncb5sspbs/Application_observability_-_PodRuntime_injection_-_Light_Mode?auto=webp&format=png&position=1)

diagram title

## Инъекция во время сборки контейнера

Application monitoring можно использовать для Pod приложений. Pod OneAgent не устанавливаются, а собирать метрики хостов с узлов Kubernetes невозможно.

### Возможности

* В образы контейнеров в процессе сборки встраиваются code modules Dynatrace.
* Разные образы контейнеров можно настроить для разных окружений Dynatrace и использовать на любой контейнерной платформе или PaaS в дополнение к Kubernetes.

### Ограничения

Без Dynatrace Operator автоматическая инъекция, настройка и обогащение не выполняются. Необходимо вручную адаптировать ваш процесс сборки.

![Container build-time injection](https://cdn.bfldr.com/B686QPH3/as/t877m9mwwnfmv55xgsfgscc/Application_observability_-_Container_build-time_injection_-_Light_Mode?auto=webp&format=png&position=1)

Container build-time injection