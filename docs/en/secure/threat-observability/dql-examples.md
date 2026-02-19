---
title: DQL examples for security data
source: https://www.dynatrace.com/docs/secure/threat-observability/dql-examples
scraped: 2026-02-19T21:16:27.392672
---

# DQL examples for security data

# DQL examples for security data

* Latest Dynatrace
* How-to guide
* Updated on Oct 22, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

The examples below illustrate how to slice and dice [security data](/docs/secure/threat-observability/concepts#security-data "Basic concepts related to Threat Observability") and build powerful and flexible security reports with [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## Query Dynatrace events

### Total number of open vulnerabilities

Get the total number of open, non-muted vulnerabilities in your environment.

**Query example**:

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

**Query result**:

![Open non-muted vulnerabilities](https://dt-cdn.net/images/2023-12-15-11-32-55-1543-ca0c6f47d5.png)

### Total number of critical open vulnerabilities

Get the total number of critical open, non-muted vulnerabilities in your environment.

**Query example**:

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

**Query result**:

![Total number of critical open vulnerabilities](https://dt-cdn.net/images/2023-12-20-13-57-44-1512-b21087af2c.png)

### Total number of open vulnerabilities in a management zone

Get the total number of open, non-muted vulnerabilities in a specific management zone (in this example, `AppSec: UNGUARD`).

**Query example**:

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

**Query result**:

![Open, non-muted vulnerabilities in a management zone](https://dt-cdn.net/images/2023-12-20-13-34-01-1580-01e1dbca61.png)

### Total number of open vulnerabilities with internet exposure

Get the total number of open, non-muted vulnerabilities with public internet exposure in your environment.

**Query example**:

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

**Query result**:

![Total number of open vulnerabilities with public internet exposure](https://dt-cdn.net/images/2023-12-20-14-09-32-1540-05942b1581.png)

### Total number of affected entities

Get the total number of affected entities in your environment.

**Query example**:

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

**Query result**:

![Total number of affected entities](https://dt-cdn.net/images/2023-12-20-14-20-33-1511-7f499653c3.png)

### Total number of affected process groups

Get the total number of affected process groups in your environment.

**Query example**:

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

**Query result**:

![Total number of affected process groups](https://dt-cdn.net/images/2023-12-20-14-27-23-1471-c0f5334716.png)

### Total number of affected entities over time

Get the total number of affected, non-muted entities over time (in three-hour buckets).

**Query example**:

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

**Query result**:

![Total number of affected entities over time](https://dt-cdn.net/images/2023-12-20-14-36-38-1380-7e18f35512.png)

### Total number of hosts related to vulnerabilities

Get the total number of hosts that are indirectly affected by open vulnerabilities in your environment.

**Query example**:

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

**Query result**:

![Total number of hosts related to vulnerabilities](https://dt-cdn.net/images/2023-12-20-16-17-58-1591-f1ab611412.png)

### Open vulnerabilities by risk level

Get a count of open vulnerabilities split by risk levels.

**Query example**:

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

**Query result**:

![Open vulnerabilities by risk level](https://dt-cdn.net/images/2023-12-20-16-05-32-1263-b388e93ee3.png)

### Open vulnerabilities by type

Get a count of open vulnerabilities split by type.

**Query example**:

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

**Query result**:

![Open vulnerabilities by type](https://dt-cdn.net/images/2023-12-20-16-03-28-1755-79c825ba70.png)

### Open vulnerabilities over time

Get the open vulnerability count over time, in three-hour buckets.

**Query example**:

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

**Query result**:

![open vulnerabilities in 3-hr buckets](https://dt-cdn.net/images/2024-06-19-10-00-41-1375-bba6223c8c.png)

### Vulnerabilities on a library

Get the open vulnerabilities on a specific library (in this example, `log4j`).

**Query example**:

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

**Query result**:

![List vulnerabilities on a library](https://dt-cdn.net/images/2023-12-20-15-56-43-1762-c9da6644e4.png)

### Vulnerabilities on a host

Get the open vulnerabilities directly or indirectly affecting a specific host (in this example, `i-05f1305a50721e04d`).

**Query example**:

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

**Query result**:

![Vulnerabilities on a host ](https://dt-cdn.net/images/2023-12-20-15-47-11-1621-799a5d1c04.png)

### Vulnerabilities on an application

Get the open vulnerabilities affecting a specific application (in this example, `www.easytravel.com`).

**Query example**:

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

**Query result**:

![Vulnerabilities on an application](https://dt-cdn.net/images/2024-01-10-06-58-57-1719-5d67b39da3.png)

### Top 10 affected entities by vulnerability count

Get the top 10 affected entities by the number of open vulnerabilities.

**Query example**:

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

**Query result**:

![Top 10 affected entities by vulnerability count](https://dt-cdn.net/images/2024-06-05-14-44-42-1131-5868876889.png)

### Top 10 process groups with owners

Get the top five process groups by the count of open vulnerabilities, with their respective owners.

**Query example**:

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

**Query result**:

![Top 10 process groups with owner teams](https://dt-cdn.net/images/2023-12-20-15-35-41-1624-fb83180f1e.png)

### Hosts related to vulnerabilities on a library with owners

Get the hosts that are indirectly related to open vulnerabilities on a specific library (in this example, `tomcat`), with their respective owners.

**Query example**:

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

**Query result**:

![Hosts related to vulnerabilities on a library with owners](https://dt-cdn.net/images/2023-12-20-15-31-09-1624-16288a4369.png)

### Vulnerable software components of a host with owners

Get the vulnerable components of a specific host (in this example, `HOST-4CF0F659B8823D74`) with owners.

**Query example**:

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

**Query result**:

![Vulnerable software components of a host with owners](https://dt-cdn.net/images/2023-12-20-15-23-11-1617-9be4d95d88.png)

### Vulnerable functions of a software component

Get the vulnerable functions of a specific software component (in this example, `SOFTWARE_COMPONENT-1D466FB7ADEBF92E`).

**Query example**:

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

**Query result**:

![Vulnerable functions of a software component](https://dt-cdn.net/images/2023-12-20-15-13-13-1623-f4c7e8d398.png)

## Query ingested events

### Total number of critical vulnerability findings

Get the total number of critical vulnerability findings ingested into Dynatrace.

**Query example**:

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

**Query result**:

![critical vulnerability findings](https://dt-cdn.net/images/image-20241029-120929-1685-ab662f5f28.png)

### Total number of vulnerable container images

Get the total number of container images containing vulnerability findings ingested into Dynatrace.

**Query example**:

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

**Query result**:

![vulnerable container images](https://dt-cdn.net/images/image-20241029-121235-1638-d550a4b6bc.png)

### Total number of vulnerable components

Get the total number of vulnerable components in the container images containing vulnerability findings ingested into Dynatrace.

**Query example**:

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

**Query result**:

![vulnerable components](https://dt-cdn.net/images/image-20241029-121220-1684-5eeb70313e.png)

### Most recent vulnerability findings

Get the most recent vulnerability findings ingested into Dynatrace.

**Query example**:

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

**Query result**:

![most recent vulnerability findings](https://dt-cdn.net/images/censored3-20241029-145107-1685-c8bb339c99.png)

### Number of scanned container images

Get the total number of ingested container images that have been scanned.

**Query example**:

```
fetch security.events



| filter dt.system.bucket == "default_securityevents"



| filter object.type == "CONTAINER_IMAGE" // includes both SCAN_EVENTS and VULNERABILITY_FINDINGS without scan events



| dedup {container_image.digest}, sort: {timestamp desc}



| summarize {containerImages=count()}
```

**Query result**:

![Number of scanned container images](https://dt-cdn.net/images/image-20241029-121426-1980-ef745c8257.png)

### Number of container image scan events

Get the total number of scan events from ingested container images.

**Query example**:

```
fetch security.events



| filter dt.system.bucket == "default_securityevents"



| filter event.type == "VULNERABILITY_SCAN"



AND object.type == "CONTAINER_IMAGE"



| summarize {scanEvents=count()}
```

**Query result**:

![Number of container image scan events](https://dt-cdn.net/images/image-20241029-121224-1605-37798c4a10.png)

## Query compliance events

### Latest results for all covered systems

Get the latest compliance results of supported standards for all systems [covered by Security Posture Management](/docs/secure/xspm/assess-coverage#coverage "Review the Security Posture Management coverage of your systems at a glance.").

**Query example**:

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

**Query result**:

![Latest results for all covered systems](https://dt-cdn.net/images/2024-11-19-12-00-23-976-c026b0abd7.png)

### Historical compliance results for a standard for all covered systems

Get the historical compliance results for a standard (in this case, DORA) for all systems [covered by Security Posture Management](/docs/secure/xspm/assess-coverage#coverage "Review the Security Posture Management coverage of your systems at a glance.").

**Query example**:

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

**Query result**:

![Historical compliance results of DORA standard for all covered systems](https://dt-cdn.net/images/2024-11-19-12-04-14-1722-f64d652cf3.png)

### Latest analysis results for a system in a selected timeframe

Get the latest analysis results for a given system in a selected timeframe.

This results in a view similar to that displayed in ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** on the **Assessment results** page.

**Query example**:

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

**Query result**:

![Latest analysis results for a given system in selected timeframe](https://dt-cdn.net/images/2025-09-15-15-02-36-1813-5461c4173d.png)

### Historical assessment results for selected rule and system

Get the counts for every assessment that happened in a selected period for a selected rule and system (in this case, `dt-cluster-01`).

**Query example**:

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

**Query result**:

![Historical assessment results for selected rule and system](https://dt-cdn.net/images/2024-11-22-10-22-05-1705-07ef87b89d.png)

### Latest misconfigurations of the object according to a specific standard

Get the counts of the latest misconfigurations of the object (in this case, `ip-10-45-243-57`) for a specific standard (in this case, CIS).

**Query example**:

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

**Query result**:

![Latest misconfigurations for a specific standard](https://dt-cdn.net/images/dql-324-v2-1979-c103989603.png)