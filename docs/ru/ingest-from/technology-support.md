---
title: Technology support
source: https://www.dynatrace.com/docs/ingest-from/technology-support
scraped: 2026-02-23T21:19:08.391476
---

# Technology support

# Technology support

* Latest Dynatrace
* 17-min read
* Updated on Feb 09, 2026

Dynatrace supports monitoring of the technologies and versions listed on this page. For serverless monitoring, see [Serverless compute support matrix](/docs/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS)."). For mainframe, see [Mainframe technology support](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

See also, [End-of-support announcements](/docs/whats-new/technology/end-of-support-news "End of support announcements for technologies supported by Dynatrace.").

Technology support version schema

Definition of the technology support version schema with examples:

* **Major version 5 is supported**

  + Major version 5 is supported, including all of its minor versions like 5.1 and 5.2
  + Other major versions are not supported like 6 and 7
* **Minor version 5.1 is supported**

  + Minor version 5.1 is supported, including all of its patch versions like 5.1.1 and 5.1.2
  + Other minor versions are not supported like 5.2 and 5.3
* **Patch version 5.1.1 is supported**

  + Patch version 5.1.1 is supported
  + Other patch versions are not supported like 5.1.2 and 5.1.3
* **Version range 5.1 â 5.3 is supported**

  + Minor versions 5.1, 5.2, and 5.3 are supported, including all of their patch versions like 5.1.1, 5.2.1, and 5.3.1
  + Other minor versions are not supported like 5.0 and 5.4
* **The minimum required version is 5+**

  + All major, minor, and patch versions starting from version 5 are supported, like 5, 5.1, 5.1.1, and 6

## Operating systems

