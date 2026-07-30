---
title: Установка модуля zRemote для мониторинга z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose
---

# Установка модуля zRemote для мониторинга z/OS

# Установка модуля zRemote для мониторинга z/OS

* 1 минута чтения
* Обновлено 12 июля 2026

Модуль zRemote обрабатывает двоичные данные, поступающие от [zLocal](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS."), и передаёт их в сжатом и зашифрованном виде через локальный ActiveGate в Dynatrace. Таким образом модуль zRemote снимает с [модулей кода CICS, IMS и z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS.") значительную часть вычислительной нагрузки по инструментированию подсистем и приложений, перенося её на открытую систему.

## Функциональность и модуль zRemote

Если на ActiveGate включён [модуль zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Список свойств ActiveGate, которые можно настраивать под конкретные нужды и требования."), другие функциональные модули включить нельзя. Следует учитывать, что модуль zRemote предъявляет более высокие [требования к аппаратному обеспечению и системе](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Подготовка и установка zRemote для мониторинга z/OS.").

ActiveGates с модулем zRemote отображаются в разделе **Deployment Status** > **ActiveGates**.

## Мониторинг z/OS

Для мониторинга z/OS LPAR, включая технологии CICS, IMS и Java, необходим ActiveGate с включённым модулем zRemote. Его можно установить на любую операционную систему [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Аппаратное обеспечение и требования к операционным системам, которые необходимо учитывать перед установкой ActiveGate на Linux для маршрутизации и мониторинга.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#supported-operating-systems "Аппаратное обеспечение и требования к операционным системам, которые необходимо учитывать перед установкой ActiveGate на Windows для маршрутизации и мониторинга."), поддерживаемую ActiveGate.

Рекомендуется устанавливать модуль zRemote на мейнфрейм IBM Z или LinuxONE на поддерживаемой [операционной системе Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Аппаратное обеспечение и требования к операционным системам, которые необходимо учитывать перед установкой ActiveGate на Linux для маршрутизации и мониторинга."), чтобы избежать проблем с производительностью или безопасностью при мониторинге z/OS.

Подробнее об установке и параметрах конфигурации: [Установка модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.").