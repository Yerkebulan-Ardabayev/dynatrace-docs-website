---
title: Use Live Debugger with your IDE
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/ide-integration
scraped: 2026-02-26T21:24:17.909647
---

# Use Live Debugger with your IDE

# Use Live Debugger with your IDE

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Dec 08, 2025

You can use ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** directly from your own integrated development environment (IDE). Currently, Dynatrace supports Visual Studio Code and the JetBrains suite.

## Requirements

### Visual Studio Code

* Minimum supported version: 1.85.0+

### JetBrains IDEs

* Minimum supported version: 2024.1
* Recommended version: 2025.1+ for the best experience

JetBrains updates their platform versions frequently. We recommend keeping your IDE updated to the latest version to ensure compatibility with the Live Debugger plugin.

## Visual Studio Code extension

Follow the steps below to set up and use the **Observability for Developers by Dynatrace** extension in Visual Studio Code.

### 1. Set up the extension

1. In Visual Studio Code, install the [Observability for Developers by Dynatraceï»¿](https://dt-url.net/6v03quu) extension.
2. From the Primary Side Bar, select  (**Dynatrace Debugger**). The **Dynatrace Debugger** configuration panel opensânormally, on the left of your IDE.
3. Select **Log in** to sign in to Dynatrace.
4. Under **Environment**, select the environment you'd like to debug. The environment list opens above, displaying all Dynatrace environments where you have Live Debugging permissions. Select an environment from the list.
5. Select **Customize session filters** to configure your debug session. Only instances with Live Debugging enabled appear. Select filters for the instances you'd like to debug, and select **Set**.

### 2. Add a Live Debugging breakpoint

You need to add a Live Debugging [breakpoint](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") in Visual Studio Code.

Right-click a code line number, and select **Add Live Debugging Breakpoint**. The breakpoint is applied to instances matching the filters and environment set in the previous steps.

### 3. View the data

When your breakpoints are triggered, the data streams into the **Dynatrace snapshots** panel in Visual Studio Code. Select **Open the Snapshot Panel** in the **Dynatrace Debugger** configuration panel, and then select a snapshot to see local variables, stack trace, process information, and tracing data.

### 4. Update debugging session configurationOptional

When required, you can access all session configuration options via the Primary Side Bar in Visual Studio Code. Select  (**Dynatrace Debugger**) to open the **Dynatrace Debugger** configuration panel.

### 5. Manage breakpointsOptional

* To add a breakpoint, right-click a code line number, and select **Add Live Debugging Breakpoint**.
* To open the breakpoint context menu, right-click the breakpoint icon. The following options are displayed:

  + **Breakpoint Status**
  + **Disable Breakpoint**
  + **Edit Breakpoint**
  + **Remove Breakpoint**
* To view the breakpoint list, select  (**Dynatrace Debugger**) from the Primary Side Bar in your IDE, and expand the **Live debugging breakpoints** section. Select a breakpoint in this list to view its status and editor.

## JetBrains plugin

Complete the steps below to configure and utilize the **Observability for Developers by Dynatrace** plugin in a JetBrains IDE.

### 1. Set up the plugin

1. Install the [Observability for Developers by Dynatraceï»¿](https://dt-url.net/pf23qui) plugin and restart your JetBrains IDE.
2. From the Tool window bar (usually located on the left), select  (**Observability for Developers**). The **Observability for Developers** panel opensânormally, at the bottom of the JetBrains IDE.
3. Select **Log in** to sign in to Dynatrace.
4. Expand the dropdown list in the panel header, and select the environment you want to debug. The environment list displays all Dynatrace environments where you have Live Debugging permissions.
5. Select **Filter Applications** in the panel header to configure your debug session.
   Only instances with Live Debugging enabled are displayed. Select filters for the instances you want to debug, and select **Set**.

### 2. Add a Live Debugging breakpoint

You need to add a Live Debugging [breakpoint](/docs/observe/application-observability/live-debugger/breakpoints "Learn how to add breakpoints, view available statuses, set breakpoint levels, and more.") in your JetBrains IDE.

Select the required code line number, and then select **Live Debugging Breakpoint**. The breakpoint is applied to instances matching the filters and environment set in the previous steps.

### 3. View the data

When your breakpoints are triggered, the data is streamed into the **Observability for Developers** panel. Select a snapshot to view local variables, stack trace, process information, and tracing data.

### 4. Update debugging session configurationOptional

When required, you can access all session configuration options via the header of the **Observability for Developers** panel in your JetBrains IDE. Open the panel and hover over the header to see the configuration options.

### 5. Manage breakpointsOptional

* To add a breakpoint, select the required code line number, and then select **Live Debugging Breakpoint** from the list.
* You can interact with your breakpoints directly from the code. Select the breakpoint icon to open the Breakpoint editor.
* Select **More** in the Breakpoint editor to access advanced editing options and view all breakpoints in this session.