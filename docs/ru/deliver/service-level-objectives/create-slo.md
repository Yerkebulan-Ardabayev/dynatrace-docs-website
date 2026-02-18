---
title: Create service-level objectives
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/create-slo
scraped: 2026-02-18T21:34:36.251123
---

# Create service-level objectives

# Create service-level objectives

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Nov 05, 2024

With ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, you can configure new service-level objectives (SLO)s from templates provided by Dynatrace.
You can also define your SLOs based on a custom [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") query.

## Steps

### Create an SLO from template

To create a new SLO with a predefined template

1. In **Dynatrace**, search for ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** and open it.
2. Select  **Service-level objective**.
3. In the SLO wizard, choose one of the following:

   * **Host CPU usage utilization**
   * **Service availability**
   * **Service performance**
   * **Kubernetes cluster CPU usage efficiency**
   * **Kubernetes cluster memory usage efficiency**
   * **Kubernetes namespace CPU usage efficiency**
   * **Kubernetes namespace memory usage efficiency**
4. Select **Create** for one of the above options.
5. Choose the entities that should meet your objective. If you're using the **Service performance** template, enter a value in milliseconds in **Requests should be faster than**.
6. Optional Select segments , choose the required segment(s), and select **Apply**. This reduces the number of filter results.

   ![Add segments filter to the SLO](https://dt-cdn.net/images/slo-level-segments-1313-399767711c.png)

   This is only an additional filter for the required entities. It does not apply to the SLO evaluation. To add the segment filter to the SLO evaluation, use step 5 in the [Create a custom SLO](/docs/deliver/service-level-objectives/create-slo#create-a-custom-slo "Create and configure service-level objectives (SLOs).") section.
7. Select **Next**.
8. Define the criteria of your SLO. Fill in the **Target** field and select the timeframe for the evaluation period by using the dropdown in the **Over the evaluation period** field.
9. Optional Turn on **Show warning** and enter the numeric percent in **Show warning at** field.
10. Select **Next**.
11. Enter a name for your SLO in **SLO Name**.
12. Optional Provide a meaningful description of what your SLO is about in **SLO description**.
13. Optional Provide tags for your SLO in the **Tags** section by filling in the **Key** and **Value** fields. Select **Add** to save the tags. Tags can be used to provide additional metadata for your SLOs, such as a responsible ownership team or additional information about the underlying entities or criticality of your SLO.
14. Select **Save**.

### Create a custom SLO

1. In **Dynatrace**, search for ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**.
2. In the overview of **Service-Level Objectives**, select  **Service-level objective**.
3. Select  **Custom SLO**.
4. Provide your DQL query. Your query has to include an "sli" field like in the following example, to ensure consistent visualization, transformation, and aggregation across your SLOs. The "sli" field needs to return an array of `double` type. The DQL query can be based on any data type in Grail, such as events or logs. Using the [makeTimeseries](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#makeTimeseries "DQL aggregation commands") provides the possibility to create an sli time series that can be used for calculating the SLO status.

```
timeseries { total=sum(dt.service.request.count) ,failures=sum(dt.service.request.failure_count) }



, by: { dt.entity.service }



, filter: { in (dt.entity.service, { services }) }



| fieldsAdd sli=(((total[]-failures[])/total[])*(100))
```

5. Optional Select segments , choose the required segment(s), and select **Apply**. This is an additional filter to the query.

   The selected segments are stored with the SLO definition. Those filters are effective with future segment modifications and new entity creations with the same DQL query.
6. Select **Next**.
7. Define the criteria of your SLO. Fill in the **Target** field and select the timeframe for the evaluation period by using the dropdown in the **over the evaluation period** field.
8. Optional Turn on **Show warning** and enter the percentage in **Show warning at**.
9. Select **Next**.
10. Provide the name for your SLO in the **SLO Name** field.
11. Optional Provide a meaningful description of what your SLO is about in the **SLO description** field.
12. Optional Provide tags for your SLO in the **Tags** section by filling in the **Key** and **Value** fields. Select the **Add** button to save the tags. Tags can be used to provide additional metadata to your SLOs, such as a responsible ownership team or additional information about the underlaying entities or criticality of your SLO.
13. Select the **Save** button to create your SLO.

## Create and manage SLOs via API

You can create, edit, list, delete, and evaluate your SLOs via API.

1. Go to Dynatrace.
2. In the [platform search](/docs/discover-dynatrace/get-started/dynatrace-ui#search "Navigate the latest Dynatrace"), type `API`. In the search results, see **Support resources** section and **Dynatrace API** below it.
3. Select **Dynatrace API** to access the Dynatrace API documentation. A new page opens with the Dynatrace API definitions.
4. In the upper right corner, go to **Select a definition**.
5. From the drop-down list, choose the endpoint.
6. Authenticate with your API token. For more details, see [Authentication](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.").