---
title: Настройка OneAgent через интерфейс командной строки
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface
scraped: 2026-05-12T11:05:28.442727
---

# Настройка OneAgent через интерфейс командной строки

# Настройка OneAgent через интерфейс командной строки

* Справочник
* Чтение: 20 мин
* Обновлено 17 сентября 2025 г.

Используйте интерфейс командной строки `oneagentctl` для выполнения ряда задач настройки OneAgent после установки на уровне отдельного хоста.

## Расположение

Расположение инструмента зависит от того, задавали ли вы параметр `<INSTALL_PATH>` при установке OneAgent:

* **Linux** или **AIX**:
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`
  Требуются привилегии root.
* **Развёртывание на основе Docker**
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`
  Обратите внимание, что для развёртывания с томами путь будет другим.
* **Windows**:
  `<INSTALL_PATH>\agent\tools`, по умолчанию `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`
  Требуются права администратора. Если запустить `oneagentctl` в консоли Windows без прав администратора, Windows отобразит диалог управления учётными записями пользователей (UAC) и завершит работу с ошибкой.

## Типы параметров

Команда `oneagentctl` принимает параметр `get` для проверки состояния или значения настройки и параметр `set` для изменения настройки. В одной команде можно использовать несколько параметров `set`.

## Перезапуск OneAgent

При использовании параметров `set` для применения изменений нужно перезапустить сервис OneAgent. Параметр `--restart-service` позволяет выполнить перезапуск автоматически вместе с основной командой. В некоторых случаях также потребуется перезапустить отслеживаемые приложения. Параметр перезапуска можно также использовать отдельно, без других параметров. Пример команды приведён ниже.

* **Linux** или **AIX**:
  `./oneagentctl --set-proxy=my-proxy.com --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service`

## Отображение справки

Используйте параметр `--help` для отображения всех поддерживаемых параметров.

* **Linux** или **AIX**:
  `./oneagentctl --help`
* **Windows**:
  `.\oneagentctl.exe --help`

## Отображение версии OneAgent

Используйте параметр `--version` для отображения версии OneAgent.

* **Linux** или **AIX**:
  `./oneagentctl --version`
* **Windows**:
  `.\oneagentctl.exe --version`

## Взаимодействие OneAgent

### Задать параметры взаимодействия OneAgent

Используйте параметр `--set-server` для задания endpoint взаимодействия OneAgent. Укажите IP-адрес или имя в сочетании с суффиксом `/communication`. В зависимости от развёртывания это может быть Dynatrace Server, Dynatrace Managed Cluster или ActiveGate.

Выполните следующую команду для изменения настроек подключения OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

Для задания нескольких endpoint разделите их точкой с запятой и заключите в кавычки. Например: `--set-server="https://server1;https://server2"`.

Эти параметры требуют перезапуска OneAgent, а также перезапуска всех приложений, отслеживаемых с помощью глубоких кодовых модулей. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретной ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Эта команда немедленно изменит endpoint подключения модуля ОС, однако кодовые модули смогут применить новую настройку только после следующего перезапуска.

OneAgent и Dynatrace Cluster автоматически поддерживают рабочее подключение. При изменении параметров endpoint кластер уведомляет OneAgent, и OneAgent автоматически обновляет endpoint, заданный через `--set-server`, на новое рабочее значение.

Направление трафика OneAgent через ActiveGate

Маршрутизация трафика OneAgent через ActiveGate позволяет повысить безопасность данных: они остаются в контролируемых сетевых путях и шифруются при передаче.

