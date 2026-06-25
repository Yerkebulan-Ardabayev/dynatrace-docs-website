---
title: Настройка Dynatrace на контейнерных и PaaS-платформах
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms
scraped: 2026-05-12T11:38:06.711760
---

# Настройка Dynatrace на контейнерных и PaaS-платформах

# Настройка Dynatrace на контейнерных и PaaS-платформах

* 3-min read
* Updated on Mar 02, 2023

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")

### Cloud Foundry

Настройка и конфигурация Dynatrace на Cloud Foundry.](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка и конфигурация Dynatrace на Cloud Foundry.")[![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")

### Docker

Настройка и конфигурация Dynatrace на Docker.](/managed/ingest-from/setup-on-container-platforms/docker "Развёртывание OneAgent на Docker.")[![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")

### Heroku

Развёртывание OneAgent для мониторинга приложений, работающих на Heroku.](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.")[![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")

### Mesos

Настройка и конфигурация Dynatrace на Mesos/Marathon.](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon "Узнайте, как развернуть OneAgent на Mesos/Marathon.")

Выбор метода мониторинга контейнеров с помощью Dynatrace зависит от следующих факторов:

* Тип контейнерной среды выполнения, например Docker, containerd или CRI-O
* Платформа оркестрации, например Kubernetes, OpenShift, Cloud Foundry или Fargate
* Уровень доступа к базовому хосту

Подробности смотрите ниже.

## Внедрение полного стека

Наиболее полный вариант мониторинга контейнеров с помощью Dynatrace — развёртывание OneAgent на вашей контейнерной платформе, что обеспечивает полную видимость стека всего контейнеризованного окружения.

Предполагается полный доступ к базовому хосту.

Для большинства развёртываний OneAgent и контейнерных сред выполнения внедрение выполняется процессом `oneagenthelper`, который работает как часть сервиса OneAgent на хосте или внутри контейнера OneAgent. Однако некоторые среды выполнения запускают процесс OneAgentHelper напрямую или требуют помощи от логики автоматического внедрения процессов OneAgent.

Если процессы `oneagenthelper` продолжают работать на ваших хостах после остановки сервиса OneAgent, возможно, потребуется отключить автоматическое внедрение, как описано в документации: [Режимы мониторинга Infrastructure и Discovery](/managed/platform/oneagent/monitoring-modes/monitoring-modes#disable-auto-injection "Подробнее о доступных режимах мониторинга при использовании OneAgent."), либо убедитесь, что используется OneAgent версии 1.281+ в развёртывании Classic Full Stack.

### Cloud Foundry

Dynatrace поддерживает полный мониторинг стека для Cloud Foundry через Dynatrace OneAgent BOSH Release.

Смотрите [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка и конфигурация Dynatrace на Cloud Foundry.").

### Docker вне контейнерной платформы

Можно развернуть OneAgent непосредственно на хосте Docker или запустить OneAgent как контейнер Docker.

* [Развёртывание OneAgent на хосте Docker](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнайте, как установить OneAgent на Linux, настроить установку и многое другое.")
* [Развёртывание OneAgent как контейнера Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установка и обновление Dynatrace OneAgent как контейнера Docker.")

### Heroku

Dynatrace поддерживает полный мониторинг стека для Heroku через buildpack Dynatrace Heroku.

Смотрите [Настройка Dynatrace на Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Установка OneAgent для мониторинга приложений, работающих на Heroku.").

## Внедрение только на уровне приложения

Используйте внедрение только на уровне приложения, если у вас нет доступа к базовым хостам. Доступные варианты зависят от используемой контейнерной платформы.

### Автоматизированное внедрение

Наиболее эффективный вариант — автоматизированное внедрение только на уровне приложения для платформ на основе Kubernetes. Оно внедряет кодовые модули OneAgent с использованием Kubernetes-нативных контроллеров допуска.

* Для Kubernetes смотрите [Начало работы с наблюдаемостью приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#automatic "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes").
* Для AWS Fargate смотрите [Мониторинг AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#autoinjection "Установка OneAgent на AWS Fargate.")

### Внедрение в среде выполнения

Внедрение кодовых модулей OneAgent в контейнер при его развёртывании.

* Для Kubernetes/OpenShift смотрите [Начало работы с наблюдаемостью приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#runtime "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")
* Для Cloud Foundry смотрите [Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")
* Для AWS Fargate смотрите [Мониторинг AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#runtime "Установка OneAgent на AWS Fargate.")

### Внедрение во время сборки

Внедрение кодовых модулей OneAgent в контейнер во время его сборки.

* Для Docker вне контейнерных платформ смотрите [Настройка OneAgent на контейнерах для мониторинга только приложений](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.")
* Для Kubernetes/OpenShift смотрите [Внедрение во время сборки контейнера Kubernetes только на уровне приложения](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#build-time "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")
* Для AWS Fargate смотрите [Мониторинг AWS Fargate](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#buildtime "Установка OneAgent на AWS Fargate.")

## Связанные темы

* [Мониторинг контейнерных платформ](/managed/observe/infrastructure-observability/container-platform-monitoring "Контейнерные платформы, которые может мониторить Dynatrace")