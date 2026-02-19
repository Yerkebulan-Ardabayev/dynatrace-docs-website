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