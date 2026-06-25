---
title: Привилегии OneAgent для мониторинга контейнеров
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/oneagent-privileges
scraped: 2026-05-12T11:52:53.896688
---

# Привилегии OneAgent для мониторинга контейнеров

# Привилегии OneAgent для мониторинга контейнеров

* 2-min read
* Published Mar 08, 2023

Dynatrace поддерживает полный стековый мониторинг контейнерных платформ — от приложения до инфраструктуры. Для получения метрик уровня контейнера и глубокого мониторинга хоста, включая внедрение OneAgent в процессы, необходимы повышенные привилегии.

Однако если вы не хотите предоставлять повышенные привилегии OneAgent или не имеете доступа к инфраструктурному уровню, можно использовать режим мониторинга только приложений.

Для Kubernetes мониторинг только приложений на основе Dynatrace Operator по-прежнему обеспечивает хороший охват данных: сведения об узлах (базовые метрики и оповещения) на основе данных, получаемых ActiveGate из Kubernetes API, а также метрики Prometheus.

## Полный стековый мониторинг (full-stack injection)

Контейнер OneAgent и базовый хост используют общие пространства имён Linux для доступа к данным, необходимым для полного стекового мониторинга:

* Общее сетевое пространство имён обеспечивает процессам внутри контейнера прямой доступ к сетевым интерфейсам хоста.
* Общее пространство имён PID позволяет процессам внутри контейнера видеть все процессы из таблицы процессов хоста.
* Смонтированная корневая файловая система хоста доступна всем модулям OneAgent и обеспечивает доступ к файлам логов, метрикам дисков и другим возможностям полного стекового мониторинга.

В процессе мониторинга область необходимых разрешений для каждого процесса ограничивается с помощью специфических [Linux System Capabilities](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Когда Dynatrace OneAgent требует права суперпользователя на Linux.").

Полный стековый мониторинг можно реализовать через следующие режимы развёртывания:

* Dynatrace Operator на Kubernetes/OpenShift

  + [Cloud-native full-stack режим](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание развёртывания на Kubernetes.")
  + [Classic full-stack режим](/managed/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание развёртывания на Kubernetes.")
* Docker вне контейнерных платформ

  + [OneAgent как Docker-контейнер](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent как Docker-контейнера.")

### OneAgent на Docker-хосте

Также можно развернуть OneAgent непосредственно на Docker-хосте под управлением Linux. В этом сценарии OneAgent работает не в контейнере, а напрямую на хосте, поэтому изоляция пространства имён Linux отсутствует. Подробнее см. в разделе [OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Установка OneAgent на Linux, настройка и дополнительная информация.").

## Мониторинг только приложений (application-only injection)

OneAgent, развёрнутый в режиме мониторинга только приложений, не запускается как привилегированный контейнер.

Подробнее см. в разделах:

* [Начало работы с наблюдаемостью приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")
* [Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")
* [Настройка OneAgent на контейнерах для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.")