You can install OneAgent on the following [Linux](#linux), [Unix](#unix), [Windows](#windows), and [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") operating systems.

### Linux

Dynatrace only tests and provides support for installation of OneAgent on the [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") distributions and versions listed below.

There are certain limitations when deploying OneAgent on a Linux host with Oracle Database Server 19c and/or mounted NFS drives. See [Troubleshoot OneAgent installation](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation#oracle-database-server-19c "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.").

Supported CPU architectures

* `x86-64` - 64-bit Intel/AMD
* `s390x` - 64-bit IBM Z mainframe
* `ppc64le` - 64-bit PowerPC
* `ARM64 (AArch64)` - 64-bit Linux ARM, including [AWS Graviton processorsï»¿](https://aws.amazon.com/ec2/graviton/)

| Supported OS | Versions | CPU architectures |
| --- | --- | --- |
| [AlmaLinux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| [Alpine Linux (musl libc) for containers](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") | 3.10 - 3.21[1](#fn-supported-os-1-def) | x86-64 |
| [Azure Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 2, 3 | x86-64 |
| [Bottlerocket](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | 1[2](#fn-supported-os-2-def) | ARM64 (AArch64), x86-64 |
| [CentOS Stream](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 9 | ARM64 (AArch64), PPCLE, x86-64 |
| [Debian](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 11, 12 | ARM64 (AArch64), x86-64 |
| [Fedora](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 41, 42 | x86-64 |
| [Oracle Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 7, 8, 9, 10 | x86-64 |
| [Red Hat Enterprise Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 7, 8, 9, 10 | ARM64 (AArch64), PPCLE, s390, x86-64 |
| [Red Hat Enterprise Linux CoreOS](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | 4.14[3](#fn-supported-os-3-def), 4.15[3](#fn-supported-os-3-def), 4.16[3](#fn-supported-os-3-def) | x86-64 |
| [Rocky Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 8, 9, 10 | ARM64 (AArch64), x86-64 |
| [SUSE Linux Enterprise Server](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 12.5, 15.3, 15.4, 15.5, 15.6, 15.7 | PPCLE, s390, x86-64 |
| [SUSE Linux Enterprise Server](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 15.3, 15.4, 15.5, 15.6, 15.7 | ARM64 (AArch64) |
| [Ubuntu](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 16.04 LTS, 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | PPCLE, x86-64 |
| [Ubuntu](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 18.04 LTS, 20.04 LTS, 22.04 LTS, 24.04 LTS | ARM64 (AArch64), s390 |
| [openSUSE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.") | 15.6 | PPCLE, x86-64 |

1

Only supported in containers that are monitored in OneAgent full-stack or application-only monitoring mode (musl libc 1.1.14 - 1.2.9). Binaries built against GNU C Library (glibc) running via gcompat library are not supported.

2

Only supported using application-only injection. Node metrics available using Kubernetes Platform Monitoring.

3

Supported for container-based rollout via Dynatrace Operator (see [OpenShift](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")).

Full-Stack Monitoring compatibility with Red Hat OpenShift

* OpenShift 4.19+: Only [Application observability](/docs/ingest-from/setup-on-k8s/how-it-works/application-monitoring "In-depth description of Application observability using the Dynatrace Operator.") and [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") are supported. This is because worker nodes can run only Red Hat Enterprise Linux CoreOS. To learn more, see [Red Hat release notes (1.5.13.2)ï»¿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).
* OpenShift 4.16â4.18: [Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "In-depth description of Classic Full-Stack monitoring using Dynatrace Operator.") is supported only on worker nodes that run Red Hat Enterprise Linux. If worker nodes run Red Hat Enterprise Linux CoreOS instead, only cloud-native [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") is supported.

### Unix

Dynatrace tests and provides support for installation of OneAgent on the [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.") and [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris "Learn how to install, update and troubleshoot OneAgent on Solaris.") versions listed below.

Supported CPU architectures

* `x86-64` - 64-bit Intel/AMD
* `POWER8` - 64-bit Power ISA
* `POWER9` - 64-bit Power ISA
* `POWER10`- 64-bit Power ISA
* `SPARC`

| UNIX System | Versions | CPU architectures |
| --- | --- | --- |
| [IBM AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix "Learn how to install OneAgent on AIX, how to customize installation, and more.") | 7.2 TL5[1](#fn-unix-system-1-def), 7.3 TL1[1](#fn-unix-system-1-def), 7.3 TL2[1](#fn-unix-system-1-def), 7.3 TL3[1](#fn-unix-system-1-def) | POWER10, POWER8, POWER9 |
| [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris "Learn how to install, update and troubleshoot OneAgent on Solaris.") | 11.4 | SPARC, x86-64 |

1

Installation on AIX WPARs is not supported.

### Windows



Dynatrace only tests and provides support for installation of OneAgent on the [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") versions listed below.

Supported CPU architectures

* `x86-64` -64-bit Intel/AMD

| Windows OS | Versions | CPU architectures |
| --- | --- | --- |
| [Windows Desktop 10](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 22H2[1](#fn-windows-os-1-def), 1507[2](#fn-windows-os-2-def), 1607[2](#fn-windows-os-2-def), 1809[2](#fn-windows-os-2-def), 21H2[2](#fn-windows-os-2-def) | x86-64 |
| [Windows Desktop 11](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 22H2, 23H2, 24H2, 25H2 | x86-64 |
| [Windows Server](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | 2012 R2[3](#fn-windows-os-3-def), 2016[4](#fn-windows-os-4-def), 2019[4](#fn-windows-os-4-def), 2022[4](#fn-windows-os-4-def), 2025[4](#fn-windows-os-4-def) | x86-64 |
| [Windows Server - Nano](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows "Learn how to install OneAgent on Windows, how to customize installation, and more.") | All versions supported[5](#fn-windows-os-5-def) | x86-64 |

1

Windows 10 Semi-Annual Channel (SAC), excluding Windows 10 IoT.

2

Windows 10 Long-Term Servicing Channel (LTSC), excluding Windows 10 IoT.

3

Windows 2012 R2 isn't supported on OneAgent versions 1.287 to 1.305. If your OneAgent is on these version, upgrade to OneAgent version 1.307 to enable support.

4

Long-Term Servicing Channel (LTSC). Support includes Server Core installation (requires OneAgent installed in headless-mode) or monitored in app-only scenario.

5

Limited support based on compatibility with Windows Server support when used as container image.

## File systems

OneAgent can detect and create disk entities (`dt.entity.disk`) on the following file systems:

| File system |
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

Starting with OneAgent version 1.307+.

2

Starting with OneAgent version 1.307+. Only space statistics are supported.

3

If the `mmpmonSocket` command on Linux fails, a fallback mode is available, which works when the CAP\_SETUID capability is enabled. For details, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#capsetuid-osagent "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

4

Starting with OneAgent version 1.309+.

5

Starting with OneAgent version 1.303+. Only space statistics are supported.

6

Starting with OneAgent version 1.323+. Only space statistics are supported.

7

Starting with OneAgent version 1.331+. Only space statistics are supported. Opt-in feature, need to be enabled in Disk options.

## Containers

| Features | Versions |
| --- | --- |
| Auto-injection in [Dockerï»¿](https://www.docker.com/) container (Deep monitoring)[1](#fn-2-1-def) | 1.6+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [containerdï»¿](https://containerd.io/) container (Deep monitoring) | 1.1.2+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [CRI-Oï»¿](https://cri-o.io/) container (Deep monitoring) | 1.12.5+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [Garden-RunCï»¿](https://docs.cloudfoundry.org/concepts/architecture/garden.html#garden-runc) container (Deep monitoring) | 1.0.0+ (32 and 64 bit) glibc or musl-libc required |
| Auto-injection in [BOSH bpmï»¿](https://bosh.io/docs/bpm/bpm/) container (Deep monitoring) | 0.11.0+ |
| Auto-injection in [Podmanï»¿](https://podman.io/) container (Deep monitoring)[2](#fn-2-2-def)[3](#fn-2-3-def) | 3.4.4â5.x.x |
| Docker container metrics[1](#fn-2-1-def) | 1.8, 1.9, 1.10, 1.11, 1.12, 1.13 RC2, 1.13.1, 17.03+ CE and EE |

1

Please see [known limitations of Docker container monitoring](/docs/observe/infrastructure-observability/container-platform-monitoring/container-platform-limitations-and-security#limitations "Overview on container groups monitoring").

2

Supported for OneAgent 1.267+ installed on the Podman node using [crunï»¿](https://github.com/containers/crun) container runtime, versions 0.17 - 1.15 Podman using the `runc` runtime isn't supported. For more details. see [OneAgent release notes version 1.267](/docs/whats-new/oneagent/sprint-267#podman-containers-support "Release notes for Dynatrace OneAgent version 1.267").

3

Podman containers started with `read-only=true` or `userns=keep-id` are not supported.

## Hypervisors

|  |
| --- |
| AIX (LPAR) |
| Hyper-V |
| KVM |
| Nutanix AHV[1](#fn-3-1-def) |
| QEMU |
| Xen |
| [VMware](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.") |
| AWS Nitro[1](#fn-3-1-def) |
| OpenShift Virtualization |

1

Dynatrace detects the hypervisor, but no dedicated logic is applied.

## Network interfaces

|  |
| --- |
| IEEE 802.3 Ethernet |
| IEEE 802.11 Wireless LAN |
| OpenVZ virtual network device (venet) |

* Both physical and virtual interfaces are supported, provided that they aren't assigned with a link-local address.

  + For IPv4: Link-local addresses are in range between `169.254.1.0` and `169.254.254.255`.
  + For IPv6: Link-local addresses are in range between `0xFE800000` and `0xFEBFFFFF`.
* Virtual Ethernet bridge interfaces aren't supported.
* Network interface bonding is supported.
* Only the TCP protocol is supported for traffic monitoring.

## Cloud platforms

### [AWS](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")

| Amazon Web Services (AWS) |
| --- |
| DynamoDB |
| Elastic Block Store (EBS) |
| Elastic Compute Cloud (EC2) |
| Elastic Load Balancing (ELB) |
| [Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.") |
| [Relational Database Service (RDS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/view-aws-monitoring-results#relational-database-service-page "Display AWS monitoring results in Dynatrace on your home dashboard, AWS account page, host page, and more.") |
| [Simple Storage Service (S3)](/docs/ingest-from/amazon-web-services/aws-platform/set-up-cors-in-amazon-s3 "Integrate CORS in Amazon Web Services for buckets within Amazon S3.") |

### [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")



| Compute service | Extension for deploying OneAgent | Integration of Dynatrace with Azure Monitor |
| --- | --- | --- |
| [Virtual Machines](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm "Learn how to install and configure OneAgent for monitoring Azure Virtual Machines using a VM extension.") | VM-Extension[1](#fn-4-1-def) | yes |
| [Virtual Machine Scale Set](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure VM Scale Set using a VM extension.") | VM-Extension[1](#fn-4-1-def) | yes |
| [Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric "Learn how to install, configure, and troubleshoot OneAgent for monitoring Azure Service Fabric using a VM extension.") | VM-Extension[1](#fn-4-1-def) | yes |
| [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Learn how to deploy, operate, and maintain OneAgent on Azure Kubernetes Service.") | Operator-rollout[2](#fn-4-2-def) | no |
| Cloud-Services (Classic) | [Startup scriptï»¿](https://github.com/dtPaTh/Dynatrace-Azure-CloudServices) | no |
| [HDInsightï»¿](https://github.com/safia-habib/Azure/blob/master/HDInsights/Readme.md) | Startup-Script | yes |
| [App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-azure-app-service "Install, configure, update, uninstall, and troubleshoot OneAgent for monitoring Azure App Service on Windows using an Azure site extension.") (Windows based) | SiteExtension | yes |
| [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | SiteExtension (Early Adopter release) | yes |

1

The VM-Extension automates the installation of OneAgent using Azure-native automation tooling. OneAgent can also be installed manually or via your automation tool of choice.

2

Windows Pods and Nodes unsupported.

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

Traces HTTP calls via HttpClient support

2

Trace database calls via supported database frameworks (for example, ADO.NET or JDBC).

3

Only available for [Standard Load Balancerï»¿](https://docs.microsoft.com/en-us/azure/load-balancer/load-balancer-standard-overview#why-use-standard-load-balancer)

4

End-2-End tracing via [Trace Contextï»¿](https://www.w3.org/TR/trace-context/)

5

End-2-End tracing using [OneAgent SDKï»¿](https://github.com/Dynatrace/OneAgent-SDK)

### [Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")

| Google Cloud services |
| --- |
| [Google Kubernetes Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke "Google GKE") |
| [GKE Autopilot](/docs/ingest-from/setup-on-k8s/deployment/application-observability#automatic "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") (only for automatic `applicationMonitoring`) |
| [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") |
| [Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine "Install OneAgent on Google Compute Engine.") |

### [VMware](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.")

| VMware | Versions |
| --- | --- |
| ESXi host | 6.5, 6.7, 7, 8.0 |
| vCenter server | 6.5, 6.7, 7, 8.0 |

### [Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")

Dynatrace supports a variety of Kubernetes flavors according to our [support model for Kubernetes and Openshift](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

| Distributions |
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

Limited support based on compatibility with upstream Kubernetes.

Some distributions and hosted versions require additional configuration. See [Technology support](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.") for more details.

## Other container and PaaS platforms

### [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")

| Buildpacks | Versions |
| --- | --- |
| Java buildpack | 3.11+ |
| PHP buildpack | v4.3.34+ |
| Staticfile buildpack | v1.4.6+ |
| Go buildpack | v1.8.41+ |
| .NET Core on Linux buildpack | v3.1+ |
| Node.js buildpack | v1.6.10+ (requires OneAgent version 1.131 or higher) |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ [See known issue](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.") |

#### [IBM Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")

| Features | Versions |
| --- | --- |
| IBM WebSphere Liberty buildpack | v3.9-20170419-1403+ [See known issue](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.") |

#### [Cloud Foundry](/docs/ingest-from/technology-support/support-model-for-pivotal-platform "Read about Dynatrace support for VMware Tanzu Application Service.")

| Features | Versions |
| --- | --- |
| Garden-runC | v1.0.0+ |
| BOSH BPM for platform process isolation | v0.11.0+ |
| Winc for Windows Server containers | Windows server 1709+ |
| VMware Tanzu Application Service (via BOSH add-on) | [See support model for Tanzu Application Service](/docs/ingest-from/technology-support/support-model-for-pivotal-platform "Read about Dynatrace support for VMware Tanzu Application Service.") |

### [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")

| Features | Versions |
| --- | --- |
| Stack | Heroku-18 |
| Stack | Heroku-20 (default) |

## Application Security

For details, see [Supported technologies](/docs/secure/application-security#tech "Access the Dynatrace Application Security functionalities.").

## Applications, services, and databases

### [Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.")

See [Dynatrace support/desupport for Java versions](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") for details.

| Virtual machines | Versions | Platforms |
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

Powered by Oracle JVM 8 or 11. For Native Images, see [Java Native Images](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.")

6

Powered by Oracle JVM 8, 11 or 17. For Native Images, see [Java Native Images](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

7

Powered by Oracle JVM 11, 17 or 19. For Native Images, see [Java Native Images](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.")

8

[Limited support](#limited-support): Dynatrace can only provide support for problems that can be reproduced on other JVMs.

9

Bellsoft Liberica v21+ 32-bit are not supported

| Application servers | Versions |
| --- | --- |
| [Apache TomEEï»¿](https://tomee.apache.org/) | 1, 7, 8 |
| [Apache Tomcatï»¿](https://tomcat.apache.org/) | 6, 7, 8, 8.5, 9, 10[1](#fn-application-servers-1-def), 11[1](#fn-application-servers-1-def) |
| [Fujitsu Interstageï»¿](https://www.fujitsu.com/global/products/software/middleware/application-infrastructure/interstage/) | 12.0[2](#fn-application-servers-2-def) |
| [IBM WebSphere Application Serverï»¿](https://www.ibm.com/products/software) | 8.5.5, 9.0, 8.5[3](#fn-application-servers-3-def) |
| [IBM WebSphere Libertyï»¿](https://developer.ibm.com/wasdev/websphere-liberty/) | 8.5 - 26[4](#fn-application-servers-4-def) |
| [JBoss Enterprise Application Platformï»¿](https://developers.redhat.com/products/eap/overview) | 7, 8 |
| [Oracle WebLogicï»¿](https://www.oracle.com/middleware/technologies/weblogic.html) | 11g[5](#fn-application-servers-5-def), 12c, 14c |
| [Payaraï»¿](https://www.payara.fish/) | 5, 6, 7 |
| [WildFlyï»¿](https://wildfly.org/) | 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18 - 26, 27 - 39 |

1

This version requires Java Servlet 5.0 support feature to be active

2

[Limited Support](#limited-support): Fully supported base technology: Java

3

Starting with OneAgent 1.183 only Java 7 is supported in WebSphere Application Server 8.5

4

Websphere Liberty's servlet 5 engine is supported since OneAgent version 1.259

5

10.3 = 11g

| ESBs and SOA | Versions |
| --- | --- |
| [Apache Camelï»¿](https://www.dynatrace.com/hub/detail/apache-camel/) | 2.21+, 3+, 4+[1](#fn-esbs-and-soa-1-def) |
| Apache OpenEJB | 3.1 |
| Mule (HTTP Listener) | 3.5, 3.6, 3.7, 3.8, 3.9, 4.1 - 4.9 |
| [Red Hat Fuse Standaloneï»¿](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| [Red Hat Fuse on OpenShiftï»¿](https://www.dynatrace.com/hub/detail/red-hat-fuse/) | 7.0+[1](#fn-esbs-and-soa-1-def) |
| TIBCO ActiveMatrix BusinessWorks | 5.8.2 - 5.14[2](#fn-esbs-and-soa-2-def), 6.4[2](#fn-esbs-and-soa-2-def), 6.5[2](#fn-esbs-and-soa-2-def), 6.6 - 6.8[2](#fn-esbs-and-soa-2-def) |

1

Only the Apache Camel connectors Undertow, Kafka, and MongoDB are supported.

2

Only TIBCO workflows that are triggered by an incoming web service request, HTTP request, or a JMS message are supported.

| Web framework | Versions |
| --- | --- |
| [Akka HTTP clientï»¿](https://doc.akka.io/docs/akka-http/current/client-side/index.html) | 10.1[2](#fn-web-framework-2-def), 10.0[2](#fn-web-framework-2-def), 10.2[2](#fn-web-framework-2-def), 10.4[2](#fn-web-framework-2-def), 10.5[2](#fn-web-framework-2-def), 10.6[2](#fn-web-framework-2-def), 10.7[2](#fn-web-framework-2-def) |
| [Akka HTTP serverï»¿](https://doc.akka.io/docs/akka-http/current/index.html) | 10.1, 10.2[1](#fn-web-framework-1-def), 10.4[1](#fn-web-framework-1-def), 10.5[1](#fn-web-framework-1-def), 10.6[1](#fn-web-framework-1-def), 10.7[1](#fn-web-framework-1-def) |
| [Apache HttpAsyncClientï»¿](https://hc.apache.org/httpcomponents-asyncclient-ga/) | 4.0[4](#fn-web-framework-4-def), 4.1[4](#fn-web-framework-4-def) |
| [Apache HttpClientï»¿](https://hc.apache.org/httpcomponents-client-ga/) | 3.1[4](#fn-web-framework-4-def), 4[4](#fn-web-framework-4-def), 5.0[4](#fn-web-framework-4-def), 5.1[4](#fn-web-framework-4-def), 5.2[4](#fn-web-framework-4-def) |
| [Apache HttpCoreï»¿](https://hc.apache.org/httpcomponents-core-ga/) | 4[3](#fn-web-framework-3-def), 5[4](#fn-web-framework-4-def) |
| [Apache Pekko HTTP clientï»¿](https://pekko.apache.org/docs/pekko-http/current/client-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| [Apache Pekko HTTP serverï»¿](https://pekko.apache.org/docs/pekko-http/current/server-side/index.html) | 1.0.0 - 1.2.0[10](#fn-web-framework-10-def) |
| Elasticsearch | 1.7[5](#fn-web-framework-5-def), 2.0[5](#fn-web-framework-5-def), 2.1[5](#fn-web-framework-5-def), 2.2[5](#fn-web-framework-5-def) |
| Grails | 3[6](#fn-web-framework-6-def) |
| Jakarta Servlet | 2.5, 3.0, 3.1, 4, 5, 6 |
| Java HttpUrlConnection | All versions supported[6](#fn-web-framework-6-def) |
| [Java IMS Soap Gateway clientï»¿](https://www.ibm.com/support/knowledgecenter/en/SS9NWR_3.2.0/com.ibm.ims.iconapij32.doc/icon_home_java.htm) | 3.2 |
| Jetty HTTP client | 7[6](#fn-web-framework-6-def), 8[6](#fn-web-framework-6-def), 9[6](#fn-web-framework-6-def), 10[6](#fn-web-framework-6-def), 11[6](#fn-web-framework-6-def), 12[6](#fn-web-framework-6-def) |
| [Jetty HTTP serverï»¿](https://www.eclipse.org/jetty/) | 7, 8, 9, 10, 11, 12 |
| LinkerdD | 1 |
| [Nettyï»¿](https://netty.io/) | 3.10[7](#fn-web-framework-7-def), 4[7](#fn-web-framework-7-def) |
| [Ning Asynchronous HTTP Clientï»¿](https://github.com/AsyncHttpClient/async-http-client) | 1.8, 1.9, 2, 3 |
| OkHttp | 3[7](#fn-web-framework-7-def), 4.0 - 4.3[7](#fn-web-framework-7-def), 4.4 - 4.12[7](#fn-web-framework-7-def), 5.+[7](#fn-web-framework-7-def) |
| [Play Frameworkï»¿](https://www.playframework.com/) | 2.2 - 2.6, 2.7, 2.8 |
| [Reactor Netty HTTP Clientï»¿](https://github.com/reactor/reactor-netty) | 0.8[7](#fn-web-framework-7-def), 0.9[7](#fn-web-framework-7-def), 1.0[7](#fn-web-framework-7-def), 1.1[7](#fn-web-framework-7-def), 1.2[7](#fn-web-framework-7-def), 1.3[7](#fn-web-framework-7-def) |
| [Reactor Netty HTTP Serverï»¿](https://github.com/reactor/reactor-netty) | 0.6, 0.7, 0.8, 0.9, 1.0 |
| [RxJavaï»¿](https://github.com/ReactiveX/RxJava) | 3+ |
| Software AG WebMethods Integration Server | 9.0[8](#fn-web-framework-8-def), 9.5 - 9.12[8](#fn-web-framework-8-def), 10.0 - 10.15[8](#fn-web-framework-8-def), 10.7[8](#fn-web-framework-8-def), 10.11[8](#fn-web-framework-8-def), 10.15[8](#fn-web-framework-8-def) |
| [Spring WebFluxï»¿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html) | 5, 6 |
| [Spring WebFlux WebClientï»¿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 5, 6 |
| [Undertowï»¿](https://undertow.io/) | 1[9](#fn-web-framework-9-def), 2.0 - 2.2[9](#fn-web-framework-9-def), 2.3+ |

1

Java and Scala bindings are supported.

2

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

3

Only synchronous request-handling supported. Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

4

Only HTTP/1.1 request-handling supported. Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

5

Currently, only the web protocol is supported, not the proprietary TCP protocol.

6

in servlet container only

7

The Promise interface and related APIs are not supported.

8

Dynatrace monitoring is limited to the incoming webrequests or JMS messages that start a workflow (business logic) on WebMethods.

9

Currently, Dynatrace can capture the incoming HTTP requests only when Undertow is configured to use the Servlet API.

10

Java and Scala 2 bindings are supported.

| Threading | Versions |
| --- | --- |
| CompletableFuture | All versions supported[1](#fn-threading-1-def) |
| [Java ForkJoinï»¿](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ForkJoinPool.html) | All versions supported[1](#fn-threading-1-def) |
| Kotlin Coroutines | 1.10.2 - 2.1 |
| Spring Integration | 2[1](#fn-threading-1-def), 3[1](#fn-threading-1-def), 4[1](#fn-threading-1-def), 5[1](#fn-threading-1-def), 6[1](#fn-threading-1-def) |
| [reactor-coreï»¿](https://github.com/reactor/reactor-core) | 3[1](#fn-threading-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Web services | Versions |
| --- | --- |
| Apache Axis2 | 1.6, 1.7, 1.8 |
| Apache CXF | 2, 3, 4 |
| Hessian Web Services | 2.1, 3.1, 4.0 |
| JAX-WS | 2 |
| [JBoss RESTEasyï»¿](https://resteasy.dev/) | 3, 4, 5, 6, 7 |
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

| Database frameworks | Versions |
| --- | --- |
| Amazon DynamoDB | 1[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def) |
| Apache Thrift | 2 |
| DataStax client for Apache Cassandra | 2.1[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| JDBC | 4+[1](#fn-database-frameworks-1-def) |
| [Jedis Redisï»¿](https://github.com/xetorthio/jedis) | 2, 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def), 5[1](#fn-database-frameworks-1-def), 6[1](#fn-database-frameworks-1-def), 7[1](#fn-database-frameworks-1-def) |
| [Lettuceï»¿](https://lettuce.io/) | 5.1 - 5.3[1](#fn-database-frameworks-1-def), 6.0.3 - 6.1.6[1](#fn-database-frameworks-1-def), 6.1.8 - 6.8[1](#fn-database-frameworks-1-def), 7.0 - 7.4[1](#fn-database-frameworks-1-def) |
| [MongoDB Reactive Streams driverï»¿](https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/) | 4.10+[1](#fn-database-frameworks-1-def), 5.0+[1](#fn-database-frameworks-1-def) |
| [MongoDB asynchronous driverï»¿](https://mongodb.github.io/mongo-java-driver/3.0/driver-async/) | 3.0 - 3.6.4[1](#fn-database-frameworks-1-def) |
| [MongoDB synchronous driver ï»¿](https://docs.mongodb.com/ecosystem/drivers/java/) | 2[1](#fn-database-frameworks-1-def), 3.0 - 3.6[1](#fn-database-frameworks-1-def), 3.7 - 3.11[1](#fn-database-frameworks-1-def), 3.12 - 4.11[1](#fn-database-frameworks-1-def), 5.0[1](#fn-database-frameworks-1-def) |
| Spring Boot Starter Data MongoDB | 2, 3, 4 |
| Spring Boot Starter Data Redis | 2.1+ |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Messaging clients | Versions |
| --- | --- |
| [ActiveMQï»¿](https://activemq.apache.org) | 4[1](#fn-messaging-clients-1-def), 5[1](#fn-messaging-clients-1-def) |
| [ActiveMQ Artemisï»¿](https://activemq.apache.org/components/artemis/) | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon EventBridge | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 1[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| HornetQ | 2.2[1](#fn-messaging-clients-1-def), 2.3[1](#fn-messaging-clients-1-def), 2.4[1](#fn-messaging-clients-1-def) |
| [IBM MQ clientï»¿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q118320_.htm) | 8[1](#fn-messaging-clients-1-def), 9[1](#fn-messaging-clients-1-def) |
| JMS | 1.1[1](#fn-messaging-clients-1-def), 2.0[1](#fn-messaging-clients-1-def), 3.0[1](#fn-messaging-clients-1-def) |
| [Kafkaï»¿](https://kafka.apache.org/documentation/) | 1.0 - 1.1[1](#fn-messaging-clients-1-def), 2.0 - 2.3[1](#fn-messaging-clients-1-def), 2.4 - 2.7[1](#fn-messaging-clients-1-def), 2.8[1](#fn-messaging-clients-1-def), 3.0 - 3.6[1](#fn-messaging-clients-1-def), 3.7 - 3.9[1](#fn-messaging-clients-1-def), 4.0[1](#fn-messaging-clients-1-def) |
| [RabbitMQï»¿](https://www.rabbitmq.com/java-client.html) | 3[1](#fn-messaging-clients-1-def), 4.0.0 - 5.22.0[1](#fn-messaging-clients-1-def) |
| Software AG WebMethod Broker and Universal messaging via JMS | All versions supported |
| [Spring AMQPï»¿](https://spring.io/projects/spring-amqp) | 1.5, 2.0, 2.1, 2.2, 2.3 |
| Spring Cloud Stream Kafka Binder | 3+ |
| Tibco EMS | All versions supported[2](#fn-messaging-clients-2-def) |

1

Publishers supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

2

Tracing is only supported via JMS.

| Remoting frameworks | Versions |
| --- | --- |
| [Akka Remotingï»¿](https://doc.akka.io/docs/akka/2.5/remoting.html) | 2.4[2](#fn-remoting-frameworks-2-def), 2.5[2](#fn-remoting-frameworks-2-def), 2.3[3](#fn-remoting-frameworks-3-def), 2.6[3](#fn-remoting-frameworks-3-def), 2.7[3](#fn-remoting-frameworks-3-def) |
| [Amazon AWS Lambda SDKï»¿](https://aws.amazon.com/en/sdk-for-java/) | 1[1](#fn-remoting-frameworks-1-def), 2[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 1[2](#fn-remoting-frameworks-2-def), 2[2](#fn-remoting-frameworks-2-def) |
| [Apache Pekko Remotingï»¿](https://pekko.apache.org/docs/pekko/current/remoting.html#classic-remoting-deprecated-) | 1.0.0 - 1.2.0[5](#fn-remoting-frameworks-5-def) |
| [Apache Thriftï»¿](https://thrift.apache.org/) | 0.7 - 0.13 |
| Glassfish RMI-IIOP | All versions supported |
| IBM JVM RMI-IIOP | All versions supported |
| JBoss Enterprise Application Platform - RMI-IIOP | 7, 8 |
| JBoss Enterprise Application Platform - Remoting | 7, 8 |
| [Java CICS Transaction Gateway clientï»¿](https://www.ibm.com/support/knowledgecenter/en/SSZHFX_9.1.0/basejavadoc/index.html) | 9.0 - 9.2 |
| Java IMS TM Resource Adapter | All versions supported |
| Java RMI-JRMP | All versions supported |
| OpenJDK/Oracle JVM RMI-IIOP | All versions supported |
| WebLogic RMI-IIOP | All versions supported |
| WebSphere Liberty RMI-IIOP | All versions supported |
| WebSphere RMI-IIOP | All versions supported |
| [gRPCï»¿](https://grpc.github.io/grpc-java/javadoc/index.html) | 1.18 - 1.79[4](#fn-remoting-frameworks-4-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

2

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Extended tracing support for all AWS service calls

3

Only supported when Netty is used; not supported when using Artery. Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

4

gRPC client calls supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

5

Only supported when classic-remoting is used; not supported when using Artery. Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Monitoring frameworks | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-frameworks-1-def), 1.4 - 1.54[1](#fn-monitoring-frameworks-1-def) |
| [OpenTracingï»¿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Logging frameworks | Versions |
| --- | --- |
| Apache Tomcat access logs | 8, 9, 10, 11 |
| [JBoss LogManagerï»¿](https://github.com/jboss-logging/jboss-logmanager) | 1.1+, 2, 3 |
| [Log4J2 (Apache)ï»¿](https://logging.apache.org/log4j/2.x/) | 2.7 - 2.12, 2.13.0, 2.13.1, 2.13.3, 2.14 - 2.17.1, 2.17.2 - 2.25 |
| [Logback (QOS)ï»¿](https://logback.qos.ch/) | 1.x |
| java.util.logging | All versions supported |

See also [OneAgent SDK for Java](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.



### [Java Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.")

| Virtual machine | Versions | Platforms |
| --- | --- | --- |
| [GraalVM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.") | GraalVM for JDK 17 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 21 version 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 22[1](#fn-virtual-machine-1-def), GraalVM for JDK 23[1](#fn-virtual-machine-1-def), GraalVM for JDK 24[1](#fn-virtual-machine-1-def) | Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

Binaries running on Alpine-based Linux systems are not supported

| Application framework | Versions |
| --- | --- |
| [Micronautï»¿](https://micronaut.io) | 3.9+[1](#fn-application-framework-1-def) |
| [Quarkusï»¿](https://quarkus.io) | 3.8+[1](#fn-application-framework-1-def) |
| [Spring Bootï»¿](https://spring.io/projects/spring-boot) | 3.0+[1](#fn-application-framework-1-def), 4.0+[1](#fn-application-framework-1-def) |

1

Supported in regard to building native images. This doesn't mean that all technologies provided by the framework are supported.

| Web framework | Versions |
| --- | --- |
| [Apache HttpClientï»¿](https://hc.apache.org/httpcomponents-client-ga/) | 5.2+ |
| [Nettyï»¿](https://netty.io/) | 4[1](#fn-web-framework-1-def) |
| [Spring WebFlux WebClientï»¿](https://docs.spring.io/spring/docs/current/spring-framework-reference/web-reactive.html#webflux-client) | 6 |

1

The Promise interface and related APIs are not supported.

| Application servers | Versions |
| --- | --- |
| [Apache Tomcatï»¿](https://tomcat.apache.org/) | 10, 11 |

| Database frameworks | Versions |
| --- | --- |
| Spring Boot Starter Data MongoDB | 3 |

### [.NET](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.")

Dynatrace supports .NET applications written in C#. Limited support for .NET applications written in other languages is available, though not explicitly tested.

| Runtime | Versions | Platforms |
| --- | --- | --- |
| [.NET and .NET Core](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | Core 2.1, Core 2.2, Core 3.0, Core 3.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64), Windows (x86-64) |
| [.NET and .NET Core](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | 5, 6, 7, 8, 9, 10 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Web framework | Versions |
| --- | --- |
| ASP.NET Core | All versions supported |
| ASP.NET Owin/Katana | 3.0.0+ |
| [HttpClientï»¿](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | All versions supported |
| [HttpListenerï»¿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | All versions supported |
| [HttpWebRequestï»¿](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | All versions supported |

| Web service | Versions |
| --- | --- |
| [Azure Functionsï»¿](https://azure.microsoft.com/en-us/services/functions/) | 2 |

| Remoting framework | Versions |
| --- | --- |
| Amazon AWS Lambda SDK | 3.5.0+ |
| Amazon AWS SDK | 3.5.0+ |
| [gRPCï»¿](https://www.nuget.org/packages/Grpc.AspNetCore) | 2.23.2+ |

| Database framework | Versions |
| --- | --- |
| ADO.NET | SQL Server, SQL CE, Oracle using Oracle.DataAccess.dll |
| Amazon DynamoDB | 3.5.0+ |
| Azure Cosmos DB | 3.18+ |
| [MongoDB .NET driverï»¿](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7, 2.8+ |

| Messaging client | Versions |
| --- | --- |
| Amazon EventBridge | 3.5.0+ |
| Amazon SNS | 3.5.0+ |
| Amazon SQS | 3.5.0+ |
| [Azure Messaging Service Busï»¿](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+ |
| [Confluent Kafka client libraryï»¿](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+ |
| [IBM MQ clientï»¿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1 |
| [MassTransitï»¿](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1, 8.3.2+ |
| [Microsoft Azure Service Bus client for .NETï»¿](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 5.2.0 |
| [RabbitMQ clientï»¿](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x, 7.x+ |

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

| Logging framework | Versions |
| --- | --- |
| [Microsoft Logging Extensionsï»¿](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+ |
| [Serilogï»¿](https://serilog.net/) | 2.9+ |
| [log4netï»¿](https://logging.apache.org/log4net/) | 2.0.6+ |

See also [OneAgent SDK for .NET](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.

### [.NET Framework](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.")

Dynatrace supports .NET applications written in C#. Limited support for .NET applications written in other languages is available, though not explicitly tested.

| Runtime | Versions | Platforms |
| --- | --- | --- |
| [.NET Framework](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | 3.5 SP1, 4[1](#fn-runtime-1-def), 4.5[1](#fn-runtime-1-def), 4.5.1[1](#fn-runtime-1-def), 4.5.2 - 4.8 | Windows (x86-64) |

1

Limited support: Dynatrace can only solve problems that can be reproduced on supported versions.

| Web framework | Versions |
| --- | --- |
| ASP.NET | All versions supported |
| ASP.NET Core | All versions supported |
| ASP.NET Owin/Katana | 3.0.0 - 4.0.1 |
| [HttpClientï»¿](https://docs.microsoft.com/en-us/previous-versions/visualstudio/hh193681(v=vs.118)) | All versions supported |
| [HttpListenerï»¿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/httplistener) | All versions supported |
| [HttpWebRequestï»¿](https://docs.microsoft.com/en-us/dotnet/api/system.net.httpwebrequest?view=netframework-4.8) | All versions supported |

| Remoting framework | Versions |
| --- | --- |
| [.NET Remotingï»¿](https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-4.0/72x4h507(v=vs.100)) | All versions supported |
| Amazon AWS Lambda SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| Amazon AWS SDK | 3.5.0+[1](#fn-remoting-framework-1-def) |
| WCF | All versions supported |

1

The IAsyncResult pattern (APM) for .NET Framework 3.5 is supported in version 1.331+.

| Database framework | Versions |
| --- | --- |
| ADO.NET | SQL Server, SQL CE, ODBC, OLEDB, Oracle using Oracle.DataAccess.dll |
| Amazon DynamoDB | 3.5.0+[1](#fn-database-framework-1-def) |
| Azure Cosmos DB | 3.18+ |
| [MongoDB .NET driverï»¿](https://mongodb.github.io/mongo-csharp-driver/) | 2.3 - 2.7, 2.8+ |

1

The IAsyncResult pattern (APM) for .NET Framework 3.5 is supported in version 1.331+.

| Messaging client | Versions |
| --- | --- |
| Amazon EventBridge | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SNS | 3.5.0+[1](#fn-messaging-client-1-def) |
| Amazon SQS | 3.5.0+[1](#fn-messaging-client-1-def) |
| [Azure Messaging Service Busï»¿](https://www.nuget.org/packages/Azure.Messaging.ServiceBus) | 7+ |
| [Confluent Kafka client libraryï»¿](https://www.nuget.org/packages/Confluent.Kafka/) | 1.4.0+ |
| [IBM MQ clientï»¿](https://www.ibm.com/support/knowledgecenter/en/SSFKSJ_9.1.0/com.ibm.mq.dev.doc/q029250_.htm) | 8.0 - 9.1 |
| MSMQ Client | All versions supported |
| [MassTransitï»¿](https://www.nuget.org/packages/MassTransit) | 7.0 - 8.3.1, 8.3.2+ |
| [Microsoft Azure Service Bus client for .NETï»¿](https://www.nuget.org/packages/Microsoft.Azure.ServiceBus/) | 2.0.0 - 3.1.1, 3.2.0 - 5.2.0 |
| [RabbitMQ clientï»¿](https://www.nuget.org/packages/RabbitMQ.Client) | 4.1 - 6.x, 7.x+ |

1

The IAsyncResult pattern (APM) for .NET Framework 3.5 is supported in version 1.331+.

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

| Logging framework | Versions |
| --- | --- |
| [Microsoft Logging Extensionsï»¿](https://docs.microsoft.com/en-us/dotnet/core/extensions/logging) | 3.0.0+ |
| [Serilogï»¿](https://serilog.net/) | 2.9+ |
| [log4netï»¿](https://logging.apache.org/log4net/) | 2.0.6+ |

### [Go](/docs/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.")



* Support for 64-bit Go binaries built with:

  + The [Golang.org toolchainï»¿](https://dt-url.net/go)
  + The [Golang.org toolchainï»¿](https://dt-url.net/go) with [openssl-fipsï»¿](https://dt-url.net/golang-fips) modifications (OneAgent version 1.295+).
* The [Go release policyï»¿](https://dt-url.net/uos3rmi) supports the last two major Go versions.
* See [Supported Go versions](/docs/ingest-from/technology-support/application-software/go/support/supported-go-versions "Find out which Go versions are supported by Dynatrace.") for details.

| Go toolchains | Versions | Platforms |
| --- | --- | --- |
| [Golang toolchain with FIPS (openssl-fips) modificationsï»¿](https://dt-url.net/golang-fips) | 1.22.7, 1.22.9, 1.23.6, 1.23.9, 1.24.4, 1.24.6, 1.25.3 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |
| [Official Golang toolchainï»¿](https://dt-url.net/go) | 1.22, 1.23, 1.24, 1.25 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

| Web framework | Versions |
| --- | --- |
| net/http | All versions supported |

| Database frameworks | Versions |
| --- | --- |
| [Cassandra client (gocql/gocql)ï»¿](https://github.com/gocql/gocql) | 1.0 - 1.7 |
| [Microsoft SQL Server (denisenkom/go-mssqldb)ï»¿](https://github.com/denisenkom/go-mssqldb) | 0.11 - 0.12 |
| [Microsoft SQL Server (microsoft/go-mssqldb)ï»¿](https://github.com/microsoft/go-mssqldb) | 0.11 - 0.21, 1.0 - 1.9 |
| [MongoDB Go driver (mongo-go-driver)ï»¿](https://github.com/mongodb/mongo-go-driver) | 1.3 - 1.17, 2.+ |
| [MySQLï»¿](https://github.com/go-sql-driver/mysql/) | 1.4.1, 1.5.0, 1.6.0, 1.7, 1.8 - 1.9 |
| [PostgreSQL (jackc/pgx)ï»¿](https://github.com/jackc/pgx) | 4.7 - 4.18, 5.0 - 5.8 |
| [PostgreSQL (lib/pq)ï»¿](https://github.com/lib/pq/) | 1.2.0, 1.3.0, 1.4.0 - 1.10.9 |
| [go-redisï»¿](https://github.com/redis/go-redis) | 7, 8.8.0 - 8.11.5, 9 |

| Messaging clients | Versions |
| --- | --- |
| [Amazon SNSï»¿](https://github.com/aws/aws-sdk-go-v2/service/sns) | 1.15-1.38[1](#fn-messaging-clients-1-def) |
| [Kafka (IBM/sarama)ï»¿](https://github.com/IBM/sarama) | 1.40+ |
| [Kafka (Shopify/sarama)ï»¿](https://github.com/Shopify/sarama) | 1.18 - 1.39 |
| [Kafka (confluentinc/confluent-kafka-go)ï»¿](https://github.com/confluentinc/confluent-kafka-go) | 1.9 - 2.8, 2.10, 2.11, 2.12 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Remoting frameworks | Versions |
| --- | --- |
| [Amazon AWS SDKï»¿](https://github.com/aws/aws-sdk-go-v2) | 1.13.0 - 1.39.0[1](#fn-remoting-frameworks-1-def) |
| [gRPCï»¿](https://godoc.org/google.golang.org/grpc) | 1.17 - 1.28, 1.29, 1.30 - 1.39, 1.40 - 1.59, 1.60 - 1.68, 1.69 - 1.76, 1.78 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Extended tracing support for all AWS service calls

| Monitoring frameworks | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.40 |

| Logging frameworks | Versions |
| --- | --- |
| [Logrusï»¿](https://github.com/sirupsen/logrus) | 1.7.1 - 1.9[1](#fn-logging-frameworks-1-def) |
| [Zapï»¿](https://github.com/uber-go/zap) | 1.10 - 1.27 |
| log/slog | All versions supported |

1

Versions 1.7.0 and lower are not supported due to [a race condition problemï»¿](https://github.com/sirupsen/logrus/issues/1046) in the Logrus framework

* [Support limited to stable Go releases](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations#go-official-stable-releases "Learn the limitations for Go support and their workarounds.").
* On Linux systems, application binary must be dynamically linked unless you're using [Go static monitoring](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring#go-static-monitoring "Learn how you can enable Go monitoring in Dynatrace.").

### [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.")



Node.js follows a Long Term Support (LTS) release schedule. The following table lists all fully supported versions. However, some end-of-life LTS versions have *limited* support. For details, see [Dynatrace support/desupport for Node.js versions](/docs/ingest-from/technology-support/application-software/nodejs#support-and-desupport "Read about Dynatrace support for Node.js applications.").

| Node.js versions | Versions | Platforms |
| --- | --- | --- |
| [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | 18, 20, 22, 24 | Alpine Linux 64-bit (x86-64), Linux (ARM64 (AArch64), PPCLE, s390, x86-64), Windows (x86-64) |

| Web frameworks | Versions |
| --- | --- |
| [Connectï»¿](https://www.npmjs.com/package/connect) | >=3.0.0 |
| [Expressï»¿](https://expressjs.com/) | 3, 4 |
| [Fastifyï»¿](https://fastify.dev/) | >=3.3.0 |
| [Koaï»¿](https://www.npmjs.com/package/koa-router) | >=7.0.0 |
| [Nestï»¿](https://nestjs.com/) | >=6.0.0[2](#fn-web-frameworks-2-def) |
| [Node.js built-in HTTP/2 moduleï»¿](https://nodejs.org/api/http2.html) | All versions supported |
| [Node.js built-in HTTP/HTTPS modulesï»¿](https://nodejs.org/api/http.html) | All versions supported[1](#fn-web-frameworks-1-def) |
| [hapiï»¿](https://hapijs.com/) | 17+ |
| [restifyï»¿](https://www.npmjs.com/package/restify) | >=4.1[2](#fn-web-frameworks-2-def) |
| [routerï»¿](https://www.npmjs.com/package/router) | >=1.0.0[2](#fn-web-frameworks-2-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Nest is supported implicitly via underlying Express or Fastify platforms.

| HTTP libraries | Versions |
| --- | --- |
| [Node.js built-in HTTP/HTTPS modulesï»¿](https://nodejs.org/api/http.html) | All versions supported[1](#fn-http-libraries-1-def) |
| [Node.js built-in fetch APIï»¿](https://nodejs.org/api/globals.html#fetch) | >=18.0.0[1](#fn-http-libraries-1-def) |
| [Undici HTTP clientï»¿](https://www.npmjs.com/package/undici) | All versions supported[1](#fn-http-libraries-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Database frameworks | Versions |
| --- | --- |
| Amazon DynamoDB | 2[1](#fn-database-frameworks-1-def), 3.0-3.901[1](#fn-database-frameworks-1-def), 3.902+[1](#fn-database-frameworks-1-def) |
| [Couchbaseï»¿](https://www.npmjs.com/package/couchbase) | 2.4[1](#fn-database-frameworks-1-def), 2.5[1](#fn-database-frameworks-1-def), 2.6[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), 4[1](#fn-database-frameworks-1-def) |
| [IOredisï»¿](https://www.npmjs.com/package/ioredis) | 4[2](#fn-database-frameworks-2-def), 5[2](#fn-database-frameworks-2-def) |
| [MongoDBï»¿](https://www.npmjs.com/package/mongodb) | 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def), >=4[1](#fn-database-frameworks-1-def) |
| [MySQLï»¿](https://www.npmjs.com/package/mysql) | 2[1](#fn-database-frameworks-1-def) |
| [MySQL2ï»¿](https://www.npmjs.com/package/mysql2) | 1.6[1](#fn-database-frameworks-1-def), 1.7[1](#fn-database-frameworks-1-def), 2[1](#fn-database-frameworks-1-def), 3[1](#fn-database-frameworks-1-def) |
| [PostgreSQLï»¿](https://www.npmjs.com/package/pg) | 5[2](#fn-database-frameworks-2-def), 6[2](#fn-database-frameworks-2-def), 7[2](#fn-database-frameworks-2-def), 8[2](#fn-database-frameworks-2-def) |
| [Redisï»¿](https://www.npmjs.com/package/redis) | 0.10[2](#fn-database-frameworks-2-def), 0.12[2](#fn-database-frameworks-2-def), 1.0[2](#fn-database-frameworks-2-def), 2.5[2](#fn-database-frameworks-2-def), 3.0[2](#fn-database-frameworks-2-def), 4[2](#fn-database-frameworks-2-def) |
| [SQLite3 (context passing only)ï»¿](https://www.npmjs.com/package/sqlite3) | <5, 5.1+[3](#fn-database-frameworks-3-def) |
| [mssqlï»¿](https://www.npmjs.com/package/mssql) | >=5[1](#fn-database-frameworks-1-def) |
| [oracledbï»¿](https://www.npmjs.com/package/oracledb) | 5[2](#fn-database-frameworks-2-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). The following APIs are not support: NoSQL, advanced queuing, two-phase commit, and continuous query notification.

3

Note that 5.0 versions are not supported

| API Querying frameworks | Versions |
| --- | --- |
| [GraphQLï»¿](https://www.dynatrace.com/hub/detail/graphql/) | 15+[1](#fn-api-querying-frameworks-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Requires Dynatrace Cluster version 1.262+. Service failure detection is not supported.

| Messaging clients | Versions |
| --- | --- |
| Amazon EventBridge | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SNS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| Amazon SQS | 2[1](#fn-messaging-clients-1-def), 3.0-3.901[1](#fn-messaging-clients-1-def), 3.902+[1](#fn-messaging-clients-1-def) |
| [KafkaJs client libraryï»¿](https://www.npmjs.com/package/kafkajs) | 1.11+[1](#fn-messaging-clients-1-def), 2[1](#fn-messaging-clients-1-def) |
| [RabbitMQï»¿](https://www.npmjs.com/package/amqplib) | 0.2[2](#fn-messaging-clients-2-def), 0.3.2[2](#fn-messaging-clients-2-def), 0.4.2[2](#fn-messaging-clients-2-def), 0.5[2](#fn-messaging-clients-2-def), 0.6[2](#fn-messaging-clients-2-def), 0.7[2](#fn-messaging-clients-2-def), 0.8[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def), 0.9[2](#fn-messaging-clients-2-def), 0.10[2](#fn-messaging-clients-2-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

RabbitMQ publishers supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Remoting frameworks | Versions |
| --- | --- |
| [Amazon AWS Lambda SDKï»¿](https://aws.amazon.com/sdk-for-javascript/) | 2[1](#fn-remoting-frameworks-1-def), 3.0-3.901[1](#fn-remoting-frameworks-1-def), 3.902+[1](#fn-remoting-frameworks-1-def) |
| Amazon AWS SDK | 2[2](#fn-remoting-frameworks-2-def), 3.0-3.901[2](#fn-remoting-frameworks-2-def), 3.902+[2](#fn-remoting-frameworks-2-def) |
| [gRPCï»¿](https://grpc.github.io/grpc/node/) | 1.10 - 1.24 |
| [grpc-jsï»¿](https://www.npmjs.com/package/@grpc/grpc-js) | 1[3](#fn-remoting-frameworks-3-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

2

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options"). Extended tracing support for all AWS service calls

3

gRPC client calls supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Monitoring frameworks | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-frameworks-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Cache | Versions |
| --- | --- |
| [Memcachedï»¿](https://www.npmjs.com/package/memcached) | 2.2[1](#fn-cache-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Logging frameworks | Versions |
| --- | --- |
| [Bunyanï»¿](https://www.npmjs.com/package/bunyan) | 1+[1](#fn-logging-frameworks-1-def) |
| [log4jsï»¿](https://www.npmjs.com/package/log4js) | >=6.0.0[1](#fn-logging-frameworks-1-def) |
| [pinoï»¿](https://www.npmjs.com/package/pino) | 5.14+[1](#fn-logging-frameworks-1-def), >=6[1](#fn-logging-frameworks-1-def) |
| [winstonï»¿](https://www.npmjs.com/package/winston) | 3[1](#fn-logging-frameworks-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

See also [OneAgent SDK for Node.js](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.

### Python



| Python runtime | Versions | Platforms |
| --- | --- | --- |
| CPython | 3.8, 3.9, 3.10, 3.11, 3.12, 3.13 | Alpine Linux 64-bit (x86-64, ARM64 (AArch64)), Linux (x86-64, ARM64 (AArch64)) |

| Web frameworks | Versions |
| --- | --- |
| [Djangoï»¿](https://github.com/django/django) | 1.8+[1](#fn-web-frameworks-1-def) |
| [FastAPIï»¿](https://github.com/tiangolo/fastapi) | 0.44+ |
| [Flaskï»¿](https://github.com/pallets/flask) | 1.1.2+ |
| [Starletteï»¿](https://github.com/encode/starlette) | 0.12+ |
| [Tornadoï»¿](https://github.com/tornadoweb/tornado) | 6.0+ |
| [aiohttp Serverï»¿](https://docs.aiohttp.org/en/stable/web.html) | 3.6.1+ |
| [httpxï»¿](https://www.python-httpx.org/) | 0.20.0+ |

1

Including Django REST framework based on supported Django versions.

| HTTP libraries | Versions |
| --- | --- |
| [Requestsï»¿](https://github.com/psf/requests) | 2[1](#fn-http-libraries-1-def) |
| [aiohttp Clientï»¿](https://docs.aiohttp.org/en/stable/client.html#aiohttp-client) | 3.0+[1](#fn-http-libraries-1-def) |
| [urllib3ï»¿](https://github.com/urllib3/urllib3) | 2.0+[1](#fn-http-libraries-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Database frameworks | Versions |
| --- | --- |
| Amazon DynamoDB | 1.11+[1](#fn-database-frameworks-1-def) |
| [PyMongoï»¿](https://pymongo.readthedocs.io/en/stable/) | 3.10+ |
| [SQL Alchemyï»¿](https://github.com/sqlalchemy/sqlalchemy) | 1.1+ |
| [mysqlclientï»¿](https://pypi.org/project/mysqlclient/) | 2.0+ |
| [psycopg2ï»¿](https://github.com/psycopg/psycopg2) | 2.8.4+ |
| [python-oracledbï»¿](https://github.com/oracle/python-oracledb) | 1.0.1+ |
| [redis-pyï»¿](https://github.com/redis/redis-py) | 3.4+[1](#fn-database-frameworks-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

| Messaging libraries | Versions |
| --- | --- |
| Amazon EventBridge | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SNS | 1.11+[1](#fn-messaging-libraries-1-def) |
| Amazon SQS | 1.11+[1](#fn-messaging-libraries-1-def) |
| [Celeryï»¿](https://github.com/celery/celery) | 5.3+ |
| [Confluent Kafka Python client libraryï»¿](https://github.com/confluentinc/confluent-kafka-python) | 2.0.2+[2](#fn-messaging-libraries-2-def) |
| [kafka-python client libraryï»¿](https://github.com/dpkp/kafka-python) | 1.4+[2](#fn-messaging-libraries-2-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

2

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options")

| Asynchronous execution libraries | Versions |
| --- | --- |
| [Geventï»¿](https://www.gevent.org/) | 20.9.0+ |
| [Python standard library: asyncioï»¿](https://docs.python.org/3/library/asyncio.html#module-asyncio) | All versions supported |
| [Python standard library: concurrent.futuresï»¿](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures) | All versions supported |
| [Python standard library: queueï»¿](https://docs.python.org/3/library/queue.html#module-queue) | All versions supported |
| [Python standard library: subprocessï»¿](https://docs.python.org/3/library/subprocess.html#module-subprocess) | All versions supported |
| [Python standard library: threadingï»¿](https://docs.python.org/3/library/threading.html#module-threading) | All versions supported |

| Logging libraries | Versions |
| --- | --- |
| [Python standard library: loggingï»¿](https://docs.python.org/3/library/logging.html) | All versions supported[1](#fn-logging-libraries-1-def) |
| [Structlogï»¿](https://github.com/hynek/structlog) | 19.0+[1](#fn-logging-libraries-1-def) |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

* See [OneAgent SDK for Python](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.
* See [Instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.") for OpenTelemetry support.

### [PHP](/docs/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.")

* Linux (mod\_php, FastCGI or PHP-FPM)
* Windows (mod\_php and PHP CGI)

| PHP versions | Versions | Platforms |
| --- | --- | --- |
| [PHP](/docs/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.") | 7.1 (Zend Engine 3.1), 7.2 (Zend Engine 3.2), 7.3 (Zend Engine 3.3), 7.4 (Zend Engine 3.4), 8.0 (Zend Engine 4.0), 8.1 (Zend Engine 4.1)[1](#fn-php-versions-1-def), 8.2 (Zend Engine 4.2)[2](#fn-php-versions-2-def), 8.3 (Zend Engine 4.3)[3](#fn-php-versions-3-def), 8.4 (Zend Engine 4.4)[4](#fn-php-versions-4-def), 8.5 (Zend Engine 4.5)[5](#fn-php-versions-5-def) | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64)), Windows (x86-64) |

1

PHP 8.1 (from RC1 to 8.1.x) is supported.

2

PHP 8.2 (from RC1 - before official PHP release up to 8.2.x) is supported.

3

PHP 8.3 (from RC1 - before official PHP release up to 8.3.x) is supported.

4

PHP 8.4 (from RC2 - before official PHP release up to 8.4.x) is supported.

5

PHP 8.5 (from RC3 - before official PHP release up to 8.5.x) is supported.

See [Dynatrace support model for PHP applications](/docs/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.") for support and desupport details.

| Database frameworks | Versions |
| --- | --- |
| [Microsoft Driver for PHP for SQL Serverï»¿](https://docs.microsoft.com/en-us/sql/connect/php/system-requirements-for-the-php-sql-driver?view=sql-server-2017) | 4.0-5.6[1](#fn-database-frameworks-1-def) |
| [MongoDB PHP for Linuxï»¿](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [MongoDB PHP for Windowsï»¿](https://www.php.net/manual/en/set.mongodb.php) | 1.3+ |
| [Oracle Databaseï»¿](https://php.net/manual/en/book.oci8.php) | All versions supported |
| [PDOï»¿](https://php.net/manual/en/book.pdo.php) | All versions supported |
| PostgreSQL | All versions supported |
| [mysql, mysqliï»¿](https://php.net/manual/en/set.mysqlinfo.php) | All versions supported |
| [phpredisï»¿](https://github.com/phpredis/phpredis) | 4.0.0+[2](#fn-database-frameworks-2-def) |
| [predisï»¿](https://github.com/predis/predis) | 1.1.2+ |

1

Supported only for PHP NG Monitoring

2

Supported only for PHP NG Monitoring. The implementation using phpredis cluster is supported from OneAgent version 1.317. The implementation using phpredis array is not currently supported.

| Messaging client | Versions |
| --- | --- |
| RabbitMQ client (php-amqplib) | 2.7+ |

| Application platforms | Versions |
| --- | --- |
| [Adobe Commerceï»¿](https://business.adobe.com/products/magento/magento-commerce.html) | All versions supported |
| [CodeIgniterï»¿](https://codeigniter.com/) | All versions supported |
| [Drupalï»¿](https://www.drupal.org/) | All versions supported |
| [Joomlaï»¿](https://www.joomla.org/) | All versions supported |
| [Laminasï»¿](https://getlaminas.org/) | All versions supported |
| [Laravelï»¿](https://laravel.com/) | All versions supported |
| [Magentoï»¿](https://business.adobe.com/products/magento/magento-commerce.html) | All versions supported |
| [Slimï»¿](https://www.slimframework.com/) | All versions supported |
| [Symfonyï»¿](https://symfony.com/) | All versions supported |
| [WordPressï»¿](https://wordpress.com/) | All versions supported |

| Monitoring frameworks | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

| Cache | Versions |
| --- | --- |
| [Memcachedï»¿](https://www.php.net/manual/en/book.memcached.php) | 3.0.0+[1](#fn-cache-1-def) |

1

Supported only for PHP NG Monitoring on Linux and Alpine Linux/MUSL

| Logging frameworks | Versions |
| --- | --- |
| [Monologï»¿](https://github.com/Seldaek/monolog) | 2.3 - 2.4, 3.0 |

See [OneAgent SDK for PHP](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.

### IBM App Connect Enterprise / IBM Integration Bus



| Versions | Versions | Platforms |
| --- | --- | --- |
| [IBM App Connect Enterpriseï»¿](https://www.ibm.com/support/knowledgecenter/en/SSTTDS) | 11.0.0.4+, 12.0.3.0+, 13.0.2.0+ | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |
| [IBM Integration Busï»¿](https://www.ibm.com/support/knowledgecenter/de/SSMKHH/mapfiles/product_welcome.html) | 10 | AIX (POWER8, POWER9, POWER10), Linux (x86-64, s390), Windows (x86-64) |

* Only the 64-bit version is supported
* Monitoring is supported for all node types
* Tracing is supported for the following node types:

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

### C / [C++](/docs/ingest-from/technology-support/application-software/cpp "Learn how to instrument your C++ application with OpenTelemetry as a data source for Dynatrace.")

* See [OneAgent SDK for C/C++](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing capabilities.
* See [Instrument your C++ application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/cpp "Learn how to instrument your C++ application using OpenTelemetry and Dynatrace.") for OpenTelemetry support.

### [Erlang/Elixir](/docs/ingest-from/technology-support/application-software/erlang-elixir "Learn how to instrument your Erlang/Elixir application with OpenTelemetry as a data source for Dynatrace.")

See [Instrument your Erlang application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/erlang "Learn how to instrument your Erlang application using OpenTelemetry and Dynatrace.") for OpenTelemetry support.

### [Ruby](/docs/ingest-from/technology-support/application-software/ruby "Learn how to instrument your Ruby application with OpenTelemetry as a data source for Dynatrace.")

See [Instrument your Ruby application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.") for OpenTelemetry support.

### [Rust](/docs/ingest-from/technology-support/application-software/rust "Learn how to instrument your Rust application with OpenTelemetry as a data source for Dynatrace monitoring.")

See [Instrument your Rust application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/rust "Learn how to instrument your Rust application using OpenTelemetry and Dynatrace.") for OpenTelemetry support.

## Web servers

### Apache HTTP

| Servers | Versions | Platforms |
| --- | --- | --- |
| Apache HTTP Server | 2.0, 2.2 | Alpine Linux 64-bit (x86-64), Linux (PPCLE, x86-64, ARM64 (AArch64)), Solaris (SPARC), Windows (x86-64) |
| Apache HTTP Server | 2.4 | Alpine Linux 64-bit (x86-64), Linux (PPCLE, x86-64, ARM64 (AArch64)), Solaris (SPARC, x86-64), Windows (x86-64) |
| Fujitsu Interstage IHS | 12[1](#fn-servers-1-def), 13[1](#fn-servers-1-def) | Linux (x86-64), Windows (x86-64) |
| IBM HTTP Server | 7, 8 | AIX (POWER8, POWER9, POWER10), Linux (PPCLE, x86-64), Solaris (SPARC), Windows (x86-64) |
| IBM HTTP Server | 8.5 | AIX (POWER8, POWER9, POWER10), Linux (PPCBE), Linux (PPCLE, x86-64), Linux (s390), Solaris (SPARC), Windows (x86-64) |
| IBM HTTP Server | 9 | AIX (POWER8, POWER9, POWER10), Linux (PPCLE, x86-64), Linux (s390), Solaris (SPARC), Windows (x86-64) |
| Oracle HTTP Server | 11g, 12c | Solaris (SPARC) |

1

Only Apache versions 2.2 and 2.4 are supported.

| Log enrichment | Versions |
| --- | --- |
| access.logs | All versions supported |
| error.logs | All versions supported |

### Microsoft IIS

| Servers | Versions | Platforms |
| --- | --- | --- |
| Microsoft IIS | 7.5, 8.0, 8.5, 10.0 | Windows (x86-64) |

### Envoy

| Servers | Versions | Platforms |
| --- | --- | --- |
| [Envoyï»¿](https://www.envoyproxy.io/) | 1.27[1](#fn-servers-1-def), 1.28[1](#fn-servers-1-def), 1.29+[2](#fn-servers-2-def) | Linux (x86-64) |

1

Data collection based on the Envoy OpenTracing API. Supported are statically configured routes in the bootstrap config file. Dynamically added routes (routes added after envoy startup) are not traced. This can occur in, for example, Istio environments.

2

As of version 1.29, Envoy exports data using [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."). See [Configure OpenTelemetry tracing with Envoy](/docs/ingest-from/opentelemetry/integrations/envoy "Learn how to configure Envoy to send OpenTelemetry traces to Dynatrace.") for details.

### NGINX

| Servers | Versions | Platforms |
| --- | --- | --- |
| [Kong Gateway](/docs/ingest-from/technology-support/application-software/nginx/kong-gateway "Learn how to monitor the Kong Gateway with Dynatrace.") | 2.8 - 3.6[2](#fn-servers-2-def), 3.7 - 3.9[3](#fn-servers-3-def) | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [NGINX](/docs/ingest-from/technology-support/application-software/nginx#nginx-versions "Learn the details of Dynatrace support for NGINX.") | 1.11.5 - 1.13.8[1](#fn-servers-1-def), 1.13.9 - 1.14.0[1](#fn-servers-1-def), 1.14.1 - 1.15.8[1](#fn-servers-1-def), 1.15.9 - 1.15.10[1](#fn-servers-1-def), 1.15.11 - 1.16.0[1](#fn-servers-1-def), 1.16.1 - 1.17.3[1](#fn-servers-1-def), 1.17.4 - 1.17.6[1](#fn-servers-1-def), 1.17.7[1](#fn-servers-1-def), 1.17.8[1](#fn-servers-1-def), 1.17.9[1](#fn-servers-1-def), 1.17.10 - 1.18.0, 1.19.0, 1.19.1, 1.19.2, 1.19.3, 1.19.4, 1.19.5, 1.19.6, 1.19.7, 1.19.8, 1.19.9, 1.19.10, 1.20.0, 1.20.1, 1.20.2, 1.21.0, 1.21.1, 1.21.2, 1.21.3, 1.21.4, 1.21.5, 1.21.6, 1.22.0, 1.22.1, 1.23.0, 1.23.1, 1.23.2, 1.23.3, 1.23.4, 1.24.0, 1.25.0, 1.25.1, 1.25.2, 1.25.3, 1.25.4, 1.25.5, 1.26.0, 1.26.1, 1.26.2, 1.26.3, 1.27.0, 1.27.1, 1.27.2, 1.27.3, 1.27.4, 1.27.5, 1.28.0, 1.29.0, 1.29.1, 1.29.2, 1.29.3, 1.29.4 | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64, PPCLE) |
| [NGINX Plus](/docs/ingest-from/technology-support/application-software/nginx#nginx-plus-versions "Learn the details of Dynatrace support for NGINX.") | R11 - R14[1](#fn-servers-1-def), R15[1](#fn-servers-1-def), R16 - R17[1](#fn-servers-1-def), R18[1](#fn-servers-1-def), R19[1](#fn-servers-1-def), R20[1](#fn-servers-1-def), R21[1](#fn-servers-1-def), R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36 | Alpine Linux 64-bit (x86-64), Linux (x86-64, ARM64 (AArch64), PPCLE) |
| [OpenResty](/docs/ingest-from/technology-support/application-software/nginx#openresty-versions "Learn the details of Dynatrace support for NGINX.") | 1.13.6, 1.15.8, 1.17.8, 1.19.3, 1.19.9, 1.21.4.1, 1.21.4.2, 1.21.4.3, 1.25.3.1, 1.25.3.2, 1.27.1.1, 1.27.1.2 | Alpine Linux 64-bit (ARM64 (AArch64), x86-64), Linux (ARM64 (AArch64), x86-64) |
| [Tengine](/docs/ingest-from/technology-support/application-software/nginx#tengineversions "Learn the details of Dynatrace support for NGINX.") | 1.4.2 - 2.2.3, 2.3.0 - 2.3.3, 2.3.4, 2.4.0, 2.4.1 | Alpine Linux 64-bit (x86-64), Linux (x86-64) |

1

Support for the CPU architecture PPCLE was added with OneAgent version 1.169 and ARM64 (AArch64) with OneAgent version 1.189.

2

Requires runtime instrumentation, see [NGINX runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.")

3

Requires runtime instrumentation, see [NGINX runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime."). Reduced instrumentation overhead with agent versions >= 1.313.

| Log enrichment | Versions |
| --- | --- |
| error.logs | All versions supported |

### Varnish Cache

[How to monitor Varnish Cache](/docs/observe/infrastructure-observability/databases/extensions/varnish-cache-1 "Monitor the statistics of your Varnish Cache instances.")

## Real User Monitoring

### Web-based Real User Monitoring



#### Browsers

All modern browsers with JavaScript and cookies enabled are supported, but only the browsers below are tested[1](#fn-7-1-def).

| Browsers | Versions |
| --- | --- |
| Google Chrome | 3 latest versions (desktop and mobile) |
| Microsoft Edge | Latest version |
| Mozilla Firefox | 3 latest versions |
| Opera | 2 latest versions |
| Safari | 3 latest versions (macOS) |

1

If you don't want the RUM JavaScript to be injected into officially unsupported versions, [define appropriate browser exclusion rules](/docs/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring#exclude-browsers "Disable Real User Monitoring for certain IP addresses, browsers, bots, and spiders.") in your application settings.

##### Browsers for session recording

| Browsers | Versions |
| --- | --- |
| Google Chrome | 3 latest versions (desktop and mobile) |
| Microsoft Edge | Latest version |
| Mozilla Firefox | 3 latest versions |
| Opera | 2 latest versions |
| Safari | 3 latest versions (macOS) |

Technologies like Electron and similar wrappers that create desktop applications from webpages are not supported.

#### Async requests and single page applications

Dynatrace offers generic support for every application via XHR or Fetch() API but also offers special support for Angular.

| Generic support |
| --- |
| Fetch API |
| XMLHttpRequest (XHR) |

| JavaScript frameworks | Versions |
| --- | --- |
| Angular | 2 - 16, 17+[1](#fn-8-1-def) |

1

Alternative configuration is required when Angular 17+ is used for your application. See [Activate support for Angular 17+](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#enable-angular-17-support "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

We stopped offering special support for certain JavaScript frameworks starting with RUM JavaScript version 1.265 and Dynatrace version 1.266. For details, see [End of special support for certain JavaScript frameworks](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions#desupported-frameworks-js-265 "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

#### Web servers and applications

On the following web servers and applications, Dynatrace supports [RUM auto-injection](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), [RUM JavaScript delivery](/docs/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements."), [RUM beacon forwarding](/docs/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."), and [user action to distributed trace correlation](/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.").

| Web servers and applications |
| --- |
| Apache HTTP Server |
| IBM HTTP Server |
| Java servlet-based web applications |
| Kestrel (ASP.NET Core applications)[1](#fn-9-1-def)[2](#fn-9-2-def) |
| Microsoft IIS |
| [NGINX](/docs/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.") |
| [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") |
| Oracle HTTP Server |

1

Minimum required versions: .Net Core 3.1, .Net Standard 2.1, Microsoft.AspNetCore.Http.Abstractions 1.0.2 (for full framework).

2

To enable this as a OneAgent feature, go to **Settings** > **Preferences** > **OneAgent features** and turn on **Enable Real User Monitoring (RUM) for ASP.NET Core**.

On the following web servers and applications, Dynatrace supports [user action to distributed trace correlation](/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs "Enable the correlation between cross-origin XHR actions and distributed traces.") for XHR requests.

| Web servers and applications |
| --- |
| Apache HttpCore |
| MuleSoft HTTP Listener |
| Netty [1](#fn-10-1-def) |
| Software AG WebMethods Integration Server |
| Undertow |

1

To enable this as a OneAgent feature, go to **Settings** > **Preferences** > **OneAgent features** and turn on **Netty Real User Monitoring (RUM) to distributed trace correlation**.

### Mobile app Real User Monitoring

#### Operating systems

| Operating systems | Versions |
| --- | --- |
| [Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.") | 5.0+ (API 21+) |
| [iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") | 12+ |
| [tvOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app "Instrument mobile application monitoring for iOS apps, customize the auto-instrumentation, and capture additional data via manual instrumentation.") | 12+ |

#### Frameworks

| Frameworks | Versions |
| --- | --- |
| AFNetworking | 3.3 |
| Alamofire | 5+ |
| [Apache Cordova](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/apache-cordova "Set up Dynatrace to monitor hybrid mobile apps with the Cordova plugin.") | 9+ |
| OkHttp | 3+[1](#fn-11-1-def), 4+[1](#fn-11-1-def), 5+[1](#fn-11-1-def) |
| [Xamarin](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget "Monitor Xamarin apps with Dynatrace OneAgent.")[2](#fn-11-2-def) | Xamarin.iOS, Xamarin.Android, Xamarin.Forms (.NET Standard 2.0+) |
| [.NET MAUI](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/maui "Monitor .NET MAUI applications with Dynatrace OneAgent.") | .NET 6.0+ |
| [React Native](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/react-native "Auto-instrument your React Native applications with OneAgent.") | 0.59+ |
| [Flutter](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/flutter "Learn how to auto-instrument your Flutter applications with OneAgent.") | 1.12+ |
| UIKit | Supported |
| [SwiftUI](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/instrumentation/instrument-swiftui-controls "Use the Dynatrace SwiftUI instrumentor to monitor your SwiftUI apps.") | 2+ |
| [Jetpack Compose](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin/monitoring-capabilities#compose-instrumentation "Configure the Dynatrace Android Gradle plugin to adjust the monitoring capabilities of OneAgent.") | 1.4 - 1.9 |

1

Including OkHttp-based libraries like Retrofit 2.

2

Dynatrace will deprecate the Dynatrace Xamarin NuGet package in May 2024 and desupport it in May 2025. For details, see [Deprecation and end of support for Dynatrace Xamarin NuGet package](/docs/observe/digital-experience/mobile-applications/cross-platform-frameworks/xamarin-nuget#deprecation-announcement "Monitor Xamarin apps with Dynatrace OneAgent.").

#### OneAgent for iOS

* **32-bit devices**: OneAgent for iOS version 8.249 is the last version that supports 32-bit devices.
* **Xcode**: We support only the Xcode versions that Apple allows for App Store submission. Check [Submit your iOS apps to the App Storeï»¿](https://developer.apple.com/ios/submit/) on the Apple Developer site to learn which Xcode versions are currently supported.

Starting with OneAgent for iOS version 8.335, Dynatrace stopped supporting Xcode 16. We only support Xcode 26+.

Also, be aware that [Apple's App Store submission guidelinesï»¿](https://dt-url.net/we038fb) will restrict support to applications built with a minimum of Xcode 26 around April 2026.

Starting with OneAgent for iOS version 8.323, Dynatrace will stop supporting `static builds` and `Carthage` as integration methods.

We recommend migrating to a supported alternative like Swift Package Manager to ensure continued compatibility and updates.

#### Dynatrace Android Gradle plugin

* Gradle version 7.0.2+
* Android Gradle plugin version 7.0+

For more details, check [Dynatrace Android Gradle plugin](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-plugin "Learn how the Dynatrace Android Gradle plugin can auto-instrument your Android application project.").

### Dynatrace OpenKit



| Product | Versions |
| --- | --- |
| [Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | 7, 8, 11, 12 |
| .NET | Core 3.1, 5, 6 |
| .NET Framework | 3.5, 4.6, 4.7, 4.8, 4.8.1 |
| .NET Standard | 2.0 |
| .NET UWP | Supported |
| .NET PCL | 4.5 |
| C/C++ Windows | Visual Studio 2015, 2017, 2019, and 2022 |
| C/C++ Linux | GCC 5.0.0+ or CLang 3.8.0+ |
| Node.js | 14+ |
| JavaScript | ES6+ |

You can view more details on the following reference pages.

* [Dynatrace OpenKit - Javaï»¿](https://github.com/Dynatrace/openkit-java/releases)
* [Dynatrace OpenKit - .NETï»¿](https://github.com/Dynatrace/openkit-dotnet/releases)
* [Dynatrace OpenKit - C/C++ï»¿](https://github.com/Dynatrace/openkit-native#prerequisites)
* [Dynatrace OpenKit - JavaScriptï»¿](https://github.com/Dynatrace/openkit-js)

## Extensions

See [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?filter=all&type=extension&internal_source=doc&internal_medium=link&internal_campaign=cross) for the complete list of technologies supported by [Dynatrace Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.").

## Metric ingestion data sources

| Technologies | Versions |
| --- | --- |
| [StatsD](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Ingest metrics into Dynatrace using OneAgent and the ActiveGate StatsD client.") | All versions supported[1](#fn-technologies-1-def) |

1

Requires OneAgent EEC. Supported on Windows and Linux and the x64 CPU architecture

## Private Synthetic locations

See [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

## Support Levels for 3rd Party Technologies

### Supported

We provide support for any problems directly caused by Dynatrace. Dynatrace has access to this technology and can typically reproduce common problems in-house but an environment may have to be set up on-demand.

### Limited support

Dynatrace provides support for a limited set of functionality for a particular technology. In most cases Dynatrace does not have access to technology that has limited support. For any problems Dynatrace support will be able to help you, if it can reproduce the problem in the fully supported technology that forms basis for the limited support.