---
title: Мониторинг Amazon Elastic Container Service (ECS)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs
scraped: 2026-03-06T21:18:11.880580
---

Чтобы развернуть OneAgent в кластерах AWS Elastic Container Service (ECS) с типом запуска EC2, следуйте приведённым ниже инструкциям.

## Предварительные требования

* Создайте [токен PaaS](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Изучите концепцию токена доступа и его областей применения.").
* Кластер ECS с **экземплярами контейнеров на базе Linux**.
* Ознакомьтесь со списком поддерживаемых приложений и версий.
* Роль IAM для ваших экземпляров контейнеров должна включать управляемую политику `AmazonEC2ContainerServiceforEC2Role`. Инструкции по созданию этой роли с именем `ecsInstanceRole` приведены в [документации AWS](https://dt-url.net/y923usz).

## Развёртывание OneAgent как службы-демона

Этот подход описывает установку OneAgent как службы-демона в собственном контейнере. ECS оркестрирует выполнение задачи OneAgent на каждом экземпляре контейнера, входящем в кластер.

Привилегированный режим и параметры томов являются обязательными условиями для данного метода развёртывания. В результате это можно сделать только с помощью JSON-ревизий. Рассмотрите возможность использования [внедрения на этапе сборки](aws-fargate.md#buildtime "Установите OneAgent на AWS Fargate.") в качестве альтернативы.

1. В консоли ECS перейдите в **Task Definitions** > **Create new task definition** > **Create new task definition with JSON**.
2. Отредактируйте JSON определения задачи:

   * Установите `requiresCompatibilities` в значение `["EC2"]`
   * Установите `family` в уникальное имя по вашему выбору для определения задачи, например `oneagent`
   * Добавьте `ipcMode` и установите значение `host`
   * Добавьте `pidMode` и установите значение `host`
   * Установите `containerDefinitions[0]` в следующее значение:

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
3. Выберите **Create**.
4. Выберите **Create new revision** > **Create new revision**.
5. В разделе **Infrastructure requirements** перейдите к **Network Mode** и выберите `host`.
6. Прокрутите до **Container - 1**, перейдите к **Resource allocation limits** и установите ограничения памяти по необходимости.

   Существует два типа ограничений памяти: мягкое и жёсткое. ECS требует, чтобы вы определили ограничение хотя бы для одного типа памяти. Мы рекомендуем использовать настройку по умолчанию (мягкое ограничение 256 МиБ), так как она менее ограничивающая, но вы можете скорректировать эту настройку по необходимости.
7. В разделе **Environment variables** перейдите к **Add individually** и определите `ONEAGENT_INSTALLER_SCRIPT_URL` в зависимости от способа подключения к Dynatrace:

   * Для Dynatrace SaaS: `https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`
   * Для ActiveGate: `https://<your-active-gate-ip-or-hostname>:9999/e/<your-environment-id>/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<paas_token>`

   Если вы подключаетесь через ActiveGate, вы можете пропустить проверку сертификата, добавив ключ `ONEAGENT_INSTALLER_SKIP_CERT_CHECK` со значением `true`.
8. Необязательно: добавьте параметры установщика OneAgent.

   Оставаясь в разделе **Environment variables**, вы можете настроить установку OneAgent, добавив несколько параметров установщика OneAgent в текстовое поле команды. Убедитесь, что каждый параметр разделён пробелом. Например, `--set-monitoring-mode=infra-only --set-app-log-content-access=false --set-network-zone=<your.network.zone>`.

   Установите параметр `--set-network-zone=<your.network.zone>`, если вы хотите настроить сетевые зоны. Дополнительную информацию см. в разделе сетевые зоны.
9. Прокрутите вниз до **Storage** > **Volume - 1** и установите **Source path** в значение `/`
10. Перейдите к **Container mount points**, выберите **Add mount point** и введите следующие значения:

    * **Container**: `oneagent`
    * **Source volume**: `oneagent`
    * **Container path**: `/mnt/root`
11. Выберите **Create** для сохранения определения задачи.
12. В меню **Task definitions** выберите только что созданную задачу OneAgent и затем выберите **Deploy** > **Create service**. Это создаст сервис для выполнения вашей задачи.
13. В разделе **Compute configuration** выберите **Launch type** и для **Launch type** выберите `EC2`.
14. В разделе **Deployment configuration** выполните следующие действия:

    * **Service name**: назовите сервис.
    * **Service type**: выберите `Daemon`.

    Остальные настройки оставьте по умолчанию. Следуйте оставшимся шагам до тех пор, пока не дойдёте до кнопки **Create** и выберите её.

    После создания сервиса связанные задачи будут выполнены. Сервис `oneagent` создаёт задачу для развёртывания OneAgent на каждом экземпляре контейнера вашего кластера.

    Вы можете увидеть экземпляры контейнеров на панели управления кластера ECS и соответствующие хосты в вашей среде мониторинга Dynatrace.

    ![ECS hosts](https://dt-cdn.net/images/hosts-ecs-1359-df8cef7810.png)
15. После развёртывания OneAgent перезапустите работающие задачи приложений для получения видимости на уровне сервисов.

## Последствия для безопасности

Подробности см. в разделе Последствия безопасности Docker.

## Ограничения

Подробности см. в разделе Ограничения Docker.

## Потребление мониторинга

Для Elastic Container Service потребление мониторинга рассчитывается на основе единиц хоста. Подробности см. в разделе Мониторинг приложений и инфраструктуры (единицы хоста).

## Связанные темы

* Матрица поддержки платформ и возможностей OneAgent
