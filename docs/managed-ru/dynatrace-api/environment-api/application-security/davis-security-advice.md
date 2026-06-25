---
title: Davis Security Advisor API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/davis-security-advice
scraped: 2026-05-12T11:12:28.921931
---

# Davis Security Advisor API

# Davis Security Advisor API

* Reference
* Updated on May 03, 2022

API **Davis Security Advisor** возвращает [рекомендации Davis](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Получите рекомендации по исправлениям безопасности от Davis Security Advisor."), связанные с открытыми и не заглушенными [уязвимостями](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Отслеживайте проблемы безопасности в ваших сторонних библиотеках.").

Вы можете ограничить вывод с помощью пагинации:

1. Укажите количество результатов на странице в query-параметре **pageSize**.
2. Затем используйте курсор из поля **nextPageKey** предыдущего ответа в query-параметре **nextPageKey** для получения последующих страниц.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/davis/securityAdvices` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/davis/securityAdvices` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `securityProblems.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| managementZoneFilter | string | Чтобы указать management zones, используйте один из вариантов ниже. Для каждого варианта можно указать несколько значений через запятую. Если указано несколько значений, применяется логика **OR**. Все значения регистрозависимы и должны быть в кавычках.  * Management zone ID: ids("mzId-1", "mzId-2"). * Имена management zone: names("mz-1", "mz-2").  Можно указать несколько критериев через запятую (например, `names("myMz"),ids("9130632296508575249")`). | query | Опциональный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Первая страница возвращается всегда, если параметр **nextPageKey** не указан.  Когда **nextPageKey** установлен для получения последующих страниц, все остальные query-параметры должны быть опущены. | query | Опциональный |
| pageSize | integer | Количество рекомендаций безопасности в одном payload ответа.  Максимально допустимый размер страницы 500.  Если не задано, используется 5. | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DavisSecurityAdviceList](#openapi-definition-DavisSecurityAdviceList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `DavisSecurityAdviceList`

Список рекомендаций от Davis security advisor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| advices | [DavisSecurityAdvice[]](#openapi-definition-DavisSecurityAdvice) | - |
| nextPageKey | string | Курсор для следующей страницы результатов. Имеет значение `null` на последней странице.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `DavisSecurityAdvice`

Рекомендация безопасности от Davis security advisor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| adviceType | string | Тип рекомендации. Элемент может принимать значения * `UPGRADE` |
| critical | string[] | ID [security problems](https://dt-url.net/p103u1h) уровня `critical`, вызванных уязвимым компонентом. |
| high | string[] | ID [security problems](https://dt-url.net/p103u1h) уровня `high`, вызванных уязвимым компонентом. |
| low | string[] | ID [security problems](https://dt-url.net/p103u1h) уровня `low`, вызванных уязвимым компонентом. |
| medium | string[] | ID [security problems](https://dt-url.net/p103u1h) уровня `medium`, вызванных уязвимым компонентом. |
| name | string | Имя рекомендации. |
| none | string[] | ID [security problems](https://dt-url.net/p103u1h) уровня `none`, вызванных уязвимым компонентом. |
| technology | string | Технология уязвимого компонента. Элемент может принимать значения * `DOTNET` * `GO` * `JAVA` * `KUBERNETES` * `NODE_JS` * `PHP` * `PYTHON` |
| vulnerableComponent | string | Уязвимый компонент, к которому применяется рекомендация. |

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



"advices": [



{



"adviceType": "UPGRADE",



"critical": [



"string"



],



"high": [



"string"



],



"low": [



"string"



],



"medium": [



"string"



],



"name": "string",



"none": [



"string"



],



"technology": "DOTNET",



"vulnerableComponent": "string"



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



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

* [Application Security](/managed/secure/application-security "Доступ к функциям Dynatrace Application Security.")
* [Vulnerabilities API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Узнайте, что предлагает API уязвимостей.")