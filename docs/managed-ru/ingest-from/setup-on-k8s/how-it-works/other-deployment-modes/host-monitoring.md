---
title: Host monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/host-monitoring
scraped: 2026-05-12T11:54:00.387980
---

# Host monitoring

# Host monitoring

* Чтение: 1 мин
* Опубликовано 31 октября 2024 г.

Host monitoring собирает метрики хостов и данные процессов с узлов Kubernetes. Он развёртывает OneAgent для сбора таких метрик, как использование CPU, памяти, диска и сети. Этот режим не включает мониторинг на уровне приложений.

Дополнительную информацию см. в разделе [`.spec.oneAgent.hostMonitoring`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") DynaKube.

## Возможности

Собирает метрики хостов и данные процессов.

## Ограничения

Диагностические файлы (архивы поддержки) для Pod приложений пока не поддерживаются для файловых систем только для чтения.

## Развёрнутые ресурсы

### Компоненты Dynatrace Operator

Следующие компоненты развёртываются через Helm/Manifests в рамках базовой установки. Подробнее см. в соответствующих разделах:

* [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Компоненты Dynatrace Operator") управляет автоматическим развёртыванием, настройкой и жизненным циклом компонентов Dynatrace в вашем окружении Kubernetes.
* [Dynatrace Operator webhook](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Компоненты Dynatrace Operator") проверяет определения DynaKube, конвертирует определения с устаревшими версиями API и внедряет конфигурации в Pod.
* [Dynatrace Operator CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Компоненты Dynatrace Operator") развёртывается как DaemonSet, предоставляет хранилище томов с возможностью записи для двоичных файлов OneAgent, чтобы минимизировать использование сети и хранилища.

### Компоненты под управлением оператора

Следующие компоненты развёртываются путём применения DynaKube с full-stack observability:

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Изучите ключевые концепции OneAgent и узнайте, как устанавливать и эксплуатировать OneAgent на различных платформах.") собирает метрики хостов с узлов Kubernetes.
* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.") маршрутизирует данные observability в кластер Dynatrace.

![host-monitoring](https://dt-cdn.net/images/image-20240612-113305-1637-c57403b85c.png)

host-monitoring