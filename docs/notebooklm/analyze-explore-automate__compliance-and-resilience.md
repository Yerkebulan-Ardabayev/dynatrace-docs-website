# Документация Dynatrace: analyze-explore-automate/compliance-and-resilience
Язык: Русский (RU)
Сгенерировано: 2026-02-20
Файлов в разделе: 2
---

## analyze-explore-automate/compliance-and-resilience/compliance-assistant.md

---
title: Compliance Assistant
source: https://www.dynatrace.com/docs/analyze-explore-automate/compliance-and-resilience/compliance-assistant
scraped: 2026-02-20T21:20:33.637198
---

# Compliance Assistant

# Compliance Assistant

* Latest Dynatrace
* App
* 3-min read
* Updated on Jan 28, 2026
* Preview

About the app

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** collects information from various sources and applications to maintain real-time visibility into the status of compliance across critical applications and systems.

It leverages the Dynatrace platform's observability, security, and other capabilities, enhanced by Dynatrace Intelligence, to bolster its operational resilience and security posture.

Prerequisites

## Set up sources and applications

* To take full advantage of ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, see [Prerequisites](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management#prereq "Configure and enable Security Posture Management in Kubernetes.") and how to [Get started](/docs/secure/xspm#start "Detect, manage, and take action on security and compliance findings.").
* Set up [Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Set up [Dynatrace Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
* [Install](/docs/manage/hub#install "See the information about Dynatrace Hub.") ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Concepts

Use cases

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** supports you in achieving and managing compliance with regulations and certifications out-of-the-box, starting with [DORA (Digital Operational Resilience Act)](#dora).

![Compliance Assistant overview](https://dt-cdn.net/hub/Compliance_Assistant_Preview_qb0fIUx.png)

1 of 1

## Navigate Compliance Assistant

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** provides the following interactions:

* Open reporting template
  Select  **ICT incident reporting notebook** in the upper-right corner of the page to access an incident reporting template in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

  Note that this is a [ready-made document](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Use ready-made documents right out of the box.").
* Open DORA regulation

  Within each widget, you can find a chapter from DORA regulation to which it refers.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Explore in Dynatrace Hub

Manage compliance with automated checks and incident handling out-of-the-box.

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/compliance-assistant/?query=compl&filter=all)

To help achieve a strong DORA compliance posture, Dynatrace:

* Consolidates data from across the Dynatrace security and observability platform to create a comprehensive compliance overview in line with Chapters of DORA.
* Maintains real-time visibility into compliance status across monitored systems.
* Supports reporting of incidents as required by DORA.

## DORA compliance

DORA is an EU regulation that enhances the digital operational resilience of the financial sector. It strives to ensure financial entities can withstand and recover from severe operational disruptions, including cyber-attacks.

## ICT configuration compliance

ICT configuration compliance widget gathers information from **Runecast** and **Security Posture Management** to continuously scan configurations and get an overview of how they meet DORA requirements.

## ICT vulnerabilities

ICT vulnerabilities gathers information from ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** (with `Risk level` filter applied).

## Incidents ICT critical services

Incidents ICT critical services widget gathers information from:

* **Attacks** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks")âif there's a security incident, helps detect and classify an attack on your environment in real time.
* **Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new")âif there's a resilience incident, analyzes abnormal system behavior and performance problems detected by Dynatrace Intelligence.
* Use [segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.") to conveniently filter observability and security incidents impacting a critical service under DORA.

**ICT vulnerabilities** widget shows you most recent resilience and security incidents, but you can view all ICT Observability in **Problems** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") and view all ICT Security incidents in **Attacks** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks").

## ICT Monitoring Coverage

ICT Monitoring Coverage widget gather information from:

* ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**âprevents unexpected outages by detecting and remediating monitoring coverage gaps.

## Use cases

Compliance Assistant enables you to easily achieve and manage your DORA compliance:

* Maintain real-time visibility into the status of DORA compliance across critical applications and systems.
* Consolidate insights from across the Dynatrace platform streamlined to specific regulatory requirements displayed in a tailored view.
* Identify critical incidents and support your team with timely and accurate reporting per DORA requirements.
* Automate reporting by providing automated workflows and templates as prescribed by regulators.

---

## analyze-explore-automate/compliance-and-resilience.md

---
title: Соблюдение требований и устойчивость
source: https://www.dynatrace.com/docs/analyze-explore-automate/compliance-and-resilience
scraped: 2026-02-18T05:47:32.440648
---

# Соблюдение требований и устойчивость

# Соблюдение требований и устойчивость

* Последнее Dynatrace
* Объяснение
* 4-минутное чтение
* Обновлено 28 января 2026 г.

Используя Dynatrace унифицированную наблюдаемость и безопасность, вы можете автоматизировать до 80% технических задач, необходимых для управления соблюдением требований и устойчивостью в крупном масштабе. Этот подход решает динамические глобальные нормативные требования для операционной устойчивости, подчеркивая растущую зависимость от безопасных, устойчивых и надежных ИТ-сред.

## Важность устойчивости в сложном нормативном ландшафте

В современную цифровую эпоху операционная устойчивость имеет первостепенное значение для бизнеса, стремящегося поддерживать бесперебойную работу и защищать свою репутацию. Способность быстро реагировать на инциденты больше не достаточна; организации должны проактивно предотвращать проблемы и управлять рисками, чтобы обеспечить непрерывную доставку услуг. Эта необходимость усиливается все более сложным нормативным и соответствующим ландшафтом, где глобальные стандарты требуют строгих мер для защиты данных, обеспечения непрерывности услуг и смягчения рисков.

Навигация по этим правилам, сохраняя при этом высокие стандарты производительности и безопасности, является сложной задачей. Несоблюдение требований может привести к операционным сбоям, суровым штрафам и ущербу репутации. Следовательно, достижение операционной устойчивости не только означает соблюдение требований, но и обеспечение долгосрочной устойчивости и защиту бизнеса от потенциальных угроз.

## Dynatrace: ваш партнер в соблюдении требований и устойчивости

Возможности соблюдения требований и устойчивости используют ведущую Dynatrace платформу для унифицированной наблюдаемости и безопасности, включая [Compliance Assistant](https://www.dynatrace.com/hub/detail/compliance-assistant/) ![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") приложение для соблюдения требований DORA. Они предлагают комплексное решение для этих проблем, предоставляя функционал, предназначенный для улучшения соблюдения требований и устойчивости в ИТ-средах. Вот как Dynatrace может помочь автоматизировать до 80% технических задач, необходимых для управления соблюдением требований и устойчивостью:

* Понять сложность ИТ-систем в режиме реального времени
* Проактивно предотвратить, расставить приоритеты и эффективно управлять инцидентами производительности и безопасности
* Автоматизировать ручные и рутинные задачи для повышения производительности

## Шаг 1: Понять сложность ИТ-систем в режиме реального времени

Dynatrace помогает вам комплексно картографировать всю ИТ-среду в режиме реального времени. Он дает вам видимость того, какие компоненты отслеживаются, а какие нет, и помогает автоматизировать трудоемкие проверки конфигурации соблюдения требований.

### Обнаружение и покрытие

[Обнаружение и покрытие](/docs/ingest-from/discovery-coverage-app "Обнаружить и устранить пробелы в покрытии мониторинга в крупном масштабе.") ![Обнаружение и покрытие](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Обнаружение и покрытие") помогает предотвратить неожиданные сбои, обнаруживая и устраняя пробелы в покрытии мониторинга во всей вашей организации.

![Обнаружение и покрытие](https://dt-cdn.net/images/image001-1432-0bb965c934.png)

### Smartscape

[Smartscape](/docs/analyze-explore-automate/smartscape-classic "Узнайте, как Smartscape Classic визуализирует все сущности и зависимости в вашей среде.") топология визуализирует отношения между приложениями, услугами, процессами, хостами и центрами данных, подчеркивая проблемы и уязвимости.

![Smartscape](https://dt-cdn.net/images/image002-1432-082bf6d3ac.png)

### Управление безопасностью

[Управление безопасностью](/docs/secure/application-security/security-posture-management-hub "Оцените, управляйте и принимайте меры по неправильной конфигурации и нарушениям безопасности и соблюдению требований.") помогает обнаружить, визуализировать, проанализировать и устранить проблемы безопасности и соблюдения требований, включая неправильную конфигурацию и оценки соблюдения требований.

![Управление безопасностью](https://dt-cdn.net/images/image003-1432-112de6ebf6.png)

### Помощник соблюдения требований

[Помощник соблюдения требований](/docs/analyze-explore-automate/compliance-and-resilience/compliance-assistant "Объедините информацию из Dynatrace платформы наблюдаемости и безопасности в едином панеле.") ![Помощник соблюдения требований](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Помощник соблюдения требований") предоставляет специальный вид, адаптированный для цифрового акта операционной устойчивости (DORA) Европейского Союза.

![Помощник соблюдения требований](https://dt-cdn.net/images/image004-1429-db68e2e050.png)

## Шаг 2: Проактивно предотвратить и расставить приоритеты инцидентов производительности и безопасности

Dynatrace помогает вам сосредоточиться на предотвращении инцидентов до их возникновения, управлении рисками проактивно и расстановке приоритетов инцидентов для устранения, когда они возникают.

### Проблемы

[Проблемы](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро добраться до коренной причины инцидентов в вашей среде.") ![Проблемы](https://dt-cdn.net/images/problems-512-34e46d913e.png "Проблемы") использует Dynatrace Intelligence для автоматического анализа вашей системы и обнаружения аномального поведения, такого как проблемы с производительностью или стабильностью. Он также исследует влияние и коренную причину инцидента и снижает среднее время ремонта (MTTR).

![Проблемы](https://dt-cdn.net/images/image005-1432-d25b248ded.png)

### Уязвимости

[![Уязвимости](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Уязвимости") **Уязвимости**](/docs/secure/vulnerabilities "Расставьте приоритеты и эффективно управляйте уязвимостями в ваших отслеживаемых средах.") - это наша Dynatrace платформа Runtime Vulnerability Analytics для обнаружения, визуализации, анализа, мониторинга и устранения уязвимостей в вашем приложении.

![Уязвимости](https://dt-cdn.net/images/image006-1432-e6c3ac31aa.png)

### Защита приложений в режиме реального времени

[Защита приложений в режиме реального времени](/docs/secure/application-security/application-protection "Настройте и.configure Dynatrace Защиту приложений в режиме реального времени для мониторинга атак и атак, сгенерированных кодом уязвимостей.") помогает вам получить обзор всех атак в вашей среде в режиме реального времени. Используя кодовые идеи и анализ транзакций, Dynatrace Защита приложений в режиме реального времени автоматически обнаруживает атаки на приложения в вашей среде.

![Атаки](https://dt-cdn.net/images/image007-1432-e9d4630b53.png)

### Сторожевой охранник надежности сайта

[Сторожевой охранник надежности сайта](/docs/deliver/site-reliability-guardian "Автоматически проверьте производительность, доступность и целевые показатели емкости ваших критически важных услуг, чтобы принять правильное решение о выпуске.") ![Сторожевой охранник надежности сайта](https://dt-cdn.net/images/site-reliability-guardian-ec19b393a6.svg "Сторожевой охранник надежности сайта") предоставляет автоматический анализ воздействия изменений для проверки доступности услуг, производительности и целевых показателей емкости в различных системах. Это позволяет инженерам платформы DevOps принимать правильные решения о выпуске новых версий и позволяет SRE применять Цели уровня обслуживания (SLO) для своих критически важных услуг.

![Сторожевой охранник надежности сайта](https://dt-cdn.net/images/image008-1428-ba22e79c5e.png)

## Шаг 3: Автоматизировать ручные задачи для повышения производительности

Автоматизация в Dynatrace позволяет вам автоматизировать задачи в вашем ИТ-ландшафте, устранять проблемы и визуализировать процессы для повышения производительности и сосредоточения на стратегических инициативах.

### Рабочие процессы

[Рабочие процессы](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Рабочих процессов - реагируйте на события, планируйте задачи и подключайте услуги.") ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы") собирает серию действий для построения процессов в графических представлениях. Рабочие процессы могут быть запущены вручную, по расписанию или по событиям в Dynatrace, таким как аномалии, обнаруженные Dynatrace Intelligence.

![Рабочие процессы](https://dt-cdn.net/images/image009-1428-01287f82a0.png)

## Связанные темы

* [Dynatrace для руководителей - Безопасность и соблюдение требований](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)

---
