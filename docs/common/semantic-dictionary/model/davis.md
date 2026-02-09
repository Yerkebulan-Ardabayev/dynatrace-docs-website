---
title: "Davis AI"
source: https://docs.dynatrace.com/docs/semantic-dictionary/model/davis
updated: 2026-02-09
---

# Davis AI

# Davis AI

* Latest Dynatrace
* Reference
* Published Feb 03, 2026

Davis events represent different types of individual incidents, such as metric-threshold breaches, baseline degradations, or point-in-time events, such as process crashes. Dynatrace also detects and processes informational events such as new software deployments, configuration changes, and other event types.

A Davis problem may result from a single event or multiple events, which is often the case in complex environments. To prevent a flood of seemingly unrelated problem alerts for related events in such environments, the Dynatrace AI correlates all events that share the exact root cause into a single, trackable problem. This approach prevents event and alert spamming.

Problems have defined lifespans and are updated in real time with all incoming events and findings. Once a problem is detected, it's listed on your problems feed.

## Davis Event Reports

Davis event reports create, update, refresh, or close events within the Davis system.
These reports are uniquely identified and linked through their event.name, event.type, and dt.source\_entity.
This linkage ensures that identical identifiers contribute to a singular event.
A new event is generated in the absence of a matching existing event,
while a matching event triggers an update to reflect the latest information.

Davis events are enriched with additional fields, as detailed in the Davis event model documentation.

Event reports can be created through various methods, including direct creation via the REST API.
Additionally, features like metric events or log events autonomously generate these reports.
These features also offer customization capabilities through event templates.

### Event

This section contains general event information that can be set on an event report or an event template.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.analysis.offset` | duration | experimental A time duration that defines one end of the analysis window relative to `event.start`. If positive, the analysis window spans from the `event.start` to `event.start` plus the offset. If negative, the window spans from `event.start` minus the offset up to `event.start`. If missing, no analysis window was required for event creation, or no information about the analysis window is provided. | `5m`; `-5m` |
| `dt.query` | string | experimental A DQL query associated with the event, see [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). If the query returns time series data, the time series is charted in the event details in the Problems app. | `timeseries avg(dt.host.cpu.idle)` |
| `dt.smartscape.__type__` | smartscapeId | resource stable A Smartscape ID that can be used to query entities from the Smartscape storage. `__type__` is a placeholder for any Smartscape type. Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F` |
| `dt.smartscape_source.id` | smartscapeId | resource experimental The ID of the entity considered the source of the signal. The string represents an entity ID of an entity that is stored in the Smartscape storage. [1](#fn-1-1-def) Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F`; `AWS_LAMBDA_FUNCTION-E0D8F94D9065F24F` |
| `dt.smartscape_source.type` | string | resource stable The entity type of the entity whose identifier is held in dt.smartscape\_source.id. | `K8S_CLUSTER`; `AWS_LAMBDA_FUNCTION` |
| `dt.source_entity` | string[] | resource stable The IDs of the entities considered as the sources of the signal. The strings represent the entity IDs of entities that are stored in the classic entity storage. [2](#fn-1-2-def) Tags: `entity-id` | `['HOST-E0D8F94D9065F24F', 'PROCESS_GROUP_INSTANCE-E0D8F94D9065F24F']` |
| `event.description` | string | stable Human-readable description of an event. | `The current response time (11 s) exceeds the auto-detected baseline (767 ms) by 1,336 %` |
| `event.end` | string | stable The event end timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). If not set, `event.start` plus `dt.davis.timeout` is used. | `16481073970000` |
| `event.group_label` | string | experimental Group label of an event. | `Availability` |
| `event.name` | string | stable The human readable display name of an event type. | `CPU saturation`; `User action duration degradation` |
| `event.start` | string | stable The event start timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). If not set, the current timestamp is used.    For events created based on a sliding window with enough violating slots, `event.start` should be the timestamp of the first violating slot.    Depending on the event type, the start time must not lie in the past more than 6 hours for problem-opening events and 30 days for info events.    Depending on the event type, the start time must not lie in the future more than 5 minutes for problem-opening events and 7 days for info events.    Events that can be sent up to 7 days in the future:  \* `CUSTOM_ANNOTATION`  \* `CUSTOM_CONFIGURATION`  \* `CUSTOM_DEPLOYMENT`  \* `CUSTOM_INFO`  \* `MARKED_FOR_TERMINATION`  \* `WARNING` | `16481073970000` |
| `event.status` | string | stable Controls the event lifecycle: `ACTIVE` creates or updates the active event; `CLOSED` closes the active event â if none exists, no event is created. | `ACTIVE`; `CLOSED` |
| `event.type` | string | stable The unique type identifier of a given event. Must be one of: \* `AVAILABILITY_EVENT` \* `PERFORMANCE_EVENT` \* `RESOURCE_CONTENTION_EVENT` \* `ERROR_EVENT` \* `CUSTOM_ALERT` \* `CUSTOM_ANNOTATION` \* `CUSTOM_CONFIGURATION` \* `CUSTOM_DEPLOYMENT` \* `CUSTOM_INFO` \* `MARKED_FOR_TERMINATION` \* `WARNING` Tags: `permission` | `AVAILABILITY_EVENT`; `CUSTOM_ALERT`; `CUSTOM_ANNOTATION`; `CUSTOM_CONFIGURATION`; `CUSTOM_DEPLOYMENT`; `CUSTOM_INFO`; `ERROR_EVENT`; `MARKED_FOR_TERMINATION`; `PERFORMANCE_EVENT`; `RESOURCE_CONTENTION_EVENT` |

