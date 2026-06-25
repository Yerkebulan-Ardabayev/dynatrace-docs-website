---
title: Dynatrace OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent
scraped: 2026-05-12T11:04:11.291426
---

# Dynatrace OneAgent

# Dynatrace OneAgent

* 2-min read
* Published Oct 09, 2018

OneAgent отвечает за сбор всех данных мониторинга в вашем мониторируемом окружении. На каждом хосте требуется один экземпляр OneAgent для сбора всех необходимых данных мониторинга — даже если ваши хосты развёрнуты в контейнерах Docker, архитектурах микросервисов или облачной инфраструктуре.

Один экземпляр OneAgent может выполнять [мониторинг всех типов объектов](/managed/platform/oneagent/supported-monitoring-types "Обзор всех возможностей мониторинга, предоставляемых OneAgent."), включая серверы, приложения, сервисы, базы данных и многое другое. OneAgent предоставляет все необходимые операционные и бизнес-метрики производительности — от фронтенда до бэкенда и всего между ними: облачные экземпляры, хосты, состояние сети, процессы и сервисы. OneAgent обнаруживает все запущенные на ваших хостах процессы. На основе найденного OneAgent автоматически активирует инструментирование, специально разработанное для вашего уникального стека приложений. Он также внедряет все теги, необходимые для мониторинга пользовательского опыта, в HTML страниц вашего приложения. Новые компоненты автоматически инструментируются на лету.

OneAgent состоит из нескольких кодовых модулей, которые позволяют ему работать с большинством технологий «из коробки». Сведения о поддерживаемых кодовых модулях для каждой платформы смотрите в [матрице поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживает OneAgent на различных операционных системах и платформах."). Сведения о поддерживаемых версиях для каждого кодового модуля смотрите в разделе [Поддерживаемые технологии и версии OneAgent](/managed/ingest-from/technology-support "Технические подробности поддержки Dynatrace для конкретных платформ и фреймворков разработки.").

### Требования

[Требования для OneAgent](/managed/ingest-from/dynatrace-oneagent/oa-requirements "Требования к кодовым модулям OneAgent")

### Смотрите также

[Adaptive Traffic Management](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Улучшение работоспособности и производительности вашего окружения Dynatrace Managed с помощью адаптивных функций управления трафиком, снижения нагрузки и контроля захвата данных.")

### Установка и эксплуатация

Облачные платформы

Kubernetes

Другие контейнерные платформы

Операционные системы

[![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS")AWS](/managed/ingest-from/amazon-web-services) [![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure")Azure](/managed/ingest-from/microsoft-azure-services) [![Google Cloud](https://dt-cdn.net/images/gcp-512-db85a455ae.webp "Google Cloud")Google Cloud](/managed/ingest-from/google-cloud-platform)

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")Kubernetes](/managed/ingest-from/setup-on-k8s)

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry) [![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")Docker](/managed/ingest-from/setup-on-container-platforms/docker) [![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")Heroku](/managed/ingest-from/setup-on-container-platforms/heroku) [![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")Mesos](/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon)

[Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [zOS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos)