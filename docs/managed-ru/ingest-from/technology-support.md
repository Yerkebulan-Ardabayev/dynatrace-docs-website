---
title: Поддержка технологий
source: https://docs.dynatrace.com/managed/ingest-from/technology-support
---

# Поддержка технологий

# Поддержка технологий

* 17 минут чтения
* Обновлено 10 июля 2026

Dynatrace поддерживает мониторинг технологий и версий, перечисленных на этой странице. Для serverless-мониторинга см. [Матрица поддержки serverless-вычислений](/managed/ingest-from/technology-support/serverless-compute-services "Узнать, какие функции и возможности поддерживает Dynatrace для serverless-вычислений (FaaS)."). Для мейнфреймов см. [Поддержка технологий мейнфреймов](/managed/ingest-from/technology-support/mainframe-technology-support "Узнать, какие технологии поддерживает Dynatrace для мониторинга мейнфреймов.").

См. также [Объявления об окончании поддержки](/managed/whats-new/technology/end-of-support-news "Объявления об окончании поддержки технологий, поддерживаемых Dynatrace.").

Схема версионирования поддержки технологий

Определение схемы версионирования поддержки технологий с примерами:

* **Поддерживается основная версия 5**

  + Поддерживается основная версия 5, включая все её минорные версии, например 5.1 и 5.2
  + Другие основные версии не поддерживаются, например 6 и 7
* **Поддерживается минорная версия 5.1**

  + Поддерживается минорная версия 5.1, включая все её патч-версии, например 5.1.1 и 5.1.2
  + Другие минорные версии не поддерживаются, например 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Поддерживается патч-версия 5.1.1
  + Другие патч-версии не поддерживаются, например 5.1.2 и 5.1.3
* **Поддерживается диапазон версий 5.1 – 5.3**

  + Поддерживаются минорные версии 5.1, 5.2 и 5.3, включая все их патч-версии, например 5.1.1, 5.2.1 и 5.3.1
  + Другие минорные версии не поддерживаются, например 5.0 и 5.4
* **Минимально необходимая версия 5+**

  + Поддерживаются все основные, минорные и патч-версии начиная с версии 5, например 5, 5.1, 5.1.1 и 6

## Операционные системы