1

The value of this field will be based on one of `dt.smartscape.<type>` fields value. That means that both fields `dt.smartscape_source.id` and `dt.smartscape.<type>` will be set to the same ID.

2

The value of this field will be based on one of the `dt.entity.<type>` fields value. This means that both `dt.source_entity` and `dt.entity.<type>` fields will be set to the same ID.

### Davis event report config fields

This section contains Davis-specific fields that influence the Davis routine on an event report or an event template.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.analysis.offset` | duration | experimental A time duration that defines one end of the analysis window relative to `event.start`. If positive, the analysis window spans from the `event.start` to `event.start` plus the offset. If negative, the window spans from `event.start` minus the offset up to `event.start`. If missing, no analysis window was required for event creation, or no information about the analysis window is provided. | `5m`; `-5m` |
| `dt.davis.analysis_time_budget` | long | stable The time budget (in seconds) that the DavisÂ® engine is granted before it must raise a problem. The analysis time budget can be set per event and controls the balance of sending out alerts early and granting the AI analysis enough time to finish its analysis. The trade-off of a short analysis budget is that the root cause and event merge analysis is limited or even skipped. For example, the time budget of 0 seconds means that the event raises a problem and sends the alert immediately, without any analysis. |  |
| `dt.davis.analysis_trigger_delay` | long | stable The time delay (in seconds) before the trigger of DavisÂ® analysis. For example, the delay of 0 seconds triggers a DavisÂ® problem and the root cause analysis immediately. The trigger delay can be used to hold the analysis until all the relevant root cause data has arrived to Dynatrace. For example, it might be beneficial for cloud integrations or log integrations that report data in different schedulesâ you can delay the analysis until data from all sources is available. Note that while longer delays mean more data is available for root cause analysis, they also delay the delivery of alerts.    Attention: When sent as an event report, the value is in seconds. In Grail, the value is represented in milliseconds. |  |
| `dt.davis.is_entity_remapping_allowed` | boolean | stable This flag defines whether the remapping of the target entity is enabled (true) or disabled (false). If the remapping is enabled, Dynatrace can map the event to an entity extracted from the event metadata. If the remapping is disabled or the extraction is not possible, Dynatrace maps the event to the entity specified in the event configuration (for example, a specific host) or to the global environment entity. |  |
| `dt.davis.is_frequent_issue_detection_allowed` | boolean | stable The flag controls whether the DavisÂ® engine should detect frequent issues. If the flag is set to true, events identified as frequent won't be triggered or merged into a problem. If the flag is set to false, frequent issues won't be detected and events will be triggered and merged as normal. |  |
| `dt.davis.is_merging_allowed` | boolean | stable This flag controls whether the DavisÂ® engine is allowed to merge this event into a larger problem (true) or if a new problem must be created (false). By default, merging is allowed, except for the event type `CUSTOM_ALERT`, where it is by default not allowed. |  |
| `dt.davis.is_problem_suppressed` | boolean | stable This flag controls whether the DavisÂ® engine suppresses the problem from showing up in the web UI and sending notifications. |  |
| `dt.davis.is_rootcause_relevant` | boolean | stable This flag controls whether the DavisÂ® engine should include this event within the root cause analysis (true) or if it is not (false) relevant. |  |
| `dt.davis.preferred_entity_type` | string | stable The preferred classic entity type for remapping. You can find possible values in the classic Dynatrace web UI under Settings > Topology model > Generic types. If the remapping (dt.event.allow\_entity\_remapping) is enabled, this property defines the entity type to which the event should be mapped. If no entity of the preferred type is extracted, no remapping is applied. | `my.custom.entity.type` |
| `dt.davis.timeout` | long | stable The event timeout period (in minutes). If not set, 15 is used. The timeout will automatically be capped to a maximum of 360 minutes (6 hours).    Various event sources use this event property to keep an event active by regularly refreshing an initial event. The timeout defines how fast the event source must refresh an event to keep it active. To keep the event active, the event source must send the refresh within the timeout period. If no refresh is sent, the event is automatically closed by Dynatrace after the timeout period.   Note that metric sources use their own configurable de-alerting windows to close events. Setting the timeout shorter than the de-alerting window will force events to close and increase the risk of false-positive alerts. |  |
| `dt.event.correlation_tag` | string | experimental Set this tag to control which event reports connect together. This value is combined with internal system fieldsâsuch as event.name, dt.source\_entity, and event.providerâto generate a unique correlation ID for event tracking. The final correlation ID that's used for connecting event reports is stored in dt.event.correlation\_id. | `custom correlation tags` |

## Davis Events

Every Davis event update is exported to Grail.
This includes updates that only refresh the event, which is guaranteed to be at least 1 update every 6 hours.

Events are essential raw data that Davis (the Dynatrace AI engine) considers during automated root-cause analysis to understand the reasons underlying any problems that are detected in your environment. Out of the box, Davis detects more than 80 different built-in system event types, including process crashes, deployment configuration changes, and VM motion events. Using extension points, you can report custom events through OneAgent plugins or via the Dynatrace API.

Davis shows all system events in the context of your data center topology. So you can analyze events in relation to their parent topological components (for example, hosts, processes, or services) and see how they relate to one another.

### Query

Searches for all Davis events.

```
fetch dt.davis.events
```

### Event

This section contains general event information.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.query` | string | experimental A DQL query associated with the event, see [Dynatrace Query Langauge](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). | `timeseries avg(dt.host.cpu.idle)` |
| `dt.smartscape_source.id` | smartscapeId | resource experimental The ID of the entity considered the source of the signal. The string represents an entity ID of an entity that is stored in the Smartscape storage. [1](#fn-2-1-def) Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F`; `AWS_LAMBDA_FUNCTION-E0D8F94D9065F24F` |
| `dt.smartscape_source.type` | string | resource stable The entity type of the entity whose identifier is held in dt.smartscape\_source.id. | `K8S_CLUSTER`; `AWS_LAMBDA_FUNCTION` |
| `dt.source_entity` | string[] | resource stable The IDs of the entities considered as the sources of the signal. The strings represent the entity IDs of entities that are stored in the classic entity storage. [2](#fn-2-2-def) Tags: `entity-id` | `['HOST-E0D8F94D9065F24F', 'PROCESS_GROUP_INSTANCE-E0D8F94D9065F24F']` |
| `dt.source_entity.type` | string | resource stable The entity type of the entity whose identifier is held in dt.source\_entity. The value must be a valid entity type and consistent with `dt.source_entity`. Note, however, that the type identifiers are expected to be lowercased in alignment with suffixes of dt.entity.\* keys. | `host`; `process_group_instance`; `cloud:azure:resource_group` |
| `event.category` | string | stable Standard categorization based on the significance of an event (similar to the severity level in the previous Dynatrace). | `INFO`; `AVAILABILITY`; `ERROR`; `SLOWDOWN`; `RESOURCE_CONTENTION`; `CUSTOM_ALERT`; `MONITORING_UNAVAILABLE` |
| `event.description` | string | stable Human-readable description of an event. | `The current response time (11 s) exceeds the auto-detected baseline (767 ms) by 1,336 %` |
| `event.end` | string | stable The event end timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). | `16481073970000` |
| `event.group_label` | string | experimental Group label of an event. | `Availability` |
| `event.id` | string | stable Unique identifier string of an event; is stable across multiple refreshes and updates. | `5547782627070661074_1647601320000` |
| `event.kind` | string | stable Gives high-level information about what kind of information the event contains without being specific about the contents of the event. It helps to determine the record type of a raw event. Tags: `permission` | `DAVIS_EVENT` |
| `event.name` | string | stable The human readable display name of an event type. | `CPU saturation`; `User action duration degradation` |
| `event.provider` | string | stable Source of the event, for example, the name of the component or system that generated the event. Tags: `permission` | `AVAILABILITY`; `LOG_EVENTS`; `METRIC_EVENTS`; `SYNTHETIC`; `EVENTS_REST_API_INGEST`; `KUBERNETES_ANOMALY_DETECTION`; `AGENT_LOCAL_REST_API_INGEST` |
| `event.start` | string | stable The event start timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). This is different from the timestamp even for the first record, as event sources require some time to analyze the underlying data, so the time when an event update is created (`timestamp`) differs from the time when the event started (`event.start`).    For events created based on a sliding window with enough violating slots, `event.start` should be the timestamp of the first violating slot. | `16481073970000` |
| `event.status` | string | stable Status of an event as being either Active or Closed. | `Active` |
| `event.status_transition` | string | experimental An enum that shows the transition of the above event state. | `CREATED`; `UPDATED`; `REFRESHED`; `TIMED_OUT`; `RECOVERED` |
| `event.type` | string | stable The unique type identifier of a given event. Tags: `permission` | `APPLICATION_SLOWDOWN`; `AVAILABILITY_EVENT` |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the event originated, typically when the source created it. If no original timestamp is available, it will be populated at ingest time and required for all events. In the case of a correlated event (for example, ITIL events), this time could be different from the event.start time, as this time represents the actual timestamp when the "update" for the event was created. | `1649822520123123123` |

