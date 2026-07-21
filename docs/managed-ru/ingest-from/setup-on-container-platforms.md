---
title: Настройка Dynatrace на контейнерных и PaaS-платформах
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms
---

# Настройка Dynatrace на контейнерных и PaaS-платформах

# Настройка Dynatrace на контейнерных и PaaS-платформах

* Чтение 3 мин
* Обновлено 02 марта 2023 г.

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")

### Cloud Foundry

Настройка и конфигурирование Dynatrace на Cloud Foundry.](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")[![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")

### Docker

Настройка и конфигурирование Dynatrace на Docker.](/managed/ingest-from/setup-on-container-platforms/docker "Deploy OneAgent on Docker.")[![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")

### Heroku

Развёртывание OneAgent для мониторинга приложений, работающих на Heroku.](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")[![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")

### Mesos

Настройка и конфигурирование Dynatrace на Mesos/Marathon.](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon "Learn how to deploy OneAgent on Mesos/Marathon.")

Способ мониторинга контейнеров с помощью Dynatrace зависит от следующего:

* Тип контейнерной среды выполнения, например Docker, containerd или CRI-O
* Платформа оркестрации, например Kubernetes, OpenShift, Cloud Foundry или Fargate
* Уровень доступа к базовому хосту

Подробности ниже.

## Full-stack-инъекция

Наиболее полный вариант мониторинга контейнеров с помощью Dynatrace, это развернуть OneAgent на контейнерной платформе, что даёт полную видимость всей контейнеризированной среды на уровне full-stack.

Предполагается полный доступ к базовому хосту.

Для большинства развёртываний OneAgent и контейнерных сред выполнения инъекция выполняется процессом `oneagenthelper`, который работает в составе службы OneAgent на хосте или внутри контейнера OA. Однако некоторые среды выполнения запускают процесс OneAgentHelper напрямую или требуют содействия логики автоматической инъекции процессов OneAgent.

Если процессы `oneagenthelper` продолжают оставаться активными на хостах даже после остановки службы OneAgent, может понадобиться отключить автоматическую инъекцию, как описано в нашей документации здесь, перед остановкой службы/контейнера oneagent: [Режимы мониторинга Infrastructure and Discovery](/managed/platform/oneagent/monitoring-modes/monitoring-modes#disable-auto-injection "Find out more about the available monitoring modes when using OneAgent.") или убедиться, что в развёртывании Classic Full Stack используется OneAgent версии 1.281+.

### Cloud Foundry

Dynatrace поддерживает full-stack-мониторинг для Cloud Foundry через Dynatrace OneAgent BOSH Release.

См. [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.").

### Docker вне контейнерной платформы

OneAgent можно развернуть напрямую на хосте Docker или запустить OneAgent как контейнер Docker.

* [Развёртывание OneAgent на хосте Docker](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.")
* [Развёртывание OneAgent как контейнера Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

### Heroku

Dynatrace поддерживает full-stack-мониторинг для Heroku через Heroku buildpack Dynatrace.

См. [Настройка Dynatrace на Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## Инъекция только приложения

Используйте инъекцию только приложения, если нет доступа к базовым хостам. Доступные варианты зависят от используемой контейнерной платформы.

### Автоматизированная инъекция

Наиболее эффективный вариант, это автоматизированная инъекция только приложения для платформ на базе Kubernetes. Она внедряет модули кода OneAgent с помощью нативных для Kubernetes admission-контроллеров.

* Для Kubernetes см. [Начало работы с Application observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#automatic "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* Для AWS Fargate на EKS см. [Установка дополнения Dynatrace Operator для AWS Elastic Kubernetes Service (AWS EKS)](/managed/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto#fargate "Deploy and configure Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS) environment.")

### Инъекция во время выполнения

Внедрение модулей кода OneAgent в контейнер при его развёртывании.

* Для Kubernetes/OpenShift см. [Начало работы с Application observability](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#runtime "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")
* Для Cloud Foundry см. [Развёртывание OneAgent на Cloud Foundry для мониторинга только приложения](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* Для AWS Fargate см. [Мониторинг AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#runtime "Install OneAgent on AWS Fargate.")

### Инъекция во время сборки

Внедрение модулей кода OneAgent в контейнер при его сборке.

* Для Docker вне контейнерных платформ см. [Настройка OneAgent на контейнерах для мониторинга только приложения](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")
* Для Kubernetes/OpenShift см. [Инъекция только приложения при сборке контейнера Kubernetes](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#build-time "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")

## Похожие темы

* [Мониторинг контейнерных платформ](/managed/observe/infrastructure-observability/container-platform-monitoring "The container platforms Dynatrace can monitor")