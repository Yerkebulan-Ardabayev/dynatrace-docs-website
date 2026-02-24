---
title: Data safety guidance for Android
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/user-privacy-for-android
scraped: 2026-02-24T21:24:58.202059
---

# Data safety guidance for Android

# Data safety guidance for Android

* Latest Dynatrace
* 5-min read
* Updated on Sep 15, 2025

Starting July 20, 2022, Google requires you to provide your users with information on how your mobile app collects, protects, and shares their data. This also includes data collected by third-party partners like Dynatrace.

This page can help you with completing the [Data safety formï»¿](https://support.google.com/googleplay/android-developer/answer/10787469#complete_form_steps) in Google Play Console. The questions and data types reflect the Data safety form, but note that the answers reflect the out-of-the-box, default state.

OneAgent might capture additional data through your [manual instrumentation](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk "Learn what OneAgent SDK for Android is."). If you instrument your app to collect additional data, make sure you reflect this in the **Data safety** section in Google Play Console.

To fill out the Data safety form

1. Sign in to Google Play Console, and select the required mobile app.
2. From the menu on the left, go to **Policy** > **App content**.
3. Under **Data safety**, select **Manage**.
4. Complete the Data safety form using the information provided on this page.

## Data collection and security

Use the table below to answer the questions in this section.

## Data types

Select all types of data that your mobile app collects or shares.

The table below contains all data that OneAgent captures by default.

## Data usage and handling

You also need to provide the information on how the data is used and handled for each data type that you've selected in the **Data types** section. Select **Start** to proceed.

Use the table below for all data types captured by OneAgent.

## Related topics

* [Preparing for Google Play's new safety sectionï»¿](https://android-developers.googleblog.com/2021/07/new-google-play-safety-section.html)
* [Provide information for Google Play's Data safety sectionï»¿](https://support.google.com/googleplay/android-developer/answer/10787469)
* [Configure data privacy settings for mobile applications](/docs/observe/digital-experience/mobile-applications/additional-configuration/configure-rum-privacy-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.")