---
title: Capture event and session properties for mobile frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/mobile-frontends/additional-configuration/event-and-session-properties
scraped: 2026-02-26T21:29:41.591618
---

# Capture event and session properties for mobile frontends

# Capture event and session properties for mobile frontends

* Latest Dynatrace
* How-to guide
* Updated on Jan 22, 2026

Event and session properties let you attach custom-defined key-value pairs to user events and user sessions, using the namespaces [`event_properties`](/docs/semantic-dictionary/model/rum/user-events#event-properties "User events provide deep visibility and insights into experience, behavior, performance, and errors of your customers and end-users in real-time.") and [`session_properties`](/docs/semantic-dictionary/model/rum/user-sessions#user-session-properties "User sessions provide a summary of the user events from the same customer or end-user of your application during a limited period of time.").

## Before you start sending event or session properties

Event and session properties must be configured before they can be used. Incoming event and session properties that are not configured are dropped during event ingest.

To define a new property

1. In ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**, select the frontend for which you want to add the property.
2. Select the **Settings** tab, then choose **Event and session properties**.
3. Select **Add** under either **Defined event properties** or **Defined session properties**, depending on the type of property you want to create.
4. In the **Field name** box, enter a name for your property (for example, `cart.total_value`).
5. Optional To make the field name case-insensitive, turn on **Field name validation should be case-insensitive**.
6. From the **Datatype** list, select the appropriate data type for your property: `string`, `boolean`, or `number`.

Dynatrace automatically prefixes your field name with `event_properties.` or `session_properties.` based on the property type you selected. For example, a field name of `cart.total_value` will become `event_properties.cart.total_value`.

## How to send properties

Event and session properties can be sent via the [New RUM APIs](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/new-rum-apis "Explore the new Real User Monitoring (RUM) APIs for mobile frontends, including startup configuration, event reporting, error handling, view tracking, and advanced features for Dynatrace on Grail."):

* To add event properties, use [`addEventModifier`](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/new-rum-apis#add-event-modifier "Explore the new Real User Monitoring (RUM) APIs for mobile frontends, including startup configuration, event reporting, error handling, view tracking, and advanced features for Dynatrace on Grail.").
* To send a session property, use [`sendSessionPropertyEvent`](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/new-rum-apis#send-session-property-event "Explore the new Real User Monitoring (RUM) APIs for mobile frontends, including startup configuration, event reporting, error handling, view tracking, and advanced features for Dynatrace on Grail.").

## Limits

* Naming

  + Field name maximum length: 100 characters (including the `event_properties.` / `session_properties.` prefix).
  + Allowed characters in field name: AâZ, aâz, 0â9, underscore `_`, and dot `.`.
  + Each dot must be followed by an alphabetic character.
  + Each underscore must be followed by an alphabetic character or number.
* Countsâa maximum of 20 event and session properties can be configured.
* Values

  + Values must be primitive types (`String`, `Int`, `Long`, `Double`, `Boolean`).
  + For event and session properties of data type `String`, the length is limited to 1,000 characters.

Valid examples:

* `event_properties.purchase_state`
* `event_properties.cart.total_value`
* `session_properties.product_tier`
* `session_properties.loyalty_status`

## Related topics

* [New RUM APIs for mobile frontends](/docs/observe/digital-experience/new-rum-experience/mobile-frontends/new-rum-apis "Explore the new Real User Monitoring (RUM) APIs for mobile frontends, including startup configuration, event reporting, error handling, view tracking, and advanced features for Dynatrace on Grail.")