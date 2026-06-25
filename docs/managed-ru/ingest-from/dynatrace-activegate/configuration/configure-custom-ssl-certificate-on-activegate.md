---
title: Пользовательский SSL-сертификат для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate
scraped: 2026-05-12T11:13:58.051235
---

# Пользовательский SSL-сертификат для ActiveGate

# Пользовательский SSL-сертификат для ActiveGate

* 6-min read
* Updated on Feb 24, 2026

Не применимо к Cluster ActiveGate

Следующая процедура прямой загрузки SSL-сертификата на ActiveGate **не применима** к Cluster ActiveGate.
Не пытайтесь настраивать SSL-сертификаты непосредственно на Cluster ActiveGate: сертификат будет перезаписан автоматическим управлением Dynatrace.
Для Cluster ActiveGate загружайте сертификаты через [Cluster Management Console](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Настройте пользовательский SSL-сертификат на Cluster ActiveGate.") или [Cluster REST API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Узнайте, как использовать Dynatrace API для хранения SSL-сертификата кластера.").

Подключение к ActiveGate от OneAgent или REST API происходит по зашифрованному HTTPS-каналу. ActiveGate предъявляет самоподписанный сертификат всем подключающимся клиентам. Хотя экземпляры OneAgent могут игнорировать действительность сертификатов ActiveGate (в зависимости от конфигурации), подключения из браузерных клиентов (например, [RUM JavaScript](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Настройте автоматическое внедрение RUM JavaScript на страницы ваших приложений")) проверяют, что имя хоста, указанное в сертификате, является корректным.

ActiveGate может использовать пользовательский сертификат вместо сертификата по умолчанию.

* В зависимости от корневого ЦС, подписавшего пользовательский сертификат ActiveGate, может потребоваться дополнительная конфигурация для OneAgent. Смотрите [Безопасность OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-security#trusted-root-certificates "Управление безопасностью OneAgent").
* Конфигурацию пользовательского сертификата также можно применить во время установки ActiveGate, указав параметры установки для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#custom-ssl-certificate "Узнайте о параметрах командной строки для ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#custom-ssl-certificate "Узнайте о параметрах для ActiveGate на Windows."). Для этого требуется файл в формате PKCS#12, содержащий закрытый ключ и соответствующую цепочку сертификатов.

## Настройка пользовательского SSL-сертификата

agctl

custom.properties

ActiveGate версии 1.333+

Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#ssl-certificate "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для настройки пользовательского SSL-сертификата.

#### Установка с минимальными параметрами:

```
agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem
```

#### Установка со всеми параметрами:

```
agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem --pem-password=secret --password=changeit --alias=mycert
```

#### Параметры:

* `--certificate`: путь к файлу сертификата в формате PEM (обязательный)
* `--key`: путь к файлу закрытого ключа в формате PEM (обязательный)
* `--pem-password`: пароль файла закрытого ключа (если зашифрован)
* `--password`: пароль для сгенерированного хранилища ключей (необязательный, генерируется автоматически)
* `--alias`: псевдоним сертификата в хранилище ключей (необязательный)

После настройки SSL-сертификата с помощью `agctl` необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").

Для настройки через `custom.properties` требуется файл в формате **PKCS#12**, содержащий закрытый ключ и цепочку сертификатов.

1. Скопируйте файл сертификата в [директорию ssl](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") и установите корректные права доступа.

   На Linux убедитесь, что права доступа к скопированному файлу сертификата включают пользователя ActiveGate (по умолчанию: `dtuserag`).

   На Windows убедитесь, что учётная запись `LocalService` имеет права доступа к файлу.

2. Добавьте следующие записи в файл `custom.properties` в [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux."):

   ```
   [com.compuware.apm.webserver]
   certificate-file = certificate-file.p12
   certificate-password = password
   certificate-alias = friendly-name
   ```

   Добавьте эти записи в раздел `[com.compuware.apm.webserver]`. Если раздел уже существует, просто добавьте свойства. Если раздела нет, создайте его заголовок.

   Пароль сертификата будет зашифрован после [перезапуска основной службы ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate."). Зашифрованный пароль хранится в `certificate-password-encr`, исходное свойство удаляется.

   **Значение `certificate-alias` должно быть указано в нижнем регистре.** Если у сертификата нет псевдонима, свойство `certificate-alias` можно опустить.

## Управление сертификатами через REST API

Сертификатами можно управлять удалённо через REST API. Подготовьте файл сертификата `PKCS#12` и загрузите его на ActiveGate с помощью REST.

API-токен для следующих операций должен иметь разрешение `ActiveGate certificate management`.

#### Загрузка и активация сертификата

```
curl https://{address of ActiveGate}:{port}/e/{environment ID}/api/v1/certificate/{certificate file name} -H"Authorization: Api-Token {token}" -H"X-Password: {password}" -H"Content-Type: application/octet-stream" -T {path to certificate file}
```

Пример:

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 \
-H "Authorization: Api-Token 123abc" \
-H "X-Password: myPassword" \
-H "Content-Type: application/octet-stream" \
-T cert.p12
```

#### Замена активного сертификата

Заменить активный сертификат через эту конечную точку невозможно (HTTP 403 Forbidden). Загрузите новый сертификат под другим именем, затем удалите старый.

#### Удаление сертификата

```
curl -XDELETE https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12 -H"Authorization: Api-Token 123abc"
```

#### Активация сертификата

```
curl -XPOST https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/activate -H"Authorization: Api-Token 123abc" -d"{\"password\":\"pass\"}"
```

#### Список всех сертификатов

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/list -H"Authorization: Api-Token 123abc"
```

#### Описание сертификата

```
curl https://myActiveGate:9999/e/myEnvironmentId/api/v1/certificate/cert.p12/list -H"Authorization: Api-Token 123abc" -H"X-Password: pass"
```

## Создание файла сертификата для тестирования

1. Сгенерируйте ключ и самоподписанный сертификат:

   ```
   openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -subj "/CN=localhost"
   ```

2. Конвертируйте в формат `PKCS#12`:

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12
   ```

   или с псевдонимом (в нижнем регистре):

   ```
   openssl pkcs12 -export -inkey key.pem -in cert.pem -out cert_key.p12 -name friendly-name
   ```

## Известные ограничения

* Пароль файла `PKCS#12` должен совпадать с паролем ключа в этом файле. Не используйте опцию `-twopass`.
* Использование нескольких файлов сертификатов невозможно: может быть только один файл сертификата ActiveGate, хотя файл может содержать несколько сертификатов и ключей.