---
title: Развёртывание сетевых зон (новая установка)
source: https://docs.dynatrace.com/managed/manage/network-zones/new-installation/deploy
scraped: 2026-05-12T11:52:32.772070
---

# Развёртывание сетевых зон (новая установка)

# Развёртывание сетевых зон (новая установка)

* Чтение 1 мин
* Опубликовано 28 янв 2020 г.

Когда [план](/managed/manage/network-zones/new-installation/plan "Планирование сетевых зон, отражающих топологию вашей сети.") сетевых зон готов, пришло время их реализовать.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Установка ActiveGate**](/managed/manage/network-zones/new-installation/deploy#install-activegates "Узнайте, как развернуть сетевые зоны для существующего окружения Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Установка OneAgent**](/managed/manage/network-zones/new-installation/deploy#install-oneagents "Узнайте, как развернуть сетевые зоны для существующего окружения Dynatrace.")

## Предварительные условия

Для выполнения следующей процедуры вам потребуются:

* Запланированные сетевые зоны с определёнными именами.
* Активированная функция сетевых зон. Подробнее о том, как её активировать, в разделе [Активация сетевых зон](/managed/manage/network-zones/network-zones-basic-info#activate "Узнайте, как начать работу с сетевыми зонами.").

## Шаг 1 Установка ActiveGate

1. Зона за зоной устанавливайте ActiveGate, ответственные за маршрутизацию сообщений.
2. При установке используйте параметр `--set-network-zone=<name>` для указания сетевой зоны. Подробнее о настройке установки ActiveGate в разделе [Информация об установке ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").
3. В демилитаризованной зоне установите ActiveGate для RUM с параметром [`MSGrouter`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#collector "Узнайте, какие свойства ActiveGate можно настроить."), установленным в `false`.

   Сетевую зону также можно указать после установки ActiveGate:
4. Укажите сетевую зону в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.").
5. [Перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").

## Шаг 2 Установка OneAgent

Зона за зоной устанавливайте OneAgent. Обязательно укажите параметр установки сетевой зоны. Подробнее в разделе [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки.").

Инструкции для облачных развёртываний смотрите в раскрывающемся разделе.

Развёртывание сетевых зон в облаке

#### Kubernetes

[Развёртывание OneAgent на Kubernetes](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Установка и удаление OneAgent на Kubernetes с помощью kubectl или Helm.")

[Развёртывание OneAgent на Kubernetes через DaemonSet](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Развёртывание, обновление и удаление OneAgent DaemonSet на Kubernetes.")

[Развёртывание OneAgent на Kubernetes только для приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")

#### OpenShift

[Развёртывание OneAgent на OpenShift](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy "Установка OneAgent на OpenShift с помощью kubectl или Helm.")

[Развёртывание OneAgent на OpenShift через DaemonSet](/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset "Развёртывание, обновление и удаление OneAgent DaemonSet на Kubernetes.")

[Развёртывание OneAgent на OpenShift только для приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")

#### Amazon Web Services

[Развёртывание OneAgent на AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Установка OneAgent на AWS Fargate.")

[Развёртывание OneAgent на Elastic Container Service](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Мониторинг кластеров ECS как службы daemon с типом запуска EC2.")

[Развёртывание OneAgent на AWS Elastic Beanstalk](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk "Установка OneAgent на AWS Elastic Beanstalk.")

[Развёртывание OneAgent на Elastic Kubernetes Service](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Установка и удаление OneAgent на Kubernetes с помощью kubectl или Helm.")

#### Azure

[Развёртывание OneAgent на виртуальных машинах Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm "Узнайте, как установить и настроить OneAgent для мониторинга виртуальных машин Azure с помощью расширения VM.")

[Развёртывание OneAgent на Azure Kubernetes Service](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Установка и удаление OneAgent на Kubernetes с помощью kubectl или Helm.")

#### Cloud Foundry

[Развёртывание OneAgent на BOSH](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Установка OneAgent на Cloud Foundry с BOSH.")

[Развёртывание OneAgent на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")

#### Google Cloud

[Развёртывание OneAgent на Google Kubernetes Engine](/managed/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy "Установка и удаление OneAgent на Kubernetes с помощью kubectl или Helm.")

#### Heroku

[Развёртывание OneAgent на Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.")

## Настройка мониторинга z/OS

1. Настройте [zLocal](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS.").
2. Настройте [zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.").
3. Добавьте сетевую зону в конфигурацию ActiveGate, на котором работает zRemote.

   1. Укажите сетевую зону ActiveGate в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.").
   2. [Перезапустите](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") ActiveGate.
4. Подключите zLocal к zRemote.