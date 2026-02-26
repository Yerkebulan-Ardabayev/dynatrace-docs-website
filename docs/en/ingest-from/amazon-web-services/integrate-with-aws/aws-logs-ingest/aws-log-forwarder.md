---
title: Log monitoring with AWS log forwarder
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/aws-log-forwarder
scraped: 2026-02-26T21:30:05.697579
---

# Log monitoring with AWS log forwarder

# Log monitoring with AWS log forwarder

* How-to guide
* 13-min read
* Updated on May 08, 2024
* Deprecated

Deprecation and end of support for AWS log forwarder

The Dynatrace AWS log forwarder is now deprecated in favor of the new [Stream logs via Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput."), which allows ingesting cloud logs directly without any additional infrastructure and with increased throughput. To check the available alternative integrations, see [Set up Dynatrace on Amazon Web Services](/docs/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.").

End of support for the Dynatrace AWS log forwarder is planned for Dec 31, 2024.

DDU consumption for Log Monitoring

DDU pricing applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.

AWS log forwarding allows you to stream logs from Amazon CloudWatch into Dynatrace logs via an ActiveGate.

## Resources needed

To enable AWS log forwarding, you need to deploy our special-purpose CloudFormation stack into your AWS account. The stack consists of a Kinesis Firehose instance and a Lambda function. These resources incur AWS costs according to standard AWS billing policy. The same applies to included self-monitoring resources (CloudWatch dashboards and metrics).

**Supported services**

