---
title: Deploy OneAgent using AWS Systems Manager Distributor
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor
scraped: 2026-02-23T21:33:10.248846
---

# Deploy OneAgent using AWS Systems Manager Distributor

# Deploy OneAgent using AWS Systems Manager Distributor

* How-to guide
* 8-min read
* Updated on Jan 12, 2024

With the [AWS Systems Manager Distributorï»¿](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html) you can distribute and automatically deploy OneAgent on your EC2 instances using the AWS Systems Manager Distributor.

## Prerequisites

Before you start deploying the `DynatraceOneAgent` distributor package, make sure your Amazon EC2 instances meet the following prerequisites:

### AWS tags

AWS tags on instance metadata are turned off by default at launch. To allow them follow the official [AWS documentationï»¿](https://dt-url.net/k2038k6).

### AWS Systems Manager

AWS Systems Manager must be set up for your AWS account and AWS Systems Manager Agent (SSM Agent) must be installed on the EC2 instances where you want to deploy `DynatraceOneAgent` distributor package. Follow the [AWS Systems Manager Quick Setupï»¿](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) or more comprehensive [Setting up AWS Systems Managerï»¿](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html).

### Supported operating systems

The `DynatraceOneAgent` distributor package is supported on the following operating systems:

| Operating system | Version | Architecture |
| --- | --- | --- |
| Windows | [All OneAgent supported versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | x86-64, |
| Amazon Linux | [All OneAgent supported versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Ubuntu | 16.04, 18.04, 22.04 | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Red Hat Enterprise Linux | 8.x, 9.x | x86-64 |
| SUSE Enterprise Linux | 15.x | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |

1

Support for ARM64 architecture, including [AWS Graviton processorsï»¿](https://aws.amazon.com/ec2/graviton/), is in [Early Adopter releaseï»¿](https://www.dynatrace.com/news/blog/get-out-of-the-box-visibility-into-your-arm-platform-early-adopter/).

### Wget

Dynatrace OneAgent distributor package requires `Wget` installed on your Linux-based instance. If there's no `Wget` installed on your instance, the OneAgent distributor package will install it for you automatically. `Wget` is necessary to download the latest OneAgent version.

### AWS CLI

AWS CLI is required if you're using Parameter Store or Secrets Manager to store the PaaS token. If there's no AWS CLI installed, the OneAgent distributor package will install the latest version.

If your instance is running AWS CLI version 1, you need to add the `SSM_DYNATRACE_TOKEN_REGION` parameter with the region where your instance is running to the SSM Distributor configuration, as region autodiscovery via EC2 IMDS is only available in AWS CLI version 2.

## Limitations

Deploying OneAgent using AWS Systems Manager Distributor is currently not supported if you set Dynatrace Managed Cluster as the `SSM_DYNATRACE_URL` parameter value.

## Installation

To install the `DynatraceOneAgent` distributor package

1. Open the [AWS Systems Manager consoleï»¿](https://dt-url.net/ug6387o).
2. In the navigation panel, select **Distributor**.
3. On the Distributor page, select **Third party** and select the `DynatraceOneAgent` package.
4. Select the installation mode. You can install or update the `DynatraceOneAgent` package one time or schedule the installation. For details on installing the Distributor packages, see [AWS Systems Manager Distributor documentationï»¿](https://dt-url.net/bv438ci).
5. To configure the `DynatraceOneAgent` package installation, add the [parameters](#installation-parameters) to the **Additional Arguments** field of the **Systems Manager Run Command**.
   The parameters require a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

   To provide a PaaS token, we recommend using a centralized cloud secret management system, such as [AWS Secrets Managerï»¿](https://dt-url.net/2803808) or [Parameter Storeï»¿](https://dt-url.net/3y238xf).

   * Provide a PaaS token via **AWS Secrets Manager** Recommended

     1. Create a secret:

        ```
        aws secretsmanager create-secret --name dynatrace-paas-token --secret-string "paas_token_value"
        ```
     2. Add an IAM policy to the IAM role attached to your EC2 instance(s) that grants access to retrieve the secret from the Secrets Manager. Here's an example policy that's attached to the IAM role (other options can be found in the [AWS User Guideï»¿](https://dt-url.net/7k838d2)):

        ```
        {



        "Version": "2012-10-17",



        "Statement": [



        {



        "Effect": "Allow",



        "Action": "secretsmanager:GetSecretValue",



        "Resource": "arn:aws:secretsmanager:us-east-2:123456789012:secret:dynatrace-paas-token"



        }



        ]



        }
        ```

        If your Secret is encrypted with a CMK KMS Key, you also need to grant Decrypt permissions on both: the IAM role and the KMS Key policy. For more information, check the [AWS Secrets Manager documentationï»¿](https://dt-url.net/3pa38cu).
     3. Provide the secret name via `SSM_DYNATRACE_TOKEN_SECRET_ID` on the **SSM Distributor package parameters**. Example:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN_SECRET_ID" : "dynatrace-paas-token"



        }
        ```
   * Provide a PaaS token via **Parameter Store** Recommended

     1. Create a `SecureString` parameter type.

        ```
        aws ssm put-parameter --name "dynatrace-paas-token" --value "paas_token_value" --type "SecureString"
        ```
     2. Add an IAM policy to the IAM role attached to your EC2 instance(s) that grants access to retrieve the secret from the Parameter Store. Here's an example policy. For more information, check the [AWS Systems Manager Documentationï»¿](https://dt-url.net/3nc38v5).

        ```
        {



        "Version": "2012-10-17",



        "Statement": [



        {



        "Effect": "Allow",



        "Action": [



        "ssm:GetParameter"



        ],



        "Resource": "arn:aws:ssm:us-east-2:123456789012:parameter/dynatrace-paas-token"



        }



        ]



        }
        ```
     3. Provide the secret name via `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` on the SSM Distributor parameters. Example:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN" : "abcdefghij123456",



        }
        ```
   * Provide a PaaS token via `SSM_DYNATRACE_TOKEN` env variable. not-recommended

     Using the `SSM_DYNATRACE_TOKEN` parameter is not secure because the PaaS token will be visible in the [Run Commandï»¿](https://dt-url.net/bf038x6) history.

   Example: Additional arguments in Systems Manager Run Command

   ![AWS distributor](https://dt-cdn.net/images/aws-distributor-1281-19fb123371.png)

   ```
   {



   "SSM_DYNATRACE_URL" : "https://your-tenant.live.dynatrace.com/",



   "SSM_DYNATRACE_HOST_GROUP" : "MY-HOST-GROUP",



   "SSM_DYNATRACE_MONITORING_MODE" : "infra-only",



   "SSM_DYNATRACE_APP_LOG_CONTENT_ACCESS" : "true",



   "SSM_DYNATRACE_TOKEN_SECRET_ID" : "dynatrace-paas-token"



   }
   ```
6. Verify the installation.

   * After you run the installation, check the progress in the **Command status** area. When you see the **Success** status it means the installation was successful.

   Example: successful installation output

   ```
   Initiating DynatraceOneAgent_ 1.0.51 install



   Plugin aws:runPowerShellScript ResultStatus Success



   install output: Running install.ps1



   Installing Dynatrace OneAgent on Windows...



   script version: 1.0.51



   Configuration parameters:



   - Dynatrace URL: https://environment.live.dynatrace.com/



   --quiet



   Installing Dynatrace Package on Windows...



   - downloading agent from: https://environment.live.dynatrace.com/ to: %PROGRAMDATA%\Amazon\SSM\Packages\DynatraceOneAgent_\1.0.51\Dynatrace-OneAgent-Windows.exe



   - running installation



   - cleaning up



   Done



   Successfully installed DynatraceOneAgent_ 1.0.51
   ```

   * In Dynatrace, go to **Deployment Status**. Search for recently connected EC2 hosts to verify the result of the installation.
7. Restart all processes that you want to monitor. Youâll be prompted with a list of the processes that need to be restarted. Note that you can restart your processes at any time, even during your organizationâs next planned maintenance period. Though until all processes have been restarted, youâll only see a limited set of metrics, for example CPU or memory consumption.

## Installation parameters



The `DynatraceOneAgent` distributor package provides a number of Dynatrace-specific parameters that map directly to the following OneAgent installation parameters.

Learn more about customizing OneAgent installation on [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") and [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.").

Distributor parameter

Maps to OneAgent parameter

Default value

Description

`SSM_DYNATRACE_URL`

`--set-server`

environment specific

The address of the OneAgent communication endpoint, which is a Dynatrace component that OneAgent sends data to. Depending on your deployment, it can be a Dynatrace SaaS cluster or an ActiveGate. A Dynatrace Managed Cluster is currently not supported. **Note**: Make sure you add a trailing slash at the end of URL (for example, `https://environment.live.dynatrace.com/`).

`SSM_DYNATRACE_HOST_GROUP`

`--set-host-group`

unset

The name of a [host group](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") you want to assign the host to.

`SSM_DYNATRACE_MONITORING_MODE`

`--set-monitoring-mode`

fullstack

When set to `infra-only`, activates [Infrastructure Monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent."), in place of Full-Stack Monitoring mode. With this approach, you receive infrastructure-only health data, with no application or user performance data.

`SSM_DYNATRACE_APP_LOG_CONTENT_ACCESS`

`--set-app-log-content-access`

true

When set to `true`, allows OneAgent to access log files for the purpose of [Log Monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

`SSM_DYNATRACE_TOKEN_SECRET_ID` [1](#fn-2-1-def)

N/A

N/A

The [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Get acquainted with the concept of access tokens.") **secret** name or ARN in Secrets Manager, used to get the [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Get acquainted with the concept of access tokens.") value.

`SSM_DYNATRACE_TOKEN_PARAMETER_NAME` [1](#fn-2-1-def)

N/A

N/A

The [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Get acquainted with the concept of access tokens.") **parameter** name in Parameter Store, used to get the [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Get acquainted with the concept of access tokens.") value.

`SSM_DYNATRACE_TOKEN_REGION`

N/A

N/A

Optional AWS region used to get a secret from a different region. If not set, **the AWS CLI auto discovers the instance region**. (This parameter is **required** if you're running AWS CLI v1, as it can't discover the instance region from EC2 IMDS).

`SSM_DYNATRACE_TOKEN` not-recommended

N/A

N/A

The [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Get acquainted with the concept of access tokens.") used to download the OneAgent installer. Using the `SSM_DYNATRACE_TOKEN` parameter is not secure because the PaaS token will be visible in the Run Command history. Use AWS Secrets Manager or AWS Systems Manager Parameter Store.

1

Remember that `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` and `SSM_DYNATRACE_TOKEN_SECRET_ID` are mutually exclusive. Choose either one.

## Troubleshooting

* [My package installation fails with 'You need to specify 'Additional Arguments' error'ï»¿](https://dt-url.net/mt638ef)
* [My package installation fails with 'ERROR: wrong Dynatrace URL'ï»¿](https://dt-url.net/lj838gb)
* [My package installation fails with 'ERROR: Can't retrieve Dynatrace PaaS token from secret store'ï»¿](https://dt-url.net/uga38ao)

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")