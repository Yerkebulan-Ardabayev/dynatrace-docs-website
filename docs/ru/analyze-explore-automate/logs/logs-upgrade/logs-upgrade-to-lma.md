---
title: Обновление Мониторинг журналов Classic до Управления журналами и Аналитики
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/logs-upgrade/logs-upgrade-to-lma
scraped: 2026-03-05T21:34:52.597060
---

# Обновление Log Monitoring Classic до Log Management and Analytics


Log Management and Analytics — это новейшее решение Dynatrace для мониторинга логов. С появлением Dynatrace Platform и [Grail](../../../platform/grail/dynatrace-grail.md "Grail — это хранилище данных Dynatrace, специально разработанное для данных наблюдаемости и безопасности, которое выступает единым унифицированным хранилищем для логов, метрик, трассировок, событий и многого другого.") мы рекомендуем перейти на новейшее решение для мониторинга логов.

### Как обновиться с Log Monitoring Classic до Log Management and Analytics?

После того как ваша среда будет доступна для активации:

1. Перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. В баннерном сообщении выберите **Go to activation page** и выберите **Activate Logs powered by Grail**.
3. На странице **Activate Grail for log and events** вы можете выбрать:

   * **Activate now**
   * **Wait 7 days**
4. Выберите **Confirm** для подтверждения вашего выбора.

* Только пользователи с правами администратора могут активировать Log Management and Analytics для среды.
* Активация Log Management and Analytics необратима.

### Обновление с существующими данными

Вы можете обновиться с сохранением существующих данных логов.

* Если вы выберете **Wait 7 days** на странице **Activate Grail for log and events**, активация Grail будет отложена на 7 дней.
  В течение этого периода ваши данные логов будут приниматься как в Log Monitoring Classic, так и в Grail. По истечении 7-дневного периода Grail будет активирован автоматически, и вы начнёте использовать Log Management and Analytics с данными за 7 дней.
* Если вам требуются данные логов за более длительный период перед обновлением, свяжитесь с экспертом по продуктам Dynatrace через чат и запросите более длительный период ожидания.
* Если обновление с существующими данными для вас не важно, выберите **Activate now** на странице **Activate Grail for log and events**, и Logs powered by Grail станет активным примерно через 30 секунд.

### Что изменится после активации

После активации Log Management and Analytics произойдут следующие изменения:

* Принимаемые данные логов

  + Принимаемые данные логов сохраняются в [базе данных Grail](../../../platform/grail/dynatrace-grail.md "Grail — это хранилище данных Dynatrace, специально разработанное для данных наблюдаемости и безопасности, которое выступает единым унифицированным хранилищем для логов, метрик, трассировок, событий и многого другого.").
  + Принимаемые данные логов могут маршрутизироваться в корзины с различными [периодами хранения](../lma-bucket-assignment.md "Ваши данные логов могут храниться в корзинах хранения данных с различными периодами хранения.").
