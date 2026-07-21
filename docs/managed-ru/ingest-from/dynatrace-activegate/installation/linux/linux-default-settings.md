---
title: Настройки установки ActiveGate по умолчанию для Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings
---

# Настройки установки ActiveGate по умолчанию для Linux

# Настройки установки ActiveGate по умолчанию для Linux

* Чтение: 1 мин
* Обновлено 21 апр. 2026 г.

Если во время установки ActiveGate не указаны параметры для настройки, применяются следующие настройки по умолчанию. Об изменении настроек по умолчанию во время установки см. [Настройка установки ActiveGate на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

## Каталоги

| **Назначение каталога** | **Путь по умолчанию** | **Путь относительно параметра установки** | **Требования к дисковому пространству**  **(если размер не указан, считать менее 1 МБ)** |
| --- | --- | --- | --- |
| Исполняемые файлы, библиотеки и связанные файлы ActiveGate | `/opt/dynatrace/gateway` | `<INSTALL>/gateway` | 600 МБ |
| [Конфигурация ActiveGate](#ag-config) | `/var/lib/dynatrace/gateway/config` | `<CONFIG>/gateway/config` |  |
| Папка SSL ActiveGate | `/var/lib/dynatrace/gateway/ssl` | `<CONFIG>/gateway/ssl` |  |
| Временные файлы ActiveGate | `/var/tmp/dynatrace/gateway` | `<TEMP>/gateway` | 4 ГБ (включая 3 ГБ для кэшированных установщиков и образов контейнеров OneAgent) |
| Логи ActiveGate | `/var/log/dynatrace/gateway` | `<LOG>/gateway` | 1,2 ГБ |
| Файлы дампов, загруженные OneAgent на ActiveGate | `/var/lib/dynatrace/gateway/dump` | `<CONFIG>/gateway/dump` | По умолчанию функциональность отключена. При активации возможен настраиваемый максимальный размер: по умолчанию 100 ГБ. |
| Каталог пакетов ActiveGate для загрузок установщика автообновления | `/var/lib/dynatrace/packages` | `<PACKAGES_DIR>` | 600 МБ |
| Исполняемые файлы, библиотеки и связанные файлы расширений ActiveGate[1](#fn-1-1-def) | `/opt/dynatrace/remotepluginmodule` | `<INSTALL>/` | 2 ГБ |
| Конфигурация, логи, кэш, рабочая область времени выполнения расширений ActiveGate | `/var/lib/dynatrace/remotepluginmodule` | `<CONFIG>/remotepluginmodule` | 2 ГБ (для логов и дампов сбоев) |
| Каталог загрузки расширений ActiveGate | `/opt/dynatrace/remotepluginmodule/plugin_deployment/` | `<INSTALL>/remotepluginmodule/plugin_deployment/` | Зависит от загруженных расширений |
| Исполняемые файлы, библиотеки и связанные файлы zRemote | `/opt/dynatrace/zremote` | `<INSTALL>/zremote` | 50 МБ |
| Изменяемая пользователем постоянная конфигурация zRemote, рабочая область времени выполнения zRemote, отчёты о сбоях | `/var/lib/dynatrace/zremote/agent` | `<CONFIG>/zremote/agent` | 50 МБ |
| Логи zRemote | `/var/log/dynatrace/zremote` | `<LOG>/zremote` | 200 МБ |
| Исполняемые файлы, библиотеки и связанные файлы Private Synthetic | `/opt/dynatrace/synthetic` | `<INSTALL>/synthetic` | 270 МБ |
| Логи Private Synthetic | `/var/log/dynatrace/synthetic` | `<LOG>/synthetic/log` | 1 ГБ |
| Временные файлы Private Synthetic | `/var/tmp/dynatrace/synthetic` | `<TEMP>/synthetic` | 20 ГБ, включая 1 ГБ для `/var/tmp/dynatrace/synthetic/cache` и 1 ГБ для `/var/tmp/dynatrace/synthetic/screenshots`.  Можно [использовать `TEMP` для настройки этого расположения](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#temporary "Learn about the command-line parameters that you can use with ActiveGate on Linux."), однако для ActiveGate с поддержкой Synthetic, установленного на Ubuntu 20.04 LTS и 22.04 LTS более ранних версий, чем 1.331, путь должен начинаться с `/var/tmp`, например `TEMP=/var/tmp/syn`. Dynatrace требует прав на запись в `/var/tmp` для установки snap-пакетов Chromium. |
| Autoupdater | `/opt/dynatrace/autoupdater` | `<INSTALL>/autoupdater` | Включено в оценку для исполняемых файлов ActiveGate |
| Логи Autoupdater | `/var/log/dynatrace/autoupdater` | `<LOG>/autoupdater` | 200 МБ |

1

Чтобы расширения работали корректно, флаг файловой системы должен быть установлен в `exec`, а не в `noexec`. Эта конфигурация критически важна, поскольку она разрешает выполнение бинарных файлов и скриптов в указанной файловой системе. Без этой настройки расширение не сможет выполняться должным образом, что приведёт к возможным ошибкам и сбоям.

## Доступ к каталогу `config` ActiveGate

Для каталога config установлены специфические права доступа для пользователя `dtuserag`. Доступ к этому каталогу требует прав root, поскольку прямой вход в учётную запись `dtuserag` запрещён.

## Службы

|  |  |  |
| --- | --- | --- |
| **Название компонента** | **Название службы** | **Описание** |
| ActiveGate | `dynatracegateway` | Основная служба ActiveGate. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") ActiveGate. |
| Автообновление ActiveGate | `dynatraceautoupdater` | Служба автообновления. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.") ActiveGate. |
| Extensions | `extensionsmodule` | Служба для [функционального модуля Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Присутствует на ActiveGate, установленных для [назначения маршрутизации и мониторинга](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."). Эта служба будет активна или неактивна в зависимости от конфигурации, настройку по умолчанию см. в описании модуля. |
| zRemote | `zremote` | Служба для [функционального модуля zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Присутствует на ActiveGate, установленных для [назначения маршрутизации трафика z/OS на Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."). |
| Synthetic | `vuc` | Служба для [функционального модуля Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."). Присутствует на ActiveGate, установленных для [назначения запуска мониторов Synthetic из частной локации](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations"). |

## Учётная запись службы

Все службы ActiveGate по умолчанию работают от имени выделенного непривилегированного пользователя `dtuserag`. Единственное исключение, `dynatraceautoupdater`, которому требуются права root.

Если пользователь `dtuserag` ещё не существует в системе, установщик создаст его.

## Использование портов

По умолчанию ActiveGate:

* принимает соединения от OneAgent или других ActiveGate на порту 9999
* принимает API Dynatrace на порту 9999
* подключается к Dynatrace SaaS или Managed-кластеру на порту 443

Дополнительную информацию о возможных схемах подключения ActiveGate см. в разделе [Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").