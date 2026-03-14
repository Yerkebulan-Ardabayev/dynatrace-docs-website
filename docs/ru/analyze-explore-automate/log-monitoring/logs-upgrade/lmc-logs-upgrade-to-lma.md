---
title: Обновление до Log Management и Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma
scraped: 2026-03-06T21:14:27.302891
---

# Обновление до Log Management and Analytics

# Обновление до Log Management and Analytics

* Classic
* Практическое руководство
* Время чтения: 6 мин.
* Обновлено 07 июля 2023

Log Management and Analytics -- это новейшее решение Dynatrace для мониторинга логов. С появлением Dynatrace Platform и [Grail](../../../platform/grail/dynatrace-grail.md "Grail -- это хранилище данных Dynatrace, разработанное специально для данных наблюдаемости и безопасности, и выступающее единым хранилищем для логов, метрик, трассировок, событий и многого другого.") мы рекомендуем вам обновиться до последней версии системы мониторинга логов. Если вы используете Dynatrace SaaS на AWS, ваша среда будет активирована для Log Management and Analytics на базе [Grail](../../../platform/grail/dynatrace-grail.md "Grail -- это хранилище данных Dynatrace, разработанное специально для данных наблюдаемости и безопасности, и выступающее единым хранилищем для логов, метрик, трассировок, событий и многого другого.") в рамках поэтапного развертывания.

Для получения дополнительной информации о поэтапном развертывании обратитесь к одному из членов вашей команды по работе с клиентами Dynatrace. Вы также можете обратиться напрямую к экспертам Dynatrace через чат в вашей среде Dynatrace. Наши эксперты свяжут вас с членами вашей команды по работе с клиентами и помогут ответить на любые другие вопросы.

### Как обновиться с Log Monitoring Classic до Log Management and Analytics?

После активации вашей среды:

1. Перейдите в ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.
2. В баннерном сообщении выберите **Go to activation page** и нажмите **Activate Logs powered by Grail**.
3. На странице **Activate Grail for log and events** вы можете выбрать:

   * **Activate now**
   * **Wait 7 days**
4. Нажмите **Confirm** для подтверждения вашего выбора.

* Только пользователи с правами администратора могут активировать Log Management and Analytics для среды.
* Активация Log Management and Analytics необратима.

### Обновление с сохранением существующих данных

Вы можете выбрать обновление с сохранением существующих данных логов.

* Если вы выберете **Wait 7 days** на странице **Activate Grail for log and events**, активация Grail будет отложена на 7 дней.
  В течение этого периода данные логов будут загружаться как в Log Monitoring Classic, так и в Grail. По истечении 7-дневного периода Grail будет активирован автоматически, и вы начнете использовать Log Management and Analytics с 7 днями существующих данных.
* Если вам требуются данные логов за более длительный период перед обновлением, обратитесь к эксперту Dynatrace через чат и запросите увеличение времени ожидания.
* Если обновление с сохранением существующих данных для вас не важно, выберите **Activate now** на странице **Activate Grail for log and events**, и Logs powered by Grail станет активным примерно через 30 секунд.

### Что изменится после активации

После активации Log Management and Analytics произойдут следующие изменения:

* Поступающие данные логов

  + Поступающие данные логов сохраняются в [базе данных Grail](../../../platform/grail/dynatrace-grail.md "Grail -- это хранилище данных Dynatrace, разработанное специально для данных наблюдаемости и безопасности, и выступающее единым хранилищем для логов, метрик, трассировок, событий и многого другого.").
  + Поступающие данные логов могут быть направлены в корзины с различными [периодами хранения](../../logs/lma-bucket-assignment.md "Данные логов могут храниться в корзинах с различными периодами хранения.").
* Потребление DDU

  + При активации Log Management and Analytics вы начинаете потреблять DDU по [новой модели с тремя измерениями: прием и обработка, хранение, запросы](../../../license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics.md "Узнайте, как рассчитывается объем потребления DDU для Dynatrace Log Management and Analytics.").
  + Если вы выберете **Wait 7 days**, вы все равно начнете потреблять DDU для приема и хранения по новой модели немедленно, а для запросов -- после выполнения первого DQL-запроса.
