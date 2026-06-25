---
title: Настройка Dynatrace на Docker
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/docker
scraped: 2026-05-12T11:03:44.532639
---

# Настройка Dynatrace на Docker

# Настройка Dynatrace на Docker

* 1-min read
* Published Jun 25, 2021

Dynatrace предлагает полнофункциональный мониторинг Docker, а также универсальный мониторинг контейнеров для containerd и CRI-O, предоставляя те же широкие возможности мониторинга контейнеризованных приложений, что и для обычных приложений.

## Интеграции

При использовании Docker вне контейнерных платформ существует два способа мониторинга приложений через OneAgent:

* [Настройка OneAgent для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.")
* [Настройка Dynatrace как Docker-контейнера](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent как Docker-контейнера.")

В типичном сценарии инструменты оркестрации контейнеров, такие как Kubernetes, OpenShift и Cloud Foundry, используют Docker, containerd или CRI-O в качестве среды выполнения контейнеров. При использовании одной из этих платформ следуйте соответствующим инструкциям по развёртыванию: [Kubernetes](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes"), [OpenShift](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes"), [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с помощью BOSH.") или [Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate."). Любая платформа, использующая контейнеры, также может отслеживаться с помощью [подхода мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.").

## Связанные темы

* [Мониторинг групп контейнеров](/managed/observe/infrastructure-observability/container-platform-monitoring/container-groups "Обзор мониторинга групп контейнеров")