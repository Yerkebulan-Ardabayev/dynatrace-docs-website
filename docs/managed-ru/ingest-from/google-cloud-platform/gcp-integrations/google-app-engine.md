---
title: Мониторинг Google App Engine
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine
scraped: 2026-03-06T21:17:51.187037
---

* 2 минуты на чтение

Стандартная среда Google App Engine поддерживает приложения, работающие на Java, .NET, Node.js, Golang и других языках. Для пользовательских образов Docker Google App Engine предоставляет поддержку гибкой среды.

## Предварительные требования

* Создайте токен PaaS.
* Ознакомьтесь со списком поддерживаемых приложений и версий.

## Интеграция OneAgent в образ приложения

Чтобы интегрировать OneAgent в контейнерное развёртывание с Dockerfile в гибкой среде Google App Engine и активировать инструментирование приложения, добавьте приведённые ниже команды в текущий Dockerfile, указав собственные значения для аргументов `DT_API_URL`, `DT_API_TOKEN` и `DT_ONEAGENT_OPTIONS`.

* `<environmentID>` следует заменить на идентификатор среды Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL-адрес сервера Dynatrace (`https://<YourDynatraceServerURL>/e/<environmentID>/api`).
* `<token>` следует заменить на токен PaaS, указанный в предварительных требованиях.
* Поддержка технологий включается с помощью параметров `include`. Допустимые параметры для `flavor=default`: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php` и `go`. Включение конкретных параметров поддержки технологий, а не поддержки всех технологий, даёт меньший пакет OneAgent. Для сред на основе Alpine Linux Dynatrace OneAgent поддерживает вариант `musl`. Допустимые параметры для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.

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


CMD [ "executable", "param1", "param2" ] # команда вашего приложения, например Java
```

Команды `wget` и `unzip`, приведённые выше, могут завершиться ошибкой, если они не предоставляются базовым образом.

## Развёртывание образа приложения

После интеграции OneAgent в Dockerfile приложения выполните развёртывание приложения. Для этого перейдите в каталог приложения, содержащий файлы `Dockerfile` и `app.yaml`, и выполните следующую команду в CLI `gcloud`.

```
gcloud app deploy
```

Google App Engine позаботится о сборке образа Docker на основе предоставленного Dockerfile и, соответственно, о загрузке и установке кодовых модулей OneAgent в образ приложения.

## Обновление OneAgent

Каждый раз, когда требуется обновить версию Dynatrace OneAgent, необходимо повторно развернуть приложение. Google App Engine пересоберёт образ приложения с последними компонентами OneAgent. Все новые контейнеры, запущенные из этого образа, будут отслеживаться с последней версией OneAgent.

## Связанные темы

* Настройка Dynatrace в Google Cloud
* Матрица поддержки платформ и возможностей OneAgent