* API

  + [API экспорта логов](../../../dynatrace-api/environment-api/log-monitoring-v2/get-export-logs.md "Получение записей логов через Log Monitoring API v2.") будет недоступен. Мы рекомендуем прекратить использование [Log GET search](../../../dynatrace-api/environment-api/log-monitoring-v2/get-search-logs.md "Получение записей логов через Log Monitoring API v2.") и [Log GET aggregate](../../../dynatrace-api/environment-api/log-monitoring-v2/get-aggregate-logs.md "Получение агрегированных записей логов через Log Monitoring API v2."). Если вы продолжите их использовать, потребуется [токен OAuth2](../../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.") с правами `storage:logs:read` и `storage:buckets:read`.
  + Мы рекомендуем перейти с существующих API на [Grail Query API](https://developer.dynatrace.com/platform-services/services/storage/).
* Отсутствие поддержки зон управления

  + Конфигурация зон управления не будет работать с Grail. Для контроля доступа необходимо использовать корзины и политики. Ознакомьтесь с разделом **Доступ пользователей** ниже.

### Что не изменится после активации

После активации Log Management and Analytics следующие аспекты останутся без изменений:

* Конфигурация приема данных, включая [конфигурацию OneAgent](../../logs/lma-log-ingestion/lma-log-ingestion-via-oa.md "Прием данных логов в Dynatrace с помощью OneAgent и их преобразование в осмысленные сообщения логов.") и [прием через общий API](../../logs/lma-log-ingestion/lma-log-ingestion-via-api.md "Потоковая передача данных логов в Dynatrace с помощью API и их преобразование в осмысленные сообщения логов.").
* Обработка логов, включая [правила обработки](../../logs/lma-classic-log-processing.md#lmc-log-processing-rules "Используйте правила обработки логов для преобразования входящих данных логов для лучшего понимания, анализа или дальнейшей обработки.") с фильтрами на основе синтаксиса LQL.
* Метрики логов, включая [запросы метрик](../../logs/lma-log-processing/lma-log-metrics.md "Создавайте метрики на основе данных логов и используйте их в Dynatrace как любую другую метрику.") на основе синтаксиса LQL.
* События логов, включая [запросы событий](../../logs/lma-log-processing/lma-log-events.md "Создавайте события логов на основе данных логов и используйте их для обнаружения проблем.") на основе синтаксиса LQL.

Тем не менее мы рекомендуем [преобразовать ваши фильтры LQL](../../logs/logs-upgrade/lma-dql-conversion.md "Преобразуйте текущие правила мониторинга логов в DQL.") для обработки логов, метрик и событий в высокопроизводительные [фильтры DQL](../../logs/lma-classic-log-processing/lma-log-processing-matcher.md "Изучите конкретные функции DQL и логические операторы для обработки логов.").

### Доступ пользователей

Процесс предоставления доступа пользователям зависит от того, являетесь ли вы новым или существующим пользователем.

Конфигурация зон управления не будет работать с Grail. Для контроля доступа необходимо использовать корзины и политики.

* Назначение политики существующим пользователям
  После активации Log Management and Analytics всем пользователям, которые уже имели доступ к данным логов, назначается новая политика для доступа к данным логов в Grail.
* Назначение политики новым пользователям

  Существует два варианта настройки политик доступа для Grail:

  Назначение политики через Account Admin

  В Dynatrace SaaS только пользователи-администраторы могут управлять политиками (пользователи с разрешением учетной записи `Manage users`).
  Необходимо назначить две политики: **Storage Events Read** и **Storage Logs Read**, привязанные к группе.

  Чтобы проверить, назначены ли ваши политики

  1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/).
  2. Перейдите в **Identity & access management** > **Policy management**.
  3. Проверьте, присутствуют ли Storage Events Read и Storage Logs Read в списке политик.

  Если **Storage Events Read** и **Storage Logs Read** отсутствуют в вашем списке политик, их необходимо добавить вручную:

  + **Storage Events Read**:
    **Название политики**: Storage Events Read
    **Описание политики**: Enables reading events from GRAIL
    **Выражения политики**: `ALLOW storage:events:read`
  + **Storage Logs Read**:
    **Название политики**: Storage Logs Read
    **Описание политики**: Enables reading logs from GRAIL
    **Выражения политики**: `ALLOW storage:logs:read`
    Подробнее см. [Управление политиками IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md#create "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace.").

  Чтобы политика вступила в силу, необходимо [привязать ее к группе](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md#add-or-remove "Работа с политиками").

  1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/).
  2. Выберите **Identity & access management** > **Group management**.
     Подробнее см. [Работа с политиками](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками").
  3. Отредактируйте группу, к которой вы хотите привязать политику (например, Logs and events). Убедитесь, что пользователям, которым необходимо использовать логи и события, назначена эта группа.
  4. Выберите вкладку **Policies**.

  Назначение политики через API

  1. Получите токен [OAuth](../../../manage/account-management/identity-access-management/oauth.md "Управление аутентификацией и разрешениями пользователей для API управления учетными записями.")
     Выполните POST-запрос с параметрами формы к SSO.

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
     Выполните POST-запрос к [IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками")

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
     Выполните POST-запрос к [IAM](../../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Работа с политиками")

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

  Ваши вновь созданные политики будут видны на уровне учетной записи. Чтобы проверить это, перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management** > **Edit Storage Events Read**.