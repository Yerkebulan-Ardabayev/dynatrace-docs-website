---
title: Syslog ingestion with ActiveGate (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog
scraped: 2026-02-20T21:22:31.879191
---

# Syslog ingestion with ActiveGate (Logs Classic)

# Syslog ingestion with ActiveGate (Logs Classic)

* Tutorial
* 4-min read
* Updated on Oct 08, 2025
* Preview

Preview ActiveGate version 1.293+ Log Monitoring Classic

Preview

This is a preview release. Your current configuration is fully compatible with future versions, but you can expect higher resiliency to traffic spikes and better handling of connection disruptions when the feature becomes generally available.

For the newest Dynatrace version, see [Syslog ingestion with ActiveGate](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

Syslog, short for system logging protocol, is a logging mechanism that enables system administrators to oversee and control log files from various system components, such as network devices, Linux host syslog, syslog servers, or other syslog producers.

This guide shows you how to configure your Environment ActiveGate on Linux to collect syslog logs in your network and ingest them to Dynatrace.

## Prerequisites

* Environment ActiveGate version 1.293+ on Linux installed to [monitor remote technologies](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.").
* Your network devices have the syslog enabled or you have other syslog producers configured in your network. Refer to RFC3164 and RFC5424 for details. Dynatrace supports a wide variety of syslog implementations, including RSysLog, Syslog-NG, NXLog, and others.

## Who is it for?

This guide is intended for network and Dynatrace admins who are tasked to enable the syslog log ingestion into Dynatrace.

## Enable syslog ingestion

Enabling syslog log ingestion requires you to:

* Deploy Environment ActiveAge in a place ensuring the connectivity between ActiveGate and monitored devices.
* Enable syslog ingestion on ActiveGate.
* Optional in some cases, you'll need to adapt the default syslog receiver configuration.

1. **Deploy Environment ActiveGate**.

   See instructions for [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux "Learn how to install ActiveGate on Windows, customize installation, and more."). Use the [remote technologies monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") purpose.
2. **Enable syslog ingestion on your ActiveGate**.

   Edit the `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf` file and add the following flag:

   ```
   syslogenabled=true
   ```
3. Optional **Edit the syslog receiver configuration**.

   ActiveGate uses an embedded Dynatrace OpenTelemetry Collector instance and stores the receiver configuration in the `/var/lib/dynatrace/remotepluginmodule/agent/conf/syslog.yaml` file. The Collector is installed by default.

   Use this configuration only for syslog ingestion.

   If your syslog producers use the default ports per supported protocols, your syslog-enabled ActiveGate should receive syslog records right away.

   You only need to modify the configuration if your syslog producers cast events on custom ports.

   Show me the fileâ¦

   ```
   receivers:



   syslog/udp:



   udp:



   listen_address: '0.0.0.0:514'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   syslog/tcp:



   tcp:



   listen_address: '0.0.0.0:601'



   add_attributes: true



   protocol: rfc5424



   operators:



   - type: syslog_parser



   protocol: rfc5424



   #  syslog/tcp_tls:



   #    tcp:



   #      listen_address: "0.0.0.0:6514"



   #      tls:



   #        cert_file: "/absolute/path/to/server.crt"



   #        key_file: "/absolute/path/to/server.key"



   #    protocol: rfc5424



   #    operators:



   #      - type: syslog_parser



   #        protocol: rfc5424



   #DO.NOT.MODIFY



   exporters:



   otlp_http/syslog: ${file:syslogendpoint.yaml}



   processors:



   batch:



   send_batch_size: 512



   send_batch_max_size: 1024



   transform:



   log_statements:



   - context: log



   statements:



   - set(body, attributes["message"])



   attributes:



   actions:



   - key: net.host.name



   action: delete



   - key: net.peer.name



   action: delete



   - key: net.peer.port



   action: delete



   - key: net.transport



   action: delete



   - key: net.host.ip



   action: delete



   - key: dt.ingest.port



   from_attribute: net.host.port



   action: upsert



   - key: dt.ingest.source.ip



   from_attribute: net.peer.ip



   action: upsert



   - key: net.peer.ip



   action: delete



   - key: net.host.port



   action: delete



   - key: syslog.hostname



   from_attribute: hostname



   action: upsert



   - key: hostname



   action: delete



   - key: syslog.facility



   from_attribute: facility



   action: upsert



   - key: facility



   action: delete



   - key: syslog.priority



   from_attribute: priority



   action: upsert



   - key: priority



   action: delete



   - key: syslog.proc_id



   from_attribute: proc_id



   action: upsert



   - key: proc_id



   action: delete



   - key: syslog.version



   from_attribute: version



   action: upsert



   - key: version



   action: delete



   - key: syslog.appname



   from_attribute: appname



   action: upsert



   - key: appname



   action: delete



   - key: message



   action: delete



   service:



   telemetry:



   metrics:



   level: none



   pipelines:



   logs/udp:



   receivers: [syslog/udp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   logs/tcp:



   receivers: [syslog/tcp]



   processors: [transform, attributes, batch]



   exporters: [otlp_http/syslog]



   #    logs/tcp_tls:



   #      receivers: [syslog/tcp_tls]



   #      processors: [transform, attributes, batch]



   #      exporters: [otlp_http/syslog]
   ```

   You can also modify the default configuration if you want to group a set of various devices by configuring them to use a specific port. For example, you can enrich your syslog events cast on specific TCP ports using the configuration as in the example below

   ```
   receivers:



   syslog/f5:



   tcp:



   listen_address: "0.0.0.0:54526"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.dt.ip_addresses



   value: "1xx.xx.xx.xx1"



   - type: add



   field: attributes.instance.name



   value: "ip-1xx-xx-x-xx9.ec2.internal"



   - type: add



   field: attributes.device.type



   value: "f5bigip"



   syslog/host:



   tcp:



   listen_address: "0.0.0.0:54527"



   protocol: rfc5424



   operators:



   - type: add



   field: attributes.log.source



   value: syslog



   - type: add



   field: attributes.device.type



   value: "ubuntu-syslog"
   ```

   **Note**: Do NOT modify the exporter configuration. The default configuration points to the embedded Collector.

   For more information on syslog receiver configuration, see [Ingest syslog data with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.").
4. **Verify the syslog ingestion is enabled**.

   After you enable syslog ingestion, check the following log files to verify it:

   Open the newest `ruxit_extensionmodule_*.log` log file in the `extensions` log directory:

   * Linux: `/var/lib/dynatrace/remotepluginmodule/log/extensions`

   It should contain the following line:

   ```
   Otel syslog enabled: true
   ```
5. **Enable syslog on the devices you want to monitor**.

   The way you enable syslog depends on the device and its platform, refer to specific documentation for details.

   **Example**
   Configure Rsyslog on Linux Ubuntu to forward syslog logs to a remote server.

   Add the following line to the syslog daemon configuration file (`/etc/rsyslog.conf`)

   * UDP

     ```
     *.* @<ActiveGate host IP>:514
     ```
   * TCP

     ```
     *.* @@<ActiveGate host IP>:601
     ```

   The `*.*` instructs the daemon to forward all messages to the specified ActiveGate listening on the provided port and IP address. `<ActiveGate host IP>` needs to point to the IP address of a syslog-enabled ActiveGate.

   For more examples, see [Syslog via OpenTelemetry Collectorï»¿](https://www.dynatrace.com/hub/detail/syslog-via-opentelemetry-collector/)
6. **Verify ActiveGate receives the syslog events**.

   After your syslog producers start to cast log records, open the latest `dynatracesourceotelcollector.*.log` file in `/var/lib/dynatrace/remotepluginmodule/agent/datasources/otelSyslog`.

   If ActiveGate receives the log records you should see entries as in the example below:

   ```
   [otelSyslog][otelSyslog][37448][err]LogRecord #3



   [otelSyslog][oteiSyslog][37448][err]ObservedTimestamp: 2024-05-06 @9:52:10.6748723 +8000 UTC



   [otelSyslog][otelSyslog][37448][err]Timestamp: 2624-05-@6 11:52:16 +90e0 UTC



   [otelSyslog][otelsyslog][37448][err]SeverityText: info



   [otelSyslog][otelSyslog][37443][err]SeverityNumber: Info(9)



   [otelSyslog][otelSyslog][37448][err]Body: Str(<30>May 6 11:52:10 SOME-HOST systemd[1]: Finished    Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Attributes:



   [otelSyslog][otelSyslog][37448][err]    -> priority: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> facility: Int(3)



   [otelSyslog][otelSyslog][37448][err]    -> appname: Str(systemd)



   [otelSyslog][otelSyslog][37448][err]    -> proc_id: Str(1)



   [otelSyslog][otelSyslog][37443][err]    -> log: Map({âsource": âsyslog"})



   [otelSyslog][otelSyslog][37443][err]    -> hostname: Str(SOME-HOST)



   [otelSyslog][otelSyslog][37443][err]    -> message: Str(Finished Load Kernel Module fuse.)



   [otelSyslog][otelSyslog][37448][err]Trace ID:



   [otelSyslog][otelSyslog][37448][err]Span ID:



   [otelSyslog][otelSyslog][37443][err]Flags: 0
   ```

For more information on troubleshooting the syslog receiver, see [Collector troubleshootingï»¿](https://opentelemetry.io/docs/collector/troubleshooting/).

## Next steps

After you enable the integration, the syslog-ingested events are enriched with the host-specific attributes and become available for log monitoring and processing.

## Troubleshooting

Visit Dynatrace Community for troubleshooting guides, as well as see [Troubleshooting Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Fix issues related to the setup and configuration of Log Monitoring Classic.").

* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)