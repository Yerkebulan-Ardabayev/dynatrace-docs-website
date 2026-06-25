---
title: Удаление сетевой зоны
source: https://docs.dynatrace.com/managed/manage/network-zones/delete-network-zones
scraped: 2026-05-12T11:10:45.135688
---

# Удаление сетевой зоны

# Удаление сетевой зоны

* Практическое руководство
* Чтение 1 мин
* Опубликовано 14 апр 2020 г.

Перед удалением сетевой зоны убедитесь, что ни один OneAgent или ActiveGate не использует эту зону. Удалить можно только пустую сетевую зону. Если сетевая зона используется как альтернативная зона для какого-либо OneAgent, она будет автоматически удалена из списка возможных альтернатив.

Выполните следующие шаги:

1. Определите OneAgent в зоне, которую нужно удалить.
2. Определите другую зону, в которую нужно переместить этих OneAgent.
3. Проверьте, достаточно ли у ActiveGate в целевой зоне ресурсов для добавления этих OneAgent. При необходимости установите дополнительные ActiveGate.
4. Измените сетевую зону для каждого OneAgent в удаляемой зоне [через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки."). Инструкции для облачных развёртываний смотрите в раскрывающемся разделе.

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

5. [Удалите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Узнайте, как удалить ActiveGate из систем на Windows или Linux."), ответственные за маршрутизацию сообщений в удаляемой сетевой зоне.
   Либо вы можете переназначить эти ActiveGate в другие сетевые зоны. Измените сетевую зону в [конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.") и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").
6. Удалите сетевую зону. Используйте вызов API [DELETE a network zone](/managed/dynatrace-api/environment-api/network-zones/del-network-zone "Удаление сетевой зоны через Dynatrace API.").

## Связанные разделы

* [API сетевых зон](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API.")