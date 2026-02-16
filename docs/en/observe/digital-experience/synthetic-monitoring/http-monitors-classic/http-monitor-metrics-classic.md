---
title: HTTP monitor metrics
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic
scraped: 2026-02-16T09:27:20.074057
---

# HTTP monitor metrics

# HTTP monitor metrics

* Explanation
* 1-min read
* Published Dec 04, 2020

The following metrics are captured and displayed for synthetic [HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types."):

Response time
:   Measures the HTTP monitor or event performance.  
    **Response time** is the sum of **DNS lookup time**, **TCP connect time**, **TLS handshake time**, **Waiting**, and **Download**.

DNS lookup time
:   The time taken to resolve the host nameâif there are multiple DNS calls because of a redirect, this is the total time of all DNS calls.

TCP connect time
:   The time taken to establish the TCP connectionâif there are multiple TCP connections because of a redirect, this is the total time of TCP connection attempts.

TLS handshake time
:   The time taken to complete the TLS handshake

Waiting
:   The time taken for the server to respond with the first byteâthis is the **Time to first byte** minus (**DNS lookup time** + **TCP connect time** + **TLS handshake time**).  
    Note that **Time to first byte** is the amount of time from the start of the request until the first byte of the response is received.

Download
:   The time taken to download the HTTP response  
    Download time can be 0 when the response is contained within a single packet. Download time can also be 0 when the network is slow. In such cases, we report network latency in **Waiting** time.