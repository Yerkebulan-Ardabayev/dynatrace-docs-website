---
title: PHP
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/php
scraped: 2026-05-12T11:22:35.469671
---

# PHP

# PHP

* Справочник
* Чтение: 1 мин
* Опубликовано: 9 июля 2018

PHP является серверным скриптовым языком, особенно хорошо подходящим для веб-разработки, но также популярным в программировании общего назначения. Изначально язык был создан Расмусом Лердорфом в 1994 году, а новые версии теперь выпускает The PHP Group.

PHP обрабатывается интерпретатором PHP, реализованным в Apache HTTP Server, исполняемом файле Common Gateway Interface (CGI) и интерфейсе командной строки (CLI).

Dynatrace предоставляет широкие возможности мониторинга PHP:

* Все операторы баз данных и метрики SQL
* Анализ времени компиляции, выполнения и отклика
* Поддерживаемые технологии кэширования: Redis (PHP-библиотеки php-redis и predis) и Memcached (PHP-расширение memcached)
* Подробные метрики запросов и ответов
* Информация о перезапусках, сбоях и изменениях развёртывания
* Анализ проблем со стеком (например, переполнение стека)
* Автоматически собираемые метрики PHP-FPM
* Определение горячих точек на уровне кода
* Анализ запросов к внешним сервисам через CURL, интерфейсы SOAP и другие удалённые интерфейсы, такие как `fopen` или `get_file_contents`
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать ваше приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых ещё нет готового кодового модуля.") для пользовательской трассировки

Ознакомьтесь со [средами и версиями, поддерживаемыми Dynatrace](/managed/ingest-from/technology-support#php "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") применительно к PHP.

### Разделы

* [Поддерживаемые версии PHP](/managed/ingest-from/technology-support/application-software/php/php-supported-versions "Узнайте о сроках поддержки всех версий PHP.")
* [Полностековый мониторинг PHP](/managed/ingest-from/technology-support/application-software/php/full-stack-monitoring "Узнайте, как Dynatrace поддерживает полностековый мониторинг PHP.")
* [Видимость на уровне кода для PHP](/managed/ingest-from/technology-support/application-software/php/code-level-visibility "Узнайте, как Dynatrace обеспечивает видимость на уровне кода в рамках поддержки глубокого мониторинга PHP.")
* [Мониторинг PHP-FPM](/managed/ingest-from/technology-support/application-software/php/php-fpm "Узнайте, как мониторинг PHP-FPM в Dynatrace предоставляет информацию о соединениях, медленных запросах и процессах.")

### См. также

[Dynatrace Open Q&A: Какова политика прекращения поддержки PHP?](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/What-is-the-desupport-policy-for-PHP/m-p/42853)

[Блог: Мониторинг PHP в средах Windows](https://www.dynatrace.com/news/blog/monitor-php-in-windows-environments-beta/)

[Блог: Общая доступность глубокого мониторинга PHP](https://www.dynatrace.com/news/blog/general-availability-of-php-deep-monitoring/)

[Блог: Новые представления для анализа времени отклика!](https://www.dynatrace.com/news/blog/new-response-time-analysis-views/)