* Потребление DDU

  + При активации Log Management and Analytics вы начинаете потреблять DDU по [новой модели с тремя измерениями: Приём и обработка, Хранение, Запросы](../../../license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Management and Analytics.").
  + Если вы выберете **Wait 7 days**, вы всё равно начнёте потреблять DDU за приём и хранение по новой модели сразу, а за запросы — после выполнения первого запроса DQL.
* API

  + [API экспорта логов](../../../dynatrace-api/environment-api/log-monitoring-v2/get-export-logs.md "Получение записей логов через Log Monitoring API v2.") будет недоступен. Мы рекомендуем прекратить использование [Log GET search](../../../dynatrace-api/environment-api/log-monitoring-v2/get-search-logs.md "Получение записей логов через Log Monitoring API v2.") и [Log GET aggregate](../../../dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs.md "Получение агрегированных записей логов через Log Monitoring API v2."). Если вы продолжите их использовать, для них потребуется [токен OAuth2](../../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управление аутентификацией и разрешениями пользователей с помощью клиентов OAuth.") с областями `storage:logs:read` и `storage:buckets:read`.
  + Мы рекомендуем перейти с существующих API на [Grail Query API](https://developer.dynatrace.com/platform-services/services/storage/).
* Отсутствие поддержки Management Zones

  + Конфигурация Management Zones не будет работать с Grail. Для управления доступом необходимо использовать корзины и политики. См. раздел **Доступ пользователей** ниже.

### Что не изменится после активации

После активации Log Management and Analytics следующее останется без изменений:

* Конфигурация приёма, включая [конфигурацию OneAgent](../lma-log-ingestion/lma-log-ingestion-via-oa.md "Приём данных логов в Dynatrace с помощью OneAgent с последующим преобразованием в информативные сообщения логов.") и [приём через общий API](../lma-log-ingestion/lma-log-ingestion-via-api.md "Потоковая передача данных логов в Dynatrace через API с последующим преобразованием в информативные сообщения логов.").
* Обработка логов, включая [правила обработки](../lma-classic-log-processing.md#lmc-log-processing-rules "Используйте правила обработки логов для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей трансформации.") с сопоставителями на основе синтаксиса LQL.
* Метрики логов, включая [запросы метрик](../lma-log-processing/lma-log-metrics.md "Создание метрик на основе данных логов и их использование в Dynatrace как любых других метрик.") на основе синтаксиса LQL.
* События логов, включая [запросы событий](../lma-log-processing/lma-log-events.md "Создание событий логов на основе данных логов и их использование при обнаружении проблем.") на основе синтаксиса LQL.

Тем не менее, мы рекомендуем [преобразовать ваши LQL-сопоставители](lma-dql-conversion.md "Преобразование текущих правил мониторинга логов в DQL.") для обработки логов, метрик и событий в высокопроизводительные [DQL-сопоставители](../lma-classic-log-processing/lma-log-processing-matcher.md "Изучите конкретные функции DQL и логические операторы для обработки логов.").

### Доступ пользователей

Процесс предоставления доступа зависит от того, являетесь ли вы новым или существующим пользователем.

* Назначение политики существующим пользователям
  После активации Log Management and Analytics всем пользователям, которые уже имели доступ к данным логов, назначается новая политика для доступа к данным логов в Grail.
* Назначение политики новым пользователям

  Существует два варианта настройки политик доступа для Grail:

  Назначение политики через Account Admin

  В Dynatrace SaaS только пользователи с правами администратора могут управлять политиками (пользователи с разрешением учётной записи `Manage users`).
  Вам необходимо назначить две политики — **Storage Events Read** и **Storage Logs Read** — привязанные к группе.

  Для проверки назначения политик

  1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/).
  2. Перейдите в **Identity & access management** > **Policy management**.
  3. Проверьте, присутствуют ли Storage Events Read и Storage Logs Read в списке политик.

  Если **Storage Events Read** и **Storage Logs Read** отсутствуют в вашем списке политик, их необходимо добавить вручную:

  + **Storage Events Read**:
    **Имя политики**: Storage Events Read
    **Описание политики**: Enables reading events from GRAIL
    **Выражения политики**: `ALLOW storage:events:read`
  + **Storage Logs Read**:
    **Имя политики**: Storage Logs Read
    **Описание политики**: Enables reading logs from GRAIL
    **Выражения политики**: `ALLOW storage:logs:read`
    Подробнее см. в разделе [Управление политиками IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md#create "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.").

  Чтобы политика вступила в силу, необходимо [привязать её к группе](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md#add-or-remove "Работа с политиками").

  1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/).
  2. Выберите **Identity & access management** > **Group management**.
     Подробнее см. в разделе [Работа с политиками](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками").
  3. Отредактируйте группу, к которой вы хотите привязать политику (например, Logs and events). Убедитесь, что пользователям, которым необходим доступ к логам и событиям, назначена эта группа.
  4. Выберите вкладку **Policies**.

  Назначение политики через API

  1. Получите токен [OAuth](../../../manage/account-management/identity-access-management/oauth.md "Управление аутентификацией и разрешениями пользователей для Account Management API.")
     Выполните POST-запрос с параметрами формы в SSO.

     + client\_id = [client\_id]
     + client\_secret = [secret]
     + grant\_type = client\_credentials
     + scope = `iam:policies:write iam:policies:read`

     В ответ вы получите токен авторизации

     ```
     {


     "scope": "iam:policies:read iam:policies:write",


     "token_type": "Bearer",


     "expires_in": 300,


     "access_token": "123(...)ABC"


     }
     ```
  2. Создайте политику чтения событий хранилища
     Выполните POST-запрос в [IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками")

     Тело запроса для политики:

     ```
     {


     "name": "Storage Events Read",


     "description": "Storage Events Read",


     "tags": [


     ],


     "statementQuery": "ALLOW storage:events:read;"
     ```
  3. Создайте политику чтения логов хранилища
     Выполните POST-запрос в [IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками")

     Тело запроса для политики:

     ```
     {


     "name": "Storage Logs Read",


     "description": "Storage Logs Read",


     "tags": [


     ]  ,


     "statementQuery": "ALLOW storage:logs:read;"


     }
     ```

  Ваши вновь созданные политики будут видны на уровне учётной записи. Для проверки перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management** > **Edit Storage Events Read**.

## Связанные темы

* [Лучшие практики обновления до последней версии Dynatrace](../../../manage/upgrade-guide-landing-page.md "Лучшие практики обновления до последней версии Dynatrace")
* [Настройка разрешений Grail для логов](../lma-security-context.md "Используйте Dynatrace с Grail и DQL для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.")