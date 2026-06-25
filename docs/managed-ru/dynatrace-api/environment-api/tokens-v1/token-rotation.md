---
title: Реализация ротации токенов
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/token-rotation
scraped: 2026-05-12T12:11:21.787932
---

# Реализация ротации токенов

# Реализация ротации токенов

* Справочник
* Обновлено 17 мая 2022 г.

Регулярная смена пароля, это хорошая практика безопасности. То же касается токенов аутентификации Dynatrace API.

С помощью Tokens API вы можете автоматизировать ротацию.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Получение ID старого токена**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#get-old "Узнайте, как использовать Dynatrace API для регулярной ротации токенов аутентификации Dynatrace API в вашей среде.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создание нового токена**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#create-new "Узнайте, как использовать Dynatrace API для регулярной ротации токенов аутентификации Dynatrace API в вашей среде.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Отзыв старого токена**  
Не удаляйте его до того, как отзовёте.](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#revoke-old "Узнайте, как использовать Dynatrace API для регулярной ротации токенов аутентификации Dynatrace API в вашей среде.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Удаление старого токена**](/managed/dynatrace-api/environment-api/tokens-v1/token-rotation#delete-old "Узнайте, как использовать Dynatrace API для регулярной ротации токенов аутентификации Dynatrace API в вашей среде.")

В качестве примера рабочего процесса предположим, что вы хотите ротировать токен со следующими параметрами:

* Имя токена, это **RW config token**.
* Scope токена включает **ReadConfig** и **WriteConfig**.
* Срок действия токена, 30 дней (**2 592 000** секунд).
* Текущий токен, это **0987654321jihgfedcba**.
* Текущий токен создан **6 марта 2019** и истекает **5 апреля 2019**.

## Шаг 1 Получение ID старого токена

Если вам известен только сам токен, нужно получить его ID, чтобы отозвать и впоследствии удалить его. Для этого выполните запрос [POST token lookup](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Узнайте, как использовать Dynatrace API для поиска метаданных токена аутентификации Dynatrace API.") с удаляемым токеном в качестве payload.

Запрос возвращает метаданные токена, включая его ID, который понадобится позже.

#### Запрос

Отправьте POST-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/lookup
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/lookup

Включите этот payload `application/json`, где `0987654321jihgfedcba`, это значение токена:

```
{



"token": "0987654321jihgfedcba"



}
```

#### Ответ

Запрос возвращает метаданные токена в payload `application/json`:

```
{



"id": "a6e91657-1fa7-4742-af40-39469b92bd65",



"name": "RW config token",



"userId": "admin@mysampleenv.com",



"created": "2019-03-06T09:15:49Z",



"expires": "2019-04-05T09:15:49Z",



"scopes": [



"ReadConfig",



"WriteConfig"



]



}
```

Вам нужно получить значение **id** токена, которое понадобится, чтобы вывести из эксплуатации (отозвать и удалить) этот токен.

## Шаг 2 Создание нового токена

Чтобы создать новый токен, который заменит устаревший, выполните запрос [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Узнайте, как использовать Dynatrace API для создания нового токена аутентификации Dynatrace API."). Поскольку вы создаёте токен с одними и теми же параметрами на регулярной основе, можно рассмотреть хранение его конфигурации в системе контроля версий.

#### Запрос

Отправьте POST-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens

Включите этот payload `application/json`:

```
{



"name": "RW config token",



"scopes": [



"WriteConfig",



"ReadConfig"



],



"expiresIn": {



"value": 30,



"unit": "DAYS"



}



}
```

#### Ответ

Запрос возвращает новый токен в payload `application/json`:

```
{



"token": "jihgfedcba0987654321"



}
```

## Шаг 3 Отзыв старого токена

Чтобы отозвать старый токен, выполните [PUT an existing token](/managed/dynatrace-api/environment-api/tokens-v1/put-token "Узнайте, как использовать Dynatrace API для обновления токена аутентификации Dynatrace API."). Вам понадобится значение **id** токена, полученное на [шаге 1](#get-old).

Отозванный токен нельзя использовать для аутентификации, но он всё ещё существует в вашей среде. Мы рекомендуем подождать неделю перед удалением отозванного токена на случай экстренной необходимости в нём. Точную задержку уточните в политиках безопасности вашей организации.

Если вы хотите ротировать токен, который сейчас используете для аутентификации вызовов API, замените его новым токеном, который вы только что создали на [шаге 2](#create-new).

В нашем примере ID отзываемого токена, это **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Запрос

Отправьте PUT-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

Включите этот payload `application/json`:

```
{



"revoked": true



}
```

#### Ответ

Об успешном запросе сигнализирует код ответа **204**. Он не возвращает никакого содержимого.

## Шаг 4 Удаление старого токена

По истечении периода ожидания, когда старый токен отключён (отозван), удалите его. Для этого выполните [DELETE an existing token](/managed/dynatrace-api/environment-api/tokens-v1/delete-token "Узнайте, как удалить токен аутентификации Dynatrace API с помощью Dynatrace API."). Вам понадобится **ID** токена, полученный на [шаге 1](#get-old).

В нашем примере ID удаляемого токена, это **a6e91657-1fa7-4742-af40-39469b92bd65**.

#### Запрос

Отправьте DELETE-запрос на этот URL:

* Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65
* Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/tokens/a6e91657-1fa7-4742-af40-39469b92bd65

#### Ответ

Об успешном запросе сигнализирует код ответа **204**. Он не возвращает никакого содержимого.