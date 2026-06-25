---
title: Настройка Dynatrace на Heroku
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/heroku
scraped: 2026-05-12T11:03:31.428984
---

# Настройка Dynatrace на Heroku

# Настройка Dynatrace на Heroku

* 6-min read
* Updated on Jun 23, 2023

Heroku — облачная платформа как сервис (PaaS), позволяющая создавать и запускать приложения в облаке. Приложения, развёрнутые на Heroku, как правило, запускаются через один или несколько buildpacks, предоставляющих поддержку фреймворков и среды выполнения.

## Возможности

Heroku buildpack для Dynatrace OneAgent не зависит от языка программирования и может использоваться с любым [поддерживаемым Dynatrace языком](/managed/ingest-from/technology-support#applications-services-and-databases "Техническая информация о поддержке платформ и фреймворков в Dynatrace."), включая Node.js-приложения. Если вы использовали [Dynatrace NPM module for PaaS](https://www.npmjs.com/package/@dynatrace/oneagent), его можно удалить из зависимостей, так как buildpack автоматически обнаруживает и инструментирует Node.js-приложения.

Heroku buildpack для Dynatrace OneAgent автоматически загружает последнюю версию OneAgent. Если в настройках обновлений OneAgent указана версия по умолчанию, buildpack загрузит указанную версию.

Следующие рекомендации описывают включение мониторинга Dynatrace для ваших приложений [Heroku](https://www.dynatrace.com/technologies/heroku-monitoring/) путём добавления [Dynatrace Heroku buildpack](https://github.com/Dynatrace/heroku-buildpack-dynatrace) в конфигурацию приложения.

Dynatrace Heroku buildpack позволяет отслеживать все [поддерживаемые языки на Linux-системах](/managed/ingest-from/technology-support#applications-services-and-databases "Техническая информация о поддержке платформ в Dynatrace.").

## Предварительные условия

* Создайте [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Концепция токена доступа и его областей видимости.").
* Ознакомьтесь со списком [поддерживаемых приложений и версий](/managed/ingest-from/technology-support "Техническая информация о поддержке платформ в Dynatrace.").
* [Требование к памяти кодового модуля OneAgent](/managed/ingest-from/dynatrace-oneagent/oa-requirements#oneagent-code-module-memory-requirement "Требования к кодовому модулю OneAgent") составляет 200 МБ от [размера slug](https://devcenter.heroku.com/articles/slug-compiler#slug-size).

## Установка

### Установка Heroku CLI

Для настройки приложений Heroku с Dynatrace Heroku buildpack можно использовать [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) или [дашборд Heroku](https://dashboard.heroku.com).

### Добавление Dynatrace Heroku buildpack

Для интеграции Dynatrace OneAgent в существующее приложение добавьте Dynatrace Heroku buildpack и установите ID окружения и PaaS-токен с помощью команд ниже.

```
# Добавление Dynatrace buildpack



heroku buildpacks:add https://github.com/Dynatrace/heroku-buildpack-dynatrace.git#<version>



# Установка учётных данных окружения Dynatrace



heroku config:set DT_TENANT=<environmentID>



heroku config:set DT_API_TOKEN=<token>



# Развёртывание на Heroku



git push heroku master
```

После внесения этих изменений buildpack устанавливает Dynatrace OneAgent для автоматического мониторинга приложения.

### Дополнительная конфигурация

Dynatrace Heroku buildpack поддерживает следующие конфигурации:

| Переменная окружения | Описание |
| --- | --- |
| DT\_TENANT | ID вашего окружения Dynatrace. **Примечание:** подробнее об ID окружения см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Работа с окружениями мониторинга."). |
| DT\_API\_TOKEN | PaaS-токен для интеграции окружения Dynatrace с Heroku. |
| DT\_API\_URL | - Для Dynatrace SaaS с доступом к интернету: `https://<your-environment-ID>.live.dynatrace.com/api` - Для Dynatrace Managed: `https://<your-managed-cluster-domain>/e/<your-environment-ID>/api` - Для Environment ActiveGates: `https://<your-ActiveGate-IP-or-FQDN>:9999/e/<your-environment-ID>/api` **Примечание:** подробнее об ID окружения см. в разделе [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Работа с окружениями мониторинга."). |
| DT\_DOWNLOAD\_URL | Необязательно: прямой URL загрузки Dynatrace OneAgent. Если задана, buildpack загрузит OneAgent из этого расположения. |
| SSL\_MODE | Необязательно: установите `all` для принятия всех самоподписанных SSL-сертификатов. |
| DT\_TAGS | не рекомендуется: теги для добавления к мониторируемым приложениям. |
| DT\_CUSTOM\_PROP | не рекомендуется: применяйте для разделения по компоненту и/или окружению. |
| SKIP\_ERRORS | Необязательно: при значении `1` развёртывание приложения не будет прерываться при ошибках загрузки установщика OneAgent. |

Рекомендуется создавать переменные окружения, специфичные для обнаружения процессов. Переменные окружения с другим назначением, такие как [`DT_TAGS`](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables#variables "Определение тегов на основе переменных окружения.") или [`DT_CUSTOM_PROP`](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Настройка метаданных групп процессов."), могут привести к некорректному разделению.

Переход с Dynatrace NPM module for PaaS на Heroku buildpack

Dynatrace Heroku buildpack не требует изменений в исходном коде приложения:

Больше не нужно устанавливать зависимость от `@dynatrace/oneagent` в вашем Node.js-приложении.
Также можно удалить следующую инструкцию как первую строку Node.js-приложения:

```
try {



require('@dynatrace/oneagent')();



} catch(err) {



console.log(err.toString());



}
```

Благодаря этим преимуществам Heroku buildpack для Dynatrace OneAgent заменяет Dynatrace NPM module for PaaS и требует OneAgent версии 1.141+.

Использование другого окружения Dynatrace для Heroku-приложений

Для OneAgent версии 1.139+, если у вас есть существующее Heroku-приложение с кодовыми модулями OneAgent для конкретного окружения Dynatrace, можно перенаправить данные в другое окружение.

Для этого выполните вызов REST-эндпоинта второго окружения Dynatrace:

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

В ответ вы получите JSON-объект, который необходимо передать как переменные окружения вашего Heroku-приложения:

* `DT_TENANT`: равно `tenantUUID`
* `DT_TENANTTOKEN`: равно `tenantToken`
* `DT_CONNECTION_POINT`: список `communicationEndpoints` через точку с запятой

### Настройка сетевых зон (Необязательно)

Сетевые зоны можно настроить через переменную окружения:

```
heroku config:set DT_NETWORK_ZONE=<your.network.zone>
```

Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Принцип работы сетевых зон в Dynatrace.").

## Обновление OneAgent

При выходе новой версии OneAgent необходимо инициировать повторный запуск buildpack в Heroku. Dynatrace buildpack автоматически загрузит последнюю версию OneAgent.

Если в настройках обновлений OneAgent указана версия по умолчанию для новых хостов и приложений, Heroku buildpack автоматически загрузит указанную версию.

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")