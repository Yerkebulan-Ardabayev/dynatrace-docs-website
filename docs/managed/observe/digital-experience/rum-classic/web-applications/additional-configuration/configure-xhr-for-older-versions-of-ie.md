---
title: Configure XHR for older versions of Internet Explorer in RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie
---

# Configure XHR for older versions of Internet Explorer in RUM Classic

# Configure XHR for older versions of Internet Explorer in RUM Classic

* How-to guide
* 2-min read
* Updated on Apr 03, 2024

The Dynatrace RUM JavaScript leverages *property listeners* to find out the exact moment a framework is completely initialized (for details regarding property listeners, please visit the [Mozilla website﻿](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)). This technique allows Dynatrace to automatically instrument several functions provided by the framework, which is needed for capturing and correlating web requests and user actions. However, property listeners are not available in versions of Internet Explorer 8 and older. The earliest automatic initialization event would be the end of the "onload" event, where it's most likely that frameworks have finished initialization. This is satisfactory for most cases, but sometimes framework components are used during the onload event. To capture these function calls, it is necessary to manually call an initial procedure of the Dynatrace RUM JavaScript. For most frameworks, it's sufficient to add a small JavaScript snippet right after the framework's script tag. For AngularJS and Prototype, additional effort is required.

Starting with RUM JavaScript version 1.293, we [ended support for Internet Explorer 11](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

Look at the following generic example to see where and how you should add the code snippet. The placeholder value `Framework` must be replaced by the actual names of the frameworks.

**Snippet location example**

```
<head>



<meta...></meta>



<script type="text/javascript" src="/ruxitagentjs_....."></script>



<script type="text/javascript" src="Framework.js"></script>



<script type="text/javascript">window.dT_&&dT_.initFramework&&dT_.initFramework();</script>



<script>/* other scripts */</script>



</head>
```

## Ajax Detection modules requiring snippets:

### AngularJS

This framework comes bundled with jqLite, a minimal version of jQuery. It's necessary that the agent initializes right after jqLite has finished its initialization. For the debug version of AngularJS, the snippet has to be injected right before `jqLite(document).ready`. The screenshot below shows where it has to be injected in the minified AngularJS version `(angular.min.js)`.

**Angular Snippet**

`window.dT_&&dT_.initAngular&&dT_.initAngular();`

![Xhr confi 1](https://dt-cdn.net/images/xhr-confi-1-1234-051d10abfc.png)

Xhr confi 1

### Dojo

Inject snippet after `dojo.js` script tag.

**Dojo Snippet**

`window.dT_&&dT_.initDojo&&dT_.initDojo();`

### ExtJS

Inject snippet after `ext-all.js` script tag.

**ExtJS Snippet**

`window.dT_&&dT_.dtInitExtJS&&dT_.dtInitExtJS();`

### jQuery

Inject snippet after `jquery.js` script tag.

**jQuery Snippet**

`window.dT_&&dT_.initJQuery&&dT_.initJQuery();`

### MooTools

Inject snippet after `mootools.core.js` script tag.

**MooTools Snippet**

`window.dT_&&dT_.initMooTools&&dT_.initMooTools();`

### Prototype

Inject snippet before the `Ajax.Updater` call in the `prototype.js` file. See the screenshot for the location in the prototype file.

**Prototype Snippet**

`window.dT_&&dT_.initPrototype&&dT_.initPrototype();`

![Xhr confi 2](https://dt-cdn.net/images/xhr-confi-2-676-9d1abd0f10.png)

Xhr confi 2