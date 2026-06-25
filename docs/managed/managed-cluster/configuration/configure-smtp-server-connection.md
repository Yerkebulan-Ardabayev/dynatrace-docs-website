---
title: Configure an SMTP server connection
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-smtp-server-connection
scraped: 2026-05-12T11:36:57.177064
---

# Configure an SMTP server connection

# Configure an SMTP server connection

* Updated on Nov 13, 2023

Use these settings to determine how Dynatrace delivers email notifications, reports, and other communications to users and administrators.

1. Go to **Settings**.
2. Expand **Emails** and select **SMTP server** to display the **Configure SMTP server** page.
3. Start by selecting how you want email to be delivered.

   * **SMTP server with Mission Control fallback** (default setting)  
     Select this to have an SMTP server deliver email but to use Mission Control as a fallback delivery method.

     + As long as your SMTP server is available, your SMTP configuration controls how email is sent (mail server, connection security, etc.).
     + If your SMTP server becomes unavailable, Mission Control delivers your email with sending address `notifications-noreply@dynatrace-managed.com`.
   * **SMTP server**  
     Select this to have an SMTP server deliver email (with no fallback delivery method).

     + Your SMTP configuration controls how your email is sent (mail server, connection security, etc).
     + If your SMTP server becomes unavailable, your email won't be sent.
   * **Mission Control**  
     Select this to have Mission Control send all email.

     + All SMTP server configuration steps described below are unavailable because there is no SMTP server configuration for you to do. Dynatrace takes care of everything for you.
     + The sending address is `notifications-noreply@dynatrace-managed.com`.
4. Set **Connection security** to the security protocol you want to use for your SMTP server. The default is `No encryption` on port `25`.

   * If you change **Connection security**, the **Port** setting automatically changes to match the standard port number for that protocol (see the default port numbers below).
   * If you manually change the **Port** number, your preference is remembered and changing the **Connection security** protocol won't automatically change the **Port** number.

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
5. Set **Mail server** to the address of the SMTP mail server.
6. Set **Port** to the port number of the SMTP mail server. See **Connection security** above for related details.
7. Set **Username** and **Password** if the server requires authentication.
8. Set **Sender email address** to the address that should be displayed as the sender's email address.
9. Set **Email test address** to the address where you want to send test messages.
10. Select **Send test message** to verify your SMTP configuration by sending a test message to **Email test address**.

    * After a moment, a `Sending succeeded` status message is displayed if sending worked.
    * Check the inbox of the **Email test address** account to make sure it received a "Dynatrace Managed: Mail server setup" message with the expected sender email address.
11. Select **Save changes** when the configuration is correct.