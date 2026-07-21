---
title: Настройка OneAgent через интерфейс командной строки
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface
---

# Настройка OneAgent через интерфейс командной строки

# Настройка OneAgent через интерфейс командной строки

* Справка
* Чтение: 20 мин
* Обновлено 13 июля 2026 г.

Утилита командной строки `oneagentctl` позволяет выполнять часть постустановочной настройки OneAgent на уровне отдельного хоста.

## Расположение

Расположение утилиты зависит от того, изменялся ли путь установки OneAgent с помощью параметра `<INSTALL_PATH>`:

* **Linux** или **AIX**:  
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`  
  Нужны права root.
* **Развёртывание на базе Docker**  
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`  
  Обрати внимание, что для развёртывания на основе тома (volume) путь будет другим.
* **Windows**:  
  `<INSTALL_PATH>\agent\tools`, по умолчанию `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`  
  Нужны права администратора. При попытке запустить `oneagentctl` в консоли Windows без прав администратора появится всплывающее окно контроля учётных записей (User Account Control) и выполнение завершится ошибкой.

## Типы параметров

Команда `oneagentctl` принимает параметр `get` для проверки состояния или значения настройки и параметр `set` для изменения настройки. Обрати внимание, что в одной команде можно использовать сразу несколько параметров `set`.

## Перезапуск OneAgent

При использовании параметров `set` для применения изменений нужно перезапустить службу OneAgent. Для этого можно добавить к команде параметр `--restart-service`, который запускает перезапуск автоматически. В некоторых случаях также потребуется перезапустить отслеживаемые приложения. Параметр перезапуска можно использовать и отдельно, без других параметров. Пример команды приведён ниже.

* **Linux** или **AIX**:  
  `./oneagentctl --set-proxy=my-proxy.com --restart-service`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service`

## Вывод справки

Используй параметр `--help`, чтобы вывести список всех поддерживаемых параметров.

* **Linux** или **AIX**:  
  `./oneagentctl --help`
* **Windows**:  
  `.\oneagentctl.exe --help`

## Отображение версии OneAgent

Используй параметр `--version`, чтобы отобразить версию OneAgent.

* **Linux** или **AIX**:  
  `./oneagentctl --version`
* **Windows**:  
  `.\oneagentctl.exe --version`

## Связь OneAgent

### Настройка параметров связи OneAgent

Используй параметр `--set-server`, чтобы задать конечную точку связи OneAgent. Указывается IP-адрес или имя вместе с суффиксом `/communication`. В зависимости от типа развёртывания это может быть сервер Dynatrace, кластер Dynatrace Managed или ActiveGate.

Выполни следующую команду, чтобы настроить параметры соединения OneAgent:

* **Linux** или **AIX**:  
  `./oneagentctl --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

Чтобы задать несколько конечных точек, раздели их точкой с запятой и заключи в кавычки. Например, `--set-server="https://server1;https://server2"`.

