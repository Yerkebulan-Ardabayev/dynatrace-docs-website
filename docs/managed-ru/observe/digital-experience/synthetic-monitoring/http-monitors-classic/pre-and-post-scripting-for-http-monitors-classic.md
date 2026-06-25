---
title: Скрипты предвыполнения и пост-выполнения для HTTP-мониторов
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic
scraped: 2026-05-12T11:32:20.664471
---

# Скрипты предвыполнения и пост-выполнения для HTTP-мониторов

# Скрипты предвыполнения и пост-выполнения для HTTP-мониторов

* Explanation
* 9-min read
* Updated on Apr 13, 2022

При выполнении сложного API-монитора скрипты предвыполнения и пост-выполнения позволяют добавлять логику до/после запросов HTTP-монитора (например, для пропуска запроса при определённых условиях, добавления заголовка, изменения содержимого тела или URL). Скрипты основаны на пользовательском JavaScript-коде, выполняемом до и/или после каждого HTTP-запроса. Также можно задавать значения в скриптах и передавать их как переменные между запросами.

## Определение скриптов предвыполнения и пост-выполнения

В режиме редактирования включите выполнение скрипта до или после запроса для отображения редактора кода. По мере ввода редактор отображает встроенную подсказку с краткими описаниями доступных методов после ввода объектов `api`, `request` (для скриптов предвыполнения) или `response` (для скриптов пост-выполнения).

