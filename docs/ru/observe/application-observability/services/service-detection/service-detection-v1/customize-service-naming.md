---
title: Service naming rules
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming
scraped: 2026-02-26T21:18:28.692575
---

# Service naming rules

# Service naming rules

* How-to guide
* 4-min read
* Published Oct 04, 2017

Dynatrace [automatically detects and names your applicationsâ server-side services](/docs/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.") based on basic properties of your application deployment and configuration. Built-in rules define these names. These properties and the resulting service names should be intuitive to you because they reflect your service landscape. Still, you might want to customize these names. Custom service naming rules enable you to enhance automated service naming.

## Built-in rules

Built-in service naming rules define how the service naming works out of the box. Built-in rules are not configurable. You can still access them for documentation purposes. Go to **Settings** > **Server-side service monitoring** > **Service naming rules** and scroll to the **Built-in rules** section. Here you can expand every rule to see how is it configured.

## Custom rules

Custom service naming rules override built-in rules enabling you to create your own naming standards. To access custom rules, go to **Settings** > **Server-side service monitoring** > **Service naming rules**.

Custom rules are evaluated from top to bottom, and the first matching rule applies, so be sure to place your rule in the correct position on the list.

To define a custom service naming rule

1. Go to **Settings** > **Server-side service monitoring** > **Service naming rules**.
2. Select the **Add a new rule**.
3. Type a **Rule name**.
4. Define the **Service name format**, including any static text string to be included that describes the named service. You can use placeholders to make it easy to dynamically include specific service and process group properties in the automated service name.
5. Optional Consider restricting this naming rule to a specific process group, technology, or service type.  
   While this step is optional, it provides a quick means of reducing the number of services that a rule applies to. To reduce the list of applicable services even further, you can add **Conditions** to the new rule.

   If within the name format you reference a property that doesnât exist in a service that the rule applies to, the placeholder will be replaced with an empty string. You can ensure that the rule only applies to services where the property exists by adding an `exists` condition for the desired property.
6. Select **Save**.

## Service name format

Service name format enable you to build complex naming standards for the services in your environment. You can use placeholders to build a name based on service properties. Placeholders will be replaced with actual values in the service name. In case the provided value is missing, the placeholder will resolve to an empty string. Place your cursor in the **Service name format** input field to see the list of available placeholders.

You can use [regular expressions](/docs/manage/tags-and-metadata/reference/regular-expressions-in-dynatrace "Learn how to use regular expressions in the context of Dynatrace.") to extract portions of the service name, created by a built-in rule. Add the regex before the closing curly bracket `}` of the placeholder. For example, for `{ProcessGroup:DetectedName}` use `{ProcessGroup:DetectedName/REGEX}`.

## Related topics

* [Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")