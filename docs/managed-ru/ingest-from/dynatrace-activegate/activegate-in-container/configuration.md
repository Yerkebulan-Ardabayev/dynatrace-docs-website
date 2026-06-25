---
title: Конфигурация контейнерного ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration
scraped: 2026-05-12T11:36:35.918031
---

# Конфигурация контейнерного ActiveGate

# Конфигурация контейнерного ActiveGate

* 6-min read
* Published Sep 01, 2023

Контейнер ActiveGate можно настроить с помощью специфичных для контейнера методов: переменных окружения или секретов. Более сложные параметры требуют предоставления файла `custom.properties` для ActiveGate. Смотрите раздел [Расширенная конфигурация](#advanced-configuration), чтобы узнать, как использовать механизмы Kubernetes, такие как `ConfigMap`, для монтирования его в `custom.properties`.

Конфиденциальная информация

Для обеспечения безопасности конфиденциальная информация должна передаваться контейнеру ActiveGate в файле-секрете.

## Конфигурация окружения

Образ контейнера ActiveGate не содержит конфигурации, привязанной к вашему окружению.

Ниже перечислены обязательные параметры конфигурации для работы контейнера ActiveGate.

### Конечные точки связи

Список конечных точек связи, разделённых запятыми, которые ActiveGate использует для отправки данных в ваше окружение Dynatrace.

Для определения конечных точек используйте [GET connectivity information for ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "Просмотрите информацию о подключении ActiveGate через Dynatrace API.") в Dynatrace API.

|  |  |
| --- | --- |
| Переменная окружения | `DT_SERVER` |
| Обязательно? | Да |

### ID окружения

[ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте об окружениях мониторинга и работе с ними.") Dynatrace.

|  |  |
| --- | --- |
| Переменная окружения | `DT_TENANT` |
| Обязательно? | Да |

### Токен

[Токен тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его изменить.") используется OneAgent и ActiveGate для передачи данных в Dynatrace. Dynatrace автоматически генерирует токен тенанта для ActiveGate.

Для определения токена используйте [GET connectivity information for ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "Просмотрите информацию о подключении ActiveGate через Dynatrace API.") в Dynatrace API.

|  |  |
| --- | --- |
| Секрет в виде файла | `/var/lib/dynatrace/secrets/tokens/tenant-token` |
| Обязательно? | Да |

### Токен ActiveGate

ActiveGate требует уникальный токен ActiveGate для авторизации в кластере Dynatrace.

Инструкции смотрите в разделе [Генерация токена ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защитите ActiveGate с помощью выделенных токенов.").

|  |  |
| --- | --- |
| Секрет в виде файла | `/var/lib/dynatrace/secrets/tokens/auth-token` |
| Обязательно? | Да |

## Параметры развёртывания

### Группа активации

Определяет группу ActiveGate, к которой принадлежит данный ActiveGate. ActiveGate может входить только в одну группу. Имя группы — строка из буквенно-цифровых символов, дефисов (`-`), символов подчёркивания (`_`) и точек (`.`). Точки используются как разделители, поэтому точка не должна быть первым символом имени группы. Длина строки ограничена 256 символами. Группы ActiveGate позволяют выполнять массовые действия над ActiveGate, например управлять [расширениями](/managed/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные расширения в Dynatrace."). Подробнее смотрите в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Понять основные концепции групп ActiveGate.").

| Переменная окружения | Пример |
| --- | --- |
| `DT_GROUP` | `myGroup` |

### Сетевая зона

Определяет [сетевую зону](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."), к которой принадлежит данный ActiveGate. ActiveGate может входить только в одну сетевую зону. Имя сетевой зоны — строка из буквенно-цифровых символов, дефисов (`-`), символов подчёркивания (`_`) и точек (`.`). Длина строки ограничена 256 символами.

| Переменная окружения | Пример |
| --- | --- |
| `DT_NETWORK_ZONE` | `myNetworkZone` |

## Включённые модули

Контейнерный ActiveGate по умолчанию не включает никаких функциональных возможностей. Включённые модули необходимо указать с помощью переменной окружения `DT_CAPABILITIES`. Укажите список имён модулей через запятую в качестве значения переменной.

| Переменная окружения | Пример |
| --- | --- |
| `DT_CAPABILITIES` | `azure_monitoring,MSGrouter` |

Полный список смотрите в разделе [Модули ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."). Как правило, следует использовать имена разделов `custom.properties` в качестве имён модулей, например `cloudfoundry_monitoring`.

Исключение составляют следующие модули, хранящиеся в разделе `[collector]`:

* `MSGrouter` — включает маршрутизацию сообщений
* `restInterface` — включает модуль REST API
* `java-script-agent-servlet` — включает агент JavaScript

Не все модули поддерживаются

Не все модули поддерживаются в контейнерных развёртываниях. Подробнее смотрите в разделе [Назначения и функциональность ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Узнайте о возможностях и применениях ActiveGate.").

## Сетевые параметры

### Прокси

Прокси, используемый для связи с кластером Dynatrace, которому ActiveGate отправляет данные.

| Секрет в виде файла | Описание |
| --- | --- |
| `/var/lib/dynatrace/secrets/internal-proxy/host` | Адрес сервера. |
| `/var/lib/dynatrace/secrets/internal-proxy/port` | Необязательный порт. Если не указан, используется порт 8080 по умолчанию. |
| `/var/lib/dynatrace/secrets/internal-proxy/scheme` | ActiveGate версии 1.289+. Необязательная схема. Если не указана, используется схема `http` по умолчанию. Это соответствует наиболее распространённой настройке: подключение к прокси инициируется по HTTP и автоматически обновляется до защищённого. Всё дальнейшее взаимодействие ActiveGate через прокси защищено SSL/TLS. Необходимо установить значение `https` для прокси, не поддерживающих HTTP вообще. |
| `/var/lib/dynatrace/secrets/internal-proxy/username` | Необязательное имя пользователя. |
| `/var/lib/dynatrace/secrets/internal-proxy/password` | Необязательный пароль, смотрите [Требования к паролю прокси](#proxy-password-requirements). |

#### Расширенные сценарии

Для более сложных сценариев, где один или несколько прокси используются не только для связи с кластером Dynatrace, смотрите раздел [Прокси для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для установки прокси."). После составления необходимой конфигурации её можно передать контейнеру ActiveGate в виде файла [custom.properties](#advanced-configuration).

#### Требования к паролю прокси

Пароль прокси должен соответствовать следующим требованиям.

| Требования | Символы |
| --- | --- |
| Разрешённые символы | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
| Запрещённые символы | пробел ' \` , & = + % \\ |

### Балансировщик нагрузки между ActiveGate и OneAgent

OneAgent обращается к ActiveGate через автоматически определённый список конечных точек. Если на пути от OneAgent к ActiveGate установлен балансировщик нагрузки, например Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/), необходимо явно указать конечную точку для использования OneAgent.

| Переменная окружения | Пример значения |
| --- | --- |
| `DT_DNS_ENTRY_POINT` | `https://sg1.mydomain.com:9999` |

### Балансировщик нагрузки между ActiveGate и кластером Dynatrace

На пути от ActiveGate к кластеру Dynatrace можно установить обратный прокси или балансировщик нагрузки. Это позволяет ActiveGate подключаться к любому доступному узлу кластера, распределяя нагрузку.

Для этого необходимо:

* Указать адрес обратного прокси/балансировщика нагрузки.
* Убедиться, что ActiveGate будет игнорировать информацию об адресе цели, поступающую от кластера Dynatrace, и подключаться только к указанному адресу.

![ActiveGate, подключающийся к кластеру Dynatrace через обратный прокси/балансировщик нагрузки](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

ActiveGate, подключающийся к кластеру Dynatrace через обратный прокси/балансировщик нагрузки

В этом сценарии необходимо установить следующие переменные окружения.

| Переменная окружения | Пример значения |
| --- | --- |
| `DT_SERVER` | `https://load.balancer.com:9999` |
| `DT_IGNORE_CLUSTER_RUNTIME_INFO` | `true` |

## Параметры SSL

### Пользовательский SSL-сертификат

ActiveGate будет использовать пользовательский сертификат вместо сертификата по умолчанию. Для настройки требуется файл в формате `PKCS#12`, содержащий закрытый ключ и соответствующую цепочку сертификатов. Подробнее смотрите в разделе [Пользовательский SSL-сертификат для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на ActiveGate.").

| Секрет в виде файла | Описание |
| --- | --- |
| `/var/lib/dynatrace/secrets/tls/server.p12` | Файл сертификата |
| `/var/lib/dynatrace/secrets/tls/password` | Необязательный пароль сертификата |
| `/var/lib/dynatrace/secrets/tls/alias` | Необязательный псевдоним сертификата. Значение должно быть в нижнем регистре. |

### Доверенные корневые сертификаты

ActiveGate может использовать дополнительные доверенные корневые сертификаты. Для настройки требуется файл в формате `PEM`, содержащий список сертификатов для включения в хранилище доверенных сертификатов. Подробнее смотрите в разделе [Доверенные корневые сертификаты для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как настроить пользовательские доверенные корневые сертификаты на ActiveGate.").

| Секрет в виде файла | Описание |
| --- | --- |
| `/var/lib/dynatrace/secrets/rootca/rootca.pem` | Файл сертификата |

### HTTP-порт

По умолчанию контейнер ActiveGate открывает HTTPS-порт `9999`. Если требуется связь через HTTP, необходимо явно указать HTTP-порт.

| Переменная окружения | Пример |
| --- | --- |
| `DT_HTTP_PORT` | `8888` |

## Расширенная конфигурация

Помимо параметров конфигурации, передаваемых через переменные окружения или файлы, можно настроить все прочие [параметры конфигурации](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."), предоставив содержимое файла `custom.properties`.

1. Определите `ConfigMap`.

   ```
   kind: ConfigMap
   apiVersion: v1
   data:
     custom.properties: |-
       [vmware_monitoring]
       vmware_monitoring_enabled = true
   metadata:
     name: vmware-config
     namespace: dynatrace
   ```

2. Укажите ссылку на `ConfigMap` в файле развёртывания.

   ```
   [...]
   volumeMounts:
   [...]
   - name: ag-conf
     mountPath: /var/lib/dynatrace/gateway/config_template/custom.properties
     subPath: custom.properties
   [...]
   volumes:
   - name: ag-conf
     configMap:
       name: vmware-config
       items:
       - key: custom.properties
         path: custom.properties
   ```