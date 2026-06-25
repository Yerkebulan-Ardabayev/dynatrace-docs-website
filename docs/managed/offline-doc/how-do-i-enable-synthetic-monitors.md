---
title: How do I enable synthetic monitors?
source: https://docs.dynatrace.com/managed/offline-doc/how-do-i-enable-synthetic-monitors
scraped: 2026-05-12T11:25:04.925366
---

# How do I enable synthetic monitors?

# How do I enable synthetic monitors?

* Published Jul 19, 2017

This topic applies to Dynatrace Managed installations only.

To enable synthetic monitors, your Dynatrace Managed deployment must be able to receive synthetic monitoring data from the Dynatrace cloud. For this to happen you must:

1. Install a [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") and
2. [Configure a public communication endpoint](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture.").

Once Dynatrace has validated that your Cluster ActiveGate can be reached from the Dynatrace cloud, you will be able to schedule synthetic monitors from all environments.

Agentless real user monitoring and mobile-app monitoring use the same endpoint to transmit monitoring data to Dynatrace.