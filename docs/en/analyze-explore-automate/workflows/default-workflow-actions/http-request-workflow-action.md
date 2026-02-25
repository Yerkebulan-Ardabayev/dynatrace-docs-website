---
title: HTTP request action for Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/default-workflow-actions/http-request-workflow-action
scraped: 2026-02-25T21:35:28.765632
---

# HTTP request action for Workflows

# HTTP request action for Workflows

* Latest Dynatrace
* Reference
* 1-min read
* Published Apr 02, 2024

The **HTTP Request** action for Workflows enables you to issue an HTTP request to any API.

## HTTP Request action security

* All HTTP calls are validated against the global allowlist.

We strictly advise against providing any static Authorization header and therefore, leak a secret. Use the credential vault to store your credentials for **Basic** or **Token** authentication, or a Run JavaScript action to implement any other authentication.

## Input

* **Method**: the HTTP request method to use.
* **ULR**: the url the request should target.
* **Authentication**: the HTTP Request action supports to use credentials of the credential vault for Basic and Token authentication.
  Make sure the credential configuration [allows access](/docs/manage/credential-vault#access-cv "Store and manage credentials in the credential vault.") for the workflow actor (credential scope: `AppEngine`, app access: `Workflows app`, Owner access or actor as selected user).
* **Payload**: the payload of the HTTP request.
  Set an appropriate content-type header.
* **Headers**: the HTTP request headers with their name and value.
  Be aware that any header value is accessible in the workflow monitor to everyone with access to the workflow. Thus it is strictly advised to not expose any secret, but use the authentication configuration via credential vault.
* **Error handling**: the HTTP response codes that let the task fail.
  Depending on the use case, issuing the HTTP request independently of the response should be successful.
  Therefore, turn the option to fail on certain HTTP response codes off or define the HTTP response codes that shall fail the task.

## Result

The result of the HTTP request action is a JSON structure that includes

* **status\_code**: the HTTP response status code.
* **body**: the raw HTTP response body.
* **headers**: the HTTP response header as objects consisting of header name and value.
* **json**: the HTTP response as a JSON document. Only JSON response payloads are supported.