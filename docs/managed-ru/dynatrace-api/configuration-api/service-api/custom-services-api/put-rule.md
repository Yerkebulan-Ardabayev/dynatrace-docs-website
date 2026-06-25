---
title: Custom services API - PUT a custom service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/put-rule
scraped: 2026-05-12T11:18:10.213789
---

# Custom services API - PUT a custom service rule

# Custom services API - PUT a custom service rule

* Reference
* Published Sep 02, 2019

## PUT a custom service rule

Обновляет указанное правило пользовательского сервиса.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Технология пользовательского сервиса для обновления. Возможные значения: * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| id | string | ID пользовательского сервиса для обновления.  ID пользовательского сервиса в теле запроса должен совпадать с этим ID. | path | Required |
| body | [CustomService](#openapi-definition-CustomService) | JSON-тело запроса, содержащее обновлённое определение пользовательского сервиса. Если присутствует *order*, оно будет использовано. | body | Optional |

### Объекты тела запроса

#### Объект `CustomService`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Пользовательский сервис включён/отключён. | Required |
| id | string | ID пользовательского сервиса. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| name | string | Имя пользовательского сервиса, отображаемое в UI. | Required |
| order | string | Строка порядка. Сортировка пользовательских сервисов в алфавитном порядке по их строке порядка определяет их относительный порядок.  Обычно этим управляет Dynatrace внутренне, и строка не присутствует в ответах GET. | Optional |
| processGroups | string[] | Список групп процессов, к которым должен принадлежать пользовательский сервис. | Optional |
| queueEntryPoint | boolean | Флаг точки входа очереди.  Установите `true` для пользовательских сервисов обмена сообщениями. | Required |
| queueEntryPointType | string | Тип точки входа очереди.. Возможные значения: * `AWS_SQS` * `AZURE_SERVICE_BUS` * `IBM_MQ` * `JMS` * `KAFKA` * `MSMQ` * `RABBIT_MQ` | Optional |
| rules | [DetectionRule[]](#openapi-definition-DetectionRule) | Список правил, определяющих пользовательский сервис. | Required |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `DetectionRule`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| annotations | string[] | Дополнительный фильтр аннотаций правила.  Инструментируются только классы, в которых все перечисленные аннотации присутствуют в самом классе или в любом из его суперклассов.  Не применяется к PHP. | Optional |
| className | string | Полностью квалифицированный класс или интерфейс для инструментирования.  Обязательно для пользовательских сервисов Java и .NET.  Не применяется к PHP. | Optional |
| enabled | boolean | Правило включено/отключено. | Required |
| fileName | string | PHP-файл, содержащий класс или методы для инструментирования.  Обязательно для пользовательского сервиса PHP.  Не применяется к Java и .NET. | Optional |
| fileNameMatcher | string | Сопоставитель, применяемый к имени файла. Значение по умолчанию `ENDS_WITH` (если применимо). Возможные значения: * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| id | string | ID правила обнаружения. | Optional |
| matcher | string | Сопоставитель, применяемый к имени класса. `STARTS_WITH` можно использовать, только если определена хотя бы одна аннотация. Значение по умолчанию `EQUALS`. Возможные значения: * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` | Optional |
| methodRules | [MethodRule[]](#openapi-definition-MethodRule) | Список методов для инструментирования. | Required |

#### Объект `MethodRule`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| argumentTypes | string[] | Полностью квалифицированные типы аргументов, которые ожидает метод. | Optional |
| id | string | ID правила метода. | Optional |
| methodName | string | Метод для инструментирования. | Required |
| modifiers | string[] | Модификаторы правила метода. Возможные значения: * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` | Optional |
| returnType | string | Полностью квалифицированный тип, возвращаемый методом. | Required |
| visibility | string | Видимость правила метода. Возможные значения: * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"enabled": true,



"name": "CustomService",



"queueEntryPoint": false,



"rules": [



{



"className": "com.your.company.ClassName",



"enabled": true,



"methodRules": [



{



"argumentTypes": [



"java.lang.String"



],



"methodName": "AMethod",



"returnType": "void"



}



]



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Пользовательский сервис создан. Тело ответа содержит ID и имя нового сервиса. |
| **204** | - | Успех. Пользовательский сервис обновлён. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

## Validate payload

{snippet name='dynatrace-api/validate-payload.md'}}

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.")