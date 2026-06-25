---
title: Mission Control API
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api
scraped: 2026-05-12T12:07:23.732507
---

# Mission Control API

# Mission Control API

* Published Mar 12, 2021

Для аутентификации в Mission Control API нужен валидный токен `OAuth REST API client`. Доступ к API контролируется через scope, поэтому токену нужны соответствующие разрешения. В описании ниже указано, какие разрешения нужны для использования.

1. Зарегистрируйте клиент ([Generate SSO client credentials](/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials "Сгенерировать Mission Control API OAuth API client.")).

   Регистрация client credentials

   Выполните следующий REST-вызов:

   ```
   curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey"



   -H "accept: application/json"



   -u "<cluster-identifier>:<license-key>"
   ```

   где:

   * `<cluster-identifier>` — идентификатор кластера (в Dynatrace, перейдите в **Licensing**). Например, `0a00a0a0-92ec-11e7-b1e6-12fbd1fb3732`
   * `<license-key>` — лицензионный ключ, выданный во welcome-письме и видимый в **Licensing**. Например, `0a0aAAAA0jeUv6N`.

   В результате должен прийти JSON-ответ с `clientId` и `clientSecret` и кодом ответа `200`. Например:

   ```
   {



   "clientId": "dt0s04.AAAAAAAA",



   "clientSecret": "dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL",



   "scopes": [



   "sso20-managed-cluster-offline-bundle",



   "sso20-identity-linking"



   ]



   }
   ```

   ```
   200
   ```
2. Сгенерируйте токен ([Generate SSO token](/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token "Сгенерировать токен Mission Control API, позволяющий выполнять URL загрузки update-пакетов.")).
   На данный момент поддерживается только scope `sso20-managed-cluster-offline-bundle`, который позволяет генерировать URL загрузки update-пакетов.

   Генерация токена

   Используя `clientId` и `clientSecret` из предыдущего вызова, выполните следующий REST-вызов:

   ```
   curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token" \



   -H "accept: application/json" \



   -H "Content-Type: application/json" \



   -d "{ \"clientId\": \"dt0s04.AAAAAAAA\", \"clientSecret\": \"dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL\", \"scope\": \"sso20-managed-cluster-offline-bundle\"}"
   ```

   В результате придёт JSON-ответ с токеном, привязанными scope'ами и датой истечения токена. Например:

   ```
   {



   "token": "aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA",



   "scopes": [



   "sso20-managed-cluster-offline-bundle"



   ],



   "expiresAt": 1615477153001



   }
   ```

   ```
   200
   ```
3. Аутентифицируйтесь в API-вызовах.

   API-вызов проходит аутентификацию по каждому вызову через HTTP-заголовок authorization. Можно аутентифицироваться, прикрепив токен в HTTP-заголовок authorization с префиксом realm `Bearer`.

   Пример аутентификации

   ```
   curl -X GET "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle/published"



   -H "accept: application/json"



   -H "Authorization: Bearer aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA"
   ```

   Если не указано иное, используются следующие коды ответа:

   * `200` — OK. Запрос выполнен успешно.
   * `400` — Bad request. Запрос не удался. Тело ответа содержит дополнительные детали.
   * `401` — Unauthorized. Аутентификация по токену не удалась. Проверьте, есть ли у токена нужные разрешения.
   * `404` — Not found. Запрошенный ресурс не найден. Проверьте корректность ввода.
   * `429` — Too many requests. Mission Control сейчас занят, повторите позже.

### Mission Control client registration

[Generate SSO client credentials](/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials "Сгенерировать Mission Control API OAuth API client.")

### Offline Bundle packages

[Get a list of available packages and updates](/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-available-packages-updates "Получить список доступных deployment packages и обновлений через Mission Control API.")

[Get offline bundle](/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-offline-package-update-bundle "Получить конкретный deployment package и обновление как Offline Bundle через Mission Control API.")

### Mission Control token generation

[Generate SSO token](/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token "Сгенерировать токен Mission Control API, позволяющий выполнять URL загрузки update-пакетов.")