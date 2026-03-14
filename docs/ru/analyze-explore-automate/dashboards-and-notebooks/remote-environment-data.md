---
title: Данные удаленной среды
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/remote-environment-data
scraped: 2026-03-03T21:23:07.840378
---

# Данные удаленной среды


* Последнее Dynatrace
* Руководство по началу работы
* 9-минутное чтение
* Обновлено 02 декабря 2024 г.

Используя [кодовые плитки](dashboards-new/components/dashboard-component-code.md "Добавьте код в свои Dynatrace-панели.") (в Панелях) и [кодовые разделы](notebooks.md#code "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве."), вы можете консолидировать данные из нескольких Dynatrace-сред.

Существуют два механизма аутентификации для получения данных из удаленных сред:

* **Аутентификация с помощью токена платформы**: Предназначена для личного использования. Используйте, когда вам нужно быстрое тестирование и быстрое получение данных из удаленных сред.
* **Аутентификация клиента OAuth**: Предназначена для обмена. Используйте, чтобы обеспечить последовательную видимость данных для всех пользователей.

Новое! Начните с фрагмента в Панелях или Тетрадях

Панели версии 1.310+ Тетради версии 1.310+

Теперь вы можете начать с фрагмента при создании панели или тетради, которая использует данные из удаленной Dynatrace-среды.

* > **Получить внешние данные**
* > **Данные удаленной среды через токен платформы**
* > **Данные удаленной среды через OAuth**

## Аутентификация с помощью токена платформы

Получение данных из удаленных сред через токен платформы предназначено для личного использования. Этот метод идеален, когда вам нужно быстро протестировать и быстро получить данные из удаленных сред, прежде чем поделиться ими с другими.

Пример кода на JavaScript, описанный ниже, использует хранилище учетных данных для безопасного хранения токена и токен платформы для аутентификации, чтобы предложить надежный и безопасный способ получения данных из удаленной Dynatrace-среды.

### Предварительные условия

Прежде чем создать код для своей плитки панели или раздела тетради:

* Создайте токен платформы Dynatrace в среде, из которой вы хотите получить данные. Подробности см. в разделе [Токены платформы](../../manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens.md "Создайте персонализированные токены платформы для доступа к службам Dynatrace через API в вашем пользовательском контексте.").
* Создайте запись хранилища учетных данных Dynatrace в основной среде для хранения токена платформы, который позже будет использоваться в кодовой плитке или разделе для аутентификации. Подробности см. в разделе [Хранилище учетных данных](../../../common/manage/credential-vault.md "Храните и управляйте учетными данными в хранилище учетных данных.").
* Разрешите внешние запросы

  Внешние запросы включают исходящие сетевые подключения из вашей Dynatrace-среды к внешним службам. Они позволяют вам контролировать доступ к публичным конечным точкам из AppEngine с помощью функций приложений и функций в Панелях, Тетрадях и Автоматизациях.

  1. Перейдите в ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Общие** > **Внешние запросы**.
  2. Выберите  **Новый шаблон хоста**.
  3. Добавьте имена доменов.
  4. Выберите **Добавить**.

  Таким образом, вы можете детально контролировать веб-сервисы, к которым могут подключаться ваши функции.

  Например, вы можете добавить `myenv8132.apps.dynatrace.com`, чтобы разрешить только эту среду, или использовать подстановочный знак, такой как `*.apps.dynatrace.com`, чтобы разрешить все свои Dynatrace-среды одновременно.

Более подробную информацию о разрешении IP-диапазонов см. в разделе [Разрешить IP-диапазоны, которые могут получить доступ к вашей среде](../../manage/account-management/settings/ip-allowlist.md "Разрешить IP-диапазоны, которые могут получить доступ к вашей среде, используя запись CIDR.").

### Код

Прежде чем начать программировать, ознакомьтесь с тем, как используются функции.

1. `async function()`

   Это основная функция. Она вызывает `fetchFromDynatrace` (см. выше) с необходимыми параметрами.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   Чтобы получить данные из Dynatrace, эта функция:

   1. Извлекает учетные данные из записи хранилища учетных данных основной среды на основе заданного идентификатора учетных данных.
   2. Выполняет вызов API в API удаленной среды на основе учетных данных, а также параметров `url` и `query`, предоставленных основной функцией.

Теперь, когда вы выполнили [предварительные условия](#предварительные-условия) и ознакомились с функциями, вы готовы программировать.

* Основывайте свой код на примере ниже.
* Читайте комментарии в примере кода, чтобы получить подробную информацию о коде.
* Замените `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` своим собственным идентификатором хранилища учетных данных.
* Замените `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` своим собственным URL-адресом.
* Настройте запрос `"fetch logs | limit 1"` в соответствии с вашими потребностями.
* Запустите свой код в [кодовой плитке](dashboards-new/components/dashboard-component-code.md "Добавьте код в свои Dynatrace-панели.") (Панели) или [кодовом разделе](notebooks.md#code "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.") (Тетради).

  Если вы столкнетесь с ошибками при запуске кода, они будут перехвачены и записаны с префиксами `[DynatraceAuthError]`, `[CredentialVaultError]` или `[ExecutionError]` для более легкой отладки.

Начните с фрагмента

Вы можете начать с фрагмента (**Данные удаленной среды через токен платформы**) при создании панели или тетради, которая использует данные из удаленной Dynatrace-среды.

```
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";


/**


* Выполните запрос против Dynatrace API с получением токена.


* @param {string} credentialId - Идентификатор записи хранилища учетных данных.


* @param {string} url - URL-адрес конечной точки API.


* @param {string} query - Запрос на выполнение.


* @returns {Promise<any>} - Данные ответа API.


* @throws Будет выброшена ошибка, если любой шаг не удался.


*/


async function fetchFromDynatrace(credentialId, url, query) {


if (!credentialId || !url || !query) {


throw new Error("[ValidationError] Отсутствуют обязательные параметры: credentialId, url или query.");


}


try 


// Извлеките токен платформы из хранилища учетных данных.


const { token } = await credentialVaultClient.getCredentialsDetails({


id: credentialId,


}).catch((error) => 


console.error(`[CredentialVaultError] Не удалось получить токен: ${error.message}`);


throw new Error("Не удалось получить токен платформы.");


 });


if (!token) 


throw new Error("[CredentialVaultError] Токен не определен или пуст.");


// Выполните запрос API.


const response = await fetch(url, 


{


method: "POST",


headers: 


{


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


if (!response.ok) 


throw new Error(`[HTTPError] API-вызов не удался со статусом ${response.status}: ${response.statusText}`);


return await response.json();


} catch (error) 


console.error(`[FetchError] Выполнение запроса не удалось: ${error.message}`);


throw new Error("Не удалось выполнить запрос.");


}


/**


* Основная функция для получения и возврата результатов из Dynatrace.


* @returns {Promise<any>} - Результат запроса.


*/


export default async function() 


const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Замените на свой идентификатор хранилища учетных данных.


const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Замените на URL-адрес API.


const query = "fetch logs | limit 1"; // Замените на свой запрос.


try 


const { result } = await fetchFromDynatrace(credentialId, url, query);


return result;


} catch (error) 


console.error(`[MainFunctionError] ${error.message}`);


return null; // Или обработайте как необходимо.


}


## Аутентификация клиента OAuth

Получение данных из удаленных сред через OAuth предназначено для обмена. Этот метод обеспечивает последовательную видимость данных для всех пользователей.

Пример кода на JavaScript, описанный ниже, использует хранилище учетных данных для безопасного хранения токена и OAuth для аутентификации, чтобы предложить надежный и безопасный способ получения данных из удаленной Dynatrace-среды.

### Предварительные условия

Прежде чем создать код для своей плитки панели или раздела тетради:

* Создайте клиент OAuth. Подробности см. в разделе [Клиенты OAuth](../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Управляйте аутентификацией и разрешениями пользователей с помощью клиентов OAuth.").
* Создайте запись хранилища учетных данных Dynatrace в основной среде для хранения токена OAuth, который позже будет использоваться в кодовой плитке или разделе для аутентификации. Подробности см. в разделе [Хранилище учетных данных](../../../common/manage/credential-vault.md "Храните и управляйте учетными данными в хранилище учетных данных.").
* Разрешите внешние запросы

  Внешние запросы включают исходящие сетевые подключения из вашей Dynatrace-среды к внешним службам. Они позволяют вам контролировать доступ к публичным конечным точкам из AppEngine с помощью функций приложений и функций в Панелях, Тетрадях и Автоматизациях.

  1. Перейдите в ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Общие** > **Внешние запросы**.
  2. Выберите  **Новый шаблон хоста**.
  3. Добавьте имена доменов.
  4. Выберите **Добавить**.

  Таким образом, вы можете детально контролировать веб-сервисы, к которым могут подключаться ваши функции.

  Например, вы можете добавить `myenv8132.apps.dynatrace.com`, чтобы разрешить только эту среду, или использовать подстановочный знак, такой как `*.apps.dynatrace.com`, чтобы разрешить все свои Dynatrace-среды одновременно.

Более подробную информацию о разрешении IP-диапазонов см. в разделе [Разрешить IP-диапазоны, которые могут получить доступ к вашей среде](../../manage/account-management/settings/ip-allowlist.md "Разрешить IP-диапазоны, которые могут получить доступ к вашей среде, используя запись CIDR.").

### Код

Прежде чем начать кодирование, просмотрите, как используются функции.

1. `async function()`

   Это основная функция. Она вызывает `fetchFromDynatrace` (см. выше) с необходимыми параметрами.
2. `fetchFromDynatrace(credentialId = "", url = "", query = "")`

   Чтобы получить данные из Dynatrace, эта функция:

   1. Извлекает учетные данные из записи хранилища учетных данных на основном клиенте на основе заданного `credentialId`.
   2. Получает токен доступа для вторичного клиента через SSO, вызывая функцию `authenticateToDynatrace`.
   3. Выполняет вызов API на API вторичного/удаленного клиента на основе ранее полученного значения `accessToken`, а также параметров `url` и `query`, предоставленных основной функцией.
3. `authenticateToDynatrace(clientId = '', clientSecret = '')`

   Чтобы аутентифицироваться против SSO, эта функция:

   1. Принимает два параметра: `clientId` и `clientSecret`.
   2. Запрашивает токен доступа на основе начальных параметров функции и набора областей, определенных внутри функции.
   3. При успехе возвращает полученный токен доступа из конечной точки SSO Dynatrace.

Теперь, когда вы выполнили [предварительные условия](#prerequisites) и просмотрели функции, вы готовы приступить к кодированию.

* Основывайте свой код на примере ниже.
* Читайте комментарии в примере кода для получения подробной информации о коде.
* Замените `CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX` своим собственным идентификатором учетных данных.
* Замените `https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute?enrich:metric-metadata` своим собственным URL-адресом.
* Настройте запрос `"fetch logs | limit 1"` в соответствии с вашими потребностями.
* Запустите свой код в [блоке кода](dashboards-new/components/dashboard-component-code.md "Добавьте код в свои панели управления Dynatrace.") (Панели управления) или [разделе кода](notebooks.md#code "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.") (Тетради).

  Если вы столкнетесь с ошибками при запуске своего кода, они будут пойманы и записаны с префиксами `[DynatraceAuthError]`, `[CredentialVaultError]` или `[ExecutionError]` для более простой отладки.

Начните с фрагмента

Вы можете начать с фрагмента (**Данные удаленной среды через OAuth**) при создании панели управления или тетради, которая использует данные из удаленной среды Dynatrace.

```javascript
import { credentialVaultClient } from "@dynatrace-sdk/client-classic-environment-v2";


/**


* Аутентифицируйтесь в Dynatrace SSO, используя учетные данные клиента.


* @param {string} clientId - Идентификатор клиента для аутентификации.


* @param {string} clientSecret - Секрет клиента для аутентификации.


* @returns {Promise<string>} - Токен доступа.


* @throws Будет бросать ошибку, если аутентификация не удалась.


*/


async function authenticateToDynatrace(clientId, clientSecret) {


if (!clientId || !clientSecret) {


throw new Error("[ValidationError] Отсутствует clientId или clientSecret для аутентификации SSO.");


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


throw new Error(`[HTTPError] Аутентификация SSO не удалась со статусом ${response.status}: ${response.statusText}`);


}


const { access_token: accessToken } = await response.json();


if (!accessToken) {


throw new Error("[SSOError] Токен доступа не получен.");


}


return accessToken;


} catch (error) {


console.error(`[DynatraceAuthError] ${error.message}`);


throw error;


}


)


/**


* Получите данные из Dynatrace, используя запрос.


* @param {string} credentialId - Идентификатор учетных данных.


* @param {string} url - URL-адрес конечной точки API.


* @param {string} query - Запрос на выполнение.


* @returns {Promise<any>} - Данные ответа API.


* @throws Будет бросать ошибку, если любой шаг не удался.


*/


async function fetchFromDynatrace(credentialId, url, query) {


if (!credentialId || !url || !query) {


throw new Error("[ValidationError] Отсутствует один или несколько обязательных параметров: credentialId, url или query.");


}


try 


// Извлеките учетные данные из хранилища учетных данных.


const { username: clientId, password: clientSecret } = await credentialVaultClient.getCredentialsDetails({


id: credentialId,


}).catch(error => 


console.error(`[CredentialVaultError] Не удалось получить учетные данные: ${error.message}`);


throw new Error("Невозможно получить учетные данные из хранилища.");


)


if (!clientId || !clientSecret) 


throw new Error("[CredentialVaultError] Отсутствует clientId или clientSecret из полученных учетных данных.");


)


// Аутентифицируйтесь и получите токен доступа.


const accessToken = await authenticateToDynatrace(clientId, clientSecret);


// Выполните запрос API.


const response = await fetch(url, 


method: "POST",


headers: 


"Content-Type": "application/json",


Accept: "application/json",


Authorization: `Bearer ${accessToken}`,


},


body: JSON.stringify({


query,


requestTimeoutMilliseconds: 60000,


enablePreview: true,


}),


)


if (!response.ok) 


throw new Error(`[HTTPError] Вызов API не удался со статусом ${response.status}: ${response.statusText}`)


)


return await response.json()


} catch (error) 


console.error(`[FetchError] ${error.message}`)


throw error


)


)


/**


* Основная функция для выполнения запроса и возврата результатов из Dynatrace.


* @returns {Promise<any>} - Результат запроса.


*/


export default async function fetchDynatraceData() 


const credentialId = "CREDENTIALS_VAULT-XXXXXXXXXXXXXXXX"; // Замените на свой идентификатор учетных данных.


const url = "https://remote-environment-id.apps.dynatrace.com/platform/storage/query/v1/query:execute"; // Замените на URL-адрес API.


const query = "fetch logs | limit 1"; // Замените на свой запрос.


try 


const { result } = await fetchFromDynatrace(credentialId, url, query)


return result


} catch (error) 


console.error(`[MainFunctionError] ${error.message}`)


return null // Верните null или обработайте благополучно.


)


```