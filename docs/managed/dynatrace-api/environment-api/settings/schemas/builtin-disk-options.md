---
title: Settings API - Disk options schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-disk-options
scraped: 2026-05-12T11:39:04.434862
---

# Settings API - Disk options schema table

# Settings API - Disk options schema table

* Published Dec 05, 2023

### Disk options (`builtin:disk.options)`

Disk options settings control the visibility of local disks on your hosts.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:disk.options` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.options` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:disk.options` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.options` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Show all NFS mount points `nfsShowAll` | boolean | When disabled OneAgent will try to deduplicate some of nfs mount points. Disabled by default, applies only to Linux hosts.  Applies only to Linux hosts | Required |
| Disable NFS disk monitoring `disableNfsDiskMonitoring` | boolean | Deactivate NFS monitoring on all supported systems | Required |
| Enable tmpfs disk monitoring `monitorTmpfs` | boolean | Activate tmpfs monitoring on Linux systems | Required |
| Exclude disks `exclusions` | [DiskComplex](#DiskComplex)[] | OneAgent automatically detects and monitors all your mount points, however you can create exception rules to remove disks from the monitoring list.  Certain filesystems are always excluded as monitoring of them is not useful. For example, autofs, proc, cgroup, tmpfs.  â ï¸ Filtering is done before resolving symbolic links. | Required |

##### The `DiskComplex` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Operating system `os` | enum | The element has these enums * `OS_TYPE_UNKNOWN` * `OS_TYPE_AIX` * `OS_TYPE_DARWIN` * `OS_TYPE_HPUX` * `OS_TYPE_LINUX` * `OS_TYPE_SOLARIS` * `OS_TYPE_WINDOWS` * `OS_TYPE_ZOS` | Required |
| Disk or mount point path `mountpoint` | text | **Disk or mount point path field:** the path to where the disk to be excluded from monitoring is mounted. Examples:  * /mnt/my\_disk * /staff/emp1 * C:\ * /staff/\* * /disk\*  â ï¸ Mount point paths are case sensitive!  The wildcard in **/staff/**\* means to exclude every child folder of /staff.  The wildcard in **/disk**\* means to exclude every mount point starting with /disk, for example /disk1, /disk99, /diskabc  â ï¸ Filtering is done before resolving symbolic links. | Optional |
| File system type `filesystem` | text | **File system type field:** the type of the file system to be excluded from monitoring. Examples:  * ext4 * ext3 * btrfs * ext\*  â ï¸ Starting from **OneAgent 1.299+** file system types are not case sensitive!  The wildcard in the last example means to exclude matching file systems such as types ext4 and ext3 | Optional |