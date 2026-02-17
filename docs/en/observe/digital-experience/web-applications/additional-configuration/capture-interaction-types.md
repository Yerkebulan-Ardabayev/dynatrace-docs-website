---
title: Capture additional interaction types for web applications
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/capture-interaction-types
scraped: 2026-02-17T05:08:48.911615
---

# Capture additional interaction types for web applications

# Capture additional interaction types for web applications

* How-to guide
* 2-min read
* Updated on Mar 20, 2023

For [XHR actions](/docs/observe/digital-experience/rum-concepts/user-actions#xhr-action "Learn what user actions are and how they help you understand what users do with your application."), Real User Monitoring detects the following interaction types:

* Click
* Double click
* Mouse down
* Mouse up
* Scroll

* Key down
* Key up
* Touch start
* Touch end
* Change

To select which interaction types Dynatrace should capture automatically

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Advanced setup**.
5. Scroll down to the **Wrappers for addEventListener and attachEvent** section, and use the toggles to include or exclude the interaction types from being captured. Some of the options are available for both **Global event capture** and `addEventListener`/`attachEvent` modes.

   Difference between Global event capture and addEventListener / attachEvent options

   The **Global event capture** option registers a single listener on the document object of the page to capture fired events.

   The `addEventListener`/`attachEvent` module walks through the DOM nodes and registers listeners directly on the specific elements. Instead of registering a single global listener on the document object (in case of the **Global event capture** option), this module adds listeners on all buttons, input elements, and other UI elements. This increases overhead because all DOM nodes must be scanned.

   You might need to use the `addEventListener`/`attachEvent` module in the following cases:

   * When your setup stops the propagation of events
   * When the JavaScript setup framework prevents adding a listener on the document element itself
   * In case of another unique security setup

   ![Wrappers for addEventListener and attachEvent](https://dt-cdn.net/images/global-event-capture-1031-01ba0aaab3.png)

## Related topics

* [User actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")