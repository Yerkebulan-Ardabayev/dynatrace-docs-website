---
title: Monitoring state API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/monitoring-state
---

# Monitoring state API

# Monitoring state API

* Reference
* Published Oct 01, 2026

The **Monitoring state** API enables you to query the monitoring state of process group instances in your environment. Only process group instances are supported.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/monitoringstate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/monitoringstate` |

## Authentication

### Api-Token:

To execute this request, you need an access token with `entities.read` scope.

To learn how to obtain and use it, see [Personal access tokens](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| entitySelector | string | Specifies the process group instances where you're querying the state. Use the `PROCESS_GROUP_INSTANCE` entity type.  You must set one of these criteria:  * Entity type: `type("TYPE")` * Dynatrace entity ID: `entityId("id")`. You can specify several IDs, separated by a comma (`entityId("id-1","id-2")`). All requested entities must be of the same type.  You can add one or more of the following criteria. Values are case-sensitive and the `EQUALS` operator is used unless otherwise specified.  * Tag: `tag("value")`. Tags in `[context]key:value`, `key:value`, and `value` formats are detected and parsed automatically. Any colons (`:`) that are part of the key or value must be escaped with a backslash(`\`). Otherwise, it will be interpreted as the separator between the key and the value. All tag values are case-sensitive. * Management zone ID: `mzId(123)` * Management zone name: `mzName("value")` * Entity name: + `entityName.equals`: performs a non-casesensitive `EQUALS` query.   + `entityName.startsWith`: changes the operator to `BEGINS WITH`.   + `entityName.in`: enables you to provide multiple values. The `EQUALS` operator applies.   + `caseSensitive(entityName.equals("value"))`: takes any entity name criterion as an argument and makes the value case-sensitive. * Health state (HEALTHY,UNHEALTHY): `healthState("HEALTHY")` * First seen timestamp: `firstSeenTms.<operator>(now-3h)`. Use any timestamp format from the **from**/**to** parameters.   The following operators are available: + `lte`: earlier than or at the specified time   + `lt`: earlier than the specified time   + `gte`: later than or at the specified time   + `gt`: later than the specified time * Entity attribute: `<attribute>("value1","value2")` and `<attribute>.exists()`. To fetch the list of available attributes, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt) request and check the **properties** field of the response. * Relationships: `fromRelationships.<relationshipName>()` and `toRelationships.<relationshipName>()`. This criterion takes an entity selector as an attribute. To fetch the list of available relationships, execute the [GET entity type﻿](https://dt-url.net/2ka3ivt) request and check the **fromRelationships** and **toRelationships** fields. * Negation: `not(<criterion>)`. Inverts any criterion except for **type**.  For more information, see [Entity selector﻿](https://dt-url.net/apientityselector) in Dynatrace Documentation.  To set several criteria, separate them with a comma (`,`). For example, `type("HOST"),healthState("HEALTHY")`. Only results matching **all** criteria are included in the response.  The maximum string length is 2,000 characters. | query | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MonitoredStates](#openapi-definition-MonitoredStates) | Success |
| **503** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Unavailable |

### Response body objects

#### The `MonitoredStates` object

A list of entities and their monitoring states.

| Element | Type | Description |
| --- | --- | --- |
| monitoringStates | [MonitoredEntityStates](#openapi-definition-MonitoredEntityStates)[] | A list of process group instances and their monitoring states. |
| totalCount | integer | The total number of entities in the response. |

#### The `MonitoredEntityStates` object

Monitoring state of the process group instance.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | The Dynatrace entity ID of the process group instance. |
| severity | string | The type of the monitoring state. The element can hold these values * `info` * `ok` * `warning` |
| state | string | The name of the monitoring state. The element can hold these values * `agent_injection_status_go_dynamizer_failed` * `agent_injection_status_go_fips_detected_but_feature_disabled` * `agent_injection_status_go_vertigo_support_added` * `agent_injection_status_nginx_patched_binary_detected` * `agent_injection_status_php_opcache_disabled` * `agent_injection_status_php_stack_size_too_low` * `agent_injection_suppression` * `aix_enable_full_monitoring_needed` * `bad_installer` * `boshbpm_disabled` * `containerd_disabled` * `crio_disabled` * `custom_pg_rule_required` * `deep_monitoring_unsuccessful` * `docker_disabled` * `garden_disabled` * `host_infra_structure_only` * `host_monitoring_disabled` * `network_agent_inactive` * `ok` * `parent_process_restart_required` * `process_group_different_id_due_to_declarative_grouping` * `process_group_disabled` * `process_group_disabled_via_container_injection_rule` * `process_group_disabled_via_container_injection_rule_restart` * `process_group_disabled_via_global_settings` * `process_group_disabled_via_injection_rule` * `process_group_disabled_via_injection_rule_restart` * `process_group_pgr_group_update_suppressed` * `restart_required` * `restart_required_apache` * `restart_required_docker_deamon` * `restart_required_host_group_inconsistent` * `restart_required_host_id_inconsistent` * `restart_required_outdated_agent_apache_update` * `restart_required_outdated_agent_injected` * `restart_required_using_different_data_storage_dir` * `restart_required_using_different_log_path` * `restart_required_virtualized_container` * `unsupported_state` * `winc_disabled` |
| params | [MonitoredEntityStateParam](#openapi-definition-MonitoredEntityStateParam)[] | Additional parameters of the monitoring state. |

#### The `MonitoredEntityStateParam` object

Key-value parameter of the monitoring state.

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of the monitoring state paramter. |
| values | string | The value of the monitoring state paramter. |

### Response body JSON models

```
{



"totalCount": 1,



"monitoringStates": [



{



"states": [



{



"entityId": "PROCESS_GROUP_INSTANCE-F1266E1D0AAC2C3C",



"state": "restart_required_outdated_agent_injected",



"severity": "warning",



"parameters": [



{



"key": "pids",



"value": "111,222,333"



}



]



}



]



}



]



}
```

## Related topics

* [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")