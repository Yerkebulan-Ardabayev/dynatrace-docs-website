---
title: JSON log processing with unescaped nested JSON strings
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-pre-processing/lma-pre-processing-json
scraped: 2026-02-24T21:36:04.399379
---

# JSON log processing with unescaped nested JSON strings

# JSON log processing with unescaped nested JSON strings

* Latest Dynatrace
* Explanation
* 2-min read
* Published Feb 02, 2026

JSON log pre-processing detects escape characters in JSON strings and converts them into structured JSON objects for further processing and deeper analysis. You can then query the unescaped JSON field using the [jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.") and [jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.") DQL functions for precise extraction and filtering log attributes.

## Benefits

JSON log pre-processing benefits:

* Simplified querying and visualizations of nested JSON logs.
* Automated processing of escaped JSON strings.
* No need for parsing of escaped JSON strings.

## Configuration notes

* Dynatrace SaaS version 1.331+ JSON log pre-processing is enabled by default. You can't disable or customize it, and you can use it only for new environments.
* Dynatrace SaaS version 1.330 or earlier JSON log pre-processing is not available.

## Unescaping nested JSON strings

Many log forwarders wrap the original log message as JSON strings within the `content` field with escape characters.

JSON log pre-processing performs the following steps.

1. Detects and unescapes escape characters in the JSON string.
2. Converts the JSON strings into structured JSON objects. The conversion happens during log pre-processing, making results available for further processing in custom pipelines.

   Before log pre-processing example

   ```
   {



   "content": {



   "loglevel": "ERROR",



   "event": "{\\\"type\\\":\\\"db_error\\\",\\\"code\\\":\\\"CONN_FAIL\\\"}"



   },



   "source": "fluentbit",



   "host.name": "app-server-01"



   }
   ```

   After log pre-processing example

   ```
   {



   "content": {



   "loglevel": "ERROR",



   "event": {



   "type": "db_error",



   "code": "CONN_FAIL"



   }



   },



   "source": "fluentbit",



   "host.name": "app-server-01"



   }
   ```

## Query unescaped JSON using DQL

You can query the unescaped JSON field for precise extraction and filtering log attributes using the following DQL functions.

* [jsonField](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonField "A list of DQL string functions.") function for extracting the value by its actual name.

  This is an example of extracting `loglevel` using `jsonField`.

  ```
  fetch logs



  | fieldsAdd logLevel = jsonField(content, "loglevel")



  | filter logLevel == "ERROR"
  ```
* [jsonPath](/docs/platform/grail/dynatrace-query-language/functions/string-functions#jsonPath "A list of DQL string functions.") function for extracting value by a `JSONPath` expression.

  This is an example of extracting `eventType` using `jsonPath`.

  ```
  fetch logs



  | fieldsAdd eventType = jsonPath(content, "$.event.type")



  | filter eventType == "db_error"
  ```

Invalid JSON

Unescapingâfor example, removing a forward slashâis skipped when the JSON is invalid. The original content stays.

## Related topics

* [Log processing with OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.")