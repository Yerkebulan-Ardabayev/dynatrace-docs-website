---
title: PHP
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/php
scraped: 2026-03-05T21:26:12.292037
---

# PHP


* Latest Dynatrace
* Reference
* 1-min read
* Published Jul 09, 2018

PHP is a server-side scripting language particularly well-suited for web development but also popular in general-purpose programming. Originally created by Rasmus Lerdorf in 1994, new versions are now produced by The PHP Group.

PHP is processed by a PHP interpreter that's implemented in Apache HTTP Server, the Common Gateway Interface (CGI) executable, and command-line interface (CLI).

Dynatrace provides extensive PHP monitoring capabilities:

* All database statements and SQL metrics
* Compilation, execution, and response time analysis
* Supported caching technologies: Redis (php-redis and predis PHP libraries) and Memcached (memcached PHP extension)
* Detailed request and response metrics
* Information about restarts, crashes, and deployment changes
* Insight into stack issues (like Stack Overflow)
* Automatically collected PHP-FPM metrics
* Location of hotspots at the code level
* Analysis of requests to external services via CURL, SOAP interfaces, and other remote interfaces, such as `fopen` or `get_file_contents`
* OneAgent SDK for custom tracing

See [the environments and versions that Dynatrace supports](../../technology-support.md#php "Find technical details related to Dynatrace support for specific platforms and development frameworks.") in conjunction with PHP.

### Topics

* Supported PHP versions
* Full-stack PHP monitoring
* Code-level visibility for PHP
* PHP-FPM monitoring

### See also

[Dynatrace Open Q&A: What is the desupport policy for PHP?ï»¿](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/What-is-the-desupport-policy-for-PHP/m-p/42853)

[Blog: Monitor PHP in Windows environmentsï»¿](https://www.dynatrace.com/news/blog/monitor-php-in-windows-environments-beta/)

[Blog: General availability of PHP deep monitoringï»¿](https://www.dynatrace.com/news/blog/general-availability-of-php-deep-monitoring/)

[Blog: New response time analysis views!ï»¿](https://www.dynatrace.com/news/blog/new-response-time-analysis-views/)