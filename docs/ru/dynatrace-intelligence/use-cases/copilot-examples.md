---
title: Generative AI quick analysis examples
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/copilot-examples
scraped: 2026-02-15T21:22:37.299426
---

# Generative AI quick analysis examples

# Generative AI quick analysis examples

* Latest Dynatrace
* Reference
* 9-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI can help you analyze data for many different use cases. See the examples below to understand what kind of DQL output you can expect from your prompts.

See the selected pairs to understand what kind of DQL output you can expect from your prompts.

## Analyze logs with generative AI

Prompt

Generated query

**Show me all logs**

```
fetch logs
```

**Show me all log lines from the last 6 hours**

```
fetch logs, from:now() - 6h
```

**Chart logs by their log level over timeExclude `"NONE"`**

```
fetch logs



| filterOut loglevel == "NONE"



| makeTimeseries by:{loglevel}, interval:1h, count = count()
```

**Show me the maximum number of logs ingested per hour for each loglevel and each host**

```
fetch logs



| makeTimeseries by:{loglevel, host = dt.entity.host}, interval:1h, count = count()



| summarize by:{loglevel, host}, max_count = max(arrayMax(count))
```

**Compare the number of error logs from today with yesterday**

```
fetch logs, from:bin(now(), 24h)



| filter loglevel == "ERROR"



| summarize todayErrorCount = count()



| append



[



fetch logs, from:bin(now(), 24h) - 24h, to:bin(now(), 24h)



| filter loglevel == "ERROR"



| summarize yesterdayErrorCount = count()



]
```

**Show me all error logs over the last day with a granularity of one hour**

```
fetch logs, from:now() - 24h



| filter loglevel == "ERROR"



| makeTimeseries interval:1h, count = count()
```

**Show me 5 log sources with the highest volume**

```
fetch logs



| summarize by:{log.source}, log_count = count()



| sort log_count desc



| limit 5
```

**Show me the most recurring log lines and add a column with the log source and AWS Region**

```
fetch logs



| summarize by:{content, log.source, aws.region}, count = count()



| sort count desc
```

**Summarize slow database queries from logs**

```
fetch logs, from:now() - 48h



| filter contains(content, "slow") AND contains(content, "database")



| summarize by:{loglevel, content}, count = count()
```

**What is causing the most error log lines?**

```
fetch logs, from:now() - 2h



| filter loglevel == "ERROR"



| summarize by:{log.source}, errorCount = count()



| sort errorCount desc



| limit 1
```

**Which host is experiencing the highest number of error logs?**

**Show host name**

```
fetch logs



| filter loglevel == "ERROR"



| summarize by:{dt.entity.host}, errorCount = count()



| lookup



[



fetch dt.entity.host



| fieldsAdd entity.name



], sourceField:dt.entity.host, lookupField:id, fields:{entity.name}



| sort errorCount desc



| limit 1
```

**Maximum number of logs ingested per hour for each loglevel and each host sorted in descending order**

```
fetch logs



| summarize by:{loglevel, host = dt.entity.host, bin(timestamp, 1h)}, count = count()



| summarize by:{loglevel, host}, max_count = max(count)



| sort max_count desc
```

## Analyze events with generative AI

Prompt

Generated query

**Return all events from the last three hours**

```
fetch events, from:now() - 3h
```

**Show an aggregated view of events by kind over the last three hours**

```
fetch events, from:-3h



| summarize by:{event.kind}, count = count()
```

## Analyze business events with generative AI

Prompt

Generated query

**Show all business events during business hours grouped by type and category**

```
fetch bizevents



| fieldsAdd day_of_week = getDayOfWeek(timestamp), hour_of_day = formatTimestamp(timestamp, format:"HH")



| filter day_of_week >= 1 AND day_of_week <= 5 AND hour_of_day >= 9 AND hour_of_day <= 17



| summarize by:{event.type, event.category}, count()
```

**Show all business events from the last month, grouped by type and category.**

**Limit this to events during business days.**

**Sort by category**

```
fetch bizevents, from:-720h



| fieldsAdd day_of_week = getDayOfWeek(timestamp)



| filter day_of_week >= 1 AND day_of_week <= 5



| summarize by:{event.type, event.category}, count = count()



| sort event.category
```

**Show all business events over time by type**

```
fetch bizevents



| makeTimeseries by:{event.type}, interval:1h, count = count()
```

**Show timeseries of bizevents by source**

```
fetch bizevents



| makeTimeseries by:{event.provider}, interval:1h, count = count()
```

