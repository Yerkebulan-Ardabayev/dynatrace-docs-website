---
title: Подписание расширений вручную с помощью OpenSSL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl
scraped: 2026-05-12T12:11:37.267488
---

# Подписание расширений вручную с помощью OpenSSL

# Подписание расширений вручную с помощью OpenSSL

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 21 апреля 2021 г.

## Использование OpenSSL

Для подписания расширения вручную используйте OpenSSL. Для Windows необходимо загрузить и установить [бинарный файл OpenSSL](https://wiki.openssl.org/index.php/Binaries) по выбору. Процедура проверена с OpenSSL 1.1.1k.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание корневого ключа и сертификата**](#create-root-key-and-cert)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Добавление корневого сертификата в хранилище учётных данных Dynatrace**](#add-root-cert)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Создание разработческого сертификата**](#create-dev-cert)[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

**Подписание расширения**](#sign-extension)[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Проверка подписи**](#verify-signature)[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

**Создание пакета расширения**](#create-extension-package)

### Создание корневого ключа и сертификата

Компания должна выпускать разработческие сертификаты на основе общекорпоративного корневого сертификата. Когда разработчики подписывают расширения собственными разработческими сертификатами, Dynatrace может проверить подлинность расширения по корневому сертификату, хранящемуся в хранилище учётных данных Dynatrace и на хостах, где выполняются расширения.

Выполните следующие команды для создания корневого сертификата организации. Не задавайте пароль. Dynatrace не поддерживает сертификаты, защищённые паролем.

```
openssl genrsa -out root.key 2048



openssl req -new -key root.key -out root.csr
```

При создании корневого сертификата необходимо явно определить расширение сертификата, указав свойство `-extfile` на файл `ca.txt`. Файл должен содержать следующие данные:

```
basicConstraints=critical, CA:true, pathlen:0



subjectKeyIdentifier    = hash



authorityKeyIdentifier  = keyid:always



keyUsage                = keyCertSign
```

```
openssl x509 -req -days 10000 -in root.csr -signkey root.key -out root.pem -extfile ca.txt
```

В результате создаётся корневой сертификат `root.pem`.

Обратите внимание, что для создания разработческих сертификатов можно также использовать существующий корневой сертификат. Dynatrace принимает только форматы PFX, P12 и PEM, поэтому может потребоваться преобразование существующего сертификата в один из допустимых форматов. Инструкции по преобразованию см. в документации OpenSSL.

### Добавление корневого сертификата в хранилище учётных данных Dynatrace

1. Откройте **Credential Vault**.
2. Выберите **Add new credential**.
3. В поле **Credential type** выберите **Public Certificate**.
4. Выберите область доступа учётных данных **Extension validation**.
5. Введите понятное **Credential name**.
6. Загрузите **Root certificate file**.
7. Нажмите **Save**.

### Создание разработческого сертификата

Для создания разработческого сертификата необходимо сформировать запрос на подпись разработческого сертификата, а затем выпустить сертификат.

#### Создание запроса на подпись разработческого сертификата

Выполните следующие команды для создания запроса на подпись сертификата (CSR) к корневому удостоверяющему центру:

```
openssl genrsa -out developer.key 2048
```

```
openssl req -new -key developer.key -out developer.csr
```

При заполнении полей Отличительного имени (DN) убедитесь, что хотя бы одно поле отличается от DN, заданного для корневого сертификата.

В результате создаётся CSR `developer.csr`, который используется для выпуска разработческого сертификата на основе корневого сертификата.

#### Выпуск разработческого сертификата

Выполните следующие команды для создания разработческого сертификата:

```
openssl req -new -key developer.key -out developer.csr
```

При создании разработческого сертификата необходимо явно определить расширение сертификата, указав свойство `-extfile` на файл `developer.txt`. Файл должен содержать следующие данные:

```
subjectKeyIdentifier    = hash



authorityKeyIdentifier  = keyid:always



keyUsage                = digitalSignature
```

```
openssl x509 -req -days 10000 -in developer.csr -CA root.pem -CAkey root.key -CAcreateserial -out developer.pem -extfile developer.txt
```

В результате создаётся файл сертификата `developer.pem`, который используется для подписания расширений.

### Подписание расширения

Имея разработческий сертификат, используйте следующую команду для подписания расширения. Убедитесь, что файл `extension.zip` находится в каталоге, из которого выполняется команда.

```
openssl cms -sign -signer developer.pem -inkey developer.key -binary -in extension.zip -outform PEM -out extension.zip.sig
```

В результате создаётся файл подписи `extension.zip.sig`.

### Проверка подписи

Используйте следующую команду для проверки файла подписи `extension.zip.sig` по корневому сертификату `root.pem`:

Linux

Windows

```
openssl cms -verify -CAfile root.pem -in extension.zip.sig -binary -content extension.zip -inform PEM -out /dev/null
```

```
openssl cms -verify -CAfile root.pem -in extension.zip.sig -binary -content extension.zip -inform PEM -out NUL
```

Вывод должен содержать фразу `Verification successful`.

### Создание пакета расширения

На завершающем этапе создайте [пакет расширения](/managed/ingest-from/extensions/concepts#package "Подробнее о концепции Dynatrace Extensions."), содержащий только архив `extension.zip` и файл подписи `extension.zip.sig`.

```
bundle.zip



|    extension.zip



|    extension.zip.sig
```

Теперь можно загрузить пакет расширения в окружение Dynatrace. Дополнительные сведения см. в разделе [Управление расширениями](/managed/upgrade/unavailable-in-managed "Выбранный вами раздел недоступен в Dynatrace Managed.").