1

The value of this field will be based on one of `dt.smartscape.<type>` fields value. That means that both fields `dt.smartscape_source.id` and `dt.smartscape.<type>` will be set to the same ID.

2

The value of this field will be based on one of the `dt.entity.<type>` fields value. This means that both `dt.source_entity` and `dt.entity.<type>` fields will be set to the same ID.

### Davis event config fields

This section contains fields that influence the Davis routine.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.analysis.offset` | duration | experimental A time duration that defines one end of the analysis window relative to `event.start`. If positive, the analysis window spans from the `event.start` to `event.start` plus the offset. If negative, the window spans from `event.start` minus the offset up to `event.start`. If missing, no analysis window was required for event creation, or no information about the analysis window is provided. | `5m`; `-5m` |
| `dt.davis.analysis_time_budget` | long | stable The time budget (in seconds) that the DavisÂ® engine is granted before it must raise a problem. The analysis time budget can be set per event and controls the balance of sending out alerts early and granting the AI analysis enough time to finish its analysis. The trade-off of a short analysis budget is that the root cause and event merge analysis is limited or even skipped. For example, the time budget of 0 seconds means that the event raises a problem and sends the alert immediately, without any analysis. |  |
| `dt.davis.analysis_trigger_delay` | long | stable The time delay (in milliseconds) before the trigger of DavisÂ® analysis. For example, the delay of 0 seconds triggers a DavisÂ® problem and the root cause analysis immediately. The trigger delay can be used to hold the analysis until all the relevant root cause data has arrived to Dynatrace. For example, it might be beneficial for cloud integrations or log integrations that report data in different schedulesâ you can delay the analysis until data from all sources is available. Note that while longer delays mean more data is available for root cause analysis, they also delay the delivery of alerts.    Attention: When sent as an event report, the value is in seconds. In Grail, the value is represented in milliseconds. |  |
| `dt.davis.is_entity_remapping_allowed` | boolean | stable This flag defines whether the remapping of the target entity is enabled (true) or disabled (false). If the remapping is enabled, Dynatrace can map the event to an entity extracted from the event metadata. If the remapping is disabled or the extraction is not possible, Dynatrace maps the event to the entity specified in the event configuration (for example, a specific host) or to the global environment entity. |  |
| `dt.davis.is_frequent_issue_detection_allowed` | boolean | stable The flag controls whether the DavisÂ® engine should detect frequent issues. If the flag is set to true, events identified as frequent won't be triggered or merged into a problem. If the flag is set to false, frequent issues won't be detected and events will be triggered and merged as normal. |  |
| `dt.davis.is_merging_allowed` | boolean | stable This flag controls whether the DavisÂ® engine is allowed to merge this event into a larger problem (true) or if a new problem must be created (false). By default, merging is allowed, except for the event type `CUSTOM_ALERT`, where it is by default not allowed. |  |
| `dt.davis.is_problem_suppressed` | boolean | stable This flag controls whether the DavisÂ® engine suppresses the problem from showing up in the web UI and sending notifications. |  |
| `dt.davis.is_rootcause_relevant` | boolean | stable This flag controls whether the DavisÂ® engine should include this event within the root cause analysis (true) or if it is not (false) relevant. |  |
| `dt.davis.preferred_entity_type` | string | stable The preferred classic entity type for remapping. You can find possible values in the classic Dynatrace web UI under Settings > Topology model > Generic types. If the remapping (dt.event.allow\_entity\_remapping) is enabled, this property defines the entity type to which the event should be mapped. If no entity of the preferred type is extracted, no remapping is applied. | `my.custom.entity.type` |
| `dt.davis.timeout` | long | stable The event timeout period (in minutes). If not set, 15 is used. The timeout will automatically be capped to a maximum of 360 minutes (6 hours).    Various event sources use this event property to keep an event active by regularly refreshing an initial event. The timeout defines how fast the event source must refresh an event to keep it active. To keep the event active, the event source must send the refresh within the timeout period. If no refresh is sent, the event is automatically closed by Dynatrace after the timeout period.   Note that metric sources use their own configurable de-alerting windows to close events. Setting the timeout shorter than the de-alerting window will force events to close and increase the risk of false-positive alerts. |  |
| `dt.event.correlation_tag` | string | experimental Set this tag to control which event reports connect together. This value is combined with internal system fieldsâsuch as event.name, dt.source\_entity, and event.providerâto generate a unique correlation ID for event tracking. The final correlation ID that's used for connecting event reports is stored in dt.event.correlation\_id. | `custom correlation tags` |

### Davis event system fields

This section contains fields that the Davis routine sets.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.davis.disable_merging_reason` | string | stable Short explanation for why an event should not be merged with other events into the same problem. This is usually set when 'dt.davis.is\_merging\_allowed' is set to true. If merging is disallowed due to a custom configuration, this field contains the value "Set by event reporter". Additionally, there are scenarios where the DavisÂ® engine may automatically disable merging, typically in cases of problem suppression. | `Set by event reporter`; `Monitored dimensions limit violated` |
| `dt.davis.entity_remapping_failure_info` | string | stable Provides additional information in case remapping an event onto an entity that was extracted from the event metadata failed. | `No entity of type 'myPreferredEntityType' could be extracted from the provided event properties.` |
| `dt.davis.impact_level` | string | stable The impact level of the event. | `Application`; `Environment`; `Infrastructure`; `Services`; `Synthetic` |
| `dt.davis.is_frequent_event` | boolean | stable Indicates if the event was found to frequently happen. Can only be true if dt.davis.is\_frequent\_issue\_detection\_allowed is set to true. If events are frequent events, they will not trigger or merge into problems. To disable frequent issue detection, i.e., set the dt.davis.is\_frequent\_issue\_detection\_allowed field to false in an event template section of an event-raising config. Frequent issue detection can be disabled globally in the frequent issue detection settings. |  |
| `dt.davis.mute.status` | string | stable Status describing if the event is muted. It is also set to muted when the event is part of a problem that is manually closed. | `MUTED` |
| `dt.davis.mute.user` | string | stable User id of the user who muted the event. | `donald_duck@gmail.com` |
| `dt.davis.suppress_problem_reason` | string | stable A short description of the suppression reason. | `Due to manual problem close with id P-2307288 by user donald` |
| `dt.event.correlation_id` | uid | experimental Event reports with the same correlation ID will be grouped together into the same event. There is only one event active at the same time for the same correlation ID. Over time, there might be multiple events with different `event.id` values but the same `dt.event.correlation_id`. | `b52o3b1a50dbbb31` |
| `maintenance.is_under_maintenance` | boolean | stable Indicates if the event is within a maintenance window. |  |

