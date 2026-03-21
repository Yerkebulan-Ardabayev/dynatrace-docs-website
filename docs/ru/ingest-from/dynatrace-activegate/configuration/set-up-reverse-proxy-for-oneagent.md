---
title: Обратный прокси или балансировщик нагрузки для OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent
scraped: 2026-03-06T21:29:19.498721
---

* Latest Dynatrace
* 1-min read

Обратный прокси или балансировщик нагрузки может быть размещён на пути от OneAgent до ActiveGate. Вам необходимо настроить URL балансировщика нагрузки на ActiveGate, чтобы OneAgent мог использовать эту конечную точку для подключения к ActiveGate.

Нет необходимости настраивать OneAgent для использования обратного прокси. OneAgent использует список конечных точек связи, встроенный в установщик, для подключения к среде. ActiveGate сообщает OneAgent URL, который используется для настройки установки OneAgent.

## Настройка во время установки

Только для Linux

На системах Linux вы можете настроить обратный прокси или балансировщик нагрузки для OneAgent, указав параметры установки во время установки ActiveGate. Подробности см. в разделе [Настройка установки ActiveGate в Linux](../installation/linux/linux-customize-installation-for-activegate.md#load-balancer-oneagent "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

## Настройка после установки

Чтобы указать адрес обратного прокси после установки ActiveGate

1. Остановите ActiveGate и отредактируйте файл `custom.properties` в [каталоге конфигурации ActiveGate](where-can-i-find-activegate-files.md "Find out where ActiveGate files are stored on Windows and Linux systems.").
2. Настройте параметр `dnsEntryPoint` в разделе `[connectivity]`, используя следующий формат:

   `dnsEntryPoint = https://<DOMAIN>:<PORT>`

   где `<PORT>` является необязательным и по умолчанию равен `443`. Например:

   ```
   [connectivity]


   dnsEntryPoint = https://address.of.my.lb.com:9999
   ```

   Чтобы указать несколько целевых адресов, к которым подключается OneAgent, используйте список, разделённый запятыми. Например:

   ```
   [connectivity]


   dnsEntryPoint = https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
   ```
3. Сохраните файл `custom.properties` и [перезапустите главную службу ActiveGate](../operation/stop-restart-activegate.md "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

## Проверка конфигурации

Чтобы проверить конфигурацию

1. В Dynatrace перейдите в раздел **Deployment Status** > **ActiveGates**.
2. Разверните строку для вашего ActiveGate и проверьте свойство **Load Balancer** в разделе **Properties**.

   Вы можете отфильтровать страницу **ActiveGates** по `Load Balancer address`.
