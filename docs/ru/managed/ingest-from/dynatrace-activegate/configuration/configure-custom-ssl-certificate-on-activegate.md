---
title: Custom SSL certificate for ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate
scraped: 2026-03-06T21:27:26.606529
---

# Пользовательский SSL-сертификат для ActiveGate

# Пользовательский SSL-сертификат для ActiveGate

* Latest Dynatrace
* Время чтения: 6 мин.
* Опубликовано 11 апреля 2019

Не применимо к Cluster ActiveGate

Следующая процедура -- прямая загрузка SSL-сертификата на ActiveGate -- не применима к Cluster ActiveGate.
Не пытайтесь настраивать SSL-сертификаты напрямую на Cluster ActiveGate. В этом случае сертификат будет перезаписан автоматическим управлением, выполняемым Dynatrace.
Для Cluster ActiveGate необходимо загружать сертификаты через [Cluster Management Console](https://docs.dynatrace.com/managed/shortlink/managed-ssl-cluster-ag) или [Cluster REST API v1](https://docs.dynatrace.com/managed/shortlink/api-cluster-post-ssl-cert-store).

Подключение к ActiveGate от OneAgent или REST API осуществляется через зашифрованный канал HTTPS. ActiveGate предъявляет самоподписанный сертификат аутентификации всем подключающимся клиентам. В то время как экземпляры OneAgent могут игнорировать валидность сертификатов ActiveGate (в зависимости от конфигурации), соединения от браузерных клиентов (таких как [RUM JavaScript](../../../../observe/digital-experience/web-applications/initial-setup/rum-injection.md "Настройка автоматического внедрения RUM JavaScript на страницы ваших приложений")) проверяют правильность имени хоста, указанного в сертификате, перед отправкой данных.

**ActiveGate может обслуживать пользовательский сертификат вместо сертификата по умолчанию. Для этого вам нужен файл в формате `PKCS#12`, содержащий закрытый ключ и соответствующую цепочку сертификатов.**

В зависимости от корневого удостоверяющего центра, подписавшего пользовательский сертификат ActiveGate, может потребоваться дополнительная настройка OneAgent. См. [Безопасность OneAgent](../../../../ingest-from/dynatrace-oneagent/oneagent-security.md#trusted-root-certificates "Управление безопасностью OneAgent").

### Возможность настройки во время установки

Эту конфигурацию также можно применить во время установки ActiveGate, указав параметры установки для [Linux](../../../../ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate.md#custom-ssl-certificate "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.") или [Windows](../../../../ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate.md#custom-ssl-certificate "Узнайте о параметрах, которые можно использовать с ActiveGate на Windows.").

## Настройка пользовательского сертификата

Чтобы настроить ActiveGate для использования пользовательского сертификата

1. Скопируйте файл сертификата в [каталог ssl](../../../../ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files.md "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.") и установите правильные разрешения.

   В Linux убедитесь, что разрешения скопированного файла сертификата включают пользователя ActiveGate, которого вы назначили для запуска службы ActiveGate. Если вы не указали пользовательского пользователя при установке, пользователь по умолчанию -- `dtuserag`.

   В Windows убедитесь, что учетная запись `LocalService` имеет разрешения на доступ к скопированному файлу сертификата.
2. Добавьте следующие записи в файл `custom.properties` в [каталоге конфигурации ActiveGate](../../../../ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files.md "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.").

   ```
   [com.compuware.apm.webserver]



   certificate-file = certificate-file.p12



   certificate-password = password



   certificate-alias = friendly-name
   ```

   Вам необходимо добавить вышеуказанные записи в секцию `[com.compuware.apm.webserver]`. Если такая секция уже существует в вашем файле `custom.properties`, просто добавьте свойства в эту секцию. Если секция не существует, создайте также заголовок секции.

   Пароль сертификата, который вы указываете в свойстве `certificate-password`, будет обфусцирован после [перезапуска основной службы ActiveGate](../../../../ingest-from/dynatrace-activegate/operation/stop-restart-activegate.md "Узнайте, как запускать, останавливать и перезапускать ActiveGate на Windows или Linux."). Обфусцированный пароль сохраняется в свойстве `certificate-password-encr`, а исходное свойство удаляется.

   **Значение `certificate-alias` должно быть указано в нижнем регистре.** Если у сертификата нет дружественного имени, вы можете опустить свойство `certificate-alias`.

## Управление сертификатами через REST API

Сертификатами можно управлять удаленно через REST API. Подготовьте файл сертификата `PKCS#12`, и вы сможете загрузить его на ActiveGate с помощью REST.

Токен авторизации

Для авторизации требуется API-токен. API-токены могут предоставляться через HTTP-заголовки или другими способами. См. [Dynatrace API -- Токены и аутентификация](../../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.")

API-токен, используемый для следующих действий, должен иметь разрешение `ActiveGate certificate management`.

#### Загрузка и активация сертификата

Следующая конечная точка REST загружает и активирует выбранный файл сертификата. Пароль для файла должен совпадать с паролем для ключей, содержащихся в файле, и должен быть указан в пользовательском HTTP-заголовке `X-Password`.

`curl https://{address of ActiveGate}:{port}/e/{environment ID}/api/v1/certificate/{certificate file name} -H"Authorization: Api-Token {token}" -H"X-Password: {password}" -H"Content-Type: application/octet-stream" -T {path to certificate file}`

* Порт настраивается, по умолчанию -- 9999.
* Путь к файлу сертификата может быть просто именем локального файла или полным путем.
* Имя сертификата, указанное в URL, не обязательно должно совпадать с именем файла.

Например:

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 \



-H "Authorization: Api-Token 123abc" \



-H "X-Password: myPassword" \



-H "Content-Type: application/octet-stream" \



-T cert.p12
```

Если API-вызов успешен, HTTP-ответ будет `200` с JSON-описанием содержимого активированного файла сертификата.

Если API-вызов завершится неудачей, HTTP-ответ будет содержать код ошибки `4xx` или `5xx` с текстовым сообщением.

#### Замена активного сертификата

Вы не можете заменить активный сертификат с помощью этой конечной точки. Операция вернет `HTTP 403 Forbidden`. Чтобы заменить активный сертификат, загрузите новый сертификат под другим именем, а затем удалите старый сертификат.

#### Удаление сертификата

Удаляет выбранный сертификат на ActiveGate.

```
curl -XDELETE https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 -H"Authorization: Api-Token 123abc"
```

Если сертификат успешно удален, API-вызов вернет HTTP-код `200` без содержимого.

Если файл с указанным именем не существует, API-вызов вернет HTTP-код `404 Not found`.

Если файл сертификата используется в данный момент, API-вызов вернет HTTP-код `403 Forbidden`.

#### Активация сертификата

Активирует существующий ранее загруженный файл сертификата с использованием указанного пароля.

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/activate -H"Authorization: Api-Token 123abc" -d"{\"password\":\"pass\"}"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/activate -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

Если сертификат успешно активирован, API-вызов вернет HTTP-код `200` с JSON-описанием содержимого активированного файла сертификата.

Если запрошенный файл сертификата не существует на ActiveGate, API-вызов вернет HTTP-код `404`.

Если предоставленный пароль не совпадает, API-вызов вернет HTTP-код `400`.

#### Список всех сертификатов

Возвращает JSON-список всех загруженных файлов.

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/list -H"Authorization: Api-Token 123abc"
```

Если активное хранилище ключей присутствует в списке, его запись будет содержать дополнительные детали.

Пример ответа:

```
[



{



"name":"cert_demo.p12"



},



{      "name":"cert.p12",



"desc":[         {



"alias":"local",



"description":"Subject:CN=myActiveGate;Valid from:Fri Feb 15 13:16:58 CET 2019;Valid to:Sat Feb 15 13:16:58 CET 2020;Serial number:71d275dd3983c3cb9382437275dd3983c3cb93dbca"



},



{



"alias":"dynatrace",



"description":"Subject:CN=*.clients.dynatrace.org;Valid from:Thu Feb 21 10:06:03 CET 2019;Valid to:Fri Feb 21 10:06:03 CET 2020;Serial number:6dc7008ab269ecebeed03652ce08ab269ecebeeeb33"



}



]



},



{



"name":"cert_key_1.p12"



}



]
```

Обратите внимание, что самоподписанный сертификат по умолчанию не включается в список.

#### Описание сертификата

Этот API-вызов возвращает JSON-описание выбранного файла.

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -d"{\"password\":\"pass\"}"
```

Если запрошенный файл сертификата не существует на ActiveGate, API-вызов вернет HTTP-код `404`.

Если пароль не совпадает, API-вызов вернет HTTP-код `400`.

Пример ответа:

```
{   "name":"cert.p12",



"desc":[      {



"alias":"local",



"description":"Subject:CN=myActiveGate;Valid from:Fri Feb 15 13:16:58 CET 2019;Valid to:Sat Feb 15 13:16:58 CET 2020;Serial number:7137275dd398c4182437275dd3983c3cb93dbca"



},



{



"alias":"dynatrace",



"description":"Subject:CN=*.clients.dynatrace.org;Valid from:Thu Feb 21 10:06:03 CET 2019;Valid to:Fri Feb 21 10:06:03 CET 2020;Serial number:6d2ce08ab269ecebeee7f1bd03652ce08ab269ecebeeeb33"



}



]



}
```

## Создание файла сертификата для тестирования

Чтобы создать самоподписанный файл сертификата `PKCS#12` для тестирования

1. Сгенерируйте ключ и самоподписанный сертификат:

   ```
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj "/CN=localhost"
   ```
2. Конвертируйте сгенерированные файлы в формат `PKCS#12`:

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12
   ```

   или, чтобы задать дружественное имя, используйте:

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12 -name friendly-name
   ```

   помните, что `friendly-name` должно быть указано в нижнем регистре.

## Известные ограничения и поддержка нескольких сертификатов

* Пароль для файла `PKCS#12` должен совпадать с паролем для ключа, содержащегося в этом файле.
  Не используйте опцию `-twopass` в команде `openssl pkcs12`.
* Использовать несколько файлов сертификатов невозможно: может быть только один файл сертификата ActiveGate, хотя этот файл может содержать несколько сертификатов и ключей.