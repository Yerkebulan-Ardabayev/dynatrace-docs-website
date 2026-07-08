---
title: Uninstall ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate
---

# Uninstall ActiveGate

# Uninstall ActiveGate

* 1-min read
* Published Jul 17, 2018

ActiveGate has a dedicated uninstall program. You'll need to run it to remove ActiveGate from your system.

* On Windows:  
  Go to **Control Panel** > **Programs and Features** and uninstall Dynatrace ActiveGate.
* On Linux:  
  Go to the `/opt/dynatrace/gateway` directory and, using root rights, run the `uninstall.sh` script.

## After uninstall

Following uninstallation, log files and part of the configuration are preserved in the ActiveGate [log and configuration directories](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.") respectively. You'll have to remove these files manually.