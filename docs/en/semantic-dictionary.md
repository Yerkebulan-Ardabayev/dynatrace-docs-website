---
title: Semantic Dictionary
source: https://www.dynatrace.com/docs/semantic-dictionary
scraped: 2026-02-26T21:16:11.941238
---

# Semantic Dictionary

# Semantic Dictionary

* Latest Dynatrace
* Overview
* Updated on Feb 23, 2026

The Semantic Dictionary defines standardized field names that are used across all types of monitoring data, such as logs, events, spans, metrics, and entities, as well as the different domain-specific data models that use these field names. This is a prerequisite for stable and robust applications and automations.

In Grail, data is organized into records, each comprising a list of fields. Fields in Grail are categorized into two main types: global and domain-specific.

Global fields maintain consistent semantics across the entire Grail product, offering standardized data references. The [Global field reference](/docs/semantic-dictionary/fields "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") contains this list.

Data models represent a group of fields that are tailored to distinct use cases and domains. The [Data models](/docs/semantic-dictionary/model "Overview of Semantic Dictionary giving context to individual fields.") section contains a list of all data models that are used in Grail.

Data models can require additional fields that are unique to specific data models or problem domains and cannot be defined globally. These fields are not part of the Global field reference. Instead, they are only defined within the data model reference.

### Stability levels

The Semantic Dictionary also employs stability levels to indicate the reliability and permanence of fields. Each documented field needs to be assigned to one of the following levels:

* experimental: fields that are in a testing phase and subject to potential changes or removal.
* stable: fields that have a confirmed and reliable status, providing a consistent foundation for data management.
* deprecated: fields that are no longer recommended for use and may be phased out in future releases.

These stability levels help users make informed decisions about field selection and usage, ensuring data consistency and longevity within the Grail ecosystem.

### Contents