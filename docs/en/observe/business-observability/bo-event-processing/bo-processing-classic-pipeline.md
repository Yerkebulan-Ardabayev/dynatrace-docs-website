---
title: Business event processing via classic pipeline
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing/bo-processing-classic-pipeline
scraped: 2026-02-15T21:11:00.046434
---

# Business event processing via classic pipeline

# Business event processing via classic pipeline

* Latest Dynatrace
* Tutorial
* 5-min read
* Published Oct 24, 2022

Business event processing via the classic pipeline allows you to define how your data will be processed further.

* You can create a processing rule that transforms incoming events.
* You can also specify the retention time for your events by assigning them to buckets.

If you create multiple rules, the rules are performed in the order in which you have defined them.

We recommend utilizing business event processing with [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") as a scalable, powerful solution to manage and process business events. If you don't have access to OpenPipeline, use the classic business event processing pipeline.

## Configure business event processing rules

To configure business event processing rules

1. Go to **Settings** > **Business Observability** > **Ingest Pipeline** > **Processing**.
2. Select **Add rule** and name your rule.
3. Add a **Matcher** to your rule by pasting your [matcher-specific DQL query](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline .").

   Matching based on previous rules is not supported

   The matcher operates on the initial data set before applying any processing rules. Matching records modified by preceding rules is not supported. For example, the modified value of an attribute in rule 1 cannot be used as a matching value in rule 2.
4. Select **Add item** to choose the fields you will transform via the processor definition. Determine the data types and names for your fields. You can choose if the rule is **Optional**, **Is Array**, or **Read-only**.

   * **Optional**: If a transformation field is marked as optional, the transformation can happen even if the field is not provided. But if a transformation field is marked as mandatory (not optional) , the transformation occures only if the field is present in the incoming data.
   * **Is Array**: Needs to be selected when a field contains multiple values, and you intend to work with specific values.
   * **Read-Only**: Cannot be changed during transformation.
5. Add a **Processor definition**.
   Processor definitions are instructions that tell Dynatrace how to transform the data youâve selected in the matcher DQL query.
   It is created using [processing commands](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-commands "Explore scenarios of how to use log processing commands in Dynatrace powered by Grail."), [functions](/docs/analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-functions "Explore scenarios of how to use log processing functions in Dynatrace powered by Grail.") and [pattern matching](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") (Dynatrace Pattern Language) that allows you to add, modify or remove incoming records.
6. In the **Rule testing** section, paste an event sample and run the test.

   Your incoming data example needs to be provided in the JSON format.
7. Select **Save changes**.

## Business events processing examples

In the below examples, you can see how ingest pipeline processing can be used to meet your technical and administrative requirements.

* Example 1. Add a new calculated field to the pipeline.  
  As a user, you need to add a calculated dollar trading volume value to the pipeline.

  ```
  {



  "action":"buy",



  "accountId":6,



  "amount":10,



  "instrumentId":1,



  "price":157.025



  }
  ```

  + **Rule name**: Add field
  + **Matcher**: `matchesValue(action, "buy")`
  + **Transformation fields**:

  Name

  Type

  Optional

  is Array

  Read-only

  amount

  double

  false

  false

  true

  price

  double

  false

  false

  true

  + **Processor definition**: `FIELDS_ADD(trading_volume: price*amount)`
* Example 2. Mask your data.  
  You need to hide the CVV field on your credit card in an incoming JSON payload.

  ```
  {



  "action": "payment",



  "creditCardNumber":"5570001112223344",



  "valid":"12/27",



  "cvv":"001"



  }
  ```

  + **Rule name**: Mask field
  + **Matcher**: `matchesValue(action, "payment")`
  + **Transformation fields**:

  Name

  Type

  Optional

  is Array

  Read-only

  cvv

  string

  false

  false

  false

  + **Processor definition**: `FIELDS_ADD(cvv: SHA1(cvv))`
* Example 3. Drop event attribute.  
  You need to drop the birthdate field in an incoming JSON payload.

  ```
  {



  "action": "newUser",



  "firstName":"Frank",



  "lastName": "Underwud",



  "birthDate": "10.01.1967"



  }
  ```

  + **Rule name**: Drop field
  + **Matcher**: `matchesValue(action, "newUser")`
  + **Transformation fields**:

  Name

  Type

  Optional

  is Array

  Read-only

  birthDate

  string

  false

  false

  false

  + **Processor definition**: `FIELDS_REMOVE(birthDate)`
* Example 4. Parse nested JSON.  
  You need to parse attributes from a nested JSON in order to have them as top-level attributes in Grail.

  ```
  {



  "action":"sell",



  "details":{



  "accountId":6,



  "amount":10,



  "instrumentId":1,



  "price":157.025



  }



  }
  ```

  + **Rule name**: Parse field
  + **Matcher**: `matchesValue(action, "sell")`
  + **Transformation fields**:

  Name

  Type

  Optional

  is Array

  Read-only

  details

  string

  false

  false

  false

  + **Processor definition**: `PARSE(details,"JSON{INTEGER:accountId,INTEGER:amount,INTEGER:instrumentId,DOUBLE:price}(flat=true)") | FIELDS_REMOVE(details)`
* Example 5. Parse error message.

  In this example, you need to remove the voucher code from the error message field below to have the ability to count how often the same error message appears. The solution below leverages the [Dynatrace Pattern language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") for parsing.

  ```
  {



  "timestamp":"2023-01-18T10:50:23.777000000Z",



  "cartId":"58583939",



  "error.message":"The voucher [XY-892940] is not valid!",



  "error.messageKey":"error.voucher "



  }
  ```

  + **Rule name**: Parse error message
  + **Matcher**: `matchesValue(error.messageKey, "error.voucher ")`
  + **Transformation fields**:

  Name

  Type;

  Optional

  is Array

  Read-only

  error.message

  string

  no

  no

  no

  + **Processor definition**:
    `FIELDS_ADD(final:REPLACE_PATTERN(error.message, "LD:p1 '[' LD:to_be_masked ']' LD:p2 ", "${p1}${p2}"))`
  + **Result**: `The voucher is not valid!`.