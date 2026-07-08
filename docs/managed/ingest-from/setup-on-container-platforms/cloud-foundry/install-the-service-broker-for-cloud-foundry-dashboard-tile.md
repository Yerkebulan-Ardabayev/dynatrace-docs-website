---
title: Install the Dynatrace Service Broker for Cloud Foundry dashboard tile
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile
---

# Install the Dynatrace Service Broker for Cloud Foundry dashboard tile

# Install the Dynatrace Service Broker for Cloud Foundry dashboard tile

* 3-min read
* Published Aug 03, 2018

Find out how to install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile (formerly Pivotal Platform), as well as how to set up application monitoring for the Dynatrace SaaS/Managed service by creating an instance of the service and binding it to an application.

## Install the Dynatrace Service Broker tile

Install the Dynatrace Service Broker tile through your **Ops Manager Installation Dashboard** by performing the following steps:

1. Download the product file from [Broadcom Support﻿](https://dt-url.net/nb03qvh).
2. Upload the product file from the **Ops Manager Installation Dashboard**.
3. Select **Add next** to the uploaded Dynatrace Service Broker tile in the **Ops Manager Available Products view** to add it to your staging area.
4. Select the newly added Dynatrace Service Broker tile to open the configuration options.
5. Select **Save**.

## Configure the Dynatrace Service Broker tile

Multiple Dynatrace SaaS/Managed environments can be supported simultaneously.

To configure the Dynatrace Service Broker tile, perform the following steps:

1. In **Tanzu Ops Manager**, select the Dynatrace Service Broker tile to open its configuration options.

   ![Pivotal 1](https://dt-cdn.net/images/configure-broker-1-1139-b706fcc7e1.png)

   Pivotal 1
2. Select **Assign AZs and Networks** to configure the network and availability zones.

   ![Pivotal 2](https://dt-cdn.net/images/pivotal2-918-717f876ef5.png)

   Pivotal 2
3. Go to **SaaS/Managed Plans**, and select the **Add** button at the upper right to add a service plan.

   ![Pivotal 3](https://dt-cdn.net/images/configure-broker-2-1400-bab7e386a3.png)

   Pivotal 3

   Perform the following steps to create and configure each service plan.

   * Enter a `Plan Name`.
   * Type your **Environment ID** and **Paas token**.
   * Type your **apiURL**.
   * Select **Save**.

   Adapt the `apiurl` setting according to your environment:

   For Dynatrace SaaS, where OneAgent can connect to the internet

   Replace the Dynatrace `ENVIRONMENTID` in `https://ENVIRONMENTID.live.dynatrace.com/api` with your own environment ID.

   For Dynatrace SaaS, where OneAgent can't connect to the internet

   Use `https://YourActiveGateIP:Port/api` or `FQDN:9999/e/<ENVIRONMENTID>/api` to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate.

   For Dynatrace Managed

   Use `https://YourActiveGateIP:Port/api`, or `https://FQDN/e/<ENVIRONMENTID>/api`, or the server IP address of your ActiveGate to connect to your server directly.
   Depending on your settings, you may need the port as well.
4. Select **Apply Changes**.

## Set up application monitoring

To set up application monitoring with the Dynatrace SaaS/Managed Service, bind the service to an application in [Apps Manager﻿](https://dt-url.net/3j23qbc) or use the [cf CLI﻿](https://dt-url.net/b543qgc). Run the command below to pass the parameters.

1. Create a service instance based on the plan(s) you have configured.

   ```
   cf create-service SERVICE PLAN SERVICE_INSTANCE
   ```

   * **SERVICE** needs to be `dynatrace`.
   * **PLAN** depends on the plans that have been configured in **Ops Manager**; in the example above, this would be `planname`.
   * **SERVICE\_INSTANCE** is the name of the `cf` service that will be created and which you need to bind to the application.
2. Bind the service to an application by using the [cf CLI﻿](https://dt-url.net/9b63qbn) for example.

   ```
   cf bind-service APP_NAME SERVICE_INSTANCE
   ```

   * **APP\_NAME**: the name of your App.
   * **SERVICE\_INSTANCE**: the name of the Service Instance you have created with the command above.

After binding the service to an application, [start using Dynatrace SaaS/Managed﻿](https://dt-url.net/6q03pwu).

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")