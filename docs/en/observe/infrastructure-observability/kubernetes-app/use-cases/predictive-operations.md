---
title: Predictive Kubernetes operations
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/kubernetes-app/use-cases/predictive-operations
scraped: 2026-02-28T21:30:44.409488
---

# Predictive Kubernetes operations

# Predictive Kubernetes operations

* Latest Dynatrace
* Tutorial
* 9-min read
* Updated on Feb 04, 2026

In today's dynamic IT landscape, managing disk space effectively in Kubernetes-based services is crucial for maintaining optimal performance and avoiding potential data loss.

This best practice guide demonstrates how teams can utilize Dynatrace workflows for automated disk resizing to proactively manage disk space within Kubernetes environments.

Designed for ease of understanding by both technical and non-technical audiences, this guide highlights the value of automating disk space management. By implementing this practice, teams can significantly reduce manual intervention, ensure smooth operations of their Kubernetes services, and maintain system efficiency. The approach focuses on preemptively addressing disk space issues before they escalate, thereby safeguarding data integrity and enhancing overall service performance.

## Target audience

This use case is intended for system administrators, DevOps engineers, and site reliability engineers (SREs) who manage Kubernetes-based services and infrastructure.

You should have a basic understanding of Kubernetes environments, including concepts like nodes, pods, and disk utilization.

Familiarity with Dynatrace, particularly its AI capabilities like Dynatrace Intelligence for predictive analytics and automated workflows, is beneficial but not mandatory. The content is also relevant for teams looking to automate and improve their Kubernetes infrastructure management, ensuring optimal performance and resource utilization without the need for deep technical expertise in Dynatrace.

This guide aims to provide practical steps for those responsible for maintaining the stability and efficiency of Kubernetes services, especially in scenarios of dynamic resource requirements.

## Scenario

In a large-scale Kubernetes environment, an operations team is responsible for managing multiple nodes and critical services that require constant and efficient disk space management. They face a challenge: ensuring optimal disk utilization for each service without manual intervention. The team needs a scalable solution that can proactively manage disk space to prevent service disruptions and data loss, especially during unexpected spikes in traffic or resource demand.

The current process of manually monitoring and resizing disks is time-consuming and prone to errors, leading to either over-provisioning (wasting resources) or under-provisioning (risking service disruption). The team seeks an automated approach to dynamically adjust disk space based on real-time usage and projected needs.

By implementing the automated disk resizing feature in Dynatrace, the team aims to:

* Automatically detect and address disk space shortages within the Kubernetes environment.
* Use predictive analytics to calculate required disk space adjustments in real time.
* Ensure consistent application of configuration changes across all Kubernetes clusters.
* Reduce manual monitoring and intervention, thus saving time and resources.

This scenario illustrates a common challenge in managing Kubernetes-based services at scale and how Dynatrace automation capabilities can provide an efficient solution. The goal is to maintain uninterrupted service and optimal performance through intelligent, automated disk management.

This particular case is an example on how to make sure that on a sudden spike in traffic, an immediate need for extra disk space for Kafka is allocated to accommodate the increased message queue.

## Prerequisites

Make sure all of these are true before you start.

### Permissions

* You have access to a Dynatrace environment with the necessary permissions for configuration and monitoring.
* You have access to Kubernetes Configurations and you're able to retrieve and modify Kubernetes service configurations for disk size adjustments.

### Knowledge

