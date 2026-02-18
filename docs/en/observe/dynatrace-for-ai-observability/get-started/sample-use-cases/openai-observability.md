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