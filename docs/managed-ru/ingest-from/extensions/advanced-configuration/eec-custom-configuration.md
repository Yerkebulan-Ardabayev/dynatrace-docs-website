---
title: Пользовательская конфигурация Extension Execution Controller
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration
scraped: 2026-05-12T12:09:01.926190
---

# Пользовательская конфигурация Extension Execution Controller

# Пользовательская конфигурация Extension Execution Controller

* Практическое руководство
* Чтение: 2 мин
* Обновлено 22 сентября 2025 г.

Extension Execution Controller (EEC) можно использовать в автономном режиме без дополнительной настройки. В этом разделе описана процедура изменения конфигурации EEC.

## Изменение конфигурации EEC

Для изменения конфигурации EEC отредактируйте файл `extensionsuser.conf`, расположенный по следующим путям:

* При использовании ActiveGate (установка по умолчанию):

  + Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* При использовании OneAgent:

  + Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/oneagent/agent/config/extensionsuser.conf`

## Перезапуск службы EEC

После изменения файла `extensionsuser.conf` требуется перезапустить службу EEC:

Linux

Windows

Для перезапуска службы EEC в системе Linux выполните следующие команды:

* Для систем с SystemV:

  ```
  service extensionsmodule stop



  service extensionsmodule start
  ```
* Для систем с systemd:

  ```
  systemctl stop extensionsmodule



  systemctl start extensionsmodule
  ```

Для перезапуска службы EEC в системе Windows запустите **Диспетчер задач** и перезапустите службу `Dynatrace Extensions Controller` либо выполните следующие команды:

```
net stop "Dynatrace Extensions Controller"



net start "Dynatrace Extensions Controller"
```

## Изменение порта для связи с ActiveGate

По умолчанию EEC отправляет данные через порт 9999, используемый ActiveGate.

При изменении порта в файле `custom.properties` ActiveGate необходимо также изменить порт, используемый EEC. Для этого отредактируйте файл `extensionsuser.conf`, заменив `PORT` на целевой порт, и перезапустите службу EEC.

```
Server=https://127.0.0.1:PORT/communication
```

Порт необходимо настроить как для модуля плагинов ActiveGate, так и для EEC.

## Изменение порта EEC для связи с расширением

Этот порт используется для связи между EEC и существующими процессами расширения (источника данных).

Для добавления отредактируйте файл `extensionsuser.conf` и вставьте следующее:

```
ingestport=<new_port>
```

## Включение/отключение расширений с пользовательским кодом для источников данных

Расширения, работающие с конфиденциальными источниками данных, могут значительно расширить функциональность и гибкость пользовательского мониторинга. Однако они также могут создавать потенциальные уязвимости. Отключение пользовательских расширений для таких источников данных существенно снижает риск несанкционированного доступа или утечки данных.

Включение или отключение расширений с пользовательским кодом для источника данных

1. [Измените конфигурацию EEC](#modify-eec), заменив `<DSID>` на идентификатор источника данных, для которого требуется включить или отключить расширения с пользовательским кодом.

   ```
   custom_code_<DSID>_allowed=[True|False]
   ```
2. [Перезапустите службу EEC](#restart-eec).

## Повышение привилегий для локальных расширений в Windows

По умолчанию все локальные расширения в Windows (кроме WMI-расширений, работающих на OneAgent) выполняются с учётной записью LOCAL SERVICE, которая имеет меньше привилегий, чем учётная запись LOCAL SYSTEM, используемая по умолчанию для OneAgent и EEC.

Если расширению требуются повышенные привилегии, его можно вручную настроить для запуска с учётной записью LOCAL SYSTEM.

Откройте файл `extensionsuser.conf` и добавьте параметр `elevated_privileges_extensions` следующим образом:

```
elevated_privileges_extensions=[<extensionName>:<extensionVersion>]
```

Параметр `extensionVersion` может быть конкретной версией в формате `<major>.<minor>.<patch>`, например `1.0.1`, или символом подстановки `*`, указывающим, что все версии данного расширения будут иметь повышенные привилегии.

При добавлении нескольких расширений используйте список, разделённый запятыми.

```
elevated_privileges_extensions=[com.dynatrace.filesystem:*, com.dynatrace.ibm-mq:1.0.1]
```

Повышение привилегий доступно только для расширений Dynatrace; пользовательские расширения не могут быть повышены. Если расширение настроено на выполнение с повышенными привилегиями, но уже запущено (процесс работает), необходимо принудительно перезапустить процесс путём перезапуска службы OneAgent или временного отключения и повторного включения конфигурации мониторинга расширения.

## Связанные темы

* [Разработка собственных расширений](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных расширений в Dynatrace.")