| Service name | CloudWatch log forwarding | Log enrichment | Entity linking |
| --- | --- | --- | --- |
| AWS Lambda | Applicable | Applicable | Applicable |
| AWS App Runner | Applicable | Applicable | Applicable |
| AWS CloudTrail [1](#fn-1-1-def) | Applicable | Applicable | - |
| Amazon API Gateway | Applicable | Applicable | - |
| Amazon SNS | Applicable | Applicable | Applicable |
| Amazon RDS | Applicable | Applicable | Applicable |
| All services that write to CloudWatch | Applicable | Applicable | - |

1

AWS CloudTrail log group name is chosen by user. For log enrichment, start the log group name with `aws-cloudtrail-logs`.

## Limitations

AWS log forwarder supports maximum 1 GB of data processing per hour in the default configuration.

* To measure the throughput, look for these Kinesis metrics in CloudWatch or check the dashboards provided by the deployed stack: `Delivery - log entries` and `Delivery - data volume`.
* To measure the latency, look for `Kinesis - record age`.

For scaling recommendations, see the [scaling guide](#scalingguide) below.

## Prerequisites

If you're using an earlier version of Dynatrace, see [Alternative deployments](#alternative) for instructions.

### Dynatrace

* [Enable generic log ingestion](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Create an API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with **Ingest logs** (API v2) permission

### CLI

* You can run the deployment from AWS CloudShell or from any machine with AWS CLI installed that supports Bash script execution.

The deployment script uses the default AWS CLI profile configuration. The profile will determine the AWS account and region. To change the account or region:

* Use a different profile - in this case, you need to [update your configuration fileï»¿](https://dt-url.net/le03r5f).
* Overwrite the default profile temporarily (this option is limited to your shell session) using [environment variablesï»¿](https://dt-url.net/3823r6v).

### Permission policy

You need the following permissions to run the deployment script:

Permissions policy for deployment

```
{



"Version": "2012-10-17",



"Statement": [



{



"Effect": "Allow",



"Action": [



"cloudformation:CreateChangeSet",



"cloudformation:ExecuteChangeSet",



"cloudformation:DescribeChangeSet",



"cloudformation:DescribeStackEvents",



"cloudformation:DescribeStacks",



"cloudformation:GetTemplateSummary",



"ec2:DescribeImages",



"s3:CreateBucket",



"s3:PutLifecycleConfiguration",



"s3:PutBucketPublicAccessBlock",



"iam:GetRole",



"iam:CreateRole",



"iam:AttachRolePolicy",



"iam:PutRolePolicy",



"iam:GetRolePolicy",



"iam:PassRole",



"lambda:CreateFunction",



"lambda:UpdateFunctionCode",



"lambda:GetFunction",



"lambda:GetFunctionCodeSigningConfig",



"cloudwatch:PutDashboard",



"cloudwatch:GetDashboard",



"firehose:DescribeDeliveryStream",



"firehose:CreateDeliveryStream",



"firehose:ListTagsForDeliveryStream",



"logs:DeleteSubscriptionFilter",



"logs:DescribeLogGroups",



"logs:PutSubscriptionFilter",



"ssm:GetParameters"



],



"Resource": "*"



}



]



}
```

## Deploy

1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values.

   * For `TARGET_URL`, enter your environment URL: `https://<your_environment_ID>.live.dynatrace.com`. To learn how to determine your environment ID for the SaaS or Managed deployment, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * For `TARGET_API_TOKEN`, enter your API token. For instructions, see [Prerequisites](#dynatrace).
   * Optional For `STACK_NAME`, the default value is `dynatrace-aws-logs`. To provide another name for the CloudFormation stack where you want to deploy the resources, replace the default value with your own.

   ```
   TARGET_URL=<your_environment_URL>



   TARGET_API_TOKEN=<your_API_token>



   STACK_NAME=dynatrace-aws-logs
   ```
2. Download the script and deploy the infrastructure.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --stack-name $STACK_NAME --require-valid-certificate true
   ```

## Subscribe to log groups

After deploying the infrastructure, you need to subscribe to the log groups whose logs you want to forward to Dynatrace.

To subscribe to log groups, you have the options described below.

Use parameter `[--stack-name <your_stack_name>]` in case you changed the default value during deployment.

### Subscribe by listing log group names

**Usage recommendation:** Use this option if the number of log groups you'd like to subscribe to is small.

**To subscribe:** Run the command below, making sure to replace `<your_log_group_list>` with a space-separated list of the log group names you want to subscribe to.

**Example list:** `/aws/lambda/my-lambda /aws/apigateway/my-api`

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list>
```

### Subscribe by reading log groups from file

**Usage recommendation:** Use this option if the number of log groups you'd like to subscribe to is large.

1. Create a file and enter each log group name on a separate line.
2. Save the file.
3. Run the command below, making sure to replace `<your_file_name>` with the actual file name.

   ```
   ./dynatrace-aws-logs.sh subscribe --log-groups-from-file <your_file_name>
   ```

Log groups auto-discovery

To simplify file creation, you can use the auto-discovery command below to list the names of all log groups in your account. You can adjust the list manually before subscribing.

Be sure to replace `<your_log_groups_file>` with the name of the file to which you want to redirect the output.

```
./dynatrace-aws-logs.sh discover-log-groups > <your_log_groups_file>
```

### Subscribe with a subscription filter pattern

**Usage recommendation:** By default, you subscribe to all the logs in the log group. Use this option if you want to restrict the logs you subscribe to. See [Filter and Pattern Syntaxï»¿](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) for details on the pattern syntax.

**Limitation:** You can use only two subscription filters per log group, so the possibility of creating multiple filters with different patterns is limited. If you create a subscription filter that exceeds the limit, an AWS `LimitExceededException` occurs.

**To subscribe:** Run the command below, making sure to replace `<your_log_group_list>` and `<your_filter_pattern>` with your own values.

```
./dynatrace-aws-logs.sh subscribe --log-groups <your_log_group_list> --filter-pattern <your_filter_pattern>
```

Subscription usage and options

For additional subscription options, see the commands below.

Consult the [Subscription table](#subscription) for the commands below when replacing placeholders (`<...>`) with your own values.

```
dynatrace-aws-logs.sh subscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>}



[--stack-name <your_stack_name>] [--filter-pattern <your_filter_pattern>] [--role-arn ROLE_ARN] [--firehose-arn FIREHOSE_ARN]
```

### Subscription table

| Command-line parameter | Environment variable | Description | Default value |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | A space-separated list of log group names you want to subscribe to. For example: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | A file listing the log groups you want to subscribe to. The file should contain each log group name on a separate line. |  |
| `--filter-pattern` | `FILTER_PATTERN` | If set, it allows you to subscribe to a filtered stream of logs. | You subscribe to all logs in the log group. |
| `--stack-name` | `STACK_NAME` | The name of the CloudFormation stack where you have deployed the resources. | `dynatrace-aws-logs` |
| `--firehose-arn` | `FIREHOSE_ARN` | Specify to which Amazon Data Firehose the logs should be streamed by providing its ARN (Amazon Resource Name). **Usage recommendation:** Set this option if you have permission or performance issues with CloudFormation. | It will be extracted from the output of the CloudFormation stack used in the deploy step: either the `$DEFAULT_STACK_NAME` default value or the one specified with the `--stack-name <your_stack_name>` option. |
| `--role-arn` | `ROLE_ARN` | The ARN of an IAM role that grants CloudWatch Logs permission to deliver ingested log events to the destination stream. **Usage recommendation:** Set this option if you have permission or performance issues with CloudFormation. | It will be extracted from the output of the CloudFormation stack used in the deploy step: either the `$DEFAULT_STACK_NAME` default value or the one specified with the `--stack-name <your_stack_name>` option. |

## Unsubscribe from log groups

If you don't want to forward logs to Dynatrace anymore, use one of the two options below to unsubscribe from log groups.

### Unsubscribe by listing the log group names

Run the command below, making sure to replace `<your_log_group_list>` with a space-separated list of the log group names you want to unsubscribe from.

```
./dynatrace-aws-logs.sh unsubscribe --log-groups <your_log_group_list>
```

### Unsubscribe by reading log groups from a file

Run the command below, making sure to replace `<your_file_name>` with the file name you created to [subscribe by reading log groups from file](#from-file).

```
./dynatrace-aws-logs.sh unsubscribe --log-groups-from-file <your_file_name>
```

Unsubscribe usage and options

For additional unsubscribe options, see the commands below.

Consult the [Unsubscribe table](#unsubscribe-table) for the commands below when replacing the placeholders (`<...>`) with your own values.

```
dynatrace-aws-logs.sh unsubscribe {--log-groups <your_log_group_list> | --log-groups-from-file <your_file_name>} [--stack-name <your_stack_name>]
```

### Unsubscribe table

| Command-line parameter | Environment variable | Description | Default value |
| --- | --- | --- | --- |
| `--log-groups` | `LOG_GROUPS_LIST` | A space-separated list of log group names you want to unsubscribe from. For example: `/aws/lambda/my-lambda /aws/apigateway/my-api`. |  |
| `--log-groups-from-file` | `LOG_GROUPS_FILE` | A file listing log groups you want to unsubscribe from, with each log group name on a separate line. |  |
| `--stack-name` | `STACK_NAME` | The name of the CloudFormation stack where you have deployed the resources. | `dynatrace-aws-logs` |

## Update to new version

To replace your old stack with a new version of the AWS log forwarder stack, deploy the new stack using the same parameters that you used before (especially the stack name, if you changed it from the default value).

## Alternative deployments

If you don't want to use direct ingest through the Cluster API, you need to use an existing ActiveGate version 1.217+. The ActiveGate must be available publicly. The stack will be created without a dedicated ActiveGate if you choose this option.

Although the Log Forwarder will still work without self-monitoring metrics, it is recommended to have them also ingested into CloudWatch. Therefore, internet access to AWS endpoints is required.

See below for instructions.

### Deploy with existing ActiveGate

Prerequisites

Dynatrace version 1.217+

* [Dynatrace requirements](#dynatrace)
* [CLI requirements](#cli)
* You need the following permission policy:

Permissions policy for deployment with an existing ActiveGate

```
{



"Version": "2012-10-17",



"Statement": [



{



"Effect": "Allow",



"Action": [



"cloudformation:CreateChangeSet",



"cloudformation:ExecuteChangeSet",



"cloudformation:DescribeChangeSet",



"cloudformation:DescribeStackEvents",



"cloudformation:DescribeStacks",



"cloudformation:GetTemplateSummary",



"ec2:DescribeImages",



"s3:CreateBucket",



"s3:PutLifecycleConfiguration",



"s3:PutBucketPublicAccessBlock",



"iam:GetRole",



"iam:CreateRole",



"iam:AttachRolePolicy",



"iam:PutRolePolicy",



"iam:GetRolePolicy",



"iam:PassRole",



"lambda:CreateFunction",



"lambda:UpdateFunctionCode",



"lambda:GetFunction",



"lambda:GetFunctionCodeSigningConfig",



"cloudwatch:PutDashboard",



"cloudwatch:GetDashboard",



"firehose:DescribeDeliveryStream",



"firehose:CreateDeliveryStream",



"firehose:ListTagsForDeliveryStream",



"logs:DeleteSubscriptionFilter",



"logs:DescribeLogGroups",



"logs:PutSubscriptionFilter",



"ssm:GetParameters"



],



"Resource": "*"



}



]



}
```

1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values, as follows.

   * For `TARGET_URL`, enter the API URL of your ActiveGate endpoint: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. To learn how to determine your environment ID, see [environment IDï»¿](https://dt-url.net/ej43qge).
   * For `TARGET_API_TOKEN`, enter your API token. For instructions, see [Prerequisites](#dynatrace).

   If you want Dynatrace to verify the SSL certificate of your Dynatrace environment URL, you can set `REQUIRE_VALID_CERTIFICATE` to `true`.

   ```
   TARGET_URL=<your_API_URL>



   TARGET_API_TOKEN=<your_API_token>



   REQUIRE_VALID_CERTIFICATE=false
   ```
2. Download the script and deploy the infrastructure.

   ```
   wget -O dynatrace-aws-log-forwarder.zip https://github.com/dynatrace-oss/dynatrace-aws-log-forwarder/releases/latest/download/dynatrace-aws-log-forwarder.zip \



   && unzip -qo dynatrace-aws-log-forwarder.zip \



   && ./dynatrace-aws-logs.sh deploy --target-url $TARGET_URL --target-api-token $TARGET_API_TOKEN --require-valid-certificate $REQUIRE_VALID_CERTIFICATE
   ```

Deployment usage and options

For additional deployment options, see the command below.

```
dynatrace-aws-logs.sh deploy --target-url <your_API_URL> --target-api-token <your_API_token> [--require-valid-certificate {true|false}] [--stack-name <your_stack_name>] [--max-log-length <max_log_content_length>] [--tags <value> [<value>...] ]
```

For a complete list of parameters, see the deploy table below.

### Deploy table

| **Command-line parameter** | **Environment variable** | **Description** | **Default value** |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `--target-url` | `TARGET_URL` | Required The API URL to your Dynatrace SaaS environment logs ingest target. If you choose to use an existing environment ActiveGate, set it to your ActiveGate endpoint: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>` **Note:** To determine `<your_environment_ID>`, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). |  |  |  |  |  |
| `--target-api-token` | `TARGET_API_TOKEN` | Required Your API token. For instructions, see [Prerequisites](#dynatrace). |  |  |  |  |  |
| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Optional If `true`, the log forwarder Lambda function verifies the SSL certificate of your Dynatrace environment URL. | `false` |  |  |  |  |
| `--stack-name` | `STACK_NAME` | Optional The name of the CloudFormation stack where you want to deploy the resources. | `dynatrace-aws-logs` |  |  |  |  |
| `--max-log-length` | `MAX_LOG_CONTENT_LENGTH` | Optional Log content's max length. If log exceeds this length it will be truncated. For values over 8192 there's also a change in Dynatrace settings neededâyou need to contact a Dynatrace product expert via live chat within your environment. | `8192` |  |  |  |  |
| `--tags` | `TAGS` | Optional A list of tags to associate with the stack that is created or updated. Syntax: TagKey1=TagValue1 TagKey2=TagValue2 â¦ |  |  |  |  |  |

## Verification

You can use the verification methods provided below to fix an unsuccessful deployment process.

### Verify deployment status

To verify deployment correctness

1. In AWS Console, go to CloudFormation.
2. Select your log forwarder stack from the list on the left by stack name (the default value is `dynatrace-aws-logs`).
3. If you find any issues or discrepancies in any of the fields below, select **Delete** to delete the stack, and then repeat the deployment process.

   * In **Stack info**, check the stack status; it should be `CREATE_COMPLETE`.
   * In **Parameters**, check if the parameter values are consistent with the values you provided during deployment.
   * In **Events**, look for any events with a failed status.

### Verify connectivity status

To verify AWS log forwarder connectivity and inspect operational logs

1. In AWS Console, go to CloudWatch Dashboards.
2. Find the self-monitoring dashboard for AWS log forwarding. It will have a name like `DynatraceLogForwarder-SelfMonitoring-eu-north-1-dynatrace-aws-logs`, where the middle part is the AWS region and the last part is the stack name you chose (the default is `dynatrace-aws-logs`).
3. Inspect the dashboard for any obvious issues.
4. Go to CloudFormation.
5. Select your log forwarder stack from the list on the left by stack name (the default value is `dynatrace-aws-logs`).
6. Select the **Resources** tab and then select the link next to `Lambda`.
7. On the Lambda screen, select the **Monitor** tab and then select **Logs**.
8. Select one of the listed log streams and look for exceptions in the logs.

## Scaling guide

To scale up the default throughput, we recommend increasing the Lambda Function's memory and the number of provisioned instances to run concurrently. The values to use depend on the actual load. The following are the maximum tested and supported values.

| **Maximum throughput** | **Lambda memory** | **Number of instances** |
| --- | --- | --- |
| up to `15 MB/minute` (1 GB/hour) | `256 MB` | `1` |
| up to `500 MB/minute` (30 GB/hour) | `1024 MB` | `5` |

As a last resort, scale horizontally: deploy more integrations and subscribe each of them to different log groups to distribute the load.

## Uninstall AWS log forwarding

To uninstall AWS log forwarding

1. Unsubscribe all log groups. You can use the log groups auto-discovery method described in [Subscribe by reading log groups from file](#from-file) and pass the auto-discovery output file to the unsubscribe command. See [Unsubscribe from log groups](#unsubscribe) for details.
2. In AWS Console, go to your CloudFormation stack.
3. Select the **Resources** tab and navigate to the `DeliveryBucket` S3 bucket.
4. Remove all objects in the bucket.
5. Go back to the CloudFormation stack and select **Delete**.