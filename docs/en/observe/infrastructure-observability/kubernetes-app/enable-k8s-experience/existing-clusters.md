---
title: Enable Kubernetes experience for existing clusters
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/enable-k8s-experience/existing-clusters
scraped: 2026-02-25T21:14:55.822150
---

# Enable Kubernetes experience for existing clusters

# Enable Kubernetes experience for existing clusters

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Jan 19, 2024

You have the option to enable all or specific Kubernetes clusters to benefit from the new Kubernetes experience.

You could accomplish this using the Settings API with the [Kubernetes app schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-app-transition-kubernetes "View builtin:app-transition.kubernetes settings schema table of your monitoring environment via the Dynatrace API."), or alternatively, by configuring the setting as described next.

To fully disable the Kubernetes experience and stop Kubernetes monitoring or related license consumption, make sure the setting is turned off at both the environment and cluster level.

## Enable all clusters

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Cloud and virtualization** > ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**.
2. Turn on **New Kubernetes experience**.

## Enable specific clusters

1. In ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, select **Activation pending** in the top menu bar.
2. Select **Activate** for your desired cluster.

   ![Activation pending](https://dt-cdn.net/images/activation-pending-3718-f43bc57878.png)
3. Turn on **New Kubernetes experience**.

When you enable Kubernetes clusters for the new Kubernetes experience, Dynatrace starts to report observability data to the Dynatrace platform, including Grail as a data lakehouse.