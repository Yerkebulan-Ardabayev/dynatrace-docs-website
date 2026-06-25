---
title: agctl — интерфейс командной строки для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface
scraped: 2026-05-12T12:09:03.572949
---

# agctl — интерфейс командной строки для ActiveGate

# agctl — интерфейс командной строки для ActiveGate

* Reference
* 15-min read
* Published Feb 05, 2026

ActiveGate версии 1.333+

`agctl` — интерфейс командной строки для управления конфигурацией ActiveGate. Позволяет настраивать различные параметры ActiveGate непосредственно из командной строки без ручного редактирования конфигурационных файлов.

После изменения конфигурации ActiveGate с помощью `agctl` необходимо перезапустить ActiveGate, чтобы изменения вступили в силу. Смотрите раздел [Запуск/остановка/перезапуск ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").

## Перед началом работы

### Предварительные требования

* ActiveGate установлен на вашей системе
* Разрешения на выполнение `agctl`. Смотрите раздел [Доступ к agctl](#access-agctl) ниже.

### Доступ к agctl

Linux

Windows

На Linux-системах `agctl` автоматически добавляется в PATH для удобного доступа. Его можно запустить из любого каталога.

Для выполнения `agctl` необходимо принадлежать к группе пользователей службы ActiveGate. По умолчанию это группа `dtuserag`. Подробнее о настройке пользователя смотрите в разделах:

* [Настройка установки ActiveGate](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.")
* [Настройки по умолчанию](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings#service-account "Узнайте о настройках по умолчанию при установке ActiveGate на Linux")

**Пример запуска agctl**

```
agctl [command] [operation] [parameters]
```

На Windows-системах `agctl.bat` должен выполняться из [директории установки ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").

`agctl.bat` должен запускаться с правами администратора.

**Пример запуска agctl.bat из директории установки**

```
"C:\Program Files\dynatrace\gateway\agctl.bat" [command] [operation] [parameters]
```

## Структура команды

```
agctl [command] [operation] [parameters]
```

Где:

* `[command]`: конкретная функция ActiveGate для управления (например, `group`, `modules`, `ssl-port`)
* `[operation]`: выполняемое действие (например, `set`, `get`, `clear`, `enable`, `disable`)
* `[parameters]`: параметры, специфичные для команды

## Доступные команды

| Команда | Описание |
| --- | --- |
| [help](#help) | Отображение справочного сообщения |
| [group](#group) | Управление конфигурацией группы ActiveGate |
| [incoming-endpoint](#incoming-endpoint) | Управление конфигурацией обратного прокси для OneAgent |
| [modules](#modules) | Управление конфигурацией модулей |
| [network-zone](#network-zone) | Управление конфигурацией сетевой зоны |
| [outgoing-endpoint](#outgoing-endpoint) | Управление конфигурацией обратного прокси для ActiveGate |
| [properties](#properties) | Установка свойств на основе предоставленного конфигурационного файла |
| [property](#property) | Управление отдельными пользовательскими свойствами |
| [ssl-certificate](#ssl-certificate) | Управление конфигурацией пользовательского SSL-сертификата |
| [ssl-port](#ssl-port) | Управление конфигурацией HTTPS-порта |
| [support-archive](#support-archive) | Создание архива поддержки для диагностики |
| [trust-store](#trust-store) | Управление конфигурацией хранилища доверенных сертификатов |
| [version](#version) | Получение версии ActiveGate |

### Help

Отображение справочной информации для `agctl`.

#### Использование

```
agctl help
```

Для получения справки по конкретной команде:

```
agctl [command] help
```

#### Примеры

```
# Общая справка
agctl help

# Справка для команды group
agctl group help
```

### Group

Управление конфигурацией группы ActiveGate. Группы позволяют выполнять массовые действия над ActiveGate.

Подробнее о группах ActiveGate смотрите в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Понять основные концепции групп ActiveGate.").

#### Использование

```
agctl group set <NAME>
agctl group set --value=<NAME>
agctl group get
agctl group clear
agctl group help
```

#### Операции

| Операция | Описание |
| --- | --- |
| `set` | Назначить имя группы ActiveGate |
| `get` | Отобразить текущее имя группы |
| `clear` | Удалить текущее имя группы |
| `help` | Показать справку для команды group |

#### Параметры для set

**Обязательный (один из):**

* `<NAME>`: имя группы как позиционный аргумент
* `--value=<NAME>`: имя группы как именованный параметр (имеет приоритет при указании обоих)

#### Правила именования

* Допустимые символы: буквенно-цифровые символы, дефисы (`-`), символы подчёркивания (`_`) и точки (`.`)
* Точки используются как разделители и не могут быть первым или последним символом
* Максимальная длина: 256 символов

#### Примеры

```
# Установка группы через позиционный аргумент
agctl group set my.group

# Установка группы через именованный параметр
agctl group set --value=production.activegate

# Получение текущей группы
agctl group get

# Очистка конфигурации группы
agctl group clear
```

### Incoming endpoint

Управление конфигурацией обратного прокси для трафика OneAgent. Настраивает URL конечных точек, используемых OneAgent для подключения через обратный прокси.

Подробнее смотрите в разделе [Настройка обратного прокси для OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Настройте свойства ActiveGate для установки обратного прокси или балансировщика нагрузки для OneAgent.").

Смотрите также конфигурацию [Outgoing endpoint](#outgoing-endpoint).

#### Использование

```
agctl incoming-endpoint set <URLS>
agctl incoming-endpoint set --value=<URLS>
agctl incoming-endpoint get
agctl incoming-endpoint clear
agctl incoming-endpoint help
```

#### Операции

| Операция | Описание |
| --- | --- |
| `set` | Настроить URL входящих конечных точек |
| `get` | Отобразить текущие URL конечных точек |
| `clear` | Удалить текущие URL конечных точек |
| `help` | Показать справку для команды incoming-endpoint |

#### Параметры для set

**Обязательный (один из):**

* `<URLS>`: список URL, разделённых запятыми, как позиционный аргумент
* `--value=<URLS>`: список URL, разделённых запятыми, как именованный параметр

#### Требования к формату URL

* Формат: `https://<DOMAIN>:<PORT>`
* `<DOMAIN>` должен быть FQDN, IPv4 или IPv6-адресом
* `<PORT>` необязателен, по умолчанию 443
* Путь `/communication` необязателен
* Несколько URL разделяются запятыми

#### Примеры

```
# Одна конечная точка
agctl incoming-endpoint set https://proxy.example.com:443

# Несколько конечных точек
agctl incoming-endpoint set https://proxy1.example.com:443,https://proxy2.example.com:8443/communication

# Через именованный параметр
agctl incoming-endpoint set --value=https://proxy.example.com/communication

# Получение текущей конфигурации
agctl incoming-endpoint get

# Очистка конфигурации
agctl incoming-endpoint clear
```

### Modules

Управление конфигурацией модулей ActiveGate. Позволяет включать или отключать отдельные функциональные модули.

Подробнее о модулях ActiveGate смотрите в разделе [Свойства и параметры конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.").

#### Использование

```
agctl modules enable <MODULES>
agctl modules enable --value=<MODULES>
agctl modules disable <MODULES>
agctl modules disable --value=<MODULES>
agctl modules get
agctl modules help
```

#### Операции

| Операция | Описание |
| --- | --- |
| `enable` | Включить один или несколько модулей |
| `disable` | Отключить один или несколько модулей |
| `get` | Отобразить включённые в настоящее время модули |
| `help` | Показать справку для команды modules |

#### Параметры для enable и disable

**Обязательный (один из):**

* `<MODULES>`: список имён модулей, разделённых запятыми, как позиционный аргумент
* `--value=<MODULES>`: список имён модулей, разделённых запятыми, как именованный параметр

#### Примеры

```
# Включить несколько модулей
agctl modules enable MSGrouter,metrics_ingest

# Отключить модуль через именованный параметр
agctl modules disable --value=synthetic

# Получить включённые модули
agctl modules get
```

### Network zone

Управление конфигурацией сетевой зоны. Сетевые зоны позволяют определять границы маршрутизации для инфраструктуры мониторинга.

Подробнее о сетевых зонах смотрите в разделе [Сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

#### Использование

```
agctl network-zone set <NAME>
agctl network-zone set --value=<NAME>
agctl network-zone get
agctl network-zone clear
agctl network-zone help
```

#### Операции

| Операция | Описание |
| --- | --- |
| `set` | Настроить имя сетевой зоны |
| `get` | Отобразить текущее имя сетевой зоны |
| `clear` | Удалить текущее имя сетевой зоны |
| `help` | Показать справку для команды network-zone |

#### Правила именования

* Допустимые символы: буквенно-цифровые символы, дефисы (`-`), символы подчёркивания (`_`) и точки (`.`)
* Точки используются как разделители и не могут быть первым или последним символом
* Максимальная длина: 256 символов

#### Примеры

```
# Установка сетевой зоны через позиционный аргумент
agctl network-zone set my.zone

# Установка через именованный параметр
agctl network-zone set --value=production.zone

# Получение текущей сетевой зоны
agctl network-zone get

# Очистка конфигурации сетевой зоны
agctl network-zone clear
```

### Outgoing endpoint

Управление конфигурацией обратного прокси для трафика ActiveGate. Настраивает URL конечных точек, используемых ActiveGate для подключения к Dynatrace через обратный прокси.

Подробнее смотрите в разделе [Настройка обратного прокси для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Узнайте, как настроить свойства ActiveGate для установки обратного прокси или балансировщика нагрузки.").

Смотрите также конфигурацию [Incoming endpoint](#incoming-endpoint).

#### Использование

```
agctl outgoing-endpoint set <URLS>
agctl outgoing-endpoint set --value=<URLS>
agctl outgoing-endpoint get
agctl outgoing-endpoint clear
agctl outgoing-endpoint help
```

#### Операции

| Операция | Описание |
| --- | --- |
| `set` | Настроить URL исходящих конечных точек |
| `get` | Отобразить текущие URL конечных точек |
| `clear` | Удалить текущие URL конечных точек |
| `help` | Показать справку для команды outgoing-endpoint |

#### Требования к формату URL

* Формат: `https://<REVERSE_PROXY>:<REVERSE_PROXY_PORT>/communication`
* `<REVERSE_PROXY>` должен быть FQDN, IPv4 или IPv6-адресом
* `<REVERSE_PROXY_PORT>` необязателен, по умолчанию 443
* Путь `/communication` необязателен
* Несколько URL разделяются запятыми

#### Примеры

```
# Одна исходящая конечная точка
agctl outgoing-endpoint set https://proxy.example.com:443

# Несколько конечных точек
agctl outgoing-endpoint set https://proxy1.example.com:443,https://proxy2.example.com:8443/communication

# Через именованный параметр
agctl outgoing-endpoint set --value=https://proxy.example.com/communication

# Получение текущей конфигурации
agctl outgoing-endpoint get

# Очистка конфигурации
agctl outgoing-endpoint clear
```

### Properties

Установка нескольких свойств на основе предоставленного конфигурационного файла. Позволяет применить полную конфигурацию из файла `.properties`.

#### Использование

```
agctl properties set <PATH>
agctl properties set --value=<PATH>
agctl properties help
```

#### Требования

* Файл должен иметь расширение `.properties`
* Файл должен существовать и быть доступным для чтения

#### Примеры

```
# Применить конфигурацию из файла properties
agctl properties set myconfig.properties

# Применить конфигурацию по абсолютному пути
agctl properties set --value=/home/user/activegate/myconfig.properties
```

### Property

Управление отдельными пользовательскими свойствами. Позволяет устанавливать, получать или удалять конкретные свойства в конфигурации ActiveGate.

#### Использование

```
agctl property set --section=<SECTION> --key=<KEY> --value=<VALUE>
agctl property get --section=<SECTION> --key=<KEY>
agctl property clear --section=<SECTION> --key=<KEY>
agctl property help
```

#### Параметры для set

**Обязательные:**

* `--section=<SECTION>`: имя раздела конфигурации
* `--key=<KEY>`: имя ключа свойства
* `--value=<VALUE>`: значение свойства (несколько значений могут разделяться запятыми)

#### Параметры для get и clear

**Обязательные:**

* `--section=<SECTION>`: имя раздела конфигурации
* `--key=<KEY>`: имя ключа свойства

#### Примеры

```
# Установить свойство
agctl property set --section=collector --key=group --value=my.group

# Получить значение свойства
agctl property get --section=collector --key=group

# Удалить свойство
agctl property clear --section=collector --key=group
```

### SSL certificate

Управление конфигурацией пользовательского SSL-сертификата для ActiveGate.

Подробнее смотрите в разделе [Настройка пользовательского SSL-сертификата на ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

#### Использование

```
agctl ssl-certificate set --certificate=<PATH> --key=<PATH> [--pem-password=<STRING>] [--password=<STRING>] [--alias=<STRING>]
agctl ssl-certificate get
agctl ssl-certificate clear
agctl ssl-certificate help
```

#### Параметры для set

**Обязательные:**

* `--certificate=<PATH>`: путь к файлу сертификата в формате PEM
* `--key=<PATH>`: путь к файлу закрытого ключа в формате PEM

**Необязательные:**

* `--pem-password=<STRING>`: пароль для закрытого ключа (если зашифрован)
* `--password=<STRING>`: пароль для шифрования хранилища ключей (по умолчанию: генерируется случайно)
* `--alias=<STRING>`: псевдоним сертификата в хранилище ключей (по умолчанию: 1)

#### Примеры

```
# Минимальные параметры
agctl ssl-certificate set --certificate=cert.crt --key=key.pem

# Все параметры
agctl ssl-certificate set --certificate=cert.crt --key=key.pem --pem-password=secret --password=changeit --alias=mycert

# Получить конфигурацию SSL-сертификата
agctl ssl-certificate get

# Очистить конфигурацию
agctl ssl-certificate clear
```

### SSL port

Управление конфигурацией HTTPS-порта для ActiveGate. Позволяет изменить порт, используемый ActiveGate для HTTPS-связи.

#### Использование

```
agctl ssl-port set <PORT>
agctl ssl-port set --value=<PORT>
agctl ssl-port get
agctl ssl-port clear
agctl ssl-port help
```

#### Требования к порту

* Допустимый диапазон: 1-65535
* Использование порта ниже 1024 требует повышенных привилегий на не-Windows-системах

#### Примеры

```
# Установить HTTPS-порт через позиционный аргумент
agctl ssl-port set 9999

# Через именованный параметр
agctl ssl-port set --value=8443

# Получить текущий HTTPS-порт
agctl ssl-port get

# Очистить конфигурацию порта
agctl ssl-port clear
```

### Support archive

Создание архива поддержки для диагностики проблем ActiveGate. Архив содержит диагностические данные, логи и информацию о конфигурации.

Смотрите также: [Сбор диагностических данных с помощью agctl](/managed/ingest-from/dynatrace-activegate/activegate-diagnostics#collect-diagnostic-data-with-agctl "Узнайте, как выполнить диагностику ActiveGate").

#### Использование

```
agctl support-archive create [--directory=<PATH>] [--days=<NUMBER>] [--modules=<MODULES>] [--stdout]
agctl support-archive help
```

#### Параметры для create

**Все параметры необязательны:**

* `--directory=<PATH>`: выходной каталог для архива поддержки (по умолчанию: текущий рабочий каталог)
* `--days=<NUMBER>`: количество дней данных для сбора (по умолчанию: 30)
* `--modules=<MODULES>`: список модулей для включения, разделённых запятыми (по умолчанию: все модули)
* `--stdout`: вывод ZIP-архива поддержки в stdout, логи консоли в stderr

#### Примеры

```
# Создать архив с настройками по умолчанию
agctl support-archive create

# Создать архив за определённый период для конкретных модулей
agctl support-archive create --directory=/home/user --days=3 --modules=MSGrouter,metrics_ingest

# Создать архив и вывести в stdout (для контейнеров)
agctl support-archive create --stdout 1> sa.zip 2> out.txt
```

#### Использование в контейнерных окружениях

Kubernetes

OpenShift

```
kubectl exec -n <namespace> <pod-name> -- agctl support-archive create --stdout > ag-support-archive.zip
```

```
oc exec -n <namespace> <pod-name> [-c <container>] -- agctl support-archive create --stdout > ag-support-archive.zip
```

Windows PowerShell не поддерживается

На Windows используйте командную строку (`cmd.exe`); PowerShell не поддерживается.

### Trust store

Управление конфигурацией хранилища доверенных сертификатов для ActiveGate. Хранилище содержит доверенные корневые сертификаты для SSL/TLS-соединений.

Подробнее смотрите в разделе [Настройка доверенных корневых сертификатов на ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate.").

#### Использование

```
agctl trust-store set --certificates=<PATH> [--truststore=<FILE>] [--password=<STRING>]
agctl trust-store get
agctl trust-store clear
agctl trust-store help
```

#### Параметры для set

**Обязательный:**

* `--certificates=<PATH>`: путь к цепочке сертификатов в формате PEM

**Необязательные:**

* `--truststore=<FILE>`: имя файла для создания в директории SSL ActiveGate (по умолчанию: `mytruststore.p12`)
* `--password=<STRING>`: пароль для хранилища доверенных сертификатов (по умолчанию: `changeit`)

#### Примеры

```
# Установить хранилище с пользовательским именем файла и паролем
agctl trust-store set --certificates=certs.crt --truststore=superstore.p12 --password=changeit

# Установить хранилище с настройками по умолчанию
agctl trust-store set --certificates=certs.crt

# Получить конфигурацию хранилища
agctl trust-store get

# Очистить конфигурацию хранилища
agctl trust-store clear
```

### Version

Получение информации о версии ActiveGate.

#### Использование

```
agctl version get
agctl version help
```

#### Примеры

```
# Получить версию ActiveGate
agctl version get
```

## Типовые сценарии использования

Не забывайте [перезапускать ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") после внесения изменений конфигурации, чтобы они вступили в силу.

### Начальная конфигурация ActiveGate

После установки ActiveGate может потребоваться настройка нескольких параметров одновременно:

```
# Установить группу ActiveGate
agctl group set production.activegate

# Настроить сетевую зону
agctl network-zone set production.zone
```

### Настройка обратного прокси

Для настройки ActiveGate за обратным прокси:

```
# Настроить исходящую конечную точку для трафика ActiveGate -> Dynatrace
agctl outgoing-endpoint set https://proxy.example.com:443/communication

# Настроить входящую конечную точку для трафика OneAgent -> ActiveGate
agctl incoming-endpoint set https://proxy.example.com:443/communication
```

### Управление модулями

Включение конкретных модулей для нужд мониторинга:

```
# Включить необходимые модули
agctl modules enable MSGrouter,metrics_ingest

# Проверить включённые модули
agctl modules get
```

### Конфигурация SSL-сертификата

```
# Установить пользовательский SSL-сертификат
agctl ssl-certificate set --certificate=/path/to/cert.crt --key=/path/to/key.pem --password=mypassword

# Проверить конфигурацию
agctl ssl-certificate get
```

### Диагностика

Создание архива поддержки при возникновении проблем:

```
# Создать архив поддержки за последние 7 дней в директорию /tmp
agctl support-archive create --days=7 --directory=/tmp
```

## Смотрите также

* [Запуск/остановка/перезапуск ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.")
* [Свойства и параметры конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.")
* [Диагностика ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-diagnostics "Узнайте, как выполнить диагностику ActiveGate")
* [Настройка установки ActiveGate](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.")
* [Настройка пользовательского SSL-сертификата на ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.")
* [Настройка доверенных корневых сертификатов на ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate.")
* [Настройка обратного прокси для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Узнайте, как настроить свойства ActiveGate для установки обратного прокси или балансировщика нагрузки.")
* [Настройка обратного прокси для OneAgent](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent "Настройте свойства ActiveGate для установки обратного прокси или балансировщика нагрузки для OneAgent.")