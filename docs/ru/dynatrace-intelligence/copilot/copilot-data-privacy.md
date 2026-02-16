---
title: Dynatrace Intelligence generative AI data privacy and security
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-data-privacy
scraped: 2026-02-16T09:29:33.353940
---

# Dynatrace Intelligence generative AI data privacy and security

# Dynatrace Intelligence generative AI data privacy and security

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Jan 28, 2026

At Dynatrace, we take our responsibility to safeguard your data seriously. Understand how Dynatrace Intelligence generative AI uses your data and understand your responsibility to keep your data secure.

## Prompt data

Although we mask Personally Identifiable Information (PII), we still recommend exercising caution when including personal or confidential information in your prompts.

Your prompts are sent to LLMs hosted by enterprise vendors such as Microsoft Azure AI and AWS Bedrock, which power Dynatrace Intelligence generative AI. Enterprise vendors don't store the data you submit or the responses you receive. The prompts you submit and the responses you receive are used only to serve your experience. Enterprise vendors also don't use the prompts to fine-tune or improve any models or services, or to train models across customers or environments.

Each data request is sent to the LLM individually, over an SSL-encrypted service, processed by respective enterprise vendors, and sent back to Dynatrace. If your environment is located in EMEA, your prompts are processed in an EU region. If your environment is located in NORAM, LATAM, or APAC, your prompts are processed in a US region.

Dynatrace may store the prompts submitted to Dynatrace Intelligence generative AI and the responses provided by the LLMs to understand the use cases, contextualize the feedback on the responses, and identify additional user expectations.

Learn more about the [Dynatrace Intelligence generative AI architecture and data flow](/docs/dynatrace-intelligence/copilot/copilot-overview#copilot-data-flow "Learn about data security and other aspects of Dynatrace Intelligence generative AI.").

## PII masking

Dynatrace version 1.305+

Starting with Dynatrace version 1.305, PII masking is in place for user prompts. This ensures that sensitive information included in your prompts won't be forwarded to LLMs hosted by enterprise vendors.

Currently masked fields include:

* Email address
* Phone number
* IBAN information
* Credit card number
* IP address
* US bank number
* US social security number
* US ABA routing numbers
* URL query parameters (only parameters with more than two characters are considered)
* Canadian Social Insurance Number (SIN)

In our logs and calls to LLM models, we replace values from the identified patterns above with fake patterns. This means that you'll be able see IBANs in logs, for example, but they'll be made up of random numbers, replacing the original values included in your prompts.

## Related topics

* [Dynatrace Intelligence generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence generative AI.")
* [Get started with Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence generative AI.")
* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")