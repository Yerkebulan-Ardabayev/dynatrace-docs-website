---
title: Enable Session Replay Classic for web applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/enable-session-replay-web
---

# Enable Session Replay Classic for web applications

# Enable Session Replay Classic for web applications

* How-to guide
* 2-min read
* Updated on Feb 13, 2024

This page describes the prerequisites and the procedure for enabling [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.").

## Prerequisites

Ensure that your system meets the following requirements:

* OneAgent version 1.241+ on all monitored hosts in your environment
* Real User Monitoring enabled for your application
* An active Dynatrace Digital Experience Monitoring license
* Firewalls configured to allow application/octet-stream content coming from your application (some beacons sent by Session Replay are binary)
* The web UI URL has a trusted certificate
* **Frontend Agents - Improved server node balancing** turned on in **Settings** > **Preferences** > **OneAgent features**

* A secondary disk configured to store user session data

Configure the secondary disk

You must store the Session Replay data in a different volume, known as the secondary disk. Therefore, every node in the cluster must have such a volume allocated to it.

Most sessions are estimated to be around 500 kB, the default data retention period is 35 days, and it is always good to have some buffer. Using these estimates, Dynatrace recommends that you calculate the secondary storage size by applying the following formula:

**Storage size =  
Sessions per day × Average session size (500 kB) × Percentage of sessions to record × Retention period (35) × Buffer (1.5)**

To configure the secondary disk

1. Mount the directory outside the transaction store. The transaction store and Session Replay folders must not be nested but parallel. For example, if the `transaction` directory resides at `/mnt1/dynatrace/transaction`, the `session_replay` directory should reside at `/mnt2/dynatrace/session_replay`.
2. Assign the ownership of the directory to the `dynatrace:dynatrace` user.
3. Set the value of the `SERVER_REPLAY_DATASTORE_PATH` property in the `/etc/dynatrace.conf` file to the directory you mounted in Step 1. For example, `SERVER_REPLAY_DATASTORE_PATH = /mnt2/dynatrace/session_replay`.
4. Launch the reconfiguration sequentially on every node with your `reconfigure.sh` file. The path of this file depends on the environment. An example command is `[Path]/dynatrace/install/dynatrace-managed/installer/reconfigure.sh`.

Dynatrace Managed is reconfigured and restarted. Upon restart, the new Session Replay storage location is used.

## Turn on Session Replay Classic

To enable Session Replay

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Enablement and cost control**.
5. Turn on **Enable Session Replay**.

After you've enabled Session Replay, it's time to [configure it](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay Classic.").

No additional configuration is required to set up [agentless monitoring](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").

## Related topics

* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Configure Session Replay Classic for web applications](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay Classic.")
* [Technical restrictions for Session Replay Classic for web applications](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Learn which restrictions apply to Session Replay Classic.")