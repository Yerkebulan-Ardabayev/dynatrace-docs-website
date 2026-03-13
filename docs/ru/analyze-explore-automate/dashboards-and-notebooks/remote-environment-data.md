---
title: Remote environment data
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/remote-environment-data
scraped: 2026-03-03T21:23:07.840378
---

# Данные удалённого окружения

# Данные удалённого окружения

* Актуальная версия Dynatrace
* Руководство
* Время чтения: 9 мин
* Обновлено 02 декабря 2024

С помощью [плиток кода](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Добавление кода на дашборды Dynatrace.") (в Dashboards) и [секций кода](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") (в Notebooks) вы можете консолидировать данные из нескольких окружений Dynatrace.

Доступны два механизма аутентификации для получения данных из удалённых окружений:

* **Аутентификация с помощью платформенного токена**: предназначена для личного использования. Используйте для быстрого тестирования и оперативного получения данных из удалённых окружений.
* **Аутентификация через OAuth-клиент**: предназначена для совместного использования. Используйте для обеспечения согласованной видимости данных для всех пользователей.

Новое! Начните со сниппета в Dashboards или Notebooks

Dashboards версии 1.310+ Notebooks версии 1.310+

Теперь вы можете начать со сниппета при создании дашборда или ноутбука, использующего данные из удалённого окружения Dynatrace.

* > **Fetch external data**
* > **Remote environment data via Platform token**
* > **Remote environment data via OAuth**

## Аутентификация с помощью платформенного токена

Получение данных из удалённых окружений с помощью платформенного токена предназначено для личного использования. Этот метод идеален, когда нужно быстро протестировать и оперативно получить данные из удалённых окружений перед тем, как делиться ими с другими.

Пример JavaScript-кода, описанный ниже, использует хранилище учётных данных для безопасного хранения токенов и платформенный токен для аутентификации, обеспечивая надёжный и безопасный способ получения данных из удалённого окружения Dynatrace.

### Предварительные требования

Перед созданием кода для плитки дашборда или секции ноутбука:

