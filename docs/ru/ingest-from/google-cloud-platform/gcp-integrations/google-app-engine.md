---
title: Monitor Google App Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine
scraped: 2026-02-06T16:24:08.961664
---

# Мониторинг Google App Engine

# Мониторинг Google App Engine

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 2 мин
* Опубликовано 23 июн. 2020 г.

Стандартная среда Google App Engine поддерживает приложения на Java, .NET, Node.js, Golang и других платформах. Для пользовательских образов Docker Google App Engine предоставляет поддержку гибкой среды.

## Предварительные требования

* Создайте [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Интеграция OneAgent в образ приложения

Чтобы интегрировать OneAgent в развёртывание контейнера с Dockerfile в гибкой среде Google App Engine и активировать инструментацию приложения, добавьте приведённые ниже команды в текущий Dockerfile, указав собственные значения для аргументов `DT_API_URL`, `DT_API_TOKEN` и `DT_ONEAGENT_OPTIONS`.

* `<environmentID>` следует заменить идентификатором среды Dynatrace. При использовании Dynatrace Managed необходимо указать URL сервера Dynatrace (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).
* `<token>` следует заменить токеном PaaS, указанным в предварительных требованиях.
* Поддержка технологий активируется с помощью параметров `include`. Допустимые значения для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` и `go`. Указание конкретных параметров поддержки технологий вместо поддержки всех вариантов приводит к уменьшению размера пакета OneAgent. Для сред на основе Alpine Linux Dynatrace OneAgent поддерживает вариант `musl`. Допустимые значения для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.

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



CMD [ "executable", "param1", "param2" ] # команда запуска вашего приложения, например Java
```

Команды `wget` и `unzip`, приведённые выше, могут завершиться с ошибкой, если они не входят в состав базового образа.

## Развёртывание образа приложения

После интеграции OneAgent в Dockerfile приложения выполните его развёртывание. Для этого перейдите в директорию приложения, содержащую файлы `Dockerfile` и `app.yaml`, и выполните следующую команду в CLI `gcloud`.

```
gcloud app deploy
```

Google App Engine самостоятельно выполнит сборку образа Docker на основе предоставленного Dockerfile и тем самым обеспечит загрузку и установку кодовых модулей OneAgent в образ приложения.

## Обновление OneAgent

Каждый раз, когда требуется обновить версию Dynatrace OneAgent, необходимо повторно развернуть приложение. Google App Engine пересоберёт образ приложения с последними компонентами OneAgent. Все новые контейнеры, запущенные из этого образа, будут отслеживаться с использованием последней версии OneAgent.

## Связанные темы

* [Настройка Dynatrace на Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
