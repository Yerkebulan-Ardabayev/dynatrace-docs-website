---
title: Журнал ингест и процесс (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data
scraped: 2026-03-06T21:37:45.649064
---

# Приём и обработка журналов (Logs Classic)


* 2-min read

Log Monitoring Classic

Dynatrace автоматически собирает данные журналов и событий из широкого спектра технологий. С помощью Log ingestion API вы можете передавать записи журналов в систему и Dynatrace преобразует поток в понятные сообщения журналов.

Dynatrace поддерживает все основные сторонние платформы и архитектуры.

## Автообнаружение журналов и пользовательские источники журналов

Вы можете полагаться на автоматически обнаруженные или добавленные вручную источники журналов для OneAgent. См. Матрицу поддержки платформ и возможностей OneAgent.

* Автоматическое обнаружение данных журналов
* Добавление файлов журналов вручную

![LMC - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lmc-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-c4876fc96b.png)

## Облачные провайдеры

Log Monitoring включает встроенную поддержку журналов и событий Red Hat OpenShift и Kubernetes для платформ Kubernetes, рабочих нагрузок и приложений, работающих внутри Kubernetes.

Log Monitoring имеет встроенную поддержку мультиоблачных сред, включая:

* AWS
* Google Cloud
* Microsoft Azure

## Syslog

Syslog — стандартный протокол для ведения журналов сообщений и управления системными журналами. Маршрутизаторы, принтеры, хосты, коммутаторы и другие устройства на различных платформах используют syslog для записи активности пользователей, событий жизненного цикла системы и программного обеспечения, статуса или диагностических данных.

Журналы Syslog принимаются через syslog-приёмник, доступный на Environment ActiveGate.

Для получения дополнительной информации см. Приём Syslog с ActiveGate (Logs Classic).

## Открытый исходный код

Dynatrace Log Monitoring поддерживает фреймворки для работы с журналами с открытым исходным кодом, включая Fluentd и Logstash.

## Log ingestion API

С помощью Log ingestion API вы можете передавать записи журналов в Dynatrace и Dynatrace преобразует поток в понятные сообщения журналов. Вы также можете использовать Log ingestion API для потоковой передачи записей журналов в Dynatrace через API.

* Log ingestion API
* Log Monitoring API

![LMC - Generic log ingestion API](https://dt-cdn.net/images/lmc-generic-log-ingestion-api-2500-e9c0d3ff5f.png)

## Обработка журналов

Dynatrace Log Monitoring включает преобразование входящих данных журналов в форму, которая может потребоваться для лучшего понимания, анализа или дальнейшей обработки данных журналов в Dynatrace. Используя Dynatrace Pattern Language (DPL), вы можете определять паттерны с помощью матчеров и создавать набор правил, которые Log Monitoring применяет к принятым данным журналов.

* Обработка журналов
* Dynatrace Pattern Language

![LMC - Log processing pipeline](https://dt-cdn.net/images/lmc-log-processing-pipeline-2500-60d2c2d7b6.png)
