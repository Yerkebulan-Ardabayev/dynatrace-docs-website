---
title: Configure additional settings for Live Debugging
source: https://www.dynatrace.com/docs/observe/application-observability/live-debugger/additional-settings
scraped: 2026-02-19T21:22:21.267410
---

# Configure additional settings for Live Debugging

# Configure additional settings for Live Debugging

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Feb 19, 2026

## Manage Opt-in/Opt-out

Grants permission to control opt-in/opt-out code monitoring for the entire environment or by scope.

**Example policy**:

```
ALLOW settings:objects:read, settings:objects:write, settings:schemas:read WHERE settings:schemaId = "builtin:devobs.agent.optin";
```

## Manage breakpoints

Grants permission to manage Live Debugging breakpoints.

**Example policy**:

Allow managing breakpoints across the environment:

```
ALLOW dev-obs:breakpoints:manage;
```

## OneAgent setup

### Node

#### Transpiled code

If your application's code is being transpiled or bundled, you need to include the source maps, either in-line or as separate files.

* Webpack  
  Use either the `inline-source-map` or `source-map` values for the `devtool` option in the Webpack config file.
* Babel  
  Use either the `inline`, `both` or `true` values for the `sourceMaps` option in the Babel config file.
* TypeScript  
  Set either `inlineSourceMap` or `sourceMap` fields to `true` as well as `inlineSources` to `true` in the TypeScript config file.
* CoffeeScript  
  Pass either the `-M` (inline) or `-m` flags to the coffee CLI tool.
* Webpack + TypeScript  
  Add `sourceMap` as well as `inlineSources` to `true` (setting `inlineSourceMap` isnât enough in this case) in the TypeScript config file and use either the `inline-source-map` or `source-map` values for the `devtool` option in the Webpack config file.

#### Uglification/minification

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** works with uglified/minified code if it's provided with source maps. However, mangling (changing of variable names) should not be applied. Webpack may automatically mangle variable names when used in production.

```
const TerserPlugin = require("terser-webpack-plugin");



module.exports = {



// ...



optimization: {



minimizer: \[new TerserPlugin({



terserOptions: {



mangle: false,



},



})],



},



};
```

## Integrate with your version control

When debugging within a remote environment, you need to know exactly what source code it is executing.

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** integrates with your source control provider to fetch the correct source code for every environment.

Configure the following environment variables to enable automatic source code fetching:

* `DT_LIVEDEBUGGER_COMMIT` - String that indicates your git commit
* `DT_LIVEDEBUGGER_REMOTE_ORIGIN` - String that indicates your git remote origin

For multiple sources, use the environment variable `DT_LIVEDEBUGGER_SOURCES` to initialize the SDK with information about the sources used in your application.

`DT_LIVEDEBUGGER_SOURCES` is a semicolon-separated list of source control repository and revision information, joined by `#`. For example: `DT_LIVEDEBUGGER_SOURCES=https://github.com/myorg/MyRepo#abc123;https://github.com/otherorg/OtherRepo#xyz789`.

In JVM languages, you can also specify a path to JAR, which must contain the following attributes in its JAR manifest:

* `DT-LiveDebugger-Repository`
* `DT-LiveDebugger-Revision`

Then you can have a combination of URLs and paths to JARs.

Example: `DT_LIVEDEBUGGER_SOURCES=https://github.com/myorg/MyRepo#abc123;/path/to/lib.jar`.

## Apply data masking rules

![Live Debugger](https://dt-cdn.net/images/live-debugger-256-b934a2bad5.png "Live Debugger") **Live Debugger** offers data masking rules to let you control sensitive data, giving you the ability to specify which data it should not collect and display to users.

You can set the data masking rules through the Live Debugger settings page.

1. Go to **Settings** > **Observability for Developers** > **Sensitive data masking**.
2. Configure data masking by adding rules with a set of matchers that identify your sensitive data.
3. Select **Add rule** to start configuring your rule.
4. Set **Name** to the name to display for your configuration.
5. Select the rule type:

   * **Redact by variable name**  
     When masking by variable name, the entire value of any variable matching that name will be redacted. You can specify how the variable name should match:

     **Equals**: Match variables with names that are exactly the same as the input string (for example, `foo` matches only `foo`).
     **Contains**: Match variables with names that include the input string (for example, `foo` matches `myfoobar` or `foo123`).
     **Starts with**: Match variables with names that begin with the input string (for example, `foo` matches `foobar` or `foo123`).
     **Ends with**: Match variables with names that end with the input string (for example, `foo` matches `myfoo` or `barfoo`).
   * **Redact by regex**  
     When masking by regular expression, all variable values matches to that expression will be redacted.
     For example, adding a rule regarding the variable value `\[0-9]+` will replace `nameAndPassword:LordHelmet-12345` with `nameAndPassword:LordHelmet-\*\*\*\*`.

Defined rules can be reordered, and they are executed in the order in which they appear on the **Sensitive data masking** page.

The redacted data is replaced, by default, with the string `\*\*\*`.

You can choose a custom string for the rule, or replace it with an SHA-256 hash. For example, adding a rule for the variable name `secretKey` with a custom replacement of `REDACTED` replaces the output `secretKey:12345` with `secretKey:REDACTED`.