OneAgent можно установить на следующие операционные системы [Linux](#linux), [Unix](#unix), [Windows](#windows) и [z/OS](/managed/ingest-from/technology-support/mainframe-technology-support "Узнать, какие технологии поддерживает Dynatrace для мониторинга мейнфреймов.").

### Linux

Dynatrace тестирует и поддерживает установку OneAgent только на дистрибутивах и версиях [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое."), перечисленных ниже.

Существуют определённые ограничения при развёртывании OneAgent на хосте Linux с Oracle Database Server 19c и/или подключёнными NFS-дисками. См. [Устранение неполадок установки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Узнать, как устранять неполадки установки OneAgent на AIX, Linux и Windows.").

Поддерживаемые архитектуры процессоров

* `x86-64` - 64-битная Intel/AMD
* `s390x` - 64-битный мейнфрейм IBM Z
* `ppc64le` - 64-битная PowerPC
* `ARM64 (AArch64)` - 64-битный Linux ARM, включая [процессоры AWS Graviton﻿](https://aws.amazon.com/ec2/graviton/)

| Поддерживаемая ОС | Версии | Архитектуры процессоров |
| --- | --- | --- |
| [AlmaLinux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| [Alpine Linux (musl libc) для контейнеров](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнать, какие возможности поддерживает OneAgent на разных операционных системах и платформах.") | 3.10 - 3.23[1](#fn-supported-os-1-def) | ARM64 (AArch64), x86-64 |
| [Amazon Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 2023 | ARM64 (AArch64), x86-64 |
| [Azure Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 2, 3 | x86-64 |
| [Bottlerocket](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развернуть Dynatrace Operator в режиме мониторинга приложений в Kubernetes") | 1[2](#fn-supported-os-2-def) | ARM64 (AArch64), x86-64 |
| [CentOS Stream](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 9 | ARM64 (AArch64), PPCLE, x86-64 |
| [Debian](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 11, 12, 13 | ARM64 (AArch64), x86-64 |
| [Fedora](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 41, 42, 43, 44 | x86-64 |
| [Fedora](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 44 | ARM64 (AArch64) |
| [Oracle Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 7, 8, 9, 10 | x86-64 |
| [Red Hat Enterprise Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 7, 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| [Red Hat Enterprise Linux CoreOS](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes") | 4.14[3](#fn-supported-os-3-def), 4.15[3](#fn-supported-os-3-def), 4.16[3](#fn-supported-os-3-def) | x86-64 |
| [Rocky Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 8, 9, 10 | ARM64 (AArch64), x86-64 |
| [SUSE Linux Enterprise Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7, 16.0 | x86-64 |
| [SUSE Linux Enterprise Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | PPCLE, s390 |
| [SUSE Linux Enterprise Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 15.3, 15.4, 15.5, 15.6, 15.7, 16.0 | ARM64 (AArch64) |
| [Ubuntu](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS, 26.04 LTS | PPCLE, x86-64 |
| [Ubuntu](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS, 26.04 LTS | ARM64 (AArch64), s390 |
| [openSUSE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Узнать, как установить OneAgent на Linux, как настроить установку и другое.") | 15.6, 16.0 | ARM64 (AArch64), PPCLE, x86-64 |

1

Поддерживается только в контейнерах, которые мониторятся в режиме OneAgent full-stack или application-only monitoring (musl libc 1.1.14 - 1.2.5). Бинарные файлы, собранные под GNU C Library (glibc) и запускаемые через библиотеку gcompat, не поддерживаются.

2

Поддерживается только с использованием application-only injection. Метрики узлов доступны с помощью Kubernetes Platform Monitoring.

3

Поддерживается для развёртывания на основе контейнеров через Dynatrace Operator (см. [OpenShift](/managed/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace на Kubernetes")).

Совместимость Full-Stack Monitoring с Red Hat OpenShift

* OpenShift 4.19+: Поддерживаются только [Application observability](/managed/ingest-from/setup-on-k8s/how-it-works/application-monitoring "Подробное описание Application observability с использованием Dynatrace Operator.") и [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с использованием Dynatrace Operator."). Это связано с тем, что рабочие узлы могут работать только под управлением Red Hat Enterprise Linux CoreOS. Подробнее см. [примечания к выпуску Red Hat (1.5.13.2)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).
* OpenShift 4.16–4.18: [Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "Подробное описание Classic Full-Stack monitoring с использованием Dynatrace Operator.") поддерживается только на рабочих узлах под управлением Red Hat Enterprise Linux. Если рабочие узлы вместо этого работают под управлением Red Hat Enterprise Linux CoreOS, поддерживается только облачно-нативная [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с использованием Dynatrace Operator.").

### Unix

Dynatrace тестирует и обеспечивает поддержку установки OneAgent на версиях [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.") и [Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris "Learn how to install, update and troubleshoot OneAgent on Solaris."), перечисленных ниже.

Поддерживаемые архитектуры процессоров

* `x86-64`, 64-битные Intel/AMD
* `POWER8`, 64-битная Power ISA
* `POWER9`, 64-битная Power ISA
* `POWER10`, 64-битная Power ISA
* `SPARC`

| UNIX-система | Версии | Архитектуры процессоров |
| --- | --- | --- |
| [IBM AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.") | 7.2 TL5[1](#fn-unix-system-1-def), 7.3 TL1[1](#fn-unix-system-1-def), 7.3 TL2[1](#fn-unix-system-1-def), 7.3 TL3[1](#fn-unix-system-1-def), 7.3 TL4[1](#fn-unix-system-1-def) | POWER10, POWER8, POWER9 |
| [Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris "Learn how to install, update and troubleshoot OneAgent on Solaris.") | 11.4 | SPARC, x86-64 |

1

Установка на AIX WPAR не поддерживается.

### Windows

Dynatrace тестирует и обеспечивает поддержку установки OneAgent только на версиях [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more."), перечисленных ниже.

Поддерживаемые архитектуры процессоров

* `x86-64`, 64-битные Intel/AMD

| ОС Windows | Версии | Архитектуры процессоров |
| --- | --- | --- |
| [Windows Desktop 10](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 22H2[1](#fn-windows-os-1-def), 1607[2](#fn-windows-os-2-def), 1809[2](#fn-windows-os-2-def), 21H2[2](#fn-windows-os-2-def) | x86-64 |
| [Windows Desktop 11](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 23H2, 24H2, 25H2 | x86-64 |
| [Windows Server](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 2012 R2[3](#fn-windows-os-3-def), 2016[4](#fn-windows-os-4-def), 2019[4](#fn-windows-os-4-def), 2022[4](#fn-windows-os-4-def), 2025[4](#fn-windows-os-4-def) | x86-64 |
| [Windows Server - Nano](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | Поддерживаются все версии[5](#fn-windows-os-5-def) | x86-64 |

1

Windows 10 Semi-Annual Channel (SAC), кроме Windows 10 IoT.

2

Windows 10 Long-Term Servicing Channel (LTSC), кроме Windows 10 IoT.

3

Windows 2012 R2 не поддерживается на версиях OneAgent с 1.287 по 1.305. Если OneAgent находится на одной из этих версий, нужно обновить до версии OneAgent 1.307, чтобы включить поддержку.

4

Long-Term Servicing Channel (LTSC). Поддержка включает установку Server Core (требует установки OneAgent в headless-режиме) или мониторинг по сценарию app-only.

5

Ограниченная поддержка на основе совместимости с поддержкой Windows Server при использовании в качестве образа контейнера.

## Файловые системы

OneAgent может обнаруживать и создавать сущности дисков (`dt.entity.disk`) на следующих файловых системах:

| Файловая система |
| --- |
| ACFS [1](#fn-1-1-def) |
| AFS |
| btrfs |
| CIFS |
| ecryptfs |
| ext, ext2, ext,3 ext4 |
| fuse.glusterfs [2](#fn-1-2-def) |
| GPFS [3](#fn-1-3-def) |
| GFS2 [4](#fn-1-4-def) |
| HFS |
| HPFS |
| ISO9660 |
| JFS |
| LVM2\_member, LVM\_member |
| MINIX |
| msdos |
| ncpfs |
| NFS |
| NTFS |
| overlay [6](#fn-1-6-def) |
| ReiserFS |
| SMB |
| SquashFS |
| sysv |
| tmpfs [7](#fn-1-7-def) |
| umsdos |
| VFAT |
| VXFS [5](#fn-1-5-def) |
| XFS |
| Xiafs |
| ZFS |

1

Начиная с версии OneAgent 1.307+.

2

Начиная с версии OneAgent 1.307+. Поддерживается только статистика по объёму.

3

Если команда `mmpmonSocket` на Linux завершается ошибкой, доступен резервный режим, который работает при включённой возможности CAP\_SETUID. Подробнее см. [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#capsetuid-osagent "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

4

Начиная с версии OneAgent 1.309+.

5

Начиная с версии OneAgent 1.303+. Поддерживается только статистика по объёму.

6

Начиная с версии OneAgent 1.323+. Поддерживается только статистика по объёму.

7

Начиная с версии OneAgent 1.331+. Поддерживается только статистика по объёму. Функция с ручным включением, нужно включить в настройках дисков.

## Контейнеры

| Функции | Версии |
| --- | --- |
| Автоматическое внедрение в контейнер [Docker﻿](https://www.docker.com/) (Deep monitoring)[1](#fn-2-1-def) | 1.6+ (32 и 64 бит), требуется glibc или musl-libc |
| Автоматическое внедрение в контейнер [containerd﻿](https://containerd.io/) (Deep monitoring) | 1.1.2+ (32 и 64 бит), требуется glibc или musl-libc |
| Автоматическое внедрение в контейнер [CRI-O﻿](https://cri-o.io/) (Deep monitoring) | 1.12.5+ (32 и 64 бит), требуется glibc или musl-libc |
| Автоматическое внедрение в контейнер [Garden-RunC﻿](https://docs.cloudfoundry.org/concepts/architecture/garden.html#garden-runc) (Deep monitoring) | 1.0.0+ (32 и 64 бит), требуется glibc или musl-libc |
| Автоматическое внедрение в контейнер [BOSH bpm﻿](https://bosh.io/docs/bpm/bpm/) (Deep monitoring) | 0.11.0+ |
| Автоматическое внедрение в контейнер [Podman﻿](https://podman.io/) (Deep monitoring)[2](#fn-2-2-def)[3](#fn-2-3-def) | 3.4.4–5.x.x |
| Метрики контейнера Docker[1](#fn-2-1-def) | 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 RC2, 1.13.1, 17.03+ CE и EE |

1

См. [известные ограничения мониторинга контейнеров Docker](/managed/observe/infrastructure-observability/container-platform-monitoring/container-groups#limitations "Overview on container groups monitoring").

2

Поддерживается для OneAgent 1.267+, установленного на узле Podman с использованием среды выполнения контейнеров [crun﻿](https://github.com/containers/crun); версии Podman 0.17-1.15 с использованием среды выполнения `runc` не поддерживаются.

3

Контейнеры Podman, запущенные с `read-only=true` или с нестандартным ремаппингом пространства имён пользователя, не поддерживаются. К нестандартному ремаппингу пространства имён пользователя относятся контейнеры, запущенные с `--userns=keep-id`, `--userns=auto`, `--userns=nomap` или с пользовательскими сопоставлениями `--uidmap`/`--gidmap`.

## Гипервизоры

|  |
| --- |
| AIX (LPAR) |
| Hyper-V |
| KVM |
| Nutanix AHV[1](#fn-3-1-def) |
| QEMU |
| Xen |
| [VMware](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.") |
| AWS Nitro[1](#fn-3-1-def) |
| OpenShift Virtualization |

1

Dynatrace обнаруживает гипервизор, но выделенная логика не применяется.

## Сетевые интерфейсы

|  |
| --- |
| IEEE 802.3 Ethernet |
| IEEE 802.11 Wireless LAN |
| Виртуальное сетевое устройство OpenVZ (venet) |

* Поддерживаются как физические, так и виртуальные интерфейсы при условии, что им не назначен link-local адрес.

  + Для IPv4: link-local адреса находятся в диапазоне от `169.254.1.0` до `169.254.254.255`.
  + Для IPv6: link-local адреса находятся в диапазоне от `0xFE800000` до `0xFEBFFFFF`.
* Интерфейсы виртуального Ethernet-моста не поддерживаются.
* Поддерживается объединение сетевых интерфейсов (bonding).
* Для мониторинга трафика поддерживается только протокол TCP.

## Облачные платформы

### [AWS](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")

| Amazon Web Services (AWS) |
| --- |
| DynamoDB |
| Elastic Block Store (EBS) |
| Elastic Compute Cloud (EC2) |
| Elastic Load Balancing (ELB) |
| [Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.") |
| [Relational Database Service (RDS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/view-aws-monitoring-results#relational-database-service-page "Display AWS monitoring results in Dynatrace on your home dashboard, AWS account page, host page, and more.") |
| [Simple Storage Service (S3)](/managed/ingest-from/amazon-web-services/aws-platform/set-up-cors-in-amazon-s3 "Integrate CORS in Amazon Web Services for buckets within Amazon S3.") |

### [Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")

| Compute service | Расширение для развёртывания OneAgent | Интеграция Dynatrace с Azure Monitor |
| --- | --- | --- |
| [Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm "Learn how to install and configure OneAgent for monitoring Azure Virtual Machines using a VM extension.") | VM-Extension[1](#fn-4-1-def) | да |
| [Virtual Machine Scale Set](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.") | VM-Extension[1](#fn-4-1-def) | да |
| [Service Fabric](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure Service Fabric using a VM extension.") | VM-Extension[1](#fn-4-1-def) | да |
| [Azure Kubernetes Service (AKS)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Learn how to deploy, operate, and maintain OneAgent on Azure Kubernetes Service.") | Operator-rollout[2](#fn-4-2-def) | нет |
| Cloud-Services (Classic) | [Startup script﻿](https://github.com/dtPaTh/Dynatrace-Azure-CloudServices) | нет |
| [HDInsight﻿](https://github.com/safia-habib/Azure/blob/master/HDInsights/Readme.md) | Startup-Script | да |
| [App Service](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service "Install, configure, update, uninstall, and troubleshoot OneAgent for monitoring Azure App Service on Windows using an Azure site extension.") (на базе Windows) | SiteExtension | да |
| [Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | SiteExtension (релиз Early Access) | да |

1

VM-Extension автоматизирует установку OneAgent с помощью нативных средств автоматизации Azure. OneAgent также можно установить вручную или через любой другой инструмент автоматизации.

2

Windows Pods и Nodes не поддерживаются.

| Platform service | Поддержка code-module OneAgent | Интеграция Dynatrace с Azure Monitor |
| --- | --- | --- |
| Blob-Storage | HttpClient[1](#fn-5-1-def) | да |
| Table-Storage | HttpClient[1](#fn-5-1-def) | да |
| Queue-Storage | HttpClient[1](#fn-5-1-def) | да |
| File-Storage | Infrastructure monitoring | да |
| Disk-Storage | Infrastructure monitoring | да |
| ServiceBus Queues and Topics | Microsoft Azure Service Bus Client for .NET | да |
| Load-Balancer | Infrastructure monitoring | да[3](#fn-5-3-def) |
| Application Gateway | Trace-Context[4](#fn-5-4-def) | да |
| API Management | Trace-Context[4](#fn-5-4-def), SDK[5](#fn-5-5-def) | да |
| Azure SQL | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | да |
| Azure SQL elastic pool | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | да |
| Azure SQL Managed Instance | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | нет |
| SQL Data Warehouse | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | нет |
| SQL Server Stretch | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | нет |
| Azure DB for MySql | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | нет |
| Azure DB for PostgreSQL | Поддерживаемые фреймворки баз данных[2](#fn-5-2-def) | нет |
| CosmosDB | MongoDB API, Cassandra API, HttpClient[1](#fn-5-1-def) | да |
| Redis Cache | Поддерживаемые клиентские библиотеки | да |
| Event Hubs | SDK[5](#fn-5-5-def) | да |
| IoT Hub | Trace Context[4](#fn-5-4-def), SDK[5](#fn-5-5-def) | да |

1

Трассировка HTTP-вызовов через поддержку HttpClient

2

Трассировка вызовов баз данных через поддерживаемые фреймворки баз данных (например, ADO.NET или JDBC).

3

Доступно только для [Standard Load Balancer﻿](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-standard-overview#why-use-standard-load-balancer)

4

Сквозная трассировка через [Trace Context﻿](https://www.w3.org/TR/trace-context/)

5

Сквозная трассировка с помощью [OneAgent SDK﻿](https://github.com/Dynatrace/OneAgent-SDK)

### [Google Cloud](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")

| Сервисы Google Cloud |
| --- |
| [Google Kubernetes Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-gke "Google GKE") |
| [GKE Autopilot](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed#automatic "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") (только для автоматического `applicationMonitoring`) |
| [Google App Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") |
| [Google Compute Engine](/managed/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine "Install OneAgent on Google Compute Engine.") |

### [VMware](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.")

| VMware | Версии |
| --- | --- |
| ESXi host | 6.5, 6.7, 7, 8.0 |
| vCenter server | 6.5, 6.7, 7, 8.0 |

### [Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")

Dynatrace поддерживает множество разновидностей Kubernetes согласно [модели поддержки Kubernetes и Openshift](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

| Дистрибутивы |
| --- |
| Google Anthos |
| Mirantis Kubernetes Engine [1](#fn-6-1-def) |
| Rancher Kubernetes Engine 2.0 |
| Red Hat OpenShift Container Platform |
| VMware Tanzu Kubernetes Grid Integrated Edition (ранее Pivotal Kubernetes Service) |
| Nutanix Kubernetes Platform (NKP, ранее D2iQ Konvoy) [1](#fn-6-1-def) |
| Oracle Container Engine for Kubernetes (OKE) [1](#fn-6-1-def) |
| Amazon Elastic Kubernetes Service |
| Azure Kubernetes Service |
| Google Kubernetes Engine |
| RedHat OpenShift Service on AWS (ROSA) |
| IBM Kubernetes Service |
| OpenShift Dedicated |
| SUSE Container as a Service platform |
| GKE Autopilot |

1

Ограниченная поддержка на основе совместимости с upstream Kubernetes.

Некоторые дистрибутивы и хостинговые версии требуют дополнительной настройки. Подробнее см. [Поддержка технологий](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Другие платформы для контейнеров и PaaS

### [Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")

| Buildpacks | Версии |
| --- | --- |
| Java buildpack | 3.11+ |
| PHP buildpack | v4.3.34+ |
| Staticfile buildpack | v1.4.6+ |
| Go buildpack | v1.8.41+ |
| .NET Core on Linux buildpack | v3.1+ |
| Node.js buildpack | v1.6.10+ (требует OneAgent версии 1.131 или выше) |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ [См. известную проблему](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.") |
| HWC buildpack | v3.1.48+ |
| Nginx buildpack | v1.1.40+ |
| Python buildpack | v1.8.7+ |

#### [IBM Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")

| Функции | Версии |
| --- | --- |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ [См. известную проблему](/managed/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.") |

#### [Cloud Foundry](/managed/ingest-from/technology-support/support-model-for-pivotal-platform "Read about Dynatrace support for VMware Tanzu Application Service.")

| Функции | Версии |
| --- | --- |
| Garden-runC | v1.0.0+ |
| BOSH BPM for platform process isolation | v0.11.0+ |
| Winc for Windows Server containers | Windows server 1709+ |
| VMware Tanzu Application Service (через BOSH add-on) | [См. модель поддержки Tanzu Application Service](/managed/ingest-from/technology-support/support-model-for-pivotal-platform "Read about Dynatrace support for VMware Tanzu Application Service.") |

### [Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")

| Функции | Версии |
| --- | --- |
| Stack | Heroku-18 |
| Stack | Heroku-20 |
| Stack | Heroku-22 |
| Stack | Heroku-24 (по умолчанию) |

## Application Security

Подробности см. в разделе [Поддерживаемые технологии](/managed/secure/application-security#tech "Access the Dynatrace Application Security functionalities.").

## Приложения, сервисы и базы данных

### [Java](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.")


Подробности см. в разделе [Dynatrace support/desupport for Java versions](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.").


| Virtual machines | Versions | Platforms |
| --- | --- | --- |
| Amazon Corretto | 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | Linux (x86-64, ARM64 (AArch64)) |
| Azul Platform Core (Zulu) | 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| Azul Platform Prime (Zing) | 6[2](#fn-virtual-machines-2-def), 7[2](#fn-virtual-machines-2-def), 8 LTS[2](#fn-virtual-machines-2-def), 11 LTS[2](#fn-virtual-machines-2-def) | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |
| Bellsoft Liberica | 8 LTS, 11 LTS, 17 LTS, 21 LTS[3](#fn-virtual-machines-3-def), 23, 24, 25 LTS, 26 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64), PPCLE), Solaris (SPARC, x86-64), Windows (x86-64) |
| Eclipse Temurin (a.k.a. 'Adoptium') | 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | AIX (POWER8, POWER9, POWER10), Linux (x86-64, ARM64 (AArch64), PPCLE, s390), Windows (x86-64) |
| Fujitsu | 5, 6, 8 | Linux (x86-64), Windows (x86-64) |
| GraalVM | 17 LTS[1](#fn-virtual-machines-1-def), 21[1](#fn-virtual-machines-1-def), 23[1](#fn-virtual-machines-1-def), 24[1](#fn-virtual-machines-1-def), 25 LTS[1](#fn-virtual-machines-1-def) | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| Hitachi | 5 | Windows (x86-64) |
| Huawei | 8 | Linux (ARM64 (AArch64)) |
| IBM JVM | 6, 7, 8 LTS | AIX (POWER8, POWER9, POWER10), Alpine Linux 64-bit (x86-64), Linux (PPCLE, PPCBE, s390, x86-64), Windows (x86-64) |
| IBM Semeru | 8 LTS, 11 LTS, 17 LTS, 21 LTS, 25 LTS | AIX (POWER8, POWER9, POWER10), Linux (x86-64, ARM64 (AArch64), PPCLE, s390), Windows (x86-64) |
| Microsoft OpenJDK | 11 LTS, 17 LTS, 21 LTS, 25 LTS | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| OpenJDK | 6, 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | Alpine Linux 64-bit (x86-64), Linux (x86-64, s390), Windows (x86-64) |
| Oracle HotSpot VM | 6, 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Solaris (SPARC, x86-64), Windows (x86-64) |
| Oracle JRockit | 6 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Solaris (SPARC), Windows (x86-64) |
| SapMachine | 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS, 26 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |


1


Работает на базе Oracle JVM. Про нативные образы см. [Java native images](/managed/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").


2


[Ограниченная поддержка](#limited-support): Dynatrace может обеспечить поддержку только для проблем, воспроизводимых на других JVM.


3


Bellsoft Liberica v21+ 32-bit не поддерживается


| Application servers | Versions |
| --- | --- |
| [Apache TomEE﻿](https://tomee.apache.org/) | 1, 7, 8 |
| [Apache Tomcat﻿](https://tomcat.apache.org/) | 6, 7, 8, 8.5, 9, 10[1](#fn-application-servers-1-def), 11[1](#fn-application-servers-1-def) |
| [Fujitsu Interstage﻿](https://www.fujitsu.com/global/products/software/middleware/application-infrastructure/interstage/) | 12.0[2](#fn-application-servers-2-def) |
| [IBM WebSphere Application Server﻿](https://www.ibm.com/products/software) | 8.5.5, 9.0, 8.5[3](#fn-application-servers-3-def) |
| [IBM WebSphere Liberty﻿](https://developer.ibm.com/wasdev/websphere-liberty/) | 8.5 - 26[4](#fn-application-servers-4-def) |
| [JBoss Enterprise Application Platform﻿](https://developers.redhat.com/products/eap/overview) | 7, 8 |
| [Oracle WebLogic﻿](https://www.oracle.com/middleware/technologies/weblogic.html) | 11g[5](#fn-application-servers-5-def), 12c, 14c, 15.1.1[6](#fn-application-servers-6-def) |
| [Payara﻿](https://www.payara.fish/) | 5, 6, 7 |
| [WildFly﻿](https://wildfly.org/) | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 - 26, 27 - 40 |


1


Для этой версии требуется включённая функция поддержки Java Servlet 5.0


2


[Ограниченная поддержка](#limited-support): полностью поддерживаемая базовая технология: Java


3


Начиная с версии OneAgent 1.183 в WebSphere Application Server 8.5 поддерживается только Java 7


4


Servlet 5 engine в Websphere Liberty поддерживается начиная с версии OneAgent 1.259


5


10.3 = 11g


6


WebLogic thin client jar (wlthint3client.jar) не поддерживается. IIOP имеет известные проблемы производителя в WebLogic 15.1.1; T3 поддерживается как обходное решение только для соединений между серверами.


| ESBs and SOA | Versions |
| --- | --- |
| [Apache Camel﻿](https://www.dynatrace.com/hub/detail/apache-camel/) | 2.21+, 3+, 4+[1](#fn-esbs-and-soa-1-def) |
| Apache OpenEJB | 3.1 |
| Mule (HTTP Listener) | 3.5, 3.6, 3.7, 3.8, 3.9, 4.1 - 4.9 |
| [Red Hat Fuse Standalone﻿](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| [Red Hat Fuse on OpenShift﻿](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| TIBCO ActiveMatrix BusinessWorks | 5.8.2 - 5.14[2](#fn-esbs-and-soa-2-def), 6.4[2](#fn-esbs-and-soa-2-def), 6.5[2](#fn-esbs-and-soa-2-def), 6.6 - 6.8[2](#fn-esbs-and-soa-2-def) |


1


Поддерживаются только коннекторы Apache Camel Undertow, Kafka и MongoDB.


2


Поддерживаются только рабочие процессы TIBCO, запускаемые входящим запросом веб-сервиса, HTTP-запросом или JMS-сообщением.


| Web framework | Versions |
| --- | --- |
| [Akka HTTP client﻿](https://doc.akka.io/docs/akka-http/current/client-side/index.html) | 10.1[2](#fn-web-framework-2-def), 10.0[2](#fn-web-framework-2-def), 10.2[2](#fn-web-framework-2-def), 10.4[2](#fn-web-framework-2-def), 10.5[2](#fn-web-framework-2-def), 10.6[2](#fn-web-framework-2-def), 10.7[2](#fn-web-framework-2-def) |
| [Akka HTTP server﻿](https://doc.akka.io/docs/akka-http/current/index.html) | 10.1, 10.2[1](#fn-web-framework-1-def), 10.4[1](#fn-web-framework-1-def), 10.5[1](#fn-web-framework-1-def), 10.6[1](#fn-web-framework-1-def), 10.7[1](#fn-web-framework-1-def) |
| [Apache HttpAsyncClient﻿](https://hc.apache.org/httpcomponents-asyncclient-ga/) | 4.0[4](#fn-web-framework-4-def), 4.1[4](#fn-web-framework-4-def) |
| [Apache HttpClient﻿](https://hc.apache.org/httpcomponents-client-ga/) | 3.1[4](#fn-web-framework-4-def), 4[4](#fn-web-framework-4-def), 5.0[4](#fn-web-framework-4-def), 5.1[4](#fn-web-framework-4-def), 5.2[4](#fn-web-framework-4-def) |
| [Apache HttpCore﻿](https://hc.apache.org/httpcomponents-core-ga/) | 4[3](#fn-web-framework-3-def), 5[4](#fn-web-framework-4-def) |
| [Apache Pekko HTTP client﻿](https://pekko.apache.org/docs/pekko-http/current/client-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| [Apache Pekko HTTP server﻿](https://pekko.apache.org/docs/pekko-http/current/server-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| Elasticsearch | 1.7[5](#fn-web-framework-5-def), 2.0[5](#fn-web-framework-5-def), 2.1[5](#fn-web-framework-5-def), 2.2[5](#fn-web-framework-5-def) |
| Grails | 3[6](#fn-web-framework-6-def) |
| Jakarta Servlet | 2.5, 3.0, 3.1, 4, 5, 6 |
| Java HttpUrlConnection | Поддерживаются все версии[6](#fn-web-framework-6-def) |
| [Java IMS Soap Gateway client﻿](https://www.ibm.com/support/knowledgecenter/en/SS9NWR_3.2.0/com.ibm.ims.iconapij32.doc/icon_home_java.htm) | 3.2 |
| Jetty HTTP client | 7[6](#fn-web-framework-6-def), 8[6](#fn-web-framework-6-def), 9[6](#fn-web-framework-6-def), 10[6](#fn-web-framework-6-def), 11[6](#fn-web-framework-6-def), 12[6](#fn-web-framework-6-def) |
| [Jetty HTTP server﻿](https://www.eclipse.org/jetty/) | 7, 8, 9, 10, 11, 12 |
| LinkerdD | 1 |
| [Netty﻿](https://netty.io/) | 3.10[7](#fn-web-framework-7-def), 4[7](#fn-web-framework-7-def) |
| [Ning Asynchronous HTTP Client﻿](https://github.com/AsyncHttpClient/async-http-client) | 1.8, 1.9, 2, 3 |
| OkHttp | 3[7](#fn-web-framework-7-def), 4.0 - 4.3[7](#fn-web-framework-7-def), 4.4 - 4.12[7](#fn-web-framework-7-def), 5.+[7](#fn-web-framework-7-def) |
| [Play Framework﻿](https://www.playframework.com/) | 2.2 - 2.6, 2.7, 2.8 |
| [Reactor Netty HTTP Client﻿](https://github.com/reactor/reactor-netty) | 0.8[7](#fn-web-framework-7-def), 0.9[7](#fn-web-framework-7-def), 1.0[7](#fn-web-framework-7-def), 1.1[7](#fn-web-framework-7-def), 1.2[7](#fn-web-framework-7-def), 1.3[7](#fn-web-framework-7-def) |
| [Reactor Netty HTTP Server﻿](https://github.com/reactor/reactor-netty) | 0.6, 0.7, 0.8, 0.9, 1.0 |
| [RxJava﻿](https://github.com/ReactiveX/RxJava) | 3+ |
| Software AG WebMethods Integration Server | 9.0[8](#fn-web-framework-8-def), 9.5 - 9.12[8](#fn-web-framework-8-def), 10.0 - 10.15[8](#fn-web-framework-8-def), 10.7[8](#fn-web-framework-8-def), 10.11[8](#fn-web-framework-8-def), 10.15[8](#fn-web-framework-8-def) |
| [Spring WebFlux﻿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html) | 5, 6, 7 |
| [Spring WebFlux WebClient﻿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 5, 6, 7 |
| [Undertow﻿](https://undertow.io/) | 1[9](#fn-web-framework-9-def), 2.0 - 2.2[9](#fn-web-framework-9-def), 2.3+ |
| [Vert.x HttpClient﻿](https://github.com/eclipse-vertx/vert.x) | 3.6+[10](#fn-web-framework-10-def), 4.x[10](#fn-web-framework-10-def), 5.x[10](#fn-web-framework-10-def) |
| [Vert.x WebClient﻿](https://github.com/vert-x3/vertx-web) | 3.6+[10](#fn-web-framework-10-def), 4.x[10](#fn-web-framework-10-def), 5.x[10](#fn-web-framework-10-def) |


1


Поддерживаются привязки для Java и Scala.


2


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").


3

Поддерживается только синхронная обработка запросов. Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


4


Поддерживается только обработка запросов по HTTP/1.1. Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


5


В настоящее время поддерживается только веб-протокол, проприетарный TCP-протокол не поддерживается.


6


только в контейнере сервлетов


7


Интерфейс Promise и связанные API не поддерживаются.


8


Мониторинг Dynatrace ограничен входящими веб-запросами или JMS-сообщениями, которые запускают workflow (бизнес-логику) на WebMethods.


9


В настоящее время Dynatrace может захватывать входящие HTTP-запросы только когда Undertow настроен на использование Servlet API.


10


Поддерживаются привязки Java и Scala 2.

| Многопоточность | Версии |
| --- | --- |
| CompletableFuture | Поддерживаются все версии[1](#fn-threading-1-def) |
| [Java ForkJoin﻿](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html) | Поддерживаются все версии[1](#fn-threading-1-def) |
| Kotlin Coroutines | 1.10.2–2.1 |
| Spring Integration | 2[1](#fn-threading-1-def), 3[1](#fn-threading-1-def), 4[1](#fn-threading-1-def), 5[1](#fn-threading-1-def), 6[1](#fn-threading-1-def), 7[1](#fn-threading-1-def) |
| [reactor-core﻿](https://github.com/reactor/reactor-core) | 3[1](#fn-threading-1-def) |


1


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


| Веб-сервисы | Версии |
| --- | --- |
| Apache Axis2 | 1.6, 1.7, 1.8 |
| Apache CXF | 2, 3, 4 |
| Hessian Web Services | 2.1, 3.1, 4.0 |
| JAX-WS | 2 |
| [JBoss RESTEasy﻿](https://resteasy.dev/) | 3, 4, 5, 6, 7 |
| JBossWS (Wildfly) | 4[1](#fn-web-services-1-def), 5[2](#fn-web-services-2-def) |
| Jakarta RESTful Web Services | 2.1+ |
| Jersey | 1, 2, 3 |
| Play WS API | 2.2–2.4 |
| REST веб-сервисы через фреймворк WINK | 1.2, 1.4 |
| Spring Web Services | 2, 3, 4 |


1


Wildfly 8


2


Wildfly 8, 9, 10


| Фреймворки для работы с базами данных | Версии |
| --- | --- |
| Amazon DynamoDB | 1[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def) |
| Apache Thrift | 2 |
| DataStax client for Apache Cassandra | 2.1[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| JDBC | 4+[1](#fn-database-frameworks-1-def) |
| [Jedis Redis﻿](https://github.com/xetorthio/jedis) | 2, 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def), 5[1](#fn-database-frameworks-1-def), 6[1](#fn-database-frameworks-1-def), 7[1](#fn-database-frameworks-1-def) |
| [Lettuce﻿](https://lettuce.io/) | 5.1–5.3[1](#fn-database-frameworks-1-def), 6.0.3–6.1.6[1](#fn-database-frameworks-1-def), 6.1.8–6.8[1](#fn-database-frameworks-1-def), 7.0–7.5[1](#fn-database-frameworks-1-def) |
| [MongoDB asynchronous driver﻿](https://mongodb.github.io/mongo-java-driver/3.0/driver-async/) | 3.0–3.6.4[1](#fn-database-frameworks-1-def) |
| [MongoDB synchronous driver ﻿](https://docs.mongodb.com/ecosystem/drivers/java/) | 2[1](#fn-database-frameworks-1-def), 3.0–3.6[1](#fn-database-frameworks-1-def), 3.7–3.11[1](#fn-database-frameworks-1-def), 3.12–4.11[1](#fn-database-frameworks-1-def), 5.0[1](#fn-database-frameworks-1-def) |
| [Redisson﻿](https://redisson.pro/) | 3+ |
| Spring Boot Starter Data MongoDB | 2, 3, 4 |
| Spring Boot Starter Data Redis | 2.1+ |


1


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


| Клиенты обмена сообщениями | Версии |
| --- | --- |
| [ActiveMQ﻿](https://activemq.apache.org) | 4[1](#fn-messaging-clients-1-def), 5[1](#fn-messaging-clients-1-def) |
| [ActiveMQ Artemis﻿](https://activemq.apache.org/components/artemis/) | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon EventBridge | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| HornetQ | 2.2[1](#fn-messaging-clients-1-def), 2.3[1](#fn-messaging-clients-1-def), 2.4[1](#fn-messaging-clients-1-def) |
| [IBM MQ client﻿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q118320_.htm) | 8[1](#fn-messaging-clients-1-def), 9[1](#fn-messaging-clients-1-def) |
| JMS | 1.1[1](#fn-messaging-clients-1-def), 2.0[1](#fn-messaging-clients-1-def), 3.0[1](#fn-messaging-clients-1-def) |
| [Kafka﻿](https://kafka.apache.org/documentation/) | 1.0–1.1[1](#fn-messaging-clients-1-def), 2.0–2.3[1](#fn-messaging-clients-1-def), 2.4–2.7[1](#fn-messaging-clients-1-def), 2.8[1](#fn-messaging-clients-1-def), 3.0–3.6[1](#fn-messaging-clients-1-def), 3.7–3.9[1](#fn-messaging-clients-1-def), 4.0–4.3[1](#fn-messaging-clients-1-def) |
| [RabbitMQ﻿](https://www.rabbitmq.com/java-client.html) | 3[1](#fn-messaging-clients-1-def), 4.0.0–5.22.0[1](#fn-messaging-clients-1-def) |
| Software AG WebMethod Broker and Universal messaging via JMS | Поддерживаются все версии |
| [Spring AMQP﻿](https://spring.io/projects/spring-amqp) | 1.5, 2.0, 2.1, 2.2, 2.3 |
| Spring Cloud Stream Kafka Binder | 3+ |
| Tibco EMS | Поддерживаются все версии[2](#fn-messaging-clients-2-def) |


1


Издатели (publishers) поддерживаются в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


2


Трассировка поддерживается только через JMS.


| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Akka Remoting﻿](https://doc.akka.io/docs/akka/2.5/remoting.html) | 2.4[2](#fn-remoting-frameworks-2-def), 2.5[2](#fn-remoting-frameworks-2-def), 2.3[3](#fn-remoting-frameworks-3-def), 2.6[3](#fn-remoting-frameworks-3-def), 2.7[3](#fn-remoting-frameworks-3-def) |
| [Amazon AWS Lambda SDK﻿](https://aws.amazon.com/en/sdk-for-java/) | 1[1](#fn-remoting-frameworks-1-def), 2[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 1[2](#fn-remoting-frameworks-2-def), 2[2](#fn-remoting-frameworks-2-def) |
| [Apache Pekko Remoting﻿](https://pekko.apache.org/docs/pekko/current/remoting.html#classic-remoting-deprecated-) | 1.0.0–1.2.0[6](#fn-remoting-frameworks-6-def) |
| [Apache Thrift﻿](https://thrift.apache.org/) | 0.7–0.13 |
| [Azure SDK﻿](https://github.com/Azure/azure-sdk-for-java) | 1.2.9+ (Azure SDK BOM) |
| Glassfish RMI-IIOP | Поддерживаются все версии |
| IBM JVM RMI-IIOP | Поддерживаются все версии |
| JBoss Enterprise Application Platform, RMI-IIOP | 7, 8 |
| JBoss Enterprise Application Platform, Remoting | 7, 8 |
| [Java CICS Transaction Gateway client﻿](https://www.ibm.com/support/knowledgecenter/en/SSZHFX_9.1.0/basejavadoc/index.html) | 9.0–9.2 |
| Java IMS TM Resource Adapter | Поддерживаются все версии |
| Java RMI-JRMP | Поддерживаются все версии |
| OpenJDK/Oracle JVM RMI-IIOP | Поддерживаются все версии |
| WebLogic RMI-IIOP | Поддерживаются все версии[5](#fn-remoting-frameworks-5-def) |
| WebSphere Liberty RMI-IIOP | Поддерживаются все версии |
| WebSphere RMI-IIOP | Поддерживаются все версии |
| [gRPC﻿](https://grpc.github.io/grpc-java/javadoc/index.html) | 1.18–1.81[4](#fn-remoting-frameworks-4-def) |


1


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


2


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda"). Расширенная поддержка трассировки для всех вызовов сервисов AWS


3


Поддерживается только при использовании Netty, при использовании Artery не поддерживается. Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


4


Вызовы клиента gRPC поддерживаются в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


5


В WebLogic 15.1.1 известны проблемы с IIOP на стороне вендора. T3 поддерживается как обходной путь только для соединений сервер-сервер; соединения тонкого клиента не поддерживаются.


6


Поддерживается только при использовании classic-remoting, при использовании Artery не поддерживается. Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0–1.3[1](#fn-monitoring-frameworks-1-def), 1.4–1.54[1](#fn-monitoring-frameworks-1-def), 1.55–1.60 |
| [OpenTracing﻿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |


1


Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").


| Фреймворки логирования | Версии |
| --- | --- |
| Apache Tomcat access logs | 8, 9, 10, 11 |
| [JBoss LogManager﻿](https://github.com/jboss-logging/jboss-logmanager) | 1.1+, 2, 3 |
| [Log4J2 (Apache)﻿](https://logging.apache.org/log4j/2.x/) | 2.7–2.12, 2.13.0, 2.13.1, 2.13.3, 2.14–2.17.1, 2.17.2–2.26 |
| [Logback (QOS)﻿](https://logback.qos.ch/) | 1.x |
| java.util.logging | Поддерживаются все версии |

См. также [OneAgent SDK for Java](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых пока нет готового модуля кода.") для дополнительных возможностей ручной трассировки.

### [Java Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.")

| Виртуальная машина | Версии | Платформы |
| --- | --- | --- |
| [GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.") | GraalVM for JDK 17 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 21 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 24[1](#fn-virtual-machine-1-def), GraalVM 25[1](#fn-virtual-machine-1-def) | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

Бинарные файлы, работающие на системах Linux на основе Alpine, не поддерживаются

| Фреймворк приложений | Версии |
| --- | --- |
| [Micronaut﻿](https://micronaut.io) | 3.9+[1](#fn-application-framework-1-def) |
| [Quarkus﻿](https://quarkus.io) | 3.8+[1](#fn-application-framework-1-def) |
| [Spring Boot﻿](https://spring.io/projects/spring-boot) | 3.0+[1](#fn-application-framework-1-def), 4.0+[1](#fn-application-framework-1-def) |

1

Поддерживается в отношении сборки нативных образов (native images). Это не означает, что поддерживаются все технологии, предоставляемые фреймворком.

| Веб-фреймворк | Версии |
| --- | --- |
| [Apache HttpClient﻿](https://hc.apache.org/httpcomponents-client-ga/) | 5.2+ |
| [Netty﻿](https://netty.io/) | 4[1](#fn-web-framework-1-def) |
| [Spring WebFlux WebClient﻿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 6, 7 |

1

Интерфейс Promise и связанные с ним APIы не поддерживаются.

| Серверы приложений | Версии |
| --- | --- |
| [Apache Tomcat﻿](https://tomcat.apache.org/) | 10, 11 |

| Фреймворки баз данных | Версии |
| --- | --- |
| Spring Boot Starter Data MongoDB | 3 |

### [.NET](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.")

Dynatrace поддерживает приложения .NET, написанные на C#. Также доступна ограниченная поддержка приложений .NET, написанных на других языках, хотя она явно не тестируется.

| Среда выполнения | Версии | Платформы |
| --- | --- | --- |
| [.NET and .NET Core](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | Core 2.1, Core 2.2, Core 3.0, Core 3.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |
| [.NET and .NET Core](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | 5, 6, 7, 8, 9, 10 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Веб-фреймворк | Версии |
| --- | --- |
| ASP.NET Core | Поддерживаются все версии |
| ASP.NET Owin/Katana | 3.0.0+ |
| [HttpClient﻿](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | Поддерживаются все версии[1](#fn-web-framework-1-def) |
| [HttpListener﻿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | Поддерживаются все версии |
| [HttpWebRequest﻿](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | Поддерживаются все версии |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.335+

| Веб-сервис | Версии |
| --- | --- |
| [Azure Functions﻿](https://azure.microsoft.com/en-us/services/functions/) | 2 |

| Фреймворк удалённого взаимодействия | Версии |
| --- | --- |
| Amazon AWS Lambda SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| Amazon AWS SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| [gRPC﻿](https://www.nuget.org/packages/Grpc.AspNetCore) | 2.23.2+[2](#fn-remoting-framework-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.335+

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.337+

| Фреймворк баз данных | Версии |
| --- | --- |
| ADO.NET | SQL Server[1](#fn-database-framework-1-def), SQL CE[1](#fn-database-framework-1-def), Oracle с использованием Oracle.DataAccess.dll[1](#fn-database-framework-1-def) |
| Amazon DynamoDB | 3.5.0+[1](#fn-database-framework-1-def) |
| Azure Cosmos DB | 3.18+[2](#fn-database-framework-2-def) |
| [MongoDB .NET driver﻿](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7[2](#fn-database-framework-2-def), 2.8+[2](#fn-database-framework-2-def) |
| [StackExchange.Redis﻿](https://github.com/StackExchange/StackExchange.Redis) | 2.0.0+[2](#fn-database-framework-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.335+

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.337+

| Клиент обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SNS | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SQS | 3.5.0+[1](#fn-messaging-client-1-def) |
| [Azure Messaging Service Bus﻿](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+[3](#fn-messaging-client-3-def) |
| [Confluent Kafka client library﻿](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+[2](#fn-messaging-client-2-def) |
| [IBM MQ client﻿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1[2](#fn-messaging-client-2-def) |
| [MassTransit﻿](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1[3](#fn-messaging-client-3-def), 8.3.2+[3](#fn-messaging-client-3-def) |
| [Microsoft Azure Service Bus client for .NET﻿](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 5.2.0[3](#fn-messaging-client-3-def) |
| [RabbitMQ client﻿](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x[3](#fn-messaging-client-3-def), 7.x+[3](#fn-messaging-client-3-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.335+

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.337+

3

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.339+

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+[1](#fn-monitoring-framework-1-def), 1.1+[1](#fn-monitoring-framework-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.337+

| Фреймворк логирования | Версии |
| --- | --- |
| [Microsoft Logging Extensions﻿](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+[1](#fn-logging-framework-1-def) |
| [Serilog﻿](https://serilog.net/) | 2.9+[1](#fn-logging-framework-1-def) |
| [log4net﻿](https://logging.apache.org/log4net/) | 2.0.6+[1](#fn-logging-framework-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") с версией OneAgent 1.335+

См. также [OneAgent SDK для .NET](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") для возможностей ручной трассировки.

### [.NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.")

Dynatrace поддерживает .NET-приложения, написанные на C#. Доступна ограниченная поддержка .NET-приложений, написанных на других языках, хотя явно она не тестировалась.

| Среда выполнения | Версии | Платформы |
| --- | --- | --- |
| [.NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | 3.5 SP1, 4[1](#fn-runtime-1-def), 4.5[1](#fn-runtime-1-def), 4.5.1[1](#fn-runtime-1-def), 4.5.2 - 4.8 | Windows (x86-64) |

1

Ограниченная поддержка: Dynatrace может решать только те проблемы, которые воспроизводятся на поддерживаемых версиях.

| Веб-фреймворк | Версии |
| --- | --- |
| ASP.NET | Поддерживаются все версии |
| ASP.NET Core | Поддерживаются все версии |
| ASP.NET Owin/Katana | 3.0.0 - 4.0.1 |
| [HttpClient﻿](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | Поддерживаются все версии |
| [HttpListener﻿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | Поддерживаются все версии |
| [HttpWebRequest﻿](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | Поддерживаются все версии |

| Фреймворк удалённого взаимодействия | Версии |
| --- | --- |
| [.NET Remoting﻿](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/72x4h507(v=vs.100)) | Поддерживаются все версии |
| Amazon AWS Lambda SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| Amazon AWS SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| WCF | Поддерживаются все версии |

1

Паттерн IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Фреймворк работы с базами данных | Версии |
| --- | --- |
| ADO.NET | SQL Server, SQL CE, ODBC, OLEDB, Oracle с использованием Oracle.DataAccess.dll |
| Amazon DynamoDB | 3.5.0+[1](#fn-database-framework-1-def) |
| Azure Cosmos DB | 3.18+ |
| [MongoDB .NET driver﻿](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7, 2.8+ |

1

Паттерн IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SNS | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SQS | 3.5.0+[1](#fn-messaging-client-1-def) |
| [Azure Messaging Service Bus﻿](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+ |
| [Confluent Kafka client library﻿](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+ |
| [IBM MQ client﻿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1 |
| MSMQ Client | Поддерживаются все версии |
| [MassTransit﻿](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1, 8.3.2+ |
| [Microsoft Azure Service Bus client for .NET﻿](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 3.1.1, 3.2.0 - 5.2.0 |
| [RabbitMQ client﻿](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x, 7.x+ |

1

Паттерн IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

| Фреймворк логирования | Версии |
| --- | --- |
| [Microsoft Logging Extensions﻿](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+ |
| [Serilog﻿](https://serilog.net/) | 2.9+ |
| [log4net﻿](https://logging.apache.org/log4net/) | 2.0.6+ |

### [Go](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.")

* Поддержка 64-битных бинарных файлов Go, собранных с помощью:

  + [Golang.org toolchain﻿](https://dt-url.net/go)
  + [Golang.org toolchain﻿](https://dt-url.net/go) с модификациями [openssl-fips﻿](https://dt-url.net/golang-fips) (OneAgent версии 1.295+).
* [Политика выпуска Go﻿](https://dt-url.net/uos3rmi) предполагает поддержку двух последних основных версий Go.
* Подробности см. в разделе [Поддерживаемые версии Go](/managed/ingest-from/technology-support/application-software/go/support/supported-go-versions "Find out which Go versions are supported by Dynatrace.").

| Инструментарий Go | Версии | Платформы |
| --- | --- | --- |
| [Golang toolchain с модификациями FIPS (openssl-fips)﻿](https://dt-url.net/golang-fips) | 1.23.6, 1.23.9, 1.24.4, 1.24.6, 1.25.3, 1.25.5, 1.25.7, 1.25.9, 1.26.2 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |
| [Официальный Golang toolchain﻿](https://dt-url.net/go) | 1.23, 1.24, 1.25, 1.26 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Веб-фреймворк | Версии |
| --- | --- |
| net/http | Поддерживаются все версии[1](#fn-web-framework-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Фреймворки баз данных | Версии |
| --- | --- |
| [Amazon DynamoDB﻿](https://github.com/aws/aws-sdk-go-v2/tree/main/service/dynamodb) | 1.13.0-1.54.0[1](#fn-database-frameworks-1-def), 1.55.0 - 1.57.4[1](#fn-database-frameworks-1-def) |
| [Cassandra client (cassandra-gocql-driver/v2)﻿](https://github.com/apache/cassandra-gocql-driver) | 2.0.0 - 2.1.0[1](#fn-database-frameworks-1-def), 2.1.1[1](#fn-database-frameworks-1-def) |
| [Cassandra client (gocql/gocql)﻿](https://github.com/gocql/gocql) | 1.0 - 1.7[1](#fn-database-frameworks-1-def) |
| [Microsoft SQL Server (denisenkom/go-mssqldb)﻿](https://github.com/denisenkom/go-mssqldb) | 0.11 - 0.12[1](#fn-database-frameworks-1-def) |
| [Microsoft SQL Server (microsoft/go-mssqldb)﻿](https://github.com/microsoft/go-mssqldb) | 0.11 - 0.21[1](#fn-database-frameworks-1-def), 1.0 - 1.10[1](#fn-database-frameworks-1-def) |
| [MongoDB Go driver (mongo-go-driver)﻿](https://github.com/mongodb/mongo-go-driver) | 1.3 - 1.17[1](#fn-database-frameworks-1-def), 2.+[1](#fn-database-frameworks-1-def) |
| [MySQL﻿](https://github.com/go-sql-driver/mysql/) | 1.4.1[1](#fn-database-frameworks-1-def), 1.5.0[1](#fn-database-frameworks-1-def), 1.6.0[1](#fn-database-frameworks-1-def), 1.7[1](#fn-database-frameworks-1-def), 1.8 - 1.10[1](#fn-database-frameworks-1-def) |
| [PostgreSQL (jackc/pgx)﻿](https://github.com/jackc/pgx) | 4.7 - 4.18[1](#fn-database-frameworks-1-def), 5.0 - 5.10[1](#fn-database-frameworks-1-def) |
| [PostgreSQL (lib/pq)﻿](https://github.com/lib/pq/) | 1.2.0[1](#fn-database-frameworks-1-def), 1.3.0[1](#fn-database-frameworks-1-def), 1.4.0 - 1.10.9[1](#fn-database-frameworks-1-def) |
| [go-redis﻿](https://github.com/redis/go-redis) | 7[1](#fn-database-frameworks-1-def), 8.8.0 - 8.11.5[1](#fn-database-frameworks-1-def), 9[1](#fn-database-frameworks-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Клиенты обмена сообщениями | Версии |
| --- | --- |
| [Amazon SNS﻿](https://github.com/aws/aws-sdk-go-v2/tree/main/service/sns) | 1.15.0 - 1.38.0[1](#fn-messaging-clients-1-def), 1.38.1 - 1.39.17[1](#fn-messaging-clients-1-def) |
| [Amazon SQS﻿](https://github.com/aws/aws-sdk-go-v2/tree/main/service/sqs) | 1.16.0-1.42.27[1](#fn-messaging-clients-1-def) |
| [Kafka (IBM/sarama)﻿](https://github.com/IBM/sarama) | 1.40+[1](#fn-messaging-clients-1-def) |
| [Kafka (Shopify/sarama)﻿](https://github.com/Shopify/sarama) | 1.18 - 1.48[1](#fn-messaging-clients-1-def) |
| [Kafka (confluentinc/confluent-kafka-go)﻿](https://github.com/confluentinc/confluent-kafka-go) | 1.9 - 2.8[1](#fn-messaging-clients-1-def), 2.10[1](#fn-messaging-clients-1-def), 2.11[1](#fn-messaging-clients-1-def), 2.12[1](#fn-messaging-clients-1-def), 2.13.0[1](#fn-messaging-clients-1-def), 2.14.0[1](#fn-messaging-clients-1-def), 2.14.1[1](#fn-messaging-clients-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Amazon AWS Lambda SDK﻿](https://github.com/aws/aws-lambda-go) | 1.18.0-1.54.0[1](#fn-remoting-frameworks-1-def) |
| [Amazon AWS SDK﻿](https://github.com/aws/aws-sdk-go-v2) | 1.13.0 - 1.39.0[2](#fn-remoting-frameworks-2-def), 1.39.1 - 1.41.1[2](#fn-remoting-frameworks-2-def), 1.41.2 - 1.41.7[2](#fn-remoting-frameworks-2-def) |
| [gRPC﻿](https://godoc.org/google.golang.org/grpc) | 1.17 - 1.28[3](#fn-remoting-frameworks-3-def), 1.29[3](#fn-remoting-frameworks-3-def), 1.30 - 1.39[3](#fn-remoting-frameworks-3-def), 1.40 - 1.59[3](#fn-remoting-frameworks-3-def), 1.60 - 1.68[3](#fn-remoting-frameworks-3-def), 1.69 - 1.76[3](#fn-remoting-frameworks-3-def), 1.78 - 1.81[3](#fn-remoting-frameworks-3-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Расширенная поддержка трассировки для всех вызовов служб AWS

3

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7[1](#fn-monitoring-frameworks-1-def), 1.8 - 1.11.0[1](#fn-monitoring-frameworks-1-def), 1.11.1 - 1.27[1](#fn-monitoring-frameworks-1-def), 1.28 - 1.44[1](#fn-monitoring-frameworks-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Фреймворки логирования | Версии |
| --- | --- |
| [Logrus﻿](https://github.com/sirupsen/logrus) | 1.7.1 - 1.9[1](#fn-logging-frameworks-1-def) |
| [Zap﻿](https://github.com/uber-go/zap) | 1.10 - 1.28[2](#fn-logging-frameworks-2-def) |
| log/slog | Поддерживаются все версии[2](#fn-logging-frameworks-2-def) |

1

Версии 1.7.0 и более ранние не поддерживаются из-за [проблемы состояния гонки﻿](https://github.com/sirupsen/logrus/issues/1046) во фреймворке Logrus. Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

* [Поддержка ограничена стабильными релизами Go](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations#go-official-stable-releases "Learn the limitations for Go support and their workarounds.").
* В системах Linux бинарный файл приложения должен быть динамически связан, если не используется [статический мониторинг Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Learn how you can enable Go monitoring in Dynatrace.").

### [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.")

Node.js следует графику выпуска Long Term Support (LTS). В следующей таблице перечислены все версии с полной поддержкой. Однако некоторые LTS-версии, вышедшие из жизненного цикла, имеют *ограниченную* поддержку. Подробности см. в разделе [Поддержка/прекращение поддержки версий Node.js Dynatrace](/managed/ingest-from/technology-support/application-software/nodejs#support-and-desupport "Read about Dynatrace support for Node.js applications.").

| Версии Node.js | Версии | Платформы |
| --- | --- | --- |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | 20, 22, 24, 25, 26 | Alpine Linux 64-bit (x86-64), Linux (ARM64 (AArch64), PPCLE, s390, x86-64), Windows (x86-64) |

| Веб-фреймворки | Версии |
| --- | --- |
| [Connect﻿](https://www.npmjs.com/package/connect) | >=3.0.0 |
| [Express﻿](https://expressjs.com/) | 3, 4, 5 |
| [Fastify﻿](https://fastify.dev/) | >=3.3.0 |
| [Koa﻿](https://www.npmjs.com/package/koa-router) | >=7.0.0 |
| [Nest﻿](https://nestjs.com/) | >=6.0.0[2](#fn-web-frameworks-2-def) |
| [Встроенный модуль HTTP/2 Node.js﻿](https://nodejs.org/api/http2.html) | Поддерживаются все версии |
| [Встроенные модули HTTP/HTTPS Node.js﻿](https://nodejs.org/api/http.html) | Поддерживаются все версии[1](#fn-web-frameworks-1-def) |
| [hapi﻿](https://hapijs.com/) | 17+ |
| [restify﻿](https://www.npmjs.com/package/restify) | >=4.1[2](#fn-web-frameworks-2-def) |
| [router﻿](https://www.npmjs.com/package/router) | >=1.0.0[2](#fn-web-frameworks-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Nest поддерживается неявно, через базовые платформы Express или Fastify.

| Библиотеки HTTP | Версии |
| --- | --- |
| [Встроенные модули HTTP/HTTPS Node.js﻿](https://nodejs.org/api/http.html) | Поддерживаются все версии[1](#fn-http-libraries-1-def) |
| [Встроенный fetch API Node.js﻿](https://nodejs.org/api/globals.html#fetch) | >=18.0.0[1](#fn-http-libraries-1-def) |
| [HTTP-клиент Undici﻿](https://www.npmjs.com/package/undici) | Поддерживаются все версии[1](#fn-http-libraries-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Фреймворки для работы с базами данных | Версии |
| --- | --- |
| Amazon DynamoDB | 2[1](#fn-database-frameworks-1-def), 3.0-3.901[1](#fn-database-frameworks-1-def), 3.902+[1](#fn-database-frameworks-1-def) |
| [Couchbase﻿](https://www.npmjs.com/package/couchbase) | 2.4[1](#fn-database-frameworks-1-def), 2.5[1](#fn-database-frameworks-1-def), 2.6[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| [IOredis﻿](https://www.npmjs.com/package/ioredis) | 4[2](#fn-database-frameworks-2-def), 5[2](#fn-database-frameworks-2-def) |
| [MongoDB﻿](https://www.npmjs.com/package/mongodb) | 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), >=4[1](#fn-database-frameworks-1-def) |
| [MySQL﻿](https://www.npmjs.com/package/mysql) | 2[1](#fn-database-frameworks-1-def) |
| [MySQL2﻿](https://www.npmjs.com/package/mysql2) | 1.6[1](#fn-database-frameworks-1-def), 1.7[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def) |
| [PostgreSQL﻿](https://www.npmjs.com/package/pg) | 5[2](#fn-database-frameworks-2-def), 6[2](#fn-database-frameworks-2-def), 7[2](#fn-database-frameworks-2-def), 8[2](#fn-database-frameworks-2-def) |
| [Redis﻿](https://www.npmjs.com/package/redis) | 0.10[2](#fn-database-frameworks-2-def), 0.12[2](#fn-database-frameworks-2-def), 1.0[2](#fn-database-frameworks-2-def), 2.5[2](#fn-database-frameworks-2-def), 3[2](#fn-database-frameworks-2-def), 4[2](#fn-database-frameworks-2-def), 5[2](#fn-database-frameworks-2-def), 4[2](#fn-database-frameworks-2-def) |
| [SQLite3 (только передача контекста)﻿](https://www.npmjs.com/package/sqlite3) | <5, 5.1+[3](#fn-database-frameworks-3-def) |
| [mssql﻿](https://www.npmjs.com/package/mssql) | >=5[1](#fn-database-frameworks-1-def) |
| [oracledb﻿](https://www.npmjs.com/package/oracledb) | 5[2](#fn-database-frameworks-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Следующие APIы Oracle не поддерживаются: NoSQL, advanced queuing, two-phase commit и continuous query notification.

3

Обрати внимание, версии 5.0 не поддерживаются

| Фреймворки для API-запросов | Версии |
| --- | --- |
| [GraphQL﻿](https://www.dynatrace.com/hub/detail/graphql/) | 15+[1](#fn-api-querying-frameworks-1-def) |
| [GraphQL Yoga﻿](https://www.npmjs.com/package/graphql-yoga) | 5.7+[2](#fn-api-querying-frameworks-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Требуется Dynatrace Cluster версии 1.262+. Обнаружение сбоев служб не поддерживается.

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Требуется Dynatrace Cluster версии 1.334+. Обнаружение сбоев служб не поддерживается.

| Клиенты обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| [Библиотека клиента KafkaJs﻿](https://www.npmjs.com/package/kafkajs) | 1.11+[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| [RabbitMQ﻿](https://www.npmjs.com/package/amqplib) | 0.2[2](#fn-messaging-clients-2-def), 0.3.2[2](#fn-messaging-clients-2-def), 0.4.2[2](#fn-messaging-clients-2-def), 0.5[2](#fn-messaging-clients-2-def), 0.6[2](#fn-messaging-clients-2-def), 0.7[2](#fn-messaging-clients-2-def), 0.8[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Издатели RabbitMQ поддерживаются в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Amazon AWS Lambda SDK﻿](https://aws.amazon.com/sdk-for-javascript/) | 2[1](#fn-remoting-frameworks-1-def), 3.0-3.901[1](#fn-remoting-frameworks-1-def), 3.902+[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 2[2](#fn-remoting-frameworks-2-def), 3.0-3.901[2](#fn-remoting-frameworks-2-def), 3.902+[2](#fn-remoting-frameworks-2-def) |
| [gRPC﻿](https://grpc.github.io/grpc/node/) | 1.10 - 1.24 |
| [grpc-js﻿](https://www.npmjs.com/package/@grpc/grpc-js) | 1[3](#fn-remoting-frameworks-3-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Расширенная поддержка трассировки для всех вызовов служб AWS

3

Вызовы клиента gRPC поддерживаются в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-frameworks-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Кэш | Версии |
| --- | --- |
| [Memcached﻿](https://www.npmjs.com/package/memcached) | 2.2[1](#fn-cache-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Фреймворки логирования | Версии |
| --- | --- |
| [Bunyan﻿](https://www.npmjs.com/package/bunyan) | 1+[1](#fn-logging-frameworks-1-def) |
| [log4js﻿](https://www.npmjs.com/package/log4js) | >=6.0.0[1](#fn-logging-frameworks-1-def) |
| [pino﻿](https://www.npmjs.com/package/pino) | 5.14+[1](#fn-logging-frameworks-1-def), >=6[1](#fn-logging-frameworks-1-def) |
| [winston﻿](https://www.npmjs.com/package/winston) | 3[1](#fn-logging-frameworks-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

См. также [OneAgent SDK для Node.js](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") для возможностей ручной трассировки.

### Python

| Среда выполнения Python | Версии | Платформы |
| --- | --- | --- |
| CPython | 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)) |

| Веб-фреймворки | Версии |
| --- | --- |
| [Django﻿](https://github.com/django/django) | 1.8+[1](#fn-web-frameworks-1-def) |
| [Falcon﻿](https://falconframework.org/) | 4.0+ |
| [FastAPI﻿](https://github.com/tiangolo/fastapi) | 0.44+ |
| [Flask﻿](https://github.com/pallets/flask) | 1.1.2+ |
| [Sanic﻿](https://github.com/sanic-org/sanic) | 22.12+ |
| [Starlette﻿](https://github.com/encode/starlette) | 0.12+ |
| [Tornado﻿](https://github.com/tornadoweb/tornado) | 6.0+ |
| [aiohttp Server﻿](https://docs.aiohttp.org/en/stable/web.html) | 3.6.1+ |

1

Включая Django REST framework, на основе поддерживаемых версий Django.

| HTTP-библиотеки | Версии |
| --- | --- |
| [Requests﻿](https://github.com/psf/requests) | 2[1](#fn-http-libraries-1-def) |
| [aiohttp Client﻿](https://docs.aiohttp.org/en/stable/client.html#aiohttp-client) | 3.0+[1](#fn-http-libraries-1-def) |
| [httpx﻿](https://www.python-httpx.org/) | 0.20.0+ |
| [urllib3﻿](https://github.com/urllib3/urllib3) | 2.0+[1](#fn-http-libraries-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").

| Фреймворки для работы с базами данных | Версии |
| --- | --- |
| Amazon DynamoDB | 1.11+[1](#fn-database-frameworks-1-def) |
| [PyMongo﻿](https://pymongo.readthedocs.io/en/stable/) | 3.10+ |
| [SQL Alchemy﻿](https://github.com/sqlalchemy/sqlalchemy) | 1.1+ |
| [mysqlclient﻿](https://pypi.org/project/mysqlclient/) | 2.0+ |
| [psycopg2﻿](https://github.com/psycopg/psycopg2) | 2.8.4+ |
| [python-oracledb﻿](https://github.com/oracle/python-oracledb) | 1.0.1+ |
| [redis-py﻿](https://github.com/redis/redis-py) | 3.4+[1](#fn-database-frameworks-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").

| Библиотеки для обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SNS | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SQS | 1.11+[1](#fn-messaging-libraries-1-def) |
| [Azure SDK EventHub﻿](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/eventhub/azure-eventhub) | 5.12+ |
| [Celery﻿](https://github.com/celery/celery) | 5.3+ |
| [Confluent Kafka Python client library﻿](https://github.com/confluentinc/confluent-kafka-python) | 2.0.2+[1](#fn-messaging-libraries-1-def) |
| [Kombu﻿](https://github.com/celery/kombu) | 4.6.7+ |
| [kafka-python client library﻿](https://github.com/dpkp/kafka-python) | 1.4+[1](#fn-messaging-libraries-1-def) |
| [pika﻿](https://github.com/pika/pika) | 1.0.0+ |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Amazon AWS SDK﻿](https://github.com/boto/boto3) | 1.11+[1](#fn-remoting-frameworks-1-def) |
| [Azure SDK﻿](https://github.com/Azure/azure-sdk-for-python) | 1.0+[2](#fn-remoting-frameworks-2-def) |
| [gRPC﻿](https://pypi.org/project/grpcio/) | 1.26+[3](#fn-remoting-frameworks-3-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda"). Расширенная поддержка трассировки для всех вызовов сервисов AWS. Поддерживаются как boto3, так и botocore.

2

на основе декоратора @distributed\_trace

3

Асинхронные вызовы поддерживаются начиная с версии 1.331

| Библиотеки для асинхронного выполнения | Версии |
| --- | --- |
| [Gevent﻿](https://www.gevent.org/) | 20.9.0+ |
| [Python standard library: asyncio﻿](https://docs.python.org/3/library/asyncio.html#module-asyncio) | Поддерживаются все версии |
| [Python standard library: concurrent.futures﻿](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) | Поддерживаются все версии |
| [Python standard library: queue﻿](https://docs.python.org/3/library/queue.html#module-queue) | Поддерживаются все версии |
| [Python standard library: subprocess﻿](https://docs.python.org/3/library/subprocess.html#module-subprocess) | Поддерживаются все версии |
| [Python standard library: threading﻿](https://docs.python.org/3/library/threading.html#module-threading) | Поддерживаются все версии |

| Библиотеки логирования | Версии |
| --- | --- |
| [Python standard library: logging﻿](https://docs.python.org/3/library/logging.html) | Поддерживаются все версии[1](#fn-logging-libraries-1-def) |
| [Structlog﻿](https://github.com/hynek/structlog) | 19.0+[1](#fn-logging-libraries-1-def) |

1

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").

| Фреймворки Generative AI-приложений | Версии |
| --- | --- |
| [Amazon Bedrock Runtime﻿](https://github.com/boto/boto3) | 1.14+ |
| [LangChain﻿](https://github.com/langchain-ai/langchain) | 1.0+ |
| [OpenAI﻿](https://github.com/openai/openai-python) | 1.54.0+ |

* Возможности пользовательской трассировки описаны в разделе [OneAgent SDK for Python](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых пока нет готового модуля кода.").
* Поддержка OpenTelemetry описана в разделе [Instrument your Python application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/python "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.").

### [PHP](/managed/ingest-from/technology-support/application-software/php "Информация о поддержке Dynatrace для PHP-приложений.")

* Linux (mod\_php, FastCGI или PHP-FPM)
* Windows (mod\_php и PHP CGI)

| Версии PHP | Версии | Платформы |
| --- | --- | --- |
| [PHP](/managed/ingest-from/technology-support/application-software/php "Информация о поддержке Dynatrace для PHP-приложений.") | 7.1 (Zend Engine 3.1), 7.2 (Zend Engine 3.2), 7.3 (Zend Engine 3.3), 7.4 (Zend Engine 3.4), 8.0 (Zend Engine 4.0), 8.1 (Zend Engine 4.1)[1](#fn-php-versions-1-def), 8.2 (Zend Engine 4.2)[2](#fn-php-versions-2-def), 8.3 (Zend Engine 4.3)[3](#fn-php-versions-3-def), 8.4 (Zend Engine 4.4)[4](#fn-php-versions-4-def), 8.5 (Zend Engine 4.5)[5](#fn-php-versions-5-def) | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

Поддерживается PHP 8.1 (от RC1 до 8.1.x).

2

Поддерживается PHP 8.2 (от RC1, до официального релиза PHP, вплоть до 8.2.x).

3

Поддерживается PHP 8.3 (от RC1, до официального релиза PHP, вплоть до 8.3.x).

4

Поддерживается PHP 8.4 (от RC2, до официального релиза PHP, вплоть до 8.4.x).

5

Поддерживается PHP 8.5 (от RC3, до официального релиза PHP, вплоть до 8.5.x).

Подробности о поддержке и прекращении поддержки см. в разделе [Dynatrace support model for PHP applications](/managed/ingest-from/technology-support/application-software/php "Информация о поддержке Dynatrace для PHP-приложений.").

| Фреймворки для работы с базами данных | Версии |
| --- | --- |
| [Microsoft Driver for PHP for SQL Server﻿](https://docs.microsoft.com/en-us/sql/connect/php/system-requirements-for-the-php-sql-driver?view=sql-server-2017) | 4.0-5.6[1](#fn-database-frameworks-1-def) |
| [MongoDB PHP for Linux﻿](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [MongoDB PHP for Windows﻿](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [Oracle Database﻿](https://php.net/manual/en/book.oci8.php) | Поддерживаются все версии |
| [PDO﻿](https://php.net/manual/en/book.pdo.php) | Поддерживаются все версии |
| PostgreSQL | Поддерживаются все версии |
| [mysql, mysqli﻿](https://php.net/manual/en/set.mysqlinfo.php) | Поддерживаются все версии |
| [phpredis﻿](https://github.com/phpredis/phpredis) | 4.0.0+[2](#fn-database-frameworks-2-def) |
| [predis﻿](https://github.com/predis/predis) | 1.1.2+ |

1

Поддерживается только для PHP NG Monitoring

2

Поддерживается только для PHP NG Monitoring. Реализация с использованием phpredis cluster поддерживается начиная с версии OneAgent 1.317. Реализация с использованием phpredis array в настоящее время не поддерживается.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| RabbitMQ client (php-amqplib) | 2.7+ |

| Платформы приложений | Версии |
| --- | --- |
| [Adobe Commerce﻿](https://business.adobe.com/products/magento/magento-commerce.html) | Поддерживаются все версии |
| [CodeIgniter﻿](https://codeigniter.com/) | Поддерживаются все версии |
| [Drupal﻿](https://www.drupal.org/) | Поддерживаются все версии |
| [Joomla﻿](https://www.joomla.org/) | Поддерживаются все версии |
| [Laminas﻿](https://getlaminas.org/) | Поддерживаются все версии |
| [Laravel﻿](https://laravel.com/) | Поддерживаются все версии |
| [Magento﻿](https://business.adobe.com/products/magento/magento-commerce.html) | Поддерживаются все версии |
| [Slim﻿](https://www.slimframework.com/) | Поддерживаются все версии |
| [Symfony﻿](https://symfony.com/) | Поддерживаются все версии |
| [WordPress﻿](https://wordpress.com/) | Поддерживаются все версии |

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry﻿](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

| Кэш | Версии |
| --- | --- |
| [Memcached﻿](https://www.php.net/manual/en/book.memcached.php) | 3.0.0+[1](#fn-cache-1-def) |

1

Поддерживается только для PHP NG Monitoring на Linux и Alpine Linux/MUSL

| Фреймворки логирования | Версии |
| --- | --- |
| [Monolog﻿](https://github.com/Seldaek/monolog) | 2.3 - 2.4, 3.0 |

Возможности пользовательской трассировки описаны в разделе [OneAgent SDK for PHP](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "Dynatrace OneAgent SDK позволяет вручную инструментировать приложение, чтобы расширить сквозную видимость для фреймворков и технологий, для которых пока нет готового модуля кода.").

### IBM App Connect Enterprise / IBM Integration Bus

| Версии | Версии | Платформы |
| --- | --- | --- |
| [IBM App Connect Enterprise﻿](https://www.ibm.com/support/knowledgecenter/en/SSTTDS) | 11.0.0.4+, 12.0.3.0+, 13.0.2.0+ | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |
| [IBM Integration Bus﻿](https://www.ibm.com/support/knowledgecenter/de/SSMKHH/mapfiles/product_welcome.html) | 10 | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |

* Поддерживается только 64-битная версия
* Мониторинг поддерживается для всех типов узлов
* Трассировка поддерживается для следующих типов узлов:

  + IBM MQ: MQInput, MQOutput, MQReply
  + JMS: JMSInput, JMSOutput
  + HTTP: HTTPInput, HTTPReply, HTTPRequest, HTTPAsyncRequest, HTTPAsyncResponse
  + REST: RESTRequest, RESTAsyncRequest, RESTAsyncResponse
  + Web services: SOAPInput, SOAPReply, SOAPRequest, SOAPAsyncRequest, SOAPAsyncResponse
  + Callables (OneAgent version 1.257+): CallableFlowAsyncInvoke, CallableFlowAsyncResponse, CallableFlowInvoke, CallableInput, CallableReply
  + Routing: Publication
  + Compute: Java
  + Database: DatabaseRetrieve, DatabaseRoute
  + CICS (OneAgent version 1.277+): CICSRequest

### C / [C++](/managed/ingest-from/technology-support/application-software/cpp "Learn how to instrument your C++ application with OpenTelemetry as a data source for Dynatrace.")

* Для возможностей произвольной трассировки см. [OneAgent SDK for C/C++](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.").
* Для поддержки OpenTelemetry см. [Instrument your C++ application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/cpp "Learn how to instrument your C++ application using OpenTelemetry and Dynatrace.").

### [Erlang/Elixir](/managed/ingest-from/technology-support/application-software/erlang-elixir "Learn how to instrument your Erlang/Elixir application with OpenTelemetry as a data source for Dynatrace.")

Для поддержки OpenTelemetry см. [Instrument your Erlang application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/erlang "Learn how to instrument your Erlang application using OpenTelemetry and Dynatrace.").

### [Ruby](/managed/ingest-from/technology-support/application-software/ruby "Learn how to instrument your Ruby application with OpenTelemetry as a data source for Dynatrace.")

Для поддержки OpenTelemetry см. [Instrument your Ruby application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.").

### [Rust](/managed/ingest-from/technology-support/application-software/rust "Learn how to instrument your Rust application with OpenTelemetry as a data source for Dynatrace monitoring.")

Для поддержки OpenTelemetry см. [Instrument your Rust application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/rust "Learn how to instrument your Rust application using OpenTelemetry and Dynatrace.").

## Веб-серверы

### Apache HTTP

| Серверы | Версии | Платформы |
| --- | --- | --- |
| Apache HTTP Server | 2.0, 2.2 | Alpine Linux 64-bit (x86-64), Linux (PPCLE, x86-64, ARM64 (AArch64)), Solaris (SPARC), Windows (x86-64) |
| Apache HTTP Server | 2.4 | Alpine Linux 64-bit (x86-64), Linux (PPCLE, x86-64, ARM64 (AArch64)), Solaris (SPARC, x86-64), Windows (x86-64) |
| Fujitsu Interstage IHS | 12[1](#fn-servers-1-def), 13[1](#fn-servers-1-def) | Linux (x86-64), Windows (x86-64) |
| IBM HTTP Server | 7, 8 | AIX (POWER8, POWER9, POWER10), Linux (PPCLE, x86-64), Solaris (SPARC), Windows (x86-64) |
| IBM HTTP Server | 8.5 | AIX (POWER8, POWER9, POWER10), Linux (PPCBE), Linux (PPCLE, x86-64), Linux (s390), Solaris (SPARC), Windows (x86-64) |
| IBM HTTP Server | 9 | AIX (POWER8, POWER9, POWER10), Linux (PPCLE, x86-64), Linux (s390), Solaris (SPARC), Windows (x86-64) |
| Oracle HTTP Server | 11g, 12c | Solaris (SPARC) |

1

Поддерживаются только версии Apache 2.2 и 2.4.

| Обогащение логов | Версии |
| --- | --- |
| access.logs | Поддерживаются все версии |
| error.logs | Поддерживаются все версии |

### Microsoft IIS

| Серверы | Версии | Платформы |
| --- | --- | --- |
| Microsoft IIS | 7.5, 8.0, 8.5, 10.0 | Windows (x86-64) |

### Envoy

| Серверы | Версии | Платформы |
| --- | --- | --- |
| [Envoy﻿](https://www.envoyproxy.io/) | 1.30+[1](#fn-servers-1-def) | Linux (x86-64) |

1

Начиная с версии 1.29 Envoy экспортирует данные через [OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."). Подробности см. в [Configure OpenTelemetry tracing with Envoy](/managed/ingest-from/opentelemetry/integrations/envoy "Learn how to configure Envoy to send OpenTelemetry traces to Dynatrace.").

### NGINX

| Серверы | Версии | Платформы |
| --- | --- | --- |
| [Kong Gateway](/managed/ingest-from/technology-support/application-software/nginx/kong-gateway "Learn how to monitor the Kong Gateway with Dynatrace.") | 2.8 - 3.6[3](#fn-servers-3-def), 3.7 - 3.9[4](#fn-servers-4-def), 3.10 - 3.14[4](#fn-servers-4-def) | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx#nginx-versions "Learn the details of Dynatrace support for NGINX.") | 1.11.5 - 1.13.8[1](#fn-servers-1-def), 1.13.9 - 1.14.0[1](#fn-servers-1-def), 1.14.1 - 1.15.8[1](#fn-servers-1-def), 1.15.9 - 1.15.10[1](#fn-servers-1-def), 1.15.11 - 1.16.0[1](#fn-servers-1-def), 1.16.1 - 1.17.3[1](#fn-servers-1-def), 1.17.4 - 1.17.6[1](#fn-servers-1-def), 1.17.7[1](#fn-servers-1-def), 1.17.8[1](#fn-servers-1-def), 1.17.9[1](#fn-servers-1-def), 1.17.10 - 1.18.0, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.19.6, 1.19.7, 1.19.8, 1.19.9, 1.19.10, 1.20.0, 1.20.1, 1.20.2, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.24.0, 1.25.0, 1.25.1, 1.25.2, 1.25.3, 1.25.4, 1.25.5, 1.26.0, 1.26.1, 1.26.2, 1.26.3, 1.27.0, 1.27.1, 1.27.2, 1.27.3, 1.27.4, 1.27.5, 1.28.0, 1.28.1, 1.28.2, 1.28.3, 1.29.0, 1.29.1, 1.29.2, 1.29.3, 1.29.4, 1.29.5, 1.29.6[2](#fn-servers-2-def), 1.29.7[2](#fn-servers-2-def), 1.29.8[2](#fn-servers-2-def), 1.30.0[2](#fn-servers-2-def), 1.30.1[2](#fn-servers-2-def), 1.31.0[2](#fn-servers-2-def) | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64, PPCLE) |
| [NGINX Plus](/managed/ingest-from/technology-support/application-software/nginx#nginx-plus-versions "Learn the details of Dynatrace support for NGINX.") | R11 - R14[2](#fn-servers-2-def), R15[2](#fn-servers-2-def), R16 - R17[2](#fn-servers-2-def), R18[2](#fn-servers-2-def), R19[2](#fn-servers-2-def), R20[2](#fn-servers-2-def), R21[2](#fn-servers-2-def), R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64), PPCLE) |
| [OpenResty](/managed/ingest-from/technology-support/application-software/nginx#openresty-versions "Learn the details of Dynatrace support for NGINX.") | 1.13.6, 1.15.8, 1.17.8, 1.19.3, 1.19.9, 1.21.4.1, 1.21.4.2, 1.21.4.3, 1.25.3.1, 1.25.3.2, 1.27.1.1, 1.27.1.2, 1.29.2.1, 1.29.2.3 | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [Tengine](/managed/ingest-from/technology-support/application-software/nginx#tengineversions "Learn the details of Dynatrace support for NGINX.") | 1.4.2 - 2.2.3, 2.3.0 - 2.3.3, 2.3.4, 2.4.0, 2.4.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |

1

Поддержка архитектуры процессора PPCLE добавлена в версии OneAgent 1.169, а ARM64 (AArch64), в версии OneAgent 1.189.

2

Функция OneAgent **Nginx Modules** не поддерживается для этой версии NGINX.

3

Требуется runtime-инструментирование, см. [NGINX runtime instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.")

4

Требуется runtime-инструментирование, см. [NGINX runtime instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime."). Сниженные накладные расходы на инструментирование при версиях агента >= 1.313.

| Обогащение логов | Версии |
| --- | --- |
| error.logs | Поддерживаются все версии |

## Real User Monitoring

### Web-based Real User Monitoring

#### Браузеры

Поддерживаются все современные браузеры с включёнными JavaScript и cookies, но тестируются только браузеры из списка ниже[1](#fn-7-1-def).

| Браузеры | Версии |
| --- | --- |
| Google Chrome | 3 последние версии (desktop и mobile) |
| Microsoft Edge | Последняя версия |
| Mozilla Firefox | 3 последние версии |
| Opera | 2 последние версии |
| Safari | 3 последние версии (macOS) |

1

Если внедрение RUM JavaScript в официально не поддерживаемые версии нежелательно, [настрой соответствующие правила исключения браузеров](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring#exclude-browsers "Disable Real User Monitoring Classic for certain IP addresses, browsers, bots, and spiders.") в настройках приложения.

##### Браузеры для записи сессий

| Браузеры | Версии |
| --- | --- |
| Google Chrome | 3 последние версии (desktop и mobile) |
| Microsoft Edge | Последняя версия |
| Mozilla Firefox | 3 последние версии |
| Opera | 2 последние версии |
| Safari | 3 последние версии (macOS) |

Технологии вроде Electron и аналогичные обёртки, создающие десктопные приложения из веб-страниц, не поддерживаются.

#### Асинхронные запросы и одностраничные приложения

Dynatrace предлагает общую поддержку для любого приложения через XHR или Fetch() API, а также специальную поддержку для Angular.

| Общая поддержка |
| --- |
| Fetch API |
| XMLHttpRequest (XHR) |

| JavaScript-фреймворки | Версии |
| --- | --- |
| Angular | 2–16, 17+[1](#fn-8-1-def) |

1

При использовании Angular 17+ для приложения требуется альтернативная настройка. См. [Активация поддержки Angular 17+](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-angular-17-support "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

Начиная с RUM JavaScript версии 1.265 и Dynatrace версии 1.266 специальная поддержка некоторых JavaScript-фреймворков прекращена. Подробности см. в [Прекращение специальной поддержки некоторых JavaScript-фреймворков](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#desupported-frameworks-js-265 "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

#### Веб-серверы и приложения

Для следующих веб-серверов и приложений Dynatrace поддерживает [автоматическое внедрение RUM](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), [доставку RUM JavaScript](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring Classic code source for your specific requirements."), [пересылку RUM beacon](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") и [корреляцию действий пользователя с распределённой трассировкой](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.").

| Веб-серверы и приложения |
| --- |
| Apache HTTP Server |
| IBM HTTP Server |
| Веб-приложения на основе Java servlet |
| Kestrel (приложения ASP.NET Core)[1](#fn-9-1-def)[2](#fn-9-2-def) |
| Microsoft IIS |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.") |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") |
| Oracle HTTP Server |

1

Минимально требуемые версии: .Net Core 3.1, .Net Standard 2.1, Microsoft.AspNetCore.Http.Abstractions 1.0.2 (для full framework).

2

Чтобы включить эту функцию как OneAgent feature, перейди в **Settings** > **Preferences** > **OneAgent features** и включи **Enable Real User Monitoring (RUM) for ASP.NET Core**.

Для следующих веб-серверов и приложений Dynatrace поддерживает [корреляцию действий пользователя с распределённой трассировкой](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.") для XHR-запросов.

| Веб-серверы и приложения |
| --- |
| Apache HttpCore |
| MuleSoft HTTP Listener |
| Netty [1](#fn-10-1-def) |
| Software AG WebMethods Integration Server |
| Undertow |

1

Чтобы включить эту функцию как OneAgent feature, перейди в **Settings** > **Preferences** > **OneAgent features** и включи **Netty Real User Monitoring (RUM) to distributed trace correlation**.

### Mobile app Real User Monitoring

#### Операционные системы

| Операционные системы | Версии |
| --- | --- |
| [Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.") | 6.0+ (API 23+) |
| [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") | 15+ |
| [tvOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") | 15+ |

#### Фреймворки

| Фреймворки | Версии |
| --- | --- |
| AFNetworking | 3.3 |
| Alamofire | 5+ |
| [Apache Cordova](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.") | 9+ |
| OkHttp | 3+[1](#fn-11-1-def), 4+[1](#fn-11-1-def), 5+[1](#fn-11-1-def) |
| [Xamarin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget "Monitor Xamarin apps with Dynatrace OneAgent.")[2](#fn-11-2-def) | Xamarin.iOS, Xamarin.Android, Xamarin.Forms (.NET Standard 2.0+) |
| [.NET MAUI](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/maui "Monitor .NET MAUI applications with Dynatrace OneAgent.") | .NET 6.0+ |
| [React Native](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/react-native "Auto-instrument your React Native applications with OneAgent.") | 0.59+ |
| [Flutter](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/flutter "Learn how to auto-instrument your Flutter applications with OneAgent.") | 1.12+ |
| UIKit | Поддерживается |
| [SwiftUI](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.") | 2+ |
| [Jetpack Compose](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") | 1.4–1.10 |

1

Включая библиотеки на основе OkHttp, например Retrofit 2.

2

Dynatrace переведёт Dynatrace Xamarin NuGet package в статус deprecated в мае 2024 года и прекратит его поддержку в мае 2025 года. Подробности см. в [Deprecation and end of support for Dynatrace Xamarin NuGet package](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/xamarin-nuget#deprecation-announcement "Monitor Xamarin apps with Dynatrace OneAgent.").

#### OneAgent for iOS

* **Xcode**: поддерживаются только те версии Xcode, которые Apple разрешает для отправки в App Store. Информацию о том, какие версии Xcode поддерживаются в данный момент, см. на сайте Apple Developer в разделе [Submit your iOS apps to the App Store﻿](https://developer.apple.com/ios/submit/).

Начиная с OneAgent for iOS версии 8.335, Dynatrace прекратил поддержку Xcode 16. Поддерживается только Xcode 26+.

Также стоит учитывать, что [правила отправки приложений в App Store от Apple﻿](https://dt-url.net/we038fb) примерно с апреля 2026 года ограничат поддержку приложениями, собранными минимум с Xcode 26.

Начиная с OneAgent for iOS версии 8.343, Dynatrace прекратил поддержку iOS 12, iOS 13 и iOS 14. Минимально поддерживаемая версия, это iOS 15. Версия 8.341, это последняя версия OneAgent for iOS, поддерживающая iOS 12–14.

#### Dynatrace Android Gradle plugin

* Gradle версии 8.0+
* Android Gradle plugin версии 8.1.1+

Подробности см. в [Dynatrace Android Gradle plugin в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.").

### Dynatrace OpenKit

| Продукт | Версии |
| --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | 7, 8, 11, 12 |
| .NET | Core 3.1, 5, 6 |
| .NET Framework | 3.5, 4.6, 4.7, 4.8, 4.8.1 |
| .NET Standard | 2.0 |
| .NET UWP | Поддерживается |
| .NET PCL | 4.5 |
| C/C++ Windows | Visual Studio 2015, 2017, 2019 и 2022 |
| C/C++ Linux | GCC 5.0.0+ или CLang 3.8.0+ |
| Node.js | 14+ |
| JavaScript | ES6+ |

Подробности можно посмотреть на следующих справочных страницах.

* [Dynatrace OpenKit - Java﻿](https://github.com/Dynatrace/openkit-java/releases)
* [Dynatrace OpenKit - .NET﻿](https://github.com/Dynatrace/openkit-dotnet/releases)
* [Dynatrace OpenKit - C/C++﻿](https://github.com/Dynatrace/openkit-native#prerequisites)
* [Dynatrace OpenKit - JavaScript﻿](https://github.com/Dynatrace/openkit-js)

## Extensions

Полный список технологий, поддерживаемых [Dynatrace Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."), можно посмотреть на странице [Dynatrace Hub﻿](https://www.dynatrace.com/hub/?filter=all&type=extension&internal_source=doc&internal_medium=link&internal_campaign=cross).

## Источники данных для приёма метрик

| Технологии | Версии |
| --- | --- |
| [StatsD](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.") | Поддерживаются все версии[1](#fn-technologies-1-def) |

1

Требует OneAgent EEC. Поддерживается на Windows и Linux, архитектура процессора x64

## Приватные локации Synthetic

См. [Требования для приватных локаций Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

## Уровни поддержки сторонних технологий

### Поддерживается

Мы обеспечиваем поддержку любых проблем, вызванных непосредственно Dynatrace. Dynatrace имеет доступ к этой технологии и обычно может воспроизвести распространённые проблемы своими силами, но окружение, возможно, придётся разворачивать по запросу.

### Ограниченная поддержка

Dynatrace обеспечивает поддержку ограниченного набора функциональности для конкретной технологии. В большинстве случаев Dynatrace не имеет доступа к технологии с ограниченной поддержкой. По любым проблемам поддержка Dynatrace сможет помочь, если получится воспроизвести проблему на полностью поддерживаемой технологии, которая лежит в основе ограниченной поддержки.