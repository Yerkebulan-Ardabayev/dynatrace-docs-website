---
title: Settings API - Session replay data privacy schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-sessionreplay-web-privacy-preferences
---

# Settings API - Session replay data privacy schema table

# Settings API - Session replay data privacy schema table

* Published Dec 05, 2023

### Session replay data privacy (`builtin:sessionreplay.web.privacy-preferences)`

[Configure Session Replay﻿](https://dt-url.net/2i3t0pju) to restrict data capture and protect your end users' data privacy.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:sessionreplay.web.privacy-preferences` | * `group:preferences` * `group:rum-settings` * `group:privacy-settings` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:sessionreplay.web.privacy-preferences` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable opt-in mode for Session Replay `enableOptInMode` | boolean | When [Session Replay opt-in mode﻿](https://dt-url.net/sr-opt-in-mode) is turned on, Session Replay is deactivated until explicitly activated via an API call. | Required |
| URL exclusion `urlExclusionPatternList` | set | Exclude webpages or views from Session Replay recording by adding [URL exclusion rules﻿](https://dt-url.net/sr-url-exclusion) | Required |
| Content masking preferences `maskingPresets` | [MaskingPresetConfig](#MaskingPresetConfig) | To protect your end users' privacy, select or customize [predefined masking options﻿](https://dt-url.net/sr-masking-preset-options) that suit your content recording and playback requirements. | Required |

##### The `MaskingPresetConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Recording masking settings `recordingMaskingPreset` | enum | Recording masking settings are applied at record time. When you set these settings to a more restrictive option, the same option is also enabled for the playback masking settings. The element has these enums * `MASK_ALL` * `MASK_USER_INPUT` * `ALLOW_LIST` * `BLOCK_LIST` | Required |
| Allow list rules `recordingMaskingAllowListRules` | Set<[AllowListRule](#AllowListRule)> | The elements are defined by the CSS selector or attribute name. | Required |
| Block list rules `recordingMaskingBlockListRules` | Set<[BlockListRule](#BlockListRule)> | The elements are defined by the CSS selector or attribute name. | Required |
| Playback masking settings `playbackMaskingPreset` | enum | Playback masking settings are applied during playback of recorded sessions, including playback of sessions that were recorded before these settings were applied. The element has these enums * `MASK_ALL` * `MASK_USER_INPUT` * `ALLOW_LIST` * `BLOCK_LIST` | Required |
| Allow list rules `playbackMaskingAllowListRules` | Set<[AllowListRule](#AllowListRule)> | The elements are defined by the CSS selector or attribute name. | Required |
| Block list rules `playbackMaskingBlockListRules` | Set<[BlockListRule](#BlockListRule)> | The elements are defined by the CSS selector or attribute name. | Required |

##### The `AllowListRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Target `target` | enum | Choose the masking rule target type The element has these enums * `ELEMENT` * `ATTRIBUTE` | Required |
| CSS selector to identify the content element `cssExpression` | text | Content masking can be applied to webpages where personal data is displayed. When content masking is applied to parent elements, all child elements are masked by default. | Required |
| Attribute name (expression) `attributeExpression` | text | Attribute masking can be applied to web applications that store data within attributes, typically data-NAME attributes in HTML5. When you define attributes, their values are masked while recording but not removed. | Required |

##### The `BlockListRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Target `target` | enum | Choose the masking rule target type The element has these enums * `ELEMENT` * `ATTRIBUTE` | Required |
| CSS selector to identify the content element `cssExpression` | text | Content masking can be applied to webpages where personal data is displayed. When content masking is applied to parent elements, all child elements are masked by default. | Required |
| Attribute name (expression) `attributeExpression` | text | Attribute masking can be applied to web applications that store data within attributes, typically data-NAME attributes in HTML5. When you define attributes, their values are masked while recording but not removed. | Required |
| Hide user interaction `hideUserInteraction` | boolean | Hide user interactions with these elements, including clicks that expand elements, highlighting that results from hovering a cursor over an option, and selection of specific form options. | Required |