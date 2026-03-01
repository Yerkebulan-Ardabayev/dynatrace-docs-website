---
title: Amazon CloudWatch Metric Streams
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams
scraped: 2026-03-01T21:17:00.881106
---

# Amazon CloudWatch Metric Streams

# Amazon CloudWatch Metric Streams

* How-to guide
* 10-min read
* Updated on Sep 30, 2025

Dynatrace integration with Amazon CloudWatch Metric Streams provides a simple and safe way to ingest AWS metrics. Amazon CloudWatch Metric Streams allows all metrics issued in a given AWS region to be streamed through Firehose to the Dynatrace API.

### AWS default integration vs AWS Metric Streams

Differences between [AWS default integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.") and AWS Metric Streams.

|  | AWS Default integration | AWS Metric Streams |
| --- | --- | --- |
| ActiveGate | Required for non-built-in services or monitored environments bigger than 2000 instancesï¸ | Not required |
| Firehose | Not required | Required |
| Dynatrace tenant open to incoming HTTPS Internet traffic | Not required | Required |
| Available metrics | Selected Amazon CloudWatch metricsï¸ | All available Amazon CloudWatch metricsï¸ |
| Metrics selection | In Dynatraceï¸ | In Amazon CloudWatch consoleï¸ |
| Metrics selection scope | Monitored metrics selection possible at the level of a single metric and its statisticsï¸ | Monitored metrics selection possible only at the level of the whole namespaceï¸ |
| Metrics key prefix | `ext:cloud.aws.<service>`ï¸ [1](#fn-1-1-def) | `cloud.aws.<service>`ï¸ |
| Topology attributes (Dynatrace Entities) | Available | Available once the [AWS Entities for Metric Streamingï»¿](https://dt-url.net/x6038p6) extension is enabled |
| Tags (Dynatrace Entities) | Available | Not available |
| Predefined alerts | Available | Not available |
| Predefined dashboards | Available | Available |
| PrivateLink support | Not available | Not available |

1

The `ext:` prefix is used by metrics from [OneAgent extensions](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") and [ActiveGate extensions](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace."), and also by [classic metrics for AWS integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.").
Despite the naming similarities, AWS integration metrics are **not** based on extensions.

## Prerequisites

* Create an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") in your Dynatrace environment and enable the **Ingest metrics** permission.
* Determine the API URL for your environment:

  + **For Dynatrace SaaS**  
    `https://<your_environment_ID>.live.dynatrace.com`
  + **For Dynatrace Managed**  
    `https://<your_domain>/e/<your_environment_ID>`
  + **For ActiveGate**  
    `https://<your_active_gate_IP_or_hostname>:9999/e/<your_environment_ID>`

To determine `<your_environment_ID>`, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").

To receive the AWS metrics, the previously selected endpoint needs to be open to incoming Internet traffic. Restrictive firewalls might block the streaming service.

## Set up a Metric Streams client

You can set up a Metric Streams client with a CloudFormation template or in the AWS console. See below for instructions.

If you're using Terraform or any other infrastructure setup solution, you need to set the following Firehose instance common attributes:

```
name = "dt-url"



value = <your_API_URL>
```

```
name = "require-valid-certificate"



value = "true"
```

With a CloudFormation template

In the AWS console

CloudFormation allows you to deploy a Metric Streams client using a single deployment command to create a stack that groups multiple AWS resources. This approach is faster and makes AWS resource management easier.

You need one client stack for each region you want to monitor. Once deployed, the client starts streaming all metrics produced in its region. You can [restrict which metrics are streamed](#restrict-metrics).

### Deploy the Metric Streams client for a default region

To fetch the CloudFormation template and deploy it to your AWS account, run the command below. Be sure to replace `<your_API_URL>` and `<your_API_token>` with your own values. Consult the parameters table that follows for details.

If you have AWS CLI configured, you can use a Bash-compliant shell. Otherwise, you can use CloudShell, which is available in the AWS console.

Parametersâ¦

| Parameter | Description | Default value |
| --- | --- | --- |
| `DYNATRACE_ENV_URL` | Required Your API URL. See [Prerequisites](#prerequisites) for instructions. |  |
| `DYNATRACE_API_KEY` | Required Your API token. See [Prerequisites](#prerequisites) for instructions. |  |
| `STACK_NAME` | Required The name of your client stack. | `dynatrace-aws-metric-streams-client` |
| `REQUIRE_VALID_CERTIFICATE` | Optional If set to `true`, Dynatrace verifies the SSL certificate of your Dynatrace environment URL. | `true` |
| `DELIVERY_ENDPOINT` | Optional One of these Metric Streams endpoints for Dynatrace: Global: `https://aws.cloud.dynatrace.com/` US: `https://us.aws.cloud.dynatrace.com/` EU: `https://eu.aws.cloud.dynatrace.com/` | `https://aws.cloud.dynatrace.com/` |

```
DYNATRACE_ENV_URL=<your_API_URL>



DYNATRACE_API_KEY=<your_API_token>



STACK_NAME=dynatrace-aws-metric-streams-client



DELIVERY_ENDPOINT=https://aws.cloud.dynatrace.com/



REQUIRE_VALID_CERTIFICATE=true



wget -O dynatrace-aws-metric-streams-client.yaml  https://assets.cloud.dynatrace.com/awsmetricstreaming/dynatrace-aws-metric-streams-client.yaml && \



aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-aws-metric-streams-client.yaml --stack-name $STACK_NAME --parameter-overrides DynatraceEnvironmentUrl=$DYNATRACE_ENV_URL DynatraceApiKey=$DYNATRACE_API_KEY RequireValidCertificate=$REQUIRE_VALID_CERTIFICATE FirehoseHttpDeliveryEndpoint=$DELIVERY_ENDPOINT
```

### Deploy the Metric Streams client for other regions

The command above uses the default AWS CLI profile and its default region. To change the profile and region, you can export additional variables such as `AWS_DEFAULT_REGION` and `AWS_PROFILE` and rerun the deployment command. If you are using CloudShell, you can change the region in the AWS console instead. For details on how to configure the AWS CLI, see [Environment variables to configure the AWS CLIï»¿](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).

Monitor multiple AWS accounts with Cross-account cross-Region CloudWatch

To monitor metrics from linked AWS accounts using one AWS Metric Streams integration, you need to set `IncludeLinkedAccountsMetrics` parameter to `true` in the CloudFormation template.

### Confirm that the Metric Streams client was deployed correctly Optional

To ensure that the Metric Streams client was deployed correctly

1. In the AWS console, go to **CloudFormation**.
2. Select the stack you created in the CloudFormation deployment.
3. On the **Events** tab, make sure all events completed successfully and there are no failed events.
4. In **Parameters** tab, make sure all parameters you provided have correct values.

### Restrict which metrics are streamed

If you want to restrict which metrics are streamed

1. In the AWS console, go to **CloudFormation**.
2. Select the stack you created in the CloudFormation deployment.
3. On the **Resources** tab, find the resource with type `AWS::CloudWatch::MetricStream` and note its Physical ID.
4. Go to **CloudWatch**.
5. Under **Metrics**, select **Streams**.
6. In the list of metric streams, select the one whose Name corresponds to the Physical ID that you noted in step 3 and then select **Edit**.
7. Under **Metrics to be streamed**, select one of the following options:

   * **All namespaces**, if you want to automatically stream all namespaces (you can manually select namespaces to exclude).
   * **Selected namespaces**, if you want to manually select the namespaces to stream.
8. Under **Select metrics for the metric stream**, select one of the following options:

   * **All metrics**, if you want to automatically stream all metrics from namespaces selected in step 7.
   * **Exclude metrics by metric name**, if you want to manually exclude metrics for each namespace.
9. Select **Save changes**.

If you don't have access to the CloudFormation template, you can manually set up a Metric Streams client in the AWS console. Follow the steps below for instructions.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a Data Firehose stream**](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams#step-1 "Ingest metrics from your AWS accounts using Amazon CloudWatch Metric Streams.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create a CloudWatch Metric Stream**](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams#step-2 "Ingest metrics from your AWS accounts using Amazon CloudWatch Metric Streams.")

For each region that you want to monitor, you need to repeat the entire procedure: create a Data Firehose stream and create a CloudWatch Metric Stream.

### Step 1 Create a Data Firehose stream

1. In the AWS console, go to **Kinesis**.
2. Select **Create delivery stream**.

#### Step 1.Step 1 Choose source and destination

1. In **Source**, select **Direct PUT**.
2. in **Destination** select **Dynatrace**.

#### Step 1.Step 2 Name

1. Enter a stream name and save it for later.

#### Step 1.Step 3 Transform records

1. Make sure **Data Transformation** is disabled.

#### Step 1.Step 4 Destination settings

1. In **Ingestion type**, select **Metrics**
2. In **HTTP endpoint URL**, select one of the available Dynatrace endpoints (Global, EU, or US).
3. In **API token**, enter your API token. See [Prerequisites](#prerequisites) for instructions.
4. In **API URL**, enter your API URL. See [Prerequisites](#prerequisites) for instructions.
5. In **Content encoding**, make sure **GZIP** is selected.
6. In **Retry duration**, enter `900`.
7. In **Buffer hints**, set **Buffer size** to 3MiB and **Buffer interval** to 60 seconds.
8. In **Backup settings**, make sure **Failed data only** is selected.
9. In **S3 backup bucket**, select **Create**.
10. Enter the name, Optional choose a region for the S3 bucket, and then select **Create bucket**.

#### Step 1.Step 5 Configure settings

1. Use the existing default settings.
2. Optional In **Tags**, enter tags to organize your AWS resources.
3. Select **Next**.

#### Step 1.Step 6 Review

1. Review your configuration.
2. Select **Create delivery stream**.

### Step 2 Create a CloudWatch Metric Stream

1. In the AWS console, go to **CloudWatch**.
2. Under **Metrics**, select **Streams**.
3. Select **Create metric stream**.
4. Select **Custom setup with Firehose** and enter the name of the Firehose created in the previous section (in **Select your Data Firehose stream**).
5. In **Change output format**, select **OpenTelemetry 1.0**.

OpenTelemetry 0.7

We recommend using OpenTelemetry 1.0 since it's a default version that allows you to fetch new metrics and is fully compatible with the 0.7 versionâwhich will still be supported.

6. Under **Metrics to be streamed**, select one of the following options:

   * **All metrics**âif you want to stream all metrics from namespaces automatically.
   * **Select metrics**âif you want to exclude metrics for each namespace manually.
7. In **Custom metric stream name**, enter a name for your metric stream.
8. Select **Create metric stream**.

## View metrics using preset dashboards

Once you deploy the Metric Streams client, you can use the [predefined dashboards from the GitHub repositoryï»¿](https://dt-url.net/ev03qe5) in Dynatrace to visualize your ingested data.

Prerequisites

* Install [Python 3ï»¿](https://www.python.org/downloads/) (no additional libraries are required)
* Enable the **Read configuration** and **Write configuration** permissions for your [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.")

To upload preset dashboards from GitHub

1. Get `upload_dashboards.py` from the GitHub repository.

```
curl -o upload_dashboards.py https://raw.githubusercontent.com/Dynatrace/snippets/master/product/dashboarding/upload_dashboards.py
```

2. Create a `dashboards` directory next to `upload_dashboards.py`.
3. Add any dashboard definition from GitHub to your `dashboards` directory.

   Each dashboard definition is a single JSON file located in the folders of the [GitHub repositoryï»¿](https://dt-url.net/ev03qe5).
4. Run the script below. Be sure to replace `<your_dynatrace_cluster_version>`, `<your_API_token>`, and `<your_API_URL>` with your own values. Consult the parameters table that follows for details.

Parametersâ¦

| Parameter | Description |
| --- | --- |
| `cluster-version` | The minor version of your Dynatrace Cluster. For instance, for version `1.210.1.xxxxx`, you need to provide `210`. |
| `dynatrace-api-token` | Your API token. See [Prerequisites](#prerequisites) for instructions. |
| `dynatrace-env-url` | Your API URL. See [Prerequisites](#prerequisites) for instructions. |

```
python3 upload_dashboards.py --cluster-version <your_dynatrace_cluster_version> --dynatrace-api-token <your_API_token> --dynatrace-env-url <your_API_URL>
```

Example command

```
python3 upload_dashboards.py --cluster-version 206 --dynatrace-api-token 123456789 --dynatrace-env-url https://my-cluster.com/e/1755ddb2-7938-41a2-b6bd-096e0fdcd3e0
```

Custom metrics

If you want to ingest custom metrics that aren't included in predefined dashboards, go back to the [AWS default integration vs AWS Metric Streams table](#default-vs-metric-streams) and check the **Metrics key prefix**.

## Uninstall the Metric Streams client

If you deployed the Metric Streams client with a CloudFormation template

1. In the AWS console, go to **CloudFormation**.
2. Select the stack you created in the CloudFormation deployment.
3. In **Resources**, find the resource with type `AWS::S3::Bucket`, select its link, and, in the S3 console, delete all objects in this bucket.
4. Back in CloudFormation, in **Stack information**, select **Delete**.

If you deployed the Metric Streams client through the AWS console, delete all the resources you created (S3 bucket, Firehose delivery stream, CloudWatch metric stream).

## Metric Streams limitations

A metric won't be streamed if it is more than two hours old. You can determine a metric's age by graphing it in the CloudWatch console and checking the age of the last datapoint displayed.

For more limitations, see [Amazon CloudWatch troubleshooting pageï»¿](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-troubleshoot.html)