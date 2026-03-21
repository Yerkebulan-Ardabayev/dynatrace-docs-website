---
title: Примеры DQL для данных безопасности
source: https://www.dynatrace.com/docs/secure/threat-observability/dql-examples
scraped: 2026-03-06T21:20:31.345755
---

* Latest Dynatrace
* How-to guide

Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список изменений и действий, необходимых для выполнения миграции, см. в [руководстве по миграции таблицы безопасности Grail](migration.md "Understand the changes in the new Grail security table and learn how to migrate to it.").

Приведённые ниже примеры иллюстрируют, как разрезать [данные безопасности](concepts.md#security-data "Basic concepts related to Threat Observability") и создавать мощные и гибкие отчёты по безопасности с помощью [Dynatrace Query Language (DQL)](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.").

## Запросы к событиям Dynatrace

### Общее количество открытых уязвимостей

Получите общее количество открытых, не отключённых уязвимостей в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status=="OPEN"


AND vulnerability.parent.mute.status!="MUTED"


AND vulnerability.mute.status!="MUTED"


// count unique vulnerabilities


| summarize {`Open vulnerabilities`=countDistinctExact(vulnerability.display_id)}
```

**Результат запроса**:

![Открытые не отключённые уязвимости](https://dt-cdn.net/images/2023-12-15-11-32-55-1543-ca0c6f47d5.png)

### Общее количество критических открытых уязвимостей

Получите общее количество критических открытых, не отключённых уязвимостей в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for critical open non-muted vulnerabilities


| filter vulnerability.resolution.status=="OPEN"


AND vulnerability.parent.mute.status!="MUTED"


AND vulnerability.mute.status!="MUTED"


AND vulnerability.risk.level=="CRITICAL"


// count unique vulnerabilities


| summarize {`Critical open vulnerabilities`=countDistinctExact(vulnerability.display_id)}
```

**Результат запроса**:

![Общее количество критических открытых уязвимостей](https://dt-cdn.net/images/2023-12-20-13-57-44-1512-b21087af2c.png)

### Общее количество открытых уязвимостей в Management Zone

Получите общее количество открытых, не отключённых уязвимостей в определённой Management Zone (в этом примере — `AppSec: UNGUARD`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities in a specific management zone


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


AND in("AppSec: Unguard", affected_entity.management_zones.names)


// count unique vulnerabilities


| summarize {`Open vulnerabilities (unguard)`=countDistinctExact(vulnerability.display_id)}
```

**Результат запроса**:

![Открытые не отключённые уязвимости в Management Zone](https://dt-cdn.net/images/2023-12-20-13-34-01-1580-01e1dbca61.png)

### Общее количество открытых уязвимостей с воздействием через Интернет

Получите общее количество открытых, не отключённых уязвимостей с публичным воздействием через Интернет в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities with public internet exposure


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


AND vulnerability.davis_assessment.exposure_status=="PUBLIC_NETWORK"


// count unique vulnerabilities


| summarize {`With internet exposure`=countDistinctExact(vulnerability.display_id)}
```

**Результат запроса**:

![Общее количество открытых уязвимостей с публичным воздействием через Интернет](https://dt-cdn.net/images/2023-12-20-14-09-32-1540-05942b1581.png)

### Общее количество затронутых объектов

Получите общее количество затронутых объектов в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// count unique entities


| summarize {`Affected entities`=countDistinctExact(affected_entity.id)}
```

**Результат запроса**:

![Общее количество затронутых объектов](https://dt-cdn.net/images/2023-12-20-14-20-33-1511-7f499653c3.png)

### Общее количество затронутых групп процессов

Получите общее количество затронутых групп процессов в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities detected in running processes


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


AND affected_entity.type=="PROCESS_GROUP"


// count unique entities


| summarize {`Affected process groups`=countDistinctExact(affected_entity.id)}
```

**Результат запроса**:

![Общее количество затронутых групп процессов](https://dt-cdn.net/images/2023-12-20-14-27-23-1471-c0f5334716.png)

### Общее количество затронутых объектов во времени

Получите общее количество затронутых, не отключённых объектов во времени (в трёхчасовых интервалах).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for open non-muted vulnerabilities


AND vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// count unique entities for each timestamp bucket of 3h


| sort timestamp desc


| summarize {entities=countDistinctExact(affected_entity.id)}, by: {timestamp=bin(timestamp, 3h)}
```

**Результат запроса**:

![Общее количество затронутых объектов во времени](https://dt-cdn.net/images/2023-12-20-14-36-38-1380-7e18f35512.png)

### Общее количество хостов, связанных с уязвимостями

Получите общее количество хостов, косвенно затронутых открытыми уязвимостями в вашей среде.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


|filter  vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// count hosts


| summarize {`Related hosts`=arraySize(collectDistinct(related_entities.hosts.ids, expand:true))}
```

**Результат запроса**:

![Общее количество хостов, связанных с уязвимостями](https://dt-cdn.net/images/2023-12-20-16-17-58-1591-f1ab611412.png)

### Открытые уязвимости по уровню риска

Получите количество открытых уязвимостей, разбитое по уровням риска.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// summarize score per vulnerability


| summarize {vulnerability.risk.score=takeMax(vulnerability.risk.score)}, by: {vulnerability.display_id}


// map the risk level


| fieldsAdd vulnerability.risk.level=if(vulnerability.risk.score>=9,"CRITICAL",


else:if(vulnerability.risk.score>=7,"HIGH",


else:if(vulnerability.risk.score>=4,"MEDIUM",


else:if(vulnerability.risk.score>=0.1,"LOW",


else:"NONE"))))


// count vulnerabilities per risk level


| summarize { Vulnerabilities=count(), maxScore=takeMax(vulnerability.risk.score) }, by:{vulnerability.risk.level}


| sort maxScore, direction:"descending"
```

**Результат запроса**:

![Открытые уязвимости по уровню риска](https://dt-cdn.net/images/2023-12-20-16-05-32-1263-b388e93ee3.png)

### Открытые уязвимости по типу

Получите количество открытых уязвимостей, разбитое по типам.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// count vulnerabilities per type


| summarize { Vulnerabilities=countDistinctExact(vulnerability.display_id) }, by:{vulnerability.type}


| sort Vulnerabilities, direction:"descending"


| limit 10
```

**Результат запроса**:

![Открытые уязвимости по типу](https://dt-cdn.net/images/2023-12-20-16-03-28-1755-79c825ba70.png)

### Открытые уязвимости во времени

Получите количество открытых уязвимостей во времени, в трёхчасовых интервалах.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for open non-muted vulnerabilities


AND vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


| sort timestamp desc


| summarize {Open=countDistinctExact(vulnerability.display_id)}, by: {timestamp=bin(timestamp,3h)}
```

**Результат запроса**:

![Открытые уязвимости в 3-часовых интервалах](https://dt-cdn.net/images/2024-06-19-10-00-41-1375-bba6223c8c.png)

### Уязвимости в библиотеке

Получите открытые уязвимости в конкретной библиотеке (в этом примере — `log4j`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// filter by the vulnerable library/component name


AND contains(affected_entity.vulnerable_component.name,"log4j",caseSensitive:false)


// now summarize on the vulnerability level


| summarize{


vulnerability.risk.score=round(takeMax(vulnerability.risk.score),decimals:1),


vulnerability.title=takeFirst(vulnerability.title),


vulnerability.references.cve=takeFirst(vulnerability.references.cve),


last_detected=coalesce(takeMax(vulnerability.resolution.change_date),takeMax(vulnerability.parent.first_seen)),


affected_entities=countDistinctExact(affected_entity.id),


vulnerable_function_in_use=if(in("IN_USE",collectArray(vulnerability.davis_assessment.vulnerable_function_status)),true, else:false),


public_internet_exposure=if(in("PUBLIC_NETWORK",collectArray(vulnerability.davis_assessment.exposure_status)),true,else:false),


public_exploit_available=if(in("AVAILABLE",collectArray(vulnerability.davis_assessment.exploit_status)),true,else:false),


data_assets_within_reach=if(in("REACHABLE",collectArray(vulnerability.davis_assessment.data_assets_status)),true,else:false)


}, by: {vulnerability.display_id}


// map the risk level


| fieldsAdd vulnerability.risk.level=if(vulnerability.risk.score>=9,"CRITICAL",


else:if(vulnerability.risk.score>=7,"HIGH",


else:if(vulnerability.risk.score>=4,"MEDIUM",


else:if(vulnerability.risk.score>=0.1,"LOW",


else:"NONE"))))


| sort   {vulnerability.risk.score, direction:"descending"}, {affected_entities, direction:"descending"}
```

**Результат запроса**:

![Список уязвимостей в библиотеке](https://dt-cdn.net/images/2023-12-20-15-56-43-1762-c9da6644e4.png)

### Уязвимости на хосте

Получите открытые уязвимости, напрямую или косвенно затрагивающие конкретный хост (в этом примере — `i-05f1305a50721e04d`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// filter by the host name of the related/affected host


AND in("easytravel-demo2",related_entities.hosts.names) OR affected_entity.name=="easytravel-demo2"


// now summarize on the vulnerability level


| summarize{


vulnerability.risk.score=round(takeMax(vulnerability.risk.score),decimals:1),


vulnerability.title=takeFirst(vulnerability.title),


vulnerability.references.cve=takeFirst(vulnerability.references.cve),


last_detected=coalesce(takeMax(vulnerability.resolution.change_date),takeMax(vulnerability.parent.first_seen)),


affected_entities=countDistinctExact(affected_entity.id),


vulnerable_function_in_use=if(in("IN_USE",collectArray(vulnerability.davis_assessment.vulnerable_function_status)),true, else:false),


public_internet_exposure=if(in("PUBLIC_NETWORK",collectArray(vulnerability.davis_assessment.exposure_status)),true,else:false),


public_exploit_available=if(in("AVAILABLE",collectArray(vulnerability.davis_assessment.exploit_status)),true,else:false),


data_assets_within_reach=if(in("REACHABLE",collectArray(vulnerability.davis_assessment.data_assets_status)),true,else:false)


}, by: {vulnerability.display_id}


// map the risk level


| fieldsAdd vulnerability.risk.level=if(vulnerability.risk.score>=9,"CRITICAL",


else:if(vulnerability.risk.score>=7,"HIGH",


else:if(vulnerability.risk.score>=4,"MEDIUM",


else:if(vulnerability.risk.score>=0.1,"LOW",


else:"NONE"))))


| sort {vulnerability.risk.score, direction:"descending"}, {affected_entities, direction:"descending"}
```

**Результат запроса**:

![Уязвимости на хосте](https://dt-cdn.net/images/2023-12-20-15-47-11-1621-799a5d1c04.png)

### Уязвимости в приложении

Получите открытые уязвимости, затрагивающие конкретное приложение (в этом примере — `www.easytravel.com`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// filter by name of the related applications


AND in("www.easytravel.com",related_entities.applications.names)


// now summarize on the vulnerability level


| summarize{


vulnerability.risk.score=round(takeMax(vulnerability.risk.score),decimals:1),


vulnerability.title=takeFirst(vulnerability.title),


vulnerability.references.cve=takeFirst(vulnerability.references.cve),


last_detected=coalesce(takeMax(vulnerability.resolution.change_date),takeMax(vulnerability.parent.first_seen)),


affected_entities=countDistinctExact(affected_entity.id),


vulnerable_function_in_use=if(in("IN_USE",collectArray(vulnerability.davis_assessment.vulnerable_function_status)),true, else:false),


public_internet_exposure=if(in("PUBLIC_NETWORK",collectArray(vulnerability.davis_assessment.exposure_status)),true,else:false),


public_exploit_available=if(in("AVAILABLE",collectArray(vulnerability.davis_assessment.exploit_status)),true,else:false),


data_assets_within_reach=if(in("REACHABLE",collectArray(vulnerability.davis_assessment.data_assets_status)),true,else:false)


}, by: {vulnerability.display_id}


// map the risk level


| fieldsAdd vulnerability.risk.level=if(vulnerability.risk.score>=9,"CRITICAL",


else:if(vulnerability.risk.score>=7,"HIGH",


else:if(vulnerability.risk.score>=4,"MEDIUM",


else:if(vulnerability.risk.score>=0.1,"LOW",


else:"NONE"))))


| sort   {vulnerability.risk.score, direction:"descending"}, {affected_entities, direction:"descending"}
```

**Результат запроса**:

![Уязвимости в приложении](https://dt-cdn.net/images/2024-01-10-06-58-57-1719-5d67b39da3.png)

### Топ-10 затронутых объектов по количеству уязвимостей

Получите топ-10 затронутых объектов по количеству открытых уязвимостей.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


| summarize {


`Affected entity name` = takeFirst(affected_entity.name),


Type = takeFirst(affected_entity.type),


Vulnerabilities = countDistinctExact(vulnerability.display_id)


}, by: {dt.source_entity=affected_entity.id}


| sort {Vulnerabilities, direction:"descending"}


| limit 10
```

**Результат запроса**:

![Топ-10 затронутых объектов по количеству уязвимостей](https://dt-cdn.net/images/2024-06-05-14-44-42-1131-5868876889.png)

### Топ-10 групп процессов с владельцами

Получите топ-10 групп процессов по количеству открытых уязвимостей с соответствующими владельцами.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


AND affected_entity.type=="PROCESS_GROUP"


// summarize per process group


| summarize {


`Affected entity name` = takeFirst(affected_entity.name),


Type = takeFirst(affected_entity.type),


Vulnerabilities = countDistinctExact(vulnerability.display_id)


}, by: {dt.source_entity=affected_entity.id}


| sort {Vulnerabilities, direction:"descending"}


| limit 10


// add ownership information


| lookup [


fetch dt.entity.process_group


| parse toString(tags), "LD ('owner:'|'owner\\\\:') (SPACE)? LD:Team ('\"')"


| fields id, Team=coalesce(Team, "-")


], sourceField:dt.source_entity, lookupField:id, fields:{Team}


| sort Vulnerabilities, direction:"descending"
```

**Результат запроса**:

![Топ-10 групп процессов с командами-владельцами](https://dt-cdn.net/images/2023-12-20-15-35-41-1624-fb83180f1e.png)

### Хосты, связанные с уязвимостями в библиотеке, с владельцами

Получите хосты, косвенно связанные с открытыми уязвимостями в конкретной библиотеке (в этом примере — `tomcat`), с соответствующими владельцами.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


AND related_entities.hosts.count > 0


// filter by the vulnerable component name


AND contains(affected_entity.vulnerable_component.name,"tomcat")


| expand entity_id=related_entities.hosts.ids


| summarize Vulnerabilities=countDistinctExact(vulnerability.display_id), by: {entity_id}


//add ownership information


| lookup [


fetch dt.entity.host


| parse toString(tags), "LD ('owner:'|'owner\\\\:') (SPACE)? LD:Team ('\"')"


| fields id, Host=entity.name, Team=coalesce(Team, "-")


], sourceField:entity_id, lookupField:id, fields: {Host,Team}


| sort Vulnerabilities, direction:"descending"
```

**Результат запроса**:

![Хосты, связанные с уязвимостями в библиотеке, с владельцами](https://dt-cdn.net/images/2023-12-20-15-31-09-1624-16288a4369.png)

### Уязвимые программные компоненты хоста с владельцами

Получите уязвимые компоненты конкретного хоста (в этом примере — `HOST-4CF0F659B8823D74`) с владельцами.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// filter by ID of the related or affected host


AND in("HOST-DBF63A01C27E4B50",related_entities.hosts.ids) or affected_entity.id=="HOST-DBF63A01C27E4B50"


| summarize{


entities=countDistinctExact(affected_entity.id),


vulnerable_functions=arraySize(collectDistinct(affected_entity.vulnerable_functions, expand:true)),


vulnerable_component.name=takeAny(affected_entity.vulnerable_component.name)


}, by: {dt.entity.software_component=affected_entity.vulnerable_component.id}


| filterOut isNull(dt.entity.software_component)


// add component information


| lookup [


fetch dt.entity.software_component


| fieldsAdd softwareComponentFileName


], sourceField:dt.entity.software_component, lookupField:id, fields:{softwareComponentFileName}


| fields dt.entity.software_component, vulnerable_component.name, softwareComponentFileName, entities, vulnerable_functions


| sort {entities, direction:"descending"}, {vulnerable_functions, direction:"descending"}
```

**Результат запроса**:

![Уязвимые программные компоненты хоста с владельцами](https://dt-cdn.net/images/2023-12-20-15-23-11-1617-9be4d95d88.png)

### Уязвимые функции программного компонента

Получите уязвимые функции конкретного программного компонента (в этом примере — `SOFTWARE_COMPONENT-1D466FB7ADEBF92E`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket=="default_securityevents_builtin"


AND event.provider=="Dynatrace"


AND event.type=="VULNERABILITY_STATE_REPORT_EVENT"


AND event.level=="ENTITY"


// filter for the latest snapshot per entity


| dedup {vulnerability.display_id, affected_entity.id}, sort:{timestamp desc}


// filter for open non-muted vulnerabilities


| filter vulnerability.resolution.status == "OPEN"


AND vulnerability.parent.mute.status != "MUTED"


AND vulnerability.mute.status != "MUTED"


// filter for the software component ID


AND affected_entity.vulnerable_component.id=="SOFTWARE_COMPONENT-1D466FB7ADEBF92E"


| expand vulnerable_function=affected_entity.vulnerable_functions


| filter isNotNull(vulnerable_function)


| summarize{Usages=countIf(in(vulnerable_function,affected_entity.vulnerable_functions))}, by: {vulnerable_function}


| sort {Usages, direction:"descending"}
```

**Результат запроса**:

![Уязвимые функции программного компонента](https://dt-cdn.net/images/2023-12-20-15-13-13-1623-f4c7e8d398.png)

## Запросы к загружаемым событиям

### Общее количество критических результатов анализа уязвимостей

Получите общее количество критических результатов анализа уязвимостей, загруженных в Dynatrace.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents"


AND event.type == "VULNERABILITY_FINDING"


AND isNotNull(component.name)


// latest findings per affected object, vulnerability and component


| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}


// aggregation and custom filtering


| filter dt.security.risk.level=="CRITICAL"


| summarize {Vulnerabilities=countDistinctExact(vulnerability.id)}
```

**Результат запроса**:

![Критические результаты анализа уязвимостей](https://dt-cdn.net/images/image-20241029-120929-1685-ab662f5f28.png)

### Общее количество уязвимых образов контейнеров

Получите общее количество образов контейнеров, содержащих результаты анализа уязвимостей, загруженные в Dynatrace.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents"


AND event.type == "VULNERABILITY_FINDING"


AND isNotNull(component.name)


// latest findings per affected object, vulnerability and component


| dedup {object.id, vulnerability.id, component.name, component.version,


container_image.registry, container_image.repository, container_image.tags}, sort: {timestamp desc}


// aggregation and custom filtering


| summarize {containerImages=countDistinctExact(container_image.digest)}
```

**Результат запроса**:

![Уязвимые образы контейнеров](https://dt-cdn.net/images/image-20241029-121235-1638-d550a4b6bc.png)

### Общее количество уязвимых компонентов

Получите общее количество уязвимых компонентов в образах контейнеров, содержащих результаты анализа уязвимостей, загруженные в Dynatrace.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents"


AND event.type == "VULNERABILITY_FINDING"


AND isNotNull(component.name)


// latest findings per affected object, vulnerability and component


| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}


// aggregation and custom filtering


| summarize {components=countDistinctExact(component.name)}
```

**Результат запроса**:

![Уязвимые компоненты](https://dt-cdn.net/images/image-20241029-121220-1684-5eeb70313e.png)

### Последние результаты анализа уязвимостей

Получите последние результаты анализа уязвимостей, загруженные в Dynatrace.

**Пример запроса**:

```
fetch security.events


// data access


| filter dt.system.bucket == "default_securityevents"


AND event.type == "VULNERABILITY_FINDING"


AND isNotNull(component.name)


// latest findings per affected object, vulnerability and component


| dedup {object.id, vulnerability.id, component.name, component.version}, sort: {timestamp desc}


| sort timestamp desc
```

**Результат запроса**:

![Последние результаты анализа уязвимостей](https://dt-cdn.net/images/censored3-20241029-145107-1685-c8bb339c99.png)

### Количество проверенных образов контейнеров

Получите общее количество загруженных образов контейнеров, которые были проверены.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents"


| filter object.type == "CONTAINER_IMAGE" // includes both SCAN_EVENTS and VULNERABILITY_FINDINGS without scan events


| dedup {container_image.digest}, sort: {timestamp desc}


| summarize {containerImages=count()}
```

**Результат запроса**:

![Количество проверенных образов контейнеров](https://dt-cdn.net/images/image-20241029-121426-1980-ef745c8257.png)

### Количество событий сканирования образов контейнеров

Получите общее количество событий сканирования из загруженных образов контейнеров.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents"


| filter event.type == "VULNERABILITY_SCAN"


AND object.type == "CONTAINER_IMAGE"


| summarize {scanEvents=count()}
```

**Результат запроса**:

![Количество событий сканирования образов контейнеров](https://dt-cdn.net/images/image-20241029-121224-1605-37798c4a10.png)

## Запросы к событиям соответствия требованиям

### Последние результаты для всех охваченных систем

Получите последние результаты соответствия поддерживаемым стандартам для всех систем, [охваченных Security Posture Management](../xspm/assess-coverage.md#coverage "Review the Security Posture Management coverage of your systems at a glance.").

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_SCAN_COMPLETED"


// filter for the latest assessment


| dedup {object.name}, sort:{timestamp desc}


// parse the compliance percentage from json


| parse `scan.result.summary_json`, """JSON{JSON_ARRAY{JSON{ STRING:standardCode, INT:compliancePercentage }}:standardResultSummaries}(flat=true)"""


| expand standardResultSummaries


| fieldsFlatten standardResultSummaries


| fields timestamp, object.name, standard = standardResultSummaries.standardCode, compliance = standardResultSummaries.compliancePercentage
```

**Результат запроса**:

![Последние результаты для всех охваченных систем](https://dt-cdn.net/images/2024-11-19-12-00-23-976-c026b0abd7.png)

### Исторические результаты соответствия стандарту для всех охваченных систем

Получите исторические результаты соответствия стандарту (в данном случае DORA) для всех систем, [охваченных Security Posture Management](../xspm/assess-coverage.md#coverage "Review the Security Posture Management coverage of your systems at a glance.").

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_SCAN_COMPLETED"


// parse the compliance percentage from json


| parse `scan.result.summary_json`, """JSON{JSON_ARRAY{JSON{ STRING:standardCode, INT:compliancePercentage }}:standardResultSummaries}(flat=true)"""


| expand standardResultSummaries


| fieldsFlatten standardResultSummaries


// filter for the specific standard


| filter standardResultSummaries.standardCode == "DORA"


| fields timestamp, object.name, standardResultSummaries.compliancePercentage
```

**Результат запроса**:

![Исторические результаты соответствия стандарту DORA для всех охваченных систем](https://dt-cdn.net/images/2024-11-19-12-04-14-1722-f64d652cf3.png)

### Последние результаты анализа для системы в выбранном временном интервале

Получите последние результаты анализа для конкретной системы в выбранном временном интервале.

Это даёт представление, аналогичное отображаемому в ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** на странице **Assessment results**.

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_FINDING"


// filter for the latest rule assessment results in the timeframe


| join [


fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_SCAN_COMPLETED"


// filter for desired system


AND object.name == "demo-kspm"


| dedup object.name, sort: { timestamp desc }


| fields scan.id


], on: {scan.id}


// summarize findings on rule level


| summarize {


compliance.rule.severity.level = takeFirst(compliance.rule.severity.level),


compliance.standard.short_name = takeFirst(compliance.standard.short_name),


compliance.rule.title = takeFirst(compliance.rule.title),


compliance.standard.url = takeFirst(compliance.standard.url),


finding.time.created = takeFirst(finding.time.created),


compliance.result.count.passed = countIf(compliance.result.status.level == "PASSED"),


compliance.result.count.failed = countIf(compliance.result.status.level == "FAILED"),


compliance.result.count.manual = countIf(compliance.result.status.level == "MANUAL"),


compliance.result.count.not_relevant = countIf(compliance.result.status.level == "NOT_RELEVANT"),


compliance.rule.metadata_json = takeFirst(compliance.rule.metadata_json)


},


by: { compliance.rule.id }


// add rule level status


| fieldsAdd compliance.result.status.level =


if(compliance.result.count.failed > 0, "FAILED",


else: if(compliance.result.count.manual > 0, "MANUAL",


else: if(compliance.result.count.passed > 0, "PASSED",


else: "NOT_RELEVANT"


)))


| filterout compliance.result.status.level == "NOT_RELEVANT"
```

**Результат запроса**:

![Последние результаты анализа для конкретной системы в выбранном временном интервале](https://dt-cdn.net/images/2025-09-15-15-02-36-1813-5461c4173d.png)

### Исторические результаты оценки для выбранного правила и системы

Получите счётчики для каждой оценки, проведённой в выбранный период, для выбранного правила и системы (в данном случае — `dt-cluster-01`).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_FINDING"


AND k8s.cluster.name == "dt-cluster-01"


// filter for the specific rule


AND compliance.rule.id == "DORA-67950"


// summarize findings on rule level


| summarize {


timestamp = takeFirst(timestamp),


Passed=countIf(compliance.result.status.level == "PASSED"),


Failed=countIf(compliance.result.status.level == "FAILED"),


Manual=countIf(compliance.result.status.level == "MANUAL")


}, by: {scan.id}


| makeTimeseries avg(Passed), avg(Failed), avg(Manual)
```

**Результат запроса**:

![Исторические результаты оценки для выбранного правила и системы](https://dt-cdn.net/images/2024-11-22-10-22-05-1705-07ef87b89d.png)

### Последние несоответствия объекта согласно конкретному стандарту

Получите счётчики последних несоответствий объекта (в данном случае — `ip-10-45-243-57`) для конкретного стандарта (в данном случае — CIS).

**Пример запроса**:

```
fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_FINDING"


// filter for desired object


AND object.name == "ip-10-45-243-57"


// filter for compliance findings reporting misconfigurations


AND compliance.result.status.level == "FAILED"


// filter for the specific standard


AND compliance.standard.short_name == "CIS"


// filter for the latest rule assessment results in the timeframe


| join [


fetch security.events


| filter dt.system.bucket == "default_securityevents_builtin"


AND event.type == "COMPLIANCE_SCAN_COMPLETED"


// filter for desired system


AND object.name == "demo-kspm"


| dedup object.name, sort: { timestamp desc }


| fields scan.id


], on: {scan.id}
```

**Результат запроса**:

![Последние несоответствия для конкретного стандарта](https://dt-cdn.net/images/dql-324-v2-1979-c103989603.png)
