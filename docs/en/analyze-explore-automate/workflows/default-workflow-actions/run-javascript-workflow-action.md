---
title: Run JavaScript action for Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/default-workflow-actions/run-javascript-workflow-action
scraped: 2026-02-19T21:23:40.301718
---

# Run JavaScript action for Workflows

# Run JavaScript action for Workflows

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jun 25, 2025

The **Run JavaScript** action for Workflows enables you to build a custom task running JavaScript code in a workflow.

The Dynatrace Platform provides a [JavaScript runtimeï»¿](https://dt-url.net/mf03qa8) for custom scripts in Workflows.

Custom JavaScript tasks in workflows are provided with an `executionId`, `actionExecutionId`, and `loopItemValue` that, in conjunction with the [automation SDKsï»¿](https://dt-url.net/vq23qax), give you access to task results, workflow execution, and loop item parameters, directly as JavaScript objects without using Jinja expressions.

To use the automation SDKs, import them into the custom script task. Then, they can be initialized with the execution context.

We offer both a [client automation SDKï»¿](https://dt-url.net/j343q5k), which gives full access to the Automation API, and a convenience-focused [automation utils SDKï»¿](https://dt-url.net/0n63qgu).

Executing the Run JavaScript for Workflows action is similar to running the code in the [Function executorï»¿](https://dt-url.net/cp83qh8). You can find the results in the **Result** tab of the **Execution** that you could use in subsequent tasks.

## Run JavaScript action security

* The **Run JavaScript** action does not support [expressions](/docs/analyze-explore-automate/workflows/reference "Get to know the workflows expression") in its input to avoid the possibility of code injection.
* All HTTP calls are validated against the global allowlist.
* If you import [third-party libraries](#third-party) for your JavaScript action, the allowlisted CDN domains provide access to the entire package portfolio. Dynatrace JavaScript runtime is robust against certain attack vectors, but you might accidentally allow malicious code. Make sure to mirror dependencies that you rely on in your internal infrastructure and monitor their security implications with [Dynatrace Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") or third-party tools like Snyk.

We strictly advise against returning any secret as part of the result. Every result is accessible in the executions to anyone with read access to the workflow.

## Run JavaScript action requirements

* See [JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/) for Node and Web API compatibility of the Dynatrace JavaScript runtime.
  The JavaScript runtime times out after 120 seconds.
  Thus, any Run JavaScript action also times out after 120 seconds.
  Please remember that this timeout isn't extendable by setting a higher timeout value in task options.
* The JavaScript runtime provides up to 256 MB RAM.
* The JavaScript runtime and thus Run Javascript actions can't return a binary result. A workaround would be to serialize the payload into an object.
* The script of a Run JavaScript action size is limited to about 5 MB. Additional context information implicitly sent by the AutomationEngine on action invocation, for example, workflow and action execution identifier, also account for this limit.
* The result of Run JavaScript action is limited to 6 MB.
* There is a limit on concurrent requests to the underlying infrastructure (Function executor) that executes the JavaScript runtime. In case your Run JavaScript tasks run into such issue, you can use the task options retry functionality to mitigate the problem.

## Task result

Your JavaScript actions can retrieve the result of a previous task and use it for further processing.

### Example using the automation-utils SDK to access the result

```
// import of sdk modules



import { result } from '@dynatrace-sdk/automation-utils';



export default async function () {



// get the result of task 'my_task'. 'my_task' must be a predecessor.



var myResult = await result('my_task');



// log the result object



console.log('The whole result object: ', myResult);



console.log('only one variable: ', myResult.myVariable)



}
```

### Example using the client-automation SDK to access the result

```
// import of sdk modules



import { executionsClient } from '@dynatrace-sdk/client-automation';



export default async function ({ executionId }) {



// load the execution object using the current executionId



var config = {executionId, id: 'my_task'}



var myResult = await executionsClient.getTaskExecutionResult(config)



// log the result object



console.log('My task result: ', myResult)



console.log('only one variable: ', myResult.myVariable)



}
```

## Available execution context

The following execution context is available out of the box and can be accessed for any use case that demand for it.

```
export default async function ({ executionId, actionExecutionId }) {



//log available execution context ids



console.log('Workflow execution id: ', executionId);



console.log('Action execution id: ', actionExecutionId)



}
```

For loop item context, please see the [Task loop](#task-loop) section below.
Various workflow context information is also available in the Dynatrace JavaScript Runtime itself.

## Task loop

When using the option to loop a task, you might want to access the value of the current loop item. You can use the `loopItemValue` parameter to access the value of the item for the current iteration.

### Example using `loopItemValue`

```
export default async function ({ loopItemValue }) {



// log the current value of the loop item



console.log(loopItemValue)



}
```

## AutomationEngine context information

The `@dynatrace-sdk/automation-utils` package available to run JavaScript tasks provides access to the following information:

* `workflowId` - the executed workflow's ID.
* `executionId` - the ID of the related workflow execution.
* `actionExecutionId` - the ID of the current action execution.
* `taskName` - the task's name in the workflow execution to which the action execution is related.

```
// optional import of sdk modules



import { actionExecutionId, executionId, taskName, workflowId } from '@dynatrace-sdk/automation-utils';



export default async function () {



console.log(`Running action execution '${actionExecutionId}' for task '${taskName}' of workflow '${workflowId}' in workflow execution '${executionId}'`)



}
```

## Import third-party libraries

If you need a certain functionality in your JavaScript action that is provided by third-party libraries, you can load the library via a URL import.

Restrictions apply:

* The JavaScript modules need to be valid [ECMAScript modulesï»¿](https://tc39.es/ecma262/#sec-modules)
* They run within the [context of the Dynatrace JavaScript runtimeï»¿](https://developer.dynatracelabs.com/reference/javascript-runtime/), and its respective compatibility.
* Only modules from allowlisted URLs can be loaded. You need to add them to the **External requests**.

  External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

  1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
  2. Select  **New host pattern**.
  3. Add the domain names.
  4. Select **Add**.

  This way you can granularly control the web services your functions can connect to.
* Imports may not exceed 6MB in size (combined).

### Example - use XMLJSON library to parse XML input

Let's say your backend produces legacy XML output, but you need to process data as JSON. In such a case, you can let the generic XML2JSON Library to parse the content rather than writing your own code do it.

1. Add the XMLJSON library URL to allowed **External requests**.

   External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

   1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
   2. Select  **New host pattern**.
   3. Add the domain names.
   4. Select **Add**.

   This way you can granularly control the web services your functions can connect to.
2. Add a snippet like below to your JavaScript action to parse the XML, convert it to JSON and use as input for your action.

```
// Load the XML parser from ESM



import xml2js from "https://esm.sh/xml2js@0.6.2";



export default async function() {



// Dummy XML, can be fetched from your back-end



const xml = "<root><list><item>Hello</item><item>World</item></list></root>";



const parser = new xml2js.Parser();



const json = await parser.parseStringPromise(xml);



return json;



}
```

Package CDNs like [esm.shï»¿](https://esm.sh), [unpkgï»¿](https://unpkg.com/), [JSRï»¿](https://jsr.io/), [JSDELIVERï»¿](https://www.jsdelivr.com/), or [Denoï»¿](https://deno.com/) offer compatible packages.

Note that some of those libraries either depend on Node.js internals or Deno internals, which the Dynatrace JavaScript runtime does not provide. See [JavaScript runtimeï»¿](https://developer.dynatrace.com/reference/javascript-runtime/) for Node and Web API compatibility of the Dynatrace JavaScript runtime.

## Intentionally fail task

If you need to fail a run JavaScript task by intention, you throw an unhandled exception.

Here is an example that will always fail the execution of the task.

```
export default async function() {



throw new Error()



}
```

## Access event trigger payload

For workflows triggered by an event, you might want to access the event payload for the business logic you want to implement.

Here is an example to retrieve event context from the workflow execution for event triggered workflows

```
import { execution } from '@dynatrace-sdk/automation-utils';



export default async function ({ executionId }) {



const ex = await execution(executionId);



console.log( ex.params.event);



// your code goes here



}
```