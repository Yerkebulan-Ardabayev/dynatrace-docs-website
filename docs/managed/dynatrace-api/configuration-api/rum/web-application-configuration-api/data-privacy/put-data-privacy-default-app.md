---
title: Web application configuration API - PUT data privacy of the default application
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api/data-privacy/put-data-privacy-default-app
scraped: 2026-05-12T11:16:46.070294
---

# Web application configuration API - PUT data privacy of the default application

# Web application configuration API - PUT data privacy of the default application

* Reference
* Published Sep 03, 2019

Updates the data privacy parameters of the default web application of your Dynatrace environment.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy` |

## Authentication

To execute this request, you need an access token with `DataPrivacy` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ApplicationDataPrivacy](#openapi-definition-ApplicationDataPrivacy) | JSON body of the request, containing new data privacy settings. | body | Optional |

### Request body objects

#### The `ApplicationDataPrivacy` object

Data privacy settings of the application.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dataCaptureOptInEnabled | boolean | Set to `true` to disable data capture and cookies until JavaScriptAPI `dtrum.enable()` is called. | Required |
| doNotTrackBehaviour | string | How to handle the "Do Not Track" header:  * `IGNORE_DO_NOT_TRACK`: ignore the header and capture the data. * `CAPTURE_ANONYMIZED`: capture the data but do not tie it to the user. * `DO_NOT_CAPTURE`: respect the header and do not capture. The element can hold these values * `CAPTURE_ANONYMIZED` * `DO_NOT_CAPTURE` * `IGNORE_DO_NOT_TRACK` | Required |
| identifier | string | Dynatrace entity ID of the web application. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Metadata useful for debugging | Optional |
| persistentCookieForUserTracking | boolean | Set to `true` to set persistent cookie in order to recognize returning devices. | Required |
| sessionReplayDataPrivacy | [SessionReplayDataPrivacySettings](#openapi-definition-SessionReplayDataPrivacySettings) | Data privacy settings for Session Replay. | Optional |

#### The `ConfigurationMetadata` object

Metadata useful for debugging

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterVersion | string | Dynatrace version. | Optional |
| configurationVersions | integer[] | A sorted list of the version numbers of the configuration. | Optional |
| currentConfigurationVersions | string[] | A sorted list of version numbers of the configuration. | Optional |

#### The `SessionReplayDataPrivacySettings` object

Data privacy settings for Session Replay.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| contentMaskingSettings | [SessionReplayContentMaskingSettings](#openapi-definition-SessionReplayContentMaskingSettings) | Content masking settings for Session Replay.  For more details, see [Configure Session Replayï»¿](https://dt-url.net/0m03slq) in Dynatrace Documentation. | Optional |
| optInModeEnabled | boolean | If `true`, session recording is disabled until JavaScriptAPI `dtrum.enableSessionReplay()` is called. | Optional |
| urlExclusionRules | string[] | A list of URLs to be excluded from recording. | Optional |

#### The `SessionReplayContentMaskingSettings` object

Content masking settings for Session Replay.

For more details, see [Configure Session Replayï»¿](https://dt-url.net/0m03slq) in Dynatrace Documentation.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| playbackMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Configuration of the Session Replay masking. | Optional |
| recordingMaskingSettings | [SessionReplayMaskingSetting](#openapi-definition-SessionReplayMaskingSetting) | Configuration of the Session Replay masking. | Optional |
| recordingMaskingSettingsVersion | integer | The version of the content masking.  You can use this API only with the version 2.  If you're using version 1, set this field to `2` in the PUT request to switch to version 2. | Required |

#### The `SessionReplayMaskingSetting` object

Configuration of the Session Replay masking.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| maskingPreset | string | The type of the masking:  * `MASK_ALL`: Mask all texts, user input, and images. * `MASK_USER_INPUT`: Mask all data that is provided through user input * `ALLOW_LIST`: Only elements, specified in **maskingRules** are shown, everything else is masked. * `BLOCK_LIST`: Elements, specified in **maskingRules** are masked, everything else is shown. The element can hold these values * `ALLOW_LIST` * `BLOCK_LIST` * `MASK_ALL` * `MASK_USER_INPUT` | Required |
| maskingRules | [MaskingRule[]](#openapi-definition-MaskingRule) | A list of masking rules. | Optional |

#### The `MaskingRule` object

The masking rule defining how data is hidden.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| maskingRuleType | string | The type of the masking rule. The element can hold these values * `ATTRIBUTE` * `ELEMENT` | Required |
| selector | string | The selector for the element or the attribute to be masked.  Specify a CSS expression for an element or a [regular expressionï»¿](https://dt-url.net/k9e0iaq) for an attribute. | Required |
| userInteractionHidden | boolean | Interactions with the element are (`true`) or are not (`false) masked. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"dataCaptureOptInEnabled": true,



"doNotTrackBehaviour": "CAPTURE_ANONYMIZED",



"identifier": "string",



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
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Data privacy settings have been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/applications/web/default/dataPrivacy/validator` |

### Authentication

To execute this request, you need an access token with `DataPrivacy` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response does not have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```