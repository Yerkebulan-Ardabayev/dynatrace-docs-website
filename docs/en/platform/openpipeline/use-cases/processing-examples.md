---
title: OpenPipeline processing examples
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/processing-examples
scraped: 2026-03-01T21:11:33.282994
---

# OpenPipeline processing examples

# OpenPipeline processing examples

* Latest Dynatrace
* Tutorial
* 13-min read
* Updated on Jun 23, 2025

This article focuses on data processing scenarios and provides standalone examples of how to configure the OpenPipeline processors in order to achieve a result.

## Configure a new processor

To configure a new processor in OpenPipeline

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and chose a date type.
2. Find an existing pipeline or create a new one.
3. Select the stage.
4. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** and choose the processor.
5. Configure the processor by entering the required fields. Note that required fields vary based on the processor and are indicated in the user interface.
6. Save the pipeline.

## Examples

Expand the steps for the following examples to learn how to configure the processors.

### Fix unrecognized timestamp and loglevel based on a matched log source

A stored event from an application (`myLogSource`) in the log viewer is missing a proper timestamp and loglevel. You can retrieve this information from the source and parse it to achieve the following:

* Transform the unrecognized timestamp to a log event timestamp.
* Show a loglevel for the log.
* Extract the thread name from the log line into a new attribute (`thread.name`).

### Steps

1. Find the matching condition.

   1. Go to **Logs and events** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") and turn on **Advanced mode**.
   2. Enter the following DQL query to filter log data from the log source. Make sure to modify `myLogSource` with the log source.

      ```
      fetch logs



      | filter matchesValue(log.source, "myLogSource")
      ```
   3. Run the query and, when you're satisfied with the filter result, copy the `matchesValue()` function.

      ```
      matchesValue(log.source, "myLogSource")
      ```
2. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines** and select (or create) the pipeline for the log ingest source.
3. Configure a **DQL processor** in the **Processing** stage as follows.
4. Save the pipeline.

Conclusion

The processed log record is displayed with metadata, including a `timestamp` and the `loglevel` attribute with proper values and the extracted attribute `thread.name`. Once new data is ingested, the processed records have a timestamp, a loglevel, and the thread name as separate attributes. You can visualize the new format, for example, in a notebook.

**Before**

```
{



"content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



"status":"NONE",



"timestamp":"1650889391528",



"log.source":"myLogSource",



"loglevel":"NONE"



}
```

**After**

```
{



"results":



[



{



"matched": true,



"record": {



"loglevel": "INFO",



"log.source": "myLogSource",



"thread.name": "myPool-thread-1",



"content": "April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



"timestamp": "2022-04-24T09:59:52.000000000Z",



"status": "NONE"



}



}



]



}
```

### Parse a field containing JSON as a raw string

A record has a field `content` (`String`) containing JSON input from which you want to parse out information. You can process specific fields, nested fields, or all fields, and treat them as plain text or bring them to top-level without knowing the schema of the JSON.

### Steps

Depending on the type of field you want to parse out, configure a **DQL** processor in the **Processing** stage with a **DQL processor definition** copied from one of the following:

Specific fields

Nested fields

All fields, without listing them

Any field from JSON, as plain text

All fields and bring them to top-level

```
parse content, "JSON{STRING:stringField:new.name}(flat=true)"



// Parses out a string field from raw record data into a standalone top-level attribute via a DPL JSON matcher.



// `flat=true` automatically creates attributes named as specified in the JSON. To rename the field, provide a new name inline after an additional `:`.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.name": "stringFieldValue"



}
```

```
parse content, "JSON{STRING:stringField, JSON {STRING:nestedStringField1}:nested}:parsedJson"



| fieldsAdd new.attribute1 = parsedJson[stringField]



| fieldsAdd new.attribute2 = parsedJson[nested][nestedStringField1]



| fieldsRemove parsedJson



// Parses out multiple string fields, including nested one, from raw record data into standalone top-level attributes, via a DPL JSON matcher.
```

Conclusion

You can process the record further; for example, you can create a top-level attribute from its nested fields.

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.attribute1": "stringFieldValue",



"new.attribute2": "NestedValue1"



}
```

```
parse content, "JSON:parsedJson"



| fieldsAdd new.field1 = parsedJson[intField],



new.field2 = parsedJson[stringField],



new.field3 = parsedJson[nested][nestedStringField1],



new.field4 = parsedJson[nested][nestedStringField2]



| fieldsRemove parsedJson



