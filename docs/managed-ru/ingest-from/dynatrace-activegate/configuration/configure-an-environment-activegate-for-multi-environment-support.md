---
title: Развёртывание ActiveGate для нескольких сред
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support
---

# Развёртывание ActiveGate для нескольких сред

# Развёртывание ActiveGate для нескольких сред

* 4 мин чтения
* Обновлено 24 февр. 2026 г.

Если настроено несколько мониторинговых сред, установка и поддержка нескольких ActiveGate может оказаться обременительной. Поэтому Dynatrace позволяет настроить один ActiveGate для поддержки нескольких мониторинговых сред. Такой ActiveGate называется **ActiveGate для нескольких сред**.

Такая конфигурация значительно сокращает затраты на обслуживание и настройку. Благодаря этой функции не нужно разворачивать несколько ActiveGate и не нужно настраивать firewall для каждого дополнительного Environment ActiveGate. ActiveGate для нескольких сред способны обрабатывать весь трафик от всех сред, с которыми они связаны.

Ограничения

Environment ActiveGate, настроенный для поддержки нескольких сред, **нельзя** использовать для:

* **Подключения к средам из разных кластеров**
* Установки [модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.")
* Мониторинга удалённых технологий с помощью фреймворка [Extensions](/managed/ingest-from/extensions "Узнайте, как создавать Extensions Dynatrace и управлять ими.")
* Запуска мониторов из [приватных Synthetic-локаций](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для synthetic-мониторинга.")
* Запуска [Database insights](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Узнайте, как расширить мониторинг баз данных на уровень инфраструктуры базы данных.")

Все остальные функции ActiveGate поддерживаются.

[Extensions](/managed/ingest-from/extensions "Узнайте, как создавать Extensions Dynatrace и управлять ими.") не поддерживаются на ActiveGate для нескольких сред и на Cluster ActiveGate. Для запуска Extensions нужно развернуть отдельный Environment ActiveGate для каждой среды и включить [Extension Execution Controller (EEC)](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Extensions Dynatrace.").

Настройка существующего Environment ActiveGate для поддержки нескольких сред

1. **Убедитесь, что модули ActiveGate, несовместимые с работой в режиме нескольких сред, отключены.** Какой модуль фактически установлен и включён, зависит от [назначения](/managed/ingest-from/dynatrace-activegate "Основные концепции, связанные с ActiveGate."), для которого ActiveGate изначально устанавливался. На ActiveGate может присутствовать только один из следующих модулей. Однако, если есть сомнения, на этом этапе допустимо отключить (а затем удалить) все эти модули:

   * Extensions ActiveGate, отключается в разделе `[extension_controller]`
   * zRemote, отключается в разделе `[zremote]`
   * Synthetic 1.0, отключается в разделе `[synthetic]`

   agctl

   custom.properties

   ActiveGate версии 1.333+

   Для отключения несовместимых модулей можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки"):

   ```
   agctl modules disable rpm,zremote,synthetic,extension_controller
   ```

   Чтобы отключить модули вручную, найдите файл `custom.properties` в [каталоге конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux."), и убедитесь, что соответствующие параметры конфигурации установлены в `false`:

   ```
   [rpm]



   rpm_enabled = false



   [zremote]



   zremote_enabled = false



   [synthetic]



   synthetic_enabled = false



   [extension_controller]



   extension_controller_enabled = false
   ```
2. **Убедитесь, что модули ActiveGate, несовместимые с работой в режиме нескольких сред, удалены.**

   * Для Linux, выполните одну из следующих команд, в зависимости от того, какой модуль нужно удалить. При сомнениях выполните все команды: если команды найдены, соответствующие модули будут удалены. Если команды не найдены, это означает, что модули отсутствуют:

     ```
     sudo /opt/dynatrace/remotepluginmodule/uninstall.sh



     sudo /opt/dynatrace/zremote/uninstall.sh



     sudo /opt/dynatrace/synthetic/uninstall.sh
     ```
   * Для Windows: найдите и удалите следующие приложения, если они установлены:

     + **Dynatrace Remote Plugin Module** (только Extensions 1.0, отсутствует в ActiveGate 1.301+)
     + **Dynatrace ZRemote**
     + **Dynatrace Synthetic**
3. **В [каталоге конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.") ActiveGate найдите файл `authorization.properties` и ознакомьтесь с его содержимым.**  
   Файл `authorization.properties` определяет авторизацию ActiveGate для каждой среды, идентифицируемой по [ID среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое мониторинговая среда Dynatrace, как найти ID своей среды и как настроить и подключить несколько сред."). ActiveGate авторизуется с помощью [токена клиента (tenant token)](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен клиента и как его изменить.") и [индивидуального токена ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security "Защита ActiveGate выделенными токенами.").
   **Только один из разделов будет содержать параметр `mainTenant = true`.** Он относится к среде, из которой ActiveGate был скачан и установлен. **Не удаляйте этот раздел или эту запись.** Не удаляйте никакие другие разделы, относящиеся к другим средам, если только не требуется, чтобы ActiveGate больше не поддерживал эти конкретные среды.

   Формат записей в `authorization.properties`:

   ```
   [<environment_ID>]



   tenantToken = <tenant_token>



   mainTenant = true     # identifies environment from which the ActiveGate was downloaded



   authToken = <individual_ActiveGate_token>
   ```

   Например:

   ```
   [mySampleEnv]



   tenantToken = abcdevjhij1234567890



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJIHGFEDCBA01234567890ABCDEFGHIGKLMNOPQ



   mainTenant = true
   ```
4. **Для создания индивидуального токена ActiveGate см. [Создание токена ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защита ActiveGate выделенными токенами.")**.
5. **Чтобы добавить дополнительные среды, добавьте новые разделы в файл `authorization.properties`.**  
   Перечислите каждую среду Dynatrace, которую должен поддерживать Environment ActiveGate. Используйте следующий формат:

   ```
   [<environment_ID>]



   tenantToken = <tenant_token>



   mainTenant = true



   authToken = <individual_ActiveGate_token>



   [<environment_ID>]



   tenantToken = <tenant_token>



   authToken = <individual_ActiveGate_token>
   ```

   Например:

   ```
   [mySampleEnv]



   tenantToken = abcdevjhij1234567890



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJIHGFEDCBA01234567890ABCDEFGHIGKLMNOPQ



   mainTenant = true



   [myAnotherEnv]



   tenantToken = 0987654321jijvedcba



   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJZYXWVUTSRQPONMLKJIHGFE56GHMNO890ZABCD
   ```

   Обеспечьте согласованность конфигурации

   Для корректной работы необходимо убедиться, что:

   * Все среды, которые должны поддерживаться одним и тем же Environment ActiveGate, работают в одном и том же кластере Dynatrace.
   * Основная среда, связанная с параметром конфигурации `mainTenant`, настроена корректно. Некорректная настройка основной среды приведёт к **отклонению ActiveGate во всех настроенных средах**: в логах ActiveGate будет зафиксирована ошибка с информацией о том, что конфигурация `mainTenant` недействительна, и ActiveGate не будет отображаться на страницах статуса развёртывания ни в одной из сред.
6. **Сохраните файл `authorization.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запускать, останавливать и перезапускать ActiveGate в Windows или Linux.").**
7. **Убедитесь, что новые среды были успешно добавлены.**  
   [Файл журнала ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.") должен содержать запись с указанием числа сред, с которыми работает ActiveGate, например:

   ```
   Working mode is set to MULTITENANT with 5 tenant(s).
   ```

   Если в сообщении журнала не указано число сред, которые вы пытались настроить, просмотрите файл журнала на предмет записей, указывающих на ошибку в файле `authorization.properties`. Сообщения об ошибках имеют следующий вид:

   ```
   Error during parsing config file `...\conf\authorization.properties` - invalid configuration: ...
   ```