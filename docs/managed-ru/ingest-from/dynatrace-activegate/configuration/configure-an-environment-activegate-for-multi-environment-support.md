---
title: Развёртывание ActiveGate в нескольких средах
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support
---

# Развёртывание ActiveGate в нескольких средах

# Развёртывание ActiveGate в нескольких средах

* Чтение: 4 мин
* Обновлено 09 июл 2026 г.

Если настроено несколько сред мониторинга, установка и обслуживание нескольких ActiveGate может быть обременительным. Поэтому Dynatrace позволяет настроить один ActiveGate для поддержки нескольких сред мониторинга. Такой ActiveGate называется **многосредовым ActiveGate**.

Такая конфигурация существенно снижает накладные расходы на обслуживание и настройку. Благодаря этой функции не нужно развёртывать несколько ActiveGate и не нужно настраивать параметры брандмауэра для каждого дополнительного Environment ActiveGate. Многосредовые ActiveGate способны обрабатывать весь трафик из всех связанных с ними сред.

Ограничения

**Нельзя** использовать Environment ActiveGate, настроенный для поддержки нескольких сред, для:

* **Подключения к средам из разных кластеров**
* Установки [модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.")
* Мониторинга удалённых технологий с помощью [фреймворка Extensions](/managed/ingest-from/extensions "Узнайте, как создавать Extensions Dynatrace и управлять ими.")
* Выполнения мониторов из [частных Synthetic-локаций](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частную локацию для синтетического мониторинга.")
* Запуска [Database insights](/managed/observe/infrastructure-observability/database-services-classic/database-insights "Узнайте, как расширить мониторинг баз данных до уровня инфраструктуры.")

Все остальные функции ActiveGate поддерживаются.

[Extensions](/managed/ingest-from/extensions "Узнайте, как создавать Extensions Dynatrace и управлять ими.") не поддерживаются на многосредовых ActiveGate или Cluster ActiveGate. Для запуска Extensions нужно развернуть отдельный Environment ActiveGate для каждой среды и включить [Extension Execution Controller (EEC)](/managed/ingest-from/extensions/concepts#eec "Подробнее о концепции Extensions Dynatrace.").

Настройка существующего Environment ActiveGate для поддержки нескольких сред

1. **Убедитесь, что модули ActiveGate, несовместимые с многосредовой работой, отключены.** Набор фактически установленных и включённых модулей зависит от [назначения](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с основными концепциями ActiveGate."), для которого ActiveGate был изначально установлен. На ActiveGate может присутствовать только один из следующих модулей. Однако если есть сомнения, на данном этапе допустимо отключить (а затем удалить) все перечисленные модули:

   * ActiveGate Extensions, отключается в секции `[extension_controller]`
   * zRemote, отключается в секции `[zremote]`
   * Synthetic 1.0, отключается в секции `[synthetic]`

   agctl

   custom.properties

   ActiveGate version 1.333+

   Для отключения несовместимых модулей можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Узнайте, как использовать agctl для настройки ActiveGate и управления им из командной строки"):

   ```
   agctl modules disable rpm,zremote,synthetic,extension_controller
   ```

   Чтобы отключить модули вручную, найдите файл `custom.properties` в [директории конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux.") и убедитесь, что соответствующие свойства конфигурации имеют значение `false`:

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
2. **Убедитесь, что модули ActiveGate, несовместимые с многосредовой работой, удалены.**

   * Для Linux: выполните одну из следующих команд в зависимости от того, какой модуль нужно удалить. Если есть сомнения, выполните все команды. Если команды найдены, соответствующие модули будут удалены. Если команды не найдены, значит модули не установлены:

     ```
     sudo /opt/dynatrace/remotepluginmodule/uninstall.sh



     sudo /opt/dynatrace/zremote/uninstall.sh



     sudo /opt/dynatrace/synthetic/uninstall.sh
     ```
   * Для Windows: найдите и удалите следующие приложения, если они установлены:

     + **Dynatrace Remote Plugin Module** (только Extensions 1.0, отсутствует в ActiveGate 1.301+)
     + **Dynatrace ZRemote**
     + **Dynatrace Synthetic**
3. **В [директории конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux.") ActiveGate найдите файл `authorization.properties` и ознакомьтесь с его содержимым.**  
   Файл `authorization.properties` определяет авторизацию ActiveGate для каждой среды, идентифицируемой по [идентификатору среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, что такое среда мониторинга Dynatrace, как найти идентификатор среды и как настроить несколько сред."). ActiveGate выполняет авторизацию через [tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое tenant token и как его изменить.") и [индивидуальный токен ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security "Защита ActiveGate с помощью выделенных токенов.").
   **Ровно одна из секций будет содержать свойство `mainTenant = true`.** Это секция среды, из которой был загружен и установлен ActiveGate. **Не удаляйте эту секцию и эту запись.** Не удаляйте и другие секции (относящиеся к другим средам), если только не нужно отключить поддержку этих конкретных сред.

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
4. **Для создания индивидуального токена ActiveGate см. [Генерация токена ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защита ActiveGate с помощью выделенных токенов.")**.
5. **Для добавления новых сред добавьте новые секции в файл `authorization.properties`.**  
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

   Обеспечение согласованной конфигурации

   Для корректной работы необходимо убедиться, что:

   * Все среды, которые должен поддерживать один Environment ActiveGate, работают на одном Dynatrace Cluster.
   * Основная среда, связанная со свойством конфигурации `mainTenant`, настроена корректно. Некорректная конфигурация основной среды приведёт к **отклонению ActiveGate во всех настроенных средах**: в логах ActiveGate будет зафиксирована ошибка с сообщением о недопустимой конфигурации `mainTenant`, и ActiveGate не будет отображаться в **Deployment Status** ни в одной из сред.
6. **Сохраните файл `authorization.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate в Windows или Linux.").**
7. **Убедитесь, что новые среды добавлены успешно.**  
   [Файл логов ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux.") должен содержать запись с указанием количества сред, с которыми работает ActiveGate, например:

   ```
   Working mode is set to MULTITENANT with 5 tenant(s).
   ```

   Если в сообщении лога не указано количество сред, которые вы пытались настроить, просмотрите файл лога на наличие записей, указывающих на ошибку в файле `authorization.properties`. Сообщения об ошибках имеют следующий вид:

   ```
   Error during parsing config file `...\conf\authorization.properties` - invalid configuration: ...
   ```