// Parses out all JSON fields without listing the attributes, via a DPL JSON matcher.
```

Conclusion

You can process the record further; for example, you can create a top-level attribute from its nested fields.

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"new.field1": "13",



"new.field2": "stringFieldValue",



"new.field3": "NestedValue1",



"new.field4": "NestedValue2"



}
```

```
parse content, """LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute"""



// Treats fields as plain text and renames any string that matches as specified.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"newAttribute": "stringField"



}
```

```
parse content, "JSON:parsedJson"



| fieldsFlatten parsedJson, prefix: "j"



// Parses out all fields without enumerating them and creates top-level fields from the JSON string without the need to enumerate the field names. It can be applied to multiple JSON objects.
```

Conclusion

**Before**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }"



}
```

**After**

```
{



"content": "{\"intField\": 13, \"stringField\": \"stringFieldValue\", \"nested\": {\"nestedStringField1\": \"NestedValue1\", \"nestedStringField2\": \"NestedValue2\"} }",



"j.stringField": "stringFieldValue",



"j.intField": 13,



"j.nested":"{\"nestedStringField1\":\"NestedValue1\", \"nestedStringField2\":\"NestedValue2\"}"



}
```

### Parse out attributes with different formats

Applications log the user ID with different schemes (`user ID=`, `userId=`, `userId:` , `user ID =`). You can parse out attributes with different formats via a single pattern expression that uses the optional modifier (`?`) and `Alternative Groups`.

### Steps

To extract the user identifier as a standalone log attribute, configure a **DQL** processor in the **Processing** with the following **DQL processor definition**.

```
parse content, "



LD // Matches any text within a single line



('user'| 'User') // Matches specified literals



SPACE? // Matches optional punctuation



('id'|'Id'|'ID')



SPACE?



PUNCT?



SPACE?



INT:my.user.id"
```

Conclusion

With a single definition, you've extracted the user identifier from different log schemes and applied a standardized format that can be used in further stages.

**Before**

```
03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0



03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0
```

**After**

```
"my.user.id":"1234567"
```

### Use specialized DPL matchers

A JSON file contains information that you want to parse out and create new dedicate fields for it, based on the format. You can use [Dynatrace Pattern Language (DPL) matchers](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") for easier pattern building.

### Steps

To use DPL matchers to identify and create new dedicated fields for a timestamp, a loglevel, the IP address, the endpoint, and response code from the JSON file content, configure a **DQL** processor in the **Processing** stage with the following definition.

```
parse content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code"
```

Conclusion

You created new fields for the timestamp, a loglevel, IP address, endpoint, and response code, based on the format used in your JSON file.

**Before**

```
{



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"



}
```

**After**

```
{



"request": "GET /api/v2/logs/ingest HTTP/1.0",



"code": 200,



"loglevel": "INFO",



"ip": "192.168.33.1",



"timestamp": "2022-05-11T13:23:45.000000000Z",



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 GET /api/v2/logs/ingest HTTP/1.0 200"



}
```

### Perform basic math on attributes

You can parse out specific values from a JSON file, perform calculations, and format the results by leveraging DQL functions and operators.

### Steps

Configure a **DQL** processor in the **Processing** stage with the following definition.

```
parse content, "LD 'total: ' INT:total '; failed: ' INT:failed" // Parses `total` and `failed` field values.



| fieldsAdd failed.percentage = 100.0 * failed / total // Calculates the failure percentage, formats the result to be a percentage, and stores it in a new attribute (`failed.percentage`).



| fieldsRemove total, failed // Removes temporary fields that are no longer needed from the JSON file.
```

Conclusion

You calculated the failure percentage based on the JSON content and created a new dedicated field.

**Before**

```
{



"content": "Lorem ipsum total: 1000; failed: 255",



}
```

**After**

```
{



"content": "Lorem ipsum total: 1000; failed: 255",



"failed.percentage": 25.5



}
```

### Add new attributes

You can add attributes that have static or dynamic values by leveraging different processors, with and without DQL queries.

### Steps

To add attributes, configure one of the following processors in the **Processing** stage.

Add fields

DQL

This processor doesn't leverage DQL queries. You can use it to add attributes with static values.

For example, you can add `company.team.name` with value `my-team` and `company.branch.name` with value `New York`. These key-value pairs will be added to all matched records.

Conclusion

You added new top-level fields that store the team name (`company.team.name`) and the branch location (`company.branch.name`) to the JSON file. The values remain static until they're manually modified.

**Before**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"company.team.name": "my-team",



"company.branch.name": "New York"



}
```

You can use it to add attributes with dynamic values. Use a definition that contains the `fieldsAdd` command, such as the following example:

