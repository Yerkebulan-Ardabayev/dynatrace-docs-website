---
title: AI data governance with Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/sample-use-cases/data-governance
scraped: 2026-02-20T21:26:27.605769
---

# AI data governance with Amazon Bedrock

# AI data governance with Amazon Bedrock

* Latest Dynatrace
* Tutorial
* 5-min read
* Updated on Dec 10, 2025

Emerging AI regulations such as the [European Union Artificial Intelligence Actï»¿](https://dt-url.net/xv038bv) provide the means to deploy a comprehensive strategy combining organizational and AI model oversight, covering everything from model training to AI/user interactions.

When running your AI models through Amazon Bedrock, Dynatrace helps you to comply with regulatory record-keeping requirements.

## What you will learn

In this tutorial, we first configure your model training and deployment observability. Afterward, we configure your application to observe user inference requests.

## Steps

The general steps are as follows:

1. Configure Dynatrace
2. Configure your AWS account to send data to your Dynatrace tenant
3. Configure your application

See below for the details of each step.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Configure Dynatrace**](#preparation)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure your AWS account**](#aws)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure your application**](#app)

### Step 1 Configure Dynatrace

In this step, we create a Dynatrace token and we configure [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") to retain the data for 5+ years.

#### Create Dynatrace token

To create a Dynatrace token

1. In Dynatrace, go to **Access Tokens**.  
   To find **Access Tokens**, press **CTRL+K** to search for and select **Access Tokens**.
2. In **Access Tokens**, select **Generate new token**.
3. Enter a **Token name** for your new token.
4. Give your new token the following permissions:
5. Search for and select all of the following scopes.

   * **Ingest bizevents** (`bizevents.ingest`)
   * **Ingest metrics** (`metrics.ingest`)
   * **Ingest logs** (`logs.ingest`)
   * **Ingest events** (`events.ingest`)
   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
6. Select **Generate token**.
7. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

#### Configure OpenPipeline

The default retention period for BizEvents is 35 days. Depending on the regulations, this might not be enough.

To change the retention period, you can create a custom Grail bucket.

1. Go to **Settings** > **Storage management** > **Bucket storage management**.
2. In **Bucket Storage Management**, select  **Bucket**.
3. On **New bucket**:

   * Set **Bucket name** (for example, `gen_ai_events`)
   * Set **Retention period (in days)** (for example, `1,825`, which is about 5 years)
   * Set **Bucket table type** to `bizevents`
4. Select **Save**.

![Grail Bucket Creation](https://dt-cdn.net/images/bucket-creation-1380-125022930c.png)

When the bucket is available, we can configure OpenPipeline to redirect AI-relevant events to storage there.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Business events** > **Pipelines**.
2. On the **Pipelines** tab, select  **Pipeline** and name your pipeline (for example, `AI Data Governance`).
3. On the **Storage** tab, select  **Processor** > **Bucket assignment**.
4. Configure the processor:

   1. Enter a **Name** for the processor
   2. Set **Matching condition** to `true`
   3. Set **Storage** to the bucket you created in the previous procedure
5. Select **Save**.

![OpenPipeline Bucket Assignment](https://dt-cdn.net/images/pipeline-creation-1383-70370d9b88.png)

Finally, we route the ingestion of AI events to the pipeline.

1. Still in **OpenPipeline** > **Business events**, select the **Dynamic routing** tab.
2. On the **Dynamic routing** tab, select  **Dynamic route** to **Add a new dynamic route**.

   * Enter a **Name** for the new route (for example, `AI Event Routing`)
   * Set **Matching condition** to `matchesValue(event.type,"gen_ai.auditing")`
   * Set **Pipeline** to the pipeline you created in the previous procedure.
3. Select **Add**.
4. Select **Save**.

Finally, to mark it as the first pipeline to trigger, drag it  up to be the first row in the table.

![OpenPipeline Routing](https://dt-cdn.net/images/pipeline-routing-1381-ec77347761.png)

### Step 2 Configure your AWS account

Amazon Bedrock emits events for every configuration action executed, such as when you deploy a new model or when the fine-tuning of your model finishes.

We can set up a rule to forward these events to Dynatrace. Please refer to our [integration with Amazon EventBridge using BizEventï»¿](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws/eventbridge-events-to-dynatrace#ingest-as-bizevents) to configure the rule.

The only change is in the [`InputTemplate` fieldï»¿](https://github.com/dynatrace-oss/cloud-snippets/blob/8785beb90e9d5c53de4f8420bf5e68b6ac673a09/aws/eventbridge-events-to-dynatrace/biz-events.yaml#L115), where the property `"type"` should be set to `gen_ai.auditing`. This change is required to match the values that OpenPipeline uses to redirect the events to our Grail bucket.

Expand to see how the AWS configuration should look

![AWS <-> Dynatrace connection](https://dt-cdn.net/images/aws-dynatrace-connection-3352-4347fe5fc8.png)

![AWS CloudTrail Transformer configuration](https://dt-cdn.net/images/aws-cloudtrail-transformer-1610-501eddb13f.png)

![AWS CloudTrail Target configuration](https://dt-cdn.net/images/aws-cloudtrail-target-2744-0f4e467998.png)

### Step 3 Configure your application

We can leverage OpenTelemetry to provide auto-instrumentation that collects traces and metrics of your AI workloads, particularly our fork of [OpenLLMetryï»¿](https://dt-url.net/0sa3uau).

Important Notice

The libraries utilized in this sample use case are currently under development and are in an alpha state. They may contain bugs or undergo significant changes. Use at your own risk.
We highly value your feedback to improve these libraries. Please report any issues, bugs, or suggestions on our GitHub issues page.

To install, use the following command:

```
pip install -i https://test.pypi.org/simple/ dynatrace-openllmetry-sdk==0.0.1a4
```

Afterward, add the following code at the beginning of your main file:

```
from traceloop.sdk import Traceloop



headers = { "Authorization": "Api-Token <YOUR_DT_API_TOKEN>" }



Traceloop.init(



app_name="<your-service>",



api_endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp",



headers=headers



)
```

And that's it! ![Progressive delivery](https://cdn.bfldr.com/B686QPH3/at/r898jztffhg3nzc7fxwh6pf/DT1015.svg?auto=webp&width=72&height=72 "Progressive delivery")

Now you can:

* Fetch all the user/AI interactions, training status, and more on demand.
* Use [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") or [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") to create data-driven documents for custom analytics on it.

![GenAI Compliance Auditing](https://dt-cdn.net/images/gen-ai-auditing-7680-1f44c8a6bf.png)