### Settings data

This section contains information on the main settings object that contributes to the event.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.settings.object_id` | string | experimental The object ID of a settings value. This corresponds to the 'objectId' field/parameter in the Settings API. | `vu9U3hXa3q0AAAABACFidWlsdGluOnJ1bS51c2VyLWV4cGVyaWVuY2Utc2NvcmUABnRlbmFudAAGdGVuYW50ACRhMzZmYmYwMy00NDY1LTNlNTYtOTZiOS1kOWMzOGQ3MzU1NmO-71TeFdrerQ` |
| `dt.settings.schema_id` | string | experimental The schema ID of a settings schema, as used in the Settings APIs. | `builtin:problem.notifications`; `app:dynatrace.jenkins:connection` |
| `dt.settings.scope_id` | string | experimental The ID of the scope that a settings object is persisted on. This corresponds to the 'scope' field/parameter in the Settings API. | `environment`; `HOST-EFAB6D2FE7274823` |

### Environmental data

This section contains information on entities.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `affected_entity_ids` | string[] | stable A list of all entities that are directly affected. Each element in the list represents a unique entity. | `['HOST-1234567890ABCDEF']` |
| `affected_entity_types` | string[] | stable A distinct list of entity types corresponding to the entities listed in 'affected\_entity\_ids'. The order of elements in this list does not necessarily correspond to the order of entity ids. | `['dt.entity.host', 'dt.entity.service']` |
| `dt.smartscape.__type__` | smartscapeId | resource stable A Smartscape ID that can be used to query entities from the Smartscape storage. `__type__` is a placeholder for any Smartscape type. Tags: `smartscape-id` | `K8S_CLUSTER-E0D8F94D9065F24F` |
| `entity_tags` | string[] | stable A list of entity tags that were assigned to the affected entities at the time of event creation. | `['departmentA', 'department:A']` |
| `related_entity_ids` | string[] | experimental A list of all entities that are related to the affected entities. Each element in the list represents a unique entity. | `['HOST-1234567890ABCDEF']` |

### Synthetic data

This section contains synthetic event information.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.entity.synthetic_location` | string | resource stable An entity ID of an entity of type SYNTHETIC\_LOCATION. Tags: `entity-id` | `SYNTHETIC_LOCATION-D140F3B85BCCBD1A` |
| `dt.synthetic.location.missing_capabilities` | array | experimental Names of missing Synthetic location capabilities. | `BROWSER`; `ICMP` |
| `dt.synthetic.request.targets` | array | experimental Request target addresses with DNS record type or TCP port number. | `127.0.0.1:22` |
| `dt.synthetic.violated_entity_ids` | array | experimental IDs of synthetic monitor or steps. | `HTTP_CHECK-9349B98E1CD87352`; `HTTP_CHECK_STEP-6349B98E1CD87352` |

