---
title: Развёртывание сетевых зон (миграция)
source: https://docs.dynatrace.com/managed/manage/network-zones/migration/deploy
scraped: 2026-05-12T11:52:30.729913
---

# Развёртывание сетевых зон (миграция)

# Развёртывание сетевых зон (миграция)

* Чтение 1 мин
* Опубликовано 28 янв 2020 г.

Когда [план](/managed/manage/network-zones/migration/plan "Узнайте, как планировать сетевые зоны, отражающие топологию вашей сети.") сетевых зон готов, пришло время их реализовать.

## Предварительные условия

Для выполнения следующей процедуры вам потребуются:

* Запланированные сетевые зоны с определёнными именами.
* Достаточное количество ActiveGate в каждой сетевой зоне для обработки запланированной нагрузки.

## Процедура

1. Активируйте функцию сетевых зон в вашем окружении. Подробнее в разделе [Активация сетевых зон](/managed/manage/network-zones/network-zones-basic-info#activate "Узнайте, как начать работу с сетевыми зонами.").
2. Добавьте сетевую зону в конфигурацию каждого ActiveGate.

   1. Укажите сетевую зону ActiveGate в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.").
   2. [Перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").
3. Добавьте сетевую зону в конфигурацию каждого OneAgent. Работайте зона за зоной, редактируя конфигурацию каждого OneAgent в одной сетевой зоне, прежде чем переходить к следующей. Это обеспечит переход без аварийных переключений.

   1. Укажите сетевую зону [через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки."). Инструкции для облачных развёртываний смотрите в раскрывающемся разделе.

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

   2. Перезапустите OneAgent в следующем порядке:

      1. Перезапустите службы OneAgent, выполняющих full-stack-мониторинг.
      2. Перезапустите приложения, мониторируемые OneAgent, чтобы они получили новую инструментацию.
      3. Перезапустите развёртывания OneAgent только для приложений.
      4. Перезапустите zRemote на ActiveGate.