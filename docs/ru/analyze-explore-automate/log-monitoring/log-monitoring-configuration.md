---
title: Настройка мониторинга журналов (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration
scraped: 2026-03-05T21:32:34.979418
---

# Конфигурация Log Monitoring (Logs Classic)


Log Monitoring Classic

По умолчанию Log Monitoring активирован в вашей среде Dynatrace. Чтобы начать приём логов, в зависимости от вашего сценария использования, вам необходимо либо настроить правила хранения логов на OneAgent, либо отправлять логи в API приёма данных.

* [Правила приёма логов (Logs Classic)](acquire-log-data/log-storage.md "Configure storage of log files that are already known to OneAgent.")
* [API приёма логов (Logs Classic)](acquire-log-data/logs-classic-ingestion-api.md "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")

Вы можете подтвердить, что Log Monitoring включён, или включить его глобально или на уровне хоста, но проверка статуса и включение или отключение Log Monitoring является необязательной в большинстве случаев. Если вы планируете использовать Log Monitoring, вы можете сосредоточиться на настройках OneAgent, которые непосредственно влияют на работу Log Monitoring.

* [Настройки OneAgent](#lm-oneagent-settings).

## Проверка статуса Log Monitoring

Необязательно

Вы можете проверить, включён ли Log Monitoring в вашей среде Dynatrace глобально (веб-интерфейс Dynatrace) или на уровне хоста (CLI OneAgent).

* Чтобы проверить, включён ли Dynatrace Log Monitoring глобально:

  1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
  2. Найдите **Log Monitoring** в списке поддерживаемых технологий и выберите **Edit** (значок карандаша).
  3. Проверьте, включён ли параметр **Monitor Log Monitoring on every host**.
* Чтобы проверить, включён ли Dynatrace Log Monitoring на уровне хоста:
  Используйте CLI OneAgent и выполните команду `oneagentctl` с параметром `--get-app-log-content-access`, чтобы проверить, включён ли Log Monitoring:

  + Linux: `./oneagentctl --get-app-log-content-access`
  + Windows: `.\oneagentctl.exe --get-app-log-content-access`

## Включение или отключение Log Monitoring

Необязательно

Аналогично проверке статуса Log Monitoring, вы можете включить или отключить Log Monitoring в вашей среде Dynatrace глобально (веб-интерфейс Dynatrace) или на уровне хоста (CLI OneAgent).

* Чтобы активировать Dynatrace Log Monitoring глобально:

  1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
  2. Найдите **Log Monitoring** в списке поддерживаемых технологий и выберите **Edit** (значок карандаша).
  3. Включите параметр **Monitor Log Monitoring on every host**.
* Чтобы включить или отключить Dynatrace Log Monitoring на уровне хоста:
  Используйте CLI OneAgent и выполните команду `oneagentctl` на уровне отдельного хоста.
  Установите параметр `--set-app-log-content-access` в значение `true` или `false`, чтобы включить или отключить Log Monitoring:

  + Linux: `./oneagentctl --set-app-log-content-access=true`
  + Windows: `.\oneagentctl.exe --set-app-log-content-access=true`

  Перезапустите сервис OneAgent для применения изменений.

## Настройки OneAgent

Dynatrace Log Monitoring использует [модуль логов OneAgent](../../discover-dynatrace/get-started/glossary.md#glossary-oneagent-log-module "Get acquainted with Dynatrace terminology."), включённый по умолчанию при всех установках OneAgent. Хотя Log Monitoring не требует специальной конфигурации, вы можете изменить некоторые параметры, доступные для модуля логов OneAgent.

Вы можете настроить:

* Включение и отключение автоматического обнаружения логов для различных технологий.
* Определение часового пояса по умолчанию в контейнерах.
* Включение определения конфигурации хранения через конфигурационный файл на хосте.
* Определение конкретного расположения метки времени и уровня серьёзности во входящих данных логов.
* Определение максимального количества экземпляров групп логов на сущность.

### Глобальные настройки OneAgent для Log Monitoring

1. Перейдите в **Settings** > **Log Monitoring** > **OneAgent settings**.
2. Измените настройки и нажмите **Save changes**.

### Настройки OneAgent для конкретного хоста для Log Monitoring

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и выберите ваш хост Linux.
2. На странице обзора хоста выберите **More** (**...**) > **Settings** в правом верхнем углу страницы.
3. На странице **Host settings** выберите **Log Monitoring** и **Advanced log settings**.
4. Измените настройки и нажмите **Save changes**.

## Настройки OneAgent по умолчанию

## Конфигурационный файл (необязательно)

Конфигурационный файл, расположенный на каждом OneAgent, используется для установки трёх параметров. По соображениям безопасности эти параметры могут быть установлены только на уровне хоста и доступны только через создание JSON-файла в определённом расположении:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\`

Имя конфигурационного файла должно иметь расширение `json`; в остальном имя файла не ограничено.

По умолчанию эти параметры установлены для корректной работы модуля логов OneAgent и автоматического обнаружения файлов логов на конкретном хосте. Изменение этого конфигурационного файла не требуется.

### Несколько конфигурационных файлов

Вы можете иметь несколько JSON-конфигурационных файлов в папке конфигурации. Файлы обрабатываются в алфавитном порядке. Параметры из последнего обработанного файла имеют приоритет.

### Существующие конфигурационные файлы

При обновлении установки OneAgent вы можете обнаружить файл `_migratedloganalytics.conf.json`, содержащий конфигурацию, перенесённую из `ruxitagentloganalytics.conf` на вашем хосте.

Во время установки установщик OneAgent может создать файл `_loganalyticsconf.ctl.json`, который будет содержать параметры, использованные во время установки. Тот же файл будет использоваться для хранения соответствующих параметров, установленных через инструмент OneAgentCtl.

### Доступные параметры

* `AppLogContentAccess`
  Включает доступ к содержимому файла логов на этом хосте. Если установлено значение `false`, файл логов будет отображаться в пользовательском интерфейсе, но содержимое не будет доступно. Обратите внимание, что OneAgent по-прежнему будет автоматически обнаруживать файлы логов, если флаг `AppLogAutoDetection` не установлен в значение `false`.
* `AppLogRemoteConfiguration`
  Включает ручную настройку логов для доступа и мониторинга. Если установлено значение `false`, добавление логов вручную через интерфейс настроек будет невозможно.
* `AppLogAutoDetection`
  Включает автоматическое обнаружение файлов логов на этом хосте. Если установлено значение `false`, логи не будут обнаруживаться автоматически.

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