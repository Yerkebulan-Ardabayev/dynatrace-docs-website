---
title: Static thresholds for infrastructure monitoring
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure
---

# Static thresholds for infrastructure monitoring

# Static thresholds for infrastructure monitoring

* Explanation
* 3-min read
* Published May 20, 2019
* Deprecated

Deprecation notice

This page is deprecated. Refer to the [Host anomaly detection](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.") page. All updates and new information will be added there.

Dynatrace infrastructure monitoring is based on numerous built-in, predefined static thresholds. These thresholds relate to resource contentions like CPU spikes, memory, and disk usage. You can change these default thresholds in **Settings** > **Anomaly Detection** > **Infrastructure**.

For applications and services, you can disable automated baselining-based reference-value detection anytime and switch to user-defined static thresholds. If you set a static threshold for response time and error rate on an application or service level, events will be raised if the static threshold is breached. A slowdown event is raised if the static thresholds for either the median or the 90th percentile response times are breached.

### Predefined static thresholds for hosts

| Hosts | Default static threshold |
| --- | --- |
| CPU saturation | Alert if CPU usage is higher than **95**% in 18 of 30 10-second intervals. |
| Memory event usage | * Alert if memory usage is higher than **90**% on Windows or **80**% on Linux * AND memory page fault rate is higher than **100** faults/s on Windows or **20** faults/s on Linux in 18 of 30 10-second intervals. |
| GC activity | * Alert if GC time is higher than **40**% * OR GC suspension is higher than **25**% in 18 of 30 10-second intervals. |
| Java out of memory | Alert if the number of Java out-of-memory exceptions is **1** per minute or higher. |
| AIX High System Load | OneAgent version 1.261+ Alert if the System Load is higher than the defined threshold for the defined amount of samples. This alert is specific to AIX hosts. |

### Predefined static thresholds for networks

| Network | Default static threshold |
| --- | --- |
| Number of dropped packets | * Alert if receive/transmit dropped packet percentage is higher than **10**% * AND total packets rate is higher than **10** packets/s in 18 of 30 10-second intervals. |
| Network utilization | Alert if sent/received traffic utilization is higher than **90**% in 18 of 30 10-second intervals. |
| TCP connectivity for process | * Alert if percentage of new connection failures is higher than **3**% * AND number of failed connections is higher than **10** connections/min in 18 of 30 10-second intervals. |
| Retransmission rate | * Alert if retransmission rate is higher than **10**% * AND number of retransmitted packets is higher than **10** packets/min in 18 of 30 10-second intervals. |

### Predefined static thresholds for disks

| Disk | Default static threshold |
| --- | --- |
| Low disk space | Alert if free disk space is less than **3**% in 18 of 30 10-second intervals. |
| Slow running disks | Alert if disk read time or write time is higher than **200** ms in 18 of 30 10-second intervals. |
| Inodes number available | Alert if percent of available inodes is less than **5**% in 18 of 30 10-second intervals. |

As static thresholds don't adapt to changing environments and require too much manual effort, Dynatrace also offers intelligent, [automated multi-dimensional baselining](/managed/dynatrace-intelligence/anomaly-detection/automated-multidimensional-baselining "Learn how Dynatrace AI automatically calculates baselines based on a multi-dimensional baselining scheme."), which works out of the box, without manual configuration of thresholds. Most importantly, it adapts automatically to changes in traffic patterns.