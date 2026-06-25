---
title: Развёртывание OneAgent на Mesos/Marathon
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon
scraped: 2026-05-12T11:04:10.043839
---

# Развёртывание OneAgent на Mesos/Marathon

# Развёртывание OneAgent на Mesos/Marathon

* 2-min read
* Published May 21, 2020

Mesos — универсальный менеджер ресурсов кластера, который совместно с фреймворком Marathon используется для запуска контейнеров в распределённых средах.

Для мониторинга приложений, работающих в [кластерах Mesos](https://www.dynatrace.com/technologies/mesos-monitoring/), рекомендуется развернуть OneAgent на всех агентских узлах Mesos через развёртывание приложения Marathon, а затем установить OneAgent на мастер-узлах Mesos, как описано на этой странице.

## Определение URL установщика OneAgent

Первый шаг — получение URL для `ONEAGENT_INSTALLER_SCRIPT_URL`. Эта информация отображается во время установки OneAgent.

Для получения `ONEAGENT_INSTALLER_SCRIPT_URL`:

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Linux**.
3. Определите URL скрипта установщика и токен из команды `wget`, предоставленной в UI.

Версия образа контейнера OneAgent 1.39.1000+

Версия образа контейнера OneAgent 1.38.1000 и ранее

* Замените значение параметра `arch` на `<arch>`. Игнорируйте параметр `flavor=default`.
* Для значения `API-Token` необходим [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Концепция токена доступа и его областей видимости.").

Ваш URL должен выглядеть так:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

Добавьте API-токен к URL с помощью параметра `API-Token`. Ваш URL должен выглядеть так:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

Это ваш `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Установка OneAgent

1. Разверните OneAgent на агентских узлах Mesos.

   При использовании DC/OS

   Без DC/OS

   При использовании [DC/OS](https://www.dynatrace.com/technologies/dcos-monitoring/) для управления кластером Mesos можно воспользоваться пакетом Dynatrace в репозитории DC/OS. Пакет автоматически развернёт Dynatrace на всех агентских узлах Mesos.

   Без [DC/OS](https://www.dynatrace.com/technologies/dcos-monitoring/) можно запустить OneAgent как Marathon-приложение, следуя следующему примеру.

   * Используйте команду `cat` для создания файла `dynatrace-oneagent.json`. Перед запуском отредактируйте JSON-часть примера ниже, заменив два плейсхолдера:

     + `REPLACE_WITH_YOUR_URL` — расположение `ONEAGENT_INSTALLER_SCRIPT_URL`, определённое ранее.
     + `REPLACE_WITH_NUMBER_OF_NODES` — целое число, представляющее количество узлов в кластере Mesos.

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

   * После создания файла `dynatrace-oneagent.json` отправьте HTTP POST-запрос на мастер-лидер Mesos для развёртывания Marathon-приложения с OneAgent.

   ```
   curl -X POST -H "Content-Type: application/json" http://your-mesos-master:8080/v2/apps -d@dynatrace-oneagent.json
   ```

2. Разверните OneAgent на мастер-узлах Mesos.

   Marathon не позволяет развёртывать приложения на мастер-узлах (за исключением узлов, настроенных как мастер и агент одновременно). Поэтому необходимо вручную установить OneAgent на всех мастер-узлах Mesos, которые не настроены как агенты. Для этого используйте стандартный [установщик Linux](/managed/ingest-from/dynatrace-oneagent "Основные концепции OneAgent и инструкции по установке на разных платформах.").

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")