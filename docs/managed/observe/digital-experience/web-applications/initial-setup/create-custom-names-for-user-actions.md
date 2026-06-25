---
title: Create custom user action names for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions
scraped: 2026-05-12T11:08:49.034675
---

# Create custom user action names for web applications

# Create custom user action names for web applications

* How-to guide
* 12-min read
* Updated on Jan 27, 2023

[User action](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") names are generated automatically based on triggered load or XHR URLs and are often difficult to read and remember. When your application handles a lot of user requests and interactions per day, tracking user actions becomes difficult when you don't have the means to group them logically.

User action naming rules give you the option to generate consistent and readable user actions that can be easily grouped and tracked throughout the application.

These action naming rules can be created and customized for each application individually and then used throughout Dynatrace in:

* User experience charts
* Graphs
* Conversion goals (for example, `add-to-shopping-cart` and `newsletter-sign-up`)
* Key user actions
* Top consumer list

To easily create and maintain user action naming rules, you can make use of placeholders, input parameters, and even different rules for Load and XHR actions.

## Action name detection

Dynatrace tries to assign meaningful names for actions. To do this, it checks several action properties, such as inner HTML, caption, and hint of the HTML element that triggers the action. This element can either be a button or an anchor. It also tries to get the caption if there's a more complex HTML structure with multiple nested tags.

The RUM JavaScript uses several techniques to choose the name that best fits an action. It starts with the innermost HTML node that is clicked, such as a button, an image tag, or a link, and checks the following in the order of precedence:

1. [`data-dtname` attribute](#change-action-name-via-data-dtname)
2. `nodeName`, such as an image, anchor, or input  
   It stops when the `html` tag, `body` tag, `head` tag, or `document` element is found.
3. `innerText` or `textContent`

If none of these return a reasonable result, the RUM JavaScript starts applying a recursive algorithm that checks different things depending on `nodeName` of the currently checked HTML node. If nothing is found, the parent node is checked.

## Add and use placeholders

Placeholders allow you to add dynamic elements to custom naming rules.

Placeholders are useful in cases where you want to have dynamic input values (for example, the URLs of blog posts visited by your users) included in user action names or when you want to remove or replace certain parts of an input value (for example, dynamic user session IDs) and group them under a common user action name.

Placeholders consist of the following three elements:

* An input value, such as a page URL
* A processing step that extracts or replaces parts of the input (optional)
* The placeholder name, which is used in the user action naming rule

To make placeholders easier to use, Dynatrace provides a set of pre-defined placeholders, such as `pageUrl`, `sourceUrl`, `xhrUrl`, `Top XHR URL`, and `pageTitle`. To understand placeholders better, consider the following example: an XHR action triggers the selection of the confirmation button on a checkout page. Selecting the confirmation button (the source action in this case) is followed by one of these target actions:

* multiple chained XHR requests are triggered by the first web request, such as `xhrUrl` or `Top XHR URL`.
* a new load action is triggered, redirecting you to a confirmation page. In this case, you have a `sourceUrl`, which is the URL where you finished the checkout process, and the `pageUrl`, which is the URL where you see the confirmation of the checkout process.

Such chains and correlations of actions are best seen in a waterfall chart. You can use `sourceURL` and `pageURL`, or the XHR equivalents `XHRUrl` and `Top XHR URL`, to properly name your actions in cases where such correlations occur.

The provided set of placeholders is non-customizable but can be immediately used for creating your own naming rules. You can also create your own placeholders.

### Create a placeholder

To create a placeholder

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **User actions**.
5. Under **Placeholders**, select **Add placeholder**, and select your input data type.

   For the **CSS selector**, **JavaScript variable**, **Meta tag**, and **Cookie value** data types, you must also specify a value.

   ![Add a placeholder](https://dt-cdn.net/images/screenshot-2020-08-27-at-15-22-45-1308-aba05796c1.png)

   Add a placeholder
6. Optional Add processing steps and conditions, and preview your placeholder to see if it works as intended.
7. Optional In case you added an **extract** or **extract with regular expression** processing step, select whether you want to fall back to an empty result (default) or the selected input.
8. Name your placeholder, and select **Save**.

You can add up to 50 placeholders per application.

### Processing steps

To help you make the most of placeholders, weâve introduced the following processing steps:

* **extract**: Requires the delimiter from which the extraction must begin and the delimiter at which the extraction must end. The delimiters are not part of the extraction. If the leading delimiter isn't present, the extraction starts from the beginning of the input. If the trailing delimiter isn't present, the extraction stops at the end of the input. Optionally, you can fall back to an empty result (default) or to the selected input.
* **replace**: Requires the delimiter from which the replacement must begin and the delimiter at which the replacement must end. Optionally, you can also provide the replacement text. When replacement text isn't provided, the matched characters are discarded.
* **replace text**: Requires the text that needs to be identified and matched. Optionally, you can provide the replacement text. When replacement text isn't provided, the matched text is discarded.
* **replace IDs**: Requires the ID that needs to be identified and matched. Optionally, you can provide the replacement IDs. When a replacement ID isn't provided, the matched ID is discarded.
* **extract with regular expression**: Requires a regular expression to identify and extract. Optionally, you can fall back to an empty result (default) or to the selected input.
* **replace with regular expression**: Requires a regular expression to identify the string to be replaced. Optionally, you can provide the replacement regular expression. When not provided, the matched regular expression is discarded. Currently, only one `(.*)` capture group is supported.

If you add multiple processing steps to a placeholder, the steps will be applied in sequence. This means that the first processing step will be applied on the selected input and each subsequent processing step will be applied on the result of the previous processing step.

## Create action names

Dynatrace provides you with the option of creating custom load as well as XHR actions. You can use new placeholders or the existing placeholders that are available in the **Placeholders** list to create your new naming rules.

In this example, we use `CampaignID` to create a new custom naming rule that identifies a page load as a campaign view with the `CampaignID` added to the action name.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **User actions**.
5. Scroll down to **User action naming rules**, and select the **Naming rules for load actions** or **Naming rules for XHR actions** tab.
6. Select **Add naming rule**.
7. Type a naming pattern using a placeholder. Ensure that the placeholder is within braces (example: `{CampaignID}`).
8. Optional Define the conditions under which you can also use placeholders to further refine the applicability of the rules.

   In our example, to create a custom action naming rule that only applies to a special promotional campaign, where `CampaignID` is **3**, you can use conditions and placeholders to only match the desired actions that should be named accordingly.

   ![Creating custom user actions](https://dt-cdn.net/images/campaignid-974-5548a30b62.png)

   Creating custom user actions
9. Optional Use the **Preview your rule** section to check if your new naming rule works as expected.
10. Select **Save**.
11. Use the **Move up/down** controls to change the priority of the rules.

    The first matching rule in the table is applied first.

    ![User action naming rules](https://dt-cdn.net/images/user-action-naming-2077-281508f770.png)

    User action naming rules

You can add up to 250 user action naming rules per application.

## Advanced configuration for action names

The following additional configuration options are available for user action names:

* **Split user actions by domain**: Deactivate this setting if different domains should not result separate user actions. For example, if your application can be accessed at two domains, `www.domain-one.com` and `www.domain-two.com`, and splitting by domain is enabled, a `load of page /index` for `www.domain-one.com` will result in a different user action than `load of page /index` for `www.domain-two.com`.
* **Case-insensitive naming**: Deactivate this setting if the user action names should be stored in case-sensitive form. Case-insensitive naming allows you to search across all cases. For example, user actions like `Loading of Page /` and `Loading of PAGE /` will both map to `loading of page /`.
* **Prioritize load actions and use value of last detected**: Enable this setting if you want to leverage our improved load action propagation. Whenever a load, which is basically a document request, is present during an action, the action is marked as a load action.  
  Additionally, enable this setting to use placeholder values, such as `pageUrl`, of your last load action values for your user action naming. As an example, consider an initial user action like `click /easytravel/search`, which triggers a page reload from the `/easytravel` page to the `/easytravel/search` page and therefore the `loading of page /easytravel/search` load action, which in turn triggers another XHR call.

  + With this setting enabled, the last detected load action is used and therefore this chain of actions is marked as the `loading of page /easytravel/search` load action.
  + With this setting disabled, the action is marked as `click /easytravel/search`, since with the previous version of our load propagation, the load action is not propagated in scenarios where XHR requests are present as well.

## Use cases and examples

In the following sections, we look at examples of user action naming rules that were created in the earlier version and show how equivalent rules can be created using the new, enhanced version of user action naming rules.

#### Extract valuable information out of your data inputs

Examples from the earlier version of user action naming rules:

* **Extract** `/some-path-before/(.*).some-defined-text-after from path` from path
* **Extract** `Loading of page /sales/(.*)` from action name
* **Extract** `(.*)` from page title
* **Extract** `(.*)` from XHR URL

You can now achieve the same result using placeholders and a processing step.  
With the **extract** processing step, you can define leading and trailing delimiters that define exactly where extracted values are to be pulled from. In this way, itâs possible to replace many naming rules that previously required regular expressions.

![Example for extract](https://dt-cdn.net/images/action-naming-examples-1-2880-6cb1cca2e3.png)

Example for extract

#### Name actions based on their URL or path

Examples from the earlier version of user action naming:

* **Design step**: if action name contains `design`
* **Config data call**: action name matches regular expression `*/config/*`
* **Product**: path begins with `/product/`
* **Search**: XHR URL begins with `/api/search/dynamic`

In the earlier version of user action naming rules, the action name was typically used as an input value for the renaming of action names that were automatically detected by Dynatrace. This often led to confusion, since users didnât understand that action names were being used as input values as they were defined.

What had to be differentiated here is the auto-detected action name by Dynatrace (a possible input) and the final action name defined by the user through the naming rule. In all these cases, a user could have simply used the page path or URL or the XHR URL instead.

With the new version, you can use a default placeholder in your naming rule, such as `pageUrlPath` or `pageUrl`, to get the same information, followed by the **begins with** or **contains** condition to do the same.

![Example for renaming](https://dt-cdn.net/images/action-naming-examples-2-2880-da3bd9717a.png)

Example for renaming

Conversely, you can use a **match regular expression** condition for more flexibility.

For example, former rules in the earlier version of user action naming:

* `Customer Contact Request for UFO`: XHR url matches regex match `.*/api/request/.*/contact?category=UFO`

![Example for regex](https://dt-cdn.net/images/action-naming-examples-3-2880-882b31b031.png)

Example for regex

#### Remove or mask parts of your data inputs

Examples from the earlier version of user action naming:

* **Remove ID**: `(\\?|&)_id=:*?(?=&|$)`
* **Remove conversation**: `(\\?|&)conversation=:*?(?=&|$)`
* **Remove params**: `\?.*`
* **Remove searched car**: `(?<=search-results\/cars\/)[a-zA-Z0-9]*`

Removing and masking parts of data can now be achieved more easily with the "remove in-between" approach. If you want to remove the value of a certain query string parameter, which could be the ID of your user, define the key as a trailing delimiter and `&` as a following character that introduces other parameters. If your matching input doesnât have a trailing delimiter, you'll be notified.

![Example for renaming](https://dt-cdn.net/images/action-naming-examples-4-2880-c6afd6f33c.png)

Example for renaming

For more flexibility or, for example, to remove all parameters of your URL, use **replace by regular expression**.

![Example for replacing with regex](https://dt-cdn.net/images/action-naming-examples-5-2880-fcdb41b968.png)

Example for replacing with regex

#### Consolidate naming rules by leveraging placeholders

Letâs consider an e-commerce checkout in this example. To name your load actions for each step in the earlier version, you had to first define one action naming rule for each individual step.

In this case, one rule is assigned per checkout step:

* **Loading of Enter personal details**: action name begins with `/checkout/index.php?step=details`
* **Loading of Select payment method**: action name begins with `/checkout/index.php?step=payment`
* **Loading of Order summary**: action name begins with `/checkout/index.php?step=summary`
* **Loading of Order confirmation**: action name begins with `/checkout/index.php?step=confirmation`

With the new version, you can create a placeholder that uses a JavaScript variable called `adobePageName` as input, which may already be available in an existing data layer of an analytics tool, for example Adobe Analytics.

![Example for JS variable](https://dt-cdn.net/images/action-naming-examples-6-2880-2ef565421f.png)

Example for JS variable

Leveraging the power of your previously defined placeholder, you can then create a single action naming rule that covers all the naming rules you created with the earlier version and result in the same action names.

![Load action example](https://dt-cdn.net/images/action-naming-examples-7-2880-03a056e0eb.png)

Load action example

## Set action name via `data-dtname`

If the standard action name detection doesn't serve your purpose, you can also set the `data-dtname` custom attribute within the HTML tags and use it as a caption. For instance, the following action:

```
<label for="txtFirstname">Firstname</label> <input data-dtname="Firstname Text Input" type="text" value="firstname" name="firstname" title="Firstname" id="txtFirstname" />
```

can be assigned the `click on "Firstname Text Input"` caption.

For a custom attribute to appear as a user action name, you also need to [configure a naming rule](#create-action-names) that includes the `{elementIdentifier (default)}` placeholder.

If you're using different attribute names for different tools, you can choose to set an alternative to `data-dtname` that Dynatrace can use for user action naming purposes.

## Related topics

* [User actions](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")