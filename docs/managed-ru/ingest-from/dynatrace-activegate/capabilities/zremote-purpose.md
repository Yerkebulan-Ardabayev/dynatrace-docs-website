---
title: Установка модуля zRemote для мониторинга z/OS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose
scraped: 2026-05-12T11:08:13.083223
---

# Установка модуля zRemote для мониторинга z/OS

# Установка модуля zRemote для мониторинга z/OS

* 1-min read
* Updated on Jul 25, 2020

Модуль zRemote обрабатывает бинарные данные, получаемые от [zLocal](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS."), и маршрутизирует их в сжатом и зашифрованном виде через локальный ActiveGate в Dynatrace. Таким образом, модуль zRemote разгружает значительную часть вычислительной работы [модулей кода CICS, IMS и z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS."), связанной с инструментированием подсистем и приложений, перенося её на открытую систему.

## Функциональность zRemote и модуль

Если [модуль zRemote](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.") включён на ActiveGate, никакой другой функциональный модуль не может быть включён. Обратите внимание, что модуль zRemote предъявляет повышенные [требования к аппаратному обеспечению и системе](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Подготовка и установка zRemote для мониторинга z/OS.").

## Мониторинг z/OS

Для мониторинга LPAR z/OS, включая такие технологии, как CICS, IMS и Java, необходим ActiveGate с включённым модулем zRemote. Этот ActiveGate можно установить на любой поддерживаемой операционной системе [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Узнайте о требованиях к аппаратному обеспечению и операционной системе перед установкой ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#supported-operating-systems "Узнайте о требованиях к аппаратному обеспечению и операционной системе перед установкой ActiveGate на Windows.").

Рекомендуется устанавливать модуль zRemote на мейнфрейм IBM Z или LinuxONE под поддерживаемой [операционной системой Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Узнайте о требованиях к аппаратному обеспечению и операционной системе перед установкой ActiveGate на Linux."), чтобы избежать проблем с производительностью или безопасностью при мониторинге z/OS.

Подробнее о конфигурации смотрите в разделе [Установка модуля zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.").