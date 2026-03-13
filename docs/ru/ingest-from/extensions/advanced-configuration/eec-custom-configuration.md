---
title: Extension Execution Controller custom configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/eec-custom-configuration
scraped: 2026-03-06T21:29:48.202555
---

# Пользовательская конфигурация Extension Execution Controller

# Пользовательская конфигурация Extension Execution Controller

* Последняя версия Dynatrace
* Практическое руководство
* 2 мин. чтения
* Обновлено 22 сентября 2025 г.

Extension Execution Controller (EEC) можно использовать автономно, без дополнительных настроек. В этом разделе описано, как изменить конфигурацию EEC.

## Изменение конфигурации EEC

Чтобы изменить конфигурацию EEC, отредактируйте файл `extensionsuser.conf`, который находится по следующему пути:

* При использовании ActiveGate (для установки по умолчанию):

  + Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`
* При использовании OneAgent:

  + Windows: `%PROGRAMDATA%C\dynatrace\oneagent\agent\config\extensionsuser.conf`
  + Linux: `/var/lib/dynatrace/oneagent/agent/config/extensionsuser.conf`

## Перезапуск службы EEC

После изменения файла `extensionsuser.conf` необходимо перезапустить службу EEC:

Linux

Windows

Чтобы перезапустить службу EEC в системе Linux, выполните следующие команды:

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

Чтобы перезапустить службу EEC в системе Windows, откройте **Диспетчер задач** и перезапустите службу `Dynatrace Extensions Controller` либо выполните следующие команды:

```
net stop "Dynatrace Extensions Controller"



net start "Dynatrace Extensions Controller"
```

## Изменение порта для связи с ActiveGate

По умолчанию EEC отправляет данные через порт 9999, который используется ActiveGate.

Если вы изменяете порт с помощью файла `custom.properties` ActiveGate, необходимо также изменить порт, используемый EEC. Для этого отредактируйте файл `extensionsuser.conf`, заменив `PORT` на целевой порт, а затем перезапустите службу EEC.

```
Server=https://127.0.0.1:PORT/communication
```

Порт должен быть настроен как для модуля плагина ActiveGate, так и для EEC.

## Изменение порта EEC для связи с расширением

Этот порт используется для связи между EEC и существующими процессами расширений (источников данных).

Чтобы добавить его, отредактируйте файл `extensionsuser.conf` и вставьте следующее:

```
ingestport=<new_port>
```

## Включение/отключение расширений пользовательского кода для источников данных

Расширения, использующие конфиденциальные источники данных, могут значительно расширить функциональность и гибкость пользовательского мониторинга. Однако они также могут создавать потенциальные уязвимости. Отключение пользовательских расширений для таких конфиденциальных источников данных существенно снижает риск несанкционированного доступа или утечки данных.

Чтобы включить или отключить расширения пользовательского кода для источника данных:

1. [Измените конфигурацию EEC](#modify-eec), заменив `<DSID>` на идентификатор источника данных, для которого необходимо включить или отключить расширения пользовательского кода.

   ```
   custom_code_<DSID>_allowed=[True|False]
   ```
2. [Перезапустите службу EEC](#restart-eec).

## Повышение привилегий для локальных расширений в Windows

По умолчанию все локальные расширения в Windows (кроме WMI, работающих на OneAgent) выполняются с учётной записью LOCAL SERVICE, которая имеет более низкие привилегии, чем учётная запись LOCAL SYSTEM — используемая по умолчанию для OneAgent и EEC.

Если расширению требуются повышенные привилегии, можно вручную настроить его выполнение от имени LOCAL SYSTEM.

Откройте файл `extensionsuser.conf` и добавьте параметр `elevated_privileges_extensions` следующим образом:

```
elevated_privileges_extensions=[<extensionName>:<extensionVersion>]
```

Параметр `extensionVersion` может быть либо конкретной версией в формате `<major>.<minor>.<patch>`, например `1.0.1`, либо символом подстановки `*`, который указывает, что все версии данного расширения будут иметь повышенные привилегии.

При добавлении нескольких расширений используйте список, разделённый запятыми.

```
elevated_privileges_extensions=[com.dynatrace.filesystem:*, com.dynatrace.ibm-mq:1.0.1]
```

Повышать привилегии можно только для расширений Dynatrace; пользовательские расширения не поддерживают это. Если расширение было настроено на запуск с повышенными привилегиями, но уже выполняется (процесс запущен), необходимо принудительно перезапустить процесс — либо перезапустив службу OneAgent, либо временно отключив и повторно включив конфигурацию мониторинга расширения.

## Связанные темы

* [Разработка собственных Extensions](/docs/ingest-from/extensions/develop-your-extensions "Разрабатывайте собственные Extensions в Dynatrace.")
