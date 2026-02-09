---
title: "Dynatrace Intelligence generative AI - Tips for writing better prompts"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips
updated: 2026-02-09
---

# Dynatrace Intelligence generative AI - Tips for writing better prompts

# Dynatrace Intelligence generative AI - Tips for writing better prompts

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI is a helpful tool for getting insights from your data without needing to learn DQL. However, as generative AI, it sometimes needs a bit of structure to ensure you get the best results. The following are tips for writing better prompts for quickly analyzing data in Notebooks and Dashboards.

## Tip 1: Make your prompt clear

Natural language is often nuanced and ambiguous, but making your prompt clear should generate better DQL queries:

* Remove and rewrite any words or phrases that aren't clear or could be interpreted in different ways.
* Avoid the use of subjective language like "interesting findings" that is open to interpretation.
* Write in short, simple sentences. You can combine multiple short sentences in a prompt; Dynatrace Intelligence generative AI understands this better than a single long or complex sentence.
* Start your prompt with **"Show me"** instead of phrases such as **"I would like to see"** and **"Tell me about"**.
* Ask yourself if a DQL expert could create a query from your prompt. If not, it probably needs to be clearer.

**Try:**

* Show me the average CPU usage for each host.

**Avoid:**

* CPU usage.
* I want to see an overall summary of the CPU usage for each host over the last week.

## Tip 2: Make your prompt specific

If you know the table where your data is located, specify it. It is especially helpful to be specific about elements such as "events" or "bizevents".

**Try:**

* Show me the number of new trip bizevents for the last day.
* Show me all error logs.

**Avoid:**

* Show me new trips.
* Show me errors.

## Tip 3: Sequence your prompt

When you're writing a complex prompt, it's good practice to make the order of the individual steps clear. Try writing the process in a step-by-step manner.

**Try:**

* First get all logs with errors, then extract the host ID only. Then lookup the CPU usage for the host IDs.

**Avoid:**

* Get the host ID from all logs with errors and lookup CPU usage.

## Tip 4: Try to gradually refine your prompt

If your prompt doesn't seem to work, try refining it to identify where Dynatrace Intelligence generative AI is getting stuck. Start with a simple statement, then gradually add more details.

For example, start with writing only the main part, such as **"Show all logs"**.

Optional If the prompt doesn't give you the intended results, gradually change it until it does. For example, **"Show me the number of logs by status"**.

Once the simpler steps work, add additional steps one by one, for example, **"Show me the number of logs by status as a timeseries"**.

## Tip 5: Use DQL syntax in your prompt

Using keywords from the DQL syntax keywords in your prompts will often generate better DQL queries. Some of the most common keywords are:

* Fetch
* Filter
* Sort
* Summarize
* Lookup

**Try:**

* Fetch all error logs and lookup the host name.

**Avoid:**

* Look at logs with errors and add matching results from the host names.

## Tip 6: Follow the DQL hierarchy in your prompt

We recommend that you get familiar with the [DQL documentation](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). The more you can reflect the DQL syntax hierarchy in your prompt, including command order, the more effective your prompts will be. For example:

* Mention filters at the beginning of your prompt
* Mention sort orders at the end of your prompt

## Known limitations

We are actively working on improving and extending the Dynatrace Intelligence generative AI abilities. You might run into issues with some of the use cases that are still in progress, for example:

* Requesting a specific visualization in your prompt. Prompts like **"Show me logs by status as pie chart"** aren't supported yet and will not work.
* Running forecasts with Dynatrace Intelligence data analyzers. Prompts like **"Forecast whenâ¦"** aren't supported yet and will not work. However, you can provide Dynatrace Intelligence generative AI with a prompt starting with **"Show meâ¦"**, and then enable a Dynatrace Intelligence data analyzer on this section or tile.
* Specifying management zones via the prompt.

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence generative AI.")
