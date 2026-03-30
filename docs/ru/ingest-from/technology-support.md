---
title: Поддержка технологий
source: https://www.dynatrace.com/docs/ingest-from/technology-support
scraped: 2026-03-06T21:12:58.632068
---

Dynatrace поддерживает мониторинг технологий и версий, перечисленных на этой странице. Информацию о бессерверном мониторинге см. в разделе Матрица поддержки бессерверных вычислений."). Информацию о мейнфреймах см. в разделе Поддержка технологий мейнфреймов.

См. также Объявления о прекращении поддержки.

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Поддерживается основная версия 5**

  + Поддерживается основная версия 5, включая все её минорные версии, такие как 5.1 и 5.2
  + Другие основные версии не поддерживаются, например 6 и 7
* **Поддерживается минорная версия 5.1**

  + Поддерживается минорная версия 5.1, включая все её патч-версии, такие как 5.1.1 и 5.1.2
  + Другие минорные версии не поддерживаются, например 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Поддерживается патч-версия 5.1.1
  + Другие патч-версии не поддерживаются, например 5.1.2 и 5.1.3
* **Version range 5.1 â 5.3 is supported**

  + Поддерживаются минорные версии 5.1, 5.2 и 5.3, включая все их патч-версии, такие как 5.1.1, 5.2.1 и 5.3.1
  + Другие минорные версии не поддерживаются, например 5.0 и 5.4
* **Минимальная требуемая версия — 5+**

  + Поддерживаются все основные, минорные и патч-версии начиная с версии 5, например 5, 5.1, 5.1.1 и 6

## Операционные системы

