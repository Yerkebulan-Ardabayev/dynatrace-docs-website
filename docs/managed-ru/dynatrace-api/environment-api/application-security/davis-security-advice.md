---
title: Davis Security Advisor API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/application-security/davis-security-advice
---

# Davis Security Advisor API

# Davis Security Advisor API

* Справочник
* Обновлено 03 мая 2022

**Davis Security Advisor** API выводит список [рекомендаций Davis](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.") по открытым и не отключённым [уязвимостям](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.").

Объём вывода можно ограничить с помощью пагинации:

1. Указать количество результатов на странице в параметре запроса **pageSize**.
2. Затем использовать курсор из поля **nextPageKey** предыдущего ответа в параметре запроса **nextPageKey**, чтобы получить последующие страницы.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/davis/securityAdvices` |
| GET | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/davis/securityAdvices` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `securityProblems.read`.

О том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| managementZoneFilter | string | Для указания management zones нужно использовать один из вариантов ниже. Для каждого варианта можно указать несколько значений через запятую. Если указано несколько значений, применяется логика **OR**. Все значения чувствительны к регистру и должны быть в кавычках.  * ID management zone: ids("mzId-1", "mzId-2"). * Названия management zone: names("mz-1", "mz-2").  Можно указать несколько критериев через запятую (например, `names("myMz"),ids("9130632296508575249")`). | query | Необязательный |
| nextPageKey | string | Курсор для следующей страницы результатов. Его можно найти в поле **nextPageKey** предыдущего ответа.  Если параметр запроса **nextPageKey** не указан, всегда возвращается первая страница.  Когда **nextPageKey** задан для получения последующих страниц, все остальные параметры запроса нужно опустить. | query | Необязательный |
| pageSize | integer | Количество рекомендаций по безопасности в одном ответе.  Максимально допустимый размер страницы: 500.  Если не задано, используется значение 5. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DavisSecurityAdviceList](#openapi-definition-DavisSecurityAdviceList) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `DavisSecurityAdviceList`

Список рекомендаций от Davis security advisor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| advices | [DavisSecurityAdvice](#openapi-definition-DavisSecurityAdvice)[] | - |
| nextPageKey | string | Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используется в параметре запроса **nextPageKey** для получения последующих страниц результата. |
| pageSize | integer | Количество записей на странице. |
| totalCount | integer | Общее количество записей в результате. |

#### Объект `DavisSecurityAdvice`

Рекомендация от Davis security advisor.

| Элемент | Тип | Описание |
| --- | --- | --- |
| adviceType | string | Тип рекомендации. Элемент может принимать следующие значения * `UPGRADE` |
| critical | string[] | ID [проблем безопасности﻿](https://dt-url.net/p103u1h?dt=m) уровня `critical`, вызванных уязвимым компонентом. |
| high | string[] | ID [проблем безопасности﻿](https://dt-url.net/p103u1h?dt=m) уровня `high`, вызванных уязвимым компонентом. |
| low | string[] | ID [проблем безопасности﻿](https://dt-url.net/p103u1h?dt=m) уровня `low`, вызванных уязвимым компонентом. |
| medium | string[] | ID [проблем безопасности﻿](https://dt-url.net/p103u1h?dt=m) уровня `medium`, вызванных уязвимым компонентом. |
| name | string | Название рекомендации. |
| none | string[] | ID [проблем безопасности﻿](https://dt-url.net/p103u1h?dt=m) уровня `none`, вызванных уязвимым компонентом. |
| technology | string | Технология уязвимого компонента. Элемент может принимать следующие значения * `DOTNET` * `GO` * `JAVA` * `KUBERNETES` * `NODE_JS` * `PHP` * `PYTHON` |
| vulnerableComponent | string | Уязвимый компонент, к которому относится рекомендация. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела ответа JSON

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

* [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")
* [Уязвимости API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")