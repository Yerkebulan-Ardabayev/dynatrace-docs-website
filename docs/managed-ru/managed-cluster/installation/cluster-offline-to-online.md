---
title: Перевод Managed Cluster из офлайн-режима в онлайн
source: https://docs.dynatrace.com/managed/managed-cluster/installation/cluster-offline-to-online
scraped: 2026-05-12T11:35:45.421914
---

# Перевод Managed Cluster из офлайн-режима в онлайн

# Перевод Managed Cluster из офлайн-режима в онлайн

* How-to guide
* 3-min read
* Updated on May 09, 2026

Для перевода Managed Cluster из офлайн-режима в онлайн выполните следующие шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Проверка требований**](/managed/managed-cluster/installation/cluster-offline-to-online#prerequisites "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Запрос онлайн-лицензии**](/managed/managed-cluster/installation/cluster-offline-to-online#request-license "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Запуск скрипта конвертации**](/managed/managed-cluster/installation/cluster-offline-to-online#run-script "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Проверка конвертации**](/managed/managed-cluster/installation/cluster-offline-to-online#verify-conversion "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")

## Шаг 1. Проверка требований

* Dynatrace Managed версии 1.338+
* SSH-доступ с возможностью sudo ко всем узлам Managed Cluster
* Токен Cluster API с областью доступа Service Provider API
* Подключение кластера к Mission Control (скрипт конвертации проверяет это)
* Прокси (при необходимости — см. [Настройка интернет-прокси для кластера](/managed/managed-cluster/configuration/internet-proxy "Configure a proxy connection for your Managed Cluster if you don't have direct internet access."))
* Cassandra и Elasticsearch работают корректно.
* Все узлы запущены и работают.
* Кластер не находится в режиме обслуживания.

## Шаг 2. Запрос онлайн-лицензии

Свяжитесь с представителем Dynatrace по продажам и запросите лицензию Dynatrace Managed в онлайн-режиме с отключёнными автоматическими обновлениями.

## Шаг 3. Запуск скрипта конвертации

Запустите скрипт последовательно на каждом узле Managed Cluster для перевода из офлайн-режима в онлайн:

```
/bin/sh /opt/dynatrace-managed/installer/convert-to-online.sh --api-token <api-token-value> --online-license <online-license-key>
```

* Обязательно: замените `<api-token-value>` на ваш токен API.
* Обязательно: замените `<online-license-key>` на ваш ключ онлайн-лицензии.
* Необязательно: для включения или отключения установки самомониторинг-OneAgent добавьте параметр `--install-agent on` или `--install-agent off`. По умолчанию используется `off`.

Если скрипт ещё не конвертировал все узлы Managed Cluster, в конце выводится следующее сообщение:

`Not all nodes have finished the conversion to online successfully yet. IDs of nodes left to convert: [2]`

## Шаг 4. Проверка конвертации

После завершения работы скрипта отображается сообщение, подтверждающее успешную конвертацию всех узлов Managed Cluster.

Если в разделе **Cluster Management Console** > **Home** > **Events** появилось следующее событие, конвертация завершена:

`Your Dynatrace Managed cluster has exited maintenance mode due to the end of node conversion to online.`

## Часто задаваемые вопросы

Где можно сгенерировать токен API?

В Cluster Management Console перейдите в **Home** > **Settings** > **API tokens** > **Cluster tokens** > **Generate token**.

Подробности см. в разделе [Аутентификация Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

Что произойдёт, если конвертация в онлайн-режим завершится ошибкой на одном из узлов?

Managed Cluster остаётся в режиме обслуживания до тех пор, пока все узлы не будут конвертированы в онлайн-режим. Скрипт является идемпотентным и может быть запущен повторно.

Где найти журналы выполнения скрипта?

По умолчанию скрипт сохраняет журналы в:

`/var/opt/dynatrace-managed/logs/installer/`

Какие предварительные проверки выполняются в начале работы скрипта?

В начале работы скрипта выполняются следующие проверки:

1. Cassandra и Elasticsearch работают корректно.
2. Все узлы запущены и работают.
3. Кластер не находится в режиме обслуживания.