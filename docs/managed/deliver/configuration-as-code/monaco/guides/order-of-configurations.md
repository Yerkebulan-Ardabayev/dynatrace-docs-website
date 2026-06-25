---
title: Ensure order of configurations
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/order-of-configurations
scraped: 2026-05-12T12:03:00.691578
---

# Ensure order of configurations

# Ensure order of configurations

* How-to guide
* 2-min read
* Updated on Jul 14, 2023

This guide shows how to enforce the order of configurations using Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI).

## Goal

While the web UI allows you to define the order of certain configurations, it's not possible to define an order with the Dynatrace Monaco CLI or the Dynatrace API.

* Using the API directly, you can control if rules are appended or prepended, but not in the exact order.
* Using the Dynatrace Monaco CLI, this control is not possible.

However, you can use the way the Dynatrace Monaco CLI handles dependencies between configurations to enforce rule order.

## Define rule order using dependencies

By creating fake dependencies between rules, the Dynatrace Monaco CLI ensures that a rule is created before another rule that depends on it. This workaround is successful only if all the rules are created from the Dynatrace Monaco CLI and don't already exist.

If rules already exist, you can manually re-order them, with updates from future configuration deployments not impacting the order.

Because newly added rules are prepended to existing rules, you will likely need to define dependencies in the opposite order than you expect. The following sample shows how to ensure order using dependencies.

Consider the following example showing a `config.yaml` file containing two app detection rules named `rule1` and `rule2`.

```
configs:



- id: rule2



config:



name: rule2



template: rule2.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment



- id: rule1



config:



name: rule1



template: rule1.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment
```

During the deployment process, `rule2` will probably be deployed before `rule1`. However, to guarantee that `rule1` is always deployed before `rule2`, you can introduce a pseudo-reference parameter within `rule2`, indicating its dependency on `rule1`. This ensures that `rule2` is deployed after `rule1`.

```
configs:



- id: rule2



config:



name: rule2



template: rule2.json



skip: false



parameters:



order:



configId: rule1



property: id



type: reference



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment



- id: rule1



config:



name: rule1



template: rule1.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment
```