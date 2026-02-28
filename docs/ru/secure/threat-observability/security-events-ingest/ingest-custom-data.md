---
title: Ingest custom security events via API
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-custom-data
scraped: 2026-02-28T21:19:19.069901
---

# Ingest custom security events via API

# Ingest custom security events via API

* Latest Dynatrace
* How-to guide
* Updated on Nov 06, 2025

This page has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

Ingest security events from custom third-party products via API.

## Get started

### Overview

In the following, you'll learn how to ingest external security events from custom third-party products into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data."), so you can get insights from Dynatrace for vulnerability findings from any source, provider, or format.

A **custom third-party product** is any product for which Dynatrace doesn't provide an out-of-the-box integration.

### Use cases

With the ingested data, you can accomplish various use cases, such as

* [Generate security events from the Dynatrace Investigations app via OpenPipelineï»¿](https://dt-url.net/r703qjx)
* [Ingest and process custom security findings](/docs/secure/use-cases/ingest-and-process-custom-security-findings "Continuously ingest your container scan findings.")
* [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.")
* [Visualize and analyze security findings](/docs/secure/use-cases/visualize-and-analyze-security-findings "Visualize, prioritize, and analyze ingested security findings.")

### Requirements

To query ingested data, you need the `storage:security.events:read` permission.

## Activation and setup

To start ingesting data, use one of the options below.

Built-in API endpoint

Custom API endpoint

For details on how to perform the API ingest, see [Learn moreï»¿](https://dt-url.net/1r03q9s).

## Details

### How it works

You ingest your data into Grail via our [built-in API endpoint](#default) or a [custom API endpoint](#custom). Then, depending on the ingest option chosen, you can either analyze data in your format or manually map data to the [Semantic Dictionary conventionsï»¿](https://dt-url.net/3q03pb0).

### Response codes

| Code | Description |
| --- | --- |
| 202 | Accepted |
| 400 | Bad request (in case of missing body or wrong format) |
| 401 | Unauthorized (in case of missing or invalid token) |

### Examples

Example JSON

```
[



{



"imageId": {



"imageDigest": "sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c"



},



"imageScanFindings": {



"findingSeverityCounts": {



"HIGH": 125,



"MEDIUM": 188,



"LOW": 30,



"UNDEFINED": 13,



"INFORMATIONAL": 353,



"CRITICAL": 6



},



"findings": [



{



"attributes": [



{ "key": "CVSS3_SCORE", "value": "9.8" },



{ "key": "package_version", "value": "4.19.269-1" },



{ "key": "package_name", "value": "linux" },



{



"key": "CVSS3_VECTOR",



"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"



}



],



"description": "An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.",



"name": "CVE-2023-45871",



"severity": "CRITICAL",



"uri": "https://security-tracker.debian.org/tracker/CVE-2023-45871 "



},



{



"attributes": [



{ "key": "CVSS3_SCORE", "value": "9.8" },



{ "key": "package_version", "value": "1:7.9p1-10+deb10u2" },



{ "key": "package_name", "value": "openssh" },



{



"key": "CVSS3_VECTOR",



"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"



}



],



"description": "The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.",



"name": "CVE-2023-38408",



"severity": "CRITICAL",



"uri": "https://security-tracker.debian.org/tracker/CVE-2023-38408 "



},



{



"attributes": [



{ "key": "CVSS3_SCORE", "value": "9.8" },



{ "key": "package_version", "value": "2.7.16-2+deb10u1" },



{ "key": "package_name", "value": "python2.7" },



{



"key": "CVSS3_VECTOR",



"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"



}



],



"description": "An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.",



"name": "CVE-2022-48565",



"severity": "CRITICAL",



"uri": "https://security-tracker.debian.org/tracker/CVE-2022-48565 "



},



{



"attributes": [



{ "key": "CVSS3_SCORE", "value": "9.8" },



{ "key": "package_version", "value": "2.7.16-2+deb10u1" },



{ "key": "package_name", "value": "python2.7" },



{



"key": "CVSS3_VECTOR",



"value": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"



},



{ "key": "CVSS2_VECTOR", "value": "AV:N/AC:L/Au:N/C:P/I:P/A:P" },



{ "key": "CVSS2_SCORE", "value": "7.5" }



],



"description": "Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.",



"name": "CVE-2021-3177",



"severity": "CRITICAL",



"uri": "https://security-tracker.debian.org/tracker/CVE-2021-3177 "



}



],



"imageScanCompletedAt": 1698376478,



"vulnerabilitySourceUpdatedAt": 1698343825



},



"imageScanStatus": {



"description": "The scan was completed successfully.",



"status": "COMPLETE"



},



"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",



"registryId": "123456789876",



"repositoryName": "unguard-frontend"



}



]
```

Example end result in Grail

Built-in API endpoint

Custom API endpoint

```
[



{



"timestamp": "2024-06-17T14:58:36.820000000+02:00",



"dt.ingest.source": "/platform/ingest/v1/security.events/",



"event.kind": "SECURITY_EVENT",



"imageId": "{\"imageDigest\":\"sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c\"}",



"imageScanFindings": "{\"findingSeverityCounts\":{\"HIGH\":125,\"MEDIUM\":188,\"LOW\":30,\"UNDEFINED\":13,\"INFORMATIONAL\":353,\"CRITICAL\":6},\"findings\":[{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"4.19.269-1\"},{\"key\":\"package_name\",\"value\":\"linux\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.\",\"name\":\"CVE-2023-45871\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-45871 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"1:7.9p1-10+deb10u2\"},{\"key\":\"package_name\",\"value\":\"openssh\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.\",\"name\":\"CVE-2023-38408\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-38408 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.\",\"name\":\"CVE-2022-48565\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2022-48565 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"},{\"key\":\"CVSS2_VECTOR\",\"value\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\"},{\"key\":\"CVSS2_SCORE\",\"value\":\"7.5\"}],\"description\":\"Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.\",\"name\":\"CVE-2021-3177\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2021-3177 \"}],\"imageScanCompletedAt\":1698376478,\"vulnerabilitySourceUpdatedAt\":1698343825}",



"imageScanStatus": "{\"description\":\"The scan was completed successfully.\",\"status\":\"COMPLETE\"}",



"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",



"registryId": "123456789876",



"repositoryName": "unguard-frontend"



}



]
```

```
{



"timestamp": "2024-06-17T14:58:36.820000000+02:00",



"dt.ingest.source": "/platform/ingest/v1/security.events/",



"imageId": "{\"imageDigest\":\"sha256:9282579f5330ae90d22f21b1a9be944f893895f06e3bc1985f14d1cfc084c60c\"}",



"imageScanFindings": "{\"findingSeverityCounts\":{\"HIGH\":125,\"MEDIUM\":188,\"LOW\":30,\"UNDEFINED\":13,\"INFORMATIONAL\":353,\"CRITICAL\":6},\"findings\":[{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"4.19.269-1\"},{\"key\":\"package_name\",\"value\":\"linux\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An issue was discovered in drivers/net/ethernet/intel/igb/igb_main.c in the IGB driver in the Linux kernel before 6.5.3. A buffer size may not be adequate for frames larger than the MTU.\",\"name\":\"CVE-2023-45871\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-45871 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"1:7.9p1-10+deb10u2\"},{\"key\":\"package_name\",\"value\":\"openssh\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"The PKCS#11 feature in ssh-agent in OpenSSH before 9.3p2 has an insufficiently trustworthy search path, leading to remote code execution if an agent is forwarded to an attacker-controlled system. (Code in /usr/lib is not necessarily safe for loading into ssh-agent.) NOTE: this issue exists because of an incomplete fix for CVE-2016-10009.\",\"name\":\"CVE-2023-38408\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2023-38408 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"}],\"description\":\"An XML External Entity (XXE) issue was discovered in Python through 3.9.1. The plistlib module no longer accepts entity declarations in XML plist files to avoid XML vulnerabilities.\",\"name\":\"CVE-2022-48565\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2022-48565 \"},{\"attributes\":[{\"key\":\"CVSS3_SCORE\",\"value\":\"9.8\"},{\"key\":\"package_version\",\"value\":\"2.7.16-2+deb10u1\"},{\"key\":\"package_name\",\"value\":\"python2.7\"},{\"key\":\"CVSS3_VECTOR\",\"value\":\"CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H\"},{\"key\":\"CVSS2_VECTOR\",\"value\":\"AV:N/AC:L/Au:N/C:P/I:P/A:P\"},{\"key\":\"CVSS2_SCORE\",\"value\":\"7.5\"}],\"description\":\"Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely.\",\"name\":\"CVE-2021-3177\",\"severity\":\"CRITICAL\",\"uri\":\"https://security-tracker.debian.org/tracker/CVE-2021-3177 \"}],\"imageScanCompletedAt\":1698376478,\"vulnerabilitySourceUpdatedAt\":1698343825}",



"imageScanStatus": "{\"description\":\"The scan was completed successfully.\",\"status\":\"COMPLETE\"}",



"nextToken": "ukD72mdD/mC8b5xV3susmJzzaTgp3hKwR9nRUW1yZZ63B5NL+m8CiI+qgoiLO0t5s6Oi9w2CQBANPaxpQTFWXxF/Sq7shr/h//oNXvOJ2XuWPSF3ox6DgxQztXUFyKzeGw+HpbYZAAxpHjJVELVXXnhpxAScZkKhVG85CbbUGfSPyuKcSeeHoNvQPGBdxCWD6CaKl4nFxtXyUeFRs3RV+mkX5FUxosMnBJepE2JbaoM9elE1niY2Rpq3BZrp/QeOyWdmjeuySi+2KZO03915df+6OMIfXtt3zclPZ+BGcdMgWoETrte2fkh2y1RDO3PI4OCohgCbjlTk9X6fYLWrrxwkhfWAIRekqToQq+S8BHEm1o82jxDoyKO0Et9UrZVIEFOofBkvenm5U+8XvgQ4V5kvMZZLa9DZykVDteq28OF+KCgjo7WHTbXMy1yh7jyRJ6A77N12YJfxYgv16JjkVgmDqGjlM3YJEH2o55SYTAnSsiBXiMvvq1RK1hl567SIstgGPMK3c0v7TGDnCE6o3EhP4FC73As6mj2q4uGkLf8eMQLi9ogBJ1UAzKCiCl3bxeTKuMz1W8hokdPauwuAd9uKg0vLdHmM6iftfrVhsgbbioNLy3R5jOon7X61YbIGF7fUOkaj72o37fpPd/JG2g==",



"registryId": "123456789876",



"repositoryName": "unguard-frontend"



}
```



### Licensing and cost

For billing information, see [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

## Related topics

* [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Security events](/docs/semantic-dictionary/model/security-events "Get to know the Semantic Dictionary models related to security events.")
* [OpenPipeline Ingest API - POST Custom security event endpoint (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.")
* [OpenPipeline Ingest API - POST Built-in security events (new)](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/security-events-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.")