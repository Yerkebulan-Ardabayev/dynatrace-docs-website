---
title: Stream syslog to Dynatrace with Fluentd
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-send-syslogs-via-fluentd
scraped: 2026-02-26T21:28:05.947700
---

# Stream syslog to Dynatrace with Fluentd

# Stream syslog to Dynatrace with Fluentd

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Jan 28, 2026

Recommended syslog ingestion

Stream syslog via Fluentd if you already collect logs with it or if a specific use case requires an additional component, for example, forwarding logs to different targets. If you want to benefit from a secure, trusted edge component with enterprise support and life-cycle management, see [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

In the case where Linux system syslog observability is the main focus, we recommend deploying OneAgent, which [autodiscovers host syslog data](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-autodiscovery#oneagent-log-configuration-flow "Dynatrace automatically discovers all new log files that meet specific requirements."), preserves topology context, and requires minimal configuration and maintenance.

You can send Syslog to Dynatrace using Fluentd. Configure Fluentd to send Syslog to Dynatrace Log ingestion API.

![Diagram showing the flow of Syslog ingest via Fluentd](https://dt-cdn.net/images/syslog-fluentd-1486-41dd7cc63c.png)

## Capabilities

* Syslog is a standard protocol for message logging and system logs management. Routers, printers, hosts, switches and other devices across platforms use Syslog to log users' activity, system and software lifecycle events, status, or diagnostics.
* During network monitoring, the remote Syslog server listens to the client's log messages and consolidates the logging data that can be then processed using the capabilities of Dynatrace Log Management and Analytics powered by Grail and Dynatrace AI-driven root cause analysis.

## Configuration

Set up the flow from Syslog producer over Fluentd to Dynatrace with the following steps:

1. Get a [Dynatrace API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") with the `logs.ingest` (Ingest Logs) scope.
2. Deploy Fluentd according to your preferences.

   * [Deploy Fluentdï»¿](https://dt-url.net/o9034h3). Fluentd can also run as a [DaemonSet in a Kubernetes clusterï»¿](https://dt-url.net/t2234xz). Built-in resiliency ensures data completeness and consistency even if Fluentd or an endpoint service temporarily goes down.
3. Enable Fluentd to accept incoming Syslog messages.

   * The [in\_syslogï»¿](https://dt-url.net/t00343n) input plugin enables Fluentd to retrieve records via the Syslog protocol on UDP or TCP. It is included in Fluentd's core so no additional installation is needed in this step.
4. Use the Dynatrace [Fluentd pluginï»¿](https://dt-url.net/gb23475) to stream logs to the Dynatrace cluster. The open-source Dynatrace Fluentd plugin uses [Log ingestion API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Stream log data to Dynatrace using API and have Dynatrace transform it into meaningful log messages.") to send logs to Dynatrace.
5. Point your devices to send syslogs to Fluentd.

## Send syslogs to a remote endpoint

In the examples below, you can send syslogs to a remote endpoint, which is Fluentd.

### Example 1

Configure Rsyslog on Linux Ubuntu to forward syslogs to a remote server, Fluentd.
You need to add the following line to the syslog daemon configuration file `/etc/rsyslog.conf` (UDP protocol):

```
*.* @<fluentd host IP>:5140
```

* The `*.*` instructs the daemon to forward all messages to the specified Fluentd instance listening on port 5140. `<fluentd host IP>` needs to point to the IP address of Fluentd.
* If you use TCP, type two `@` symbols, ( `@@`), as follows:

```
*.* @@<fluentd host IP>:5140
```

### Example 2

Configure the F5 BIG-IP system to log to a remote syslog server (11.x - 17.x).
Refer to the [F5 BIG-IP documentationï»¿](https://dt-url.net/080348q) for procedures regarding remote Syslog configuration.

## Add attributes to syslogs in Fluentd

The Dynatrace software intelligence platform and Dynatrace Intelligence depend on context-rich, quality data. You can provide the context for your data ingested via Log ingestion API that supports a set of [keys and semantic attributes](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#parameters "Push custom logs to Dynatrace via the Log Monitoring API v2."). You can also provide custom attributes that don't require indexing in [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.").

### Example 1

Add the `log.source` attribute based on the source of syslogs in Fluentd.  
The syslog message often needs additional context to differentiate sources during analysis. In this example, there are two separate syslog endpoints exposed in Fluentd: one for the Linux syslogs, and the other one for F5 syslogs. This helps decorate log streams with meaningful `log.source attribute`. The Fluentd configuration file needs to look like this:

```
<source>



@type syslog



port 5140



bind 0.0.0.0



tag system-linux



</source>



<source>



@type syslog



port 5141



bind 0.0.0.0



tag system-f5



</source>
```

You need to add `log.source` attribute based on the fluentd tag.

```
<filter system-linux.**>



@type record_transformer



<record>



log.source "linux syslogs"



</record>



</filter>



<filter system-f5.**>



@type record_transformer



<record>



log.source "f5 syslogs"



</record>



</filter>
```

Refer to the [Fluentd record\_transformer filter plugin documentationï»¿](https://dt-url.net/ac2345m) for more details.