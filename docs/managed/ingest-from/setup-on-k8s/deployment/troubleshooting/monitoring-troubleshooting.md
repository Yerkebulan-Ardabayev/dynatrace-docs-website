---
title: Monitoring issues troubleshooting
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting
---

# Monitoring issues troubleshooting

# Monitoring issues troubleshooting

* 1-min read
* Published Jul 28, 2023

This guide provides general troubleshooting steps and guidance for common issues encountered when using Dynatrace with Kubernetes. It covers how to access debug logs, use the `troubleshoot` subcommand, or generate a support archive.

If you need to manually collect OneAgent files or logs directly from Kubernetes nodes, see [Storage requirements](/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments") for exact storage paths.

* [Pods stuck in `Terminating` state after upgrade﻿](https://dt-url.net/lga38l5)
* [Unable to retrieve the complete list of server APIs﻿](https://dt-url.net/9m838d0)
* [`CrashLoopBackOff`: Downgrading OneAgent is not supported, please uninstall the old version first﻿](https://dt-url.net/3n838mb)
* [Crash loop on pods when installing OneAgent﻿](https://dt-url.net/tv0382u)
* [Deployment seems successful but the `dynatrace-oneagent` container doesn't show up as ready﻿](https://dt-url.net/ss638y7)
* [Deployment seems successful, however the `dynatrace-oneagent` image can't be pulled﻿](https://dt-url.net/lw238h9)
* [Deployment seems successful, but the `dynatrace-oneagent` container doesn't produce meaningful logs﻿](https://dt-url.net/38438k2)
* [Deployment seems successful, but the `dynatrace-oneagent` container isn't running﻿](https://dt-url.net/6r638b3)
* [Deployment was successful, but monitoring data isn't available in Dynatrace﻿](https://dt-url.net/wg237zk)
* [No pods scheduled on control-plane nodes﻿](https://dt-url.net/fk038ey)
* [Error when applying the custom resource on GKE﻿](https://dt-url.net/6ye38x5)
* [`CannotPullContainerError`﻿](https://dt-url.net/df837qz)
* [Limit log timeframe﻿](https://dt-url.net/lr6370p)
* [Dynatrace Kubernetes service creation fails when Istio is enabled﻿](https://dt-url.net/qd038te)
* [Application pods are stuck in terminating state﻿](https://dt-url.net/pf03ng8)
* [AKS WASM node-pools troubleshooting﻿](https://dt-url.net/qa03q47)