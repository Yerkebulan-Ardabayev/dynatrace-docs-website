---
title: OneAgent privileges for container monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/oneagent-privileges
scraped: 2026-03-05T21:38:31.407473
---

# Привилегии OneAgent для мониторинга контейнеров

# Привилегии OneAgent для мониторинга контейнеров

* Latest Dynatrace
* 2-min read
* Published Mar 08, 2023

Dynatrace поддерживает Full-Stack Monitoring для контейнерных платформ — от уровня приложения до уровня инфраструктуры. Для получения метрик на уровне контейнеров и выполнения глубокого мониторинга кода хоста, включая внедрение OneAgent в процессы, требуются повышенные привилегии.

Однако если вы не хотите предоставлять повышенные привилегии OneAgent или у вас нет доступа к уровню инфраструктуры, вы можете использовать мониторинг только приложений.

Для Kubernetes мониторинг только приложений на основе Dynatrace Operator всё же предоставляет широкий набор данных, например: insights на уровне узлов (основные метрики и оповещения) на основе данных, полученных ActiveGate из Kubernetes API, а также метрики Prometheus.

## Полностековое внедрение

Контейнер OneAgent и базовый хост совместно используют выбранные пространства имён Linux, чтобы OneAgent мог получать доступ к данным, необходимым для full-stack мониторинга:

* Общее сетевое пространство имён позволяет процессам, запущенным внутри контейнера, напрямую обращаться к сетевым интерфейсам хоста.
* Общее пространство имён PID позволяет процессам, запущенным внутри контейнера, видеть и работать со всеми процессами из таблицы процессов хоста.
* Смонтированная корневая файловая система хоста доступна всем модулям OneAgent и обеспечивает доступ к лог-файлам, дисковым метрикам и другим возможностям full-stack мониторинга.

В процессе мониторинга область необходимых разрешений для каждого процесса ограничивается с помощью специальных [возможностей Linux System Capabilities](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux.").

Полностековое внедрение можно реализовать с использованием следующих режимов развёртывания:

* Dynatrace Operator на Kubernetes/OpenShift

  + [Режим cloud-native full-stack](/docs/ingest-from/setup-on-k8s/how-it-works#cloud-native "Подробное описание принципа работы развёртывания на Kubernetes.")
  + [Режим classic full-stack](/docs/ingest-from/setup-on-k8s/how-it-works#classic "Подробное описание принципа работы развёртывания на Kubernetes.")
* Docker вне контейнерной платформы

  + [OneAgent в качестве Docker-контейнера](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Установите и обновите Dynatrace OneAgent в качестве Docker-контейнера.")

### OneAgent на хосте Docker

В качестве альтернативы вы также можете развернуть OneAgent на хосте Docker под управлением Linux. В этом случае OneAgent не запускается в контейнере, а работает непосредственно на хосте, поэтому изоляция пространства имён Linux отсутствует. Подробнее см. в [OneAgent на Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнайте, как установить OneAgent на Linux, как настроить установку и многое другое.").

## Внедрение только для приложений

OneAgent, развёрнутый в режиме только для приложений, не запускается как привилегированный контейнер.

Подробнее см. в:

* [Начало работы с мониторингом платформы Kubernetes + наблюдаемость приложений](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Развёртывание Dynatrace Operator в режиме мониторинга приложений на Kubernetes")
* [Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Установка OneAgent на Cloud Foundry.")
* [Настройка OneAgent на контейнерах для мониторинга только приложений](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга только приложений.")
