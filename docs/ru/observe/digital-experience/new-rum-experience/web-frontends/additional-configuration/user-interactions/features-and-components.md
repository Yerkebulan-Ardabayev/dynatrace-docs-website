---
title: Associate user interactions with features and UI components
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions/features-and-components
scraped: 2026-03-05T21:30:50.126179
---

# Associate user interactions with features and UI components

# Associate user interactions with features and UI components

* Latest Dynatrace
* How-to guide
* Updated on Mar 03, 2026

Early Access

The New RUM Experience allows you to associate user interactions with features and UI components by adding dedicated attributes to your HTML. This comprehensive interaction context facilitates powerful queries and deeper analysis of how users engage with your application's UI and functionality.

## Associate user interactions with features

Use the `data-dt-features` attribute to associate user interactions on an HTML element with one or more specific product features. On user interactions, the captured features are available in the field `ui_element.features`; see [User interactions](/docs/semantic-dictionary/model/rum/user-events/user-interactions). Elements inherit features from their ancestors, providing comprehensive feature tracking.

### Use cases

The `data-dt-features` attribute lets you:

* Track user interactions by featureâfor example, "search", "checkout", "navigation".
* Group related UI components across the page.
* Analyze user behavior by feature area.
* Create feature-based dashboards and reports.

### Format

The value of the `data-dt-features` attribute is a comma-separated list of feature names, where a feature can be any string. Features are case-sensitiveâfor example, "Search" and "search" are different features.

Examples

```
<!-- Single feature -->



<div data-dt-features="search">



<input type="text" placeholder="Search...">



<button>Search</button>



</div>



<!-- Multiple features -->



<nav data-dt-features="navigation,sidebar">



<a href="/home">Home</a>



<a href="/products">Products</a>



<a href="/about">About</a>



</nav>
```

### Feature inheritance

Feature inheritance works by collecting feature values from all ancestor elements in a top-down order. All inherited features are combined into a single array, and any duplicates are removed while keeping the first occurrence. The final list reflects the DOM hierarchy, starting with the most distant ancestor element and ending with the element itself.

Examples

```
<div data-dt-features="shop,product-catalog">



<div data-dt-features="filters">



<button>Price</button>          <!-- ui_element.features: ["shop", "product-catalog", "filters"] -->



<button>Brand</button>          <!-- ui_element.features: ["shop", "product-catalog", "filters"] -->



</div>



<div data-dt-features="results">



<div>Product 1</div>            <!-- ui_element.features: ["shop", "product-catalog", "results"] -->



<div>Product 2</div>            <!-- ui_element.features: ["shop", "product-catalog", "results"] -->



</div>



</div>



<div data-dt-features="app,main">



<div data-dt-features="sidebar,navigation">



<div data-dt-features="menu,navigation">



<button>Click</button>  <!-- ui_element.features: ["app", "main", "sidebar", "navigation", "menu"] -->



</div>



</div>



</div>
```

### DQL example

The following DQL query generates a timeseries that shows, for each feature, the number of sessions that include at least one interaction with that feature.

```
fetch user.events



| filter isNotNull(ui_element.features)



| expand ui_element.features



| makeTimeseries countDistinct(dt.rum.session.id), by: {ui_element.features}, interval: 1d
```

## Associate user interactions with UI components

Use the `data-dt-component` attribute to associate user interactions on an HTML element with one or more UI components, such as a date picker or a calendar. Component values are inherited from all ancestor elements and collected in topâdown order, forming a path through the component tree. On the captured user interaction, the collected components are available in the field `ui_element.components`; see [User interactions](/docs/semantic-dictionary/model/rum/user-events/user-interactions).

### Use cases

The `data-dt-component` attribute lets you:

* Locate where user interactions occur within component-based UI frameworks such as React, Vue, and Angular.
* Understand the component path from the root to the interacted element.
* Distinguish between identical elements in different component contexts.
* Debug and analyze interactions in nested component structures.

### Format and inheritance

The value of `data-dt-component` is a string representing a component. Components are collected top-down from all ancestors, resulting in an array that represents the path through the component tree. Empty or whitespace-only values are ignored.

Example (React JSX)

```
<App data-dt-component="App">



<Container data-dt-component="Container">



<AuthProvider data-dt-component="AuthProvider">



<Dashboard data-dt-component="Dashboard">



<Container data-dt-component="Container">



<Card data-dt-component="Card">



<Button data-dt-component="Button">Save</Button>



{/* ui_element.components: ["App", "Container", "AuthProvider", "Dashboard", "Container", "Card", "Button"] */}



</Card>



</Container>



</Dashboard>



</AuthProvider>



</Container>



</App>
```

### DQL example

The following DQL query generates a timeseries showing how many different users interacted with the `TimeframeSelector` component. The results are split by frontend.

```
fetch user.events



| expand ui_element.components



| filter ui_element.components == "TimeframeSelector"



| makeTimeseries countDistinct(dt.rum.instance.id), by: {frontend.name}, interval: 1d
```