```
fieldsAdd content.length = stringLength(content), content.words = arraySize(splitByPattern(content, "' '"))
```

Conclusion

You added new top-level fields that store the length (`content.length`) and number of words (`content.words`) of a JSON field. The values adapt to the content of the record.

**Before**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"content.length": "62",



"content.words": "9"



}
```

### Remove attributes

You can remove attributes by leveraging different processors, with and without DQL queries.

### Steps

To remove specific fields

* Configure a **Remove fields** processor in the **Processing** stage by providing the field names. This processor doesn't leverage DQL queries.
* Configure a **DQL** processor in the **Processing** stage by entering a definition that contains the `fieldsRemove` command, such as the following example:

  ```
  fieldsRemove redundant.attribute
  ```

Conclusion

**Before**

```
{



"redundant.attribute": "value",



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

**After**

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

### Rename attributes

You can rename attributes by leveraging different processors, with and without DQL queries.

### Steps

To rename an attribute of a matching record to a static value,

* Configure a **Rename fields** processor in the **Processing** stage by providing the field names that you want to be renamed and the new names. This processor doesn't leverage DQL queries.
* Configure a **DQL** processor in the **Processing** stage by entering a definition that contains the `fieldsRename` command, such as the following example:

  ```
  fieldsRename better_name = field // Renames a field to a static value
  ```

Conclusion

**Before**

```
{



"content": {"field": "Lorem ipsum"}



}
```

**After**

```
"content": {"better_name": "Lorem ipsum"}
```

### Drop records

You can drop ingested records at different stages by leveraging different processors.

### Steps

To drop an ingested record

* Before it's processed, configure a **Drop record** processor in the **Processing** stage by providing a matcher query.
* After it's processed, configure a **No storage assignment** processor in the **Storage** stage by providing a matcher query.

Conclusion

The matching records won't be stored in Grail.

### Mask data

You can mask parts of an attribute by leveraging `replacePattern` in combination with other DQL functions.

### Steps

In this scenario you want to mask part of an IP address. Configure a **DQL** processor in the **Processing** stage with one of the following definitions, depending on the part that you want to mask.

Given bits

Pattern

Repetitive patterns

Part of a field

The following example uses the [`ipMask`](/docs/platform/grail/dynatrace-query-language/functions/network-functions#ipMask "A list of DQL array functions.") function to set the last octet to the value `0`.

```
fieldsAdd ip = ipMask(ip, 24)
```

Conclusion

**Before**

```
{



"ip": "192.168.1.12"



}
```

**After**

```
{



"ip": "192.168.1.0"



}
```

The following example uses the [`replacePattern`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.") function together with DPL matchers and the [`Lookaround` behind modifier](/docs/platform/grail/dynatrace-pattern-language/log-processing-modifiers#lookaround "Explore DPL syntax for optional controlling elements (modifiers).")(`<<`) to match a specific part (the last octet) of an IP address and set it to `xxx`.

```
fieldsAdd ip = replacePattern(ip, "<< (INT'.'INT'.'INT'.') INT", "xxx")
```

Conclusion

**Before**

```
{



"ip": "192.168.1.12"



}
```

**After**

```
{



"ip": "192.168.1.xxx"



}
```

The following example uses the [`replacePattern`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replacePattern "A list of DQL string functions.") function to mask all IP addresses within a single field.

```
fieldsAdd content=replacePattern(content, "IPADDR", "xxx.xxx.xxx.xxx")
```

Conclusion

**Before**

```
{



"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194  dolor sit amet"



}
```

**After**

```
{



"content": "Lorem ipsum client_ip: xxx.xxx.xxx.xxx email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: xxx.xxx.xxx.xxx dolor sit amet"



}
```

The following example parses out the username of an email address and uses the [`replaceString`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#replaceString "A list of DQL string functions.") function to replace it with a static value.

```
parse content, "LD 'email: ' LD:user '@'"



| fieldsAdd content = replaceString(content, user, "xxx")



| fieldsRemove user
```

Conclusion

**Before**

```
{



"content" : "Lorem ipsum client_ip: 192.168.1.12 email: john.doe@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"



}
```

**After**

```
{



"content": "Lorem ipsum client_ip: 192.168.1.12 email: xxx@dynatrace.com card number: 4012888888881881 server_ip: 215.131.189.194 dolor sit amet"



}
```

## Related topics

* [Configure a processing pipeline](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Configure ingest sources, routes, and processing for your data in OpenPipeline.")
* [Processing in OpenPipeline](/docs/platform/openpipeline/concepts/processing "Learn the core concepts of Dynatrace OpenPipeline processing.")