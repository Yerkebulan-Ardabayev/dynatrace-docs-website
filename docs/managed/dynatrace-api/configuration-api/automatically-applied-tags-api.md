---
title: Automatically applied tags API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/automatically-applied-tags-api
---

# Automatically applied tags API

# Automatically applied tags API

* Reference
* Published Oct 22, 2018

Deprecated

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "View builtin:tags.auto-tagging settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:tags.auto-tagging`) schema instead.

The **Automatically applied tags** API enables you to manage the rules for automatically applied tags (auto-tags). You can find these settings in the Dynatrace UI at **Settings > Tags > Automatically applied tags**.

[### List all auto-tags

Get an overview of all auto-tags stored in your environment.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-all "View all automatically applied tags of your environment via the Dynatrace API.")[### View an auto-tag

Get the configuration of an auto-tag by configuration ID.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/get-auto-tag "View an automatically applied tag via the Dynatrace API.")

[### Create an auto-tag

Create a new auto-tag with the exact parameters you need.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/post-auto-tag "Create an automatically applied tag via the Dynatrace API.")[### Edit an auto-tag

Update an existing configuration of an auto-tag. You can also create a new auto-tag with the specified ID.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/put-auto-tag "Edit an automatically applied tag via the Dynatrace API.")[### Delete an auto-tag

Delete an auto-tag you no longer need.](/managed/dynatrace-api/configuration-api/automatically-applied-tags-api/del-auto-tag "Delete an auto-tag via the Dynatrace API.")

## Related topics

* [Define and apply tags](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Tags and metadata](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.")