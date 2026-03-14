---
title: Настройка Dynatrace в Heroku
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/heroku
scraped: 2026-03-06T21:15:35.528815
---

# Настройка Dynatrace на Heroku


* Latest Dynatrace
* Чтение: 6 мин
* Обновлено 23 июня 2023

Heroku — это облачная платформа как услуга (PaaS), которая позволяет создавать и запускать приложения в облаке. Приложения, развёрнутые на Heroku, обычно запускаются через один или несколько билдпаков (buildpack), которые обеспечивают поддержку фреймворков и среды выполнения.

## Возможности

Билдпак Heroku для Dynatrace OneAgent не зависит от языка и может использоваться с любым [языком, поддерживаемым Dynatrace](../technology-support.md#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks."), включая приложения на основе Node.js. Если вы использовали [модуль Dynatrace NPM для PaaS](https://www.npmjs.com/package/@dynatrace/oneagent), вы можете удалить его из зависимостей, так как билдпак автоматически обнаруживает и инструментирует ваши приложения Node.js.

Вам также больше не нужно полагаться на релизы зависимостей Dynatrace OneAgent для NPM. Билдпак Heroku для Dynatrace OneAgent автоматически загружает последнюю версию Dynatrace OneAgent, чтобы вы могли получать потенциальные исправления максимально быстро и легко. Если вы [указали версию OneAgent по умолчанию для установки на новые хосты и приложения в настройках обновления OneAgent](../dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux.md "Learn about the different ways to update OneAgent on Linux."), билдпак Heroku для Dynatrace OneAgent загрузит указанную версию Dynatrace OneAgent по умолчанию.

Следующие инструкции объясняют, как включить мониторинг Dynatrace для ваших приложений [Heroku](https://www.dynatrace.com/technologies/heroku-monitoring/), добавив [билдпак Dynatrace Heroku](https://github.com/Dynatrace/heroku-buildpack-dynatrace) в конфигурацию Heroku вашего приложения.

Билдпак Dynatrace Heroku позволяет мониторить все [поддерживаемые языки на системах Linux](../technology-support.md#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Предварительные условия

* Создайте [PaaS-токен](../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Learn the concept of an access token and its scopes.").
* Ознакомьтесь со списком [поддерживаемых приложений и версий](../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* [Требования к памяти кодового модуля OneAgent](../dynatrace-oneagent/oa-requirements.md#oneagent-code-module-memory-requirement "OneAgent code module requirements") составляют 200 МБ от вашего [размера slug](https://devcenter.heroku.com/articles/slug-compiler#slug-size).

## Установка

Эти инструкции объясняют, как интегрировать Dynatrace OneAgent в ваши Heroku dyno и начать мониторинг приложений Heroku.

### Получение Heroku CLI

Для настройки приложений Heroku на использование билдпака Dynatrace Heroku вы можете использовать [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) или настроить приложения через [панель управления Heroku](https://dashboard.heroku.com).

### Добавление билдпака Dynatrace Heroku

Для интеграции Dynatrace OneAgent в существующее приложение необходимо добавить билдпак Dynatrace Heroku в билдпаки вашего приложения и задать идентификатор среды Dynatrace и PaaS-токен с помощью команд ниже.

```
# Add the Dynatrace buildpack


heroku buildpacks:add https://github.com/Dynatrace/heroku-buildpack-dynatrace.git#<version>


# Set required credentials to your Dynatrace environment


heroku config:set DT_TENANT=<environmentID>


heroku config:set DT_API_TOKEN=<token>


# Deploy to Heroku


git push heroku master
```

После отправки этих изменений билдпак устанавливает Dynatrace OneAgent для автоматического мониторинга вашего приложения.

### Дополнительная настройка

Билдпак Dynatrace Heroku поддерживает следующие конфигурации:

| Переменная среды | Описание |
| --- | --- |
| DT\_TENANT | Идентификатор вашей среды Dynatrace. **Примечание:** Подробности о том, как определить идентификатор среды, см. в разделе [идентификатор среды](../../discover-dynatrace/get-started/monitoring-environment.md "Understand and learn how to work with monitoring environments."). |
| DT\_API\_TOKEN | PaaS-токен для интеграции вашей среды Dynatrace с Heroku. |
| DT\_API\_URL | - Для Dynatrace SaaS, когда OneAgent может подключаться к интернету: `https://<your-environment-ID>.live.dynatrace.com/api` - Для Dynatrace Managed: `https://<your-managed-cluster-domain>/e/<your-environment-ID>/api` - Для ActiveGate среды (SaaS или Managed), используйте следующее для загрузки OneAgent, а также для маршрутизации трафика OneAgent через ActiveGate: `https://<your-ActiveGate-IP-or-FQDN>:9999/e/<your-environment-ID>/api` **Примечание:** Подробности о том, как определить идентификатор среды, см. в разделе [идентификатор среды](../../discover-dynatrace/get-started/monitoring-environment.md "Understand and learn how to work with monitoring environments."). |
| DT\_DOWNLOAD\_URL | Необязательно. Прямой URL загрузки Dynatrace OneAgent. Если эта переменная среды установлена, билдпак загрузит OneAgent из этого расположения. |
| SSL\_MODE | Необязательно. Установите значение `all`, если вы хотите принимать все самоподписанные SSL-сертификаты. |
| DT\_TAGS | Не рекомендуется. Теги, которые вы хотите добавить к мониторируемым приложениям. |
| DT\_CUSTOM\_PROP | Не рекомендуется. Применяйте, если хотите разделить по компоненту и/или среде. |
| SKIP\_ERRORS | Необязательно. Если установлено значение `1`, развёртывание приложения не будет завершено ошибкой при ошибках загрузки установщика OneAgent. |

Мы рекомендуем создавать переменные среды, специфичные для обнаружения процессов. Переменные среды, обслуживающие другие области, такие как [`DT_TAGS`](../../manage/tags-and-metadata/setup/define-tags-based-on-environment-variables.md#variables "Find out how Dynatrace enables you to define tags based on environment variables.") или [`DT_CUSTOM_PROP`](../../observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata.md#variables "Configure your own process-related metadata based on the unique needs of your organization or environment."), могут вызвать некорректное или непреднамеренное разделение, поскольку все значения переменных среды учитываются при обнаружении группы процессов.

Как использовать билдпак Heroku для Dynatrace OneAgent вместо модуля Dynatrace NPM для PaaS

Билдпак Heroku для Dynatrace OneAgent не требует изменений в исходном коде вашего приложения:

Вам больше не нужно устанавливать зависимость от `@dynatrace/oneagent` в каталоге проекта вашего приложения Node.js.
Также вам больше не требуется добавлять следующее выражение в качестве первого выражения вашего приложения Node.js:

```
try {


require('@dynatrace/oneagent')();


} catch(err) {


console.log(err.toString());


}
```

Благодаря этим преимуществам билдпак Heroku для Dynatrace OneAgent заменяет модуль Dynatrace NPM для PaaS и требует OneAgent версии 1.141+.

Если вы хотите начать использовать билдпак Heroku для Dynatrace OneAgent вместо модуля Dynatrace NPM для PaaS, всё, что вам нужно сделать, — это удалить зависимость от `@dynatrace/oneagent` в вашем файле `package.json`:

```
$ npm uninstall --save @dynatrace/oneagent
```

Кроме того, вы можете удалить выражение `require`, упомянутое выше, из вашего приложения Heroku.

Вы можете использовать другую среду Dynatrace для приложений Heroku, обогащённых OneAgent.

Как использовать другую среду Dynatrace для приложений Heroku, обогащённых OneAgent

Для OneAgent версии 1.139+, если у вас есть существующее приложение Heroku, в которое вы уже добавили кодовые модули OneAgent для определённой среды Dynatrace, вы можете настроить OneAgent на отправку данных в другую среду Dynatrace.

Для этого вам необходимо выполнить вызов REST-эндпоинта вашей второй среды Dynatrace. Не забудьте адаптировать соответствующие заполнители `<environmentID>` и `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

В ответ вы получите JSON-объект, содержащий необходимую информацию, которую нужно передать в качестве переменной среды в контейнер приложения. Убедитесь, что вы задали переменные среды вашего приложения Heroku, как описано ниже:

* `DT_TENANT`: равен `tenantUUID`
* `DT_TENANTTOKEN`: равен `tenantToken`
* `DT_CONNECTION_POINT`: список `communicationEndpoints`, разделённых точкой с запятой

### Настройка сетевых зон (необязательно)

Вы можете настроить сетевые зоны через переменную среды:

```
heroku config:set DT_NETWORK_ZONE=<your.network.zone>
```

Подробнее см. [сетевые зоны](../../manage/network-zones.md "Find out how network zones work in Dynatrace.").

## Обновление OneAgent

Когда становится доступна новая версия OneAgent, вам необходимо запустить повторное выполнение билдпака в Heroku. Билдпак Dynatrace автоматически загрузит последнюю версию OneAgent.

Если вы указали версию OneAgent по умолчанию для установки на новые хосты и приложения в [настройках обновления OneAgent](../dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux.md "Learn about the different ways to update OneAgent on Linux."), билдпак Heroku автоматически загрузит указанную версию OneAgent по умолчанию.

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")