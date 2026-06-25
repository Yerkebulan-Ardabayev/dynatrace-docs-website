---
title: Обратный прокси или балансировщик нагрузки для OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-oneagent
scraped: 2026-05-12T11:36:23.797788
---

# Обратный прокси или балансировщик нагрузки для OneAgent

# Обратный прокси или балансировщик нагрузки для OneAgent

* 1-min read
* Updated on Feb 24, 2026

На пути от OneAgent к ActiveGate можно установить обратный прокси или балансировщик нагрузки. Необходимо настроить URL балансировщика нагрузки на ActiveGate, чтобы OneAgent мог использовать эту конечную точку для подключения к ActiveGate.

Настраивать OneAgent для использования обратного прокси не нужно. OneAgent использует список конечных точек связи, встроенных в установщик, для подключения к окружению. ActiveGate сообщает OneAgent URL, используемый для настройки установки OneAgent.

## Настройка во время установки

Только Linux

На Linux-системах можно настроить обратный прокси или балансировщик нагрузки для OneAgent, указав параметры установки во время установки ActiveGate. Подробнее см. [Настройка установки ActiveGate на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#load-balancer-oneagent "Узнайте о параметрах командной строки для ActiveGate на Linux.").

## Настройка после установки

agctl

custom.properties

ActiveGate версии 1.333+

Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#incoming-endpoint "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для настройки обратного прокси или балансировщика нагрузки для OneAgent.

#### Установка одной конечной точки обратного прокси:

```
agctl incoming-endpoint set https://address.of.my.lb.com:9999
```

#### Установка нескольких конечных точек обратного прокси:

```
agctl incoming-endpoint set https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
```

После настройки обратного прокси с помощью `agctl` необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") для применения изменений.

1. Остановите ActiveGate и отредактируйте файл `custom.properties` в [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.").
2. Настройте параметр `dnsEntryPoint` в разделе `[connectivity]` в следующем формате:

   `dnsEntryPoint = https://<DOMAIN>:<PORT>`

   где `<PORT>` необязателен и по умолчанию равен `443`. Например:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb.com:9999
   ```

   Для указания нескольких адресов, к которым подключается OneAgent, используйте список через запятую. Например:

   ```
   [connectivity]



   dnsEntryPoint = https://address.of.my.lb-1.com:9999,https://address.of.my.lb-2.com:9999
   ```
3. Сохраните файл `custom.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.").

## Проверка конфигурации

Для проверки конфигурации:

1. В Dynatrace перейдите в **Deployment Status** > **ActiveGates**.
2. Разверните строку нужного ActiveGate и проверьте свойство **Load Balancer** в разделе **Properties**.

   Страницу **ActiveGates** можно фильтровать по `Load Balancer address`.