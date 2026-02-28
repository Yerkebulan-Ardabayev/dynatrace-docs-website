---
title: Stop/restart OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/stop-restart-oneagent-on-aix
scraped: 2026-02-28T21:11:16.424421
---

# Stop/restart OneAgent on AIX

# Stop/restart OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:

1. Go to **Settings > Monitoring overview**.
2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.
3. Slide the **Monitoring** switch to the **Off** position.
4. Restart all processes for which monitoring has been disabled.

## Stop and start OneAgent using the command line

* [Restart OneAgent via `oneagentctl` command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
* If you use configuration management tools like Puppet or Ansible, you can alternatively stop the OneAgent service using the shell command. The `oneagent` service script is located in `<INSTALL_PATH>/agent/initscripts/`.

  To stop OneAgent, use root privileges and execute the `oneagent` service script with the `stop` parameter.

  If you stop OneAgent service, monitoring will be disabled until the service is restarted.

  To start OneAgent, use root privileges and execute the `oneagent` service script with the `start` parameter.

Learn more about [how OneAgent interacts with your OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix "Learn about Dynatrace OneAgent security and modifications to your AIX-based system.").