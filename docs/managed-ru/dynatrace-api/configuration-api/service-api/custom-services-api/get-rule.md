---
title: Custom services API - GET a custom service rule
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/custom-services-api/get-rule
scraped: 2026-05-12T11:18:08.437767
---

# Custom services API - GET a custom service rule

# Custom services API - GET a custom service rule

* Reference
* Published Sep 02, 2019

Возвращает параметры указанного правила пользовательского сервиса.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/customServices/{technology}/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| technology | string | Технология запрашиваемого пользовательского сервиса. Возможные значения: * `dotNet` * `go` * `java` * `nodeJS` * `php` | path | Required |
| id | string | ID запрашиваемого пользовательского сервиса. | path | Required |
| includeProcessGroupReferences | boolean | Флаг включения ссылок на группы процессов в ответ.  Ссылки на группы процессов несовместимы между окружениями.  Если значение не задано, используется `false`. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CustomService](#openapi-definition-CustomService) | Успех |

### Объекты тела ответа

#### Объект `CustomService`

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Пользовательский сервис включён/отключён. |
| id | string | ID пользовательского сервиса. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| name | string | Имя пользовательского сервиса, отображаемое в UI. |
| order | string | Строка порядка. Сортировка пользовательских сервисов в алфавитном порядке по их строке порядка определяет их относительный порядок.  Обычно этим управляет Dynatrace внутренне, и строка не присутствует в ответах GET. |
| processGroups | string[] | Список групп процессов, к которым должен принадлежать пользовательский сервис. |
| queueEntryPoint | boolean | Флаг точки входа очереди.  Установите `true` для пользовательских сервисов обмена сообщениями. |
| queueEntryPointType | string | Тип точки входа очереди.. Возможные значения: * `AWS_SQS` * `AZURE_SERVICE_BUS` * `IBM_MQ` * `JMS` * `KAFKA` * `MSMQ` * `RABBIT_MQ` |
| rules | [DetectionRule[]](#openapi-definition-DetectionRule) | Список правил, определяющих пользовательский сервис. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `DetectionRule`

| Элемент | Тип | Описание |
| --- | --- | --- |
| annotations | string[] | Дополнительный фильтр аннотаций правила.  Инструментируются только классы, в которых все перечисленные аннотации присутствуют в самом классе или в любом из его суперклассов.  Не применяется к PHP. |
| className | string | Полностью квалифицированный класс или интерфейс для инструментирования.  Обязательно для пользовательских сервисов Java и .NET.  Не применяется к PHP. |
| enabled | boolean | Правило включено/отключено. |
| fileName | string | PHP-файл, содержащий класс или методы для инструментирования.  Обязательно для пользовательского сервиса PHP.  Не применяется к Java и .NET. |
| fileNameMatcher | string | Сопоставитель, применяемый к имени файла. Значение по умолчанию `ENDS_WITH` (если применимо). Возможные значения: * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| id | string | ID правила обнаружения. |
| matcher | string | Сопоставитель, применяемый к имени класса. `STARTS_WITH` можно использовать, только если определена хотя бы одна аннотация. Значение по умолчанию `EQUALS`. Возможные значения: * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| methodRules | [MethodRule[]](#openapi-definition-MethodRule) | Список методов для инструментирования. |

#### Объект `MethodRule`

| Элемент | Тип | Описание |
| --- | --- | --- |
| argumentTypes | string[] | Полностью квалифицированные типы аргументов, которые ожидает метод. |
| id | string | ID правила метода. |
| methodName | string | Метод для инструментирования. |
| modifiers | string[] | Модификаторы правила метода. Возможные значения: * `ABSTRACT` * `EXTERN` * `FINAL` * `NATIVE` * `STATIC` |
| returnType | string | Полностью квалифицированный тип, возвращаемый методом. |
| visibility | string | Видимость правила метода. Возможные значения: * `INTERNAL` * `PACKAGE_PROTECTED` * `PRIVATE` * `PROTECTED` * `PUBLIC` |

### JSON-модели тела ответа

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

## Связанные темы

* [Define custom services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.")