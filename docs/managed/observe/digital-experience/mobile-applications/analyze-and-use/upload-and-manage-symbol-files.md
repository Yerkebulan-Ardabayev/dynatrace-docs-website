---
title: Upload and manage symbol files for mobile applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files
scraped: 2026-05-12T11:19:40.061601
---

# Upload and manage symbol files for mobile applications

# Upload and manage symbol files for mobile applications

* How-to guide
* 8-min read
* Updated on Nov 12, 2025

Android iOS tvOS

For details on source maps for web applications, see [Source map support for JavaScript error analysis](/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis "Learn how source maps make it easy to analyze, reproduce, and fix JavaScript errors.").

Deobfuscation (Android) or symbolication (iOS and tvOS) is the process of making classes and methods human-readable in a crash report stack trace.

The following example is an Android stack trace, before and after deobfuscation:

![Android stack trace before and after deobfuscation](https://dt-cdn.net/images/symbolication-1638-f52b7612e0.png)

Android stack trace before and after deobfuscation

Dynatrace enables you to manage Android mapping files and iOS or tvOS symbol extract files required to interpret mobile stack traces that Dynatrace receives.

Dynatrace supports three different ways of uploading these files:

* Through a symbolication service known as "Deobfuscation and Symbolication Service" (DSS)
* Via the Dynatrace REST API
* Via the Dynatrace Fastlane plugin
* Through the Dynatrace web UI

Currently, Dynatrace only supports symbolication of stack-trace lines from applications and third-party libraries on iOS and tvOS, for which the dSYM files have been provided. Symbolication of system library stack trace lines is not supported.

You can upload a symbol file in any supported format (compressed or uncompressed). Note the following limits:

* Uploaded fileâmust not exceed 100 MiB.
* Uncompressed fileâmust not exceed 500 MiB after decompression (if compressed).

If your file is too large, try compressing it to stay within the 100 MiB upload limit.

You need the **Change monitoring settings** [permission](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment level to upload source maps and symbol files.

## Upload mapping files for Android

For Android, upload your app's mapping files in their original form. You do not need to preprocess these files.

To learn more about mapping files and where to find them, check the [official Android documentationï»¿](https://developer.android.com/studio/build/shrink-code#decode-stack-trace).

Upload mapping files via DSSClient

The DSSClient enables you to deobfuscate mobile application crash reports or handled exceptions.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get the DSSClient**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#get-dssclient "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Upload mapping files via DSSClient**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#upload-mapping-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")

You can use the DSSClient only on machines running macOS.

### Step 1 Get the DSSClient

You can download the DSSClient from the Dynatrace web UI.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Scroll to the bottom of the page, and follow the **DSSClient** link.
6. Run the DSSClient.

   On macOS Catalina, the system denies running the DSSClient on first launch and displays a warning dialog. Cancel the warning dialog; go to **System Preferences** > **Security & Privacy**, and select **Open Anyway** to allow running the DSSClient.  
   This behavior is caused by the DSSClient referencing Xcode's LLDB framework, which is not accepted by Gatekeeper, regardless of the DSSClient being notarized.

### Step 2 Upload mapping files via DSSClient

Upload your app's mapping file to Dynatrace in their original form. Run the following command in the DSSClient:

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 file=/usr/local/mapping.txt server=https://server.com
```

| Option | Definition | Where to find |
| --- | --- | --- |
| -upload | The command flag. | â |
| appId | The application ID Dynatrace uses to identify the app. | Dynatrace web UI > **Mobile** > your app settings > **Instrumentation wizard** |
| apitoken | A private token used for secure REST API communication. | Dynatrace web UI > **Access Tokens** |
| os | The OS that should be processed (`android`). | â |
| bundleId | The app's package name, for example, `com.yourcompany.app`. | â |
| versionStr | The app's version name. | `build.gradle` file |
| version | The app's version code. | `build.gradle` file |
| file | The path to the mapping file you want to upload. | `build/outputs/mapping/release/mapping.txt` |
| server | The URL to the Dynatrace server, for example, `xyz.dynatrace.com`. | â |

For a detailed overview of all possible parameters, start the `DTXDssClient` binary with `-h`.

Should you need to delete the mapping files, use the following command:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=android bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Upload mapping files via REST API

The [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") allows you to automate the upload of Android mapping files.

To upload your app's mapping files to Dynatrace, use the [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Upload symbol files for a specific version of your mobile app via the Dynatrace API.") method.

Upload mapping files via Fastlane plugin

You can leverage the Dynatrace Fastlane plugin to automate the entire process of delivering Android mapping files to Dynatrace.

For more information and detailed instructions, check the [plugin documentationï»¿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) on GitHub.

Upload mapping files via Dynatrace web UI

You can also use the Dynatrace web UI to upload your application's mapping files either via environment settings or application settings.

Environment settings

Application settings

1. In Dynatrace, go to **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. Under **Android**, select **Upload files**.
3. Select your application from the dropdown list.
4. Provide the **Package name**âthe application package name, such as `com.yourcompany.app`.
5. Enter the **Version code** and **Version name**âyou can find these in the `build.gradle` file.
6. Select **Select the file you want to upload** and choose your mapping file.
7. Select **Upload**.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Under **Android**, select **Upload files**.
6. Provide the **Package name**âthe application package name, such as `com.yourcompany.app`.
7. Enter the **Version code** and **Version name**âyou can find these in the `build.gradle` file.
8. Select **Select the file you want to upload** and choose your mapping file.
9. Select **Upload**.

## Upload symbol files for iOS and tvOS

For iOS or tvOS symbolication, you need to preprocess dSYM files using the DSSClient before you can upload them to Dynatrace.

Upload symbol files via DSSClient

The DSSClient enables you to symbolicate mobile application crash reports or handled exceptions.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get dSYM files**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Get the DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Preprocess dSYM files**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Upload symbol extract files via DSSClient**

For iOS, you need to get the dSYM files, preprocess them using the DSSClient, and then upload the resulting files to Dynatrace.

### Step 1 Get dSYM files

Use the dSYM files from the app's `.xcarchive` or build directory.

To download dSYM files using Xcode's app archive

1. From the Xcode menu, select **Window** > **Organizer** > **Archives** > your mobile app.
2. Select the archive with the required app version and build number.
3. Select **Download Debug Symbols**.
4. Right-click the downloaded archive, and select **Show in Finder**. Use the revealed `.xcarchive` file as an input in the DSSClient (see next step).

### Step 2 Get the DSSClient

You can use the DSSClient only on machines running macOS.

You can download the DSSClient from the Dynatrace web UI.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Scroll to the bottom of the page, and follow the **DSSClient** link.
6. Run the DSSClient.

   On macOS Catalina, the system denies running the DSSClient on first launch and displays a warning dialog. Cancel the warning dialog; go to **System Preferences** > **Security & Privacy**, and select **Open Anyway** to allow running the DSSClient.  
   This behavior is caused by the DSSClient referencing Xcode's LLDB framework, which is not accepted by Gatekeeper, regardless of the DSSClient being notarized.

### Step 3 Preprocess dSYM files

Preprocess your app's dSYM files before you upload them to Dynatrace. Run one of the following commands in the DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Step 4 Upload symbol extract files via DSSClient

Upload the processed files to Dynatrace using the DSSClient.

```
DTXDssClient -upload appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app bundleName=App versionStr=1.0 version=1 symbolsfile=/usr/local/app.xcarchive/dSYMs server=https://server.com
```

| Option | Definition | Where to find |
| --- | --- | --- |
| -upload | The command flag. | â |
| appId | The application ID Dynatrace uses to identify the app. | Dynatrace web UI > **Mobile** > your app settings > **Instrumentation wizard** |
| apitoken | A private token that is used for secure REST API communication. | Dynatrace web UI > **Access Tokens** |
| os | The OS that should be processedâeither `tvOS` or `iOS`. | â |
| bundleId | The app's bundleId. | App's target > General > Bundle Identifier |
| bundleName | The app's bundleName. | App's target > General > Display Name |
| versionStr | The app's version string. | App's target > General > Version |
| version | The app's version. | App's target > General > Build |
| symbolsFile | The path to the folder containing the app's dSYM files. | `your_app_name.xcarchive/dSYMs` |
| server | The URL to the Dynatrace server, for example, `xyz.dynatrace.com`. | â |

For a detailed overview of all possible parameters, start the `DTXDssClient` binary with `-h`.

Should you need to delete the symbol files, use the following command:

```
DTXDssClient -delete appid=aa-bb-cc-dd-ee apitoken=Z-123aefc os=ios bundleId=org.comp.app versionStr=1.0 version=1 server=https://server.com
```

Upload symbol files via REST API

The [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") enables you to automate the upload of your symbol files.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get dSYM files**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Get the DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Preprocess dSYM files**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Upload processed files to Dynatrace via API**

For iOS, you need to get the dSYM files, preprocess them using the DSSClient, and then upload the resulting files to Dynatrace.

### Step 1 Get dSYM files

Use the dSYM files from the app's `.xcarchive` or build directory.

To download dSYM files using Xcode's app archive

1. From the Xcode menu, select **Window** > **Organizer** > **Archives** > your mobile app.
2. Select the archive with the required app version and build number.
3. Select **Download Debug Symbols**.
4. Right-click the downloaded archive, and select **Show in Finder**. Use the revealed `.xcarchive` file as an input in the DSSClient (see next step).

### Step 2 Get the DSSClient

You can use the DSSClient only on machines running macOS.

You can download the DSSClient from the Dynatrace web UI.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Scroll to the bottom of the page, and follow the **DSSClient** link.
6. Run the DSSClient.

   On macOS Catalina, the system denies running the DSSClient on first launch and displays a warning dialog. Cancel the warning dialog; go to **System Preferences** > **Security & Privacy**, and select **Open Anyway** to allow running the DSSClient.  
   This behavior is caused by the DSSClient referencing Xcode's LLDB framework, which is not accepted by Gatekeeper, regardless of the DSSClient being notarized.

### Step 3 Preprocess dSYM files

Preprocess your app's dSYM files before you upload them to Dynatrace. Run one of the following commands in the DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Step 4 Upload processed files to Dynatrace via API

Upload the processed symbol files using the [`PUT upload file for an app version`](/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version "Upload symbol files for a specific version of your mobile app via the Dynatrace API.") method.

Upload symbol files via Fastlane plugin

You can leverage the Dynatrace Fastlane plugin to automate the entire process, including getting dSYMs files from App Store Connect, preprocessing the files, and uploading the files to Dynatrace.

For more information and detailed instructions, check the [plugin documentationï»¿](https://github.com/Dynatrace/fastlane-plugin-dynatrace) on GitHub.

Upload symbol files via Dynatrace web UI

You can also use the Dynatrace web UI to upload symbol files to Dynatrace.

![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Get dSYM files**

![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Get the DSSClient**

![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Preprocess dSYM files**

![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Upload processed files via Dynatrace web UI**

For iOS, you need to get the dSYM files, preprocess them using the DSSClient, and then upload the resulting files to Dynatrace.

### Step 1 Get dSYM files

Use the dSYM files from the app's `.xcarchive` or build directory.

To download dSYM files using Xcode's app archive

1. From the Xcode menu, select **Window** > **Organizer** > **Archives** > your mobile app.
2. Select the archive with the required app version and build number.
3. Select **Download Debug Symbols**.
4. Right-click the downloaded archive, and select **Show in Finder**. Use the revealed `.xcarchive` file as an input in the DSSClient (see next step).

### Step 2 Get the DSSClient

You can use the DSSClient only on machines running macOS.

You can download the DSSClient from the Dynatrace web UI.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Scroll to the bottom of the page, and follow the **DSSClient** link.
6. Run the DSSClient.

   On macOS Catalina, the system denies running the DSSClient on first launch and displays a warning dialog. Cancel the warning dialog; go to **System Preferences** > **Security & Privacy**, and select **Open Anyway** to allow running the DSSClient.  
   This behavior is caused by the DSSClient referencing Xcode's LLDB framework, which is not accepted by Gatekeeper, regardless of the DSSClient being notarized.

### Step 3 Preprocess dSYM files

Preprocess your app's dSYM files before you upload them to Dynatrace. Run one of the following commands in the DSSClient:

```
# For dSYM files downloaded using Xcode's app archive



DTXDssClient -decode symbolsfile=easyTravelApp.xcarchive



# For dSYM files from App Store Connect



DTXDssClient -decode symbolsfile=appDsyms.zip
```

### Step 4 Upload processed files via Dynatrace web UI

You can also use the Dynatrace web UI to upload symbol files either via environment settings or application settings.

Environment settings

Application settings

1. In Dynatrace, go to **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.
2. Under **iOS** or **tvOS**, select **Upload files**.
3. Select your application from the dropdown list.
4. Provide the **Bundle identifier**âthis is the application `bundleId` that can be found in **App's target** > **General** > **Bundle Identifier**.
5. Enter the **Bundle version** from **App's target** > **General** > **Version** and the **Bundle version string** from **App's target** > **General** > **Build**.
6. Select **Select the file you want to upload** and open your symbol file.
7. Select **Upload**.

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.
5. Under **iOS** or **tvOS**, select **Upload files**.
6. Provide the **Bundle identifier**âthis is the application `bundleId` that can be found in **App's target** > **General** > **Bundle Identifier**.
7. Enter the **Bundle version** from **App's target** > **General** > **Version** and the **Bundle version string** from **App's target** > **General** > **Build**.
8. Select **Select the file you want to upload** and open your symbol file.
9. Select **Upload**.

## Manage uploaded symbol files

You can use the Dynatrace web UI to manage the previously uploaded Android mapping files and iOS or tvOS symbol extract files.

To list the uploaded symbol files for a particular application

1. Go to **Mobile**.
2. Select the mobile application that you want to configure.
3. Select **More** (**â¦**) > **Edit** in the upper-right corner of the tile with your application name.
4. From the application settings, select **Symbol files**.

To list the uploaded source maps and symbol files for all your applications

1. Go to **Settings**.
2. Select **Web and mobile monitoring** > **Source maps and symbol files**.

The page displays the amount of storage that is currently used and the storage limit. When the storage limit is reached, Dynatrace begins deleting source maps and symbol files, starting with the oldest ones.

For Dynatrace Managed, the default storage size for symbol and mapping files is 1 GiB. You can modify the storage size according to your requirements.

To free up space, you can manually delete files that you no longer need. Select **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") in the row of the file you want to delete.

To prevent files from being automatically deleted when the storage limit is reached, turn on **Pinned** for the source maps and symbol files that you want to keep.

Alternatively, you can use the [Mobile Symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.") to view, pin, or delete your symbol files.