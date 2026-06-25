---
title: Dynatrace API - Коды ответа
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/dynatrace-api-response-codes
scraped: 2026-05-12T11:03:39.713479
---

# Dynatrace API - Коды ответа

# Dynatrace API - Коды ответа

* Reference
* Published Sep 13, 2018

Если не указано иное, используются следующие коды ответа:

| Код | Описание |
| --- | --- |
| 200 | **OK**. Запрос выполнен успешно. |
| 400 | **Bad request**. Запрос завершился ошибкой. Подробности в теле ответа. |
| 401 | **Unauthorized.** Не удалось аутентифицировать токен. Проверьте, есть ли у токена [необходимые scopes](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для работы с Dynatrace API."). |
| 404 | **Not found**. Запрашиваемый ресурс не найден в вашем окружении. Проверьте корректность ввода. |
| 429 | **Too many requests**. Достигнут [лимит](/managed/dynatrace-api/basics/access-limit "Лимиты payload и дросселирование запросов, которые могут влиять на использование Dynatrace API.") использования API. |

## Configuration API

[Configuration API](/managed/dynatrace-api/configuration-api "Что нужно для работы с configuration-секцией Dynatrace API.") использует немного другой набор кодов ответа. Применяются следующие коды:

| Код | Описание |
| --- | --- |
| 200 | **OK**. GET-запрос выполнен успешно. |
| 201 | **Created**. POST- или PUT-запрос успешно создал новый ресурс. |
| 204 | **No content**. PUT- или DELETE-запрос успешно обновил или удалил ресурс. |
| 400 | **Bad request**. Запрос завершился ошибкой. Подробности в теле ответа. |
| 401 | **Unauthorized.** Не удалось аутентифицировать токен. Проверьте, есть ли у токена [необходимые scopes](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для работы с Dynatrace API."). |
| 404 | **Not found**. Запрашиваемый ресурс не найден в вашем окружении. Проверьте корректность ввода. |
| 429 | **Too many requests**. Достигнут [лимит](/managed/dynatrace-api/basics/access-limit "Лимиты payload и дросселирование запросов, которые могут влиять на использование Dynatrace API.") использования API. |

Если успешный запрос может возвращать разные коды, это указано в описании запроса.