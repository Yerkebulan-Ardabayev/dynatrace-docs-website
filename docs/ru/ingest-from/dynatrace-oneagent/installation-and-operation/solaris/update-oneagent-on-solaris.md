---
title: Update OneAgent on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/update-oneagent-on-solaris
scraped: 2026-02-18T21:28:36.129480
---

# Update OneAgent on Solaris

# Update OneAgent on Solaris

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

To update an installed OneAgent instance on Solaris (x86 and SPARC) follow the instructions below:

1. Redo all steps of the [initial installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") but install OneAgent to a new directory.
2. Stop all monitored processes.
3. Rename the current OneAgent installation directory (for example, `/opt/dynatrace/oneagent-old`) using the following command:

   `mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old`.

   This folder can be deleted following OneAgent update.
4. Rename the updated OneAgent folder to point to the original installation directory (for example, `/opt/dynatrace/oneagent`) using the following command:

   `mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent`
5. Restart all processes that are to be monitored.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.