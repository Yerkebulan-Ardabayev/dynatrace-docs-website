---
title: Set up CORS on Amazon S3
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/aws-platform/set-up-cors-in-amazon-s3
scraped: 2026-02-28T21:16:52.998801
---

# Set up CORS on Amazon S3

# Set up CORS on Amazon S3

* How-to guide
* 3-min read
* Published Jul 19, 2017

Use these guidelines to set up CORS (cross-origin HTTP requests) in AWS for buckets within Amazon S3 (Simple Storage Service). To learn more about CORS and how it works, see [HTTP access control (CORS)ï»¿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS).

## Introduction

Modern web browsers don't provide access to error information in `window.onerror` for scripts that are loaded across domains. This is a severe restriction that limits the usefulness of the Dynatrace JavaScript error-detection engine.

Without CORS, instead of providing error details and a stacktrace when an uncaught JavaScript error is thrown, a message such as the follow appears:

"Script error" is usually reported when an exception violates the browsers same-origin-policy i.e. when the error occurs in a script that is hosted on a domain other than the domain of the current page.
If the script is received with the CORS HTTP headers set, it's possible to get the full error details for most browsers by adding the attribute `crossorigin="anonymous"` to the script tag. Unfortunately Internet Explorer 11 and Edge don't currently support the `crossorigin` attribute. Care is also required to only set the `crossorigin` attribute for scripts with CORS headers present as otherwise the script will not be executed anymore.

In order to gain full visibility into thrown JavaScript errors, CORS HTTP headers must be set on the cross-domain servers and the `crossorigin` attribute must be applied to the script tag. Before performing this step, you must configure Amazon S3.

### Configure Amazon S3

The first step is to input CORS settings for your resources on S3. This is done at the bucket level. Unfortunately, it's not possible to input CORS settings for individual resources within buckets.

1. Open the Amazon S3 console.
2. Select the bucket that contains your resources.
3. Select **Permissions**.
4. Scroll down to **Cross-origin resource sharing (CORS)** and select **Edit**.
5. Insert the CORS configuration in JSON format.

   Example JSON:

   ```
   [



   {



   "AllowedHeaders": [



   "*"



   ],



   "AllowedMethods": [



   "GET",



   "HEAD"



   ],



   "AllowedOrigins": [



   "*"



   ],



   "ExposeHeaders": []



   }



   ]
   ```

   See [Creating a cross-origin resource sharing (CORS) configurationï»¿](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html) for details.
6. Select **Save changes** to save your configuration.

### Configure CloudFront

With Amazon S3 configured, it's now time to enable CORS headers in CloudFront. Otherwise the headers will be filtered out and this mechanism won't work.

1. Open the CloudFront console. You should see a window similar to that shown below. Find your distribution in the list and click its **ID** link. If necessary, use the search field (highlighted below in red) to search for your distribution.

   ![AWS cors 3](https://dt-cdn.net/images/aws-cors-3-1652-d619805ef5.png)
2. Now you should see your distribution. Click the **Behaviors** tab. Find the behavior entry for your resource, described in the **Path Pattern** column. Select the pattern and click **Edit**. If the behavior entry doesn't exist, you must create it.

   ![AWS cors 4](https://dt-cdn.net/images/aws-cors-4-968-4f0dee4542.png)
3. Now we can edit the behavior settings. All CORS-relevant elements are highlighted in red below. First you must choose which HTTP method will be available for this behavior. For **Allowed HTTP Methods**, we recommend that you select the second or third option and select the **OPTIONS** check box, otherwise you won't be able to use CORS for REST calls, which use preflighted requests.
4. From the **Forward Headers** list, select **Allowlist**. You should then see the **Allowlist headers** menu. Select a particular header from the left listbox and click **Add**. If you don't see a particular header you can input it into **Filter headersâ¦** textbox and click **Add custom**. For CORS, the most important headers are `Origin` and `Access-Control-Allow-Origin`. Other headers are optional and dependent on what you want to achieve.
5. Confirm your changes by clicking **Yes, Edit**.

   ![AWS cors 5](https://dt-cdn.net/images/aws-cors-5-953-60dec24e19.png)