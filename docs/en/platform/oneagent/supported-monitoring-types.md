---
title: OneAgent monitoring capabilities
source: https://www.dynatrace.com/docs/platform/oneagent/supported-monitoring-types
scraped: 2026-02-18T05:38:54.759816
---

# OneAgent monitoring capabilities

# OneAgent monitoring capabilities

* Latest Dynatrace
* 3-min read
* Published Oct 12, 2018

OneAgent offers a rich set of monitoring capabilities.

## Real User Monitoring

Real User Monitoring analyzes the performance of all user interaction with your applications, whether the interactions take place in a browser or on a mobile device. Real user monitoring also enables application availability monitoring, verification of correct display of UI elements, third-party content provider performance analysis, backend service performance analysis (down to the code level), and performance analysis of all underlying infrastructure. For details, see [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.").

## Mobile app monitoring

OneAgent supports real user monitoring for mobile applications as well. The process of monitoring the user experience of your native mobile applications is fundamentally different from monitoring browser-based web applications. This is because mobile-app monitoring involves the compilation, packaging, and shipment of a monitoring library along with your own mobile application package. The process of instrumenting your mobile application largely depends on the platform of your mobile application. Dynatrace supports both Android and iOS platforms. For details, see [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.").

## Server-side service monitoring

Web applications consist of web pages that are served by web servers (for example, Apache Tomcat) and web containers (for example, Docker). The web requests that are sent to a specific Tomcat server are an example of a server-side service. Server-side services may be of various types like web services, web containers, database requests, and custom services. OneAgent can provide information such as which applications or services use which other services and whether or not a service makes calls to other services or databases. For details, see [Services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.").

## Network, process, and host monitoring

OneAgent enables monitoring throughout your entire infrastructure including your hosts, processes, and network. You can perform log monitoring and view information such as the total traffic of your network, the CPU usage of your hosts, the response time of your processes, and more. OneAgent also provides detailed topological information so that you know, for example, which processes run on which hosts and how your processes are interconnected. For details, see [Application & Infrastructure Observability overview (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

## Cloud and virtual machine monitoring

OneAgent monitors your entire stack, including private, public, and hybrid cloud environments. Whether you run on AWS, Azure, Cloud Foundry, or OpenStack, OneAgent auto-detects all virtualized components and keeps up with all changes. OneAgent can be integrated with your virtualized infrastructure, allowing you to connect the dots between the dependencies of the vCenters in your data center, the processes that run on them, and your applications. For details, see [Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

## Docker container monitoring

OneAgent seamlessly integrates with existing Docker environments and automatically monitors your containerized applications and services. Thereâs no need to modify your Docker images, modify run commands, or create additional containers to enable Docker monitoring. Simply install OneAgent on your hosts that serve containerized applications and services. OneAgent automatically detects the creation and termination of containers and monitors the applications and services contained within those containers. For details, see [Monitor container groups](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring").

## Root-cause analysis

A key feature of OneAgent is the ability to continuously monitor every aspect of your applications, services, and infrastructure and to automatically learn the baseline performance metrics related to these components. Dynatrace also automatically learns the baseline response times and failure rates of all requests that are vital to the success of your business. Based on these baseline values, Dynatrace determines when a detected slowdown or error-rate increase justifies the generation of a new problem event. For details, see [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.").

For a complete list of the technologies that can be monitored by OneAgent, please see [OneAgent capabilities](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").