Эти параметры требуют перезапуска OneAgent, а также перезапуска всех приложений, отслеживаемых с помощью deep code модулей. Добавь к команде параметр [`--restart-service`](#oneagent-restart), чтобы перезапустить OneAgent автоматически (версия 1.189 и выше), либо останови и запусти процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнай, как остановить и перезапустить OneAgent в Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнай, как остановить и перезапустить OneAgent в Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнай, как остановить и перезапустить OneAgent в AIX.").

Эта команда сразу же изменяет конечную точку соединения модуля ОС, но code модули не смогут прочитать новую настройку до следующего перезапуска.

OneAgent и кластер Dynatrace автоматически поддерживают рабочее соединение. Если данные конечной точки меняются, кластер уведомляет OneAgent об изменении, и OneAgent автоматически обновляет заданную с помощью `--set-server` конечную точку на новое рабочее значение.

Направление трафика OneAgent через ActiveGate

Маршрутизация трафика OneAgent через ActiveGate повышает безопасность данных, поскольку они остаются в пределах контролируемых сетевых маршрутов и шифруются при передаче.

1. Определи IP-адрес или имя хоста ActiveGate, который будет обрабатывать трафик.
2. [Настрой конечную точку связи](#set-oneagent-communication-settings).

   Настрой OneAgent, указав ActiveGate в качестве новой конечной точки. Например:

   ```
   .\oneagentctl.exe --set-server=https://<activegate-endpoint>:9999/communication --restart-service
   ```
3. [Проверь, включено ли автоматическое обновление](#check-if-auto-update-is-enabled).

### Отображение текущих конечных точек связи

Используй параметр `--get-server`, чтобы отобразить конечные точки, на которые OneAgent отправляет данные. Это могут быть сервер Dynatrace, кластер Dynatrace Managed или ActiveGate.

* **Linux** или **AIX**:  
  `./oneagentctl --get-server`
* **Windows**:  
  `.\oneagentctl.exe --get-server`

Начиная с версии OneAgent 1.207, конечные точки отображаются в формате, где точки с одинаковым приоритетом группируются с помощью фигурных скобок (`{...}`) и сортируются по приоритету соединения. Звёздочка (`*`) указывает на конечную точку, на которую OneAgent отправляет данные в данный момент. Конечные точки разделяются точкой с запятой (`;`).
Например:

```
{https://endpoint1.com/communication;https:/10.0.0.0/communication;*https://endpoint3.com/communication}{https://endpoint4.com:9999/communication}
```

### Задание идентификатора среды

Используй параметр `--set-tenant`, чтобы задать [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнай, что такое среда мониторинга Dynatrace, как найти идентификатор среды и как настроить и подключить несколько сред."). По умолчанию он уже установлен в верное значение. Если ты продаёшь услуги на базе Dynatrace, используй эту опцию, чтобы задавать идентификаторы своих клиентов из пула идентификаторов, приобретённых у Dynatrace.

* **Linux** или **AIX**:  
  `./oneagentctl --set-tenant=abc123456`
* **Windows**:  
  `.\oneagentctl.exe --set-tenant=abc123456`

Всегда используй в сочетании с `--set-tenant-token`, который задаёт [токен клиента (tenant token)](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнай, что такое токен клиента и как его изменить.") для внутренней аутентификации.

### Отображение идентификатора среды

[Идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Узнай, что такое среда мониторинга Dynatrace, как найти идентификатор среды и как настроить и подключить несколько сред.") Dynatrace, который был получен в письме об активации.

Используй параметр `--get-tenant`, чтобы отобразить идентификатор среды:

* **Linux** или **AIX**:  
  `./oneagentctl --get-tenant`
* **Windows**:  
  `.\oneagentctl.exe --get-tenant`

### Задание токена клиента

Используй параметр `--set-tenant-token`, чтобы задать [токен клиента (tenant token)](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнай, что такое токен клиента и как его изменить."), который используется для аутентификации связи с заданной конечной точкой. Всегда используй в сочетании с `--set-tenant`.

* **Linux** или **AIX**:  
  `./oneagentctl --set-tenant-token=abcdefg123456790`
* **Windows**:  
  `.\oneagentctl.exe --set-tenant-token=abcdefg123456790`

### Отображение токена клиента

Используй параметр `--get-tenant-token`, чтобы отобразить текущий заданный токен:

* **Linux** или **AIX**:  
  `./oneagentctl --get-tenant-token`
* **Windows**:  
  `.\oneagentctl.exe --get-tenant-token`

### Настройка прокси

Используй параметр `--set-proxy`, чтобы задать прокси-сервер:

* **Linux** или **AIX**:  
  `./oneagentctl --set-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=my-proxy.com`

### Очистка настроек прокси

Используй параметр `--set-proxy` с пустым значением, чтобы очистить настройки прокси:

* **Linux** или **AIX**:  
  `./oneagentctl --set-proxy=`
* **Windows**:  
  `.\oneagentctl.exe --set-proxy=`

Перезапусти службу OneAgent, чтобы применить изменения.

### Отображение текущего прокси

Используй параметр `--get-proxy`, чтобы отобразить прокси, через который в данный момент подключается OneAgent:

* **Linux** или **AIX**:  
  `./oneagentctl --get-proxy`
* **Windows**:  
  `.\oneagentctl.exe --get-proxy`

### Исключение отдельных IP-адресов из использования прокси

Используй параметр `--set-no-proxy`, чтобы исключить определённые домены или IP-адреса из использования прокси:

* **Linux** или **AIX**:  
  `./oneagentctl --set-no-proxy=my-proxy.com`
* **Windows**:  
  `.\oneagentctl.exe --set-no-proxy=my-proxy.com`

### Отображение текущих настроек исключения прокси

Используй параметр `--get-no-proxy`, чтобы просмотреть текущие настройки доменов и диапазонов IP-адресов, исключённых из использования прокси:

* **Linux** или **AIX**:  
  `./oneagentctl --get-no-proxy`
* **Windows**:  
  `.\oneagentctl.exe --get-no-proxy`

### Проверка текущего диапазона портов

OneAgent состоит из нескольких процессов, которые взаимодействуют с watchdog по TCP-порту. При запуске watchdog OneAgent пытается открыть первый доступный порт в диапазоне от 50000 до 50100. В некоторых случаях этот порт может понадобиться для собственных приложений, запускаемых после OneAgent.

Используй параметр `--get-watchdog-portrange`, чтобы проверить текущий диапазон портов, заданный для watchdog.

* **Linux** или **AIX**:  
  `./oneagentctl --get-watchdog-portrange`
* **Windows**:  
  `.\oneagentctl.exe --get-watchdog-portrange`

### Задать новый диапазон портов

Устарело

Начиная с версии OneAgent 1.301, OneAgent не использует TCP-порты для собственного межпроцессного взаимодействия. Если OneAgent занимает порты, нужные приложениям, обнови OneAgent до версии 1.301+.

Watchdog, это бинарный файл, который используется для запуска и мониторинга процессов мониторинга OneAgent:

* `oneagentos`, мониторинг операционной системы
* `oneagentplugin`, мониторинг с помощью [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Develop your own Extensions in Dynatrace.")
* `oneagentextensions`, мониторинг с помощью локальных [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")
* `oneagentloganalytics`, [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")
* `oneagentnetwork`, [мониторинг сети](/managed/observe/infrastructure-observability/networks "Learn how to monitor network communications.")

Используй параметр `--set-watchdog-portrange=arg`, чтобы изменить диапазон портов прослушивания watchdog на `<arg>`. `<arg>` должен содержать два номера портов, разделённых двоеточием (`:`). Например, `50000:50100`. Максимальный поддерживаемый диапазон портов, от 1024 до 65535. Диапазон портов должен охватывать минимум 4 порта. Номер порта, с которого начинается диапазон, должен быть меньше.

* **Linux** или **AIX**:
  `./oneagentctl --set-watchdog-portrange=50000:50100`
* **Windows**:
  `.\oneagentctl.exe --set-watchdog-portrange=50000:50100`

## Автоматические обновления

Подробнее см. темы об обновлении OneAgent для [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.") и [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix "Learn how you can update Dynatrace OneAgent on AIX.").

### Проверить, включено ли автообновление

Используй параметр `get-auto-update-enabled`, чтобы проверить, включено ли автообновление OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-auto-update-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-auto-update-enabled`

### Включить или отключить автообновление

Задай параметру `--set-auto-update-enabled` значение `true` или `false`, чтобы отключить или включить автообновление OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-update-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-auto-update-enabled=true`

После использования этой команды для отключения автообновлений управлять автоматическими обновлениями OneAgent через Dynatrace в разделе **Settings** > **Deployment** > **OneAgent updates** не получится.

## Log monitoring

Подробнее см. [Log Monitoring﻿](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics).

### Проверить, включён ли Log Monitoring

Используй параметр `--get-app-log-content-access`, чтобы проверить, включён ли Log Monitoring:

* **Linux**:
  `./oneagentctl --get-app-log-content-access`
* **Windows**:
  `.\oneagentctl.exe --get-app-log-content-access`

### Включить или отключить Log Monitoring

Задай параметру `--set-app-log-content-access` значение `true` или `false`, чтобы отключить или включить Log Monitoring:

* **Linux**:
  `./oneagentctl --set-app-log-content-access=true`
* **Windows**:
  `.\oneagentctl.exe --set-app-log-content-access=true`

## Создать архив поддержки

OneAgent версии 1.225+

Если нет доступа к Dynatrace или нужно скриптово собрать диагностические данные, можно использовать команду `oneagentctl`, чтобы собрать [подмножество](#contents) данных полной [диагностики OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") прямо на хосте, где установлен OneAgent. С собранными диагностическими данными OneAgent можно:

* легко собрать диагностические данные для конкретного хоста;
* напрямую предоставить поддержке Dynatrace сведения, нужные для диагностики проблемы.

Для выполнения команды требуется, чтобы служба OneAgent была запущена.

Чтобы создать архив поддержки с диагностическими данными, запусти `oneagentctl` с параметром `--create-support-archive`. По умолчанию архив поддержки содержит данные за 7-дневный период и создаётся в текущем рабочем каталоге. При необходимости можно задать другой каталог и период с помощью параметров `directory` и `days`. Обрати внимание: `onegentctl` не создаёт каталог, нужно указать существующий каталог с относительным или абсолютным путём. Например:

* **Linux** или **AIX**:
  `./oneagentctl --create-support-archive directory=/data/support-archive days=30`
* **Windows**:
  `.\oneagentctl.exe --create-support-archive directory=C:\data\support-archive days=30`

Команда сохраняет архив в виде файла `support_archive_agent_YYYY-MM-DD_hhmmss.zip`. Например:

```
Creating support archive from last 30 days in C:\data\support-archive



Waiting 30s for archive request to be processed



Processing archive, waiting up to 15m 0s



Archive saved as C:\data\support-archive\support_archive_agent_2021-09-07_121619.zip
```

### Содержимое диагностических данных

Все собранные диагностические данные сжимаются в архив `support_archive_agent_YYYY-MM-DD_hhmmss.zip`, который включает следующее подмножество данных полной [диагностики OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics"):

| Папка или файл | Описание |
| --- | --- |
| `support_archive` (ZIP) | Содержит локальную конфигурацию OneAgent, установленного на хосте или в процессе, где выполнялось устранение неполадок, а также файлы журналов, связанные с OneAgent. |
| `diagnostic_files` (ZIP) | Содержит информацию об обнаружении групп процессов, проблемах автоматического внедрения и конфигурации расширений. |

## Доступ к системным журналам для проактивной поддержки

OneAgent загружает определённые системные журналы, чтобы Dynatrace мог диагностировать проблемы, которые могут быть вызваны условиями в среде. Журналы также сохраняются в архиве поддержки. Чаще всего такие проблемы связаны с глубоким мониторингом или установкой автообновлений.

### Проверить, включён ли доступ к системным журналам

Используй параметр `--get-system-logs-access-enabled`, чтобы проверить, включён ли доступ к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --get-system-logs-access-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-system-logs-access-enabled`

### Включить или отключить доступ к системным журналам

Задай параметру `--set-system-logs-access-enabled` значение `true` или `false`, чтобы отключить или включить доступ к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --set-system-logs-access-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-system-logs-access-enabled=true`
  Перезапусти службу OneAgent, чтобы применить изменения.

Обрати внимание: параметры `--set-system-logs-access-enabled` и `--get-system-logs-access-enabled` относятся к настройке самодиагностики и не связаны с [Log Monitoring](#log-monitoring).

Отключение доступа к системным журналам ограничивает нашу способность проактивно диагностировать и решать проблемы. При отозванном доступе к системным журналам может понадобиться вручную предоставить Dynatrace содержимое системных журналов, чтобы помочь диагностировать проблемы в среде.

## Host ID

Dynatrace присваивает уникальный ID каждому хосту, который отслеживается в среде. Host ID можно использовать как параметры в запросах API Dynatrace, например [Topology and Smartscape API - Hosts API](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api "Learn how you can use the Dynatrace API to manage monitored hosts."). Host ID также составляет URL страницы **Host overview**, например, `https://environment.org/#newhosts/hostdetails;id=HOST-6E56EE455C84E232`.

### Отобразить свой host ID

Чтобы найти host ID, используй параметр `--get-host-id`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-id`
* **Windows**:
  `.\oneagentctl.exe --get-host-id`

### Определение источника ID хоста

Доступно на всех поддерживаемых платформах для OneAgent версии 1.223+. Для OneAgent версии 1.221 и более ранних эта функция поддерживается только для Citrix Virtual Apps and Desktops.

Особенно важно поддерживать статичность ID хоста в динамических виртуальных средах, где хосты пересоздаются ежедневно.

Чтобы **определить источник для генерации ID хоста**, используется `--set-host-id-source`, значение задаётся одним из предопределённых:

* `auto`, позволяет Dynatrace генерировать ID хоста автоматически
* `ip-addresses`, генерирует ID хоста на основе IP-адреса хоста
* `mac-addresses`, генерирует ID хоста на основе MAC-адреса сетевого адаптера хоста
* `fqdn`, генерирует ID хоста на основе полного доменного имени хоста (FQDN) в формате `host.domain`. Если FQDN не содержит символ точки, вместо него используется MAC-адрес сетевого адаптера.
* При мониторинге нескольких сред можно разделить хосты с одинаковыми IP-адресами, MAC-адресами или FQDN, используя отдельное пространство имён для каждой среды. Пространство имён может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки, максимальная длина составляет 256 символов.

  + `ip-addresses;namespace=<namespace>`
  + `mac-addresses;namespace=<namespace>`
  + `fqdn;namespace=<namespace>`

Например, чтобы задать источником ID хоста `ip-addresses` и присвоить его пространству имён с названием `test`, нужно запустить `oneagentctl` со следующим параметром:

* **Linux** или **AIX**:  
  `./oneagentctl --set-host-id-source="ip-addresses;namespace=test"`
* **Windows**:  
  `.\oneagentctl.exe --set-host-id-source="ip-addresses;namespace=test"`

После изменения источника ID хоста нужно перезапустить все отслеживаемые приложения, а затем перезапустить службу OneAgent, чтобы создать новый объект хоста в среде. Для автоматического перезапуска OneAgent можно использовать параметр `--restart-service` с `oneagentctl`, либо остановить и запустить процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

Чтобы **проверить источник ID хоста**, используется параметр `--get-host-id-source`:

* **Linux** или **AIX**:  
  `./oneagentctl --get-host-id-source`
* **Windows**:  
  `.\oneagentctl.exe --get-host-id-source`

Для источника ID хоста, установленного в `ip-addresses`, и пространства имён `test` команда вернёт следующий результат:

```
ip-addresses;namespace=test
```

## Группы хостов

Обзор использования групп хостов см. в разделе [Организация среды с помощью групп хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").

Также для централизованного изменения назначения группы хостов из Dynatrace Cluster можно использовать [централизованное управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрав действие **modify host group**).

### Изменение назначения группы хостов

Параметр `--set-host-group` используется для изменения назначения группы хостов.

Чтобы назначить хост группе `MyHostGroup`:

* **Linux** или **AIX**:  
  `./oneagentctl --set-host-group=MyHostGroup`
* **Windows**:  
  `.\oneagentctl.exe --set-host-group=MyHostGroup`

Требования к строке группы хостов:

* Может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки
* Не должна начинаться с `dt.`
* Максимальная длина составляет 100 символов

Использование `--set-host-group` требует перезапуска OneAgent, а также перезапуска всех отслеживаемых служб. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) либо остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

Изменение назначения групп хостов приводит к пересчёту ID групп процессов, что влияет на агрегацию данных. Подробнее о влиянии изменений группы хостов на обнаружение групп процессов см. в разделе [Организация среды с помощью групп хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#how-host-groups-affect-your-monitoring-environment "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.").

### Очистка назначения группы хостов

Чтобы очистить назначение группы хостов, используйте параметр `--set-host-group` с пустым значением:

* **Linux** или **AIX**:  
  `./oneagentctl --set-host-group=`
* **Windows**:  
  `.\oneagentctl.exe --set-host-group=`

### Отображение назначения группы хостов

Чтобы отобразить текущее назначение группы хостов, используйте параметр `--get-host-group`:

* **Linux** или **AIX**:  
  `./oneagentctl --get-host-group`
* **Windows**:  
  `.\oneagentctl.exe --get-host-group`

## Теги и метаданные хоста

В динамических или крупных средах ручная разметка хостов тегами может быть непрактичной. Для динамических развёртываний с часто меняющимися экземплярами хостов и именами (например, AWS или MS Azure) можно использовать выделенные параметры `oneagentctl` для применения пользовательских тегов, имён и метаданных к хостам.

Перечисленные ниже методы `oneagentctl` позволяют редактировать только те метаданные, которые были добавлены с помощью самого `oneagentctl` или ранее с помощью файлов конфигурации. Теги и метаданные, добавленные с помощью Dynatrace, а также полученные из отслеживаемой среды (например, теги AWS), недоступны для редактирования через `oneagentctl` и не отображаются с помощью параметров `--get-host-tags` и `--get-host-properties`.

### Обнаружение метаданных облака

По умолчанию процесс `oneagentos` автоматически обнаруживает облачные среды, такие как AWS, Azure и Google Compute Engine. Он отправляет запросы на выделенный API метаданных, расположенный по внутреннему IP-адресу `169.254.169.254`. OneAgent использует полученные метаданные, чтобы предоставить дополнительный контекст об отслеживаемых ресурсах в этих средах.

### Пользовательское имя хоста

Инструмент командной строки `oneagentctl` с параметром `--set-host-name` используется для переопределения автоматически обнаруженного имени хоста. Имя хоста не должно содержать символы `<`, `>`, `&`, `CR` (возврат каретки) или `LF` (перевод строки). Максимальная длина составляет 256 символов.

Эта команда добавляет пользовательское имя хоста для отображения в UI, но обнаруженное имя хоста при этом не изменяется. Подробнее см. в разделе [Задание пользовательских имён хостов](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.").

Чтобы изменить имя хоста:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=myhostname`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=myhostname`

Чтобы вернуться к автоматически обнаруженному имени хоста, задайте параметру `--set-host-name` пустое значение, как в `--set-host-name=""`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=""`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=""`

Изменение может не отображаться в веб-интерфейсе Dynatrace до 6 минут.

Использование `--set-host-name` требует перезапуска OneAgent. Добавьте `--restart-service` к команде для автоматического перезапуска OneAgent (версия 1.189+) либо остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

Чтобы показать имя хоста:

* **Linux** или **AIX**:  
  `./oneagentctl --get-host-name`
* **Windows**:  
  `.\oneagentctl.exe --get-host-name`

### Пользовательские метаданные хоста

После настройки пользовательские метаданные отображаются в виде набора свойств внизу раздела **Properties and tags** на странице обзора хоста. Значения свойств не должны содержать символ `=` (кроме использования как разделителя ключ-значение) или пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключ-значение. Имя ключа не должно начинаться с символа `#`.

Когда пользовательские метаданные хоста используются для обогащения метрик и другой телеметрии, ключи и значения могут корректироваться под требования нормализации: ключи приводятся к нижнему регистру, неподдерживаемые символы заменяются на подчёркивание (`_`), а ключи или значения, превышающие максимальную длину, обрезаются. В результате обогащённое значение может отличаться от заданного здесь.

Также можно изменять метаданные хоста централизованно из Dynatrace Cluster с помощью [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify host properties**).

Для версий раньше 1.189 используется [файл конфигурации метаданных хоста](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-metadata-configuration-file "Learn how to tag and set additional properties for a monitored host.").

Чтобы **добавить или изменить свойства хоста**, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --set-host-property=AppName --set-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --set-host-property=AppName --set-host-property Environment=Dev`

В одной команде можно добавить или изменить более одного свойства.

Чтобы **удалить свойства хоста**, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**  
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

Одной командой можно удалить более одного свойства. Если ключ свойства, переданный в команде, не существует, возвращается ненулевой код завершения, но все существующие свойства, переданные в команде, будут удалены. После удаления свойств хоста они остаются видимыми в Dynatrace ещё до 7 часов.

Чтобы **показать все свойства**, настроенные для хоста, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --get-host-properties`
* **Windows**  
  `.\oneagentctl.exe --get-host-properties`

### Пользовательские теги хоста

После настройки пользовательских тегов хоста они отображаются вверху раздела **Properties and tags** на странице обзора хоста. Значение свойства не должно содержать `=` (кроме использования как разделителя ключ-значение) или пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключ-значение. Имя ключа не должно начинаться с `#`.

Также можно изменять теги хоста централизованно из Dynatrace Cluster с помощью [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") (выбрать действие **modify host tags**).

Чтобы **добавить или изменить теги хоста**, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`

В одной команде можно добавить или изменить более одного тега. Допускается задавать теги с одинаковым ключом, но разными значениями.

Чтобы **удалить теги**, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --remove-host-tag=role=fallback --remove-host-tag=Gdansk`
* **Windows**  
  `.\oneagentctl.exe --remove-host-tag=role=fallback --remove-host-tag=Gdansk`

Одной командой можно удалить более одного тега. Если тег, переданный в команде, не существует, возвращается ненулевой код завершения, но все существующие теги, переданные в команде, удаляются. После удаления тегов они остаются видимыми в Dynatrace ещё до 6 часов.

Чтобы **показать все теги**, настроенные для хоста, нужно выполнить следующую команду:

* **Linux** и **AIX**  
  `./oneagentctl --get-host-tags`
* **Windows**  
  `.\oneagentctl.exe --get-host-tags`

## Режимы мониторинга

Активирует один из режимов мониторинга OneAgent:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

Чтобы включить конкретный режим мониторинга, нужно задать параметру `--set-monitoring-mode` одно из значений:

* `fullstack`
* `infra-only`
* `discovery`

Например:

```
--set-monitoring-mode=infra-only
```

Режим Infrastructure Monitoring или Discovery можно использовать вместо режима Full-Stack Monitoring. При таком подходе поступают данные о состоянии инфраструктуры, без данных о производительности приложений и пользователей. Подробнее см. [Monitoring modes](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

### Проверка включённого режима мониторинга

Параметр `--get-monitoring-mode` используется для проверки, какой режим мониторинга включён:

* **Linux** или **AIX**:  
  `./oneagentctl --get-monitoring-mode`
* **Windows**:  
  `.\oneagentctl.exe --get-monitoring-mode`

Команда возвращает одно из следующих значений:

* `fullstack`: режим Full-Stack Monitoring
* `infra-only`: режим Infrastructure Monitoring
* `discovery`: режим Discovery

Изменение режима Infrastructure Monitoring требует перезапуска OneAgent, а также перезапуска всех отслеживаемых сервисов. Нужно добавить [`--restart-service`](#oneagent-restart) к команде, чтобы перезапустить OneAgent автоматически (версия 1.189+), либо остановить и запустить процесс OneAgent вручную. Инструкции по конкретным ОС см. [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Learn how to stop and restart OneAgent on Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows."), или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Learn how to stop and restart OneAgent on AIX.").

## Автоматическое внедрение для режима Infrastructure Monitoring

OneAgent версии 1.213

Автоматическое внедрение OneAgent по умолчанию включено в режиме Infrastructure Monitoring. Оно требуется для сбора метрик JMX/PMI и для работы Application Security в режиме Infrastructure Monitoring.

Подробнее см. [OneAgent monitoring modes](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").

### Проверка, включено ли автоматическое внедрение

Параметр `get-auto-injection-enabled` используется для проверки, включено ли автоматическое внедрение OneAgent:

* **Linux** или **AIX**:  
  `./oneagentctl --get-auto-injection-enabled`
* **Windows**:  
  `.\oneagentctl.exe --get-auto-injection-enabled`

### Включение или отключение автоматического внедрения

Параметру `--set-auto-injection-enabled` нужно задать значение `true` или `false`, чтобы включить или отключить автоматическое внедрение OneAgent:

Чтобы включить автоматическое внедрение:

* **Linux** или **AIX**:  
  `./oneagentctl --set-auto-injection-enabled=true`
* **Windows**:  
  `.\oneagentctl.exe --set-auto-injection-enabled=true`

Чтобы отключить автоматическое внедрение:

* **Linux** или **AIX**:  
  `./oneagentctl --set-auto-injection-enabled=false`
* **Windows**:  
  `.\oneagentctl.exe --set-auto-injection-enabled=false`

Подробнее см. [Disable auto-injection](/managed/platform/oneagent/monitoring-modes/monitoring-modes#disable-auto-injection "Find out more about the available monitoring modes when using OneAgent.").

## Приём метрик

Локальный приём метрик в настоящее время поддерживается только на Windows и Linux.

Команду `oneagentctl` можно использовать для проверки или изменения портов связи, используемых для локального приёма метрик, с помощью [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities."), [Scripting integration](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Learn how to ingest metrics using local scripting integration."), [Telegraf](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Ingest Telegraf metrics into Dynatrace."), или [DynatraceStatsd](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client."). Изменение порта приёма метрик требует перезапуска OneAgent. Нужно добавить [`--restart-service`](#oneagent-restart) к команде, чтобы перезапустить OneAgent автоматически.

См. [Metrics ingestion](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."), чтобы узнать больше.

### OneAgent API, scripting integration и Telegraf

Порт приёма метрик по умолчанию, `14499`. При необходимости можно использовать команду [oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для проверки или изменения порта. Изменение порта приёма метрик требует перезапуска OneAgent. Нужно добавить [`--restart-service`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") к команде, чтобы перезапустить OneAgent автоматически.

### Проверка порта приёма данных

Используй параметр `--get-extensions-ingest-port`, чтобы показать текущий локальный порт приёма данных, по умолчанию `14499`.

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Настройка пользовательского порта приёма данных

Используй параметр `--set-extensions-ingest-port=<arg>`, чтобы задать пользовательский локальный порт приёма данных.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Настройка прокси

Настрой прокси хоста так, чтобы разрешить трафик localhost, идущий на порт приёма метрик (по умолчанию `14499`).

### StatsD

### Слушатель OneAgent

Порт прослушивания DynatraceStatsD UDP по умолчанию для слушателя OneAgent, это `18125`. При необходимости можно использовать команду [oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.") для проверки или изменения порта приёма метрик. Изменение порта требует перезапуска OneAgent. Добавь [`--restart-service`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнай, как выполнить некоторые задачи конфигурации OneAgent без необходимости переустановки OneAgent.") к команде, чтобы автоматически перезапустить OneAgent.

#### Проверка порта приёма данных

Используй параметр `--get-extensions-statsd-port`, чтобы показать текущий порт прослушивания DynatraceStatsd UDP (по умолчанию = `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Настройка пользовательского порта приёма данных

Используй параметр `--set-extensions-statsd-port=<arg>`, чтобы задать пользовательский порт прослушивания DynatraceStatsd UDP.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Удалённый StatsD

Порт прослушивания DynatraceStatsD UDP по умолчанию для удалённого слушателя, это `18126`.

Чтобы изменить порт прослушивания по умолчанию `18126`, измени параметр `StatsdPort` в файле ActiveGate `extensionsuser.conf`:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Сетевые зоны

Чтобы узнать о правилах именования сетевых зон и другой справочной информации, смотри [Network zones](/managed/manage/network-zones "Узнай, как работают сетевые зоны в Dynatrace.").

Также можно изменить назначение сетевой зоны централизованно из Dynatrace Cluster, используя [Remote configuration management](/managed/ingest-from/bulk-configuration#configure-oneagents "Выполни конфигурацию OneAgent и ActiveGate на хостах со страницы Deployment status или в массовом порядке с помощью Dynatrace API.") (выбери действие **modify network zone**).

### Настройка сетевой зоны

Используй параметр `--set-network-zone`, чтобы указать OneAgent взаимодействовать через заданную сетевую зону. Имя сетевой зоны, это строка из буквенно-цифровых символов. Также можно использовать дефис (`-`), подчёркивание (`_`) и точку (`.`) в качестве разделителя. Имя сетевой зоны не должно начинаться с точки. Длина строки ограничена 256 символами. Имена сетевых зон не чувствительны к регистру. Dynatrace хранит эти имена в нижнем регистре. Подробнее смотри раздел про [именование сетевых зон](/managed/manage/network-zones/network-zones-basic-info#naming "Узнай, как начать работу с сетевыми зонами.")

* На **Linux** или **AIX**:  
  `./oneagentctl --set-network-zone=<your.network.zone>`
* На **Windows**:  
  `.\oneagentctl.exe --set-network-zone=<your.network.zone>`

#### Сброс сетевой зоны

Можно сбросить настройку сетевой зоны, передав пустое имя сетевой зоны:

* На **Linux** или **AIX**:  
  `./oneagentctl --set-network-zone=""`
* На **Windows**:  
  `.\oneagentctl.exe --set-network-zone=""`

### Отображение настройки сетевой зоны

Используй параметр `--get-network-zone`, чтобы отобразить текущую конфигурацию сетевой зоны:

* На **Linux** или **AIX**:  
  `./oneagentctl --get-network-zone`
* На **Windows**:  
  `.\oneagentctl.exe --get-network-zone`

## Передача параметров конфигурации во время установки

Параметры `--set-*` можно передавать во время установки. Параметры конфигурации применяются непосредственно перед запуском службы OneAgent, и нет необходимости перезапускать её для применения конфигурации.

Linux и AIX

Windows

Чтобы передать параметры конфигурации, просто добавь параметр, а перед значением поставь знак равенства (`=`). Например:

```
/bin/sh Dynatrace-OneAgent-Linux.sh –-set-host-group=test_group
```

### EXE-установщик

Чтобы передать параметры конфигурации с помощью EXE-установщика, просто добавь параметр, а перед значением поставь знак равенства (`=`). Например:

```
Dynatrace-OneAgent-Windows.exe --set-host-group=test_group
```

### Пакет MSI

Параметры конфигурации также можно передать с помощью пакета MSI. В этом случае, однако, нужно использовать дополнительный параметр `ADDITIONAL_CONFIGURATION`. Например:

```
Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-host-group=test_group"
```

## Криптографические алгоритмы FIPS 140

OneAgent версии 1.245+

OneAgent использует режим FIPS для соответствия стандарту компьютерной безопасности FIPS 140-3.

### Проверка, включён ли FIPS 140

Используй `--get-fips-enabled`, чтобы проверить, использует ли OneAgent криптографические алгоритмы, валидированные по FIPS 140.

* На **Linux** или **AIX**  
  `./oneagentctl --get-fips-enabled`
* На **Windows**  
  `.\oneagentctl.exe --get-fips-enabled`

### Включение или отключение FIPS 140

Включение или отключение криптографических алгоритмов, валидированных по FIPS 140, можно выполнить только во время установки.

Установи параметр `--set-fips-enabled` в значение `true` или `false`, чтобы включить или отключить криптографические алгоритмы, валидированные по FIPS 140, на OneAgent. Значение по умолчанию при первой установке, это `false`.

Чтобы включить режим FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запусти установщик с `--set-fips-enabled=true`

Чтобы отключить режим FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запусти установщик с `--set-fips-enabled==false`

Если нужно включить режим FIPS для развёртывания только приложений, перейди в `/paas/package/agent` и удали `dt_fips_disabled.flag`.

## cap\_setuid для OS Agent на Linux

Мониторинг GPFS

OneAgent версии 1.293+

Включение `cap_setuid` для OS Agent требуется для мониторинга GPFS.

Следующие параметры доступны только в [непривилегированном режиме OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнай, когда Dynatrace OneAgent требует root-прав на Linux.").

* `get-osagent-cap-setuid-enabled`
* `set-osagent-cap-setuid-enabled`

Можно включить `cap_setuid` для OS Agent начиная с версии OneAgent 1.293+, но использовать мониторинг GPFS можно только с версии OneAgent 1.295+.

### Проверка, включён ли cap\_setuid для OS Agent

Используй параметр `get-osagent-cap-setuid-enabled`, чтобы проверить, включён ли cap\_setuid для OS Agent:

`./oneagentctl --get-osagent-cap-setuid-enabled`

### Включение или отключение cap\_setuid для OS Agent

Установи параметр `set-osagent-cap-setuid-enabled` в значение `true` или `false`, чтобы отключить или включить cap\_setuid для OS Agent:

`./oneagentctl --set-osagent-cap-setuid-enabled=true`

## Windows Redirection Guard

OneAgent версии 1.341+

Dynatrace OneAgent поддерживает Windows Redirection Guard в редакциях Windows, предоставляющих эту функцию.

OneAgent отклоняет пути или файлы, которые разрешаются через NTFS junction, созданные обычными (непривилегированными) учётными записями пользователей Windows. Это касается расположений, к которым обращается OneAgent (например, при определении технологии процесса).

Это уменьшает поверхность атаки для junction-атак на Windows, предотвращая переход OneAgent по потенциально вредоносным junction, созданным непривилегированными пользователями.

### Проверка, включена ли поддержка Windows Redirection Guard в OneAgent

Используй параметр `get-watchdog-redirection-trust-policy-enabled`, чтобы проверить, включена ли поддержка Windows Redirection Guard в OneAgent:

`./oneagentctl --get-watchdog-redirection-trust-policy-enabled`

### Включение или отключение поддержки Windows Redirection Guard

Установи параметр `set-watchdog-redirection-trust-policy-enabled` в значение `true` или `false`, чтобы включить (включено по умолчанию) или отключить поддержку Windows Redirection Guard в OneAgent:

`./oneagentctl --set-watchdog-redirection-trust-policy-enabled=false`