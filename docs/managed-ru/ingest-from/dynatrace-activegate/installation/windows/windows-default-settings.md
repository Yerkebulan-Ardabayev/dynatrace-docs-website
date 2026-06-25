---
title: Параметры установки ActiveGate по умолчанию для Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings
scraped: 2026-05-12T11:36:29.629318
---

# Параметры установки ActiveGate по умолчанию для Windows

# Параметры установки ActiveGate по умолчанию для Windows

* 1-min read
* Updated on Apr 21, 2026

Если во время установки ActiveGate не указаны никакие параметры для настройки, применяются следующие параметры по умолчанию. Для изменения параметров по умолчанию во время установки см. [Настройка установки ActiveGate на Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate "Узнайте о параметрах для ActiveGate на Windows.").

## Директории

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

## Службы

| **Название компонента** | **Название службы** | **Описание** |
| --- | --- | --- |
| ActiveGate | `Dynatrace Gateway` | Основная служба ActiveGate. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Автообновление ActiveGate | `Dynatrace Autoupdater` | Служба автообновления. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Extensions | `Dynatrace Extensions Controller` | Служба для [функционального модуля Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [назначения маршрутизации и мониторинга](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."). Служба может быть активна или неактивна в зависимости от конфигурации. |
| zRemote | `Dynatrace zRemote` | Служба для [функционального модуля zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [маршрутизации z/OS-трафика к Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."). |
| Synthetic | `Dynatrace Synthetic` | Служба для [функционального модуля Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [запуска синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных расположений Synthetic."). |

## Учётная запись службы

Все службы ActiveGate запускаются от имени непривилегированной учётной записи `Local Service`. Единственное исключение: `Dynatrace Autoupdater` запускается от имени `Local System`.

## Использование портов

По умолчанию ActiveGate:

* принимает подключения от OneAgent или других ActiveGate на порту 9999
* принимает Dynatrace API на порту 9999
* подключается к Dynatrace SaaS или кластеру Managed на порту 443

Подробнее о возможных схемах подключения ActiveGate см. [Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").