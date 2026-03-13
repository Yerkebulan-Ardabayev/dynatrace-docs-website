---
title: Add and access validation insight links
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/validation-insight-link
scraped: 2026-03-05T21:34:43.909572
---

# Add and access validation insight links

# Add and access validation insight links

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Feb 17, 2026

Add validation insight links to provide contextual information and resources for an objective.
Using validation insight links, you can go directly to dashboards, notebooks, or external tools such as SonarQube.

## How to add and access validation insight links

To add a validation insight link:

1. Go to your guardian.
2. Select your objective.
3. On the right-hand side, select  **Add link**.
4. Enter the dashboard, notebook, or SonarQube URL in the **Enter or paste the link** field.

These validation insight links are visible as **Validation insights** for the objective.

* You can add up to five links per objective.
* Links must be valid HTTPS URLs.
* Display text for each link is optional.

Access validation insight links from ![Site Reliability Guardian](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Site Reliability Guardian") **Site Reliability Guardian**:

1. Go to your guardian.
2. Select  **Analyze**.
3. Go to the **Validation result** section.
   The links are under **Validation insights** for the objective.

   ![Validation Insights on Analysis Page](https://dt-cdn.net/images/validation-insights-links-1340-a2f8e028f8.png)

Access validation insight links using DQL:

* For [Lifecycle guardians](../site-reliability-guardian.md#lifecycle-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision."), you can find the validation insights for the event type `validation.objective` in the property `dt.srg.objective`.

  Here is an example query for Lifecycle guardian:

  ```
  fetch events



  | filter event.kind == "SDLC_EVENT"



  | filter event.type == "validation.objective"



  | filter event.provider == "dynatrace.site.reliability.guardian"



  | fields dt.srg.objective
  ```
* For [Business guardians](../site-reliability-guardian.md#business-guardian "Automatically validate the performance, availability, and capacity objectives of your critical services to make the right release decision."), you can find the objective links for the event type `guardian.validation.objective` in the property `guardian.objective`.

  Here is an example query for Business guardian:

  ```
  fetch bizevents



  | filter event.provider == "dynatrace.site.reliability.guardian"



  | filter event.type == "guardian.validation.objective"



  | fields guardian.objective
  ```

## Next steps

Take a look at [Guardian execution context](execution-context.md "Filter Site Reliability Guardian validation events triggered by an external tool using the context information provided by the tool."). Use events from your Continuous Integration (CI) tool to send them to Dynatrace, which, in turn, can trigger validation of your guardian in a workflow.