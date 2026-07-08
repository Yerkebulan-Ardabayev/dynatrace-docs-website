---
title: Dynatrace web UI cookies
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/web-ui-cookies
---

# Dynatrace web UI cookies

# Dynatrace web UI cookies

* Reference
* Published Apr 02, 2026

The following tables list the cookies used in Dynatrace web UI. Due to self-monitoring, [RUM cookies](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.") may also be added. All listed cookies are first-party cookies.

### Dynatrace web UI cookies

The table below contains cookies placed in the Dynatrace web UI for single sign-on (SSO).

| Cookie | Expires | Purpose |
| --- | --- | --- |
| `b925d32c` | Session | Indicates if a user is logged in or not. |
| `ssoCSRFCookie` | Session | Serves as cross-site request forgery (CSRF) protection when moving between servlets in SSO. |
| `p23mn32t` | 5 years | Contains a unique Base32 identifier that indicates to SSO that a user is logging in from a new device. The identifier is created based on the user login, browser, and user agent. |
| `l34kn6no` | Session | Stores the OpenID `state` when SSO acts as a relying party, for example, for signing in with Microsoft using OpenID. |
| `iu2g34bw` | Session | Stores the OpenID `code_verifier` when SSO acts as a relying party, for example, for signing in with Microsoft using OpenID. |
| `a69k21bb` | Session | Stores `redirect_uri` upon successful sign-in when SSO acts as a relying party, for example, for signing in with Microsoft using OpenID. |
| `cgq80xhu` | Session | Contains an SHA-256 hash of a random UUID. When a user signs in via OpenID, this cookie is used to track the session state via the SSO OpenID iFrame and perform frontend logout if necessary. |
| `72ddbc27` | 3 months | Added when a user selects the **Remember me** option to store their credentials. Thanks to this option, the user doesn't have to provide their credentials again when the session expires, and the user is logged in automatically. |
| `kj76fg4h` | 5 minutes | Prevents the user from becoming stuck following a failed federated login if the user selected the **Remember me** option to store their credentials. If the user is signed in, this cookie is deleted. |

### Dynatrace web server cookies

| Cookie | Expires | Purpose |
| --- | --- | --- |
| `SRV` | 1 hour | Load balancer (HA Proxy) session stickiness. |
| `apmsessionid` | Session | Web server session cookie. |