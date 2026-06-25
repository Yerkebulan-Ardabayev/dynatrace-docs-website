---
title: Устранение проблем развёртывания OneAgent на Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/troubleshoot-cf
scraped: 2026-05-12T11:09:25.777114
---

# Устранение проблем развёртывания OneAgent на Cloud Foundry

# Устранение проблем развёртывания OneAgent на Cloud Foundry

* 1-min read
* Published Apr 23, 2020

Данная статья описывает устранение возможных проблем при развёртывании OneAgent на Cloud Foundry и способы доступа к файлам логов OneAgent.

* [Проблемы развёртывания OneAgent на Cloud Foundry для мониторинга только приложений](https://dt-url.net/7a637wx)

## Файлы логов

Для устранения проблем при развёртывании OneAgent на Cloud Foundry изучите логи. В зависимости от стратегии развёртывания они расположены по следующим путям:

* [Файлы логов OneAgent для мониторинга только приложений](https://dt-url.net/86437m0)

### Файлы логов BOSH OneAgent

При развёртывании через OneAgent BOSH файлы логов доступны по следующим путям:

* **Путь по умолчанию**: `/opt/dynatrace/oneagent` (символическая ссылка на `/var/vcap/data/dynatrace/oneagent/log`)
* `/var/vcap/data/dynatrace/oneagent/log`
* `/var/vcap/sys/log/dynatrace`

Для доступа к директории `/var/vcap/data/dynatrace` необходимы права суперпользователя (root).

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")