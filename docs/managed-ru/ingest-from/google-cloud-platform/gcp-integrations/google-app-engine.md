---
title: Мониторинг Google App Engine
source: https://docs.dynatrace.com/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine
scraped: 2026-05-12T11:22:56.656451
---

# Мониторинг Google App Engine

# Мониторинг Google App Engine

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 июня 2020 г.

Стандартный тип окружения Google App Engine поддерживает приложения, работающие на Java, .NET, Node.js, Golang и других технологиях. Для собственных образов Docker Google App Engine предоставляет поддержку гибкого окружения (flexible environment).

## Предварительные условия

* Создайте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей действия (scopes).").
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Интеграция OneAgent в образ приложения

Чтобы интегрировать OneAgent в развёртывание контейнера с Dockerfile в гибком окружении Google App Engine и активировать инструментирование приложения, добавьте приведённые ниже команды в текущий Dockerfile, указав собственные значения для аргументов `DT_API_URL`, `DT_API_TOKEN` и `DT_ONEAGENT_OPTIONS`.

* `<environmentID>` нужно заменить идентификатором вашей среды Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL вашего Dynatrace Server (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).
* `<token>` нужно заменить PaaS-токеном, указанным в предварительных условиях.
* Поддержка технологий включается через параметры `include`. Допустимые значения для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` и `go`. Подключение отдельных опций поддержки технологий вместо поддержки всех технологий уменьшает размер пакета OneAgent. Для окружений на базе Alpine Linux Dynatrace OneAgent поддерживает flavor `musl`. Допустимые значения для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.

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

Приведённые выше команды `wget` и `unzip` могут не сработать, если они не предоставляются базовым образом.

## Развёртывание образа приложения

После интеграции OneAgent в Docker-файл приложения разверните приложение. Для этого перейдите в каталог приложения, содержащий файлы `Dockerfile` и `app.yaml`, и выполните следующую команду в `gcloud` CLI.

```
gcloud app deploy
```

Google App Engine сам соберёт образ Docker на основе предоставленного Docker-файла и тем самым загрузит и установит code-modules OneAgent в образ приложения.

## Обновление OneAgent

Каждый раз, когда вы хотите обновить версию Dynatrace OneAgent, необходимо повторно развернуть приложение. После этого Google App Engine пересобирает образ приложения с новейшими компонентами OneAgent. Любые контейнеры, заново запущенные из этого образа приложения, затем отслеживаются с новейшей версией OneAgent.

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/managed/ingest-from/google-cloud-platform "Мониторинг Google Cloud с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в разных операционных системах и на разных платформах.")