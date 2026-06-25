---
title: Обратный прокси или балансировщик нагрузки для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate
scraped: 2026-05-12T11:36:22.648753
---

# Обратный прокси или балансировщик нагрузки для ActiveGate

# Обратный прокси или балансировщик нагрузки для ActiveGate

* 1-min read
* Updated on Feb 24, 2026

На пути от ActiveGate к кластеру Dynatrace можно установить обратный прокси или балансировщик нагрузки. Это позволяет ActiveGate подключаться к любому доступному узлу кластера, распределяя нагрузку.

Для этого необходимо:

* Указать адрес обратного прокси/балансировщика нагрузки.
* Убедиться, что ActiveGate будет игнорировать информацию об адресе цели, поступающую от кластера Dynatrace, и подключаться только к указанному адресу.

![ActiveGate, подключающийся к кластеру Dynatrace через обратный прокси/балансировщик нагрузки](https://dt-cdn.net/images/rev-proxy-001-1000-f7d875625b.png)

ActiveGate, подключающийся к кластеру Dynatrace через обратный прокси/балансировщик нагрузки

### Возможность настройки во время установки

Эту конфигурацию также можно применить во время установки ActiveGate, указав параметры установки для [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#reverse-proxy-or-load-balancer-configuration "Узнайте о параметрах командной строки для ActiveGate на Linux.") или [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-customize-installation-for-activegate#reverse-proxy-or-load-balancer-configuration "Узнайте о параметрах для ActiveGate на Windows.").

Балансировщик нагрузки не следует размещать между ActiveGate и OneAgent: это может нарушить передачу и обработку дампов памяти.

## Настройка после установки

agctl

custom.properties

ActiveGate версии 1.333+

Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#outgoing-endpoint "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для настройки обратного прокси или балансировщика нагрузки для ActiveGate.

#### Установка одной конечной точки обратного прокси:

```
agctl outgoing-endpoint set https://my.reverse-proxy.com:443/communication
```

#### Установка нескольких конечных точек обратного прокси:

```
agctl outgoing-endpoint set https://my.reverse-proxy-1.com:443/communication,https://my.reverse-proxy-2.com:443/communication
```

После настройки необходимо [перезапустить ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.").

Через `custom.properties`:

1. Остановите ActiveGate и отредактируйте файл `custom.properties` в [директории конфигурации ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate.").

2. Чтобы ActiveGate игнорировал информацию о подключении, получаемую от кластера Dynatrace, добавьте или измените параметр `ignoreClusterRuntimeInfo` в разделе `[connectivity]`:

   ```
   [connectivity]
   ignoreClusterRuntimeInfo = true
   ```

3. Укажите адрес обратного прокси: добавьте параметр `seedServerUrl` в раздел `[collector]`:

   ```
   [collector]
   seedServerUrl = https://my.reverse-proxy.com:443/communication
   ```

   Для нескольких адресов через запятую:

   ```
   [collector]
   seedServerUrl = https://my.reverse-proxy-1.com:443/communication,https://my.reverse-proxy-2.com:443/communication
   ```

4. Сохраните файл `custom.properties` и [перезапустите основную службу ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как перезапустить ActiveGate.").