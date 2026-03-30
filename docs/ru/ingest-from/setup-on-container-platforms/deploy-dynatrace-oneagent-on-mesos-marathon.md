---
title: Развертывание OneAgent на Mesos/Marathon
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon
scraped: 2026-03-06T21:15:40.651397
---

# Развёртывание OneAgent на Mesos/Marathon


Mesos — универсальный менеджер кластерных ресурсов, который можно использовать совместно с фреймворком Marathon для запуска контейнеров в распределённых средах.

Для мониторинга приложений, работающих в [кластерах Mesos](https://www.dynatrace.com/technologies/mesos-monitoring/), рекомендуется развернуть OneAgent на всех узлах агентов Mesos с помощью развёртывания приложения Marathon. После этого установите OneAgent на главных узлах Mesos, как описано на этой странице.

## Определение URL-адреса установщика OneAgent

Первым шагом необходимо получить адрес для `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация предоставляется в процессе установки OneAgent.

Чтобы получить `ONEAGENT_INSTALLER_SCRIPT_URL`

1. В Dynatrace Hub выберите **OneAgent**.
2. Выберите **Настроить** > **Linux**.

3. Определите URL-адрес скрипта установщика и токен из команды `wget`, предоставленной в интерфейсе:

Версия образа контейнера OneAgent 1.39.1000+

Версия образа контейнера OneAgent 1.38.1000 и более ранние

Это URL-адрес:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр `flavor=default`.
* Для значения `API-Token` требуется [токен PaaS](../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Learn the concept of an access token and its scopes.").

Ваш URL должен выглядеть следующим образом:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Ваш URL и токен API.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Добавьте токен API к URL с помощью параметра `API-Token`. Ваш URL должен выглядеть следующим образом:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Установка OneAgent

1. Разверните OneAgent на узлах агентов Mesos.

   При использовании DC/OS

   При отсутствии DC/OS

   Если вы используете [DC/OS](https://www.dynatrace.com/technologies/dcos-monitoring/) для управления кластером Mesos, вы можете воспользоваться пакетом Dynatrace в репозитории DC/OS. Пакет репозитория автоматически развернёт Dynatrace на всех узлах агентов Mesos.

   Если вы не используете [DC/OS](https://www.dynatrace.com/technologies/dcos-monitoring), вы можете запустить OneAgent как приложение Marathon, следуя приведённому примеру.

   * Используйте команду `cat` для создания файла `dynatrace-oneagent.json`. Перед запуском отредактируйте JSON-часть из примера ниже и замените два заполнителя данными вашего кластера Mesos:

     + `REPLACE_WITH_YOUR_URL` — расположение `ONEAGENT_INSTALLER_SCRIPT_URL`, определённое ранее.
     + `REPLACE_WITH_NUMBER_OF_NODES` — целое число, представляющее количество узлов в вашем кластере Mesos.

   ```
   cat <<- EOF > dynatrace-oneagent.json


   {


   "id": "dynatrace-oneagent",


   "cpus": 0.1,


   "mem": 256,


   "instances": REPLACE_WITH_NUMBER_OF_NODES,


   "constraints": [["hostname", "UNIQUE"], ["hostname", "GROUP_BY"]],


   "container": {


   "type": "DOCKER",


   "volumes": [


   {


   "containerPath": "/mnt/root",


   "hostPath": "/",


   "mode": "RW"


   }


   ],


   "docker": {


   "image": "dynatrace/oneagent",


   "forcePullImage": true,


   "network": "HOST",


   "privileged": true,


   "parameters": [


   { "key": "pid", "value": "host" },


   { "key": "ipc", "value": "host" },


   { "key": "env", "value": "ONEAGENT_INSTALLER_SCRIPT_URL=REPLACE_WITH_YOUR_URL" },


   { "key": "env", "value": "ONEAGENT_INSTALLER_SKIP_CERT_CHECK=false "}


   ]


   }


   },


   "args": [


   ]


   }


   EOF
   ```

   * После создания файла `dynatrace-oneagent.json` отправьте HTTP POST-запрос к главному узлу-лидеру Mesos для развёртывания приложения Marathon с OneAgent.

   ```
   curl -X POST -H "Content-Type: application/json" http://your-mesos-master:8080/v2/apps -d@dynatrace-oneagent.json
   ```
2. Разверните OneAgent на главных узлах Mesos.

   Marathon не позволяет развёртывать приложения на главных узлах (за исключением узлов, одновременно являющихся и главными, и агентами). По этой причине необходимо вручную установить OneAgent на все главные узлы Mesos, которые не настроены дополнительно как агенты Mesos. Для этого воспользуйтесь стандартным установщиком для Linux.

## Связанные темы

* Матрица поддержки платформ и возможностей OneAgent
