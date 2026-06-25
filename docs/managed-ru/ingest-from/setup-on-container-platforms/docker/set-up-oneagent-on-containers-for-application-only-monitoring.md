---
title: Настройка OneAgent на контейнерах для мониторинга только приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring
scraped: 2026-05-12T11:11:06.267932
---

# Настройка OneAgent на контейнерах для мониторинга только приложений

# Настройка OneAgent на контейнерах для мониторинга только приложений

* 2-min read
* Published Jun 25, 2021

При отсутствии доступа к базовым хостам OneAgent можно развернуть на контейнерах для мониторинга только приложений. Следуйте приведённым ниже шагам для интеграции OneAgent в образ приложения.

## Развёртывание OneAgent

Требуемые версии

* Docker версии 17.05+

1. Войдите в Docker, используя ID окружения Dynatrace в качестве имени пользователя.

   ```
   docker login <environmentURL> -u <environmentID>
   ```

2. Введите `<PAAS_TOKEN>` при появлении запроса.

3. Добавьте следующие строки в образ приложения после последней команды `FROM`:

   ```
   COPY --from=<environmentURL>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

   где:

* `<environmentURL>`:

  + Environment ActiveGate: `<ActiveGateaddress:9999>`
  + Managed: `{ManagedAddress}`
* `<TECHNOLOGY>` — кодовый модуль OneAgent, необходимый для вашего приложения. Допустимые значения: `all`, `java`, `python`, `apache`, `nginx`, `nodejs`, `dotnet`, `php`, `go` и `sdk`. Для указания нескольких кодовых модулей разделяйте их дефисами (например, `java-go` для `java` и `go`). Указание конкретных технологий вместо `all` уменьшает размер пакета OneAgent.

Если образ Docker основан на Alpine Linux?

Dynatrace OneAgent поддерживает окружения на основе Alpine Linux.
Используйте следующий синтаксис:

```
COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules-musl:<TECHNOLOGY> / /



ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
```

Допустимые значения: `all`, `dotnet`, `php`, `java`, `apache`, `nginx`, `nodejs` и `go`.

3. Соберите образ приложения.

   Соберите Docker-образ из Dockerfile для использования в Kubernetes.

   ```
   docker build -t yourapp .
   ```

   Можно мониторить контейнеры приложения с другим окружением Dynatrace.

   Для OneAgent версии 1.139+, если у вас есть существующий образ приложения с уже добавленными кодовыми модулями OneAgent для конкретного окружения Dynatrace, можно перенаправить данные в другое окружение без пересборки образа.
   Для этого выполните вызов REST-эндпоинта второго окружения Dynatrace:

   ```
   curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
   ```

   В ответ вы получите JSON-объект с необходимой информацией, которую нужно передать в качестве переменных окружения контейнера приложения:

   * `DT_TENANT`: равно `tenantUUID`
   * `DT_TENANTTOKEN`: равно `tenantToken`
   * `DT_CONNECTION_POINT`: список `communicationEndpoints` через точку с запятой

   4. Необязательно: настройте сетевые зоны.

   Сетевые зоны можно настроить как переменную окружения:

   * `DT_NETWORK_ZONE`: равно `your.network.zone`

   Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Принцип работы сетевых зон в Dynatrace.").

4. Необязательно: настройте адрес прокси.

   При работе в среде с прокси установите переменную окружения `DT_PROXY` в контейнере приложения для передачи учётных данных прокси в OneAgent.

   Для контейнеров на основе Alpine Linux может потребоваться обновление `wget`, поставляемого с Alpine, для поддержки аутентификации через прокси при загрузке OneAgent.

## Обновление OneAgent

При выходе новой версии Dynatrace OneAgent необходимо пересобрать локальные кодовые модули OneAgent и образ приложения. Все новые поды, созданные из этого образа, будут отслеживаться с последней версией OneAgent.

Если в настройках обновлений OneAgent указана версия по умолчанию для новых хостов и приложений, ваши Kubernetes-приложения будут автоматически отслеживаться указанной версией Dynatrace OneAgent.

## Удаление OneAgent

Для удаления OneAgent из режима мониторинга только приложений просто удалите ссылки из образа приложения или Docker и повторно разверните приложение.

### Build-time injection контейнера

Docker multi-stage image builds

Классическая интеграция

1. Удалите из образа приложения следующие строки кода:

   ```
   COPY --from=<ACTIVEGATE-ADDRESS>/linux/oneagent-codemodules:<TECHNOLOGY> / /



   ENV LD_PRELOAD /opt/dynatrace/oneagent/agent/lib64/liboneagentproc.so
   ```

2. Пересоберите образ приложения.

   ```
   docker build -t yourapp .
   ```

1. Удалите из Dockerfile следующие команды:

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

2. Пересоберите образ приложения.

   ```
   docker build -t yourapp .
   ```

## Связанные темы

* [Настройка Dynatrace на Docker](/managed/ingest-from/setup-on-container-platforms/docker "Развёртывание OneAgent на Docker.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")