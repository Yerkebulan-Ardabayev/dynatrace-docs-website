---
title: Install a Synthetic-enabled ActiveGate
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/active-gate-for-private-locations-install
scraped: 2026-02-22T21:28:04.704869
---

# Install a Synthetic-enabled ActiveGate

# Install a Synthetic-enabled ActiveGate

* Latest Dynatrace
* How-to guide
* Published Sep 09, 2025

Synthetic-enabled ActiveGate is used exclusively to run synthetic monitors. A clean ActiveGate installation for the purpose of synthetic monitoring disables all other ActiveGate features, including communication with OneAgents. Make sure the host on which you install the ActiveGate has access to the internet.

You can install a Synthetic-enabled ActiveGate from the **Install ActiveGate** wizard in ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**.

1. In **Purpose**, choose **Synthetic**.
2. In **Deployment type**, choose the operating system.
3. Linux only In **Architecture**, keep the default selection: `x86`.
4. [**Generate token**](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") or enter an existing token. This token has the **Download OneAgent and ActiveGate installers** `InstallerDownload` token scope, which allows you to download the ActiveGate installer. Once provided, the token is automatically appended to download and installation commands, which are then displayed in the web UI.

   You can find existing tokens listed on the **Access tokens** page. Note that a token is only displayed once upon creation, after which it's stored encrypted and cannot be revealed. We recommend that you store the token after creation in a password manager so that you can reuse it as needed.
5. Optional Expand **Optional parameters** and:

   * Use the **Support browser monitors** switch to turn off support for browser monitors. If you do so, the Synthetic ActiveGate will be treated as [browserless](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#browserless "Learn how to manage private locations in the Synthetic app.").
   * Assign the ActiveGate to a private Synthetic locationâchoose a location from the dropdown list or create a new one. You can also [assign the ActiveGate to a location](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations#create-private-location "Learn how to manage private locations in the Synthetic app.") after installation when creating or editing the location.
   * Assign the ActiveGate to a [**Network zone**](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") and [**ActiveGate group**](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups."). You can also create a new network zone and ActiveGate group.
6. Download the installer to the target host.
7. Linux only Recommended **Verify signature**ârun the displayed command on the target host to download a certificate file and verify the installer.
8. Linux only Choose a Linux distribution and follow the instructions that precede the **Install ActiveGate as the privileged user** box if there are any.
9. Run the installer with the command provided in the **Install ActiveGate as the privileged user** box, and then follow the instructions displayed in the web UI.

   Linux only The installer automatically downloads Chromium and the dependencies required by the Synthetic engine. On Red Hat, Oracle Linux, and Rocky Linux, you also need to enable repositories from which the installer downloads the dependencies. As a prerequisite for enabling proprietary repositories on Red Hat, you need to register your Red Hat instance. The web UI provides you with all the required commands for doing so, as shown in the example below.

   If the web UIâguided installation fails or you prefer to prepare the host for the Synthetic engine yourself, you can install Chromium and other dependencies [manually or from a custom repository](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/install-chromium-for-linux "Learn how to install Chromium for Linux manually and from custom repositories.").

   ![Commands to install ActiveGate on Red Hat 9](https://dt-cdn.net/images/synth-ag-commands-red-hat-9-2025-04-24-813-39a89e370b.png)
10. Select **Show deployment status** to verify the ActiveGate installation.