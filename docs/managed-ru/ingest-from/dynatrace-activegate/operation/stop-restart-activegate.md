---
title: Запуск, остановка и перезапуск ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate
scraped: 2026-05-12T11:37:34.631043
---

# Запуск, остановка и перезапуск ActiveGate

# Запуск, остановка и перезапуск ActiveGate

* 1-min read
* Updated on Apr 06, 2022

Для запуска, остановки или перезапуска ActiveGate необходимо запустить, остановить или перезапустить соответствующие [службы для Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings#services "Узнайте о параметрах по умолчанию, с которыми устанавливается ActiveGate на Linux.") или [службы для Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-default-settings#services "Узнайте о параметрах по умолчанию, с которыми устанавливается ActiveGate на Windows.") в зависимости от операционной системы, на которой установлен ActiveGate. Набор присутствующих служб также зависит от [назначения](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate."), для которого установлен ActiveGate, и от включённых функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.").

Linux

Windows

Для выполнения команд запуска, остановки или перезапуска служб ActiveGate необходимы привилегии root:

* Запуск службы ActiveGate
  `systemctl start <service name>`

  Например:

  ```
  systemctl start dynatracegateway
  ```
* Остановка службы ActiveGate
  `systemctl stop <service name>`

  Например:

  ```
  systemctl stop dynatracegateway
  ```
* Перезапуск службы ActiveGate
  `systemctl restart <service name>`

  Например:

  ```
  systemctl restart dynatracegateway
  ```
* Запрос текущего статуса службы ActiveGate
  `systemctl status <service name>`

  Например:

  ```
  systemctl status dynatracegateway
  ```

#### Службы

| **Название компонента** | **Название службы** | **Описание** |
| --- | --- | --- |
| ActiveGate | `dynatracegateway` | Основная служба ActiveGate. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Автообновление ActiveGate | `dynatraceautoupdater` | Служба автообновления. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Extensions | `extensionsmodule` | Служба для [функционального модуля Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [назначения маршрутизации и мониторинга](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."). Служба может быть активна или неактивна в зависимости от конфигурации. |
| zRemote | `zremote` | Служба для [функционального модуля zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [маршрутизации z/OS-трафика к Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."). |
| Synthetic | `vuc` | Служба для [функционального модуля Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [запуска синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных расположений Synthetic."). |

На Windows запуск и остановку служб ActiveGate можно выполнить через Диспетчер задач Windows на вкладке Службы. Также можно использовать команды:

* Запуск ActiveGate
  `net start "<service_name>"`

  Например:

  ```
  net start "Dynatrace Gateway"
  ```
* Остановка ActiveGate
  `net stop "<service_name>"`

  Например:

  ```
  net stop "Dynatrace Gateway"
  ```

#### Службы

| **Название компонента** | **Название службы** | **Описание** |
| --- | --- | --- |
| ActiveGate | `Dynatrace Gateway` | Основная служба ActiveGate. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Автообновление ActiveGate | `Dynatrace Autoupdater` | Служба автообновления. Присутствует для всех [назначений](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.") и функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить.") ActiveGate. |
| Extensions | `Dynatrace Extensions Controller` | Служба для [функционального модуля Extensions](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#extn2_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [назначения маршрутизации и мониторинга](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Узнайте о возможностях маршрутизации и мониторинга ActiveGate."). Служба может быть активна или неактивна в зависимости от конфигурации. |
| zRemote | `Dynatrace zRemote` | Служба для [функционального модуля zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [маршрутизации z/OS-трафика к Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS."). |
| Synthetic | `Dynatrace Synthetic` | Служба для [функционального модуля Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настроить."). Присутствует на ActiveGate, установленных для [запуска синтетических мониторов из частного расположения](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из частных расположений Synthetic."). |