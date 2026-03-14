---
title: Остановка/перезапуск OneAgent на Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux
scraped: 2026-03-06T21:19:02.259999
---

# Остановка и перезапуск OneAgent в Linux


* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

Если вы не хотите использовать OneAgent в конкретном процессе Java (или другом процессе), вы можете легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:

1. Перейдите в **Settings > Monitoring overview**.
2. Нажмите на вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных объектов.
3. Переведите переключатель **Monitoring** в положение **Off**.
4. Перезапустите все процессы, для которых был отключён мониторинг.

Горячее клонирование

Горячее клонирование в целом не поддерживается OneAgent из-за требований к генерации идентификатора хоста. При горячем клонировании хоста с установленным OneAgent выполните следующие шаги для обеспечения корректной работы:

1. Остановите OneAgent на исходном хосте.
2. Клонируйте хост.
3. Запустите OneAgent.
4. Выполните перезапуск процессов на новом хосте.

## Перезапуск с помощью интерфейса командной строки OneAgent

При использовании параметров `set` необходимо перезапустить службу OneAgent для применения изменений. Вы можете использовать параметр `--restart-service` вместе с командой, которая автоматически инициирует перезапуск. В некоторых случаях также потребуется перезапуск отслеживаемых приложений. Параметр перезапуска можно использовать и самостоятельно, без других параметров. Пример команды приведён ниже.

```
./oneagentctl --set-proxy=my-proxy.com --restart-service
```

Дополнительную информацию см. в разделе [Настройка OneAgent через интерфейс командной строки](../../../oneagent-configuration-via-command-line-interface.md "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Остановка OneAgent с помощью командной строки

Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, вы также можете остановить службу OneAgent с помощью следующей команды:

* для систем с SystemV: `service oneagent stop`
* для систем с systemd: `systemctl stop oneagent`

где `oneagent` — скрипт `init.d` для OneAgent.

Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.

## Запуск OneAgent с помощью командной строки

Чтобы снова запустить Dynatrace OneAgent, используйте следующую команду:

* для систем с SystemV: `service oneagent start`
* для систем с systemd: `systemctl start oneagent`

где `oneagent` — скрипт `init.d` для OneAgent.

Узнайте больше о [взаимодействии Dynatrace с вашей операционной системой](../installation/oneagent-security-linux.md "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").
