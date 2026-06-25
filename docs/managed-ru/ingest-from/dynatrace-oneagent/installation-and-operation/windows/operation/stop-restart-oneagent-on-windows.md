---
title: Остановка/перезапуск OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows
scraped: 2026-05-12T11:07:37.350189
---

# Остановка/перезапуск OneAgent на Windows

# Остановка/перезапуск OneAgent на Windows

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), можно легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:

1. Перейдите в **Settings > Monitoring overview**.
2. Откройте вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных сущностей.
3. Переведите переключатель **Monitoring** в положение **Off**.
4. Перезапустите все процессы, для которых мониторинг был отключён.

## Перезапуск через интерфейс командной строки OneAgent

При использовании параметров `set` необходимо перезапустить службу OneAgent, чтобы изменения вступили в силу. Можно использовать параметр `--restart-service` с командой, которая запускает перезапуск автоматически. В некоторых случаях также потребуется перезапустить мониторируемые приложения. Параметр перезапуска можно использовать и сам по себе, без других параметров. Пример команды приведён ниже.

```
.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service
```

Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").

## Остановка OneAgent через командную строку

Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, остановить службу OneAgent можно с помощью команды `net stop "Dynatrace OneAgent"`, где `Dynatrace OneAgent` является именем службы OneAgent.

Остановить службу OneAgent через командную строку невозможно, если эта служба является частью другого процесса, например инструментирования байт-кода Java. Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.

## Запуск OneAgent через командную строку

Чтобы снова запустить OneAgent, используйте следующую команду:

`net start "Dynatrace OneAgent"`, где `Dynatrace OneAgent` является именем службы OneAgent.

Подробнее о том, [как Dynatrace взаимодействует с вашей ОС](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").