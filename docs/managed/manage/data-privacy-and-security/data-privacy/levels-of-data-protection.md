---
title: Levels of data protection
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection
scraped: 2026-05-12T11:09:01.261844
---

# Levels of data protection

# Levels of data protection

* 2-min read
* Updated on Dec 13, 2023

Depending on your environment setup and settings, you might capture data for which you have legal obligations due to protection laws, standards, and regulations, such as GDPR, CCPA, HIPAA, LGPD, PCI-DSS and more. To address such cases, Dynatrace offers multiple layers of protection to help you fine-tune the data flows in Dynatrace.

[**Masking at capture**](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection#at-capture "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")[**Masking at storage**](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection#at-storage "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")[**Masking at display**](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection#at-display "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")

Check a flowchart below to see on what levels and entities your end users' data is masked in Dynatrace.

![Dynatrace data flowchart](https://dt-cdn.net/images/data-flow-model-for-masking-6216-3bbc2bd428.png)

Dynatrace data flowchart

For masking at capture and masking at storage, any related masking capability in Dynatrace is applied only after you enable it; such masking is not applied retroactively.

## Protect personal data by not capturing it (masking at capture)

With masking at capture, data is masked at first contact with Dynatrace. The original data does not leave the monitored environment.

Dynatrace can automatically mask sensitive data points at first contact with a Dynatrace technology. This happens within the application, monitored process, or browser so that the data points are replaced with a placeholder before sending them to the Dynatrace Cluster. Asterisks (`*`) are used for such placeholders. For example, the `john.smith@domain.com` email address is transformed into `*********` and is never sent or stored in its original form.

Use the following settings to control masking at capture.

* [OneAgent-side masking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#oneagent-side-masking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [Log masking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#log-masking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [End-user IP address masking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [User action masking](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-user-actions "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

## Protect personal data by not storing it (masking at storage)

When masking at storage is implemented, data is sent to the Dynatrace server for optimal analysis and is masked before it's stored.

Leverage the following settings to control masking at storage.

* [Masking of personal data in URIs](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-uris "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

## Protect personal data by not displaying it (masking at display)

When data is masked at display, it's stored in its original form but is accessible only to the users of your choice.

Check the following information to learn how to configure masking at display.

* [Restricted view access to personal data](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#restrict-view-access "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [Confidential request attributes](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#conf-attribute "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")