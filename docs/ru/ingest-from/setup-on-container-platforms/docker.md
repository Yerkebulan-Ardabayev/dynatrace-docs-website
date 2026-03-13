---
title: Set up Dynatrace on Docker
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/docker
scraped: 2026-03-06T21:15:44.080621
---

# Настройка Dynatrace в Docker

# Настройка Dynatrace в Docker

* Latest Dynatrace
* 1-min read
* Published Jun 25, 2021

Dynatrace предлагает полнофункциональный мониторинг Docker, а также универсальный мониторинг контейнеров для containerd и CRI-O, предоставляя все те же возможности глубокого мониторинга контейнеризованных приложений, что и для неконтейнеризованных приложений.

## Интеграции

Если вы хотите использовать Docker вне контейнерной платформы, существуют два метода мониторинга приложений с помощью OneAgent:

* [Настройка OneAgent только для приложений](docker/set-up-oneagent-on-containers-for-application-only-monitoring.md "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.")
* [Настройка Dynatrace в качестве контейнера Docker](docker/set-up-dynatrace-oneagent-as-docker-container.md "Установка и обновление Dynatrace OneAgent в качестве контейнера Docker.")

В типичном сценарии инструменты оркестрации и управления контейнерами, такие как Kubernetes, OpenShift и Cloud Foundry, используют Docker, containerd или CRI-O в качестве среды выполнения контейнеров. Если вы работаете на одной из этих платформ, следуйте соответствующим инструкциям по развёртыванию: [Kubernetes](../setup-on-k8s/deployment.md "Развернуть Dynatrace Operator на Kubernetes"), [OpenShift](../setup-on-k8s/deployment.md "Развернуть Dynatrace Operator на Kubernetes"), [Cloud Foundry](cloud-foundry/deploy-oneagent-on-cloud-foundry.md "Установка OneAgent на Cloud Foundry с помощью BOSH.") или [Fargate](../amazon-web-services/integrate-into-aws/aws-fargate.md "Установка OneAgent на AWS Fargate."). Любую платформу, использующую контейнеры, также можно отслеживать с помощью [подхода только для приложений](docker/set-up-oneagent-on-containers-for-application-only-monitoring.md "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.").

## Связанные темы

* [Мониторинг групп контейнеров](../../observe/infrastructure-observability/container-platform-monitoring/container-groups.md "Обзор мониторинга групп контейнеров")