**Show all easytravel `bizevents` by type as a timeseries for the last week**

```
fetch bizevents, from:-168h



| filter event.provider == "www.easytravel.com"



| makeTimeseries by:{event.type}, interval:24h, count = count()
```

**Show all easytrade `bizevents` by type as a timeseries for the last week**

```
fetch bizevents, from:now() - 168h, to:now()



| filter contains(event.provider, "easytrade")



| makeTimeseries by:{event.type}, interval:24h, count = count()
```

**How many trades took place on easytrade in the last 24 hours?**

```
fetch bizevents, from:now() - 24h, to:now()



| filter event.type == "com.easytrade.trades"



| summarize tradeCount = count()
```

**Summarize easytrade `buy.finish` event types by country**

```
fetch bizevents



| filter event.type == "com.easytrade.buy.finish"



| summarize by:{geo.country.name}, event_count = count()
```

**Show me the count of distinct emails containing `"@gmail.com"` from `bizevents`**

```
fetch bizevents



| filter contains(email, "@gmail.com")



| summarize distinctEmailCount = countDistinct(email)
```

## Analyze Davis events with generative AI

Prompt

Generated query

**Compare the number of Davis events day-by-day for the last week**

```
fetch dt.davis.events.snapshots, from:now() - 168h, to:now()



| summarize by:{bin(timestamp, 24h)}, dailyEventCount = count()
```

**Summarize how many and which categories of Davis events occurred**

```
fetch dt.davis.events, from:-48h



| summarize by:{event.category}, event_count = count()
```

**How many service slowdown events occurred yesterday?**

```
fetch dt.davis.events.snapshots, from:bin(now(), 24h) - 24h, to:bin(now(), 24h)



| filter event.type == "SERVICE_SLOWDOWN"



| summarize slowdown_count = count()
```

**Compare the number of Davis events day-by-day for the last week**

```
fetch dt.davis.events, from:now() - 168h, to:now()



| fieldsAdd day = bin(timestamp, 24h)



| summarize by:{day}, event_count = count()
```

**Summarize how many and which categories of Davis events occurred**

```
fetch dt.davis.events



| summarize by:{event.category}, count = count()
```

## Analyze spans with generative AI

Prompt

Generated query

**Show me the average database response time broken down by host and database**

```
fetch spans



| filter span.kind == "client" AND isNotNull(db.system) AND isNotNull(server.address) AND isNotNull(db.namespace)



| summarize by:{host = server.address, database = db.namespace}, avg_duration = avg(duration)
```

**Show me the average database response time in 1 minute granularity, split by database**

```
fetch spans



| filter span.kind == "client" AND isNotNull(db.system)



| makeTimeseries by:{db.system}, interval:1m, avg_duration = avg(duration)
```

## Analyze metrics with generative AI

Prompt

Generated query

**Show the three most important metrics for host HOST-12ABC**

```
timeseries by:{dt.entity.host}, filter:dt.entity.host == "HOST-12ABC", {availability = avg(dt.host.availability), uptime = avg(dt.host.uptime), cpu_usage = avg(dt.host.cpu.usage)}



| fieldsAdd avg_availability = arrayAvg(availability), avg_uptime = arrayAvg(uptime), avg_cpu_usage = arrayAvg(cpu_usage)



| sort avg_availability desc, avg_uptime desc, avg_cpu_usage desc



| limit 3
```

**Show each lambda function's execution time as metric timeseries**

```
timeseries by:{dt.entity.aws_lambda_function}, avg_execution_time = avg(dt.cloud.aws.lambda.duration)
```

**Compare last 24 hours' CPU usage with the corresponding timeframe from one week ago**

```
timeseries from:now() - 24h, to:now(), cpu_usage_last_24h = avg(dt.host.cpu.usage)



| append [timeseries from:now() - 168h - 24h, to:now() - 168h, cpu_usage_last_week = avg(dt.host.cpu.usage)]
```

**Show me the top ten processes with respect to memory consumption and the host they are running on**

```
timeseries by:{dt.entity.process_group_instance, dt.entity.host}, maxMemory = max(dt.process.memory.working_set_size)



| summarize by:{dt.entity.process_group_instance, dt.entity.host}, maxMemory = max(maxMemory)



| sort maxMemory desc



| limit 10



| lookup [fetch dt.entity.host], sourceField:dt.entity.host, lookupField:id, fields:{entity.name}
```

**Give me an overview of the CPU-related metrics for `HOST-14DC825E0C327E32` for the last day**

