---
title: Public Synthetic locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations
scraped: 2026-02-16T21:20:24.823807
---

# Public Synthetic locations

# Public Synthetic locations

* Reference
* 8-min read
* Updated on Feb 08, 2024

Dynatrace offers a global network of public Synthetic Monitoring locations out of the box. With Dynatrace Synthetic Monitoring, you can run your monitors from public locations that are based on the infrastructure of these major cloud providers: Alibaba Cloud, Amazon AWS, Google Cloud, and Microsoft Azure.

Note that you can also [create private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") within your own network infrastructure. All public and private Synthetic locations can run [browser as well as HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.").

## Location release stages

Locations are released in one of these progressive stages: **Coming soon**, **Early Adopter**, or **GA**. Locations can also be **Deprecated**. Learn about the relationship between the stages:

| Stage | Description |
| --- | --- |
| **Coming soon** | Location is already created; we're performing final performance tests before making the location available. |
| **Deprecated** | Location is about to be removed; you can't assign new monitors to a deprecated location. |
| **Early Adopter** | Location is production ready and fully supported. Its future availability depends on the interest the location receives and on vendor-dependent factors. |
| **GA** | Location is generally available and fully supported. |

## Location IP addresses

If your security policy requires you to add a location IP address to a list of allowed addresses or you need to know this information for other purposes, you can determine a location IP address in one of the following ways.

* When you create or modify your monitors, all the locations and their IP addresses are displayed in the table on the **Frequency and locations** page. Select one or more locations, scroll to the bottom of the page, and select **Copy IPs to clipboard** or **Download IPs** to copy or download the associated IP addresses.
* Use the [Synthetic locations API - GET all locations](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "List all synthetic locations via the Synthetic v1 API.") API call, which returns all the locations available for your Environment along with their IP addresses.

## Locations

**All public Synthetic locations are set to Coordinated Universal Time (UTC)**.

Location change notice

**The Alibaba Sydney and Mumbai public locations will be discontinued by the end of March 2024**.

Alibaba has announced the closure of data centers in Australia and India, scheduled to take effect by the end of March 2024.

In anticipation of this change, if you use the Alibaba Sydney or Mumbai locations, we recommend reassigning your monitors to alternative locations to ensure that your tests remain functional. If you prefer not to do this yourself, starting from March 2024, we will automatically transfer your monitors to the alternative public locations listed below.

**Summary of change**

| Location to be deprecated by end March 2024 | Recommended alternative location |
| --- | --- |
| **Sydney (Alibaba)** | **Sydney (AWS)** |
| **Mumbai (Alibaba)** | **Mumbai (AWS)** |

Migrate your monitors

If you have synthetic monitors assigned to the soon-to-be-deprecated Sydney (Alibaba) or Mumbai (Alibaba) locations, we recommend that you assign them to other locations. The alternative Sydney (AWS) and Mumbai (AWS) locations would be your natural first choices, but you can, of course, select other locations.

1. Go to **Synthetic Classic** and select a monitor.
2. On the monitor details page, select **Edit**.
3. Select **Frequency and locations**.
4. Clear the **Sydney** (Alibaba) and **Mumbai** (Alibaba) checkboxes and select alternative locations.
5. **Save changes**.

You can also use the [Synthetic Monitors API](/docs/dynatrace-api/environment-api/synthetic/synthetic-monitors "Manage synthetic monitors via the Synthetic v1 API.") for configuration at scale.

Additional actions to update your firewall rules

While we aim to make this transition as seamless as possible, there are specific tasks we can't perform on your behalf, so you might need to take additional actions.

* If you have applications monitored by Dynatrace Synthetic Monitoring, you might need to adjust your firewall configuration to permit incoming traffic from your selected alternative locations to reach your websites.
* After the end of March 2024, the Alibaba Sydney and Mumbai public locations will no longer be accessible. Consequently, you'll also need to remove the associated IP addresses for these locations from your firewall configuration.

