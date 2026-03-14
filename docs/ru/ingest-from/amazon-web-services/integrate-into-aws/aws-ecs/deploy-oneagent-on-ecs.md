---
title: Мониторинг Elastic Container Service (ECS) с типом запуска EC2
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs
scraped: 2026-03-04T21:35:27.635545
---

# Мониторинг Elastic Container Service (ECS) с типом запуска EC2


* Classic
* Практическое руководство
* Чтение: 3 мин
* Опубликовано 18 мая 2020 г.

Для развёртывания OneAgent в кластерах **AWS Elastic Container Service** (ECS) с типом запуска EC2 следуйте приведённым ниже инструкциям.

## Предварительные требования

* Создайте [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Learn the concept of an access token and its scopes.").
* Кластер ECS с **контейнерными экземплярами на базе Linux**.
* Ознакомьтесь со списком [поддерживаемых приложений и версий](../../../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Создайте IAM-роль `ecsinstanceRole` в консоли ECS.

## Развёртывание OneAgent как сервиса-демона

Этот подход описывает установку OneAgent как сервиса-демона в собственном контейнере. ECS оркестрирует выполнение задачи OneAgent на каждом контейнерном экземпляре, входящем в кластер.

1. В консоли ECS перейдите в **Task Definitions** > **Create new Task Definition**. Выберите **EC2**, а затем **Next step**.
2. В разделе **Configure task and container definitions** введите следующие значения:

   * **Task Definition Name**: `oneagent`
   * **Network Mode**: `host`
3. Прокрутите вниз до раздела **Volumes**. Нажмите **Add volume** и введите следующие значения:

   * **Name**: `oneagent`
   * **Volume type**: `Bind Mount`
   * **Source path**: `/`

   Нажмите **Add**, чтобы добавить том.
4. Прокрутите до раздела **Container Definitions** и нажмите **Add container**. В разделе **Standard** введите следующие значения:

   * **Container name**: `oneagent`
   * **Image**: `dynatrace/oneagent`
   * **Memory limits**: по необходимости

   Существует два типа ограничений памяти: мягкое и жёсткое. ECS требует определить ограничение хотя бы для одного типа памяти. Мы рекомендуем использовать настройку по умолчанию (мягкое ограничение 256 МиБ), так как она менее строгая, но вы можете изменить эту настройку по необходимости.
5. В разделе **Advanced container configuration** перейдите в **Environment**. Убедитесь, что выбран параметр **Essential**.

   В **Environment variables** определите `ONEAGENT_INSTALLER_SCRIPT_URL` в зависимости от способа подключения к Dynatrace:

   * Для SaaS: `https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * Для Managed: `https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * Для ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   Если вы подключаетесь через ActiveGate, вы можете пропустить проверку сертификата, добавив ключ `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` со значением `true`.
6. Необязательно: добавьте параметры установщика OneAgent.

   Оставаясь в разделе **Environment variables**, вы можете [настроить установку OneAgent](../../../dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux.md "Learn how to use the Linux installer with command line parameters."), добавив несколько параметров установщика OneAgent в текстовое поле команды. Убедитесь, что каждый параметр отделён пробелом. Например, `--set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Установите параметр `--set-network-zone=<your.network.zone>`, если хотите настроить сетевые зоны. Дополнительную информацию см. в разделе [сетевые зоны](../../../../manage/network-zones.md "Find out how network zones work in Dynatrace.").
7. Перейдите в **Storage and logging** и введите следующие значения в **Mount point**:

   * **Source volume**: `oneagent`
   * **Container path**: `/mnt/root`
8. Прокрутите вниз до раздела **Security** и установите контейнер для работы в **привилегированном** режиме.
9. Нажмите **Add**, чтобы добавить определение контейнера.
10. Оставаясь в определении задачи, вернитесь к разделу **Volumes** и нажмите **Configure via JSON**. Добавьте следующие два параметра на корневом уровне (например, перед `"tags"`):

    ```
    "ipcMode": "host",


    "pidMode": "host",
    ```

    Нажмите **Save**, чтобы сохранить JSON-конфигурацию.
11. Нажмите **Create**, чтобы сохранить определение задачи.
12. В меню **Task definitions** выберите только что созданную задачу OneAgent, затем нажмите **Actions** > **Create service**. Это создаст сервис для выполнения вашей задачи.
13. В разделе **Configure service** введите следующие значения:

    * **Launch type**: `EC2`
    * **Task Definition**: `oneagent`
    * **Service type**: `DAEMON`
    * **Service name**: укажите имя сервиса.

    Оставьте остальные настройки по умолчанию. Следуйте оставшимся шагам, пока не дойдёте до **Create service** и не выберете его.

    После создания сервиса связанные задачи будут выполнены. Сервис `oneagent` создаёт задачу для развёртывания OneAgent на каждом контейнерном экземпляре вашего кластера.

    Вы можете увидеть контейнерные экземпляры, отображённые на панели кластера ECS, и соответствующие хосты в вашей среде мониторинга Dynatrace.

    ![Хосты ECS](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)
14. После развёртывания OneAgent перезапустите работающие задачи приложения, чтобы получить видимость на уровне сервисов.

## Последствия для безопасности

Подробности см. в разделе [Последствия для безопасности Docker](../../../setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md#security "Install and update Dynatrace OneAgent as a Docker container.").

## Ограничения

Подробности см. в разделе [Ограничения Docker](../../../setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md#limitations "Install and update Dynatrace OneAgent as a Docker container.").

## Потребление мониторинга

Для Elastic Container Service потребление мониторинга основано на единицах хостов. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (Host Units)](../../../../license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")