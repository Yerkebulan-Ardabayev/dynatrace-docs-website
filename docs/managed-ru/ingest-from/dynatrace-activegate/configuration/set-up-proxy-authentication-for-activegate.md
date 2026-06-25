---
title: Прокси для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate
scraped: 2026-05-12T11:27:38.311343
---

# Прокси для ActiveGate

# Прокси для ActiveGate

* 5-min read
* Updated on Apr 21, 2026

Конфигурация подключения ActiveGate позволяет определить один или несколько прокси для исходящих соединений: можно использовать [единый прокси для всего исходящего трафика](#proxy-for-cluster-aws-vmware-azure) или задать **разные прокси для разных целей**, либо **отключить использование прокси для отдельных соединений**, сохранив его для других.

Подробнее о конфигурации в более широком контексте смотрите в разделе [Поддерживаемые схемы подключения](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").

## Свойства конфигурации прокси

Конфигурация прокси ActiveGate включает следующие параметры:

| Свойство | Описание |
| --- | --- |
| `proxy-server` | Адрес сервера (имя хоста или IP-адрес) |
| `proxy-port` | Порт (необязательный; по умолчанию `8080`) |
| `proxy-scheme` | Схема (необязательный; по умолчанию `http`). Для прокси, не поддерживающих HTTP, необходимо установить `https`. |
| `proxy-user` | Имя пользователя (необязательный) |
| `proxy-domain` | Домен пользователя (для NTLM-аутентификации) |
| `proxy-password` | Пароль (необязательный). После перезапуска ActiveGate обфусцируется и сохраняется в `proxy-password-encr`. Если запятая входит в значение, перед ней необходим экранирующий символ `\`. |
| `proxy-off` | При значении `true` отключает прокси для конкретного типа связи. |
| `proxy-non-proxy-hosts` | Список хостов для прямого подключения без прокси. Хосты разделяются символом `|`, допускается маска `*`. Пример: `proxy-non-proxy-hosts=*.foo.com|localhost`. ActiveGate версии 1.335+: поддерживается нотация CIDR для `cloudfoundry_monitoring` и `kubernetes_monitoring`. |
| `proxy-authentication-schemes` | ActiveGate версии 1.271+. Приоритетный список схем аутентификации прокси (`NTLM`, `BASIC`). |

## Указание конфигурации прокси для ActiveGate

Конфигурация прокси может быть задана во время установки ActiveGate на [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#linux_proxy "Узнайте о параметрах командной строки для ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#windows_proxy "Узнайте о параметрах для ActiveGate на Windows."), или после установки.

agctl

custom.properties

ActiveGate версии 1.333+

Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#property "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для настройки свойств прокси в разделе `http.client`:

```
# Установить адрес и порт прокси
agctl property set --section=http.client --key=proxy-server --value=127.0.0.1
agctl property set --section=http.client --key=proxy-port --value=8080

# Учётные данные аутентификации (если необходимо)
agctl property set --section=http.client --key=proxy-user --value=username
agctl property set --section=http.client --key=proxy-password --value=password
```

После настройки необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.").

Через `custom.properties`:

1. Отредактируйте файл `custom.properties` [в директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate.").
2. Укажите параметры прокси в соответствующем разделе:

   ```
   [http.client]
   proxy-server=127.0.0.1
   proxy-port=8080
   proxy-user=username
   proxy-password=password
   ```

3. Сохраните файл и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.").

## Простые сценарии конфигурации прокси ActiveGate

### Прокси для всего исходящего трафика

Наиболее распространённый случай: укажите параметры прокси в разделе `[http.client]` — они применяются как для связи с кластером Dynatrace, так и для мониторинга AWS, VMware, Azure.

agctl:

```
agctl property set --section=http.client --key=proxy-server --value=127.0.0.1
agctl property set --section=http.client --key=proxy-port --value=8080
```

custom.properties:

```
[http.client]
proxy-server=127.0.0.1
proxy-port=8080
proxy-user=username
proxy-password=password
```

### Прокси только для кластера Dynatrace

Для настройки прокси исключительно для кластера Dynatrace при прямом подключении к мониторируемым технологиям задайте параметры в разделе `[http.client.internal]`:

agctl:

```
agctl property set --section=http.client.internal --key=proxy-server --value=127.0.0.1
agctl property set --section=http.client.internal --key=proxy-port --value=8080
```

custom.properties:

```
[http.client.internal]
proxy-server=127.0.0.1
proxy-port=8080
```

### Прокси для мониторингового трафика при прямом подключении к кластеру

Укажите параметры прокси в `[http.client]`, а в `[http.client.internal]` отключите прокси:

agctl:

```
agctl property set --section=http.client --key=proxy-server --value=127.0.0.1
agctl property set --section=http.client --key=proxy-port --value=8080
agctl property set --section=http.client.internal --key=proxy-off --value=true
```

custom.properties:

```
[http.client]
proxy-server=127.0.0.1
proxy-port=8080
proxy-user=username
proxy-password=password

[http.client.internal]
proxy-off=true
```

## Расширенные сценарии конфигурации прокси ActiveGate

В зависимости от раздела конфигурации, в котором указаны свойства, прокси (и другие параметры связи) применяются только к выбранным типам соединений:

* `[http.client]` — настройки прокси для всех исходящих соединений ActiveGate (кластер Dynatrace и все мониторируемые технологии).
* `[http.client.internal]` — настройки специально для связи с кластером Dynatrace. Переопределяют `[http.client]`.
* `[http.client.external]` — настройки для CloudFoundry, Kubernetes, частного синтетического мониторинга. Переопределяют `[http.client]`.
* `[<имя технологии>]` — настройки для конкретной мониторируемой технологии: `cloudfoundry_monitoring`, `kubernetes_monitoring`, `synthetic`. Переопределяют `[http.client]` и `[http.client.external]`.

### Прокси для Kubernetes, CloudFoundry и частного синтетического мониторинга

agctl:

```
agctl property set --section=http.client.external --key=proxy-server --value=127.0.0.1
agctl property set --section=http.client.external --key=proxy-port --value=8080
```

custom.properties:

```
[http.client.external]
proxy-server=127.0.0.1
proxy-port=8080
proxy-user=username
proxy-password=password
```

### Разные прокси для Kubernetes, CloudFoundry и частного синтетического мониторинга

Укажите отдельные параметры прокси в разделах:

* CloudFoundry: `cloudfoundry_monitoring`
* Kubernetes: `kubernetes_monitoring`
* Частный синтетический мониторинг: `synthetic`

agctl (пример для Kubernetes):

```
agctl property set --section=kubernetes_monitoring --key=proxy-server --value=127.0.0.1
agctl property set --section=kubernetes_monitoring --key=proxy-port --value=8080
```

Смотрите также: [Настройка прокси ActiveGate для частного синтетического мониторинга](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для установки прокси для частного синтетического мониторинга.")