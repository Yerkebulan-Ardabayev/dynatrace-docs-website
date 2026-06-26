# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics"

TRANS = {
    "title: View AWS monitoring results": "title: Просмотр результатов мониторинга AWS",
    "# View AWS monitoring results": "# Просмотр результатов мониторинга AWS",
    "* Explanation": "* Пояснение",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Jul 19, 2018": "* Опубликовано 19 июля 2018 г.",
    "## Your home dashboard": "## Домашний дашборд",
    "The **AWS account** tile is included on your home dashboard by default. This tile gives you a high-level overview of the AWS services in your account, distinguishing between healthy and unhealthy services. The contents of this tile vary based on your Amazon account configuration and the services you're running in your environment (EC2, RDS, EBS and ECB).": "Плитка **учётной записи AWS** включена в домашний дашборд по умолчанию. Она даёт общее представление о сервисах AWS в вашей учётной записи, разделяя работоспособные и неработоспособные сервисы. Содержимое плитки зависит от конфигурации учётной записи Amazon и сервисов, запущенных в вашем окружении (EC2, RDS, EBS и ECB).",
    "![AWS dashboard](https://dt-cdn.net/images/aws-dashboard-296-4a8fa91d21.png)": "![AWS dashboard](https://dt-cdn.net/images/aws-dashboard-296-4a8fa91d21.png)",
    "AWS dashboard": "AWS dashboard",
    "## AWS account page": "## Страница учётной записи AWS",
    "Each **AWS account page** gives you an overview of the Amazon services running under that account. On this page you see:": "На каждой **странице учётной записи AWS** отображается обзор сервисов Amazon, работающих в этой учётной записи. На странице можно увидеть:",
    "* Dynamics of your environment. The **Environment dynamics** section shows you daily totals of EC2 instances segmented by Availability Zone. We present a 7 day overview with special attention paid to increases and decreases in total instance numbers.": "* Динамику окружения. В разделе **Environment dynamics** отображаются ежедневные итоги по экземплярам EC2, сегментированным по зонам доступности. Представлен обзор за 7 дней с особым вниманием к росту и уменьшению общего числа экземпляров.",
    "* List of Elastic Load Balancers (ELB) and their backend EC2 instances.": "* Список балансировщиков нагрузки (ELB) и их серверных экземпляров EC2.",
    "* List of monitored cloud services integrating CloudWatch metrics into Dynatrace monitoring.": "* Список отслеживаемых облачных сервисов, интегрирующих метрики CloudWatch в мониторинг Dynatrace.",
    "* List of load balancers in your environment.": "* Список балансировщиков нагрузки в вашем окружении.",
    "* List of Amazon Relational Database Services (RDS) instances": "* Список экземпляров Amazon Relational Database Service (RDS).",
    "* Number of S3 buckets.": "* Количество бакетов S3.",
    "![The Environment dynamics section shows you daily totals of EC2 instances](https://dt-cdn.net/images/aws-environment-dynamics-nosupsrv-1071-bd28ce9f23.png)": "![The Environment dynamics section shows you daily totals of EC2 instances](https://dt-cdn.net/images/aws-environment-dynamics-nosupsrv-1071-bd28ce9f23.png)",
    "The Environment dynamics section shows you daily totals of EC2 instances": "The Environment dynamics section shows you daily totals of EC2 instances",
    "Serverless scenarios aren't instances and won't be displayed as instances in your AWS setup. Integrate with CloudWatch to have them show up as cloud services in Dynatrace.": "Бессерверные сценарии не являются экземплярами и не отображаются как экземпляры в настройках AWS. Интегрируйтесь с CloudWatch, чтобы они отображались как облачные сервисы в Dynatrace.",
    "## Host page": "## Страница хоста",
    "When we discover a monitored host running in Amazon cloud, we include an icon in the upper-left corner to indicate that the machine is cloud-based.": "При обнаружении отслеживаемого хоста, работающего в облаке Amazon, в верхнем левом углу отображается значок, указывающий на принадлежность машины к облаку.",
    "Each **Host** page details the health of the hardware resources that that host relies on.": "На каждой странице **хоста** отображаются подробные сведения о состоянии аппаратных ресурсов, на которых работает данный хост.",
    "For disks we offer both **Disk latency** and **EBS latency** metrics. When it comes to EBS metrics, Dynatrace discovers how local disks and EBS volumes are mapped together. We also detect striped volumes which helps us better understand the logic of your infrastructure.": "Для дисков доступны метрики **задержки диска** и **задержки EBS**. Применительно к метрикам EBS Dynatrace определяет соответствие между локальными дисками и томами EBS. Также обнаруживаются чередующиеся тома, что помогает лучше понять логику инфраструктуры.",
    "For CPU we provide 2 perspectives of CPU usage—AWS perspective (**CPU AWS**: how much AWS CPU resource the EC2 instance consumes) and operating system perspective (**CPU utilization** ). The operating system perspective comes from Dynatrace OneAgent, and includes among other things, process breakdown so that you know what the CPU cycles are used for.": "Для процессора предоставляются 2 перспективы использования ЦП: перспектива AWS (**CPU AWS**: сколько ресурсов ЦП AWS потребляет экземпляр EC2) и перспектива операционной системы (**CPU utilization**). Перспектива операционной системы поступает от Dynatrace OneAgent и включает, в частности, разбивку по процессам, позволяющую понять, на что расходуются циклы ЦП.",
    "For more information, see [Host monitoring with Dynatrace](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring \"Monitor hosts with Dynatrace.\").": "Подробнее см. [Мониторинг хостов с помощью Dynatrace](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring \"Monitor hosts with Dynatrace.\").",
    "## Relational Database Service page": "## Страница Relational Database Service",
    "On each **Relational Database Service** (RDS) page we show you key performance metrics for that RDS instance and its properties, including engine type and version, endpoint, port, and Availability Zone.": "На каждой странице **Relational Database Service** (RDS) отображаются ключевые метрики производительности для данного экземпляра RDS и его свойства: тип и версия движка, эндпоинт, порт и зона доступности.",
    "For multi-Availability Zone, high availability (HA) deployments (RDS running in primary and standby mode), Dynatrace also shows the secondary Availability Zone. When a service disruption affecting the primary zone takes place and your RDS fails over to the secondary Availability Zone, the primary Availability Zone is automatically updated, while other properties (for example, endpoint) remain the same.": "Для развёртываний с несколькими зонами доступности и высокой доступностью (HA), когда RDS работает в режиме «основной/резервный», Dynatrace также отображает вторичную зону доступности. При сбое, затрагивающем основную зону, и переходе RDS на вторичную зону доступности основная зона доступности обновляется автоматически, тогда как остальные свойства (например, эндпоинт) остаются неизменными.",
    "![AWS RDS](https://dt-cdn.net/images/aws-rds-798-44e97675cc.webp)": "![AWS RDS](https://dt-cdn.net/images/aws-rds-798-44e97675cc.webp)",
    "AWS RDS": "AWS RDS",
    "## Smartscape": "## Smartscape",
    "Smartscape shows Availability Zones as data centers. All Amazon services in an Availability Zone belong to the same data center.": "Smartscape отображает зоны доступности как центры обработки данных. Все сервисы Amazon в одной зоне доступности принадлежат одному центру обработки данных.",
    "To help you understand the relationships within your monitoring environment, we enable you to navigate directly to Smartscape from all EC2 instance (host) pages, RDS instance pages, and ELB pages.": "Для понимания взаимосвязей внутри окружения мониторинга можно перейти непосредственно в Smartscape со всех страниц экземпляров EC2 (хостов), страниц экземпляров RDS и страниц ELB.",
    "![Smartscape AWS datacenter az](https://dt-cdn.net/images/smartscape-aws-datacenter-az-1051-35d491b93a.png)": "![Smartscape AWS datacenter az](https://dt-cdn.net/images/smartscape-aws-datacenter-az-1051-35d491b93a.png)",
    "Smartscape AWS datacenter az": "Smartscape AWS datacenter az",
    "## Problems page": "## Страница проблем",
    "When Amazon cloud is identified as the root cause of a problem, or when your cloud-based application suffers from problems, the cloud environment and its performance are factored into our event correlation and root cause analysis.": "Когда облако Amazon определяется как первопричина проблемы или когда облачное приложение испытывает проблемы, облачное окружение и его производительность учитываются при корреляции событий и анализе первопричин.",
    "## Super search": "## Суперпоиск",
    "Any time you need information regarding one of your Amazon services, type the service's name, ID, or other attribute into the search field on the menu bar. You can search based on any of the following attributes:": "Когда нужна информация об одном из сервисов Amazon, введите имя сервиса, его идентификатор или другой атрибут в поле поиска на панели меню. Поиск осуществляется по любому из следующих атрибутов:",
    "* EC2 name, instance ID, IP address, public or private host name": "* имя EC2, идентификатор экземпляра, IP-адрес, публичное или приватное имя хоста;",
    "* RDS name or endpoint": "* имя RDS или эндпоинт;",
    "* EBS volume ID": "* идентификатор тома EBS;",
    "* ELB name": "* имя ELB;",
    "* Auto Scaling Group name": "* имя группы Auto Scaling.",
    "![AWS search](https://dt-cdn.net/images/aws-search-883-2d74fc27c9.png)": "![AWS search](https://dt-cdn.net/images/aws-search-883-2d74fc27c9.png)",
    "AWS search": "AWS search",
}

PASS = set()

build_one(REL, "view-aws-monitoring-results.md", TRANS, PASS)
qa_one(REL, "view-aws-monitoring-results.md")
