---
title: Site Reliability guardian event structure
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/event-structure
scraped: 2026-02-24T21:26:58.458201
---

# Site Reliability guardian event structure

# Site Reliability guardian event structure

* Latest Dynatrace
* Reference
* 4-min read
* Published Oct 24, 2025

Depending on the type of [guardian](/docs/deliver/site-reliability-guardian#guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") â [Lifecycle guardian](/docs/deliver/site-reliability-guardian#lifecycle-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") or [Business guardian](/docs/deliver/site-reliability-guardian#business-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") â you use, the underlying event structure is different.
The number of events written by the Site Reliability guardian is the same, no matter the type.
For each validation, one **started** event, one **finished** event, and `n` **objective** event, one for each objective of the respective guardian, are written.

## Lifecycle guardian (SDLC events)

To query [Lifecycle guardian](/docs/deliver/site-reliability-guardian#lifecycle-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision.") events with DQL, use the following query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"
```

There are two different types of events: `validation` and `validation.objective`.
For `validation` event types, there are two additional subtypes based on the event status `started` and `finished`.

validation started

validation finished

validation.objective

To query Lifecycle guardian `validation` `started` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation"



| filter event.status == "started"
```

To query Lifecycle guardian `validation` `finished` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation"



| filter event.status == "finished"
```

To query Lifecycle guardian `validation.objective` events, use the following DQL query:

```
fetch events



| filter event.kind == "SDLC_EVENT"



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "validation.objective"
```

The above lifecycle events share several common fields.
Any data that is related to guardian internals is stored with a prefix of `dt.srg.`.
The structure of the other event fields aligns with the [Semantic Dictionary for Software Development Lifecycle Validation Events](/docs/semantic-dictionary/model/sdlc-events#sdlc-validation-events "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.").

### Lifecycle guardian event fields

When you want to integrate Lifecycle guardian validation results with a [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or other tooling that you have created, the event fields below is a good starting point for your queries.

## Business guardian (Business events)

To query business guardian events with DQL, use the following query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"
```

You can see three different types of events: `guardian.validation.started`, `guardian.validation.finished`, and `guardian.validation.objective`.

guardian.validation.started

guardian.validation.finished

guardian.validation.objective

To query Business `guardian.validation.started` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.started"
```

To query Business `guardian.validation.finished` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.finished"
```

To query Business `guardian.validation.objective` events, use the following DQL query:

```
fetch bizevents



| filter event.provider == "dynatrace.site.reliability.guardian"



| filter event.type == "guardian.validation.objective"
```

The above business events share several common fields.

### Business guardian event fields

When you want to integrate business guardian validation results with a [dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") or other tooling that you have created, the event fields below is a good starting point for your queries.