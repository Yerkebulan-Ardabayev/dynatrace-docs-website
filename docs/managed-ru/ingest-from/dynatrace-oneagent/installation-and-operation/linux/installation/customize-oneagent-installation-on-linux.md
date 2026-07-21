---
title: Настройка установки OneAgent в Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux
---

# Настройка установки OneAgent в Linux

# Настройка установки OneAgent в Linux

* Чтение: 7 мин
* Опубликовано 19 сент. 2018 г.

Установщик для Linux можно запускать с параметрами командной строки, если настройки по умолчанию не подходят. Все параметры, перечисленные ниже, необязательны.

## Передача параметров установки

Чтобы передать параметры, добавь их к команде установщика через пробел.

Например:

```
Dynatrace-OneAgent-Linux.sh --set-host-group=my_host_group --set-monitoring-mode=infra-only
```

## Удалённые параметры установки

Нужно перейти на новые параметры `--set-param=<value>`. Эквивалентные параметры `PARAM=<value>` больше не поддерживаются установщиком OneAgent начиная с версии 1.213.

| Удалённый параметр `PARAM=<value>` | Новый параметр `--set-param=<value>` |
| --- | --- |
| `SERVER` | `--set-server` |
| `TENANT` | `--set-tenant` |
| `TENANT_TOKEN` | `--set-tenant-token` |
| `PROXY` | `--set-proxy` |
| `HOST_GROUP` | `--set-host-group` |
| `APP_LOG_CONTENT_ACCESS` | `--set-app-log-content-access` |
| `DISABLE_SYSTEM_LOGS_ACCESS` | `--set-system-logs-access-enabled` |

При одновременном использовании эквивалентных настроек `PARAM=<value>` и `--set-param=<value>` настройка `--set-param=<value>` переопределяет `PARAM=<value>`.

## Путь установки

**Значение по умолчанию**: `/opt/dynatrace/oneagent`

**Предварительное условие**: при использовании этого параметра с включённым SELinux в системе должна быть доступна утилита semanage.

Параметр **`INSTALL_PATH`** позволяет установить OneAgent в другой каталог. Например:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh INSTALL_PATH=/data/dynatrace/agent
```

Установщик создаёт символическую ссылку `/opt/dynatrace/oneagent` > `/data/dynatrace/agent`, а файлы установки OneAgent размещаются в указанном каталоге (в этом примере, `/data/dynatrace/agent`). Обрати внимание: эту символическую ссылку нужно удалить вручную после удаления OneAgent.

Параметр `INSTALL_PATH` не управляет каталогами [журналов и конфигурационных файлов](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Узнай про структуру каталогов OneAgent и требования к дисковому пространству для установки OneAgent в Linux.") OneAgent. Чтобы настроить путь для журналов, используй параметр `LOG_PATH`.

Кроме того, пути установки по умолчанию не должны быть символическими ссылками. В частности, `/var/lib/dynatrace` изменять нельзя, за исключением части `/var/lib/dynatrace/oneagent/datastorage`, которую можно изменить с помощью опции `DATA_STORAGE`.

Каталог установки

ActiveGate и OneAgent, установленные на одном хосте, **не должны** использовать один и тот же каталог установки.

### Требования к произвольному каталогу

Убедись, что путь произвольного каталога установки соответствует следующим требованиям:

* Каталог должен использоваться исключительно для нужд OneAgent. Никакое другое ПО не должно иметь к нему доступ. Причина в том числе в безопасности, а также в автоматической очистке, периодически выполняемой OneAgent, которая может удалить файлы, созданные другими приложениями.
* Каталоги [установки](#installation-path), [хранилища](#data-storage) и [журналов](#log-path) не должны совпадать друг с другом или быть вложенными друг в друга.
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть уже существующей символической ссылкой.
* Значение не должно быть дочерним каталогом `/var/lib/dynatrace`.

## Путь для журналов

**Значение по умолчанию**: `/var/log/dynatrace/oneagent`

**Предварительное условие**: при использовании этого параметра с включённым SELinux в системе должна быть доступна утилита semanage.

Параметр **`LOG_PATH`** позволяет настроить каталог журналов OneAgent. Например:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh LOG_PATH=/data/dynatrace/logs
```

### Требования к произвольному каталогу

Убедись, что путь произвольного каталога журналов соответствует следующим требованиям:

