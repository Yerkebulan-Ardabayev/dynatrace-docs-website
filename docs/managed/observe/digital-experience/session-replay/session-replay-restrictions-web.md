---
title: Technical restrictions for Session Replay for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/session-replay-restrictions-web
scraped: 2026-05-12T11:33:33.912266
---

# Technical restrictions for Session Replay for web applications

# Technical restrictions for Session Replay for web applications

* Explanation
* 4-min read
* Updated on Feb 27, 2024

Session Replay is compatible with page-based applications, single-page applications, and applications that use IFrames. However, certain restrictions apply.

## Browser support

* [Supported browser versions for session recording](/managed/ingest-from/technology-support#supported-browsers "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Supported browser versions for Session Replay](/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements "Find out which browsers Dynatrace Managed can run on.")

## Technology restrictions

The following technologies aren't supported:

* Frames
* Canvas
* WebGL
* Web Animations API
* Plugins, such as Adobe Flash Player, Java applets, and non-HTML technologies
* Documents, such as PDF files and Word documents
* :visited, :focus and :activeCSS pseudo-classes
* Movie replay

## IFrames

IFrame and nested IFrame recording are supported. However, the following restrictions are applicable:

* Each IFrame must have the RUM JavaScript injected into it. If the RUM JavaScript has been injected only into the parent and not into the IFrames, the IFrame content and interactions won't be displayed in the replay. This is because it is not possible to look into IFrames from a parent page.
* IFrame recording works only when the page contains the RUM JavaScript. If only the IFrame that isn't the parent page has the RUM JavaScript, the replay will show it as the top frame of the recording. In this case, interactions in the parent frame (such as scroll) will not be recorded.
* The same application must monitor the parent page and the IFrame. When different applications are used for the parent page and for the IFrame, the IFrame won't be displayed properly in the replay.

## Resources

By default, Session Replay [captures and stores CSS resources](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-resource-capturing "Configure monitoring consumption and data privacy settings for Session Replay.") during the user session recording. However, Session Replay can't reproduce [blob/object URLsï»¿](https://w3c.github.io/FileAPI/#DefinitionOfScheme).

If you disable [resource capture for Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-resource-capturing "Configure monitoring consumption and data privacy settings for Session Replay."), the following restrictions apply. These restrictions also apply to images and fonts even when resource capture for Session Replay is enabled.

* Resources must be available on the browser that's used for replay. There must be a direct connection to the server that serves the resources.
* Resources can't be protected. If resources are protected, ensure that the player can access them without authentication.
* Resources can't be personalized. This applies to resources that are different for each user but are served by the same URL. However, the restriction doesn't apply to URLs that are different for each personalized resource. An example of this is avatar images that use the same URL to deliver different avatars for different users.

To overcome these restrictions, we recommend that you [enable resource capture for Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-resource-capturing "Configure monitoring consumption and data privacy settings for Session Replay.").

## Dynamic forms

If you're dynamically updating the values in your form, and they're not being displayed in your Session Replay recording, check your application code and verify how you're effecting the updateâyou might be updating the `.value` property of your form element. While we understand that this is a valid update method, it doesn't trigger any events on the page, so Dynatrace doesn't know that something has changed. As an alternative solution, we suggest updating the attribute value (in case of `<input>` elements) or the `.textContent` property (in case of `<textarea>` elements). This way, Dynatrace will be notified of the changes and will record them correctly.

## Volume

On average, a minute of session recording and replay consumes 100 kB of storage space. This is also the required amount of upstream bandwidth from the client system to the Dynatrace servers that is consumed. However, this value can't be guaranteed because it depends on the web application. Applications with very frequent DOM changes, big initial sizes, or heavy usage of IFrames can create large amounts of data.

## Data transmission and OneAgent

Ensure that you're using OneAgent version 1.193+ because it supports a high volume of beacon transmission.

High volume beacon support is available for all Real User Monitoring capable agents:

* Apache
* NGINX
* Java
* IIS
* Node.JS

## Application support

Web applications are complex. While Session Replay is built to work with any web application and includes support for IFrames and single-page applications, there might be cases in which the reproduction of user interactions isn't perfect. For this reason, Session Replay may not recreate user experiences adequately for all web applications.

Websites that modify the browser's native APIs may cause conflicts with the JavaScript agent code and prevent the page from being recorded properly.

## Environment

Session Replay must send data from client browsers to your Dynatrace Cluster. Data transmission can fail depending on the environment, available network connectivity, speed, network latency, connection problems, bandwidth, and other environment-related issues.

## Related topics

* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Enable Session Replay for web applications](/managed/observe/digital-experience/session-replay/enable-session-replay-web "Learn the prerequisites and the procedure for enabling Session Replay.")
* [Configure Session Replay for web applications](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.")