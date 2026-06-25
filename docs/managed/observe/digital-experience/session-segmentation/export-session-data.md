---
title: Export user sessions
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-segmentation/export-session-data
scraped: 2026-05-12T11:33:28.246047
---

# Export user sessions

# Export user sessions

* How-to guide
* 12-min read
* Updated on Sep 06, 2022

Dynatrace can continually send user session data to a provided webhook endpoint.

To start getting user session data, you need to [set up your endpoint](#define-endpoint) and then [configure session export via the Dynatrace web UI](#configure-export-ui) or via the [Settings API](#configure-export-api).

Dynatrace sends the data on [completed user sessions](/managed/observe/digital-experience/rum-concepts/user-session#user-session-end "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") in bulk to all defined endpoints, with a flush every few seconds to export the data as soon as the user session is marked as complete. The data transfer happens as soon as one of the following conditions is met:

* 1000 user sessions have finished
* The bulk size exceeds 896,000 bytes
* No user session has finished in the last 30 seconds

To prevent system overload, Dynatrace cancels the request when your endpoint doesn't respond within 30 seconds. Dynatrace retries three more times before it finally discards the request and sends an alert notification with the **Request timeout** error message.

## Define your endpoint

The server that provides the webhook needs to listen for `PUT` or `POST` requests on a URL specified as part of the session export configuration. Also, for security reasons, Dynatrace allows only HTTPS endpoints.

* **HTTP method**: `PUT` or `POST`
* **Path**: as configured
* **Content Type**: `application/json` or `application/x-ndjson`. When [sending to Elasticsearch](#send-to-elasticsearch), set to `application/x-ndjson`.
* **Response status code**: `200`

Sample code for Eclipse Jersey

The following sample code uses the open-source Jersey RESTful Web Services framework. You can use this code to set up the necessary endpoint for receiving the user session data.

```
@Path("/export/")



public class ExportREST {



...



@PUT



@Produces(MediaType.APPLICATION_JSON)



@Path("events")



public JResponse<String> jsonEvents(final String data) {



...



// split the bulk into single documents



final String[] lines = StringUtils.split(data, '\n');



for(String line : lines) {



...



// handle the JSON-data



}



return JResponse.ok("")



.header(HttpHeaders.SERVER, "Endpoint for Dynatrace session data export")



.build();



}



}
```

## Configure session export via Dynatrace web UI

To configure user session export via the Dynatrace web UI

1. Go to **Settings** > **Integration** > **User session exports**.
2. Select **Add item**.
3. Specify the **Endpoint URL**, and turn on **Enable user session export** if you're ready to start receiving the user session data.

   For security reasons, Dynatrace allows only HTTPS endpoints.
4. Set **Content type** to `application/json` or `application/x-ndjson`. When [sending session data to Elasticsearch](#send-to-elasticsearch), set it to `application/x-ndjson`.
5. Turn on **Use POST method (instead of PUT)** when [sending session data to Elasticsearch](#send-to-elasticsearch) or when your configured your endpoint to accept `POST` requests.
6. Optional [Configure the authentication](#authentication), [enable data transfer to Elasticsearch](#send-to-elasticsearch), or [set up the export scope, alerting, and advanced configuration](#export).

You can also [test user session export](#test-export) as well as [download a sample dataset](#download-sample-dataset) or a [sample mapping](#mapping).

You can configure up to three HTTPS endpoints.

### Configure authentication

Dynatrace can send user session data using either basic or OAuth 2.0 authentication. These types of authentication enable you to secure your endpoints.

When you activate the authentication for your session export configuration, [test the configuration](#test-export) before saving it.

For security reasons, you need to re-enter the basic authentication password or the OAuth 2.0 client secret when testing your session export configuration. You also need to re-enter the password or secret when you edit the existing session export configuration with enabled authentication.

#### Configure basic authentication

To configure user session export with basic authentication

1. On the **User session exports** page, expand the required endpoint URL.
2. Under **Authentication**, turn on **Activate**.
3. Set **Basic authentication** as the authentication type.
4. Enter your username and password.

The password is encrypted and masked in your environment.

#### Configure OAuth 2.0 authentication

To configure user session export with OAuth 2.0 client credentials authentication

1. On the **User session exports** page, expand the required endpoint URL.
2. Under **Authentication**, turn on **Activate**.
3. Set **OAuth 2.0** as the authentication type.
4. Enter your access token URL, client ID, client secret, and scope (optional).

The client secret is encrypted and masked in your environment.

Additional information on OAuth 2.0 authentication

[OAuth 2.0ï»¿](https://auth0.com/intro-to-iam/what-is-oauth-2/) offers various grant types, but Dynatrace supports only the client credentials grant type. For information on this grant type, see the following resources:

* [Client Credentials Flowï»¿](https://auth0.com/docs/get-started/authentication-and-authorization-flow/client-credentials-flow)
* [Call Your API Using the Client Credentials Flowï»¿](https://auth0.com/docs/get-started/authentication-and-authorization-flow/call-your-api-using-the-client-credentials-flow)
* [The OAuth 2.0 Authorization Framework | Client Credentials Grantï»¿](https://www.rfc-editor.org/rfc/rfc6749.html#section-4.4)

To send user session data using OAuth 2.0 authentication, you need to set up an OAuth2 Authorization Server that has an access token endpoint. Also, make sure that your **Endpoint URL** works with an access token.

The steps below describe how OAuth 2.0 authentication works for user session export.

1. Dynatrace makes a request to your Authorization Server to obtain an access token. Your **Access token URL**, **Client ID**, **Client secret**, and **Scope** (optional) are included in the request.

   ```
   curl --insecure -w "\nHTTP Status: %{http_code}\n" \



   --location --request POST 'https://[your-access-token-url]/oauth2/token' \



   --header 'Content-Type: application/x-www-form-urlencoded' \



   --header 'Accept: application/json' \



   --data-urlencode 'client_id=[your-client-id]' \



   --data-urlencode 'client_secret=[your-client-secret]' \



   --data-urlencode 'grant_type=client_credentials' \



   --data-urlencode 'scope=[your-scope]'
   ```
2. Your Authorization Server responds with an access token, for example:

   ```
   {



   "scope":"session-export-api",



   "token_type":"Bearer",



   "expires_in":300,



   "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2V4YW1wbGUuYXV0aDAuY29tLyIsImF1ZCI6Imh0dHBzOi8vYXBpLmV4YW1wbGUuY29tL2NhbGFuZGFyL3YxLyIsInN1YiI6InVzcl8xMjMiLCJpYXQiOjE0NTg3ODU3OTYsImV4cCI6MTQ1ODg3MjE5Nn0.CA7eaHjIHz5NxeIJoFK9krqaeZrPLwmMmgI_XiQiIkQ"



   }
   ```
3. Dynatrace issues a POST request to the configured **Endpoint URL**. The request includes the user session data as well as the access token retrieved in the previous step, which is passed as a Bearer token in the `Authorization` header.

   ```
   curl --request POST \



   --url https://[your-endpoint-url] \



   --header 'Authorization: Bearer ACCESS_TOKEN' \



   --header 'Content-type: application/json'
   ```

### Send data directly to Elasticsearch

To send data directly to your Elasticsearch installation

1. Make sure your Elasticsearch instance is reachable from the cluster server.
2. Make sure your export URL has the following format: `https://<your_host>:9200/_bulk`. Replace `<your_host>` with your actual value.
3. On the **User session exports** page, expand the required endpoint URL.
4. Under **Define your endpoint**, make sure that **Content type** is set to `application/x-ndjson` and that **Use POST method (instead of PUT)** is turned on.
5. Under **Send data directly to Elasticsearch** section, turn on **Activate**.
6. Enter the [name of the index where data is sent](#index) and the [type of documents in the Elasticsearch index](#type).

#### Elasticsearch index

Create an index where you want to send the user session data and define the mapping for your index. See [Download a sample mapping](#mapping) for details on how to download a sample mapping for your session export configuration.

If you don't create the index before enabling user session export, your Elasticsearch installation automatically creates the mappings for the fields. This automatic mapping doesn't always create the appropriate field mappings. For example, date fields are mapped as `long`.

#### Elasticsearch index type

Elasticsearch is currently removing support for mapping types. The way you create indexes and configure types depends on your Elasticsearch version. See below for details.

We recommend that you set `_doc` as the type of document regardless of the Elasticsearch version you're running.

* **Elasticsearch version 6**

  + Specify one single type per index.
  + When creating an index, specify an `include_type_name` query string parameter to indicate that requests and responses should include a type name. This parameter defaults to `true`. If you don't set it, you get a deprecation warning. If you don't specify any type when creating an index, `_doc` is used.
* **Elasticsearch version 7**

  + Specifying types is deprecated in this Elasticsearch version. The `include_type_name` parameter defaults to `false`.
  + You can force Elasticsearch to use a type name by setting the parameter to `true`, which results in a deprecation warning.
* **Elasticsearch version 8**

  + Specifying types is no longer supported. Starting with this version, omit the document type. For more information, see [Removal of mapping typesï»¿](https://www.elastic.co/guide/en/elasticsearch/reference/current/removal-of-types.html).

`Type` refers to the "index type" used in Elasticsearch and doesn't restrict which user sessions are exported. Regardless of the type you choose to configure, all user session dataâincluding user actions, events, and errorsâis exported.

To restrict the user sessions you export, you can define a management zone. See the [Set up export scope, alerting, and advanced configuration](#export) section below.

### Set up export scope, alerting, and advanced configuration

In the **Export scope, alerting, and advanced configuration** section of your endpoint, you can narrow down the session export scope, disable the notifications, and adjust some other session export settings.

* **Export scope**: To define the scope of your user session export, select the required **Management zone**. After you set up a management zone, Dynatrace sends only those user sessions that have at least one user action with a matching application.

  Restricting the session export to synthetic only user sessions isn't currently possible.
* **Alerting**: Turn on **Disable notification** if you don't want to receive notifications when your user session export fails.
* **Custom configuration**: Specify **Custom configuration properties** to further tweak the user session export configuration. Contact a Dynatrace product expert via live chat before changing this field.

If you experience any issues with user session export, contact a Dynatrace product expert via live chat before configuring any additional properties.

## Test export

To test your user session export configuration, expand the required endpoint URL on the **User session exports** page, and select **Test export**.

If the **Test export** button is disabled, it's likely because your **Endpoint URL** or **Access token URL** specifies the HTTP protocol. For security reasons, Dynatrace allows only the HTTPS protocol.

Dynatrace uses the current session export configuration to export up to 50 user sessions for the last seven days.
If no data is available during this timeframe, the test export isn't available. As soon as the test export finishes, you are notified of the results.

You don't need to save a configuration to test your endpoint.

If you set up an endpoint that is secured via [authentication](#authentication):

* Test your configuration before saving it.
* Re-enter your basic authentication password or the OAuth 2.0 client secret when testing your configuration.

## Download a sample dataset

To see what user session data looks like when you export it to your endpoints, expand the required endpoint URL on the **User session exports** page, and select **Download sample export data**.

The sample dataset consists of up to 50 user sessions tracked in your environment for the last seven days. If there aren't any user sessions during this timeframe, downloading sample data isn't available.

* If you configured a regular endpoint for your user session export, the sample data contains user sessions in JSON format, separated by newline characters.

  Sample: three sessions sent in bulk as three lines

  ```
  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}



  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}



  {"tenantId":"umsaywsjuo","userSessionId":"1394_1008","startTime":1511441593539,"endTime":1511441716896,"duration":123357,"internalUserId":"1394","userType":"REAL_USER","applicationType":"MOBILE_APPLICATION","bounce":false,"newUser":false,"userActionCount":1,"totalErrorCount":1,"ip":"2001:1800:ffff:eac2:63f5:568e:b3c6:6c54","geolocationContinentName":"North America","geolocationCountryName":"United States","geolocationRegionName":"Florida","geolocationCityName":"Delray Beach","osFamilyName":"Windows","osVersionName":"Windows 10.0 Mobile","manufacturer":"Nokia","device":"L-930","userId":"fearghasbag","screenHeight":1920,"screenWidth":1080,"screenOrientation":"PORTRAIT","displayResolution":"FHD","hasCrash":true,"isp":"SWCP-AS - Southwest Cyberport","stringTags":{ },"numTags":{ },"dateTags":{ },"userActions":[ { "name":"Checkout","type":"Custom","startTime":1511441593539,"endTime":1511441593562,"duration":23,"application":"easyTravel Demo","speedIndex":null,"errorCount":0,"apdexCategory":"UNKNOWN","networkTime":null,"serverTime":null,"frontendTime":null,"documentInteractiveTime":null,"failedImages":null,"failedXhrRequests":null,"httpRequestsWithErrors":null,"thirdPartyResources":null,"thirdPartyBusyTime":0,"cdnResources":null,"cdnBusyTime":0,"firstPartyResources":null,"firstPartyBusyTime":0,"hasCrash":false,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":null,"requestStart":null,"responseStart":null,"responseEnd":null,"visuallyCompleteTime":null } ],"events":[ { "type":"UserTag","name":"fearghasbag","startTime":1511441593562,"application":"MOBILE_APPLICATION-752C288D59734C79" } ],"errors":[ { "type":"Crash","name":"ThrowAsync","startTime":1511441716896,"application":"MOBILE_APPLICATION-752C288D59734C79"}]}
  ```
* If you configured your endpoint to [send data directly to Elasticsearch](#send-to-elasticsearch), the sample data also contains header lines as shown in the example below. These are used to tell Elasticsearch what to do with the data.

  Sample: a session sent to Elasticsearch

  ```
  { "index" : { "_index" : "my-index", "_type" : "_doc", "_id" : "umsaywsjuo-744377345-1622107543233" } }



  {"tenantId":"umsaywsjuo","userSessionId":"744377345","startTime":1622107543233,"endTime":1622107578205,"duration":34972,"internalUserId":"744377345","userType":"SYNTHETIC","applicationType":"WEB_APPLICATION","bounce":false,"newUser":true,"userActionCount":12,"totalErrorCount":5,"totalLicenseCreditCount":0,"matchingConversionGoalsCount":0,"ip":"157.25.19.100","continent":"Europe","country":"Poland","region":"synthetic","city":"Bydgoszcz","browserType":"Synthetic Agent","browserFamily":"Synthetic monitor","browserMajorVersion":"Synthetic monitor","osFamily":"Linux","osVersion":"Linux","screenHeight":1080,"screenWidth":1920,"screenOrientation":"LANDSCAPE","displayResolution":"FHD","hasSessionReplay":false,"isp":"T-Mobile Czech Republic","clientType":"Synthetic Agent","browserMonitorId":"SYNTHETIC_TEST-18B209EFE2F438F8","browserMonitorName":"mySampleEnv.dynatrace.com - browser monitor - analysis","stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActions":[{"name":"/rest/cvalidation/validate/%2fvalidateappmetrickey?input=<masked>&appmetrickey=<masked>&gtf=<masked>","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;mode=performance;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107568648,"endTime":1622107569320,"duration":672,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"FRUSTRATED","matchingConversionGoals":[],"networkTime":5,"serverTime":58,"frontendTime":609,"documentInteractiveTime":null,"thirdPartyResources":1,"thirdPartyBusyTime":659,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":9,"firstPartyBusyTime":333,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107568730,"requestStart":2,"responseStart":60,"responseEnd":63,"visuallyCompleteTime":null,"syntheticEvent":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":1,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null},{"name":"/rest/webcheckdetails/overviewdata/browsermonitoranalysis/synthetic_<masked>?selectedtimeframe=<masked>&actiontype=<masked>&analysistf=<masked>&analysismode=<masked>&analysisoverviewsplitting=<masked>&analysisactiontype=<masked>&parts_details=<masked>&parts_chart=<masked>&parts=<masked>&timeframe=<m","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;mode=performance;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107569821,"endTime":1622107570083,"duration":262,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"FRUSTRATED","matchingConversionGoals":[],"networkTime":5,"serverTime":65,"frontendTime":192,"documentInteractiveTime":null,"thirdPartyResources":0,"thirdPartyBusyTime":null,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":5,"firstPartyBusyTime":223,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107569826,"requestStart":3,"responseStart":68,"responseEnd":70,"visuallyCompleteTime":null,"syntheticEvent":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":1,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null},{"name":"/rest/webcheckdetails/overviewdata/browsermonitoranalysis/synthetic_<masked>?selectedtimeframe=<masked>&actiontype=<masked>&analysistf=<masked>&analysismode=<masked>&analysisoverviewsplitting=<masked>&visitid=<masked>&timestamp=<masked>&analysisactiontype=<masked>&parts=<masked>&timeframe=<masked>&g","domain":"mySampleEnv.dynatrace.com","targetUrl":"https://mySampleEnv.dynatrace.com/#monitoranalysiskpm;webcheckId=SYNTHETIC_TEST-67444FBB89C6F11B;actionType=Load;splitting=event;analysisTf=custom1622103968000to1622107568000;ensureAnalysisTimeframe=true;mode=performance;visitId=623513409;analysisActionType=Load;gtf=l_2_HOURS","type":"Xhr","startTime":1622107572811,"endTime":1622107572911,"duration":100,"application":"mySampleEnv.dynatrace.com - browser monitor - analysis - 1620645163422","internalApplicationId":"APPLICATION-A8894472DACEDA0E","speedIndex":null,"apdexCategory":"SATISFIED","matchingConversionGoals":[],"networkTime":14,"serverTime":61,"frontendTime":25,"documentInteractiveTime":null,"thirdPartyResources":0,"thirdPartyBusyTime":null,"cdnResources":0,"cdnBusyTime":null,"firstPartyResources":2,"firstPartyBusyTime":167,"domCompleteTime":null,"domContentLoadedTime":null,"loadEventStart":null,"loadEventEnd":null,"navigationStart":1622107572831,"requestStart":12,"responseStart":73,"responseEnd":75,"visuallyCompleteTime":null,"syntheticEvent":"open first execution","syntheticEventId":"SYNTHETIC_TEST_STEP-3A281F8FB8AB3C37","keyUserAction":false,"stringProperties":[],"longProperties":[],"doubleProperties":[],"dateProperties":[],"userActionPropertyCount":0,"customErrorCount":0,"javascriptErrorCount":0,"requestErrorCount":0,"largestContentfulPaint":null,"firstInputDelay":null,"totalBlockingTime":null,"cumulativeLayoutShift":null}],"events":[],"errors":[],"syntheticEvents":[{"name":"navigate to details screen","syntheticEventId":"SYNTHETIC_TEST_STEP-09D1E2CC97B5878B","sequenceNumber":1,"timestamp":1622107547988,"type":"navigate"},{"name":"keystrokes on \"user\"","syntheticEventId":"SYNTHETIC_TEST_STEP-0FCD20FF925F44B1","sequenceNumber":2,"timestamp":1622107550155,"type":"keystrokes"},{"name":"click on next","syntheticEventId":"SYNTHETIC_TEST_STEP-84854E56BAA53321","sequenceNumber":3,"timestamp":1622107551834,"type":"click"},{"name":"keystrokes on \"password\"","syntheticEventId":"SYNTHETIC_TEST_STEP-6CB903FD28430FE6","sequenceNumber":4,"timestamp":1622107553985,"type":"keystrokes"},{"name":"click on login button","syntheticEventId":"SYNTHETIC_TEST_STEP-6400C0C04B6B76E3","sequenceNumber":5,"timestamp":1622107564154,"type":"click"},{"name":"open first event","syntheticEventId":"SYNTHETIC_TEST_STEP-395A7BBE253C8C8C","sequenceNumber":6,"timestamp":1622107566364,"type":"click"},{"name":"select performance part","syntheticEventId":"SYNTHETIC_TEST_STEP-A53F6787F97741F7","sequenceNumber":7,"timestamp":1622107568548,"type":"click"},{"name":"click on \"Analyze performance\"","syntheticEventId":"SYNTHETIC_TEST_STEP-7D9201BEB990247E","sequenceNumber":8,"timestamp":1622107572734,"type":"click"},{"name":"open first execution","syntheticEventId":"SYNTHETIC_TEST_STEP-3A281F8FB8AB3C37","sequenceNumber":9,"timestamp":1622107574905,"type":"click"},{"name":"open screenshot","syntheticEventId":"SYNTHETIC_TEST_STEP-DF43A9A21ADE0E10","sequenceNumber":10,"timestamp":1622107576588,"type":"click"}],"endReason":"END_EVENT","numberOfRageClicks":0,"userExperienceScore":"TOLERATED","connectionType":"UNKNOWN","hasError":true}
  ```

## Download a sample mapping

To [export user session data directly to your own Elasticsearch instance](#send-to-elasticsearch), you can download a sample mapping for your indexes. Expand the required endpoint URL on the **User session exports** page, and select **Download mapping**. The downloaded template mapping file contains a mapping for each exported field.

The created sample mapping reflects your current settings, so you can use it when creating the index where user session data is to be exported.

```
PUT /my-usersession-index



{



"settings": {



"index": {



"number_of_shards": 3,



"number_of_replicas": 1



}



},



"mappings": {



"properties": {



// add the mappings from the downloaded file here ...



}



}



}
```

Example

```
{



"mappings" : {



"dynamic_templates" : [ {



"string_fields" : {



"match" : "*",



"match_mapping_type" : "string",



"mapping" : {



"norms" : "false",



"type" : "keyword"



}



}



} ],



"properties" : {



"applicationType" : {



"type" : "keyword"



},



"appVersion" : {



"type" : "keyword"



},



// ...



}



}



}
```

## Configure session export via API

The user session export configuration is stored using the Settings 2.0 framework. This provides a REST API that you can use to create, read, update, and delete your session export configurations. See [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for details.

* Endpoints to access the Settings API:

  + For Dynatrace Managed deployments: `https://{your-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
  + For Environment ActiveGate: `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/objects/{objectId}`
* Address for OpenAPI documentation: `https://{your-environment-id}.live.dynatrace.com/rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Settings%20-%20Objects`.
* Schema ID for the user session export configuration: `builtin:elasticsearch.user-session-export-settings-v2`.  
  With this schema ID, you can, for example, read your current user session export configuration using any REST client.

  ```
  GET https://{your-domain}/api/v2/settings/objects?schemaIds=builtin:elasticsearch.user-session-export-settings-v2&scopes=tenant&fields=objectId,value
  ```

To add a session export configuration via the REST API

```
POST https://{your-domain}/api/v2/settings/objects?schemaIds=builtin:elasticsearch.user-session-export-settings-v2&scopes=tenant



[



{



"schemaVersion": "0.0.214",



"schemaId": "builtin:elasticsearch.user-session-export-settings-v2",



"scope": "tenant",



"value": {



"endpointDefinition": {



"endpointUrl": "https://endpoint-export.dev",



"enableUserSessionExport": true,



"contentType": "application/json",



"usePost": false



},



"authentication": {



"active": false



},



"sendDirect": {



"active": false



},



"exportBehavior": {



"managementZone": null,



"disableNotification": false,



"customConfiguration": null



}



}



}



]
```

You can add only one user session export configuration per request. If you need to add a second session export configuration, issue a new `POST` request.

For details on how to update or delete a settings object, see [Settings API - PUT an object](/managed/dynatrace-api/environment-api/settings/objects/put-object "Edit a settings object via the Dynatrace API.") and [Settings API - DELETE an object](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.").

## Verify session export configuration

To verify the session export configuration, run the command below.

```
curl -v -H "Content-Type: application/json" -X PUT -d '{"visitorId":"14804637803609BCTKP776NMJBOIF3R8OD6R0E4NQALJO","visitId":"16229530","startTime":1480463779085,"endTime":1480463784889,"visitType":"SYNTHETIC"}' http://localhost:3000/export/events
```

You can set the following additional flags as needed.

* `--insecure` to disable the SSL check
* `--http1.1` if the command returns a `REFUSED_STREAM` error