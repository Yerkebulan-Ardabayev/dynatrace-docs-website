---
title: Uninstall OneAgent on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux
scraped: 2026-02-26T21:19:12.830301
---

# Uninstall OneAgent on Linux

# Uninstall OneAgent on Linux

* Latest Dynatrace
* 1-min read
* Updated on Oct 20, 2025

OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system.

Go to the `/opt/dynatrace/oneagent/agent` directory and, using root rights, run the `uninstall.sh` script.

## Following uninstallation

Following uninstallation, log files, the user running OneAgent, and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at:

  + OneAgent version 1.203+: `/var/log/dynatrace/oneagent`
  + OneAgent version 1.201 and earlier: `/opt/dynatrace/oneagent/log`
* Configuration files located at `/var/lib/dynatrace/oneagent/agent/config`.
* The user running OneAgent, `dtuser`.
* Optional If you use a custom installation path, the installer creates a symbolic link in the default directory (`/opt/dynatrace/oneagent`) to the custom installation path.
  This symbolic link needs to be removed manually after OneAgent is uninstalled.
  For more information, see [Installation path](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.").