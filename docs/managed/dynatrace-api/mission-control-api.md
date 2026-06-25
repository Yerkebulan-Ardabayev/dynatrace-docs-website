---
title: Mission Control API
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api
scraped: 2026-05-12T12:07:23.732507
---

# Mission Control API

# Mission Control API

* Published Mar 12, 2021

To get authenticated to use the Mission Control API, you need a valid `OAuth REST API client` token. Access to the API is controlled by scope, meaning that you also need the proper permissions assigned to the token. See the description below to find out which permissions are required to use it.

1. Register a client ([Generate SSO client credentials](/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials "Generate Mission Control API OAuth API client.")).

   Register client credentials

   Execute the following REST call:

   ```
   curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/registration/withLicenseKey"



   -H "accept: application/json"



   -u "<cluster-identifier>:<license-key>"
   ```

   where:

   * `<cluster-identifier>` is a cluster identifier (in Dynatrace, go to **Licensing**). For example, `0a00a0a0-92ec-11e7-b1e6-12fbd1fb3732`
   * `<license-key>` is a license key provided to you in welcome email and visible in **Licensing**. For example, `0a0aAAAA0jeUv6N`.

   As a result, you should receive a JSON response containing `clientId` and `clientSecret` and the response code `200`. For example:

   ```
   {



   "clientId": "dt0s04.AAAAAAAA",



   "clientSecret": "dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL",



   "scopes": [



   "sso20-managed-cluster-offline-bundle",



   "sso20-identity-linking"



   ]



   }
   ```

   ```
   200
   ```
2. Generate a token ([Generate SSO token](/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token "Generate a Mission Control API token that allows you to execute update package download URLs.")).  
   Currently, only the `sso20-managed-cluster-offline-bundle` scope, which allows to generate update package download URLs is supported.

   Generate token

   Using the `clientId` and `clientSecret` from the previous call, execute the following REST call:

   ```
   curl -X POST "https://mcsvc.dynatrace.com/rest/public/v1.0/oauth/api-token" \



   -H "accept: application/json" \



   -H "Content-Type: application/json" \



   -d "{ \"clientId\": \"dt0s04.AAAAAAAA\", \"clientSecret\": \"dt0s04.AAAAAAAA.AAAA00AAAAAAAAAA0OBA6AVNCQVQAGSO25VM5KDFBIKEZ7HVG6THKTHGWAY5ACCL\", \"scope\": \"sso20-managed-cluster-offline-bundle\"}"
   ```

   As a result you will receive a JSON response with a token, associated scopes and the token expiration date. For example:

   ```
   {



   "token": "aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA",



   "scopes": [



   "sso20-managed-cluster-offline-bundle"



   ],



   "expiresAt": 1615477153001



   }
   ```

   ```
   200
   ```
3. Authenticate in your API calls.

   Your API call can get authenticated per call via an HTTP header authorization. You can authenticate by attaching the token to the authorization HTTP header preceding the `Bearer` realm.

   Authentication example

   ```
   curl -X GET "https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle/published"



   -H "accept: application/json"



   -H "Authorization: Bearer aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA"
   ```

   Unless otherwise specified, the following response codes are used:

   * `200` - OK. The request is successful.
   * `400` - Bad request. The request has failed. The body of the response provides additional details.
   * `401` - Unauthorized. The token authentication has failed. Check to see if your token has the required permissions.
   * `404` - Not found. The requested resource is not found. Check if your input is correct.
   * `429` - Too many requests. Mission Control is currently busy, try again later.

### Mission Control client registration

[Generate SSO client credentials](/managed/dynatrace-api/mission-control-api/cluster-sso-client-registration/post-generate-sso-client-credentials "Generate Mission Control API OAuth API client.")

### Offline Bundle packages

[Get a list of available packages and updates](/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-available-packages-updates "Get a list of available deployment packaged and updates via Mission Control API.")

[Get offline bundle](/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-offline-package-update-bundle "Gets specific deployment package and update as an Offline Bundle via Mission Control API.")

### Mission Control token generation

[Generate SSO token](/managed/dynatrace-api/mission-control-api/cluster-sso-token-generation/post-generate-sso-token "Generate a Mission Control API token that allows you to execute update package download URLs.")