For help on determining the new addresses, see [Location IP addresses](#ip-addresses).

### Africa

| Location | Platform | Stage |
| --- | --- | --- |
| Cape Town | Microsoft Azure | GA |
| Cape Town | Amazon AWS | GA |
| Johannesburg | Microsoft Azure | GA |

### Australia

| Location | Platform | Stage |
| --- | --- | --- |
| Canberra | Microsoft Azure | GA |
| New South Wales | Microsoft Azure | GA |
| Sydney[1](#fn-1-1-def) | Alibaba Cloud | Early Adopter |
| Sydney | Amazon AWS | GA |
| Sydney | Google Cloud | GA |
| Victoria | Microsoft Azure | GA |

1

See [Location change notice](#location-change).

### Asia

| Location | Platform | Stage |
| --- | --- | --- |
| Abu Dhabi | Microsoft Azure | GA |
| Bahrain | Amazon AWS | GA |
| Beijing | Alibaba Cloud | Early Adopter |
| Busan | Microsoft Azure | GA |
| Chennai | Microsoft Azure | GA |
| Dubai | Alibaba Cloud | Early Adopter |
| Dubai | Microsoft Azure | GA |
| Hohhot | Alibaba Cloud | Early Adopter |
| Mumbai | Alibaba Cloud | Early Adopter |
| Hangzhou | Alibaba Cloud | Early Adopter |
| Hong Kong | Alibaba Cloud | Early Adopter |
| Hong Kong | Microsoft Azure | GA |
| Hong Kong | Google Cloud | GA |
| Mumbai | Amazon AWS | GA |
| Mumbai | Microsoft Azure | GA |
| Pune | Microsoft Azure | GA |
| Osaka | Microsoft Azure | GA |
| Qingdao | Alibaba Cloud | Early Adopter |
| Seoul | Amazon AWS | GA |
| Seoul | Microsoft Azure | GA |
| Shanghai | Alibaba Cloud | Early Adopter |
| Shenzhen | Alibaba Cloud | Early Adopter |
| Singapore | Alibaba Cloud | Early Adopter |
| Singapore | Amazon AWS | GA |
| Taiwan | Google Cloud | GA |
| Tokyo | Alibaba Cloud | Early Adopter |
| Tokyo | Amazon AWS | GA |
| Tokyo | Microsoft Azure | GA |
| Zhangjiakou | Alibaba Cloud | Early Adopter |

### Europe

| Location | Platform | Stage |
| --- | --- | --- |
| Amsterdam | Microsoft Azure | GA |
| Belgium West | Google Cloud | GA |
| Berlin | Microsoft Azure | GA |
| Cardiff | Microsoft Azure | GA |
| Dublin | Amazon AWS | GA |
| Dublin | Microsoft Azure | GA |
| Finland South | Google Cloud | GA |
| Frankfurt | Alibaba Cloud | Early Adopter |
| Frankfurt | Amazon AWS | GA |
| Frankfurt | Microsoft Azure | GA |
| Groningen | Google Cloud | GA |
| London | Alibaba Cloud | Early Adopter |
| London | Amazon AWS | GA |
| London | Microsoft Azure | GA |
| Madrid | Google Cloud | Early Adopter |
| Marseille | Microsoft Azure | GA |
| Milan | Amazon AWS | GA |
| Paris | Amazon AWS | GA |
| Paris | Microsoft Azure | GA |
| Oslo | Microsoft Azure | GA |
| Stavanger | Microsoft Azure | GA |
| Stockholm | Amazon AWS | GA |
| ZÃ¼rich | Microsoft Azure | GA |
| ZÃ¼rich | Google Cloud | GA |

### North America

| Location | Platform | Stage |
| --- | --- | --- |
| Cheyenne | Microsoft Azure | GA |
| Chicago | Microsoft Azure | GA |
| Des Moines | Microsoft Azure | GA |
| Iowa | Google Cloud | GA |
| Las Vegas | Google Cloud | GA |
| Los Angeles | Google Cloud | GA |
| Montreal | Amazon AWS | GA |
| Montreal | Google Cloud | GA |
| N. California | Amazon AWS | GA |
| N. Virginia | Amazon AWS | GA |
| Ohio | Amazon AWS | GA |
| Oregon | Amazon AWS | GA |
| Oregon | Google Cloud | GA |
| Quebec City | Microsoft Azure | GA |
| Salt Lake City | Google Cloud | GA |
| San Jose | Microsoft Azure | GA |
| Seattle | Microsoft Azure | GA |
| Silicon Valley | Alibaba Cloud | Early Adopter |
| South Carolina | Google Cloud | GA |
| Texas | Microsoft Azure | GA |
| Toronto | Microsoft Azure | GA |
| Virginia | Alibaba Cloud | Early Adopter |
| Virginia | Microsoft Azure | GA |

### South America

| Location | Platform | Stage |
| --- | --- | --- |
| SÃ£o Paulo | Amazon AWS | GA |
| SÃ£o Paulo | Microsoft Azure | GA |

## Related topics

* [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")
* [Synthetic locations API - GET all locations](/docs/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations "List all synthetic locations via the Synthetic v1 API.")