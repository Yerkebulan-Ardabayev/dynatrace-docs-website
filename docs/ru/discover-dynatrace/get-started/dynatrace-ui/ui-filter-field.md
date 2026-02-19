---
title: Filter field
source: https://www.dynatrace.com/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field
scraped: 2026-02-19T21:16:12.233947
---

# Filter field

# Filter field

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jan 07, 2026

The filter field is a powerful UI component that enables you to quickly narrow down results and find relevant information within Dynatrace apps. Use the filter field when you need to search by specific attributes (like service name or status), combine multiple conditions with logical operators, or filter JSON data using dot or bracket notation.

For complex queries beyond what the filter field offers, consider using [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") instead.

## Anatomy

![Filter field component in the Dynatrace UI.](https://dt-cdn.net/images/ui-filter-field-2018-44c7241dc1.png)

1. **Filter statement**: Each gray section is one complete statement of a filter criteria.
2. **Key**: The first part of the filter statement is the filter key or category.
3. **Comparison operator**: Shows the type of comparison.
4. **Value**: The specific value that youâre looking for.
5. **Logical operator**: Connects multiple filter statements. `AND` will be used automatically unless you add `OR`.

## How to use filters

* To create a filter statement, simply start typing in the filter field. A dropdown with suggestions will immediately open.
* Depending on the implementation, you can apply the filter:

  + By making a change in the filter field (dynamic filtering)
  + By selecting **Apply** (batched filtering)
  + By using the keyboard shortcuts: Windows**Ctrl+Enter** or macOS**Cmd+Enter**
* To clear the entire filter field, select the `X` at the right side of the field.
* To remove an individual filter, hover over the filter statement and select the `X` for that statement.

### Use filter suggestions

To make things easier for you, filter field offers relevant suggestions as you type.

* Descriptions on the right side of the suggestion provide context.
* To apply a suggestion, select it from the list (click or tap), or use the up and down arrow keys to navigate the list and then press **Enter**.

## General syntax

* Use a space as the separator, or delimiter, between keys, comparison operators, values, and filter statements.
* For numbers, use a decimal point `.` as the decimal separator.
* For arrays, use an equals sign `key = value`.

Note

Some features may not be available due to performance or data source limitations. For example, filter field generally supports [wildcards](#wildcards) (indicated by an asterisk `*`) at either the beginning (ends-with) or end (starts-with) of a value. However, certain implementations, such as those based on the classic entity selector API, might not support the ends-with option.

### Search

* Use `* ~ searchterm` to search across all data.
* Multiple searches can be combined using `AND` or `OR`. For details, see [Logical operators](#filter-field-logical-operators). In the following example, the result includes all data with the terms `paymentError` or `timeout` in any field.

  `* ~Â paymentError OR * ~ timeout`
* Searches can be combined with filters using `AND`. For details, see [Logical operators](#filter-field-logical-operators). In the following example, the result includes all data from the `payment-service` with the term `paymentError` in any field.

  `service = payment-service AND * ~Â paymentError`

### Comparison operators

Comparison operators define how a key compares to a value. Here are the available comparison operators:

Filter syntax

Description

Example

`=`

equals

`key = value`

`!=`

doesn't equal

`key != value`

`<`

less than

`key < value`

`<=`

less than or equal to

`key <= value`

`>`

greater than

`key > value`

`>=`

greater than or equal to

`key >= value`

`= *`

is any value

`key = *`

`!= *`

isn't any value

`key != *`

`in`

matches one or more values in a list of values

`key in (value1, value2)`

`not in`

doesnât match any value in a list of values

`key not in (value1, value2)`

### Logical operators

The filter field supports the logical operators `AND` and `OR`. If you donât specify an operator, filter statements are automatically connected by an implicit `AND`, which is the default logical operator between any two expressions.

Filter syntax

Description

Example

`AND`

Both expressions must be true.

`key = value key2 = value`  
Alternative:  
`key = value AND key2 = value`

`OR`

Only one expression must be true.

`key = value OR key2 = value`

### Grouping filter statements

Use parentheses `()` to group filter statements logically. For example, `key = value OR (key2 = value key3 = value)`.

### Escaping values

Space, `*`, `,`, `(`, `)`, `!`, `<`, `>`, `=`, `"`, `$`, `:`, `[`, `]`, `\`, and `~` are special characters in the filter field. To use special characters as part of a key or a value, you need to escape them.

Escape option

Description

Example

Quotation marks `"`

Wrap the corresponding key or value in quotation marks. In the following example, the spaces between `Product` and `Name`, and between `Widget` and `A`, are escaped by wrapping the values in quotation marks.

`"Product Name" = "Widget A"`

Backslash `\`

Escape a single character with a backslash `\`. In the following example, the asterisk on the right end is escaped with a backslash. This means it isn't interpreted as a wildcard.

`key = openshift-service-serving-signer@1677006647\*`

If you want a backslash to appear in a value, it must itself be escaped.
For example, to get `path = C:\my\path` you need to write `path = C:\\my\\path`.

### Case sensitivity

String values are case-insensitive for all operators.

### Wildcards

A wildcard will match any character in a value. Wildcards are indicated by an asterisk `*`.

Wildcard syntax

Description

`key = *value`

ends with any `value`

`key = value*`

starts with any `value`

`key = *value*`

contains any `value`

When a value contains **special characters** such as spaces, you must escape the value to ensure that it is correctly interpreted. In such cases, wildcards can be used **outside or inside** the escaped value. See examples below:

Suppose you want to filter for a service named "Payment Service". You would write the filter like this:

`Name = "Payment Service"`

This ensures that the entire string "Payment Service" is treated as a single value, including the space between "Payment" and "Service".

If you want to use wildcards with a value that contains spaces, you can do it like this:

`Name = *"Payment Service"*`

Or like this:

`Name = "*Payment Service*"`

This filter will match any service name that contains "Payment Service" anywhere within the name.

Wildcards are not supported within the `in ()` operator. The `in ()` operator filters for exact matches and does not interpret `*` as a wildcard.
If you want to use `*` as a literal character, you need to escape it using a backslash `\`. For example, to match the string `/visit*/_settings`, use `key = "/visit\*/_settings"`.
For more details, see [Escaping values](#escaping-values) in filter expressions.

### Variables

Variables act as a placeholder and allow you to dynamically select the values you want to use. To reference a variable, start the value with a `$`. For example: `k8s.cluster.name = $cluster`.

#### Variables and wildcards

Use the wildcard character `*` to filter for data that starts with, ends with, or contains a variable's value. You can place the `*` before, after, or on both sides of a variable. The position of the `*` determines how the filter behaves. For more insights see [wildcards](#wildcards).

When using a variable like `$cluster`, the position of the `*` relative to the variable determines the matching behavior:

* **Ends with the variable value**

  + `k8s.cluster.name = *$cluster` matches any value that ends with the value of `$cluster`.
  + **Example:** If `$cluster` is *myClusterName*, this matches *prod-myClusterName*.
* **Starts with the variable value**

  + `k8s.cluster.name = $cluster*` matches any value that starts with the value of `$cluster`.
  + **Example:** Matches *myClusterName-east*.
* **Contains the variable value**

  + `k8s.cluster.name = *$cluster*` matches any value that contains the value of `$cluster` anywhere within the string.
  + **Example:** Matches *prod-myClusterName-east*.

#### Related content

* [Variables in dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new/components/dashboard-component-variable "Add variables to your Dynatrace dashboards.")
* [Variables in segments](/docs/manage/segments/concepts/segments-concepts-variables "Learn how variables help to form dynamic segments and reduce configuration effort and maintenance.")

### Filtering JSON data

Access nested fields in JSON data with dot or bracket notation. JSON filters may use a combination of dot and bracket notations.

Notation

Description

Example

Dot notation
`key$.field`

Use the compact dot notation for simple syntax.

`content$.uri = "/status-service/deployments/health"`

Bracket notation
`key$["field"][index]`

Use bracket notation for subkeys with special characters (spaces, dashes, etc.) and to access a child of an array.

`content$["spans"][0]["duration-ms"] > 75`