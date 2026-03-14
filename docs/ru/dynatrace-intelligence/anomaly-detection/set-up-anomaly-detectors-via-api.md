---
title: Автоматизация оповещений с помощью API
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/set-up-anomaly-detectors-via-api
scraped: 2026-03-06T21:20:44.696000
---

# Автоматизация оповещений через API

# Автоматизация оповещений через API

* Latest Dynatrace
* Руководство
* Обновлено 28 января 2026

Новейшая платформа Dynatrace предоставляет универсальные сервисы ИИ, охватывающие различную функциональность. Обычно платформа обрабатывает аутентификацию и маршрутизацию к нужной среде за вас. Однако Dynatrace предлагает возможность вызывать API извне платформы. В этом руководстве вы узнаете, как настроить пользовательские оповещения на основе DQL в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** через API.

## Для кого предназначено

Эта статья предназначена для всех пользователей, которые хотят настраивать и управлять пользовательскими оповещениями на основе DQL в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** через API.

## Чему вы научитесь

В этой статье вы узнаете, как настроить пользовательское оповещение через API.

## Перед началом работы

Пользовательские оповещения на основе DQL в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** используют схему `builtin:davis.anomaly-detectors`.

### Предварительные знания

* [Обнаружение аномалий](../anomaly-detection.md "Как Dynatrace обнаруживает аномалии в вашей среде.")
* [Настройка чувствительности обнаружения аномалий](adjust-sensitivity-anomaly-detection.md "Узнайте, как адаптировать чувствительность обнаружения проблем в Dynatrace.")
* [Модели ИИ](../reference/ai-models.md "Узнайте о моделях ИИ, которые использует Dynatrace Intelligence.")
* [Клиенты OAuth](../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управляйте аутентификацией и правами пользователей с помощью клиентов OAuth.") или [Токены платформы](../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md "Создавайте персонализированные токены платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.")
* [Как получить доступ к API платформы](https://developer.dynatrace.com/develop/access-platform-apis-from-outside/)

### Предварительные требования

Для настройки пользовательских оповещений через API вам необходимы следующие разрешения:

* `settings:schemas:read`
* `settings:objects:read`
* Разрешения, специфичные для Grail, для данных, которые вы хотите запрашивать (например, `storage:buckets:read`, `storage:logs:read`, `storage:events:read`, `storage:metrics:read`)

Если вы планируете создавать или редактировать существующие конфигурации, вам также потребуются следующие разрешения:

* `settings:objects:write`
* `iam:service-users:use` — обязательно только при использовании сервисных пользователей, что рекомендуется для автоматизации

Если вы планируете запускать пользовательские оповещения без использования сервисного пользователя в качестве актора, разрешение `davis:analyzers:execute` является обязательным.

### Аутентификация

Для аутентификации доступа к API и настройки пользовательского оповещения вам необходимо использовать клиент OAuth или токен платформы. Классические методы аутентификации, такие как имя пользователя и пароль, не будут работать.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** не работает на классических конечных точках.

Для аутентификации доступа к API с помощью клиента OAuth необходимо

1. Создать клиент OAuth со всеми разрешениями, перечисленными в [Предварительных требованиях](#api-prerequisites).
2. Сгенерировать bearer-токен из созданного клиента.

Дополнительную информацию о создании клиента OAuth и генерации bearer-токена см. в разделе [Клиенты OAuth](../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управляйте аутентификацией и правами пользователей с помощью клиентов OAuth.").

Если вы хотите использовать токен платформы, создайте токен платформы для выбранного пользователя или среды. Дополнительную информацию о создании и управлении токенами платформы см. в разделе [Токены платформы](../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md "Создавайте персонализированные токены платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.").

Токен платформы будет работать только в пределах разрешений назначенного пользователя. Это означает, что выбранная область предоставляет доступ только в том случае, если у этого пользователя есть соответствующие разрешения.

После выполнения описанных выше шагов вы сможете вызывать Settings 2.0 API, аутентифицируясь с помощью токена платформы или bearer-токена, сгенерированного из клиента OAuth. Пример URL конечной точки Settings 2.0 приведён ниже:

```
https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects
```

## Создание конфигурации пользовательского оповещения

Чтобы создать конфигурацию пользовательского оповещения

1. Получите токен платформы или bearer-токен, сгенерированный на этапе [Аутентификации](../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").
2. Вызовите функцию приложения через URL конечной точки.
3. Создайте новый объект настроек, используя schemaID для пользовательских оповещений на основе DQL, `builtin:davis.anomaly-detectors`, и токен платформы или клиент OAuth. Это создаст объект настроек пользовательского оповещения. Пример вызова для нового объекта настроек приведён ниже:

   ```
   curl 'https://{your-environment-id}.apps.dynatrace.com/platform/classic/environment-api/v2/settings/objects' \



   -X POST \



   -H 'Accept: application/json; charset=utf-8' \



   -H 'Content-Type: application/json; charset=utf-8' \



   -H 'Authorization: Bearer {your-bearer-token}' \



   -d '[



   {



   "schemaId": "builtin:davis.anomaly-detectors",



   "scope": "environment",



   "value": {



   "enabled": true,



   "title": "Low disk space alert",



   "description": "",



   "source": "Rest-API",



   "executionSettings": {



   "actor": null,



   "queryOffset": null



   },



   "analyzer": {



   "name": "dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer",



   "input": [



   {



   "key": "query",



   "value": "timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}"



   },



   {



   "key": "threshold",



   "value": "10"



   },



   {



   "key": "alertCondition",



   "value": "BELOW"



   },



   {



   "key": "alertOnMissingData",



   "value": "false"



   },



   {



   "key": "violatingSamples",



   "value": "3"



   },



   {



   "key": "slidingWindow",



   "value": "5"



   },



   {



   "key": "dealertingSamples",



   "value": "5"



   }



   ]



   },



   "eventTemplate": {



   "properties": [



   {



   "key": "dt.source_entity",



   "value": "{dims:dt.entity.host}"



   },



   {



   "key": "event.type",



   "value": "CUSTOM_ALERT"



   },



   {



   "key": "event.description",



   "value": "The disk {dims:dt.entity.disk.name} runs out of space. Free up space or resize disk."



   },



   {



   "key": "event.name",



   "value": "Low amount of disk space available on host {dims:dt.entity.host.name}"



   }



   ]



   }



   }



   }



   ]'
   ```

### Параметры

Конфигурация обнаружения аномалий состоит из следующих полей:

* `enabled`: логический параметр. Если установлен в `true`, указывает, что конфигурация включена и используется для оценки.
* `title`: название вашей конфигурации пользовательского оповещения. Вы можете задать любое имя.
* `description`: параметр свободного текста, описывающий вашу конфигурацию пользовательского оповещения.
* `source`: параметр свободного текста, который можно использовать для группировки и фильтрации конфигураций в интерфейсе. Например, установка source как `kubernetes` для некоторых конфигураций позволяет фильтровать все конфигурации `kubernetes` в приложении. Если `source` не задан, используется значение по умолчанию, указывающее, что конфигурация создана через REST API.
* `executionSettings`: этот объект содержит необязательное поле `queryOffset`. Когда `queryOffset` установлен в значение типа `integer`, он смещает скользящее окно оценки. Это можно использовать для исключения последних нескольких точек данных в метриках, связанных с задержкой.
* `analyzer`: этот объект указывает модель обнаружения аномалий и связанные параметры, которые будут использоваться в конфигурации. Дополнительные сведения о моделях обнаружения аномалий см. в разделе [Модели ИИ](../reference/ai-models.md "Узнайте о моделях ИИ, которые использует Dynatrace Intelligence.").
* `eventTemplate`: этот объект определяет содержание событий, генерируемых при обнаружении настроенной аномалии.

#### Поля объекта `analyzer`

Объект `analyzer` имеет дополнительные поля, которые необходимо настроить для работы вашего пользовательского оповещения.

* `name`: название модели обнаружения аномалий, которая будет использоваться для оценки вашего запроса. Доступны три модели:

  + `dt.statistics.ui.anomaly_detection.StaticThresholdAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.AutoAdaptiveAnomalyDetectionAnalyzer`
  + `dt.statistics.ui.anomaly_detection.SeasonalBaselineAnomalyDetectionAnalyzer`
* `input`: список параметров, определяющих работу вашего пользовательского оповещения.

  + `numberOfSignalFluctuations`: параметр, доступный только для авто-адаптивной модели пользовательского оповещения. Он контролирует, сколько раз флуктуация сигнала должна быть добавлена к базовой линии для получения фактического порога оповещения. Значение по умолчанию — `1`.
  + `tolerance`: параметр, доступный только для модели сезонной базовой линии пользовательского оповещения. Более высокий допуск означает более широкую полосу доверия и приводит к меньшему количеству сгенерированных событий. Значение по умолчанию — `4`.
  + `alertCondition`: условие для оповещения.

    - `ABOVE` — значение выше порога. Доступно для всех моделей.
    - `BELOW` — значение ниже порога. Доступно для всех моделей.
    - `OUTSIDE` — значение за пределами верхнего или нижнего порога. Доступно для авто-адаптивной модели и модели сезонной базовой линии.
  + `alertOnMissingData`: логический параметр. Если установлен в `true`, отсутствие данных в окне оценки будет считаться нарушением настроенного порога.
  + `threshold`: параметр, доступный для моделей со статическим порогом. Это числовое значение для сравнения при оценке конфигурации. Оно должно быть предоставлено в базовой единице запрашиваемых данных, например, в миллисекундах для метрики длительности.
  + `violatingSamples`: числовое значение, максимум `60`. Этот параметр указывает, сколько точек данных в скользящем окне должны превысить, упасть ниже или выйти за пределы настроенного порога для генерации оповещения.
  + `slidingWindow`: числовое значение, максимум `60`. Этот параметр указывает, сколько точек данных непрерывно анализируется при оценке количества нарушений порога.

    Скользящее окно должно быть больше или равно значению, установленному для `violatingSamples`.
  + `delalertingSamples`: числовое значение, максимум `60`. Этот параметр указывает, сколько точек данных должны не нарушать порог, чтобы событие было закрыто.
  + `query`: запрос DQL, оцениваемый конфигурацией. Результат запроса должен быть типа `timeseries`, полученного с помощью команд DQL `timeseries` или `makeTimeseries`.

    Запрос должен явно указывать временной интервал `interval:1m`. Вы не можете устанавливать временные рамки с помощью операторов DQL `from:` и `to:` в этой конфигурации.

#### Поля объекта `eventTemplate`

Объект `eventTemplate` имеет дополнительные поля, которые необходимо настроить для работы вашего пользовательского оповещения.

* `properties`: пары ключ-значение свойств, которые отображаются в сгенерированных событиях.

  + Обязательно `event.name`: заголовок для событий, генерируемых этим пользовательским оповещением. Вы можете задать любое имя.
  + Обязательно `event.description`: параметр свободного текста, описывающий вашу конфигурацию пользовательского оповещения.
  + Обязательно `event.type`: тип генерируемого события, например, `CUSTOM_INFO`, `ERROR_EVENT`, `AVAILABILITY_EVENT`, `PERFORMANCE_EVENT`, `RESOURCE_CONTENTION_EVENT`, `CUSTOM_ALERT`, `CUSTOM_ANNOTATION`, `CUSTOM_CONFIGURATION`, `CUSTOM_DEPLOYMENT`, `MARKED_FOR_TERMINATION`.

    Все доступные типы событий см. в [Семантическом словаре Dynatrace Intelligence](../../../common/semantic-dictionary/model/davis.md "Познакомьтесь с моделями семантического словаря, связанными с Davis AI."). Вы также можете использовать здесь свои пользовательские события.

## Заключение

Вы узнали, как настроить и сконфигурировать пользовательское оповещение через API. Теперь вы можете напрямую вызывать пользовательские оповещения и использовать обнаружение аномалий на основе DQL через конфигурацию API.

## Связанные темы

* [Обнаружение аномалий](../anomaly-detection.md "Как Dynatrace обнаруживает аномалии в вашей среде.")
* [Модели ИИ](../reference/ai-models.md "Узнайте о моделях ИИ, которые использует Dynatrace Intelligence.")
* [Settings API — GET objects](../../dynatrace-api/environment-api/settings/objects/get-objects.md "Просмотр нескольких объектов настроек через Dynatrace API.")
* [Settings API — POST an object](../../dynatrace-api/environment-api/settings/objects/post-object.md "Создание или проверка объекта настроек через Dynatrace API.")
* [Settings API — PUT an object](../../dynatrace-api/environment-api/settings/objects/put-object.md "Редактирование объекта настроек через Dynatrace API.")
* [Settings API — DELETE an object](../../dynatrace-api/environment-api/settings/objects/del-object.md "Удаление объекта настроек через Dynatrace API.")