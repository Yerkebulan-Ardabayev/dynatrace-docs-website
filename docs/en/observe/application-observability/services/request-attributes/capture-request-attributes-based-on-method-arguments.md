---
title: Capture request attributes based on method arguments
source: https://www.dynatrace.com/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments
scraped: 2026-02-06T16:26:02.461517
---

# Capture request attributes based on method arguments

# Capture request attributes based on method arguments

* Latest Dynatrace
* 6-min read
* Published May 11, 2018

Dynatrace allows you to create request attributes based on method arguments.

## Create request attributes

To create a request attribute based on a method argument

1. Go to **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Select **Define a new request attribute**.
3. Provide a unique **Request attribute name**. You can rename an attribute at any point in the future.
4. Select **Add new data source**.
5. Optional Define the scope of the request attribute.
6. From the **Request attribute source** list, select **Java method parameter(s)**, **.NET method parameter(s)**, or **PHP method parameter(s)**.
7. Select the **Select method sources** button to open the class wizard. Here you can select the class of the method upon whose argument you want to set an attribute.
8. Select the process group that contains the classes or interfaces youâre interested in and select **Continue**.
9. Search for the class that includes the method youâre interested in. Begin typing the class name and select **Search** button. The list may take a few seconds to populate.
10. Select a class from the displayed list. If the list doesnât contain the class youâre looking for, refine the search string.

    ![Request attributes .NET](https://dt-cdn.net/images/request-attributes-dotnet-1-1326-b3cbc95405.png)
11. Finally, select one or more methods that you want to capture parameters from and then select **Finish**.
12. The methods you selected are listed in the method argument capture rule (see below). For each method, from the list box under **Capture**, select the argument or return value of the method you want to capture.

    ![Request attributes .NET](https://dt-cdn.net/images/request-attributes-dotnet-2-1325-6354f7c2ab.png)
13. You can always extend the list or remove methods later. Once saved, restart the processes that this rule applies to.

### Notes

* In addition to arguments and return values of any method, you can also capture the number of occurrences. You should only use a single method rule when capturing occurrences. Dynatrace will count the number of calls of this method within a single request.
* You can [capture non-primitive and non-string objects](#numerical). This can, however, result in increased performance overhead. Some objects may inadvertently change their state based on the method called, so use this option with caution.
* Core Java classes (for example, `javax.` and `java.`) or .NET classes (for example, `System.`) produce the warning **Not instrumentable**. These classes can't be used, because instrumenting them would mean instrumenting a substantial part of your environment.

## What's next?

Once your services begin calling the respective methods, you should see the request attribute appear on the distributed traces page.

![Request attributes .NET](https://dt-cdn.net/images/request-attributes-net-1801-7073b46dd3.png)

The code-level tree view also contains these methods. This view tells you what the value was on each specific methodâin case the method is called multiple times with different values.

![Request attributes .NET - code level](https://dt-cdn.net/images/request-attributes-net-code-level-1804-839768da1d.png)

## Post processing

In most cases, a captured value will contain what it is youâre looking for. However, you may not want an entire value, or even every value. With post processing you can manipulate the captured value.

Expand the **Optionally restrict or process the captured parameter(s) further** option to see the processing steps. The steps are executed in the presented orderâeach step is applied to the result of the previous step.

You don't have to apply all the steps. Each step becomes active once you provide a value for it or select the option box.

![Post processing options for defining request attribute rule](https://dt-cdn.net/images/post5steps-1353-6e753964a1.png)

Step 1 enables you to extract something from the resulting string based on delimited characters.

Step 2 can split the captured value into several values based on a delimited character.

Step 3 removes whitespaces.

Step 4 enables you to filter out captured values that don't fit the provided criterion.

Step 5 enables you to extract something from the resulting string based a [regular expression](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.").

## Numerical values and aggregations

You might want to capture an argument of a method and the method is called multiple times. Sometimes youâre only interested in a specific value. In other cases, you may only want to count the executions or average the captured values. Within other values, the argument in question may be a complex object and youâre really only interested in one aspect of the object.

To tackle such situations, you can use the **Data type** and the **Aggregation on request** options when you define or configure a request attribute.

### Aggregations

Aggregation is applied not only within a single data source (for example, a method rule) but also across multiple data sources. The order is defined by:

* Order of the data source rules
* Order of the method rules within a method data source
* Order of the method executions in your application (when a method is executed multiple times)

#### Text attributes

For text attributes, you can choose between these options:

* First occurrence
* Last occurrence
* Set of distinct values

The **Set of distinct** values option enables you to use all distinct values found in a request for filtering. For example, if a request captures a request attribute called `Product` and two values are captured for this attribute, `Book` and `Video`. You can filter by either of these values to find the request in question.

#### Numeric attributes

For numeric values, you can use the following aggregations:

* Minimum of captured values
* Maximum of captured values
* Average of captured values
* Sum of captured values
* Count occurrences
* Count distinct

If you choose one of these options, the data type changes to integer automatically. These settings are useful when youâre counting something.

## Deep object access

A value that youâre interested in may not be available as a simple argument, but rather as part of a complex argument object or even a member variable of a class youâre looking at. Such values can still be accessed. You can access not only argument values and return values, but also an object itself. Whenever an item to be captured (be it an argument or an object) is a complex object, you have the ability to define a method (chain) that enables deep access into the object. The example below uses the method `getBookingCode`. You can even execute a chain, for example, `getBookingCode().getCustomerCode()`.

![Request attributes](https://dt-cdn.net/images/deep-object-access-1157-bad06a137b.png)

The deep object access feature introduces new code into your application that must be executed. As such, it may change the state of your application or introduce performance impact. Use this feature with caution.

### Limitations

The following limitations apply to deep object access:

* You can access only one field at a time. If you're accessing a field, it must be in the beginning of the chain.
* Method parameters are not allowed.
* You must use valid Java, .NET, or PHP notation.