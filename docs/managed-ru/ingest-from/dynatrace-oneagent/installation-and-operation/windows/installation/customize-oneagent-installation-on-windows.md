---
title: Настройка установки OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows
---

# Настройка установки OneAgent на Windows

# Настройка установки OneAgent на Windows

* 9 мин чтения
* Обновлено 21 января 2026 г.

Установщик OneAgent для Windows поставляется и используется как самораспаковывающийся EXE-файл. Установщик также можно извлечь и использовать напрямую, как MSI-пакет. Этот подход обычно применяется при [развёртывании через групповую политику](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Узнайте, как загрузить и установить Dynatrace OneAgent на Windows.").

Установку можно настроить, указав параметры командной строки для отдельных настроек, либо положиться на настройки по умолчанию.
При этом параметры, отмеченные ниже как `environment-specific`, то есть параметры, задающие конечную точку связи, ID окружения и токен:

* обязательны
* предварительно настроены только для EXE-версии установщика.
  Поэтому при использовании установщика в виде MSI-пакета эти параметры нужно указывать явно.

## Передача параметров установки

### Командная строка

Чтобы передать параметры, добавь их к команде установщика, разделяя пробелами.

Например, для EXE-версии установщика:

```
.\Dynatrace-OneAgent-Windows.exe --set-host-group=my_host_group --set-monitoring-mode=infra-only INSTALL_PATH="C:\installdir"
```

При использовании установщика в виде MSI-пакета напрямую можно добавить только параметры `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER` и `SKIP_OS_SUPPORT_CHECK`. Такой тип установки обычно запускается в тихом режиме как часть [развёртывания через групповую политику](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Узнайте, как загрузить и установить Dynatrace OneAgent на Windows."). Параметр `--set-param=<value>` нужно размещать внутри `ADDITIONAL_CONFIGURATION` (`ADDITIONAL_CONFIGURATION="--set-param=<value>"`).  
Подробнее о синтаксисе командной строки см. [Тихая установка](#silent-installation).

### Интерфейс установщика

Параметры `--set-param=<value>` также можно добавить на экране установки **Configure OneAgent settings**.

![настройка OneAgent на windows](https://dt-cdn.net/images/windows-customize-495-ec2f24e000.png)

настройка OneAgent на windows

Параметры, поддерживаемые интерфейсом установщика

Интерфейс установщика OneAgent для Windows поддерживает только параметры `--set-param=<value>`.

Следующие параметры НЕ поддерживаются интерфейсом установщика: `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER` и `SKIP_OS_SUPPORT_CHECK`.

## Удалённые параметры установки

Начиная с версии 1.213 следующие параметры принимаются только при указании в синтаксисе `--set-param=<value>`. Для этих конкретных параметров эквивалентный синтаксис `PARAM=<value>` больше не поддерживается:

| Удалённый параметр `PARAM=<value>` | Новый параметр `--set-param=<value>` |
| --- | --- |
| `SERVER` | `--set-server` |
| `TENANT` | `--set-tenant` |
| `TENANT_TOKEN` | `--set-tenant-token` |
| `PROXY` | `--set-proxy` |
| `HOST_GROUP` | `--set-host-group` |
| `APP_LOG_CONTENT_ACCESS` | `--set-app-log-content-access` |

## Параметры установки MSI

`INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER` и `USER`, это особый тип параметров, соответствующих [синтаксису публичных свойств MSI﻿](https://docs.microsoft.com/en-us/windows/win32/msi/public-properties). Они не заменяются эквивалентными параметрами `--set-param=<value>`. Использовать их можно только в командной строке установщика, но не в интерфейсе установщика.

## Путь установки

**Значение по умолчанию**: `%PROGRAMFILES%\dynatrace\oneagent`

Параметр **`INSTALL_PATH`** позволяет установить OneAgent в выбранный каталог.

Например:  
`.\Dynatrace-OneAgent-Windows.exe INSTALL_PATH="C:\test dir"`

Этот параметр не поддерживается интерфейсом установщика.

Параметр `INSTALL_PATH` не управляет каталогами [файлов журналов и конфигурации](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте структуру каталогов OneAgent и требования к дисковому пространству для установки OneAgent на Windows.") OneAgent. Чтобы настроить путь к журналам, используй параметр `LOG_PATH`.

### Требования к пользовательскому каталогу

Убедись, что пользовательский путь установки соответствует следующим требованиям:

* Каталог должен использоваться только для целей OneAgent. Никакое другое ПО не должно иметь к нему доступ. Причина в безопасности, а также в том, что OneAgent периодически выполняет автоматическую очистку, которая может удалить файлы, созданные другими приложениями.
* Нельзя использовать общий каталог или вкладывать друг в друга каталоги [установки](#installation-path), [хранилища](#data-storage) и [журналов](#log-path).
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть дочерним каталогом `%PROGRAMDATA%\dynatrace`.

## Путь к журналам

**Значение по умолчанию**: `%PROGRAMDATA%\dynatrace\oneagent\log`

Параметр **`LOG_PATH`** позволяет настроить каталог журналов OneAgent.

Например:

`.\Dynatrace-OneAgent-Windows.exe LOG_PATH=C:\dynatrace\logs`

Этот параметр не поддерживается интерфейсом установщика.

### Требования к пользовательскому каталогу

Убедись, что пользовательский путь к журналам соответствует следующим требованиям:

* Каталог должен использоваться только для целей OneAgent. Никакое другое ПО не должно иметь к нему доступ. Причина в безопасности, а также в том, что OneAgent периодически выполняет автоматическую очистку, которая может удалить файлы, созданные другими приложениями.
* Нельзя использовать общий каталог или вкладывать друг в друга каталоги [установки](#installation-path), [хранилища](#data-storage) и [журналов](#log-path).
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть дочерним каталогом `%PROGRAMDATA%\dynatrace`.

### Изменение расположения

Если параметр используется для изменения расположения для уже установленного OneAgent:

* Существующие файлы не переносятся в новое расположение

* После установки или изменения параметра `LOG_PATH` нужно перезапустить процессы с глубоким мониторингом, чтобы отслеживающие их OneAgent могли подхватить новый путь для хранения журналов. Уведомление о необходимости перезапустить соответствующий процесс появится на странице **Process overview**.

## Хранилище данных

OneAgent версии 1.199

**Значение по умолчанию**: `%PROGRAMDATA%\dynatrace\oneagent\datastorage`

Параметр **`DATA_STORAGE`** позволяет определить каталог для хранения больших объёмов runtime-данных, создаваемых OneAgent в режиме full-stack мониторинга, таких как отчёты о сбоях или дампы памяти.

Например:

`.\Dynatrace-OneAgent-Windows.exe DATA_STORAGE=D:\data\dynatrace\runtime`

Этот параметр не поддерживается интерфейсом установщика.

### Требования к пользовательскому каталогу

Убедись, что пользовательский путь к хранилищу данных соответствует следующим требованиям:

* Каталог должен использоваться только для целей OneAgent. Никакое другое ПО не должно иметь к нему доступ. Причина в безопасности, а также в том, что OneAgent периодически выполняет автоматическую очистку, которая может удалить файлы, созданные другими приложениями.
* Нельзя использовать общий каталог или вкладывать друг в друга каталоги [установки](#installation-path), [хранилища](#data-storage) и [журналов](#log-path).
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть дочерним каталогом `%PROGRAMDATA%\dynatrace`.

### Изменение расположения

Если параметр используется для изменения расположения для уже установленного OneAgent:

* Существующие файлы не переносятся в новое расположение

* После установки или изменения параметра `DATA_STORAGE` нужно перезапустить процессы с глубоким мониторингом, чтобы отслеживающие их OneAgent могли подхватить новый путь для хранения runtime-данных. В противном случае дампы памяти и другие runtime-данные не будут сохранены. Уведомление о необходимости перезапустить соответствующий процесс появится на странице **Process overview**.

## Конечная точка связи

**Значение по умолчанию**: `environment specific`

Адрес конечной точки связи OneAgent, компонента Dynatrace, которому OneAgent отправляет данные. В зависимости от развёртывания это может быть Dynatrace Cluster или ActiveGate. Если OneAgent устанавливается через страницу **Deploy** Dynatrace, это значение уже задано корректно. Чтобы изменить его, используй IP-адрес или имя. Номер порта добавляется после двоеточия.

Чтобы задать конечную точку связи, передай её как значение параметра:

```
--set-server=https://100.20.10.1:443
```

OneAgent и Dynatrace Cluster автоматически поддерживают рабочее соединение. Если данные конечной точки меняются, кластер уведомляет OneAgent об изменении, и OneAgent автоматически обновляет конечную точку, заданную через `--set-server`, до нового рабочего значения.

Чтобы изменить конечную точку после установки, используй `--set-server` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять отдельные задачи настройки OneAgent без необходимости переустановки OneAgent.").

## Environment ID

**Значение по умолчанию**: `environment specific`

[ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") Dynatrace, полученный вместе с письмом об активации. При установке OneAgent через страницу **Deploy** Dynatrace это значение уже задано правильно. Если продаётся сервис на базе Dynatrace, эта опция позволяет задать ID клиентов из пула ID, приобретённого у Dynatrace.

Чтобы задать ID окружения, передать его как значение параметра:

```
--set-tenant=mySampleEnv
```

Чтобы изменить tenant после установки, использовать `--set-tenant` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Token

**Значение по умолчанию**: `environment specific`

Tenant token, используемый для аутентификации при подключении OneAgent к endpoint'у связи для отправки данных. При установке OneAgent через страницу **Deploy** Dynatrace это значение уже задано правильно.

Чтобы задать token, передать его как значение параметра:

```
--set-tenant-token=abcdefghij123456
```

О том, как получить token, см. [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.").

Чтобы изменить tenant token после установки, использовать `--set-tenant-token` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Network zones

**Значение по умолчанию**: `unset`

О правилах именования network zone и другой справочной информации см. [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.").

Параметр `--set-network-zone` указывает OneAgent работать через заданную network zone:

```
--set-network-zone=your.network.zone
```

Чтобы изменить или очистить назначение network zone после установки, использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify network zone**).

Также можно использовать `--set-network-zone` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Proxy

**Значение по умолчанию**: `unset`

Адрес прокси-сервера. Использовать IP-адрес или имя, добавив номер порта через двоеточие. Для прокси с аутентификацией можно указать имя пользователя и пароль в формате `username:password@172.1.1.128:8080`, при этом и имя пользователя, и пароль нужно закодировать в URL-кодировке.

Чтобы задать прокси, передать его как значение параметра:

```
--set-proxy=172.1.1.128:8080
```

Dynatrace также поддерживает адреса IPv6.

Чтобы изменить или очистить адрес прокси после установки, использовать `--set-proxy` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Port range

Устарело

Начиная с версии OneAgent 1.301, OneAgent не использует TCP-порты для собственного межпроцессного взаимодействия. Если OneAgent занимает порты приложений, нужно обновить OneAgent до версии 1.301+.

**Значение по умолчанию**: `50000:50100`

Watchdog, это бинарный файл, используемый для запуска и мониторинга процессов мониторинга OneAgent:

* `oneagentos`, мониторинг операционной системы
* `oneagentplugin`, мониторинг с использованием [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`, мониторинг с использованием локальных [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`, [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`, [network monitoring](/managed/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Параметр `--set-watchdog-portrange=<arg>` изменяет диапазон портов прослушивания watchdog на `<arg>`. `<arg>` должен содержать два номера портов, разделённых двоеточием (`:`), например `50000:50100`. Максимальный поддерживаемый диапазон портов, от 1024 до 65535. Диапазон портов должен охватывать минимум 4 порта. Номер порта, начинающий диапазон, должен быть меньше. Например:

```
--set-watchdog-portrange=50000:50100
```

Чтобы изменить диапазон портов после установки, использовать `--set-watchdog-portrange` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#portrange "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Auto-update

Параметр `--set-auto-update-enabled=<arg>` включает или отключает автообновление OneAgent. Например:

```
--set-auto-update-enabled=true
```

После установки параметра в значение `false` управлять автоматическими обновлениями OneAgent через веб-интерфейс Dynatrace в разделе **Settings** > **Deployment** > **OneAgent updates** будет невозможно.

## Host group

**Значение по умолчанию**: `unset`

Имя группы, к которой нужно отнести хост. Подробнее см. [Organize your environment using host groups](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Требования к строке host group:

* Может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки
* Не должна начинаться с `dt.`
* Максимальная длина, 100 символов

Чтобы отнести хост к host group, передать имя host group как значение параметра:

```
--set-host-group=My.HostGroup_123-456
```

Чтобы убрать хост из группы, нужно [удалить OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.") или передать пустое значение `--set-host-group=""` при выполнении обновления OneAgent. Убрать хост из группы с помощью параметра `HOST_GROUP` при обновлении OneAgent нельзя.

Чтобы изменить или очистить назначение host group после установки, использовать [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify host group**).

Также можно использовать `--set-host-group` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Monitoring mode

**Значение по умолчанию**: `fullstack`

Активирует один из режимов мониторинга OneAgent:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

Чтобы включить определённый режим мониторинга, установить параметр `--set-monitoring-mode` в одно из следующих значений:

* `fullstack`
* `infra-only`
* `discovery`

Например:

```
--set-monitoring-mode=infra-only
```

Чтобы изменить режим мониторинга после установки, использовать `--set-monitoring-mode` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#infrastructure-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") или задать его на странице [Host settings](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

## Custom host name

**Значение по умолчанию**: `unset`

Параметр `--set-host-name` переопределяет автоматически определённое имя хоста. Значение имени хоста не должно содержать символы `<`, `>`, `&`, `CR` (возврат каретки) и `LF` (перевод строки), максимальная длина, 256 символов.

Эта команда добавляет пользовательское имя хоста для отображения в UI, но определённое имя хоста при этом не меняется. Подробнее см. [Set custom host names](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

Чтобы задать имя хоста:

```
--set-host-name=myhostname
```

Чтобы изменить имя хоста после установки, использовать `--set-host-name` в [командной строке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Пользовательские метаданные хоста

**Значение по умолчанию**: `unset`

После настройки пользовательские метаданные отображаются в виде набора свойств внизу раздела **Properties and tags** на странице обзора хоста. Значения свойств не должны содержать символ `=` (кроме как в качестве разделителя ключа и значения) и пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключа и значения.

Когда пользовательские метаданные хоста используются для обогащения метрик и другой телеметрии, ключи и значения могут корректироваться для соответствия требованиям нормализации: ключи приводятся к нижнему регистру, неподдерживаемые символы заменяются на подчёркивание (`_`), а ключи или значения, превышающие максимальную длину, обрезаются. В результате обогащённое значение может отличаться от заданного здесь.

Чтобы добавить или изменить свойства хоста:

```
--set-host-property=AppName --set-host-property=Environment=Dev
```

В одной команде можно добавить или изменить несколько свойств.

Чтобы изменить метаданные хоста после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбери действие **modify host properties**).

Также можно использовать `--set-host-property` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Пользовательские теги хоста

**Значение по умолчанию**: `unset`

После настройки теги отображаются вверху раздела **Properties and tags** на странице обзора хоста. Значения свойств не должны содержать символ `=` (кроме как в качестве разделителя ключа и значения) и пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключа и значения.

Чтобы добавить или изменить теги хоста:

```
--set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk
```

В одной команде можно добавить или изменить несколько тегов. Допускается задавать теги с одинаковым ключом, но разными значениями.

Чтобы изменить теги хоста после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбери действие **modify host tags**).

Также можно использовать `--set-host-tag` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Источник host ID

**Значение по умолчанию**: `auto`

Доступно на всех поддерживаемых платформах для OneAgent версии 1.223+. Для OneAgent версии 1.221 и более ранних эта функция поддерживается только для Citrix Virtual Apps and Desktops.

Особенно важно сохранять статичный host ID в динамических виртуальных средах, где хосты пересоздаются ежедневно.

Чтобы **задать источник для генерации host ID**, используй `--set-host-id-source` и укажи одно из предустановленных значений:

* `auto`, позволяет Dynatrace генерировать host ID автоматически
* `ip-addresses`, генерирует host ID на основе IP-адреса хоста
* `mac-addresses`, генерирует host ID на основе MAC-адреса сетевого адаптера хоста
* `fqdn`, генерирует host ID на основе полного доменного имени хоста (FQDN) в формате `host.domain`. Если FQDN не содержит символа точки, вместо этого используется MAC-адрес сетевого адаптера.
* Если отслеживается несколько сред, можно разделить хосты с одинаковыми IP-адресами, MAC-адресами или FQDN, используя для каждой среды отдельное пространство имён. Пространство имён может содержать только буквенно-цифровые символы, дефисы, подчёркивания и точки; максимальная длина составляет 256 символов:

* `ip-addresses;namespace=<namespace>`
* `mac-addresses;namespace=<namespace>`
* `fqdn;namespace=<namespace>`

Например, чтобы задать источник host ID `ip-addresses` и присвоить ему пространство имён `test`, запусти установщик OneAgent со следующим параметром:

```
--set-host-id-source="ip-addresses;namespace=test"
```

Чтобы установить OneAgent на хост Citrix, задай в качестве источника host ID значение `FQDN`:

```
--set-host-id-source="fqdn;namespace=test"
```

## Доступ к системным журналам

OneAgent может загружать системные журналы для диагностики проблем, которые могут быть вызваны условиями в окружении. OneAgent в настоящий момент не загружает журналы Windows, но это может измениться в будущих релизах.

`--set-system-logs-access-enabled=false` отключает доступ к журналам  
`--set-system-logs-access-enabled=true` включает доступ к журналам

Если нужно изменить этот доступ после установки, используй [интерфейс командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent."):

Обрати внимание, что это настройка самодиагностики, которая не связана с [Log Monitoring](#log-monitoring).

## Log Monitoring

**Значение по умолчанию**: `true`

При значении `true` разрешает OneAgent доступ к файлам журналов для целей Log Monitoring. Допустимые значения: (`true`, `false`) или (`1`, `0`).

Также можно включить или отключить эту настройку конфигурации в ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**.

1. Выбери **Install** и **Install OneAgent**.
2. Разверни выпадающий список **Optional parameters**.
3. Включи/выключи опцию **Enable access to application log-file content on this host for problem analysis**.

Например:
`--set-app-log-content-access=true`

Если нужно включить или отключить Log Monitoring после установки, используй `-set-app-log-content-access` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Automatic injection

Не задавай этому параметру значение `true` в процессе установки.

**Значение по умолчанию**: `true`

Параметру `--set-auto-injection-enabled=<arg>` можно задать значение `true` или `false`, чтобы отключить или включить auto-injection OneAgent.

Подробнее см. [Automatic injection](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Локальный приём метрик

**Значение по умолчанию**: `14499`

Параметр `--set-extensions-ingest-port=<arg>` можно использовать для изменения порта, используемого по умолчанию для связи при локальном приёме метрик. Этот порт используется [OneAgent REST API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Scripting integration](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration.") (`dynatrace_ingest`) и [Telegraf](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace.").

Подробнее см. [Metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## Приём метрик StatsD

**Значение по умолчанию**: `18125`

Параметр `--set-extensions-statsd-port=<arg>` можно использовать для изменения порта UDP-прослушивания Dynatrace StatsD, используемого по умолчанию: [DynatraceStatsD](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.") UDP listening port.

Подробнее см. [Metric ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## Пользователь расширения OneAgent

**Значение по умолчанию**: `LocalSystem` (OneAgent версии 1.195+)

Параметр **`USER`** используется, чтобы задать пользователя, от имени которого запускается процесс, отвечающий за функциональность [расширений Dynatrace](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."). Например:

`.\Dynatrace-OneAgent-Windows.exe USER=LocalService`

Этот параметр не поддерживается в UI установщика.

Если параметр `USER` не добавлен:

* Для новых установок OneAgent 1.195+ по умолчанию используется учётная запись `LocalSystem` для запуска расширений OneAgent, но Python-расширения запускаются от имени `LocalService`.
* Для новых развёртываний OneAgent до версии 1.195 OneAgent использует учётную запись `dtuser`.
* При обновлении OneAgent ранее настроенная учётная запись пользователя сохраняется. Чтобы изменить её, нужно переустановить OneAgent, задав параметру `USER` новое значение.

Параметр `USER` может принимать одно из следующих значений:

* Рекомендуется `LocalSystem`, учётная запись пользователя по умолчанию для запуска расширений OneAgent начиная с версии OneAgent 1.195. Применяется автоматически, если параметр `USER` не используется. Это значение параметра заставляет OneAgent использовать привилегированную системную учётную запись `NT AUTHORITY\SYSTEM` для запуска расширений OneAgent. По сути, локальная учётная запись пользователя не создаётся. В результате все модули OneAgent, включая все расширения, кроме Python-расширений, полностью функциональны. Python-расширения запускаются от имени `LocalService`.
* `LocalService`: это значение параметра заставляет OneAgent использовать системную учётную запись `NT AUTHORITY\LOCAL SERVICE` для запуска расширений OneAgent. Хотя такого урезанного набора привилегий достаточно для работы большинства расширений, есть те, которые не смогут эффективно собирать данные (а именно расширения, собирающие счётчики Performance Monitor, такие как расширения MS SQL или .NET). Если неясно, какие расширения понадобятся, лучше использовать значение параметра `LocalSystem`.
* Устарело `no_create` отключало создание пользователя при установке OneAgent до версии OneAgent 1.209. Начиная с версии 1.209, при использовании параметра `no_create` установщик OneAgent применяет параметр `LocalSystem` без каких-либо предупреждений. Настройка `no_create` не преобразуется в `LocalSystem` для существующих установок при выполнении обновления. Чтобы выполнить преобразование, нужно переустановить OneAgent, задав параметру `USER` новое значение.
* Устарело `dtuser` была учётной записью пользователя по умолчанию для запуска расширений OneAgent до версии OneAgent 1.195. Она заставляла установщик создавать в системе локальную учётную запись пользователя с таким же именем. Начиная с версии 1.209, при использовании параметра `dtuser` установщик OneAgent применяет параметр `LocalSystem` без каких-либо предупреждений. Начиная с OneAgent версии 1.239, настройка `dtuser` преобразуется в `LocalSystem` для существующих установок при выполнении обновления.

При развёртывании Dynatrace на Windows Server Domain Controller нужно убедиться, что параметру `USER` задано значение `LocalSystem`, либо, как альтернатива, `LocalService`, чтобы избежать распространения `dtuser` по домену, что может привести к конфликту с существующими учётными записями `dtuser` на хостах, где установлен Dynatrace.

## Тихая установка

При использовании режима тихой установки установщик OneAgent должен быть предварительно настроен с соответствующими значениями параметров, поскольку интерактивные диалоги и запросы во время установки не отображаются.

Параметры, зависящие от окружения, предварительно настроены только для EXE-версии установщика. При использовании установщика в виде MSI-пакета все эти параметры нужно указывать самостоятельно.

### MSI-пакет, тихая установка

Чтобы настроить тихую установку из командной строки при использовании MSI-пакета, добавьте `/quiet /qn`, как в этих примерах:

#### Command shell

```
msiexec /i C:\some\path\Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-server=https://someserver.com --set-tenant=xxx --set-tenant-token=xxx --set-host-group=myGroup" /quiet /qn
```

#### PowerShell 3.0+

```
msiexec /i C:\some\path\Dynatrace-OneAgent-Windows.msi --% ADDITIONAL_CONFIGURATION="--set-server=https://someserver.com --set-tenant=xxx --set-tenant-token=xxx --set-host-group=myGroup" /quiet /qn
```

Обратите внимание на символ остановки разбора `--%`, используемый в команде PowerShell.

### EXE-установщик, тихая установка

Чтобы настроить тихую установку из командной строки для EXE-версии установщика, добавьте `--quiet`, как в этом примере:

```
.\Dynatrace-OneAgent-Windows.exe --set-host-group="myGroup" --quiet
```

## Драйвер захвата пакетов (pcap)

OneAgent версии 1.229+

Параметр `PCAP_DRIVER` позволяет указать, какой драйвер захвата пакетов будет установлен и использован для сбора сетевых метрик.

Пример:

```
.\Dynatrace-OneAgent-Windows.exe PCAP_DRIVER=npcap
```

**Значение по умолчанию**: `npcap`

**Возможные значения:**

| Значение | Описание |
| --- | --- |
| `npcap` | `PCAP_DRIVER=npcap` устанавливает драйвер `Npcap`.  Этот вариант удаляет любую установку WinPcap или устаревшего Npcap, ранее установленного OneAgent. Однако, если WinPcap или Npcap был установлен вручную, его нужно удалить самостоятельно. |
| `winpcap` | `PCAP_DRIVER=winpcap` устанавливает драйвер `WinPcap`.  Этот вариант **НЕ** удаляет и не перекрывает никакую существующую установку `Npcap` или `WinPcap`. |
| `auto` | Устарело с версии OneAgent 1.255+  `PCAP_DRIVER=auto` автоматически определяет, какой драйвер устанавливать. Этот вариант **НЕ** удаляет и не перекрывает никакую существующую установку `Npcap` или `WinPcap`. Во время установки, если драйвер захвата пакетов не найден, по умолчанию устанавливается `Npcap`. |
| `disabled` | Доступно с версии OneAgent 1.249+  `PCAP_DRIVER=disabled` отключает установку любого драйвера захвата пакетов и отключает модуль сетевого мониторинга OneAgent. Если на хосте уже установлен какой-либо драйвер захвата пакетов, его нужно удалить вручную. |

* Этот параметр не поддерживается в веб-UI установщика.
* Значение этого параметра сохраняется при обновлениях.
* Если во время установки OneAgent устанавливается `Npcap`, установщик создаёт запланированную задачу с названием `npcapwatchdog`.

  + Эта задача обеспечивает корректную работу драйвера `Npcap` после обновлений функций Windows. Задача выполняется в фоновом режиме и не влияет на производительность или функциональность системы.
  + Хотя задача `npcapwatchdog` предназначена для предотвращения проблем с обновлениями Windows, её можно удалить. Однако, если она удалена, драйвер Npcap может потребоваться переустановить перед повторным использованием.

Дополнительные сведения см.:

* [Безопасность OneAgent в Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows#installation "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")
* [Установка OneAgent в Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#winpcapuninstall "Learn how to download and install Dynatrace OneAgent on Windows.")

## Пропуск проверки поддержки операционной системы

Если задать этому параметру значение `true`, это позволит установить OneAgent на иначе неподдерживаемой платформе. Dynatrace не несёт ответственности за подобные установки.

Этот параметр не поддерживается в UI установщика.

Этот параметр не сохраняется при автоматических обновлениях.

Информацию об автоматическом механизме обновления OneAgent см. в [Обновление Dynatrace OneAgent в Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.").

**Значение по умолчанию**: `false`

Параметр **`SKIP_OS_SUPPORT_CHECK`** позволяет принудительно установить OneAgent на иначе неподдерживаемой платформе.

Например:
`.\Dynatrace-OneAgent-Windows.exe SKIP_OS_SUPPORT_CHECK=true`

Список поддерживаемых платформ см. в [Поддержка технологий](/managed/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.").