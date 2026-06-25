---
title: Mobile Symbolication API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api
scraped: 2026-05-12T11:04:53.894186
---

# Mobile Symbolication API

# Mobile Symbolication API

* Reference
* Published Dec 05, 2018

The Symbolication Service (also known as DSS, or Deobfuscation and Symbolication Service) enables you to symbolicate (iOS and tvOS) or deobfuscate (Android) mobile application crash reports or handled exceptions. This allows you to view the classes and methods in the stack trace in plain text.

The **Mobile Symbolication** API enables you to manage the Android mapping and iOS/tvOS symbol extract files needed to interpret the mobile stack traces when they arrive to Dynatrace.

[### List all symbol files

Get an overview of all symbol files you have.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-all "View all symbol files of your monitoring environment via the Dynatrace API.")[### View storage info

Check the state of the symbol files storage.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-storage-info "View the information on symbol file storage of your monitoring environment via the Dynatrace API.")[### View supported versions

View the supported version of iOS symbol files.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-supported-versions "View the supported version of iOS symbol files via the Dynatrace API.")

[### View files for an app

Get an overview of symbol files of an app.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app "View symbol files of your mobile app via the Dynatrace API.")[### Delete files for an app

Delete all symbol files of an app.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app "Delete all symbol files for your mobile app via the Dynatrace API.")

### View files for a version

[Get an overview](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app-version "View symbol files for a specific version of your mobile app via the Dynatrace API.") of symbol files of an app version.

[### Upload files for a version

Upload a symbol file for an app version.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Upload symbol files for a specific version of your mobile app via the Dynatrace API.")[### Pin files for a version

Pin or unpin symbol files of an app version.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version-pin "Prevent the deletion of mobile symbol files via the Dynatrace API.")[### Delete files for a version

Delete symbol files belonging to an app version.](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/del-files-app-version "Delete symbol files for a specific version of your mobile app via the Dynatrace API.")

## Related topics

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")