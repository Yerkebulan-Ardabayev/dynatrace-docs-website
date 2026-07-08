---
title: Define custom services
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services
---

# Define custom services

# Define custom services

* How-to guide
* 9-min read
* Updated on Sep 17, 2025

A custom service is a service that has a manually defined entry point, such as a method, class, or interface. You can define custom services for Java, .NET, Go, and PHP. Each custom service may contain multiple entry points.

Methods of a specific class or implementations of an interface can serve as entry points for your custom service. Each non-recursive call to such a method represents a single request to your custom service.

If your application services aren't built on standard technologies, they may not be recognized out-of-the box. You can monitor these technologies, but you need to define them as custom services with specific service entry points.

You can also use custom services for microservices that are used by a larger application and aren't exposed via communication technologies.

Dynatrace allows you to define any method, class, or interface as the entry point of a service to be monitored. The method being instrumented, though, must return before the whole process is shutdown. If the method is never exited, no data is reported.

Dissociated transactions

If transactions aren't connected, creating a custom service **will not** help to stitch them. A custom service will create a new entry point.

## Method delegation

OneAgent understands the concept of method delegation and only records the first call in a delegation chain. For example, if you have several methods that are calling each other, you can safely mark all these methods as entry points—instances where one method directly calls the other are recorded as single requests.

### Delegation suppression

OneAgent suppresses method delegation **per service**. That is, any calls between two methods of one service are not recorded. If you need to capture such calls you must create a separate custom service for it.

## Java, .NET, and Go services

Java method instrumentation

In Java, the entry method must terminate before the process shuts down. If the entry method—for example, `main()` or `execute()` that start a process—only ends with process termination, OneAgent can't finalize and send the data.

For Java, .NET, and Go you can use search to select the entry point and methods or you can specify them manually. To create a new custom Java, .NET, or Go service:

Find the entry point

Manually specify the entry point

1. Go to **Settings** > **Service detection** > **Custom service detection**.
2. Do one of the following:

   * Java Select the **Java services** tab and select **Define Java services**.
   * .NET Select the **.NET services** tab and select **Define .NET services**.
   * Go Select the **Go services** tab and select **Define Go services**.
3. Give your service a meaningful name.
4. Select **Find entry point**.
5. Find and select the process group that contains your entry point.
6. Select the process that contains your entry point and select **Continue**.
7. Find the class you want to instrument. Type in the name or part of the name to search for it.
8. Select the required class and select **Continue**.
9. Define how you want to instrument the class. You have two options:

   * **Use the selected class** for instrumenting methods of the selected class only.
   * Java .NET **Use an implemented interface or superclass** for instrumenting methods in any interface or super class in the class hierarchy. In such cases, select **Load inheritance** to load all available superclasses and interfaces, then select the one you need.
10. Select the methods you want to instrument and then select **Finish**.  
    The **Define custom service** page displays the newly added entry point and methods.
