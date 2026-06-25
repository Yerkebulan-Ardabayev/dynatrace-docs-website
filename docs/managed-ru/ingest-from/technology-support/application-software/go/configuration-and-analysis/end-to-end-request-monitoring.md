---
title: Сквозной мониторинг запросов
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring
scraped: 2026-05-12T12:04:01.672620
---

# Сквозной мониторинг запросов

# Сквозной мониторинг запросов

* Чтение: 1 мин
* Опубликовано: 15 апреля 2019

С Dynatrace можно мониторить входящие и исходящие веб-запросы как ваших собственных, так и любых сторонних Go-приложений. OneAgent выявляет сервисы, размещённые в процессах на основе Go, и предоставляет сведения о сервисах, связанные со временем отклика, экземплярами и выполненными веб-запросами.

![Динамические веб-запросы](https://dt-cdn.net/images/dynamic-web-requests-1683-38937e6063.png)

Динамические веб-запросы

[Service flow](/managed/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает отслеживать последовательность вызовов сервисов, которые инициируются каждым запросом к сервису в вашем окружении.") раскрывает больше данных о транзакциях и обеспечивает удобный доступ к отдельным запросам, включая связанные с ними распределённые трассировки.

![Service flow](https://dt-cdn.net/images/service-flow-for-influxdb-stress-test-1683-7c250d283a.png)

Service flow

Как видно на скриншотах ниже, OneAgent захватывает сведения о каждом веб-запросе, включая URI запроса, метод и заголовки, а также код состояния ответа и заголовки.

![PurePath - сводка](https://dt-cdn.net/images/purepath1-for-influxdb-stress-test-1869-1c6edc761a.png)

PurePath - сводка

![PurePath - уровень кода](https://dt-cdn.net/images/purepath2-for-influxdb-stress-test-1886-6faae42e94.png)

PurePath - уровень кода