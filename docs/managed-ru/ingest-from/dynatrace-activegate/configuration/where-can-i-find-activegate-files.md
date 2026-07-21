---
title: Каталоги ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files
---

# Каталоги ActiveGate

# Каталоги ActiveGate

* 1 минута чтения
* Обновлено 07 июля 2026

Linux

Windows

| **Назначение каталога** | **Путь по умолчанию** | **Путь относительно параметра установки** | **Требования к дисковому пространству**  **(если размер не указан, считать менее 1 МБ)** |
| --- | --- | --- | --- |
| Исполняемые файлы, библиотеки и связанные с ними файлы ActiveGate | `/opt/dynatrace/gateway` | `<INSTALL>/gateway` | 600 МБ |
| [Конфигурация ActiveGate](#ag-config) | `/var/lib/dynatrace/gateway/config` | `<CONFIG>/gateway/config` |  |
| Папка SSL ActiveGate | `/var/lib/dynatrace/gateway/ssl` | `<CONFIG>/gateway/ssl` |  |
| Временные файлы ActiveGate | `/var/tmp/dynatrace/gateway` | `<TEMP>/gateway` | 4 ГБ (включая 3 ГБ для кэшированных установщиков OneAgent и образов контейнеров) |
| Логи ActiveGate | `/var/log/dynatrace/gateway` | `<LOG>/gateway` | 1,2 ГБ |
| Файлы дампов, загружаемые в ActiveGate через OneAgent | `/var/lib/dynatrace/gateway/dump` | `<CONFIG>/gateway/dump` | Функциональность по умолчанию отключена. При активации может занимать настраиваемый максимальный размер: по умолчанию 100 ГБ. |
| Каталог пакетов ActiveGate для загрузок установщика автообновления | `/var/lib/dynatrace/packages` | `<PACKAGES_DIR>` | 600 МБ |
| Исполняемые файлы, библиотеки и связанные с ними файлы расширений ActiveGate[1](#fn-1-1-def) | `/opt/dynatrace/remotepluginmodule` | `<INSTALL>/` | 2 ГБ |
| Конфигурация, логи, кэш, рабочая область расширений ActiveGate во время выполнения | `/var/lib/dynatrace/remotepluginmodule` | `<CONFIG>/remotepluginmodule` | 2 ГБ (для логов и дампов сбоев) |
| Каталог загрузки расширений ActiveGate | `/opt/dynatrace/remotepluginmodule/plugin_deployment/` | `<INSTALL>/remotepluginmodule/plugin_deployment/` | В зависимости от загруженных расширений |
| Исполняемые файлы, библиотеки и связанные с ними файлы zRemote | `/opt/dynatrace/zremote` | `<INSTALL>/zremote` | 50 МБ |
| Изменяемая пользователем постоянная конфигурация zRemote,  рабочая область zRemote во время выполнения, отчёты о сбоях | `/var/lib/dynatrace/zremote/agent` | `<CONFIG>/zremote/agent` | 50 МБ |
| Логи zRemote | `/var/log/dynatrace/zremote` | `<LOG>/zremote` | 200 МБ |
| Исполняемые файлы, библиотеки и связанные с ними файлы Private Synthetic | `/opt/dynatrace/synthetic` | `<INSTALL>/synthetic` | 270 МБ |
| Логи private synthetic | `/var/log/dynatrace/synthetic` | `<LOG>/synthetic/log` | 1 ГБ |
| Временные файлы Private Synthetic | `/var/tmp/dynatrace/synthetic` | `<TEMP>/synthetic` | 20 ГБ, включая 1 ГБ для `/var/tmp/dynatrace/synthetic/cache` и 1 ГБ для `/var/tmp/dynatrace/synthetic/screenshots`  Можно [использовать `TEMP` для настройки этого расположения](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#temporary "Learn about the command-line parameters that you can use with ActiveGate on Linux."), однако для ActiveGate с включённым Synthetic, установленного на Ubuntu 20.04 LTS и 22.04 LTS более ранних версий, чем 1.331, путь должен начинаться с `/var/tmp`, например `TEMP=/var/tmp/syn`. Dynatrace требует права на запись в `/var/tmp` для установки snap-пакетов Chromium. |
| Autoupdater | `/opt/dynatrace/autoupdater` | `<INSTALL>/autoupdater` | Включено в оценку для исполняемых файлов ActiveGate |
| Логи Autoupdater | `/var/log/dynatrace/autoupdater` | `<LOG>/autoupdater` | 200 МБ |

1

Чтобы расширения работали корректно, флаг файловой системы должен быть установлен в `exec`, а не в `noexec`. Эта настройка критична, поскольку она разрешает выполнение бинарных файлов и скриптов в указанной файловой системе. Без этой настройки расширение не сможет корректно выполняться, что приведёт к возможным ошибкам и сбоям.

## Доступ к каталогу `config` ActiveGate

Для каталога config заданы особые права доступа для пользователя `dtuserag`. Доступ к этому каталогу требует прав root, поскольку прямой вход в учётную запись `dtuserag` не разрешён.

В Windows каталог `%PROGRAMDATA%` обычно скрыт для непривилегированных пользователей. Поэтому выбрать его через обычный просмотр папок нельзя. Вместо этого, чтобы получить доступ к папке, нужно вставить путь к папке напрямую в адресную строку Windows Explorer.

| **Назначение каталога** | **Путь по умолчанию** | **Путь относительно параметра установки** | **Требования к дисковому пространству**  **(если размер не указан, считать менее 1 МБ)** |
| --- | --- | --- | --- |
| Исполняемые файлы, библиотеки и связанные с ними файлы ActiveGate | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | 600 МБ |
| Конфигурация ActiveGate | `%PROGRAMDATA%\dynatrace\gateway\config` |  |  |
| Папка SSL ActiveGate | `%PROGRAMDATA%\dynatrace\gateway\ssl` |  |  |
| Временные файлы ActiveGate | `%PROGRAMDATA%\dynatrace\gateway\tmp` |  | 4 ГБ (включая 3 ГБ для кэшированных установщиков OneAgent и образов контейнеров) |
| Логи ActiveGate | `%PROGRAMDATA%\dynatrace\gateway\log` |  | 1,2 ГБ |
| Файлы дампов, загружаемые в ActiveGate через OneAgent | `%PROGRAMDATA%\dynatrace\gateway\dump` |  | Функциональность по умолчанию отключена. При активации может занимать настраиваемый максимальный размер: по умолчанию 100 ГБ. |
| Каталог пакетов ActiveGate для загрузок установщика автообновления | `%PROGRAMDATA%\dynatrace\packages` |  | 600 МБ |
| Исполняемые файлы, библиотеки и связанные с ними файлы расширений ActiveGate | `%PROGRAMFILES%\dynatrace\remotepluginmodule` | `<INSTALL>\remotepluginmodule` | 1,2 ГБ |
| Конфигурация, логи, кэш, рабочая область расширений ActiveGate во время выполнения | `%PROGRAMDATA%\dynatrace\remotepluginmodule` |  | 2 ГБ (для логов и дампов сбоев) |
| Каталог загрузки расширений ActiveGate | `%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` | `<INSTALL>\remotepluginmodule\plugin_deployment` | В зависимости от загруженных расширений |
| Исполняемые файлы, библиотеки и связанные с ними файлы zRemote | `%PROGRAMFILES%\dynatrace\zremote` | `<INSTALL>\zremote` | 50 МБ |
| Изменяемая пользователем постоянная конфигурация zRemote,  рабочая область zRemote во время выполнения, отчёты о сбоях | `%PROGRAMDATA%\dynatrace\zremote\agent` |  | 50 МБ |
| Логи zRemote | `%PROGRAMDATA%\dynatrace\zremote\log` |  | 200 МБ |
| Исполняемые файлы, библиотеки и связанные с ними файлы Private Synthetic | `%PROGRAMFILES%\dynatrace\synthetic` | `<INSTALL>\synthetic` | 270 МБ |
| Логи private synthetic | `%PROGRAMDATA%\dynatrace\synthetic\log` |  | 1 ГБ |
| Временные файлы private synthetic | `%PROGRAMDATA%\dynatrace\synthetic` |  | 20 ГБ, включая 1 ГБ для `%PROGRAMDATA%\dynatrace\synthetic\cache` и 1 ГБ для `%PROGRAMDATA%\dynatrace\synthetic\screenshots` |
| Autoupdater | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | Включено в оценку для исполняемых файлов ActiveGate |
| Логи Autoupdater | `%PROGRAMDATA%\dynatrace\autoupdater\log` |  | 200 МБ |