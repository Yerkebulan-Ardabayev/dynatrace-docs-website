---
title: Okta SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-okta
scraped: 2026-02-16T21:27:02.902548
---

# Okta SCIM configuration for Dynatrace

# Okta SCIM configuration for Dynatrace

* Latest Dynatrace
* How-to guide
* 1-min read
* Published May 14, 2020

This page describes the IdP (**Okta**) end of your **SCIM** SSO configuration, not the Dynatrace end. Use it as part of the entire [SCIM configuration procedure](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM") for Dynatrace SaaS if you're using Okta.

While we do our best to provide you with current information, Dynatrace has no control over changes that may be made by third-party providers. Always refer to official third-party documentation from your IdP as your primary source of information for third-party products.

To integrate Dynatrace SCIM in Okta, you will need the Dynatrace SCIM Base URL and a secret token you got in the [Get Dynatrace SCIM endpoint and create secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

Okta provides two possibilities of SCIM integration:

1. [Add SCIM provisioning to already integrated Okta app with Dynatrace SSOï»¿](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SCIM.htm)
2. [Integrate Dynatrace SCIM in separate SCIM Okta Appï»¿](https://developer.okta.com/docs/guides/build-provisioning-integration/prepare-app/)

   * You can use either [SCIM 2.0 Test App (Header Auth)ï»¿](https://www.okta.com/integrations/scim-2-0-test-app-header-auth) or [SCIM 2.0 Test App (OAuth Bearer Token)ï»¿](https://www.okta.com/integrations/scim-2-0-test-app-oauth-bearer-token)

Dynatrace SCIM supports only bearer token authentication. Depending on the Okta application type, while configuring API Credentials the token should be provided with the **Bearer** prefix.