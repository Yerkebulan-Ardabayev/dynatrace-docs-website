---
title: Release monitoring Classic
source: https://www.dynatrace.com/docs/deliver/release-monitoring
scraped: 2026-02-18T21:29:53.158842
---

# Release monitoring Classic

# Release monitoring Classic

* Overview
* 1-min read
* Published Sep 14, 2020

The software product lifecycle of a release requires careful management of release risks. Also, as more and more components and versions are deployed, the frequency of releases in your organization increases, and manually collecting release-relevant data can easily become a bottleneck in your release automation pipeline and automated software lifecycle.

Dynatrace offers a built-in release-analysis solution that helps you determine:

* Which versions are deployed across your deployment stages and production environments based on multiple version-detection strategies.
* The release stages of the deployed versions.
* The changelog for a new version.
* Known bugs and whether they're release blockers.
* Risks related to specific versions.
* Which version has an excessive load (for example, if you're temporarily redirecting the load with a canary deployment).
* How the new version is behaving compared to previous versions.
* Issue statistics related to the monitored entities.

## Configure

* Learn how to [configure environment variables for version detection](/docs/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies").
* Optionally, you can [integrate your issue-tracking systems and configure dynamic queries](/docs/deliver/release-monitoring/issue-tracking-integration "Integrate your issue tracker into Dynatrace to pull statistics for monitored entities.").

## Analyze

Once you configure your software/issue tracker, you can [analyze the software product lifecycle of your releases](/docs/deliver/release-monitoring/monitor-releases-with-dynatrace "Analyze data related to each release version of your software.").