## Davis Problems

Every Davis problem update is exported to Grail.
This includes updates that only refresh the problem, which is guaranteed to be at least 1 update every 6 hours.

Problems in Dynatrace represent anomalies in normal behavior or state. Such anomalies can be, for example, a slow service response or user-login process. Whenever a problem is detected, Dynatrace raises a specific problem event indicating such an anomaly.

Raised problems provide insight into their underlying root causes. To identify the root causes of problems, Dynatrace follows a context-aware approach that detects interdependent events across time, processes, hosts, services, applications, and both vertical and horizontal topological monitoring perspectives. Only through such a context-aware approach is it possible to pinpoint the true root causes of problems. For this reason, newly detected anomalous events in your environment won't necessarily result in the immediate raising of a new problem.

### Query

Query davis problems.

```
fetch dt.davis.problems
```

Searches for all unique Davis problems and return status, title and the display id.

```
fetch dt.davis.problems



| filter not(dt.davis.is_duplicate)



| fields id=display_id, title=event.name, status=event.status
```

Searches for all currently active, unique Davis problems and return status, title and the display id.

```
fetch dt.davis.problems



| filter not(dt.davis.is_duplicate)



| filter event.status == "ACTIVE"



| fields id=display_id, title=event.name, status=event.status
```

Search for details of a specific problem with a given display id.

