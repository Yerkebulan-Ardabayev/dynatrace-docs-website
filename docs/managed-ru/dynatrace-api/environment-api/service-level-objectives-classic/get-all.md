---
title: Service-level objectives API - GET все SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/get-all
scraped: 2026-05-12T11:57:39.454058
---

# Service-level objectives API - GET все SLO

# Service-level objectives API - GET все SLO

* Справочник
* Обновлено 7 января 2025 г.

Возвращает список всех целей уровня обслуживания и их вычисленные значения.

По умолчанию значения вычисляются для собственного временного диапазона SLO. Можно использовать пользовательский временной диапазон:

1. Установите параметр **timeFrame** в `GTF`.
2. Укажите временной диапазон в параметрах **from** и **to**.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `slo.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если query-параметр **nextPageKey** не указан.  Когда **nextPageKey** задан для получения следующих страниц, все остальные query-параметры нужно опустить. | query | Необязательный |
| pageSize | integer | Количество SLO в одном payload ответа.  Максимально допустимый размер страницы: 10000.  Если не задан, используется 10. | query | Необязательный |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон в две недели (`now-2w`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| sloSelector | string | Область запроса. В ответ включаются только SLO, соответствующие указанным критериям.  Можно добавить один или несколько из перечисленных ниже критериев.  * ID SLO: `id("id-1","id-2")`. * Имя: `name("name")`. Фильтрует SLO с заданным именем. Фильтр чувствителен к регистру. * Состояние здоровья: `healthState("HEALTHY")` или `healthState("UNHEALTHY")`. Фильтрует SLO без связанных открытых проблем (`HEALTHY`) или SLO со связанными открытыми проблемами (`UNHEALTHY`). Можно указать только одно состояние здоровья. * Текст: `text("value")`. Фильтрует все SLO, содержащие заданное значение в имени или описании. Фильтр нечувствителен к регистру. * Проблема: `problemDisplayName("value")`. Фильтрует все SLO, связанные с заданным отображаемым именем проблемы (например, P-12345). * Имя зоны управления: `managementZone("MZ-A")`. Фильтрует все SLO, связанные с заданным именем зоны управления. Возвращаемые SLO оцениваются относительно заданной зоны управления. * ID зоны управления: `managementZoneID("123")`. Фильтрует все SLO, связанные с заданным ID зоны управления. Возвращаемые SLO оцениваются относительно заданной зоны управления.  Чтобы задать несколько критериев, разделяйте их запятой (`,`). В ответ включаются только SLO, соответствующие всем критериям. Примеры:  * .../api/v2/slo?sloSelector=name("Service Availability") * .../api/v2/slo?sloSelector=id("id") * .../api/v2/slo?sloSelector=text("Description"),healthState("HEALTHY").  Специальные символы `~` и `"` нужно экранировать с помощью `~` (например, поиск по двойной кавычке `text("~"")`). | query | Необязательный |
| sort | string | Сортировка записей SLO:  * `name`: имена по возрастанию. * `-name`: имена по убыванию.  Если не задано, используется порядок по возрастанию. | query | Необязательный |
| timeFrame | string | Временной диапазон для вычисления значений SLO:  * `CURRENT`: собственный временной диапазон SLO. * `GTF`: временной диапазон, заданный параметрами **from** и **to**.  Если не задано, используется значение `CURRENT`. Поле может принимать значения: * `CURRENT` * `GTF` | query | Необязательный |
| demo | boolean | Получить ваши SLO (`false`) или набор демонстрационных SLO (`true`). | query | Необязательный |
| evaluate | string | Получить ваши SLO без их оценки (`false`) или с оценками (`true`) с максимальным `pageSize` 25. Поле может принимать значения: * `true` * `false` | query | Необязательный |
| enabledSlos | string | Получить ваши включённые SLO (`true`), отключённые (`false`) или и включённые, и отключённые (`all`). Поле может принимать значения: * `true` * `false` * `all` | query | Необязательный |
| showGlobalSlos | boolean | Получить ваши глобальные SLO (`true`) независимо от выбранного фильтра или отфильтровать их (`false`). | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SLOs](#openapi-definition-SLOs) | Успех. Ответ содержит параметры и вычисленные значения запрошенного SLO. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Некорректный ввод. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `SLOs`

Содержит SLO и информацию о постраничной разбивке.

| Поле | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения следующих страниц результата. |
| pageSize | integer | Количество записей на страницу. |
| slo | [SLO[]](#openapi-definition-SLO) | Список SLO. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `SLO`

Параметры цели уровня обслуживания (SLO).

| Поле | Тип | Описание |
| --- | --- | --- |
| burnRateMetricKey | string | Ключ func-метрики скорости расходования бюджета ошибок SLO. |
| ~~denominatorValue~~ | number | УСТАРЕЛО  Значение знаменателя, используемое для оценки SLO, когда **useRateMetric** имеет значение `false`. |
| description | string | Краткое описание SLO. |
| enabled | boolean | SLO включён (`true`) или отключён (`false`). |
| error | string | Ошибка вычисления SLO.  Если значение отличается от `NONE`, с вычислением SLO что-то не так. |
| errorBudget | number | Бюджет ошибок вычисленного SLO.  Бюджет ошибок это разница между вычисленным и целевым значениями. Положительное число означает, что всё хорошо; отрицательное число означает проблему.  Имеет значение оценённого бюджета ошибок или значение `-1`:  * Если есть ошибка вычисления SLO; в этом случае проверьте значение свойства **error**. * Если параметр evaluate не был установлен в `true`; в этом случае свойство **error** не будет содержать ошибки. |
| errorBudgetBurnRate | [SloBurnRate](#openapi-definition-SloBurnRate) | Оценка скорости расходования бюджета ошибок цели уровня обслуживания (SLO). |
| errorBudgetMetricKey | string | Ключ func-метрики бюджета ошибок SLO. |
| evaluatedPercentage | number | Вычисленное значение статуса SLO. Имеет значение оценённого статуса SLO или значение `-1`:  * Если есть ошибка вычисления SLO; в этом случае проверьте значение свойства **error**. * Если параметр evaluate не был установлен в `true`; в этом случае свойство **error** не будет содержать ошибки. |
| evaluationType | string | Тип оценки SLO. Поле может принимать значения: * `AGGREGATE` |
| filter | string | Фильтр сущностей для оценки SLO. Общая длина строки entitySelector в SLO ограничена 1 000 символами. Используйте [синтаксис entity selector](https://dt-url.net/entityselector). |
| id | string | ID SLO |
| ~~metricDenominator~~ | string | УСТАРЕЛО  Метрика общего количества (знаменатель в расчёте отношения).  Обязательно, когда **useRateMetric** имеет значение `false`. |
| metricExpression | string | Процентное метрическое выражение для вычисления SLO. |
| metricKey | string | Ключ func-метрики статуса SLO. |
| metricName | string | Имя, используемое для создания ключей func-метрик SLO. После создания имя метрики изменить нельзя. |
| ~~metricNumerator~~ | string | УСТАРЕЛО  Метрика количества успехов (числитель в расчёте отношения).  Обязательно, когда **useRateMetric** имеет значение `false`. |
| ~~metricRate~~ | string | УСТАРЕЛО  Процентная метрика для вычисления SLO.  Обязательно, когда **useRateMetric** имеет значение `true`. |
| name | string | Имя SLO. |
| normalizedErrorBudgetMetricKey | string | Ключ func-метрики нормализованного бюджета ошибок SLO. |
| ~~numeratorValue~~ | number | УСТАРЕЛО  Значение числителя, используемое для оценки SLO, когда **useRateMetric** имеет значение `false`. |
| ~~problemFilters~~ | string[] | УСТАРЕЛО  Фильтр сущностей для получения количества проблем, связанных с SLO. Генерируется автоматически, если к SLO не добавлен фильтр. |
| relatedOpenProblems | integer | Количество открытых проблем, связанных с SLO.  Имеет значение `-1`, если при получении связанных с SLO проблем произошла ошибка. |
| relatedTotalProblems | integer | Общее количество проблем, связанных с SLO.  Имеет значение `-1`, если при получении связанных с SLO проблем произошла ошибка. |
| status | string | Статус вычисленного SLO. Поле может принимать значения: * `FAILURE` * `SUCCESS` * `WARNING` |
| target | number | Целевое значение SLO. |
| timeframe | string | Временной диапазон для оценки SLO. Используйте синтаксис глобального селектора временного диапазона. |
| ~~useRateMetric~~ | boolean | УСТАРЕЛО  Тип метрики для вычисления SLO:  * `true`: существующая процентная метрика. * `false`: отношение двух метрик.  Список доступных метрик смотрите на [странице встроенных метрик](https://dt-url.net/be03kow) или попробуйте вызов API [GET metrics](https://dt-url.net/8e43kxf). |
| warning | number | Предупредительное значение SLO.  В состоянии предупреждения SLO ещё выполняется, но близко к нарушению. |

#### Объект `SloBurnRate`

Оценка скорости расходования бюджета ошибок цели уровня обслуживания (SLO).

| Поле | Тип | Описание |
| --- | --- | --- |
| burnRateType | string | Вычисленный тип скорости расходования.  Имеет значение 'FAST', 'SLOW' или 'NONE'. Поле может принимать значения: * `FAST` * `NONE` * `SLOW` |
| burnRateValue | number | Скорость расходования SLO, вычисленная за последний час. |
| burnRateVisualizationEnabled | boolean | Вычисление скорости расходования бюджета ошибок включено (`true`) или отключено (`false`).  В случае `false` вычисленные значения здесь отсутствуют. |
| estimatedTimeToConsumeErrorBudget | number | Оценочное оставшееся время до исчерпания бюджета ошибок, в часах. |
| fastBurnThreshold | number | Порог между медленной и быстрой скоростью расходования. |
| sloValue | number | Вычисленное значение SLO за временной диапазон, выбранный для расчёта скорости расходования. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"slo": [



{



"burnRateMetricKey": "func:slo.errorBudgetBurnRate.payment_service_availability",



"denominatorValue": 90,



"description": "Rate of successful payments per week",



"enabled": true,



"error": "NONE",



"errorBudget": 1.25,



"errorBudgetBurnRate": {



"burnRateType": "SLOW",



"burnRateValue": 1.25,



"burnRateVisualizationEnabled": true,



"estimatedTimeToConsumeErrorBudget": 24,



"fastBurnThreshold": 1.5,



"sloValue": 95



},



"errorBudgetMetricKey": "func:slo.errorBudget.payment_service_availability",



"evaluatedPercentage": 96.25,



"evaluationType": "AGGREGATE",



"filter": "type(\"SERVICE\")",



"id": "123e4567-e89b-42d3-a456-556642440000",



"metricDenominator": "builtin:service.requestCount.server",



"metricExpression": "(100)*(builtin:service.errors.server.successCount:splitBy())/(builtin:service.requestCount.server:splitBy())",



"metricKey": "func:slo.payment_service_availability",



"metricName": "payment_service_availability",



"metricNumerator": "builtin:service.errors.server.successCount",



"metricRate": "builtin:service.successes.server.rate",



"name": "Payment service availability",



"normalizedErrorBudgetMetricKey": "func:slo.normalizedErrorBudget.payment_service_availability",



"numeratorValue": 80,



"problemFilters": "[type(\"SERVICE\")]",



"relatedOpenProblems": 1,



"relatedTotalProblems": 1,



"status": "WARNING",



"target": 95,



"timeframe": "-1d",



"useRateMetric": true,



"warning": 97.5



}



],



"totalCount": 1



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Мониторинг и алертинг по service-level objectives в Dynatrace через Service-Level Objectives Classic.")