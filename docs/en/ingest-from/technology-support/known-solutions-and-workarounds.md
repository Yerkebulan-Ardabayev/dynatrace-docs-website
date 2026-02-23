---
title: Known solutions and workarounds
source: https://www.dynatrace.com/docs/ingest-from/technology-support/known-solutions-and-workarounds
scraped: 2026-02-23T21:23:18.600898
---

# Known solutions and workarounds

# Known solutions and workarounds

* Latest Dynatrace
* 14-min read
* Updated on Feb 26, 2024

This page details a number of resolved issues and solutions to issues that have been reported to the Dynatrace Support team.

## OneAgent prevents startup of Elasticsearch 8.18+

**Issue:**

OneAgent prevents startup of Elasticsearch 8.18+

**Solution:**

For more information, kindly visit [this pageï»¿](https://community.dynatrace.com/t5/Heads-up-from-Dynatrace/OneAgent-prevents-startup-of-Elasticsearch-8-18/ta-p/278744)

## OneAgent on a SAP HANA host

**Issue:**

OneAgent installed on a HANA host may interfere with database updates if it has automatic process injection enabled (default).

**Solution:**

Disable process auto-injection for a OneAgent installed on a SAP HANA host.

### Disable auto-injection at installation time

To install OneAgent with the parameters to enable Infrastructure Monitoring mode and disable process injection, run the command below:

```
/bin/sh Dynatrace-OneAgent-Linux-<version>.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
```

### Disable auto-injection after OneAgent installation

To disable auto-injection after OneAgent is installed

1. Open a terminal on your HANA host.
2. Run the `oneagentctl` command-line tool with the following parameters to enable Infrastructure Monitoring mode and disable process injection. The command will also restart the OneAgent service to automatically apply your changes.

```
./oneagentctl --set-monitoring-mode=infra-only --set-auto-injection-enabled=false --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

#### Dynatrace web UI

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find your HANA host and select it.
3. Select **More** (**â¦**) > **Settings** > **Monitoring**.
4. Turn off **Full-stack monitoring** and **Auto-injection**.

## Alpine Linux/musl-libc, Memory allocation

**Issue:**

On musl-libc-based Alpine Linux systems, each executable has its memory limits which are controlled via the `MPROTECT` parameter. When monitoring an musl-libc-based Alpine Linux application with Dynatrace OneAgent, your process (for example, a Java process) may exceed the specified memory limit. When this is the case, the subsequent memory allocation will fail with a message like `There is insufficient memory for the Java Runtime Environment to continue.`

**Solution:**

To overcome such issues, it's recommended that you ignore the memory protection parameter for executables that you plan to monitor with Dynatrace OneAgent. To do this, you must install the paxctl tool using:

`apk add paxctl`

You can then remove the memory check, for example

`paxctl -m /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

For 3rd-party executables not shipped by Alpine, you'll be notified that

`<file> does not have a PT_PAX_FLAGS program`

In such instances, convert your file beforehand, for example

`paxctl -C /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

## Alpine Linux/musl-libc, GNU C Library (glibc) compatibility packages

**Issue:**

Binaries built against GNU C Library (glibc) running on Alpine based Linux systems via **gcompat (GNU C Library compatibility layer for musl)** package or **libc6-compat (compatibility libraries for glibc)** package are not supported.

**Solution:**

Please migrate your build pipeline to natively compile and package against the Alpine based Linux.

## PHP running in Apache on Windows, Stack size

**Issue:**

The default stack size of Apache on Windows is 1 MB, which is rather low compared to other platforms. Therefore, the additional memory footprint involved in enabling Dynatrace monitoring for PHP can lead to stack overflows.

**Solution:**

This problem can be solved by changing the stack size to 8 MB, which is the default on Linux.

```
<IfModule mpm_winnt_module>



ThreadStackSize 8388608



</IfModule>
```

## Cloud Foundry, IBM WebSphere Liberty buildpack

**Issue:**

The recommended version of IBM WebSphere Liberty buildpack changed from `v3.7-20170118-2046` to `v3.9-20170419-1403` due to known issues related to a limitation of the JVM command line to 512 characters and an issue with trailing slashes.

**Solution:**  
Please use IBM WebSphere Liberty buildpack version v3.9-20170419-1403+

## Host, Ubuntu 16.10

**Issue:**

Due to compile optimization changes in the C runtime packages provided with Ubuntu 16.10, new stack-alignment requirements have been introduced. OneAgent versions earlier than 1.103.237 don't yet fulfill these requirements. Using versions of OneAgent earlier than 1.103.237 may lead to process crashes during dynamic symbol resolution (`dlsym`) calls in the C runtime.

**Solution:**

Update to OneAgent version 1.103.237 or higher. This version of OneAgent will be available to all Dynatrace environments by October 20th, 2016. Here are the instructions for upgrading OneAgent:

1. Go to **Settings** > **Preferences** (only visible to environment admins).
2. Ensure that the **Automatically update OneAgent instances** setting is enabled. OneAgent version 1.103.237 will be automatically deployed once itâs available on your environment.
   If **Automatically update One Agent instances** is disabled, select **OneAgent version 1.103.237 or higher** and click **Update now**.

## Java, IBM J9

**Issue:**

In rare situations, when implementing a try-catch-finally block and catching a multi-type exception with Java 7, the exception is caught, but the source code in the finally block doesn't execute. This issue has been fixed since IBM J9.

**Solution:**

Fixed since IBM J9

* 7 R1 SR2 FP11 (7.1.3.0)
* 7 SR9 (7.0.9.0)
* 8 SR1 (8.0.1.0)

**Source:**

* [IBM 1IV68110ï»¿](https://www-01.ibm.com/support/docview.wss?uid=swg1IV68110)

## Java, WebSphere MQ , JMS

**Issue:**

When using WebSphere MQ via JMS, Dynatrace isn't always able to determine the queue name and may report the queue name as 'unavailable'. This happens when MQ messages have not been properly mapped to JMS.

**Solution:**

Follow the IBM documentation for [mapping JMS messages onto IBM MQ messagesï»¿](https://www.ibm.com/support/knowledgecenter/SSFKSJ_8.0.0/com.ibm.mq.dev.doc/q031990_.htm). Once the `MQRFH2` header has been properly mapped, Dynatrace will pick up the correct queue name.

## Java, Oracle HotSpot/OpenJDK

**Issue:**

A known issue in Oracle HotSpot and OpenJDK can lead to a JVM deadlock in `ThreadTimesClosure` or incomplete CPU timings of background activities. Be sure to update to Oracle HotSpot 6u38/7u40 or OpenJDK 7u45 and higher to benefit from this solution.

**Solution:**

Fixed in Oracle HotSpot 6u38/7u40 and OpenJDK 7u45

**Source:**

* [Source Oracle HotSpot 6 (bug 7196045))ï»¿](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=7196045)
* [Source Oracle HotSpot 7 (bug 8005479)ï»¿](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=8005479)
* [Source OpenJDK (JDK-7196045)ï»¿](https://bugs.openjdk.java.net/browse/JDK-7196045)

**Issue:**

A known issue in Oracle HotSpot and OpenJDK can lead to a JVM crash when a JVMTI agent is loaded, [class data sharingï»¿](https://docs.oracle.com/en/java/javase/11/vm/class-data-sharing.html#GUID-7EAA3411-8CF0-4D19-BD05-DF5E1780AA91) is turned on, and the `classes.jsa` file exists. This is not normally the case, but it does occur in Docker environments, especially with Java 11 where class data sharing is set to `auto`.

**Solution:**

Change the java command line to turn off class data sharing via -Xshare:off.

**Source:**

* [Source OpenJDK (JDK-8212200)ï»¿](https://bugs.openjdk.java.net/browse/JDK-8212200)

## Java, Spring, AspectJ

**Issue:**

Some customers have reported the following `NullPointerException` during startup of their Java Spring or AspectJ applications. AspectJ has resolved this issue in version 1.6+. Ensure that the classpath is updated to use AspectJ 1.6+.

Message: `NullPointerException at`

```
`org.aspectj.weaver.reflect.Java15AnnotationFindergetAnnotations



(Java15AnnotationFinder.java:109)`
```

**Solution:**

Fixed since Spring 2.5.4/AspectJ 1.6

**Source:**

* [SPR-4390ï»¿](https://jira.spring.io/browse/SPR-4390)

## Java/Real User Monitoring/Apigee

**Issue:**

Real User Monitoring of Java applications may trigger a `ClassCastException` error upon a type cast to the implemented `HttpServletRequest` interface because Dynatrace replaces the original `HttpServletRequest` implementation with a `RequestWrapper` for automatic RUM JavaScript injection.

This crash also occurs for customers using [Apigeeï»¿](https://apigee.com).

**Solution:**

You have a few options:

1. Change your source code so that it doesn't expect a specific implementation of the `HttpServletRequest` interface.
2. If you're using a 3rd party framework, you can reach out to your framework vendor.
3. For Apigee, we've disabled Real User Monitoring auto-injection. Manual Real User Monitoring injection isn't affected and can be used as a workaround.
4. You can use a web server in front of Javaâthe web server will auto-inject the Real User Monitoring JavaScript and thereby avoid the crash.

**Source:**  
n/a

## Java CPU overhead

**Issue:**

Periodically, spikes of CPU usage or overall CPU usage occur when instrumenting Preview for JBoss. Querying JMX measures cause these spikes. JMX calls done in 10 sec intervals lead to a CPU spike on certain versions affected by this JBoss bug. Versions 6.4.x are considered to be problematic.

**Solution:**

Solution is to upgrade to Preview for JBoss and/or contact RedHat.

**Source:**

* [Bug 1367784ï»¿](https://bugzilla.redhat.com/show_bug.cgi?id=1367784)

## UI/Docker

**Issue:**

With Docker versions 1.10.3 - 1.11, CPU, memory, and network container statistics are missing from the UI because data requests sent to containers via `docker stats` time out. Restarting Docker addresses this issue temporarily.

**Solution:**

Fixed since Docker 1.12. Upgrade to Docker 1.12.

**Source:**

* [Issue 22655ï»¿](https://github.com/docker/docker/issues/22655)

## UI/IIS

**Issue:**

Due to a lack of Windows Performance Counters, the **Further details** tab may be not visible in the UI for IIS processes, even following IIS restart. No errors are raised during OneAgent injection.

**Solution:**

This can occur if there is a problem with the Performance Counter Library in the Windows Registry. To check this:

Using a Windows command, verify that the metrics are not retrievable from the Windows Registry:
typeperf `"\Process(w3wp*)\ID Process" -sc 15`
Alternatively, use `Perfmon.exe` to see if data is available for the counters or to confirm that the counters don't exist.

Consult Microsoft technical documentation to rebuild the performance libraries in the registry.

**Source:**

* [KB 00956ï»¿](https://support.microsoft.com/en-us/kb/300956)

## .NET, IIS

**Issue:**

If IIS monitoring is enabled for an ASP.NET application using .NET >= 4.5 and < 4.6, in rare circumstances the application could fail with an unhandled `NullReferenceException`.

Message: `System.NullReferenceException at`

```
`System.Web.Security.Roles.IsUserInRole(String username, String roleName)`
```

**Solution:**

Fixed since .NET 4.6.

* [Sourceï»¿](https://connect.microsoft.com/VisualStudio/feedbackdetail/view/967133/roles-getrolesforuser-throw-a-nullreferenceexception-in-a-wcf-service-which-is-hosted-in-asp-net-with-the-aspnetcompatibilityenabled-define-to-false)

## .NET, Cassette

**Issue:**

Customers reported a crash when using the Cassette web asset management library.

Message: Crash at

```
`[TinyIoCResolutionException: Unable to resolve type: Cassette.Views.BundlesDocumentationer]`
```

**Solution:**

As a workaround, you can use the file system as Cassette's cache by specifying a directory in your `web.config` file as follows:

```
`<cassette cacheDirectory="App_Data\Cassette" />`
```

Potentially fixed in v2.4.1

**Source:**

* [Pull 441ï»¿](https://github.com/andrewdavey/cassette/pull/441)

## .NET, ConfuserEx

**Issue:**

Using the assembly-obfuscation tool ConfuserEx can sometimes crash .NET applications because the ConfuserEx assembly doesn't allow "profilers" like Dynatrace.

Message: Crash at

```
`System.Environment.FailFast(System.String)`
```

**Solution:**

Disable ConfuserEx obfuscation or disable Dynatrace monitoring at the process level.

**Source:**

* [Sourceï»¿](https://github.com/yck1509/ConfuserEx/blob/816172adcb1ea2a6c74a964274373987fc2e9fe5/Confuser.Runtime/AntiDebug.Antinet.cs)

## Real User Monitoring, Chrome

**Issue:**

Real User Monitoring analysis with Google Chrome can lead to browser crashes when some resources can't be loaded.

Message: Crash at

```
`window.performance.getEntriesByType('resource')`
```

**Solution:**

Until Chrome provides a fix for this issue, make sure that all resources are loaded successfully (no 301 responses) or disable **W3C resource timing for third party/CDN**.

To disable W3C resource timing for third party/CDN:

1. Go to **Frontend**.
2. Select the application you want to edit.
3. Click the **More** (**â¦**) button.
4. Click **Edit**.
5. Click **Content capture**.
6. Set the **W3C resource timing for third party/CDN** switch to **Off**.

**Source:**

* [Issue 586443ï»¿](https://bugs.chromium.org/p/chromium/issues/detail?id=586443)

## Agentless Real User Monitoring, Chrome

**Issue:**

Users may see a browser warning in Chrome's Developer Console if they are on slow connections such as 2G networks.

Message:
`A Parser-blocking, cross-origin script, https://js-cdn.dynatrace.com/jstag/148709fdc4b/ruxitagent_2fgjqrx_10111170210093847.js, is invoked via document.write. This may be blocked by the browser if the device has poor network connectivity. See https://www.chromestatus.com/feature/5718547946799104 for more details.`

**Solution:**

1. Go to **Frontend**.
2. Select the application you want to configure.
3. Click the **Browse (â¦)** button and select **Edit**.
4. In the **Setup** section, select **Agentless monitoring setup**.
5. Disable the **Easy monitoring** switch.

The only downside of this change is that every time you make a configuration change you have to copy and re-inject the Real User Monitoring JavaScript again. Therefore, it's better to use the REST API to get the updated tag.

**Source:**

* [Update 2016/08ï»¿](https://developers.google.com/web/updates/2016/08/removing-document-write)

## Real User Monitoring, jQuery

**Issue:**

In the course of Real User Monitoring, failing asynchronous JQuery user actions lead to action timeouts after 180 seconds, but no error is reported. This is caused by a known jQuery limitation.

**Solution:**

JQuery has not provided a fix for this problem. To resolve this issue, fix the failing jQuery call on your end (for example, an AJAX request to a missing resource) or disable jQuery in XHR (Ajax) detection settings and enable basic XHR detection.

To disable JQuery detection and enable basic XHR detection:

1. Go to **Frontend**.
2. Select the application you want to edit.
3. Click the **More** (**â¦**) button.
4. Click **Edit**.
5. Click **XHR (Ajax)** detection.
6. Set the **JQuery, Backbone.js** switch to **Off**.
7. Set the **Basic XHR detection** switch to **On**.

**Source:**

* [Ticket 9613ï»¿](https://bugs.jquery.com/ticket/9613)

## Real User Monitoring, Ext JS

**Issue:**

In large, complex Ext JS applications customers experienced client side response time degradation like a web browser notification about an unresponsive script. Due to the internal event handling mechanism of Ext JS the application can be running slow if too many events are triggered which are captured by the RUM JavaScript.

**Solution:**

Turn off extended Ext JS event capturing in Real User Monitoring settings.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Custom configuration properties**.
5. Select **Add a custom configuration property** and enter `exteventsoff=1`.

If certain user actions are not captured afterwards, use the JavaScript API to trigger actions manually.

## Real User Monitoring, Salesforce

**Issue:**
When [injecting RUM](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") into Salesforce, you may experience the application stuck in "loading" when viewing records from a search result. When this happens, browser debugging displays the JavaScript error: `Wrong number of arguments or invalid property assignment on b.b.open,arguments,b.b`.

This occurs when the RUM JavaScript is not the first JavaScript loaded on the page. There can be JavaScript code loading in the heading that has a negative impact on the RUM JavaScript.

**Solution:**
Shifting the RUM JavaScript to load before any JavaScript resolves this issue.

**Issue:**
Dynatrace RUM isn't working for Salesforce applications based on the [Lightning Component Frameworkï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm).

The reason for this is that many Salesforce applications and offerings are based on [Lightning Component Frameworkï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm). This framework has a security architecture called [Lightning Lockerï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/security_code.htm), which restricts access to DOM elements and therefore influences the Dynatrace RUM JavaScript. Whenever the Locker code is loaded and executed before the Dynatrace RUM JavaScript, monitoring won't work, independently of whether you add the [RUM JavaScript](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications").

**Solution:**
There is currently no solution from the Dynatrace side. Please contact Salesforce support. Perhaps there is a way to allow the Dynatrace RUM JavaScript.

## Real User Monitoring, Salesforce Commerce

**Issue:**

There is currently an incompatibility between Dynatrace Agentless RUM and Salesforce Commerce. This is due to a reserved character within the Salesforce compiler.

**Solution:**

Replace `#` with `${'#'}` in the Dynatrace RUM JavaScript.

## Real User Monitoring, Visually complete, Internet Explorer 11

**Issue:**

Enabling the [**Visually complete**](/docs/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.") application setting while using Dynatrace with Internet Explorer 11 can lead to a complete page crash or hanging in cases where heavy `<table>` or table-like (using the style attribute `display:table`) DOM mutations occur. This tends to be more common with single-page applications. Simply monitoring mutations with the MutationObserver, as is done for Visually complete, can crash the page once it's loaded. Here is a [simple reproduction of the issueï»¿](https://jsfiddle.net/gd88q1n3/2/) with a table-like element mutation crash.

#### More information on Visually complete and Speed index

Speed index and Visually complete metrics are only available on browsers that support [`mutationobservers`ï»¿](https://developers.google.com/web/updates/2012/02/Detect-DOM-changes-with-Mutation-Observers). This includes the following browsers:

* Microsoft Internet Explorer 11
* Microsoft Edge 15 or later
* Firefox 57 or later
* Google Chrome 61 or later

Speed index is available only for load actions. Visually complete is available for all actions, including load actions, but not for AJAX requests that don't affect the DOM.

**Solution:**

Microsoft fixed the bulk of this issue for `<table>` element mutations in a [recent updateï»¿](https://support.microsoft.com/en-za/help/4025252/cumulative-security-update-for-internet-explorer-july-11-2017). Update Internet Explorer 11 to this version to fix this issue in most cases.

Elements with the style attribute `display:table` still run into this problem following update of Internet Explorer 11. For this reason, we've created a feature flag you can use to disable Visually complete within Internet Explorer 11 only. To enable this feature flag, Please contact a Dynatrace product expert via live chat within your environment..

## Redhat Enterprise Linux 7.4

**Issue:**

RHEL v7.4 (upgraded from v7.3 or fresh install) comes with the stix-fonts package. When this package is installed, the default font changes from `Utopia` to `STIX`. As a result, Java default fonts are mapped to `STIX`, including the `sans-serif` font family. However, the `STIX` fonts don't seem to be compatible with Java (OpenJDK + IBM JDK) and cause exceptions and bad calculated artefacts when using `java.awt`, which is the case with `JasperReports`.

For Dynatrace Managed, which is based on Java, this issue was experienced as a problem in Smartscape. More specifically, selecting any item in Smartscape shows an unspecific error message that something went wrong.

**Solution:**

Create a file `/etc/fonts/local.conf` with the content shown below to explicitly make `Utopia` the default font again.

```
<?xml version='1.0'?>



<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>



<fontconfig>



<alias>



<family>serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>sans-serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>monospace</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialog</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialoginput</family>



<prefer><family>Utopia</family></prefer>



</alias>



</fontconfig>
```

**Source:**

* [Bug 1484079ï»¿](https://bugzilla.redhat.com/show_bug.cgi?id=1484079#c8)

## IBM HTTP Server (IHS) 8.5

**Issue:**

IHS 8.5 on Linux crashes with segmentation fault.

**Solution:**

Disable prelink on IHS server.

**Source:**

* [Sourceï»¿](https://www.google.at/search?q=prelink+crash)

## Adobe Dispatcher

**Issue:**

When using Adobe Dispatcher with a web server monitored by Dynatrace OneAgent, the RUM JavaScript agent tag is injected twice into the HTML page. As a consequence, the RUM JavaScript agent will be executed twice at the browser, producing unnecessary load (e.g. the beacons will be sent twice, etc.).

The reason for this is that Adobe Dispatcher doesn't cache HTTP response headers by default and so the header X-OneAgent-JS-Injection "gets lost" for already injected sites, which are served from the cache. If this header is not present, the webserver agent injects (another) RUM JavaScript agent tag, even if it's already present in the cached content.

**Solution:**

The dispatcher needs to be configured to cache the response header "X-OneAgent-JS-Injection". To avoid double injection of the RUM JavaScript agent tag when using Adobe Dispatcher with a web server monitored by Dynatrace OneAgent, add "X-OneAgent-JS-Injection" to the `/cache/headers` section of the Adobe Dispatcher configuration:

```
/cache



{



# Cache configuration



# <existing configuration>



# ...



/headers



{



"X-OneAgent-JS-Injection"



}



}
```