```
timeseries by:{dt.entity.host}, filter:dt.entity.host == "HOST-14DC825E0C327E32", timeframe:timeframe(from:now() - 24h, to:now()), {avg_cpu_usage = avg(dt.host.cpu.usage), avg_cpu_system = avg(dt.host.cpu.system), avg_cpu_user = avg(dt.host.cpu.user), avg_cpu_iowait = avg(dt.host.cpu.iowait), avg_cpu_load15m = avg(dt.host.cpu.load15m)}
```

**Show the CPU average from all Kubernetes services grouped by container name.**

**Limit to top 10**

```
timeseries by:{k8s.container.name}, avg_cpu = avg(dt.kubernetes.container.cpu_usage)



| sort avg_cpu desc



| limit 10
```

## Analyze entities with generative AI



Prompt

Generated query

**Show me the top lambda function with respect to code size**

```
fetch dt.entity.aws_lambda_function



| sort awsCodeSize desc



| fieldsKeep awsCodeSize, entity.name



| limit 1
```

**Show me the most tagged host groups**

```
fetch dt.entity.host_group



| fieldsAdd tags



| expand tags



| summarize by:{entity.name}, tag_count = count()



| sort tag_count desc



| limit 10
```

**How many Azure VMs do we have compared to ec2 instances?**

```
fetch dt.entity.azure_vm



| summarize azure_vm_count = count()



| append



[



fetch dt.entity.ec2_instance



| summarize ec2_instance_count = count()



]
```

**Show me the 5 shortest lived Kubernetes services**

```
fetch dt.entity.kubernetes_service



| fieldsAdd id, entity.name, lifetime



| fieldsAdd duration = toDuration(lifetime)



| sort duration



| limit 5
```

**How many AWS lambda functions are deployed?**

```
fetch dt.entity.aws_lambda_function



| summarize deployed_functions = count()
```

**Show me all hosts with CPU usage greater than 60% over the last week**

```
timeseries by:{dt.entity.host}, from:now() - 168h, cpuUsage = avg(dt.host.cpu.usage)



| filter arrayAvg(cpuUsage) > 60



| lookup [fetch dt.entity.host], sourceField:dt.entity.host, lookupField:id
```

## Analyze problems with generative AI

Prompt

Generated query

**Show number of problems by problem status for the last day, as a timeseries**

```
fetch dt.davis.problems, from:now() - 24h, to:now()



| makeTimeseries by:{status = event.status}, interval:1h, count = count()
```

**Summarize the top ten problems of the last 24 hours, ranked by number of affected entities**

```
fetch dt.davis.problems, from:now() - 24h



| expand affected_entity_ids



| summarize by:{event.name}, affectedEntityCount = count()



| sort affectedEntityCount desc



| limit 10
```

**Show most problem-affected entities**

```
fetch dt.davis.problems



| expand affected_entity_ids



| summarize by:{affected_entity_ids}, count = count()



| sort count desc
```

**Show all active problems by category as a timeseries**

```
fetch dt.davis.problems



| filter event.status == "ACTIVE"



| makeTimeseries by:{event.category}, interval:1h, count = count()
```

**Show active problems by their root cause, where the root cause is not null or empty**

```
fetch dt.davis.problems



| filter isNotNull(root_cause_entity_id) AND root_cause_entity_id != ""



| fields root_cause_entity_id, display_id, event.name, timestamp
```

**How many entities are affected by a problem called "HTTP monitor global outage"?**

```
fetch dt.davis.problems



| filter event.name == "Http monitor global outage"



| expand affected_entity_ids



| summarize affected_entities = countDistinct(affected_entity_ids)
```

**How many slowdown problems have been detected over the last 3 days?**

```
fetch dt.davis.problems, from:now() - 72h



| filter event.category == "SLOWDOWN"



| summarize slowdownCount = count()
```

**Show all problems that affected more than 500 users. Keep these fields: `display\_id`, `dt.davis.affected\_users\_count`, `event.category`, `event.description`, and `resolved\_problem\_duration`**

```
fetch dt.davis.problems



| filter dt.davis.affected_users_count > 500



| fieldsKeep display_id, dt.davis.affected_users_count, event.category, event.description, resolved_problem_duration
```

**Show how many problems there have been this year, as a week-by-week comparison**

```
fetch dt.davis.problems, from:bin(now(), 24h) - 365d



| fieldsAdd week_of_year = getWeekOfYear(timestamp)



| summarize by:{week_of_year}, problem_count = count()
```

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")