---
title: AI in Workflows - Predictive maintenance of cloud disks
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-for-workflows
scraped: 2026-02-20T21:25:48.863545
---

# AI in Workflows - Predictive maintenance of cloud disks

# AI in Workflows - Predictive maintenance of cloud disks

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence data analyzers offer a broad range of general-purpose artificial intelligence and machine learning (AI/ML) functionality, such as learning and predicting time series, detecting anomalies, or identifying metric behavior changes within time series. Dynatrace Intelligence enables you to seamlessly integrate those analyzers into your custom workflows. An example use case is a fully automated task of predicting and remediating future capacity demands. It helps you to avoid critical outages by being notified days in advance before incidents even arise.

## Install Dynatrace Intelligence (Preview)

To use Dynatrace Intelligence actions, you first need to install **Dynatrace Intelligence (Preview)** from Dynatrace Hub.

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Dynatrace Intelligence (Preview)**.
2. Select **Dynatrace Intelligence (Preview)** and select **Install**.

After installation, Dynatrace Intelligence actions appear automatically in the **Chose action** section of [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").

## Example use case

This use case shows how you can leverage the Dynatrace Intelligence predictive AI analyzer to foresee future disk capacity needs and raise predictive alerts weeks before critical incidents occur.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

Grant necessary permissions](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#permissions "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

Explore capacity measurements](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#explore "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

Define a trigger schedule](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#schedule "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

Configure the forecast](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#forecast "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

Evaluate the result](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#evaluate "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

Remediate before it happens](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#remediate "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")[![Step 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Step 7")

Review raised problems](/docs/dynatrace-intelligence/use-cases/davis-for-workflows#problems "Automate predictive maintenance of cloud resources with Dynatrace Intelligence within AutomationEngine.")

### Step 1 Grant necessary permissions

A successful Dynatrace Intelligence analysis requires proper access rights.

1. In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, go to **Settings** > **Authorization settings**.
2. Grant the following primary permission.

   ```
   app-engine:functions:run
   ```
3. Grant the following secondary permissions.

   ```
   davis:analyzers:read



   davis:analyzers:execute



   storage:bizevents:read



   storage:buckets:read



   storage:events:read



   storage:logs:read



   storage:metrics:read



   storage:spans:read



   storage:system:read
   ```
4. In the top right, select **Save**.

### Step 2 Explore capacity measurements in a notebook

Predictive capacity management starts within [**Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") where you need to configure your capacity indicators. The image below shows an example of the free disk percentage indicator for an operations team.

![An example of an AI data analysis forecast.](https://dt-cdn.net/images/notebooks-data-analyzer-forecast-1891-28bee08431.png)

Once you have the required indicators, it's time to build the workflow that triggers a forecast at regular intervals.

### Step 3 Define a trigger schedule

In ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**, configure the required schedule to trigger the forecast. To learn how, see [Workflow schedule trigger](/docs/analyze-explore-automate/workflows/trigger/schedules "Guide to creating workflow automation schedule triggers in Dynatrace Workflows."). The image below shows the workflow that runs at 8:00 AM to trigger the forecast of all the disks that are likely to run out of space in the next week.

![Example of a Dynatrace Intelligence trigger in the Workflows app.](https://dt-cdn.net/images/workflows-forecast-trigger-1920-652d16e024.png)

### Step 4 Configure the forecast

To trigger the forecast from a workflow, you need the **Analyze data** action. The action uses the forecast analysis and a data set for the forecast. You can use any time series data for the forecast. All you need is to fetch it from Grail via a DQL query. Here, we define a set of disks for which we want to predict capacity. We use the `dt.host.disk.free` metric, but you can use any capacity metricâhost CPU, memory, network load. You can even extract the value from a log line.

Our forecast is trained on a relative timeframe of the last seven days, specified in the DQL query. It predicts 100 data points; that is, the original 120 points fetched from Grail are expanded by predicted 100 data points, spanning approximately one week into the future. See the DQL query below.

The action returns all the forecasted time series, which could be hundreds or thousands of individual disk predictions.

To configure this forecast in the action

1. Add a new **Analyze data** action.
2. Set the name of the action as `predict_disk_capacity`.
3. Select the **Generic Forecast Analysis** as an analyzer.
4. In **Time series data**, specify the following DQL query:

   ```
   timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}, bins: 120, from:now()-7d, to:now()
   ```
5. Set **Data points to predict** as `100`.

![Dynatrace Intelligence forecast for workflows in the Workflows app.](https://dt-cdn.net/images/dynatrace-intelligence-forecast-for-workflows-1920-de2e97e37b.png)

### Step 5 Evaluate the result

The next workflow action tests each prediction to determine whether the disk will run out of space during the next week. It's a **Run JavaScript** action, running the custom TypeScript code, checking threshold violations, and passing all violations to the next action. It returns a custom object with a boolean flag (`violation`) and an array containing violation details (`violations`).

1. Add a new **Run JavaScript** action.
2. Set the name of the action as `check_prediction`.
3. Use the following source code.

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';



   const THRESHOLD = 15;



   const TASK_ID = 'predict_disk_capacity';



   export default async function ({ executionId }) {



   const exe = await execution(executionId);



   const predResult = await exe.result(TASK_ID);



   const result = predResult['result'];



   const predictionSummary = { violation: false, violations: new Array<Record<string, string>>() };



   console.log("Total number of predicted lines: " + result.output.length);



   // Check if prediction was successful.



   if (result && result.executionStatus == 'COMPLETED') {



   console.log('Prediction was successful.')



   // Check each predicted result, if it violates the threshold.



   for (let i = 0; i < result.output.length; i++) {



   const prediction = result.output[i];



   // Check if the prediction result is considered valid



   if (prediction.analysisStatus == 'OK' && prediction.forecastQualityAssessment == 'VALID') {



   const lowerPredictions = prediction.timeSeriesDataWithPredictions.records[0]['dt.davis.forecast:lower'];



   const lastValue = lowerPredictions[lowerPredictions.length-1];



   // check against the threshold



   if (lastValue < THRESHOLD) {



   predictionSummary.violation = true;



   // we need to remember all metric properties in the result,



   // to inform the next actions which disk ran out of space



   predictionSummary.violations.push(prediction.timeSeriesDataWithPredictions.records[0]);



   }



   }



   }



   console.log(predictionSummary.violations.length == 0 ? 'No violations found :)' : '' + predictionSummary.violations.length + ' capacity shortages were found!')



   return predictionSummary;



   } else {



   console.log('Prediction run failed!');



   }



   }
   ```

### Step 6 Remediate before it happens

You have a variety of remediation actions to follow up on predicted capacity shortages. In our example, the workflow raises a Davis problem and sends a Slack message for each potential shortage. Both are conditional actions that only trigger if the forecast predicts any disk space shortages.

Each raised Davis problem carries custom properties that provide insight into the situation and help to identify the problematic disk.

![An example of a Dynatrace Intelligence conditional action.](https://dt-cdn.net/images/workflows-forecast-conditional-action-1920-8dbefdfc44.png)

To send a message

1. Add a new **Send message** action.
2. Set the name of the action as `send_message`.
3. Configure the message. To learn how, see [Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces").
4. Open the **Conditions** tab.
5. Select the `success` condition for the **check\_prediction** action.
6. Add the following custom condition:

   ```
   {{ result('check_prediction').violation }}
   ```

To raise a Davis problem

1. Add a new **Run JavaScript** action.
2. Set the name of the action as `raise_violation_events`.
3. Use the following source code.

   ```
   import { eventsClient, EventIngestEventType } from "@dynatrace-sdk/client-classic-environment-v2";



   import { execution } from '@dynatrace-sdk/automation-utils';



   export default async function ({ executionId }) {



   const exe = await execution(executionId);



   const checkResult = await exe.result('check_prediction');



   const violations = await checkResult.violations;



   // Raise an event for each violation



   violations.forEach(function (violation) {



   eventsClient.createEvent({



   body : {



   eventType: EventIngestEventType.ResourceContentionEvent,



   title: 'Predicted Disk Capacity Alarm',



   entitySelector: 'type(DISK),entityId("' + violation['dt.entity.disk'] + '")',



   properties: {



   'dt.entity.host' : violation['dt.entity.host']



   }



   }



   });



   });



   };
   ```
4. Open the **Conditions** tab.
5. Select the `success` condition for the **check\_prediction** action.
6. Add the following custom condition.

   ```
   {{ result('check_prediction').violation }}
   ```

### Step 7 Review all Dynatrace Intelligence predicted capacity problems

In Dynatrace, the operations team can review all predicted capacity shortages in the Dynatrace Intelligence problems feed.

Raising a problem is an optional remediation step that you can skip completely, opting for notifications for responsible teams. In this example it illustrates the flexibility and power of the AutomationEngine combined with the analytical capabilities of Dynatrace Intelligence and Grail.

![An example of Dynatrace Intelligence Capacity Prediction and Predictive Alerts.](https://dt-cdn.net/images/problems-predictive-capacity-alert-3600-89a8dfa6a9.png)

## Related topics

* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")