---
title: Process group metadata for Cloud Foundry
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/define-process-group-metadata-for-cloud-foundry-applications
---

# Process group metadata for Cloud Foundry

# Process group metadata for Cloud Foundry

* 2-min read
* Published Feb 25, 2019

Dynatrace allows you to [define your own metadata](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") based on the needs of your organization or environment. You can also define process group metadata using a Cloud Foundry service and reuse it across multiple applications.

## Define Cloud Foundry service metadata

To define your own process group metadata, you can use one or more Cloud Foundry service instances that have the name `dynatrace` as a substring. For example:

```
cf cups dynatrace-metadata -p "meta-data:owner"
```

You’re automatically prompted to provide values for certain metadata. To update more than one at a time, separate by comma.

```
cf cups dynatrace-metadata -p "meta-data:owner, meta-data:github-source, meta-data:step"
```

If your monitored Cloud Foundry application is available on GitHub, you can easily add a link to the respective GitHub repository using custom process group metadata. As shown in the example below, we’ve specified custom process group metadata for a sample monolithic application called TicketMonster (you can read up on this in the blog post [Fearless Monolith to Microservices Migration – A guided journey﻿](https://www.dynatrace.com/news/blog/fearless-monolith-to-microservices-migration-a-guided-journey/) by Johannes Bräuer). We’ve added the [GitHub repository link of the TicketMonster application﻿](https://github.com/dynatrace-innovationlab/monolith-to-microservice-cloudfoundry/tree/master/monolith) as a github-source property and we’ve also identified the application as the monolithic starting point for the “break-up journey” towards a microservices architecture.

![Cloud Foundry metadata](https://dt-cdn.net/images/cf-metadata-example-1-1713-4b8cbb3f14.png)

Cloud Foundry metadata

If you’re leveraging [Cloud Foundry buildpacks](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.") to integrate Dynatrace OneAgent into your application, specifying the buildpack version that was used to deploy the application can be helpful in understanding the features that are available as part of a buildpack release.

```
cf cups dynatrace-apps-only-metadata -p "meta-data:buildpack, meta-data:version"
```

If you want to compare the behavior of two application versions in a [Blue-Green deployment﻿](https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html), you can also use custom process group metadata to identify different application versions.

In order to exploit the service instance `dynatrace-metadata` (or `dynatrace-*-metadata`) you must bind the instance to your application (for example, `ticket-monster`):

```
cf bs ticket-monster dynatrace-metadata
```

## Use custom process group metadata for organizing your Cloud Foundry applications

You can use your Cloud Foundry process group metadata as a placeholder when creating automatically applied tags (as shown in the example below) or for process group naming. The rule-based tag below will be added to the monolithic TicketMonster application and all related services. In this example, we’ve defined the custom process group `meta-data:step>monolith` to be the tag value.

![Cloud foundry metadata](https://dt-cdn.net/images/cf-metadata-example-2-1713-d1d3894ed6.png)

Cloud foundry metadata

![Cloud foundry metadata](https://dt-cdn.net/images/cf-metadata-example-3-1665-3c163aaccf.png)

Cloud foundry metadata

## Related topics

* [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")