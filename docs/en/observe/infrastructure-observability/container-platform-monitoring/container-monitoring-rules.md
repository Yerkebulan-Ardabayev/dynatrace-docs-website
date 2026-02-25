---
title: Container monitoring rules
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/container-monitoring-rules
scraped: 2026-02-25T21:17:17.398511
---

# Container monitoring rules

# Container monitoring rules

* How-to guide
* 2-min read
* Published Jun 25, 2021

To manage all container-related settings, follow the instructions below.

## Define container monitoring rules

The container monitoring rules define if deep monitoring is enabled for processes running in containers.

**To add a monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Select **Add item**.
3. Select the **Mode**: whether you want Dynatrace to monitor the container.
4. Select the **Container property** to compare against your rule.
5. Select the condition operator (for example `begins with`)
6. Set the condition value.
7. Select **Save changes** to save your configuration and the new rule to your list of container monitoring rules.

**To edit a custom monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Find the rule and make your changes.

   * To change the rule conditions, display the **Details** and make changes as needed
   * To delete the rule, select in the **Delete** column
   * To disable or enable the rule, change the switch setting in the **Enabled** column
   * To move the rule up or down in the list, in the **Order** column, select and drag the rule to a new position

     Container monitoring rules are executed in the order in which they appear on the list.
3. Select **Save changes**.

## Enable or disable container monitoring rules

There are two categories of container monitoring rules that you can enable or disable by default:

* Custom rulesâcreated by you
* Built-in rulesâdefined by Dynatrace

**To enable/disable a custom monitoring rule**

1. Go to **Settings** > **Processes and containers** > **Container monitoring rules**.
2. Find the rule and change the switch setting in the **Enabled** column.
3. Select **Save changes** to save your configuration.

**To enable/disable built-in monitoring rules**

1. Go to **Settings** > **Processes and containers** > **Built-in container monitoring rules**.
2. Turn these rules on or off as needed:

   * Do not monitor containers where Kubernetes container name equals `POD`
   * Do not monitor containers where Docker stripped image name contains `pause-amd64`
   * Do not monitor containers where Kubernetes namespaces equals `openshift-sdn`
3. Select **Save changes** to save your configuration.

Built-in rules are enabled by default. You can choose to disable them, but you can't edit them.

## Limitations

* Container monitoring rules are effective only when you install OneAgent on your hosts.
* Application-only integrations without a full OneAgent installation donât support monitoring rules. However, in such situations, the integrations themselves effectively provide the same level of control over your container monitoring setup.
* In Kubernetes, container monitoring rules apply only to the `classicFullStack` injection mode.

  Container monitoring rules are ignored for webhook-based injection modes (`cloudNativeFullStack` or `applicationMonitoring`). For these modes, use the annotation-based configuration option as described in [Configure monitoring for namespaces and pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods").