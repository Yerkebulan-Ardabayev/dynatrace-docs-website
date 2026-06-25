---
title: Требования к операционной системе
source: https://docs.dynatrace.com/managed/managed-cluster/installation/operating-system-requirements
scraped: 2026-05-12T11:25:10.427673
---

# Требования к операционной системе

# Требования к операционной системе

* Reference
* 2-min read
* Updated on May 08, 2026

Перед установкой Dynatrace Managed ознакомьтесь с требованиями к операционной системе.

* Dynatrace Managed требует **выделенного хоста**. На хосте не должны выполняться другие сервисы, интенсивно использующие CPU или память, или использующие [порты, необходимые Dynatrace Managed](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.").
* Dynatrace Managed работает на **64-битном дистрибутиве Linux** (поддерживаемые дистрибутивы см. ниже). Поддерживается установка на физических и виртуализированных хостах, но не в контейнерах.
* Dynatrace Managed требует фиксированный IPv4-адрес. Поддерживаются только адресные пространства IPv4.
* Перед установкой настройте [параметры фаервола](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.").
* Библиотеки, устанавливаемые вместе с Dynatrace Managed, зависят от локали. Установите системную локаль на английский вариант, например `LANG=en_US.UTF-8`, для корректного отображения текста и символов.

## Поддерживаемые операционные системы

| Дистрибутив Linux | Версии | Архитектура CPU |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | x86-64 |
| Debian | 11, 12 | x86-64 |
| Oracle Linux | 8.8, 8.10, 9.2, 9.4, 9.6, 10.1[1](#fn-linux-distribution-1-def) | x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 10.0[1](#fn-linux-distribution-1-def) | x86-64 |
| Rocky Linux | 9.2, 9.4, 9.6, 10.0[1](#fn-linux-distribution-1-def) | x86-64 |
| SUSE Enterprise Linux | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |

1

Для Dynatrace Managed требуется ручная установка библиотеки 'libcrypt.so.1' из пакета 'libxcrypt-compat.rpm', который не устанавливается по умолчанию.

## Изменения в поддержке

### Предстоящие изменения в поддержке операционных систем Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 июня 2026 года

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление вендора](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление вендора](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 июля 2026 года

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление вендора](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 ноября 2026 года

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление вендора](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление вендора](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 января 2027 года

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление вендора](https://aws.amazon.com/linux/)

### Прошедшие изменения в поддержке операционных систем Dynatrace Managed

##### Следующие операционные системы не поддерживаются с 01 декабря 2025 года

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление вендора](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление вендора](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление вендора](https://endoflife.date/rocky-linux)

##### Следующие операционные системы не поддерживаются с 01 января 2026 года

* Linux: Debian 10

  + x86-64
  + [Объявление вендора](https://wiki.debian.org/DebianReleases)