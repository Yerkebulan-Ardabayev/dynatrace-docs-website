---
title: PHP
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/php
scraped: 2026-03-05T21:26:12.292037
---

# PHP

# PHP

* Latest Dynatrace
* Reference
* 1-min read
* Published Jul 09, 2018

PHP — серверный язык сценариев, особенно хорошо подходящий для веб-разработки, а также широко применяемый в программировании общего назначения. Первоначально созданный Расмусом Лердорфом в 1994 году, новые версии теперь выпускаются The PHP Group.

PHP обрабатывается интерпретатором PHP, реализованным в Apache HTTP Server, исполняемом файле Common Gateway Interface (CGI) и интерфейсе командной строки (CLI).

Dynatrace предоставляет широкие возможности мониторинга PHP:

* Все операторы баз данных и метрики SQL
* Анализ времени компиляции, выполнения и ответа
* Поддерживаемые технологии кэширования: Redis (PHP-библиотеки php-redis и predis) и Memcached (расширение PHP memcached)
* Подробные метрики запросов и ответов
* Информация о перезапусках, сбоях и изменениях в развёртывании
* Анализ проблем со стеком (например, переполнение стека)
* Автоматически собираемые метрики PHP-FPM
* Определение горячих точек на уровне кода
* Анализ запросов к внешним сервисам через CURL, интерфейсы SOAP и другие удалённые интерфейсы, такие как `fopen` или `get_file_contents`
* [OneAgent SDK](../../extend-dynatrace/extend-tracing/oneagent-sdk.md "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") для пользовательской трассировки

См. [среды и версии, поддерживаемые Dynatrace](../../technology-support.md#php "Find technical details related to Dynatrace support for specific platforms and development frameworks.") в сочетании с PHP.

### Темы

* [Поддерживаемые версии PHP](php/php-supported-versions.md "Find out the support timeline for all PHP versions.")
* [Мониторинг полного стека PHP](php/full-stack-monitoring.md "Find out how Dynatrace supports full-stack monitoring for PHP.")
* [Видимость на уровне кода для PHP](php/code-level-visibility.md "Learn how Dynatrace offers code-level visibility for its PHP deep-monitoring support.")
* [Мониторинг PHP-FPM](php/php-fpm.md "Learn how Dynatrace PHP-FPM monitoring provides information about connections, slow requests, and processes.")

### См. также

[Dynatrace Open Q&A: What is the desupport policy for PHP?](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/What-is-the-desupport-policy-for-PHP/m-p/42853)

[Blog: Monitor PHP in Windows environments](https://www.dynatrace.com/news/blog/monitor-php-in-windows-environments-beta/)

[Blog: General availability of PHP deep monitoring](https://www.dynatrace.com/news/blog/general-availability-of-php-deep-monitoring/)

[Blog: New response time analysis views!](https://www.dynatrace.com/news/blog/new-response-time-analysis-views/)
