---
title: DQL use cases
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-use-cases
scraped: 2026-03-01T21:24:33.184551
---

# DQL use cases

# DQL use cases

* Latest Dynatrace
* Reference
* Published Jan 16, 2023

The following use cases show some of the ways you can use Dynatrace Query Language to leverage data ingested into Grail.

### Parse JSON data and aggregate records

In this use case, let's assume that you need to check how many transactions were conducted by each payment service provider, and the share of each provider in the total number of transactions.

The content field for every record looks as below:

```
{



"country_code":"US",



"session_id":"6a6c6b6d6a7c7b7f7a7c7b7a7f7",



"invoicing_data":null,



"bill_to":{



"first_name":"John",



"last_name":"Doe",



"email":"john.doe@gmail.com",



"phone":null



},



"payment_provider":"paypal"



}
```

You can use the `parse` command in combination with the [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.") for parsing JSON objects. The query parses the `payment_provider` field from the JSON data and groups the number of transactions by each provider using the `summarize` command, as well as calculates the total count of transactions. The share is calculated in a separate column, next to each provider's number of transactions.

```
fetch logs



| parse content, "JSON:json"



| fields payment = json[payment_provider]



| summarize



bank_card=countIf(payment=="bank_card"), bank_cardPer=toDouble(countIf(payment=="bank_card"))/toDouble(count()),



apple_pay=countIf(payment=="apple_pay"),apple_payPerc=toDouble(countIf(payment=="apple_pay"))/toDouble(count()),



paypal=countIf(payment=="paypal"),paypalPerc=toDouble(countIf(payment=="paypal"))/toDouble(count()),



google_pay=countIf(payment=="google_pay"),google_payPerc=toDouble(countIf(payment=="google_pay"))/toDouble(count()),



unpaid_booking=countIf(payment=="unpaid_booking"),unpaid_bookingPerc=toDouble(countIf(payment=="unpaid_booking"))/toDouble(count()),



total=count()
```

Results:

### Extract the first 'n' characters from the field.

In this example, you have a field called `kiosk` and need to extract the first three characters to identify the location abbreviation of the kiosk.

```
{



"kiosk": "LAOBAUA729"



}
```

```
...



| parse kiosk, "DATA{3}:kioskLoc"



| fields kiosk, kioskLoc
```

Results:

### Extract information from an XML element

In this use case, an API gateway creates logs in XML format and you want to extract some information from it.

The XML field for every record looks as below:

```
<log-entry serial='1467' domain='bca_icas_soa'>



<date>Fri Sep 21 2023</date>



<time utc='1380295304719'>11:21:44</time>



<date-time>2012-09-21T11:21:44</date-time>



<type>xmlfirewall</type>



<class>xmlfirewall</class>



<object>example-Firewall</object>



<level num='3'>error</level>



<transaction-type>error</transaction-type>



<transaction>6187</transaction>



<client>127.0.0.1</client>



<code>0x01130007</code>



<file></file>



<message>Failed to establish backend connection</message>



</log-entry>
```

In the DQL query, you need to use the [DPL matcher](/docs/platform/grail/dynatrace-pattern-language/dpl-xml "Find out how to use XML matchers with DPL.") to extract the whole XML element:

```
...



| parse content, "XML(excludeRoot=true):xml"



| fields domain = xml[`@domain`],



serial = toLong(xml[`@serial`]),



object = xml[object],



transaction = xml[transaction],



code = xml[code]
```

Results:

### Investigate security incidents in Kubernetes clusters Threat hunting

Application Security

In this use case, you perform queries using [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") to analyze unauthorized requests in your Kubernetes audit logs. Follow different investigation paths, navigate between executed queries, and get a detailed overview of your results in the original format.

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL compared to SQL and more](/docs/platform/grail/dynatrace-query-language/dql-comparison "See how DQL compares to other query languages.")
* [DQL language reference](/docs/platform/grail/dynatrace-query-language/dql-reference "Dynatrace Query Language syntax reference.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")