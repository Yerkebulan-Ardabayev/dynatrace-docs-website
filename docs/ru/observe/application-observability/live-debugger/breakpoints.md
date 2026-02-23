---
title: Live Debugger breakpoints
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/breakpoints
scraped: 2026-02-23T21:37:10.713090
---

# Live Debugger breakpoints

# Live Debugger breakpoints

* Latest Dynatrace
* Explanation
* 8-min read
* Published May 07, 2024

Dynatrace **non-breaking breakpoints** allow the OneAgent deployed in your application to fetch data from any place in your code, allowing you to observe the current state of your application and quickly find bugs in production without stopping your application.

## Add breakpoints

To add a breakpoint in ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger**, select the gutter by the required code line number.

## Breakpoint status

Once you set a non-breaking breakpoint, it has a status associated with it (**Active**, **Pending**, **Disabled**, **Error**, or **Warning**). To view more information about the status, right-click the breakpoint and select **Status**.

For more information, you can select the Breakpoint status indicator or read more about it on this page.

Expand any of the following for a summary of a breakpoint status.

Active

`Active` status occurs when one of or more of your applications has applied the breakpoint and no errors have been reported.
In most cases, once the breakpoint has transitioned to active, you will see snapshots collected the next time the line is executed.
If you don't see any snapshots arriving, this may be due to any of the following reasons:

* **Incorrect Application**  
  You aren't invoking the correct line of code in the correct application instance.
* **Long Running Function**  
  You have placed a breakpoint on a long-running function. In this runtime, breakpoints are only applied for function calls performed after the breakpoint was created.

Pending

`Pending` status indicates that the breakpoint has not been applied to any of your applications. This could mean one of the following:

* **No Application instances**  
  The breakpoint couldn't be applied because no application instance matches the current filter. This could mean one of the following:

  + OneAgent has not been installed.
  + OneAgent has been installed, but the application can't connect to the Dynatrace service.
  + The application can connect to the Dynatrace service, but it is excluded by the current filter definition.
  + The application is currently not running and will be running in the future.
* **Wrong Source File**  
  The source file you used to set the breakpoint isn't loaded in any of the applications in the current filter.
* **No Code**  
  You have set the breakpoint on a line that has no executable code associated with it.
* **(JVM) No Debug Information**  
  You have compiled your classes without debug information. Select here for more information.
* **(Node) No Source Maps**  
  You are using a transpiled application without including source maps. Try using a minimal transpilation level, or make sure to add source maps to your deployed application. Check out the source code section for more information.
* **(Node) Code is in a Dependency**  
  You are debugging a package deployed as a dependency. This requires setting up your source repository accordingly.
* **(Node) Different File Layout**  
  File paths are changed between source repository and deployment. This requires setting up your source repository accordingly.

Disabled

`Disabled` status occurs when the breakpoint was disabled due to limits. These include limits applied by the user for that specific breakpoint (for example, time limit, hit limit).

* For more information on the reason why the breakpoint was disabled, right-click the breakpoint and select **Status**.
* To re-enable the breakpoint (by resetting the limit counter), right-click the breakpoint and select **Enable**.

Error

`Error` status occurs when one of or more of your applications has reported an error in processing, applying, or executing the breakpoint.

`Error` messages are documented within ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or IDE, but examples include:

* **Source file has changed**  
  Dynatrace verifies that the source file you see in our IDE is the file you are deploying in your application. If the file version is wrong, the breakpoint will not be set. If you use source commit detection, you will see the correct git commit to use on the app instances page.
* **Breakpoint collection took too long**  
  Dynatrace employs a safeguard in case a single breakpoint takes too long to collect data from your application.
* **(Node) Running with a Debugger**  
  You are using ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** side-by-side with another debugger such as WebStorm Debugger.

Warning

`Warning` indicates some problems have occurred with the breakpoint, and Dynatrace is trying its best to deliver the data you've requested.

`Warning` messages are documented within ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or IDE, but examples include:

