---
title: Deploy OneAgent on Mesos/Marathon
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon
scraped: 2026-03-01T21:12:11.379559
---

# Deploy OneAgent on Mesos/Marathon

# Deploy OneAgent on Mesos/Marathon

* Latest Dynatrace
* 2-min read
* Published May 21, 2020

Mesos is a generic cluster resource manager which can be used together with the Marathon framework to run containers in distributed environments.

To monitor applications running in [Mesos clustersï»¿](https://www.dynatrace.com/technologies/mesos-monitoring/), we recommend that you deploy OneAgent on all Mesos agent nodes by means of a Marathon application deployment. Following this, install OneAgent on the Mesos master nodes, as explained on this page.

## Locate your OneAgent installer URL

The first step is to obtain the location for `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is presented to you during OneAgent installation.

To get your `ONEAGENT_INSTALLER_SCRIPT_URL`

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.

3. Determine the installer script URL and token from the UI-provided `wget` command:

OneAgent container image version 1.39.1000+

OneAgent container image version 1.38.1000 and earlier

This is the URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

* Replace the value of `arch` parameter with `<arch>`. Ignore the `flavor=default` parameter.
* For the `API-Token` value, you need a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Your URL should look like this:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

This your URL and API token.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Append the API token to the URL using the `API-Token` parameter. Your URL should look like this:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Install OneAgent

1. Deploy OneAgent on Mesos agent nodes.

   If you use DC/OS

   If you don't use DC/OS

   If you're using [DC/OSï»¿](https://www.dynatrace.com/technologies/dcos-monitoring/) to manage your Mesos cluster, you can take advantage of the Dynatrace package in the DC/OS universe. The universe package will automatically deploy Dynatrace to all your Mesos agent nodes.

   If you're not using [DC/OSï»¿](https://www.dynatrace.com/technologies/dcos-monitoring), you can run OneAgent as a Marathon application by following this example.

   * Use the `cat` command to create the `dynatrace-oneagent.json` file. Before you run it, edit the JSON part from the example below and replace the two placeholders with your Mesos cluster specific data:

     + `REPLACE_WITH_YOUR_URL` is the location for `ONEAGENT_INSTALLER_SCRIPT_URL` you determined earlier.
     + `REPLACE_WITH_NUMBER_OF_NODES` is the integer representing the number of nodes in your Mesos cluster.

   ```
   cat <<- EOF > dynatrace-oneagent.json



   {



   "id": "dynatrace-oneagent",



   "cpus": 0.1,



   "mem": 256,



   "instances": REPLACE_WITH_NUMBER_OF_NODES,



   "constraints": [["hostname", "UNIQUE"], ["hostname", "GROUP_BY"]],



   "container": {



   "type": "DOCKER",



   "volumes": [



   {



   "containerPath": "/mnt/root",



   "hostPath": "/",



   "mode": "RW"



   }



   ],



   "docker": {



   "image": "dynatrace/oneagent",



   "forcePullImage": true,



   "network": "HOST",



   "privileged": true,



   "parameters": [



   { "key": "pid", "value": "host" },



   { "key": "ipc", "value": "host" },



   { "key": "env", "value": "ONEAGENT_INSTALLER_SCRIPT_URL=REPLACE_WITH_YOUR_URL" },



   { "key": "env", "value": "ONEAGENT_INSTALLER_SKIP_CERT_CHECK=false "}



   ]



   }



   },



   "args": [



   ]



   }



   EOF
   ```

   * After you created the `dynatrace-oneagent.json` file, send an HTTP POST request to the Mesos master leader to deploy the Marathon application with OneAgent.

   ```
   curl -X POST -H "Content-Type: application/json" http://your-mesos-master:8080/v2/apps -d@dynatrace-oneagent.json
   ```
2. Deploy OneAgent on Mesos master nodes.

   Marathon doesn't allow you to deploy applications to master nodes (except for nodes that are tagged as both master and agent). This is why you must manually install OneAgent on all Mesos master nodes that aren't additionally configured as Mesos agents. For this, use the default [Linux installer](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.").

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")