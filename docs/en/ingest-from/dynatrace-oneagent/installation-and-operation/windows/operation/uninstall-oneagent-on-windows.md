---
title: Uninstall Dynatrace OneAgent on Windows
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows
scraped: 2026-02-06T16:31:01.793551
---

# Uninstall Dynatrace OneAgent on Windows

# Uninstall Dynatrace OneAgent on Windows

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

Your OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system.

## Uninstall OneAgent using Windows Control Panel

Use the Windows **Control Panel** to remove OneAgent.

After all OneAgent files have been removed from your system, you'll need to reboot your machine to remove the agent libraries from memory.

## Uninstall OneAgent silently

### Command line

To silently uninstall OneAgent using Windows command line, run the following WMIC commands as an administrator.

```
> wmic product where name='Dynatrace OneAgent' call uninstall /nointeractive
```

or

```
> wmic product where name='Dynatrace OneAgent' get IdentifyingNumber



IdentifyingNumber



{12345678-ABCD-1234-ABCD-12345678ABCD}



> msiexec /x {12345678-ABCD-1234-ABCD-12345678ABCD} /quiet /l*vx uninstall.log
```

You can omit `/l*vx uninstall.log` if the log file is not relevant to you.

### PowerShell

```
PS> $app = Get-WmiObject win32_product -filter "Name like 'Dynatrace OneAgent'"



PS> msiexec /x $app.IdentifyingNumber /quiet /l*vx uninstall.log
```

## After you uninstall OneAgent

Following uninstallation, log files, the user running OneAgent, and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.

For a complete OneAgent uninstallation, remove the following:

* Log files located at `%PROGRAMDATA%\dynatrace\oneagent\log`.
* Configuration files located at `%PROGRAMDATA%\dynatrace\oneagent\agent\config`.