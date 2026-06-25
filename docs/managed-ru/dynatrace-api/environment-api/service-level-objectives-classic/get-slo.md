---
title: Service-level Objectives API - GET SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/get-slo
scraped: 2026-05-12T11:57:37.162047
---

# Service-level Objectives API - GET SLO

# Service-level Objectives API - GET SLO

* Справочник
* Обновлено 7 января 2025 г.

Возвращает параметры указанной цели уровня обслуживания (SLO) classic.

Если указаны параметры **from** и **to**, SLO вычисляется для этого временного диапазона; иначе используется собственный временной диапазон SLO.

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `slo.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный диапазон в две недели (`now-2w`). | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона.  Можно использовать один из следующих форматов:  * Метка времени в UTC миллисекундах. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не указан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды необязательны. * Относительный диапазон, назад от текущего момента. Формат `now-NU/A`, где `N` это количество времени, `U` это единица времени, а `A` это выравнивание. Выравнивание округляет все меньшие значения к ближайшему нулю в прошлом. Например, `now-1y/w` это один год назад, выровненный по неделе.   Можно также указать относительный диапазон без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного диапазона:  + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущая метка времени. | query | Необязательный |
| id | string | ID требуемого SLO. | path | Обязательный |
| timeFrame | string | Временной диапазон для вычисления значений SLO:  * `CURRENT`: собственный временной диапазон SLO. * `GTF`: временной диапазон, заданный параметрами **from** и **to**.  Если не задано, используется значение `CURRENT`. Поле может принимать значения: * `CURRENT` * `GTF` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SLO](#openapi-definition-SLO) | Успех. Ответ содержит параметры и вычисленные значения запрошенного SLO. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Некорректный ввод. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

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