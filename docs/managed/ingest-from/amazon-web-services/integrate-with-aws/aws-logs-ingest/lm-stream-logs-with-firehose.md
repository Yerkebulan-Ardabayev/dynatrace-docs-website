---
title: Stream logs via Amazon Data Firehose (Logs Classic)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose
---

# Stream logs via Amazon Data Firehose (Logs Classic)

# Stream logs via Amazon Data Firehose (Logs Classic)

* How-to guide
* 1-min read
* Published Mar 13, 2024

Log Monitoring Classic

Dynatrace Cluster version 1.288

Dynatrace integration with Amazon Data Firehose provides a simple and safe way to ingest AWS logs. To enable AWS log forwarding, you need to create Amazon Data Firehose instance and configure it with your Dynatrace environment as a destination. Then you can connect your CloudWatch log groups by creating a subscription filter or send logs directly to Data Firehose from services that support it (e.g. Amazon Managed Streaming for Apache Kafka). Data Firehose and other created cloud resources incur AWS costs according to standard AWS billing policy.
See the
[Cloud log forwarding page](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding#aws-log-forwarding "Learn how to configure AWS, Azure and Google Cloud log forwarding to ingest logs.") to learn about all the options for AWS log ingestion.

## Prerequisites

You need to have your Dynatrace Managed Cluster nodes open to incoming Internet traffic (or at least to AWS traffic) and configured with valid CA-signed SSL certificate to be able to receive logs from Amazon Data Firehose.

1. Create an [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") in your Dynatrace environment and enable the Ingest logs permission.
2. Determine the API URL for your environment:

   * **For Dynatrace Managed** Recommended
     `https://<your_domain>/e/<your_environment_ID>`

   * **For ActiveGate** ([additional setup required](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose#environment-activegate-support "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput."))
     `https://<your_active_gate_IP_or_hostname>/e/<your_environment_ID>`

     To determine `<your_environment_ID>`, see [What's a monitoring environment?](/managed/discover-dynatrace/get-started/monitoring-environment#environment-id "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").

## Set up Firehose logs streaming

You can set up an Amazon Data Firehose delivery stream with a CloudFormation template or in the AWS console. Check the instructions below.

If you choose another deployment method (for example, Terraform or custom script), use the full URL: `https://<your_domain>/e/<your_environment_ID>/api/v2/logs/ingest/aws_firehose` in the Firehose HTTP endpoint destination configuration.

With a CloudFormation template

In the AWS console

CloudFormation allows you to deploy an Amazon Data Firehose delivery stream using a single deployment command to create a stack that groups multiple AWS resources. This approach is faster and makes AWS resource management easier.

### Deploy the Amazon Data Firehose delivery stream

To fetch the CloudFormation template and deploy it to your AWS account, run the command below.

Make sure to replace `<your_API_URL>` and `<your_API_token>` with your values.

Consult the parameters table that follows for more details.

| Parameter | Description | Default value |
| --- | --- | --- |
| `DYNATRACE_API_URL` | Required Your API URL. See [Prerequisites](#prerequisites) for instructions. |  |
| `DYNATRACE_API_KEY` | Required Your API token. See [Prerequisites](#prerequisites) for instructions. |  |
| `STACK_NAME` | Required The name of your stack. | `dynatrace-log-delivery-stream` |

If you have AWS CLI configured, you can use a Bash-compliant shell. Otherwise, you can use CloudShell available in the AWS console.

```
DYNATRACE_API_URL=<your_API_URL>



DYNATRACE_API_KEY=<your_API_token>



STACK_NAME=dynatrace-log-delivery-stream



wget -O dynatrace-firehose-log-stream.yaml https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-log-stream.yaml && \



aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-firehose-log-stream.yaml --stack-name $STACK_NAME --parameter-overrides DtApiUrl=$DYNATRACE_API_URL DtApiToken=$DYNATRACE_API_KEY
```

### Confirm that the Amazon Data Firehose delivery stream was deployed correctly

To ensure that the Amazon Data Firehose delivery stream was deployed correctly, follow the steps below:

1. In the AWS console, go to **CloudFormation**.
2. Select the stack you have created in the CloudFormation deployment.
3. On the **Events** tab, make sure that all events have completed successfully and there are no failed events.
4. In **Parameters** tab, make sure that all parameters you have provided have correct values.
5. In the **Output** tab, take a note of the outputs:

   * `CloudWatchSubscriptionFilterRoleArn` - ARN of the IAM role to use when creating CloudWatch subscription filter;
   * `FirehoseArn` - ARN of the newly created Firehose delivery stream.

### Create Amazon Data Firehose delivery stream

1. In the AWS console, open **Amazon Data Firehose** service.
2. Select **Create Firehose stream**.
3. Choose **Source**, and select **Direct PUT**.
4. Choose **Destination**, and select **Dynatrace**.
5. Enter **Firehose stream name**.
6. Make sure data transformation is disabled.
7. In **Ingestion type**, make sure **Logs** is selected.
8. In **API token**, enter your API token. See Prerequisites for instructions.
9. In **API url**, enter your API URL. See Prerequisites for instructions.
10. In **Content encoding**, make sure **GZIP** is selected.
11. In **Retry duration**, enter `900` seconds.
12. In **Buffer hints**, set the **Buffer size** to `1` MiB and **Buffer interval** to `60` seconds.
13. In **Backup settings**, make sure **Failed data only** is selected.
14. In **S3 backup bucket**, select **Create**.
15. In **Create bucket** section, enter the S3 backup bucket name, optionally choose a region, and then select **Create bucket**.
16. Browse and choose created **S3 backup bucket**.
17. Select **Create Firehose Stream**.

### Create IAM role for streaming CloudWatch Logs to Firehose

Data Firehose stream requires trust relationship with CloudWatch through an IAM role. This role needs to be created first, before creating CloudWatch Logs subscription filter.

1. In the AWS console, go to **IAM > Policies**.
2. Select **Create policy**.
3. Switch to JSON editor and paste the JSON below as policy content.

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Sid": "VisualEditor0",



   "Effect": "Allow",



   "Action": [



   "firehose:PutRecord", "firehose:PutRecordBatch"



   ],



   "Resource": "*"



   }



   ]



   }
   ```

   You can replace `*` with your Firehose arn if you want to have more restrictive policy.
4. Select **Next**, enter the **Policy name**, optionally add tags, and select **Create policy**.
5. In the AWS console, go to **IAM > Roles**.
6. Select **Create role**.
7. Select **Custom trust policy** and paste the JSON below as policy content.

   ```
   {



   "Version": "2012-10-17",



   "Statement": [



   {



   "Sid": "Statement1",



   "Effect": "Allow",



   "Principal": {



   "Service": "logs.amazonaws.com"



   },



   "Action": "sts:AssumeRole"



   }



   ]



   }
   ```
8. Select **Next** and choose Firehose write policy created in step 4.
9. Select **Next**, enter **Role name**, optionally add tags, and select **Create role**.

## Stream logs from CloudWatch

To learn about streaming CloudWatch Logs from log group in other region or other account, see [Cross-account cross-Region log data sharing using Firehose﻿](https://dt-url.net/mn03w1l).

After creating a Firehose delivery stream and IAM role, you need to subscribe to the CloudWatch log groups whose logs you want to forward to Dynatrace.
You can subscribe to log groups using shell script or in the AWS console. See the instructions below.

Using shell script

In the AWS console

To fetch the shell script, run the command below in a bash shell.

```
wget -O dynatrace-firehose-logs.sh https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-logs.sh && chmod +x dynatrace-firehose-logs.sh
```

If you have AWS CLI configured, you can use a Bash-compliant shell. Otherwise, you can use CloudShell, which is available in the AWS console.

### Subscribe by listing log group names

**Usage recommendation:** Use this option if the number of log groups you'd like to subscribe to is small.

**To subscribe:** Run the command below, making sure to replace `<your_log_group_list>` with a space-separated list of the log group names you want to subscribe to.

**Example list:** `/aws/lambda/my-lambda /aws/apigateway/my-api`

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list>
```

No additional parameters are needed if the Firehose delivery stream was created with a CloudFormation template using the default stack name.

Add `[--stack-name <your_stack_name>]` parameter if you used a different stack name.

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --stack-name <your_stack_name>
```

If the Firehose delivery stream was created in a different way (AWS console or other tools), add the following parameters:

* `[--firehose-arn <firehose_arn>]`
* `[--role-arn <role_arn>]`

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --firehose-arn <firehose_arn> --role-arn <role_arn>
```

### Subscribe by reading log groups from file

**Usage recommendation:** Use this option if the number of log groups you'd like to subscribe to is large.

1. Create a file and enter each log group name on a separate line.
2. Save the file.
3. Run the command below, making sure to replace `<your_file_name>` with the actual file name.

   ```
   ./dynatrace-firehose-logs.sh subscribe --log-groups-from-file <your_file_name>
   ```

Log groups auto-discovery

To simplify file creation, you can use the auto-discovery command below to list the names of all log groups in your account. You can adjust the list manually before subscribing.

Make sure to replace `<your_log_groups_file>` with the name of the file to which you want to redirect the output.

```
./dynatrace-firehose-logs.sh discover-log-groups > <your_log_groups_file>
```

### Subscribe with a subscription filter pattern

**Usage recommendation:** By default, you subscribe to all the logs in the log group. Use this option if you want to restrict the logs you subscribe to. See [Filter and Pattern Syntax﻿](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) for details on the pattern syntax.

**Limitation:** You can use only two subscription filters per log group, so the possibility of creating multiple filters with different patterns is limited. If you create a subscription filter that exceeds the limit, an AWS `LimitExceededException` occurs.

**To subscribe:** Run the command below, making sure to replace `<your_log_group_list>` and `<your_filter_pattern>` with your values.

```
./dynatrace-firehose-logs.sh subscribe --log-groups <your_log_group_list> --filter-pattern <your_filter_pattern>
```

### Subscription usage and options Optional

For additional subscription options, see the commands below.

Consult the [Subscription parameters table](#subscription) for the commands below when replacing placeholders (`<...>`) with your values.

```
dynatrace-firehose-logs.sh subscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>}



[--stack-name <your_stack_name>] [--filter-pattern <your_filter_pattern>] [--role-arn <role_arn>] [--firehose-arn <firehose_arn>]
```

### Subscription parameters table

| Command-line parameter | Environment variable | Description | Default value |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | A space-separated list of log group names you want to subscribe to. For example: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | A file listing the log groups you want to subscribe to. The file should contain each log group name on a separate line. |  |
| `--filter-pattern` | `FILTER_PATTERN` | If set, it allows you to subscribe to a filtered stream of logs. | You subscribe to all logs in the log group. |
| `--stack-name` | `STACK_NAME` | The name of the CloudFormation stack where you have deployed the resources. | `dynatrace-aws-logs` |
| `--firehose-arn` | `FIREHOSE_ARN` | Specify to which Amazon Data Firehose instance the logs should be streamed by providing its ARN (Amazon Resource Name). **Usage recommendation:** Set this option if you haven't used CloudFormation template for creating delivery stream. | It will be extracted from the output of the CloudFormation stack used in the deployment step: either the `$DEFAULT_STACK_NAME` default value or the one specified with the `--stack-name <your_stack_name>` option. |
| `--role-arn` | `ROLE_ARN` | The ARN of an IAM role that grants CloudWatch Logs permission to deliver ingested log events to the destination stream. **Usage recommendation:** Set this option if you haven't used CloudFormation template for creating delivery stream. | It will be extracted from the output of the CloudFormation stack used in the deployment step: either the `$DEFAULT_STACK_NAME` default value or the one specified with the `--stack-name <your_stack_name>` option. |

## Unsubscribe from log groups

If you don't want to forward logs to Dynatrace anymore, use one of the two options below to unsubscribe from log groups.

### Unsubscribe by listing the log group names

Run the command below, making sure to replace `<your_log_group_list>` with a space-separated list of the log group names you want to unsubscribe from.

```
./dynatrace-firehose-logs.sh unsubscribe --log-groups <your_log_group_list>
```

### Unsubscribe by reading log groups from a file

Run the command below, making sure to replace `<your_file_name>` with the file name you created to [subscribe by reading log groups from file](#from-file).

```
./dynatrace-firehose-logs.sh unsubscribe --log-groups-from-file <your_file_name>
```

### Unsubscribe usage and options Optional

For additional unsubscribe options, see the commands below.

Consult the [Unsubscribe parameters table](#unsubscribe-table) for the commands below when replacing the placeholders (`<...>`) with your values.

```
dynatrace-firehose-logs.sh unsubscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>} [--stack-name <your_stack_name>]
```

### Unsubscribe parameters table

| Command-line parameter | Environment variable | Description | Default value |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | A space-separated list of log group names you want to unsubscribe from. For example: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | A file listing log groups you want to unsubscribe from, with each log group name on a separate line. |  |
| `--stack-name` | `STACK_NAME` | The name of the CloudFormation stack where you have deployed the resources. | `dynatrace-aws-logs` |

1. In the AWS console, go to **CloudWatch > Logs > Log Groups**.
2. Select log group details.
3. Select **Actions > Subscription filters > Create Amazon Data Firehose subscription filter**.
4. Select Firehose delivery stream created in previous steps.
5. Select IAM Role created in previous steps.
6. Enter subscription filter name.
7. Select **Start Streaming**.

## Send logs from other services directly to Firehose

To configure logs not stored in CloudWatch for services that send them directly to Firehose, refer to specific service documentation, for example:

* [Amazon Managed Streaming for Apache Kafka﻿](https://docs.aws.amazon.com/msk/latest/developerguide/msk-logging.html)
* [Amazon Virtual Private Cloud﻿](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-firehose.html)

For logs from AWS services that are sent to S3—not Firehose or CloudWatch—see [GitHub documentation﻿](https://github.com/dynatrace-oss/dynatrace-aws-s3-log-forwarder).

## View AWS logs

After configuring Data Firehose streaming, you can view and analyze AWS logs in Dynatrace: Go to **Logs & Events** or **Notebooks**, and filter for AWS logs. Logs ingested via Amazon Data Firehose will have `aws.data_firehose.arn` attribute set to ARN of Firehose that streamed the data into Dynatrace. Logs from AWS services with entity linking support will automatically be displayed in the Cloud application for in context analysis.

If you see logs coming in, you managed to configure AWS logs streaming successfully.

If there are no logs within 10 minutes, check out the Troubleshooting guide section of the page.

Amazon Data Firehose includes optional parameters (key-value pairs) in each HTTP call. These instance parameters can help you identify and manage your destinations since they're processed and added automatically to ingested log records as attributes.

**Supported services**

| Service name | Log enrichment | Entity linking |
| --- | --- | --- |
| AWS Lambda [1](#fn-1-1-def) | Applicable | Applicable |
| AWS App Runner | Applicable | Applicable |
| AWS CloudTrail [2](#fn-1-2-def) | Applicable | - |
| Amazon API Gateway | Applicable | - |
| Amazon SNS | Applicable | Applicable |
| Amazon RDS | Applicable | Applicable |
| All services that write to CloudWatch | Applicable | - |
| All Services that send logs to Data Firehose directly | - | - |

1

You can modify the AWS Lambda log group name. For log enrichment, use the default log group name `/aws/lambda/<function name>`.

2

You can modify the AWS CloudTrail log group name. For log enrichment, start the log group name with `aws-cloudtrail-logs`.

## Environment ActiveGate support

ActiveGate version 1.287+

By default, Environment ActiveGate listens for API requests on port 9999. However, currently, only port 443 is supported for HTTP endpoint data delivery for Amazon Data Firehose.

Your ActiveGate needs to be configured with a valid CA-signed SSL certificate to be able to receive logs from AWS Data Firehose.

To successfully deliver data from Amazon Data Firehose to the Environment ActiveGate API endpoint, we recommend setting up port forwarding from port 443 to 9999 on ActiveGate host.

Below we have included a few examples of such configurations. Consult the documentation specific to your operating system and networking solutions for details.

### Example configurations

#### Amazon Linux, RedHat Linux

`firewalld` provides a dynamically managed firewall. See the [documentation﻿](https://firewalld.org/documentation/) for details.

To add port forwarding with `firewalld` (note: this actions need to be done using the root account):

```
firewall-cmd --zone=public --add-forward-port=port=443:proto=tcp:toport=9999 --permanent



firewall-cmd --zone=public --add-port=9999/tcp --permanent
```

#### Ubuntu Linux

The Uncomplicated Firewall (`ufw`) is a frontend for iptables. See the [documentation﻿](https://wiki.ubuntu.com/UncomplicatedFirewall) for details.

To add port forwarding with `ufw` (note: this actions need to be done using the root account):

1. In the `/etc/ufw/before.rules` file, let’s add a NAT table after the filter table (the table that starts with `*filter` and ends with `COMMIT`):

```
*nat



:PREROUTING ACCEPT [0:0]



-A PREROUTING -p tcp --dport 443 -j REDIRECT --to-port 9999



COMMIT
```

2. Allow traffic through the 443 and 9999 ports:

```
ufw allow 443/tcp



ufw allow 9999/tcp
```

3. Restart `ufw`.

#### Windows Server 2022

Network shell (netsh) is a command-line utility that allows you to configure and display the status of various network communications server roles and components. See the [documentation﻿](https://learn.microsoft.com/en-us/windows-server/networking/technologies/netsh/netsh) for details.

To add port forwarding with `netsh interface portproxy`:

```
netsh interface portproxy add v4tov4 listenport=443 connectport=9999 connectaddress=<the current IP address of your computer>
```

Using the `netsh interface portproxy add` `v4tov6`/`v6tov4`/`v6tov6` options, you can create port forwarding rules between IPv4 and IPv6 addresses.

## Troubleshooting

In case the logs forwarded from Data Firehose are not available in your environment, follow the steps below:

1. Verify that logs from CloudWatch are sent into Firehose. Check Firehose Delivery stream metrics (Incoming put requests, Incoming bytes). When there is no data set into Firehose, verify that CloudWatch Logs group is producing current logs, verify that IAM role selected when creating subscription filter has permission to write logs into Firehose.
2. Verify that logs are successfully sent from Firehose to Dynatrace. Check Firehose Delivery stream metrics (HTTP endpoint delivery success, records delivered to HTTP endpoint). In case of errors, check AWS Firehose CloudWatch Logs and verify the Dynatrace API token and API URL.
3. Verify that logs are accepted by Dynatrace. Verify Dynatrace self-monitoring metric in data explorer:

```
dsfm:active_gate.rest.request_count:filter(and(or(eq(operation,"POST /logs/ingest/aws_firehose")))):splitBy(response_code):sort(value(auto,descending)):limit(20)
```

There should be metric data, and the `response\_code` should only have the value `200`.

## Limitations

The ingest throughput is limited by Amazon Data Firehose. For more details, see [Amazon Data Firehose Quota﻿](https://docs.aws.amazon.com/firehose/latest/dev/limits.html). Amazon can increase firehose limits on request.

AWS Firehose does not support connections through VPC for HTTP endpoints.