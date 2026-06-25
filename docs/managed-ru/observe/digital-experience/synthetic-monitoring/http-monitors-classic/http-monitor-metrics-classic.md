---
title: Метрики HTTP-мониторов
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic
scraped: 2026-05-12T11:32:03.339642
---

# Метрики HTTP-мониторов

# Метрики HTTP-мониторов

* Explanation
* 1-min read
* Published Dec 04, 2020

Для синтетических [HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.") собираются и отображаются следующие метрики:

Response time (время отклика)
:   Измеряет производительность HTTP-монитора или события.  
    **Response time** — это сумма **DNS lookup time**, **TCP connect time**, **TLS handshake time**, **Waiting** и **Download**.

DNS lookup time (время разрешения DNS)
:   Время, затраченное на разрешение имени хоста. Если из-за редиректа выполняется несколько DNS-запросов, это суммарное время всех DNS-запросов.

TCP connect time (время установки TCP-соединения)
:   Время, затраченное на установку TCP-соединения. Если из-за редиректа выполняется несколько TCP-соединений, это суммарное время всех попыток установки TCP-соединения.

TLS handshake time (время TLS-рукопожатия)
:   Время, затраченное на завершение TLS-рукопожатия.

Waiting (ожидание)
:   Время, затраченное сервером на ответ первым байтом. Это **Time to first byte** минус (**DNS lookup time** + **TCP connect time** + **TLS handshake time**).  
    Обратите внимание: **Time to first byte** — это время от начала запроса до получения первого байта ответа.

Download (загрузка)
:   Время, затраченное на загрузку HTTP-ответа.  
    Время загрузки может быть равно 0, если ответ помещается в один пакет. Время загрузки также может быть равно 0 при медленной сети. В таких случаях сетевая задержка отображается в метрике **Waiting**.