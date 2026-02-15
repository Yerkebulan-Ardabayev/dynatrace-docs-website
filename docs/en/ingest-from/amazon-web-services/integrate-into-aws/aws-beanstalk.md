---
title: Monitor AWS Elastic Beanstalk
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk
scraped: 2026-02-15T08:56:49.279960
---

# Monitor AWS Elastic Beanstalk

# Monitor AWS Elastic Beanstalk

* How-to guide
* 1-min read
* Published Jul 19, 2017

[AWS Elastic Beanstalkï»¿](https://aws.amazon.com/elasticbeanstalk/faqs/) is a service provided by Amazon Web Services (AWS) that gives you the option of deploying and auto-scaling applications and services.

As this type of installation depends heavily on user customizations, there isn't any set of steps that will work in all scenarios. The following aims to provide an overview of the entire process, with examples to help you create your own deployment.

## Prerequisites

* Locate the `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is shared during Dynatrace OneAgent installation.

Locate your installer URL

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

* Access to the AWS console

For configurations where OneAgent is already part of your application deployment, you don't have to manually install OneAgent or restart servers to enable service monitoring.

## Download OneAgent

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Windows** or **Linux**.

For more information, see the OneAgent installation instructions for [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.") or [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux "Learn how to download and install Dynatrace OneAgent on Linux.").

## Customize your installation

* Make sure the configuration files are properly formatted YAML files.
* Don't use tabs for indentation. Only spaces are allowed.
* The Elastic Beanstalk extension script file names are importantâthe Amazon interpreter executes them in alphabetical order.

Linux

Windows

To install OneAgent, you need two configuration files:

* One file for downloading the OneAgent installer
* Another file for invoking the installation and post-installation tasks.

1. In the Beanstalk deployment package, create a `.ebextensions` directory within the same directory as the main Beanstalk project source code. The two configuration files mentioned above must be placed in this directory.
2. Create a configuration file for downloading the installer named `0dynatraceDownload.config`.

   The file must contain a `files` section that defines:

   * The download path and target file name (for example, `/tmp/dynatraceinstall.sh`)
   * Proper user rights settings
   * The OneAgent download URL mentioned in the prerequisites.

   Example:

   ```
   files:



   "/tmp/dynatraceinstall.sh":



   mode: "000755"



   owner: root



   group: root



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=abcdefghijklmnopqrstu"
   ```

   Make sure to replace the generic values in the example above with your own.
3. Create a configuration file to execute the OneAgent installer and perform other tasks such as service restart, named `1dynatraceInstallAndPost.config`.

   In the example below, the script checks for an existing OneAgent setup and, if no OneAgent is found, executes the installation from the `/tmp` directory, setting the `--set-proxy=172.1.1.128:8080` installation parameter to connect the agent to a specific proxy. Then the `httpd` service is restarted.

   ```
   commands:



   install_dynatrace:



   cwd: /tmp



   command: "/bin/sh dynatraceinstall.sh --set-proxy=172.1.1.128:8080"



   restart_httpd:



   command: "service httpd restart"
   ```

   If you want to add more parameters, separate them with spaces. To learn more about installation parameters, see [how to customize OneAgent installation on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").

   Do not use the command's `env` property because it overwrites, rather than appends, the existing environment and will cause OneAgent installation to fail.
4. Optional Extend your configuration.

   You can also include steps to download OneAgent in your configuration.

   The example below includes OneAgent download in the configuration. While this is necessary for the first installation of OneAgent, it might substantially lengthen future application updates because you download OneAgent each time you run the script. To improve your Beanstalk configuration, add a check for an existing OneAgent installation and have your scripts download OneAgent only when it isn't found on the system.

   Inspect the following Linux configuration example carefully before creating your own scripts. The Amazon interpreter is sensitive to syntax errors. Take care in formatting and escaping special characters.

   ```
   files:



   "/tmp/dynatraceinstall.sh":



   mode: "000755"



   owner: root



   group: root



   content: |



   #!/bin/bash



   if [ ! -d /opt/dynatrace/oneagent ]; then



   wget -O /tmp/Dynatrace-OneAgent.sh "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=abcdefghijklmnopqrstu"



   chmod 755 /tmp/Dynatrace-OneAgent.sh



   sudo chown root:root /tmp/Dynatrace-OneAgent.sh



   sudo /tmp/Dynatrace-OneAgent.sh



   fi



   commands:



   install_dynatrace:



   cwd: /tmp



   command: "/bin/sh dynatraceinstall.sh --set-proxy=172.1.1.128:8080"



   restart_nginx:



   command: service nginx restart



   ignoreErrors: true
   ```

To install OneAgent, you need two configuration files:

* One file for downloading the OneAgent installer
* Another file for invoking the installation and post-installation tasks.

1. Create a configuration file for downloading the installer named `0dynatraceDownload.config`.

   The file must contain a `sources` section that defines:

   * The download destination (for example, your desktop)
   * The OneAgent download URL mentioned in the prerequisites.

   Example:

   ```
   files:



   "C:/OneAgent/Dynatrace-OneAgent-Installer.exe":



   source: "https://abcdefghij.live.dynatrace.com/api/v1/deployment/installer/agent/windows/default/latest?Api-Token=abcdefghijklmnopqrstu&arch=x86&flavor=default"
   ```

   Make sure to replace the generic values in the example above with your own.
2. Create a configuration file to execute the OneAgent installer and perform other tasks such as service restart, named `1dynatraceInstallAndPost.config`.

   The file must contain a `commands` section that defines the installation command for OneAgent.

   Do not use the command's `env` property because it overwrites, rather than appends, the existing environment and will cause OneAgent installation to fail.

   In the example below, the script executes the installer from the administrator's desktop folder in quiet mode (no graphical user interface involved). The file passes the `--set-proxy=172.1.1.128:8080` installation parameter to connect the agent to a specific proxy.

   ```
   commands:



   install_oneagent:



   command: "C:/OneAgent/Dynatrace-OneAgent-Installer.exe --quiet --set-proxy=172.1.1.128:8080"
   ```

   If you want to add more parameters, separate them with with spaces. To learn more about installation parameters, see [how to customize OneAgent installation on Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.").

   You don't need to add extra commands following OneAgent installation. Amazon will restart IIS on its own after you've successfully uploaded all your application files.

## Configure network zones Optional

To configure network zones, use the following argument: `--set-network-zone=<your.network.zone>`. See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Monitoring consumption

For AWS Elastic Beanstalk, monitoring consumption is based on hosts units. See [Application and Infrastructure Monitoring (Host Units)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.") for details.

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Limit API calls to AWS using tags](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Add and configure AWS tags to limit AWS resources.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")