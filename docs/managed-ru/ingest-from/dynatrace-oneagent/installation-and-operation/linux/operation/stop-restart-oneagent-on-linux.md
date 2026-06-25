---
title: Остановка/перезапуск OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux
scraped: 2026-05-12T11:05:22.394739
---

# Остановка/перезапуск OneAgent на Linux

# Остановка/перезапуск OneAgent на Linux

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), можно легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:

1. Перейдите в **Settings > Monitoring overview**.
2. Откройте вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных сущностей.
3. Переведите переключатель **Monitoring** в положение **Off**.
4. Перезапустите все процессы, для которых мониторинг был отключён.

Горячее клонирование

Горячее клонирование, как правило, не поддерживается OneAgent из-за требований к генерации идентификатора хоста. При горячем клонировании хоста с установленным OneAgent выполните следующие шаги, чтобы обеспечить корректную работу:

1. Остановите OneAgent на исходном хосте.
2. Клонируйте хост.
3. Запустите OneAgent.
4. Выполните перезапуск процессов на новом хосте.

## Перезапуск через интерфейс командной строки OneAgent

При использовании параметров `set` необходимо перезапустить службу OneAgent, чтобы изменения вступили в силу. Можно использовать параметр `--restart-service` с командой, которая запускает перезапуск автоматически. В некоторых случаях также потребуется перезапустить мониторируемые приложения. Параметр перезапуска можно использовать и сам по себе, без других параметров. См. пример команды ниже.

```
./oneagentctl --set-proxy=my-proxy.com --restart-service
```

Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").

## Остановка OneAgent через командную строку

Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, можно также остановить службу OneAgent с помощью следующей команды:

* для систем с SystemV: `service oneagent stop`
* для систем с systemd: `systemctl stop oneagent`

где `oneagent` является скриптом `init.d` для OneAgent.

Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.

## Запуск OneAgent через командную строку

Чтобы снова запустить Dynatrace OneAgent, используйте следующую команду:

* для систем с SystemV: `service oneagent start`
* для систем с systemd: `systemctl start oneagent`

где `oneagent` является скриптом `init.d` для OneAgent.

Подробнее о том, [как Dynatrace взаимодействует с вашей ОС](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Linux").