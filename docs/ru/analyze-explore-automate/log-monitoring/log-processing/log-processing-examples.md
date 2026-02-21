---
title: Log processing examples (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples
scraped: 2026-02-21T21:19:40.165564
---

# Log processing examples (Logs Classic)

# Log processing examples (Logs Classic)

* Tutorial
* 18-min read
* Updated on Sep 22, 2025

Log Monitoring Classic

Depending on the rules that you create, you can customize incoming log data according to your needs. See below for example data processing scenarios.

* [Example 1](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample1 "Example log processing scenarios.") - Fix unrecognized timestamp and loglevel visible in the log viewer based on matched log source.
* [Example 2](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample2 "Example log processing scenarios.") - Define searchable custom attribute using the extracted identifier from a matched phrase in the log content.
* [Example 3](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample3 "Example log processing scenarios.") - Create billed duration metric for AWS service using log data.
* [Example 4](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample4 "Example log processing scenarios.") - Parse out specific fields from JSON content.
* [Example 5](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample5 "Example log processing scenarios.") - Parse out attributes from different formats within a single pattern expression.
* [Example 6](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample6 "Example log processing scenarios.") - Multiple PARSE commands within a single processing rule.
* [Example 7](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample7 "Example log processing scenarios.") - Use specialized matchers.
* [Example 8](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample8 "Example log processing scenarios.") - Manipulate any attribute from log (not only content).
* [Example 9](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample9 "Example log processing scenarios.") - Add a new attribute to the current log event structure.
* [Example 10](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample10 "Example log processing scenarios.") - Basic math on attributes.
* [Example 11](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample11 "Example log processing scenarios.") - Drop a specific attribute from log message.
* [Example 12](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample12 "Example log processing scenarios.") - Drop the whole log event.
* [Example 13](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios.") - Mask any attribute.
* [Example 14](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample14 "Example log processing scenarios.") - Rename attributes.
* [Example 15](/docs/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample15 "Example log processing scenarios.") - Input field data types.

### Example 1: Fix unrecognized timestamp and loglevel

You can fix unrecognized timestamp and loglevel visible in the log viewer based on matched log source.
For this example, let's assume that you see a stored event in the log viewer from the `log.source` application that is set to `/var/log/myapp/application.log.#`

You notice a couple of things you want to fix:

* The log contains an unrecognized timestamp format that you want to be treated as a log event timestamp.
* There is no proper logLevel detected.

So you want to transform your log data to contain the proper values in the timestamp and logLevel fields, and you want to add a new `thread.name` attribute containing a properly extracted value.

To create a processing rule

1. Copy the log viewer query to the clipboard (`log.source="/var/log/myapp/application.log.#"`).
2. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
3. Enter the rule name and the copied log query from your clipboard.  
   **Rule name**: `MyApp log processor`  
   **Matcher**: `log.source="/var/log/myapp/application.log.#"`
4. Enter the rule definition to parse out the timestamp, thread name, and log level.  
   **Rule definition**: `PARSE(content, "TIMESTAMP('MMMMM d, yyyy HH:mm:ss'):timestamp ' [' LD:thread.name '] ' UPPER:loglevel")`  
   where:

   * `TIMESTAMP` matcher is used to look for the specific datetime format, and the matched value is set as the existing timestamp log attribute.
   * `LD` (Line Data) matcher is used to match any chars between literals `' ['` and `'] '`.
   * `UPPER` literal is used to match uppercase letters.
   * The remaining part of the content is not matched.
5. Enter the following log data fragment manually in the **Log sample** text box.

   ```
   {



   "event.type":"LOG",



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "status":"NONE",



   "timestamp":"1650889391528",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"NONE"



   }
   ```
6. Select **Test the rule**.  
   The processed log data is displayed. The `timestamp` and the `loglevel` fields have proper values. The additional attribute `thread.name` is also correctly extracted.

   ```
   {



   "content":"April 24, 2022 09:59:52 [myPool-thread-1] INFO Lorem ipsum dolor sit amet",



   "timestamp":"1650794392000",



   "event.type":"LOG",



   "status":"NONE",



   "log.source":"/var/log/myapp/application.log.#",



   "loglevel":"INFO",



   "thread.name":"myPool-thread-1"



   }
   ```
7. Save your log processing rule.

As the new log data is ingested, you'll be able to see processed log data in the log viewer.

### Example 2: Define searchable custom attribute

You can define a searchable custom attribute using the extracted identifier from a matched phrase in the log content.

In this example, you see the following log line in the log file (not stored in Dynatrace yet), and you want to extract an identifier from that log line to make it searchable in the log viewer.

`2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`

1. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
2. Enter a rule name and log query. For the log query, use the constant phrase from the log data content (`content="Critical error occurred for product ID"`)  
   **Rule name**: `MyApp product ID with error`  
   **Matcher**: `content="Critical error occurred for product ID"`
3. Enter a rule definition to parse out the ID.  
   **Rule definition**: `PARSE(content, "LD 'product ID:' SPACE? INT:my.product.id")`
4. Assuming that you observed the following log record in the log viewer, you can select **Download a log sample** and automatically populate the **Log sample** text box with your log data.  
   `2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet`  
   Alternatively, you can insert the observed log record as log record content manually in the **Log sample** text box:

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet"



   }
   ```
5. Select **Test the rule**.  
   The processed log data is displayed. The processed log data displayed is enriched with the parsed-out product identifier.

   ```
   {



   "content": "2022-04-26 10:53:01 UTC ERROR Critical error occurred for product ID: 12345678 Lorem ipsum dolor sit amet",



   "timestamp": "1650961124832",



   "my.product.id": "12345678"



   }
   ```
6. Save your log processing rule.
7. Go to **Settings** > **Log Monitoring** > **Custom attributes** and select **Add custom attribute**.
8. Create a custom attribute based on a parsed-out product identifier (`my.product.id`).  
   **Key**: `my.product.id`  
   For details see, [Log custom attributes (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-custom-attributes "Learn how to create and use custom attributes during log data ingestion.").
9. Save your custom attribute.
10. Now you can search and filter the log data by the `my.product.id` attribute in the log viewer.

### Example 3: Create billed duration metric for AWS service using log data



In this example, you want to monitor the actual billed duration from your AWS services. You want to use the `cloud.provider` attribute with the `aws` value in your log data. In the log viewer, you see a log record containing the following line:

`REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`

Additionally, that log record contains the `cloud.provider` attribute with the `aws` value.

1. Go to **Settings** > **Log Monitoring** > **Processing** and select **Add processing rule**.
2. Enter the rule name and the log query. For the log query, use the constant phrase from the log data content for `cloud.provider="aws"` and `content="Billed Duration"`  
   **Rule name**: `AWS services - billed duration`  
   **Matcher**: `cloud.provider="aws" and content="Billed Duration"`
3. Enter a rule definition to parse out the billed duration value.  
   **Rule definition**: `PARSE(content, "LD 'Billed Duration:' SPACE? INT:aws.billed.duration")`
4. Assuming that you observed the following log record the log viewer, you can select **Download a log sample** and automatically populate the **Log sample** text box with your log data.  
   `REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc Duration: 5033.50 ms Billed Duration: 5034 ms Memory Size: 1024 MB Max Memory Used: 80 MB Init Duration: 488.08 ms`  
   Alternatively, you can enter the following log data fragment (containing other additional attributes) manually in the **Log sample** text box:

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO"



   }
   ```
5. Select **Test the rule**.  
   The processed log data is displayed. The processed log data displayed is enriched with the new `aws.billed.duration` attribute.

   ```
   {



   "event.type": "LOG",



   "content": "REPORT RequestId: 000d000-0e00-0d0b-a00e-aec0aa0000bc\tDuration: 5033.50 ms\tBilled Duration: 5034 ms\tMemory Size: 1024 MB\tMax Memory Used: 80 MB\t\n",



   "status": "INFO",



   "timestamp": "1651062483672",



   "cloud.provider": "aws",



   "cloud.account.id": "999999999999",



   "cloud.region": "eu-central-1",



   "aws.log_group": "/aws/lambda/aws-dev",



   "aws.log_stream": "2022/04/27/[$LATEST]0d00000daa0c0c0a0a0e0ea0eccc000f",



   "aws.region": "central-1",



   "aws.account.id": "999999999999",



   "aws.service": "lambda",



   "aws.resource.id": "aws-dev",



   "aws.arn": "arn:aws:lambda:central-1:999999999999:function:aws-dev",



   "cloud.log_forwarder": "999999999999:central-1:dynatrace-aws-logs",



   "loglevel": "INFO",



   "aws.billed.duration": "5034"



   }
   ```
6. Save your log processing rule.
7. Go to **Settings** > **Log Monitoring** > **Metrics extraction** and select **Add log metric**.
8. Create a log metric based on the parsed-out product identifier (`aws.billed.duration`).  
   **Key**: `log.aws.billed.duration`  
   **Query**: `cloud.provider="aws" and content="Billed Duration"`  
   **Measure**: `Attribute value`  
   **Attribute**: `aws.billed.duration`  
   For details see, [Log metrics (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.").
9. Save your log metric.
10. The `log.aws.billed.duration` metric is visible in Data Explorer, and you can use it throughout Dynatrace like any other metric. You can add it to your dashboard, include it in analysis, and even use it to create alerts.

    Log metric availability in Dynatrace

    A created log metric is available only when new log data is ingested and it matches the log query defined during log metric creation. Ensure that new log data has been ingested before using the log metric in other areas of Dynatrace.

### Example 4: Parse out specific fields from JSON content

In this example, you see a log line that has the following JSON structure:

`{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }`

The sample log would look like this:

```
{



"content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

* Parsing field from JSON in flat mode.  
  You can use a JSON matcher and configure it to extract desired fields as top-level log attributes. The matcher in flat mode creates attributes automatically and names them exactly the same as the corresponding JSON field names.

  You can then use the `FIELDS_RENAME` command to set the names that fit you.

  Processing rule definition:

  ```
  PARSE(content, "JSON{STRING:stringField}(flat=true)")



  | FIELDS_RENAME(better.name: stringField)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "better.name": "someValue"



  }
  ```
* Parsing nested field from JSON.  
  You can also parse more fields (including nested ones) using a JSON matcher without flat mode. As a result, you get a `VariantObject` that you can process further. For example, you can create a top-level attribute from its inner fields.

  Processing rule definition:

  ```
  PARSE(content, "



  JSON{



  STRING:stringField,



  JSON {STRING:nestedStringField1}:nested



  }:parsedJson")



  | FIELDS_ADD(top_level.attribute1: parsedJson["stringField"], top_level.attribute2: parsedJson["nested"]["nestedStringField1"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "top_level.attribute1": "someValue",



  "top_level.attribute2": "someNestedValue1"



  }
  ```
* Parsing all fields from JSON in auto-discovery mode.  
  Sometimes you're interested in all of the JSON fields. You don't have to list all of the attributes. Instead, a JSON matcher can be used in auto-discovery mode. As a result, you get a `VARIANT_OBJECT` that you can process further. For example, you can create a top-level attribute from its inner fields.

  Processing rule definition:

  ```
  PARSE(content,"JSON:parsedJson")



  | FIELDS_ADD(f1: parsedJson["intField"],



  f2:parsedJson["stringField"],



  f3:parsedJson["nested"]["nestedStringField1"],



  f4:parsedJson["nested"]["nestedStringField2"])



  | FIELDS_REMOVE(parsedJson)
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "f1": "13",



  "f2": "someValue",



  "f3": "someNestedValue1",



  "f4": "someNestedValue2"



  }
  ```
* Parsing any field from JSON, treating content like plain text.  
  With this approach, you can name the attribute as you lik, but the processing rule is more complex.

  Processing rule definition:

  ```
  PARSE(content, "LD '"stringField"' SPACE? ':' SPACE?  DQS:newAttribute ")
  ```

  Result after transformation:

  ```
  {



  "content": "{"intField": 13, "stringField": "someValue", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



  "newAttribute": "someValue"



  }
  ```

### Example 5: Parse out attributes from different formats

You can parse out attributes from different formats within a single pattern expression.

In this example, one or more applications is logging a user identifier that you want to extract as a standalone log attribute. The log format is not consistent because it includes various schemes to log the user ID:

* `user ID=`
* `userId=`
* `userId:`
* `user ID =`

With the optional modifier (question `?`) and `Alternative Groups`, you can cover all such cases with a single pattern expression:

```
PARSE(content, "



LD //matches any text within a single line



('user'| 'User') //user or User literal



SPACE? //optional space



('id'|'Id'|'ID') //matches any of these



SPACE? //optional space



PUNCT? //optional punctuation



SPACE? //optional space



INT:my.user.id



")
```

Using such a rule, you can parse out the user identifier from many different notations. For example:

`03/22 08:52:51 INFO user ID=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO UserId = 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user id=1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO user ID:1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO User ID: 1234567 Call = 0319 Result = 0`  
`03/22 08:52:51 INFO userid: 1234567 Call = 0319 Result = 0`

### Example 6: Multiple PARSE commands within a single processing rule



You can handle various formats or perform additional parsing on already parsed-out attributes with multiple `PARSE` commands connected with pipes (`|`).

For example, with the following log:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }"



}
```

First, you can parse out the message field, the user ID, and the error message.

```
PARSE(content, "JSON{STRING:message}(flat=true)") | PARSE(message, "LD 'user ' INT:user.id ': ' LD:error.message")
```

The result is:

```
{



"content": "{"intField": 13, "message": "Error occurred for user 12345: Missing permissions", "nested": {"nestedStringField1": "someNestedValue1", "nestedStringField2": "someNestedValue2"} }",



"message": "Error occurred for user 12345: Missing permissions",



"user.id": "12345",



"error.message": "Missing permissions"



}
```

### Example 7: Use specialized matchers

We provide a comprehensive list of matchers that ease pattern building.

For example, you can parse the following sample log event:

```
{



"content":"2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200"



}
```

using the specialized matchers:

```
PARSE(content, "ISO8601:timestamp SPACE UPPER:loglevel SPACE IPADDR:ip SPACE DQS:request SPACE INTEGER:code")
```

and the result is:

```
{



"content": "2022-05-11T13:23:45Z INFO 192.168.33.1 "GET /api/v2/logs/ingest HTTP/1.0" 200",



"timestamp": "1652275425000",



"loglevel": "INFO",



"ip": "192.168.33.1",



"request": "GET /api/v2/logs/ingest HTTP/1.0",



"code": "200"



}
```

### Example 8: Manipulate any attribute from log (not only content)

Unless specified otherwise, the processing rule works only on the read-only content field. For it to work on different log event attributes, you need to use the `USING` command.

For example, the following rule declares two input attributes: writable status and read-only content.
Next, it checks whether the status is `WARN` and the content contains the text `error`. If both conditions are true, the rule overwrites `status` with the value `ERROR`.

Processing rule definition:

```
USING(INOUT status:STRING, content)



| FIELDS_ADD(status:IF_THEN(status == 'WARN' AND content CONTAINS('error'), "ERROR"))
```

Log data sample:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "WARN",



"content":"Some error message"



}
```

Result after transformation:

```
{



"log.source": "using",



"timestamp": "1656011002196",



"status": "ERROR",



"content":"Some error message"



}
```

### Example 9: Add a new attribute to the current log event structure

The FIELDS\_ADD command can be used to introduce additional top-level log attributes.
The following script adds two attributes: the first one stores the length and the second one stores the number of words that are in the content field.

Processing rule definition:

```
FIELDS_ADD(content.length: STRLEN(content), content.words: ARRAY_COUNT(SPLIT(content,"' '")))
```

Log data sample:

```
{



"log.source": "new_attributes",



"timestamp": "1656010654603",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis."



}
```

Result after transformation:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis.",



"timestamp": "1656010654603",



"log.source": "new_attribute",



"content.length": "62",



"content.words": "9"



}
```

### Example 10: Basic math on attributes

With all of the available functions and operators, it's easy to perform calculations.

In the following example, we parse the values of `total` and `failed`, calculate the percentage that failed, and concatenate the value with the percentage sign. Then we store it in a new attribute called `failed.percentage` and remove the temporary fields.

Processing rule definition:

```
PARSE(content,"LD 'total: ' INT:total '; failed: ' INT:failed")



| FIELDS_ADD(failed.percentage: 100.0 * failed / total + '%')



| FIELDS_REMOVE(total, failed)
```

Log data sample:

```
{



"timestamp": "1656011338522",



"content":"Lorem ipsum total: 1000; failed: 250"



}
```

Result after transformation:

```
{



"content": "Lorem ipsum total: 1000; failed: 250",



"timestamp": "1656011338522",



"failed.percentage": "25.0%"



}
```

### Example 11: Drop a specific attribute from log message

To drop an event attribute that is a part of the original record, we first need to declare it as a writable (`INOUT` option) input field with the `USING` command and then explicitly remove it with the `FIELDS_REMOVE` command so that it is not present in the output of the transformation.

In the following example, we declare `redundant.attribute` as an obligatory writeable attribute of `STRING` type and then we remove it.

Processing rule definition:

```
USING(INOUT redundant.attribute:STRING)



| FIELDS_REMOVE(redundant.attribute)
```

Log data sample:

```
{



"redundant.attribute": "value",



"timestamp": "1656011525708",



"content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



}
```

Result after transformation:

```
{



"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus.",



"timestamp": "1656011525708"



}
```

We could use the `?` character to mark the attribute as optional so that the transformation will still run and also succeed if the attribute is not present in the source event.

In this case, the definition would look like this:

```
USING(INOUT redundant.attribute:STRING?)



| FIELDS_REMOVE(redundant.attribute)
```

### Example 12: Drop the whole log event

The whole log event can be dropped with a `FILTER_OUT` command. The event is dropped when the condition passed as the command parameter is fulfilled.

* Prematcher-based dropping
  In most cases, it is enough to drop every event that has been pre-matched.

  For example, if we want to drop all `DEBUG` and `TRACE` events, we could set the matcher query to match either of those statuses and then use the `FILTER_OUT` command to catch everything.

  Matcher:

  ```
  status="DEBUG" or status="TRACE"
  ```

  Processing rule definition:

  ```
  FILTER_OUT(true)
  ```

  Log data sample:

  ```
  {



  "status": "DEBUG",



  "content":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ac neque nisi. Nunc accumsan sollicitudin lacus."



  }
  ```

  This way, all logs with status `DEBUG` or `TRACE` are dropped.
* Advanced dropping condition
  It's also possible to have some extra logic and not drop all the events that are pre-matched.

  In the following example, we drop incoming events where the execution time is below 100 ms.

  Log data sample:

  ```
  {



  "content":"2022-06-23 06:52:35.280 UTC INFO My monitored service call took 97ms"



  }
  ```

  Processing rule definition:

  ```
  PARSE(content, "LD 'My monitored service call took ' INT:took 'ms'")



  | FILTER_OUT(took < 100)



  | FIELDS_REMOVE(took)
  ```

### Example 13: Mask any attribute



Whenever the content or any other attribute is to be changed, it has to be declared as `INOUT` (writable) with the `USING` command. The `REPLACE_PATTERN` is a very powerful function that can be useful when we want to mask some part of the attribute.

* In the following example, we mask the IP address, setting value 0 to the last octet.

  Processing rule definition:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: IPADDR(ip) & 0xFFFFFF00l)
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.0"



  }
  ```
* In the following example, we mask the IP address, setting value `xxx` to the last octet.

  Processing rule definition:

  ```
  USING(INOUT ip)



  | FIELDS_ADD(ip: REPLACE_PATTERN(ip, "(INT'.'INT'.'INT'.'):not_masked INT", "${not_masked}xxx"))
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.12"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009021053",



  "ip": "192.168.0.xxx"



  }
  ```
* In the following example, we mask the entire email address using `sha1` (Secured Hash Algorithm)

  Processing rule definition:

  ```
  USING(INOUT email)



  | FIELDS_ADD(email: REPLACE_PATTERN(email, "LD:email_to_be_masked", "${email_to_be_masked|sha1}"))
  ```

  Log data sample:

  ```
  {



  "content":"Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "john.doe@dynatrace.com"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum",



  "timestamp": "1656009924312",



  "email": "9940e79e41cbf7cc452b137d49fab61e386c602d"



  }
  ```
* In the following example, we mask the IP address, email address, and credit card number from the content field.

  Processing rule definition:

  ```
  USING(INOUT content)



  | FIELDS_ADD(content: REPLACE_PATTERN(content, "



  (LD 'ip: '):p1                                   // Lorem ipsum ip:



  (INT'.'INT'.'INT'.'):ip_not_masked               // 192.168.0.



  INT                                              // 12



  ' email: ':p2                                    //  email:



  LD:email_name '@' LD:email_domain                // john.doe@dynatrace.com



  ' card number: ': p3                             //  card number:



  CREDITCARD:card                                  // 4012888888881881



  ", "${p1}${ip_not_masked}xxx${p2}${email_name|md5}@${email_domain}${p3}${card|sha1}"))
  ```

  Log data sample:

  ```
  {



  "timestamp": "1656010291511",



  "content": "Lorem ipsum ip: 192.168.0.12 email: john.doe@dynatrace.com card number: 4012888888881881 dolor sit amet"



  }
  ```

  Result after transformation:

  ```
  {



  "content": "Lorem ipsum ip: 192.168.0.xxx email: abba0b6ff456806bab66baed93e6d9c4@dynatrace.com card number: 62163a017b168ad4a229c64ae1bed6ffd5e8fb2d dolor sit amet",



  "timestamp": "1656010291511"



  }
  ```

### Example 14: Rename attributes

With the `FIELDS_RENAME` command, we can rename attributes that were a part of an original log event and attributes created within the processor.
Whenever we want to change any attribute from the original event, we need to declare it as `INOUT` (writeable).

In the following example, we rename an existing attribute. Furthermore, we parse out the field from JSON in flat mode and rename the new attribute that has been created automatically with the JSON field name.

Processing rule definition:

```
USING(INOUT to_be_renamed, content)



| FIELDS_RENAME(better_name: to_be_renamed)



| PARSE(content,"JSON{STRING:json_field_to_be_renamed}(flat=true)")



| FIELDS_RENAME(another_better_name: json_field_to_be_renamed)
```

Log data sample:

```
{



"timestamp": "1656061626073",



"content":"{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"to_be_renamed": "Lorem ipsum"



}
```

Result after transformation:

```
{



"content": "{"json_field_to_be_renamed": "dolor sit amet", "field2": "consectetur adipiscing elit"}",



"timestamp": "1656061626073",



"better_name": "Lorem ipsum",



"another_better_name": "dolor sit amet"



}
```

### Example 15: Input field data types

The script in a processor definition operates with strongly typed data: the functions and operators accept only declared types of data. The type is assigned to all input fields defined in the `USING` command as well as to variables created while parsing or using casting functions.

Processing rule definition:

```
USING(number:INTEGER, avg:DOUBLE, addr:IPADDR, arr:INTEGER[],bool:BOOLEAN, ts:TIMESTAMP)



| FIELDS_ADD(multi:number*10)



| FIELDS_ADD(avgPlus1:avg+1)



| FIELDS_ADD(isIP: IS_IPV6(addr))



| FIELDS_ADD(arrAvg: ARRAY_AVG(arr))



| FIELDS_ADD(negation: NOT(bool))



| FIELDS_ADD(tsAddYear: TIME_ADD_YEAR(ts,1))
```

Log data sample:

```
{



"content":"Lorem ipsum",



"number":"5",



"avg":"123.5",



"addr":"2a00:1450:4010:c05::69",



"arr": ["1","2"],



"bool":"false",



"ts":"1984-11-30 22:19:59.789 +0000"



}
```

Result after transformation:

```
{



"content": "Lorem ipsum",



"number": "5",



"avg": "123.5",



"addr": "2a00:1450:4010:c05::69",



"arr": [



"1",



"2"



],



"bool": "false",



"ts": "1984-11-30 22:19:59.789 +0000",



"tsAddYear": "1985-11-30T22:19:59.789000000 +0000",



"negation": "true",



"arrAvg": "1.5",



"isIP": "true",



"avgPlus1": "124.5",



"multi": "50"



}
```