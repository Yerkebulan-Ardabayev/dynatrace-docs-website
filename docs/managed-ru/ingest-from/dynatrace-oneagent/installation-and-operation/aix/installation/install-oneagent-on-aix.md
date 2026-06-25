---
title: Установка OneAgent на AIX
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix
scraped: 2026-05-12T11:10:53.804328
---

# Установка OneAgent на AIX

# Установка OneAgent на AIX

* Практическое руководство
* Чтение: 7 мин
* Обновлено 16 марта 2026 г.

На этой странице описано, как загрузить и установить Dynatrace OneAgent на AIX.

Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.

## Требования

### Разрешения

* Вам нужны разрешения [Download/install OneAgent](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Разрешения на основе ролей") для загрузки и установки OneAgent.
* Вам нужны права администратора на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если ваша внутренняя политика маршрутизации может препятствовать доступу программного обеспечения Dynatrace в Интернет).
* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.

### Ресурсы

* Ознакомьтесь с [требованиями к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/disk-space-requirements-for-oneagent-installation-and-update-on-aix "Узнайте о требованиях к дисковому пространству для установки OneAgent на AIX.").
* Вашему хосту требуется 200 МБ свободной памяти для выполнения установки и обновления OneAgent.
* Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").

### Ограничения

* Установка OneAgent не поддерживается на сетевых точках монтирования хранилищ, управляемых такими стандартами, как NFS или iSCSI.
* Поддержка [Log management and Analytics](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics) и [Log Monitoring Classic](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить Log Monitoring, какие сведения он может предоставить, и многое другое.") на хостах AIX ограничена:

  + обнаружение логов в модуле логов ограничено только пользовательскими источниками логов.

### Разрешите подключения через брандмауэр

Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.  
В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation**. Затем выберите платформу, на которую нужно установить OneAgent.
3. Вставьте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей.") в поле **Installer download token** или выберите **Generate token**, чтобы сгенерировать токен сейчас и автоматически вставить его в **Installer download token**. Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать далее.
4. В поле **Download OneAgent** нажмите **Copy**, чтобы скопировать команду `wget` в буфер обмена.
5. Войдите на ваш хост AIX, затем вставьте и выполните только что скопированную команду `wget`.

   * Команда `wget` не установлена на AIX по умолчанию. Установите её или используйте альтернативный способ загрузки OneAgent.
   * Если при загрузке OneAgent возникает ошибка, установите требуемый сертификат: скачайте файл корневого CA с [Comodo](https://support.comodo.com/index.php?/Knowledgebase/Article/View/854/75/root-addtrustexternalcaroot), затем добавьте содержимое CRT-файла в `/var/ssl/cert.pem`. Как вариант, можно пропустить проверку сертификата, добавив параметр `--no-check-certificate`.
   * Если вы планируете загружать OneAgent напрямую на сервер, учтите, что устаревшие или отсутствующие библиотеки (например, CA-сертификаты или OpenSSL) не позволят установщику выполнить загрузку. Мы используем зашифрованные подключения. OpenSSL необходим, чтобы `wget` мог получить доступ к серверу.
6. **Verify the signature**

   После завершения загрузки нажмите **Copy** в поле **Verify signature**, чтобы скопировать команду `wget` в буфер обмена, затем вставьте предоставленную команду в окно терминала и выполните её. Убедитесь, что ваша система обновлена, особенно SSL и связанные с ним библиотеки сертификатов.
7. Необязательно **Set customized options**

   * Включите мониторинг логического раздела [Virtual I/O Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix#vios-installation "Узнайте, как загрузить и установить Dynatrace OneAgent на AIX.").
   * Задайте [сетевую зону](/managed/manage/network-zones#deploy-network-zones "Узнайте, как работают сетевые зоны в Dynatrace.") для этого хоста.
   * Если ваше окружение сегментировано (например, на разработку и продакшен), рассмотрите возможность [организации хостов в группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.").
   * Переопределите автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя мониторируемого хоста."). Это полезно в крупных и динамичных окружениях, где заданные имена хостов могут быть неинтуитивными или часто меняться.
   * Примените [теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") к хосту, чтобы осмысленно организовать ваши мониторируемые окружения.
   * Задайте [Properties](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Узнайте, как назначать теги и задавать дополнительные свойства для мониторируемого хоста.") для хоста, чтобы автоматически добавлять метаданные.
   * Измените режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Дополнительные сведения см. в [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

     Этот режим недоступен, если включён параметр мониторинга Virtual I/O Server.

   Установщик командной строки OneAgent предоставляет больше параметров для [настройки установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки.").
8. Скопируйте команду из текстового поля **Run the installer with root rights**.
9. Запустите установщик.  
   Вставьте команду в терминал и выполните её.

   * Вам нужны права root. Перед запуском от имени root необходимо сделать скрипт исполняемым.
   * Используйте `su` или `sudo` для запуска скрипта установки. Введите следующую команду в каталоге, куда вы скачали скрипт установки.  
     `sudo /bin/sh Dynatrace-OneAgent-AIX-1.0.0.sh`

   Сводку изменений, внесённых в вашу систему при установке OneAgent, см. в [Безопасность OneAgent на AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе AIX.").
10. На AIX Dynatrace поддерживает глубокий мониторинг кода для приложений Java, Apache, WebLogic и Websphere. Для OneAgent версии 1.189+ это автоматизировано. Для более ранних версий необходимо выполнить некоторую настройку на AIX, что можно сделать как для отдельных приложений, так и в масштабе всей оболочки.

    Автоматическая инъекция глубокого мониторинга кода включена по умолчанию в Dynatrace версии 1.195+ для новых установок OneAgent 1.189+.

    Включить глубокий мониторинг кода можно после установки OneAgent и его успешного подключения к Dynatrace. На странице **Hosts** найдите ваш хост, перейдите в **Host settings** > **Monitoring** и выберите **Allow AIX kernel extension**.

## Установка на Virtual I/O Server (VIOS)

Используйте общие шаги установки для загрузки OneAgent, а затем, когда установщик OneAgent окажется на вашей машине VIOS, выполните следующие команды.

1. Запустите установку OEM и настройте окружение.

   ```
   oem_setup_env
   ```
2. Войдите в группу `system`.

   ```
   newgrp system
   ```
3. Установите OneAgent.

   * Параметр `--set-monitoring-mode=infra-only` включает Infrastructure Monitoring.
   * Параметр `--set-auto-injection-enabled=false` отключает автоматическую инъекцию в процессы.

   ```
   /bin/sh Dynatrace-OneAgent.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
   ```
4. Вернитесь к приглашению Virtual I/O Server.

   ```
   exit
   ```

## Ручная инъекция OneAgent

Если вы не можете использовать унифицированный подход к мониторингу, OneAgent можно внедрить вручную.

Для процессов, которым предоставлены особые привилегии с помощью системы управления доступом на основе ролей (RBAC) в AIX, автоматическая инъекция невозможна. Это защитный механизм операционной системы, ограничивающий запуск неизвестного кода с повышенными привилегиями. Например, веб-серверу Apache или IHS может быть предоставлена привилегия `PV_NET_PORT`, чтобы разрешить запуск сервера от имени пользователя без прав root, но при этом позволить ему привязываться к ограниченным портам, таким как порт `80`. В этом случае любые библиотеки, настроенные для предзагрузки, включая OneAgent, будут молча проигнорированы. В таких случаях работает только ручная инъекция OneAgent.

Ручная инъекция OneAgent

IBM Java 1.6 – 1.8

IBM/Apache HTTP Server

Предварите команду вашего приложения следующими командами:

```
export DT_HOME=/opt/dynatrace/oneagent



export LDR_PRELOAD64=$DT_HOME/agent/lib64/liboneagentproc.so



export LDR_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so
```

Переменная `DT_HOME` должна указывать на папку установки OneAgent. Если вы изменили каталог установки OneAgent, скорректируйте переменную `DT_HOME` соответствующим образом. Запись для 32-бит или 64-бит можно опустить в зависимости от вашего окружения.

Отредактируйте ваш `httpd.conf` и добавьте следующие две строки в выбранном вами месте:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Кроме того, если вы предпочитаете оставить `httpd.conf` без изменений, те же директивы можно указать с помощью командной строки:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/current/aix-ppc-64/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID` является идентификатором вашего [окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Разберитесь и научитесь работать с окружениями мониторинга.") Dynatrace, который следует взять из `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent). Параметр `tenantUUID` представлен в скрипте как `DT_TENANT`.
* `tenantToken` является [токеном](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое tenant-токен и как его изменить."), который OneAgent использует для отправки данных в Dynatrace. Его следует взять из `dynatrace-env.sh` (или `ruxitagent.conf`, в зависимости от версии вашего OneAgent), который находится в корневом каталоге установки OneAgent. Параметр `tenantToken` представлен в скрипте как `DT_TENANTTOKEN`.

  Этот токен не следует путать с токенами Dynatrace API или PaaS. Те токены здесь использовать нельзя.
* `communicationEndpoints` соответствует одному или нескольким HTTP-адресам, представляющим Dynatrace Server или ActiveGate. Параметр `communicationEndpoints` представлен в скрипте как `DT_CONNECTION_POINT`. Например, `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent) может содержать следующее:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  В этом случае параметр будет следующим

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## Вы на месте!

Отлично, настройка завершена! Теперь можно осмотреться в своём новом окружении мониторинга.

Доступ к окружению мониторинга можно получить через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними.").

![Вы на месте](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)

Вы на месте

И последнее: чтобы мониторить ваши процессы, их нужно перезапустить. Перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации.