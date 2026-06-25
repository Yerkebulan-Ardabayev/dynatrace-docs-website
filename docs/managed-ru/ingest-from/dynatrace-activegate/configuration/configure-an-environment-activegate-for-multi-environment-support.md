---
title: Развёртывание ActiveGate с поддержкой нескольких окружений
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support
scraped: 2026-05-12T11:52:40.838032
---

# Развёртывание ActiveGate с поддержкой нескольких окружений

# Развёртывание ActiveGate с поддержкой нескольких окружений

* 4-min read
* Updated on Feb 24, 2026

Если у вас настроено несколько окружений мониторинга, установка и поддержка нескольких ActiveGate может оказаться сложной задачей. Поэтому Dynatrace позволяет настроить один ActiveGate для поддержки нескольких окружений мониторинга. Такой ActiveGate называется **multi-environment ActiveGate**.

Эта конфигурация существенно снижает накладные расходы на обслуживание и настройку. Благодаря этой функции не нужно развёртывать несколько ActiveGate и изменять настройки брандмауэра для каждого дополнительного Environment ActiveGate. Multi-environment ActiveGate способен обрабатывать весь трафик из всех связанных с ним окружений.

Ограничения

Environment ActiveGate с поддержкой нескольких окружений **не может** использоваться для:

* **Подключения к окружениям из разных кластеров**
* Установки [модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.")
* Мониторинга удалённых технологий с помощью [фреймворка Extensions](/managed/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace.")
* Выполнения мониторов из [частных синтетических расположений](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.")
* Запуска [Database insights](/managed/observe/infrastructure-observability/databases/database-services-classic/database-insights "Узнайте, как расширить мониторинг баз данных.")

Все прочие функции ActiveGate поддерживаются.

[Extensions](/managed/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace.") не поддерживаются на multi-environment ActiveGate или Cluster ActiveGate. Для запуска Extensions развёртывайте выделенный Environment ActiveGate для каждого окружения и включайте [Extension Execution Controller (EEC)](/managed/ingest-from/extensions/concepts#eec "Узнайте о концепции Dynatrace Extensions.").

Процедура настройки существующего Environment ActiveGate для поддержки нескольких окружений

1. **Убедитесь, что несовместимые с мультиокружением модули ActiveGate отключены.** Набор установленных и включённых модулей зависит от [назначения](/managed/ingest-from/dynatrace-activegate "Понять основные концепции ActiveGate."), для которого ActiveGate был изначально установлен. На ActiveGate может присутствовать только один из следующих модулей. Если вы не уверены, отключите (и затем удалите) все они:

   * ActiveGate Extensions — отключено в разделе `[extension_controller]`
   * zRemote — отключено в разделе `[zremote]`
   * Synthetic 1.0 — отключено в разделе `[synthetic]`

   agctl

   custom.properties

   ActiveGate версии 1.333+

   Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для отключения несовместимых модулей:

   ```
   agctl modules disable rpm,zremote,synthetic,extension_controller
   ```

   Для ручного отключения модулей найдите файл `custom.properties` в [директории конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") и убедитесь, что соответствующие свойства конфигурации установлены в `false`:

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

2. **Убедитесь, что несовместимые с мультиокружением модули ActiveGate удалены.**

   * Для Linux: выполните следующие команды (в зависимости от того, какой модуль нужно удалить). Если сомневаетесь, выполните все. Если команды не найдены, соответствующие модули не установлены:

     ```
     sudo /opt/dynatrace/remotepluginmodule/uninstall.sh
     sudo /opt/dynatrace/zremote/uninstall.sh
     sudo /opt/dynatrace/synthetic/uninstall.sh
     ```

   * Для Windows: найдите и удалите следующие приложения (если установлены):

     + **Dynatrace Remote Plugin Module** (только Extensions 1.0, отсутствует в ActiveGate 1.301+)
     + **Dynatrace ZRemote**
     + **Dynatrace Synthetic**

3. **В [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") найдите файл `authorization.properties` и ознакомьтесь с его содержимым.**

   Файл `authorization.properties` определяет авторизацию ActiveGate для каждого окружения по [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте об окружениях мониторинга и работе с ними."). ActiveGate авторизуется через [токен тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его изменить.") и [индивидуальный токен ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security "Защитите ActiveGate с помощью выделенных токенов.").

   **Один и только один раздел будет содержать свойство `mainTenant = true`.** Это раздел окружения, из которого был загружен и установлен ActiveGate. **Не удаляйте этот раздел и эту запись.** Не удаляйте другие разделы (относящиеся к другим окружениям), если только не хотите, чтобы ActiveGate перестал поддерживать эти окружения.

   Формат записей в `authorization.properties`:

   ```
   [<environment_ID>]
   tenantToken = <tenant_token>
   mainTenant = true     # идентифицирует окружение, из которого загружен ActiveGate
   authToken = <individual_ActiveGate_token>
   ```

   Например:

   ```
   [mySampleEnv]
   tenantToken = abcdevjhij1234567890
   authToken = dt0g01.HVMTLRLZ.1234567890ZYXWVUTSRQPONMLKJIHGFEDCBA01234567890ABCDEFGHIGKLMNOPQ
   mainTenant = true
   ```

4. **Для создания индивидуального токена ActiveGate смотрите раздел [Генерация токена ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защитите ActiveGate с помощью выделенных токенов.").**

5. **Для добавления дополнительных окружений добавьте новые разделы в файл `authorization.properties`.**

   Перечислите каждое окружение Dynatrace, которое должен поддерживать Environment ActiveGate, в следующем формате:

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

   Обеспечение согласованности конфигурации

   Для корректной работы убедитесь, что:

   * Все окружения, поддерживаемые одним Environment ActiveGate, работают на одном кластере Dynatrace.
   * Основное окружение, связанное со свойством `mainTenant`, настроено правильно. Неверная конфигурация основного окружения приведёт к **отклонению ActiveGate во всех настроенных окружениях**: в логах ActiveGate появится ошибка с информацией о недействительной конфигурации `mainTenant`, и ActiveGate не будет отображаться на страницах Deployment Status ни в одном из окружений.

6. **Сохраните файл `authorization.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").**

7. **Убедитесь, что новые окружения успешно добавлены.**

   В [лог-файле ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") должна появиться запись с указанием количества окружений, с которыми работает ActiveGate, например:

   ```
   Working mode is set to MULTITENANT with 5 tenant(s).
   ```

   Если в сообщении лога не указано ожидаемое количество окружений, просканируйте лог-файл на наличие записей об ошибках в файле `authorization.properties`. Сообщения об ошибках имеют следующий вид:

   ```
   Error during parsing config file `...\conf\authorization.properties` - invalid configuration: ...
   ```