---
title: Configure URL path pattern matching in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/url-pattern-matching-v2
scraped: 2026-02-17T05:07:01.435963
---

# Configure URL path pattern matching in Service Detection v2

# Configure URL path pattern matching in Service Detection v2

* Latest Dynatrace
* How-to guide
* 7-min read
* Published Jan 23, 2026

Dynatrace SaaS version 1.330+

With the **URL pattern matching** feature, Service Detection v2 (SDv2) can generate better endpoint names by extracting URL path patterns from raw URL paths.

Dynatrace can extract stable, lowâvolatility URL patterns from raw URL paths and write them to the `url.path.pattern` span attribute. The `url.path.pattern` attribute is derived beforehand and then used by [SDv2 endpoint detection](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2 "Find out how to detect endpoints that are entry points into your service.") to name and group endpoints appropriately.

The **URL pattern matching** feature is designed for situations where frameworks or servers don't provide route templates (for example, reverse proxies or libraries without `http.route`), so endpoint names remain meaningful and consistent, preserving correct granularity for critical performance metrics.

## Aim and context

This page describes URL path pattern matching for SDv2 and how to create URL path pattern matching rules, specifically how to define URL path patterns correctly.

* SDv2 applies URL pattern matching to the `span.kind == server` and `span.kind == consumer` span types.
* Endpoint detection includes the **HTTP request method and URL path pattern** [built-in endpoint rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2#default-endpoint-rules "Find out how to detect endpoints that are entry points into your service."). This rule uses `url.path.pattern` and takes precedence over the **HTTP request method and route** rule in determining endpoint names. This way, your extracted URL pattern takes precedence when both `url.path.pattern` and `http.route` are available.
* To benefit from the **URL pattern matching** feature, you need to [create URL path pattern matching rules](#create-rule), specifying the required URL path patterns according to the pattern syntax reference.
* A URL path pattern describes how a raw URL path (for example, `/order/12345`) is generalized into a stable template (for example, `/order/{id}`). It's leveraged to produce lowâvolatility values for the `url.path.pattern` span attribute.

## Pattern matching logic and precedence

* Only spans with `span.kind == server` and `span.kind == consumer` are processed.
* One URL path pattern matching rule may contain one or more URL path patterns.
* URL path pattern matching rules are evaluated in order from top to bottom. Only the first matching rule is applied. The first rule with a URL pattern that matches is applied to a span.
* URL path patterns within a matching rule are also evaluated in order from top to bottom. Only the first matching URL pattern is applied.

  The first matching URL path pattern defines the resulting value for the `url.path.pattern` attribute of a span. When the URL pattern matches, the `url.path.pattern` span attribute is based on this matching URL pattern.
* URL patterns operate on path segments; path segments are URL parts between a slash `/`.
* Leading slashes in URL paths are normalized before matching.

  Before URL patterns are evaluated, any number of leading slashes in the path is reduced to a single `/` to ensure consistent and reliable matching.
* Matching is case sensitive.

## URL pattern syntax reference

Use the information below to construct meaningful URL path patterns for your [URL path pattern matching rules](#create-rule).

The following characters or values are possible in the URL path patterns. Use them to replace highâcardinality parts of your URLs (IDs, version numbers, and deep internal URL paths) with placeholders or asterisks while keeping the overall structure of the endpoint recognizable.

* Literal segments
* Placeholders `{placeholder-name}`
* Variable segments `_`
* Catch-all `*`

### Literal segments

* Represented by a literal value of a path segment.
* Matches an exact path segment.
* Copied as-is to the output.
* Use for fixed path parts that never change.

URL pattern

URL path

Resulting endpoint

`/api/orders`

`/api/orders`

`/api/orders`

### Placeholder `{placeholder-name}`

* Represented by a placeholder name in curly braces, for example, `{id}` or `{date}`.
* Matches exactly one path segment.
* Replaced with a placeholder name in curly braces.
* Use to hide dynamic path values, for example, IDs, UUIDs, or timestamps.

URL pattern

URL path

Resulting endpoint

`/api/orders/{id}`

`/api/orders/1234`

`/api/orders/abcd`

`/api/orders/{id}`

`/api/orders/{id}`

### Variable segments `_`

* Represented by an underscore `_`.
* Matches exactly one path segment.
* Replaced with the original segment value.
* Use when the segment should remain visible, for example, for versioned APIs where the version should remain visible.

URL pattern

URL path

Resulting endpoint

`/api/_/orders`

`/api/v1/orders`

`/api/v2/orders`

`/api/v1/orders`

`/api/v2/orders`

### Catch-all `*`

* Represented by an asterisk `*`.
* Matches zero or more trailing segments. Must be the last token in the URL pattern.
* Replaced with `*`.
* Use when matching any remaining path segments.

URL pattern

URL path

Resulting endpoint

`/internal/*`

`/internal/service`

`/internal/service/operation/extra`

`/internal/*`

`/internal/*`

## Configure URL pattern matching

The sections below describe how to create and manage URL pattern matching rules.

### Create a URL pattern matching rule

To create a URL path pattern matching rule

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Service detection** > **URL path pattern matching**.

When the **Settings Classic** option is not available for you, use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to create URL pattern matching rules.

2. Select **Add rule**.
3. Fill in the following optional and required fields.

   * **Rule name**: Required

     A user-defined name for the rule.
   * **Description**: Optional

     A human-readable descriptor of the rule.
   * **Matching condition**: Required

     A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
4. Select **Add item** and specify a URL path pattern according to the [pattern syntax reference](#syntax-reference). Repeat if more path patterns should to be added.
5. If required, use ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") to re-order the added URL path patterns, considering that the first matching pattern is used to determine the `url.path.pattern` attribute value.
6. Select **Save changes**.

### Manage URL pattern matching rules

You can edit, disable, or delete your URL pattern matching rules.

1. Go to **Settings** (Dynatrace Classic) or **Settings Classic** > **Service detection** > **URL path pattern matching**.

When the **Settings Classic** option is not available for you, use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to create URL pattern matching rules.

2. Make the required changes to your URL path pattern matching rules:

   * ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") in the **Details** column to edit a rule.
   * ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") in the **Enabled** column to disable or enable a rule.
   * ![Drag handle](https://dt-cdn.net/images/drag-handle-turquoise-600-1aa0e5ea00.svg "Drag handle") to re-order the rules.
   * ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the **Delete** column to permanently delete a rule.
3. Select **Save changes** to apply the changes you've made.

## Use cases and examples

The **URL pattern matching** feature is particularly useful for the following use cases:

* Nginx reverse proxy routing
* Versioned APIs
* REST endpoints with IDs
* Internal APIs with deep paths
* Mixed depth paths

Use case

URL pattern

URL path

Resulting endpoint

Nginx reverse proxy routing

`/api/_/_/{id}`

`/api/v1/users/john`

`/api/v2/users/jack`

`/api/v1/users/{id}`

`/api/v2/users/{id}`

API versioning patterns

`/api/_/_/{id}`

`/api/v1/orders/123456789`

`/api/v2/orders/987654321`

`/api/v1/orders/{id}`

`/api/v2/orders/{id}`

Mixed depth paths

`/blog/_/_/*`

`/blog/2024/11/my-post.md`

`/blog/2024/12/my-holiday.md`

`/blog/2026/01/15/my-thoughts.md`

`/blog/2026/02/05/my-memories.md`

`/blog/2024/11/*`

`/blog/2024/12/*`

`/blog/2026/01/*`

`/blog/2026/02/*`

## Related topics

* [Customize endpoint detection in Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2 "Find out how to detect endpoints that are entry points into your service.")