---
title: Update OneAgent on PPC BE Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-ppc-be-linux
scraped: 2026-02-16T21:15:55.440568
---

# Update OneAgent on PPC BE Linux

# Update OneAgent on PPC BE Linux

* Latest Dynatrace
* 1-min read
* Published Aug 21, 2019

To update an installed OneAgent instance on PPC BE follow the instructions below:

1. Redo all steps of the [initial installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux.") but install OneAgent to a new directory.
2. Stop all monitored processes.
3. Rename the current OneAgent installation directory (for example, `/opt/dynatrace/oneagent` to `/opt/dynatrace/oneagent-old`) and use the following command:

   ```
   mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old
   ```

   This folder can be deleted following OneAgent update.
4. Rename the updated OneAgent folder to point to the original installation directory (for example, from `/opt/dynatrace/oneagent-update` to `/opt/dynatrace/oneagent`) using the following command:

   ```
   mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent
   ```
5. Restart all processes that are to be monitored.

## Check installed version of OneAgent

Use one of these methods to check which version of OneAgent you currently have installed.

### OneAgent command-line interface

Run `oneagentctl` with the `--version` parameter. For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Host Overview

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Click the host you are interested in.
3. Expand **Properties** under the host's name. The installed version of OneAgent is included in the listed properties.

### Deployment status

1. Go to **Deployment Status**.
2. Click the **All hosts** or **Recently connected hosts** tab.
3. Expand the host entry you are interested in. The installed version of OneAgent is included in the information that shows up.