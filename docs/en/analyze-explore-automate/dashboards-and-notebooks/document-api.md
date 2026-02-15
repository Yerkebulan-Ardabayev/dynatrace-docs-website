---
title: API for Dashboards and Notebooks
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-api
scraped: 2026-02-15T09:10:09.623813
---

# API for Dashboards and Notebooks

# API for Dashboards and Notebooks

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 23, 2024

The Dynatrace platform provides a collection of [platform servicesï»¿](https://dt-url.net/sx23ug5), each with a specific area of responsibility. You need one of these services, the [document serviceï»¿](https://dt-url.net/x403ua9), to manage Dynatrace documents such as dashboards and notebooks via API.

## Access document data

The ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** apps use the document service API to persist data as documents.

Documents are content-agnostic, but both notebook and dashboard documents have common metadata: a unique identifier, a name, and a description.

To distinguish notebook and dashboard documents, and to make them visible to the respective apps, they need the correct `type` document attribute: `dashboard` or `notebook`. This attribute can also be used to query the API as shown in the following examples.

#### List all accessible dashboards

```
https://environment/platform/document/v1/documents?filter=type='dashboard'
```

#### List all accessible notebooks

```
https://environment/platform/document/v1/documents?filter=type='notebook'
```

## Access full document service documentation

To see the full API documentation for the documents service

1. Go to the [Document serviceï»¿](https://dt-url.net/x403ua9) page of the [Dynatrace Developerï»¿](https://developer.dynatrace.com/) site.
2. In the **Related links** section, select the **Swagger API** link.

   You may need to sign in to your Dynatrace environment.