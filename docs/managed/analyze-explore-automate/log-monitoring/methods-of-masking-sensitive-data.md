---
title: Methods of masking sensitive data (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/methods-of-masking-sensitive-data
scraped: 2026-05-12T11:53:54.856378
---

# Methods of masking sensitive data (Logs Classic)

# Methods of masking sensitive data (Logs Classic)

* 4-min read
* Updated on Feb 26, 2026

Log Monitoring Classic

Your logs may contain sensitive data that requires masking before you can use it for analytics, observability, security, and other purposes. Dynatrace provides you with tools that enable you to meet your data protection and other compliance requirements while still getting value from your logs.

Choose one or both methods, based on your information architecture and log setup:

* **Masking at capture**  
  This approach allows masking sensitive data in your environment, hosts or processes before it is transferred to the Dynatrace SaaS environment, using OneAgent.
* **Masking at ingest**  
  This approach allows masking sensitive data once it arrives in the Dynatrace SaaS environment, and before it is written to disk (stored).

We recommend that you combine masking data at the capture with masking data at the ingest, to set up two layers of security.

## Mask your logs at capture

At-capture masking requires identifying and masking sensitive parts of your log records before data is transferred to Dynatrace. To achieve this, you can choose OneAgent to collect your logs.
OneAgent has a built-in mechanism for sensitive data masking that can be granularly configured on the host, host group, or environment level. Use at-capture masking with OneAgent to:

* Make sure your sensitive data never leaves your environment.
* Avoid using multiple tools.
* Simplify configuration.

To mask your data this way, follow the steps described in [Sensitive data masking (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking "Mask sensitive information in your log data using Log Monitoring Classic.").

Mask before sending logs to generic ingest API

If you send logs to the Dynatrace generic ingest API and need to mask sensitive data at capture, you need to either:

* Mask your data by configuring a log producer
* Or set up a log shipper or forwarder that masks sensitive data before it is sent to Dynatrace (in your environment)

## Mask your logs at ingest

With this method, you can mask the data once it reaches Dynatrace, by setting log processing rules. After data is processed, it is sent to storage and is available for further analysis. The key advantage of this method is the fact that it allows data flow from all log ingest channels, including:

* OneAgent
* Generic ingest API
* Dynatrace Extensions

To mask sensitive data in Dynatrace with this method, you need to create a processing rule specific to the attributes that you would like to mask, see [Log Monitoring Classic](/managed/analyze-explore-automate/log-monitoring/log-processing#lprules "Create log processing rules that reshape your incoming log data for better analysis or further processing.").
For example, if you need to mask your IP address, you can set the processing rules as shown in the example below.

### Example: Mask any attribute

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

## Related topics

* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Sensitive data masking (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking "Mask sensitive information in your log data using Log Monitoring Classic.")