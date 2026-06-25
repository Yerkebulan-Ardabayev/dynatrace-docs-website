---
title: Остановка/перезапуск OneAgent на AIX
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix
scraped: 2026-05-12T11:10:50.109101
---

# Остановка/перезапуск OneAgent на AIX

# Остановка/перезапуск OneAgent на AIX

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), можно легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:

1. Перейдите в **Settings > Monitoring overview**.
2. Откройте вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных сущностей.
3. Переведите переключатель **Monitoring** в положение **Off**.
4. Перезапустите все процессы, для которых мониторинг был отключён.

## Остановка и запуск OneAgent через командную строку

* [Перезапуск OneAgent через интерфейс командной строки `oneagentctl`](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").
* Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, остановить службу OneAgent можно также с помощью команды оболочки. Скрипт службы `oneagent` расположен в `<INSTALL_PATH>/agent/initscripts/`.

  Чтобы остановить OneAgent, с правами root выполните скрипт службы `oneagent` с параметром `stop`.

  Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.

  Чтобы запустить OneAgent, с правами root выполните скрипт службы `oneagent` с параметром `start`.

Подробнее о том, [как OneAgent взаимодействует с вашей ОС](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе AIX.").