---
title: Мониторинг Amazon Elastic Container Service (ECS)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs
scraped: 2026-05-12T11:14:24.040122
---

# Мониторинг Amazon Elastic Container Service (ECS)

# Мониторинг Amazon Elastic Container Service (ECS)

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 16 января 2023 г.

Чтобы развернуть OneAgent в кластерах AWS Elastic Container Service (ECS) с типом запуска EC2, следуйте приведённым ниже инструкциям.

## Предварительные требования

* Создайте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его области действия.").
* ECS-кластер с **Linux-инстансами контейнеров**.
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").
* К IAM-роли ваших инстансов контейнеров должна быть прикреплена управляемая политика `AmazonEC2ContainerServiceforEC2Role`. Инструкции по созданию этой роли с именем `ecsInstanceRole` приведены в [документации AWS](https://dt-url.net/y923usz).

## Развёртывание OneAgent в виде daemon-сервиса

Этот подход описывает установку OneAgent как daemon-сервиса в собственном контейнере. ECS оркестрирует выполнение задачи OneAgent на каждом инстансе контейнера, входящем в кластер.

Привилегированный режим и параметры томов являются обязательными для этого метода развёртывания. Поэтому это можно сделать только через JSON-ревизии. Рассмотрите вариант с [внедрением на этапе сборки](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate#buildtime "Установка OneAgent в AWS Fargate.").

1. В консоли ECS перейдите в **Task Definitions** > **Create new task definition** > **Create new task definition with JSON**.
2. Отредактируйте JSON определения задачи:

   * Установите `requiresCompatibilities` в `["EC2"]`
   * Установите `family` в выбранное вами уникальное имя для определения задачи, например `oneagent`
   * Добавьте `ipcMode` и установите в `host`
   * Добавьте `pidMode` и установите в `host`
   * Установите `containerDefinitions[0]` в

     ```
     {



     "name": "oneagent",



     "image": "dynatrace/oneagent",



     "essential": true,



     "privileged": true



     }
     ```
   * Создайте новый словарь в массиве `volumes`:

     ```
     {



     "name": "oneagent"



     }
     ```
3. Нажмите **Create**.
4. Нажмите **Create new revision** > **Create new revision**.
5. В разделе **Infrastructure requirements** перейдите к **Network Mode** и выберите `host`.
6. Прокрутите до **Container - 1**, перейдите в **Resource allocation limits** и задайте лимиты памяти при необходимости.

   Существует два типа лимитов памяти: soft и hard. ECS требует, чтобы вы определили лимит хотя бы для одного типа памяти. Мы рекомендуем использовать настройку по умолчанию (soft-лимит 256 MiB), так как она менее ограничительна, но вы можете изменить эту настройку при необходимости.
7. В разделе **Environment variables** перейдите в **Add individually** и определите `ONEAGENT_INSTALLER_SCRIPT_URL` в зависимости от того, как вы подключаетесь к Dynatrace:

   * Для Dynatrace Managed: `https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`
   * Для ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   Если вы подключаетесь через ActiveGate, можно пропустить проверку сертификата, добавив ключ `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` со значением `true`.
8. Опционально. Добавьте параметры установщика OneAgent.

   Оставаясь в **Environment variables**, вы можете [настроить установку OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки."), добавив несколько параметров установщика OneAgent в текстовое поле команды. Убедитесь, что параметры разделены пробелом. Например, `--set-monitoring-mode=infra-only --set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Установите параметр `--set-network-zone=<your.network.zone>`, если хотите настроить сетевые зоны. Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").
9. Прокрутите вниз до **Storage** > **Volume - 1** и установите **Source path** в `/`
10. Перейдите в **Container mount points**, нажмите **Add mount point** и введите следующие значения:

    * **Container**: `oneagent`
    * **Source volume**: `oneagent`
    * **Container path**: `/mnt/root`
11. Нажмите **Create**, чтобы сохранить определение задачи.
12. В меню **Task definitions** выберите вновь созданную задачу OneAgent, затем нажмите **Deploy** > **Create service**. Это создаст сервис для выполнения вашей задачи.
13. В **Compute configuration** выберите **Launch type** и для **Launch type** выберите `EC2`.
14. В **Deployment configuration** выполните следующие действия:

    * **Service name**: задайте имя сервиса.
    * **Service type**: выберите `Daemon`.

    Остальные настройки оставьте по умолчанию. Следуйте оставшимся шагам, пока не дойдёте до **Create** и не нажмёте её.

    После создания сервиса связанные с ним задачи будут выполнены. Сервис `oneagent` создаёт задачу для развёртывания OneAgent на каждом инстансе контейнера вашего кластера.

    Вы можете увидеть инстансы контейнеров на дашборде кластера ECS и соответствующие хосты в вашей среде мониторинга Dynatrace.

    ![ECS hosts](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)

    Хосты ECS
15. После развёртывания OneAgent перезапустите запущенные задачи приложений, чтобы получить видимость на уровне сервисов.

## Влияние на безопасность

Подробнее см. в разделе [Влияние Docker на безопасность](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#security "Установка и обновление Dynatrace OneAgent как Docker-контейнера.").

## Ограничения

Подробнее см. в разделе [Ограничения Docker](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Установка и обновление Dynatrace OneAgent как Docker-контейнера.").

## Потребление ресурсов мониторинга

Для Elastic Container Service потребление ресурсов мониторинга рассчитывается на основе host units. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе host units.").

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на различных платформах.")