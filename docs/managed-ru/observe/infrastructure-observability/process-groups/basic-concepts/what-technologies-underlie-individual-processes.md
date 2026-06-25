---
title: Какие технологии лежат в основе отдельных процессов?
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes
scraped: 2026-05-12T11:37:47.698559
---

# What technologies underlie individual processes?

# Какие технологии лежат в основе отдельных процессов?

* Reference
* 1-min read
* Published Jul 19, 2017

Dynatrace не только определяет типы процессов в вашей среде (например, Java или .NET), но и понимает технологии, лежащие в их основе. Например, Dynatrace распознаёт, когда Java-процесс работает на базе Tomcat или Jetty — во многих случаях он даже знает версии этих технологий. Эта информация доступна на странице каждого **Process**.

Детальный анализ технологий и версий, лежащих в основе конкретных процессов, позволяет точно определить, где развёрнуты те или иные версии. Это важный первый шаг в диагностике проблем.

Чтобы просмотреть свойства технологий, лежащих в основе процесса:

1. Перейдите в **Hosts**.
2. Выберите хост, на котором выполняется интересующий процесс.
3. В разделе **Processes** на странице **Host** выберите интересующий процесс.
4. На странице **Process** раскройте панель **Properties** в верхней части страницы.

Свойство **Type** указывает основную технологию процесса. Вспомогательные технологии отображаются в свойстве **Technologies**. В свойстве **Technologies** обычно содержатся дополнительные сведения, например версия CLR или Java, а также, возможно, версия SOLR или клиента MongoDB. Примеры ниже позволяют лучше понять типы информации, которую может предоставить Dynatrace.

![Example 1](https://dt-cdn.net/images/2016-08-31-14-56-14-photos-822-1fdc8f7618.png)

Example 1

![Example 2](https://dt-cdn.net/images/2016-09-01-08-56-57-process-deve2e-ruxitlabs-com-deve2e-dynatrace-671-aa158da1b5.png)

Example 2

![Example 3](https://dt-cdn.net/images/2016-08-31-14-56-26-photos-824-77d5e9af35.png)

Example 3

![Example 4](https://dt-cdn.net/images/2016-08-31-14-56-41-photos-824-ccb8f73c23.png)

Example 4