1. Определите IP-адрес или имя хоста ActiveGate, который будет обрабатывать трафик.
2. [Задайте endpoint взаимодействия](#set-oneagent-communication-settings).

   Настройте OneAgent, указав ActiveGate в качестве нового endpoint. Например:

   ```
   .\oneagentctl.exe --set-server=https://<activegate-endpoint>:9999/communication --restart-service
   ```
3. [Проверьте, включено ли автоматическое обновление](#check-if-auto-update-is-enabled).

### Показать текущие endpoint взаимодействия

Используйте параметр `--get-server` для отображения endpoint, на которые OneAgent отправляет данные. Это может быть Dynatrace Server, Dynatrace Managed Cluster или ActiveGate.

* **Linux** или **AIX**:
  `./oneagentctl --get-server`
* **Windows**:
  `.\oneagentctl.exe --get-server`

Начиная с OneAgent версии 1.207 endpoint отображаются в формате, при котором endpoint одинакового приоритета группируются в фигурные скобки (`{...}`) и сортируются по приоритету подключения. Звёздочка (`*`) обозначает endpoint, на который OneAgent в данный момент отправляет данные. Endpoint разделяются точкой с запятой (`;`).
Например:

```
{https://endpoint1.com/communication;https:/10.0.0.0/communication;*https://endpoint3.com/communication}{https://endpoint4.com:9999/communication}
```

### Задать идентификатор окружения

Используйте параметр `--set-tenant` для задания [идентификатора окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как работать с окружениями мониторинга."). По умолчанию это значение уже задано корректно. Если вы перепродаёте услуги на основе Dynatrace, используйте этот параметр для задания идентификаторов ваших клиентов из пула идентификаторов, приобретённых у Dynatrace.

* **Linux** или **AIX**:
  `./oneagentctl --set-tenant=abc123456`
* **Windows**:
  `.\oneagentctl.exe --set-tenant=abc123456`

Всегда используйте в сочетании с `--set-tenant-token`, который задаёт [токен тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его изменить.") для внутренней аутентификации.

### Показать идентификатор окружения

Идентификатор [окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Узнайте, как работать с окружениями мониторинга.") Dynatrace, который вы получили в письме с активацией.

Используйте параметр `--get-tenant` для отображения идентификатора окружения:

* **Linux** или **AIX**:
  `./oneagentctl --get-tenant`
* **Windows**:
  `.\oneagentctl.exe --get-tenant`

### Задать токен тенанта

Используйте параметр `--set-tenant-token` для задания [токена тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен тенанта и как его изменить."), используемого для аутентификации взаимодействия с заданным endpoint. Всегда используйте в сочетании с `--set-tenant`.

* **Linux** или **AIX**:
  `./oneagentctl --set-tenant-token=abcdefg123456790`
* **Windows**:
  `.\oneagentctl.exe --set-tenant-token=abcdefg123456790`

### Показать токен тенанта

Используйте параметр `--get-tenant-token` для отображения текущего токена:

* **Linux** или **AIX**:
  `./oneagentctl --get-tenant-token`
* **Windows**:
  `.\oneagentctl.exe --get-tenant-token`

### Задать конфигурацию прокси

Используйте параметр `--set-proxy` для задания прокси-сервера:

* **Linux** или **AIX**:
  `./oneagentctl --set-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-proxy=my-proxy.com`

### Очистить конфигурацию прокси

Используйте параметр `--set-proxy` с пустым значением для очистки конфигурации прокси:

* **Linux** или **AIX**:
  `./oneagentctl --set-proxy=`
* **Windows**:
  `.\oneagentctl.exe --set-proxy=`

Перезапустите сервис OneAgent для применения изменений.

### Показать текущий прокси

Используйте параметр `--get-proxy` для отображения текущего прокси, через который подключается OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-proxy`
* **Windows**:
  `.\oneagentctl.exe --get-proxy`

### Исключить определённые IP-адреса из прокси

Используйте параметр `--set-no-proxy` для исключения определённых доменов или IP-адресов из использования прокси:

* **Linux** или **AIX**:
  `./oneagentctl --set-no-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-no-proxy=my-proxy.com`

### Показать текущие настройки no-proxy

Используйте параметр `--get-no-proxy` для просмотра текущих настроек доменов и диапазонов IP-адресов, исключённых из использования прокси:

* **Linux** или **AIX**:
  `./oneagentctl --get-no-proxy`
* **Windows**:
  `.\oneagentctl.exe --get-no-proxy`

### Проверить текущий диапазон портов

OneAgent состоит из различных процессов, взаимодействующих с watchdog через TCP-порт. При запуске watchdog OneAgent пытается открыть первый доступный порт в диапазоне от 50000 до 50100. В некоторых случаях этот порт может потребоваться для ваших приложений, запускаемых после OneAgent.

Используйте параметр `--get-watchdog-portrange` для проверки текущего диапазона портов, заданного для watchdog.

* **Linux** или **AIX**:
  `./oneagentctl --get-watchdog-portrange`
* **Windows**:
  `.\oneagentctl.exe --get-watchdog-portrange`

### Задать новый диапазон портов

Устарело

Начиная с OneAgent версии 1.301 OneAgent не использует TCP-порты для внутреннего взаимодействия между процессами. Если OneAgent занимает порты ваших приложений, обновите OneAgent до версии 1.301+.

Watchdog, это исполняемый файл, используемый для запуска и мониторинга процессов OneAgent:

* `oneagentos`: мониторинг операционной системы
* `oneagentplugin`: мониторинг с помощью [расширений OneAgent](/managed/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Разрабатывайте собственные расширения в Dynatrace.")
* `oneagentextensions`: мониторинг с помощью локальных [расширений](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.")
* `oneagentloganalytics`: [мониторинг журналов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов и какие возможности он предоставляет.")
* `oneagentnetwork`: [мониторинг сети](/managed/observe/infrastructure-observability/networks "Узнайте, как вести мониторинг сетевых коммуникаций.")

Используйте параметр `--set-watchdog-portrange=arg` для изменения диапазона прослушиваемых портов watchdog на `<arg>`. Значение `<arg>` должно содержать два номера портов, разделённых двоеточием (`:`). Например: `50000:50100`. Максимально поддерживаемый диапазон: от 1024 до 65535. Диапазон должен включать не менее 4 портов. Начальный номер порта должен быть меньше конечного.

* **Linux** или **AIX**:
  `./oneagentctl --set-watchdog-portrange=50000:50100`
* **Windows**:
  `.\oneagentctl.exe --set-watchdog-portrange=50000:50100`

## Автоматические обновления

Подробнее см. в разделах обновления OneAgent: [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Узнайте о различных способах обновления Dynatrace OneAgent на Windows.") и [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix "Узнайте, как обновить Dynatrace OneAgent на AIX.").

### Проверить, включено ли автоматическое обновление

Используйте параметр `get-auto-update-enabled` для проверки того, включено ли автоматическое обновление OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-auto-update-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-auto-update-enabled`

### Включить или отключить автоматическое обновление

Установите параметр `--set-auto-update-enabled` в `true` или `false` для включения или отключения автоматического обновления OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-update-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-auto-update-enabled=true`

После отключения автоматических обновлений этой командой управление ими через Dynatrace по пути **Settings** > **Updates** > **OneAgent updates** станет недоступным.

## Мониторинг журналов

Подробнее см. [Мониторинг журналов](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics).

### Проверить, включён ли мониторинг журналов

Используйте параметр `--get-app-log-content-access` для проверки того, включён ли мониторинг журналов:

* **Linux**:
  `./oneagentctl --get-app-log-content-access`
* **Windows**:
  `.\oneagentctl.exe --get-app-log-content-access`

### Включить или отключить мониторинг журналов

Установите параметр `--set-app-log-content-access` в `true` или `false` для включения или отключения мониторинга журналов:

* **Linux**:
  `./oneagentctl --set-app-log-content-access=true`
* **Windows**:
  `.\oneagentctl.exe --set-app-log-content-access=true`

## Создать архив поддержки

OneAgent версии 1.225+

Если доступ к Dynatrace отсутствует или нужно автоматизировать сбор диагностических данных, используйте команду `oneagentctl` для сбора [подмножества](#contents) данных полной [диагностики OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как выполнять диагностику OneAgent.") прямо на хосте, где установлен OneAgent. После сбора диагностических данных можно:

* Легко собирать диагностические данные для конкретного хоста
* Напрямую предоставить в Dynatrace Support все необходимые для диагностики подробности

Для выполнения команды сервис OneAgent должен быть запущен.

Для создания архива поддержки с диагностическими данными запустите `oneagentctl` с параметром `--create-support-archive`. По умолчанию архив поддержки содержит данные за 7 дней и создаётся в текущем рабочем каталоге. При необходимости можно задать собственный каталог и период с помощью параметров `directory` и `days`. Обратите внимание, что `oneagentctl` не создаёт каталог самостоятельно: нужно указать путь к уже существующему каталогу (относительный или абсолютный). Например:

* **Linux** или **AIX**:
  `./oneagentctl --create-support-archive directory=/data/support-archive days=30`
* **Windows**:
  `.\oneagentctl.exe --create-support-archive directory=C:\data\support-archive days=30`

Команда сохраняет архив в файл `support_archive_agent_YYYY-MM-DD_hhmmss.zip`. Например:

```
Creating support archive from last 30 days in C:\data\support-archive



Waiting 30s for archive request to be processed



Processing archive, waiting up to 15m 0s



Archive saved as C:\data\support-archive\support_archive_agent_2021-09-07_121619.zip
```

### Содержимое диагностических данных

Все собранные диагностические данные сжимаются в архив `support_archive_agent_YYYY-MM-DD_hhmmss.zip`, который включает следующее подмножество данных полной [диагностики OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как выполнять диагностику OneAgent."):

| Папка или файл | Описание |
| --- | --- |
| `support_archive` (ZIP) | Содержит локальную конфигурацию OneAgent, установленного на хосте или в процессе, для которых выполнялась диагностика, а также связанные с OneAgent файлы журналов. |
| `diagnostic_files` (ZIP) | Содержит информацию об обнаружении групп процессов, проблемах автоматической инъекции и конфигурации расширений. |

## Доступ к системным журналам для проактивной поддержки

OneAgent загружает определённые системные журналы, чтобы Dynatrace мог диагностировать проблемы, вызванные условиями в вашем окружении. Журналы также сохраняются в архиве поддержки. Чаще всего такие проблемы связаны с глубоким мониторингом или установками автоматических обновлений.

### Проверить, включён ли доступ к системным журналам

Используйте параметр `--get-system-logs-access-enabled` для проверки того, включён ли доступ к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --get-system-logs-access-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-system-logs-access-enabled`

### Включить или отключить доступ к системным журналам

Установите параметр `--set-system-logs-access-enabled` в `true` или `false` для включения или отключения доступа к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --set-system-logs-access-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-system-logs-access-enabled=true`
  Перезапустите сервис OneAgent для применения изменений.

Параметры `--set-system-logs-access-enabled` и `--get-system-logs-access-enabled` относятся к настройке самодиагностики и не связаны с [мониторингом журналов](#log-monitoring).

Отключение доступа к системным журналам ограничивает возможности проактивной диагностики и устранения неполадок. При отозванном доступе к системным журналам может потребоваться передать содержимое системных журналов в Dynatrace вручную для диагностики проблем в вашем окружении.

## Идентификатор хоста

Dynatrace присваивает уникальный идентификатор каждому хосту, отслеживаемому в вашем окружении. Идентификаторы хостов можно использовать в качестве параметров в запросах к Dynatrace API, например [Topology and Smartscape API - Hosts API](/managed/dynatrace-api/environment-api/topology-and-smartscape/hosts-api "Узнайте, как использовать Dynatrace API для управления отслеживаемыми хостами."). Идентификатор хоста также является частью URL страницы **Host overview**, например: `https://environment.org/#newhosts/hostdetails;id=HOST-6E56EE455C84E232`.

### Отобразить идентификатор хоста

Для получения идентификатора хоста используйте параметр `--get-host-id`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-id`
* **Windows**:
  `.\oneagentctl.exe --get-host-id`

### Определить источник идентификатора хоста

Доступно на всех поддерживаемых платформах для OneAgent версии 1.223+. Для OneAgent версии 1.221 и более ранних эта функция поддерживается только для Citrix Virtual Apps and Desktops.

Сохранение статического идентификатора хоста особенно важно в динамических виртуальных окружениях, где хосты пересоздаются ежедневно.

Для **определения источника генерации идентификатора хоста** используйте `--set-host-id-source` и задайте одно из предопределённых значений:

* `auto`: Dynatrace генерирует идентификатор хоста автоматически
* `ip-addresses`: идентификатор хоста генерируется на основе IP-адреса хоста
* `mac-addresses`: идентификатор хоста генерируется на основе MAC-адреса сетевого адаптера хоста
* `fqdn`: идентификатор хоста генерируется на основе полного доменного имени (FQDN) хоста в формате `host.domain`. Если FQDN не содержит точки, используется MAC-адрес сетевого адаптера.
* При мониторинге нескольких окружений можно разделить хосты с одинаковыми IP-адресами, MAC-адресами или FQDN, задав разные пространства имён для каждого окружения. Пространство имён может содержать только буквенно-цифровые символы, дефисы, знаки подчёркивания и точки; максимальная длина: 256 символов.

  + `ip-addresses;namespace=<namespace>`
  + `mac-addresses;namespace=<namespace>`
  + `fqdn;namespace=<namespace>`

Например, чтобы задать `ip-addresses` в качестве источника идентификатора хоста и назначить пространство имён `test`, запустите `oneagentctl` со следующим параметром:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-id-source="ip-addresses;namespace=test"`
* **Windows**:
  `.\oneagentctl.exe --set-host-id-source="ip-addresses;namespace=test"`

После изменения источника идентификатора хоста нужно перезапустить все отслеживаемые приложения, а затем перезапустить сервис OneAgent для создания новой сущности хоста в вашем окружении. Используйте параметр `--restart-service` с `oneagentctl` для автоматического перезапуска OneAgent или остановите и запустите процесс OneAgent вручную. Инструкции для конкретной ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Для **проверки источника идентификатора хоста** используйте параметр `--get-host-id-source`:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-id-source`
* **Windows**:
  `.\oneagentctl.exe --get-host-id-source`

Для источника идентификатора хоста `ip-addresses` с пространством имён `test` команда вернёт следующий результат:

```
ip-addresses;namespace=test
```

## Группы хостов

Обзор использования групп хостов см. в разделе [Организация окружения с помощью групп хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.").

Для централизованного изменения назначения групп хостов из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Настраивайте OneAgent и ActiveGate на хостах со страницы статуса развёртывания или массово через Dynatrace API.") (действие **modify host group**).

### Изменить назначение группы хостов

Используйте параметр `--set-host-group` для изменения назначения группы хостов.

Для назначения хоста в `MyHostGroup`:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-group=MyHostGroup`
* **Windows**:
  `.\oneagentctl.exe --set-host-group=MyHostGroup`

Требования к строке группы хостов:

* Может содержать только буквенно-цифровые символы, дефисы, знаки подчёркивания и точки
* Не должна начинаться с `dt.`
* Максимальная длина: 100 символов

Использование `--set-host-group` требует перезапуска OneAgent, а также перезапуска всех отслеживаемых сервисов. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретной ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Изменение назначения группы хостов приводит к пересчёту идентификаторов групп процессов, что влияет на агрегацию данных. Подробнее о влиянии изменений групп хостов на обнаружение групп процессов см. в разделе [Организация окружения с помощью групп хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#how-host-groups-affect-your-monitoring-environment "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.").

### Очистить назначение группы хостов

Используйте параметр `--set-host-group` с пустым значением для удаления назначения группы хостов:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-group=`
* **Windows**:
  `.\oneagentctl.exe --set-host-group=`

### Отобразить назначение группы хостов

Используйте параметр `--get-host-group` для отображения текущего назначения группы хостов:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-group`
* **Windows**:
  `.\oneagentctl.exe --get-host-group`

## Теги и метаданные хоста

В динамических или крупных окружениях ручная расстановка тегов на хостах может быть нецелесообразной. Для динамических развёртываний с часто меняющимися экземплярами хостов и именами (например, AWS или MS Azure) используйте специальные параметры `oneagentctl` для применения пользовательских тегов, имён и метаданных к хостам.

Перечисленные ниже методы `oneagentctl` позволяют редактировать только метаданные, добавленные с помощью самого `oneagentctl` или ранее через конфигурационные файлы. Теги и метаданные, добавленные через Dynatrace или полученные из отслеживаемого окружения (например, теги AWS), не редактируются через `oneagentctl` и не отображаются параметрами `--get-host-tags` и `--get-host-properties`.

### Обнаружение метаданных облака

По умолчанию процесс `oneagentos` автоматически определяет облачные окружения, такие как AWS, Azure и Google Compute Engine. Он отправляет запросы к специальному Metadata API по внутреннему IP-адресу `169.254.169.254`. OneAgent использует полученные метаданные для предоставления дополнительного контекста об отслеживаемых ресурсах в этих окружениях.

### Пользовательское имя хоста

Используйте инструмент командной строки `oneagentctl` с параметром `--set-host-name` для переопределения автоматически обнаруженного имени хоста. Имя хоста не должно содержать символы `<`, `>`, `&`, `CR` (возврат каретки) или `LF` (перевод строки). Максимальная длина: 256 символов.

Эта команда добавляет пользовательское имя хоста для отображения в UI, не изменяя обнаруженное имя. Подробнее см. в разделе [Задание пользовательских имён хостов](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя отслеживаемого хоста.").

Для изменения имени хоста:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=myhostname`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=myhostname`

Для возврата к автоматически определённому имени хоста задайте параметру `--set-host-name` пустое значение: `--set-host-name=""`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=""`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=""`

Изменение может отобразиться в веб-интерфейсе Dynatrace с задержкой до 6 минут.

Использование `--set-host-name` требует перезапуска OneAgent. Добавьте `--restart-service` к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретной ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Для отображения имени хоста:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-name`
* **Windows**:
  `.\oneagentctl.exe --get-host-name`

### Пользовательские метаданные хоста

После настройки пользовательские метаданные отображаются как набор свойств в нижней части раздела **Properties and tags** страницы обзора хоста. Значения свойств не должны содержать символ `=` (если только он не используется как разделитель ключа и значения) или пробельные символы. Максимальная длина: 256 символов, включая разделитель ключа и значения. Имя ключа не должно начинаться с символа `#`.

Для централизованного изменения метаданных хоста из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Настраивайте OneAgent и ActiveGate на хостах со страницы статуса развёртывания или массово через Dynatrace API.") (действие **modify host properties**).

Для версий ниже 1.189 используйте [файл конфигурации метаданных хоста](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-metadata-configuration-file "Узнайте, как задавать теги и дополнительные свойства для отслеживаемого хоста.").

Для **добавления или изменения свойств хоста** выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=AppName --set-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --set-host-property=AppName --set-host-property Environment=Dev`

В одной команде можно добавить или изменить несколько свойств.

Задать контекст безопасности для хоста

Для задания контекста безопасности для хоста используйте следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=dt.security_context=easytrade_sec`
* **Windows**
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`

Для **удаления свойств хоста** выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

В одной команде можно удалить несколько свойств. Если ключ свойства, переданный в команде, не существует, будет возвращён ненулевой код выхода, однако все существующие свойства, указанные в команде, будут удалены. После удаления свойства остаются видимы в Dynatrace до 7 часов.

Для **отображения всех свойств**, настроенных для хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --get-host-properties`
* **Windows**
  `.\oneagentctl.exe --get-host-properties`

### Пользовательские теги хоста

После настройки пользовательские теги хоста отображаются в верхней части раздела **Properties and tags** страницы обзора хоста. Значение свойства не должно содержать `=` (если только он не используется как разделитель ключа и значения) или пробельные символы. Максимальная длина: 256 символов, включая разделитель ключа и значения. Имя ключа не должно начинаться с `#`.

Для централизованного изменения тегов хоста из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Настраивайте OneAgent и ActiveGate на хостах со страницы статуса развёртывания или массово через Dynatrace API.") (действие **modify host tags**).

Для **добавления или изменения тегов хоста** выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`

В одной команде можно добавить или изменить несколько тегов. Допускается задавать теги с одинаковым ключом, но разными значениями.

Для **удаления тегов** выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-tag=role=fallback --remove-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --remove-host-tag=role=fallback --remove-host-tag=Gdansk`

В одной команде можно удалить несколько тегов. Если тег, переданный в команде, не существует, возвращается ненулевой код выхода, однако все существующие теги, указанные в команде, удаляются. После удаления теги остаются видимы в Dynatrace до 6 часов.

Для **отображения всех тегов**, настроенных для хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --get-host-tags`
* **Windows**
  `.\oneagentctl.exe --get-host-tags`

## Режимы мониторинга

Активирует один из режимов мониторинга OneAgent:

* `fullstack`: Full-Stack Monitoring
* `infra-only`: Infrastructure Monitoring
* `discovery`: Discovery

Для включения определённого режима мониторинга установите параметр `--set-monitoring-mode` в одно из следующих значений:

* `fullstack`
* `infra-only`
* `discovery`

Например:

```
--set-monitoring-mode=infra-only
```

Используйте режим Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. При таком подходе доступны данные о состоянии инфраструктуры без данных о производительности приложений или пользователей. Подробнее см. в разделе [Режимы мониторинга](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

### Проверить, какой режим мониторинга включён

Используйте параметр `--get-monitoring-mode` для проверки текущего режима мониторинга:

* **Linux** или **AIX**:
  `./oneagentctl --get-monitoring-mode`
* **Windows**:
  `.\oneagentctl.exe --get-monitoring-mode`

Команда возвращает одно из следующих значений:

* `fullstack`: режим Full-Stack Monitoring
* `infra-only`: режим Infrastructure Monitoring
* `discovery`: режим Discovery

Изменение режима Infrastructure Monitoring требует перезапуска OneAgent, а также перезапуска всех отслеживаемых сервисов. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретной ОС см. в разделах [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

## Автоматическая инъекция в режиме Infrastructure Monitoring

OneAgent версии 1.213

Автоматическая инъекция OneAgent включена по умолчанию в режиме Infrastructure Monitoring. Она необходима для сбора метрик JMX/PMI и обработки Application Security в режиме Infrastructure Monitoring.

Подробнее см. в разделе [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

### Проверить, включена ли автоматическая инъекция

Используйте параметр `get-auto-injection-enabled` для проверки того, включена ли автоматическая инъекция OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-auto-injection-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-auto-injection-enabled`

### Включить или отключить автоматическую инъекцию

Установите параметр `--set-auto-injection-enabled` в `true` или `false` для включения или отключения автоматической инъекции OneAgent:

Для включения автоматической инъекции:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-injection-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-auto-injection-enabled=true`

Для отключения автоматической инъекции:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-injection-enabled=false`
* **Windows**:
  `.\oneagentctl.exe --set-auto-injection-enabled=false`

Подробнее см. в разделе [Отключение автоматической инъекции](/managed/platform/oneagent/monitoring-modes/monitoring-modes#disable-auto-injection "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

## Приём метрик

Локальный приём метрик в настоящее время поддерживается только на Windows и Linux.

Используйте команду `oneagentctl` для проверки или изменения портов взаимодействия, используемых для локального приёма метрик через [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик отслеживаемых сущностей."), [интеграцию сценариев](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной интеграции сценариев."), [Telegraf](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Принимайте метрики Telegraf в Dynatrace.") или [DynatraceStatsd](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Принимайте метрики в Dynatrace с помощью OneAgent и клиента StatsD для ActiveGate."). Изменение порта приёма метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent.

Подробнее см. раздел [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.").

### OneAgent API, интеграция сценариев и Telegraf

Порт приёма метрик по умолчанию: `14499`. При необходимости используйте команду [oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Узнайте, как выполнять задачи настройки OneAgent без переустановки.") для проверки или изменения порта. Изменение порта требует перезапуска OneAgent. Добавьте [`--restart-service`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять задачи настройки OneAgent без переустановки.") к команде для автоматического перезапуска OneAgent.

### Проверить порт приёма метрик

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта приёма метрик (по умолчанию: `14499`).

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Задать пользовательский порт приёма метрик

Используйте параметр `--set-extensions-ingest-port=<arg>` для задания пользовательского локального порта приёма метрик.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Настроить прокси

Настройте прокси хоста так, чтобы разрешить локальный трафик на порт приёма метрик (по умолчанию: `14499`).

### StatsD

### Прослушиватель OneAgent

Порт UDP-прослушивания DynatraceStatsD для прослушивателя OneAgent по умолчанию: `18125`. При необходимости используйте команду [oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Узнайте, как выполнять задачи настройки OneAgent без переустановки.") для проверки или изменения порта приёма метрик. Изменение порта требует перезапуска OneAgent. Добавьте [`--restart-service`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять задачи настройки OneAgent без переустановки.") к команде для автоматического перезапуска OneAgent.

#### Проверить порт приёма метрик

Используйте параметр `--get-extensions-statsd-port` для отображения текущего UDP-порта прослушивания DynatraceStatsd (по умолчанию: `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Задать пользовательский порт приёма метрик

Используйте параметр `--set-extensions-statsd-port=<arg>` для задания пользовательского UDP-порта прослушивания DynatraceStatsd.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Удалённый StatsD

UDP-порт прослушивания DynatraceStatsD для удалённого прослушивателя по умолчанию: `18126`.

Для изменения порта прослушивания `18126` по умолчанию измените параметр `StatsdPort` в файле `extensionsuser.conf` ActiveGate:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Сетевые зоны

Сведения о правилах именования сетевых зон и другая справочная информация: [Сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

Для централизованного изменения назначения сетевой зоны из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Настраивайте OneAgent и ActiveGate на хостах со страницы статуса развёртывания или массово через Dynatrace API.") (действие **modify network zone**).

### Задать сетевую зону

Используйте параметр `--set-network-zone` для настройки взаимодействия OneAgent через указанную сетевую зону. Имя сетевой зоны, это строка буквенно-цифровых символов. Допускается использование дефисов (`-`), знаков подчёркивания (`_`) и точки (`.`) в качестве разделителя. Имя сетевой зоны не должно начинаться с точки. Длина строки ограничена 256 символами. Имена сетевых зон нечувствительны к регистру; Dynatrace хранит их в нижнем регистре. Подробнее см. раздел [именование сетевых зон](/managed/manage/network-zones/network-zones-basic-info#naming "Узнайте, как приступить к работе с сетевыми зонами.")

* На **Linux** или **AIX**:
  `./oneagentctl --set-network-zone=<your.network.zone>`
* На **Windows**:
  `.\oneagentctl.exe --set-network-zone=<your.network.zone>`

#### Сбросить сетевую зону

Для сброса настройки сетевой зоны передайте пустое имя сетевой зоны:

* На **Linux** или **AIX**:
  `./oneagentctl --set-network-zone=""`
* На **Windows**:
  `.\oneagentctl.exe --set-network-zone=""`

### Отобразить настройку сетевой зоны

Используйте параметр `--get-network-zone` для отображения текущей конфигурации сетевой зоны:

* На **Linux** или **AIX**:
  `./oneagentctl --get-network-zone`
* На **Windows**:
  `.\oneagentctl.exe --get-network-zone`

## Передача параметров конфигурации при установке

Параметры `--set-*` можно передавать во время установки. Параметры конфигурации применяются непосредственно перед запуском сервиса OneAgent, перезапуск для их применения не требуется.

Linux и AIX

Windows

Для передачи параметров конфигурации добавьте параметр и укажите значение после знака равенства (`=`). Например:

```
/bin/sh Dynatrace-OneAgent-Linux.sh –-set-host-group=test_group
```

### Установщик EXE

Для передачи параметров конфигурации через EXE-установщик добавьте параметр и укажите значение после знака равенства (`=`). Например:

```
Dynatrace-OneAgent-Windows.exe --set-host-group=test_group
```

### Пакет MSI

Параметры конфигурации можно передать и через MSI-пакет. В этом случае необходимо использовать дополнительный параметр `ADDITIONAL_CONFIGURATION`. Например:

```
Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-host-group=test_group"
```

## Криптографические алгоритмы FIPS 140

OneAgent версии 1.245+

OneAgent использует режим FIPS для соответствия стандарту компьютерной безопасности FIPS 140-3.

### Проверить, включён ли FIPS 140

Используйте `--get-fips-enabled` для проверки того, использует ли OneAgent криптографические алгоритмы, прошедшие валидацию FIPS 140.

* На **Linux** или **AIX**
  `./oneagentctl --get-fips-enabled`
* На **Windows**
  `.\oneagentctl.exe --get-fips-enabled`

### Включить или отключить FIPS 140

Включение или отключение криптографических алгоритмов, прошедших валидацию FIPS 140, возможно только во время установки.

Установите параметр `--set-fips-enabled` в `true` или `false` для включения или отключения криптографических алгоритмов, прошедших валидацию FIPS 140, в OneAgent. Значение по умолчанию при первоначальной установке: `false`.

Для включения режима FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запустите установщик с параметром `--set-fips-enabled=true`

Для отключения режима FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запустите установщик с параметром `--set-fips-enabled==false`

Для включения режима FIPS при развёртывании только приложения перейдите в `/paas/package/agent` и удалите файл `dt_fips_disabled.flag`.

## cap\_setuid для OS Agent

Мониторинг GPFS

OneAgent версии 1.293+

Включение `cap_setuid` для OS Agent необходимо для мониторинга GPFS.

Следующие параметры доступны только в [непривилегированном режиме OneAgent на Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux.").

* `get-osagent-cap-setuid-enabled`
* `set-osagent-cap-setuid-enabled`

Включить `cap_setuid` для OS Agent можно начиная с OneAgent версии 1.293+, однако мониторинг GPFS доступен только с OneAgent версии 1.295+.

### Проверить, включён ли cap\_setuid для OS Agent

Используйте параметр `get-osagent-cap-setuid-enabled` для проверки того, включён ли cap\_setuid для OS Agent:

`./oneagentctl --get-osagent-cap-setuid-enabled`

### Включить или отключить cap\_setuid для OS Agent

Установите параметр `--set-osagent-cap-setuid-enabled` в `true` или `false` для включения или отключения cap\_setuid для OS Agent:

`./oneagentctl --set-osagent-cap-setuid-enabled=true`