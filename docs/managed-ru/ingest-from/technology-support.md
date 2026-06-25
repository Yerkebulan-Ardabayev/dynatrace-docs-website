---
title: Поддержка технологий
source: https://docs.dynatrace.com/managed/ingest-from/technology-support
scraped: 2026-05-12T11:05:39.922098
---

# Поддержка технологий

# Поддержка технологий

* 17-min read
* Updated on Mar 31, 2026

Dynatrace поддерживает мониторинг технологий и версий, перечисленных на этой странице. Для бессерверного мониторинга смотрите [Матрицу поддержки бессерверных вычислений](/managed/ingest-from/technology-support/serverless-compute-services "Узнайте, какие функции и возможности Dynatrace поддерживает для бессерверных вычислительных сервисов (FaaS)."). Для мейнфреймов смотрите [Поддержку технологий мейнфреймов](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии поддерживает Dynatrace для мониторинга мейнфреймов.").

Смотрите также [Объявления о завершении поддержки](/managed/whats-new/technology/end-of-support-news "Объявления о завершении поддержки технологий в Dynatrace.").

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Основная версия 5 поддерживается**

  + Основная версия 5 поддерживается, включая все её второстепенные версии, например 5.1 и 5.2
  + Другие основные версии не поддерживаются, например 6 и 7
* **Второстепенная версия 5.1 поддерживается**

  + Второстепенная версия 5.1 поддерживается, включая все её патч-версии, например 5.1.1 и 5.1.2
  + Другие второстепенные версии не поддерживаются, например 5.2 и 5.3
* **Патч-версия 5.1.1 поддерживается**

  + Патч-версия 5.1.1 поддерживается
  + Другие патч-версии не поддерживаются, например 5.1.2 и 5.1.3
* **Поддерживается диапазон версий от 5.1 до 5.3**

  + Поддерживаются второстепенные версии 5.1, 5.2 и 5.3, включая все их патч-версии, например 5.1.1, 5.2.1 и 5.3.1
  + Другие второстепенные версии не поддерживаются, например 5.0 и 5.4
* **Минимальная требуемая версия: 5+**

  + Поддерживаются все основные, второстепенные и патч-версии, начиная с версии 5, например 5, 5.1, 5.1.1 и 6

## Операционные системы

OneAgent можно установить на следующих операционных системах: [Linux](#linux), [Unix](#unix), [Windows](#windows) и [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнайте, какие технологии поддерживает Dynatrace для мониторинга мейнфреймов.").

> _Reference-таблицы ниже на английском._

### Linux

Dynatrace тестирует и предоставляет поддержку установки OneAgent только для дистрибутивов и версий [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнайте, как установить OneAgent на Linux, настроить установку и многое другое."), перечисленных ниже.

При развёртывании OneAgent на хосте Linux с Oracle Database Server 19c и/или смонтированными NFS-дисками существуют определённые ограничения. Смотрите [Устранение неполадок при установке OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Узнайте, как устранить неполадки при установке OneAgent на AIX, Linux и Windows.").

Поддерживаемые архитектуры CPU

* `x86-64` – 64-разрядный Intel/AMD
* `s390x` – 64-разрядный IBM Z mainframe
* `ppc64le` – 64-разрядный PowerPC
* `ARM64 (AArch64)` – 64-разрядный Linux ARM, включая [процессоры AWS Graviton](https://aws.amazon.com/ec2/graviton/)

| Поддерживаемая ОС | Версии | Архитектуры CPU |
| --- | --- | --- |
| AlmaLinux | 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| Alpine Linux (musl libc) для контейнеров | 3.10 - 3.23 | x86-64 |
| Amazon Linux | 2023 | ARM64 (AArch64), x86-64 |
| Azure Linux | 2, 3 | x86-64 |
| Bottlerocket | 1 | ARM64 (AArch64), x86-64 |
| CentOS Stream | 9 | ARM64 (AArch64), PPCLE, x86-64 |
| Debian | 11, 12, 13 | ARM64 (AArch64), x86-64 |
| Fedora | 41, 42, 43 | x86-64 |
| Oracle Linux | 7, 8, 9, 10 | x86-64 |
| Red Hat Enterprise Linux | 7, 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| Red Hat Enterprise Linux CoreOS | 4.14, 4.15, 4.16 | x86-64 |
| Rocky Linux | 8, 9, 10 | ARM64 (AArch64), x86-64 |
| SUSE Linux Enterprise Server | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7, 16.0 | x86-64 |
| SUSE Linux Enterprise Server | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | PPCLE, s390 |
| SUSE Linux Enterprise Server | 15.3, 15.4, 15.5, 15.6, 15.7, 16.0 | ARM64 (AArch64) |
| Ubuntu | 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | PPCLE, x86-64 |
| Ubuntu | 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | ARM64 (AArch64), s390 |
| openSUSE | 15.6, 16.0 | ARM64 (AArch64), PPCLE, x86-64 |

Детальные таблицы поддержки технологий (фреймворки приложений, языки, базы данных, веб-серверы, облачные технологии и т. д.) доступны в оригинальной английской документации по адресу [https://docs.dynatrace.com/managed/ingest-from/technology-support](https://docs.dynatrace.com/managed/ingest-from/technology-support).