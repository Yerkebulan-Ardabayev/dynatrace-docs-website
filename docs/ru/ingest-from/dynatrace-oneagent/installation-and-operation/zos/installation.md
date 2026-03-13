---
title: z/OS installation overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation
scraped: 2026-03-06T21:19:48.285337
---

# z/OS installation overview

# z/OS installation overview

* Latest Dynatrace
* 1-min read
* Published Jul 22, 2016

Поскольку модули z/OS требуют нескольких компонентов как в среде мейнфрейма, так и в открытых системах, процесс установки сложнее, чем стандартная установка OneAgent. Однако при должном планировании и координации с различными архитектурными группами установка программных модулей может пройти без затруднений.

Эффективная установка модулей z/OS, как правило, является командной работой с участием следующих специалистов:

* **Администратор открытых систем (Open Systems Administrator)** — устанавливает модуль zRemote.
* **Системный программист мейнфрейма (Mainframe Systems Programmer)** — загружает и устанавливает наборы данных продукта Dynatrace для z/OS.
* **Администратор безопасности мейнфрейма (Mainframe Security Administrator)** — настраивает безопасность для подсистемы zDC.
* **Системный программист мейнфрейма (Mainframe Systems Programmer)** — устанавливает модули для каждой технологии, которую вы хотите мониторить.

В зависимости от состава вашей команды один специалист может выполнять более одной из перечисленных задач.

![z/OS monitoring architecture](https://dt-cdn.net/images/zos-architecture-1745-8d165d1510.png)

## Связанные темы

* [Поддержка технологий](../../../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
