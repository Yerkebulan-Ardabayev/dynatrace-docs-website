---
title: Settings API - Application detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-app-detection
---

# Settings API - Application detection schema table

# Settings API - Application detection schema table

* Published Dec 05, 2023

### Application detection (`builtin:rum.web.app-detection)`

Define new applications for Real User Monitoring (RUM) using [application detection rules﻿](https://dt-url.net/wb3f0pfr), check how your existing rules map to your applications.

By default, Dynatrace associates all your monitoring data with a placeholder application (`<your-dynatrace-url>//#uemapplications/uemappmetrics;uemapplicationId=APPLICATION-EA7C4B59F27D43EB`). Define your own detection rules for grouping your monitoring data into distinct applications in Dynatrace.

If you haven't done so already, deploy OneAgent (`<your-dynatrace-url>//#install`). After the deployment [RUM﻿](https://dt-url.net/1n2b0prq) is enabled by default for all web applications that are auto-detected by OneAgent. OneAgent [automatically injects﻿](https://dt-url.net/kp5f0p5z) a JavaScript code snippet into the HTML of all the pages of your monitored web applications so that it can capture monitoring data and ensure end-to-end monitoring visibility.

* Rules are applied sequentially, with rules at the top taking priority over lower rules.
* [Not seeing your applications or RUM data?﻿](https://dt-url.net/kl2a0pm4)
* More details on [defining your web application﻿](https://dt-url.net/r63b0pgq).

Given a set of URLs:

* http://www.mybookshop.com/about
* http://checkout.mybookshop.com/proceed
* http://mybook.shop.com/about/index.php
* http://www.this-is-mybookshop.com/about/index.php

The rule *Domain (host) contains* **mybook** matches against:

* http://www.**mybook**shop.com/about
* http://checkout.**mybook**shop.com/proceed
* http://**mybook**.shop.com/about/index.php
* http://www.this-is-**mybook**shop.com/about/index.php

The rule *Domain (host) ends with* **shop.com** matches against:

* http://www.mybook**shop.com**/about
* http://checkout.mybook**shop.com**/proceed
* http://mybook.**shop.com**/about/index.php
* http://www.this-is-mybook**shop.com**/about/index.php

The rule *Domain (host) equals* **www.mybookshop.com** matches against:

* http://**www.mybookshop.com**/about/index.php

The rule *Domain (host) matches* **mybookshop.com** matches against:

* http://www.**mybookshop.com**/about
* http://checkout.**mybookshop.com**/proceed

The rule *Domain (host) starts with* **checkout** matches against:

* http://**checkout**.mybookshop.com/proceed

The rule *URL contains* **mybookshop.com/about** matches against:

* http://www.**mybookshop.com/about**
* http://www.this-is-**mybookshop.com/about**/index.php

The rule *URL ends with* **about/index.php** matches against:

* http://mybook.shop.com/**about/index.php**
* http://www.this-is-mybookshop.com/**about/index.php**

The rule *URL equals* **http://www.mybookshop.com/about** matches against:

* **http://www.mybookshop.com/about**

The rule *URL starts with* **http://www.mybookshop.com** matches against:

* **http://www.mybookshop.com**/about

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.app-detection` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.app-detection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.app-detection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.app-detection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Matcher `matcher` | enum | The element has these enums * `DOMAIN_CONTAINS` * `DOMAIN_ENDS_WITH` * `DOMAIN_EQUALS` * `DOMAIN_MATCHES` * `DOMAIN_STARTS_WITH` * `URL_CONTAINS` * `URL_ENDS_WITH` * `URL_EQUALS` * `URL_STARTS_WITH` | Required |
| Pattern `pattern` | text | - | Required |
| Application `applicationId` | text | Select an existing application or create a new one. | Required |
| Description `description` | text | Add a description for your rule | Optional |