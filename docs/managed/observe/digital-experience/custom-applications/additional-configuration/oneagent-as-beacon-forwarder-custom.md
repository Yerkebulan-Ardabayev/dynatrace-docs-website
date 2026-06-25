---
title: Use OneAgent as a beacon endpoint for custom applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom
scraped: 2026-05-12T11:34:04.731345
---

# Use OneAgent as a beacon endpoint for custom applications

# Use OneAgent as a beacon endpoint for custom applications

* How-to guide
* 1-min read
* Published Jan 30, 2023

OneAgent can be used as an alternative beacon endpoint to allow for a smooth transition to Dynatrace mobile RUM.

This is especially useful in cases where your Cluster ActiveGate is internal-only and it can't use a publicly available IP address. Dynatrace Managed can't be installed in such environments, and therefore can't manage the domain and create the trusted certificate.

The instrumented OneAgent server must be set up with one of the following technologies:

* Apache HTTP Server
* IBM HTTP Server
* Oracle HTTP Server
* Java servlet-based web applications (such as Tomcat and Wildfly)
* IIS
* NGINX
* Node.js

To use OneAgent as a beacon endpoint for your application

1. Go to **Frontend**.
2. Select the application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **General** > **Beacon Endpoint**.
5. From the **Type** dropdown list, select **Instrumented web server**.
6. Enter the web server or Java application server (servlet-based) URL in the following format:  
   `http(s)://<my-instrumented-server>:port/dtmb`
7. Select **Save changes**.
8. From the application settings, select **Instrumentation wizard**, and select the required operating system.
9. Build and test your mobile app to validate the configuration change.