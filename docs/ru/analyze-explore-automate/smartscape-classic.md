---
title: Visualize your environment through Smartscape Classic
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape-classic
scraped: 2026-02-18T05:31:17.066531
---

# Visualize your environment through Smartscape Classic

# Visualize your environment through Smartscape Classic

* 8-min read
* Published Jul 19, 2017

![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**, our near real-time environment-topology visualization tool, is one of the most powerful features of Dynatrace.

![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** auto-discovery delivers a quick and efficient visualization of all the topological dependencies in your infrastructure, processes, and services:

* On the vertical axis, it displays full-stack dependencies across all tiers
* On the horizontal axis, it visualizes all ingoing and outgoing call relationships within each tier

With just a few clicks, ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** gives you access to a detailed topological view of your entire environment, giving you more insight into and control over your environment.

* Make better decisions, such as adjusting your service architecture or infrastructure to improve application performance.
* Examine cross-tier and same-tier process, host, and service interdependencies to better understand how dependencies affect the performance of your applications.
* Drill down to gain clearer insight into problems. For example, Dynatrace might identify an issue with third-party dependencies and help you understand the impact of the issue on your application's performance.

## Access Smartscape **Smartscape Classic**

To access the classic Smartscape environment-topology view, go to ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**.

To start, select the view you want to see:

* Select **Show problems** to display a topology of [problems](#problems)
* Select **Show third-party vulnerabilities** and specify risk levels (you can select more than one) to display a topology of [third-party vulnerabilities](#vulnerabilities)

## Problems

When **Show problems** is selected, each ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** tier includes a dedicated tab with a health indicator. Select the tier at which you want to view the topology:

* Applications
* Services
* Processes
* Hosts
* Data centers

Each tier shows a different entity type: application, service, process, host, or data center.

* To view a different tier, select that tier's tab.
* To zoom in and out, use the **+/-** buttons at the top-right corner or rotate the mouse wheel.
* To shift your view to a different position, select and drag anywhere in ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**.
* To view the name of an entity, hover your cursor over the entity's symbol. While the name is displayed, you can select the arrow next to the entity name to go to that entity's overview page.

In the first example image below:

* The **Hosts** tier displays a health status of **1/33**, meaning there are 33 monitored hosts and 1 of them has a problem.
* The other four tiers (**Applications**, **Services**, **Processes**, and **Data centers**) in this example show only the number of entities on each tier, because all the entities on those tiers are healthy.

![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** displays data from the past 72 hours and therefore can't be adjusted using the timeframe selector. To view the dependencies among entities of the same tier, just select the associated tab on the left.

### Applications

In this example, the **Applications** tab is selected and the **12** detected applications in this environment are displayed on the right.

![Smartscape applications](https://dt-cdn.net/images/smartscape-applications-1310-dc4704a941.png)

Dynatrace supports monitoring of web-based applications and mobile apps. The node symbols indicates the application type:

| Icon | Meaning |
| --- | --- |
| Smartscape symbol new | **Web application** |
| Smartscape symbol 2 | **Mobile app** |

There are no application connections or dependencies because, in Dynatrace, applications are viewed from the perspective of the user and therefore only constitute user endpoints. Therefore, multiple applications may use the same services, but applications can't be connected directly to one another.

### Services

The **Services** tab displays the topology of all the services that are running in your environment.

![Smartscape services](https://dt-cdn.net/images/smartscape-services-1621-d595e2d107.png)

**Nodes**

Each node represents a different service with a symbol that signifies the underlying service type.

| Icon | Meaning |
| --- | --- |
| see example above | Commercial logos such as the MySQL dolphin, Apache feather, and Tomcat cat indicate [service technologies supported by Dynatrace](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks."). |
| Smartscape symbol 3 | Services of unrecognized technologies are depicted using a generic service symbol. These are typically [opaque services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services "Understand what opaque services are."). |

**Connections**

* Arrows on connection lines to and from the selected service indicate whether they're incoming or outgoing service calls.
* A dashed connection line indicates that there has been no request between the two services during the last two hours, or that a service hasn't forwarded or received anything during the last two hours.
* A connection ages out and is no longer shown in ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** if the connection has been inactive for more than 72 hours or if a service hasn't received any load during the last 72 hours.

**Filtering your display**  
Open the Browse (**â¦**) menu in the upper-right corner of ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** to hide or show:

* Inactive requests
* Services that aren't connected to other services

Note that you might observe a difference in the number of services presented in **Services** tab of the ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** page versus the **Services** page. This is because ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic** takes a broader scope of service categories into account.

### Processes

The **Processes** tab provides a visualization within which each node corresponds to a process and each connection represents a TCP/IP request.

* Not all processes running in your environment are shown because the number of running processes is often quite high. For clarity, only the [most important processes](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.") are shown.
* Dashed lines show connections between processes that are inactive or have timed out.

![Smartscape processes](https://dt-cdn.net/images/smartscape-processes-1623-2321abf3d3.png)

### Hosts

The **Hosts** tab shows the topology of your infrastructure from the perspective of your hosts.

* Connections represent TCP/IP requests.
* Hosts, whether physical or virtual machines, are signified with the commercial logos of the host operating systems.

![Smartscape hosts](https://dt-cdn.net/images/smartscape-hosts-1659-8c03fceb20.png)

Generic host symbols are used to signify monitoring candidates (unknown hosts that are detected because they receive TCP/IP requests from monitored hosts). We recommend that you install Dynatrace OneAgent on monitoring candidates in your environment whenever possible.

| Icon | Meaning |
| --- | --- |
| Smartscape symbol 4 | monitoring candidate |

Inactive monitoring candidates are monitoring candidates that havenât communicated with a host. Inactive connections between hosts and connections that have timed-out are visualized with dashed lines.

### Data centers

The **Data centers** tab displays nodes that indicate where your hosts reside. If you have physical servers in your infrastructure, the corresponding data center nodes indicate the cities where the data centers are located. These are signified with generic host icons.

If you use virtual servers or you have a PaaS-based infrastructure, the data center nodes will be labeled accordingly (for example, VMware data center, AWS Availability Zone, or Azure region) and visualized with the corresponding company logos.

![Smartscape datacenters](https://dt-cdn.net/images/smartscape-datacenters-1625-63d687b49e.png)

### Cross-tier interconnections

Для просмотра межъярусных связей выберите любую сущность в любом ярусе ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**. Вертикальные зависимости этой сущности будут отображены слева.

В этом примере выбражено веб-приложение с именем `easytravel-dynatrace-dev`. Слева вы можете увидеть, как зависимости приложения простираются вниз до яруса центров обработки данных.

![Smartscape inter 1](https://dt-cdn.net/images/smartscape-inter1-1687-680a65579e.png)

Приложение `easytravel-dynatrace-dev` отображается красным, поскольку испытывает проблему. Двигаясь вниз по связанным зависимостям, мы видим, что это приложение вызывает 27 служб Tomcat и 4 службы ASP/.NET. Эти службы работают на процессах одного и того же типа технологии (те, что показаны красным, испытывают проблемы). Вы можете видеть, что эти процессы находятся на хосте Windows с именем `lr-ws-l02v` (чтобы увидеть эту деталь, наведите курсор на узел хоста). Поскольку неисправные процессы работают на этом хосте, этот хост также неисправен (обратите внимание на красную **1** на плитке **Hosts** слева).

Этот пример показывает, как легко можно обнаружить первопричину проблемы и сократить время ее устранения, изучая связанные сущности в ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**.

## Уязвимости сторонних компонентов

Когда **Show third-party vulnerabilities** (Показать уязвимости сторонних компонентов) выбрано в ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**, выберите **Risk level** (Уровень риска), чтобы указать уровни риска, которые вы хотите отобразить. Вы можете выбрать несколько флажков.

* На левой стороне вертикальный столбец показывает количество затронутых узлов красным цветом и общее количество узлов серым цветом на уровнях процессов и хостов.
* На топологии затронутые узлы отображаются цветом уровня риска:

  + Темно-красный для `Critical` (Критический)
  + Красный для `High` (Высокий)
  + Желтый для `Medium` (Средний)
  + Синий для `Low` (Низкий)

Чтобы увидеть уязвимости для затронутых сущностей, переключитесь на ярус **Processes** (Процессы) или **Hosts** (Хосты). (Уязвимости могут быть связаны с приложением, службой или центром обработки данных, но они не влияют на них напрямую. Только процессы или хосты могут быть затронуты.)

* Чтобы увеличить и уменьшить масштаб, используйте кнопки **+/-** в правом верхнем углу или вращайте колесико мыши.
* Чтобы изменить положение обзора, выберите и перетащите в любом месте ![Smartscape](https://dt-cdn.net/images/smartscape-topology-512-dca23011f9.png "Smartscape") **Smartscape Classic**.
* Чтобы увидеть имя сущности, наведите курсор на символ сущности. Пока отображается имя, вы можете выбрать стрелку рядом с именем сущности, чтобы перейти на страницу обзора этой сущности.
* Для просмотра межъярусных связей выберите любую сущность. Панель слева расширится, чтобы отобразить вертикальные зависимости сущности.

Дополнительную информацию об управлении уязвимостями сторонних компонентов можно найти в разделе [Third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities "Monitor, visualize, analyze, and remediate third-party vulnerabilities, track the remediation progress, and create monitoring rules.").

## Связанные темы

* [What is a monitoring environment?](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") (Что такое среда мониторинга?)
* [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape "Learn about the Dynatrace Topology and Smartscape API.") (Топология и Smartscape API)
* [Performance analysis](/docs/observe/digital-experience/web-applications/analyze-and-use/performance-analysis "Understand the available types of performance analysis that are provided by Dynatrace.") (Анализ производительности)
* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") (Концепции анализа первопричин)
* [Third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities "Monitor, visualize, analyze, and remediate third-party vulnerabilities, track the remediation progress, and create monitoring rules.") (Уязвимости сторонних компонентов)