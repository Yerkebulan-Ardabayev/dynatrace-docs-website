---
title: Установка OneAgent на Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris
scraped: 2026-03-06T21:20:16.604221
---

На этой странице описывается, как загрузить и установить Dynatrace OneAgent на Solaris.

Для начала войдите в свою среду Dynatrace SaaS через веб-сайт [Dynatrace.com](https://www.dynatrace.com), используя учётные данные, предоставленные при регистрации. Затем перейдите к описанным ниже шагам установки.

## Требования

### Разрешения

* Вам необходимы права администратора на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если внутренняя политика маршрутизации может помешать программному обеспечению Dynatrace получить доступ к Интернету).
* Вам необходимы разрешения и учётные данные для перезапуска всех сервисов приложений.

### Ресурсы

Все хосты, подлежащие мониторингу, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace и настроек сети и безопасности вы можете выбрать прямой доступ к кластеру Dynatrace или настроить ActiveGate.

### Ограничения

* Установка OneAgent не поддерживается на сетевых точках монтирования, управляемых стандартами NFS или iSCSI.
* Режим Infrastructure Monitoring не поддерживается на хостах Solaris.

### Разрешение подключений через брандмауэр

Убедитесь, что настройки брандмауэра разрешают обмен данными с Dynatrace.
В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые необходимо добавить в список разрешённых, указаны на странице установки OneAgent.**

## Установка

