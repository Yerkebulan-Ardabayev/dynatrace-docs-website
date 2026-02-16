---
title: How to pass a proxy address during OneAgent installation on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux
scraped: 2026-02-16T21:16:11.493187
---

# How to pass a proxy address during OneAgent installation on Linux

# How to pass a proxy address during OneAgent installation on Linux

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

The OneAgent installer recognizes the `--set-proxy` (recommended since version 1.185) or `PROXY` parameters. The value of these parameters is the proxy server address. Add the port number following a colon, for example `172.1.1.128:8080`. For an authenticating proxy you can specify username and password like this `username:password@172.1.1.128:8080` where both username and password need to be URL encoded. We also support IPv6 addresses.

Parameter names are case sensitive, so use `ALL CAPS` for parameter names.

## Passing a proxy address to the installer

Let's say you're running an openSUSE server, you've downloaded your OneAgent installer to the `/tmp` directory and your proxy IP address is `10.1.1.5`. In such a scenario you would begin the installation like this:

```
cd /tmp



chmod +x Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh



su -c 'Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh --set-proxy=10.1.1.5'
```

## Change proxy after installation

If you need to change the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").