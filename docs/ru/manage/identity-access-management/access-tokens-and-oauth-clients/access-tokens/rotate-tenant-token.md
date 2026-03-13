---
title: Tenant token classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token
scraped: 2026-03-06T21:31:16.699787
---

# Классический токен тенанта

# Классический токен тенанта

* Classic
* Время чтения: 2 мин
* Опубликовано 23 фев. 2021

В этой статье рассматриваются токены доступа, используемые в предыдущих версиях Dynatrace для аутентификации в классических API конфигурации и среды. Для доступа к актуальной версии Dynatrace см. [Токены платформы](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Создавайте персонализированные токены платформы для доступа к сервисам Dynatrace через API в контексте вашего пользователя.") и [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управляйте аутентификацией и правами пользователей с помощью OAuth-клиентов.").

Токен тенанта используется OneAgent и ActiveGate для отправки данных в Dynatrace. Dynatrace автоматически генерирует токен тенанта и добавляет его в установщики OneAgent и ActiveGate при загрузке.

## Доступ к токену тенанта

Чтобы получить токен тенанта для вашей среды, выполните запрос [GET информации о подключении OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр информации о подключении OneAgent через Dynatrace API.") в Deployment API. Токен тенанта находится в поле `tenantToken` тела ответа. Для аутентификации запроса вам потребуется токен PaaS.

## Ротация токена тенанта

Вы можете изменить токен тенанта по мере необходимости (например, для соблюдения внутренних политик безопасности или в случае непреднамеренного раскрытия). Процедура изменения токена тенанта называется *ротацией токена тенанта*.

Для ротации токена необходимо сгенерировать новый токен, назначить его всем OneAgent и ActiveGate, которые отправляют данные в среду, а затем отключить старый токен.

Во избежание потери данных и старый, и новый токены действительны в процессе ротации. Во время ротации не разворачивайте новые OneAgent до тех пор, пока все ваши ActiveGate не будут настроены с новым токеном тенанта.

1. Начните ротацию и сгенерируйте новый токен тенанта, выполнив запрос [POST начала ротации](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start "Инициация ротации токена тенанта Dynatrace.").

   Запрос возвращает новый токен в поле **active** тела ответа.
2. Добавьте новый токен в ActiveGate. Для каждого ActiveGate:

   1. [Остановите ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate в Windows или Linux.").
   2. В файле `authorization.properties` [каталога конфигурации ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux.") найдите запись для нужной среды и укажите новый токен в поле **tenantToken**.
   3. В зависимости от [назначения ActiveGate](/docs/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate."):

      * [Маршрутизация трафика OneAgent и мониторинг удалённых технологий](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."): Найдите запись для нужной среды в файлах `ruxitagent.conf` и `extensions.conf` и укажите новый токен в поле **tenantToken**.

        **Windows**: `%PROGRAMFILES%\dynatrace\remotepluginmodule\agent\conf`
        **Linux**: `/opt/dynatrace/remotepluginmodule/agent/conf`
      * [Установка модуля zRemote для мониторинга z/OS](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."): Найдите запись для нужной среды и укажите новый токен в поле **tenantToken**.

        **Windows**: `%PROGRAMFILES%\dynatrace\zremote\agent\conf\ruxitagent.conf`
        **Linux**: `/opt/dynatrace/zremote/agent/conf/ruxitagent.conf`
   4. Только для Windows. Измените значение записи реестра: `HKEY_LOCAL_MACHINE\Software\Dynatrace\Dynatrace ActiveGate\common\tenant_token`.
   5. [Запустите ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate в Windows или Linux.").
3. Добавьте новый токен в OneAgent. Для каждого OneAgent:

   1. Добавьте новый токен в настройки связи OneAgent.

      Используйте команду `--set-tenant-token` [интерфейса командной строки OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#change-oneagent-communication-settings "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки.").
   2. [Перезапустите](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки.") OneAgent.

   Вы можете объединить оба шага в одну команду:

   ```
   oneagentctl --restart-service --set-tenant-token={new token}
   ```
4. Завершите ротацию, выполнив запрос [POST завершения ротации](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-finish "Завершение ротации токена тенанта Dynatrace."). Это завершает процесс и делает старый токен недействительным.

## Связанные темы

* [API токенов тенанта](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Ротация токенов тенанта Dynatrace.")
* [Каталоги ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux.")
* [Настройка OneAgent через интерфейс командной строки](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без необходимости его переустановки.")
