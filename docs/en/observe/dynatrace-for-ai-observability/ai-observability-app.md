---
title: AI Observability
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/ai-observability-app
scraped: 2026-02-28T21:22:44.908993
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

Get a unified view of the operational state of your AI services. **Service Health** is organized into focused tabs so you can move from a high-level pulse to root cause in a couple of clicks.

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