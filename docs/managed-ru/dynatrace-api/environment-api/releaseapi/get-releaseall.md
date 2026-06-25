---
title: Releases API - GET releases
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/releaseapi/get-releaseall
scraped: 2026-05-12T11:55:50.023568
---

# Releases API - GET releases

# Releases API - GET releases

* Reference
* Published Apr 20, 2021

Возвращает список всех доступных релизов.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/releases` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/releases` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `releases.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| from | string | Начало запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется относительный таймфрейм две недели (`now-2w`). | query | Optional |
| to | string | Конец запрашиваемого таймфрейма.  Можно использовать один из следующих форматов:  * Таймстамп в миллисекундах UTC. * Человекочитаемый формат `2021-01-25T05:57:01.123+01:00`. Если часовой пояс не задан, используется UTC. Вместо `T` можно использовать пробел. Секунды и доли секунды опциональны. * Относительный таймфрейм, отсчитываемый от текущего момента. Формат: `now-NU/A`, где `N` это количество, `U` единица времени, `A` выравнивание. Выравнивание округляет все меньшие значения до ближайшего нуля в прошлом. Например, `now-1y/w` это год назад с выравниванием по неделе.   Также можно указать относительный таймфрейм без выравнивания: `now-NU`.   Поддерживаемые единицы времени для относительного таймфрейма: + `m`: минуты   + `h`: часы   + `d`: дни   + `w`: недели   + `M`: месяцы   + `y`: годы  Если не задано, используется текущий таймстамп. | query | Optional |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница всегда возвращается, если query-параметр **nextPageKey** не указан.  Если **nextPageKey** задан для получения последующих страниц, все остальные query-параметры должны быть опущены. | query | Optional |
| pageSize | integer | Количество Releases в одном payload ответа.  Максимально допустимый размер страницы: 1000.  Если не задано, используется 100. | query | Optional |
| demo | boolean | Получить ваши Releases (`false`) или набор демо-Releases (`true`). | query | Optional |
| releasesSelector | string | Определяет область запроса. Только Releases, соответствующие указанным критериям, включаются в ответ.  Можно добавить один или несколько критериев из списка ниже.  * Management zone: type(PROCESS\_GROUP\_INSTANCE),mzName("ManagementZone-A"). Фильтрует все releases в указанной management zone. Фильтр чувствителен к регистру. * Monitoring state: monitoringState("Active") или monitoringState("Inactive"). Можно указать только одно состояние мониторинга. * Health state: healthState("HEALTHY") или healthState("UNHEALTHY"). Можно указать только одно health state. * Security vulnerability: affectedBySecurityProblem("Detected") или affectedBySecurityProblem("Not detected"). Можно указать только одно состояние security vulnerability. * Name: entityName("name"). Фильтрует все releases, содержащие указанное значение в имени. Фильтр нечувствителен к регистру. * Entity ID: entityId("id"). * Product: releasesProduct("product"). Фильтрует все releases, содержащие указанное значение в product. Фильтр нечувствителен к регистру. * Stage: releasesStage("stage"). Фильтрует все releases, содержащие указанное значение в stage. Фильтр нечувствителен к регистру. * Version: releasesVersion("version"). Фильтрует все releases, содержащие указанное значение в version. Фильтр нечувствителен к регистру.  Для задания нескольких критериев разделяйте их запятыми (,). В ответ включаются только результаты, соответствующие всем критериям. Например, .../api/v2/releases?releasesSelector=name("Server"),monitoringState("Active"),healthState("HEALTHY"),releasesVersion("1.0.7").  Спецсимволы ~ и " нужно экранировать через ~ (например, поиск двойной кавычки: entityName("~""). | query | Optional |
| sort | string | Указывает поле, используемое для сортировки списка releases. У поля есть префикс знака (+/-), соответствующий направлению сортировки ('+' для возрастания, '-' для убывания). Если префикс не задан, применяется сортировка по возрастанию. Можно сортировать по следующим свойствам:  * 'product': Имя продукта * 'name': Имя release * 'stage': Имя stage * 'version': Версия * 'instances': Экземпляры * 'traffic': Трафик  Если не задано, применяется сортировка по возрастанию по полю name. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Releases](#openapi-definition-Releases) | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `Releases`

Список releases.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| releases | [Release[]](#openapi-definition-Release) | Список releases. |
| releasesWithProblems | integer | Количество releases с проблемами. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `Release`

Содержит данные об одном release компонента.
Release это комбинация компонента и версии.
Компонент может быть любой формой развёртываемого артефакта, который можно связать с версией.
В первом черновике компонент всегда является Service.

Кортеж <name, product, stage, version> всегда уникален.

| Элемент | Тип | Описание |
| --- | --- | --- |
| affectedByProblems | boolean | У сущности есть одна или несколько проблем. |
| affectedBySecurityVulnerabilities | boolean | У сущности есть одна или несколько security vulnerabilities. |
| instances | [ReleaseInstance[]](#openapi-definition-ReleaseInstance) | entityIds экземпляров, входящих в этот release. |
| name | string | Имя сущности. |
| problemCount | integer | Количество проблем сущности. |
| product | string | Имя продукта. |
| releaseEntityId | string | Entity id соответствующего release. |
| running | boolean | Связанный PGI всё ещё работает/отслеживается. |
| securityVulnerabilitiesCount | integer | Количество security vulnerabilities сущности. |
| securityVulnerabilitiesEnabled | boolean | Указывает, что включена функция security vulnerabilities. |
| softwareTechs | [SoftwareTechs[]](#openapi-definition-SoftwareTechs) | Программные технологии release. |
| stage | string | Имя stage. |
| throughput | number | Количество байт в секунду сущности. |
| version | string | Идентифицированная версия release. |

#### Объект `ReleaseInstance`

Содержит данные об одном экземпляре release.
Экземпляр это Process Group Instance с опциональной build version.

| Элемент | Тип | Описание |
| --- | --- | --- |
| buildVersion | string | Build version. |
| entityId | string | Entity id экземпляра. |
| problems | string[] | Список event ID открытых проблем. |
| securityVulnerabilities | string[] | Список ID security vulnerabilities. |

#### Объект `SoftwareTechs`

Содержит информацию об используемой программной технологии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| edition | string | Edition технологии. |
| technology | string | Тип технологии. |
| verbatimType | string | Verbatim-тип технологии. |
| version | string | Версия технологии. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"releases": [



{



"affectedByProblems": true,



"affectedBySecurityVulnerabilities": true,



"instances": [



"PROCESS_GROUP_INSTANCE-49D94B90FB71C45B",



"PROCESS_GROUP_INSTANCE-7EA049157C82D1A5"



],



"name": "cluster",



"problemCount": 4,



"product": "Sockshop",



"releaseEntityId": "PROCESS_GROUP-DFDBAC9CBF104253",



"running": true,



"securityVulnerabilitiesCount": 4,



"securityVulnerabilitiesEnabled": true,



"softwareTechs": [



{



"edition": "OpenJDK",



"technology": "JAVA",



"verbatimType": "Java",



"version": "1.8.0_242"



}



],



"stage": "staging",



"throughput": 923234,



"version": "1.195.34.12341232423-012342"



}



],



"releasesWithProblems": 1,



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

* [Release monitoring](/managed/deliver/release-monitoring "Обнаружение версий отслеживаемых приложений и анализ жизненного цикла программного продукта.")