---
title: Установка OneAgent на AIX
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix
---

# Установка OneAgent на AIX

# Установка OneAgent на AIX

* Практическое руководство
* Чтение 7 минут
* Обновлено 16 марта 2026 г.

На этой странице описано, как загрузить и установить Dynatrace OneAgent на AIX.

Для начала перейти в [Cluster Management Console и выбрать среду](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments."), которую нужно мониторить, затем продолжить установку по шагам ниже.

## Требования

### Разрешения

* Для загрузки и установки OneAgent нужны разрешения [Download/install OneAgent](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").
* Нужны права администратора на серверах, где будет установлен OneAgent, а также права на изменение настроек firewall (нужно только если внутренняя политика маршрутизации может препятствовать доступу ПО Dynatrace к интернету).
* Нужны разрешения и учётные данные для перезапуска всех сервисов приложений.

### Ресурсы

* Проверить [требования к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Find out what the disk space requirements are for OneAgent installation on AIX.").
* На хосте требуется как минимум 256 МБ свободной памяти для установки и обновления OneAgent.
* Процесс установки требует как минимум 256 МБ виртуальной памяти.
* Все хосты, которые нужно мониторить, должны иметь возможность отправлять данные в кластер Dynatrace. Все хосты, которые нужно мониторить, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от развёртывания Dynatrace, конфигурации сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### Ограничения

* Установка OneAgent не поддерживается на точках монтирования сетевых хранилищ, управляемых стандартами вроде NFS или iSCSI.
* Поддержка [Log management and Analytics﻿](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics) и [Log Monitoring Classic](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") на хостах AIX ограничена:

  + обнаружение логов в модуле логов ограничено только пользовательскими источниками логов.

### Разрешить соединения через firewall

Убедиться, что настройки firewall разрешают связь с Dynatrace.  
В зависимости от политики firewall может потребоваться явно разрешить определённые исходящие соединения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. Перейти в **Deploy Dynatrace**.
2. Выбрать **Start installation**. Затем выбрать платформу, на которой нужно установить OneAgent.
3. Вставить [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") в поле **Installer download token** или выбрать **Generate token**, чтобы сгенерировать токен сейчас и автоматически вставить его в **Installer download token**. Этот токен нужен для загрузки установщика OneAgent из среды. Токен автоматически добавляется в команды загрузки и установки, которые будут использоваться далее.
4. В блоке **Download OneAgent** выбрать **Copy**, чтобы скопировать команду `wget` в буфер обмена.
5. Войти на хост AIX, затем вставить и выполнить только что скопированную команду `wget`.

   * Команда `wget` по умолчанию не установлена на AIX. Либо установить её, либо использовать другой способ загрузки OneAgent.
   * Если при загрузке OneAgent возникает ошибка, установить нужный сертификат, загрузив файл корневого CA с [Comodo﻿](https://support.comodo.com/index.php?/Knowledgebase/Article/View/854/75/root-addtrustexternalcaroot) и затем присоединив содержимое CRT-файла к `/var/ssl/cert.pem`. Также можно пропустить проверку сертификата, добавив параметр `--no-check-certificate`.
   * При планировании загрузки OneAgent напрямую на сервер стоит учесть, что устаревшие или отсутствующие библиотеки (например, сертификаты CA или OpenSSL) помешают установщику загрузиться. Используются зашифрованные соединения. Для доступа `wget` к серверу требуется OpenSSL.
6. **Проверить подпись**

   После завершения загрузки выбрать **Copy** в блоке **Verify signature**, чтобы скопировать команду `wget` в буфер обмена, затем вставить предоставленную команду в окно терминала и выполнить её. Убедиться, что система обновлена, особенно библиотеки SSL и связанных сертификатов.
7. Опционально **Set customized options**

   * Включить мониторинг логического раздела [Virtual I/O Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#vios-installation "Learn how to download and install Dynatrace OneAgent on AIX.").
   * Задать [network zone](/managed/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") для этого хоста.
   * Если среда сегментирована (например, на разработку и продакшн), стоит рассмотреть [организацию хостов в host groups](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").
   * Переопределить автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). Это полезно в крупных и динамических средах, где заданные имена хостов могут быть неинтуитивными или часто меняться.
   * Применить [теги](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") к хосту, чтобы организовать мониторируемые среды осмысленным образом.
   * Задать [Properties](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.") для хоста, чтобы автоматически добавить метаданные.
   * Изменить режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Подробнее см. [режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

     Недоступно, если включена опция мониторинга Virtual I/O Server.

   Установщик OneAgent через командную строку предоставляет больше вариантов для [настройки установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
8. Скопировать команду из текстового поля **Run the installer with root rights**.
9. Запустить установщик.  
   Вставить команду в терминал и выполнить её.

   * Нужны права root. Перед запуском от root скрипт нужно сделать исполняемым.
   * Использовать `su` или `sudo` для запуска установочного скрипта. Ввести следующую команду в каталоге, куда был загружен установочный скрипт.  
     `sudo /bin/sh Dynatrace-OneAgent-AIX-1.0.0.sh`

   Сводку изменений, внесённых установкой OneAgent в систему, см. в разделе [безопасность OneAgent на AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").
10. На AIX Dynatrace поддерживает deep-code мониторинг для приложений Java, Apache, WebLogic и Websphere. Для OneAgent версии 1.189+ он автоматизирован. Для более ранних версий нужно выполнить некоторую настройку на AIX, которую можно провести как для отдельных приложений, так и на уровне всей оболочки.

    Автоматическое внедрение deep-code мониторинга по умолчанию включено в Dynatrace версии 1.195+ для новых установок OneAgent 1.189+.

    Deep-code мониторинг можно включить после установки OneAgent и успешного подключения к Dynatrace. На странице **Hosts** найти нужный хост, перейти в **Host settings** > **Monitoring** и выбрать **Allow AIX kernel extension**.

## Установка на Virtual I/O Server (VIOS)

Использовать общие шаги установки для загрузки OneAgent, а затем, после того как установщик OneAgent окажется на машине VIOS, выполнить следующие команды.

1. Инициировать установку OEM и настроить среду.

   ```
   oem_setup_env
   ```
2. Войти в группу `system`.

   ```
   newgrp system
   ```
3. Установить OneAgent.

   * Параметр `--set-monitoring-mode=infra-only` включает Infrastructure Monitoring.
   * Параметр `--set-auto-injection-enabled=false` отключает автоматическое внедрение в процессы.

   ```
   /bin/sh Dynatrace-OneAgent.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
   ```
4. Вернуться к приглашению Virtual I/O Server.

   ```
   exit
   ```

## Ручное внедрение OneAgent

Если использовать унифицированный подход мониторинга не получается, OneAgent можно внедрить вручную.

Процессы, которым выданы особые привилегии через систему ролевого контроля доступа AIX (RBAC), не могут внедряться автоматически. Это защитный механизм операционной системы, ограничивающий запуск неизвестного кода с повышенными привилегиями. Например, веб-серверу Apache или IHS могла быть выдана привилегия `PV_NET_PORT`, чтобы позволить запускать сервер от имени пользователя без прав root, но при этом дать ему возможность привязываться к ограниченным портам вроде порта `80`. В этом случае любые библиотеки, настроенные на предзагрузку, включая OneAgent, будут молча проигнорированы. В таких случаях сработает только ручное внедрение OneAgent.

Ручное внедрение OneAgent

IBM Java 1.6 – 1.8

IBM/Apache HTTP Server

Добавь перед командой запуска приложения следующие команды:

```
export DT_HOME=/opt/dynatrace/oneagent



export LDR_PRELOAD64=$DT_HOME/agent/lib64/liboneagentproc.so



export LDR_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so
```

Переменная `DT_HOME` должна указывать на папку установки OneAgent. Если папка установки OneAgent была изменена, подстрой переменную `DT_HOME` соответствующим образом. 32-битную или 64-битную запись можно опустить, в зависимости от окружения.

Отредактируй файл `httpd.conf` и добавь следующие две строки в удобном месте:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Если вместо этого нужно оставить `httpd.conf` без изменений, те же директивы можно указать через командную строку:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID`, это ID [окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") Dynatrace, которое нужно взять из `dynatrace-env.sh` (находится в корневой папке установки OneAgent). Параметр `tenantUUID` представлен в скрипте как `DT_TENANT`.
* `tenantToken`, это [токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it."), который OneAgent использует для отправки данных Dynatrace. Его нужно взять из `dynatrace-env.sh` (или `ruxitagent.conf`, в зависимости от версии OneAgent), который находится в корневой папке установки OneAgent. Параметр `tenantToken` представлен в скрипте как `DT_TENANTTOKEN`.

  Не путай этот токен с API Dynatrace или PaaS-токенами. Эти токены здесь использовать нельзя.
* `communicationEndpoints` соответствует одному или нескольким HTTP-адресам, представляющим Servers Dynatrace или ActiveGate. Параметр `communicationEndpoints` представлен в скрипте как `DT_CONNECTION_POINT`. Например, `dynatrace-env.sh` (находится в корневой папке установки OneAgent) может содержать следующее:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  В этом случае параметр будет выглядеть так:

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## Готово!

Отлично, настройка завершена! Теперь можно осмотреться в новом окружении мониторинга.

Доступ к окружению мониторинга открывается через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").

![Arrived](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)

Arrived

Последний штрих: чтобы начать мониторинг процессов, их нужно перезапустить. Процессы можно перезапустить в любой момент, даже во время следующего планового периода обслуживания организации.