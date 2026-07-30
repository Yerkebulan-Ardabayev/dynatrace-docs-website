---
title: Обратный прокси или балансировщик нагрузки для OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent
---

# Обратный прокси или балансировщик нагрузки для OneAgent

# Обратный прокси или балансировщик нагрузки для OneAgent

* Чтение займёт 1 минуту
* Обновлено 09 июля 2026 г.

Обратный прокси или балансировщик нагрузки можно разместить на пути от OneAgent до ActiveGate. Нужно настроить URL балансировщика на стороне ActiveGate, чтобы OneAgent мог использовать этот endpoint для подключения к ActiveGate.

Настраивать OneAgent на работу через обратный прокси не нужно. OneAgent использует список коммуникационных endpoint'ов, встроенных в установщик, для подключения к среде. ActiveGate сообщает OneAgent URL, который применяется при настройке установки OneAgent.

## Настройка во время установки

Только Linux

На системах Linux обратный прокси или балансировщик нагрузки для OneAgent можно настроить, указав параметры установки во время инсталляции ActiveGate. Подробнее см. [Customize ActiveGate installation on Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#load-balancer-oneagent "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

## Настройка после установки

agctl

custom.properties

ActiveGate версии 1.333+

Для настройки обратного прокси или балансировщика нагрузки для OneAgent можно использовать [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#incoming-endpoint "Learn how to use agctl to configure and manage ActiveGate from the command line").

#### Задать один endpoint обратного прокси:

```
agctl incoming-endpoint set https://address.of.my.lb.com:9999
```

#### Задать несколько endpoint'ов обратного прокси:

```
agctl incoming-endpoint set https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
```

После настройки обратного прокси через `agctl` нужно [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux."), чтобы изменения вступили в силу.

1. Остановите ActiveGate и откройте файл `custom.properties` в [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").
2. Настройте параметр `dnsEntryPoint` в секции `[connectivity]`, используя следующий формат:

   `dnsEntryPoint = https://<DOMAIN>:<PORT>`

   где `<PORT>` необязателен и по умолчанию равен `443`. Например:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb.com:9999
   ```

   Чтобы указать несколько адресов назначения, к которым подключается OneAgent, используйте список через запятую. Например:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
   ```
3. Сохраните файл `custom.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Проверка конфигурации

Чтобы проверить конфигурацию:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Раскройте строку нужного ActiveGate и проверьте свойство **Load Balancer** в разделе **Properties**.

   Страницу **ActiveGates** можно отфильтровать по `Load Balancer address`.