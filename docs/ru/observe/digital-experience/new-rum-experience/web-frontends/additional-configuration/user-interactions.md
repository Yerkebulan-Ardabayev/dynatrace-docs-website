---
title: Configure user interaction capturing for web frontends
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions
scraped: 2026-02-28T21:29:57.464130
---

# Configure user interaction capturing for web frontends

# Configure user interaction capturing for web frontends

* Latest Dynatrace
* How-to guide
* Updated on Feb 26, 2026

Early Access

The New RUM Experience allows you to capture [user interactions](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-interactions "Get familiar with the data model at the heart of the New RUM Experience.") such as clicks and scrolls and turn them into actionable insights:

* You can view all user interactions that occurred during a user session using the [![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions") **Users & Sessions**](/docs/observe/digital-experience/new-rum-experience/users-and-sessions#events "The Users & Sessions app delivers insight into individual user journeys and behavior patterns.") app. This is especially useful for customer support teams and developers when diagnosing customer issues or bugs.
* User interaction analysis via DQL allows you to understand behavioral patterns across a wide range of use cases; see [DQL examples](/docs/observe/digital-experience/new-rum-experience/use-cases/dql-examples#behavioral-insights "Analyze and explore RUM data in depth by leveraging DQL.").

During the User Interaction Early Access, there are no additional charges for ingesting user interactions. Querying user interactions is also included at no extra cost, because raw DEM data queries are currently in Early Access; see [Calculate your consumption of Digital Experience Monitoring (DEM) - Query](/docs/license/capabilities/digital-experience-monitoring-query-retain/queries-dem "Learn how your consumption of the DEM-related DQL queries is consumed and billed before and after Early Access.").

## Activate capturing of user interactions

To capture user interactions

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. Switch to the **Settings** tab.
5. Under **Enablement and cost control**, turn on **User Interactions** .

## Types of user interactions

The following table provides an overview of the available types of user interactions. For a detailed specification, see [User interaction](/docs/semantic-dictionary/model/rum/user-events/user-interactions) in the Semantic Dictionary.

## Opt-in user interaction types

Most user interaction types are captured automatically once you have [activated user interaction capturing](#activate-capturing). Some interaction types, however, require an explicit opt-in by adding dedicated attributes to the corresponding HTML elements. These attributes enable event capture but don't affect the element's behavior.

### Focus/Blur

To capture focus and blur user interactions, add the attributes `data-dt-focus` and `data-dt-blur` to the corresponding HTML elements. The attribute can be empty or assigned a value; both `data-dt-focus` and `data-dt-focus="true"` are valid.

Examples

```
<!-- Track when users focus on search -->



<input data-dt-focus type="text" placeholder="Search products...">



<!-- Monitor form field interaction -->



<form>



<input data-dt-focus name="email" type="email" placeholder="Email">



<input data-dt-focus name="password" type="password" placeholder="Password">



<button type="submit">Login</button>



</form>



<!-- Track focus on custom components -->



<div data-dt-focus tabindex="0" role="button">Custom Button</div>



<!-- Track both focus and blur for complete interaction -->



<textarea data-dt-focus data-dt-blur placeholder="Your feedback..."></textarea>



<!-- Monitor search abandonment -->



<input data-dt-focus data-dt-blur type="search" placeholder="What are you looking for?">
```

### Mouseover

To capture mouseover user interactions, add the attribute `data-dt-mouse-over="<milliseconds>"` to the corresponding HTML element. The attribute's value specifies how many milliseconds the user must hover over the element before the interaction is captured. When choosing an appropriate delay, consider the following factors:

* If you want to measure engagement with CTAs (call-to-action elements) or product cards, how many milliseconds should the user hover before the mouseover is considered intentional?
* If your goal is to track tooltip interactions, what delay does your application use before tooltips appear?

Examples

```
<!-- Track hover after 300ms (shows intent) -->



<button data-dt-mouse-over="300">



Learn More



</button>



<!-- Monitor product card interest with 500ms threshold -->



<div class="product-card" data-dt-mouse-over="500">



<img src="product.jpg">



<h3>Premium Headphones</h3>



<p>$299.99</p>



</div>



<!-- Track tooltip hover with 1 second threshold -->



<span data-dt-mouse-over="1000">



<i class="info-icon">?</i>



<div class="tooltip">Detailed information appears here</div>



</span>



<!-- Possible different thresholds for different intents -->



<nav>



<div data-dt-mouse-over="200">Products</div>      <!-- Quick hover -->



<div data-dt-mouse-over="500">Solutions</div>     <!-- Medium intent -->



<div data-dt-mouse-over="1000">Documentation</div> <!-- Strong intent -->



</nav>
```

## Customization

For additional context, you can add attributes to your HTML that associate the captured user interactions with features and UI components; see [Associate user interactions with features and UI components](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions/features-and-components "Learn how to associate user interactions for web frontends with features and UI components."). This customization facilitates powerful queries and deeper analysis of how users engage with your application's UI and functionality.