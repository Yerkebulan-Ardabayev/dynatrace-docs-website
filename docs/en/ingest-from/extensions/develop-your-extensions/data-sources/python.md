---
title: Dynatrace Extensions Python SDK
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/python
scraped: 2026-03-06T21:32:00.044917
---

# Dynatrace Extensions Python SDK

# Dynatrace Extensions Python SDK

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Mar 04, 2026

The Dynatrace Extensions Python SDK provides you with a framework to ingest data into Dynatrace from any technology exposing an interface.

Custom-coded extensions are based on the same principles. They're declarative, similar to other data sources, but you use the provided methods to use extracted data to create metrics and events.

This SDK offers:

* Greater flexibility to ingest the data from your proprietary technologies or when your case requires extended customization that available data sources don't offer.
* Tooling to export your current OneAgent and ActiveGate extensions to the new framework.

Dynatrace Extensions Python SDK is publicly available with [OneAgent 1.285](../../../../whats-new/oneagent/sprint-285.md#custom-coded-python-extensions "Release notes for Dynatrace OneAgent version 1.285").

Set the filesystem flag to `exec` and not `noexec` to ensure a Python extension runs correctly. This configuration is crucial because it allows the execution of binaries and scripts within the specified filesystem. The extension can't execute properly without this setting, leading to potential errors and failures.

Python 3.10 reaches end of life in October 2026. For extensions built with the Dynatrace Extensions Python SDK, the build command must use `--python-version 3.14`.
For more information, see the [build command guideï»¿](https://github.com/dynatrace-extensions/dt-extensions-python-sdk/blob/main/docs/guides/building.rst).

For more information, see:

* [Dynatrace Extensions Python SDK documentationï»¿](https://dt-url.net/7g638yh)
* [Dynatrace Extensions Python SDK repositoryï»¿](https://dt-url.net/jsa38pm) on Dynatrace Extensions GitHub.