```
fetch dt.davis.problems



| filter not(dt.davis.is_duplicate)



| filter display_id == "P-12345678"



| fields id=display_id, title=event.name, status=event.status
```

Count the total number of active problems in the last hour.

```
fetch dt.davis.problems, from:-1h



| filter not(dt.davis.is_duplicate)



| filter event.status == "ACTIVE"



| summarize active_problem_count = count()
```

Chart the number of currently active problems over the last 24 hours.

```
fetch dt.davis.problems, from:-24h



| filter event.status == "ACTIVE"



| makeTimeseries active_problems = count(), interval:1h, spread: timeframe(from:event.start, to:coalesce(event.end, now()))
```

Shows the logs of all entities affected by the problem 'P-12345678'.

```
fetch logs



| filter dt.source_entity in [



fetch dt.davis.problems



| filter display_id == "P-12345678"



| fields affected_entity_ids



]
```

### Event

This section contains general event information.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `dt.analysis.offset` | duration | experimental A time duration that defines one end of the analysis window relative to `event.start`. If positive, the analysis window spans from the `event.start` to `event.start` plus the offset. If negative, the window spans from `event.start` minus the offset up to `event.start`. If missing, no analysis window was required for event creation, or no information about the analysis window is provided. | `5m`; `-5m` |
| `event.category` | string | stable Standard categorization based on the significance of an event (similar to the severity level in the previous Dynatrace). | `AVAILABILITY`; `ERROR`; `SLOWDOWN`; `RESOURCE_CONTENTION`; `CUSTOM_ALERT`; `MONITORING_UNAVAILABLE` |
| `event.description` | string | stable A description of the problem. The problem description contains the different event descriptions from the events of the problem. | `The current response time (11 s) exceeds the auto-detected baseline (767 ms) by 1,336 %` |
| `event.end` | string | stable The problem end timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). | `16481073970000` |
| `event.id` | string | stable Unique identifier string of a problem, is stable across refreshes and updates. | `5547782627070661074_1647601320000` |
| `event.kind` | string | stable Gives high-level information about what kind of information the event contains without being specific about the contents of the event. It helps to determine the record type of a raw event. Tags: `permission` | `DAVIS_PROBLEM` |
| `event.name` | string | stable The human readable display name of an event type. | `CPU saturation`; `Multiple infrastructure problems` |
| `event.start` | string | stable The problem start timestamp in UTC (given in Grail preferred Linux timestamp nano precision format). This is different from the timestamp even for the first record, as event sources require some time to analyze the underlying data, so the time when a problem update is created (timestamp) differs from the time when the event started (event.start).    The problem start time is set to the start time + analysis offset of the earliest event in the problem.   For problems created based on a sliding window with enough violating slots, `event.start` should be the timestamp of the last violating slot. | `16481073970000` |
| `event.status` | string | stable Status of an event as being either Active or Closed. | `ACTIVE`; `CLOSED` |
| `event.status_transition` | string | experimental An enum that shows the transition of the above event state. | `CREATED`; `UPDATED`; `REFRESHED`; `RESOLVED`; `REOPENED`; `CLOSED` |
| `timestamp` | timestamp | stable The time (UNIX Epoch time in nanoseconds) when the event originated, typically when the source created it. If no original timestamp is available, it will be populated at ingest time and required for all events. In the case of a correlated event (for example, ITIL events), this time could be different from the event.start time, as this time represents the actual timestamp when the "update" for the event was created. | `1649822520123123123` |

