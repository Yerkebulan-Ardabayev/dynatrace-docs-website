---
title: "Data privacy and security"
source: https://docs.dynatrace.com/docs/manage/data-privacy-and-security
updated: 2026-02-09
---

# Data privacy and security

# Data privacy and security

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Jan 20, 2023

Privacy laws around the globe are improving the protection of personal data in response to an evolving technology landscape, increased globalization, and complex international data flows. Companies are held accountable for transparency, fairness, and accuracy in how they collect, store, use, and protect personal data.

At Dynatrace, we take our responsibility to safeguard your data seriously. Have a look at the following resources to understand how your organization can maximize data protection provided by Dynatrace.

### Data privacy overview

[Dynatrace policies in Trust Centerï»¿](https://www.dynatrace.com/company/trust-center/#general-data-protection-regulation-gdpr)

[Data protection at Dynatrace](../../ru/manage/data-privacy-and-security/data-privacy/data-protection.md "Find out how Dynatrace ensures that your data is secured.")

[Personal data captured by Dynatrace](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Levels of data protection](data-privacy-and-security/data-privacy/levels-of-data-protection.md "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")

### Data security

* [Data security controls](../../ru/manage/data-privacy-and-security/data-security/data-security-controls.md "Learn about data security and operational security controls.")
* [Secure development controls](../../ru/manage/data-privacy-and-security/data-security/secure-development-controls.md "Learn how we ensure complete security for all Dynatrace software components and development practices.")
* [Report a security-related concern](data-privacy-and-security/data-security/report-a-security-related-concern.md "Find out how to report vulnerabilities and whom to contact in case of security concerns.")

### Environment-wide settings

[Configure data privacy settings](../../ru/manage/data-privacy-and-security/configuration/configure-global-privacy-settings.md "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

[Role-based permissions](identity-access-management/permission-management/role-based-permissions.md "Role-based permissions")

[Define request attribute rules](../../ru/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data.md#request-attribute-rules "Create request attributes based on web request data.")

[Mark request attributes as confidential](../../ru/observe/application-observability/services/request-attributes.md#confidential "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")

[Audit logs via API](data-privacy-and-security/configuration/audit-logs-api.md "Learn how to manage audit logs using an API.")

[Cookies](data-privacy-and-security/data-privacy/cookies.md "Learn about first-party cookie usage in Dynatrace.")

[Data retention periods](../../ru/manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Check retention times for various data types.")

[Adaptive Data Retention](../../ru/manage/data-privacy-and-security/data-privacy/adaptive-data-retention.md "Find out how the retention time for the data stored in the transaction, Session Replay, and Log monitoring storages is adjusted.")

### Real User Monitoring

[Configure data privacy settings for web applications](../observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr.md "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")

[Configure data privacy settings for mobile applications](../observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile.md "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[Define URL cleanup rules](../observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis.md#define-url-cleanup-rules "Learn how to analyze all user action monitoring data through waterfall analysis.")

[Create custom user action names for web applications](../observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions.md "Customize automatically generated user action names for your web applications.")

[Personal data captured for RUM](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md#real-user-monitoring-rum "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data retention periods](../../ru/manage/data-privacy-and-security/data-privacy/data-retention-periods.md "Check retention times for various data types.")

[Detection of IP addresses, geolocations, and user agents](../observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents.md "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")

[Firewall constraints for RUM](../observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum.md#cookies "Find out how to make sure that Real User Monitoring data passes through your firewall.")

[User privacy for iOS](../../ru/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios.md "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.")

[Data safety guidance for Android](../../ru/manage/data-privacy-and-security/data-privacy/user-privacy-for-android.md "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.")

### Session Replay

[Configure Session Replay for web applications](../observe/digital-experience/session-replay/configure-session-replay-web.md "Configure monitoring consumption and data privacy settings for Session Replay.")

[Mask sensitive data for Session Replay on iOS](../../ru/observe/digital-experience/session-replay/session-replay-ios.md#mask-sensitive-data "Prerequisites and the procedure for enabling Session Replay for your iOS apps.")

[Mask sensitive data for Session Replay on Android](../../ru/observe/digital-experience/session-replay/session-replay-android.md#mask-sensitive-data "Set up Session Replay for your Android apps to learn which actions your users perform.")

[Personal data captured for Session Replay](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md#session-replay "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data retention periods](../../ru/manage/data-privacy-and-security/data-privacy/data-retention-periods.md#rum-session-replay "Check retention times for various data types.")

### Data privacy APIs

[Data privacy API](../dynatrace-api/configuration-api/data-privacy-api.md "Learn what the Dynatrace data privacy config API offers.")

[Anonymization API](../dynatrace-api/environment-api/anonymization.md "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

[Audit logs API](../dynatrace-api/environment-api/audit-logs.md "Read Dynatrace audit logs via Dynatrace API.")

### OpenTelemetry

[Mask sensitive data](../../ru/ingest-from/opentelemetry/collector/use-cases/redact.md "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")

### Log Monitoring

#### Log Management and Analytics

[Sensitive log data masking on source with OneAgent](../../ru/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-sensitive-data-masking.md "Mask sensitive information in your log data using Log Management and Analytics.")

[Sensitive data masking on write (during ingest) with Log Processing](../analyze-explore-automate/logs/lma-classic-log-processing/lma-log-processing-examples.md#lpexample12 "Explore scenarios of how to use log processing in Dynatrace powered by Grail.")

[Configure data storage and retention for logs](../../ru/analyze-explore-automate/logs/lma-bucket-assignment.md "Your log data can be stored in data retention buckets based on specific retention periods.")

[Personal data captured for Log Monitoring](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md#log-monitoring "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Log Management and Analytics compliance in Dynatrace](../analyze-explore-automate/logs/lma-use-cases/lma-compliance-use-cases.md "Explore compliance-related Log Management and Analytics use cases in Dynatrace deployments.")

#### Log Monitoring Classic

[Sensitive log data masking with OneAgent](../../ru/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking.md "Mask sensitive information in your log data using Log Monitoring Classic.")

[Sensitive data masking on write (during ingest) with Log Processing](../../ru/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples.md#lpexample13 "Example log processing scenarios.")

[Management zones and ingested log data (Logs Classic)](../../ru/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring.md "Find out how ingested log data is assigned to management zones.")

[Personal data captured for Log Monitoring](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md#log-monitoring "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

## Live Debugger

[Personal data captured by Live Debugger](data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace.md#live-debugger "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data masking on capture with Live Debugger](../../ru/observe/application-observability/live-debugger/additional-settings.md#applying-data-masking-rules "Manage breakpoint permissions, configure OneAgent-related settings, set up the version control integration, and apply data masking rules.")
