# Документация Dynatrace: observe/dynatrace-for-ai-observability
Язык: Русский (RU)
Сгенерировано: 2026-02-22
Файлов в разделе: 14
---

## observe/dynatrace-for-ai-observability/ai-observability-app.md

---
title: AI Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/ai-observability-app
scraped: 2026-02-22T21:23:55.707261
---

# AI Observability

# AI Observability

* Latest Dynatrace
* App
* 4-min read
* Updated on Feb 12, 2026

![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** is now Generally Available. Go ahead and install it now from the platform HUB!

20+ technologies supported out of the box, this includes OpenAI, Amazon Bedrock, Google Gemini and Vertex, Anthropic, LangChain and a lot more!

The ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** app delivers a dedicated experience for AI workloads with outâofâtheâbox analytics, autoâinstrumentation, targeted metrics, a debugging flow, and readyâmade dashboards.
Together, these are designed to provide endâtoâend visibility across services, LLMs, agents, and protocols.

It provides out-of-the-box support for 20+ technologies, including OpenAI, Amazon Bedrock, Google Gemini, Google Vertex, Anthropic, LangChain, and more.

Prerequisites

* ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** needs to be installed from the platform HUB. Go ahead and install it now!
* To use ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability**, you need a [DPS license](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") with the following capabilities on your [rate cardï»¿](https://www.dynatrace.com/pricing/):

  + [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")
  + [Traces powered by Grail](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")
  + [Logs powered by Grail](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

Query and sampling cost for AI Observability dashboards

Some out-of-the-box ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") AI Observability dashboards use span queries, which consume DPS trace query capacity even if AI Observability isnât fully configured yet or dashboards show no data. To control this, use the sampling variable on these dashboards (where available) to reduce the queried span volume, and prefer metrics-based tiles and views when possibl.

### Permissions

The following table describes the required permissions.

Permission

Description

storage:events:read

Query events from GRAIL

storage:entities:read

Query entities from GRAIL

storage:logs:read

Query logs from GRAIL

storage:metrics:read

Query metrics from GRAIL

storage:spans:read

Read spans from GRAIL

storage:buckets:read

Read buckets

settings:objects:read

Read settings objects from settings V2

settings:objects:write

Write settings objects from settings V2

davis:analyzers:execute

Run Davis Analyzers

hub:catalog:read

Read Hub catalog

10

rows per page

Page

1

of 1

Get started

Use cases

![AI Observability app - Overview](https://dt-cdn.net/images/overview-page-1920-e8cd84ac11.png)![AI Observability app - Service Health - Main](https://dt-cdn.net/images/service-health-filtered-1920-b489f056a8.png)![AI Observability app - Onboarding](https://dt-cdn.net/images/onboarding-app-1920-bedbc4f9f7.png)![AI Observability - Service Health - Error](https://dt-cdn.net/images/errors-latencies-1920-0a6fb8f618.png)![AI Observability - Service Health - Latency](https://dt-cdn.net/images/traffic-and-latency-1920-a3b9e3514e.png)![AI Observability -  Service Health - Cost](https://dt-cdn.net/images/cost-overview-1920-7969004915.png)![AI Observability -  Service Health - Guardrails](https://dt-cdn.net/images/app-guardrails-1920-6da2e86ebc.png)![AI Observability - Debug traces)](https://dt-cdn.net/images/debug-traces-1920-2d540b770b.png)

1 of 8

![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** has an integrated onboarding flow that guides you through all the required steps to get started and start ingesting data, regardless if it's through OpenTelemetry, open source auto-instrumentation libraries like OpenLLMetry from Traceloop, our OneAgent solution, or directly pulling the data from cloud providers through cloud monitoring.

Additionally, you can instrument your AI applications and services directly using [OpenTelemetry with GenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-agent-spans/) for full control and standardized observability across your entire stack.

### Overview

The **Overview** tab is your starting point to discover AI workloads, quickly validate data ingestion, and see a highâlevel summary of health, performance, and costs across your AI services.

* Use the tiles to view your AI landscape at a glanceâmodel providers, agents, model versions, and servicesâplus activity such as LLM requests, token usage, and cost trends.
* Select any tile to open the **Service Health** page and drill down with deeper analysis: validate errors, review traffic and latency, monitor token and cost behavior, and observe guardrail outcomes.
* Open readyâmade dashboards for popular AI services or select **Browse all dashboards** to find dashboards tagged with **[AI Observability]**. Dashboards include navigation that redirects back into the app for contextual analysis.

![AI Observability app - Overview](https://dt-cdn.net/images/overview-page-1920-e8cd84ac11.png)

### Service Health

Get a unified view of the operational state of your AI services. \*\*Service Health \*\* is organized into focused tabs so you can move from a high-level pulse to root cause in a couple of clicks.

Filter your results:

* In the sidebar on the left, you can select a specific service category (such as  **Containers** or  **Functions**) or analyze all services. In addition, you can quickly filter by predefined attributes that are relevant for the selected category. Select any attribute in the facets sidebar and select **Update** to get results. The filter field is updated with your selection. This allows you to keep the same scoped context when switching between tabs (**Overview**, **Errors**, **Traffic and Latency**, **Cost**, **Guardrails**).
* Alternatively, select the filter field at the top to view suggestions and enter filtering options. Add more statements to narrow down the results. Criteria of the same type are grouped by OR logic. Criteria of different types are grouped by AND logic. You can filter services using tags, alert status, and attributes like name or region. This helps you focus on specific subsets of services based on your criteria. For more details on the filter field syntax, see [Filter field](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").
* **Overview** tab: See counts for Services, Models, and Agents, plus Model Requests, Token Usage, Average Request Duration, and Overall Cost. Each tile supports drillâdown and alert creation.
* **Errors** tab: Track success/failure rate, number of problems, invocation error count, error rate over time, HTTP error types (4xx/5xx), and an error trend with forecast. Use the time brush to zoom into a spike and jump to traces.
* **Traffic and Latency**: Monitor time to response (AVG, p50, p90, p95), response time per model, number of requests, time to first token, and invocation latency. Create alerts for latency regressions.
* **Cost**: Analyze token count, token usage forecast, overall average cost, tokens per model, cached hit ratio, savings through caching, and input/output tokens. Identify cost hot spots and set proactive cost alerts.
* **Guardrails**: Observe providerâreported guardrail outcomes: requests with guardrails enabled, overall executions and activations, activation by type (for example, PII, topics, content, words), detected PII leaks, blocked prompts, denied topics, and filtered content. Note: Dynatrace does not enforce runtime guardrails; providers expose these signals, which we capture and visualize. Configure guardrails at the provider level for lowest latency and complexity.

![AI Observability - Service Health - Error](https://dt-cdn.net/images/errors-latencies-1920-0a6fb8f618.png)

![AI Observability -  Service Health - Guardrails](https://dt-cdn.net/images/app-guardrails-1920-6da2e86ebc.png)

â>

### Create and manage Alerts



* Create new alerts: Select **New alert** on metrics-based tiles (for example, Invocation error count, Invocation latency, Token count, Token usage forecast, Overall guardrail activation). The alert wizard is preâfilled with the current scope (time range, provider/model/service/agent filters) so you can fineâtune thresholds and notifications. Alerts appear in **Manage all alerts** for review and muting.
* Manage all alerts: Use the **Manage all alerts** action from any tab to review, edit, or mute [custom alerts](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.") created from Service Health cards and charts. You can also create a new alert directly from most tiles.

You can find all custom alerts and more information about capabilities and limits in [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

### Debug prompts and traces

When you select **View traces and prompts** from Service Health (for example, via **Error rate over time** > **View traces in this time range** or a tile drillâdown), ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** opens with your current filters and timeframe (provider, model, service/endpoint, agent).
The trace list is enriched with GenAI fields. It is pre-scoped and laid out so that only the relevant requests appear and that GenAI context is front and center for faster investigation.

You can view traces from the following tiles and interactions:

* **Error rate over time**
* **HTTP errors types**
* **HTTP error trend and forecast**
* **Response time per model**
* **Token usage forecast**
* **Tokens per model**
* **Cached hit ratio**
* **Success and failure rate**
* **Guardrail activation by type**

![AI Observability - Debug traces)](https://dt-cdn.net/images/debug-traces-1920-2d540b770b.png)

* Understand AI architectures and dependencies across services, agents, and models with contextual health, performance, and cost views.
* Detect and troubleshoot problems (latency, errors, bottlenecks) in logs and traces, with deep drillâdowns on prompts/traces via the ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** **Explorer** view.
* Monitor token consumption, caching efficiency, and guardrail outcomes to balance quality, cost, and speed.
* Set proactive alerts for spikes in performance, cost, and quality, explain data with Davis, and drive workflows and notifications.
* A/B testing and model versioning.
* Data governance and audit trails.
* Get visibility into your Kubernetes workloads where your AI service is running.

## FAQ

### How do I instrument my services and send data?

Use the onboarding page to configure OpenTelemetry/OpenLLMetry, define permissions, sampling strategies, and tokens. It includes scenarioâbased guidance (for example, "data not in", "no access") and validation tools to confirm successful ingestion.

### Which metrics are available?

Service Health covers

* Volume
* Errors
* Success/failure rates
* Latency/traffic by model
* Tokens (input/completion/total)
* Prompt caching (hit percentage, time/cost saved, read/write tokens)
* Cost (per model, input/output totals)
* Guardrails (invocation counts and providerâspecific dimensions)

Views are customizable, and you can add DQLâbased metrics.

### How do guardrail metrics work? Who provides guardrail runtime protection?

Dynatrace does not execute or enforce guardrail runtime protection. Guardrail enforcement happens at the model/provider level during inference (for example, Amazon Bedrock Guardrails), which then exposes results (such as whether a guardrail intervened) via response payloads and/or provider metrics. ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** instruments these provider signals and surfaces them for monitoring and analysis.

You need to configure guardrails with your model provider. Once configured, Dynatrace ingests and displays the resulting guardrail outcomes and metrics (for example, guardrail invocation counts and providerâspecific categories like toxicity, PII, or denied topics) so you can observe behavior and trends centrally.

You can build on top of these guardrail metrics in Dynatraceâcreate custom alerts and notifications, add tiles to dashboards, and trigger workflowsâjust like with other AI Observability signals. This includes pre-filled alert creation flows and realâtime monitoring with customizable views.

### Does Dynatrace support agent frameworks and protocols?

Yes. OTEL/OpenLLMetry integrations cover Amazon Bedrock Strands and AgentCore, OpenAI Agents, Gemini Agents, and SDKs like Google ADK, AWS Strands, Agentcore, with protocol support for MCP to monitor multiâagent communication. See some Github examples at [Dynatrace AI Agent instrumentation examplesï»¿](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples).

### Can I configure proactive alerts?

Yes, you can create custom alerts from context with preâfilled fields, embed notifications (Slack/email), and link back to investigate. Manage all alerts will drop you right away to a centralised view to review all AI Observability related alerts you and your teams have been created.

### What if I am already using ready-made dashboards?

You can continue using your existing readyâmade dashboards, which remain available until the ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** is generally available.
The dashboards are tagged for discoverability and include navigation that redirects into ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** for deeper, contextual analysis.
For a more integrated and centralized workflow (instrumentation guidance, service health, proactive alerts, and inâcontext prompt/log/trace debugging), we recommend using ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** as your primary entry point, because it provides a dedicated endâtoâend experience purposeâbuilt for AI workloads. Dashboards alone can be limited or inconsistent for GenAIâspecific workflows.

### Does AI Observability generate additional query cost?

Some out-of-the-box ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** dashboards use span queries, which consume DPS trace query capacity, even if AI Observability isnât fully configured yet or the app/dashboards show no data. To control this, use the sampling variable on these dashboards (where available) to reduce the number of spans queried, restrict access to exploratory AI Observability dashboards to relevant users, and prefer metrics-based tiles and views when possible.

### What's coming next?

* AI Model and AI Services Explorer: richer details and list views with integrated Logs, Vulnerabilities, and a new Prompt view for detailed root-cause analysis.
* Prompt management: a dedicated prompt overview to inspect prompts/completions, compare versions, and analyze token/cost usage for faster troubleshooting and optimization.
* Alert templates: out-of-the-box templates for AI-specific signals (e.g., latency spikes, error rates, guardrail violations, token/cost anomalies) to enable proactive alerting.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Review all observable AI technologies in the Dynatrace Hub.](https://www.dynatrace.com/hub/?filter=ai-ml-observability)

---

## observe/dynatrace-for-ai-observability/ai-traffic-management-and-security/kong.md

---
title: Kong AI Gateway
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/ai-traffic-management-and-security/kong
scraped: 2026-02-20T21:19:59.642378
---

# Kong AI Gateway

# Kong AI Gateway

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Nov 20, 2025

The **Kong AI Gateway** is a set of features built on top of Kong Gateway, designed to help developers and organizations adopt AI capabilities quickly and securely. It provides a normalized API layer that allows clients to consume multiple AI services from the same client code base.

![Kong-dashboard](https://dt-cdn.net/images/kong-dashboard-1639-51c812bf99.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/dynatrace.genai.observability.kong)

## Enable monitoring

Ensure that the [Kong Prometheus pluginï»¿](https://docs.konghq.com/hub/kong-inc/prometheus/#ai-llm-metrics) is enabled and exposes AI LLM metrics.

Kubernetes

OpenTelemetry Collector

Follow the [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") guide to monitor your cluster.

Afterwards, add the following annotations to your Kong Deployments:

* `metrics.dynatrace.com/scrape: "true"`
* `metrics.dynatrace.com/port: "8100"`

Follow the [OpenTelemetry Collector installation guide](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") to deploy a collector.
With the following config, the collector will scrape AI LLM metrics every 10 seconds from the `kong-metrics.kong:8100` endpoint.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: kong



scrape_interval: 10s



honor_labels: false



static_configs:



- targets:



- kong-metrics.kong:8100



processors:



cumulativetodelta:



max_staleness: 25h



extensions:



health_check:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions: [health_check]



metrics:



receivers: [prometheus]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to a value higher than how often the collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

Kong does not provide the `kong-metrics` service to scrape the metrics out of the box, so you need to create it with the following service definition:

```
apiVersion: v1



kind: Service



metadata:



name: kong-metrics



namespace: kong



spec:



type: ClusterIP



ports:



- name: metrics



port: 8100



targetPort: 8100



protocol: TCP



selector:



app.kubernetes.io/name: kong



app.kubernetes.io/instance: kong
```

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.content_filter_results` | string | The filter results of the response received from the GenAI model. |
| `gen_ai.completion.0.finish_reason` | string | The reason the GenAI model stopped producing tokens. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.openai.api_base` | string | GenAI server address. |
| `gen_ai.openai.api_version` | string | GenAI API version. |
| `gen_ai.openai.system_fingerprint` | string | The fingerprint of the response generated by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.prompt.prompt_filter_results` | string | The filter results of the prompt sent to the GenAI model. |
| `gen_ai.request.max_tokens` | integer | The maximum number of tokens the model generates for a request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.request.temperature` | double | The temperature setting for the GenAI request. |
| `gen_ai.request.top_p` | double | The top\_p sampling setting for the GenAI request. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Metrics

After following the steps above, the following metrics will be available:

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `ai_llm_requests_total` | counter | integer | AI requests total per ai\_provider in Kong |
| `ai_llm_cost_total` | counter | integer | AI requests cost per ai\_provider/cache in Kong |
| `ai_llm_provider_latency_ms_bucket` | histogram | ms | AI latencies per ai\_provider in Kong |
| `ai_llm_tokens_total` | counter | integer | AI tokens total per ai\_provider/cache in Kong |
| `ai_cache_fetch_latency` | histogram | ms | AI cache latencies per ai\_provider/database in Kong |
| `ai_cache_embeddings_latency` | histogram | ms | AI cache embedding latencies per ai\_provider/database in Kong |
| `ai_llm_provider_latency` | histogram | ms | AI provider latencies per ai\_provider/database in Kong |

Additionally, the following metrics are reported.

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | The number of choices returned by chat completions call. |
| `gen_ai.client.operation.duration` | histogram | `s` | The GenAI operation duration. |
| `gen_ai.client.token.usage` | histogram | `none` | The number of input and output tokens used. |
| `llm.openai.embeddings.vector_size` | counter | `none` | The size of returned vector. |

---

## observe/dynatrace-for-ai-observability/get-started/sample-use-cases/data-governance.md

---
title: AI data governance with Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/data-governance
scraped: 2026-02-18T05:48:43.190195
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

---

## observe/dynatrace-for-ai-observability/get-started/sample-use-cases/openai-observability.md

---
title: OpenAI Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/openai-observability
scraped: 2026-02-18T05:43:54.663089
---

# OpenAI Observability

# OpenAI Observability

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jan 28, 2026

Dynatrace enables enterprises to automatically collect, visualize and alert on OpenAI API request consumption, latency, and stability information in combination with all other services used to build their AI application. This includes [OpenAIï»¿](https://openai.com/) as well as [Azure OpenAI servicesï»¿](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service) such as GPT-3, Codex, DALL-E, or ChatGPT.

The example dashboard below visualizes OpenAI token consumption, showing critical SLOs for latency and availability as well as the most important OpenAI generative AI service metrics, such as response time, error count, and overall number of requests.

![OpenAI dashboard](https://dt-cdn.net/images/dashboard-new-1267-2e968ca9ae.png)

Dynatrace OneAgent discovers, observes, and protects access to OpenAI automatically, without any manual configuration whatsoever. It reveals the full context of used technologies, shows the service interaction topology, analyzes security vulnerabilities, and observes metrics, traces, logs, and business events in real time.

The sections below show how to trace OpenAI/GPT model requests, how to chart OpenAI golden signals within a dashboard, and how Dynatrace Intelligence automatically detects abnormal service behavior such as slowdowns in OpenAI/GPT requests as the root cause of large-scale situations.

## Trace OpenAI model requests

This simple Node.js example is used to explain how Dynatrace OneAgent automatically traces OpenAI model requests. OpenAI offers a Node.js language binding that allows the direct integration of a model request by adding the following lines of code to your own Node.js AI application:

```
const { Configuration, OpenAIApi } = require("openai");



const configuration = new Configuration({



apiKey: process.env.OPENAI_API_KEY



});



const openai = new OpenAIApi(configuration);



const response = await openai.createCompletion({



model: "text-davinci-003",



prompt: "Say hello!",



temperature: 0,



max_tokens: 10,



});
```

Once the AI application is started on a OneAgent-monitored server, OneAgent automatically detects it and collects traces and metrics for all outgoing requests.

The automatic injection of monitoring and tracing code not only works for the Node.js language binding, but also works when using the raw HTTPS request in Node.js.

While OpenAI offers official language bindings only for Python and Node.js, there is a long list of [community-provided language bindingsï»¿](https://platform.openai.com/docs/libraries/community-libraries).

OneAgent automatically monitors all C#, .NET, Java, Go, and Node.js bindings, but we recommend using OpenTelemetry instrumentation to monitor the OpenAI Python binding with Dynatrace.

The example below shows all the traces that OneAgent collects, along with all the latency and reliability measurements for each of the outgoing GPT model requests.

![Dynatrace trace with OpenAI generative service calls](https://dt-cdn.net/images/serviceflow-larger-1920-f08becaeed.png)

To correctly split out all OpenAI service calls, you need to configure a custom device with the OpenAI domain within your Dynatrace environment.

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Select **Custom devices**.
3. Select **New Custom Device** from the menu in the upper-right corner of the page.

The example below shows the necessary configuration for correctly handling OpenAI.

![Create an OpenAI custom device for correctly detecting all requests to the OpenAI domain.](https://dt-cdn.net/images/custom-device-config-1262-6624bc280f.png)

Once the OpenAI custom device is configured, Dynatrace ServiceFlow shows the flow of your requests, starting with your Node.js service and calling the OpenAI model.

![Dynatrace ServiceFlow showing all request traces to OpenAI generative AI services.](https://dt-cdn.net/images/serviceflow-new-1558-70f4b2b0fa.png)

As you can see in the example, the Dynatrace OneAgent automatically collects all latency and reliability-related information along with all the traces showing how your OpenAI requests traverse your service graph.

The seamless tracing of OpenAI model requests allows operators to identify behavioral patterns within your AI service landscape and understand the typical load situation of your infrastructure.

This knowledge is essential for further optimizing the performance and cost of your services.
By adding some lines of manual instrumentation to your Node.js service, cost-related measurements are also picked up by OneAgent, which collects the number of OpenAI conversational tokens used.
Dynatrace offers multiple ways of capturing request payload content, such as the OpenAI token counts.

Capturing request payload content with Dynatrace can be achieved by:

* [Logging the information and capture the metrics and trace mapping directly from the log entries.](/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/openai-observability#lplogs "Learn about Dynatrace for OpenAI Observability, how Dynatrace observes OpenAI SaaS services, and much more.")
* [Sending custom metrics by using the OneAgent metric ingest channel.](/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/openai-observability#lpcustom-metrics "Learn about Dynatrace for OpenAI Observability, how Dynatrace observes OpenAI SaaS services, and much more.")
* [Capturing parts of the request payload using business events.](/docs/observe/business-observability/bo-event-processing/bo-processing-classic-pipeline "Process business event data in Dynatrace via the classic pipeline.")

## Observe OpenAI request cost using logs

Using logs to collect and observe OpenAI request costs is both simple and powerful. It allows the owner of the service to write a log line using a standard Node.js logging framework such as [Winstonï»¿](https://www.npmjs.com/package/winston) and to collect and analyze those logs within Dynatrace.

The following code snippet writes a Winston log line containing the OpenAI request token counts.

```
logger.log('info', `OpenAI response promt_tokens:${response.data.usage.prompt_tokens} completion_tokens:${response.data.usage.completion_tokens} total_tokens:${response.data.usage.total_tokens}`);
```

The OpenAI request log lines can be viewed in the Dynatrace log viewer.

We recommend that you also enable trace context enrichment for Node.js logs (go to **Settings** > **Preferences** > **OneAgent features** and turn on **Node.js Trace/span context enrichment for logs**) to automatically map all log lines to their captured request traces.

![Trace context enrichment setting](https://dt-cdn.net/images/trace-context-enrichment-1727-8133fcc4b5.png)

With **Node.js Trace/span context enrichment for logs** enabled, you even get a convenient mapping of all OpenAI traces with their log lines.

![Capture OpenAI logs](https://dt-cdn.net/images/trace-logs-1925-03fb9d7d0f.png)

Use a log processing rule to automatically extract the three token counts into separate log entry fields.

![Process OpenAI logs](https://dt-cdn.net/images/log-processing-rule-1925-cb21914d08.png)

After defining the log processing rule, additional metric extraction rules help to make those three token counts into chartable metrics.

![Extract OpenAI log metrics](https://dt-cdn.net/images/log-metric-extraction-1927-5e25da86ed.png)

## Observe OpenAI request cost by sending custom metrics

Each request to an OpenAI model such as text-davinci-003, gpt-3.5-turbo, or GPT-4 reports back how many tokens were used for the request prompt (the length of your text question) and how many tokens the model generated as a response.

Customers of OpenAI are billed by the total number of tokens consumed by all the requests they made.

By extracting those token measurements from the returning payload and reporting them through the Dynatrace OneAgent, users can observe the token consumption across all their OpenAI-enhanced services in their monitoring environment.

You need the following instrumentation to extract the token count from the OpenAI response and report those three measurements to the local OneAgent.

```
function report_metric(openai_response) {



var post_data = "openai.promt_token_count,model=" + openai_response.model + " " + openai_response.usage.prompt_tokens + "\n";



post_data += "openai.completion_token_count,model=" + openai_response.model + " " + openai_response.usage.completion_tokens + "\n";



post_data += "openai.total_token_count,model=" + openai_response.model + " " + openai_response.usage.total_tokens + "\n";



console.log(post_data);



var post_options = {



host: 'localhost',



port: '14499',



path: '/metrics/ingest',



method: 'POST',



headers: {



'Content-Type': 'text/plain',



'Content-Length': Buffer.byteLength(post_data)



}



};



var metric_req = http.request(post_options, (resp) => {}).on("error", (err) => { console.log(err); });



metric_req.write(post_data);



metric_req.end();



}
```

After adding those lines to your Node.js service, three new OpenAI token consumption metrics are available in Dynatrace.

![OpenAI token consumption metrics collected in Dynatrace](https://dt-cdn.net/images/token-metrics-1412-f9c654f368.png)

## Dynatrace Intelligence automatically detects GPT as root cause



One of the superb features of Dynatrace is how its Dynatrace Intelligence automatically learns the typical behavior of monitored services.

When an abnormal slowdown or increase of errors is detected, Dynatrace Intelligence triggers a root cause analysis to identify the cause of complex situations.

Our simple example of a Node.js service entirely depends on the ChatGPT model response. Whenever the latency of the model response degrades or the model request returns with an error, Dynatrace Intelligence automatically detects it.

The Davis problem details page shows all affected services, the OpenAI generative service as the root cause for the slowdown, and the ripple effect of its slowdown. The problem details page also lists all service level objectives (SLOs) that were negatively impacted by this slowdown.

In the example below, Dynatrace Intelligence automatically reported a slowdown of the Node.js prompt service and correctly detected the OpenAI generative service as being the root cause of this slowdown.

---

## observe/dynatrace-for-ai-observability/get-started.md

---
title: Get started
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started
scraped: 2026-02-22T21:19:41.214373
---

# Get started

# Get started

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Feb 04, 2026

The Dynatrace Full-Stack observability platform combined with Traceloop's OpenLLMetry OpenTelemetry SDK can seamlessly provide comprehensive insights into large language models (LLMs) in production environments. By observing AI models, businesses can make informed decisions, optimize performance, and ensure compliance with emerging AI regulations.

## Create a Dynatrace token

Create a Dynatrace token so you can report AI observability data to your Dynatrace tenant.

Create a Dynatrace Token

To create a Dynatrace token

1. In Dynatrace, go to **Access Tokens**.  
   To find **Access Tokens**, press **Ctrl/Cmd+K** to search for and select **Access Tokens**.
2. In **Access Tokens**, select **Generate new token**.
3. Enter a **Token name** for your new token.
4. Give your new token the following permissions:
5. Search for and select all of the following scopes.

   * **Ingest metrics** (`metrics.ingest`)
   * **Ingest logs** (`logs.ingest`)
   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
6. Select **Generate token**.
7. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

## Instrument your application

Choose your instrumentation framework and language to get started.

The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality. Set the `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` environment variable to `DELTA`.

OpenLLMetry

OpenTelemetry

OpenLLMetry provides auto-instrumentation for popular AI frameworks and automatically collects GenAI semantic conventions.

Python

Node.js

We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

```
pip install traceloop-sdk
```

Afterward, add the following code at the beginning of your main file.

```
from traceloop.sdk import Traceloop



headers = { "Authorization": "Api-Token <YOUR_DT_API_TOKEN>" }



Traceloop.init(



app_name="<your-service>",



api_endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", # or OpenTelemetry Collector URL



headers=headers



)
```

We can leverage OpenTelemetry to provide autoinstrumentation that collects traces and metrics of your AI workloads, particularly [OpenLLMetryï»¿](https://dt-url.net/0sa3uau) that can be installed with the following command:

```
npm i @opentelemetry/exporter-trace-otlp-proto @traceloop/node-server-sdk
```

Afterward, add the following code at the beginning of your main file.

```
import {OTLPTraceExporter} from "@opentelemetry/exporter-trace-otlp-proto";



import * as traceloop from "@traceloop/node-server-sdk";



const exporter = new OTLPTraceExporter({



url: "https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp", // or OpenTelemetry Collector URL



headers: { Authorization: "Api-Token <YOUR_DT_API_TOKEN>" },



});



traceloop.initialize({



appName: "<your-service>",



exporter: exporter



});
```

Currently, OpenLLMetry for Node.js doesn't support Metrics.

OpenTelemetry provides flexible instrumentation that you can customize for your specific needs. For more details on the GenAI semantic conventions, see [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Python

Node.js

Install the required packages:

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp-proto-http
```

Configure the OpenTelemetry SDK:

```
from opentelemetry import trace



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider



from opentelemetry.sdk.trace.export import BatchSpanProcessor



from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter



resource = Resource.create({"service.name": "<your-service>"})



provider = TracerProvider(resource=resource)



trace.set_tracer_provider(provider)



exporter = OTLPSpanExporter(



endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces",



headers={"Authorization": "Api-Token <YOUR_DT_API_TOKEN>"},



)



provider.add_span_processor(BatchSpanProcessor(exporter))



tracer = trace.get_tracer(__name__)
```

Install the required packages:

```
npm install @opentelemetry/sdk-node @opentelemetry/api @opentelemetry/exporter-trace-otlp-proto
```

Configure the OpenTelemetry SDK:

```
import { NodeSDK } from '@opentelemetry/sdk-node';



import { Resource } from '@opentelemetry/resources';



import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-proto';



import { trace } from '@opentelemetry/api';



const sdk = new NodeSDK({



resource: new Resource({ 'service.name': '<your-service>' }),



traceExporter: new OTLPTraceExporter({



url: 'https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp/v1/traces',



headers: { Authorization: 'Api-Token <YOUR_DT_API_TOKEN>' },



}),



});



sdk.start();



const tracer = trace.getTracer('my-tracer');
```

---

## observe/dynatrace-for-ai-observability/models-and-platforms/bedrock.md

---
title: Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/bedrock
scraped: 2026-02-22T21:19:42.570703
---

# Amazon Bedrock

# Amazon Bedrock

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 28, 2026

Amazon Bedrock is a fully managed service that provides a single API to access and utilize various high-performing foundation models (FMs) from leading AI companies. It offers a broad set of capabilities to build generative AI applications with security, privacy, and responsible AI practices.

Monitoring your Bedrock models via Dynatrace, you can get cost analysis and forecast estimation via Dynatrace Intelligence, prompt and completion recording, error tracking, performance metrics of your AI services, and more.

![Bedrock Observability](https://dt-cdn.net/images/bedrock-dashboard-4108-e3504d724e.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/document/dynatrace.genai.observability.bedrock)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.finish_reason` | string | The reason the model stopped generating tokens, corresponding to each generation received. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.request.max_tokens` | integer | The maximum number of tokens the model generates for a request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.request.temperature` | double | The temperature setting for the GenAI request. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Metrics

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `gen_ai.client.operation.duration` | histogram | `s` | The GenAI operation duration. |
| `gen_ai.client.token.usage` | histogram | `none` | The number of input and output tokens used. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

---

## observe/dynatrace-for-ai-observability/models-and-platforms/nvidia-nim.md

---
title: NVIDIA NIM
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/nvidia-nim
scraped: 2026-02-22T21:19:45.246811
---

# NVIDIA NIM

# NVIDIA NIM

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Nov 20, 2025

NVIDIA NIM (NVIDIA Inference Microservices) is a set of microservices that accelerate foundation model deployment on any cloud or data center, optimizing AI infrastructure for efficiency and cost-effectiveness while reducing hardware and operational costs.

![NVIDIA NIM Dashboard](https://dt-cdn.net/images/ai-observability-nvidia-nim-3580-bc02ba8523.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/cdf180cb-3153-447f-8f28-5bfb05bd3e93)

## Enable monitoring

Kubernetes

OpenTelemetry Collector

Follow the [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") guide to monitor your cluster.

Afterwards, add the following annotations to your NVIDIA NIM deployments:

* `metrics.dynatrace.com/scrape: "true"`
* `metrics.dynatrace.com/port: "8000"`

Follow the [OpenTelemetry Collector installation guide](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") to deploy a collector.
With the following config, the collector will scrape AI metrics every 10 seconds from the `<NIM-endpoint>:8000` endpoint.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: nim-metrics



scrape_interval: 10s



honor_labels: false



static_configs:



- targets:



- ["<NIM-endpoint>:8000"]



processors:



cumulativetodelta:



max_staleness: 25h



extensions:



health_check:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



extensions: [health_check]



metrics:



receivers: [prometheus]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to a value higher than how often the collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.content_filter_results` | string | The filter results of the response received from the GenAI model. |
| `gen_ai.completion.0.finish_reason` | string | The reason the GenAI model stopped producing tokens. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.openai.api_base` | string | GenAI server address. |
| `gen_ai.openai.api_version` | string | GenAI API version. |
| `gen_ai.openai.system_fingerprint` | string | The fingerprint of the response generated by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.prompt.prompt_filter_results` | string | The filter results of the prompt sent to the GenAI model. |
| `gen_ai.request.max_tokens` | integer | The maximum number of tokens the model generates for a request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.request.temperature` | double | The temperature setting for the GenAI request. |
| `gen_ai.request.top_p` | double | The top\_p sampling setting for the GenAI request. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Metrics

The following metrics will be available:

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `e2e_request_latency_seconds` | histoGrailm | s | Histogram of end-to-end request latency in seconds |
| `generation_tokens_total` | counter | integer | Number of generation tokens processed |
| `gpu_cache_usage_perc` | gauge | integer | GPU KV-cache usage. 1 means 100 percent usage |
| `num_request_max` | counter | integer | Maximum number of concurrently running requests |
| `num_requests_running` | counter | integer | Number of requests currently running on GPU |
| `num_requests_waiting` | counter | integer | Number of requests waiting to be processed |
| `prompt_tokens_total` | counter | integer | Number of prefill tokens processed |
| `request_failure_total` | counter | integer | Number of failed requests; requests with other finish reason are counted |
| `request_finish_total` | counter | integer | Number of finished requests, with label indicating finish reason |
| `request_generation_tokens` | histogram | integer | Histogram of number of generation tokens processed |
| `request_prompt_tokens` | histogram | integer | Histogram of number of prefill tokens processed |
| `request_success_total` | counter | integer | Number of successful requests; requests with finish reason "stop" or "length" are counted |
| `time_per_output_token_seconds` | histogram | s | Histogram of time per output token in seconds |
| `time_to_first_token_seconds` | histogram | s | Histogram of time to first token in seconds |

Additionally, the following metrics are reported.

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | The number of choices returned by chat completions call. |
| `gen_ai.client.operation.duration` | histogram | `s` | The GenAI operation duration. |
| `gen_ai.client.token.usage` | histogram | `none` | The number of input and output tokens used. |
| `llm.openai.embeddings.vector_size` | counter | `none` | The size of returned vector. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

---

## observe/dynatrace-for-ai-observability/models-and-platforms/ollama.md

---
title: Ollama
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/ollama
scraped: 2026-02-22T21:19:46.501531
---

# Ollama

# Ollama

* Latest Dynatrace
* Explanation
* 1-min read
* Published Oct 22, 2024

Ollama is a platform that allows users to run and manage AI models locally on their own machines. It provides tools for deploying, interacting with, and fine-tuning various AI models, particularly those related to natural language processing.

Monitoring your Ollama models via Dynatrace, you can get prompt and completion recording, error tracking, performance metrics of your AI services, and more.

![Ollama Observability](https://dt-cdn.net/images/ollama-1600-47c2844bfa.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/apps/dynatrace.dashboards/dashboard/43d1aa93-b926-4245-9970-6eaca5e26e76)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Observability of Retrieval-Augmented Generation pipelines](/docs/observe/dynatrace-for-ai-observability/sample-use-cases/self-service-ai-observability-tutorial "Learn how to use Dynatrace to have deep insights into your RAG pipelines.")

---

## observe/dynatrace-for-ai-observability/models-and-platforms/openai.md

---
title: OpenAI
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/openai
scraped: 2026-02-22T21:19:39.711317
---

# OpenAI

# OpenAI

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 28, 2026

Monitoring your OpenAI requests via Dynatrace, you can get cost analysis and forecast estimation via Dynatrace Intelligence, prompt and completion recording, error tracking, performance metrics of your AI services, and more.

![OpenAI Observability](https://dt-cdn.net/images/openai-dashboard-4102-e844fa80f9.png)

[Explore the sample dashboard on the Dynatrace Playground.ï»¿](https://wkf10640.apps.dynatrace.com/ui/document/dynatrace.genai.observability.openai)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.content_filter_results` | string | The filter results of the response received from the GenAI model. |
| `gen_ai.completion.0.finish_reason` | string | The reason the GenAI model stopped producing tokens. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.openai.api_base` | string | GenAI server address. |
| `gen_ai.openai.api_version` | string | GenAI API version. |
| `gen_ai.openai.system_fingerprint` | string | The fingerprint of the response generated by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.prompt.prompt_filter_results` | string | The filter results of the prompt sent to the GenAI model. |
| `gen_ai.request.max_tokens` | integer | The maximum number of tokens the model generates for a request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.request.temperature` | double | The temperature setting for the GenAI request. |
| `gen_ai.request.top_p` | double | The top\_p sampling setting for the GenAI request. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `gen_ai.usage.completion_tokens` | integer | The number of tokens used in the GenAI response (completion). |
| `gen_ai.usage.prompt_tokens` | integer | The number of tokens used in the GenAI input (prompt). |
| `llm.request.type` | string | The type of the operation being performed. |

## Metrics

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `gen_ai.client.generation.choices` | counter | `none` | The number of choices returned by chat completions call. |
| `gen_ai.client.operation.duration` | histogram | `s` | The GenAI operation duration. |
| `gen_ai.client.token.usage` | histogram | `none` | The number of input and output tokens used. |
| `llm.openai.embeddings.vector_size` | counter | `none` | The size of returned vector. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

---

## observe/dynatrace-for-ai-observability/models-and-platforms/tensorflow-keras-observability.md

---
title: TensorFlow Keras observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/models-and-platforms/tensorflow-keras-observability
scraped: 2026-02-20T21:18:50.443573
---

# TensorFlow Keras observability

# TensorFlow Keras observability

* Latest Dynatrace
* Tutorial
* 4-min read
* Published Jun 06, 2023

**TensorFlow** and its user-friendly **Keras sequential interface** represent state-of-the-art technology for training and running deep learning models.

TensorFlow represents a general-purpose machine learning framework that allows data scientists to build, train and run all kinds of AI models on top.

TensorFlow also ships together with a convenient debugging server called **TensorBoard** that allows data scientists to collect and visualize all relevant training information such as logs, events, and metrics within a Web dashboard.

See below an example screenshot of TensorBoard and how it visualizes the progress of model training:

![TensorBoard based AI training visualization](https://dt-cdn.net/images/tensorboard-1600-04dc516f95.png)

While TensorBoard is a great tool for local debugging of your AI model, it is not applicable for long-term observability of your running AI model in production.

As TensorBoard data collection is built on top of a **flexible TensorFlow callback receiver interface**, it is easy to directly send observability information about your running AI model to Dynatrace.

All that is necessary is a dedicated TensorFlow callback implementation that collects the data and forwards to a Dynatrace monitoring environment.

## Dynatrace TensorFlow callback receiver

A TensorFlow callback receiver implementation does receive important information updates during training and evaluation phase of a model.

See below the implementation of a Dynatrace TensorFlow callback receiver that forwards metric data during training and evaluation of a model.

```
import tensorflow as tf



from tensorflow import keras



import requests



# Custom TensorFlow Keras callback receiver that sends the logged metrics



# to a Dynatrace monitoring environment.



# Read more about writing your own callback receiver here:



# https://www.tensorflow.org/guide/keras/custom_callback



class DynatraceKerasCallback(keras.callbacks.Callback):



metricprefix = ''



modelname = ''



url = ''



apitoken = ''



batch = ''



# Constructor that takes a metric prefix, the name of the current model that is used,



# the Dynatrace metric ingest API endpoint (e.g.: https://your.live.dynatrace.com/api/v2/metrics/ingest)



# and the Dynatrace API token (with metric ingest scope enabled)



def __init__(self, metricprefix='tensorflow.', modelname='', url='', apitoken=''):



self.metricprefix = metricprefix



self.modelname = modelname



self.url = url



self.apitoken = apitoken



def send_metric(self, name, value, tags):



tags_str = ''



for tag_key in tags:



tags_str = tags_str + ',{key}={value}'.format(key=tag_key, value=tags[tag_key])



line = '{prefix}.{name}{tags} {value}\n'.format(prefix=self.metricprefix, tags=tags_str, model=self.modelname, name=name, value=value)



self.batch = self.batch + line



def flush(self):



print(self.batch)



r = requests.post(self.url, headers={'Content-Type': 'text/plain', 'Authorization' : 'Api-Token ' + self.apitoken}, data=self.batch)



self.batch = ''



def on_train_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })



self.flush()



def on_epoch_end(self, epoch, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'train' })



self.flush()



def on_test_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'test' })



self.flush()



def on_predict_end(self, logs=None):



keys = list(logs.keys())



for m in keys:



self.send_metric(m, logs[m], { 'model' : self.modelname, 'stage' : 'predict' })



self.flush()
```

## Example Keras model training and evaluation

In the following example, a Keras model loads a well-known sample data set (MNIST) and trains a Keras sequential model.

A Dynatrace TensorFlow callback receiver is configured that automatically receives and forwards the accuracy and loss metric to the configured monitoring environment.

In a production deployment of the model (the evaluation step) the same Dynatrace callback receiver is used to continuously receive observability data about the running model.

```
import tensorflow as tf



print("TensorFlow version:", tf.__version__)



import time



# load the Dynatrace callback receiver



from dynatrace import DynatraceKerasCallback



# Load a sample data set



mnist = tf.keras.datasets.mnist



(x_train, y_train), (x_test, y_test) = mnist.load_data()



x_train, x_test = x_train / 255.0, x_test / 255.0



# Define a model



model = tf.keras.models.Sequential([



tf.keras.layers.Flatten(input_shape=(28, 28)),



tf.keras.layers.Dense(128, activation='relu'),



tf.keras.layers.Dropout(0.2),



tf.keras.layers.Dense(10)



])



# Define a loss function



loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)



# Compile the model



model.compile(optimizer='adam',



loss=loss_fn,



metrics=['accuracy'])



# Define the tensor board callbacks



dt_callback = DynatraceKerasCallback(metricprefix='tensorflow', modelname='mnist-classifier', url='https://<YOUR_ENV>.live.dynatrace.com/api/v2/metrics/ingest', apitoken='<YOUR_TOKEN>')



# Train the model



model.fit(x_train, y_train, epochs=5, callbacks=[dt_callback])



# Use the model in production



while True:



model.evaluate(x_test,  y_test, verbose=2, callbacks=[dt_callback])



time.sleep(60)
```

## Visualize TensorFlow model metrics in Dynatrace

Once the Dynatrace TensorFlow callback receiver is registered within your own AI model, all the collected metrics are forwarded to your monitoring environment.

The screenshot below shows a Data Explorer visualization of the accuracy metric that was collected from the TensorFlow callback receiver:

![AI Observability in Dynatrace for Tensorflow and Keras](https://dt-cdn.net/images/dynatrace-notebook-1920-31cf259f10.png)

---

## observe/dynatrace-for-ai-observability/orchestration-frameworks/langchain.md

---
title: LangChain
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/orchestration-frameworks/langchain
scraped: 2026-02-22T21:19:38.456653
---

# LangChain

# LangChain

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Oct 22, 2024

LangChain is a framework designed for building applications that utilize large language models (LLMs). It provides a set of tools and components that make it easier to integrate LLMs into various applications, enabling developers to create complex workflows and functionalities.

With Dynatrace, you can get visibility into each step of the workflows monitoring prompt and completion messages, error tracking, performance metrics, and more.

![trace-agentic-pipeline](https://dt-cdn.net/images/trace-agentic-pipeline-1708-3a40424e8a.png)

## Spans

The following attributes are available for GenAI Spans.

| Attribute | Type | Description |
| --- | --- | --- |
| `gen_ai.completion.0.content` | string | The full response received from the GenAI model. |
| `gen_ai.completion.0.role` | string | The role used by the GenAI model. |
| `gen_ai.prompt.0.content` | string | The full prompt sent to the GenAI model. |
| `gen_ai.prompt.0.role` | string | The role setting for the GenAI request. |
| `gen_ai.request.model` | string | The name of the GenAI model a request is being made to. |
| `gen_ai.response.model` | string | The name of the model that generated the response. |
| `gen_ai.system` | string | The GenAI product as identified by the client or server instrumentation. |
| `llm.request.type` | string | The type of the operation being performed. |
| `traceloop.entity.name` | string | The name of the action in the chain. |
| `traceloop.span.kind` | string | The type of action in the chain. |
| `traceloop.workflow.name` | string | The name of the chain. |

## Metrics

| Metric | Type | Unit | Description |
| --- | --- | --- | --- |
| `http.client.duration` | histogram | `ms` | The duration of the outbound HTTP request. |

## Related topics

* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Observability of Retrieval-Augmented Generation pipelines](/docs/observe/dynatrace-for-ai-observability/sample-use-cases/self-service-ai-observability-tutorial "Learn how to use Dynatrace to have deep insights into your RAG pipelines.")

---

## observe/dynatrace-for-ai-observability/sample-use-cases/data-governance.md

---
title: AI data governance with Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/sample-use-cases/data-governance
scraped: 2026-02-22T21:22:07.830095
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

---

## observe/dynatrace-for-ai-observability/sample-use-cases/openai-observability.md

---
title: OpenAI Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/sample-use-cases/openai-observability
scraped: 2026-02-19T21:23:37.503881
---

# OpenAI Observability

# OpenAI Observability

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jan 28, 2026

Dynatrace enables enterprises to automatically collect, visualize and alert on OpenAI Agent, API request consumption, latency, and stability information in combination with all other services used to build their AI application. This includes [OpenAIï»¿](https://openai.com/) and [Azure OpenAIï»¿](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service) services, such as GPT-5.2, Codex, DALL-E, or ChatGPT.

The example dashboard below visualizes OpenAI token consumption, showing critical SLOs for latency and availability as well as the most important OpenAI generative AI service metrics, such as response time, error count, and overall number of requests.

![OpenAI dashboard](https://dt-cdn.net/images/openai-dashboard-v11-2560-987f66adf6.png)

Dynatrace with OpenTelemetry or OpenLLMetry helps to:

* Reveal the full context of used technologies.
* Shows the service interaction topology.
* Analyzes security vulnerabilities.
* Observes metrics, traces, logs, and business events in real time.

The sections below show how to:

* Trace OpenAI/GPT model requests.
* Chart OpenAI golden signals within a dashboard.
* Use Dynatrace Intelligence to automatically detect abnormal service behavior such as slowdowns in OpenAI/GPT requests as the root cause of large-scale situations.

## OpenAI Agents SDK sample app

Use the [OpenAI Agents SDK sampleï»¿](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples/tree/main/openai-agent-sample) to see AI Observability in action. The sample is a Customer Service Agent interface built on the [OpenAI Agents SDKï»¿](https://openai.github.io/openai-agents-python/) and based on the [openai-cs-agents-demoï»¿](https://github.com/openai/openai-cs-agents-demo). The backend uses Traceloop's OpenLLMetry OpenTelemetry SDK to emit traces and metrics to Dynatrace.

In the sample, you:

1. Configure OpenLLMetry in `python-backend/api.py`.
2. Point `api_endpoint` to your Dynatrace OTLP endpoint.
3. Authenticate with a Dynatrace API token (the sample reads it from `/etc/secrets/dynatrace_otel`).

For more configuration options, see the [Get started with AI Observability](/docs/observe/dynatrace-for-ai-observability/get-started "Learn how to set up OpenLLMetry to observe an AI/ML model.") guide.

### Run the sample

1. Set your OpenAI or Azure OpenAI credentials as environment variables.

   ```
   export OPENAI_API_KEY=your_api_key
   ```

   ```
   export AZURE_OPENAI_API_KEY=your_api_key



   export AZURE_OPENAI_API_VERSION='2024-08-01-preview'



   export AZURE_OPENAI_ENDPOINT=your_endpoint



   export AZURE_OPENAI_DEPLOYMENT=your_deployment
   ```

   Alternatively, set the environment variables in an `.env` file in `python-backend` and load them with `python-dotenv`.
2. Install backend dependencies.

   ```
   cd python-backend



   python3.12 -m venv .venv



   source .venv/bin/activate



   pip install -r requirements.txt
   ```
3. Install UI dependencies.

   ```
   cd ui



   npm install
   ```
4. Start the app.

   ```
   npm run dev
   ```

   The frontend is available at `http://localhost:3000`. This command also starts the backend.

## Observe OpenAI request costs using logs

Using logs to collect and observe OpenAI request costs is both simple and powerful. It allows the owner of the service to write a log line using a standard Node.js logging framework such as [Winstonï»¿](https://www.npmjs.com/package/winston) and to collect and analyze those logs within Dynatrace.

The following code snippet writes a Winston log line containing the OpenAI request token counts.

```
logger.log('info', `OpenAI response promt_tokens:${response.data.usage.prompt_tokens} completion_tokens:${response.data.usage.completion_tokens} total_tokens:${response.data.usage.total_tokens}`);
```

The OpenAI request log lines can be viewed in the Dynatrace log viewer.

We recommend that you also enable trace context enrichment for Node.js logs (go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Preferences** > **OneAgent features** and turn on **Node.js Trace/span context enrichment for logs**) to automatically map all log lines to their captured request traces.

![Trace context enrichment setting](https://dt-cdn.net/images/openai-logs-2912-9de465dc73.png)

With **Node.js Trace/span context enrichment for logs** enabled, you even get a convenient mapping of all OpenAI traces with their log lines. You can view them at ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** > **Explorer** > **Logs**.

![Logs explorer](https://dt-cdn.net/images/open-ai-logs-prev-2912-b5ac096261.png)

## Observe OpenAI request cost by sending custom metrics

Each request to an OpenAI model, such as GPT-5.2 or GPT-5.1, reports back how many tokens were used for the request prompt (the length of your text question) and how many tokens the model generated as a response.

By extracting token measurements from the returning payload and reporting them through OneAgent, users can observe the token consumption across all OpenAI-enhanced services in their monitoring environment.

To extract the token count from the OpenAI response and report those measurements to the local OneAgent, add the following instrumentation to your Node.js service.

```
function report_metric(openai_response) {



var post_data = "openai.promt_token_count,model=" + openai_response.model + " " + openai_response.usage.prompt_tokens + "\n";



post_data += "openai.completion_token_count,model=" + openai_response.model + " " + openai_response.usage.completion_tokens + "\n";



post_data += "openai.total_token_count,model=" + openai_response.model + " " + openai_response.usage.total_tokens + "\n";



console.log(post_data);



var post_options = {



host: 'localhost',



port: '14499',



path: '/metrics/ingest',



method: 'POST',



headers: {



'Content-Type': 'text/plain',



'Content-Length': Buffer.byteLength(post_data)



}



};



var metric_req = http.request(post_options, (resp) => {}).on("error", (err) => { console.log(err); });



metric_req.write(post_data);



metric_req.end();



}
```

The three new OpenAI token consumption metrics are available in Dynatrace.

![OpenAI token consumption metrics collected in Dynatrace](https://dt-cdn.net/images/openai-dashboard-2-2551-f433fa0e84.png)

## Dynatrace Intelligence automatically detects GPT as root cause

Dynatrace Intelligence automatically learns the typical behavior of monitored services.

When an abnormal slowdown or increase of errors is detected, Dynatrace Intelligence triggers a root cause analysis to identify the cause of complex situations.

Our simple example of a Node.js service entirely depends on the ChatGPT model response. Whenever the latency of the model response degrades or the model request returns with an error, Dynatrace Intelligence automatically detects it.

---

## observe/dynatrace-for-ai-observability.md

---
title: AI and LLM Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability
scraped: 2026-02-22T21:09:47.549127
---

# AI and LLM Observability

# AI and LLM Observability

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Jan 28, 2026

AI observability is the practice of collecting, analyzing, and correlating telemetry across your tech stack to understand how AI systems, agents, and LLMs behave in all environments including production. It enables real-time visibility into LLMs, AI agents, orchestration layers, and their downstream impact on your application and infrastructure.

AI observability delivers actionable insights that enable developers, SREs, and platform teams to debug, optimize, and improve AI-powered services, ensuring they stay reliable, performant, cost-efficient, and meet quality standards.

Full-stack observability for AI apps is especially critical when working with AI platforms like OpenAI, Anthropic, Gemini (Google Cloud), Amazon Bedrock, Azure AI Foundry, and Vertex AI, where model execution happens externally and opaquely, yet directly affects business-critical workflows.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Get a holistic view of the AI-generated parts of your system such as LLM, vector databases, and prompt engineering frameworks to gain comprehensive insights.](https://www.dynatrace.com/hub/?filter=ai-ml-observability&internal_source=doc&internal_medium=link&internal_campaign=cross)

## Dynatrace end-to-end AI and LLM observability

Dynatrace unifies metrics, logs, traces, problem analytics, and root cause information in dashboards and notebooks, providing a single operational view of your AI-powered cloud applications end-to-end.

Use Dynatrace with [Traceloop OpenLLMetry](/docs/observe/dynatrace-for-ai-observability/get-started "Learn how to set up OpenLLMetry to observe an AI/ML model.") or [OpenTelemetry with GenAI semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/gen-ai/) to gain detailed insights into your generative AI stack.

![Full AI/ML observability with Dynatrace](https://dt-cdn.net/images/ai-obs-tech-stack-latest-1892-88a8b44f2c.png)

This approach covers the complete AI stack, from foundational models and vector databases to RAG orchestration frameworks, ensuring visibility across every layer of modern AI applications.

## Key metrics for AI observability

* **Stability**: Frequency of successful model responses vs. failures.
* **Latency**: Time taken by models or services to return results.
* **Load**: Volume of requests handled; identify abnormal load spikes or drops.
* **Model drift**: Changes in model accuracy due to shifting input data.
* **Data drift**: Monitoring input data stationarity to anticipate model drift.
* **Cost**: Token usage, service fees, or overall resource consumption.

Observing AI models is inherently domain-driven: model owners must expose critical logs, metrics, and data to enable effective monitoring.

## Dynatrace Platform capabilities

* **Monitoring**: Continuous collection and analysis of model metrics, events, logs.
* **Logging**: Captures relevant events and errors for debugging and post-mortem analysis.
* **Metrics & Performance Analysis**: Dashboards and notebooks for performance trends.
* **Visualization**: Domain-specific dashboards to quickly identify patterns and issues.
* **Anomaly Detection**: Automated alerts for deviations from normal patterns.
* **Explainability & Interpretability**: Techniques to illuminate a model's decision-making process.

![Unlock your AI and LLM observability with Dynatrace](https://dt-cdn.net/images/ai-obs-a-b-test-7233-74b08ff0a7.png)

## Key use cases for AI observability

* **Monitor service health and performance**: Track real-time metrics (request counts, durations, and error rates). Stay aligned with SLOs.
* **Monitor service quality and cost**: Implement error budgets for performance and cost control. Validate model consumption and response times. Prevent quality degradation by monitoring models and usage patterns in real time.
* **End-to-end tracing and debugging**: Trace prompt flows from initial request to final response for quick root cause analysis and troubleshoot. Gain granular visibility into LLM prompt latencies and model-level metrics. Pinpoint issues in prompts, tokens, or system integrations.
* **Build trust, reduce compliance and audit risks**: Track every input and output for an audit trail. Query all data in real time and store for future reference. Maintain full data lineage from prompt to response.

By embracing AI observability, organizations improve reliability, trustworthiness, and overall performance, leading to more robust and responsible AI deployments.

### Observing Agents and Agentic workloads

Get visibility into Agentic AI workloads: agent execution paths, tool invocations, and inter-agent communication. Monitor and debug Agent interactions such as function calling, LLM calls, tool-use, RAG, and resolve performance, latency, cost, and reliability issues.
Dynatrace integrates with workloads such as OpenAI Agent SDK, LangChain/LangGraph Agents, CrewAI, Amazon Bedrock Agentcore, MCP tools, Google ADK, and [many moreï»¿](https://www.dynatrace.com/hub/?filter=ai-ml-observability).

### Observing model providers and platforms

Dynatrace integrates with providers such as [OpenAI](/docs/observe/dynatrace-for-ai-observability/models-and-platforms/openai "OpenAI observability"), [Amazon Bedrock](/docs/observe/dynatrace-for-ai-observability/models-and-platforms/bedrock "Bedrock observability"), [NVIDIA NIM](/docs/observe/dynatrace-for-ai-observability/models-and-platforms/nvidia-nim "NVIDIA NIM observability"), [Ollama](/docs/observe/dynatrace-for-ai-observability/models-and-platforms/ollama "Ollama observability") to monitor performance (token consumption, latency, availability, and errors) at scale.

### Observing semantic caches and vector databases

Vector databases and semantic caches are central to RAG architectures. Dynatrace monitors solutions like [Milvusï»¿](https://www.dynatrace.com/hub/detail/milvus), [Weaviateï»¿](https://www.dynatrace.com/hub/detail/weaviate), and [Qdrantï»¿](https://www.dynatrace.com/hub/detail/qdrant) to help identify performance bottlenecks and usage anomalies.

### Observing orchestration frameworks

Frameworks like [LangChain](/docs/observe/dynatrace-for-ai-observability/orchestration-frameworks/langchain "LangChain observability") manage data ingestion and prompt engineering for RAG applications. Dynatrace ensures you can track performance, versions, and degradation points in these pipelines.

### Observing infrastructure and resources

Monitor infrastructure usage (GPU/TPU metrics, temperature, memory, etc.) for cloud services such as [Amazon Elastic Inference](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-inference "Monitor Amazon Elastic Inference and view available metrics.") and [Google TPU](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace."), or custom hardware like [NVIDIA GPUï»¿](https://www.dynatrace.com/hub/detail/nvidia-gpu). This helps optimize resources and supports sustainability initiatives.

An overview of all of our integrations can be found on our [Dynatrace Hub pageï»¿](https://www.dynatrace.com/hub/?filter=ai-ml-observability)

## AI observability provided by Dynatrace

Dynatrace, a software intelligence company, has implemented its own AI observability solution to monitor, analyze, and visualize the internal states, inputs, and outputs of its own AI models.

The example below shows one of many self-monitoring dashboards that Dynatrace data scientists use to observe the operation of [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") across all monitoring environments.

![An example of an anomaly detection self-monitoring dashboard.](https://dt-cdn.net/images/dashboards-self-monitoring-model-statistics-1818-c5c0a57141.png)

---
