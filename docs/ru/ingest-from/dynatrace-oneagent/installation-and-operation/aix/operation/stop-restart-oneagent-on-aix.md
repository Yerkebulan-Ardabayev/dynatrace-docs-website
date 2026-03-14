---
title: Остановка/перезапуск OneAgent на AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix
scraped: 2026-03-06T21:18:34.259197
---

# Stop/restart OneAgent on AIX

# Stop/restart OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), вы можете легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:

1. Перейдите в **Settings > Monitoring overview**.
2. Нажмите вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных объектов.
3. Переведите переключатель **Monitoring** в положение **Off**.
4. Перезапустите все процессы, для которых мониторинг был отключён.

## Остановка и запуск OneAgent с помощью командной строки

* [Перезапустите OneAgent через интерфейс командной строки `oneagentctl`](../../../oneagent-configuration-via-command-line-interface.md#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
* Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, вы также можете остановить службу OneAgent с помощью команды оболочки. Сценарий службы `oneagent` находится по пути `<INSTALL_PATH>/agent/initscripts/`.

  Для остановки OneAgent используйте права суперпользователя (root) и выполните сценарий службы `oneagent` с параметром `stop`.

  Если вы остановите службу OneAgent, мониторинг будет отключён до повторного запуска службы.

  Для запуска OneAgent используйте права суперпользователя (root) и выполните сценарий службы `oneagent` с параметром `start`.

Узнайте больше о том, [как OneAgent взаимодействует с вашей ОС](../installation/oneagent-security-aix.md "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").
