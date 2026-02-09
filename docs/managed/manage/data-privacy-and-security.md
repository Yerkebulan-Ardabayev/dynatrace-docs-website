---
title: "Data privacy and security"
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security
updated: 2026-02-09
---

# Data privacy and security

# Data privacy and security

* Explanation
* 2-min read
* Updated on Jan 20, 2023

Privacy laws around the globe are improving the protection of personal data in response to an evolving technology landscape, increased globalization, and complex international data flows. Companies are held accountable for transparency, fairness, and accuracy in how they collect, store, use, and protect personal data.

At Dynatrace, we take our responsibility to safeguard your data seriously. Have a look at the following resources to understand how your organization can maximize data protection provided by Dynatrace.

### Data privacy overview

[Dynatrace policies in Trust Centerï»¿](https://www.dynatrace.com/company/trust-center/#general-data-protection-regulation-gdpr)

[Data protection at Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/data-protection "Find out how Dynatrace ensures that your data is secured.")

[Personal data captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Levels of data protection](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")

### Data security

* [Data security controls](/managed/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.")
* [Secure development controls](/managed/manage/data-privacy-and-security/data-security/secure-development-controls "Learn how we ensure complete security for all Dynatrace software components and development practices.")
* [Report a security-related concern](/managed/manage/data-privacy-and-security/data-security/report-a-security-related-concern "Find out how to report vulnerabilities and whom to contact in case of security concerns.")

### Environment-wide settings

[Configure data privacy settings](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

[Role-based permissions](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions")

[Define request attribute rules](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data#request-attribute-rules "Create request attributes based on web request data.")

[Mark request attributes as confidential](/managed/observe/application-observability/services/request-attributes#confidential "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")

[Audit logs via API](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.")

[Cookies](/managed/manage/data-privacy-and-security/data-privacy/cookies "Learn about first-party cookie usage in Dynatrace.")

[Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

[Adaptive Data Retention](/managed/manage/data-privacy-and-security/data-privacy/adaptive-data-retention "Find out how the retention time for the data stored in the transaction, Session Replay, and Log monitoring storages is adjusted.")

### Real User Monitoring

[Configure data privacy settings for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.")

[Configure data privacy settings for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")

[Define URL cleanup rules](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis#define-url-cleanup-rules "Learn how to analyze all user action monitoring data through waterfall analysis.")

[Create custom user action names for web applications](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.")

[Personal data captured for RUM](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#real-user-monitoring-rum "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.")

[Detection of IP addresses, geolocations, and user agents](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")

[Firewall constraints for RUM](/managed/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum#cookies "Find out how to make sure that Real User Monitoring data passes through your firewall.")

[User privacy for iOS](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-ios "Learn about what kind of data OneAgent collects when you need to report your app privacy to Apple.")

[Data safety guidance for Android](/managed/manage/data-privacy-and-security/data-privacy/user-privacy-for-android "Information on types of data that OneAgent for Android collects. You can use this page when filling out the Data safety form in Google Play Console.")

### Session Replay

[Configure Session Replay for web applications](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.")

[Mask sensitive data for Session Replay on iOS](/managed/observe/digital-experience/session-replay/session-replay-ios#mask-sensitive-data "Prerequisites and the procedure for enabling Session Replay for your iOS apps.")

[Mask sensitive data for Session Replay on Android](/managed/observe/digital-experience/session-replay/session-replay-android#mask-sensitive-data "Set up Session Replay for your Android apps to learn which actions your users perform.")

[Personal data captured for Session Replay](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#session-replay "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#rum-session-replay "Check retention times for various data types.")

### Data privacy APIs

[Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

[Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.")

[Audit logs API](/managed/dynatrace-api/environment-api/audit-logs "Read Dynatrace audit logs via Dynatrace API.")

### Dynatrace Managed

* [Data privacy and exchange in Managed](/managed/managed-cluster/data-privacy/managed-data-privacy-and-exchange "Learn what data is exchanged between your Managed cluster and Mission Control.")
* [Monitored technologies and feature usage](/managed/managed-cluster/data-privacy/monitored-technologies "Learn how Dynatrace sends information about monitored technologies and feature usage.")
* [Mission Control proactive support](/managed/managed-cluster/data-privacy/mission-control-proactive-support "Learn about how Mission Control proactive support works.")

### OpenTelemetry

[Mask sensitive data](/managed/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")

### Log Monitoring

#### Log Monitoring Classic

[Sensitive log data masking with OneAgent](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/sensitive-data-masking "Mask sensitive information in your log data using Log Monitoring Classic.")

[Sensitive data masking on write (during ingest) with Log Processing](/managed/analyze-explore-automate/log-monitoring/log-processing/log-processing-examples#lpexample13 "Example log processing scenarios.")

[Management zones and ingested log data (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")

[Personal data captured for Log Monitoring](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#log-monitoring "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

## Live Debugger

[Personal data captured by Live Debugger](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#live-debugger "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")

[Data masking on capture with Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
