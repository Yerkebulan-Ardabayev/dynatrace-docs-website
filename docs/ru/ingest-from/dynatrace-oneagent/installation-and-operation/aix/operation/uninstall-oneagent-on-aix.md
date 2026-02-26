---
title: Uninstall OneAgent on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix
scraped: 2026-02-26T21:19:45.593813
---

# Uninstall OneAgent on AIX

# Uninstall OneAgent on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Sep 19, 2018

OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system. Go to the `/opt/dynatrace/oneagent/agent` directory and, using root rights, run the `uninstall.sh` script.

## Following uninstallation

Following uninstallation, log files and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at:

  + OneAgent version 1.203+ `/var/log/dynatrace/oneagent`
  + OneAgent version 1.201 and earlier `/opt/dynatrace/oneagent/log`
* Configuration files located at `/var/lib/dynatrace/oneagent/agent/config`.
* Clear the `LDR_PRELOAD` and the `LDR_PRELOAD64` environment variables.