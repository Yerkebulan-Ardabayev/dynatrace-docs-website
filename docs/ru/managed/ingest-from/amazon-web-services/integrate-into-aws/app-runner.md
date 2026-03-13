---
title: Monitor AWS App Runner
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner
scraped: 2026-03-06T21:17:49.528383
---

# Мониторинг AWS App Runner

# Мониторинг AWS App Runner

* Classic
* How-to guide
* Время чтения: 3 мин
* Опубликовано 16 января 2023 г.

Для развёртывания OneAgent на App Runner ознакомьтесь с приведёнными ниже инструкциями.

## Предварительные требования

* [Создайте API-токен](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") в вашей среде Dynatrace и включите следующие разрешения:

  + **Access problem and event feed, metrics, and topology** (`DataExport`) (API v1)
  + **PaaS integration - Installer download** (`InstallerDownload`)
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Интеграция OneAgent в образ приложения

### Внедрение на этапе сборки (EKS, ECS и App Runner)

Если вы используете ECS, EKS и App Runner, вы можете использовать внедрение на этапе сборки для встраивания OneAgent в образ контейнера.

Многоэтапная сборка Docker-образов

Классическая интеграция

Для использования этого варианта вам потребуется:

* Docker версии 17.05+
* OneAgent версии 1.155+

1. Войдите в Docker, используя ID вашей среды Dynatrace в качестве имени пользователя и PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Добавьте две дополнительные строки кода в образ приложения после последней команды `FROM`:

   ```
   COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

* Замените `<your-environment-url>` URL-адресом или IP-адресом вашей среды или ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    Если вы используете собственный ActiveGate среды, используйте формат `<ip-address>:9999` или `<hostname>:9999`.
* Замените `<technology>` кодовым модулем, необходимым для вашего приложения. Допустимые значения: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `sdk` и `go`. Вы можете указать несколько кодовых модулей через дефис (`-`), например `java-go`. Указание конкретных технологий вместо поддержки всех технологий приводит к уменьшению размера пакета OneAgent.

Что если мой Docker-образ основан на Alpine Linux?

Dynatrace OneAgent поддерживает среды на базе Alpine Linux. Используйте следующий синтаксис:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые значения: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.

3. Соберите образ приложения.

   Соберите Docker-образ из вашего dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете мониторить контейнеры приложений с помощью другой среды Dynatrace. Для этого ознакомьтесь с инструкциями ниже:

   Для OneAgent версии 1.139+, если у вас есть существующий образ приложения, в который вы уже добавили кодовые модули OneAgent для определённой среды Dynatrace, вы можете настроить отправку данных OneAgent в другую среду Dynatrace без пересборки образа приложения.

   Для этого необходимо выполнить вызов к REST-эндпоинту вашей второй среды Dynatrace. Убедитесь, что вы заменили соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий необходимую информацию, которую нужно передать в качестве переменной окружения контейнеру приложения. Убедитесь, что вы установили переменные окружения контейнера приложения, как описано ниже:

   * `DT_TENANT`: соответствует `tenantUUID`
   * `DT_TENANTTOKEN`: соответствует `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённый точкой с запятой

1. Добавьте следующие команды в ваш текущий Dockerfile для интеграции OneAgent и активации инструментирования приложения. Определите переменные с необязательными значениями по умолчанию с помощью инструкций `ARG`.

   ```
   ARG DT_API_URL="https://<your-environment-id>.live.dynatrace.com/api"



   ARG DT_API_TOKEN="<your-paas-token>"



   ARG DT_ONEAGENT_OPTIONS="flavor=default&include=<technology1>&include=<technology2>"



   ENV DT_HOME="/opt/dynatrace/oneagent"



   RUN mkdir -p "$DT_HOME" && \



   wget -O "$DT_HOME/oneagent.zip" "$DT_API_URL/v1/deployment/installer/agent/unix/paas/latest?Api-Token=$DT_API_TOKEN&$DT_ONEAGENT_OPTIONS" && \



   unzip -d "$DT_HOME" "$DT_HOME/oneagent.zip" && \



   rm "$DT_HOME/oneagent.zip"



   ENTRYPOINT [ "/opt/dynatrace/oneagent/dynatrace-agent64.sh" ]



   CMD [ "executable", "param1", "param2" ] # the command of your application, for example, Java
   ```

   * Указанные выше команды, использующие `wget` и `unzip`, могут завершиться ошибкой, если они не предоставлены базовым образом.
   * Замените `<your-environment-id>` идентификатором вашей среды Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL кластера Dynatrace (`https://<YourDynatraceServerURL>/e/<your-environment-id>/api`).
   * Замените `<your-paas-token>` вашим PaaS-токеном.
   * `DT_ONEAGENT_OPTIONS` — это вариант сборки (допустимые значения: `default` или `musl` для образов Alpine) и технология (кодовый модуль).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.

   **Что если мой Docker-образ основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает вариант `musl` для сред на базе Alpine Linux. Допустимые значения для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.
2. Соберите образ приложения.

   Соберите Docker-образ из вашего dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете мониторить контейнеры приложений с помощью другой среды Dynatrace. Для этого ознакомьтесь с инструкциями ниже:

   Для OneAgent версии 1.139+, если у вас есть существующий образ приложения, в который вы уже добавили кодовые модули OneAgent для определённой среды Dynatrace, вы можете настроить отправку данных OneAgent в другую среду Dynatrace без пересборки образа приложения.

   Для этого необходимо выполнить вызов к REST-эндпоинту вашей второй среды Dynatrace. Убедитесь, что вы заменили соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий необходимую информацию, которую нужно передать в качестве переменной окружения контейнеру приложения. Убедитесь, что вы установили переменные окружения контейнера приложения, как описано ниже:

   * `DT_TENANT`: соответствует `tenantUUID`
   * `DT_TENANTTOKEN`: соответствует `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённый точкой с запятой

### Настройка сетевых зон (необязательно)

Вы можете настроить сетевые зоны в качестве переменной окружения:

* `DT_NETWORK_ZONE`: соответствует `your.network.zone`

Подробнее см. [сетевые зоны](/docs/manage/network-zones "Find out how network zones work in Dynatrace.").

## Потребление мониторинга

Для AWS App Runner потребление мониторинга основано на хост-единицах. Подробнее см. [Мониторинг приложений и инфраструктуры (хост-единицы)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## Устранение неполадок

* [Проблемы интеграции OneAgent в образ приложения](https://dt-url.net/yu23mli)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
