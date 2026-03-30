---
title: Dynatrace OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent
scraped: 2026-03-06T21:12:35.235477
---

* Latest Dynatrace

OneAgent отвечает за сбор всех данных мониторинга в вашей отслеживаемой среде. Один экземпляр OneAgent на хост необходим для сбора всех актуальных данных мониторинга — даже если ваши хосты развёрнуты в контейнерах Docker, архитектурах микросервисов или облачной инфраструктуре.

Один экземпляр OneAgent может обеспечить мониторинг для всех типов объектов, включая серверы, приложения, службы, базы данных и многое другое. OneAgent предоставляет все необходимые операционные и бизнес-метрики производительности — от фронтенда до бэкенда и всего между ними: облачные экземпляры, хосты, состояние сети, процессы и службы. OneAgent обнаруживает все процессы, запущенные на ваших хостах. На основе найденного OneAgent автоматически активирует инструментирование, специально разработанное для вашего уникального стека приложений. Он также внедряет все теги, необходимые для мониторинга пользовательского опыта, в HTML страниц вашего приложения. Новые компоненты инструментируются автоматически на лету.

OneAgent состоит из нескольких модулей кода, которые позволяют ему работать с большинством технологий «из коробки». Чтобы узнать, какие модули кода поддерживаются для каждой платформы, см. матрицу поддержки платформ и возможностей OneAgent. Чтобы узнать, какие версии поддерживаются для каждого модуля кода, см. поддерживаемые OneAgent технологии и версии.

### Требования

Требования к OneAgent

### Смотрите также

Адаптивное управление трафиком

### Установка и эксплуатация

Облачные платформы

Kubernetes

Другие контейнерные платформы

Операционные системы

[![AWS](https://dt-cdn.net/images/aws-512-eed109b7f1.png "AWS")AWS](amazon-web-services.md) [![Azure](https://dt-cdn.net/images/azure-512-a93a37d351.png "Azure")Azure](microsoft-azure-services.md) [![Google Cloud](https://dt-cdn.net/images/gcp-512-db85a455ae.webp "Google Cloud")Google Cloud](google-cloud-platform.md)

[![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes")Kubernetes](setup-on-k8s.md)

[![Cloud Foundry](https://dt-cdn.net/images/cloud-foundry-512-d7620ed0ba.png "Cloud Foundry")Cloud Foundry](setup-on-container-platforms/cloud-foundry.md) [![Docker](https://dt-cdn.net/images/docker-512-0c0977826e.webp "Docker")Docker](setup-on-container-platforms/docker.md) [![Heroku](https://dt-cdn.net/images/heroku-512-984aa81b41.webp "Heroku")Heroku](setup-on-container-platforms/heroku.md) [![Mesos](https://dt-cdn.net/images/mesos-512-0c28279189.webp "Mesos")Mesos](setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon.md)

[AIX](dynatrace-oneagent/installation-and-operation/aix.md) [Linux](dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](dynatrace-oneagent/installation-and-operation/windows.md) [zOS](dynatrace-oneagent/installation-and-operation/zos.md)
