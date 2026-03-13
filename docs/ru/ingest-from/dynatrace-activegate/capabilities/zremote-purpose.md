---
title: Install the zRemote module for z/OS monitoring
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose
scraped: 2026-03-06T21:25:15.913103
---

# Установка модуля zRemote для мониторинга z/OS

# Установка модуля zRemote для мониторинга z/OS

* Latest Dynatrace
* 1-min read
* Updated on Jul 25, 2020

Модуль zRemote обрабатывает двоичные данные, полученные от [zLocal](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS."), и передаёт эти данные в сжатом и зашифрованном виде через локальный ActiveGate в Dynatrace. Таким образом, модуль zRemote снимает большую часть вычислительной нагрузки с [модулей CICS, IMS и z/OS Java](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS."), возникающей при инструментировании подсистем и приложений, и переносит её на открытую систему.

## Функциональность и модуль zRemote

Если [модуль zRemote](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") включён на ActiveGate, никакой другой функциональный модуль не может быть включён одновременно. Обратите внимание, что модуль zRemote предъявляет более высокие требования к [аппаратному обеспечению и системным ресурсам](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring.").

## Мониторинг z/OS

Для мониторинга LPAR под управлением z/OS, включая такие технологии, как CICS, IMS и Java, требуется ActiveGate с включённым модулем zRemote. Вы можете установить этот ActiveGate на любой операционной системе [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") или [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring."), поддерживаемой ActiveGate.

Мы рекомендуем устанавливать модуль zRemote на мэйнфрейме IBM Z или LinuxONE под управлением поддерживаемой [операционной системы Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes."), чтобы избежать проблем с производительностью или безопасностью при мониторинге z/OS.

Дополнительные сведения и параметры конфигурации см. в разделе [Установка модуля zRemote](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.").