11. If needed, add more entry points.
12. If needed, restrict the new custom service to certain process groups. See the [**Restrict a custom service to specific process groups**](#restrict) section below.
13. Review the entry point and methods to be instrumented.
14. In the lower-right corner of the page, select **Save**.

1. Go to **Settings** > **Service detection** > **Custom service detection**.
2. Do one of the following:

   * Java Select the **Java services** tab and select **Define Java services**.
   * .NET Select the **.NET services** tab and select **Define .NET services**.
   * Go Select the **Go services** tab and select **Define Go services**.
3. Give your service a meaningful name.
4. Select **Define entry point manually**.
5. In the **Fully qualified class** field, type the name of the class that contains the methods you want to instrument.
6. Specify the methods to be instrumented in one of two ways:

   * Type the full method name manually.
   * Look for methods in the class, and select them:

     1. Select **Search for methods**.
     2. Select the process group that contains your entry point.
     3. Select methods you want to instrument and then select **Finish**.
7. If needed, add more methods.
8. If needed, add more entry points.
9. Review the entry point and methods to be instrumented.
10. If needed, restrict the new custom service to certain process groups. See the [**Restrict a custom service to process groups**](#restrict) section below.
11. In the lower-right corner of the page, select **Save**.

Unsupported scenario

Note that some scenarios do not work in Dynatrace, like the Queue/Worker scenario. Anything that is put into a `java.util.Queue` and is handled by another worker thread, cannot be seen in the Pure Path. See [Oracle java.util Interface Queue﻿](https://dt-url.net/xy03uja).

## PHP services

For PHP you can use search to select the entry point and methods or you can specify them manually. To create a new custom PHP service:

Find the entry point

Manually specify the entry point

1. Go to **Settings** > **Process and contextualize** > **Services** > **Custom service detection**.
2. Select the **PHP services** tab and select **Define PHP service**.
3. Give your service a meaningful name.
4. Select **Find entry point**.
5. Find and select the process group that contains your entry point.
6. Select the process that contains your entry point and then select **Continue**.
7. Find the class you want to instrument. Type in the name or part of the name to search for it.
8. Select the required class and then select **Continue**.
9. Select the methods you want to instrument and then select **Finish**.  
   The **Define custom service** page displays the newly added entry point and methods.
10. If needed, add more entry points.
11. If needed, restrict the new custom service to certain process groups. See the [**Restrict a custom service to specific process groups**](#restrict) section below.
12. Review the entry point and methods to be instrumented.
13. In the lower-right corner of the page, select **Save**.

1. Go to **Settings** > **Process and contextualize** > **Services** > **Custom service detection**.
2. Select the **PHP services** tab and then select **Define PHP service**.
3. Give your service a meaningful name.
4. Select **Define entry point manually**.
5. In the **File name** field, type the full path to the PHP file that contains the methods you want to instrument.
6. In the **Fully qualified class name** field, type the name of the class that contains the methods you want to instrument.
7. In the **Methods** field, type the name of the method you want to instrument.
8. If needed, select **Add method manually** and specify more methods for instrumentation.
9. If needed, restrict the new custom service to specific process groups. See the [**Restrict a custom service to specific process groups**](#restrict) section below.
10. Once all methods have been added, select **Save** in the upper-right corner of the page.

### Example: Define a custom PHP service through a file

The following example shows how to define a custom service based on a `.php` file. It also shows how the resulting custom service detection is presented in the **Distributed Traces**.

```
<?php



class InternalExample {



public function say($what) {



echo $what;



}



}



class Example {



public $internalExample;



public function __construct() {



$this->internalExample = new InternalExample();



}



public function run() {



$this->internalExample->say("Hello world!\n");



}



}



$example = new Example();



$example->run();
```

In the above script, the class object `Example` creates and calls the object of the class `InternalExample` to print `Hello world!`. In this example, we want to trace the `Hello world!` printing and the `Example` class creation.

Now, we'll use our `index.php` file to define a custom service by following the steps in the [Manually specify the entry point](#manual-php-service) section above. Within the file, we can instrument specific functions as follows:

* We can instrument the `say` function from the `InternalExample` class:

  ![Instrument the say function](https://dt-cdn.net/images/php-custom-service-example-1-1091-b7b92d31ae.png)

  Instrument the say function
* We can instrument the `run` function from the `Example` class. Additionally, we'll instrument the `__construct` function of the `Example` class to show its creation in the trace.

  ![Instrument the construct function](https://dt-cdn.net/images/php-custom-service-example-2-1087-65aa6d790c.png)

  Instrument the construct function

In both examples, in the **File name** field, we use the **Match** option to use the local path to find the `index.php` file. Using local paths in custom service definitions is helpful because some PHP frameworks modify the script execution directory. When declaring class and method names, case sensitivity is essential, but you don't need to list method parameters.

You can see the resulting pure paths in the **Distributed Traces**, both combined in one trace:

![See several traces from one PHP file combined into one view](https://dt-cdn.net/images/distributed-traces-1395-e9a66831e8.png)

See several traces from one PHP file combined into one view

## Define a custom Go service via API

To define a custom Go service via API

1. Prepare the HTTP request

1. Determine the scope (`className`)—the package or type the method is defined in.

   In the following examples, the scope is `main.(*CronJob)` because the function is defined as a method of the `CronJob` type in the `main` package.
2. Determine the fully qualified method name (`methodName`)—the method name, prefixed with the scope.

In the example request body below, the fully qualified method name is `main.(*CronJob).Run`. The example contains all the required parameters. To use it, adjust the values according to your request.

```
{



"name": "Cron Job Service",



"enabled": true,



"rules": [



{



"enabled": true,



"className": "main.(*CronJob)",



"methodRules": [



{



"methodName": "main.(*CronJob).Run",



"returnType": ""



}



]



}



],



"queueEntryPoint": false



}
```

2. Send a POST request to your endpoint

* Use `go` as the technology.
* Use your access token or personal access token for authentication.

```
curl --request POST 'https://{your-environment-id}.live.dynatrace.com/api/config/v1/service/customServices/go' \



--header 'Authorization: Api-Token dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM' \



--header 'Content-Type: application/json' \



--data '{



"name": "Cron Job Service",



"enabled": true,



"rules": [



{



"enabled": true,



"className": "main.(*CronJob)",



"methodRules": [



{



"methodName": "main.(*CronJob).Run",



"returnType": ""



}



]



}



],



"queueEntryPoint": false



}'
```

The `id` of the newly created custom service is returned upon success; a descriptive error message is returned in case of failure. With this `id`, you can edit the custom service via API.

```
{



"id": "114ff497-be8a-44c7-a990-35bb4267b677",



"name": "Cron Job Service"



}
```

## Closures in Go

Closures are anonymous functions to which the Go compiler assigns special names.

The generated closure names defined in a scope are numbered in order of their appearance: `func1`, `func2`, and so on. For instance, the closure in the `main` function gets the `func1` label:

```
package main



func main() {



go func() {



// ...



}()



}
```

## Priority of custom services

If you have several custom services defined, the evaluation goes from top to bottom, applying the first matching rule. If for some reason you have the same class and method defined in several custom services, make sure to prioritize the services accordingly.

## x-dynatrace header

For HTTP requests, Dynatrace uses an additional HTTP header called `x-dynatrace` for transaction stitching. This header is set by OneAgent between web servers to link them with each other. PurePath® technology for distributed tracing relies heavily on such headers, which is why it’s important to ensure that network components, such as firewalls and routers, are never configured to remove these headers. Incorrect configuration of network components can potentially lead to broken pure paths. Also, some of the network components completely disable such requests (and deliver HTTP 403 error) as the additional header may be considered as unsafe. In such cases, it is necessary to configure these components to accept the `x-dynatrace` header.

## Edit a custom service

You can edit any custom service at any time. For changes to take effect, you need to restart the affected processes, unless the real-time updates are activated for Java and PHP. For .NET, you must restart the process.

To edit a custom service, select the service's **Edit** button in the list of services.

You can activate/deactivate existing entry points, add/delete entry points, add/delete methods in entry points.

You can also restrict the custom service to certain process groups. See the [**Restrict a custom service to specific process groups**](#restrict) section below.

### Real-time updates

Updates to Java and PHP custom services can be applied in near real time, without process restarts. To activate this feature, go to **Settings** > **Server-side service detection** > **Deep monitoring** > **Real-time updates to Java and PHP services** and enable the dedicated switches.

With this feature, you add monitoring capabilities for services and request attributes during existing application Garbage Collection halts, instead of only during process startup. This can increase Garbage Collection halts and slowdowns. We recommend limited usage in timing-sensitive environments as Dynatrace doesn't control Garbage Collection halts provided and implemented by virtual machines.

## Restrict a custom service to specific process groups

You can restrict usage of any custom service to certain process groups. Custom services rules will apply in specified process groups only and will be ignored in other process groups. You can restrict a custom service during creation or edit it later.

To restrict a custom service:

1. On the **Define custom service** or **Edit service** page, expand **Optionally restrict custom service rules by process groups**.
2. Select **Add process group**.
3. Select the process group where you want to apply the custom service.
4. Select **Add**.
5. In the lower-right corner of the **Define custom service** or **Edit service** page, select **Save**.

## Related topics

* [Custom services API](/managed/dynatrace-api/configuration-api/service-api/custom-services-api "Learn what the Dynatrace custom services config API offers.")
* [Custom API definitions](/managed/observe/application-observability/services/customize-api-definitions "Set detection rules to customize APIs in your environment.")