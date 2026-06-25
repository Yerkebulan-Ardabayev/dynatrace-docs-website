---
title: Установка OneAgent на Solaris
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris
scraped: 2026-05-12T11:09:49.455973
---

# Установка OneAgent на Solaris

# Установка OneAgent на Solaris

* Чтение: 7 мин
* Обновлено 22 января 2026 г.

На этой странице описано, как загрузить и установить Dynatrace OneAgent на Solaris.

Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.

## Требования

### Разрешения

* Вам нужны права администратора на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если ваша внутренняя политика маршрутизации может препятствовать доступу программного обеспечения Dynatrace в Интернет).
* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.

### Ресурсы

Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").

### Ограничения

* Установка OneAgent не поддерживается на сетевых точках монтирования хранилищ, управляемых такими стандартами, как NFS или iSCSI.
* Режим [Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.") не поддерживается на хостах Solaris.

### Разрешите подключения через брандмауэр

Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.  
В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **Solaris**.
3. Выберите архитектуру ЦП вашего окружения.
4. Укажите [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей."). Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Если у вас нет PaaS-токена, его можно сгенерировать прямо в интерфейсе. Токен автоматически добавляется к команде загрузки, которую вы будете использовать далее.
5. Нажмите **Copy**, чтобы скопировать команду `wget`.
6. Войдите на ваш хост Solaris и выполните команду `wget`.

   * Команда `wget` не установлена на Solaris по умолчанию. Установите её или используйте альтернативный способ загрузки OneAgent.
7. Создайте на локальной системе папку для OneAgent (например, `/opt/dynatrace/oneagent`) и распакуйте zip-архив в эту папку.

   В отличие от других платформ, для установки OneAgent на Solaris не требуется доступ root. OneAgent можно установить в любой каталог.

   * Поскольку все мониторируемые приложения должны иметь возможность читать библиотеку, убедитесь, что разрешения это позволяют.

     + Предоставьте глобальные разрешения на чтение для `/opt/dynatrace/oneagent`
     + Предоставьте глобальные разрешения на запись для `/opt/dynatrace/oneagent/logs`
   * Обязательно правильно указывайте эту папку на последующих шагах развёртывания.
8. На Solaris Dynatrace поддерживает только приложения Java и Apache HTTP Server, поэтому вам нужно решить, какие приложения мониторить. Это можно сделать как для одного приложения, так и в рамках всей оболочки. Следуйте соответствующим инструкциям ниже.

   Мониторинг одного приложения

   Чтобы мониторить одно приложение, выполните вашу команду, предварив её следующими командами.

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD
   ```

   Переменная `DT_HOME` указывает на папку установки OneAgent. Запись для 32-бит или 64-бит можно опустить в зависимости от вашего окружения.

   Настройка WebSphere Application Server через административную консоль

   Унифицированный подход одинаково хорошо работает и для WebSphere, однако настроить WebSphere можно и через административную консоль. Это работает для OneAgent v1.141 и выше.

   1. Запустите сервер WebSphere через интерфейс WebSphere или командную строку. Например: `/opt/ibm/WebSphere<version>/AppServer/bin/sh startServer.sh server1`
   2. Откройте административную консоль через интерфейс WebSphere или введите URL в веб-браузере. Например:`http://localhost:9060/ibm/console`. При удалённом доступе к серверу укажите имя хоста машины вместо `localhost`.
   3. Введите ваш идентификатор пользователя и пароль, затем войдите в систему.
   4. Перейдите в **Server** > **Application servers** > `[yourprofilename]`> **Java and Process Management** > **Process Definition** > **Environment Entries** > **New**.
   5. Добавьте в список 3 записи.

      ```
      DT_HOME=/opt/dynatrace/oneagent



      LD_PRELOAD_64=/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so



      LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
      ```

      Запись для 32-бит или 64-бит можно опустить в зависимости от вашего окружения. Переменная `DT_HOME` должна указывать на папку установки OneAgent.
   6. Примените изменения и сохраните конфигурацию.

   Настройка Oracle WebLogic через скрипт запуска

   Чтобы мониторить Oracle WebLogic, нужно добавить следующие строки в скрипт запуска WebLogic (`startWebLogic.sh`)

   ```
   # Monitor WebLogic with Dynatrace OneAgent



   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD



   # WebLogic checks and startup, this is part of your script, add the 3 lines prior to this.



   echo "starting weblogic with Java version:"



   ${JAVA_HOME}/bin/java ${JAVA_VM} -version



   if [ "${WLS_REDIRECT_LOG}" = "" ] ; then



   echo "Starting WLS with line:"



   echo "${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS} ${SERVER_CLASS}"



   ${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS} ${SERVER_CLASS}



   else



   echo "Redirecting output from WLS window to ${WLS_REDIRECT_LOG}"



   ${JAVA_HOME}/bin/java ${JAVA_VM} ${MEM_ARGS} ${JAVA_OPTIONS} -Dweblogic.Name=${SERVER_NAME}



   -Djava.security.policy=${WL_HOME}/server/lib/weblogic.policy ${PROXY_SETTINGS}



   ${SERVER_CLASS} 2>&1 >"${WLS_REDIRECT_LOG}"



   fi
   ```

   Запись для 32-бит или 64-бит можно опустить в зависимости от вашего окружения. Переменная `DT_HOME` должна указывать на папку установки OneAgent.

   Мониторинг каждого сервиса Java и Apache HTTP в вашем контексте выполнения

   OneAgent можно настроить на мониторинг каждого приложения в текущем контексте приложений. Для этого добавьте следующие строки в скрипт запуска приложения, которое вы хотите мониторить. Убедитесь, что они выполняются до самого приложения. Не делайте это в масштабе всей системы или для пользователей, входящих в систему.

   OneAgent v1.141 и выше

   OneAgent с v1.137 по v1.139

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so



   export LD_PRELOAD_64



   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so



   export LD_PRELOAD
   ```

   ```
   DT_HOME=/opt/dynatrace/oneagent



   export DT_HOME



   . $DT_HOME/dynatrace-agent64.sh



   . $DT_HOME/dynatrace-agent32.sh
   ```

   `LD_PRELOAD` не переносится в вызовы `sudo` или `su`. Более того, вызов `sudo` в контексте выполнения, где задан `LD_PRELOAD`, приведёт к сообщению об ошибке о том, что библиотека находится в небезопасном расположении. Это не имеет негативных последствий. Это сообщение можно игнорировать.

Если вы используете административный сервер WebLogic для перезапуска управляемых узлов на Solaris, см. [Устранение неполадок при установке OneAgent на Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris#weblogic-admin "Узнайте, как решать проблемы, связанные с установкой OneAgent на Solaris."), чтобы узнать, как изменить скрипт запуска.

## Версии OneAgent старше v1.137 и запасной вариант

Если ваш OneAgent старше v1.137 или если у вас возникают проблемы с унифицированным подходом к мониторингу, OneAgent можно внедрить вручную.

Ручное внедрение OneAgent

Стандартные Java-приложения

Apache HTTP Server

Измените командную строку вашего Java-приложения:

```
DT_HOME=/opt/dynatrace/oneagent



. $DT_HOME/dynatrace-java-env.sh 64



java $JAVA_OPTS <MainClass>
```

Убедитесь, что вы включили переменную `$JAVA_OPTS` в свою команду. Для 32-битных процессов Java опустите параметр `64`.

Для настройки Dynatrace на мониторинг Apache HTTP server, работающего на Solaris, требуются следующие шаги:

Отредактируйте ваш `httpd.conf` и добавьте следующие две строки в выбранном вами месте:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so



OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

Кроме того, если вы предпочитаете оставить `httpd.conf` без изменений, те же директивы можно указать с помощью командной строки:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so"



-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"



-k start
```

* `tenantUUID` является идентификатором вашего окружения Dynatrace, который следует взять из `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent). Параметр `tenantUUID` представлен в скрипте как `DT_TENANT`.
* `tenantToken` является токеном, который OneAgent использует для подключения к Dynatrace Server. Его следует взять из `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent). Параметр `tenantToken` представлен в скрипте как `DT_TENANTTOKEN`.

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