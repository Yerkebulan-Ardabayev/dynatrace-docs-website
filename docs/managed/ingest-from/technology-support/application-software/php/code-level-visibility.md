---
title: Code-level visibility for PHP
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/php/code-level-visibility
---

# Code-level visibility for PHP

# Code-level visibility for PHP

* 2-min read
* Published Jun 12, 2019

Code-level visibility gives you insights into where your PHP code spends the most time and uses the most CPU.

To access the PHP code-level view

1. Go to **Services**.
2. Optional Filter the table by `Technology: PHP`.
3. Select a PHP service.
   Example: PHP request

   ![Dynamic requests](https://dt-cdn.net/images/php1-1595-f396bf2d41.png)

   Dynamic requests
4. Select **View dynamic requests** and then select a PHP request.
5. Select **View response time hotspots**.  
   If you use FPM, select the FPM service and then select **View response time hotspots** to view the entire service or any individual request.
   Example: response time

   ![Response time](https://dt-cdn.net/images/php2-1620-3b68309947.png)

   Response time
6. To view a breakdown of your request's code-level timings, select **Analyze outliers** or refer to the **Response time** tab.
7. To view method-level hotspots in your PHP code, on the **Response time analysis** page, select **PHP execution**.
   Example: PHP execution

   ![PHP execution](https://dt-cdn.net/images/php3-1673-ed6ceb7e1e.png)

   PHP execution
8. To examine CPU consumption of code at the method level, select the **CPU** tab and then select **View method hotspots**, where you can display charts for **Execution time** and **Top APIs**. You can also check **Call hierarchy** and **Hotspots** for the overall contribution of every file/method called.
   Example: view method hotspots

   ![View method hotspots](https://dt-cdn.net/images/php4-1672-5c1658871f.png)

   View method hotspots