* Создайте платформенный токен Dynatrace в окружении, из которого вы хотите получать данные. Подробнее см. в разделе [Платформенные токены](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Создание персонализированных платформенных токенов для доступа к сервисам Dynatrace через API в контексте вашего пользователя.").
* Создайте запись в хранилище учётных данных Dynatrace в основном окружении для хранения платформенного токена, который затем будет использоваться в плитке кода или секции для аутентификации. Подробнее см. в разделе [Хранилище учётных данных](/docs/manage/credential-vault "Хранение и управление учётными данными в хранилище учётных данных.").
* Разрешите внешние запросы

  Внешние запросы обеспечивают исходящие сетевые подключения из вашего окружения Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с функциями приложений и функциями в Dashboards, Notebooks и Automations.

  1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Выберите  **New host pattern**.
  3. Добавьте доменные имена.
  4. Выберите **Add**.

  Таким образом вы можете детально контролировать веб-сервисы, к которым могут подключаться ваши функции.

  Например, вы можете добавить `myenv8132.apps.dynatrace.com`, чтобы разрешить только это окружение, или использовать подстановочный знак `*.apps.dynatrace.com`, чтобы разрешить все ваши окружения Dynatrace сразу.

Подробнее о добавлении в белый список см. [Разрешение IP-диапазонов для доступа к окружению](/docs/manage/account-management/settings/ip-allowlist "Разрешение IP-диапазонов для доступа к окружению с использованием нотации CIDR.")

### Код

Перед началом написания кода ознакомьтесь с тем, как используются функции.

1. `async function()`

   Это основная функция. Она вызывает `fetchFromDynatrace` (см. выше) с необходимыми параметрами.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   Для получения данных из Dynatrace эта функция:

   1. Извлекает учётные данные из записи хранилища учётных данных в основном тенанте на основе указанного credentialId.
   2. Выполняет вызов API на API вторичного/удалённого тенанта на основе учётных данных, а также параметров `url` и `query`, предоставленных основной функцией.

Теперь, когда вы выполнили [предварительные требования](#prerequisites) и ознакомились с функциями, вы готовы к написанию кода.

* Используйте приведённый ниже пример в качестве основы для своего кода.
* Прочитайте комментарии в примере кода для получения подробностей.
* Замените `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` на ваш собственный идентификатор учётных данных.
* Замените `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` на ваш собственный URL.
* Настройте запрос `"fetch logs | limit 1"` в соответствии с вашими потребностями.
* Выполните код в [плитке кода](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Добавление кода на дашборды Dynatrace.") (Dashboards) или [секции кода](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") (Notebooks).

  Если при выполнении кода возникнут ошибки, они будут перехвачены и залогированы с префиксами `[DynatraceAuthError]`, `[CredentialVaultError]` или `[ExecutionError]` для упрощения отладки.

Начните со сниппета

Вы можете начать со сниппета (**Remote environment data via Platform token**) при создании дашборда или ноутбука, использующего данные из удалённого окружения Dynatrace.

```
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";



/**



* Execute a query against a Dynatrace API with token retrieval inlined.



* @param {string} credentialId - The ID of the credential vault entry.



* @param {string} url - The API endpoint URL.



* @param {string} query - The query to execute.



* @returns {Promise<any>} - The API response data.



* @throws Will throw an error if any step fails.



*/



async function fetchFromDynatrace(credentialId, url, query) {



if (!credentialId || !url || !query) {



throw new Error("[ValidationError] Missing required parameters: credentialId, url, or query.");



}



try {



// Retrieve the platform token from the credential vault.



const { token } = await credentialVaultClient.getCredentialsDetails({



id: credentialId,



}).catch((error) => {



console.error(`[CredentialVaultError] Failed to retrieve token: ${error.message}`);



throw new Error("Unable to fetch platform token.");



});



if (!token) {



throw new Error("[CredentialVaultError] Token is undefined or empty.");



}



// Perform the API request.



const response = await fetch(url, {



method: "POST",



headers: {



"Content-Type": "application/json",



Accept: "application/json",



Authorization: `Bearer ${token}`,



},



body: JSON.stringify({



query,



requestTimeoutMilliseconds: 60000,



enablePreview: true,



}),



});



if (!response.ok) {



throw new Error(`[HTTPError] API call failed with status ${response.status}: ${response.statusText}`);



}



return await response.json();



} catch (error) {



console.error(`[FetchError] Query execution failed: ${error.message}`);



throw new Error("Unable to execute query.");



}



}



/**



* Main function to fetch and return results from Dynatrace.



* @returns {Promise<any>} - The query result.



*/



export default async function() {



const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Replace with your credential vault ID.



const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Replace with API URL.



const query = "fetch logs | limit 1"; // Replace with your query.



try {



const { result } = await fetchFromDynatrace(credentialId, url, query);



return result;



} catch (error) {



console.error(`[MainFunctionError] ${error.message}`);



return null; // Or handle as needed.



}



}
```

## Аутентификация через OAuth-клиент

Получение данных из удалённых окружений через OAuth предназначено для совместного использования. Этот метод обеспечивает согласованную видимость данных для всех пользователей.

Пример JavaScript-кода, описанный ниже, использует хранилище учётных данных для безопасного хранения токенов и OAuth для аутентификации, обеспечивая надёжный и безопасный способ получения данных из удалённого окружения Dynatrace.

### Предварительные требования

Перед созданием кода для плитки дашборда или секции ноутбука:

* Создайте OAuth-клиент. Подробнее см. в разделе [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").
* Создайте запись в хранилище учётных данных Dynatrace в основном окружении для хранения OAuth-токена, который затем будет использоваться в плитке кода или секции для аутентификации. Подробнее см. в разделе [Хранилище учётных данных](/docs/manage/credential-vault "Хранение и управление учётными данными в хранилище учётных данных.").
* Разрешите внешние запросы

  Внешние запросы обеспечивают исходящие сетевые подключения из вашего окружения Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с функциями приложений и функциями в Dashboards, Notebooks и Automations.

  1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Выберите  **New host pattern**.
  3. Добавьте доменные имена.
  4. Выберите **Add**.

  Таким образом вы можете детально контролировать веб-сервисы, к которым могут подключаться ваши функции.

  Например, вы можете добавить `myenv8132.apps.dynatrace.com`, чтобы разрешить только это окружение, или использовать подстановочный знак `*.apps.dynatrace.com`, чтобы разрешить все ваши окружения Dynatrace сразу.

Подробнее о добавлении в белый список см. [Разрешение IP-диапазонов для доступа к окружению](/docs/manage/account-management/settings/ip-allowlist "Разрешение IP-диапазонов для доступа к окружению с использованием нотации CIDR.")

### Код

Перед началом написания кода ознакомьтесь с тем, как используются функции.

1. `async function()`

   Это основная функция. Она вызывает `fetchFromDynatrace` (см. выше) с необходимыми параметрами.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   Для получения данных из Dynatrace эта функция:

   1. Извлекает учётные данные из записи хранилища учётных данных в основном тенанте на основе указанного credentialId.
   2. Получает токен доступа для вторичного тенанта через SSO, вызывая функцию authenticateToDynatrace.
   3. Выполняет вызов API на API вторичного/удалённого тенанта на основе ранее полученного значения `accessToken`, а также параметров `url` и `query`, предоставленных основной функцией.
3. `authenticateToDynatrace(clientId = '', clientSecret = '')`

   Для аутентификации через SSO эта функция:

   1. Принимает два параметра: `clientId` и `clientSecret`.
   2. Запрашивает токен доступа на основе начальных параметров функции и набора областей доступа, определённых внутри функции.
   3. В случае успеха возвращает полученный токен доступа от конечной точки SSO Dynatrace.

Теперь, когда вы выполнили [предварительные требования](#prerequisites) и ознакомились с функциями, вы готовы к написанию кода.

* Используйте приведённый ниже пример в качестве основы для своего кода.
* Прочитайте комментарии в примере кода для получения подробностей.
* Замените `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` на ваш собственный идентификатор учётных данных.
* Замените `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` на ваш собственный URL.
* Настройте запрос `"fetch logs | limit 1"` в соответствии с вашими потребностями.
* Выполните код в [плитке кода](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-code "Добавление кода на дашборды Dynatrace.") (Dashboards) или [секции кода](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#code "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") (Notebooks).

  Если при выполнении кода возникнут ошибки, они будут перехвачены и залогированы с префиксами `[DynatraceAuthError]`, `[CredentialVaultError]` или `[ExecutionError]` для упрощения отладки.

Начните со сниппета

Вы можете начать со сниппета (**Remote environment data via OAuth**) при создании дашборда или ноутбука, использующего данные из удалённого окружения Dynatrace.

```
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";



/**



* Authenticate to Dynatrace SSO using client credentials.



* @param {string} clientId - The client ID for authentication.



* @param {string} clientSecret - The client secret for authentication.



* @returns {Promise<string>} - The access token.



* @throws Will throw an error if authentication fails.



*/



async function authenticateToDynatrace(clientId, clientSecret) {



if (!clientId || !clientSecret) {



throw new Error("[ValidationError] Missing clientId or clientSecret for SSO authentication.");



}



const scopes = [



"environment-api",



"storage:buckets:read",



"storage:bizevents:read",



"storage:logs:read",



"storage:metrics:read",



"storage:entities:read",



].join(" ");



try {



const response = await fetch("https://sso.dynatrace.com/sso/oauth2/token", {



method: "POST",



headers: { "Content-Type": "application/x-www-form-urlencoded" },



body: `grant_type=client_credentials&client_id=${clientId}&client_secret=${clientSecret}&scopes=${scopes}`,



});



if (!response.ok) {



throw new Error(`[HTTPError] SSO authentication failed with status ${response.status}: ${response.statusText}`);



}



const { access_token: accessToken } = await response.json();



if (!accessToken) {



throw new Error("[SSOError] Access token not received.");



}



return accessToken;



} catch (error) {



console.error(`[DynatraceAuthError] ${error.message}`);



throw error;



}



}



/**



* Fetch data from Dynatrace using a query.



* @param {string} credentialId - The credential vault ID.



* @param {string} url - The API endpoint URL.



* @param {string} query - The query to execute.



* @returns {Promise<any>} - The API response data.



* @throws Will throw an error if any step fails.



*/



async function fetchFromDynatrace(credentialId, url, query) {



if (!credentialId || !url || !query) {



throw new Error("[ValidationError] Missing one or more required parameters: credentialId, url, or query.");



}



try {



// Retrieve credentials from the credential vault.



const { username: clientId, password: clientSecret } = await credentialVaultClient.getCredentialsDetails({



id: credentialId,



}).catch(error => {



console.error(`[CredentialVaultError] Failed to retrieve credentials: ${error.message}`);



throw new Error("Unable to fetch credentials from the vault.");



});



if (!clientId || !clientSecret) {



throw new Error("[CredentialVaultError] Missing clientId or clientSecret from the retrieved credentials.");



}



// Authenticate and get an access token.



const accessToken = await authenticateToDynatrace(clientId, clientSecret);



// Perform the API request.



const response = await fetch(url, {



method: "POST",



headers: {



"Content-Type": "application/json",



Accept: "application/json",



Authorization: `Bearer ${accessToken}`,



},



body: JSON.stringify({



query,



requestTimeoutMilliseconds: 60000,



enablePreview: true,



}),



});



if (!response.ok) {



throw new Error(`[HTTPError] API call failed with status ${response.status}: ${response.statusText}`);



}



return await response.json();



} catch (error) {



console.error(`[FetchError] ${error.message}`);



throw error;



}



}



/**



* Main function to execute a query and return results from Dynatrace.



* @returns {Promise<any>} - The query result.



*/



export default async function fetchDynatraceData() {



const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Replace with your credential vault ID.



const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Replace with API URL.



const query = "fetch logs | limit 1"; // Replace with your query.



try {



const { result } = await fetchFromDynatrace(credentialId, url, query);



return result;



} catch (error) {



console.error(`[MainFunctionError] ${error.message}`);



return null; // Return null or handle gracefully.



}



}
```
