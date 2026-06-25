---
title: Параметры установки ActiveGate по умолчанию для Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings
scraped: 2026-05-12T11:25:11.792721
---

# Параметры установки ActiveGate по умолчанию для Linux

# Параметры установки ActiveGate по умолчанию для Linux

* 1-min read
* Updated on Apr 21, 2026

Если во время установки ActiveGate не указаны никакие параметры для настройки, применяются следующие параметры по умолчанию. Для изменения параметров по умолчанию во время установки см. [Настройка установки ActiveGate на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Узнайте о параметрах командной строки для ActiveGate на Linux.").

## Директории

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

## Службы

| **Название компонента** | **Название службы** | **Описание** |
| --- | --- | --- |
| ActiveGate | `dynatracegateway` | Основная служба ActiveGate. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Автообновление ActiveGate | `dynatraceautoupdater` | Служба автообновления. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Extensions | `extensionsmodule` | Служба для [функционального модуля Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [назначения маршрутизации и мониторинга](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."). Служба может быть активна или неактивна в зависимости от конфигурации: настройку по умолчанию см. в описании модуля. |
| zRemote | `zremote` | Служба для [функционального модуля zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [маршрутизации z/OS-трафика к Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."). |
| Synthetic | `vuc` | Служба для [функционального модуля Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [запуска синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных расположений Synthetic."). |

## Учётная запись службы

По умолчанию все службы ActiveGate запускаются от имени выделенного непривилегированного пользователя `dtuserag`. Единственное исключение: `dynatraceautoupdater` требует привилегий root.

Если пользователь `dtuserag` ещё не существует в системе, установщик создаст его.

## Использование портов

По умолчанию ActiveGate:

* принимает подключения от OneAgent или других ActiveGate на порту 9999
* принимает Dynatrace API на порту 9999
* подключается к Dynatrace SaaS или кластеру Managed на порту 443

Подробнее о возможных схемах подключения ActiveGate см. [Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").