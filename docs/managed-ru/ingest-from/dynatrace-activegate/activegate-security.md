---
title: Безопасность ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-security
scraped: 2026-05-12T12:05:30.331384
---

# Безопасность ActiveGate

# Безопасность ActiveGate

* 8-min read
* Published Jul 08, 2022

## Пользовательский сертификат для ActiveGate

Рекомендуется использовать пользовательские сертификаты для ActiveGate в целях повышения безопасности.

Смотрите раздел [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

## Токены

Убедитесь, что токены ActiveGate применяются в вашем окружении. Для этого [проверьте статус использования токенов ActiveGate](#determine-status-of-active-gate-token-usage) и выполните необходимые действия по результатам проверки.

### Переход на токены ActiveGate

Чтобы перейти на безопасность на основе токенов ActiveGate, начните с определения статуса использования токенов.

#### Определение статуса использования токенов ActiveGate

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Проверьте сообщения на странице **Network security** и устраните обнаруженные проблемы, как описано ниже.

##### Действий не требуется

Если Dynatrace отображает следующее сообщение:

![Токены ActiveGate применяются](https://dt-cdn.net/images/updated-ss-1-582-2d81cc06ad.png)

Токены ActiveGate применяются

* Действий не требуется. Применение токенов ActiveGate включено.
* К Dynatrace могут подключаться только ActiveGate с действующими токенами.

##### Исправление проблем с токенами ActiveGate

Если Dynatrace отображает следующее сообщение:

![Проблемы с токенами ActiveGate](https://dt-cdn.net/images/updated-ss-2-584-c069a85f68.png)

Проблемы с токенами ActiveGate

* Токены ActiveGate ещё не применяются, и некоторые ActiveGate используют недействующие токены.
* Необходимо устранить проблемы в соответствии со [статусами](#statuses). В противном случае такие ActiveGate потеряют подключение после включения принудительного использования токенов.

##### Принудительное применение токенов ActiveGate немедленно

Если Dynatrace отображает следующее сообщение:

![Принудительное применение токенов ActiveGate вручную](https://dt-cdn.net/images/manual-enforcement-580-5c1b3dbaf4.webp)

Принудительное применение токенов ActiveGate вручную

* У вас есть возможность немедленно включить принудительное применение токенов ActiveGate в любое время, вне зависимости от того, сообщают ли ваши ActiveGate о проблемах с токенами. Перед этим обязательно прочитайте раздел [Принудительное применение токенов ActiveGate вручную](#manual). Все ActiveGate со статусом, отличным от **Valid**, потеряют подключение к Dynatrace.

### Типы токенов ActiveGate

Токены ActiveGate бывают двух типов:

* **Seed token** (исходный токен) — исходный токен ActiveGate автоматически встраивается в установщик ActiveGate при его загрузке через веб-интерфейс Dynatrace или [Dynatrace API](/managed/dynatrace-api/environment-api/deployment/activegate "Загрузите установщики ActiveGate через Dynatrace API.").
* **Individual token** (индивидуальный токен) — при первом подключении ActiveGate к кластеру Dynatrace исходный токен заменяется автоматически сгенерированным индивидуальным токеном. Один и тот же установщик можно использовать несколько раз: исходный токен позволяет создать несколько индивидуальных токенов.

### Структура токена ActiveGate

Токен ActiveGate состоит из трёх частей, разделённых точками (`.`).

Пример:

`dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E`

| Часть | Название | Описание |
| --- | --- | --- |
| 1 | **prefix** | Первая часть (`dt0g02` в примере) — **префикс** токена. Определяет тип токена. |
| 2 | **public** | Вторая часть (`4KWZO5EF` в примере) — 8-символьная **публичная** часть токена. Вместе с префиксом образует **идентификатор токена**. Идентификатор токена можно безопасно отображать в веб-интерфейсе и использовать для логирования. |
| 3 | **secret** | Третья часть (`XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E` в примере) — 64-символьная **секретная** часть токена. Обращайтесь с ней как с паролем: не отображайте в Dynatrace после первоначального создания и не храните в лог-файлах. |

### Применение токенов ActiveGate

Все ActiveGate уже постепенно перешли на использование токенов ActiveGate в ходе обновлений, начиная с версии 1.225.

Чтобы проверить, у каких ActiveGate включены токены:

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. Отфильтруйте ActiveGate по следующим статусам токенов (подробнее: [Статус токена ActiveGate](#statuses)):

   * Absent
   * Expiring
   * Invalid
   * Unknown
   * Valid
   * Unsupported

#### Автоматическое применение токенов ActiveGate

Если все ваши ActiveGate готовы к сетевой безопасности на основе токенов в течение 30 дней подряд, окружение автоматически переключится на этот режим.

#### Принудительное применение токенов ActiveGate вручную

Если вы хотите ускорить процесс и уверены, что в окружении присутствуют только ActiveGate версии 1.225+, можно принудительно включить применение токенов в любое удобное время.

1. В Dynatrace перейдите в **Settings** > **Preferences** > **Network security**.
2. Включите **Manually enforce ActiveGate token authentication**.

* При включении **Manually enforce ActiveGate token authentication** и сохранении изменений все ActiveGate со статусом, отличным от **Valid**, потеряют подключение к Dynatrace.
* У вас есть максимум 30 дней после последнего обнаружения недействительного токена, чтобы отменить принудительное применение (отключить **Manually enforce ActiveGate token authentication**). Например, если последний недействительный токен был обнаружен 20 дней назад, у вас есть ещё 10 дней. По истечении переходного периода переключатель блокируется.

#### Переходный период

Переходный период в 30 дней предназначен для предотвращения потери данных от ActiveGate, в которых новые токены ещё не реализованы.

В течение этого периода, если обнаружена попытка подключения без токена ActiveGate:

* Принудительное применение токенов не включается, и все ActiveGate могут подключаться к кластеру Dynatrace (требуются только токены тенанта).
* Переходный период сбрасывается на 30 дней: принудительное применение токенов будет включено автоматически не ранее чем через 30 дней с этого момента.

### Статус токена ActiveGate

Если ваши ActiveGate не используют действительные токены, вы можете выяснить причину.

1. В Dynatrace перейдите в **Deployment Status** и выберите **ActiveGates**.
2. Выберите **Check ActiveGate token statuses**.

   Этот параметр доступен только при наличии проблем с токенами ActiveGate.

В зависимости от статуса может потребоваться выполнить определённые действия для перехода на безопасность на основе токенов.

#### Absent

ActiveGate поддерживает токены, но всё ещё использует токен тенанта. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Expiring

Срок действия токена ActiveGate истекает через 30 дней или менее. Если применение токенов включено, ActiveGate потеряет подключение после истечения срока действия токена.

#### Invalid

ActiveGate настроен на использование токена, но формат токена недействителен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Unknown

ActiveGate настроен на использование токена, формат токена действителен, но кластер Dynatrace не распознаёт этот токен. [Сгенерируйте и настройте](#generate) новый токен ActiveGate.

#### Valid

ActiveGate использует действительный токен для аутентификации.

#### Unsupported

ActiveGate имеет версию 1.223 или ниже: безопасность на основе токенов поддерживается начиная с версии 1.225+.

### Генерация и настройка токена ActiveGate

* Если ActiveGate развёрнут как [StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet."), необходимо [сгенерировать токен ActiveGate](#generate-individual) и добавить его в конфигурацию.

  + Seed token нельзя использовать для контейнерных ActiveGate.
  + Один токен ActiveGate может использоваться несколькими ActiveGate в рамках одного окружения.
* Если ActiveGate развёрнут с помощью [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Развёртывание Dynatrace Operator на Kubernetes"), Dynatrace Operator управляет токеном авторизации. Начиная с версии Dynatrace Operator 0.9.0+ необходимо включить область **Create ActiveGate tokens** (`activeGateTokenManagement.create`). Подробнее смотрите в разделе [Токены доступа и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга кластера Kubernetes").
* Все установленные через веб-интерфейс или API ActiveGate уже имеют автоматически сгенерированный токен. Однако иногда может потребоваться [сгенерировать токен](#generate-individual) и [настроить его в файле `authorization.properties`](#configure-hostbased).

#### Генерация токена ActiveGate

1. [Создайте API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API."). Выберите одну из следующих областей для ограничения доступа:

   * **Create ActiveGate tokens**
   * **Write ActiveGate tokens**
2. Сохраните токен.

   Он отображается только один раз.
3. Используйте конечную точку [ActiveGate tokens API - POST a token](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Создайте новый токен ActiveGate через Dynatrace API.") для создания токена. Авторизуйте запрос только что созданным API-токеном. Пример команды для генерации токена со следующими параметрами:

   * Тип ActiveGate: `ENVIRONMENT`
   * Срок действия: `6 месяцев`
   * Тип токена: индивидуальный (`seedToken` равен false)

   Начиная с Dynatrace версии 1.293+ убедитесь, что поле **expirationDate** не установлено в прошлое и не превышает **двух лет** с момента создания.

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

   * `{your-environment-id}` на ваш [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Изучите окружения мониторинга и работу с ними.")
   * `{api-token}` на [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с одной из следующих областей: **Create ActiveGate tokens** или **Write ActiveGate tokens**.

   **Пример тела ответа:**

   ```
   {
   "id": "dt0g02.4KWZO5EF",
   "token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E",
   "expirationDate": "2020-11-24T08:15:30.144Z"
   }
   ```

#### Настройка токена на ActiveGate на основе хоста

1. В [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") найдите файл `authorization.properties`.
2. Отредактируйте файл, добавив сгенерированный токен ActiveGate как значение свойства `authToken`. Например:

   ```
   authToken = dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E
   ```
3. [Перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.")

### Уведомления об истечении срока токена ActiveGate

Помимо настройки собственного механизма ротации токенов ActiveGate до истечения их срока действия, вы можете настроить уведомления об истекающих токенах. Для этого создайте интеграцию уведомлений о проблемах (например, [Email](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Получайте email при обнаружении Dynatrace проблемы, влияющей на реальных пользователей.")) с использованием встроенного профиля оповещений **Default for ActiveGate Token Expiry**.

В Dynatrace Managed [аварийные контакты](/managed/managed-cluster/configuration/configure-emergency-contacts-managed "Узнайте, как настроить аварийные контакты в Dynatrace Managed.") также получают уведомления об истечении срока токена.

Чтобы отключить уведомления:

1. В Dynatrace перейдите в **Deployment Status** > **ActiveGates**.
2. Выберите **More** (**...**), затем **ActiveGate token enforcement settings**.
3. Отключите **Enable notifications about ActiveGate tokens expiration dates**.
4. Выберите **Save changes**.

### Автоматическая очистка токенов ActiveGate

Dynatrace версии 1.272+

Dynatrace выполняет автоматическую очистку неиспользуемых токенов ActiveGate. Токен считается неиспользуемым по истечении двух лет с момента последнего использования. Проверить токены можно через запрос [GET all tokens](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens "Список всех токенов ActiveGate, доступных для вашего окружения мониторинга.") Tokens API: обратите внимание на поле **lastUsedDate**.