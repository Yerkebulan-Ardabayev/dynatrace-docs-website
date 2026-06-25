---
title: Доверенные корневые сертификаты для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate
scraped: 2026-05-12T11:27:41.983574
---

# Доверенные корневые сертификаты для ActiveGate

# Доверенные корневые сертификаты для ActiveGate

* 7-min read
* Updated on Feb 24, 2026

В некоторых ситуациях необходимо добавить дополнительные сертификаты в хранилище сертификатов, поставляемое с ActiveGate. Следуйте приведённой ниже процедуре для добавления дополнительного сертификата в существующий ActiveGate.

### Альтернатива: добавление сертификатов во время установки ActiveGate (необязательно)

Дополнительные доверенные корневые сертификаты также можно указать во время установки ActiveGate через параметры установки для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#ca-certificate "Узнайте о параметрах командной строки для ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#ca-certificate "Узнайте о параметрах для ActiveGate на Windows.").

## Определение необходимости добавления CA-сертификата в ActiveGate

ActiveGate подключается к другим компонентам Dynatrace (кластерам, серверам) или сторонним системам (VMware, Cloud Foundry, Kubernetes, OpenShift) по защищённым SSL-каналам. Хранилище корневых CA-сертификатов, поставляемое с ActiveGate (стандартный набор сертификатов Java), иногда недостаточно для покрытия всех необходимых сценариев.

Например:

* Сертификат был выдан внутренним удостоверяющим центром вашей организации для прокси, перехватывающего SSL-трафик
* Некоторые серверы в вашей организации используют самоподписанные сертификаты

В таких случаях в лог-файле ActiveGate появится ошибка о том, что сертификат, предъявленный сервером, к которому ActiveGate пытался подключиться, не является доверенным. В этих случаях необходимо импортировать недостающий сертификат в ActiveGate.

Добавление сертификата является потенциальной угрозой безопасности. Проконсультируйтесь с командой безопасности вашей организации, прежде чем добавлять новый доверенный корневой сертификат. Если в логах ActiveGate появилась ошибка о ненадёжном сертификате, **не** предполагайте автоматически, что нужно добавить сертификат. **Ошибка недействительного сертификата может также означать попытку взлома системы безопасности вашей организации.**

## Настройка доверенных корневых сертификатов

### Получение необходимых CA-сертификатов

Перед добавлением сертификата в ActiveGate необходимо его получить и поместить в файл `ca.crt`. Получение CA-сертификата зависит от конкретного контекста: обратитесь к соответствующим специалистам в вашей организации.

### Настройка хранилища доверенных сертификатов

agctl

custom.properties

ActiveGate версии 1.333+

Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#trust-store "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для настройки доверенных корневых сертификатов.

#### Установка с минимальными параметрами:

```
agctl trust-store set --certificates=/path/to/ca.crt
```

#### Установка с пользовательским именем файла и паролем:

```
agctl trust-store set --certificates=/path/to/ca.crt --truststore=custom-truststore.p12 --password=mypassword
```

#### Параметры:

* `--certificates`: путь к файлу(ам) сертификатов в формате PEM (обязательный)
* `--truststore`: имя файла для хранилища в директории SSL ActiveGate (необязательный, по умолчанию: `mytruststore.p12`)
* `--password`: пароль для хранилища доверенных сертификатов (необязательный, по умолчанию: `changeit`)

После настройки необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.").

Ручная настройка требует создания файла хранилища PKCS#12 с помощью `keytool`.

1. **Создайте хранилище доверенных сертификатов из файла CA-сертификата**

   Создайте дополнительное хранилище, содержащее только ваши CA-сертификаты. При запуске ActiveGate объединит его со встроенным хранилищем JDK.
   Хранилище должно быть в формате **PKCS#12**. Форматы OpenSSL не поддерживаются, поэтому используйте команду `keytool`.
   После конвертации поместите сертификат в [директорию SSL ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").

   При импорте нескольких сертификатов укажите уникальный псевдоним для каждого. Использование одного и того же псевдонима перезаписывает предыдущие сертификаты.

   Примеры (Linux):

   ```
   /opt/dynatrace/gateway/jre/bin/keytool -import -file ca.crt -alias dt_k8s_api -storetype pkcs12 -keystore /var/lib/dynatrace/gateway/ssl/mytrusted.p12
   ```

   или:

   ```
   /opt/dynatrace/gateway/jre/bin/keytool -import -file dt_k8s_api.pem -alias myCertAuthority -storetype pkcs12 -keystore mytrusted.p12
   ```

   Для Linux убедитесь, что пользователь ActiveGate (`dtuserag` по умолчанию) имеет:

   * право записи в [директорию SSL ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") (по умолчанию `/var/lib/dynatrace/gateway/ssl`)
   * право чтения созданного хранилища

2. **Настройте ActiveGate для использования пользовательского хранилища**

   Убедитесь, что файл хранилища находится в [директории SSL ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux."), затем добавьте следующие записи в файл `custom.properties`:

   ```
   [collector]
   trustedstore = mytrusted.p12
   # следующие записи необязательны
   trustedstore-password = changeit
   trustedstore-type = PKCS12
   ```

   Зашифрованный пароль

   Пароль будет зашифрован при перезапуске службы ActiveGate.

3. **Перезапустите службу ActiveGate и проверьте конфигурацию сертификата**

   [Перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.") для применения изменений.
   При корректной настройке в логах ActiveGate появится запись:

   ```
   Custom certificate configuration created successfully.
   ```

## Конфигурация

**Раздел: [collector]**

| Свойство | Значение по умолчанию | Описание |
| --- | --- | --- |
| `trustedstore` | не задано | Путь к файлу с доверенными сертификатами (относительно директории SSL ActiveGate). Смотрите [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate."). |
| `trustedstore-exclusive` | не задано | При значении `true` ActiveGate использует только пользовательское хранилище (встроенное хранилище JRE не объединяется). |
| `trustedstore-password` | `changeit` | Пароль пользовательского хранилища (шифруется при запуске). |
| `trustedstore-type` | `pkcs12` | Формат хранилища ключей Java. |

## Ограничения

Настроенное хранилище не будет использоваться (конфигурация хранилища останется неизменной), если выполняется любое из следующих условий:

* Задано системное свойство `javax.net.ssl.trustStore` (имеет приоритет над конфигурацией ActiveGate).
* Настроенное хранилище не может быть прочитано с использованием настроенных пути, пароля и типа.
* Объединённая конфигурация не может быть записана в файл `ssl/runtime.cacerts`.

## Общая информация о CA-сертификатах

Для создания доверенного SSL-соединения необходимо:

* Между сертификатами, предъявляемыми сервером (конечной точкой API), и сертификатами в хранилище ActiveGate должна быть построена полная цепочка сертификатов.
* Корневой сертификат цепочки должен быть включён в хранилище ActiveGate.

Для просмотра сертификатов, предъявляемых конечной точкой:

```
openssl s_client -connect <API_ENDPOINT>:<PORT> -showcerts -servername <API_ENDPOINT_HOSTNAME>
```

Если команда показывает полную цепочку сертификатов, необходимо добавить корневой сертификат в хранилище ActiveGate. Если цепочка неполная, корневой сертификат необходимо получить из другого источника.