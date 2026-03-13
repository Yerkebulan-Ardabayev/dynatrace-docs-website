---
title: Containerized ActiveGate configuration
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration
scraped: 2026-03-06T21:38:19.412641
---

# Настройка контейнеризированного ActiveGate

# Настройка контейнеризированного ActiveGate

* Последняя версия Dynatrace
* Чтение: 6 минут
* Опубликовано 1 сентября 2023 г.

Контейнер ActiveGate можно в определённой степени настроить с помощью специфичных для контейнеров методов через переменные или секреты. Для более продвинутых настроек необходимо предоставить файл `custom.properties` для ActiveGate. См. раздел [Расширенная настройка](#advanced-configuration), чтобы узнать, как использовать механизмы Kubernetes, такие как `ConfigMap`, для привязки к `custom.properties`.

Конфиденциальная информация

Для обеспечения безопасности вы должны передавать конфиденциальную информацию контейнеру ActiveGate в файле, содержащем секрет.

## Настройка среды

Образ контейнера ActiveGate не содержит никакой конфигурации, связанной с вашей средой.

Ниже приведены обязательные параметры конфигурации для работы вашего контейнера ActiveGate.

### Эндпоинты связи

Это разделённый запятыми список эндпоинтов связи, которые ActiveGate использует для отправки данных в вашу среду Dynatrace.

Для определения эндпоинтов используйте [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "Просмотр информации о подключении ActiveGate через Dynatrace API.") в Dynatrace API.

### Идентификатор среды

[Идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Понимание и работа со средами мониторинга.") Dynatrace.

### Токен

[Токен тенанта](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его изменить.") используется OneAgent и ActiveGate для передачи данных в Dynatrace. Dynatrace автоматически генерирует токен тенанта для вашего ActiveGate.

Для определения токена используйте [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "Просмотр информации о подключении ActiveGate через Dynatrace API.") в Dynatrace API.

### Токен ActiveGate

ActiveGate требует уникальный токен ActiveGate для авторизации в кластере Dynatrace.

Инструкции см. в разделе [Генерация токена ActiveGate](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защита ActiveGate с помощью выделенных токенов.").

## Параметры развёртывания

### Группа активации

Определяет группу ActiveGate, к которой принадлежит ActiveGate. ActiveGate может принадлежать только одной группе. Имя группы ActiveGate -- это строка из буквенно-цифровых символов, дефисов (`-`), подчёркиваний (`_`) и точек (`.`). Точки используются как разделители, поэтому нельзя использовать точку в качестве первого символа имени группы. Длина строки ограничена 256 символами. Вы можете использовать группы ActiveGate для выполнения массовых операций с вашими ActiveGate, таких как управление [расширениями](/docs/ingest-from/extensions "Узнайте, как создавать и управлять расширениями Dynatrace."), работающими на ActiveGate. Если вы хотите назначить ActiveGate группе, см. [Группа ActiveGate](/docs/ingest-from/dynatrace-activegate/activegate-group "Основные концепции групп ActiveGate.").

### Сетевая зона

Определяет [сетевую зону](/docs/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace."), к которой принадлежит ActiveGate. ActiveGate может принадлежать только одной сетевой зоне. Имя сетевой зоны -- это строка из буквенно-цифровых символов, дефисов (`-`), подчёркиваний (`_`) и точек (`.`). Точки используются как разделители, поэтому нельзя использовать точку в качестве первого символа имени сетевой зоны. Длина строки ограничена 256 символами.

## Включённые модули

Контейнеризированный ActiveGate не включает никакие функциональные возможности по умолчанию. Включённые модули необходимо указать с помощью переменной окружения `DT_CAPABILITIES`. Добавьте разделённый запятыми список имён модулей в качестве значения переменной.

См. [Модули ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями.") для полного списка. Как правило, в качестве имён модулей следует использовать имена секций `custom.properties`, например `cloudfoundry_monitoring`.

Исключениями из этого правила являются следующие модули, хранящиеся в секции `[collector]`.

* `MSGrouter` -- включает маршрутизацию сообщений
* `restInterface` -- включает модуль REST API
* `java-script-agent-servlet` -- включает JavaScript-агент

Поддерживаются не все модули

В контейнеризированных развёртываниях пока поддерживаются не все модули. Дополнительную информацию см. в разделе [Назначение и функциональность ActiveGate](/docs/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Узнайте о возможностях и применениях ActiveGate.").

## Сетевые настройки

### Прокси

Прокси, используемый для связи с кластером Dynatrace, в который ActiveGate отправляет данные.

#### Расширенные сценарии

Для более продвинутых сценариев, когда один или несколько прокси используются не только для связи с кластером Dynatrace, см. [Прокси для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Узнайте, как настроить свойства ActiveGate для настройки прокси."). После создания необходимой конфигурации вы можете предоставить её контейнеру ActiveGate в виде файла [custom.properties](#advanced-configuration).

#### Правила для пароля прокси

Пароль прокси должен соответствовать следующим требованиям.

| Требования | Соответствующие символы |
| --- | --- |
| Допустимые символы | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
| Недопустимые символы | пробел ' ` , & = + % \ |

### Балансировщик нагрузки между ActiveGate и OneAgent

Dynatrace OneAgent обращается к ActiveGate через автоматически определяемый список эндпоинтов. Если на пути от OneAgent к ActiveGate размещён балансировщик нагрузки, например Kubernetes [Service](https://kubernetes.io/docs/concepts/services-networking/service/), необходимо явно указать эндпоинт для использования OneAgent.

### Балансировщик нагрузки между ActiveGate и кластером Dynatrace

На пути от ActiveGate к кластеру Dynatrace может быть размещён обратный прокси или балансировщик нагрузки. Это позволяет вашему ActiveGate подключаться к любому доступному узлу кластера, распределяя нагрузку между узлами.
Для этого необходимо:

* Указать адрес обратного прокси/балансировщика нагрузки.
* Убедиться, что ActiveGate будет игнорировать любую дополнительную информацию о целевом адресе, отправленную кластером Dynatrace, и, таким образом, будет подключаться только к указанному вами адресу.

![ActiveGate подключается к кластеру Dynatrace через обратный прокси/балансировщик нагрузки](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

В этом сценарии необходимо установить следующие переменные окружения.

## Настройки SSL

### Пользовательский SSL-сертификат

ActiveGate будет предоставлять пользовательский сертификат вместо сертификата по умолчанию. Для настройки вам потребуется файл в формате `PKCS#12`, содержащий закрытый ключ и соответствующую цепочку сертификатов. Дополнительную информацию см. в разделе [Пользовательский SSL-сертификат для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Узнайте, как настроить SSL-сертификат на вашем ActiveGate.").

### Доверенные корневые сертификаты

Дополнительные доверенные корневые сертификаты могут использоваться ActiveGate. Для настройки вам потребуется файл в формате `PEM`, содержащий список сертификатов для включения в хранилище доверия. Дополнительную информацию см. в разделе [Доверенные корневые сертификаты для ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Узнайте, как указать пользовательский файл хранилища доверия, который объединяется с корневыми сертификатами Java и используется по умолчанию для всех соединений.").

### HTTP-порт

Контейнер ActiveGate по умолчанию открывает HTTPS-порт `9999`. Если вам необходимо, чтобы ActiveGate обменивался данными через обычный HTTP, необходимо явно указать HTTP-порт.

## Расширенная настройка

В дополнение к параметрам конфигурации, передаваемым через переменные окружения или файлы, вы можете настроить все остальные [параметры конфигурации](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями."), предоставив содержимое файла `custom.properties`.

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
2. Укажите ссылку на `ConfigMap` в вашем файле развёртывания.

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
