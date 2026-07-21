---
title: Мониторинг Amazon ECS на EC2
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs
---

# Мониторинг Amazon ECS на EC2

# Мониторинг Amazon ECS на EC2

* Практическое руководство
* 1 минута на чтение
* Обновлено 03 июн. 2026 г.

Чтобы развернуть OneAgent на кластерах AWS Elastic Container Service (ECS) с типом запуска EC2, следуй приведённым ниже инструкциям.

## Предварительные требования

* Создать [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучить концепцию токена доступа и его области действия.").
* Кластер ECS с **контейнерными инстансами на базе Linux**.
* Ознакомиться со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найти технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").
* К роли IAM для контейнерных инстансов должна быть подключена управляемая политика `AmazonEC2ContainerServiceforEC2Role`. Инструкции по созданию этой роли, названной `ecsInstanceRole`, приведены в [документации AWS﻿](https://dt-url.net/y923usz).

## Развёртывание OneAgent как службы-демона

Этот подход описывает установку OneAgent как службы-демона в собственном контейнере. ECS оркестрирует выполнение задачи OneAgent на каждом контейнерном инстансе, входящем в состав кластера.

Привилегированный режим и параметры томов, это предварительные условия для этого метода развёртывания. Из-за этого выполнить его можно только с помощью ревизий JSON. Вместо этого стоит рассмотреть [внедрение на этапе сборки](/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Установка, обновление и удаление OneAgent на контейнерах для мониторинга уровня приложений.").

1. В консоли ECS перейти в **Task Definitions** > **Create new task definition** > **Create new task definition with JSON**.
2. Отредактировать определение задачи JSON:

   * Установить `requiresCompatibilities` в значение `["EC2"]`
   * Установить `family` в уникальное имя по своему выбору для определения задачи, например `oneagent`
   * Добавить `ipcMode` и установить значение `host`
   * Добавить `pidMode` и установить значение `host`
   * Установить `containerDefinitions[0]` в

     ```
     {



     "name": "oneagent",



     "image": "dynatrace/oneagent",



     "essential": true,



     "privileged": true



     }
     ```
   * Создать новый словарь в массиве `volumes`:

     ```
     {



     "name": "oneagent"



     }
     ```
3. Выбрать **Create**.
4. Выбрать **Create new revision** > **Create new revision**.
5. В **Infrastructure requirements** перейти в **Network Mode** и выбрать `host`.
6. Прокрутить до **Container - 1**, перейти в **Resource allocation limits** и задать лимиты памяти по необходимости

   Есть два типа лимитов памяти: мягкий и жёсткий. ECS требует определить лимит хотя бы для одного типа памяти. Рекомендуется использовать значение по умолчанию (мягкий лимит 256 МиБ), так как оно менее ограничительное, но при необходимости этот параметр можно скорректировать.
7. В разделе **Переменные Environment** перейти в **Add individually** и определить `ONEAGENT_INSTALLER_SCRIPT_URL` в зависимости от способа подключения к Dynatrace:

   * Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`
   * Для ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   При подключении через ActiveGate можно пропустить проверку сертификата, добавив ключ `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` со значением `true`.
8. Опционально Добавить параметры установщика OneAgent.

   Оставаясь в разделе **Переменные Environment**, можно [настроить установку OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнать, как использовать установщик для Linux с параметрами командной строки.") добавив несколько параметров установщика OneAgent в текстовое поле команды. Каждый параметр нужно разделять пробелом. Например, `--set-monitoring-mode=infra-only --set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Задать параметр `--set-network-zone=<your.network.zone>`, если нужно настроить сетевые зоны. Подробнее см. [сетевые зоны](/managed/manage/network-zones "Узнать, как работают сетевые зоны в Dynatrace.").
9. Прокрутить вниз до **Storage** > **Volume - 1** и установить **Source path** в значение `/`
10. Перейти в **Container mount points**, выбрать **Add mount point** и ввести следующие значения:

    * **Container**: `oneagent`
    * **Source volume**: `oneagent`
    * **Container path**: `/mnt/root`
11. Выбрать **Create**, чтобы сохранить определение задачи.
12. В меню **Task definitions** выбрать только что созданную задачу OneAgent, а затем **Deploy** > **Create service**. Это создаст службу для выполнения задачи.
13. В **Compute configuration** выбрать **Launch type** и для **Launch type** выбрать `EC2`.
14. В **Deployment configuration** выполнить следующие действия:

    * **Service name**: указать имя службы.
    * **Service type**: выбрать `Daemon`.

    Остальные настройки оставить как есть по умолчанию. Пройти оставшиеся шаги, пока не дойдёшь до кнопки **Create**, и выбрать её.

    После создания службы будут выполнены связанные с ней задачи. Служба `oneagent` создаёт задачу для развёртывания OneAgent на каждом контейнерном инстансе кластера.

    Контейнерные инстансы отображаются на панели кластера ECS, а соответствующие хосты, в среде мониторинга Dynatrace.

    ![Хосты ECS](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)

    Хосты ECS
15. После развёртывания OneAgent нужно перезапустить выполняющиеся задачи приложений, чтобы получить видимость на уровне сервисов.

## Последствия для безопасности

Подробности см. в разделе [последствия для безопасности Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#security "Установка и обновление OneAgent Dynatrace в виде контейнера Docker.").

## Ограничения

Подробности см. в разделе [ограничения Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление OneAgent Dynatrace в виде контейнера Docker.").

## Потребление мониторинга

Для Elastic Container Service потребление мониторинга рассчитывается на основе host units. Подробности см. в разделе [Application and Infrastructure Monitoring (Host Units)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Понять, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

## Похожие темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнать, какие возможности поддерживаются OneAgent на разных операционных системах и платформах.")