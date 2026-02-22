---
title: Troubleshooting OneAgent installation on Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris
scraped: 2026-02-22T21:11:55.518681
---

# Troubleshooting OneAgent installation on Solaris

# Troubleshooting OneAgent installation on Solaris

* Latest Dynatrace
* 3-min read
* Published Sep 19, 2018

Find out how to solve problems related to installing OneAgent on Solaris.

SSL handshake failed

While downloading, you may encounter the following error:

```
Releasing 0x0000000239ae1890 (new refcount 1).



Initiating SSL handshake.



SSL handshake failed.



Closed fd 5



Unable to establish SSL connection.
```

This can be caused by selecting the wrong SSL or TLS protocol on handshake. As different operating systems act differently (both server and client side), you must specify some protocols manually under certain conditions.

For this specific case, to select the correct protocol, you must specify `--secure-protocol=tlsv1_2` as an additional parameter of the `wget` command. The command should appear as follows:

```
wget --secure-protocol=tlsv1_2



-O Dynatrace-OneAgent-Solaris-xxx-1.xxx.xxx.zip



"https://xxx/xxx/api/v1/deployment/installer/agent/solaris/paas/latest?Api-Token=xxx&arch=x86"
```

It can also be set permanently by creating the file `~/.wgetrc` with the following content:

`secureprotocol = tlsv1_2`

Could not find required opcodes in caller trying to resolve main

You may encounter the following error message when you start your Java application:

```
severe  [hooking   ] Could not find required opcodes in caller trying to resolve main
```

This happens if you use one of the unified monitoring scripts `dynatrace-agentXX.sh` but additionally have OneAgent referenced in `JAVA_OPTS`.

* Ensure that `dynatrace-java-env.sh` isn't called anywhere in your shell when you use the `dynatrace-agentXX.sh` script.
  `dynatrace-java-env.sh` is deprecated and should only be used as a fallback.
* Check for and remove the following parameter from your Java command line or startup scripts (specific directory may vary):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

Following this, the error message should go away.

LD\_PRELOAD\_64: parameter not set

You may encounter an error like this when you use `dynatrace-agentXX.sh` in a shell script.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LD_PRELOAD_64: parameter not set
```

This happens if use `set -u` to treat unset variables and parameters as errors. `dynatrace-agentXX.sh` does export variables which, though they may not yet exist in your script, are nevertheless needed and key to proper function. To overcome this, call `set +u` ahead of `dynatrace-agentXX.sh` in your script.

```
# avoid error



set +u



DT_HOME=/opt/dynatrace/oneagent



export DT_HOME



. $DT_HOME/dynatrace-agent64.sh
```

ld.so.1: sudo: warning: /opt/dynatrace/oneagent/agent/lib/liboneagentproc.so: open failed: illegal insecure pathname

You may encounter an error like this when you set `LD_PRELOAD` in your execution environment and call sudo or su. This happens because OneAgent isn't installed in the secure `ld_preload` directory. This error message has no negative impact and can be ignored. To avoid this, ensure that you don't set `LD_PRELOAD` in an execution context where you want to use sudo.

See [Further detail on this topicï»¿](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)

Why doesn't OneAgent start to monitor Apache process after restart?

Following installation of OneAgent, your Apache web server must be *completely* restarted to enable monitoring. To do this correctly, it's important to understand the difference between "partial" and "complete" restarts. In the case of partial restarts, the main Apache process re-reads its configuration files, re-opens its log files, and then restarts its worker processes. OneAgent however, requires a complete Apache web server restart in which all workers andâmost importantlyâthe main Apache process are shut down entirely and then restarted.

See [Stopping and Restarting Apache HTTP Serverï»¿](https://httpd.apache.org/docs/2.4/stopping.html) for more information on the different types of available restarts.

## How to perform a complete restart

You may be accustomed to restarting Apache by issuing an `apachectl restart` command. However, this command only results in a partial Apache restart.

To execute a complete Apache restart and enable deep monitoring with Dynatrace OneAgent, you need to first invoke a complete shutdown using the `apachectl stop` command. Only following this step can you restart the server using `apachectl start` .

It's fine to use `service apache2 restart` on Ubuntu systems. Note however that whatever commands you use, you'll likely need superuser rights (sudo).

I use WebLogic admin server to restart the managed nodes on Solaris. I can't set environment variables.

If you have trouble setting the environment variables

1. Shut down the managed nodes and Node Manager (make sure no process is running under the functional ID).
2. Back up the `$Domain_home/startNodeManagerMx.sh` script.
3. Modify the `startNodeManagerMx.sh` script to add the lines below.  
   (After running `commEnv.sh`, refer to the script under `/apps/wldomains/wls-aabb-1a` on `aaaabbb01a`).

   ```
   DT_HOME="/opt/dynatrace/oneagent"



   export DT_HOME



   source "$DT_HOME/dynatrace-env.sh"



   LD_PRELOAD="$DT_HOME/agent/lib/liboneagentproc.so"



   export LD_PRELOAD
   ```
4. Start a new session.
5. Start Node Manager.
6. Get a PID while Node Manager is working.

   Use the command line `$ pargs -e pid |grep LD` to see if the environment is there.

   Example:

   ```
   aabb@aaaabbb01a:/apps/wldomains/wls-aabb-1a$pargs -e 26531 |grep LD



   envp[27]: envp[28]: LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
   ```
7. Start managed nodes from the console.
8. Check the log directory to make sure a new log is generated:

   ```
   ls -ltr /opt/dynatrace/oneagent/log/java
   ```

For more details on setting up Oracle WebLogic monitoring, see [Configure Oracle WebLogic via startup script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris#weblogic "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).")