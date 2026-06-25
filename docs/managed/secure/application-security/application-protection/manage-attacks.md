---
title: Manage attacks
source: https://docs.dynatrace.com/managed/secure/application-security/application-protection/manage-attacks
scraped: 2026-05-12T11:37:04.319287
---

# Manage attacks

# Manage attacks

* Explanation
* Updated on Apr 22, 2024

After you [enable and configure Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities."), Dynatrace starts detecting attacks on all monitored applications in your environment. An attack is any request (call) from a certain client IP to your application code with malicious intent (for example, to access or delete protected information with SQL injection) targeting a code-level vulnerability.

## Attacks list

To see the list of attacks in your environment, go to **Attacks**. The following information is displayed.

### Infographic of the key features

![infographic-attacks](https://dt-cdn.net/images/2023-03-14-09-09-23-1579-7f13f156a2.png)

infographic-attacks

* A general overview of how many attacks happened, according to your [selected timeframe](#global) and [management zone](#mz). There are three types of attacks, select any of them for a shortcut to attacks filtered by the respective type:

  + **Exploited:** The attack went through. This happens if the monitoring mode is activated.
  + **Blocked:** The attack was blocked. This happens if the block mode is activated.
  + **Allowlisted:** You allow an attack to go through. This happens when you add an attack to your allowlist.
* Your current global attack control mode (`Monitoring`, `Blocking`, `Off`). Selecting it takes you to the **Application Protection: General settings** page, where you can change your configuration. For details, see [Configure Runtime Application Protection](/managed/secure/application-security/application-protection#config "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").
* **Attack source locations:** A map of the countries from which attacks originated, based on the selected timeframe.

  + The map is colored to indicate the number of attacks coming from certain countries; see the map legend for details. Select a country to view more information about the attacks from that country:

    - **IPs:** Number of unique [IP addresses](#client-ip-address) from which the attacks originated.
    - **Locations:** Number of unique locations within the country from which the attacks originated.
    - **Attacks:** Total number of attacks from the location.
    - **Amount:** An indicator of the number of attacks, from left (zero attacks) to the right (several attacks). An indicator that is all the way to the right means that the selected country has the most attacks originating from it relative to other countries.
    - **Last attacks** is a list of the most recent recorded attacks, displaying the injection type, the source IP of the attacker, the timestamp, and the city.

  To filter the attacks list by the selected country, select **Filter for attacks from this country**.

  + A grayed-out location is one from which no attack was generated during the selected timeframe and therefore no details are available.
* **Attacks over time:** A graph of the number of attacks (exploited, blocked, allowlisted) over the selected timeframe. The default timeframe is `Last two hours`. You can set a different filter in the [global timeframe](#global).

### Attacks detected

![attacks detected](https://dt-cdn.net/images/2024-06-18-11-40-25-1670-17779ad624.png)

attacks detected

A list of detected attacks in your environment.
For optimized performance, a maximum of 500 attacks are displayed at a time. You can narrow down the results by applying [filters](#filter).
To sort the list by any item, select the corresponding column heading. To add or remove column headings, select **Format table**.

#### Attack

* The Dynatrace attack ID (example: `A-2JPGJXQF`)
* A short version of the attack's entry point code location (example: `org.springframework.web.filter.DelegatingFilterProxy.invokeDelegate():135`).
* The name of the attacked process group (example: `BloatedJavaSoftwareGroup-IG-1`)
* The public internet exposure symbol, if there's any public internet exposure. If the symbol is grayed out and crossed out, no public internet exposure was found. If the symbol isn't present, there's no data available.
* The reachable data symbol, if there are any reachable data assets affected. If the symbol is grayed out and crossed out, there are no reachable data assets within range. If the symbol isn't present, there's no data available.

#### Entry point

The HTTP path of the request (example: `/image`).

#### Source IP

The IPv4 or IPv6 address of the attacker.

#### Location

The country from which the attack originated.

#### Type

The exploit type:

* **SQL injection:** Targets a database.
* **Command injection:** Targets a host.
* **JNDI injection:** Targets a host.
* **SSRF:** Targets a host/service.

#### Status

How the attack is controlled, based on your [configuration settings](/managed/secure/application-security/application-protection#config "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities."):

* **Exploited:** The attack went through. This happens if monitoring mode is activated.
* **Blocked:** The attack was blocked. This happens if block mode is activated.
* **Allowlisted:** You allowed an attack to go through. This happens when you add an attack to your allowlist.

#### Timestamp

The time when the attack happened.

#### Details

Expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") attack rows for details, or to perform the following actions:

* Select **Add to allowlist** if you want to add and configure a new exception rule for the attack. For details, see [Define exception rules](/managed/secure/application-security/application-protection/application-protection-rules#exception-rules "Create, modify, and delete rules for specific attacks.").
* Select **Block attack** if you want to add and define a new rule to block the attack. For details, see [Define specific attack control rules](/managed/secure/application-security/application-protection/application-protection-rules#handling-rules "Create, modify, and delete rules for specific attacks.").
* Select **View attack details** to go to the [attack details page](#details).

## Attack details

To see details about an attack, go to **Attacks** and select an attack.
The following information is displayed.

### Attack title

Example title:

![attack title](https://dt-cdn.net/images/2024-06-18-11-43-33-498-d7d7345219.png)

attack title

* The type of exploit (`SQL injection`, `Command injection`, `JNDI injection`, or `SSRF`)
* The Dynatrace attack ID (example: `A-2JPGJXQF`)
* The name of the attacked process group (example: `MembershipService.dll unguard-membership-service-*`)

### Infographic of the key features

![infographic-attack-details](https://dt-cdn.net/images/2022-11-11-12-27-00-1355-c6f3eb1c6a.png)

infographic-attack-details

* Type of attack (`Exploited`, `blocked`, `allowlisted`)
* **Public internet exposure:** If there's any public internet exposure. Possible states are:

  + **Public network:** There is public internet exposure.
  + **Not detected:** No public internet exposure was found.
  + **Not available:** Data isn't available, because the related hosts are running in Infrastructure Monitoring mode. For details, see [Monitoring modes](/managed/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
* **Reachable data assets:** If there are any reachable data assets affected. Possible states are:

  + **Within range:** There are reachable data assets affected.
  + **None within range:** There are no reachable data assets within range.
  + **Not available:** Data isn't available, because the related hosts are running in Infrastructure Monitoring mode. For details, see [Monitoring modes](/managed/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
* **Process group instance:** The name of the affected process.
* **Vulnerability:** The type of injection and location of the vulnerable code.
* **Timestamp:** The time when the attack happened.
* **Source IP:** The IP from which the attack originated.

The following actions are available:

* Select **Add to allowlist** to [add the attack to the allowlist](/managed/secure/application-security/application-protection/application-protection-rules#exception-rules "Create, modify, and delete rules for specific attacks.").
* Select **Block attack** to [block the attack](/managed/secure/application-security/application-protection/application-protection-rules#handling-rules "Create, modify, and delete rules for specific attacks.").

### Attack path

![attack-path](https://dt-cdn.net/images/2022-11-11-12-30-25-1570-938080fffb.png)

attack-path

The attack path is a visual representation of the attack and contains the following steps:

1. **Source IP:** The IP from which the attack originated.
2. **Entry point:** The path of the request containing the malicious payload used for this attack.
3. **Vulnerability:** The code-level vulnerability used.
4. Depending on the injection type:

* **Target:** Displays the attacked host (for command and JNDI injections) or targeted host/service (for SSRF).
* **Database:** Displays the attacked database (for SQL injections).

### Entry point

![Entry point section](https://dt-cdn.net/images/2024-02-14-07-54-51-782-2d98081aea.png)

Entry point section

* **HTTP path:** The HTTP path used for the attack.
* **Entry point function:** The function where the malicious payload was first accessed in the attacked process.
* **Payload:** The HTTP parameter that contains the malicious payload and its value.

### Vulnerability

![vulnerability-attacks](https://dt-cdn.net/images/2022-11-11-12-34-22-786-0e08b656b0.png)

vulnerability-attacks

* **Name:** The code-level vulnerability used.
* **Code location:** The location in the code where the entry point function is called.

  If the location is unavailable, **Code location** isn't displayed.
* **Vulnerable function:** The function that used a part of the attacker's payload, which resulted in the exploitation of the vulnerability.
* Depending on the injection type

  + **SQL statement** (in the case of SQL injection)
  + **Command** (in the case of command injection)
  + **JNDI lookup name** (in the case of JNDI injection)
  + **Request URL** (in the case of SSRF)

The user-controlled input is highlighted.

Select **View vulnerability** to navigate to the [details page of the respective code-level vulnerability](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities#details "Monitor the code-level vulnerabilities in your environment.").

This option is only available if [code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is enabled.

### Process-related logs around attack timestamp

![process-related-logs-attacks](https://dt-cdn.net/images/2022-11-11-12-36-46-1580-8320b03300.png)

process-related-logs-attacks

Process logs that happened around the same time as the attack (+/- 5 min), and which might be related to the attack. To view this information, you need to [configure Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").

Select **View all process-related logs** to navigate to the **Log viewer** page for a list of all process-related logs.

### Identified request

![identified-request-attacks](https://dt-cdn.net/images/2022-11-11-12-38-26-771-85f5991eaf.png)

identified-request-attacks

Details about the malicious request, such as the request, host, user agent, HTTP headers, and parameters.

### Attacks detected

![attacks detected](https://dt-cdn.net/images/2024-06-18-11-52-56-823-f347ec1cd9.png)

attacks detected

* Identifies how many attacks happened on the same vulnerability in the last 30 days, and displays the ratio of exploited, blocked, and allowlisted attacks out of the total number of attacks. If there are several attacks from different IP addresses affecting the same vulnerable location, all respective attacks are attached to the same vulnerability.
* Lists the last five attacks that happened for the last 30 days, with details such as the Dynatrace attack ID (and link to the respective [code-level vulnerability details page](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities#details "Monitor the code-level vulnerabilities in your environment.")), entry point, status (exploited, blocked, allowlisted), source IP, and timestamp.

The following actions are available:

* Select **Application Protection settings** to navigate to the **Application Protection: General settings** page and edit your configuration.
* Select **View all attacks** to go to **Attacks**.

### Attacker details

![attacker-details](https://dt-cdn.net/images/2022-11-11-12-41-50-773-11fe3c8e8f.png)

attacker-details

Details about the attacker, such as:

* **IP:** IP address of the attacker.
* **Timestamp:** Time when the attack happened.
* **Location:** Country of the attacker, derived from the IP address.
* **Attacks:** How many previous attacks happened on the same vulnerability and how many overall, from the same attacker, in the last 30 days.

## Client IP address detection

When web requests are directly sent to a monitored server, Dynatrace identifies the IP addresses of the end users' devices via socket connections. However, when unmonitored components such as load balancers, CDNs, or proxies are used, the remote IP address is different from the original IP address. For such cases, Dynatrace also considers certain HTTP headers. These headers are most frequently used to identify the originating IP address when a client connects to a web server through an HTTP proxy, a CDN, or a load balancer, and are not configurable.

## Filter attacks

There are several ways you can filter attacks, as shown below.

### Filter by global timeframe

You can use the global timeframe selector to filter for attacks that happened during a specific timeframe.

### Filter by management zone

If you filter by a specific management zone, only attacks from that management zone will be displayed. This restriction also affects the **Attack source locations** map, the **Attacks over time** chart, as well as the attack list itself.

Once they occur, attacks are assigned to existing management zones. They can only be part of management zones that exist at the moment of the attack. Creating a management zone for an attack that already happened will not affect it, and the attack won't be part of it.

For information on how to set up and apply management zones, and about the rules that define and limit the entities that can be accessed within a management zone, see [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.").

### Filter by attack details

In the filter bar, the following filters are available.

* **Process group name:** Displays attacks based on a process group name.
* **Entry point:** Displays attacks based on the HTTP request path.
* **Source IP:** Displays attacks based on the exact IPv4 or IPv6 address of the attacker. For details, see [Client IP address](#client-ip-address).
* **Attack source location:** Displays attacks based on the location (country) from which they were generated.
* **Technology**: Displays attacks based on the supported technologies (`Java`, `.NET`).
* **Type:** Displays attacks based on the type of exploit (SQL injection, command injection, JNDI injection, or SSRF).
* **Status:** Displays attacks based on the attack status (`blocked`, `allowlisted`, or `exploited`). For details, see the [configuration settings](/managed/secure/application-security/application-protection#config "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

You can also filter for attack status by selecting any type of attack from the general overview bar on top of the **Attacks** page.

### Filter by attack source location

On the **Attack source locations** map, select any location from which attacks were generated, and then select **Filter for attacks from this country**.

## FAQ

* [How does Dynatrace actually block attacks?](/managed/secure/faq#block-attacks "Frequently asked questions about Dynatrace Application Security.")
* [How is an attacker's IP determined?](/managed/secure/faq#attacker "Frequently asked questions about Dynatrace Application Security.")
* [What's the data retention period for attacks?](/managed/secure/faq#attacks "Frequently asked questions about Dynatrace Application Security.")

## Related topics

* [Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")