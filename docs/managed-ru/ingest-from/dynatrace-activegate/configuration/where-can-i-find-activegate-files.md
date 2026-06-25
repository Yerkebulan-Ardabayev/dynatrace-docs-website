---
title: Директории ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files
scraped: 2026-05-12T11:36:26.148012
---

# Директории ActiveGate

# Директории ActiveGate

* 1-min read
* Updated on Apr 21, 2026

Linux

Windows

> _Reference-таблица ниже на английском._

| **Purpose of directory** | **Default path** | **Path relative to installation parameter** | **Disk space requirements**  **(if size is not given, assume less than 1 MB)** |
| --- | --- | --- | --- |
| ActiveGate executable files, libraries, and related files | `/opt/dynatrace/gateway` | `<INSTALL>/gateway` | 600 MB |
| [ActiveGate configuration](#ag-config) | `/var/lib/dynatrace/gateway/config` | `<CONFIG>/gateway/config` |  |
| ActiveGate SSL folder | `/var/lib/dynatrace/gateway/ssl` | `<CONFIG>/gateway/ssl` |  |
| ActiveGate temporary files | `/var/tmp/dynatrace/gateway` | `<TEMP>/gateway` | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| ActiveGate logs | `/var/log/dynatrace/gateway` | `<LOG>/gateway` | 500 MB |
| Dump files uploaded to ActiveGate by OneAgent | `/var/lib/dynatrace/gateway/dump` | `<CONFIG>/gateway/dump` | Functionality off by default. When activated, can take configurable maximum size: default 100 GB. |
| ActiveGate packages directory for auto-update installer downloads | `/var/lib/dynatrace/packages` | `<PACKAGES_DIR>` | 500 MB. |
| ActiveGate extensions executable files, libraries, and related files[1](#fn-1-1-def) | `/opt/dynatrace/remotepluginmodule` | `<INSTALL>/remotepluginmodule` | 350 MB |
| ActiveGate extensions configuration, logs, cache, run-time work area | `/var/lib/dynatrace/remotepluginmodule` | `<CONFIG>/remotepluginmodule` | 2 GB (for logs and crash dumps) |
| ActiveGate extensions upload directory | `/opt/dynatrace/remotepluginmodule/plugin_deployment/` | `<INSTALL>/remotepluginmodule/plugin_deployment/` | Depending on uploaded extensions |
| zRemote executable files, libraries, and related files | `/opt/dynatrace/zremote` | `<INSTALL>/zremote` | 50 MB |
| zRemote user-modifiable persistent configuration,  zRemote runtime work area, crash reports | `/var/lib/dynatrace/zremote/agent` | `<CONFIG>/zremote/agent` | 50 MB |
| zRemote logs | `/var/log/dynatrace/zremote` | `<LOG>/zremote` | 200 MB |
| Private Synthetic executable files, libraries, and related files | `/opt/dynatrace/synthetic` | `<INSTALL>/synthetic` | 270 MB |
| Private synthetic logs | `/var/log/dynatrace/synthetic` | `<LOG>/synthetic/log` | 1 GB |
| Private Synthetic temporary files | `/var/tmp/dynatrace/synthetic` | `<TEMP>/synthetic` | 20 GB, including 1 GB for the `/var/tmp/dynatrace/synthetic/cache` and 1 GB for `/var/tmp/dynatrace/synthetic/screenshots`  You can [use `TEMP` to customize this location](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#temporary "Learn about the command-line parameters that you can use with ActiveGate on Linux."); however, for Synthetic-enabled ActiveGate installed on Ubuntu 20.04 LTS and 22.04 LTS earlier than 1.331, the path must begin with `/var/tmp`, for example, `TEMP=/var/tmp/syn`. Dynatrace requires write access to `/var/tmp` for the installation of Chromium snap packages. |
| Autoupdater | `/opt/dynatrace/autoupdater` | `<INSTALL>/autoupdater` | Included in estimate for ActiveGate executable files |
| Autoupdater logs | `/var/log/dynatrace/autoupdater` | `<LOG>/autoupdater` | 200 MB |

1

Для корректной работы расширений флаг файловой системы должен быть установлен в `exec`, а не `noexec`. Эта конфигурация необходима, так как позволяет выполнять бинарные файлы и скрипты в указанной файловой системе. Без этой настройки расширение не сможет выполняться корректно, что приведёт к ошибкам и сбоям.

## Доступ к директории `config` ActiveGate

Директория config имеет специфические права доступа для пользователя `dtuserag`. Доступ к ней требует привилегий root, так как прямой вход в учётную запись `dtuserag` не разрешён.

На Windows директория `%PROGRAMDATA%` обычно скрыта для непривилегированных пользователей. Поэтому выбрать её при просмотре папок невозможно. Вместо этого для доступа к папке вставьте путь к ней напрямую в адресную строку Windows Explorer.

> _Reference-таблица ниже на английском._

| **Purpose of directory** | **Default path** | **Path relative to installation parameter** | **Disk space requirements**  **(if size not given, assume less than 1 MB)** |
| --- | --- | --- | --- |
| ActiveGate executable files, libraries,and related files | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | 600 MB |
| ActiveGate configuration | `%PROGRAMDATA%\dynatrace\gateway\config` |  |  |
| ActiveGate SSL folder | `%PROGRAMDATA%\dynatrace\gateway\ssl` |  |  |
| ActiveGate temporary files | `%PROGRAMDATA%\dynatrace\gateway\tmp` |  | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| ActiveGate logs | `%PROGRAMDATA%\dynatrace\gateway\log` |  | 500 MB |
| Dump files uploaded to ActiveGate by OneAgent | `%PROGRAMDATA%\dynatrace\gateway\dump` |  | Functionality off by default. When activated, can take configurable maximum size: default 100 GB. |
| ActiveGate packages directory for auto-update installer downloads | `%PROGRAMDATA%\dynatrace\packages` |  | 500 MB |
| ActiveGate extensions executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\remotepluginmodule` | `<INSTALL>\remotepluginmodule` | 350 MB |
| ActiveGate extensions configuration, logs, cache, run-time work area | `%PROGRAMDATA%\dynatrace\remotepluginmodule` |  | 2 GB (for logs and crash dumps) |
| ActiveGate extensions upload directory | `%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` | `<INSTALL>\remotepluginmodule\plugin_deployment` | Depending on uploaded extensions |
| zRemote executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\zremote` | `<INSTALL>\zremote` | 50 MB |
| zRemote user-modifiable persistent configuration,  zRemote runtime work area, crash reports | `%PROGRAMDATA%\dynatrace\zremote\agent` |  | 50 MB |
| zRemote logs | `%PROGRAMDATA%\dynatrace\zremote\log` |  | 200 MB |
| Private Synthetic executable files, libraries, and related files | `%PROGRAMFILES%\dynatrace\synthetic` | `<INSTALL>\synthetic` | 270 MB |
| Private synthetic logs | `%PROGRAMDATA%\dynatrace\synthetic\log` |  | 1 GB |
| Private synthetic temporary files | `%PROGRAMDATA%\dynatrace\synthetic` |  | 20 GB, including 1 GB for the `%PROGRAMDATA%\dynatrace\synthetic\cache` and 1 GB for `%PROGRAMDATA%\dynatrace\synthetic\screenshots` |
| Autoupdater | `%PROGRAMFILES%\dynatrace\gateway` | `<INSTALL>\gateway` | Included in estimate for ActiveGate executable files |
| Autoupdater logs | `%PROGRAMDATA%\dynatrace\autoupdater\log` |  | 200 MB |