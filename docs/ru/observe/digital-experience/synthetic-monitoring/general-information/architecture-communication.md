---
title: Synthetic architecture and communication
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/general-information/architecture-communication
scraped: 2026-02-23T21:38:02.509346
---

# Synthetic architecture and communication

# Synthetic architecture and communication

* Explanation
* 3-min read
* Published Feb 27, 2025

Understand synthetic architecture and how your data securely flows through it. Learn about its main components and how they fit together to make everything work smoothly. By looking at the data flow, you can see how information moves around and gets processed and encrypted, ensuring the system runs efficiently.

## Architecture components

The following components are involved in the synthetic communication flow:

* **Dynatrace Cluster**âhosts the Synthetic monitors configuration, schedules monitors executions for private locations, and sends monitor configuration to public infrastructure if necessary.
* **Private location**âgroup of Synthetic ActiveGates, assigned to your monitor. The Dynatrace Cluster schedules executions for a private location.
* **ActiveGate**âcomponent used by the Synthetic engine to register and communicate with The Dynatrace Cluster.
* **Synthetic public infrastructure**âinfrastructure responsible for public location scheduling and configuration.
* **Public location**âgroup of Synthetic engines, assigned to your monitor. The Synthetic public infrastructure schedules executions for a public location.
* **Synthetic engine**âengine responsible for monitoring executions.
* **Beacon forwarder**âforwards the results from Synthetic engines to The Dynatrace Cluster.

![Architecture and communication for Synthetic](https://dt-cdn.net/images/synthetic-architecture-and-communication-2500-c31e40f6b2.webp)

## Communication and data flow

Depending on the location you use, the data flow varies. With the support of the diagram above, see how communication works for both private and public locations, and how tokens are involved in the process.

Each number corresponds to a step in the diagram above.

Private location communication

Public location communication

1. **Dynatrace Cluster to ActiveGate**

   The cluster provides the configuration, monitors definitions, and schedules executions. The data is encrypted through the [ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").
2. **Synthetic engine to ActiveGate**

   The Synthetic engine requests the configuration, and monitors definitions and executions from clusters via ActiveGate. The data is encrypted through the `synthetic token`, which is created on the ActiveGate start and stored in the `synthetic.token` file within your `config` foler. This token file is shared between ActiveGate and the Synthetic engine.
3. **Synthetic engine to beacon forwarder**

   The Synthetic engine sends results of the executions. The data is encrypted through the `synthetic monitors` token. The Dynatrace Cluster generates this token on a tenant level, and it rotates every 24 hours. Once a day, tokens that are older than 48 hours get deleted. The token is provided to the engine with execution details, and the communication is secured with the [ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").
4. **Beacon forwarder to Dynatrace cluster**

   The beacon forwarder forwards results sent by the engine to the cluster. The data is encrypted through the [ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").

5. **Dynatrace Cluster to Synthetic public infrastructure**

   The cluster provides monitors definitions, maintenance windows details, and tenant stateâincluding license state. The data is encrypted through the `synthetic monitors` token. The Dynatrace Cluster generates this token on a tenant level, and it rotates every 24 hours. Once a day, tokens that are older than 48 hours get deleted. The token is provided to the engine with execution details, and the communication is secured with the [ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").
6. **Synthetic engine to public infrastructure**

   The Synthetic engine requests configuration, monitors definitions and executions from the public infrastructure, and delivers diagnostic data. The data is secured on the network level.
7. **Synthetic engine to beacon forwarder**

   The Synthetic engine sends results of the executions. The data is encrypted through the `synthetic monitors` token. The Dynatrace Cluster generates this token on a tenant level, and it rotates every 24 hours. Once a day, tokens that are older than 48 hours get deleted. The token is provided to the engine with execution details, and the communication is secured with the [ActiveGate token](/docs/ingest-from/dynatrace-activegate/activegate-security "Secure ActiveGates with dedicated tokens.").