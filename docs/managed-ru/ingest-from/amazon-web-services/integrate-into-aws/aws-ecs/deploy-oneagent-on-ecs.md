---
title: Monitor Elastic Container Service (ECS) with EC2 launch type
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs
scraped: 2026-05-12T11:52:04.148330
---

# Мониторинг Elastic Container Service (ECS) с типом запуска EC2

# Мониторинг Elastic Container Service (ECS) с типом запуска EC2

* Практическое руководство
* Чтение: 3 мин
* Опубликовано 18 мая 2020 г.

Чтобы развернуть OneAgent на кластерах **AWS Elastic Container Service** (ECS) с типом запуска EC2, следуйте инструкциям ниже.

## Предварительные условия

* Создайте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Кластер ECS с **Linux-based container instances**.
* Изучите список [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").
* Создайте IAM-роль `ecsinstanceRole` в консоли ECS.

## Развёртывание OneAgent как daemon-сервиса

Этот подход описывает установку OneAgent как daemon-сервиса в собственном контейнере. ECS оркестрирует выполнение задачи OneAgent на каждом экземпляре-контейнере кластера.

1. В консоли ECS перейдите в **Task Definitions** > **Create new Task Definition**. Выберите **EC2**, затем **Next step**.
2. В **Configure task and container definitions** введите следующие значения:

   * **Task Definition Name**: `oneagent`
   * **Network Mode**: `host`
3. Прокрутите вниз до **Volumes**. Нажмите **Add volume** и введите значения:

   * **Name**: `oneagent`
   * **Volume type**: `Bind Mount`
   * **Source path**: `/`

   Нажмите **Add**, чтобы добавить том.
4. Прокрутите до **Container Definitions** и нажмите **Add container**. В секции **Standard** введите следующие значения:

   * **Container name**: `oneagent`
   * **Image**: `dynatrace/oneagent`
   * **Memory limits**: по необходимости

   Существует два типа лимитов памяти: soft и hard. ECS требует, чтобы был задан лимит хотя бы для одного типа памяти. Рекомендуется использовать настройку по умолчанию (soft limit 256 МиБ), так как она менее строгая, но при необходимости значение можно скорректировать.
5. В секции **Advanced container configuration** перейдите в **Environment**. Убедитесь, что **Essential** выбран.

   В **Environment variables** задайте `ONEAGENT_INSTALLER_SCRIPT_URL` в зависимости от того, как вы подключаетесь к Dynatrace:

   * Для SaaS: `https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * Для Managed: `https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<pass_token>`
   * Для ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   Если подключаетесь через ActiveGate, можно пропустить проверку сертификата, добавив ключ `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` со значением `true`.
6. Опционально добавьте параметры установщика OneAgent.

   Не выходя из **Environment variables**, можно [настроить установку OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать Linux-установщик с параметрами командной строки."), добавив несколько параметров установщика OneAgent в текстовое поле команды. Параметры разделяйте пробелом. Например, `--set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Задайте параметр `--set-network-zone=<your.network.zone>`, если хотите настроить network zones. Подробнее см. [network zones](/managed/manage/network-zones "Узнайте, как работают network zones в Dynatrace.").
7. Перейдите в **Storage and logging** и введите в **Mount point** следующие значения:

   * **Source volume**: `oneagent`
   * **Container path**: `/mnt/root`
8. Прокрутите вниз до **Security** и переведите контейнер в режим **Privileged**.
9. Нажмите **Add**, чтобы добавить определение контейнера.
10. Не выходя из определения задачи, вернитесь в **Volumes** и нажмите **Configure via JSON**. Добавьте следующие два параметра на корневом уровне (например, перед `"tags"`):

    ```
    "ipcMode": "host",



    "pidMode": "host",
    ```

    Нажмите **Save**, чтобы сохранить JSON-конфигурацию.
11. Нажмите **Create**, чтобы сохранить определение задачи.
12. В меню **Task definitions** выберите только что созданную задачу OneAgent, затем нажмите **Actions** > **Create service**. Так будет создан сервис для запуска вашей задачи.
13. В **Configure service** введите следующие значения:

    * **Launch type**: `EC2`
    * **Task Definition**: `oneagent`
    * **Service type**: `DAEMON`
    * **Service name**: задайте имя сервиса.

    Остальные настройки оставьте по умолчанию. Пройдите оставшиеся шаги и нажмите **Create service**.

    После создания сервиса связанные с ним задачи будут запущены. Сервис `oneagent` создаёт задачу для развёртывания OneAgent на каждом экземпляре-контейнере вашего кластера.

    Экземпляры-контейнеры отображаются на дашборде кластера ECS, а соответствующие хосты, в среде мониторинга Dynatrace.

    ![ECS hosts](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)

    ECS hosts
14. После развёртывания OneAgent перезапустите запущенные задачи приложений, чтобы получить видимость на уровне сервисов.

## Аспекты безопасности

Подробности см. в [Аспекты безопасности Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#security "Установка и обновление Dynatrace OneAgent как Docker-контейнера.").

## Ограничения

Подробности см. в [Ограничения Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как Docker-контейнера.").

## Потребление мониторинга

Для Elastic Container Service потребление мониторинга рассчитывается на основе host units. Подробности см. в [Application and Infrastructure Monitoring (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры в Dynatrace на основе host units.").

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в разных операционных системах и платформах.")