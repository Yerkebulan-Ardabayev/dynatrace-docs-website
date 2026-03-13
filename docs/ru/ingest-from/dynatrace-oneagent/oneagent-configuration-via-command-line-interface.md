---
title: Настройка OneAgent через интерфейс командной строки
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface
scraped: 2026-02-06T16:30:55.688261
---

# Настройка OneAgent через интерфейс командной строки

# Настройка OneAgent через интерфейс командной строки

* Последняя версия Dynatrace
* Справочник
* 20 минут чтения
* Обновлено 17 сентября 2025 г.

Используйте интерфейс командной строки `oneagentctl` для выполнения некоторых задач по настройке OneAgent после установки на уровне отдельного хоста.

## Расположение

Расположение инструмента зависит от того, настраивали ли вы установку OneAgent с помощью параметра `<INSTALL_PATH>`:

* **Linux** или **AIX**:
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`
  Требуются права root.
* **Развёртывание на основе Docker**
  `<INSTALL_PATH>/agent/tools`, по умолчанию `/opt/dynatrace/oneagent/agent/tools`
  Обратите внимание, что для развёртывания на основе тома этот путь будет отличаться.
* **Windows**:
  `<INSTALL_PATH>\agent\tools`, по умолчанию `%PROGRAMFILES%\dynatrace\oneagent\agent\tools`
  Требуются права администратора. Если вы попытаетесь запустить `oneagentctl` в консоли Windows без прав администратора, Windows отобразит всплывающее окно контроля учётных записей пользователей и завершит работу с ошибкой.

## Типы параметров

Команда `oneagentctl` принимает параметр `get` для проверки состояния или значения параметра и параметр `set` для изменения параметра. Обратите внимание, что в одной команде можно использовать несколько параметров `set`.

## Перезапуск OneAgent

При использовании параметров `set` необходимо перезапустить службу OneAgent для применения изменений. Параметр `--restart-service` можно использовать с командой, которая вызывает перезапуск автоматически. В некоторых случаях также потребуется перезапустить отслеживаемые приложения. Параметр перезапуска можно также использовать отдельно, без других параметров. Пример команды ниже.

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

## Связь OneAgent

### Задание параметров связи OneAgent

Используйте параметр `--set-server` для задания конечной точки связи OneAgent. Используйте IP-адрес или имя в сочетании с суффиксом `/communication`. В зависимости от вашего развёртывания это может быть Dynatrace Server, Dynatrace Managed Cluster или ActiveGate.

Выполните следующую команду для настройки параметров подключения OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-server=https://my-server.com:9999/communication --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

Чтобы задать несколько конечных точек, разделите их точкой с запятой и заключите в кавычки. Например: `--set-server="https://server1;https://server2"`.

Для этих параметров требуется перезапуск OneAgent, а также перезапуск всех приложений, отслеживаемых с помощью глубоких кодовых модулей. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Эта команда немедленно изменит конечную точку подключения модуля ОС, но кодовые модули не смогут прочитать новый параметр до следующего перезапуска.

OneAgent и Dynatrace Cluster автоматически поддерживают рабочее соединение. Если данные конечной точки изменятся, кластер уведомит OneAgent об изменении, и OneAgent автоматически обновит конечную точку, заданную с помощью `--set-server`, до нового рабочего значения.

Направление трафика OneAgent через ActiveGate

Маршрутизация трафика OneAgent через ActiveGate может повысить безопасность ваших данных, обеспечив их передачу по контролируемым сетевым путям в зашифрованном виде.

1. Определите IP-адрес или имя хоста ActiveGate, который будет обрабатывать трафик.
2. [Задайте конечную точку связи](#set-oneagent-communication-settings).

   Настройте OneAgent, указав ActiveGate в качестве новой конечной точки. Например:

   ```
   .\oneagentctl.exe --set-server=https://<activegate-endpoint>:9999/communication --restart-service
   ```
3. [Проверьте, включено ли автоматическое обновление](#check-if-auto-update-is-enabled).

### Отображение текущих конечных точек связи

Используйте параметр `--get-server` для отображения конечных точек, на которые OneAgent отправляет данные. Это могут быть Dynatrace Server, Dynatrace Managed Cluster или ActiveGate.

* **Linux** или **AIX**:
  `./oneagentctl --get-server`
* **Windows**:
  `.\oneagentctl.exe --get-server`

Начиная с OneAgent версии 1.207, конечные точки отображаются в формате, в котором конечные точки одинакового приоритета сгруппированы в фигурные скобки (`{...}`) и отсортированы согласно приоритету подключения. Звёздочка (`*`) обозначает конечную точку, на которую OneAgent в настоящее время отправляет данные. Конечные точки разделяются точкой с запятой (`;`).
Например:

```
{https://endpoint1.com/communication;https:/10.0.0.0/communication;*https://endpoint3.com/communication}{https://endpoint4.com:9999/communication}
```

### Задание идентификатора среды

Используйте параметр `--set-tenant` для задания [идентификатора среды](/docs/discover-dynatrace/get-started/monitoring-environment "Поймите и научитесь работать со средами мониторинга."). По умолчанию это значение уже установлено правильно. Если вы предоставляете услуги на базе Dynatrace, используйте этот параметр для установки идентификаторов ваших клиентов из пула идентификаторов, приобретённых у Dynatrace.

* **Linux** или **AIX**:
  `./oneagentctl --set-tenant=abc123456`
* **Windows**:
  `.\oneagentctl.exe --set-tenant=abc123456`

Всегда используйте в сочетании с `--set-tenant-token`, который определяет [токен tenant](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен tenant и как его изменить.") для внутренней аутентификации.

### Отображение идентификатора среды

[Идентификатор среды](/docs/discover-dynatrace/get-started/monitoring-environment "Поймите и научитесь работать со средами мониторинга.") Dynatrace, полученный в письме об активации.

Используйте параметр `--get-tenant` для отображения идентификатора среды:

* **Linux** или **AIX**:
  `./oneagentctl --get-tenant`
* **Windows**:
  `.\oneagentctl.exe --get-tenant`

### Задание токена tenant

Используйте параметр `--set-tenant-token` для задания [токена tenant](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Узнайте, что такое токен tenant и как его изменить."), который используется для аутентификации связи с определённой конечной точкой. Всегда используйте в сочетании с `--set-tenant`.

* **Linux** или **AIX**:
  `./oneagentctl --set-tenant-token=abcdefg123456790`
* **Windows**:
  `.\oneagentctl.exe --set-tenant-token=abcdefg123456790`

### Отображение токена tenant

Используйте параметр `--get-tenant-token` для отображения текущего определённого токена:

* **Linux** или **AIX**:
  `./oneagentctl --get-tenant-token`
* **Windows**:
  `.\oneagentctl.exe --get-tenant-token`

### Задание конфигурации прокси

Используйте параметр `--set-proxy` для задания прокси-сервера:

* **Linux** или **AIX**:
  `./oneagentctl --set-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-proxy=my-proxy.com`

### Очистка конфигурации прокси

Используйте параметр `--set-proxy` со значением пустой строки для очистки конфигурации прокси:

* **Linux** или **AIX**:
  `./oneagentctl --set-proxy=`
* **Windows**:
  `.\oneagentctl.exe --set-proxy=`

Перезапустите службу OneAgent для применения изменений.

### Отображение текущего прокси

Используйте параметр `--get-proxy` для отображения текущего определённого прокси, через который подключается OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-proxy`
* **Windows**:
  `.\oneagentctl.exe --get-proxy`

### Исключение определённых IP-адресов из прокси

Используйте параметр `--set-no-proxy` для исключения определённых доменов или IP-адресов из использования прокси:

* **Linux** или **AIX**:
  `./oneagentctl --set-no-proxy=my-proxy.com`
* **Windows**:
  `.\oneagentctl.exe --set-no-proxy=my-proxy.com`

### Отображение текущих параметров no-proxy

Используйте параметр `--get-no-proxy` для просмотра текущих настроек доменов и диапазонов IP-адресов, исключённых из использования прокси:

* **Linux** или **AIX**:
  `./oneagentctl --get-no-proxy`
* **Windows**:
  `.\oneagentctl.exe --get-no-proxy`

### Проверка текущего диапазона портов

OneAgent состоит из различных процессов, взаимодействующих с watchdog через TCP-порт. При запуске watchdog OneAgent пытается открыть первый доступный порт в диапазоне от 50000 до 50100. В некоторых случаях этот порт может потребоваться для ваших собственных приложений, запускаемых после OneAgent.

Используйте параметр `--get-watchdog-portrange` для проверки текущего диапазона портов, определённого для watchdog.

* **Linux** или **AIX**:
  `./oneagentctl --get-watchdog-portrange`
* **Windows**:
  `.\oneagentctl.exe --get-watchdog-portrange`

### Задание нового диапазона портов

Устарело

Начиная с версии OneAgent 1.301, OneAgent не использует порты TCP для собственного межпроцессного взаимодействия. Если OneAgent занимает порты ваших приложений, обновите OneAgent до версии 1.301+.

Watchdog — это двоичный файл, используемый для запуска и мониторинга процессов мониторинга OneAgent:

* `oneagentos` — мониторинг операционной системы
* `oneagentplugin` — мониторинг с использованием [расширений OneAgent](/docs/ingest-from/extensions/develop-your-extensions#oneagent-extensions "Разработайте собственные расширения в Dynatrace.")
* `oneagentextensions` — мониторинг с использованием локальных [расширений](/docs/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими.")
* `oneagentloganalytics` — [мониторинг журналов](/docs/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какие аналитические данные он предоставляет и многое другое.")
* `oneagentnetwork` — [мониторинг сети](/docs/observe/infrastructure-observability/networks "Узнайте, как осуществлять мониторинг сетевых взаимодействий.")

Используйте параметр `--set-watchdog-portrange=arg` для изменения диапазона прослушиваемых портов watchdog на `<arg>`. Аргумент `<arg>` должен содержать два номера портов, разделённых двоеточием (`:`). Например, `50000:50100`. Максимально поддерживаемый диапазон портов — от 1024 до 65535. Диапазон портов должен охватывать не менее 4 портов. Начальный номер порта диапазона должен быть меньше.

* **Linux** или **AIX**:
  `./oneagentctl --set-watchdog-portrange=50000:50100`
* **Windows**:
  `.\oneagentctl.exe --set-watchdog-portrange=50000:50100`

## Автоматические обновления

Дополнительные сведения см. в разделах об обновлении OneAgent для [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Узнайте о различных способах обновления OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Узнайте о различных способах обновления Dynatrace OneAgent на Windows.") и [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/update-oneagent-on-aix "Узнайте, как обновить Dynatrace OneAgent на AIX.").

### Проверка состояния автообновления

Используйте параметр `get-auto-update-enabled` для проверки, включено ли автоматическое обновление OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-auto-update-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-auto-update-enabled`

### Включение или отключение автообновления

Задайте параметр `--set-auto-update-enabled` значением `true` или `false` для отключения или включения автоматического обновления OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-update-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-auto-update-enabled=true`

После использования этой команды для отключения автоматических обновлений вы не сможете управлять автоматическими обновлениями OneAgent через Dynatrace в разделе **Настройки** > **Обновления** > **Обновления OneAgent**.

## Мониторинг журналов

Дополнительные сведения см. в разделе [Мониторинг журналов](/docs/analyze-explore-automate/logs "Управление журналами и аналитика предоставляет унифицированный подход к контролю и изучению данных журналов в Dynatrace.").

### Проверка состояния мониторинга журналов

Используйте параметр `--get-app-log-content-access` для проверки, включён ли мониторинг журналов:

* **Linux**:
  `./oneagentctl --get-app-log-content-access`
* **Windows**:
  `.\oneagentctl.exe --get-app-log-content-access`

### Включение или отключение мониторинга журналов

Задайте параметр `--set-app-log-content-access` значением `true` или `false` для отключения или включения мониторинга журналов:

* **Linux**:
  `./oneagentctl --set-app-log-content-access=true`
* **Windows**:
  `.\oneagentctl.exe --set-app-log-content-access=true`

## Создание архива поддержки

OneAgent версии 1.225+

Если у вас нет доступа к Dynatrace или вы хотите автоматизировать сбор диагностических данных, можно использовать команду `oneagentctl` для сбора [подмножества](#contents) полных данных [диагностики OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как запустить диагностику OneAgent") непосредственно на хосте, где установлен OneAgent. С диагностическими данными, собранными для OneAgent, вы можете:

* Легко собирать диагностические данные для конкретного хоста
* Напрямую предоставлять службе поддержки Dynatrace сведения, необходимые для диагностики проблемы

Для выполнения команды требуется, чтобы служба OneAgent была запущена.

Для создания архива поддержки с диагностическими данными запустите `oneagentctl` с параметром `--create-support-archive`. По умолчанию архив поддержки содержит данные за 7-дневный период и создаётся в текущем рабочем каталоге. Дополнительно можно задать пользовательский каталог и период с помощью параметров `directory` и `days`. Обратите внимание, что `oneagentctl` не создаёт каталог; необходимо указать ему существующий каталог с относительным или абсолютным путём. Например:

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

Все собранные диагностические данные сжимаются в архив `support_archive_agent_YYYY-MM-DD_hhmmss.zip`, который включает следующее подмножество полных данных [диагностики OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как запустить диагностику OneAgent"):

Папка или файл

Описание

`support_archive` (ZIP)

Содержит локальную конфигурацию OneAgent, установленного на хосте или процессе, где была выполнена диагностика, а также файлы журналов, связанные с OneAgent.

`diagnostic_files` (ZIP)

Содержит информацию об обнаружении групп процессов, проблемах с автоматическим внедрением и конфигурации расширений.

## Доступ к системным журналам для проактивной поддержки

OneAgent скачивает определённые системные журналы, чтобы Dynatrace мог диагностировать проблемы, которые могут быть вызваны условиями в вашей среде. Журналы также сохраняются в архиве поддержки. Чаще всего такие проблемы связаны с глубоким мониторингом или установками с автоматическим обновлением.

### Проверка доступа к системным журналам

Используйте параметр `--get-system-logs-access-enabled` для проверки, включён ли доступ к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --get-system-logs-access-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-system-logs-access-enabled`

### Включение или отключение доступа к системным журналам

Задайте параметр `--set-system-logs-access-enabled` значением `true` или `false` для отключения или включения доступа к системным журналам:

* **Linux** или **AIX**:
  `./oneagentctl --set-system-logs-access-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-system-logs-access-enabled=true`
  Перезапустите службу OneAgent для применения изменений.

Обратите внимание, что параметры `--set-system-logs-access-enabled` и `--get-system-logs-access-enabled` относятся к параметру самодиагностики и не связаны с [мониторингом журналов](#log-monitoring).

Отключение доступа к системным журналам ограничивает нашу возможность проактивно диагностировать и решать проблемы. При отозванном доступе к системным журналам вам может потребоваться вручную предоставить Dynatrace содержимое системных журналов для помощи в диагностике проблем в вашей среде.

## Идентификатор хоста

Dynatrace присваивает уникальный идентификатор каждому хосту, отслеживаемому в вашей среде. Идентификаторы хостов можно использовать в качестве параметров в запросах Dynatrace API, например [API топологии и Smartscape — API хостов](/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api "Узнайте, как использовать Dynatrace API для управления отслеживаемыми хостами."). Идентификатор хоста также составляет URL-адрес страницы **Обзор хоста**, например `https://environment.org/#newhosts/hostdetails;id=HOST-6E56EE455C84E232`.

### Отображение идентификатора хоста

Для нахождения идентификатора хоста используйте параметр `--get-host-id`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-id`
* **Windows**:
  `.\oneagentctl.exe --get-host-id`

### Определение источника идентификатора хоста

Доступно на всех поддерживаемых платформах для OneAgent версии 1.223+. Для OneAgent версии 1.221 и более ранних эта функция поддерживается только для Citrix Virtual Apps and Desktops.

Особенно важно сохранять статичность идентификатора хоста в динамических виртуальных средах, где хосты воссоздаются ежедневно.

Чтобы **определить источник для генерации идентификатора хоста**, используйте `--set-host-id-source` и задайте одно из предопределённых значений:

* `auto` — позволить Dynatrace генерировать идентификатор хоста автоматически
* `ip-addresses` — генерировать идентификатор хоста на основе IP-адреса хоста
* `mac-addresses` — генерировать идентификатор хоста на основе MAC-адреса сетевого адаптера хоста
* `fqdn` — генерировать идентификатор хоста на основе полного доменного имени (FQDN) хоста в формате `host.domain`. Если FQDN не содержит символа точки, вместо него используется MAC-адрес сетевого адаптера.
* Если вы отслеживаете несколько сред, можно разделить хосты с одинаковыми IP-адресами, MAC-адресами или FQDN, используя разные пространства имён для каждой среды. Пространство имён может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки; максимальная длина составляет 256 символов.

  + `ip-addresses;namespace=<namespace>`
  + `mac-addresses;namespace=<namespace>`
  + `fqdn;namespace=<namespace>`

Например, чтобы задать источник идентификатора хоста `ip-addresses` и назначить его пространству имён `test`, запустите `oneagentctl` со следующим параметром:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-id-source="ip-addresses;namespace=test"`
* **Windows**:
  `.\oneagentctl.exe --set-host-id-source="ip-addresses;namespace=test"`

После изменения источника идентификатора хоста необходимо перезапустить все отслеживаемые приложения, а затем перезапустить службу OneAgent для создания новой сущности хоста в вашей среде. Параметр `--restart-service` можно использовать с `oneagentctl` для автоматического перезапуска OneAgent или остановить и запустить процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Чтобы **проверить источник идентификатора хоста**, используйте параметр `--get-host-id-source`:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-id-source`
* **Windows**:
  `.\oneagentctl.exe --get-host-id-source`

Для источника идентификатора хоста, установленного в `ip-addresses` и пространства имён `test`, команда вернёт следующий результат:

```
ip-addresses;namespace=test
```

## Группы хостов

Обзор использования групп хостов см. в разделе [Организация среды с помощью групп хостов](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.").

Кроме того, для централизованного изменения назначения группы хостов из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/docs/ingest-from/bulk-configuration#configure-oneagents "Выполняйте настройку OneAgent и ActiveGate на хостах со страницы состояния развёртывания или в большом масштабе с помощью Dynatrace API.") (выберите действие **изменить группу хостов**).

### Изменение назначения группы хостов

Используйте параметр `--set-host-group` для изменения назначения группы хостов.

Для включения хоста в `MyHostGroup`:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-group=MyHostGroup`
* **Windows**:
  `.\oneagentctl.exe --set-host-group=MyHostGroup`

Требования к строке группы хостов:

* Может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки
* Не должна начинаться с `dt.`
* Максимальная длина — 100 символов

Использование `--set-host-group` требует перезапуска OneAgent, а также перезапуска всех отслеживаемых сервисов. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Изменение назначений групп хостов приводит к пересчёту идентификаторов групп процессов, что влияет на агрегацию данных. Дополнительные сведения о влиянии изменений группы хостов на обнаружение групп процессов см. в разделе [Организация среды с помощью групп хостов](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#how-host-groups-affect-your-monitoring-environment "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.").

### Очистка назначения группы хостов

Используйте параметр `--set-host-group` с пустым значением для очистки назначения группы хостов:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-group=`
* **Windows**:
  `.\oneagentctl.exe --set-host-group=`

### Отображение назначения группы хостов

Используйте параметр `--get-host-group` для отображения текущего назначения группы хостов:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-group`
* **Windows**:
  `.\oneagentctl.exe --get-host-group`

## Теги и метаданные хостов

В динамических или крупных средах ручная разметка хостов тегами может быть непрактичной. Для динамических развёртываний, включающих часто изменяющиеся экземпляры и имена хостов (например, AWS или MS Azure), можно использовать специальные параметры `oneagentctl` для применения пользовательских тегов, имён и метаданных к хостам.

Методы `oneagentctl`, перечисленные ниже, позволяют редактировать только метаданные, добавленные с помощью самого `oneagentctl` или ранее с помощью файлов конфигурации. Теги и метаданные, добавленные с помощью Dynatrace, а также полученные из отслеживаемой среды (например, теги AWS), не редактируются с помощью `oneagentctl` и не будут отображаться при использовании параметров `--get-host-tags` и `--get-host-properties`.

### Обнаружение облачных метаданных

По умолчанию процесс `oneagentos` автоматически обнаруживает облачные среды, такие как AWS, Azure и Google Compute Engine. Он отправляет запросы в специальный Metadata API по внутреннему IP-адресу `169.254.169.254`. OneAgent использует полученные метаданные для предоставления дополнительного контекста об отслеживаемых ресурсах в этих средах.

### Пользовательское имя хоста

Используйте инструмент командной строки `oneagentctl` с параметром `--set-host-name` для переопределения автоматически определённого имени хоста. Имя хоста не должно содержать символы `<`, `>`, `&`, `CR` (возврат каретки) или `LF` (перевод строки). Максимальная длина составляет 256 символов.

Эта команда добавляет пользовательское имя хоста для отображения в интерфейсе, но определённое имя хоста не изменяется. Подробнее см. в разделе [Задание пользовательских имён хостов](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя отслеживаемого хоста.").

Для изменения имени хоста:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=myhostname`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=myhostname`

Для возврата к автоматически определённому имени хоста задайте параметр `--set-host-name` пустым значением, например `--set-host-name=""`. Например:

* **Linux** или **AIX**:
  `./oneagentctl --set-host-name=""`
* **Windows**:
  `.\oneagentctl.exe --set-host-name=""`

Изменение может не отразиться в веб-интерфейсе Dynatrace в течение до 6 минут.

Использование `--set-host-name` требует перезапуска OneAgent. Добавьте `--restart-service` к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

Для отображения имени хоста:

* **Linux** или **AIX**:
  `./oneagentctl --get-host-name`
* **Windows**:
  `.\oneagentctl.exe --get-host-name`

### Пользовательские метаданные хоста

После настройки пользовательские метаданные отображаются как набор свойств в нижней части раздела **Свойства и теги** на странице обзора хоста. Значения свойств не должны содержать символ `=` (если только он не используется как разделитель ключ-значение) или пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключ-значение. Имя ключа не должно начинаться с символа `#`.

Кроме того, для централизованного изменения метаданных хоста из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/docs/ingest-from/bulk-configuration#configure-oneagents "Выполняйте настройку OneAgent и ActiveGate на хостах со страницы состояния развёртывания или в большом масштабе с помощью Dynatrace API.") (выберите действие **изменить свойства хоста**).

Для версий ранее 1.189 используйте [файл конфигурации метаданных хоста](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#edit-the-host-metadata-configuration-file "Узнайте, как пометить тегами и задать дополнительные свойства для отслеживаемого хоста.").

Чтобы **добавить или изменить свойства хоста**, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=AppName --set-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --set-host-property=AppName --set-host-property Environment=Dev`

В одной команде можно добавить или изменить несколько свойств.

Задание контекста безопасности для хоста

Для задания контекста безопасности для вашего хоста используйте следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-property=dt.security_context=easytrade_sec`
* **Windows**
  `.\oneagentctl.exe --set-host-property=dt.security_context=easytrade_sec`

`dt.security_context` используется несколькими функциями в Dynatrace, такими как [контекст безопасности журналов](/docs/analyze-explore-automate/logs/lma-security-context "Используйте Dynatrace на базе Grail и DQL для преобразования входящих данных журналов для лучшего понимания, анализа или дальнейшей обработки.") и [контекст безопасности бизнес-событий](/docs/observe/business-observability/bo-event-processing/bo-security-context "Используйте Dynatrace на базе Grail и DQL для преобразования входящих данных бизнес-событий для лучшего понимания, анализа или дальнейшей обработки.").
Кроме того, если вы являетесь администратором учётной записи и хотите предоставить доступ к отслеживаемым сущностям на основе их контекста безопасности, см. раздел [Предоставление доступа к сущностям с контекстом безопасности](/docs/manage/identity-access-management/use-cases/access-security-context "Предоставьте доступ к сущностям с контекстом безопасности").

Чтобы **удалить свойства хоста**, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-property=AppName --remove-host-property=Environment=Dev`
* **Windows**
  `.\oneagentctl.exe --remove-host-property=AppName --remove-host-property=Environment=Dev`

Одной командой можно удалить несколько свойств. Если ключ свойства, переданный в команде, не существует, будет возвращён ненулевой код выхода, но все существующие свойства, переданные в команде, будут удалены. После удаления свойств хоста они остаются видимыми в Dynatrace до 7 часов.

Чтобы **отобразить все свойства**, настроенные для хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --get-host-properties`
* **Windows**
  `.\oneagentctl.exe --get-host-properties`

### Пользовательские теги хоста

После настройки пользовательских тегов хоста они отображаются в верхней части раздела **Свойства и теги** на странице обзора хоста. Значение свойства не должно содержать символ `=` (если только он не используется как разделитель ключ-значение) или пробельные символы. Максимальная длина составляет 256 символов, включая разделитель ключ-значение. Имя ключа не должно начинаться с `#`.

Кроме того, для централизованного изменения тегов хоста из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/docs/ingest-from/bulk-configuration#configure-oneagents "Выполняйте настройку OneAgent и ActiveGate на хостах со страницы состояния развёртывания или в большом масштабе с помощью Dynatrace API.") (выберите действие **изменить теги хоста**).

Чтобы **добавить или изменить теги хоста**, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --set-host-tag=TestHost --set-host-tag=role=fallback --set-host-tag=Gdansk`

В одной команде можно добавить или изменить несколько тегов. Допускается определение тегов с одинаковым ключом, но разными значениями.

Чтобы **удалить теги**, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --remove-host-tag=role=fallback --remove-host-tag=Gdansk`
* **Windows**
  `.\oneagentctl.exe --remove-host-tag=role=fallback --remove-host-tag=Gdansk`

Одной командой можно удалить несколько тегов. Если тег, переданный в команде, не существует, возвращается ненулевой код выхода, но все существующие теги, переданные в команде, удаляются. После удаления тегов они остаются видимыми в Dynatrace до 6 часов.

Чтобы **отобразить все теги**, настроенные для хоста, выполните следующую команду:

* **Linux** и **AIX**
  `./oneagentctl --get-host-tags`
* **Windows**
  `.\oneagentctl.exe --get-host-tags`

## Режимы мониторинга

Активирует один из режимов мониторинга OneAgent:

* `fullstack`: Мониторинг полного стека
* `infra-only`: Мониторинг инфраструктуры
* `discovery`: Обнаружение

Чтобы включить определённый режим мониторинга, задайте параметр `--set-monitoring-mode` в одно из следующих значений:

* `fullstack`
* `infra-only`
* `discovery`

Например:

```
--set-monitoring-mode=infra-only
```

Используйте режим мониторинга инфраструктуры или режим обнаружения вместо режима мониторинга полного стека. При таком подходе вы получаете данные о работоспособности инфраструктуры без данных о производительности приложений или пользователей. Подробнее см. в разделе [Режимы мониторинга](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Узнайте, что входит в режим мониторинга инфраструктуры Dynatrace.").

### Проверка включённого режима мониторинга

Используйте параметр `--get-monitoring-mode` для проверки включённого режима мониторинга:

* **Linux** или **AIX**:
  `./oneagentctl --get-monitoring-mode`
* **Windows**:
  `.\oneagentctl.exe --get-monitoring-mode`

Команда возвращает одно из следующих значений:

* `fullstack`: режим мониторинга полного стека
* `infra-only`: режим мониторинга инфраструктуры
* `discovery`: режим обнаружения

Изменение режима мониторинга инфраструктуры требует перезапуска OneAgent, а также перезапуска всех отслеживаемых сервисов. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent (версия 1.189+) или остановите и запустите процесс OneAgent вручную. Инструкции для конкретных ОС см. в разделах [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux "Узнайте, как остановить и перезапустить OneAgent на Linux."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.") или [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix "Узнайте, как остановить и перезапустить OneAgent на AIX.").

## Автоматическое внедрение для режима мониторинга инфраструктуры

OneAgent версии 1.213

Автоматическое внедрение OneAgent включено по умолчанию в режиме мониторинга инфраструктуры. Оно необходимо для сбора метрик JMX/PMI и обработки Application Security в режиме мониторинга инфраструктуры.

Дополнительные сведения см. в разделе [Режимы мониторинга инфраструктуры и обнаружения](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Узнайте, что входит в режим мониторинга инфраструктуры Dynatrace.").

### Проверка состояния автоматического внедрения

Используйте параметр `get-auto-injection-enabled` для проверки, включено ли автоматическое внедрение OneAgent:

* **Linux** или **AIX**:
  `./oneagentctl --get-auto-injection-enabled`
* **Windows**:
  `.\oneagentctl.exe --get-auto-injection-enabled`

### Включение или отключение автоматического внедрения

Задайте параметр `--set-auto-injection-enabled` значением `true` или `false` для включения или отключения автоматического внедрения OneAgent:

Для включения автоматического внедрения:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-injection-enabled=true`
* **Windows**:
  `.\oneagentctl.exe --set-auto-injection-enabled=true`

Для отключения автоматического внедрения:

* **Linux** или **AIX**:
  `./oneagentctl --set-auto-injection-enabled=false`
* **Windows**:
  `.\oneagentctl.exe --set-auto-injection-enabled=false`

Дополнительные сведения см. в разделе [Отключение автоматического внедрения](/docs/observe/infrastructure-observability/hosts/monitoring-modes#disable-auto-injection "Узнайте, что входит в режим мониторинга инфраструктуры Dynatrace.").

## Приём метрик

Локальный приём метрик в настоящее время поддерживается только на Windows и Linux.

Команда `oneagentctl` позволяет проверять или изменять порты связи, используемые для локального приёма метрик через [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте Dynatrace API для получения метрик отслеживаемых объектов."), [интеграцию со скриптами](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной интеграции со скриптами."), [Telegraf](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Принимайте метрики Telegraf в Dynatrace.") или [DynatraceStatsd](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Принимайте метрики в Dynatrace с помощью клиента OneAgent и ActiveGate StatsD."). Изменение порта приёма метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](#oneagent-restart) к команде для автоматического перезапуска OneAgent.

Дополнительные сведения см. в разделе [Приём метрик](/docs/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.").

### OneAgent API, интеграция со скриптами и Telegraf

Порт приёма метрик по умолчанию — `14499`. При необходимости можно использовать команду [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Узнайте, как выполнять некоторые задачи по настройке OneAgent без необходимости его переустановки.") для проверки или изменения порта. Изменение порта приёма метрик требует перезапуска OneAgent. Добавьте [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять некоторые задачи по настройке OneAgent без необходимости его переустановки.") к команде для автоматического перезапуска OneAgent.

### Проверка порта приёма

Используйте параметр `--get-extensions-ingest-port` для отображения текущего локального порта приёма (по умолчанию `14499`).

* **Linux**, **AIX**:
  `./oneagentctl --get-extensions-ingest-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-ingest-port`

### Задание пользовательского порта приёма

Используйте параметр `--set-extensions-ingest-port=<arg>` для задания пользовательского локального порта приёма.

* **Linux**, **AIX**:
  `./oneagentctl --set-extensions-ingest-port=14499 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-ingest-port=14499 --restart-service`

### Настройка прокси

Настройте прокси вашего хоста для разрешения трафика localhost, направляемого на порт приёма метрик (по умолчанию `14499`).

### StatsD

### Прослушиватель OneAgent

Порт UDP-прослушивания DynatraceStatsD для прослушивателя OneAgent по умолчанию — `18125`. При необходимости можно использовать команду [oneagentctl](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#metrics "Узнайте, как выполнять некоторые задачи по настройке OneAgent без необходимости его переустановки.") для проверки или изменения порта приёма метрик. Изменение порта требует перезапуска OneAgent. Добавьте [`--restart-service`](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять некоторые задачи по настройке OneAgent без необходимости его переустановки.") к команде для автоматического перезапуска OneAgent.

#### Проверка порта приёма

Используйте параметр `--get-extensions-statsd-port` для отображения текущего UDP-порта прослушивания DynatraceStatsd (по умолчанию `18125`).

* **Linux**:
  `./oneagentctl --get-extensions-statsd-port`
* **Windows**:
  `.\oneagentctl.exe --get-extensions-statsd-port`

#### Задание пользовательского порта приёма

Используйте параметр `--set-extensions-statsd-port=<arg>` для задания пользовательского UDP-порта прослушивания DynatraceStatsd.

* **Linux**:
  `./oneagentctl --set-extensions-statsd-port=18125 --restart-service`
* **Windows**:
  `.\oneagentctl.exe --set-extensions-statsd-port=18125 --restart-service`

### Удалённый StatsD

Порт UDP-прослушивания DynatraceStatsD для удалённого прослушивателя по умолчанию — `18126`.

Для изменения порта прослушивания по умолчанию `18126` измените параметр `StatsdPort` в файле `extensionsuser.conf` ActiveGate:

* Linux
  `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* Windows
  `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`:

```
StatsdPort=18126
```

## Сетевые зоны

Сведения о правилах именования сетевых зон и другую справочную информацию см. в разделе [Сетевые зоны](/docs/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

Кроме того, для централизованного изменения назначения сетевой зоны из Dynatrace Cluster можно использовать [удалённое управление конфигурацией](/docs/ingest-from/bulk-configuration#configure-oneagents "Выполняйте настройку OneAgent и ActiveGate на хостах со страницы состояния развёртывания или в большом масштабе с помощью Dynatrace API.") (выберите действие **изменить сетевую зону**).

### Задание сетевой зоны

Используйте параметр `--set-network-zone` для указания OneAgent осуществлять связь через указанную сетевую зону. Имя сетевой зоны — это строка буквенно-цифровых символов. Можно также использовать дефисы (`-`), символы подчёркивания (`_`) и точку (`.`) в качестве разделителя. Имя сетевой зоны не должно начинаться с точки. Длина строки ограничена 256 символами. Имена сетевых зон нечувствительны к регистру. Dynatrace хранит эти имена в нижнем регистре. Дополнительные сведения см. в разделе [именование сетевых зон](/docs/manage/network-zones/network-zones-basic-info#naming "Узнайте основы сетевых зон.").

* На **Linux** или **AIX**:
  `./oneagentctl --set-network-zone=<your.network.zone>`
* На **Windows**:
  `.\oneagentctl.exe --set-network-zone=<your.network.zone>`

#### Сброс сетевой зоны

Можно сбросить параметр сетевой зоны, передав пустое имя сетевой зоны:

* На **Linux** или **AIX**:
  `./oneagentctl --set-network-zone=""`
* На **Windows**:
  `.\oneagentctl.exe --set-network-zone=""`

### Отображение параметра сетевой зоны

Используйте параметр `--get-network-zone` для отображения текущей конфигурации сетевой зоны:

* На **Linux** или **AIX**:
  `./oneagentctl --get-network-zone`
* На **Windows**:
  `.\oneagentctl.exe --get-network-zone`

## Передача параметров конфигурации при установке

Параметры `--set-*` можно передавать во время установки. Параметры конфигурации применяются непосредственно перед запуском службы OneAgent, и для применения конфигурации не требуется её перезапускать.

Linux и AIX

Windows

Для передачи параметров конфигурации просто добавьте параметр и предварите значение знаком равенства (`=`). Например:

```
/bin/sh Dynatrace-OneAgent-Linux.sh --set-host-group=test_group
```

### EXE-установщик

Для передачи параметров конфигурации через EXE-установщик просто добавьте параметр и предварите значение знаком равенства (`=`). Например:

```
Dynatrace-OneAgent-Windows.exe --set-host-group=test_group
```

### Пакет MSI

Параметры конфигурации также можно передавать через пакет MSI. Однако на этот раз необходимо использовать дополнительный параметр `ADDITIONAL_CONFIGURATION`. Например:

```
Dynatrace-OneAgent-Windows.msi ADDITIONAL_CONFIGURATION="--set-host-group=test_group"
```

## Криптографические алгоритмы FIPS 140

OneAgent версии 1.245+

OneAgent использует режим FIPS для соответствия стандарту компьютерной безопасности FIPS 140-3.

### Проверка состояния FIPS 140

Используйте параметр `--get-fips-enabled` для проверки, использует ли OneAgent криптографические алгоритмы, соответствующие FIPS 140.

* На **Linux** или **AIX**
  `./oneagentctl --get-fips-enabled`
* На **Windows**
  `.\oneagentctl.exe --get-fips-enabled`

### Включение или отключение FIPS 140

Включение или отключение криптографических алгоритмов, соответствующих FIPS 140, можно выполнить только во время установки.

Задайте параметр `--set-fips-enabled` значением `true` или `false` для включения или отключения криптографических алгоритмов FIPS 140 в OneAgent. Значение по умолчанию для первой установки — `false`.

Для включения режима FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запустите установщик с `--set-fips-enabled=true`

Для отключения режима FIPS:

* На **Linux**, **AIX** или **Windows**:
  Запустите установщик с `--set-fips-enabled==false`

Если вы хотите включить режим FIPS для развёртывания только приложения, перейдите в `/paas/package/agent` и удалите `dt_fips_disabled.flag`.

## cap\_setuid для агента ОС

Мониторинг GPFS

OneAgent версии 1.293+

Включение `cap_setuid` для агента ОС требуется для мониторинга GPFS.

Следующие параметры доступны только в [непривилегированном режиме OneAgent на Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Узнайте, когда Dynatrace OneAgent требует привилегий root на Linux.").

* `get-osagent-cap-setuid-enabled`
* `set-osagent-cap-setuid-enabled`

Включить `cap_setuid` для агента ОС можно начиная с OneAgent версии 1.293+, но использовать мониторинг GPFS можно только начиная с OneAgent версии 1.295+.

### Проверка состояния cap\_setuid для агента ОС

Используйте параметр `get-osagent-cap-setuid-enabled` для проверки, включён ли cap\_setuid для агента ОС:

`./oneagentctl --get-osagent-cap-setuid-enabled`

### Включение или отключение cap\_setuid для агента ОС

Задайте параметр `--set-osagent-cap-setuid-enabled` значением `true` или `false` для отключения или включения cap\_setuid для агента ОС:

`./oneagentctl --set-osagent-cap-setuid-enabled=true`