* **Breakpoint collection is sampled due to rate-limiting**  
  Dynatrace employs a built-in rate-limiting mechanism to prevent breakpoints set in hot code paths from impacting application performance. This error indicates that the rate limit has been hit and the breakpoint has been rate-limited for the offending application instance. Collection is sampled to prevent performance impact on your application.
* **(JVM) Source file not found**  
  Dynatrace relies on source file hashing to ensure you are debugging the correct version of the files you are trying to debug. In most JVM based languages, include your source within your Jar/War/Ear archives.

## Data collection

The next time the code on which you set the breakpoint is invoked, Dynatrace will collect parts of the application state and send it to ![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** or the IDE.

## Collection levels

There are several collection levels that you can set to a breakpoint. The collection levels set three different values:

* **Collection depth**: how deep to go in the collection.
* **String width**: how many characters to collect from a string.
* **Collection width**: how many elements to collect from vectors, arrays, lists, etc.

Three collection levels are available:

Level\Language

JVM

Node.js

Low

Collection depth: 2

String width: 128

Collection width: 10

Collection depth: 2

String width: 128

Collection width: 5

Medium

Collection depth: 5

String width: 512

Collection width: 15

Collection depth: 3

String width: 512

Collection width: 10

High

Collection depth: 8

String width: 4096

Collection width: 25

Collection depth: 5

String width: 4096

Collection width: 20

For example, if an object has a deeply nested field, we will stop when we reach the maximum collection depth (as in the following example). Note that `l5` has more fields, but they werenât collected because they were too deep.

![Example of an object with deeply nested fields](https://dt-cdn.net/images/2025-01-30-22-13-44-1200-5eed210010-640-cfbd29135d.jpg)

## Breakpoint limits

You can set limits on individual breakpoints to limit the amount of data that will be collected. When limits are reached, the breakpoint will be automatically disabled. Once disabled, it will not collect additional data. To re-enable a breakpoint, right-click it and select **Enable**.

The limits can be set based on:

* Time (for example, 1 Hour, 24 hours, a week)
* Hit count (the number of times the breakpoint is triggered)

Breakpoint default limit values:

* Breakpoint time limit: 7 days
* Breakpoint hit limit: 100
* Collection level: Medium

## Breakpoint conditions



Conditional breakpoints allow you to limit the data collected by OneAgent. You will only collect data when the defined expression evaluates as true. This makes it possible to debug specific scenarios and limit the number of messages you receive.
To set a condition, right-click a breakpoint and select **Edit**.

Condition types:

* Simple conditions  
  Using a simple condition, you can compare a variable with some value (or another variable).
* Advanced conditions  
  Using an advanced condition, you can define a more complex condition using logical parameters. Use `&&` for an AND statement, `||` for an OR statement, and `(` and `)` for encapsulation.

Advanced conditions support the following operators and functions:

Operator

Example

Description

`==`

`a==1`, `b=='bbb'`, `x==y`

If the values of two operands are equal, the condition is true.

`!=`

`a!=1`, `b!='bbb'`, `x!=y`

If values of two operands are not equal, the condition is true.

`>`

`a>1`, `x>y`

If the value of the left operand is greater than the value of the right operand, the condition is true.

`>=`

`a>=1`, `x>=y`

If the value of the left operand is greater than or equal to the value of the right operand, the condition is true.

`<`

`a<1`, `x<y`

If the value of left operand is less than the value of right operand, then condition becomes true.

`<=`

`a<=1`, `x<=y`

If the value of the left operand is less than or equal to the value of the right operand, the condition is true.

`in`

`'bbb' in a`

If the value of the left operand is included in the right operand, the condition is true.

`&&`

`a<=1 && b!='bbb'`

If both operands are true, the condition is true.

`||`

`a<=1 || b=='bbb'`

If any of the two operands are non-zero, the condition is true.

`()`

``` (a<=1``||``b=='bbb') && (x<y) ```

You can use parentheses to change the precedence when evaluating the condition.

`[]`

`arr[4]!=4`, `dict['a']!=4`

Set conditions regarding to a specific sequenceâs element - list, dict, etc.

`size`

`arr.size() >= 32`

Use size instead of len or length on any platform.