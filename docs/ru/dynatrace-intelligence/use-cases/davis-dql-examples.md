---
title: Dynatrace Intelligence DQL examples
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-dql-examples
scraped: 2026-02-23T21:27:35.825130
---

# Dynatrace Intelligence DQL examples

# Dynatrace Intelligence DQL examples

* Latest Dynatrace
* Reference
* 7-min read
* Updated on Jan 28, 2026

These examples illustrate how to build powerful and flexible health dashboards by using DQL to slice and dice all Dynatrace Intelligence reported problems and events.

Davis problems represent results that originate from the Dynatrace Intelligence root-cause analysis runs. In Grail, Davis problems and their updates are stored as Grail events.

* [Problem example 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Count the total number of problems in the last 24 hours.
* [Problem example 2](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample2 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Count the current number of active problems.
* [Problem example 3](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample3 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Chart the number of problems in the last 7 days to identify a trend within your environment stability.
* [Problem example 4](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample4 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Identify the top 10 problem-affected entities within your environment.
* [Problem example 5](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample5 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Join entity attributes with detected problems and apply a name filter.
* [Problem example 6](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample6 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Load the last state of a given problem.
* [Problem example 7](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample7 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Load all active problems and exclude all those that are marked as duplicates.
* [Problem example 8](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample8 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Calculate the mean time to resolve for problems over time.
* [Problem example 9](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpproblemexample9 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Show a chart of the concurrently open problems over time.

Davis events represent raw events that originate from various custom alerts within Dynatrace or within the OneAgent. Examples here are OneAgent-detected CPU saturation events or high garbage collection time events.

* [Davis event example 1](/docs/dynatrace-intelligence/use-cases/davis-dql-examples#lpdaviseventexample1 "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")  
  Chart the number of process restart events in the last 7 days.

## Count the total number of problems in the last 24 hours

* Fetches table `dt.davis.problems`.
* Uses the summarize DQL command to get the total number of distinct problems.
* The `event.id` holds the unique problem ID, which is stable across all refreshes and updates that Dynatrace Intelligence reports for the same problem.

```
fetch dt.davis.problems, from:now()-24h, to:now()



| summarize {problemCount = countDistinct(event.id)}
```

**Query result**

problemCount

415

## Count the current number of distinct active problems

* Fetches table `dt.davis.problems`.
* Groups the result by the unique `event.id` field, which contains the problem ID.
* Filters out all problems that are no longer in state `ACTIVE`. To do this, the DQL command `takeLast` of the field `event.status` receives the last state.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE"



| summarize {activeProblems = countDistinct(event.id)}
```

**Query result**

activeProblems

15

## Chart the number of problems from the last 7 days

* Fetches table `dt.davis.problems`.
* Shows the number of problems that occurred during the day over the span of 7 days.
* Counts in a resolution of 6-hour bins.
* Allows to identify stability trends within your environment

```
fetch dt.davis.problems, from:now()-7d



| makeTimeseries count(default:0)
```

**Query result**

timeframe

interval

count

start: 20/11/2024, 12:00 end: 27/11/2024, 13:00

60 min

0.00, 55.00, 143.00, 703.00, 504.00, 120.00, 117.00, 692.00, 534.00

## Identify the top 3 problem-affected entities within your environment

* Fetches table `dt.davis.problems`.
* Expands the arrays field containing all affected entity IDs into individual fields.
* Counts all unique problems grouped by the affected entity IDs.
* Sorts by that problem count.
* Returns the top 3 entity IDs.

```
fetch dt.davis.problems



| expand affected_entity_ids



| summarize count = countDistinct(display_id), by:{affected_entity_ids}



| sort count, direction:"descending"



| limit 3
```

**Query result**

affected\_entity\_ids

count

HOST-A9449CACDE12B2BF

10

SERVICE-5624DD59D74FF453

5

PROCESS\_GROUP\_INSTANCE-3184C659684130C7

3

## Fetch all problems for a host with the name "myhost"

This example joins entity attributes in order to filter all problems with a given host name.

* Fetches table `dt.davis.problems`.
* Expands the arrays field containing all affected entity IDs into individual fields.
* Does a topology and entity lookup on the `affected_entity_ids` field.
* Enriches the resulting records with two entity fields that are prefixed with `host.`: `host.id` and `host.name`.
* Applies a filter for the host name `myhost`.

```
fetch dt.davis.problems



| expand affected_entity_ids



| fieldsAdd host.name = entityName(affected_entity_ids, type: "dt.entity.host")



| filter host.name == "myhost"
```

**Query result**

timestamp

affected\_entity\_ids

host.id

host.name

display\_id

5/31/2023, 1:31:39 PM

HOST-27D70086952122CF

HOST-27D70086952122CF

myhost

P-23054243

## Load the last state of a given problem

This example shows you how to filter problems by a unique ID.

* Fetches table `dt.davis.problems`.
* Filters by the unique display identifier of the problem.
* Allows to find problems connected to a particular ID.

```
fetch dt.davis.problems



| filter display_id == "P-24051200"
```

**Query result**

timestamp

affected\_entity\_ids

host.id

host.name

display\_id

5/31/2023, 1:31:39 PM

HOST-27D70086952122CF

HOST-27D70086952122CF

myhost

P-23053506

## Load all active problems and exclude all those that are marked as duplicates

This example shows you how to fetch all active problems that weren't marked as duplicates.

Since the duplicate flag appears during the lifecycle of a problem, the update events need to be sorted by timestamp. Then, the events need to be summarized by taking the last state of the duplicate and status fields. It's possible to correctly apply the filter only after you sort the events by the timestamp.

* Fetches table `dt.davis.problems`.
* Filters out problems that are marked as duplicates.
* Filters out problems that were closed already.

```
fetch dt.davis.problems



| filter event.status == "ACTIVE" and not dt.davis.is_duplicate == "true"
```

**Query result**

display\_id

status

id

duplicate

P-230910385

ACTIVE

P-230910385

false

## Calculate the mean time of resolving problems over time

This example shows you how to calculate the mean time that was needed to resolve all the reported problems by summarizing the delta between start and end of each problem over time.

* Fetches table `dt.davis.problems`.
* Flattens the problem fields into the record.
* Filters out all frequent and duplicate problems.
* Returns all closed problems.
* Converts the values into a time series of averages over time.

```
fetch dt.davis.problems, from:now()-7d



| filter event.status == "CLOSED"



| filter dt.davis.is_frequent_event == false and dt.davis.is_duplicate == false and maintenance.is_under_maintenance == false



| makeTimeseries `AVG Problem duration in hours` = avg(toLong(resolved_problem_duration)/3600000000000.0), time:event.end
```

## Show a chart of the concurrently open problems over time

This example shows how to create a chart displaying the number of concurrently open problems over time. The resolution gaps are filled with the `spread` command.

* Fetches table `dt.davis.problems`.
* Creates a time series of the problem count.
* Fills the gaps between start and end timestamps of a problem with the correct count by using the `spread` command.

```
fetch dt.davis.problems



| makeTimeseries count = count(), spread: timeframe(from: event.start, to: coalesce(event.end, now()))
```

## Chart the number of CPU saturation and high-memory events in the last 7 days



* Fetches table `dt.davis.events` for the last 7 days.
* Counts in a resolution of 60-minute bins.

```
fetch dt.davis.events, from:now()-7d, to:now()



| filter event.kind == "DAVIS_EVENT"



| filter event.type == "OSI_HIGH_CPU" or event.type == "OSI_HIGH_MEMORY"



| makeTimeseries count =  count(default: 0)
```

**Query result**

60min interval

count

5/25/2023, 3:00 PM

146

5/25/2023, 4:00 PM

312

5/25/2023, 5:00 PM

201