---
title: Токен тенанта
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token
scraped: 2026-05-12T11:22:20.752000
---

# Токен тенанта

# Токен тенанта

* 2-min read
* Published Feb 23, 2021

Токен тенанта используется OneAgent и ActiveGate для передачи данных в Dynatrace. Dynatrace автоматически генерирует токен тенанта и добавляет его в установщики OneAgent и ActiveGate при загрузке.

## Получение токена тенанта

Для получения токена тенанта вашего окружения выполните запрос [GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр информации о подключении OneAgent через Dynatrace API.") Deployment API. Токен тенанта будет находиться в поле `tenantToken` тела ответа. Для аутентификации запроса потребуется PaaS-токен.

## Ротация токена тенанта

При необходимости токен тенанта можно изменить (например, для соблюдения внутренних политик безопасности или в ответ на непреднамеренное раскрытие). Процедура смены токена тенанта называется *ротацией токена тенанта*.

Для ротации токена необходимо сгенерировать новый токен, назначить его всем OneAgent и ActiveGate, передающим данные в окружение, а затем отключить старый токен.

Чтобы избежать потери данных, в процессе ротации действительны как старый, так и новый токен. В период ротации не развёртывайте новые экземпляры OneAgent до тех пор, пока все ActiveGate не будут настроены с новым токеном тенанта.

1. Запустите ротацию и создайте новый токен тенанта, выполнив запрос [POST start rotation request](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start "Инициирование ротации токена тенанта Dynatrace.").

   Запрос возвращает новый токен в поле **active** тела ответа.
2. Добавьте новый токен в ActiveGate. Для каждого ActiveGate:

   1. [Остановите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate на Windows или Linux.").
   2. В файле `authorization.properties` [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") найдите запись для нужного окружения и укажите новый токен в поле **tenantToken**.
   3. В зависимости от [назначения ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate."):

      * [Маршрутизация трафика OneAgent и мониторинг удалённых технологий](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."): найдите запись для нужного окружения в файлах `ruxitagent.conf` и `extensions.conf` и укажите новый токен в поле **tenantToken**.

        **Windows**: `%PROGRAMFILES%\dynatrace\remotepluginmodule\agent\conf`  
        **Linux**: `/opt/dynatrace/remotepluginmodule/agent/conf`
      * [Установка модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."): найдите запись для нужного окружения и укажите новый токен в поле **tenantToken**.

        **Windows**: `%PROGRAMFILES%\dynatrace\zremote\agent\conf\ruxitagent.conf`  
        **Linux**: `/opt/dynatrace/zremote/agent/conf/ruxitagent.conf`
   4. Только для Windows: измените значение записи реестра: `HKEY_LOCAL_MACHINE\Software\Dynatrace\Dynatrace ActiveGate\common\tenant_token`.
   5. [Запустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate на Windows или Linux.").
3. Добавьте новый токен в OneAgent. Для каждого OneAgent:

   1. Добавьте новый токен в настройки связи OneAgent.

      Используйте команду `--set-tenant-token` [интерфейса командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#change-oneagent-communication-settings "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без переустановки.").
   2. [Перезапустите](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без переустановки.") OneAgent.

   Оба шага можно объединить в одну команду:

   ```
   oneagentctl --restart-service --set-tenant-token={new token}
   ```
4. Завершите ротацию, выполнив запрос [POST finish rotation request](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-finish "Завершение ротации токена тенанта Dynatrace."). Это завершает процесс и делает старый токен недействительным.

## Связанные темы

* [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация токенов тенанта Dynatrace.")
* [Директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.")
* [Конфигурация OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи конфигурации OneAgent без переустановки.")