1. В Dynatrace Hub выберите **OneAgent**.
2. Выберите **Set up** > **Solaris**.
3. Выберите архитектуру процессора вашей среды.
4. Укажите [PaaS-токен](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия."). Этот токен необходим для загрузки установщика OneAgent из вашей среды. Если у вас нет PaaS-токена, вы можете сгенерировать его прямо в интерфейсе. Токен автоматически добавляется к команде загрузки, которую вы будете использовать позже.
5. Нажмите **Copy**, чтобы скопировать команду `wget`.
6. Войдите на хост Solaris и выполните команду `wget`.

   * Команда `wget` не установлена на Solaris по умолчанию. Установите её или используйте альтернативный способ загрузки OneAgent.
7. Создайте папку в локальной системе для OneAgent (например, `/opt/dynatrace/oneagent`) и распакуйте zip-архив в эту папку.

   В отличие от других платформ, для установки OneAgent на Solaris не требуется доступ root. OneAgent можно установить в любой каталог.

   * Поскольку все контролируемые приложения должны иметь возможность читать библиотеку, убедитесь, что разрешения это позволяют.

     + Предоставьте глобальные разрешения на чтение для `/opt/dynatrace/oneagent`
     + Предоставьте глобальные разрешения на запись для `/opt/dynatrace/oneagent/logs`
   * Обязательно правильно указывайте папку в последующих шагах развёртывания.
8. На Solaris Dynatrace поддерживает только приложения Java и Apache HTTP Server, поэтому вам нужно решить, какие приложения мониторить. Вы можете сделать это для одного приложения или для всей оболочки. Следуйте соответствующим инструкциям ниже.

   Мониторинг одного приложения

   Для мониторинга одного приложения выполните команду, добавив перед ней следующие команды.

   ```
   DT_HOME=/opt/dynatrace/oneagent


   export DT_HOME


   LD_PRELOAD_64=$DT_HOME/agent/lib64/liboneagentproc.so


   export LD_PRELOAD_64


   LD_PRELOAD=$DT_HOME/agent/lib/liboneagentproc.so


   export LD_PRELOAD
   ```

   Переменная `DT_HOME` указывает на папку установки OneAgent. Вы можете опустить запись для 32-битной или 64-битной версии в зависимости от вашей среды.

   Настройка WebSphere Application Server через административную консоль

   Унифицированный подход работает и для WebSphere, однако вы можете настроить WebSphere через административную консоль. Это работает для OneAgent версии v1.141 и выше.

   1. Запустите сервер WebSphere через интерфейс WebSphere или командную строку. Например: `/opt/ibm/WebSphere<version>/AppServer/bin/sh startServer.sh server1`
   2. Откройте административную консоль через интерфейс WebSphere или введите URL в веб-браузере. Например: `http://localhost:9060/ibm/console`. При удалённом доступе к серверу укажите имя хоста машины вместо `localhost`.
   3. Введите свой идентификатор пользователя и пароль, а затем войдите в систему.
   4. Перейдите в **Server** > **Application servers** > `[yourprofilename]` > **Java and Process Management** > **Process Definition** > **Environment Entries** > **New**.
   5. Добавьте 3 записи в список.

      ```
      DT_HOME=/opt/dynatrace/oneagent


      LD_PRELOAD_64=/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so


      LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
      ```

      Вы можете опустить запись для 32-битной или 64-битной версии в зависимости от вашей среды. Переменная `DT_HOME` должна указывать на папку установки OneAgent.
   6. Примените изменения и сохраните конфигурацию.

   Настройка Oracle WebLogic через скрипт запуска

   Для мониторинга Oracle WebLogic необходимо добавить следующие строки в скрипт запуска WebLogic (`startWebLogic.sh`)

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

   Вы можете опустить запись для 32-битной или 64-битной версии в зависимости от вашей среды. Переменная `DT_HOME` должна указывать на папку установки OneAgent.

   Мониторинг каждого сервиса Java и Apache HTTP в вашем контексте выполнения

   Вы можете настроить OneAgent для мониторинга каждого приложения в текущем контексте приложения. Для этого добавьте следующие строки в скрипт запуска приложения, которое вы хотите мониторить. Убедитесь, что они выполняются перед самим приложением. Не следует делать это на уровне всей системы или для пользователей при входе.

   OneAgent v1.141 и выше

   OneAgent v1.137 — v1.139

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

   `LD_PRELOAD` не передаётся в вызовы `sudo` или `su`. Кроме того, вызов `sudo` в контексте выполнения с установленной переменной `LD_PRELOAD` приведёт к сообщению об ошибке, что библиотека находится в небезопасном расположении. Это не имеет негативного влияния. Это сообщение можно игнорировать.

Если вы используете административный сервер WebLogic для перезапуска управляемых узлов на Solaris, см. раздел [Устранение неполадок установки OneAgent на Solaris](troubleshoot-oneagent-installation-on-solaris.md#weblogic-admin "Узнайте, как решать проблемы, связанные с установкой OneAgent на Solaris."), чтобы узнать, как изменить скрипт запуска.

## Версии OneAgent старше v1.137 и резервный вариант

Если ваш OneAgent старше v1.137 или у вас возникли проблемы с унифицированным подходом к мониторингу, вы можете внедрить OneAgent вручную.

Ручное внедрение OneAgent

Универсальные Java-приложения

Apache HTTP Server

Измените командную строку вашего Java-приложения:

```
DT_HOME=/opt/dynatrace/oneagent


. $DT_HOME/dynatrace-java-env.sh 64


java $JAVA_OPTS <MainClass>
```

Убедитесь, что вы включили переменную `$JAVA_OPTS` в свою команду. Для 32-битных Java-процессов опустите параметр `64`.

Для настройки мониторинга Apache HTTP Server, работающего на Solaris, в Dynatrace необходимо выполнить следующие шаги:

Отредактируйте ваш `httpd.conf` и добавьте следующие две строки в любое место по вашему выбору:

```
LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so


OneAgentConfig tenant=<tenant-id>,tenantToken=<tenant-token>,server=https://<server-url>/communication
```

В качестве альтернативы, если вы предпочитаете оставить `httpd.conf` без изменений, вы можете указать те же директивы через командную строку:

```
apachectl -c "LoadModule oneagent_module /opt/dynatrace/oneagent/agent/bin/solaris-<arch>-<bitness>/liboneagentloader.so"


-c "OneAgentConfig tenant=<tenantUUID>,tenantToken=<tenant-token>,server=<communicationEndpoints>"


-k start
```

* `tenantUUID` — это идентификатор среды Dynatrace, который следует взять из `dynatrace-env.sh` (находится в корневой директории установки OneAgent). Параметр `tenantUUID` представлен в скрипте как `DT_TENANT`.
* `tenantToken` — это токен, который OneAgent использует для подключения к Dynatrace Server. Его следует взять из `dynatrace-env.sh` (находится в корневой директории установки OneAgent). Параметр `tenantToken` представлен в скрипте как `DT_TENANTTOKEN`.

  Этот токен не следует путать с API-токенами или PaaS-токенами Dynatrace. Эти токены здесь использовать нельзя.
* `communicationEndpoints` соответствует одному или нескольким HTTP-адресам, представляющим серверы Dynatrace или ActiveGate. Параметр `communicationEndpoints` представлен в скрипте как `DT_CONNECTION_POINT`. Например, `dynatrace-env.sh` (находится в корневой директории установки OneAgent) может содержать следующее:

  ```
  export DT_CONNECTION_POINT="https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication"
  ```

  В этом случае параметр будет

  ```
  server=https://x1.live.dynatrace.com/communication;https://x2.live.dynatrace.com/communication;https://x3.live.dynatrace.com/communication
  ```

## Готово!

Отлично, настройка завершена! Теперь вы можете ознакомиться с вашей новой средой мониторинга.

Вы можете получить доступ к среде мониторинга в любое время, перейдя на веб-сайт Dynatrace и выбрав **Login** в правом верхнем углу.

Последнее замечание: для мониторинга ваших процессов необходимо их перезапустить. В любой момент вы можете проверить, какие процессы не мониторятся и требуют перезапуска. Просто перейдите в **Deployment Status**, переключитесь на вкладку **All hosts** или **Recently connected hosts** и разверните интересующий вас хост.
