---
title: Группа ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-group
scraped: 2026-05-12T11:37:35.788222
---

# Группа ActiveGate

# Группа ActiveGate

* 2-min read
* Updated on Feb 24, 2026

Группы ActiveGate можно использовать для массовых действий над ActiveGate, таких как управление [расширениями](/managed/ingest-from/extensions/develop-your-extensions "Разработайте собственные расширения в Dynatrace."), запущенными на ActiveGate, или подключение [фондов Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Включите мониторинг ваших фондов Cloud Foundry.").

## Требования

* Имя группы ActiveGate — строка из буквенно-цифровых символов, дефисов (`-`), подчёркиваний (`_`) и точек (`.`).
* Точки используются как разделители, поэтому нельзя использовать точку в качестве первого символа имени группы.
* Длина строки ограничена 256 символами.

## Назначение ActiveGate в группу

ActiveGate может принадлежать только одной группе. По умолчанию ActiveGate назначается в группу `default`. Назначить ActiveGate в группу можно во время или после установки.

### Назначение в группу во время установки

Для назначения ActiveGate в группу используйте параметр установки `--set-group` во время установки. Обратите внимание, что этот параметр нельзя использовать при обновлении ActiveGate. Например:

Linux

Windows

```
/bin/bash Dynatrace-ActiveGate-Linux-x86-<version>.sh --set-group=my-group
```

```
Dynatrace-ActiveGate-Windows-x86-<version>.exe --set-group=my-group
```

### Назначение в группу после установки

Для назначения ActiveGate в группу можно использовать [удалённое управление конфигурацией](/managed/ingest-from/bulk-configuration#configure-activegates "Выполняйте конфигурацию OneAgent и ActiveGate на хостах со страницы статуса развёртывания или в масштабе через Dynatrace API.") (выберите действие **modify ActiveGate group**).

Альтернативно, назначить ActiveGate в группу можно с помощью [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#group "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки.") или путём редактирования файла `custom.properties`:

agctl

custom.properties

ActiveGate версии 1.333+

```
agctl group set mygroup
```

После назначения ActiveGate в группу с помощью `agctl` необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") для вступления изменений в силу.

1. Отредактируйте файл `custom.properties` в [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.") и настройте параметр `group` в разделе `[collector]`. Например:

   ```
   [collector]



   group = mygroup
   ```

   Подробнее смотрите в разделе [Основные правила работы с конфигурацией ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#basic-rules "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.").
2. Сохраните файл `custom.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").

## Расширения

ActiveGate, запускающий удалённое расширение, должен принадлежать группе ActiveGate, поскольку Dynatrace использует группу для указания расширению, где оно должно запускаться. Если вы планируете использовать один ActiveGate для запуска удалённого расширения, назначьте его в выделенную группу, содержащую только этот ActiveGate.

При активации расширения необходимо указать группу ActiveGate, которая будет запускать расширение. Группу ActiveGate можно выбрать в рамках рабочего процесса активации через Dynatrace Hub или указать её имя в JSON-payload при активации расширения через Dynatrace API.

## Фонды Cloud Foundry

При подключении Dynatrace к фондам Cloud Foundry указывается группа ActiveGate, ответственная за запрос данных из Cloud Foundry. Подробнее смотрите в разделе [Подключение фондов Cloud Foundry к Dynatrace](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Включите мониторинг ваших фондов Cloud Foundry.")