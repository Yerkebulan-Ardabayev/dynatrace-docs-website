---
title: Безопасность ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-security
---

# Безопасность ActiveGate

# Безопасность ActiveGate

* Чтение: 8 мин
* Опубликовано 08 июля 2022 г.

## Пользовательский сертификат для ActiveGate

Для повышения безопасности рекомендуется использовать пользовательские сертификаты для ActiveGate.

См. [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

## Токены

Убедитесь, что в среде применяется принудительное использование токенов ActiveGate. Для этого [проверьте статус использования токенов ActiveGate](#determine-status-of-active-gate-token-usage) и примите меры по результату.

### Переход на токены ActiveGate

Чтобы перейти на безопасность на основе токенов ActiveGate, сначала определите статус использования токенов ActiveGate.

#### Определение статуса использования токенов ActiveGate

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Просмотрите сообщения на странице **Network security** и устраните проблемы, как описано ниже.

##### Действия не требуются

Если Dynatrace отображает такое сообщение:

![Принудительное использование токенов ActiveGate включено](https://dt-cdn.net/images/updated-ss-1-582-2d81cc06ad.png)

Принудительное использование токенов ActiveGate включено

* Никаких действий не требуется. Принудительное использование токенов ActiveGate включено, всё готово.
* Подключаться к Dynatrace могут только ActiveGate с действительными токенами ActiveGate.

##### Устранение проблем с токенами ActiveGate

Если Dynatrace отображает такое сообщение:

![Проблемы с токенами ActiveGate](https://dt-cdn.net/images/updated-ss-2-584-c069a85f68.png)

Проблемы с токенами ActiveGate

* Принудительное использование токенов ActiveGate пока не включено, и часть ActiveGate использует недействительные токены.
* Нужно устранить проблемы в зависимости от [статуса](#statuses). В противном случае такие ActiveGate потеряют соединение после включения принудительного использования токенов ActiveGate.

##### Немедленное принудительное включение токенов ActiveGate

Если Dynatrace отображает такое сообщение:

![Ручное принудительное включение токенов ActiveGate](https://dt-cdn.net/images/manual-enforcement-580-5c1b3dbaf4.webp)

Ручное принудительное включение токенов ActiveGate

* Есть возможность немедленно включить принудительное использование токенов ActiveGate. Это можно сделать в любой момент, независимо от того, сообщают ли ActiveGate о проблемах с токенами, но сначала обязательно прочитайте раздел [Ручное принудительное включение токенов ActiveGate](#manual) ниже. Все ActiveGate со статусом, отличным от **Valid**, потеряют соединение с Dynatrace.

### Типы токенов ActiveGate

Токены ActiveGate бывают двух типов:

* **Seed-токен**, seed-токен ActiveGate автоматически встраивается в установщик ActiveGate при загрузке установщика через веб-интерфейс Dynatrace или [Dynatrace API](/managed/dynatrace-api/environment-api/deployment/activegate "Загрузка установщиков ActiveGate через Dynatrace API.").
* **Индивидуальный токен**, при первом подключении ActiveGate к кластеру Dynatrace исходный seed-токен ActiveGate заменяется автоматически сгенерированным индивидуальным токеном ActiveGate. Один и тот же установщик можно использовать многократно: исходный seed-токен ActiveGate позволяет создавать несколько индивидуальных токенов ActiveGate.

### Структура токена ActiveGate

Формат токена ActiveGate состоит из трёх частей, разделённых точками (`.`).

Пример:

`dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E`

| Часть | Название | Описание |
| --- | --- | --- |
| 1 | **prefix** | Первая часть (`dt0g02` в примере выше), это **префикс** токена. Он определяет тип токена. |
| 2 | **public** | Вторая часть (`4KWZO5EF` в примере выше), это 8-символьная **публичная** часть токена.  Вместе префикс и публичная часть составляют **идентификатор токена**.  Идентификатор токена можно безопасно отображать в веб-интерфейсе и использовать для целей логирования. |
| 3 | **secret** | Третья часть (`XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E` в примере выше), это 64-символьная **секретная** часть токена.  К секретной части нужно относиться как к паролю. Она не должна отображаться в Dynatrace (после первоначального создания) и не должна сохраняться в файлах журнала. |

### Принудительное использование токенов ActiveGate

Все ActiveGate уже были постепенно переведены на использование токенов ActiveGate в ходе обновлений ActiveGate, начиная с версии ActiveGate 1.225.

Чтобы проверить, у каких ActiveGate включены токены ActiveGate:

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. ActiveGate можно фильтровать по следующим статусам токенов ActiveGate, подробнее см. [Статус токена ActiveGate](#statuses).

   * Absent
   * Expiring
   * Invalid
   * Unknown
   * Valid
   * Unsupported

#### Автоматическое принудительное включение токенов ActiveGate

Если все ActiveGate готовы к сетевой безопасности на основе токенов в течение 30 дней, среда автоматически переключится на сетевую безопасность на основе токенов ActiveGate.

#### Ручное принудительное включение токенов ActiveGate

Если нужно ускорить процесс и есть уверенность, что в среде используются только ActiveGate версии 1.225+, можно принудительно переключиться на токены ActiveGate в любой удобный момент.

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Включите **Manually enforce ActiveGate token authentication**.

* При включении **Manually enforce ActiveGate token authentication** и сохранении изменений все ActiveGate со статусом, отличным от **Valid**, потеряют соединение с Dynatrace.
* На отказ от ручного принудительного включения (отключение **Manually enforce ActiveGate token authentication**) даётся максимум 30 дней с момента обнаружения последнего недействительного токена. Например, если последний недействительный токен был обнаружен 20 дней назад, есть ещё 10 дней на отказ от принудительного включения. По истечении переходного периода переключатель отключается (то есть выключить его уже нельзя).

#### Переходный период

Переходный период в 30 дней предназначен для предотвращения потери данных от ActiveGate, на которых новые токены в среде ещё не реализованы.

В течение этого периода при обнаружении любой попытки подключения без токена ActiveGate:

* Принудительное использование токенов ActiveGate не будет включено, и всем ActiveGate будет разрешено подключаться к кластеру Dynatrace (потребуются только tenant-токены).
* Переходный период сбрасывается на 30 дней, принудительное использование токенов ActiveGate будет включено автоматически не раньше, чем через 30 дней с этого момента.

### Статус токена ActiveGate

Если ActiveGate не используют действительные токены ActiveGate, можно проверить причину недействительности токенов.

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. Выберите **Check ActiveGate token statuses**.

   Эта опция доступна только при наличии проблем с токенами ActiveGate.

В зависимости от статуса может потребоваться выполнить определённые действия для перехода на сетевую безопасность на основе токенов ActiveGate.

#### Absent

Версия ActiveGate поддерживает токены ActiveGate, но для связи всё ещё используется tenant-токен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Expiring

Срок действия токена ActiveGate истекает через 30 дней или менее. Если в среде включено принудительное использование токенов ActiveGate, ActiveGate потеряет соединение после истечения срока действия токена.

#### Invalid

ActiveGate настроен на использование токена ActiveGate, но формат недействителен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Unknown

ActiveGate настроен на использование токена ActiveGate, и формат токена действителен, но токен не распознаётся кластером Dynatrace. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Valid

ActiveGate использует для аутентификации действительный токен ActiveGate.

#### Unsupported

Версия ActiveGate 1.223 или более ранняя; сетевая безопасность на основе токенов ActiveGate поддерживается для ActiveGate версии 1.225+.

### Генерация и настройка токена ActiveGate

* Если ActiveGate развёрнут как [StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet."), нужно [сгенерировать токен ActiveGate](#generate-individual) и добавить его в конфигурацию.

  + Seed-токен ActiveGate нельзя использовать для контейнеризированных ActiveGate.
  + Токен ActiveGate можно использовать совместно для нескольких ActiveGate в рамках одной среды.
* Если ActiveGate развёрнут с помощью [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), Dynatrace Operator сам обрабатывает токен авторизации. Начиная с версии Dynatrace Operator 0.9.0+, нужно включить область действия **Create ActiveGate tokens** (`activeGateTokenManagement.create`). Подробности см. в разделе [Tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

  По вопросам, связанным с токеном ActiveGate, см. [Problem with ActiveGate token﻿](https://dt-url.net/ym238od) в Dynatrace Community.
* Все хост-based ActiveGate, установленные через веб-интерфейс Dynatrace или Dynatrace API, уже имеют автоматически сгенерированный токен ActiveGate. Однако иногда может понадобиться [сгенерировать токен ActiveGate](#generate-individual) и [настроить его в файле `authorization.properties`](#configure-hostbased).

#### Генерация токена ActiveGate

1. [Сгенерировать токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API."). В целях безопасности выбрать одну из следующих областей действия токена, чтобы ограничить доступ:

   * **Create ActiveGate tokens**
   * **Write ActiveGate tokens**
2. Сохранить токен.

   Он отображается только один раз.
3. Использовать эндпоинт [ActiveGate tokens API - POST a token](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.") для создания токена. Авторизовать вызов только что созданным токеном API. Например, следующая команда сгенерирует токен ActiveGate со следующими параметрами:

   * Тип ActiveGate: `ENVIRONMENT`
   * Срок действия токена ActiveGate истекает через: `6 months`
   * Тип токена ActiveGate: индивидуальный токен ActiveGate (`seedToken` равен false).

   Начиная с версии Dynatrace 1.293+, нужно убедиться, что поле **expirationDate** не задано в прошлом и не превышает **двух лет** с момента создания.

   **Команда:**

   ```
   curl -X POST "https://{your-environment-id}.live.dynatrace.com/api/v2/activeGateTokens" \



   -H 'Authorization: Api-Token {api-token}' \



   -H 'Accept: application/json; charset=utf-8' \



   -H 'Content-Type: application/json; charset=utf-8' \



   -d '{



   "name": "myToken",



   "expirationDate": "now+6M",



   "seedToken": false,



   "activeGateType": "ENVIRONMENT"



   }'
   ```

   Заменить:

   * `{your-environment-id}` на [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.")
   * `{api-token}` на [токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") с одной из следующих областей действия: **Create ActiveGate tokens** или **Write ActiveGate tokens**.

   **Пример тела ответа:**

   ```
   {



   "id": "dt0g02.4KWZO5EF",



   "token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E",



   "expirationDate": "2020-11-24T08:15:30.144Z"



   }
   ```

#### Настройка токена на хост-based ActiveGate

1. В [каталоге конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") ActiveGate найти файл `authorization.properties`.
2. Отредактировать файл, добавив сгенерированный токен ActiveGate как значение свойства `authToken`. Например:

   ```
   authToken = dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E     # present, if required
   ```
3. [Перезапустить основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.")

### Уведомления об истечении срока действия токена ActiveGate

Помимо настройки собственного механизма ротации токенов ActiveGate до истечения срока их действия, можно настроить уведомления об истекающих токенах ActiveGate. Для этого нужно создать интеграцию уведомлений о проблемах (например, [Email](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.")), используя встроенный профиль оповещений **Default for ActiveGate Token Expiry**.

Для Dynatrace Managed [экстренные контакты](/managed/managed-cluster/configuration/configure-cluster-event-notifications "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.") также получают уведомления об истечении срока действия токенов.

Чтобы остановить уведомления

1. В Dynatrace перейти в **Deployment Status** > **ActiveGates**.
2. Выбрать **More** (**…**), затем выбрать **ActiveGate token enforcement settings**.
3. Отключить **Enable notifications about ActiveGate tokens expiration dates**.
4. Выбрать **Save changes**.

### Автоматическая очистка токенов ActiveGate

Dynatrace версии 1.272+

Dynatrace выполняет автоматическую очистку неиспользуемых токенов ActiveGate. Токен считается неиспользуемым по истечении двух лет с момента последнего использования. Проверить свои токены можно с помощью запроса [GET all tokens](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens "List all ActiveGate tokens available for your monitoring environment via Dynatrace API.") API токенов, обратив внимание на поле **lastUsedDate**.

Пример полезной нагрузки API

```
{



"activeGateTokens": [



{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.321cba",



"name": "system:installer",



"owner": "john.smith@company.com",



"creationDate": "2021-11-30T14:11:40.913Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.123abc",



"name": "system:initial-setup",



"owner": "mary.brown@company.com",



"creationDate": "2021-10-22T13:48:00.135Z",



"expirationDate": "2021-12-02T11:52:17.201Z",



"lastUsedDate": "2020-11-24T08:15:30.144Z",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}



],



"nextPageKey": "AAAAAAAAAAAAAABOAAAAAAAAAAAAAAA6ACQAEAAAABgACgAITFdXQk1BRzYAAAhtZXRhZGF0YQB___-bf___m3iIYxfF7xVQvY72rwblQkcAAwAAAAAAAADHAAAAZA==",



"pageSize": 100,



"totalCount": 1000



}
```