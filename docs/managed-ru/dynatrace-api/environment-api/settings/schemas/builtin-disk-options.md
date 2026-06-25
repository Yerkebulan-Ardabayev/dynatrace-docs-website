---
title: Settings API - Disk options schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-disk-options
scraped: 2026-05-12T11:39:04.434862
---

# Settings API - Disk options schema table

# Settings API - Disk options schema table

* Published Dec 05, 2023

### Параметры диска (`builtin:disk.options)`

Параметры диска управляют видимостью локальных дисков на хостах.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:disk.options` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.options` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:disk.options` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:disk.options` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Показывать все NFS-точки монтирования `nfsShowAll` | boolean | При отключении OneAgent будет пытаться дедуплицировать часть nfs-точек монтирования. По умолчанию отключено, применяется только к Linux-хостам.  Применяется только к Linux-хостам | Required |
| Отключить мониторинг NFS-дисков `disableNfsDiskMonitoring` | boolean | Деактивировать мониторинг NFS на всех поддерживаемых системах | Required |
| Включить мониторинг tmpfs-дисков `monitorTmpfs` | boolean | Активировать мониторинг tmpfs на Linux-системах | Required |
| Исключённые диски `exclusions` | [DiskComplex](#DiskComplex)[] | OneAgent автоматически обнаруживает и мониторит все точки монтирования, при этом можно создавать правила-исключения для удаления дисков из списка мониторинга.  Некоторые файловые системы всегда исключаются, так как их мониторинг бесполезен. Например, autofs, proc, cgroup, tmpfs.  â ï¸ Фильтрация выполняется до разрешения символьных ссылок. | Required |

##### Объект `DiskComplex`

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Операционная система `os` | enum | Возможные значения: * `OS_TYPE_UNKNOWN` * `OS_TYPE_AIX` * `OS_TYPE_DARWIN` * `OS_TYPE_HPUX` * `OS_TYPE_LINUX` * `OS_TYPE_SOLARIS` * `OS_TYPE_WINDOWS` * `OS_TYPE_ZOS` | Required |
| Путь к диску или точке монтирования `mountpoint` | text | **Поле «Путь к диску или точке монтирования»:** путь, по которому смонтирован диск, исключаемый из мониторинга. Примеры:  * /mnt/my\_disk * /staff/emp1 * C:\ * /staff/\* * /disk\*  â ï¸ Пути точек монтирования регистрозависимы!  Wildcard в **/staff/**\* означает исключение каждой дочерней папки /staff.  Wildcard в **/disk**\* означает исключение каждой точки монтирования, начинающейся на /disk, например /disk1, /disk99, /diskabc  â ï¸ Фильтрация выполняется до разрешения символьных ссылок. | Optional |
| Тип файловой системы `filesystem` | text | **Поле «Тип файловой системы»:** тип файловой системы, исключаемой из мониторинга. Примеры:  * ext4 * ext3 * btrfs * ext\*  â ï¸ Начиная с **OneAgent 1.299+** типы файловых систем нечувствительны к регистру!  Wildcard в последнем примере означает исключение совпавших файловых систем, например типов ext4 и ext3 | Optional |