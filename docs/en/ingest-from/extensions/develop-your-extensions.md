---
title: Develop your own Extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions
scraped: 2026-02-06T16:33:55.259256
---

# Develop your own Extensions

# Develop your own Extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Jun 16, 2025

Dynatrace can ingest data from [hundreds of toolsï»¿](https://www.dynatrace.com/hub/), which means you get:

* A single source of truth for observability.
* A continuous flow of actionable data to help you fix problems quickly, maintain complex systems, improve code quality, and accelerate digital transformation.

If we don't have a pre-built solution for your situation, you can declaratively bring metrics into Dynatrace that feed platform analytics and monitoring capabilities. Dynatrace links your data in a meaningful way so you can explore it, build instrumentation, and set up alerting.

Extensions support policy

Dynatrace support staff are committed to aiding within the defined scope of support. However, specific topics fall outside our support capabilities, including:

* **Custom Extensions**: Technical support can only aid customers with extensions that are available on Dynatrace Hub and marked as **Supported by Dynatrace**, unless the problem is related to the extensions framework itself.
* **Custom Extension Files**: Technical support cannot support with the analysis of custom configuration or code, and requests to create such files are not within the support scope.

Customers needing help with unsupported extensions or extension files can request paid assistance from our services department.

## Before you begin

Get familiar with the [Dynatrace Extensions concepts](/docs/ingest-from/extensions/concepts#concepts "Learn more about the concept of Dynatrace Extensions.").

## Security best practices

Dynatrace applies [secure development controls](/docs/manage/data-privacy-and-security/data-security/secure-development-controls "Learn how we ensure complete security for all Dynatrace software components and development practices.") in its Security Development Lifecycle (SDL).

Follow these best practices to ensure your extensions are secure, reliable, and compliant with your environmentâs security standards.

### Certificate management

* Use signed extensions to ensure integrity and prevent tampering.
* Assign different signing certificates for different categories of extensions (for example, sensitive data vs. general monitoring).
* Store and manage root and developer certificates separately.
* Replace leaked certificates immediately and re-sign affected extensions.

### Extension code

* Review and validate all extension logic, including scripts, queries, and third-party components.
* Avoid embedding code from untrusted sources without proper inspection.

### Least-privilege access

* Create dedicated user accounts (for example, for SQL or SNMP) with minimal permissions.
* Avoid using shared or admin-level credentials for extension data collection.
* When using the API to manage extensions, use personal tokens instead of tokens that have global extension write access.
* Set up security policies that allow editing extension settings, and assign them only to trusted user groups.

  + Use the [Extensions IAM service](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#extensions "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") to restrict who can edit settings, based on specific scopes like extensions, zones, or host groups. This helps you create detailed, secure policies.

### Sensitive data sources

* Make sure your extension doesn't retrieve sensitive information (for example, executing SQL queries).
* Audit your extensions to ensure they do not access or transmit private data unintentionally.

## Troubleshooting in Dynatrace Community

Find solutions to common issues with our expert-written troubleshooting articles.

[Go to troubleshooting forum](https://dt-url.net/6303zdg)