---
title: Capture event and session properties for web frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/event-and-session-properties
scraped: 2026-02-24T21:31:52.137175
---

# Capture event and session properties for web frontends

# Capture event and session properties for web frontends

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

Event and session properties let you attach custom-defined key-value pairs to user events and user sessions, using the namespaces [`event_properties`](/docs/semantic-dictionary/model/rum/user-events#event-properties "User events provide deep visibility and insights into experience, behavior, performance, and errors of your customers and end-users in real-time.") and [`session_properties`](/docs/semantic-dictionary/model/rum/user-sessions#user-session-properties "User sessions provide a summary of the user events from the same customer or end-user of your application during a limited period of time.").

## Before you start sending event or session properties

Event and session properties must be configured before they can be used. Incoming event and session properties that are not configured are dropped during event ingest.

To configure an event or session property

1. In ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**, select the frontend for which you want to add the property.
2. In the **Settings** tab, select **Event and session properties**.
3. Depending on whether you want to configure an event or session property, select **Add** under either **Defined event properties** or **Defined session properties**.
4. In **Field name**, specify a name, for example `cart.total_value`.
5. If you want field name validation to be case insensitive, turn on **Field name validation should be case-insensitive**.
6. Under **Datatype**, select one of the available typesâeither `string`, `boolean`, or `number`.

Note that the field name is always prefixed with either `event_properties.` or `session_properties.`, depending on the selected type, for example `event_properties.cart.total_value`

## How to send properties

Event and session properties can be sent via the JavaScript API:

* To add event properties, use [`addEventModifier`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.addEventModifier.html).
* To send a session property, use [`sendSessionPropertyEvent`ï»¿](https://www.dynatrace.com/support/doc/javascriptapi/doc-latest/functions/Types.dynatrace.sendSessionPropertyEvent.html).

## Limits

* **Naming**

  + Field name maximum length: 100 characters (including the `event_properties.` / `session_properties.` prefix).
  + Allowed characters in field name: AâZ, aâz, 0â9, underscore `_`, and dot `.`.
* **Counts**

  + Maximum of 20 event and session properties can be configured.
* **Values**

  + For event and session properties of data type string, the length is limited to 1000 characters.