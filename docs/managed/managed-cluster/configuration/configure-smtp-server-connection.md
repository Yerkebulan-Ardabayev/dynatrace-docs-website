---
title: Configure SMTP server connection
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-smtp-server-connection
---

# Configure SMTP server connection

# Configure SMTP server connection

* How-to guide
* 3-min read
* Updated on Jun 18, 2026

To configure how your Managed Cluster delivers email to users and administrators, follow these steps.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Open SMTP server settings**](/managed/managed-cluster/configuration/configure-smtp-server-connection#open-smtp-server-settings "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Choose delivery method**](/managed/managed-cluster/configuration/configure-smtp-server-connection#choose-delivery-method "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure connection security**](/managed/managed-cluster/configuration/configure-smtp-server-connection#configure-connection-security "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Enter server details**](/managed/managed-cluster/configuration/configure-smtp-server-connection#enter-server-details "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Test and save**](/managed/managed-cluster/configuration/configure-smtp-server-connection#test-and-save "Learn how to configure an SMTP server connection on your Managed Cluster, including connection security, mail server settings, and delivery method options.")

## Step 1 Open SMTP server settings

1. In the Cluster Management Console, go to **Settings** > **Emails** > **SMTP server**.
2. Dynatrace Managed displays the **Configure SMTP server** page.

## Step 2 Choose delivery method

Select how you want email to be delivered.

* **SMTP server with Mission Control fallback** (default setting)  
  Select this to have an SMTP server deliver email but to use Mission Control (MC) as a fallback delivery method.

  + As long as your SMTP server is available, your SMTP configuration controls the mail server, connection security, and sender settings.
  + If your SMTP server becomes unavailable and MC email fallback is available for your cluster, MC attempts to deliver the email.
* **SMTP server**  
  Select this to have an SMTP server deliver email (with no fallback delivery method).

  + Your SMTP configuration controls the mail server, connection security, and sender settings.
  + If your SMTP server becomes unavailable, your email won't be sent.
* **Mission Control**  
  Select this to have MC send all email.

  + All SMTP server configuration steps described below are unavailable because there is no SMTP server configuration for you to do. Dynatrace Managed sends email through MC.

## Step 3 Configure connection security

Set **Connection security** to the security protocol you want to use for your SMTP server. The default is `No encryption` on port `25`.

* If you change **Connection security**, the **Port** setting automatically changes to match the standard port number for that protocol (see the default port numbers below).
* If you manually change the **Port** number, Dynatrace Managed remembers your preference and changing the **Connection security** protocol won't automatically change the **Port** number.

* `No encryption`: Not secure. Default port: `25`.  
  Send email unencrypted. Use this option only if the SMTP server supports no other option.
* `SSL/TLS required`: Secure. Default port: `465`.

  + If an SSL/TLS connection can be established, send encrypted email using SSL/TLS.
  + If an SSL/TLS connection can't be established, don't send email.
* `STARTTLS optional`: Not secure. Default port: `587`.

  + If a STARTTLS connection can be established, send encrypted email using STARTTLS.
  + If a STARTTLS connection can't be established, send email without encryption.
* `STARTTLS required`: Secure. Default port: `587`.

  + If a STARTTLS connection can be established, send encrypted email using STARTTLS.
  + If a STARTTLS connection can't be established, don't send email.

## Step 4 Enter server details

1. Set **Mail server** to the address of the SMTP mail server.
2. Set **Port** to the port number of the SMTP mail server. For details on connection security settings, see [Configure connection security](#configure-connection-security).
3. Set **Username** and **Password** if the server requires authentication.
4. Set **Sender email address** to the address that should be displayed as the sender's email address.
5. Set **Email test address** to the address where you want to send test messages.

## Step 5 Test and save

1. Select **Send test message** to verify your SMTP configuration by sending a test message to **Email test address**.

   * After a moment, Dynatrace Managed displays a `Sending succeeded` status message when sending succeeds.
   * Check the inbox of the **Email test address** account to make sure it received a "Dynatrace Managed: Mail server setup" message with the expected sender email address.
2. Select **Save changes** when the configuration is correct.

After you save the configuration, Dynatrace Managed uses the selected delivery method for email to users and administrators.