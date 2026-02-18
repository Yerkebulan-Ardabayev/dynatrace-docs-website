---
title: Live Debugger
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger
scraped: 2026-02-18T05:41:00.298020
---

# Live Debugger

# Live Debugger

* Latest Dynatrace
* App
* 8-min read
* Updated on Dec 01, 2025

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** is a cloud native, live data collection app that gives you instant access to the code-level data you need to troubleshoot and debug quickly in any environment, from development to production.

* Access the necessary and relevant data without adding additional code, waiting for redeployment, or attempting to reproduce issues locally.
* Using non-breaking breakpoints, instantly see the complete state of your application, including stack trace, variable values, and more, all without stopping or breaking your running code.

## Prerequisites

* Dynatrace SaaS environment with a Dynatrace Platform Subscription (DPS) that includes [Code Monitoring](/docs/license/capabilities/container-monitoring#code-monitoring "Learn about the different container monitoring modes that are available with a Dynatrace Platform Subscription (DPS) license.")
* OneAgent version 1.309+ with **Java Live-Debugger** and **Node.js Live-Debugger** [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") enabled
* [Monitoring modes](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent."): Full-Stack, Infrastructure, or Discovery (with container code-module injection)
* [Code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#other-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms."): Java and Node.js

## Get started

![Real-time snapshot of debug data created once a non-breaking breakpoint has been triggered.](https://dt-cdn.net/hub/LiveDebugger_Ddll6iV.png)![Real-time snapshots with VS Code PlugIn](https://dt-cdn.net/hub/VSCode_2.png)![Real-time snapshots with JetBrains PlugIn](https://dt-cdn.net/hub/Jetbrains_1.png)

1 of 3Real-time snapshot of debug data created once a non-breaking breakpoint has been triggered.

### Activate the Live Debugger feature

To activate the Live Debugger feature

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Turn on **Java Live-Debugger**, **Node.js Live-Debugger**, or both, depending on your needs.
3. Restart any process that is affected.

### Enable Observability for Developers

To use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, you need to opt-in to Observability for Developers. You can enable it for specific process groups, Kubernetes namespaces, clusters, or the entire environment.

Environment level

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Observability for Developers** > **Enable Observability for Developers**.
2. Turn on **Enable Observability for Developers**.

Process group level

1. Go to **Technologies & Processes Classic**.
2. Select the category and then the required process group.
3. On the process group overview page, select **Settings**.
4. Go to **Observability for Developers** > **Enable Observability for Developers**.
5. Turn on **Enable Observability for Developers**.

Kubernetes namespaces and clusters level

1. Go to ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Select the required namespace or cluster.
3. In the upper-right corner, select  > **Connection settings** or, if not available, **Anomaly detection settings**.
4. Close the **Kubernetes namespace anomaly detection** or **Connection settings** overlay. You should see the namespace or cluster settings page.
5. Go to **Collect and capture** > **Observability for Developers** > **Enable Observability for Developers**.
6. Turn on **Enable Observability for Developers**.

### Enable Live Debugging in ActiveGate

ActiveGate version 1.311+

An ActiveGate isn't strictly required for ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** to work, but it significantly streamlines the process, especially in Kubernetes environments. It allows you to reduce your interaction with Dynatrace to one single point, which is available locally. Besides convenience, this solution optimizes traffic volume and reduces the complexity of the network and cost.

#### Host-based deployments

The Live Debugger module is enabled by default for host-based ActiveGate deployments starting from ActiveGate version 1.311.

#### Kubernetes Operator deployments

For Kubernetes Operator deployments, enable the Live Debugger module via the ActiveGate capabilities section in the DynaKube configuration.

To enable the Live Debugger module

1. Set `debugging` capability in the `DynaKube.yaml` file.

   ```
   activeGate:



   capabilities:



   - debugging
   ```

If you're using a proxy, configure it within the Environment ActiveGate as described in [Proxy for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate "Learn how to configure ActiveGate properties to set up a proxy.").

### Start live debugging an application

To start a live debugging session

1. Go to ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.
2. Select  (**Debug Configuration**) under the app header to open the **Customize your debug session** overlay.
3. Scope the instances you would like to debug.

   * Add one or more filters from the facets list.
   * Choose a filter within the application properties.

### Fetch source code

Each debug session must contain the application source code you're about to debug. ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets you quickly load sources from your local file system and various Git providers. When you integrate your source code into ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, it remains between your code repository and your local browser.

There are two main ways to import your source code:

* Automatic fetching
* Manual fetching

#### Automatic fetching

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** can connect to a repository and automatically fetch the source code for the selected instance.

Your repository can be automatically fetched for the selected instance based on your Git permissions if your admin has already set it up.

To learn more about automatic fetching, see [Integrate with your version control](/docs/observe/application-observability/live-debugger/additional-settings#integrate-with-your-version-control "Manage breakpoint permissions, configure OneAgent-related settings, set up the version control integration, and apply data masking rules.").

#### Manual fetching

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets you easily load your relevant source code into the application. Select  under **Source Code** to open a list of the supported Git providers from which you can fetch sources.

##### Git on-premises integration

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** integrates directly with the cloud editions of the following Git providers, both on-premises and SaaS:

* GitHub
* Bitbucket
* GitLab
* Azure DevOps

To enable ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** to integrate with your on-premises or locally hosted Git provider

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Apps** > **Git On-Premise Servers**.
2. Select **Add item**.

   * **Git Provider**: Specify your Git provider.
   * **Server URL**: Provide your server's HTTP/HTTPS URL.
3. Select **Save and close**.

To use Bitbucket On-Premises, install the [Dynatrace Desktop app](#local-file-system).

##### Local file system

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** includes a desktop application (**Dynatrace Desktop app**) that can access source repositories from your local file system. This allows you to fetch source code from locally hosted Git providers.

**Windows**: Versions 7, 8, and 8.1 aren't supported.
**MacOS**: All versions are supported.

1. Under **Source Code**, select  > **Local Filesystem**.
2. Select **Download desktop app** to get the installation file for the Dynatrace Desktop app.
3. Install the app according to the instructions in your operating system.

### Place a non-breaking breakpoint

To get real-time code-level data

1. Select the service you want to debug.
2. Navigate to the file system.
3. Set a non-breaking breakpoint on the line of code you want to debug.

[Non-breaking breakpoints](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") are reference breakpoints for the lines of code from which you want to collect debug data. These breakpoints don't stop your code from running. Instead, they carry the debug data collection request. Placing these breakpoints and receiving the derived snapshots don't affect your application or its users.

After placing a non-breaking breakpoint, ensure your code has been triggered so that the data is collected and appears immediately in ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.

### See the debug data

Once the non-breaking breakpoint is triggered, the collected data is displayed in the Snapshots Pane at the bottom of ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**.

Select the required snapshot to view the following information:

* All local variables and their values.
* Process information.
* Complete stack trace leading to the breakpoint.
* Tracing information from the running application.

You can also debug code up the stack from the stack trace view, including third-party components.

## Concepts

Application Observability
:   The inability to access code-level data on demand is a challenge that most developers face when troubleshooting and debugging application issues. Instead, they have to go through long deployment cycles and investigation of logs to find the relevant data they need to understand what's going on in their running code.

Live Debugger
:   ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** is a cloud native debugging and live data collection solution that gives instant access to the code-level debug data you need to troubleshoot and understand complex, modern applications with no extra coding, redeployments, or restarts.

    You can use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** in any environment, from development to production, and at any time, to instantly access the real-time data needed to get to the root cause of issues faster.

Dynamic logging
:   Developer teams often try to log as much as possible, as they're often not sure what data will be needed to debug an issue. This generates many unneeded logs and horrid signal-to-noise ratios.

    By shifting their logging mindset to Live Debugging, teams can reduce logging costs and, most importantly, the heavy effort required to support intense logging pipelines and cleanups.

Development collaboration
:   Collected debug data can be shared among team members when debugging application issues. This allows team members to have their own view of collected debug data and share that data with other team members for improved collaboration.

    As a result, ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** can become a single source of truth, the go-to place for developers to see reality as it is and collaborate on it.

On-demand trace inspection
:   ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** collects an object representation of traces used by your application. Developers can then correlate captured debug data with tracing data from your application.

Dev training and onboarding
:   Understanding new code can be challenging. It's twice as tricky when it's legacy code or, as often occurs, code written by someone else.

    ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** lets developers speed up their learning process by allowing them to observe unfamiliar code running in its native environment.

## Use cases

### Capture real-time debug data

* Instantly understand the state of your application using non-breaking breakpoints and get instant output, including your full stack trace, local and global variables, tracing data and context, and server metrics (CPU, memory, time measurements, and more).

### Troubleshoot faster

* Instantly debug the most complex flows.
* Fix bugs with zero friction, overhead, or risk.
* Get real-time data without stopping your app.
* Gain visibility into third-party dependencies and overcome debugging challenges from using open source components, external dependencies, or your legacy code.

### Dev-friendly debugging experience

* Empower your developers with on-demand access to code-level data.
* Get full visibility into your code with a simple and intuitive experience.
  Optimize R&D efficiency: Spend less time fixing bugs and more time developing value for your organization and customers.
* Never leave your comfort zone with the choice of either an IDE plugin or the Live Debugger web app.

### Test and optimize your code faster

* Instantly understand if specific line of code was reached at all with exploratory analytics

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub](https://www.dynatrace.com/hub/detail/live-debugger)