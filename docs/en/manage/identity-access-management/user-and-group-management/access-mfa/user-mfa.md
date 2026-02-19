---
title: Enhance your account security with MFA TOTP
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-mfa/user-mfa
scraped: 2026-02-19T21:20:08.205190
---

# Enhance your account security with MFA TOTP

# Enhance your account security with MFA TOTP

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 05, 2025

**Non-federated users** can choose to increase their user account security by enabling MFA Time-based One-Time Password (TOTP) with their preferred authenticator app. When enabled, they will be prompted to enter the verification code from their registered authenticator app every time they access any environment.

Federated Users

**Federated users** are not required to register or apply MFA, even if MFA is enabled on their environment. Instead, their login is verified by their Identity Provider (IdP) during the login process.

### Enable MFA TOTP for your user account

To enable MFA TOTP

1. Go to the [Account Managementï»¿](https://myaccount.dynatrace.com/accounts) **My profile** > **Security options** tab and select **Add authenticator app**.
2. Enter the verification code sent to your registered email address.
3. Scan the QR code using your phone's camera in your preferred authenticator app. Optionally, you can enter the code by selecting **Can't scan the QR code?**.
4. Enter the code generated into the **One-Time Password** field and select **Add**.

Verification code prompt frequency

Verification code prompts display once during a user login session. To further reduce code verification requests on trusted devices, use the **Remember Me** option on the login screen to instruct the system to remember you on that web browser.

To remove MFA TOTP

1. Go to the [Account Managementï»¿](https://myaccount.dynatrace.com/accounts) **My profile** > **Security options** tab and select **Add authenticator app**.
2. Open the  menu and select **Delete**.
3. Enter the code generated into the **One-Time Password** field and select **Delete**.

## FAQ

While signing up for MFA TOTP, I did not receive a one-time password via email.

Please wait 30 seconds and check your junk email folder.

I signed up for MFA TOTP, but the verification code does not work.

Ensure that you're using the correct code from the Dynatrace entry in your authenticator app and that the code has not timed out.

Can I register another Authenticator app?

Currently, only one authenticator app can be registered at a time. If you want to switch to another authenticator app, do not delete the old app yet. First, remove MFA TOTP by deleting it from [Dynatrace accountï»¿](https://myaccount.dynatrace.com/accounts), and then enable it again with the new authenticator app.

I signed up for MFA TOTP, but Iâm not prompted for a verification code.

Common reasons why you might not be prompted for MFA when accessing Dynatrace:

* You're a federated user, logging in through your federated identity provider (such as Azure AD or Okta). In this case, MFA should be handled by your IdP.
* You're a non-federated user, but you're in the same login session and have previously provided an MFA code.
* You're a non-federated user but have previously chosen the **Remember me** option on the login window and are using the same web browser.