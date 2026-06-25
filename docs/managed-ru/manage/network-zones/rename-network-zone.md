---
title: Переименование сетевой зоны
source: https://docs.dynatrace.com/managed/manage/network-zones/rename-network-zone
scraped: 2026-05-12T11:10:42.650724
---

# Переименование сетевой зоны

# Переименование сетевой зоны

* Практическое руководство
* Чтение 1 мин
* Опубликовано 08 апр 2020 г.

Для переименования сетевой зоны создайте новую сетевую зону с новым именем и переместите в неё все ActiveGate и OneAgent.

Перемещение ActiveGate из существующей сетевой зоны означает снижение ёмкости этой зоны. Для поддержания полной ёмкости в любое время и обеспечения плавного перехода рекомендуется установить новые ActiveGate для новой сетевой зоны, чтобы OneAgent начали использовать новые ActiveGate по мере перемещения в новую зону.

1. Создайте новое [имя](/managed/manage/network-zones/network-zones-basic-info#naming "Узнайте, как начать работу с сетевыми зонами.") для сетевой зоны.
2. Установите ActiveGate для новой сетевой зоны.
   Обязательно укажите параметр установки сетевой зоны. Подробнее в разделе [Настройка установки ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").
3. Измените сетевую зону для каждого OneAgent в старой зоне [через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки."). Инструкции для облачных развёртываний смотрите в раскрывающемся разделе.

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

1. Перезапустите OneAgent в следующем порядке:

   1. Кодовые модули для ОС
   2. Технологические кодовые модули
   3. Развёртывания только для приложений
   4. Кодовый модуль zRemote
2. [Удалите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Узнайте, как удалить ActiveGate из систем на Windows или Linux.") из старой сетевой зоны.
3. Удалите старую сетевую зону. Используйте вызов API [DELETE a network zone](/managed/dynatrace-api/environment-api/network-zones/del-network-zone "Удаление сетевой зоны через Dynatrace API.").

## Связанные разделы

* [API сетевых зон](/managed/dynatrace-api/environment-api/network-zones "Управление сетевыми зонами через Dynatrace API.")