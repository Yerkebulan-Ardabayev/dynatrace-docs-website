---
title: How to pass a proxy address during OneAgent installation on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows
scraped: 2026-02-22T21:12:00.568402
---

# How to pass a proxy address during OneAgent installation on Windows

# How to pass a proxy address during OneAgent installation on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

The Windows installer allows you to enter a proxy address during installation, so in the majority of cases you don't need to worry about adding extra command line parameters. Command line parameters are particularly useful when you're deploying a [Group Policy installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.") or other automated task.

The OneAgent installer recognizes the `--set-proxy` parameter. The value of the parameter is the proxy server address. Add the port number following a colon (for example, `172.1.1.128:8080`). For an authenticating proxy, you can specify the username and password like this `username:password@172.1.1.128:8080`, where both username and password need to be URL encoded. Dynatrace also supports IPv6 addresses.

Parameter names are case-sensitive, so use `ALL CAPS` for parameter names.

## Passing a proxy address to the installer

Let's say you've downloaded your OneAgent installer to the `C:\Users\Admin\Downloads` folder and your proxy IP address is `10.1.1.5`. In such a scenario you would begin the installation like this:

```
C:\Users\Admin\Downloads>Dynatrace-OneAgent-Windows-1.171.0.exe  --set-proxy=10.1.1.5
```

## Change proxy after installation

If you need to change the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").