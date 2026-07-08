---
title: Stop/restart OneAgent on Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/stop-restart-oneagent-on-linux
---

# Stop/restart OneAgent on Linux

# Stop/restart OneAgent on Linux

* 1-min read
* Updated on May 20, 2026

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Select the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

Hot cloning

Hot cloning is generally not supported by OneAgent due to host ID generation requirements. When hot cloning a host with OneAgent installed, follow these steps to ensure proper functionality:

1. Stop OneAgent on the original host.
2. Clone the host.
3. Start OneAgent.
4. Perform process restarts on the new host.

## Restart using OneAgent command-line interface

When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.

```
./oneagentctl --set-proxy=my-proxy.com --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Stop OneAgent using the command line

If you use configuration management tools like Puppet or Ansible, you can alternatively stop the OneAgent service using the `systemctl stop oneagent` command.

If you stop OneAgent service, monitoring will be disabled until the service is restarted.

## Start OneAgent using the command line

To start OneAgent again, use the `systemctl start oneagent` command.

Learn more about [how Dynatrace interacts with your OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Learn about Dynatrace OneAgent security and modifications to your Linux-based system").