---
title: End-to-end request monitoring
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring
scraped: 2026-05-12T12:04:01.672620
---

# End-to-end request monitoring

# End-to-end request monitoring

* 1-min read
* Published Apr 15, 2019

With Dynatrace, you can monitor incoming and outgoing web requests of your own or any third-party Go applications. OneAgent identifies services that are hosted by Go-based processes and provides service details associated with response times, instances, and executed web requests.

![Dynamic web requests](https://dt-cdn.net/images/dynamic-web-requests-1683-38937e6063.png)

Dynamic web requests

[Service flow](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") reveals more data on the transactions and allows easy access to individual requests, including their related distributed traces.

![Service flow](https://dt-cdn.net/images/service-flow-for-influxdb-stress-test-1683-7c250d283a.png)

Service flow

As you can see from the screenshots below, OneAgent captures details of each web request, including the request URI, method, and headers as well as the response status code and headers.

![PurePath - summary](https://dt-cdn.net/images/purepath1-for-influxdb-stress-test-1869-1c6edc761a.png)

PurePath - summary

![PurePath - code level](https://dt-cdn.net/images/purepath2-for-influxdb-stress-test-1886-6faae42e94.png)

PurePath - code level