Скрипты также можно добавлять в [режиме скрипта](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Создавайте и редактируйте HTTP-мониторы в формате JSON."): просто добавьте скрипт как значение ключей `preProcessingScript` или `postProcessingScript`. Однако при таком подходе встроенный помощник методов будет недоступен, и потребуется экранировать все специальные символы и обозначать переносы строк обратным слешем (например, `\n` для новой строки, `\"` для двойной кавычки, `\t` для табуляции).

Объект `api` можно использовать в скриптах предвыполнения или пост-выполнения для хранения и получения переменных, выполнения криптографических функций, журналирования данных, пропуска запросов и многого другого. Скрипты предвыполнения используют объект `request` для добавления или изменения параметров текущего HTTP-запроса (например, URL, значений заголовков и тела запроса). Скрипты пост-выполнения используют объект `response` для доступа к телу ответа, заголовкам и коду статуса текущего HTTP-запроса после получения ответа.

Скрипты предвыполнения и пост-выполнения имеют прямой доступ только к данным, полученным в результате текущего запроса. Иными словами, детали ответа доступны только в скрипте пост-выполнения того же запроса. Для передачи информации другому запросу в рамках того же монитора используйте [переменную](#variables).

## Передача переменных

Переменные могут передаваться только в контексте одного выполнения HTTP-монитора. Также необходимо убедиться, что при обращении к переменной данные за ней логически доступны монитору. Например, если переменная задана на основе данных из тела ответа запроса, её нельзя получить в скрипте предвыполнения этого же запроса, поскольку в этот момент содержимое ещё не существует.

После установки глобальной переменной с помощью метода `api.setValue()` вы можете применить её значение по соглашению `{variable_name}` с помощью `api.getValue()` или `api.getValues()` в последующих скриптах предвыполнения или пост-выполнения. [Пример ниже](#variables-example) демонстрирует установку переменной и её получение с помощью `api.setValue()` и `api.getValue()`.

Значение переменной, ранее установленной с помощью `api.setValue()`, также можно применять в последующих полях конфигурации HTTP-монитора по соглашению `{variable_name}`. Интерфейс информирует вас, когда это возможно.

Имена переменных и ключей ограничены 100 символами. Значения глобальных переменных ограничены 5000 символами.

![Passing variables](https://dt-cdn.net/images/httpmonitorsvariables-973-778f630782.png)

Passing variables

### Пример монитора

В данном примере выполняется авторизация OAuth 2.0 с использованием скриптов предвыполнения и пост-выполнения для получения и применения токена доступа.

HTTP-монитор состоит из двух запросов. Первый запрос получает токен доступа, а скрипт пост-выполнения сохраняет его в переменную `bearerToken`. Затем выполняется второй запрос, где скрипт предвыполнения добавляет значение переменной `bearerToken` в заголовок авторизации запроса.

#### Запрос 1

**URL запроса**: `https://somesite.com/sso/oauth2/access_token?realm=/somename`
**HTTP-метод**: POST
**Скрипт пост-выполнения**:

```
if (response.getStatusCode() != 200) {



api.fail("HTTP error: " + response.getStatusCode());



}



var responseBody = response.getResponseBody();



var jsonData = JSON.parse(responseBody);



api.setValue("bearerToken", jsonData.access_token);



api.info(jsonData.access_token);
```

#### Запрос 2

**URL запроса**: `https://account.somesite.com/rest/user/user%40somesite%2Ecom?`
**HTTP-метод**: GET
**Скрипт предвыполнения**:

```
request.addHeader("Authorization", "Bearer " + api.getValue("bearerToken"));
```

#### Полный скрипт монитора

```
{



"version": "1.0",



"requests": [



{



"description": "GET access_token",



"url": "https://somesite.com/sso/oauth2/access_token?realm=/somename",



"method": "POST",



"requestBody": "scope=openid%20read&client_secret=somesecret&grant_type=password&username=user%40somesite%2Ecom&password=password123&client_id=clientid",



"configuration": {



"requestHeaders": [



{



"name": "Content-Type",



"value": "application/x-www-form-urlencoded"



}



],



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "",



"postProcessingScript": "if (response.getStatusCode() != 200) {\n    api.fail(\"HTTP error: \" + response.getStatusCode());\n}\nvar responseBody = response.getResponseBody();\nvar jsonData = JSON.parse(responseBody);\napi.setValue(\"bearerToken\", jsonData.access_token);\napi.info(jsonData.access_token);"



},



{



"description": "GET tenants",



"url": "https://account.somesite.com/rest/user/user%40somesite%2Ecom?",



"method": "GET",



"requestBody": "",



"configuration": {



"acceptAnyCertificate": true,



"followRedirects": true



},



"preProcessingScript": "request.addHeader(\"Authorization\", \"Bearer \" + api.getValue(\"bearerToken\"));",



"postProcessingScript": ""



}



]



}
```

## Справочник по методам

При написании скриптов предвыполнения и пост-выполнения в JavaScript-коде доступны следующие методы. Редактор скриптов имеет встроенный синтаксический помощник с подсказками и проверкой синтаксиса.

### Хранение и получение значений между HTTP-запросами

* `api.setValue(key, value)` — устанавливает `value` для `key`. Для каждой пары ключ-значение используйте отдельный экземпляр `api.setValue()`.
* `api.getValue(key)` — получает значение `key`, ранее установленного с помощью `api.setValue()`.
* `api.getValues()` — возвращает объект, содержащий пары ключ-значение, ранее установленные с помощью `api.setValue()`.

Имена переменных и ключей ограничены 100 символами. Значения глобальных переменных ограничены 5000 символами.

### Пометка запросов как неудачных или завершённых

* `api.fail(message)` — помечает запрос как неудачный, предоставляя `message` в качестве причины, и помечает выполнение монитора как неудачное. Параметр `message` ограничен 1000 символами. Сообщение `message` отображается как **Failure message** в карточке **Events** на [странице деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов."). Пользовательские журнальные сообщения также отображаются в атрибуте `customLogs` в [деталях выполнения HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Узнайте о странице Synthetic details для HTTP-мониторов.").
* `api.finish()` — завершает запрос, после чего выполняется следующий.

### Пропуск HTTP-запросов

Эти методы пропускают HTTP-запросы после завершения текущего запроса.

* `api.skipNextRequest()` — пропускает выполнение следующего запроса.
* `api.skipNextRequests(n)` — пропускает выполнение следующих `n` последовательных запросов.
* `api.skipRequest(requestIndex)` — пропускает выполнение запроса с индексом `requestIndex`. Нумерация индексов запросов начинается с `1` и соответствует номерам запросов в интерфейсе.
* `api.skipRequests(requestIndexes)` — пропускает выполнение нескольких запросов; массив `Int32Array` из `requestIndexes` задаёт пропускаемые запросы, например `api.skipRequests(new Int32Array([2,4]))`. Также можно сначала определить массив и затем ссылаться на него, например `api.skipRequests(x)`, где `x=new Int32Array([2,4])` уже определён.

### Базовое журналирование

* `api.info(message)` — записывает `message` в журнал с уровнем `info`.
* `api.warn(message)` — записывает `message` в журнал с уровнем `warning`.
* `api.error(message)` — записывает `message` в журнал с уровнем `error`.

Параметр `message` ограничен 1000 символами. Сообщения записываются в файл `vuc-http-custom.log` в [директории журналов ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate в Windows и Linux."), доступной для [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга."). Пользовательские журнальные сообщения также отображаются в атрибуте `customLogs` в [деталях выполнения HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Узнайте о странице Synthetic details для HTTP-мониторов.").

### Базовое кодирование

* `api.urlEncode(url)` — преобразует строку `url` в формат MIME `application/x-www-form-urlencoded`.
* `api.base64UrlEncode(urlToEncode)` — кодирует входные данные (`urlToEncode`) с использованием Base64URL.
* `api.base64UrlDecode(encodedUrl)` — декодирует входные данные Base64URL (`encodedUrl`).

* `api.HMACSHA256(message, secret)` — создаёт хеш Base64 с использованием HMAC-SHA256, где `message` — кодируемый текст, `secret` — секретный ключ.
* `api.btoa(value)` — создаёт строку ASCII в кодировке Base64 из строки (`value`) двоичных данных.
* `api.atob(value)` — декодирует строку ASCII в кодировке Base64 (`value`) в двоичную строку. Входная строка должна быть представлением Base64 допустимой строки UTF-8. Для более универсального декодирования Base64 используйте функцию `api.base64decode()`. Параметр `value` ограничен 10 000 символами.

### Генерация случайных значений

* `api.randomNextInt()` — возвращает псевдослучайное, равномерно распределённое значение `int`.
* `api.randomNextIntWithBound(value)` — возвращает псевдослучайное, равномерно распределённое значение `int` в диапазоне от 0 (включительно) до указанного `value` (исключительно).
* `api.randomNextFloat()` — возвращает псевдослучайное, равномерно распределённое значение float.
* `api.randomNextLong()` — возвращает псевдослучайное, равномерно распределённое значение long.
* `api.randomString(numberOfChars, supportedChars)` — создаёт случайную строку длиной `numberOfChars` символов; символы выбираются из множества, заданного строкой `supportedChars`. Оба параметра ограничены 5000 символами.

### Форматирование даты

* `api.dateToFormat(timestamp, format)` — возвращает входную метку времени `timestamp` в указанном формате `format` на основе класса [Java SimpleDateFormat](https://docs.oracle.com/javase/8/docs/api/java/text/SimpleDateFormat.html). `timestamp` должен быть в формате UNIX Epoch.
* `api.date()` — возвращает текущую дату в виде «сырого» значения в миллисекундах в формате UNIX Epoch.

Пример:

```
api.setValue("dateToFormat", api.dateToFormat("1346524199000", "dd/MM/yy"));



api.setValue("dateToFormatCurrentDate", api.dateToFormat(api.date(), "dd/MM/yy"));
```

### Получение данных

* `api.UUID()` — возвращает универсальный уникальный идентификатор.

* `api.getContext().location.name` — возвращает имя частного или публичного расположения, из которого выполняется монитор. Полезно для применения условной логики в зависимости от расположения (например, для использования разных данных входа в разных расположениях) или для записи в журналы, как показано в примере ниже.

  Пример:

  ```
  var loc = api.getContext().location.name;



  api.info("Location Name is: " + loc);
  ```
* `api.getCredential(id, type)` — получает значение учётных данных по их идентификатору (`id`) и типу (`type`), который может быть `username`, `password` или `token`. Необходимо указать точное значение одного из вариантов автодополнения для идентификатора учётных данных; использование динамических идентификаторов (например, переменных) не поддерживается. Список включает только [доступные вам учётные данные](/managed/manage/credential-vault#owner-shared-public "Храните учётные данные и управляйте ими в хранилище credential vault.").

  Требуется ActiveGate версии 1.212+ для [частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

  В качестве лучшей практики безопасности рекомендуется использовать только специальные тестовые учётные данные для синтетических мониторов.

  Пример:

  ```
  var userName = api.getCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", "username");



  api.setValue("un", userName + "1");
  ```

### Запись данных

* `api.saveCredential(id, username, password)` — перезаписывает учётные данные типа «имя пользователя/пароль» по идентификатору `id`, новому значению имени пользователя (`username`) и новому значению пароля (`password`). Параметры `username` и `password` могут быть строками или переменными.

  Пример со строками имени пользователя и пароля:

  ```
  api.saveCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", "newusername", "newpassword");
  ```

  Пример с переменными, содержащими значения имени пользователя и пароля:

  ```
  api.saveCredential("CREDENTIALS_VAULT-000000A0A00A0AA0", myusernamevariable, mypasswordvariable);
  ```
* `api.saveToken(id, token)` — перезаписывает токен-учётные данные по идентификатору `id` и новому значению токена (`token`). Параметр `token` может быть строкой или переменной.

### Методы скриптов предвыполнения

Эти методы специфичны для запроса, поэтому их можно использовать только в скриптах предвыполнения.

* `request.addHeader(key, value)` — добавляет заголовок запроса, где `key` — имя заголовка, `value` — значение заголовка.
* `request.setUrl(URL)` — задаёт `URL` запроса.
* `request.setBody(requestBody)` — задаёт тело запроса (`requestBody`).

### Методы скриптов пост-выполнения

Эти методы специфичны для ответа, поэтому их можно использовать только в скриптах пост-выполнения.

* `response.getResponseBody()` — возвращает первые 50 КБ тела ответа в виде строки. Для разбора JSON-ответа в объект используйте, например:

  ```
  var responseBody = response.getResponseBody();



  var jsonData = JSON.parse(responseBody);
  ```
* `response.getHeaders()` — возвращает объект, содержащий все HTTP-заголовки ответа.

  Используйте `response.getHeaders().get(<header-name>)` для получения значения конкретного заголовка ответа в виде строки.
* `response.getStatusCode()` — возвращает код статуса ответа в виде числа.