* Каталог должен использоваться исключительно для нужд OneAgent. Никакое другое ПО не должно иметь к нему доступ. Причина в том числе в безопасности, а также в автоматической очистке, периодически выполняемой OneAgent, которая может удалить файлы, созданные другими приложениями.
* Каталоги [установки](#installation-path), [хранилища](#data-storage) и [журналов](#log-path) не должны совпадать друг с другом или быть вложенными друг в друга.
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть уже существующей символической ссылкой.
* Значение не должно быть дочерним каталогом `/var/lib/dynatrace`.

* Не следует использовать `/opt/dynatrace/oneagent/log`, поскольку это расположение журналов по умолчанию для версий OneAgent раньше 1.203.

### Изменение расположения

Если параметр используется для изменения расположения уже установленного OneAgent:

* Существующие файлы не переносятся в новое расположение

* После установки или изменения параметра `LOG_PATH` нужно перезапустить процессы с глубоким мониторингом, чтобы отслеживающие их OneAgent могли применить новый путь для хранения журналов. Уведомление о необходимости перезапустить соответствующий процесс появится на странице **Process overview**.

## Хранилище данных

OneAgent версии 1.199

**Значение по умолчанию**: `/var/lib/dynatrace/oneagent/datastorage`

**Предварительное условие**: при использовании этого параметра с включённым SELinux в системе должна быть доступна утилита semanage.

Параметр **`DATA_STORAGE`** позволяет задать каталог, предназначенный для хранения больших объёмов runtime-данных, создаваемых OneAgent в режиме полного мониторинга (full-stack monitoring), таких как отчёты о сбоях или дампы памяти.
Например:

`/bin/sh Dynatrace-OneAgent-Linux.sh DATA_STORAGE=/data/dynatrace/runtime`

## Конечная точка связи

**Значение по умолчанию**: `зависит от среды`

Адрес конечной точки связи OneAgent, компонента Dynatrace, которому OneAgent отправляет данные. В зависимости от развёртывания это может быть Dynatrace Cluster или ActiveGate. Если OneAgent устанавливается со страницы **Deploy** Dynatrace, это значение уже задано корректно. Чтобы изменить его, используй IP-адрес или имя. Номер порта добавляется после двоеточия.

Чтобы задать конечную точку связи, передай её как значение параметра:

```
--set-server=https://100.20.10.1:443
```

OneAgent и Dynatrace Cluster автоматически поддерживают рабочее соединение. Если реквизиты конечной точки меняются, кластер уведомляет об этом OneAgent, и OneAgent автоматически обновляет конечную точку, заданную через `--set-server`, на новое рабочее значение.

Чтобы изменить конечную точку после установки, используй `--set-server` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.").

## ID Environment

**Значение по умолчанию**: `зависит от среды`

[ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнай, что такое среда мониторинга Dynatrace, как найти ID своей среды, а также как настроить и подключить несколько сред.") Dynatrace, полученный в письме об активации. Если OneAgent устанавливается со страницы **Deploy** Dynatrace, это значение уже задано корректно. Если продаются сервисы на базе Dynatrace, используй эту опцию, чтобы задавать ID клиентов из пула ID, приобретённого у Dynatrace.

Чтобы задать ID окружения, передай его как значение параметра:

```
--set-tenant=mySampleEnv
```

Чтобы изменить tenant после установки, используй `--set-tenant` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.").

## Токен

**Значение по умолчанию**: `зависит от среды`

Токен tenant, используемый для аутентификации при подключении OneAgent к конечной точке связи для отправки данных. Если OneAgent устанавливается со страницы **Deploy** Dynatrace, это значение уже задано корректно.

Чтобы задать токен, передай его как значение параметра:

```
--set-tenant-token=abcdefghij123456
```

О том, как получить токен, читай в разделе [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнай, что такое токен tenant и как его изменить.").

Чтобы изменить токен tenant после установки, используй `--set-tenant-token` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.").

## Сетевые зоны

**Значение по умолчанию**: `не задано`

О правилах именования сетевых зон и другой справочной информации читай в разделе [Network zones](/managed/manage/network-zones "Узнай, как работают сетевые зоны в Dynatrace.").

Используй параметр `--set-network-zone`, чтобы указать OneAgent взаимодействовать через определённую сетевую зону:

```
--set-network-zone=your.network.zone
```

Чтобы изменить или сбросить назначение сетевой зоны после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Выполняй конфигурацию OneAgent и ActiveGate на хостах со страницы Deployment status или в массовом режиме с помощью Dynatrace API.") (выбери действие **modify network zone**).

Также можно использовать `--set-network-zone` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#nz "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.").

## Прокси

**Значение по умолчанию**: `unset`

Адрес прокси-сервера. Используется IP-адрес или имя, а после двоеточия указывается номер порта. Для прокси с аутентификацией можно указать имя пользователя и пароль в формате `username:password@172.1.1.128:8080`, где и имя пользователя, и пароль должны быть в URL-кодировке.

Чтобы настроить прокси, передай его как значение параметра:

```
--set-proxy=172.1.1.128:8080
```

Dynatrace также поддерживает адреса IPv6.

Чтобы изменить или очистить адрес прокси после установки, используй `--set-proxy` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Диапазон портов

Устарело

Начиная с версии OneAgent 1.301, OneAgent не использует TCP-порты для собственного межпроцессного взаимодействия. Если OneAgent занимает порты приложений, нужно обновить OneAgent до версии 1.301 и выше.

**Значение по умолчанию**: `50000:50100`

Watchdog, это бинарный файл, используемый для запуска и мониторинга процессов мониторинга OneAgent:

* `oneagentos`, мониторинг операционной системы
* `oneagentplugin`, мониторинг с использованием [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`, мониторинг с использованием локальных [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`, [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`, [мониторинг сети](/managed/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Используй параметр `--set-watchdog-portrange=<arg>`, чтобы изменить диапазон портов прослушивания watchdog на `<arg>`. В `<arg>` нужно указать два номера портов, разделённых двоеточием (`:`), например `50000:50100`. Максимально поддерживаемый диапазон портов: от 1024 до 65535. Диапазон портов должен охватывать не менее 4 портов. Номер порта, с которого начинается диапазон, должен быть меньше. Например:

```
--set-watchdog-portrange=50000:50100
```

Чтобы изменить диапазон портов после установки, используй `--set-watchdog-portrange` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#portrange "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Автообновление

Используй `--set-auto-update-enabled=<arg>`, чтобы включить или отключить автообновление OneAgent. Например:

```
--set-auto-update-enabled=true
```

После того как параметр установлен в `false`, управлять автоматическими обновлениями OneAgent через веб-интерфейс Dynatrace на странице **Settings** > **Deployment** > **OneAgent updates** будет нельзя.

## Host group

**Значение по умолчанию**: `unset`

Имя группы, к которой нужно отнести хост. Подробности см. в разделе [Организация окружения с помощью host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."). Требования к строке host group:

* Может содержать только буквенно-цифровые символы, дефисы, подчёркивания и точки
* Не должна начинаться с `dt.`
* Максимальная длина, 100 символов

Чтобы отнести хост к host group, передай имя host group как значение параметра:

```
--set-host-group=My.HostGroup_123-456
```

Чтобы убрать хост из группы, нужно [удалить OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.") или передать пустое значение `--set-host-group=""` при выполнении обновления OneAgent. Убрать хост из группы с помощью параметра `HOST_GROUP` при обновлении OneAgent нельзя.

Чтобы изменить или очистить привязку к host group после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбери действие **modify host group**).

Также можно использовать `--set-host-group` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Режим мониторинга

**Значение по умолчанию**: `fullstack`

Активирует один из режимов мониторинга OneAgent:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

Чтобы включить определённый режим мониторинга, установи параметр `--set-monitoring-mode` в одно из следующих значений:

* `fullstack`
* `infra-only`
* `discovery`

Например:

```
--set-monitoring-mode=infra-only
```

Чтобы изменить режим мониторинга после установки, используй `--set-monitoring-mode` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#infrastructure-monitoring "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") или настрой его на странице [Host settings](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

## Пользовательское имя хоста

**Значение по умолчанию**: `unset`

Используй `--set-host-name`, чтобы переопределить автоматически определённое имя хоста. Значение имени хоста не должно содержать символы `<`, `>`, `&`, `CR` (возврат каретки) и `LF` (перевод строки), максимальная длина, 256 символов.

Эта команда добавляет пользовательское имя хоста для отображения в UI, но определённое имя хоста при этом не меняется. Подробности см. в разделе [Настройка пользовательских имён хостов](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

Чтобы задать имя хоста:

```
--set-host-name=myhostname
```

Чтобы изменить имя хоста после установки, используй `--set-host-name` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Пользовательские метаданные хоста

**Значение по умолчанию**: `unset`

После настройки пользовательские метаданные отображаются в виде набора свойств внизу раздела **Properties and tags** на странице обзора хоста. Значения свойств не должны содержать символ `=` (кроме как разделитель ключ-значение) и пробельные символы. Максимальная длина, 256 символов, включая разделитель ключ-значение.

Когда пользовательские метаданные хоста используются для обогащения метрик и прочей телеметрии, ключи и значения могут корректироваться для соответствия требованиям нормализации: ключи приводятся к нижнему регистру, неподдерживаемые символы заменяются на подчёркивание (`_`), а ключи или значения, превышающие максимальную длину, обрезаются. В результате обогащённое значение может отличаться от того, что задано здесь.

Чтобы добавить или изменить свойства хоста:

```
--set-host-property=AppName --set-host-property=Environment=Dev
```

В одной команде можно добавить или изменить несколько свойств.

Чтобы изменить метаданные хоста после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбери действие **modify host properties**).

Также можно использовать `--set-host-property` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Пользовательские теги хоста

**Значение по умолчанию**: `unset`

После настройки теги отображаются вверху раздела **Properties and tags** на странице обзора хоста. Значения свойств не должны содержать символ `=` (кроме как разделитель ключ-значение) и пробельные символы. Максимальная длина, 256 символов, включая разделитель ключ-значение.

Чтобы добавить или изменить теги хоста:

```
--set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk
```

В одной команде можно добавить или изменить несколько тегов. Допускается определять теги с одинаковым ключом, но разными значениями.

Чтобы изменить теги хоста после установки, используй [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбери действие **modify host tags**).

Также можно использовать `--set-host-tag` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Источник ID хоста

**Значение по умолчанию**: `auto`

Доступно на всех поддерживаемых платформах для OneAgent версии 1.223+. Для OneAgent версии 1.221 и более ранних эта функция поддерживается только для Citrix Virtual Apps and Desktops.

Особенно важно поддерживать статичный ID хоста в динамических виртуальных средах, где хосты пересоздаются ежедневно.

Чтобы **задать источник генерации ID хоста**, используй `--set-host-id-source` и укажи одно из предопределённых значений:

* `auto`, предоставить Dynatrace генерировать ID хоста автоматически
* `ip-addresses`, генерировать ID хоста на основе IP-адреса хоста
* `mac-addresses`, генерировать ID хоста на основе MAC-адреса сетевого адаптера хоста
* `fqdn`, генерировать ID хоста на основе полного доменного имени хоста (FQDN) в формате `host.domain`. Если FQDN не содержит символа точки, вместо него используется MAC-адрес сетевого адаптера.
* Если отслеживается несколько сред, можно разделить хосты с одинаковыми IP-адресами, MAC-адресами или FQDN, используя для каждой среды отдельное пространство имён. Пространство имён может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки; максимальная длина, 256 символов:

* `ip-addresses;namespace=<namespace>`
* `mac-addresses;namespace=<namespace>`
* `fqdn;namespace=<namespace>`

Например, чтобы задать источник ID хоста как `ip-addresses` и присвоить его пространству имён `test`, запусти установщик OneAgent со следующим параметром:

```
--set-host-id-source="ip-addresses;namespace=test"
```

Чтобы установить OneAgent на хост Citrix, задай источник ID хоста как `FQDN`:

```
--set-host-id-source="fqdn;namespace=test"
```

### Требования к пользовательскому каталогу

Нужно убедиться, что пользовательский путь хранения данных отвечает следующим требованиям:

* Каталог должен быть выделен исключительно для нужд OneAgent. Никакое другое ПО не должно иметь к нему доступа. Одна причина, это безопасность, другая, периодическая автоматическая очистка, выполняемая OneAgent, которая может удалить файлы, созданные другими приложениями.
* Нельзя использовать совместно или вкладывать друг в друга каталоги [установки](#installation-path), [хранения](#data-storage) и [логов](#log-path).
* Значение должно быть абсолютным путём и не должно указывать на корневой каталог тома.

* Значение не должно быть уже существующей символической ссылкой.
* Значение не должно быть дочерним каталогом `/var/lib/dynatrace`.

### Изменение расположения

Если используется параметр для изменения расположения уже установленного OneAgent:

* Существующие файлы не переносятся в новое расположение

* После задания или изменения параметра `DATA_STORAGE` нужно перезапустить процессы с глубоким мониторингом, чтобы отслеживающие их OneAgent смогли получить новый путь для хранения runtime-данных. В противном случае дампы памяти и другие runtime-данные не будут сохраняться. На странице **Process overview** появится уведомление о необходимости перезапуска соответствующего процесса.

## Доступ к системным логам

**Значение по умолчанию**: `true`

OneAgent загружает системные логи Linux для диагностики проблем, которые могут быть вызваны условиями в среде. Подробнее см. [Системные логи, загружаемые OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#system-logs "Узнай о безопасности Dynatrace OneAgent и изменениях, вносимых в систему на базе Linux").

Чтобы отключить доступ к логам:

```
--set-system-logs-access-enabled=false
```

Чтобы включить доступ к логам:

```
--set-system-logs-access-enabled=true
```

Если нужно изменить этот доступ после установки, используй [интерфейс командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнай, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent."):

Обрати внимание, что это настройка самодиагностики, не связанная с [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнай, как включить Log Monitoring, какие данные предоставляет Log Monitoring, и многое другое.").

## Log Monitoring

**Значение по умолчанию**: `true`

При значении `true` разрешает OneAgent доступ к файлам логов для целей Log Monitoring. Допустимые значения: (`true`, `false`) или (`1`, `0`).

Также можно включить или отключить эту настройку в ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**.

1. Выбери **Install** и укажи **Install OneAgent**.
2. Разверни выпадающий список **Optional parameters**.
3. Включи/отключи опцию **Enable access to application log-file content on this host for problem analysis**.

Например:
`--set-app-log-content-access=true`

Если нужно включить или отключить Log Monitoring после установки, используй `-set-app-log-content-access` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнай, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.").

## Автоматическое внедрение

Не устанавливай этот параметр в `true` во время процесса установки.

**Значение по умолчанию**: `true`

Можно задать параметр `--set-auto-injection-enabled=<arg>` в `true` или `false`, чтобы отключить или включить авто-внедрение OneAgent.

Подробнее см. [Автоматическое внедрение](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Узнай, как выполнить некоторые задачи настройки OneAgent без необходимости переустановки OneAgent.").

## Локальный приём метрик

**Значение по умолчанию**: `14499`

Можно использовать параметр `--set-extensions-ingest-port=<arg>`, чтобы изменить порт связи по умолчанию, используемый для локального приёма метрик. Этот порт используется [OneAgent REST API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используй Dynatrace API для получения метрик отслеживаемых сущностей."), [Scripting integration](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнай, как принимать метрики с помощью локальной интеграции скриптов.") (`dynatrace_ingest`) и [Telegraf](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Принимай метрики Telegraf в Dynatrace.").

Подробнее см. [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнай, как расширить наблюдаемость метрик в Dynatrace.").

## Приём метрик StatsD

**Значение по умолчанию**: `18125`

Можно использовать параметр `--set-extensions-statsd-port=<arg>`, чтобы изменить порт прослушивания UDP по умолчанию для [DynatraceStatsD](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Принимай метрики в Dynatrace с помощью OneAgent и клиента ActiveGate StatsD.").

Подробнее см. [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнай, как расширить наблюдаемость метрик в Dynatrace.").

## Непривилегированный режим

### **`NON_ROOT_MODE`**

**Значение по умолчанию**: `1` (OneAgent версии 1.193+. Для более ранних версий, `0`)

При установке OneAgent в непривилегированном режиме повышенные привилегии нужно предоставлять OneAgent только во время установки. Повышенные привилегии сбрасываются сразу после развёртывания OneAgent.

Начиная с версии 1.193, OneAgent устанавливается в непривилегированном режиме по умолчанию. Существующие установки не переключаются в непривилегированный режим автоматически.

Чтобы переключить установленный OneAgent в непривилегированный режим, нужно вручную добавить параметр `NON_ROOT_MODE=1` к команде установки. Пример:
`sudo /bin/sh Dynatrace-Agent-Linux-1.0.0.sh NON_ROOT_MODE=1`  
Чтобы вернуть установщик к режиму по умолчанию для последующих обновлений, запусти его с `NON_ROOT_MODE=0`.

Обрати внимание, что непривилегированный режим требует возможностей ядра Linux (kernel capabilities), доступных в следующих версиях:

* Версия ядра Linux 2.6.26+ для установки OneAgent без root-привилегий.
* Версия ядра Linux 4.3+ (рекомендуется systemd версии 221+) для автоматических обновлений OneAgent и полноценной работы без root-привилегий.
  Подробнее см. [Непривилегированный режим Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнай, когда Dynatrace OneAgent требует root-привилегии в Linux.")

### **`DISABLE_ROOT_FALLBACK`**

**Значение по умолчанию**: `0`

Используется совместно с параметром `NON_ROOT_MODE`, чтобы заблокировать уровень прав суперпользователя для OneAgent, работающего в непривилегированном режиме. Root-привилегии требуются для автоматических обновлений и отдельных операций на версиях ядра между 2.6.26 и 4.3, то есть версиях без поддержки Linux ambient capabilities.

`sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh NON_ROOT_MODE=1 DISABLE_ROOT_FALLBACK=1`

Чтобы вернуть установщик к использованию уровня прав суперпользователя для последующих обновлений, запусти его с `DISABLE_ROOT_FALLBACK=0`.

Подробнее см. [требования к правам для установки и работы OneAgent в Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнай, когда Dynatrace OneAgent требует root-привилегии в Linux.").

* Процесс удаления не удаляет непривилегированного пользователя из системы (независимо от того, `dtuser` это или указан параметром `USER`).
* Непривилегированное `username` сохраняется при обновлениях, если только при обновлении не указано новое имя пользователя.

## Указание непривилегированного пользователя и группы

### **`USER`**

**Значение по умолчанию**: `dtuser`

Задаёт имя непривилегированного пользователя, который используется непривилегированными процессами OneAgent. Непривилегированные процессы, это процессы, которым не нужны права root. В Linux эти процессы называются `Network OneAgent` и `Plugin OneAgent`.

* По умолчанию установщик Dynatrace использует имя `dtuser` для непривилегированного пользователя.
* Если указан параметр `USER=<username>`, установщик использует `<username>` в качестве имени непривилегированного пользователя.

В обоих случаях установщик Dynatrace проверяет, существует ли уже в системе требуемый пользователь (`dtuser` или пользователь, указанный параметром `USER`).

* Если существуют и пользователь, и группа с тем же именем, и у этого пользователя эта группа задана как основная, для запуска сетевого и плагин-модуля OneAgent используется этот пользователь.
* Если пользователь не существует, установщик Dynatrace создаёт этого пользователя и группу и впоследствии запускает эти непривилегированные процессы от имени нового пользователя.
* Если пользователь существует в системе, но у него нет группы с тем же именем, заданной как основная, установка прерывается: чтобы использовать группу с другим именем, нужно использовать параметр `GROUP`.

Требования к строке `USER`:

* Может содержать только буквенно-цифровые символы, дефис `-`, подчёркивание `_` и точку `.`
* Минимальная длина, 3 символа
* Максимальная длина, 32 символа
* Не может быть строкой [идентификатора пользователя﻿](https://man7.org/linux/man-pages/man7/credentials.7.html)

### **`GROUP`**

**Значение по умолчанию**: `dtuser`

Может использоваться только вместе с параметром `USER` и служит для указания основной группы пользователя, переданного через параметр `USER`. Если параметр `GROUP` не указан, установщик считает её совпадающей с `USER`, как для существующих, так и для несуществующих пользователей. Если группа указана через параметр `GROUP` и пользователь не существует, установщик создаёт пользователя и назначает его в указанную группу. Параметр `GROUP` также используется для указания непривилегированного пользователя, принадлежащего определённой группе с именем, отличным от имени пользователя. Для повышения безопасности системы настоятельно рекомендуется использовать выделенную группу пользователей для запуска процессов OneAgent.

Требования к строке `GROUP`:

* Может содержать только буквенно-цифровые символы, дефис `-`, подчёркивание `_` и точку `.`
* Минимальная длина, 3 символа
* Максимальная длина, 32 символа
* Не может быть строкой [идентификатора группы﻿](https://man7.org/linux/man-pages/man7/credentials.7.html)

## Пропуск проверки поддержки операционной системы

Установка этого параметра в `true` разрешит установку OneAgent на платформе, которая иначе не поддерживается. Dynatrace не несёт ответственности за такие установки.

Этот параметр не сохраняется при автоматических обновлениях.

Информацию о механизме автообновления OneAgent см. в разделе [Обновление OneAgent в Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.").

**Значение по умолчанию**: `false`

Параметр **`SKIP_OS_SUPPORT_CHECK`** позволяет принудительно выполнить установку OneAgent на платформе, которая иначе не поддерживается.

Например:

```
/bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh SKIP_OS_SUPPORT_CHECK=true
```

Список поддерживаемых платформ см. в разделе [Поддержка технологий](/managed/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.").