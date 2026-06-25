---
title: Install OneAgent using Ansible
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/deployment-orchestration/ansible
scraped: 2026-05-12T11:35:18.354639
---

# Install OneAgent using Ansible

# Install OneAgent using Ansible

* 5-min read
* Published Sep 25, 2020

Dynatrace provides an Ansible collection that you can use to orchestrate OneAgent deployment in your environment.

## Requirements

* Ansible >= 2.15.0
* OneAgent version 1.199+
* Dynatrace version 1.204+
* Script access to OneAgent installer files

## Dependencies

### Windows

* pywinrm 0.4.3+

## Install the Dynatrace Ansible collection

The Dynatrace Ansible collection project is hosted on [GitHubï»¿](https://github.com/Dynatrace/Dynatrace-OneAgent-Ansible) and available via [Ansible Galaxyï»¿](https://galaxy.ansible.com/ui/repo/published/dynatrace/oneagent/).
To install the `dynatrace.oneagent` Ansible collection, run the following command:

```
ansible-galaxy collection install dynatrace.oneagent
```

The collection consists of a single Ansible role, which deploys OneAgent using a dedicated configuration.
The configuration ensures that the OneAgent service remains in a running state.
For more information, see [Using collectionsï»¿](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) in Ansible documentation.

## Configure the Dynatrace Ansible collection

The Ansible script requires access to the appropriate OneAgent installer files.

* If your Ansible control node has access to your Dynatrace environment, you can configure the script to download the installer files directly from the Dynatrace environment.
* Alternatively, you can download the appropriate installer files yourselfâusing the Dynatrace web UIâand upload them to the control node. This provides the script with local copies of the installers.

### Option 1: Use direct download from Dynatrace environment

The script utilizes [Deployment API](/managed/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API.") to download the platform-specific installers to the managed nodes.
You will need to specify the variables to supply the Ansible role with the information required to authenticate the API call in your environment:

* `oneagent_environment_url`:

  + **SaaS**: `https://{your-environment-id}.live.dynatrace.com`
  + **Managed**: `https://{your-domain}/e/{your-environment-id}`
* `oneagent_paas_token`

  + The [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") of your environment

    For example:

    ```
    # Set environment variables



    oneagent_environment_url: 'https://your-environment.live.dynatrace.com'



    oneagent_paas_token: 'abcdefjhij1234567890'
    ```

We recommend that you store both the PAAS-token and the environment-id securely, using encryption mechanisms such as Ansible Vault.
For details, see [Encrypting content with Ansible Vaultï»¿](https://docs.ansible.com/ansible/latest/user_guide/vault.html).

### Option 2: Use local installers

Use the Dynatrace web UI to download the required OneAgent installer files and then upload them to the control node.
The Ansible script will then copy the installer files to the managed nodes during execution.

Use the `oneagent_local_installer` variable to supply the Ansible role with the path of the installer file. For example:

```
oneagent_local_installer: /path/of/oneagent_linux_installer.sh
```

Note that Windows, Linux, and AIX require their dedicated installers. The original installer names, as downloaded from Dynatrace, include target platform designations. If you change the installer names, make sure the script can distinguish them.

If you don't specify a local installer, the script attempts to use the direct download method.

For sample usage, see the `local_installer.yml` file in [Examples](#examples).

## Variables

The OneAgent Ansible role supports the following variables:

| Name | Default | Description |
| --- | --- | --- |
| `oneagent_environment_url` | unset | The URL of the target Dynatrace environment (SaaS or Managed) |
| `oneagent_paas_token` | unset | The [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") retrieved from the **PaaS integration** page |
| `oneagent_local_installer` | unset | The path of the OneAgent installer stored on the control node |
| `oneagent_installer_arch` | Linux: `x86` Windows: `x86` AIX: `ppc` | The OneAgent installer architecture |
| `oneagent_version` | `latest` | The required version of the OneAgent in 1.199.247.20200714-111723 format |
| `oneagent_download_dir` | Linux/AIX: `$TEMP` or `/tmp` Windows: `%TEMP%` or `C:\Windows\Temp` | The installer download directoryâfor Linux and AIX, the directory must not contain spaces. |
| `oneagent_install_args` | unset | Dynatrace OneAgent installation parameters defined as a list of items |
| `oneagent_platform_install_args` | unset | Additional list of platform-specific installation parameters, appended to `oneagent\_install\_args' when run on the respective platform |
| `oneagent_preserve_installer` | `false` | Option to preserve the installer on the managed node after OneAgent installation |
| `oneagent_package_state` | `present` | Desired OneAgent package stateâspecify `present` or `latest` to install. Specify `absent` to uninstall. |
| `oneagent_reboot_host` | `false` | Option to reboot the managed node after OneAgent installation |
| `oneagent_validate_certs` | `true` | Option to require certificatesâif set to `false`, allows to download OneAgent from a server with an insecure SSL certificate (for example, expired or self-signed). |
| `oneagent_reboot_timeout` | 3600 | Timeout, in seconds, for rebooting the managed node |

## Logging

Instead of being printed to STDOUT, the logs produced by Ansible can be collected into a single file located on the managed node.
There are several ways to achieve this using Ansible configuration setting:

* Set the `ANSIBLE_LOG_PATH` environment variable to the path of the log file.
* Specify the `log_path` variable in the `[default]` section of Ansible's configuration settings file.

The verbosity of the logs can be controlled with the `-v` command-line option.
Repeating the option multiple times increases the verbosity level up to the connection debugging level, which is achieved with `-vvvv`.

## Examples

The following example playbook:

* Downloads a OneAgent installer of a specific version (`oneagent_version`) and saves it to a custom directory (`oneagent_download_dir`).
* Uses the `vars_files` variable to point to a secure `credentials.yml` file that stores your Environment ID and PaaS token.
* Instructs the script to deploy OneAgent on the host groups called `linux_other` and `linux_arm` in your inventory
* Instructs the script to use `x86` as the default architecture for the `linux_other` host group. The `linux_arm` host group has its own `oneagent_installer_arch` parameter specified in the inventory file.
* Uses the `oneagent_install_args` variable to specify the OneAgent installation parameters that assign the hosts to the `My.HostGroup_123-456` host group and to the `my.network.zone` network zone.
* Sets a different `USER` parameter using the `oneagent_platform_install_args` parameter for each host group in the inventory.

```
---



- name: Download OneAgent installer in specific version to a custom



directory with additional OneAgent install parameters. Both linux_other



and linux_arm have different user specified by platform args parameter.



hosts: linux_other,linux_arm



collections:



- dynatrace.oneagent



vars_files:



- encrypted_credentials.yml



vars:



oneagent_download_dir: /home/user1



oneagent_version: 1.199.247.20200714-111723



oneagent_install_args:



- INSTALL_PATH=/opt/example



- --set-host-group=My.HostGroup_123-456



- --set-network-zone=my.network.zone



tasks:



- import_role:



name: oneagent
```

You can find more example playbooks and inventory files in the `examples` directory within the Ansible role. The directory contains the following playbooks:

* `local_installer.yml` â OneAgent installation using a local installer.
* `advanced_config.yml` â OneAgent installation with a custom installation path and a download directory.
* `oneagentctl_config.yml` â OneAgent configuration using the `oneagentctl` command.

In addition, each directory contains an inventory file with a basic host configuration for playbooks.

For path issues when installing on Windows, review [Path Formatting for Windows in Ansible documentationï»¿](https://docs.ansible.com/ansible/latest/user_guide/windows_usage.html#path-formatting-for-windows).