---
title: Наблюдаемость приложений через внедрение во время сборки контейнера
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/container-buildtime
scraped: 2026-05-12T11:52:45.250678
---

# Наблюдаемость приложений через внедрение во время сборки контейнера

# Наблюдаемость приложений через внедрение во время сборки контейнера

* Чтение: 5 мин
* Обновлено 17 октября 2025 г.

Внедрение модулей кода Dynatrace в контейнер во время процесса его сборки.

У этого метода инструментирования приложений есть ограничения при связывании рабочих нагрузок Kubernetes с отслеживаемыми контейнерами/процессами. Чтобы добиться корректных связей и сопоставления, рассмотрите возможность использования [автоматического внедрения только на уровне приложения](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Разверните Dynatrace Operator в режиме application monitoring в Kubernetes").

## Предварительные требования

* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").
* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей действия (scopes).").
* Требования к хранилищу:

  + ~325 МБ для glibc
  + ~290 МБ для musl
  + ~650 МБ для glibc и musl вместе
* Для архитектуры ARM убедитесь, что установлены `wget` и `unzip`.

Внедрение во время сборки контейнера и cgroup v2

Если внедрение во время сборки контейнера используется с [cgroup v2](https://kubernetes.io/docs/concepts/architecture/cgroups/), метрики `builtin:containers.*` отправляются в Dynatrace только при соблюдении всех следующих условий:

* Доступен **Kubernetes API** (см. [Предоставление роли viewer служебным учётным записям](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments#viewer "Упорядочивайте и фильтруйте отслеживаемые приложения, импортируя метки и аннотации из вашего окружения Kubernetes/OpenShift."))
* Под запускает **один контейнер**

## Развёртывание

Чтобы интегрировать OneAgent в образ приложения, выполните шаги ниже.

Kubernetes/OpenShift v4.0

OpenShift v3.11

ARM

1. Войдите в Docker, указав ID вашего окружения Dynatrace в качестве имени пользователя и токен доступа в качестве пароля.

   ```
   docker login -u <environmentID> -p <accessToken> <environmentURL>
   ```
2. Добавьте следующие строки кода в образ приложения после последней команды `FROM`:

   ```
   COPY --from=<environment>/linux/oneagent-codemodules:<technology> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   * `<technology>`, модуль кода OneAgent, необходимый для вашего приложения. Доступные варианты: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go` и `sdk`. Можно указать несколько модулей кода, разделённых дефисом (`-`), например `java-go`. Включение определённых опций поддержки технологий вместо поддержки всех технологий приводит к уменьшению размера пакета OneAgent.

Что делать, если мой образ Docker основан на Alpine Linux?

Dynatrace OneAgent поддерживает окружения на основе Alpine Linux.

```
COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые варианты здесь: `all`, `dotnet`, `php`, `java`, `apache`, `nginx`, `nodejs` и `go`.

3. Соберите образ вашего приложения.

   Соберите образ Docker из вашего Dockerfile, чтобы использовать его в вашем окружении Kubernetes.

   ```
   docker build -t yourapp .
   ```

Контейнеры вашего приложения можно отслеживать с помощью другого окружения Dynatrace.

Для OneAgent версии 1.139+, если у вас есть готовый образ приложения, в который вы уже добавили модули кода OneAgent для определённого окружения Dynatrace, можно настроить отправку данных OneAgent в другое окружение Dynatrace без пересборки образа приложения.  
Для этого необходимо обратиться к REST-эндпоинту вашего второго окружения Dynatrace. Не забудьте подставить соответствующие плейсхолдеры `<environmentID>` и `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

В ответ вы получите объект JSON, содержащий необходимую информацию, которую нужно передать в контейнер приложения в виде переменной окружения.  
Убедитесь, что переменные окружения контейнера приложения заданы, как описано ниже:

* `DT_TENANT`: равно `tenantUUID`
* `DT_TENANTTOKEN`: равно `tenantToken`
* `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённый точкой с запятой

4. Необязательно. Настройте сетевые зоны

Сетевые зоны можно настроить в виде переменной окружения:

* `DT_NETWORK_ZONE`: равно `your.network.zone`

Подробнее см. [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

5. Необязательно. Настройте адрес прокси

   Если вы используете окружение с прокси, необходимо задать переменную окружения `DT_PROXY` в контейнере приложения, чтобы передать учётные данные прокси в OneAgent.

   Для контейнеров на основе Alpine Linux может потребоваться обновить `wget`, поставляемый с образом Alpine, чтобы разрешить аутентификацию через прокси при загрузке OneAgent.

1. Определите переменные с необязательными значениями по умолчанию с помощью инструкций `ARG`, как показано ниже.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_PAAS_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"
   ```

   * Значения по умолчанию можно переопределить в `BuildConfig` OpenShift. Замените `<environmentID>` на ID вашего окружения Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL вашего сервера Dynatrace (`https://<YourDynatraceServerURL>/e/<environmentID>/api`). Замените `<token>` на PaaS-токен, упомянутый выше.
   * Поддержка технологий включается через параметры `include`. Допустимые варианты для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go` и `sdk`. Включение определённых опций поддержки технологий вместо поддержки всех технологий приводит к уменьшению размера пакета OneAgent.

   Что делать, если мой образ Docker основан на Alpine Linux?

   OneAgent поддерживает вариант `musl` для окружений на основе Alpine Linux. Допустимые варианты для `flavor=musl`: `all`, `java`, `apache`, `nginx` и `nodejs`.
2. Добавьте следующие команды в ваш текущий Dockerfile, чтобы интегрировать OneAgent и активировать инструментирование вашего приложения.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENV LD_PRELOAD="/opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so"
   ```

   Приведённые выше команды, использующие `wget` и `unzip`, могут завершиться ошибкой, если они не предоставляются базовым образом.
3. Соберите образ вашего приложения.

   В контексте OpenShift приведённый выше Dockerfile можно использовать для двоичных сборок следующим образом:

   ```
   oc new-build --binary --strategy=docker --allow-missing-images yourapp



   oc patch bc/yourapp --type=json --patch='[{"op":"remove","path":"/spec/strategy/dockerStrategy/from"}]'



   oc start-build yourapp --from-dir=. --follow
   ```

Контейнеры вашего приложения можно отслеживать с помощью другого окружения Dynatrace.

Для OneAgent версии 1.139+, если у вас есть готовый образ приложения, в который вы уже добавили модули кода OneAgent для определённого окружения Dynatrace, можно настроить отправку данных OneAgent в другое окружение Dynatrace без пересборки образа приложения.  
Для этого необходимо обратиться к REST-эндпоинту вашего второго окружения Dynatrace. Не забудьте подставить соответствующие плейсхолдеры `<environmentID>` и `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

В ответ вы получите объект JSON, содержащий необходимую информацию, которую нужно передать в контейнер приложения в виде переменной окружения.  
Убедитесь, что переменные окружения контейнера приложения заданы, как описано ниже:

* `DT_TENANT`: равно `tenantUUID`
* `DT_TENANTTOKEN`: равно `tenantToken`
* `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённый точкой с запятой

4. Необязательно. Настройте сетевые зоны

Сетевые зоны можно настроить в виде переменной окружения:

* `DT_NETWORK_ZONE`: равно `your.network.zone`

Подробнее см. [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

5. Необязательно. Настройте адрес прокси

   Если вы используете окружение с прокси, необходимо задать переменную окружения `DT_PROXY` в контейнере приложения, чтобы передать учётные данные прокси в OneAgent.

   Для контейнеров на основе Alpine Linux может потребоваться обновить `wget`, поставляемый с образом Alpine, чтобы разрешить аутентификацию через прокси при загрузке OneAgent.

1. Задайте следующие переменные времени сборки:

   * `$DT_API_URL` (URL API вашего окружения Dynatrace)
   * `$DT_PAAS_TOKEN` (PaaS-токен для загрузки модулей кода)
   * `$DT_ONEAGENT_TECHNOLOGY` (Загружаемый модуль, например `php`)
2. Добавьте следующие команды в Dockerfile:

   ```
   RUN mkdir -p /opt/dynatrace/oneagent && ARCHIVE=$(mktemp) && wget -O $ARCHIVE "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_PAAS_TOKEN&flavor=default&arch=arm&include=$DT_ONEAGENT_TECHNOLOGY" && unzip -o -d /opt/dynatrace/oneagent $ARCHIVE && rm -f $ARCHIVE



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

## Обновление

OneAgent необходимо обновлять вручную, пересобирая образ контейнера каждый раз, когда требуется новая версия модуля кода.

## Удаление

Чтобы удалить OneAgent из мониторинга приложений

Многоэтапные сборки образов Docker

Классическая интеграция

1. Удалите две строки кода из образа приложения.

   ```
   COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```
2. Пересоберите образ приложения.

   ```
   docker build -t yourapp .
   ```

1. Удалите следующие команды из вашего Dockerfile.

   ```
   ARG DT_API_URL="https://<environmentID>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



   CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
   ```
2. Пересоберите образ приложения.

   ```
   docker build -t yourapp .
   ```