* You have basic knowledge of Kubernetes architecture, including nodes, pods, and services.
* You have experience with Kubernetes Disk Management: Understanding of disk utilization in Kubernetes and the challenges associated with managing disk space in dynamic environments.
* You know how to set up automated workflows in Dynatrace for responding to disk space alerts. See [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* You know how to set up monitoring and alerting mechanisms within Dynatrace for Kubernetes environments.
* You understand GitOps principles, particularly for managing Kubernetes configurations through repository-based approaches.

## Steps

To keep the internal systems up and running, create an automated workflow for Kubernetes (K8s) disk management. This process is tailored to ensure critical internal services maintain optimal performance, even when unexpected disk utilization spikes occur. By leveraging continuous monitoring and automated remediation steps, downtime is minimized and maintains the consistency of the operations.

### 1. Set up continuous monitoring

[Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") to continuously monitor all services within the Kubernetes infrastructure. When your monitoring is providing you with data, [set up an alert](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") for disk utilization exceeding a 60% threshold to ensure optimal performance without resource wastage. With this alert, you'll be able to model a workflow for solving a disk size shortage issue.

### 2. Set up configuration file retrieval through ownership

With [ownership](/docs/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") assigned to objects, you can store the repository information. On detecting an anomaly, the system identifies the impacted service and fetches its associated configuration file. This step ensures that any adaptation made aligns directly with the specific service configuration.

### 3. Set up a workflow

Use the configuration retrieval on the alert to trigger the workflow. The workflow is composed of the following steps:

1. Identify the host with the disk that needs your attention.
   Use DQL as your workflow input.

   ```
   fetch dt.entity.host | filter like(entity.name, "%-grail kafka") | limit 1
   ```
2. Identify the disk.
   Use DQL as your workflow input.

   ```
   fetch dt.entity.disk  | fieldsAdd belongs_to[dt.entity.host] | filter belongs_to[dt.entity.host] == "{{result('query_grail_kafka_hosts').records[0].id}}"
   ```
3. Use Dynatrace Intelligence to calculate the necessary disk size.

   Dynatrace Intelligence analyzes the current disk usage compared to expected inflows, determining the appropriate disk size adjustment. This calculated response ensures both immediate and future needs are addressed.

   Use the Run Javascript workflow action to extract the prediction using the Dynatrace SDK [Automation utils packageï»¿](https://developer.dynatrace.com/reference/sdks/automation-utils/).

   Show me code

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function ({ executionId }) {



   const ex = await execution(executionId);



   // In this demo workflow we use a previous grail query to get a valid host ID.



   // Usually this would come from a Davis Event



   const res = await ex.result("analyze_with_davis_1");



   let prediction = 0.0;



   let validPrediction = true;



   try {



   const points = res.result.output[0].timeSeriesDataWithPredictions.records[0]["dt.davis.forecast:point"];



   console.log("Got these prediction: %s", points);



   const floatPoints = points.map(p => Number(p));



   prediction = Math.max(...floatPoints);



   console.log("Max value is: %s", prediction);



   } catch (e) {



   console.error("Unable to predict: %s", e instanceof Error ? e.message : JSON.stringify(e));



   validPrediction = false;



   }



   return {



   prediction,



   validPrediction,



   };



   }
   ```
4. Determine the ownership.
   Knowing the ownership will enable you to pick the right repository to apply the new disk size configuration.

   * Use the Ownership action to identify the owners of the disk entity you identified earlier.
   * With the ownership information, in the next step, you'll be able to identify the right repository to apply the change:

     Show me code

     ```
     import {



     monitoredEntitiesClient



     } from "@dynatrace-sdk/client-classic-environment-v2";



     import {



     execution



     } from '@dynatrace-sdk/automation-utils';



     async function getEntityName(entityId) {



     const data = await monitoredEntitiesClient.getEntity({



     entityId: entityId,



     });



     return data.displayName;



     }



     function isKafkaEntity(entityName) {



     return entityName.match(/(\[a-z0-9-]+)-grail kafka/) !== null;



     }



     async function getKafkaConfigURL(ex, entityName) {



     const owners = (await ex.result("get\_owners")).owners;



     let repoLink = undefined;



     // Go though all the owners and figure out which one as a REPOSITORY link type set.



     // We assume that is the correct one and will just use it later for building the URL



     for (const owner of owners) {



     for (const link of owner.links) {



     if (link.linkType === "REPOSITORY") {



     repoLink = link.url;



     break;



     }



     }



     if (repoLink !== undefined) {



     break;



     }



     }



     // "Gracefully" fail and tell the user that no owner had the required link type set;



     // Helps with debugging since otherwise we would build a URL undefined/... which can



     // cause more problems down the line.



     if (repoLink === undefined) {



     throw new Error('No REPOSITORY link was provided for any tagged owner!')



     }



     const baseUrl = repoLink;



     const file = "app//kafka-worker/kafka-configuration/values-scoped.yaml";



     const cluster = entityName.match(/(\[a-z0-9-]+)-grail kafka/)\[1];



     return `${baseUrl}/${cluster}/${file}`;



     }



     export default async function({



     execution\ _id



     }) {



     const ex = await execution(execution\ _id);



     // In this demo workflow we use a previous grail query to get a valid host ID.



     // Usually this would come from a Davis Event



     const queryResults = await ex.result("query\_grail\_kafka\_hosts");



     const records = queryResults.records;



     // Only have a look at the first element because an event likely only



     // contains one element:



     const {



     id



     } = records\[0];



     // Use the following DQL to query host IDs for grail kafka entities



     // >>> fetch dt.entity.host | filter like(entity.name, "%-grail kafka")



     const name = await getEntityName(id);



     // name should be used here, but only if isKafkaEntity is true!



     return {



     isKafkaHost: isKafkaEntity(name),



     url: await getKafkaConfigURL(ex, name)



     };
     ```
5. Commit and create pull request/merge file.

   Use the Kubernetes workflow action to apply the new configuration. With the desired disk size identified, the workflow automatically creates a pull request. This pull request adapts the service configuration file to reflect the newly determined disk size.

   Show me code

   ```
   apiVersion: batch/v1



   kind: Job



   metadata:



   name: {{ "demo-job-resize-%s" % result('disk_from_host').records[0].id | lower }}



   labels:



   joblabel: "test"



   spec:



   ttlSecondsAfterFinished: 300



   backoffLimit: 0



   activeDeadlineSeconds: 60



   podFailurePolicy:



   rules:



   - action: FailJob



   onExitCodes:



   operator: NotIn



   values: [0]



   template:



   spec:



   restartPolicy: Never



   containers:



   - name: main



   image: docker.io/library/bash:5



   command: ["bash"]



   args:



   - -c



   - echo "Computing..."; sleep 10; echo $PATH_URL; echo $IS_KAFKA_HOST; echo $PREDICTION; echo $VALID_PREDICTION; test $VALID_PREDICTION = 'True'; exit $?



   resources:



   limits:



   memory: 10Mi



   cpu: 1m



   env:



   - name: PATH_URL



   value: "{{result('repository_url').url}}"



   - name: IS_KAFKA_HOST



   value: "{{result('repository_url').isKafkaHost}}"



   - name: PREDICTION



   value: "{{result('extract_prediction').prediction}}"



   - name: VALID_PREDICTION



   value: "{{result('extract_prediction').validPrediction}}"
   ```
6. Deploy.
   The modified configurations are deployed into the service through ArgoCD and ArgoWorkflows. This quick deployment minimizes service disruption and ensures that the adjustments are immediately effective.
7. Post-Deployment validation.
   After the configuration rollout, there's a validation phase where the system checks if the disk resize was successful and if the initial anomaly has been resolved.

If any issue arises during the workflow, the Dynatrace alerting system ensures that potential complications get immediate attention. The workflow also incorporates the Ownership feature that determines the responsible entity for a given issue, ensuring efficient communication, for example using the Slack workflow action.

## Conclusion

By implementing automated disk resizing in Kubernetes environments with Dynatrace, teams can effectively manage disk space, ensuring their services run smoothly and efficiently. This guide has provided a comprehensive approach to setting up continuous monitoring, automating configuration updates, and ensuring effective deployment and validation. The integration of Dynatraceâs AI capabilities allows for predictive adjustments, reducing manual efforts and enhancing system reliability.

With these steps in place, teams can focus more on strategic tasks rather than constant monitoring and manual interventions. The ability to proactively manage resources in a Kubernetes environment is a significant step towards optimizing infrastructure performance and minimizing potential disruptions or data loss.

To fully leverage these benefits, you're encouraged to try implementing these practices in your Kubernetes environments. Experiment with the settings, monitor the results and adjust as necessary to fit your specific needs.

Explore further how Dynatrace can transform your approach to Kubernetes management, bringing efficiency and predictability to your operational workflows.

## Related topics

* [AI in Workflows - Predictive maintenance of cloud disks](/docs/dynatrace-intelligence/use-cases/davis-for-workflows "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")
* [Dynatrace Intelligence DQL examples](/docs/dynatrace-intelligence/use-cases/davis-dql-examples "Build powerful health dashboards by slicing and dicing of Dynatrace Intelligence reported problems and events using DQL.")