---
title: Мониторинг AWS App Runner
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner
scraped: 2026-02-06T16:23:23.536585
---

# Мониторинг AWS App Runner


* Практическое руководство
* Чтение: 3 мин
* Опубликовано 16 января 2023 г.

Для развёртывания OneAgent в App Runner следуйте приведённым ниже инструкциям.

## Предварительные требования

* [Создайте API-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Узнайте о концепции токена доступа и его областях действия.") в вашей среде Dynatrace и включите следующие разрешения:

  + **Access problem and event feed, metrics, and topology** (`DataExport`) (API v1)
  + **PaaS integration - Installer download** (`InstallerDownload`)
* Ознакомьтесь со списком [поддерживаемых приложений и версий](../../technology-support.md "Техническая информация о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Интеграция OneAgent в образ вашего приложения

### Внедрение на этапе сборки для EKS, ECS и App Runner

Если вы используете ECS, EKS и App Runner, вы можете использовать внедрение на этапе сборки для встраивания OneAgent в образ контейнера.

Многоэтапная сборка образов Docker

Классическая интеграция

Для использования этого варианта вам потребуется:

* Docker версии 17.05+
* OneAgent версии 1.155+

1. Войдите в Docker, используя идентификатор среды Dynatrace в качестве имени пользователя и ваш PaaS-токен в качестве пароля.

   ```
   docker login -u <your-environment-id> <your-environment-url>
   ```
2. Добавьте две дополнительные строки кода в образ приложения после последней команды `FROM`:

   ```
   COPY --from=<your-environment-url>/linux/oneagent-codemodules:<technology> / /


   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

* Замените `<your-environment-url>` на URL или IP-адрес вашей среды или вашего ActiveGate.

  + Dynatrace SaaS {your-environment-id}.live.dynatrace.com[1](#fn-1-1-def)
  + Dynatrace Managed {your-domain}/e/{your-environment-id}[1](#fn-1-1-def)

    1

    Если вы используете собственный ActiveGate среды, используйте формат `<ip-address>:9999` или `<hostname>:9999`.
* Замените `<technology>` на модуль кода, необходимый для вашего приложения. Допустимые варианты: `all`, `java`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `sdk` и `go`. Вы можете указать несколько модулей кода, разделённых дефисом (`-`), например `java-go`. Указание конкретных модулей технологий вместо поддержки всех технологий приводит к уменьшению размера пакета OneAgent.

Что делать, если мой образ Docker основан на Alpine Linux?

Dynatrace OneAgent поддерживает среды на основе Alpine Linux. Используйте следующий синтаксис:

```
COPY --from=<your-activegate>/linux/oneagent-codemodules-musl:<technology> / /


ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые варианты: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.

3. Соберите образ вашего приложения.

   Соберите образ Docker из вашего dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете осуществлять мониторинг контейнеров приложений с помощью другой среды Dynatrace. Для этого следуйте приведённым ниже инструкциям:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения с добавленными модулями кода OneAgent для определённой среды Dynatrace, вы можете настроить OneAgent на отправку данных в другую среду Dynatrace без пересборки образа приложения.

   Для этого необходимо выполнить вызов к REST-конечной точке второй среды Dynatrace. Убедитесь, что вы заменили соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий необходимую информацию, которую нужно передать в качестве переменных окружения контейнеру приложения. Убедитесь, что вы установили переменные окружения контейнера приложения, как описано ниже:

   * `DT_TENANT`: равен `tenantUUID`
   * `DT_TENANTTOKEN`: равен `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённых точкой с запятой

1. Добавьте следующие команды в ваш текущий Dockerfile для интеграции OneAgent и активации инструментирования вашего приложения. Определите переменные с необязательными значениями по умолчанию с помощью инструкций `ARG`.

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

   * Команды выше, использующие `wget` и `unzip`, могут завершиться с ошибкой, если они не предоставлены базовым образом.
   * Замените `<your-environment-id>` на идентификатор вашей среды Dynatrace. Если вы используете Dynatrace Managed, необходимо указать URL кластера Dynatrace (`https://<YourDynatraceServerURL>/e/<your-environment-id>/api`).
   * Замените `<your-paas-token>` на ваш PaaS-токен.
   * `DT_ONEAGENT_OPTIONS` — это вариант сборки (допустимые варианты: `default` или `musl` для образов Alpine) и технология (модуль кода).

     + Синтаксис для `default`: `flavor=default&include=all`.
     + Синтаксис для `musl`: `flavor=musl&include=all`.

   **Что делать, если мой образ Docker основан на Alpine Linux?**

   Dynatrace OneAgent поддерживает вариант `musl` для сред на основе Alpine Linux. Допустимые варианты для `flavor=musl`: `all`, `go`, `java`, `apache`, `nginx` и `nodejs`.
2. Соберите образ вашего приложения.

   Соберите образ Docker из вашего dockerfile для использования в среде Kubernetes:

   ```
   docker build -t yourapp .
   ```

   Вы можете осуществлять мониторинг контейнеров приложений с помощью другой среды Dynatrace. Для этого следуйте приведённым ниже инструкциям:

   Для OneAgent версии 1.139+, если у вас уже есть образ приложения с добавленными модулями кода OneAgent для определённой среды Dynatrace, вы можете настроить OneAgent на отправку данных в другую среду Dynatrace без пересборки образа приложения.

   Для этого необходимо выполнить вызов к REST-конечной точке второй среды Dynatrace. Убедитесь, что вы заменили соответствующие заполнители `<your-environment-id>` и `<your-paas-token>`.

   ```
   curl "https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your-paas-token>"
   ```

   В ответ вы получите JSON-объект, содержащий необходимую информацию, которую нужно передать в качестве переменных окружения контейнеру приложения. Убедитесь, что вы установили переменные окружения контейнера приложения, как описано ниже:

   * `DT_TENANT`: равен `tenantUUID`
   * `DT_TENANTTOKEN`: равен `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённых точкой с запятой

### Настройка сетевых зон (необязательно)

Вы можете настроить сетевые зоны в качестве переменной окружения:

* `DT_NETWORK_ZONE`: равен `your.network.zone`

Дополнительную информацию см. в разделе [Сетевые зоны](../../../manage/network-zones.md "Узнайте, как работают сетевые зоны в Dynatrace.").

## Потребление мониторинга

Для AWS App Runner потребление мониторинга основано на единицах хостов. Подробности см. в разделе [Мониторинг приложений и инфраструктуры (единицы хостов)](../../../license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md "Узнайте, как рассчитывается потребление мониторинга приложений и инфраструктуры Dynatrace на основе единиц хостов.").

## Устранение неполадок

* [Проблемы интеграции OneAgent в образ приложения](https://dt-url.net/yu23mli)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
