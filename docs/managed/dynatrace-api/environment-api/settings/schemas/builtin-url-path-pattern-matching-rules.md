---
title: Settings API - URL path pattern matching schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-url-path-pattern-matching-rules
---

# Settings API - URL path pattern matching schema table

# Settings API - URL path pattern matching schema table

* Published Sep 25, 2025

### URL path pattern matching (`builtin:url-path-pattern-matching-rules)`

Define rules to match URL patterns out of URL paths. See [Service Detection v2 documentation﻿](https://dt-url.net/sy035si)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:url-path-pattern-matching-rules` | * `group:service-detection` | `CLOUD_APPLICATION_NAMESPACE` - Kubernetes namespace  `KUBERNETES_CLUSTER` - Kubernetes cluster  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:url-path-pattern-matching-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If enabled, the rule will be evaluated. | Required |
| Rule `rule` | [Rule](#Rule) | - | Required |

##### The `Rule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Rule name `ruleName` | text | - | Required |
| Description `description` | text | - | Optional |
| Matching condition `condition` | text | Limits the scope of the service splitting rule using [DQL matcher﻿](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match. | Optional |
| URL path patterns `urlPathPatterns` | list | First matching pattern defines the resulting url.path.pattern attribute value.  A URL path pattern describes how a raw URL path (for example, `/path/123`) is generalized into a stable template (for example, `/path/{id}`). It operates on path segments (parts between `/`) and is used to produce low‑volatility values for the `url.path.pattern` attribute.  Patterns are matched against a normalized path that always starts with a single leading `/`. Matching is case sensitive.  Syntax Patterns are written as a sequence of segments separated by `/`:  * Literal segments + Match an exact path segment and are copied as‑is.   + Example: `/api/items` matches only paths whose first two segments are `api` and `items`. * `{placeholder}` + Matches exactly one path segment and outputs the placeholder name in braces.   + Use this to hide variable parts like IDs or other dynamic identifiers.   + Example: `/api/items/{id}` matches `/api/items/123` or `/api/items/abc` and produces `/api/items/{id}`. * `_` + Variable segment that matches exactly one path segment and keeps the original value in the result.   + A common use is versioned APIs where the version should remain visible.   + Example: `/api/_/getAll` matches `/api/v1/getAll` or `/api/v2/getAll` and produces `/api/v1/getAll` or `/api/v2/getAll` respectively. * `*` + Catch‑all that matches zero or more trailing segments.   + Must be the last token in the pattern.   + Example: `/internal/*` matches `/internal`, `/internal/service`, `/internal/service/operation/extra` and produces `/internal/*`.  Examples  * `/api/items/{id}` + Matches: `/api/items/1`, `/api/items/xyz`   + Non‑matches: `/api/items`, `/api/items/1/details` * `/api/_/getAll` + Matches: `/api/v1/getAll`, `/api/v2/getAll` * `/internal/*` + Matches any path starting with `/internal`, regardless of depth.  Use these patterns to replace high‑cardinality parts of your URLs (IDs, version numbers, deep internal paths) with placeholders or catch‑alls while keeping the overall structure of the endpoint recognizable. | Required |