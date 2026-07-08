---
title: Web application configuration API - GET data privacy of all web applications
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/get-data-privacy-all-web-apps
---

# Web application configuration API - GET data privacy of all web applications

# Web application configuration API - GET data privacy of all web applications

* Reference
* Published Sep 03, 2019

Gets data privacy parameters of all web applications configured in your Dynatrace environment.

This API only supports web applications. For mobile and custom applications, see [Mobile and custom app API](/managed/dynatrace-api/configuration-api/rum/mobile-custom-app-configuration "Learn what the Dynatrace mobile and custom app config API offers.").

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/dataPrivacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/dataPrivacy` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApplicationDataPrivacyList](#openapi-definition-ApplicationDataPrivacyList) | Success |

### Response body objects

#### The `ApplicationDataPrivacyList` object

| Element | Type | Description |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| values | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy)[] | - |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description |
| --- | --- | --- |
| clusterVersion | string | Dynatrace version. |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. |

#### The `ApplicationDataPrivacy` object

Data privacy settings of the application.

| Element | Type | Description |
| --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Set to `true` to disable data capture and cookies until JavaScriptAPI `dtrum.enable()` is called. |
| doNotTrackBehaviour | string | How to handle the "Do Not Track" header:  * `IGNORE_DO_NOT_TRACK`: ignore the header and capture the data. * `CAPTURE_ANONYMIZED`: capture the data but do not tie it to the user. * `DO_NOT_CAPTURE`: respect the header and do not capture. The element can hold these values * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` |
| identifier | string | Dynatrace entity ID of the web application. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging |
| persistentCookieForUserTracking | boolean | Set to `true` to set persistent cookie in order to recognize returning devices. |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Data privacy settings for Session Replay. |

#### The `SessionReplayDataPrivacySettings` object

Data privacy settings for Session Replay.

| Element | Type | Description |
| --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Content masking settings for Session Replay.  For more details, see [Configure Session Replay﻿](https://dt-url.net/0m03slq) in Dynatrace Documentation. |
| optInModeEnabled | boolean | If `true`, session recording is disabled until JavaScriptAPI `dtrum.enableSessionReplay()` is called. |
| urlExclusionRules | string[] | A list of URLs to be excluded from recording. |

#### The `SessionReplayContentMaskingSettings` object

Content masking settings for Session Replay.

For more details, see [Configure Session Replay﻿](https://dt-url.net/0m03slq) in Dynatrace Documentation.

| Element | Type | Description |
| --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Configuration of the Session Replay masking. |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Configuration of the Session Replay masking. |
| recordingMaskingSettingsVersion | integer | The version of the content masking.  You can use this API only with the version 2.  If you're using version 1, set this field to `2` in the PUT request to switch to version 2. |

#### The `SessionReplayMaskingSetting` object

Configuration of the Session Replay masking.

| Element | Type | Description |
| --- | --- | --- |
| maskingPreset | string | The type of the masking:  * `MASK_ALL`: Mask all texts, user input, and images. * `MASK_USER_INPUT`: Mask all data that is provided through user input * `ALLOW_LIST`: Only elements, specified in **maskingRules** are shown, everything else is masked. * `BLOCK_LIST`: Elements, specified in **maskingRules** are masked, everything else is shown. The element can hold these values * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` |
| maskingRules | [MaskingRule](#openapi-definition-MaskingRule)[] | A list of masking rules. |

#### The `MaskingRule` object

The masking rule defining how data is hidden.

| Element | Type | Description |
| --- | --- | --- |
| maskingRuleType | string | The type of the masking rule. The element can hold these values * `ATTRIBUTE` * `ELEMENT` |
| selector | string | The selector for the element or the attribute to be masked.  Specify a CSS expression for an element or a [regular expression﻿](https://dt-url.net/k9e0iaq) for an attribute. |
| userInteractionHidden | boolean | Interactions with the element are (`true`) or are not (`false) masked. |

### Response body JSON models

```
{



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"values": [



{



"dataCaptureOptInEnabled": true,



"doNotTrackBehaviour": "CAPTURE_ANONYMIZED",



"identifier": "string",



"metadata": {},



"persistentCookieForUserTracking": true,



"sessionReplayDataPrivacy": {



"contentMaskingSettings": {



"playbackMaskingSettings": {



"maskingPreset": "ALLOW_LIST",



"maskingRules": [



{



"maskingRuleType": "ATTRIBUTE",



"selector": "string",



"userInteractionHidden": false



}



]



},



"recordingMaskingSettings": {},



"recordingMaskingSettingsVersion": 2



},



"optInModeEnabled": true,



"urlExclusionRules": [



"string"



]



}



}



]



}
```