---
title: Конфигурация Log Monitoring (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration
scraped: 2026-05-12T11:13:28.083958
---

# Конфигурация Log Monitoring (Logs Classic)

# Конфигурация Log Monitoring (Logs Classic)

* Чтение: 5 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

По умолчанию Log Monitoring активирован в окружении Dynatrace. Для начала приёма журналов в зависимости от варианта использования необходимо либо настроить правила хранения журналов на OneAgent, либо отправлять журналы в API приёма.

* [Правила приёма журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Настройте хранение файлов журналов, уже известных OneAgent.")
* [API приёма журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Узнайте, как Dynatrace принимает данные журналов.")

Можно подтвердить, что Log Monitoring включён, или включить/отключить его глобально или на уровне хоста, однако в большинстве случаев это необязательно. При использовании Log Monitoring можно сосредоточиться на настройках OneAgent, которые напрямую влияют на работу Log Monitoring.

## Проверка статуса Log Monitoring

Опционально

Можно проверить, включён ли Log Monitoring в окружении Dynatrace глобально (веб-интерфейс Dynatrace) или на уровне хоста (OneAgent CLI).

* Проверка глобального включения Log Monitoring:

  1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
  2. Найдите **Log Monitoring** в списке поддерживаемых технологий и нажмите **Edit** (значок карандаша).
  3. Проверьте, включена ли опция **Monitor Log Monitoring on every host**.
* Проверка включения Log Monitoring на уровне хоста:
  Используйте OneAgent CLI и выполните команду `oneagentctl` с параметром `--get-app-log-content-access`:

  + Linux: `./oneagentctl --get-app-log-content-access`
  + Windows: `.\oneagentctl.exe --get-app-log-content-access`

## Включение или отключение Log Monitoring

Опционально

* Глобальная активация Log Monitoring:

  1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
  2. Найдите **Log Monitoring** и нажмите **Edit**.
  3. Включите **Monitor Log Monitoring on every host**.
* Включение или отключение Log Monitoring на уровне хоста:
  Используйте OneAgent CLI. Установите параметр `--set-app-log-content-access` в `true` или `false`:

  + Linux: `./oneagentctl --set-app-log-content-access=true`
  + Windows: `.\oneagentctl.exe --set-app-log-content-access=true`

  Перезапустите службу OneAgent для применения изменений.

## Настройки OneAgent

Dynatrace Log Monitoring использует [модуль журналов OneAgent](/managed/discover-dynatrace/get-started/glossary#glossary-oneagent-log-module "Ознакомьтесь с терминологией Dynatrace."), включённый по умолчанию при всех установках OneAgent. Хотя Log Monitoring не требует специфической конфигурации, можно изменять некоторые доступные опции.

Можно настроить:

* Включение и отключение автоматического обнаружения журналов для различных технологий.
* Установку часового пояса по умолчанию в контейнерах.
* Включение конфигурации хранилища через файл конфигурации на хосте.
* Определение конкретного места, где во входящих данных журнала находятся временная метка и серьёзность.
* Определение максимального количества экземпляров групп журналов на сущность.

### Глобальные настройки OneAgent для Log Monitoring

1. Перейдите в **Settings** > **Log Monitoring** > **OneAgent settings**.
2. Настройте параметры и нажмите **Save changes**.

### Специфичные для хоста настройки OneAgent для Log Monitoring

1. Перейдите в **Hosts** и выберите нужный Linux-хост.
2. На странице обзора хоста в правом верхнем углу выберите **More** (**...**) > **Settings**.
3. На странице **Host settings** выберите **Log Monitoring** и **Advanced log settings**.
4. Настройте параметры и нажмите **Save changes**.

## Настройки OneAgent по умолчанию

| Настройка | Описание | По умолчанию |
| --- | --- | --- |
| **Detect open log files** | Автоматически обнаруживает журналы, записываемые важными процессами. | включено |
| **Detect IIS logs** | Позволяет обнаруживать журналы и журналы событий Microsoft IIS. | включено |
| **Detect system logs** | Linux: обнаруживает syslog и журналы сообщений. Windows: обнаруживает системные, прикладные и журналы безопасности. | включено |
| **Detect logs on network file systems** | Обнаруживает журналы, хранящиеся на сервере NFS. Только для Linux. | отключено |
| **Allow OneAgent to monitor OneAgent logs** | Позволяет OneAgent отслеживать собственные журналы. | отключено |
| **Detect logs of containerized applications** | Позволяет обнаруживать сообщения журналов, записываемые в потоки stdout/stderr контейнеризованного приложения. | включено |
| **Set UTC as default timezone in containers** | Устанавливает UTC как часовой пояс по умолчанию для контейнеров. | включено |
| **Timestamp search limit** | Устанавливает поиск временной метки. | `64` байта |
| **Severity search chars limit** | Устанавливает лимит символов поиска серьёзности. | `100` байт |
| **Severity search lines limit** | Устанавливает лимит строк поиска серьёзности. | `2` |
| **Maximum of log group instances per entity limit** | Устанавливает верхний лимит экземпляров группы журналов на запись. | `200` |

## Файл конфигурации (опционально)

Файл конфигурации, расположенный на каждом OneAgent, используется для установки трёх параметров. По соображениям безопасности эти параметры можно задавать только на уровне хоста путём создания JSON-файла в определённом месте:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\`

Имя файла конфигурации должно иметь расширение `json`.

### Несколько файлов конфигурации

Может быть несколько JSON-файлов конфигурации в папке конфигурации. Файлы обрабатываются в алфавитном порядке. Параметры из последнего обработанного файла имеют приоритет.

### Доступные параметры

* `AppLogContentAccess` — включает доступ к содержимому файла журнала на данном хосте. Если `false`, файл журнала будет отображаться в интерфейсе, но содержимое будет недоступно.
* `AppLogRemoteConfiguration` — включает ручную настройку журналов для доступа и мониторинга. Если `false`, нельзя добавлять журналы вручную через интерфейс настроек.
* `AppLogAutoDetection` — включает автообнаружение файлов журналов на данном хосте. Если `false`, журналы не обнаруживаются автоматически.

### Пример

```
{



"agent-configuration": [



{



"AppLogRemoteConfiguration": true,



"AppLogContentAccess": true,



"AppLogAutoDetection": true



}



]



}
```