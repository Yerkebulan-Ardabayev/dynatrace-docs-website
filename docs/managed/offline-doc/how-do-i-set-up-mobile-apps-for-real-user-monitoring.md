---
title: How do I set up mobile apps for real user monitoring?
source: https://docs.dynatrace.com/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring
---

# How do I set up mobile apps for real user monitoring?

# How do I set up mobile apps for real user monitoring?

* Published Jul 19, 2017

This topic applies to Dynatrace Managed installations only.

Dynatrace Managed installations typically run within private data centers, where each incoming connection is restricted by a firewall. To enable instrumented mobile apps to report real user monitoring data to your Dynatrace Managed installation, you'll need to:

1. [Install a Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").
2. [Configure a public communication endpoint](/managed/managed-cluster/basics/managed-deployments "Understand how Dynatrace Managed deployments evolve from a basic internal setup to a globally distributed high-availability architecture."). A Cluster ActiveGate provides a secure IP address where your mobile apps can safely send their monitoring data. Use this public endpoint URL for your mobile app instrumentation configuration.

The Cluster ActiveGate is listening by default to port `9999`. If this isn't desired, it's possible to change this port in the [Cluster ActiveGate configuration](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements."). Alternatively, you can use the port of your choice and then redirect the traffic to port `9999` through the firewall settings.

Your existing publicly available ActiveGate URLs are available for viewing within your Dynatrace Managed installation at **Settings** > **Public endpoints**.

## Mobile app instrumentation

Based on your platform, follow the instructions below to enable your mobile app to send session information directly to your Dynatrace Managed cluster.

* [Android](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-android-app "Learn how to instrument mobile application monitoring on Android, how to customize instrumentation and more.")
* [iOS](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/dynatrace-auto-instrumentation-for-ios "Set up user experience monitoring for iOS apps within Dynatrace.")

## Troubleshooting

To investigate problems that you may encounter with mobile real user monitoring, check the following:

#### Is the certificate of the Cluster ActiveGate correct?

* Is the certificate root CA signed? [OneAgent for Android](/managed/discover-dynatrace/get-started/glossary#glossary-oneagent-android "Get acquainted with Dynatrace terminology.") and [OneAgent for iOS](/managed/discover-dynatrace/get-started/glossary#glossary-oneagent-android "Get acquainted with Dynatrace terminology.") require a special setting for working with self-signed certificates.
* Does the Cluster ActiveGate have a host name that matches the certificate? Certificate host name validation fails for IP addresses.

#### Is the Cluster ActiveGate reachable from the mobile app network?

* Using a mobile device browser, confirm that `timesync` delivers a valid response. For example, `https://<psg-url>:<port>/mbeacon?type=mts` should deliver something like `type=mts&t1=-1&t2=-1`.

#### Are you receiving a correct OneAgent configuration response from the Cluster ActiveGate?

* Using a mobile device browser, confirm if OneAgent configuration requests deliver a valid response. For example, `https://<psg-url>:<port>/mbeacon/<environment id>?type=m&app=<app id>`.
* Verify that the environment ID and the app ID are the same as those shown in the mobile OneAgent setup instructions for mobile apps.
* The response should start with `type=m` and should not contain `cp=0`. Such a value would mean that capture is disabled for this app ID and that it is an unknown app. The response may also contain other configuration values like `type=m&id=1&bl=150`.