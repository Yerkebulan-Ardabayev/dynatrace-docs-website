---
title: Dynatrace OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent
scraped: 2026-03-06T21:12:35.235477
---

# Dynatrace OneAgent

# Dynatrace OneAgent

* Latest Dynatrace
* Чтение: 2 мин
* Опубликовано 09 окт. 2018 г.

OneAgent отвечает за сбор всех данных мониторинга в вашей отслеживаемой среде. Один экземпляр OneAgent на хост необходим для сбора всех актуальных данных мониторинга — даже если ваши хосты развёрнуты в контейнерах Docker, архитектурах микросервисов или облачной инфраструктуре.

Один экземпляр OneAgent может обеспечить [мониторинг для всех типов объектов](/docs/platform/oneagent/supported-monitoring-types "Read an overview of all monitoring capabilities offered by OneAgent."), включая серверы, приложения, службы, базы данных и многое другое. OneAgent предоставляет все необходимые операционные и бизнес-метрики производительности — от фронтенда до бэкенда и всего между ними: облачные экземпляры, хосты, состояние сети, процессы и службы. OneAgent обнаруживает все процессы, запущенные на ваших хостах. На основе найденного OneAgent автоматически активирует инструментирование, специально разработанное для вашего уникального стека приложений. Он также внедряет все теги, необходимые для мониторинга пользовательского опыта, в HTML страниц вашего приложения. Новые компоненты инструментируются автоматически на лету.

OneAgent состоит из нескольких модулей кода, которые позволяют ему работать с большинством технологий «из коробки». Чтобы узнать, какие модули кода поддерживаются для каждой платформы, см. [матрицу поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). Чтобы узнать, какие версии поддерживаются для каждого модуля кода, см. [поддерживаемые OneAgent технологии и версии](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Требования

[Требования к OneAgent](/docs/ingest-from/dynatrace-oneagent/oa-requirements "OneAgent code module requirements")

### Смотрите также

[Адаптивное управление трафиком](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.")

### Установка и эксплуатация

Облачные платформы

Kubernetes

Другие контейнерные платформы

Операционные системы

[![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS")AWS](/docs/ingest-from/amazon-web-services) [![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure")Azure](/docs/ingest-from/microsoft-azure-services) [![Google Cloud](https://dt-cdn.net/images/gcp-512-db85a455ae.webp "Google Cloud")Google Cloud](/docs/ingest-from/google-cloud-platform)

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")Kubernetes](/docs/ingest-from/setup-on-k8s)

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry) [![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")Docker](/docs/ingest-from/setup-on-container-platforms/docker) [![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")Mesos](/docs/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon)

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)