### Davis system fields

This section contains fields that the Davis routine sets.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `display_id` | string | stable A pretty, mostly unique id for the problem. | `P-2307288` |
| `dt.analysis.ready` | boolean | experimental Indicates whether problem analysis has progressed enough for followâup actions. When true, initial analysis results are available, and it is a suitable point to trigger actions like notifications, automation, or integrations. This is the exact moment when classic problem notifications start being sent. This property does not mean the problem will remain unchanged. Problem details may still evolve during the analysis's lifecycle. You can adjust the speed of analysis progresses by setting the `dt.davis.analysis_trigger_delay` event property. |  |
| `dt.davis.affected_users_count` | long | experimental The estimated count of users affected by the problem for the application with the highest individual impact. |  |
| `dt.davis.event_ids` | string[] | stable A collection of Davis event ids that belong to the problem. | `['-2127669892157121805_1688396340000']` |
| `dt.davis.impact_level` | string | stable Lists all impact levels observed in the events contributing to the problem. Identifies the affected system layers and helps estimate potential endâuser impact. For example, if a problem contains events with impact levels `Application` and `Services`, then both the user-facing application and its underlying services are affected, making real endâuser impact very likely. | `Application`; `Environment`; `Infrastructure`; `Services`; `Synthetic` |
| `dt.davis.is_duplicate` | boolean | stable Indicates if the problem has become a duplicate of another problem. Duplicates can be related by looking for event ids that are part of multiple problems. |  |
| `dt.davis.last_reopen_timestamp` | timestamp | stable Timestamp in UTC (given in Grail preferred Linux timestamp nano precision format) when the problem has reopened the last time. A reopen can occur when a problem has resolved, but is not yet closed. If Davis causal AI identified a new event that should be part of the problem, the problem reopens. The field is not set if the problem never reopened. |  |
| `dt.davis.mute.status` | string | stable Status describing if the problem is muted. It is also set to muted when the problem is manually closed. | `MUTED` |
| `dt.davis.mute.user` | string | stable User id of the user who muted the event. | `donald_duck@gmail.com` |
| `labels.alerting_profile` | string[] | **deprecated Alerting profiles, previously used to filter problems, have been deprecated. Use DQL to query problem properties directly, and simple workflows to handle notifications instead. To replicate event filtering without joins in DQL, configure problem field settings to propagate relevant event fields to problems.** A list of alerting profiles that match the problem at the current time. | `['Production', 'Team DevOps']` |
| `maintenance.is_under_maintenance` | boolean | stable Indicates if the problem is within a maintenance window. |  |
| `resolved_problem_duration` | duration | stable Final duration of the problem in nanoseconds after it was resolved. |  |

