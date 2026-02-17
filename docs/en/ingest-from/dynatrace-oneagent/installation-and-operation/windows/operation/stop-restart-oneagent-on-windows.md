---
title: Stop/restart OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows
scraped: 2026-02-17T04:53:55.448996
---

# Stop/restart OneAgent on Windows

# Stop/restart OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

## Restart using OneAgent command-line interface

When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.

```
.\oneagentctl.exe --set-proxy=my-proxy.com --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Stop OneAgent using the command line

If you use configuration management tools like Puppet or Ansible, you can stop the OneAgent service using the `net stop "Dynatrace OneAgent"` command, where `Dynatrace OneAgent` is the service name for OneAgent.

You can't stop the OneAgent service using the command line if that service is a part of another process, such as Java bytecode instrumentation. If you stop OneAgent service, monitoring will be disabled until the service is restarted.

## Start OneAgent using the command line

To start OneAgent again, use the following command:

`net start "Dynatrace OneAgent"`, where `Dynatrace OneAgent` is the service name for OneAgent.

Learn more about [how Dynatrace interacts with your OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").