---
title: PHP
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/php
scraped: 2026-03-05T21:26:12.292037
---

* Latest Dynatrace
* 1-min read

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
* OneAgent SDK для пользовательской трассировки

См. [среды и версии, поддерживаемые Dynatrace](../../technology-support.md#php "Find technical details related to Dynatrace support for specific platforms and development frameworks.") в сочетании с PHP.

### Темы

* Поддерживаемые версии PHP
* Мониторинг полного стека PHP
* Видимость на уровне кода для PHP
* Мониторинг PHP-FPM

### См. также

[Dynatrace Open Q&A: What is the desupport policy for PHP?](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/What-is-the-desupport-policy-for-PHP/m-p/42853)

[Blog: Monitor PHP in Windows environments](https://www.dynatrace.com/news/blog/monitor-php-in-windows-environments-beta/)

[Blog: General availability of PHP deep monitoring](https://www.dynatrace.com/news/blog/general-availability-of-php-deep-monitoring/)

[Blog: New response time analysis views!](https://www.dynatrace.com/news/blog/new-response-time-analysis-views/)