### Environmental data

This section contains information on entities.

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `affected_entity_ids` | string[] | stable A list of all entities that are directly affected. Each element in the list represents a unique entity. | `['HOST-1234567890ABCDEF']` |
| `affected_entity_types` | string[] | stable A distinct list of entity types corresponding to the entities listed in 'affected\_entity\_ids'. The order of elements in this list does not necessarily correspond to the order of entity ids. | `['dt.entity.host', 'dt.entity.service']` |
| `entity_tags` | string[] | stable A combined list of all Davis event entity tags. | `['departmentA', 'department:A']` |
| `related_entity_ids` | string[] | experimental A list of all entities that are related to the affected entities. Each element in the list represents a unique entity. | `['HOST-1234567890ABCDEF']` |
| `root_cause_entity_id` | string | stable The problem root cause entity. | `HOST-1234567890ABCDEF` |
| `root_cause_entity_name` | string | stable The name of the problem root cause entity at the time when the problem snapshot was created. | `Server 1.2.3.4` |

| Attribute | Type | Description | Examples |
| --- | --- | --- | --- |
| `smartscape.affected_entity.ids` | smartscapeId[] | experimental A distinct list of all Smartscape IDs that are directly affected. Each element in the list represents a unique Smartscape node. | `['HOST-1234567890ABCDEF']` |
| `smartscape.affected_entity.types` | string[] | experimental A distinct list of Smartscape types corresponding to the Smartscape IDs listed in 'smartscape.affected\_entity.ids'. The order of elements in this list does not necessarily correspond to the order of IDs. | `['host', 'service']` |
| `smartscape.related_entity.ids` | smartscapeId[] | experimental A distinct list of all Smartscape IDs that are related to the affected Smartscape IDs. Each element in the list represents a unique Smartscape node. | `['HOST-1234567890ABCDEF']` |
| `smartscape.related_entity.types` | string[] | experimental A distinct list of Smartscape types corresponding to the Smartscape IDs listed in 'smartscape.related\_entity.ids'. The order of elements in this list does not necessarily correspond to the order of IDs. | `['host', 'service']` |
