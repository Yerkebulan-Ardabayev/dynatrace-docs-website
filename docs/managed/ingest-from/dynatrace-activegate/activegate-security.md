---
title: ActiveGate security
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-security
scraped: 2026-05-12T12:05:30.331384
---

# ActiveGate security

# ActiveGate security

* 8-min read
* Published Jul 08, 2022

## Custom certificate for ActiveGate

We recommend using custom certificates for ActiveGates to increase security.

See [Custom SSL certificate for ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

## Tokens

Ensure ActiveGate tokens are enforced in your environment. To do so, [check the status of your ActiveGate token usage](#determine-status-of-active-gate-token-usage) and take action based on the outcome.

### Migrate to ActiveGate tokens

To migrate to ActiveGate token-based security, start by determining the status of your ActiveGate token usage.

#### Determine the status of you ActiveGate token usage

1. In Dynatrace, go to **Settings** > **Preferences** > **Network security**.
2. Review the messages displayed on the **Network security** page and address any issues as described below.

##### No action required

If Dynatrace displays a message like this:

![ActiveGate tokens enforced](https://dt-cdn.net/images/updated-ss-1-582-2d81cc06ad.png)

ActiveGate tokens enforced

* No action is required. ActiveGate enforcement is on and you're all set.
* Only ActiveGates with valid ActiveGate tokens can connect to Dynatrace.

##### Fix ActiveGate token issues

If Dynatrace displays a message like this:

![ActiveGate token issues](https://dt-cdn.net/images/updated-ss-2-584-c069a85f68.png)

ActiveGate token issues

* ActiveGate tokens are not yet enforced and some of your ActiveGates use invalid tokens.
* You need to address the issues based on the [status](#statuses). Otherwise, such ActiveGates will lose connectivity after ActiveGate tokens are enforced.

##### Enforce ActiveGate tokens immediately

If Dynatrace displays a message like this:

![Manual ActiveGate token enforcement](https://dt-cdn.net/images/manual-enforcement-580-5c1b3dbaf4.webp)

Manual ActiveGate token enforcement

* You have the option to enforce ActiveGate tokens immediately. You can do so at any time, regardless of whether your ActiveGates report token issues, but be sure to read [Manual ActiveGate token enforcement](#manual) below first. All ActiveGates with a status other than **Valid** will lose their connection to Dynatrace.

### ActiveGate token types

ActiveGate tokens come in two types:

* **Seed token**âAn ActiveGate seed token is automatically customized into the ActiveGate installer when you download the installer via the Dynatrace web UI or [Dynatrace API](/managed/dynatrace-api/environment-api/deployment/activegate "Download ActiveGate installers via Dynatrace API.").
* **Individual token**âDuring the first ActiveGate connection to the Dynatrace Cluster, the initial ActiveGate seed token is replaced with an automatically generated, individual ActiveGate token. The same installer can be used multiple times; the initial ActiveGate seed token is allowed to create multiple individual ActiveGate tokens.

### ActiveGate token structure

The format of an ActiveGate token consists of three parts separated by dots (`.`).

Example:

`dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E`

| Part | Name | Description |
| --- | --- | --- |
| 1 | **prefix** | The first part (`dt0g02` in the example above) is the token **prefix**. It identifies the token type. |
| 2 | **public** | The second part (`4KWZO5EF` in the example above) is the 8-character **public** portion of the token.  Together, the prefix and the public portion comprise the **token identifier**.  You can safely display the token identifier in the web UI and use it for logging purposes. |
| 3 | **secret** | The third part (`XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E` in the example above) is the 64-character **secret** portion of the token.  Treat the secret portion like a password. It shouldn't be displayed in Dynatrace (following initial creation) or stored in log files. |

### ActiveGate token enforcement

All your ActiveGates have already been gradually migrated to use ActiveGate tokens during the ActiveGate updates starting with ActiveGate version 1.225.

To check which of your ActiveGates have ActiveGate tokens enabled:

1. In Dynatrace, go to **Deployment Status** and select **ActiveGates**.
2. You can filter your ActiveGates by the following ActiveGate token statuses, see [ActiveGate token status](#statuses) for more information.

   * Absent
   * Expiring
   * Invalid
   * Unknown
   * Valid
   * Unsupported

#### Automatic ActiveGate token enforcement

If all of your ActiveGates are ready for token-based network security for 30 days, your environment will automatically switch to ActiveGate token-based network security.

#### Manual ActiveGate token enforcement

If you want to speed up the process and you are sure that there are only ActiveGates version 1.225+ in your environment, you can force the switch to ActiveGate tokens whenever you're ready.

1. In Dynatrace, go to **Settings** > **Preferences** > **Network security**.
2. Turn on **Manually enforce ActiveGate token authentication**.

* When you turn on **Manually enforce ActiveGate token authentication** and save your changes, all ActiveGates with a status other than **Valid** will lose their connection to Dynatrace.
* You have a maximum of 30 days after the last invalid token was detected to withdraw from manual enforcement (to turn off **Manually enforce ActiveGate token authentication**). For example, if the last invalid token was detected 20 days earlier, you still have 10 days to withdraw from enforcement. After the transitional period is over, the switch is disabled (so you can't turn it off).

#### Transitional period

The transitional period of 30 days is designed to prevent data loss from ActiveGates where new tokens are not implemented in your environment.

During that period, if any attempt to connect without an ActiveGate token is detected:

* ActiveGate token enforcement won't be switched on and all ActiveGates will be allowed to connect to the Dynatrace cluster (only tenant tokens will be required).
* The transitional period is reset to 30 daysâActiveGate token enforcement will be switched on automatically no sooner than 30 days from that point.

### ActiveGate token status

If your ActiveGates don't use valid ActiveGate tokens, you can check to learn why the tokens are invalid.

1. In Dynatrace, go to **Deployment Status** and select **ActiveGates**.
2. Select **Check ActiveGate token statuses**.

   This option is only available if there are problems with the ActiveGate tokens.

Depending on the status, you may be required to perform some actions to transition to ActiveGate token-based network security.

#### Absent

The ActiveGate version supports ActiveGate tokens, but it's still using the tenant token for communication. [Generate and configure](#generate) a new ActiveGate token.

#### Expiring

The ActiveGate token is set to expire in 30 or fewer days. If your environment has ActiveGate tokens enforced, your ActiveGate will lose its connection after the token expires.

#### Invalid

The ActiveGate is configured to use an ActiveGate token, but the format is invalid. [Generate and configure](#generate) a new ActiveGate token.

#### Unknown

The ActiveGate is configured to use an ActiveGate token and the token format is valid, but the token isn't recognized by the Dynatrace Cluster. [Generate and configure](#generate) a new ActiveGate token.

#### Valid

The ActiveGate is using a valid ActiveGate token to authenticate.

#### Unsupported

The ActiveGate is version 1.223 or earlier; ActiveGate token-based network security is supported for ActiveGate version 1.225+.

### Generate and configure ActiveGate token

* If your ActiveGate is deployed as a [StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet."), you need to [generate an ActiveGate token](#generate-individual) and add it to your configuration.

  + An ActiveGate seed token can't be used for containerized ActiveGates.
  + An ActiveGate token can be shared among ActiveGates within the same environment.
* If your ActiveGate is deployed by using [Dynatrace Operator](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), Dynatrace Operator handles the authorization token. Starting with Dynatrace Operator version 0.9.0+, you must enable the **Create ActiveGate tokens** (`activeGateTokenManagement.create`) scope. For details, see [Access tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

  For issues with your ActiveGate token, see [Problem with ActiveGate tokenï»¿](https://dt-url.net/ym238od) in Dynatrace Community.
* All host-based ActiveGates installed via the Dynatrace web UI or Dynatrace API already have an automatically generated ActiveGate token. However, you may sometimes need to [generate an ActiveGate token](#generate-individual) and [configure it in the `authorization.properties` file](#configure-hostbased).

#### Generate ActiveGate token

1. [Generate an API token](/managed/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API."). Select one of the following token scopes to limit access for security reasons:

   * **Create ActiveGate tokens**
   * **Write ActiveGate tokens**
2. Save the token.

   It's displayed only once.
3. Use the [ActiveGate tokens API - POST a token](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.") endpoint to create the token. Authorize your call with the API token you just created. For example, the following command will generate an ActiveGate token with the following parameters:

   * ActiveGate type: `ENVIRONMENT`
   * ActiveGate token expires in: `6 months`
   * ActiveGate token type: individual ActiveGate token (`seedToken` is false).

   Starting with Dynatrace version 1.293+, you must ensure that the **expirationDate** field is not set in the past and does not exceed **two years** from the moment of creation.

   **Command:**

   ```
   curl -X POST "https://{your-environment-id}.live.dynatrace.com/api/v2/activeGateTokens" \



   -H 'Authorization: Api-Token {api-token}' \



   -H 'Accept: application/json; charset=utf-8' \



   -H 'Content-Type: application/json; charset=utf-8' \



   -d '{



   "name": "myToken",



   "expirationDate": "now+6M",



   "seedToken": false,



   "activeGateType": "ENVIRONMENT"



   }'
   ```

   Replace:

   * `{your-environment-id}` with your [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
   * `{api-token}` with an [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") set to one of the following scopes: **Create ActiveGate tokens** or **Write ActiveGate tokens**.

   **Response body example:**

   ```
   {



   "id": "dt0g02.4KWZO5EF",



   "token": "dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E",



   "expirationDate": "2020-11-24T08:15:30.144Z"



   }
   ```

#### Configure token on host-based ActiveGate

1. In the ActiveGate [configuration directory](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), locate the `authorization.properties` file.
2. Edit the file to add the ActiveGate token you generated as the value of the `authToken` property. For example:

   ```
   authToken = dt0g02.4KWZO5EF.XT47R5DRADJIZUFOX4UDNOKTSUSABGLN7XSMJG7UXHRXKNY4WLORH4OF4T75MG7E     # present, if required
   ```
3. [Restart the ActiveGate main service](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.")

### ActiveGate token expiry notifications

Besides setting up your internal mechanism for rotating ActiveGate tokens before their expiration date, you can set up notifications about expiring ActiveGate tokens. To do so, create a problem notification integration (for example, [Email](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.")) using the built-in **Default for ActiveGate Token Expiry** alerting profile.

For Dynatrace Managed, [emergency contacts](/managed/managed-cluster/configuration/configure-emergency-contacts-managed "Learn how to configure emergency contacts in Dynatrace Managed.") also receive token expiry notifications.

To stop notifications

1. In Dynatrace, go to **Deployment Status** > **ActiveGates**.
2. Select **More** (**â¦**), then select **ActiveGate token enforcement settings**.
3. Turn off **Enable notifications about ActiveGate tokens expiration dates**.
4. Select **Save changes**.

### Automatic ActiveGate token cleanup

Dynatrace version 1.272+

Dynatrace performs an automatic cleanup of unused ActiveGate tokens. The token is considered unused after two years from the last usage. You can check your tokens via the [GET all tokens](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/get-all-activegate-tokens "List all ActiveGate tokens available for your monitoring environment via Dynatrace API.") request of the Tokens APIâlook for the **lastUsedDate** field.

Sample API payload

```
{



"activeGateTokens": [



{



"id": "dt0g02.abc123",



"name": "system:installer",



"owner": "max.mustermann@company.com",



"creationDate": "2021-11-22T11:39:29.797Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.321cba",



"name": "system:installer",



"owner": "john.smith@company.com",



"creationDate": "2021-11-30T14:11:40.913Z",



"seedToken": true,



"activeGateType": "ENVIRONMENT"



},



{



"id": "dt0g02.123abc",



"name": "system:initial-setup",



"owner": "mary.brown@company.com",



"creationDate": "2021-10-22T13:48:00.135Z",



"expirationDate": "2021-12-02T11:52:17.201Z",



"lastUsedDate": "2020-11-24T08:15:30.144Z",



"seedToken": false,



"activeGateType": "ENVIRONMENT"



}



],



"nextPageKey": "AAAAAAAAAAAAAABOAAAAAAAAAAAAAAA6ACQAEAAAABgACgAITFdXQk1BRzYAAAhtZXRhZGF0YQB___-bf___m3iIYxfF7xVQvY72rwblQkcAAwAAAAAAAADHAAAAZA==",



"pageSize": 100,



"totalCount": 1000



}
```