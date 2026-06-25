---
title: Мониторинг платформы Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/kubernetes-monitoring
scraped: 2026-05-12T11:54:01.558186
---

# Мониторинг платформы Kubernetes

# Мониторинг платформы Kubernetes

* Чтение: 1 мин
* Опубликовано 31 октября 2024 г.

Мониторинг платформы Kubernetes закладывает основу для понимания и устранения неполадок в ваших кластерах Kubernetes. По умолчанию эта конфигурация не включает OneAgent или мониторинг на уровне приложений, но её можно сочетать с другими подходами к мониторингу и инъекции.

Дополнительную информацию см. в разделе [`.spec.activeGate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-ag "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") DynaKube.

## Возможности

* Предоставляет инсайты по здоровью и использованию ваших кластеров Kubernetes, включая связи объектов (топологию)
* Использует Kubernetes API и cAdvisor для получения метрик уровня узлов и контейнеров, а также событий Kubernetes
* Обеспечивает оповещения и обнаружение аномалий «из коробки» для рабочих нагрузок, Pod, узлов и кластеров

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/Manifests в рамках базовой установки. Подробнее см. в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Компоненты Dynatrace Operator") управляет автоматическим развёртыванием, настройкой и жизненным циклом компонентов Dynatrace в вашем окружении Kubernetes.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Компоненты Dynatrace Operator") проверяет определения DynaKube, конвертирует определения с устаревшими версиями API и внедряет конфигурации в Pod.

### Компоненты под управлением оператора

Следующий компонент развёртывается путём применения DynaKube с мониторингом платформы Kubernetes:

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.") маршрутизирует данные observability в кластер Dynatrace и отслеживает Kubernetes API.

![k8s-monitoring](https://dt-cdn.net/images/screenshot-2024-01-31-at-3-22-25-pm-2348-59be4489a6.png)

k8s-monitoring