Вы можете установить OneAgent на следующие операционные системы: [Linux](#linux), [Unix](#unix), [Windows](#windows) и z/OS.

### Linux

Dynatrace тестирует и обеспечивает поддержку установки OneAgent только для дистрибутивов и версий Linux, перечисленных ниже.

Существуют определённые ограничения при развёртывании OneAgent на хосте Linux с Oracle Database Server 19c и/или смонтированными NFS-дисками. См. [Troubleshoot OneAgent installation](dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation.md#oracle-database-server-19c "Узнайте, как устранить неполадки при установке OneAgent на AIX, Linux и Windows.").

Поддерживаемые архитектуры CPU

* `x86-64` - 64-bit Intel/AMD
* `s390x` - 64-bit IBM Z mainframe
* `ppc64le` - 64-bit PowerPC
* `ARM64 (AArch64)` - 64-bit Linux ARM, including [AWS Graviton processors](https://aws.amazon.com/ec2/graviton/)

| Поддерживаемая ОС | Версии | Архитектуры CPU |
| --- | --- | --- |
| AlmaLinux | 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| Alpine Linux (musl libc) for containers | 3.10 - 3.23[1](#fn-supported-os-1-def) | x86-64 |
| Amazon Linux | 2023 | ARM64 (AArch64), x86-64 |
| Azure Linux | 2, 3 | x86-64 |
| Bottlerocket | 1[2](#fn-supported-os-2-def) | ARM64 (AArch64), x86-64 |
| CentOS Stream | 9 | ARM64 (AArch64), PPCLE, x86-64 |
| Debian | 11, 12, 13 | ARM64 (AArch64), x86-64 |
| Fedora | 41, 42, 43 | x86-64 |
| Oracle Linux | 7, 8, 9, 10 | x86-64 |
| Red Hat Enterprise Linux | 7, 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| Red Hat Enterprise Linux CoreOS | 4.14[3](#fn-supported-os-3-def), 4.15[3](#fn-supported-os-3-def), 4.16[3](#fn-supported-os-3-def) | x86-64 |
| Rocky Linux | 8, 9, 10 | ARM64 (AArch64), x86-64 |
| SUSE Linux Enterprise Server | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | PPCLE, s390, x86-64 |
| SUSE Linux Enterprise Server | 15.3, 15.4, 15.5, 15.6, 15.7 | ARM64 (AArch64) |
| Ubuntu | 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | PPCLE, x86-64 |
| Ubuntu | 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | ARM64 (AArch64), s390 |
| openSUSE | 15.6 | PPCLE, x86-64 |

1

Поддерживается только в контейнерах, мониторинг которых осуществляется в режиме full-stack или application-only OneAgent (musl libc 1.1.14 - 1.2.5). Бинарные файлы, собранные с GNU C Library (glibc) и работающие через библиотеку gcompat, не поддерживаются.

2

Поддерживается только с использованием application-only injection. Метрики узлов доступны через Kubernetes Platform Monitoring.

3

Поддерживается для контейнерного развёртывания через Dynatrace Operator (см. OpenShift).

Совместимость Full-Stack Monitoring с Red Hat OpenShift

* OpenShift 4.19+: поддерживаются только Application observability и Full-stack observability. Это связано с тем, что рабочие узлы могут работать только на Red Hat Enterprise Linux CoreOS. Подробнее см. [Red Hat release notes (1.5.13.2)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).
* OpenShift 4.16â4.18: Classic Full-Stack monitoring поддерживается только на рабочих узлах с Red Hat Enterprise Linux. Если рабочие узлы работают на Red Hat Enterprise Linux CoreOS, поддерживается только облачный Full-stack observability.

### Unix

Dynatrace тестирует и обеспечивает поддержку установки OneAgent для версий AIX и Solaris, перечисленных ниже.

Поддерживаемые архитектуры CPU

* `x86-64` - 64-bit Intel/AMD
* `POWER8` - 64-bit Power ISA
* `POWER9` - 64-bit Power ISA
* `POWER10`- 64-bit Power ISA
* `SPARC`

| Система UNIX | Версии | Архитектуры CPU |
| --- | --- | --- |
| IBM AIX | 7.2 TL5[1](#fn-unix-system-1-def), 7.3 TL1[1](#fn-unix-system-1-def), 7.3 TL2[1](#fn-unix-system-1-def), 7.3 TL3[1](#fn-unix-system-1-def) | POWER10, POWER8, POWER9 |
| Solaris | 11.4 | SPARC, x86-64 |

1

Установка на AIX WPAR не поддерживается.

### Windows

Dynatrace тестирует и обеспечивает поддержку установки OneAgent только для версий Windows, перечисленных ниже.

Поддерживаемые архитектуры CPU

* `x86-64` -64-bit Intel/AMD

| ОС Windows | Версии | Архитектуры CPU |
| --- | --- | --- |
| Windows Desktop 10 | 22H2[1](#fn-windows-os-1-def), 1507[2](#fn-windows-os-2-def), 1607[2](#fn-windows-os-2-def), 1809[2](#fn-windows-os-2-def), 21H2[2](#fn-windows-os-2-def) | x86-64 |
| Windows Desktop 11 | 22H2, 23H2, 24H2, 25H2 | x86-64 |
| Windows Server | 2012 R2[3](#fn-windows-os-3-def), 2016[4](#fn-windows-os-4-def), 2019[4](#fn-windows-os-4-def), 2022[4](#fn-windows-os-4-def), 2025[4](#fn-windows-os-4-def) | x86-64 |
| Windows Server - Nano | All versions supported[5](#fn-windows-os-5-def) | x86-64 |

1

Полугодовой канал Windows 10 (SAC), за исключением Windows 10 IoT.

2

Канал долгосрочного обслуживания Windows 10 (LTSC), за исключением Windows 10 IoT.

3

Windows 2012 R2 не поддерживается в OneAgent версий 1.287 — 1.305. Если у вас установлена одна из этих версий OneAgent, обновитесь до версии 1.307 для включения поддержки.

4

Канал долгосрочного обслуживания (LTSC). Поддержка включает установку Server Core (требуется установка OneAgent в headless-режиме) или мониторинг в режиме app-only.

5

Ограниченная поддержка на основе совместимости с поддержкой Windows Server при использовании в качестве образа контейнера.

## Файловые системы

OneAgent может обнаруживать и создавать сущности дисков (`dt.entity.disk`) в следующих файловых системах:

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

Начиная с OneAgent версии 1.307+.

2

Начиная с OneAgent версии 1.307+. Поддерживается только статистика пространства.

3

Если команда `mmpmonSocket` в Linux завершается ошибкой, доступен резервный режим, который работает при включённой возможности CAP_SETUID. Подробности см. в разделе [Конфигурация OneAgent через командную строку](dynatrace-oneagent/oneagent-configuration-via-command-line-interface.md#capsetuid-osagent "Узнайте, как выполнить некоторые задачи настройки OneAgent без переустановки.").

4

Начиная с OneAgent версии 1.309+.

5

Начиная с OneAgent версии 1.303+. Поддерживается только статистика пространства.

6

Начиная с OneAgent версии 1.323+. Поддерживается только статистика пространства.

7

Начиная с OneAgent версии 1.331+. Поддерживается только статистика пространства. Опциональная функция, необходимо включить в настройках диска.

## Контейнеры

| Функции | Версии |
| --- | --- |
| Auto-injection in [Docker](https://www.docker.com/) container (Deep monitoring)[1](#fn-2-1-def) | 1.6+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [containerd](https://containerd.io/) container (Deep monitoring) | 1.1.2+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [CRI-O](https://cri-o.io/) container (Deep monitoring) | 1.12.5+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [Garden-RunC](https://docs.cloudfoundry.org/concepts/architecture/garden.html#garden-runc) container (Deep monitoring) | 1.0.0+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [BOSH bpm](https://bosh.io/docs/bpm/bpm/) container (Deep monitoring) | 0.11.0+ |
| Auto-injection in [Podman](https://podman.io/) container (Deep monitoring)[2](#fn-2-2-def)[3](#fn-2-3-def) | 3.4.4â5.x.x |
| Docker container metrics[1](#fn-2-1-def) | 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 RC2, 1.13.1, 17.03+ CE and EE |

1

См. известные ограничения мониторинга контейнеров Docker.

2

Поддерживается для OneAgent 1.267+, установленного на узле Podman с использованием [crun](https://github.com/containers/crun) среды выполнения контейнеров, версии 0.17 - 1.15. Podman с использованием среды выполнения `runc` не поддерживается. Подробности см. в OneAgent release notes version 1.267.

3

Контейнеры Podman, запущенные с `read-only=true` или `userns=keep-id`, не поддерживаются.

## Гипервизоры

|  |
| --- |
| AIX (LPAR) |
| Hyper-V |
| KVM |
| Nutanix AHV[1](#fn-3-1-def) |
| QEMU |
| Xen |
| VMware |
| AWS Nitro[1](#fn-3-1-def) |
| OpenShift Virtualization |

1

Dynatrace обнаруживает гипервизор, но специальная логика не применяется.

## Сетевые интерфейсы

|  |
| --- |
| IEEE 802.3 Ethernet |
| IEEE 802.11 Wireless LAN |
| OpenVZ virtual network device (venet) |

* Поддерживаются как физические, так и виртуальные интерфейсы при условии, что им не назначен локальный адрес канала (link-local address).

  + Для IPv4: локальные адреса канала находятся в диапазоне от `169.254.1.0` до `169.254.254.255`.
  + Для IPv6: локальные адреса канала находятся в диапазоне от `0xFE800000` до `0xFEBFFFFF`.
* Виртуальные интерфейсы Ethernet-мостов не поддерживаются.
* Агрегирование сетевых интерфейсов (bonding) поддерживается.
* Для мониторинга трафика поддерживается только протокол TCP.

## Облачные платформы

### AWS

| Amazon Web Services (AWS) |
| --- |
| DynamoDB |
| Elastic Block Store (EBS) |
| Elastic Compute Cloud (EC2) |
| Elastic Load Balancing (ELB) |
| Lambda |
| Relational Database Service (RDS) |
| Simple Storage Service (S3) |

### Microsoft Azure

| Вычислительный сервис | Расширение для развёртывания OneAgent | Интеграция Dynatrace с Azure Monitor |
| --- | --- | --- |
| Virtual Machines | VM-Extension[1](#fn-4-1-def) | yes |
| Virtual Machine Scale Set | VM-Extension[1](#fn-4-1-def) | yes |
| Service Fabric | VM-Extension[1](#fn-4-1-def) | yes |
| Azure Kubernetes Service (AKS) | Operator-rollout[2](#fn-4-2-def) | no |
| Cloud-Services (Classic) | [Startup script](https://github.com/dtPaTh/Dynatrace-Azure-CloudServices) | no |
| [HDInsight](https://github.com/safia-habib/Azure/blob/master/HDInsights/Readme.md) | Startup-Script | yes |
| App Service (Windows based) | SiteExtension | yes |
| Azure Functions | SiteExtension (Early Adopter release) | yes |

1

VM-Extension автоматизирует установку OneAgent с использованием средств автоматизации Azure. OneAgent также можно установить вручную или с помощью выбранного вами инструмента автоматизации.

2

Поды и узлы Windows не поддерживаются.

| Platform service | OneAgent code-module support | Integration of Dynatrace with Azure Monitor |
| --- | --- | --- |
| Blob-Storage | HttpClient[1](#fn-5-1-def) | yes |
| Table-Storage | HttpClient[1](#fn-5-1-def) | yes |
| Queue-Storage | HttpClient[1](#fn-5-1-def) | yes |
| File-Storage | Infrastructure monitoring | yes |
| Disk-Storage | Infrastructure monitoring | yes |
| ServiceBus Queues and Topics | Microsoft Azure Service Bus Client for .NET | yes |
| Load-Balancer | Infrastructure monitoring | yes[3](#fn-5-3-def) |
| Application Gateway | Trace-Context[4](#fn-5-4-def) | yes |
| API Management | Trace-Context[4](#fn-5-4-def), SDK[5](#fn-5-5-def) | yes |
| Azure SQL | Supported database frameworks[2](#fn-5-2-def) | yes |
| Azure SQL elastic pool | Supported database frameworks[2](#fn-5-2-def) | yes |
| Azure SQL Managed Instance | Supported database frameworks[2](#fn-5-2-def) | no |
| SQL Data Warehouse | Supported database frameworks[2](#fn-5-2-def) | no |
| SQL Server Stretch | Supported database frameworks[2](#fn-5-2-def) | no |
| Azure DB for MySql | Supported database frameworks[2](#fn-5-2-def) | no |
| Azure DB for PostgreSQL | Supported database frameworks[2](#fn-5-2-def) | no |
| CosmosDB | MongoDB API, Cassandra API, HttpClient[1](#fn-5-1-def) | yes |
| Redis Cache | Supported client libraries | yes |
| Event Hubs | SDK[5](#fn-5-5-def) | yes |
| IoT Hub | Trace Context[4](#fn-5-4-def), SDK[5](#fn-5-5-def) | yes |

1

Трассировка HTTP-вызовов через поддержку HttpClient

2

Трассировка вызовов баз данных через поддерживаемые фреймворки баз данных (например, ADO.NET или JDBC).

3

Доступно только для [Standard Load Balancer](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-standard-overview#why-use-standard-load-balancer)

4

Сквозная трассировка через [Trace Context](https://www.w3.org/TR/trace-context/)

5

Сквозная трассировка с использованием [OneAgent SDK](https://github.com/Dynatrace/OneAgent-SDK)

### Google Cloud

| Google Cloud services |
| --- |
| Google Kubernetes Engine |
| [GKE Autopilot](setup-on-k8s/deployment/application-observability.md#automatic "Развёртывание Dynatrace Operator в режиме мониторинга приложений в Kubernetes") (only for automatic `applicationMonitoring`) |
| Google App Engine |
| Google Compute Engine |

### VMware

| VMware | Versions |
| --- | --- |
| ESXi host | 6.5, 6.7, 7, 8.0 |
| vCenter server | 6.5, 6.7, 7, 8.0 |

### Kubernetes

Dynatrace поддерживает различные варианты Kubernetes в соответствии с нашей моделью поддержки Kubernetes и OpenShift.

| Дистрибутивы |
| --- |
| Google Anthos |
| Mirantis Kubernetes Engine [1](#fn-6-1-def) |
| Rancher Kubernetes Engine 2.0 |
| Red Hat OpenShift Container Platform |
| VMware Tanzu Kubernetes Grid Integrated Edition (formerly Pivotal Kubernetes Service) |
| Nutanix Kubernetes Platform (NKP, former D2iQ Konvoy) [1](#fn-6-1-def) |
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

Ограниченная поддержка на основе совместимости с upstream-версией Kubernetes.

Некоторые дистрибутивы и размещённые версии требуют дополнительной настройки. Подробности см. в разделе Technology support.

## Другие контейнерные и PaaS-платформы

### Cloud Foundry

| Buildpacks | Версии |
| --- | --- |
| Java buildpack | 3.11+ |
| PHP buildpack | v4.3.34+ |
| Staticfile buildpack | v1.4.6+ |
| Go buildpack | v1.8.41+ |
| .NET Core on Linux buildpack | v3.1+ |
| Node.js buildpack | v1.6.10+ (requires OneAgent version 1.131 or higher) |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ See known issue |

#### IBM Cloud Foundry

| Функции | Версии |
| --- | --- |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ See known issue |

#### Cloud Foundry

| Функции | Версии |
| --- | --- |
| Garden-runC | v1.0.0+ |
| BOSH BPM for platform process isolation | v0.11.0+ |
| Winc for Windows Server containers | Windows server 1709+ |
| VMware Tanzu Application Service (via BOSH add-on) | See support model for Tanzu Application Service |

### Heroku

| Функции | Версии |
| --- | --- |
| Stack | Heroku-18 |
| Stack | Heroku-20 (default) |

## Безопасность приложений

Подробности см. в разделе [Supported technologies](../secure/application-security.md#tech "Access the Dynatrace Application Security functionalities.").

## Приложения, сервисы и базы данных

### Java

Подробности см. в разделе Dynatrace support/desupport for Java versions.

| Виртуальные машины | Версии | Платформы |
| --- | --- | --- |
| Amazon Corretto | 8 LTS, 11 LTS, 17 LTS, 21 LTS, 22, 23, 24, 25 LTS | Linux (x86-64, ARM64 (AArch64)) |
| Azul Platform Core (Zulu) | 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 22, 23, 24, 25 LTS | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| Azul Platform Prime (Zing) | 6[8](#fn-virtual-machines-8-def), 7[8](#fn-virtual-machines-8-def), 8 LTS[8](#fn-virtual-machines-8-def), 11 LTS[8](#fn-virtual-machines-8-def) | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |
| Bellsoft Liberica | 8 LTS, 11 LTS, 17 LTS, 21 LTS[9](#fn-virtual-machines-9-def), 22, 23, 24, 25 LTS | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64), PPCLE), Solaris (SPARC, x86-64), Windows (x86-64) |
| Eclipse Temurin (a.k.a. 'Adoptium') | 8 LTS, 11 LTS, 17 LTS, 21 LTS, 22, 23, 24, 25 LTS | AIX (POWER8, POWER9, POWER10), Linux (x86-64, ARM64 (AArch64), PPCLE, s390), Windows (x86-64) |
| Fujitsu | 5, 6, 8 | Linux (x86-64), Windows (x86-64) |
| GraalVM | 19[5](#fn-virtual-machines-5-def), 20[5](#fn-virtual-machines-5-def), 21[6](#fn-virtual-machines-6-def), 22[7](#fn-virtual-machines-7-def) | Linux (x86-64), Windows (x86-64) |
| GraalVM for JDK | 17 LTS, 20, 21 LTS | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| Hitachi | 5 | Windows (x86-64) |
| Huawei | 8 | Linux (ARM64 (AArch64)) |
| IBM JVM | 6, 7, 8 LTS | AIX (POWER8, POWER9, POWER10), Alpine Linux 64-bit (x86-64), Linux (PPCLE, PPCBE, s390, x86-64), Windows (x86-64) |
| IBM Semeru | 8 LTS, 11 LTS, 17 LTS, 21 LTS | AIX (POWER8, POWER9, POWER10), Linux (x86-64, ARM64 (AArch64), PPCLE, s390), Windows (x86-64) |
| Microsoft OpenJDK | 11 LTS, 17 LTS, 21 LTS | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |
| OpenJ9 | 0.8[1](#fn-virtual-machines-1-def), 0.9[2](#fn-virtual-machines-2-def), 0.10[3](#fn-virtual-machines-3-def), 0.11[4](#fn-virtual-machines-4-def) | Linux (x86-64) |
| OpenJDK | 6, 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 22, 23, 24, 25 LTS | Alpine Linux 64-bit (x86-64), Linux (x86-64, s390), Windows (x86-64) |
| Oracle HotSpot VM | 6, 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 22, 23, 24, 25 LTS | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Solaris (SPARC, x86-64), Windows (x86-64) |
| Oracle JRockit | 6 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Solaris (SPARC), Windows (x86-64) |
| SapMachine | 7, 8 LTS, 11 LTS, 17 LTS, 21 LTS, 23, 24, 25 LTS | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |

1

JDK8

2

JDK8, JDK10

3

JDK 11

4

JDK8, JDK11

5

Работает на Oracle JVM 8 или 11. Информацию о Native Images см. в разделе [Java Native Images](technology-support.md#java-native-image "Найдите технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")

6

Работает на Oracle JVM 8, 11 или 17. Информацию о Native Images см. в разделе [Java Native Images](technology-support.md#java-native-image "Найдите технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

7

Работает на Oracle JVM 11, 17 или 19. Информацию о Native Images см. в разделе [Java Native Images](technology-support.md#java-native-image "Найдите технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")

8

[Ограниченная поддержка](#limited-support): Dynatrace может обеспечить поддержку только для проблем, воспроизводимых на других JVM.

9

32-разрядные версии Bellsoft Liberica v21+ не поддерживаются

| Серверы приложений | Версии |
| --- | --- |
| [Apache TomEE](https://tomee.apache.org/) | 1, 7, 8 |
| [Apache Tomcat](https://tomcat.apache.org/) | 6, 7, 8, 8.5, 9, 10[1](#fn-application-servers-1-def), 11[1](#fn-application-servers-1-def) |
| [Fujitsu Interstage](https://www.fujitsu.com/global/products/software/middleware/application-infrastructure/interstage/) | 12.0[2](#fn-application-servers-2-def) |
| [IBM WebSphere Application Server](https://www.ibm.com/products/software) | 8.5.5, 9.0, 8.5[3](#fn-application-servers-3-def) |
| [IBM WebSphere Liberty](https://developer.ibm.com/wasdev/websphere-liberty/) | 8.5 - 26[4](#fn-application-servers-4-def) |
| [JBoss Enterprise Application Platform](https://developers.redhat.com/products/eap/overview) | 7, 8 |
| [Oracle WebLogic](https://www.oracle.com/middleware/technologies/weblogic.html) | 11g[5](#fn-application-servers-5-def), 12c, 14c |
| [Payara](https://www.payara.fish/) | 5, 6, 7 |
| [WildFly](https://wildfly.org/) | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 - 26, 27 - 39 |

1

Для этой версии требуется активная функция поддержки Java Servlet 5.0

2

[Ограниченная поддержка](#limited-support): полностью поддерживаемая базовая технология: Java

3

Начиная с OneAgent 1.183 в WebSphere Application Server 8.5 поддерживается только Java 7

4

Движок servlet 5 Websphere Liberty поддерживается начиная с OneAgent версии 1.259

5

10.3 = 11g

| ESB и SOA | Версии |
| --- | --- |
| [Apache Camel](https://www.dynatrace.com/hub/detail/apache-camel/) | 2.21+, 3+, 4+[1](#fn-esbs-and-soa-1-def) |
| Apache OpenEJB | 3.1 |
| Mule (HTTP Listener) | 3.5, 3.6, 3.7, 3.8, 3.9, 4.1 - 4.9 |
| [Red Hat Fuse Standalone](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| [Red Hat Fuse on OpenShift](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| TIBCO ActiveMatrix BusinessWorks | 5.8.2 - 5.14[2](#fn-esbs-and-soa-2-def), 6.4[2](#fn-esbs-and-soa-2-def), 6.5[2](#fn-esbs-and-soa-2-def), 6.6 - 6.8[2](#fn-esbs-and-soa-2-def) |

1

Поддерживаются только коннекторы Apache Camel: Undertow, Kafka и MongoDB.

2

Поддерживаются только рабочие процессы TIBCO, запускаемые входящим запросом веб-сервиса, HTTP-запросом или JMS-сообщением.

| Веб-фреймворк | Версии |
| --- | --- |
| [Akka HTTP client](https://doc.akka.io/docs/akka-http/current/client-side/index.html) | 10.1[2](#fn-web-framework-2-def), 10.0[2](#fn-web-framework-2-def), 10.2[2](#fn-web-framework-2-def), 10.4[2](#fn-web-framework-2-def), 10.5[2](#fn-web-framework-2-def), 10.6[2](#fn-web-framework-2-def), 10.7[2](#fn-web-framework-2-def) |
| [Akka HTTP server](https://doc.akka.io/docs/akka-http/current/index.html) | 10.1, 10.2[1](#fn-web-framework-1-def), 10.4[1](#fn-web-framework-1-def), 10.5[1](#fn-web-framework-1-def), 10.6[1](#fn-web-framework-1-def), 10.7[1](#fn-web-framework-1-def) |
| [Apache HttpAsyncClient](https://hc.apache.org/httpcomponents-asyncclient-ga/) | 4.0[4](#fn-web-framework-4-def), 4.1[4](#fn-web-framework-4-def) |
| [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) | 3.1[4](#fn-web-framework-4-def), 4[4](#fn-web-framework-4-def), 5.0[4](#fn-web-framework-4-def), 5.1[4](#fn-web-framework-4-def), 5.2[4](#fn-web-framework-4-def) |
| [Apache HttpCore](https://hc.apache.org/httpcomponents-core-ga/) | 4[3](#fn-web-framework-3-def), 5[4](#fn-web-framework-4-def) |
| [Apache Pekko HTTP client](https://pekko.apache.org/docs/pekko-http/current/client-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| [Apache Pekko HTTP server](https://pekko.apache.org/docs/pekko-http/current/server-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| Elasticsearch | 1.7[5](#fn-web-framework-5-def), 2.0[5](#fn-web-framework-5-def), 2.1[5](#fn-web-framework-5-def), 2.2[5](#fn-web-framework-5-def) |
| Grails | 3[6](#fn-web-framework-6-def) |
| Jakarta Servlet | 2.5, 3.0, 3.1, 4, 5, 6 |
| Java HttpUrlConnection | All versions supported[6](#fn-web-framework-6-def) |
| [Java IMS Soap Gateway client](https://www.ibm.com/support/knowledgecenter/en/SS9NWR_3.2.0/com.ibm.ims.iconapij32.doc/icon_home_java.htm) | 3.2 |
| Jetty HTTP client | 7[6](#fn-web-framework-6-def), 8[6](#fn-web-framework-6-def), 9[6](#fn-web-framework-6-def), 10[6](#fn-web-framework-6-def), 11[6](#fn-web-framework-6-def), 12[6](#fn-web-framework-6-def) |
| [Jetty HTTP server](https://www.eclipse.org/jetty/) | 7, 8, 9, 10, 11, 12 |
| LinkerdD | 1 |
| [Netty](https://netty.io/) | 3.10[7](#fn-web-framework-7-def), 4[7](#fn-web-framework-7-def) |
| [Ning Asynchronous HTTP Client](https://github.com/AsyncHttpClient/async-http-client) | 1.8, 1.9, 2, 3 |
| OkHttp | 3[7](#fn-web-framework-7-def), 4.0 - 4.3[7](#fn-web-framework-7-def), 4.4 - 4.12[7](#fn-web-framework-7-def), 5.+[7](#fn-web-framework-7-def) |
| [Play Framework](https://www.playframework.com/) | 2.2 - 2.6, 2.7, 2.8 |
| [Reactor Netty HTTP Client](https://github.com/reactor/reactor-netty) | 0.8[7](#fn-web-framework-7-def), 0.9[7](#fn-web-framework-7-def), 1.0[7](#fn-web-framework-7-def), 1.1[7](#fn-web-framework-7-def), 1.2[7](#fn-web-framework-7-def), 1.3[7](#fn-web-framework-7-def) |
| [Reactor Netty HTTP Server](https://github.com/reactor/reactor-netty) | 0.6, 0.7, 0.8, 0.9, 1.0 |
| [RxJava](https://github.com/ReactiveX/RxJava) | 3+ |
| Software AG WebMethods Integration Server | 9.0[8](#fn-web-framework-8-def), 9.5 - 9.12[8](#fn-web-framework-8-def), 10.0 - 10.15[8](#fn-web-framework-8-def), 10.7[8](#fn-web-framework-8-def), 10.11[8](#fn-web-framework-8-def), 10.15[8](#fn-web-framework-8-def) |
| [Spring WebFlux](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html) | 5, 6, 7 |
| [Spring WebFlux WebClient](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 5, 6, 7 |
| [Undertow](https://undertow.io/) | 1[9](#fn-web-framework-9-def), 2.0 - 2.2[9](#fn-web-framework-9-def), 2.3+ |
| [Vert.x HttpClient](https://github.com/eclipse-vertx/vert.x) | 3.6+[10](#fn-web-framework-10-def), 4.x[10](#fn-web-framework-10-def), 5.x[10](#fn-web-framework-10-def) |
| [Vert.x WebClient](https://github.com/vert-x3/vertx-web) | 3.6+[10](#fn-web-framework-10-def), 4.x[10](#fn-web-framework-10-def), 5.x[10](#fn-web-framework-10-def) |

1

Поддерживаются привязки Java и Scala.

2

Поддерживается в AWS Lambda.

3

Поддерживается только синхронная обработка запросов. Поддерживается в AWS Lambda.

4

Поддерживается только обработка запросов HTTP/1.1. Поддерживается в AWS Lambda.

5

В настоящее время поддерживается только веб-протокол, проприетарный TCP-протокол не поддерживается.

6

только в контейнере сервлетов

7

Интерфейс Promise и связанные API не поддерживаются.

8

Мониторинг Dynatrace ограничен входящими веб-запросами или JMS-сообщениями, запускающими рабочий процесс (бизнес-логику) на WebMethods.

9

В настоящее время Dynatrace может перехватывать входящие HTTP-запросы только при настройке Undertow на использование Servlet API.

10

Поддерживаются привязки Java и Scala 2.

| Многопоточность | Версии |
| --- | --- |
| CompletableFuture | All versions supported[1](#fn-threading-1-def) |
| [Java ForkJoin](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html) | All versions supported[1](#fn-threading-1-def) |
| Kotlin Coroutines | 1.10.2 - 2.1 |
| Spring Integration | 2[1](#fn-threading-1-def), 3[1](#fn-threading-1-def), 4[1](#fn-threading-1-def), 5[1](#fn-threading-1-def), 6[1](#fn-threading-1-def), 7[1](#fn-threading-1-def) |
| [reactor-core](https://github.com/reactor/reactor-core) | 3[1](#fn-threading-1-def) |

1

Поддерживается в AWS Lambda.

| Веб-сервисы | Версии |
| --- | --- |
| Apache Axis2 | 1.6, 1.7, 1.8 |
| Apache CXF | 2, 3, 4 |
| Hessian Web Services | 2.1, 3.1, 4.0 |
| JAX-WS | 2 |
| [JBoss RESTEasy](https://resteasy.dev/) | 3, 4, 5, 6, 7 |
| JBossWS (Wildfly) | 4[1](#fn-web-services-1-def), 5[2](#fn-web-services-2-def) |
| Jakarta RESTful Web Services | 2.1+ |
| Jersey | 1, 2, 3 |
| Play WS API | 2.2 - 2.4 |
| REST web services via WINK framework | 1.2, 1.4 |
| Spring Web Services | 2, 3, 4 |

1

Wildfly 8

2

Wildfly 8,9,10

| Фреймворки баз данных | Версии |
| --- | --- |
| Amazon DynamoDB | 1[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def) |
| Apache Thrift | 2 |
| DataStax client for Apache Cassandra | 2.1[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| JDBC | 4+[1](#fn-database-frameworks-1-def) |
| [Jedis Redis](https://github.com/xetorthio/jedis) | 2, 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def), 5[1](#fn-database-frameworks-1-def), 6[1](#fn-database-frameworks-1-def), 7[1](#fn-database-frameworks-1-def) |
| [Lettuce](https://lettuce.io/) | 5.1 - 5.3[1](#fn-database-frameworks-1-def), 6.0.3 - 6.1.6[1](#fn-database-frameworks-1-def), 6.1.8 - 6.8[1](#fn-database-frameworks-1-def), 7.0 - 7.4[1](#fn-database-frameworks-1-def) |
| [MongoDB Reactive Streams driver](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/) | 4.10+[1](#fn-database-frameworks-1-def), 5.0+[1](#fn-database-frameworks-1-def) |
| [MongoDB asynchronous driver](https://mongodb.github.io/mongo-java-driver/3.0/driver-async/) | 3.0 - 3.6.4[1](#fn-database-frameworks-1-def) |
| [MongoDB synchronous driver ](https://docs.mongodb.com/ecosystem/drivers/java/) | 2[1](#fn-database-frameworks-1-def), 3.0 - 3.6[1](#fn-database-frameworks-1-def), 3.7 - 3.11[1](#fn-database-frameworks-1-def), 3.12 - 4.11[1](#fn-database-frameworks-1-def), 5.0[1](#fn-database-frameworks-1-def) |
| [Redisson](https://redisson.pro/) | 3+ |
| Spring Boot Starter Data MongoDB | 2, 3, 4 |
| Spring Boot Starter Data Redis | 2.1+ |

1

Поддерживается в AWS Lambda.

| Клиенты обмена сообщениями | Версии |
| --- | --- |
| [ActiveMQ](https://activemq.apache.org) | 4[1](#fn-messaging-clients-1-def), 5[1](#fn-messaging-clients-1-def) |
| [ActiveMQ Artemis](https://activemq.apache.org/components/artemis/) | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon EventBridge | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| HornetQ | 2.2[1](#fn-messaging-clients-1-def), 2.3[1](#fn-messaging-clients-1-def), 2.4[1](#fn-messaging-clients-1-def) |
| [IBM MQ client](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q118320_.htm) | 8[1](#fn-messaging-clients-1-def), 9[1](#fn-messaging-clients-1-def) |
| JMS | 1.1[1](#fn-messaging-clients-1-def), 2.0[1](#fn-messaging-clients-1-def), 3.0[1](#fn-messaging-clients-1-def) |
| [Kafka](https://kafka.apache.org/documentation/) | 1.0 - 1.1[1](#fn-messaging-clients-1-def), 2.0 - 2.3[1](#fn-messaging-clients-1-def), 2.4 - 2.7[1](#fn-messaging-clients-1-def), 2.8[1](#fn-messaging-clients-1-def), 3.0 - 3.6[1](#fn-messaging-clients-1-def), 3.7 - 3.9[1](#fn-messaging-clients-1-def), 4.0[1](#fn-messaging-clients-1-def) |
| [RabbitMQ](https://www.rabbitmq.com/java-client.html) | 3[1](#fn-messaging-clients-1-def), 4.0.0 - 5.22.0[1](#fn-messaging-clients-1-def) |
| Software AG WebMethod Broker and Universal messaging via JMS | All versions supported |
| [Spring AMQP](https://spring.io/projects/spring-amqp) | 1.5, 2.0, 2.1, 2.2, 2.3 |
| Spring Cloud Stream Kafka Binder | 3+ |
| Tibco EMS | All versions supported[2](#fn-messaging-clients-2-def) |

1

Поддерживаются публикаторы в AWS Lambda.

2

Трассировка поддерживается только через JMS.

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Akka Remoting](https://doc.akka.io/docs/akka/2.5/remoting.html) | 2.4[2](#fn-remoting-frameworks-2-def), 2.5[2](#fn-remoting-frameworks-2-def), 2.3[3](#fn-remoting-frameworks-3-def), 2.6[3](#fn-remoting-frameworks-3-def), 2.7[3](#fn-remoting-frameworks-3-def) |
| [Amazon AWS Lambda SDK](https://aws.amazon.com/en/sdk-for-java/) | 1[1](#fn-remoting-frameworks-1-def), 2[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 1[2](#fn-remoting-frameworks-2-def), 2[2](#fn-remoting-frameworks-2-def) |
| [Apache Pekko Remoting](https://pekko.apache.org/docs/pekko/current/remoting.html#classic-remoting-deprecated-) | 1.0.0 - 1.2.0[5](#fn-remoting-frameworks-5-def) |
| [Apache Thrift](https://thrift.apache.org/) | 0.7 - 0.13 |
| Glassfish RMI-IIOP | All versions supported |
| IBM JVM RMI-IIOP | All versions supported |
| JBoss Enterprise Application Platform - RMI-IIOP | 7, 8 |
| JBoss Enterprise Application Platform - Remoting | 7, 8 |
| [Java CICS Transaction Gateway client](https://www.ibm.com/support/knowledgecenter/en/SSZHFX_9.1.0/basejavadoc/index.html) | 9.0 - 9.2 |
| Java IMS TM Resource Adapter | All versions supported |
| Java RMI-JRMP | All versions supported |
| OpenJDK/Oracle JVM RMI-IIOP | All versions supported |
| WebLogic RMI-IIOP | All versions supported |
| WebSphere Liberty RMI-IIOP | All versions supported |
| WebSphere RMI-IIOP | All versions supported |
| [gRPC](https://grpc.github.io/grpc-java/javadoc/index.html) | 1.18 - 1.79[4](#fn-remoting-frameworks-4-def) |

1

Поддерживается в AWS Lambda.

2

Поддерживается в AWS Lambda. Расширенная поддержка трассировки для всех вызовов сервисов AWS

3

Поддерживается только при использовании Netty; не поддерживается при использовании Artery. Supported in AWS Lambda.

4

Клиентские вызовы gRPC поддерживаются в AWS Lambda.

5

Поддерживается только при использовании classic-remoting; не поддерживается при использовании Artery. Supported in AWS Lambda.

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-frameworks-1-def), 1.4 - 1.54[1](#fn-monitoring-frameworks-1-def) |
| [OpenTracing](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Поддерживается в AWS Lambda.

| Фреймворки логирования | Версии |
| --- | --- |
| Apache Tomcat access logs | 8, 9, 10, 11 |
| [JBoss LogManager](https://github.com/jboss-logging/jboss-logmanager) | 1.1+, 2, 3 |
| [Log4J2 (Apache)](https://logging.apache.org/log4j/2.x/) | 2.7 - 2.12, 2.13.0, 2.13.1, 2.13.3, 2.14 - 2.17.1, 2.17.2 - 2.25 |
| [Logback (QOS)](https://logback.qos.ch/) | 1.x |
| java.util.logging | All versions supported |

См. также OneAgent SDK for Java для расширенных возможностей трассировки.

### Java Native Image

| Виртуальная машина | Версии | Платформы |
| --- | --- | --- |
| GraalVM Native Image | GraalVM for JDK 17 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 21 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 22[1](#fn-virtual-machine-1-def), GraalVM for JDK 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 24[1](#fn-virtual-machine-1-def) | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

Бинарные файлы, работающие на системах Linux на базе Alpine, не поддерживаются

| Фреймворк приложений | Версии |
| --- | --- |
| [Micronaut](https://micronaut.io) | 3.9+[1](#fn-application-framework-1-def) |
| [Quarkus](https://quarkus.io) | 3.8+[1](#fn-application-framework-1-def) |
| [Spring Boot](https://spring.io/projects/spring-boot) | 3.0+[1](#fn-application-framework-1-def), 4.0+[1](#fn-application-framework-1-def) |

1

Поддерживается в контексте сборки нативных образов. Это не означает, что все технологии, предоставляемые фреймворком, поддерживаются.

| Веб-фреймворк | Версии |
| --- | --- |
| [Apache HttpClient](https://hc.apache.org/httpcomponents-client-ga/) | 5.2+ |
| [Netty](https://netty.io/) | 4[1](#fn-web-framework-1-def) |
| [Spring WebFlux WebClient](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 6 |

1

Интерфейс Promise и связанные API не поддерживаются.

| Серверы приложений | Версии |
| --- | --- |
| [Apache Tomcat](https://tomcat.apache.org/) | 10, 11 |

| Фреймворки баз данных | Версии |
| --- | --- |
| Spring Boot Starter Data MongoDB | 3 |

### .NET

Dynatrace поддерживает приложения .NET, написанные на C#. Доступна ограниченная поддержка приложений .NET, написанных на других языках, хотя они не тестировались явно.

| Среда выполнения | Версии | Платформы |
| --- | --- | --- |
| .NET and .NET Core | Core 2.1, Core 2.2, Core 3.0, Core 3.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |
| .NET and .NET Core | 5, 6, 7, 8, 9, 10 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Веб-фреймворк | Версии |
| --- | --- |
| ASP.NET Core | All versions supported |
| ASP.NET Owin/Katana | 3.0.0+ |
| [HttpClient](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | All versions supported |
| [HttpListener](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | All versions supported |
| [HttpWebRequest](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | All versions supported |

| Веб-сервис | Версии |
| --- | --- |
| [Azure Functions](https://azure.microsoft.com/en-us/services/functions/) | 2 |

| Фреймворк удалённого взаимодействия | Версии |
| --- | --- |
| Amazon AWS Lambda SDK | 3.5.0+ |
| Amazon AWS SDK | 3.5.0+ |
| [gRPC](https://www.nuget.org/packages/Grpc.AspNetCore) | 2.23.2+ |

| Фреймворк баз данных | Версии |
| --- | --- |
| ADO.NET | SQL Server, SQL CE, Oracle using Oracle.DataAccess.dll |
| Amazon DynamoDB | 3.5.0+ |
| Azure Cosmos DB | 3.18+ |
| [MongoDB .NET driver](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7, 2.8+ |

| Клиент обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 3.5.0+ |
| Amazon SNS | 3.5.0+ |
| Amazon SQS | 3.5.0+ |
| [Azure Messaging Service Bus](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+ |
| [Confluent Kafka client library](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+ |
| [IBM MQ client](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1 |
| [MassTransit](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1, 8.3.2+ |
| [Microsoft Azure Service Bus client for .NET](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 5.2.0 |
| [RabbitMQ client](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x, 7.x+ |

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

| Фреймворк логирования | Версии |
| --- | --- |
| [Microsoft Logging Extensions](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+ |
| [Serilog](https://serilog.net/) | 2.9+ |
| [log4net](https://logging.apache.org/log4net/) | 2.0.6+ |

См. также OneAgent SDK for .NET для расширенных возможностей трассировки.

### .NET Framework

Dynatrace поддерживает приложения .NET, написанные на C#. Доступна ограниченная поддержка приложений .NET, написанных на других языках, хотя они не тестировались явно.

| Среда выполнения | Версии | Платформы |
| --- | --- | --- |
| .NET Framework | 3.5 SP1, 4[1](#fn-runtime-1-def), 4.5[1](#fn-runtime-1-def), 4.5.1[1](#fn-runtime-1-def), 4.5.2 - 4.8 | Windows (x86-64) |

1

Ограниченная поддержка: Dynatrace может решать только проблемы, воспроизводимые на поддерживаемых версиях.

| Веб-фреймворк | Версии |
| --- | --- |
| ASP.NET | All versions supported |
| ASP.NET Core | All versions supported |
| ASP.NET Owin/Katana | 3.0.0 - 4.0.1 |
| [HttpClient](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | All versions supported |
| [HttpListener](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | All versions supported |
| [HttpWebRequest](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | All versions supported |

| Фреймворк удалённого взаимодействия | Версии |
| --- | --- |
| [.NET Remoting](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/72x4h507(v=vs.100)) | All versions supported |
| Amazon AWS Lambda SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| Amazon AWS SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| WCF | All versions supported |

1

Шаблон IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Фреймворк баз данных | Версии |
| --- | --- |
| ADO.NET | SQL Server, SQL CE, ODBC, OLEDB, Oracle using Oracle.DataAccess.dll |
| Amazon DynamoDB | 3.5.0+[1](#fn-database-framework-1-def) |
| Azure Cosmos DB | 3.18+ |
| [MongoDB .NET driver](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7, 2.8+ |

1

Шаблон IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SNS | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SQS | 3.5.0+[1](#fn-messaging-client-1-def) |
| [Azure Messaging Service Bus](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+ |
| [Confluent Kafka client library](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+ |
| [IBM MQ client](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1 |
| MSMQ Client | All versions supported |
| [MassTransit](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1, 8.3.2+ |
| [Microsoft Azure Service Bus client for .NET](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 3.1.1, 3.2.0 - 5.2.0 |
| [RabbitMQ client](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x, 7.x+ |

1

Шаблон IAsyncResult (APM) для .NET Framework 3.5 поддерживается в версии 1.331+.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

| Фреймворк логирования | Версии |
| --- | --- |
| [Microsoft Logging Extensions](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+ |
| [Serilog](https://serilog.net/) | 2.9+ |
| [log4net](https://logging.apache.org/log4net/) | 2.0.6+ |

### Go

* Поддержка 64-разрядных бинарных файлов Go, собранных с помощью:

  + The [Golang.org toolchain](https://dt-url.net/go)
  + The [Golang.org toolchain](https://dt-url.net/go) with [openssl-fips](https://dt-url.net/golang-fips) modifications (OneAgent version 1.295+).
* [Политика выпусков Go](https://dt-url.net/uos3rmi) поддерживает две последние основные версии Go.
* См. Supported Go versions для получения подробной информации.

| Инструментарий Go | Версии | Платформы |
| --- | --- | --- |
| [Golang toolchain with FIPS (openssl-fips) modifications](https://dt-url.net/golang-fips) | 1.23.6, 1.23.9, 1.24.4, 1.24.6, 1.25.3 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |
| [Official Golang toolchain](https://dt-url.net/go) | 1.23, 1.24, 1.25 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Веб-фреймворк | Версии |
| --- | --- |
| net/http | All versions supported |

| Фреймворки баз данных | Версии |
| --- | --- |
| [Cassandra client (gocql/gocql)](https://github.com/gocql/gocql) | 1.0 - 1.7 |
| [Microsoft SQL Server (denisenkom/go-mssqldb)](https://github.com/denisenkom/go-mssqldb) | 0.11 - 0.12 |
| [Microsoft SQL Server (microsoft/go-mssqldb)](https://github.com/microsoft/go-mssqldb) | 0.11 - 0.21, 1.0 - 1.9 |
| [MongoDB Go driver (mongo-go-driver)](https://github.com/mongodb/mongo-go-driver) | 1.3 - 1.17, 2.+ |
| [MySQL](https://github.com/go-sql-driver/mysql/) | 1.4.1, 1.5.0, 1.6.0, 1.7, 1.8 - 1.9 |
| [PostgreSQL (jackc/pgx)](https://github.com/jackc/pgx) | 4.7 - 4.18, 5.0 - 5.8 |
| [PostgreSQL (lib/pq)](https://github.com/lib/pq/) | 1.2.0, 1.3.0, 1.4.0 - 1.10.9 |
| [go-redis](https://github.com/redis/go-redis) | 7, 8.8.0 - 8.11.5, 9 |

| Клиенты обмена сообщениями | Версии |
| --- | --- |
| [Amazon SNS](https://github.com/aws/aws-sdk-go-v2/service/sns) | 1.15-1.38[1](#fn-messaging-clients-1-def) |
| [Kafka (IBM/sarama)](https://github.com/IBM/sarama) | 1.40+ |
| [Kafka (Shopify/sarama)](https://github.com/Shopify/sarama) | 1.18 - 1.39 |
| [Kafka (confluentinc/confluent-kafka-go)](https://github.com/confluentinc/confluent-kafka-go) | 1.9 - 2.8, 2.10, 2.11, 2.12, 2.13.0 |

1

Поддерживается в AWS Lambda.

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Amazon AWS SDK](https://github.com/aws/aws-sdk-go-v2) | 1.13.0 - 1.39.0[1](#fn-remoting-frameworks-1-def), 1.39.1 - 1.41.1[1](#fn-remoting-frameworks-1-def) |
| [gRPC](https://godoc.org/google.golang.org/grpc) | 1.17 - 1.28, 1.29, 1.30 - 1.39, 1.40 - 1.59, 1.60 - 1.68, 1.69 - 1.76, 1.78 - 1.79 |

1

Поддерживается в AWS Lambda. Расширенная поддержка трассировки для всех вызовов сервисов AWS

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.41 |

| Фреймворки логирования | Версии |
| --- | --- |
| [Logrus](https://github.com/sirupsen/logrus) | 1.7.1 - 1.9[1](#fn-logging-frameworks-1-def) |
| [Zap](https://github.com/uber-go/zap) | 1.10 - 1.27 |
| log/slog | All versions supported |

1

Версии 1.7.0 и ниже не поддерживаются из-за [a race condition problem](https://github.com/sirupsen/logrus/issues/1046) во фреймворке Logrus

* Поддержка ограничена стабильными выпусками Go.
* В системах Linux бинарный файл приложения должен быть динамически связан, если вы не используете Go static monitoring.

### Node.js

Node.js следует графику выпусков с долгосрочной поддержкой (LTS). В следующей таблице перечислены все полностью поддерживаемые версии. Однако некоторые версии LTS с истёкшим сроком поддержки имеют *ограниченную* поддержку. Подробности см. в разделе [Dynatrace support/desupport for Node.js versions](technology-support/application-software/nodejs.md#support-and-desupport "Узнайте о поддержке Dynatrace для Node.js-приложений.").

| Версии Node.js | Версии | Платформы |
| --- | --- | --- |
| Node.js | 18, 20, 22, 24, 25 | Alpine Linux 64-bit (x86-64), Linux (ARM64 (AArch64), PPCLE, s390, x86-64), Windows (x86-64) |

| Веб-фреймворки | Версии |
| --- | --- |
| [Connect](https://www.npmjs.com/package/connect) | >=3.0.0 |
| [Express](https://expressjs.com/) | 3, 4 |
| [Fastify](https://fastify.dev/) | >=3.3.0 |
| [Koa](https://www.npmjs.com/package/koa-router) | >=7.0.0 |
| [Nest](https://nestjs.com/) | >=6.0.0[2](#fn-web-frameworks-2-def) |
| [Node.js built-in HTTP/2 module](https://nodejs.org/api/http2.html) | All versions supported |
| [Node.js built-in HTTP/HTTPS modules](https://nodejs.org/api/http.html) | All versions supported[1](#fn-web-frameworks-1-def) |
| [hapi](https://hapijs.com/) | 17+ |
| [restify](https://www.npmjs.com/package/restify) | >=4.1[2](#fn-web-frameworks-2-def) |
| [router](https://www.npmjs.com/package/router) | >=1.0.0[2](#fn-web-frameworks-2-def) |

1

Поддерживается в AWS Lambda

2

Nest поддерживается неявно через базовые платформы Express или Fastify.

| HTTP-библиотеки | Версии |
| --- | --- |
| [Node.js built-in HTTP/HTTPS modules](https://nodejs.org/api/http.html) | All versions supported[1](#fn-http-libraries-1-def) |
| [Node.js built-in fetch API](https://nodejs.org/api/globals.html#fetch) | >=18.0.0[1](#fn-http-libraries-1-def) |
| [Undici HTTP client](https://www.npmjs.com/package/undici) | All versions supported[1](#fn-http-libraries-1-def) |

1

Поддерживается в AWS Lambda

| Фреймворки баз данных | Версии |
| --- | --- |
| Amazon DynamoDB | 2[1](#fn-database-frameworks-1-def), 3.0-3.901[1](#fn-database-frameworks-1-def), 3.902+[1](#fn-database-frameworks-1-def) |
| [Couchbase](https://www.npmjs.com/package/couchbase) | 2.4[1](#fn-database-frameworks-1-def), 2.5[1](#fn-database-frameworks-1-def), 2.6[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| [IOredis](https://www.npmjs.com/package/ioredis) | 4[2](#fn-database-frameworks-2-def), 5[2](#fn-database-frameworks-2-def) |
| [MongoDB](https://www.npmjs.com/package/mongodb) | 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), >=4[1](#fn-database-frameworks-1-def) |
| [MySQL](https://www.npmjs.com/package/mysql) | 2[1](#fn-database-frameworks-1-def) |
| [MySQL2](https://www.npmjs.com/package/mysql2) | 1.6[1](#fn-database-frameworks-1-def), 1.7[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def) |
| [PostgreSQL](https://www.npmjs.com/package/pg) | 5[2](#fn-database-frameworks-2-def), 6[2](#fn-database-frameworks-2-def), 7[2](#fn-database-frameworks-2-def), 8[2](#fn-database-frameworks-2-def) |
| [Redis](https://www.npmjs.com/package/redis) | 0.10[2](#fn-database-frameworks-2-def), 0.12[2](#fn-database-frameworks-2-def), 1.0[2](#fn-database-frameworks-2-def), 2.5[2](#fn-database-frameworks-2-def), 3.0[2](#fn-database-frameworks-2-def), 4[2](#fn-database-frameworks-2-def) |
| [SQLite3 (context passing only)](https://www.npmjs.com/package/sqlite3) | <5, 5.1+[3](#fn-database-frameworks-3-def) |
| [mssql](https://www.npmjs.com/package/mssql) | >=5[1](#fn-database-frameworks-1-def) |
| [oracledb](https://www.npmjs.com/package/oracledb) | 5[2](#fn-database-frameworks-2-def) |

1

Поддерживается в AWS Lambda

2

Поддерживается в AWS Lambda. Следующие API не поддерживаются: NoSQL, расширенная очередь, двухфазная фиксация и уведомление о непрерывных запросах.

3

Обратите внимание, что версии 5.0 не поддерживаются

| Фреймворки запросов API | Версии |
| --- | --- |
| [GraphQL](https://www.dynatrace.com/hub/detail/graphql/) | 15+[1](#fn-api-querying-frameworks-1-def) |
| [GraphQL Yoga](https://www.npmjs.com/package/graphql-yoga) | 5.7+[2](#fn-api-querying-frameworks-2-def) |

1

Поддерживается в AWS Lambda. Требуется Dynatrace Cluster версии 1.262+. Обнаружение сбоев сервисов не поддерживается.

2

Поддерживается в AWS Lambda. Требуется Dynatrace Cluster версии 1.334+. Обнаружение сбоев сервисов не поддерживается.

| Клиенты обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| [KafkaJs client library](https://www.npmjs.com/package/kafkajs) | 1.11+[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| [RabbitMQ](https://www.npmjs.com/package/amqplib) | 0.2[2](#fn-messaging-clients-2-def), 0.3.2[2](#fn-messaging-clients-2-def), 0.4.2[2](#fn-messaging-clients-2-def), 0.5[2](#fn-messaging-clients-2-def), 0.6[2](#fn-messaging-clients-2-def), 0.7[2](#fn-messaging-clients-2-def), 0.8[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def) |

1

Поддерживается в AWS Lambda

2

Публикаторы RabbitMQ поддерживаются в AWS Lambda

| Фреймворки удалённого взаимодействия | Версии |
| --- | --- |
| [Amazon AWS Lambda SDK](https://aws.amazon.com/sdk-for-javascript/) | 2[1](#fn-remoting-frameworks-1-def), 3.0-3.901[1](#fn-remoting-frameworks-1-def), 3.902+[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 2[2](#fn-remoting-frameworks-2-def), 3.0-3.901[2](#fn-remoting-frameworks-2-def), 3.902+[2](#fn-remoting-frameworks-2-def) |
| [gRPC](https://grpc.github.io/grpc/node/) | 1.10 - 1.24 |
| [grpc-js](https://www.npmjs.com/package/@grpc/grpc-js) | 1[3](#fn-remoting-frameworks-3-def) |

1

Поддерживается в AWS Lambda

2

Поддерживается в AWS Lambda. Расширенная поддержка трассировки для всех вызовов сервисов AWS

3

Клиентские вызовы gRPC поддерживаются в AWS Lambda

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-frameworks-1-def) |

1

Поддерживается в AWS Lambda

| Кэш | Версии |
| --- | --- |
| [Memcached](https://www.npmjs.com/package/memcached) | 2.2[1](#fn-cache-1-def) |

1

Поддерживается в AWS Lambda

| Фреймворки логирования | Версии |
| --- | --- |
| [Bunyan](https://www.npmjs.com/package/bunyan) | 1+[1](#fn-logging-frameworks-1-def) |
| [log4js](https://www.npmjs.com/package/log4js) | >=6.0.0[1](#fn-logging-frameworks-1-def) |
| [pino](https://www.npmjs.com/package/pino) | 5.14+[1](#fn-logging-frameworks-1-def), >=6[1](#fn-logging-frameworks-1-def) |
| [winston](https://www.npmjs.com/package/winston) | 3[1](#fn-logging-frameworks-1-def) |

1

Поддерживается в AWS Lambda

См. также OneAgent SDK for Node.js для расширенных возможностей трассировки.

### Python

| Среда выполнения Python | Версии | Платформы |
| --- | --- | --- |
| CPython | 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)) |

| Веб-фреймворки | Версии |
| --- | --- |
| [Django](https://github.com/django/django) | 1.8+[1](#fn-web-frameworks-1-def) |
| [FastAPI](https://github.com/tiangolo/fastapi) | 0.44+ |
| [Flask](https://github.com/pallets/flask) | 1.1.2+ |
| [Starlette](https://github.com/encode/starlette) | 0.12+ |
| [Tornado](https://github.com/tornadoweb/tornado) | 6.0+ |
| [aiohttp Server](https://docs.aiohttp.org/en/stable/web.html) | 3.6.1+ |
| [httpx](https://www.python-httpx.org/) | 0.20.0+ |

1

Включая Django REST framework на основе поддерживаемых версий Django.

| HTTP-библиотеки | Версии |
| --- | --- |
| [Requests](https://github.com/psf/requests) | 2[1](#fn-http-libraries-1-def) |
| [aiohttp Client](https://docs.aiohttp.org/en/stable/client.html#aiohttp-client) | 3.0+[1](#fn-http-libraries-1-def) |
| [urllib3](https://github.com/urllib3/urllib3) | 2.0+[1](#fn-http-libraries-1-def) |

1

Поддерживается в AWS Lambda.

| Фреймворки баз данных | Версии |
| --- | --- |
| Amazon DynamoDB | 1.11+[1](#fn-database-frameworks-1-def) |
| [PyMongo](https://pymongo.readthedocs.io/en/stable/) | 3.10+ |
| [SQL Alchemy](https://github.com/sqlalchemy/sqlalchemy) | 1.1+ |
| [mysqlclient](https://pypi.org/project/mysqlclient/) | 2.0+ |
| [psycopg2](https://github.com/psycopg/psycopg2) | 2.8.4+ |
| [python-oracledb](https://github.com/oracle/python-oracledb) | 1.0.1+ |
| [redis-py](https://github.com/redis/redis-py) | 3.4+[1](#fn-database-frameworks-1-def) |

1

Поддерживается в AWS Lambda.

| Библиотеки обмена сообщениями | Версии |
| --- | --- |
| Amazon EventBridge | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SNS | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SQS | 1.11+[1](#fn-messaging-libraries-1-def) |
| [Celery](https://github.com/celery/celery) | 5.3+ |
| [Confluent Kafka Python client library](https://github.com/confluentinc/confluent-kafka-python) | 2.0.2+[2](#fn-messaging-libraries-2-def) |
| [kafka-python client library](https://github.com/dpkp/kafka-python) | 1.4+[2](#fn-messaging-libraries-2-def) |

1

Поддерживается в AWS Lambda.

2

Поддерживается в AWS Lambda

| Библиотеки асинхронного выполнения | Версии |
| --- | --- |
| [Gevent](https://www.gevent.org/) | 20.9.0+ |
| [Python standard library: asyncio](https://docs.python.org/3/library/asyncio.html#module-asyncio) | All versions supported |
| [Python standard library: concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) | All versions supported |
| [Python standard library: queue](https://docs.python.org/3/library/queue.html#module-queue) | All versions supported |
| [Python standard library: subprocess](https://docs.python.org/3/library/subprocess.html#module-subprocess) | All versions supported |
| [Python standard library: threading](https://docs.python.org/3/library/threading.html#module-threading) | All versions supported |

| Библиотеки логирования | Версии |
| --- | --- |
| [Python standard library: logging](https://docs.python.org/3/library/logging.html) | All versions supported[1](#fn-logging-libraries-1-def) |
| [Structlog](https://github.com/hynek/structlog) | 19.0+[1](#fn-logging-libraries-1-def) |

1

Поддерживается в AWS Lambda.

* См. OneAgent SDK for Python для расширенных возможностей трассировки.
* См. Instrument your Python application with OpenTelemetry для поддержки OpenTelemetry.

### PHP

* Linux (mod\_php, FastCGI or PHP-FPM)
* Windows (mod\_php and PHP CGI)

| Версии PHP | Версии | Платформы |
| --- | --- | --- |
| PHP | 7.1 (Zend Engine 3.1), 7.2 (Zend Engine 3.2), 7.3 (Zend Engine 3.3), 7.4 (Zend Engine 3.4), 8.0 (Zend Engine 4.0), 8.1 (Zend Engine 4.1)[1](#fn-php-versions-1-def), 8.2 (Zend Engine 4.2)[2](#fn-php-versions-2-def), 8.3 (Zend Engine 4.3)[3](#fn-php-versions-3-def), 8.4 (Zend Engine 4.4)[4](#fn-php-versions-4-def), 8.5 (Zend Engine 4.5)[5](#fn-php-versions-5-def) | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

PHP 8.1 (от RC1 до 8.1.x) поддерживается.

2

PHP 8.2 (от RC1 — до официального выпуска PHP, до 8.2.x) поддерживается.

3

PHP 8.3 (от RC1 — до официального выпуска PHP, до 8.3.x) поддерживается.

4

PHP 8.4 (от RC2 — до официального выпуска PHP, до 8.4.x) поддерживается.

5

PHP 8.5 (от RC3 — до официального выпуска PHP, до 8.5.x) поддерживается.

См. Dynatrace support model for PHP applications с информацией о поддержке и прекращении поддержки.

| Фреймворки баз данных | Версии |
| --- | --- |
| [Microsoft Driver for PHP for SQL Server](https://docs.microsoft.com/en-us/sql/connect/php/system-requirements-for-the-php-sql-driver?view=sql-server-2017) | 4.0-5.6[1](#fn-database-frameworks-1-def) |
| [MongoDB PHP for Linux](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [MongoDB PHP for Windows](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [Oracle Database](https://php.net/manual/en/book.oci8.php) | All versions supported |
| [PDO](https://php.net/manual/en/book.pdo.php) | All versions supported |
| PostgreSQL | All versions supported |
| [mysql, mysqli](https://php.net/manual/en/set.mysqlinfo.php) | All versions supported |
| [phpredis](https://github.com/phpredis/phpredis) | 4.0.0+[2](#fn-database-frameworks-2-def) |
| [predis](https://github.com/predis/predis) | 1.1.2+ |

1

Поддерживается только для PHP NG Monitoring

2

Поддерживается только для PHP NG Monitoring. Реализация с использованием phpredis cluster поддерживается начиная с OneAgent версии 1.317. Реализация с использованием phpredis array в настоящее время не поддерживается.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| RabbitMQ client (php-amqplib) | 2.7+ |

| Платформы приложений | Версии |
| --- | --- |
| [Adobe Commerce](https://business.adobe.com/products/magento/magento-commerce.html) | All versions supported |
| [CodeIgniter](https://codeigniter.com/) | All versions supported |
| [Drupal](https://www.drupal.org/) | All versions supported |
| [Joomla](https://www.joomla.org/) | All versions supported |
| [Laminas](https://getlaminas.org/) | All versions supported |
| [Laravel](https://laravel.com/) | All versions supported |
| [Magento](https://business.adobe.com/products/magento/magento-commerce.html) | All versions supported |
| [Slim](https://www.slimframework.com/) | All versions supported |
| [Symfony](https://symfony.com/) | All versions supported |
| [WordPress](https://wordpress.com/) | All versions supported |

| Фреймворки мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

| Кэш | Версии |
| --- | --- |
| [Memcached](https://www.php.net/manual/en/book.memcached.php) | 3.0.0+[1](#fn-cache-1-def) |

1

Поддерживается только для PHP NG Monitoring на Linux и Alpine Linux/MUSL

| Фреймворки логирования | Версии |
| --- | --- |
| [Monolog](https://github.com/Seldaek/monolog) | 2.3 - 2.4, 3.0 |

См. OneAgent SDK for PHP для расширенных возможностей трассировки.

### IBM App Connect Enterprise / IBM Integration Bus

| Версии | Версии | Платформы |
| --- | --- | --- |
| [IBM App Connect Enterprise](https://www.ibm.com/support/knowledgecenter/en/SSTTDS) | 11.0.0.4+, 12.0.3.0+, 13.0.2.0+ | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |
| [IBM Integration Bus](https://www.ibm.com/support/knowledgecenter/de/SSMKHH/mapfiles/product_welcome.html) | 10 | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |

* Поддерживается только 64-разрядная версия
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

### C / C++

* См. OneAgent SDK for C/C++ для расширенных возможностей трассировки.
* См. Instrument your C++ application with OpenTelemetry для поддержки OpenTelemetry.

### Erlang/Elixir

См. Instrument your Erlang application with OpenTelemetry для поддержки OpenTelemetry.

### Ruby

См. Instrument your Ruby application with OpenTelemetry для поддержки OpenTelemetry.

### Rust

См. Instrument your Rust application with OpenTelemetry для поддержки OpenTelemetry.

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

Поддерживаются только Apache версий 2.2 и 2.4.

| Обогащение логов | Версии |
| --- | --- |
| access.logs | All versions supported |
| error.logs | All versions supported |

### Microsoft IIS

| Серверы | Версии | Платформы |
| --- | --- | --- |
| Microsoft IIS | 7.5, 8.0, 8.5, 10.0 | Windows (x86-64) |

### Envoy

| Серверы | Версии | Платформы |
| --- | --- | --- |
| [Envoy](https://www.envoyproxy.io/) | 1.27[1](#fn-servers-1-def), 1.28[1](#fn-servers-1-def), 1.29+[2](#fn-servers-2-def) | Linux (x86-64) |

1

Сбор данных на основе Envoy OpenTracing API. Поддерживаются статически настроенные маршруты в файле конфигурации bootstrap. Динамически добавленные маршруты (маршруты, добавленные после запуска envoy) не трассируются. Это может происходить, например, в средах Istio.

2

Начиная с версии 1.29, Envoy экспортирует данные с использованием OpenTelemetry в Dynatrace."). See Configure OpenTelemetry tracing with Envoy для получения подробной информации.

### NGINX

| Серверы | Версии | Платформы |
| --- | --- | --- |
| Kong Gateway | 2.8 - 3.6[2](#fn-servers-2-def), 3.7 - 3.9[3](#fn-servers-3-def) | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [NGINX](technology-support/application-software/nginx.md#nginx-versions "Узнайте подробности о поддержке NGINX в Dynatrace.") | 1.11.5 - 1.13.8[1](#fn-servers-1-def), 1.13.9 - 1.14.0[1](#fn-servers-1-def), 1.14.1 - 1.15.8[1](#fn-servers-1-def), 1.15.9 - 1.15.10[1](#fn-servers-1-def), 1.15.11 - 1.16.0[1](#fn-servers-1-def), 1.16.1 - 1.17.3[1](#fn-servers-1-def), 1.17.4 - 1.17.6[1](#fn-servers-1-def), 1.17.7[1](#fn-servers-1-def), 1.17.8[1](#fn-servers-1-def), 1.17.9[1](#fn-servers-1-def), 1.17.10 - 1.18.0, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.19.6, 1.19.7, 1.19.8, 1.19.9, 1.19.10, 1.20.0, 1.20.1, 1.20.2, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.24.0, 1.25.0, 1.25.1, 1.25.2, 1.25.3, 1.25.4, 1.25.5, 1.26.0, 1.26.1, 1.26.2, 1.26.3, 1.27.0, 1.27.1, 1.27.2, 1.27.3, 1.27.4, 1.27.5, 1.28.0, 1.28.1, 1.29.0, 1.29.1, 1.29.2, 1.29.3, 1.29.4 | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64, PPCLE) |
| [NGINX Plus](technology-support/application-software/nginx.md#nginx-plus-versions "Узнайте подробности о поддержке NGINX в Dynatrace.") | R11 - R14[1](#fn-servers-1-def), R15[1](#fn-servers-1-def), R16 - R17[1](#fn-servers-1-def), R18[1](#fn-servers-1-def), R19[1](#fn-servers-1-def), R20[1](#fn-servers-1-def), R21[1](#fn-servers-1-def), R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64), PPCLE) |
| [OpenResty](technology-support/application-software/nginx.md#openresty-versions "Узнайте подробности о поддержке NGINX в Dynatrace.") | 1.13.6, 1.15.8, 1.17.8, 1.19.3, 1.19.9, 1.21.4.1, 1.21.4.2, 1.21.4.3, 1.25.3.1, 1.25.3.2, 1.27.1.1, 1.27.1.2 | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [Tengine](technology-support/application-software/nginx.md#tengineversions "Узнайте подробности о поддержке NGINX в Dynatrace.") | 1.4.2 - 2.2.3, 2.3.0 - 2.3.3, 2.3.4, 2.4.0, 2.4.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |

1

Поддержка архитектуры CPU PPCLE добавлена в OneAgent версии 1.169, ARM64 (AArch64) — в OneAgent версии 1.189.

2

Требуется инструментация во время выполнения, см. NGINX runtime instrumentation

3

Требуется инструментация во время выполнения, см. NGINX runtime instrumentation. Снижение накладных расходов на инструментацию с агентами версий >= 1.313.

| Обогащение логов | Версии |
| --- | --- |
| error.logs | All versions supported |

### Varnish Cache

How to monitor Varnish Cache

## Мониторинг реальных пользователей

### Веб-мониторинг реальных пользователей

#### Браузеры

Все современные браузеры с включённым JavaScript и cookies поддерживаются, но тестируются только перечисленные ниже браузеры[1](#fn-7-1-def).

| Браузеры | Версии |
| --- | --- |
| Google Chrome | 3 latest versions (desktop and mobile) |
| Microsoft Edge | Latest version |
| Mozilla Firefox | 3 latest versions |
| Opera | 2 latest versions |
| Safari | 3 latest versions (macOS) |

1

Если вы не хотите, чтобы RUM JavaScript внедрялся в официально неподдерживаемые версии, define appropriate browser exclusion rules в настройках вашего приложения.

##### Браузеры для записи сессий

| Браузеры | Версии |
| --- | --- |
| Google Chrome | 3 latest versions (desktop and mobile) |
| Microsoft Edge | Latest version |
| Mozilla Firefox | 3 latest versions |
| Opera | 2 latest versions |
| Safari | 3 latest versions (macOS) |

Технологии, такие как Electron и аналогичные обёртки, создающие настольные приложения из веб-страниц, не поддерживаются.

#### Асинхронные запросы и одностраничные приложения

Dynatrace предлагает универсальную поддержку для каждого приложения через XHR или Fetch() API, а также специальную поддержку Angular.

| Универсальная поддержка |
| --- |
| Fetch API |
| XMLHttpRequest (XHR) |

| JavaScript-фреймворки | Версии |
| --- | --- |
| Angular | 2 - 16, 17+[1](#fn-8-1-def) |

1

При использовании Angular 17+ для вашего приложения требуется альтернативная конфигурация. См. Activate support for Angular 17+.

Мы прекратили предоставление специальной поддержки для определённых JavaScript-фреймворков начиная с RUM JavaScript версии 1.265 и Dynatrace версии 1.266. For details, see End of special support for certain JavaScript frameworks.

#### Веб-серверы и приложения

На следующих веб-серверах и в приложениях Dynatrace поддерживает автоматическое внедрение RUM, доставку RUM JavaScript, перенаправление RUM-маяков, и корреляцию действий пользователя с распределённой трассировкой.

| Веб-серверы и приложения |
| --- |
| Apache HTTP Server |
| IBM HTTP Server |
| Java servlet-based web applications |
| Kestrel (ASP.NET Core applications)[1](#fn-9-1-def)[2](#fn-9-2-def) |
| Microsoft IIS |
| NGINX |
| Node.js |
| Oracle HTTP Server |

1

Минимальные требуемые версии: .Net Core 3.1, .Net Standard 2.1, Microsoft.AspNetCore.Http.Abstractions 1.0.2 (for full framework).

2

Чтобы включить эту функцию OneAgent, перейдите в **Settings** > **Preferences** > **OneAgent features** и включите **Enable Real User Monitoring (RUM) for ASP.NET Core**.

На следующих веб-серверах и в приложениях Dynatrace поддерживает корреляцию действий пользователя с распределённой трассировкой для XHR-запросов.

| Веб-серверы и приложения |
| --- |
| Apache HttpCore |
| MuleSoft HTTP Listener |
| Netty [1](#fn-10-1-def) |
| Software AG WebMethods Integration Server |
| Undertow |

1

Чтобы включить эту функцию OneAgent, перейдите в **Settings** > **Preferences** > **OneAgent features** и включите **Netty Real User Monitoring (RUM) to distributed trace correlation**.

### Мониторинг реальных пользователей мобильных приложений

#### Операционные системы

| Операционные системы | Версии |
| --- | --- |
| Android | 5.0+ (API 21+) |
| iOS | 12+ |
| tvOS | 12+ |

#### Фреймворки

| Фреймворки | Версии |
| --- | --- |
| AFNetworking | 3.3 |
| Alamofire | 5+ |
| Apache Cordova | 9+ |
| OkHttp | 3+[1](#fn-11-1-def), 4+[1](#fn-11-1-def), 5+[1](#fn-11-1-def) |
| Xamarin[2](#fn-11-2-def) | Xamarin.iOS, Xamarin.Android, Xamarin.Forms (.NET Standard 2.0+) |
| .NET MAUI | .NET 6.0+ |
| React Native | 0.59+ |
| Flutter | 1.12+ |
| UIKit | Supported |
| SwiftUI | 2+ |
| Jetpack Compose | 1.4 - 1.10 |

1

Включая библиотеки на основе OkHttp, такие как Retrofit 2.

2

Dynatrace объявил о прекращении поддержки пакета Dynatrace Xamarin NuGet в мае 2024 г. и полном прекращении поддержки в мае 2025 г. Подробности см. в разделе [Deprecation and end of support for Dynatrace Xamarin NuGet package](../observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget.md#deprecation-announcement "Мониторинг приложений Xamarin с помощью Dynatrace OneAgent.").

#### OneAgent для iOS

* **32-разрядные устройства**: OneAgent для iOS версии 8.249 — последняя версия с поддержкой 32-разрядных устройств.
* **Xcode**: мы поддерживаем только версии Xcode, разрешённые Apple для отправки в App Store. Посетите [Submit your iOS apps to the App Store](https://developer.apple.com/ios/submit/) на сайте Apple Developer, чтобы узнать, какие версии Xcode поддерживаются в настоящее время.

Начиная с OneAgent для iOS версии 8.335, Dynatrace прекратил поддержку Xcode 16. Поддерживается только Xcode 26+.

Также учитывайте, что [Apple's App Store submission guidelines](https://dt-url.net/we038fb) ограничат поддержку приложениями, собранными с минимальной версией Xcode 26 примерно в апреле 2026 г.

Начиная с OneAgent для iOS версии 8.323, Dynatrace прекращает поддержку `static builds` and `Carthage` как методов интеграции.

Рекомендуем перейти на поддерживаемую альтернативу, такую как Swift Package Manager, для обеспечения совместимости и получения обновлений.

#### Плагин Dynatrace Android Gradle

* Gradle version 7.0.2+
* Android Gradle plugin version 7.0+

Подробности см. в разделе Dynatrace Android Gradle plugin.

### Dynatrace OpenKit

| Продукт | Версии |
| --- | --- |
| Java | 7, 8, 11, 12 |
| .NET | Core 3.1, 5, 6 |
| .NET Framework | 3.5, 4.6, 4.7, 4.8, 4.8.1 |
| .NET Standard | 2.0 |
| .NET UWP | Supported |
| .NET PCL | 4.5 |
| C/C++ Windows | Visual Studio 2015, 2017, 2019, and 2022 |
| C/C++ Linux | GCC 5.0.0+ or CLang 3.8.0+ |
| Node.js | 14+ |
| JavaScript | ES6+ |

Подробности доступны на следующих справочных страницах.

* [Dynatrace OpenKit - Java](https://github.com/Dynatrace/openkit-java/releases)
* [Dynatrace OpenKit - .NET](https://github.com/Dynatrace/openkit-dotnet/releases)
* [Dynatrace OpenKit - C/C++](https://github.com/Dynatrace/openkit-native#prerequisites)
* [Dynatrace OpenKit - JavaScript](https://github.com/Dynatrace/openkit-js)

## Расширения

См. [Dynatrace Hub](https://www.dynatrace.com/hub/?filter=all&type=extension&internal_source=doc&internal_medium=link&internal_campaign=cross) для получения полного списка технологий, поддерживаемых Dynatrace Extensions.

## Источники данных для приёма метрик

| Технологии | Версии |
| --- | --- |
| StatsD | All versions supported[1](#fn-technologies-1-def) |

1

Требуется OneAgent EEC. Поддерживается в Windows и Linux на архитектуре CPU x64

## Частные Synthetic-локации

См. Requirements for private Synthetic locations.

## Уровни поддержки сторонних технологий

### Поддерживается

Мы обеспечиваем поддержку любых проблем, непосредственно вызванных Dynatrace. Dynatrace имеет доступ к этой технологии и обычно может воспроизвести распространённые проблемы собственными силами, хотя среду может потребоваться настроить по запросу.

### Ограниченная поддержка

Dynatrace обеспечивает поддержку ограниченного набора функциональности для конкретной технологии. В большинстве случаев Dynatrace не имеет доступа к технологии с ограниченной поддержкой. При возникновении проблем служба поддержки Dynatrace сможет помочь вам, если сможет воспроизвести проблему в полностью поддерживаемой технологии, которая является основой для ограниченной поддержки.