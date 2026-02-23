---
title: Google Cloud Hybrid Connectivity monitoring
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new/gcp-hybrid-connectivity-monitoring
scraped: 2026-02-23T21:29:50.549091
---

# Google Cloud Hybrid Connectivity monitoring

# Google Cloud Hybrid Connectivity monitoring

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jan 17, 2022

Dynatrace Google Cloud integration leverages data collected from the Google Operation API to constantly monitor health and performance of Google Cloud Services. While combining all relevant data into dashboards, it also enables alerting and event tracking.

## Prerequisites

[Set up integration](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")

## Add services and feature sets Optional

After integration, Dynatrace automatically monitors a number of preset Google Cloud services and feature sets (metrics). Besides these, you can add more services or feature sets to monitoring. For details, see [Add or remove services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8#manage "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.").

For a list of feature sets available for this service, see [Metric table](#table).

## View metrics

After deploying the integration, you can see metrics from monitored services in the [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser."), [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), and your dashboard tiles.

## Metric table

The following feature sets are available for Google Cloud Hybrid Connectivity.

| Feature set | Name | Unit | GCP metric identifier |
| --- | --- | --- | --- |
| gce\_router/default\_metrics | Received routes count | Count | router.googleapis.com/best\_received\_routes\_count |
| gce\_router/default\_metrics | BFD control packets receive intervals | MilliSecond | router.googleapis.com/bfd/control/receive\_intervals |
| gce\_router/default\_metrics | Control packets received | Count | router.googleapis.com/bfd/control/received\_packets\_count |
| gce\_router/default\_metrics | Control packets rejected | Count | router.googleapis.com/bfd/control/rejected\_packets\_count |
| gce\_router/default\_metrics | BFD control packets transmit intervals | MilliSecond | router.googleapis.com/bfd/control/transmit\_intervals |
| gce\_router/default\_metrics | Control packets transmitted | Count | router.googleapis.com/bfd/control/transmitted\_packets\_count |
| gce\_router/default\_metrics | BFD session status | Count | router.googleapis.com/bfd/session\_up |
| gce\_router/default\_metrics | BGP received routes count | Count | router.googleapis.com/bgp/received\_routes\_count |
| gce\_router/default\_metrics | BGP sent routes count | Count | router.googleapis.com/bgp/sent\_routes\_count |
| gce\_router/default\_metrics | BGP session status | Count | router.googleapis.com/bgp/session\_up |
| gce\_router/default\_metrics | BGP sessions down count | Count | router.googleapis.com/bgp\_sessions\_down\_count |
| gce\_router/default\_metrics | BGP sessions up count | Count | router.googleapis.com/bgp\_sessions\_up\_count |
| gce\_router/default\_metrics | Router status | Count | router.googleapis.com/router\_up |
| gce\_router/default\_metrics | Sent routes count | Count | router.googleapis.com/sent\_routes\_count |
| interconnect/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/interconnect/capacity |
| interconnect/default\_metrics | Dropped Packets | Unspecified | interconnect.googleapis.com/network/interconnect/dropped\_packets\_count |
| interconnect/default\_metrics | Circuit Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/link/operational |
| interconnect/default\_metrics | Circuit Receive Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/rx\_power |
| interconnect/default\_metrics | Circuit Transmit Power | Unspecified | interconnect.googleapis.com/network/interconnect/link/tx\_power |
| interconnect/default\_metrics | Operational Status | Unspecified | interconnect.googleapis.com/network/interconnect/operational |
| interconnect/default\_metrics | Ingress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/receive\_errors\_count |
| interconnect/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/interconnect/received\_bytes\_count |
| interconnect/default\_metrics | Ingress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/received\_unicast\_packets\_count |
| interconnect/default\_metrics | Egress Errors | Unspecified | interconnect.googleapis.com/network/interconnect/send\_errors\_count |
| interconnect/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/interconnect/sent\_bytes\_count |
| interconnect/default\_metrics | Egress Unicast Packets | Unspecified | interconnect.googleapis.com/network/interconnect/sent\_unicast\_packets\_count |
| vpn\_gateway/default\_metrics | Number of connections | Count | vpn.googleapis.com/gateway/connections |
| vpn\_gateway/default\_metrics | Incoming packets dropped | Count | vpn.googleapis.com/network/dropped\_received\_packets\_count |
| vpn\_gateway/default\_metrics | Outgoing packets dropped | Count | vpn.googleapis.com/network/dropped\_sent\_packets\_count |
| vpn\_gateway/default\_metrics | Received bytes | Byte | vpn.googleapis.com/network/received\_bytes\_count |
| vpn\_gateway/default\_metrics | Received packets | Unspecified | vpn.googleapis.com/network/received\_packets\_count |
| vpn\_gateway/default\_metrics | Sent bytes | Byte | vpn.googleapis.com/network/sent\_bytes\_count |
| vpn\_gateway/default\_metrics | Sent packets | Unspecified | vpn.googleapis.com/network/sent\_packets\_count |
| vpn\_gateway/default\_metrics | Tunnel established | Count | vpn.googleapis.com/tunnel\_established |
| interconnect\_attachment/default\_metrics | Network Capacity | BytePerSecond | interconnect.googleapis.com/network/attachment/capacity |
| interconnect\_attachment/default\_metrics | Ingress Bytes | Byte | interconnect.googleapis.com/network/attachment/received\_bytes\_count |
| interconnect\_attachment/default\_metrics | Ingress Packets | Unspecified | interconnect.googleapis.com/network/attachment/received\_packets\_count |
| interconnect\_attachment/default\_metrics | Egress Bytes | Byte | interconnect.googleapis.com/network/attachment/sent\_bytes\_count |
| interconnect\_attachment/default\_metrics | Egress Packets | Unspecified | interconnect.googleapis.com/network/attachment/sent\_packets\_count |

## Related topics

* [Google Cloud integrations](/docs/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")