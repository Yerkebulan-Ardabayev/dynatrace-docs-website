---
title: Proxy for private locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations
scraped: 2026-02-25T21:30:14.716025
---

# Proxy for private locations

# Proxy for private locations

* Latest Dynatrace
* How-to guide
* Published Sep 11, 2025

You can incorporate [proxies, load balancers, and reverse proxies in your Dynatrace deployment](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#proxies "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents."). In particular, your ActiveGate configuration allows you to define one or more proxies for outgoing connections.

* To set up a proxy for communication with the tested resource, edit the [`custom.properties`](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.") file and set properties in the `[synthetic]` section.
* To set up a proxy only for internal communication with the Dynatrace Cluster, see [settings for Dynatrace Cluster communication only](/docs/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#internal "Learn how to configure ActiveGate properties to set up a proxy.").
* To set up the same proxy for both a tested resource and the Dynatrace Cluster, set properties in the `[http.client]` section.

## Proxy configuration properties

You can use the following properties when configuring a proxy for your Synthetic-enabled ActiveGate:

## Proxy connection scenarios

These are the possible scenarios for your proxy configuration. Access to tested resource via proxy is only supported for browser monitors and http monitors.

### Connect to the Dynatrace Cluster

```
[http.client]



proxy-server=<proxy>



proxy-port=8080



proxy-user=username



proxy-password=password



[synthetic]



proxy-off=true
```

### Connect to both the Dynatrace Cluster and tested resource

```
[http.client]



proxy-server=<proxy>



proxy-port=8080



proxy-user=username



proxy-password=password
```

### Connect to the Dynatrace Cluster and tested resources via different proxies

* Connect to the Dynatrace Cluster

  ```
  [http.client]



  proxy-server=<proxy>



  proxy-port=8080



  proxy-user=username



  proxy-password=password
  ```
* Connect to the tested resource

  ```
  [synthetic]



  proxy-server=<proxy between AG and tested resource>



  proxy-port=9090



  proxy-user=username_two



  proxy-password=password_two
  ```

### Connect to the tested resource and/or Amazon S3

The Synthetic-enabled ActiveGate needs access to the Amazon S3 service to upload and access screenshots for browser monitors on private locations.

```
[synthetic]



proxy-server=<proxy between AG and tested resource>



proxy-port=8080



proxy-user=username



proxy-password=password
```

For more information, see [Proxy Auto-Configuration (PAC) files](#proxy-auto-configuration-pac-files).

### Configure synthetic monitoring with direct connection to other resources

```
[synthetic]



proxy-server=<proxy between AG and tested resource>



proxy-port=8080



proxy-user=username



proxy-password=password



proxy-non-proxy-hosts=my.corp.org|*.gdansk.dynatrace.com
```

## Proxy Auto-Configuration (PAC) files

You can use Proxy Auto-Configuration (PAC) files to handle complex proxy configuration for private browser monitors.

### What is a PAC file?

A Proxy Auto-Configuration (PAC) file is a JavaScript function that determines whether web browser requests (HTTP, HTTPS, and FTP) go directly to the destination or are forwarded to a web proxy server (for details, see [Proxy Auto-Configuration (PAC) fileï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_%28PAC%29_file) on [developer.mozilla.orgï»¿](https://developer.mozilla.org/en-US/)).

### Provide a PAC file to your browser monitors

1. Go to ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.
2. Optional To filter the table for browser monitors, select **Browser** under **Filter options** on the left.
3. From the list of browser monitors, select the monitor for which you want to provide a PAC file. This displays a preview panel on the right.
4. Select **Edit** in the upper-right of the preview panel.

   From this point, you're redirected to previous Dynatrace where you can provide a PAC file URL.
5. Switch to the [script mode](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.").

   * For a clickpath, select **Recorded clickpath** > **Script**.
   * For a single-URL monitor, select **Monitor script**.
6. Add the following to the `configuration` object of the JSON file:

   ```
   "proxy": {



   "pacUrl": "https://www.example.com/test.pac"



   }
   ```

   `pacUrl` points to your hosted PAC file.

   ![Add a PAC file to a browser monitor.](https://dt-cdn.net/images/screenshot-2025-09-18-145741-826-11ee737f0f.png)

   For more information on script mode, see [Script mode for browser monitor configuration](/docs/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Create or edit your browser monitors in JSON format.").

### PAC file configuration compatibility

* PAC file configuration only applies to private Synthetic locations, not public locations.
* PAC file configuration applies only to the monitor you configureâeach individual monitor must have the PAC file configured in its script; there is no global setting for all monitors to use a PAC file for proxy services.

* When you set a PAC file proxy for one synthetic monitor script, it only applies to that monitor.

* If a PAC file is specified, it overrides the proxy settings specified at the ActiveGate level for communication with the tested resource. Specifically, it overrides the properties in the `[synthetic]` section.
* The PAC file must be served via HTTP/S.

## Proxy configuration for FIPS mode

When Synthetic location is installed in FIPS mode, browser monitor traffic must be routed through local intercepting proxy, so that all traffic leaving the host is encrypted with a crypto library that is FIPS-certified:

![FIPS proxy](https://dt-cdn.net/images/syn-proxy-for-fips-811-26fb991173.png)

In this example setup, we use the Squid proxy linked to the system's OpenSSL library, but you can use different proxy software as long as its crypto library is FIPS-certified.

1. Install proxy on the same host as Synthetic engine:

   Red Hat

   Ubuntu Pro

   ```
   sudo dnf install squid
   ```

   ```
   sudo apt install squid-openssl
   ```
2. Provide CA certificate for [re-signingï»¿](https://wiki.squid-cache.org/Features/DynamicSslCert) intercepted requests:

   Red Hat

   Ubuntu Pro

   ```
   sudo mkdir /etc/squid/ssl_cert



   sudo mv ~/prepared_ca_cert.pem /etc/squid/ssl_cert/squid.pem



   sudo chown --recursive squid:squid /etc/squid/ssl_cert



   sudo chmod 700 /etc/squid/ssl_cert



   sudo chmod 600 /etc/squid/ssl_cert/squid.pem
   ```

   ```
   sudo mkdir /etc/squid/ssl_cert



   sudo mv ~/prepared_ca_cert.pem /etc/squid/ssl_cert/squid.pem



   sudo chown --recursive proxy:proxy /etc/squid/ssl_cert



   sudo chmod 700 /etc/squid/ssl_cert



   sudo chmod 600 /etc/squid/ssl_cert/squid.pem
   ```

   If SELinux is enabled, you might need to adjust [file labelsï»¿](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/sect-security-enhanced_linux-working_with_selinux-selinux_contexts_labeling_files) to avoid permission errors.
3. Create temporary certificate cache:

   Red Hat

   Ubuntu Pro

   ```
   sudo /usr/lib64/squid/security_file_certgen -c -s /var/spool/squid/ssl_db -M 4MB



   sudo chown --recursive squid:squid /var/spool/squid/ssl_db
   ```

   ```
   sudo /usr/lib/squid/security_file_certgen -c -s /var/spool/squid/ssl_db -M 4MB



   sudo chown --recursive proxy:proxy /var/spool/squid/ssl_db
   ```
4. Configure the proxy to perform [SSL interceptionï»¿](https://wiki.squid-cache.org/Features/SslPeekAndSplice) (by default, `/etc/squid/squid.conf`):

   ```
   acl SSL_ports port 443



   acl Safe_ports port 80 443 1025-65535



   acl CONNECT method CONNECT



   http_access deny !Safe_ports



   http_access deny CONNECT !SSL_ports



   http_access allow localhost



   http_access deny all



   http_port 3128 ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=4MB cert=/etc/squid/ssl_cert/squid.pem



   acl step1 at_step SslBump1



   ssl_bump peek step1



   ssl_bump bump all



   cache deny all
   ```
5. Restart the proxy for configuration to take effect:

   ```
   sudo systemctl enable squid



   sudo systemctl restart squid
   ```
6. Verify that proxy is working correctly:

   ```
   curl --proxy localhost:3128 https://example.com
   ```
7. Optional If you chose a different proxy port, you need to adjust Synthetic configuration (by default, `/var/lib/dynatrace/synthetic/config/user.properties`):

   ```
   com.vuc.fips.proxy.port=3128
   ```

### Proxy configuration for FIPS mode with corporate proxy



If your organization mandates use of a corporate proxy, you need to set up a second local Squid instance due to limitations of Squid:

![FIPS proxy chain](https://dt-cdn.net/images/syn-proxy-for-fips-upstream-1141-ebd20f3425.png)

If you're using a different proxy software, this might not be applicable to you.

1. Configure proxy for FIPS, as described in the previous section.

   Squid version `5+` is required, so Red Hat version `8` and Ubuntu version `20` aren't supported.
2. On the same host, create a second squid service definition:

   Red Hat

   Ubuntu Pro

   `/usr/lib/systemd/system/squid2.service`

   ```
   [Unit]



   Description=Squid with upstream proxy



   After=network.target network-online.target nss-lookup.target



   [Service]



   Type=notify



   LimitNOFILE=16384



   PIDFile=/run/squid2.pid



   ExecStart=/usr/sbin/squid --foreground -n squid2 -f "/etc/squid/squid2.conf"



   ExecReload=/usr/bin/kill -HUP $MAINPID



   KillMode=mixed



   NotifyAccess=all



   [Install]



   WantedBy=multi-user.target
   ```

   `/lib/systemd/system/squid2.service`

   ```
   [Unit]



   Description=Squid with upstream proxy



   After=network.target network-online.target nss-lookup.target



   [Service]



   Type=notify



   PIDFile=/run/squid2.pid



   Group=proxy



   RuntimeDirectory=squid2



   RuntimeDirectoryMode=0775



   ExecStart=/usr/sbin/squid --foreground -sYC -n squid2 -f "/etc/squid/squid2.conf"



   ExecReload=/bin/kill -HUP $MAINPID



   KillMode=mixed



   NotifyAccess=all



   [Install]



   WantedBy=multi-user.target
   ```
3. Create a second proxy configuration (`/etc/squid/squid2.conf`) and provide your corporate proxy host, port and [authenticationï»¿](https://www.squid-cache.org/Doc/config/cache_peer):

   ```
   acl SSL_ports port 443



   acl Safe_ports port 80 443 1025-65535



   acl CONNECT method CONNECT



   http_access deny !Safe_ports



   http_access deny CONNECT !SSL_ports



   http_access allow localhost



   http_access deny all



   http_port 3129



   access_log daemon:/var/log/squid/access2.log squid



   cache_log /var/log/squid/cache2.log



   pid_filename /run/squid2.pid



   cache_peer upstream-proxy.example.com parent 443 0 default no-digest proxy-only login=proxyuser:proxypass tls tls-min-version=1.2 tls-options=NO_SSLv3



   never_direct allow all



   visible_hostname squid2



   cache deny all
   ```
4. Update first proxy configuration (`/etc/squid/squid.conf`) to use the second proxy as [parent proxyï»¿](https://wiki.squid-cache.org/Features/CacheHierarchy) by appending the following lines:

   ```
   cache_peer localhost parent 3129 0 default no-digest proxy-only



   never_direct allow all



   visible_hostname squid1
   ```
5. Restart both squid services:

   ```
   sudo systemctl daemon-reload



   sudo systemctl enable squid2



   sudo systemctl start squid2



   sudo systemctl restart squid
   ```
6. Verify that proxy chain is working correctly:

   ```
   curl --proxy localhost:3128 https://example.com
   ```

### Resource considerations

* Each Squid service requires an additional 500 MiB of RAM, which needs to be taken into account when choosing instance size for a particular workload.
* Requests going through multiple proxies will take longer, so performance metrics will be worse than those from a non-FIPS instance.