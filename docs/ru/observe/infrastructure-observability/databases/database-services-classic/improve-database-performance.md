---
title: Improve database performance
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance
scraped: 2026-02-26T21:29:20.096294
---

# Improve database performance

# Improve database performance

* How-to guide
* 6-min read
* Published Mar 20, 2019

Databases are sophisticated applications, and database access is a core feature of many applications. To avoid failures or poor performance, it's important that your databases be hosted securely and resourced well enough to perform at their best.

You can optimize your databases with:

* Server data that supports host health monitoring
* Hypervisor and virtual machine metrics that support monitoring of your virtualization layer
* Application data that optimizes database access
* Network data that provides insight into the network impact of database communications

With the following few steps for simple database performance tuning, you can significantly speed up most applications.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Check the health of your database**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-health "Boost your database performance in a few practical steps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Understand how your database is accessed**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-access "Boost your database performance in a few practical steps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Understand the load and individual response time of each service instance**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#load-and-response-time "Boost your database performance in a few practical steps.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Check the number of database connections**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#database-connections "Boost your database performance in a few practical steps.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Check your network**](/docs/observe/infrastructure-observability/databases/database-services-classic/improve-database-performance#check-network "Boost your database performance in a few practical steps.")

## Step 1 Check the health of your database

The first step is to ensure that the host serving your database process has sufficient resources such as CPU, memory, and disk space.

### CPU

* Equip each host with a minimum of two CPU cores. Matching the CPU count of your host helps with:

  + Ensuring host responsiveness, because database servers induce a continuous base load on machines.
  + Preventing overspending or hardware limitations, because database-server licensing is affected by the number of CPUs.
* When monitoring virtual machines, monitor the host that the virtual machines run on as well. This provides a more complete picture than the CPU metrics of individual virtual machines, which generate insights only on the respective CPU time availability.

  ![CPU metrics](https://dt-cdn.net/images/cpu-1198-a20fe73396.png)

### Memory

* In addition to monitoring the **Memory usage** metric, monitor **Page faults** per second to learn how much additional memory is required. Having thousands of page faults per second indicates that your host is out of memory.

  ![Host memory usage](https://dt-cdn.net/images/host-memory-analysis-page-faults-2372-02f34bdaa5.png)

### Disk space

* Ensure that storage availability for your database server is higher than the disk space required for the data.

  Because of indices and other performance improvements, databases might use more disk space than required by the data itself. For example, NoSQL databases (such as Cassandra and MongoDB) consume a lot more disk space than expected. Compared to common SQL databases, MongoDB databases might consume less RAM but more disk space.
* Ensure that your database runs on dedicated hard drives to reduce disk fragmentation caused by other processes.
* Check **Disk latency**.

  Depending on the hard drive load, disk latency can increase, leading to a reduction in database performance. You can prevent high disk latency by leveraging the caching mechanisms of your application and database as much as possible.

  ![Disk latency](https://dt-cdn.net/images/host-disk-latency-2060-80803a8edc.png)
* If the results of the measures above aren't satisfactory, consider the following.

  1. Add additional hard drives.

     Read performance can be multiplied by simply mirroring hard drives. Write performance benefits from using RAID 1 or RAID 10 instead of RAID 6.
  2. Try solid-state drives.

     Ensure that you select a model designed for database usage, because databases apply more read/write cycles to storage than most common applications. Solid-state drives are more expensive than traditional hard disks but offer a substantial boost in performance.

## Step 2 Understand how your database is accessed

Once your database resides on healthy hardware, take a look at the applications that access it. If you know of an application or service that has bad database performance, donât assume that it's the application that's affecting the performance of your databaseâit may be another application or service entirely.

![Database overview | Unified analysis](https://dt-cdn.net/images/database-ua-overview-3502-2a520ae771.png)

Reduction in database performance can affect the entire database or a single client.

* If all clients experience bad performance, check if the host is healthy. In most cases, the cause is hardware that isn't capable of handling the work.
* If only a single service suffers from poor response times, dig deeper into the serviceâs metrics to find the root cause of the problem.

## Step 3 Understand the load and individual response time of each service instance

When a service has poor database performance, you can analyze its communication with the database via **database statements**. You can gain insights into the number of executed queries, the query execution frequency per request, the number of rows each query returns, and so on.

![Database details page](https://dt-cdn.net/images/database-details-page-1293-85e42be938.png)

* If you're running multiple **service instances**, check if all the instances are affected rather than a single service instance.

* Check how often the queries are called per request. You might be able to reduce the number of database queries by improving the database cache of your service. If a single query is executed more than once per request, you can unlock potential performance by applying smart caching strategies.

## Step 4 Check the number of database connections

You might continue to face poor database performance even when database queries are correctly configured. In such cases, check that the applicationâs database connection pool is correctly sized.

When configuring a connection pool, consider the following:

* The maximum number of connections the database can handle
* The correct size connection pool required for the application

Because your application may not be the only client connected to the database, ensure that the connection pool size isn't set to the maximum. If the application takes up all the connections, the database server wonât perform as expected.

How to determine the maximum number of connections

The maximum number of connections to the database is a function of the resources in the database. To find the maximum number of connections, gradually increase the load and the number of allowed connections to your database.

While doing this, keep an eye on your database serverâs metrics: CPU, memory, and disk performance. Once any of these maxes out, youâve reached the limit. If the number of available connections isn't enough for your application, consider upgrading your hardware.

To learn more about the database connection pool size, see [About Pool Sizingï»¿](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing).

How to determine the correct size for your application connection pool

The number of allowed concurrent connections to your database is equivalent to the amount of parallel load that your application applies to the database server. There are certain tools that you can use to determine the right number.

Increasing the load leads to higher transaction response times, even if your database server is healthy. Measure the transaction response time from end-to-end to see if **Connection acquisition** time increases under heavy load. If that's the case, your connection pool may be exhausted. If not, review your database server metrics to determine the maximum number of connections that your database can handle.

A connection poolâs size should be constant. Therefore, set the minimum and maximum pool sizes to the same value.

## Step 5 Check your network

Physical constraints of your virtualized infrastructure can affect database performance; cables can fail and routers can break. Network metrics generate insights into non-virtual problems. For example, if problems appear after months or even years of flawless operation, your infrastructure might be suffering physical problems. Check your routers, cables, and network interfaces.

![Host process analysis](https://dt-cdn.net/images/host-process-analysis-1922-6b4f5157a1.png)

Most often, over-stressed processes start dropping packets when resources are depleted. If your network issue isn't hardware based, process-level visibility can help you identify any failing component.

## Related topics



* [Host monitoring with Dynatrace](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.")