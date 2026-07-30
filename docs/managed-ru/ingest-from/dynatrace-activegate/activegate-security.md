---
title: Безопасность ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-security
---

# Безопасность ActiveGate

# Безопасность ActiveGate

* 8 мин чтения
* Обновлено Jul 20, 2026

## Пользовательский сертификат для ActiveGate

Рекомендуется использовать пользовательские сертификаты для ActiveGate, чтобы повысить безопасность.

См. [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

## Токены

Убедитесь, что токены ActiveGate применяются в вашей среде. Для этого [проверьте статус использования токенов ActiveGate](#determine-status-of-active-gate-token-usage) и выполните необходимые действия по результатам проверки.

### Переход на токены ActiveGate

Чтобы перейти на защиту на основе токенов ActiveGate, сначала определите статус использования токенов ActiveGate.

#### Определение статуса использования токенов ActiveGate

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Просмотрите сообщения на странице **Network security** и устраните проблемы в соответствии с описанием ниже.

##### Действий не требуется

Если Dynatrace показывает сообщение следующего вида:

![Токены ActiveGate применяются](https://dt-cdn.net/images/updated-ss-1-582-2d81cc06ad.png)

Токены ActiveGate применяются

* Никаких действий не требуется. Применение ActiveGate включено, всё готово.
* Только ActiveGate с действительными токенами ActiveGate могут подключаться к Dynatrace.

##### Устранение проблем с токенами ActiveGate

Если Dynatrace показывает сообщение следующего вида:

![Проблемы с токенами ActiveGate](https://dt-cdn.net/images/updated-ss-2-584-c069a85f68.png)

Проблемы с токенами ActiveGate

* Токены ActiveGate ещё не применяются, и часть ActiveGate использует недействительные токены.
* Необходимо устранить проблемы в соответствии со [статусом](#statuses). В противном случае такие ActiveGate потеряют подключение после применения токенов ActiveGate.

##### Немедленное применение токенов ActiveGate

Если Dynatrace показывает сообщение следующего вида:

![Ручное применение токенов ActiveGate](https://dt-cdn.net/images/manual-enforcement-580-5c1b3dbaf4.webp)

Ручное применение токенов ActiveGate

* Можно применить токены ActiveGate немедленно. Это доступно в любое время, независимо от того, сообщают ли ActiveGate о проблемах с токенами, однако сначала прочитайте раздел [Ручное применение токенов ActiveGate](#manual) ниже. Все ActiveGate со статусом, отличным от **Valid**, потеряют подключение к Dynatrace.

### Типы токенов ActiveGate

Токены ActiveGate бывают двух типов:

* **Seed token**, seed-токен ActiveGate, автоматически встраивается в установщик ActiveGate при загрузке установщика через веб-интерфейс Dynatrace или [Dynatrace API](/managed/dynatrace-api/environment-api/deployment/activegate "Загрузка установщиков ActiveGate через Dynatrace API.").
* **Individual token**, при первом подключении ActiveGate к кластеру Dynatrace исходный seed-токен ActiveGate заменяется автоматически сгенерированным индивидуальным токеном ActiveGate. Один и тот же установщик можно использовать несколько раз; исходный seed-токен ActiveGate позволяет создать несколько индивидуальных токенов ActiveGate.

### Структура токена ActiveGate

Формат токена ActiveGate состоит из трёх частей, разделённых точками (`.`).

Пример:

`dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E`

| Часть | Название | Описание |
| --- | --- | --- |
| 1 | **prefix** | Первая часть (`dt0g02` в примере выше) является **prefix** токена. Она определяет тип токена. |
| 2 | **public** | Вторая часть (`4KWZO5EF` в примере выше) является 8-символьной **public**-частью токена. Вместе prefix и public-часть образуют **идентификатор токена** (token identifier). Идентификатор токена можно безопасно отображать в веб-интерфейсе и использовать в целях журналирования. |
| 3 | **secret** | Третья часть (`XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E` в примере выше) является 64-символьной **secret**-частью токена. Обращаться с secret-частью нужно как с паролем. Её не следует отображать в Dynatrace (после первоначального создания) или хранить в файлах журналов. |

### Применение токенов ActiveGate

Все ActiveGate уже постепенно перенесены на использование токенов ActiveGate в ходе обновлений ActiveGate, начиная с версии 1.225.

Чтобы проверить, у каких ActiveGate включены токены ActiveGate:

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. Можно фильтровать ActiveGate по следующим статусам токенов ActiveGate; подробнее см. раздел [Статус токена ActiveGate](#statuses).

   * Absent
   * Expiring
   * Invalid
   * Unknown
   * Valid
   * Unsupported

#### Автоматическое применение токенов ActiveGate

Если все ActiveGate готовы к сетевой защите на основе токенов в течение 30 дней, среда автоматически переключится на сетевую защиту на основе токенов ActiveGate.

#### Ручное применение токенов ActiveGate

Если нужно ускорить процесс и есть уверенность, что в среде используются только ActiveGate версии 1.225+, можно принудительно переключиться на токены ActiveGate в любое удобное время.

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Включите **Manually enforce ActiveGate token authentication**.

* При включении **Manually enforce ActiveGate token authentication** и сохранении изменений все ActiveGate со статусом, отличным от **Valid**, потеряют подключение к Dynatrace.
* После обнаружения последнего недействительного токена есть не более 30 дней для отмены ручного применения (то есть для отключения **Manually enforce ActiveGate token authentication**). Например, если последний недействительный токен был обнаружен 20 дней назад, остаётся ещё 10 дней для отмены применения. По истечении переходного периода переключатель отключается (выключить его будет невозможно).

#### Переходный период

Переходный период длиной 30 дней предназначен для предотвращения потери данных от ActiveGate, в которых новые токены ещё не внедрены в среде.

В течение этого периода, если обнаруживается попытка подключения без токена ActiveGate:

* Применение токенов ActiveGate не будет включено, и всем ActiveGate разрешается подключаться к кластеру Dynatrace (потребуются только tenant-токены).
* Переходный период сбрасывается на 30 дней, и применение токенов ActiveGate будет включено автоматически не ранее чем через 30 дней с этого момента.

### Статус токена ActiveGate

Dynatrace Classic

Если ActiveGate не используют действительные токены ActiveGate, можно выяснить причину недействительности.

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. Выберите **Check ActiveGate token statuses**.

   Эта опция доступна только при наличии проблем с токенами ActiveGate.

В зависимости от статуса может потребоваться выполнить ряд действий для перехода на сетевую защиту на основе токенов ActiveGate.

#### Absent

Версия ActiveGate поддерживает токены ActiveGate, но для связи всё ещё используется tenant-токен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Expiring

Токен ActiveGate истекает через 30 или менее дней. Если в среде применяются токены ActiveGate, ActiveGate потеряет подключение после истечения срока действия токена.

#### Invalid

ActiveGate настроен на использование токена ActiveGate, но формат токена недействителен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Unknown

ActiveGate настроен на использование токена ActiveGate, формат токена действителен, однако токен не распознаётся кластером Dynatrace. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Valid

ActiveGate использует действительный токен ActiveGate для аутентификации.

#### Unsupported

ActiveGate использует версию 1.223 или более раннюю; сетевая защита на основе токенов ActiveGate поддерживается для версий ActiveGate 1.225+.

### Генерация и настройка токена ActiveGate

* Если ActiveGate развёрнут как [StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet."), нужно [сгенерировать токен ActiveGate](#generate-individual) и добавить его в конфигурацию.

  + Seed-токен ActiveGate не подходит для контейнеризованных ActiveGate.
  + Токен ActiveGate можно использовать совместно между несколькими ActiveGate в одной среде.
* Если ActiveGate развёрнут с помощью [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), Dynatrace Operator управляет токеном авторизации. Начиная с версии Dynatrace Operator 0.9.0+, необходимо включить область **Create ActiveGate tokens** (`activeGateTokenManagement.create`). Подробнее: [Tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

  При проблемах с токеном ActiveGate обращайтесь к [Problem with ActiveGate token﻿](https://dt-url.net/ym238od) в Dynatrace Community.
* Все host-based ActiveGate, установленные через веб-интерфейс Dynatrace или Dynatrace API, уже имеют автоматически сгенерированный токен ActiveGate. Однако иногда может потребоваться [сгенерировать токен ActiveGate](#generate-individual) и [настроить его в файле `authorization.properties`](#configure-hostbased).

#### Генерация токена ActiveGate

1. [Сгенерируйте токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API."). Для ограничения доступа в целях безопасности выберите одну из следующих областей токена:

   * **Create ActiveGate tokens**
   * **Write ActiveGate tokens**
2. Сохраните токен.

   Он отображается только один раз.
3. Используйте endpoint [ActiveGate tokens API - POST a token](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.") для создания токена. Авторизуйте вызов с помощью только что созданного токена API. Например, следующая команда сгенерирует токен ActiveGate со следующими параметрами:

   * Тип ActiveGate: `ENVIRONMENT`
   * Срок действия токена ActiveGate: `6 месяцев`
   * Тип токена ActiveGate: индивидуальный токен ActiveGate (значение `seedToken` равно false).

   Начиная с версии Dynatrace 1.293+, необходимо убедиться, что поле **expirationDate** не установлено в прошедшую дату и не превышает **двух лет** с момента создания.

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

   Замените:

   * `{your-environment-id}` на [идентификатор среды Environment](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.")
   * `{api-token}` на [токен API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") с одной из следующих областей: **Create ActiveGate tokens** или **Write ActiveGate tokens**.

   **Пример тела ответа:**

   ```
   {



   "id": "dt0g02.4KWZO5EF",



   "token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E",



   "expirationDate": "2020-11-24T08:15:30.144Z"



   }
   ```

#### Настройка токена на host-based ActiveGate

1. В [директории конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") ActiveGate найдите файл `authorization.properties`.
2. Отредактируйте файл: добавьте сгенерированный токен ActiveGate в качестве значения свойства `authToken`. Например:

   ```
   authToken = dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E     # present, if required
   ```
3. [Перезапустите основной сервис ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.")

### Уведомления об истечении срока действия токена ActiveGate

Помимо настройки собственного механизма ротации токенов ActiveGate до истечения срока их действия, можно настроить уведомления об истекающих токенах ActiveGate. Для этого создайте интеграцию уведомлений о проблемах (например, [Email](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.")) с использованием встроенного профиля оповещения **Default for ActiveGate Token Expiry**.

В Dynatrace Managed [экстренные контакты](/managed/managed-cluster/configuration/configure-cluster-event-notifications "Configure Dynatrace Managed Cluster event notification recipients, emergency contacts, and which Managed Cluster events trigger email notifications.") также получают уведомления об истечении срока действия токенов.

Dynatrace Classic

Чтобы отключить уведомления

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Выберите **More** (**…**), затем выберите **ActiveGate token enforcement settings**.
3. Отключите **Enable notifications about ActiveGate tokens expiration dates**.
4. Нажмите **Save changes**.

### Автоматическая очистка токенов ActiveGate

Dynatrace версия 1.272+

Dynatrace выполняет автоматическую очистку неиспользуемых токенов ActiveGate. Токен считается неиспользуемым спустя два года с момента последнего использования. Проверить токены можно через запрос [GET all tokens](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens "List all ActiveGate tokens available for your monitoring environment via Dynatrace API.") Tokens API: нужно обратить внимание на поле **lastUsedDate**.

Пример payload API

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