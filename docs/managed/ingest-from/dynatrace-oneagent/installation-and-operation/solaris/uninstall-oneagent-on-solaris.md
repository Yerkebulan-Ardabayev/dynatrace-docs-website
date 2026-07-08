---
title: Uninstall OneAgent on Solaris
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/uninstall-oneagent-on-solaris
---

# Uninstall OneAgent on Solaris

# Uninstall OneAgent on Solaris

* How-to guide
* 1-min read
* Published Nov 13, 2025

To uninstall OneAgent on Solaris, revert any configuration changes that were made when OneAgent was [installed](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).").

* Remove environment variables that are set.
  For example:

  + `DT_HOME`
  + `LD_PRELOAD`
* Restore any application configuration that reference OneAgent.
  For example:

  + `httpd.conf LoadModule`
* Delete any downloaded files.

Although these configuration options are common, your environment may require additional steps based on your configuration during install. For details specific to your setup, refer to the [installation guide](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") and reverse the steps you applied for your applications.

Reinstalling OneAgent

If the configuration files are removed and OneAgent is reinstalled, the host will appear as a new host with a different internal identifier.