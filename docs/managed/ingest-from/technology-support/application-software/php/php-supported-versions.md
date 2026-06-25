---
title: Supported PHP versions
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/php/php-supported-versions
scraped: 2026-05-12T12:03:51.214287
---

# Supported PHP versions

# Supported PHP versions

* 2-min read
* Published Jun 12, 2019

The different PHP versions have support timelines defined by PHP. Please refer to [Supported PHP versionsï»¿](https://php.net/supported-versions.php) at [php.netï»¿](https://php.net/) to see which versions are currently supported by PHP and when each version is planned for end of support.

* Deprecated versions don't receive updates or security patches, so running them in production should be avoided.
* Dynatrace is committed to supporting each PHP version for at least as long as the vendor supports it (in most cases, support extends for at least six months beyond this point).

## Support matrix

See also [Support for Early Access releases](#early-adopter) following this table.

| PHP version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 8.5 (Zend Engine 4.5) | 2025-11-25 | 2029-12-31 | 1.329 | - | - | Supported[1](#fn-php-1-def) |
| 8.4 (Zend Engine 4.4) | 2024-11-21 | 2028-12-31 | 1.307 | - | - | Supported[2](#fn-php-2-def) |
| 8.3 (Zend Engine 4.3) | 2023-11-23 | 2026-11-23 | 1.277 | - | - | Supported[3](#fn-php-3-def) |
| 8.2 (Zend Engine 4.2) | 2022-12-08 | 2025-12-08 | 1.253 | - | - | Supported[4](#fn-php-4-def) |
| 8.1 (Zend Engine 4.1) | 2021-09-02 | 2024-11-25 | 1.227 | - | - | Supported[5](#fn-php-5-def) |
| 8.0 (Zend Engine 4.0) | 2020-11-26 | 2023-11-26 | 1.207 | - | - | Supported |
| 7.4 (Zend Engine 3.4) | 2019-11-28 | 2022-11-28 | 1.179 | - | - | Supported |
| 7.3 (Zend Engine 3.3) | 2018-12-06 | 2021-12-06 | 1.169 | - | - | Supported |
| 7.2 (Zend Engine 3.2) | 2017-11-30 | 2020-11-30 | - | - | - | Supported |
| 7.1 (Zend Engine 3.1) | 2016-12-01 | 2019-12-01 | - | - | - | Supported |

1

PHP 8.5 (from RC3 - before official PHP release up to 8.5.x) is supported.

2

PHP 8.4 (from RC2 - before official PHP release up to 8.4.x) is supported.

3

PHP 8.3 (from RC1 - before official PHP release up to 8.3.x) is supported.

4

PHP 8.2 (from RC1 - before official PHP release up to 8.2.x) is supported.

5

PHP 8.1 (from RC1 to 8.1.x) is supported.

## Support for Early Access releases

If there is Early Access support for a PHP version, it has a separate switch that enables you to opt in or out of monitoring for that version.

To enable an Early Access release of PHP monitoring in Dynatrace

1. Go to **Settings** and select **Monitoring** > **Monitored technologies**.
2. On the **Supported technologies** tab, find **PHP** and open it for editing.
3. On the **PHP** page, turn on **Enable PHP *x* monitoring on every host**.

   Verify that your monitoring environment meets the requirements stated under the switch.

## Messaging for unsupported versions

When OneAgent detects an unsupported PHP version, we exclude it from monitoring and display a warning in the process overview page:

```
Activation of deep monitoring was unsuccessful



Process version is not supported
```

![PHP Monitoring Process version not supported](https://dt-cdn.net/images/php-monitoring-1668-782cbab381.png)

PHP Monitoring Process version not supported

We also write the message to the error logs on the host machine.

See [the environments and versions that Dynatrace supports](/managed/ingest-from/technology-support#php "Find technical details related to Dynatrace support for specific platforms and development frameworks.") in conjunction with PHP and [the PHP supported versionsï»¿](https://php.net/supported-versions.php).

## Known limitations

* CLI monitoring is turned off by default, because, during a short-lived CLI execution, injection overhead may make up a large percentage of the whole runtime. You should refrain from using CLI monitoring when threading and forking is used for the monitored application, as these features aren't supported.
* At this point, there is no differentiation between CGI and Fast-CGI; these are reported as a single type: CGI.