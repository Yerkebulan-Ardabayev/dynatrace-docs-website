---
title: ActiveGate group
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-group
scraped: 2026-03-06T21:24:16.455659
---

# Группа ActiveGate

# Группа ActiveGate

* Последняя версия Dynatrace
* Чтение займёт 2 минуты
* Опубликовано 08 июл. 2022 г.

Вы можете использовать группы ActiveGate для выполнения массовых операций над вашими ActiveGate, например для управления [расширениями](../extensions.md "Узнайте, как создавать расширения Dynatrace и управлять ими."), запущенными на ActiveGate, или для подключения [фундаментов Cloud Foundry](../setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace.md "Включите мониторинг для ваших фундаментов Cloud Foundry.").

## Требования

* Имя группы ActiveGate представляет собой строку из буквенно-цифровых символов, дефисов (`-`), знаков подчёркивания (`_`) и точек (`.`).
* Точки используются в качестве разделителей, поэтому нельзя использовать точку в качестве первого символа имени группы.
* Длина строки ограничена 256 символами.

## Назначение ActiveGate группе

ActiveGate может принадлежать только одной группе. По умолчанию ActiveGate назначается группе `default`. Вы можете назначить ActiveGate группе во время установки или после неё.

### Назначение группе во время установки

Чтобы назначить ActiveGate группе, во время установки можно использовать параметр `--set-group`. Обратите внимание, что этот параметр нельзя использовать при обновлении ActiveGate. Например:

Linux

Windows

```
/bin/bash Dynatrace-ActiveGate-Linux-x86-<version>.sh --set-group=my-group
```

```
Dynatrace-ActiveGate-Windows-x86-<version>.exe --set-group=my-group
```

### Назначение группе после установки

Для назначения ActiveGate группе можно воспользоваться [удалённым управлением конфигурацией](../bulk-configuration.md#configure-activegates "Выполняйте настройку OneAgent и ActiveGate на хостах со страницы состояния развёртывания или в масштабе с помощью Dynatrace API.") (выберите действие **modify ActiveGate group**).

Альтернативно можно использовать свойство конфигурации ActiveGate `group`. Например:

```
[collector]



group = mygroup
```

Дополнительные сведения см. в разделе [Основные правила работы с конфигурацией ActiveGate](configuration/configure-activegate.md#basic-rules "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований.")

## Расширения

ActiveGate, запускающий удалённое расширение, должен принадлежать группе ActiveGate, поскольку Dynatrace использует группу для указания расширению, где оно должно выполняться. Если вы планируете использовать один ActiveGate для запуска удалённого расширения, назначьте его в выделенную группу, содержащую только этот ActiveGate.

При активации расширения необходимо указать группу ActiveGate, которая будет запускать это расширение. Вы можете выбрать группу ActiveGate либо в процессе активации через Dynatrace Hub, либо указав имя группы ActiveGate в JSON-payload при активации расширения с помощью Dynatrace API.

## Фундаменты Cloud Foundry

При подключении Dynatrace к фундаментам Cloud Foundry вы указываете группу ActiveGate, ответственную за запрос данных у Cloud Foundry. Дополнительные сведения см. в разделе [Подключение ваших фундаментов Cloud Foundry к Dynatrace](../setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace.md "Включите мониторинг для ваших фундаментов Cloud Foundry.")
