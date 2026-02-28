---
title: Node.js
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nodejs
scraped: 2026-02-28T21:15:48.065925
---

# Node.js

# Node.js

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Nov 21, 2025

[Node.jsï»¿](https://nodejs.org) is a server-side framework based on the [V8 JavaScript engineï»¿](https://developers.google.com/v8/) by Google. Node.js has an asynchronous execution model and is frequently used for gluing or as a proxy tier within enterprise environments.

## Capabilities

Dynatrace provides extensive Node.js monitoring capabilities:

* Heap and process metrics
* Heap dumps
* CPU sampling
* Event loop metrics
* Insights into inbound and outbound HTTP calls
* Dedicated support for a variety of databases (includes query capture)
* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-js-api/) for capturing traces and ingesting metrics.  
  For more information, see [Instrument your JavaScript application on Node.js with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/nodejs "Learn how to instrument your JavaScript application on Node.js using OpenTelemetry and Dynatrace.")
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* [Continuous thread analysis for worker threads](#worker-threads)

See [our supported technologies matrix](/docs/ingest-from/technology-support#nodejs "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details about supported technologies that will be used in conjunction with Node.js.

## Support & desupport

Node.js follows an [LTS release modelï»¿](https://github.com/nodejs/Release).

Each odd-numbered version reaches EOL shortly after each new even-numbered version is released. Each even-numbered version eventually becomes an LTS release. For enterprise production environments, we recommend that you stick to LTS releases.

Whenever a new Node.js major version (even or uneven) is released, we add support for that version.

Dynatrace will follow this support model, but will support each Node.js version at least half a year longer to give our customers time for upgrades.

| Node.js version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/docs/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 25 | 2025-10-15 | 2026-06-01 | 1.333 | - | 2026-12-01 | Supported |
| 24 | 2025-05-06 | 2028-04-30 | 1.329 | - | 2029-04-30 | Supported |
| 23 | 2024-10-16 | 2025-06-01 | 1.305 | 1.329 | 2025-12-01 | Not supported |
| 22 | 2024-04-23 | 2027-04-30 | 1.295 | - | 2028-04-30 | Supported |
| 21 | 2023-10-17 | 2024-06-01 | 1.281 | 1.303 | 2024-12-01 | Not supported |
| 20 | 2023-04-18 | 2026-04-30 | 1.271 | - | 2027-04-30 | Supported |
| 19 | 2022-10-18 | 2023-06-01 | 1.257 | 1.285 | 2023-12-01 | Not supported |
| 18 | 2022-04-19 | 2025-04-30 | 1.243 | - | 2026-04-30 | Supported |
| 17 | 2021-10-19 | 2022-06-01 | 1.235 | 1.265 | 2022-12-01 | Not supported |
| 16 | 2021-04-20 | 2023-09-11 | 1.219 | - | 2024-09-11 | Limited[1](#fn-node-js-1-def) |
| 15 | 2020-10-20 | 2021-06-01 | 1.207 | 1.233 | 2021-12-01 | Not supported |
| 14 | 2020-04-21 | 2023-04-30 | 1.195 | - | 2024-04-30 | Limited[1](#fn-node-js-1-def) |
| 13 | 2019-10-22 | 2020-06-01 | 1.183 | 1.205 | 2020-12-01 | Not supported |
| 12 | 2019-04-23 | 2022-04-30 | 1.171 | - | 2023-04-30 | Limited[1](#fn-node-js-1-def) |
| 11 | 2018-10-23 | 2019-06-30 | 1.159 | 1.181 | 2019-12-31 | Not supported |
| 10 | 2015-04-24 | 2021-04-30 | 1.147 | 1.329 | 2022-04-30 | Not supported[2](#fn-node-js-2-def) |
| 9 | 2017-10-01 | 2018-06-30 | - | 1.157 | 2018-12-31 | Not supported |
| 8 | 2017-05-30 | 2019-12-31 | - | 1.239 | 2020-12-31 | Not supported |

1

Limited support: Dynatrace can only solve problems that can be reproduced on supported versions.

2

Not supported: Instrumentation is deprecated off by default on OneAgent version >=1.321 and <=1.329. Define DT\_SUPPORT\_DEPRECATED\_NODE\_VERSIONS environment variable to opt in on these OA versions.

## Continuous thread analysis for worker threads

Node.js version 12+ OneAgent version 1.251+ Dynatrace version 1.256+

[Continuous thread analysis](/docs/observe/application-observability/profiling-and-optimization/continuous-thread-analysis "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") for [worker threadsï»¿](https://nodejs.org/api/worker_threads.html#worker-thread) can automatically identify CPU-intensive threads and pinpoint scalability issues when work is distributed across many threads so that you can solve performance bottlenecks before your end users are impacted.

Continuous thread analysis in action

Statistics about the `main` and `worker` threads:

![Node.js worker thread stats](https://dt-cdn.net/images/worker-thread-stats-1815-5a10cfd6f5.png)

CPU time consumed by the various `worker` threads:

![Node.js worker thread CPU times](https://dt-cdn.net/images/worker-thread-cpu-times-1815-7223ec5892.png)

To get started with the continuous thread analysis for worker threads, activate the [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Node.js worker threads monitoring** and **Node.js code module preloading**.

Limitations

Node.js specific metrics (for example, memory, garbage collection, and event-loops) are only reported for the `main` thread.

Class browsing (required for the custom messaging services of kafkajs) is limited to the `main` thread.

There is no automatic transaction tracing in place between the `main` and `worker` threads. For tracing transactions across threads, you can either use [OpenTelemetry tracing](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.") or the [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.").

## Known limitations

* Due to platform limitations of JavaScript and Node.js, code-level visibility is limited compared to .NET or Java.
* In conjunction with unsupported third-party modules, context can be lost in asynchronous callbacks. In such cases, please contact a Dynatrace product expert via live chat within your Dynatrace environment.
* OneAgent version 1.279+ CPU times are not reported for Node.js services. These numbers were misleading, since by design a major part of any operation is handled asynchronously inside the Node.js runtime without the possibility to correlate the actual CPU time to a specific service.
* Web Streams, WebSocket Client are not supported.
* Node.js features marked as 'experimental' are not supported.
* Using the NPM module [esmï»¿](https://github.com/standard-things/esm) in [variant 1 for packagesï»¿](https://github.com/standard-things/esm/tree/3.2.25#getting-started) might result in reduced visibility (especially if used for the main application script). It's preferable to use variant 2 to preload `esm` via the `-r` command line option.
* There is currently only limited support for [ECMAScript modulesï»¿](https://nodejs.org/api/esm.html) (aka "ES6 modules"):

  + If the main script file itself is an ECMAScript module OneAgent version 1.219+ with [Agent preloading](/docs/whats-new/preview-releases#oneagent-1-219-nodejs-agent-preloading "Learn about our Preview releases and how you can participate in them.") enabled is needed for the OneAgent to be injected into the Node.js process.
  + Instrumentation of ECMAScript modules is currently not available. This limits support for `kafkajs` in case the user defined entrypoint for the KafkaJs sensor is inside an ECMAScript module.
* **Webpack** bundles all modules into a single file by default. OneAgent is unable to instrument bundled modules. To work around this limitation, all modules that need to be instrumented by OneAgent (such as `express`, `mongodb`, and `pg`) need to be externalized in the webpack configuration. For details, see the [webpack externalsï»¿](https://webpack.js.org/configuration/externals/) documentation.
* Using **Webpack** or other bundlers might also have an impact on automatic vulnerability detection. This is because the software components cannot be detected, as they are hidden behind the bundler configuration and not available at runtime. Only packages that are deployed as external packages can be detected and reported.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Monitoring



* [How do I monitor Cloud Foundry applications?](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

### See also

* [Blog: Understanding Garbage Collection and hunting Memory Leaks in Node.jsï»¿](https://www.dynatrace.com/news/blog/understanding-garbage-collection-and-hunting-memory-leaks-in-node-js/)
* [Blog: How to track down CPU issues in Node.jsï»¿](https://www.dynatrace.com/news/blog/how-to-track-down-cpu-issues-in-node-js/)
* [Blog: All you need to know to really understand the Node.js Event Loop and its Metricsï»¿](https://www.dynatrace.com/news/blog/all-you-need-to-know-to-really-understand-the-node-js-event-loop-and-its-metrics/)