---
title: Интеграция с внешним хранилищем
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration
scraped: 2026-05-12T11:31:58.437491
---

# Интеграция с внешним хранилищем

# Интеграция с внешним хранилищем

* How-to guide
* 22-min read
* Updated on Jan 17, 2024

Учётные данные Synthetic Monitoring типа [username-password](/managed/manage/credential-vault#uid-password "Храните и управляйте учётными данными в хранилище.") и [token](/managed/manage/credential-vault#token "Храните и управляйте учётными данными в хранилище.") из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace можно синхронизировать с внешним хранилищем: [Azure Key Vault](#azure-key-vault), [HashiCorp Vault](#hashicorp) или [CyberArk Vault](#cyberark) (только учётные данные типа username-password). Синхронизированные учётные данные содержат ключи внешних пар «ключ-значение» с нужными значениями.

При настройке синхронизированных учётных данных в хранилище Dynatrace автоматически создаёт [HTTP-мониторы](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности сайта.") специально для синхронизации. Также можно использовать методы `api.saveCredential()` или `api.saveToken()` в [скриптах до/после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") для создания собственных мониторов синхронизации.

Автоматически созданные мониторы синхронизации именуются по ID синхронизированных учётных данных и по умолчанию выполняются ежечасно из публичного расположения Amazon US East (N. Virginia) [Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring."). Тела запросов и ответов, а также заголовки мониторов синхронизации автоматически скрываются в деталях выполнения (**Analyze execution details**).

Другие синтетические мониторы могут обращаться к этим синхронизированным учётным данным для тестирования API-эндпоинтов и сайтов. Мониторы, использующие эти учётные данные, применяют синхронизированные значения из внешних хранилищ. Частота синхронизации определяет, как часто учётные данные ротируются в синтетических мониторах.

Процесс синхронизации считывает учётные данные из внешнего хранилища и сохраняет копию в хранилище Dynatrace.

## Azure Key Vault

Учётные данные типа username-password или token для использования в синтетических мониторах можно синхронизировать с парами «ключ-значение» Azure Key Vault, содержащими имя пользователя, пароль или значение токена.

### Предварительные условия

Перед настройкой учётных данных, синхронизированных с Azure Key Vault, необходимо определить требуемые **client (application) ID** и **client secret** как [токен-учётные данные](/managed/manage/credential-vault#token "Храните и управляйте учётными данными в хранилище.") в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace. Рекомендуется называть такие вспомогательные токены так, чтобы их легко можно было идентифицировать как companion-учётные данные для синхронизации. Если в хранилище нет токенов с доступом для вас, появится предупреждение.

### Настройка синхронизированных учётных данных

1. В хранилище учётных данных создайте учётные данные типа **User and password** или **Token**. Можно также перезаписать существующие.
2. В поле **Credential scope** выберите **Synthetic**.
3. Включите **Synchronization with external vault**.
4. Выберите **Azure Key Vault** (по умолчанию) в поле **Credential source**.
5. Рекомендуется изменить **Credential name** по умолчанию для удобства идентификации.
6. Введите URL для доступа к хранилищу (**Vault URL**) и **Tenant (directory) ID**.
7. Выберите [созданные ранее companion-токены](#azure-prereqs) для полей **Client (application) ID** и **Client secret**.
8. Введите имя ключа Azure Key Vault.

   Учётные данные username-password

   Токен-учётные данные

   * В поле **Secret name for username** введите имя ключа Azure Key Vault, сопоставленного со значением имени пользователя; не вводите реальное имя пользователя.
   * В поле **Secret name for password** введите имя ключа Azure Key Vault, сопоставленного со значением пароля; не вводите реальный пароль.

   * В поле **Secret name for token** введите имя ключа Azure Key Vault, сопоставленного со значением токена; не вводите реальное значение токена.
9. Выберите **Location for synchronization** — можно выбрать любое публичное или частное расположение Synthetic для выполнения монитора синхронизации. Поиск расположения по имени доступен в поле.
10. Необязательно Укажите **Description** для учётных данных.
11. По умолчанию учётные данные имеют доступ **Owner access only**. (Подробнее о [владении учётными данными](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище.").)
12. **Save** учётные данные.

Также ознакомьтесь с [рекомендациями](#best-practices) и тем, что происходит при [редактировании или удалении синхронизированных и companion-учётных данных](#edit-delete-credential).

![Set up Azure synchronization - token](https://dt-cdn.net/images/cv-azure-token-1113-f0f69b54d9.webp)

Set up Azure synchronization - token

### Мониторы синхронизации Azure Key Vault

После [настройки синхронизированных учётных данных типа username-password или token](#azure-set-up) Dynatrace автоматически создаёт и выполняет [HTTP-монитор](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности сайта."), синхронизирующий учётные данные с Azure Key Vault. Этот монитор автоматически связывается с синхронизированными учётными данными.

Также ознакомьтесь с [рекомендациями](#best-practices) и тем, что происходит при [редактировании или удалении учётных данных синхронизации](#edit-delete-credential).

Учётные данные username-password

Токен-учётные данные

Монитор синхронизации содержит три запроса. Azure Key Vault требует разделения получения имени пользователя и пароля на два отдельных запроса.

1. Первый запрос (POST) получает токен доступа.
   Детали конфигурации запроса

   * URL запроса ссылается на ID клиента как атрибут [синхронизированных учётных данных](#azure-set-up), определённых выше; ID клиента не отображается.

     ![Azure KV request 1 URL](https://dt-cdn.net/images/cvazurerequest1url-1446-eed3251a4d.png)

     Azure KV request 1 URL
   * Client ID и client secret, ссылающиеся как атрибуты синхронизированных учётных данных, передаются как пары «ключ-значение» в [теле запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Узнайте о настройке HTTP-мониторов."); client ID и client secret не отображаются.

     ![Azure KV request 1 request body](https://dt-cdn.net/images/cvazurerequest1requestbody-984-7631f538d2.png)

     Azure KV request 1 request body
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![Azure KV request 1 post script](https://dt-cdn.net/images/cvazurerequest1postscript-962-26b361836f.png)

     Azure KV request 1 post script
2. Второй запрос (GET) получает значение имени пользователя.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#azure-set-up), определённых выше; URL хранилища не отображается. URL также содержит ссылку на ключ, сопоставленный со значением имени пользователя в Azure Key Vault.

     ![Azure KV request 2 URL](https://dt-cdn.net/images/cvazurerequest2url-1775-b114ec0406.png)

     Azure KV request 2 URL
   * [Заголовок Authorization](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит токен доступа, полученный в первом запросе.

     ![Azure KV request 2 request header](https://dt-cdn.net/images/cvazurerequest2authheader-964-9fb3850f7d.png)

     Azure KV request 2 request header
   * В теле ответа возвращается значение имени пользователя. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значение в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![Azure KV request 2 post script](https://dt-cdn.net/images/cvazurerequest2postscript-962-8bccc9e09c.png)

     Azure KV request 2 post script
3. Третий запрос (GET) получает значение пароля. В скрипте после выполнения используется `api.saveCredential()` для записи полученных значений в [синхронизированные учётные данные username-password](#azure-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#azure-set-up); URL хранилища не отображается. URL также содержит ссылку на ключ, сопоставленный со значением пароля в Azure Key Vault.

     ![Azure KV request 3 URL](https://dt-cdn.net/images/cvazurerequest3url-1777-8a113269d0.png)

     Azure KV request 3 URL
   * [Заголовок Authorization](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит токен доступа, полученный в первом запросе.
   * В теле ответа возвращается значение пароля. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значение в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveCredential()` для записи полученных значений в синхронизированные учётные данные типа username-password.

     ![Azure KV request 3 post script](https://dt-cdn.net/images/cvazurerequest3postscript-962-b44c6bda2a.png)

     Azure KV request 3 post script

Монитор синхронизации содержит два запроса.

1. Первый запрос (POST) получает токен доступа.
   Детали конфигурации запроса

   * URL запроса ссылается на ID клиента, хранящийся как атрибут [синхронизированных учётных данных](#azure-set-up), определённых выше; ID клиента не отображается.

     ![Azure KV request 1 URL](https://dt-cdn.net/images/cv-azure-token-request1-url-1446-9fd964d06c.png)

     Azure KV request 1 URL
   * Client ID и client secret, ссылающиеся как атрибуты синхронизированных учётных данных, передаются как пары «ключ-значение» в [теле запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Узнайте о настройке HTTP-мониторов."); client ID и client secret не отображаются.

     ![Azure KV request 1 request body](https://dt-cdn.net/images/cvazurerequest1requestbody-984-7631f538d2.png)

     Azure KV request 1 request body
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![Azure KV request 1 post script](https://dt-cdn.net/images/cvazurerequest1postscript-962-26b361836f.png)

     Azure KV request 1 post script
2. Второй запрос (GET) получает значение токена.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#azure-set-up), определённых выше; URL хранилища не отображается. URL также содержит ссылку на ключ, сопоставленный со значением токена в Azure Key Vault.

     ![Azure KV request 2 URL](https://dt-cdn.net/images/cv-azure-token-request2-url-1770-f949f51173.png)

     Azure KV request 2 URL
   * [Заголовок Authorization](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит токен доступа, полученный в первом запросе.

     ![Azure KV request 2 request header](https://dt-cdn.net/images/cvazurerequest2authheader-964-9fb3850f7d.png)

     Azure KV request 2 request header
   * В теле ответа возвращается значение токена. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значение в переменной. Также используется `api.saveToken()` для записи полученного значения в синхронизированные токен-учётные данные.

     ![Azure KV request 2 post script](https://dt-cdn.net/images/cv-azure-token-request2-post-script-961-337899fa61.png)

     Azure KV request 2 post script

## HashiCorp Vault

[Учётные данные типа username-password или token](#hashicorp-set-up) для использования в синтетических мониторах можно синхронизировать с парами «ключ-значение» HashiCorp Vault. Доступна аутентификация через **[AppRole](#app-role) или [сертификат](#certificate)**.

### Предварительные условия

* Перед использованием [AppRole-аутентификации](#app-role) необходимо определить **secret ID** как [токен-учётные данные](/managed/manage/credential-vault#token "Храните и управляйте учётными данными в хранилище.") в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace. Не используйте другие токены как secret ID. Если в хранилище нет токенов с доступом для вас, появится предупреждение.
* Перед использованием [аутентификации по сертификату](#certificate) необходимо сохранить нужный **TLS [сертификат](/managed/manage/credential-vault#certificate "Храните и управляйте учётными данными в хранилище.")** в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace. Если в хранилище нет сертификатов с доступом для вас, появится предупреждение.

Рекомендуется называть такие вспомогательные токены и сертификаты так, чтобы их легко можно было идентифицировать как companion-учётные данные для синхронизации.

### Настройка синхронизированных учётных данных

1. В хранилище учётных данных создайте учётные данные типа **User and password** или **Token**. Можно также перезаписать существующие.
2. В поле **Credential scope** выберите **Synthetic**.
3. Включите **Synchronization with external vault**.
4. Выберите **HashiCorp Vault** в поле **Credential source**.
5. Рекомендуется изменить **Credential name** по умолчанию для удобства идентификации.
6. Введите URL для доступа к хранилищу (**Vault URL**) и **Path to credentials** (папки разделяются прямым слешем).

   **Vault URL** HashiCorp для аутентификации по сертификату может отличаться от используемого при AppRole-аутентификации.
7. Введите имя ключа HashiCorp Vault.

   Учётные данные username-password

   Токен-учётные данные

   * В поле **Secret name for username** введите имя ключа HashiCorp Vault, сопоставленного со значением имени пользователя; не вводите реальное имя пользователя.
   * В поле **Secret name for password** введите имя ключа HashiCorp Vault, сопоставленного со значением пароля; не вводите реальный пароль.

   * В поле **Secret name for token** введите имя ключа HashiCorp Vault, сопоставленного со значением токена; не вводите реальное значение токена.
8. Выполните шаги для выбранного **Authentication method**.

   AppRole

   Certificate

   1. Выберите **AppRole** для **Authentication method**.
   2. Введите строку от HashiCorp в поле **Role ID**.
   3. Выберите [companion-токен](#hashicorp-prereqs), созданный ранее, для **Secret ID**.
   4. Введите **Vault namespace**.

   ![Set up HashiCorp AppRole synchronization - token](https://dt-cdn.net/images/cv-hashicorp-approle-token-1113-2263da2bbc.webp)

   Set up HashiCorp AppRole synchronization - token

   5. Выберите **Certificate** для **Authentication method**.
   6. В поле **Certificate** выберите [companion-сертификат TLS](#hashicorp-prereqs), созданный ранее.

   ![Set up HashiCorp certificate synchronization - UID](https://dt-cdn.net/images/cv-hashicorp-certificate-uid-1113-8b177811b5.webp)

   Set up HashiCorp certificate synchronization - UID
9. Выберите **Location for synchronization** — можно выбрать любое публичное или частное расположение Synthetic для выполнения монитора синхронизации. Поиск расположения по имени доступен в поле.
10. Необязательно Укажите **Description**.
11. По умолчанию учётные данные имеют доступ **Owner access only**. (Подробнее о [владении учётными данными](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище.").)
12. **Save** учётные данные.

Также ознакомьтесь с [рекомендациями](#best-practices) и тем, что происходит при [редактировании или удалении синхронизированных и companion-учётных данных](#edit-delete-credential).

После настройки синхронизированных учётных данных Dynatrace автоматически создаёт и выполняет [HTTP-монитор](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности сайта."), синхронизирующий учётные данные с HashiCorp Vault.

### Мониторы синхронизации HashiCorp Vault AppRole

Автоматически созданный HTTP-монитор содержит два запроса и автоматически связывается с [синхронизированными учётными данными](#hashicorp-set-up), определёнными выше.

Учётные данные username-password

Токен-учётные данные

1. Первый запрос (POST) получает клиентский токен.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#hashicorp-set-up); URL хранилища не отображается. URL также содержит метод аутентификации `approle`.

     ![HashiCorp AppRole request 1 URL](https://dt-cdn.net/images/cvhashiapprolerequest1url-1447-20b5ca2512.png)

     HashiCorp AppRole request 1 URL
   * Пространство имён хранилища (namespace), ссылающееся как атрибут синхронизированных учётных данных, передаётся как [заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов."); пространство имён не отображается.

     ![HashiCorp AppRole request 1 header](https://dt-cdn.net/images/cvhashiapprolerequest1requestheader-964-7efd88a7af.png)

     HashiCorp AppRole request 1 header
   * Role ID и secret ID, ссылающиеся как атрибуты синхронизированных учётных данных, передаются как пары «ключ-значение» в [теле запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Узнайте о настройке HTTP-мониторов."); role ID и secret ID не отображаются.

     ![HashiCorp AppRole request 1 body](https://dt-cdn.net/images/cvhashiapprolerequest1requestbody-966-5eb6ad4427.png)

     HashiCorp AppRole request 1 body
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![HashiCorp AppRole request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)

     HashiCorp AppRole request 1 post script
2. Второй запрос (GET) получает значения имени пользователя и пароля. В скрипте после выполнения используется `api.saveCredential()` для записи полученных значений в [синхронизированные учётные данные username-password](#hashicorp-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища и путь к учётным данным как атрибуты синхронизированных учётных данных; URL хранилища и путь не отображаются.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)

     HashiCorp AppRole request 2 URL
   * [Заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит клиентский токен, полученный в первом запросе. Пространство имён хранилища (не отображается, но ссылается как атрибут синхронизированных учётных данных) также передаётся как заголовок.

     ![HashiCorp AppRole request 2 headers](https://dt-cdn.net/images/cvhashiapprolerequest2requestheader-964-739c560649.png)

     HashiCorp AppRole request 2 headers
   * Значения имени пользователя и пароля возвращаются в JSON-ответе. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значения в [глобальных переменных](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveCredential()` для записи значений в синхронизированные учётные данные типа username-password.

     ![HashiCorp AppRole request 2 post script](https://dt-cdn.net/images/cvhashiapprolerequest2postscript-964-828da84802.png)

     HashiCorp AppRole request 2 post script

1. Первый запрос (POST) получает клиентский токен.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#hashicorp-set-up); URL хранилища не отображается. URL также содержит метод аутентификации `approle`.

     ![HashiCorp AppRole request 1 URL](https://dt-cdn.net/images/cvhashiapprolerequest1url-1447-20b5ca2512.png)

     HashiCorp AppRole request 1 URL
   * Пространство имён хранилища, ссылающееся как атрибут синхронизированных учётных данных, передаётся как [заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов."); пространство имён не отображается.

     ![HashiCorp AppRole request 1 header](https://dt-cdn.net/images/cvhashiapprolerequest1requestheader-964-7efd88a7af.png)

     HashiCorp AppRole request 1 header
   * Role ID и secret ID, ссылающиеся как атрибуты синхронизированных учётных данных, передаются как пары «ключ-значение» в [теле запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Узнайте о настройке HTTP-мониторов."); role ID и secret ID не отображаются.

     ![HashiCorp AppRole request 1 body](https://dt-cdn.net/images/cvhashiapprolerequest1requestbody-966-5eb6ad4427.png)

     HashiCorp AppRole request 1 body
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![HashiCorp AppRole request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)

     HashiCorp AppRole request 1 post script
2. Второй запрос (GET) получает значение токена. В скрипте после выполнения используется `api.saveToken()` для записи полученных значений в [синхронизированные токен-учётные данные](#hashicorp-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища и путь к учётным данным как атрибуты синхронизированных учётных данных; URL хранилища и путь не отображаются.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)

     HashiCorp AppRole request 2 URL
   * [Заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит клиентский токен, полученный в первом запросе. Пространство имён хранилища (не отображается, но ссылается как атрибут синхронизированных учётных данных) также передаётся как заголовок.

     ![HashiCorp AppRole request 2 headers](https://dt-cdn.net/images/cvhashiapprolerequest2requestheader-964-739c560649.png)

     HashiCorp AppRole request 2 headers
   * Значение токена возвращается в JSON-ответе. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значение в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveToken()` для записи значения в синхронизированные токен-учётные данные.

     ![HashiCorp AppRole request 2 post-script to save token](https://dt-cdn.net/images/cv-hashi-approle-request2-postscript-savetoken-936-a139146cec.png)

     HashiCorp AppRole request 2 post-script to save token

### Мониторы синхронизации HashiCorp Vault через TLS-сертификат

Автоматически созданный HTTP-монитор содержит два запроса и автоматически связывается с [синхронизированными учётными данными](#hashicorp-set-up), определёнными выше.

Учётные данные username-password

Токен-учётные данные

1. Первый запрос (POST) получает клиентский токен.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#hashicorp-set-up); URL хранилища не отображается. URL также содержит метод аутентификации `cert`.

     ![HashiCorp certificate request 1 URL](https://dt-cdn.net/images/cvhashicertificaterequest1url-1448-630ba53192.png)

     HashiCorp certificate request 1 URL
   * Запрос использует TLS-сертификат для аутентификации.

     ![HashiCorp certificate request 1 certificate](https://dt-cdn.net/images/cvhashicertificaterequest1cert-964-996d51d92a.png)

     HashiCorp certificate request 1 certificate
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![HashiCorp certificate request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)

     HashiCorp certificate request 1 post script
2. Второй запрос (GET) получает значения имени пользователя и пароля. В скрипте после выполнения используется `api.saveCredential()` для записи полученных значений в [синхронизированные учётные данные username-password](#hashicorp-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища и путь к учётным данным как атрибуты синхронизированных учётных данных; URL хранилища и путь не отображаются.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)

     HashiCorp AppRole request 2 URL
   * [Заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит клиентский токен, полученный в первом запросе.

     ![HashiCorp certificate request 2 header](https://dt-cdn.net/images/cvhashicertificaterequest2requestheader-964-230e35242e.png)

     HashiCorp certificate request 2 header
   * Значения имени пользователя и пароля возвращаются в JSON-ответе. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значения в [глобальных переменных](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveCredential()` для записи значений в синхронизированные учётные данные типа username-password.

     ![HashiCorp certificate request 2 post script](https://dt-cdn.net/images/cvhashiapprolerequest2postscript-964-828da84802.png)

     HashiCorp certificate request 2 post script

1. Первый запрос (POST) получает клиентский токен.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища как атрибут [синхронизированных учётных данных](#hashicorp-set-up); URL хранилища не отображается. URL также содержит метод аутентификации `cert`.

     ![HashiCorp certificate request 1 URL](https://dt-cdn.net/images/cvhashicertificaterequest1url-1448-630ba53192.png)

     HashiCorp certificate request 1 URL
   * Запрос использует TLS-сертификат для аутентификации.

     ![HashiCorp certificate request 1 certificate](https://dt-cdn.net/images/cvhashicertificaterequest1cert-964-996d51d92a.png)

     HashiCorp certificate request 1 certificate
   * В теле ответа возвращается клиентский токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![HashiCorp certificate request 1 post script](https://dt-cdn.net/images/cvhashiapprolerequest1postscript-964-48e414d846.png)

     HashiCorp certificate request 1 post script
2. Второй запрос (GET) получает значение токена. В скрипте после выполнения используется `api.saveToken()` для записи полученного значения в [синхронизированные токен-учётные данные](#hashicorp-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на URL хранилища и путь к учётным данным как атрибуты синхронизированных учётных данных; URL хранилища и путь не отображаются.

     ![HashiCorp AppRole request 2 URL](https://dt-cdn.net/images/cvhashiapprolerequest2url-1777-d33a680540.png)

     HashiCorp AppRole request 2 URL
   * [Заголовок запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.") содержит клиентский токен, полученный в первом запросе.

     ![HashiCorp certificate request 2 header](https://dt-cdn.net/images/cvhashicertificaterequest2requestheader-964-230e35242e.png)

     HashiCorp certificate request 2 header
   * Значение токена возвращается в JSON-ответе. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значение в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveToken()` для записи значения в синхронизированные токен-учётные данные.

     ![HashiCorp certificate request 2 post-script to save token](https://dt-cdn.net/images/cv-hashi-approle-request2-postscript-savetoken-936-a139146cec.png)

     HashiCorp certificate request 2 post-script to save token

## CyberArk Vault

Учётные данные типа username-password для использования в синтетических мониторах можно синхронизировать с парами «ключ-значение» CyberArk Vault. Доступна аутентификация по [имени пользователя и паролю](#cyberark-monitor-uid-authentication) или [на основе хостов](#cyberark-monitor-allowed-machines). Аутентификация на основе хостов позволяет заранее определить в CyberArk Vault хосты (**Allowed Machines**), имеющие доступ к учётным данным. Эти хосты — это [публичные или частные расположения Synthetic](#cyberark-set-up), выбранные для выполнения мониторов синхронизации; они определяются по имени хоста или IP-адресу. Аутентификация на основе хостов позволяет мониторам синхронизации обходить получение токена доступа от CyberArk Vault.

### Предварительные условия

* Перед использованием [аутентификации по имени пользователя и паролю](#cyberark-monitor-uid-authentication) необходимо определить учётные данные для аутентификации в CyberArk Vault: [пару username-password](/managed/manage/credential-vault#uid-password "Храните и управляйте учётными данными в хранилище.") и опционально [сертификатные учётные данные](/managed/manage/credential-vault#certificate "Храните и управляйте учётными данными в хранилище.") в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace. Рекомендуется называть такие companion-учётные данные так, чтобы их было легко идентифицировать.
* Перед использованием [аутентификации на основе хостов](#cyberark-monitor-allowed-machines) необходимо определить **Allowed Machines** по имени хоста или IP-адресу в разделе CyberArk Vault Application Details. Это хосты, которым разрешён доступ к синхронизированным учётным данным в CyberArk Vault, и это публичные или частные расположения Synthetic, выбранные для выполнения мониторов синхронизации. При определении allowed machines в CyberArk Vault ID приложения должен совпадать с указанным при [настройке синхронизированных учётных данных в Dynatrace](#cyberak-set-up). Опционально можно также определить [сертификатные учётные данные](/managed/manage/credential-vault#certificate "Храните и управляйте учётными данными в хранилище.") в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") Dynatrace для аутентификации в CyberArk Vault. Если в хранилище нет сертификатов с доступом для вас, появится предупреждение.

Рекомендуется называть любые вспомогательные учётные данные так, чтобы их было легко идентифицировать как companion-учётные данные для синхронизации.

### Настройка синхронизированных учётных данных

1. В хранилище учётных данных создайте учётные данные типа **User and password**. Можно также перезаписать существующие.
2. В поле **Credential scope** выберите **Synthetic**.
3. Включите **Synchronization with external vault**.
4. Выберите **CyberArk Vault** в поле **Credential source**.
5. Рекомендуется изменить **Credential name** по умолчанию для удобства идентификации.
6. Введите **Central Credential Provider URL** (HTTPS) для доступа к хранилищу.
7. Выполните шаги для выбранного **Authentication method**.

   Username and password

   Allowed machines

   1. Выберите **Username and password** для **Authentication method**.
   2. Выберите [companion-учётные данные username-password](#cyberark-prereqs), созданные ранее для аутентификации в CyberArk, из списка **Username and password for Central Credential Provider**.

   ![Set up CyberArk synchronization - UID](https://dt-cdn.net/images/cyberark-credential-vault-uid-1145-62675d95c7.webp)

   Set up CyberArk synchronization - UID

   1. Выберите **Allowed machines (location)** для **Authentication method**.

      Имя хоста или IP-адрес выбранного **Location for synchronization** должны уже быть зарегистрированы в списке CyberArk Allowed Machines — см. [Предварительные условия](#cyberark-prereqs).

   ![Set up CyberArk synchronization - allowed machines](https://dt-cdn.net/images/cyberark-credential-vault-allowed-machines-1154-a9d5d09098.webp)

   Set up CyberArk synchronization - allowed machines
8. Рекомендуется Выберите **Certificate used for authentication to CyberArk application** из предложенного списка.
9. Заполните дополнительные поля для идентификации пары «ключ-значение» CyberArk Vault.

   * **Application ID** — должен совпадать с ID приложения при определении allowed machines в CyberArk Vault — см. [Предварительные условия](#cyberark-prereqs).
   * **Safe name**
   * **Account name** — имя объекта, хранящего имя пользователя и пароль для получения и синхронизации с хранилищем учётных данных Dynatrace; это не имя аккаунта, вошедшего в CyberArk Central Credential Provider.
   * **Folder name** Необязательно — имя папки, где хранятся учётные данные в CyberArk Vault; имя папки по умолчанию: `Root`.
10. Выберите **Location for synchronization** — можно выбрать любое публичное или частное расположение Synthetic для выполнения монитора синхронизации. Поиск расположения по имени доступен в поле.
11. Необязательно Укажите **Description** для учётных данных.
12. По умолчанию учётные данные имеют доступ **Owner access only**. (Подробнее о [владении учётными данными](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище.").)
13. **Save** учётные данные.

Также ознакомьтесь с [рекомендациями](#best-practices) и тем, что происходит при [редактировании или удалении синхронизированных и companion-учётных данных](#edit-delete-credential).

После настройки синхронизированных учётных данных Dynatrace автоматически создаёт и выполняет [HTTP-монитор](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности сайта."), синхронизирующий учётные данные с CyberArk Vault.

### Мониторы синхронизации CyberArk Vault (аутентификация по имени пользователя и паролю)

Автоматически созданный HTTP-монитор содержит два запроса и автоматически связывается с [синхронизированными учётными данными](#cyberark-set-up), определёнными выше.

1. Первый запрос (POST) получает токен доступа.
   Детали конфигурации запроса

   * URL запроса ссылается на **Central Credential Provider URL** как атрибут [синхронизированных учётных данных](#cyberark-set-up), определённых выше; URL не отображается.

     ![CyberArk Vault request 1 URL](https://dt-cdn.net/images/cv-cyberark-request1-url-1445-f352bc0566.png)

     CyberArk Vault request 1 URL
   * [Тело запроса](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#request-body "Узнайте о настройке HTTP-мониторов.") ссылается на учётные данные username-password, выбранные для аутентификации в CyberArk Vault (**Username and password for Central Credential Provider**); имя пользователя и пароль не отображаются.

     ![CyberArk Vault request 1 request body](https://dt-cdn.net/images/cv-cyberark-request1-request-body-1409-efb85f9433.png)

     CyberArk Vault request 1 request body
   * Дополнительно первый запрос содержит любой сертификат аутентификации, указанный в **Certificate used for authentication to CyberArk**.

     ![CyberArk Vault request 1 certificate](https://dt-cdn.net/images/cv-cyberark-request1-certificate-962-8b7934f165.png)

     CyberArk Vault request 1 certificate
   * В теле ответа возвращается токен. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет токен в [глобальной переменной](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам.").

     ![CyberArk Vault request 1 post script](https://dt-cdn.net/images/cv-cyberark-request1-post-script-962-04c94bf083.png)

     CyberArk Vault request 1 post script
2. Второй запрос (GET) получает значения имени пользователя и пароля из CyberArk Vault. В скрипте после выполнения используется `api.saveCredential()` для записи полученных значений в [синхронизированные учётные данные username-password](#cyberark-set-up), определённые выше.
   Детали конфигурации запроса

   * URL запроса ссылается на **Central Credential Provider URL** как атрибут синхронизированных учётных данных; URL не отображается. Также содержатся ссылки (без отображения) на **Application ID**, **Safe name**, **Account name** и **Folder name**.

     ![CyberArk Vault request 2 URL](https://dt-cdn.net/images/cv-cyberark-request2-url-1879-7911c0b652.png)

     CyberArk Vault request 2 URL
   * Второй запрос также содержит любой сертификат аутентификации и токен доступа из первого запроса в [заголовке Authorization](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#headers "Узнайте о настройке HTTP-мониторов.").

     ![CyberArk Vault request 2 token and certificate](https://dt-cdn.net/images/cv-cyberark-request2-certificate-auth-header-1269-b10aa9737b.png)

     CyberArk Vault request 2 token and certificate
   * Значения имени пользователя и пароля возвращаются в теле ответа. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значения в [глобальных переменных](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveCredential()` для записи значений в синхронизированные учётные данные типа username-password.

     ![CyberArk Vault request 2 post script](https://dt-cdn.net/images/cv-cyberark-request2-post-script-999-5b4607154b.png)

     CyberArk Vault request 2 post script

### Мониторы синхронизации CyberArk Vault (аутентификация на основе хостов)

Поскольку автоматически созданный HTTP-монитор может обходить получение токена доступа, он содержит один GET-запрос для получения значений имени пользователя и пароля из CyberArk Vault. В скрипте после выполнения используется `api.saveCredential()` для записи полученных значений в [синхронизированные учётные данные username-password](#cyberark-set-up), определённые выше. Монитор синхронизации автоматически связывается с синхронизированными учётными данными.

Детали конфигурации запроса

* URL запроса ссылается на **Central Credential Provider URL** как атрибут синхронизированных учётных данных; URL не отображается. Также содержатся ссылки (без отображения) на **Application ID**, **Safe name**, **Account name** и **Folder name**.

![CyberArk Vault allowed machines request URL](https://dt-cdn.net/images/cv-cyberark-allowed-machines-url-1881-1ea05be669.jpg)

CyberArk Vault allowed machines request URL

* Запрос также содержит любой сертификат аутентификации, указанный при настройке учётных данных.

![CyberArk Vault allowed machines authentication certificate](https://dt-cdn.net/images/cv-cyberark-allowed-machines-certificate-1415-568a21181f.jpg)

CyberArk Vault allowed machines authentication certificate

* Значения имени пользователя и пароля возвращаются в теле ответа. [Скрипт после выполнения](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять скрипты до и после выполнения к запросам.") сохраняет значения в [глобальных переменных](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic#variables "Узнайте, как применять скрипты до и после выполнения к запросам."). Также вызывается `api.saveCredential()` для записи значений в синхронизированные учётные данные типа username-password.

![CyberArk Vault allowed machines post script](https://dt-cdn.net/images/cv-cyberark-allowed-machines-post-script-1415-5e3ea56704.jpg)

CyberArk Vault allowed machines post script

## Рекомендации и ограничения

При создании монитора синхронизации вручную обязательно выберите **Do not store and display request and response bodies and header values in execution details** для всех запросов, получающих клиентские токены или значения учётных данных из внешних хранилищ. В противном случае конфиденциальная информация будет раскрыта при **Analyze execution details** на [странице деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице деталей синтетических HTTP-мониторов.").

* Автоматически созданные мониторы синхронизации можно редактировать. Для редактирования автоматически созданного монитора синхронизации необходимо иметь [доступ к учётным данным](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище."), на которые ссылается монитор. Редактирование может потребоваться, если поставщик внешнего хранилища вносит изменения. Например, может потребоваться изменить URL запросов, если Microsoft изменяет версию API для получения клиентских токенов из Azure Key Vault.

  + В общем случае рекомендуется ограничивать изменения частотой выполнения или расположениями.
  + При изменении расположения избегайте [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") без внешнего доступа к сети.
  + При переходе на частное расположение Synthetic убедитесь, что конфигурация прокси не блокирует доступ к нужным ресурсам.
* Рекомендуется редактировать имена синхронизированных учётных данных, companion-учётных данных (например, TLS-сертификатов для HashiCorp Vault) и мониторов синхронизации для удобства идентификации.
* Не рекомендуется повторно использовать companion-учётные данные (например, токен secret ID для HashiCorp) в других синтетических мониторах для тестирования.

### Редактирование или удаление синхронизированных и companion-учётных данных

* После создания синхронизированные учётные данные не могут быть изменены никем; их можно только [перезаписать](/managed/manage/credential-vault#overwrite-credential "Храните и управляйте учётными данными в хранилище."). При перезаписи синхронизированных учётных данных необходимо указать новые данные синхронизации; не вводите реальные значения имени пользователя, пароля или токена.

  + При перезаписи синхронизированных учётных данных созданные Dynatrace мониторы синхронизации обновляются автоматически.
* Убедитесь, что [владение](/managed/manage/credential-vault#owner-shared-public "Храните и управляйте учётными данными в хранилище.") одинаково для всех учётных данных в мониторе синхронизации (то есть синхронизированных учётных данных и companion-учётных данных).
* Нельзя удалить companion-учётные данные, на которые ссылается монитор синхронизации, без его отключения или удаления.
* При удалении синхронизированных учётных данных их автоматически созданный монитор синхронизации также удаляется.

  + При наличии более одного монитора синхронизации необходимо удалить или отключить такие мониторы перед удалением синхронизированных учётных данных.
  + Любой синтетический монитор, использующий удалённые синхронизированные учётные данные для тестирования, отключается.