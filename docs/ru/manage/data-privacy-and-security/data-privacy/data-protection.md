---
title: Data protection at Dynatrace
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/data-protection
scraped: 2026-02-26T21:32:57.026240
---

# Data protection at Dynatrace

# Data protection at Dynatrace

* Latest Dynatrace
* 4-min read
* Published May 17, 2018

We're committed to protecting the security, privacy, and availability of the Dynatrace Software Intelligence Platform. The security of your data and digital experience is a key priority for us, and we strive to protect and process your data responsibly. Proper care for data is at the core of our business.

Dynatrace enables you to be in full control of your data. With appropriate defaults in place, you determine what data to share with Dynatrace. To prevent unauthorized access, maintain data accuracy, and ensure the correct use of information, Dynatrace has physical, technical, and organizational procedures in place to safeguard your data with multiple layers of protection.

## Data minimization strategy

Dynatrace provides you with the opportunity to follow the principle of data minimization, with an aim to reduce the processing of data to a strict minimum. You control the data sent to Dynatrace with the built-in mechanisms including [data masking rules](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), [user action naming rules](/docs/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), [Anonymization API](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data."), and more. We enable you to obtain the full value of Dynatrace products and services without the necessity of sharing personal data (aside from authentication purposes) with Dynatrace.

## Privacy and security by design

Dynatrace values your privacy and trust, so we have implemented the concepts of privacy and security by design. These concepts transparently empower you to control your data and make specific privacy choices. Dynatrace assists you in making these choices and aims to ensure that privacy and security components are embedded in all parts of the product right from the beginning. This way, privacy becomes an integral part of the Dynatrace Software Intelligence Platform without diminishing the core functionality. Furthermore, our "privacy and security by design" approach allows for best-in-class [privacy and security defaults](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") out-of-the-box.

## Automated testing

To ensure best-in-class privacy, Dynatrace relies on extensive automated testing for all new and existing product functionality. Ongoing automated testing ensures the efficiency of the privacy measures that are deployed at each stage of the Dynatrace product lifecycle.

Our automated tests are:

* Adjusted and performed for every new release (bi-weekly schedule)
* Regularly reviewed to ensure 100% test coverage (bi-monthly schedule)
* Checked as part of a yearly privacy framework review

## Employee enablement

At Dynatrace, we recognize that our high data privacy and security standards depend on the awareness and engagement of each Dynatrace employee. With a culture of privacy and security risk awareness, focused data privacy principles, and recurring individual cybersecurity and privacy training, we empower our employees to sustain our market leadership in privacy and security. Easily accessible help channels and data privacy partnerships throughout the company further reinforce the culture of data privacy and security at Dynatrace.

## Access control

You control whether Dynatrace has access to your data. Only users who are members of the monitoring environment's administrative groups, which are tightly controlled by you, can grant or revoke access to the collected data. For information on what options you have for managing access control in Dynatrace, see [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions").

When you need our support, authorized Dynatrace employeesâspecifically, second- and third-level support representativesâcan be granted access to view your data. Such access is restricted by a strong "need to access" policy. Each access is logged, time-stamped, and made available to you in an automated way via our REST API. All authorized Dynatrace employees are bound by strict confidentiality agreements.

## Monitoring and audit logging

All systems operated by Dynatrace are subject to health and security monitoring, audit logging, and automated system log analysis. When Dynatrace support is requested for remote installations, access to your systems is recorded in [audit logs](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.").

## Data retention management

To perform monitoring services, Dynatrace retains only the data that you elect to share and stores it in your Dynatrace Cluster. Dynatrace automatically deletes data that is older than the configured [retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types."). Dynatrace also provides [Adaptive Data Retention](/docs/manage/data-privacy-and-security/data-privacy/adaptive-data-retention "Find out how the retention time for the data stored in the transaction, Session Replay, and Log monitoring storages is adjusted.") as functionality to periodically increase or decrease the data retention time when your environment storage quota is exceeded.

## Alignment with data protection laws

Dynatrace provides flexible [data privacy settings](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") that enable you to fine-tune your environment and application configuration according to regional privacy laws.

## Security controls

Dynatrace also provides multi-layered [security controls](/docs/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.") to keep your data safe.