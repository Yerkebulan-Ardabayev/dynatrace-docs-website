---
title: Управление состоянием безопасности
source: https://www.dynatrace.com/docs/secure/application-security/security-posture-management-hub
scraped: 2026-02-19T21:23:14.729413
---

# Управление состоянием безопасности

# Управление состоянием безопасности

* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 13 января 2026 г.

Dynatrace Security Posture Management (SPM) позволяет оценивать, управлять и принимать меры по исправлению неправильных конфигураций и нарушений требований по ужесточению защиты и стандартов регуляторного соответствия.

Доступны следующие варианты Security Posture Management.

* **Dynatrace Kubernetes Security Posture Management (KSPM)**: позволяет обнаруживать, анализировать и отслеживать неправильные конфигурации, требования по ужесточению защиты и потенциальные нарушения соответствия в вашем развёртывании Kubernetes.
* **Runecast Cloud Security Posture Management (CSPM)**: предоставляет детальную информацию о состоянии безопасности ваших облачных сред (AWS, Azure и GCP).
* **Runecast VMware Security Posture Management (VSPM)**: предоставляет детальную информацию о состоянии безопасности ваших сред VMware (vCenter и NSX-T).

## Возможности

* Автоматические оценки на соответствие [поддерживаемым стандартам](#support), позволяющие управлять наиболее критическими находками и составлять по ним отчёты.
* Непрерывный анализ и формирование доказательной базы для внутреннего и внешнего аудита.
* Практические выводы, позволяющие

  + Приоритизировать усилия по обеспечению соответствия требованиям
  + Создавать аудиторские доказательства и отчёты для аудиторов и внутренних команд по безопасности и соответствию требованиям

## Как это работает

Security Posture Management (SPM) непрерывно оценивает вашу среду на предмет неправильных конфигураций, нарушений политик и рисков соответствия. Dynatrace собирает данные конфигурации из вашей инфраструктуры и облачных платформ, передаёт их в Grail и нормализует в события безопасности. Затем они оцениваются по требованиям ужесточения защиты и стандартам соответствия. Результаты обновляются в реальном времени по мере изменения среды, помогая вам оставаться защищёнными и готовыми к аудиту.

Краткий обзор см. в статье [Dynatrace Cloud Security Posture Management повышает уровень облачной безопасности с соблюдением требований в реальном времени у гиперскейлеров](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/). Технические подробности см. в разделе [Концепции SPM](/docs/secure/xspm/concepts "Concepts that are specific to the Dynatrace Security Posture Management app.").

## Матрица поддержки

Стандарт соответствия объединяет требования к безопасности, конфигурации и процессам, зачастую основанные на уже устоявшихся руководящих принципах и лучших практиках в области ИКТ-безопасности. Соблюдение этих требований помогает организациям поддерживать требуемый нормативами уровень ужесточения защиты и минимизировать риски в масштабах организации.

Эти стандарты поддерживаются либо нативно, либо через интеграцию Dynatrace с Runecast Analyzer. Нативные стандарты всегда поддерживаются в актуальном состоянии. Dynatrace Security Posture Management поддерживает следующие стандарты и технологии.

| **Стандарты соответствия** | **Kubernetes[1](#fn-1-1-def)** | **AWS** | **Azure** | **GCP** | **vSphere[2](#fn-1-2-def)** | **NSX-T[3](#fn-1-3-def)** |
| --- | --- | --- | --- | --- | --- | --- |
| [BSI C5](#bsic5) |  |  |  |  |  |  |
| [BSI IT-Grundschutz](#bsi-it) |  |  |  |  |  |  |
| [CIS](#cis) |  |  |  |  |  |  |
| [Cyber Essentials](#cyber) |  |  |  |  |  |  |
| [DISA STIG](#stig) |  |  |  |  |  |  |
| [DORA](#dora) |  |  |  |  |  |  |
| [Essential Eight](#essential) |  |  |  |  |  |  |
| [GDPR](#gdpr) |  |  |  |  |  |  |
| [HIPAA](#hipaa) |  |  |  |  |  |  |
| [ISO 27001](#iso) |  |  |  |  |  |  |
| [KVKK](#kvkk) |  |  |  |  |  |  |
| [NIST](#nist) |  |  |  |  |  |  |
| [PCI DSS](#pci) |  |  |  |  |  |  |
| [TISAX](#tisax) |  |  |  |  |  |  |
| [VMware SCG](#vmware) |  |  |  |  |  |  |

1

Поддержка включает upstream Kubernetes, Amazon EKS и Azure AKS. Совместимость ограничена архитектурами процессоров x86-64 и требует версии Kubernetes в соответствии с жизненным циклом поддержки Dynatrace (если иное не указано в конкретном стандарте).

2

Поддерживаемые версии: VMware ESXi 8.0 v1.1.0, VMware ESXi 7.0 v1.4.0, VMware ESXi 6.7 v1.2.0 и VMware ESXi 6.5 v1.0.0.

3

Поддержка NSX-T ограничена версией 3.2 и выше.

## Стандарты соответствия

BSI C5

C5, также известный как [Cloud Computing Compliance Criteria Catalogue](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html), разработан Федеральным ведомством по информационной безопасности Германии (BSI) и определяет базовые требования к безопасному облачному вычислению. Он в первую очередь предназначен для обеспечения высокого уровня доверия к безопасности облачных сервисов. Основываясь на международных стандартах, таких как ISO 27001, C5 идёт дальше, включая дополнительные меры контроля, специально адаптированные к облачным средам.

#### Поддержка версий BSI C5

Поддерживаемая версия: C5:2020.

BSI IT-Grundschutz

Стандарт [Базовой защиты ИТ (IT-Grundschutz)](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html) создан Федеральным ведомством по информационной безопасности Германии (BSI) как надёжная и устойчивая система управления информационной безопасностью (ISMS). IT-Grundschutz в равной мере охватывает технические, организационные, инфраструктурные и кадровые аспекты. Благодаря широкой основе IT-Grundschutz предлагает системный подход к информационной безопасности, совместимый с ISO/IEC 27001.

#### Поддержка версий BSI IT-Grundschutz

Поддерживаемые редакции: 2022 и 2023.

### Center for Internet Security (CIS)

[Center for Internet Security (CIS)](https://dt-url.net/cm03uso) публикует CIS Critical Security Controls (CSC), помогающие организациям улучшить общую защиту кибербезопасности. Эти меры контроля представляют собой рекомендованный набор действий для киберзащиты, предлагающий конкретные и практические способы противодействия наиболее распространённым и опасным атакам. Ключевым преимуществом этих мер является то, что они приоритизируют и сосредотачивают меньшее число действий с высокой эффективностью.

#### Поддержка эталонных показателей CIS

| **Эталонный показатель** | **Облачный провайдер/программное обеспечение сервера** | **Поддерживаемые версии** |
| --- | --- | --- |
| CIS Kubernetes v1.12.0 | Upstream Kubernetes | 1.32, 1.33, 1.34 |
| CIS Kubernetes v1.11.1 | Upstream Kubernetes | 1.29, 1.30, 1.31, 1.32 |
| CIS Amazon Elastic Kubernetes Service (EKS) Benchmark v1.7.0 | Amazon EKS | 1.30, 1.31, 1.32 |
| CIS Azure Kubernetes Service (AKS) Benchmark v1.8.0 | Azure AKS | 1.32, 1.33, 1.34 |
| CIS Amazon Web Services Foundations Benchmark v3.0.0 | AWS | — |
| CIS Microsoft Azure Foundations Benchmark v5.0.0 | Azure | — |
| CIS Google Cloud Platform Foundation Benchmark v1.3.0 | GCP | — |
| CIS VMware ESXi 8.0 Benchmark v1.2.0 | VMware | VMware ESXi 8.0 |
| CIS VMware ESXi 7.0 Benchmark v1.4.0 | VMware | VMware ESXi 7.0 |
| CIS VMware ESXi 6.7 Benchmark v1.2.0 | VMware | VMware ESXi 6.7 |
| CIS VMware ESXi 6.5 Benchmark v1.0.0 | VMware | VMware ESXi 6.5 |

Cyber Essentials

Cyber Essentials — британский стандарт безопасности, направленный на демонстрацию того, что организация внедрила минимальные средства защиты кибербезопасности посредством ежегодных оценок. Он включает основополагающие технические меры контроля для защиты организаций от распространённых онлайн-угроз безопасности. [Схема Cyber Essentials](https://www.ncsc.gov.uk/files/Cyber-Essentials-Requirements-for-Infrastructure-v3-1-January-2023.pdf) — это поддерживаемая правительством структура, созданная Национальным центром кибербезопасности Великобритании (NCSC).

#### Поддержка версий Cyber Essentials

Поддерживаемая версия Cyber Essentials: требования к ИТ-инфраструктуре — v3.1.

DISA STIG

[Security Technical Implementation Guides (STIGs)](https://dt-url.net/cmc3uif) основаны на стандартах Министерства обороны США (DoD). Руководства DISA STIG часто используются в качестве базы в других секторах для обеспечения соответствия стандартам и доступа к сетям DoD. Все организации должны соответствовать стандартам безопасности DISA STIG перед получением доступа к сетям DoD и работой в них.

#### Поддержка DISA STIG

| **STIG** | **Поддерживаемые версии** |
| --- | --- |
| Kubernetes STIG - Ver 2, Rel 4 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| VMware vSphere 8.0 STIG | VMware vCenter 8.0.x, VMware ESXi 8.0.x |
| VMware vSphere 7.0 STIG | VMware vCenter 7.0.x, VMware ESXi 7.0.x |
| VMware vSphere 6.7 STIG | VMware vCenter 6.7.x, VMware ESXi 6.7.x |
| VMware vSphere 6.5 STIG | VMware vCenter 6.5.x, VMware ESXi 6.5.x |
| VMware NSX 4.x STIG | NSX 4.x |
| VMware NSX-T Data Center STIG | NSX 3.x |

DORA

[Закон о цифровой операционной устойчивости (DORA)](https://dt-url.net/xp43uj2) — важный законодательный акт Европейского союза (Регламент (ЕС) 2022/2554). DORA направлен на повышение устойчивости цифровых операций и защиту целостности инфраструктуры финансового рынка в Европейском союзе. Соответствие DORA — это путь к созданию более безопасной и надёжной цифровой среды внутри финансовых учреждений. Закон затрагивает повседневные операции, протоколы безопасности и меры обеспечения соответствия. DORA вступил в силу 17 января 2025 года.

Essential Eight

Стандарт Essential Eight основан на [восьми приоритетных стратегиях снижения рисков](https://www.cyber.gov.au/resources-business-and-government/essential-cybersecurity/essential-eight), разработанных для помощи специалистам по кибербезопасности в снижении последствий инцидентов, вызванных различными киберугрозами. Разработан Австралийским центром кибербезопасности (ACSC), является обязательным для всех некорпоративных (федеральных) государственных структур Австралии и настоятельно рекомендован другим коммерческим организациям.

GDPR

Общий регламент по защите данных (GDPR) — европейский закон о конфиденциальности, разработанный для гармонизации регулирования защиты данных в рамках Европейского союза (ЕС) путём создания единой обязательной базы для всех государств — членов ЕС. [**GDPR.eu**](https://gdpr.eu/) предлагает обширную библиотеку ресурсов для помощи организациям в достижении соответствия GDPR.

HIPAA

Закон о переносимости и подотчётности медицинского страхования 1996 года (HIPAA) обязал Министерство здравоохранения и социальных служб США (HHS) разработать нормы, направленные на защиту конфиденциальности и безопасности определённой медицинской информации. В ответ HHS ввело [Правило конфиденциальности HIPAA и Правило безопасности HIPAA](https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html), которые в настоящее время являются широко признанными стандартами.

#### Поддержка версий HIPAA

Поддерживаемая версия: 5/2005 с редакцией 3/2007.

ISO 27001

[ISO 27001](https://www.iso.org/standard/27001) — один из наиболее признанных в мире стандартов, предлагающий комплексную основу для систем управления информационной безопасностью (ISMS). Он помогает организациям согласовать практики безопасности с международными передовыми практиками и требованиями бизнеса, законодательства и нормативных актов. Стандарт охватывает все аспекты управления информационными рисками — от оценки до обработки рисков, что делает его важнейшим инструментом в постоянно меняющейся сфере кибербезопасности.

#### Поддержка версий ISO 27001

Поддерживаемая версия: ISO 27001/2022.

KVKK

[Закон о защите персональных данных](https://www.kvkk.gov.tr/en/) (тур.: Kişisel Verilerin Korunması Kanunu, KVKK) — турецкое законодательство, регулирующее защиту персональных данных и определяющее правовые обязательства организаций и физических лиц, обрабатывающих персональные данные. Этот закон обеспечивает соответствие техническим требованиям в области защиты данных, доступа к данным и готовности к аудиту, смоделированным по образцу Общего регламента по защите данных (GDPR) Европейского союза.

NIST

[Национальный институт стандартов и технологий (NIST)](https://dt-url.net/5p23u79) публикует NIST SP 800-53, предлагающий меры контроля безопасности и конфиденциальности для информационных систем и организаций. Согласно требованиям Административно-бюджетного управления (OMB), стандарты и политики NIST являются обязательными для всех несекретных систем, эксплуатируемых федеральными агентствами США.

#### Поддержка редакций NIST

| **Редакция** | **Облачный провайдер/программное обеспечение сервера** |
| --- | --- |
| SP 800-53 Rev. 5.1.1 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| SP 800-53 Rev. 5 | AWS, Azure |
| SP 800-53 Rev. 5.1 | VMware vSphere |

PCI DSS

[Стандарт безопасности данных индустрии платёжных карт (PCI DSS)](https://www.pcisecuritystandards.org/document_library/) — набор требований, обеспечивающих безопасную работу компаний, обрабатывающих, хранящих или передающих данные кредитных карт. Разработанный для снижения растущего риска утечки данных в платёжных карточных системах, PCI DSS является важнейшим стандартом для любого бизнеса, принимающего, обрабатывающего или хранящего информацию о платёжных картах.

#### Поддержка версий PCI DSS

Поддерживаемая версия: PCI DSS v4.0.

TISAX

Trusted Information Security Assessment Exchange (TISAX) — ведущий стандарт информационной безопасности в автомобильной промышленности, разработанный Немецкой ассоциацией автомобильной промышленности (VDA). Требования TISAX изложены в [каталоге оценок информационной безопасности (ISA)](https://enx.com/en-US/TISAX/downloads/), которым управляет ассоциация ENX. Эти требования основаны на международном стандарте ISO/IEC 27001 по управлению информационной безопасностью с дополнительными положениями, специально адаптированными к автомобильному сектору.

#### Поддержка версий TISAX

Поддерживаемая версия: VDA ISA 5.1.

VMware SCG

Руководства по конфигурации безопасности VMware (Security Configuration Guides) содержат рекомендации по безопасному развёртыванию и эксплуатации продуктов VMware на основе [VMware Security Configuration Guide](https://www.vmware.com/solutions/security/hardening-guides).

#### Поддержка версий VMware SCG

Поддерживаемая версия: vCenter Server 8.0 Update 3.

## Начало работы

* Чтобы начать работу с Kubernetes Security Posture Management, см. [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.").

* Чтобы начать работу с Cloud Security Posture Management и/или VMware Security Posture Management, см. [Загрузка результатов соответствия Runecast Analyzer](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").

## Дальнейшие шаги

* После настройки Kubernetes Security Posture Management вы можете

  + Обнаруживать, управлять и принимать меры по нахождениям безопасности и соответствия с помощью [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")
  + Запрашивать [события соответствия](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследований**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.")

    - Список примеров DQL на основе событий соответствия для дальнейшего расследования или составления отчётов см. в разделе [Запрос событий соответствия](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

  Попробуйте ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** и [поделитесь отзывом](https://dt-url.net/1m03u6q), чтобы помочь нам улучшить продукт.
* После настройки CSPM/VSPM вы можете

  + Визуализировать данные с помощью нашей панели мониторинга **Security Posture Overview**. Подробнее см. в разделе [Следующие шаги](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer#next "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").
  + Запрашивать [события соответствия](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследований**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.").

    - Список примеров DQL на основе событий соответствия для дальнейшего расследования или составления отчётов см. в разделе [Запрос событий соответствия](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

## Варианты использования

[Соблюдение требований с помощью Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.")

## FAQ

### Как проверить кластер Kubernetes на соответствие стандартам безопасности?

* Чтобы просмотреть статус соответствия кластера, см. [Просмотр статуса соответствия по системам](/docs/secure/xspm/assess-coverage#systems "Review the Security Posture Management coverage of your systems at a glance.").
* Чтобы просмотреть нахождения по кластеру, вы можете [фильтровать и сортировать результаты](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.").
* Контекстная информация для устранения нахождений по кластеру — см. [Получение аналитики](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").

### Можно ли включать или отключать стандарты соответствия?

* Для [Dynatrace Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.") можно управлять стандартами соответствия в **Настройках** Dynatrace, см. [Настройка области оценки](/docs/secure/xspm#configure-assessment "Detect, manage, and take action on security and compliance findings.").
* Для Runecast Cloud Security Posture Management (CSPM) и Runecast VMware Security Posture Management (VSPM) настройте выбор стандартов непосредственно в [Runecast Analyzer](https://www.dynatrace.com/platform/runecast-analyzer/).

### Что можно делать с нахождениями, созданными Dynatrace?

Обзор использования нахождений соответствия см. в разделе [Соблюдение требований с помощью Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### Как обеспечить соответствие критическим нахождениям, созданным Dynatrace?

Рекомендации по повышению уровня соответствия см. в разделе [Соблюдение требований с помощью Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### Как улучшить охват Security Posture Management?

Инструкции см. в разделе [Улучшение охвата](/docs/secure/xspm/assess-coverage#improve "Review the Security Posture Management coverage of your systems at a glance.").

### Почему в моей системе отображаются неуспешные результаты?

Ресурсы вашей системы оцениваются как `Failed` (не соответствующие) согласно правилам, указанным в [поддерживаемых стандартах](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

* Чтобы лучше понять конфигурацию ресурсов и изучить источник правила, см. [Получение аналитики](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").
* Чтобы лучше понять типы результатов, см. [Концепции: Результаты](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.").

### Что произойдёт, если не устранять нахождения?

Поддержание состояния безопасности является основой вашей общей стратегии безопасности. Рассматривайте это как базовую гигиену безопасности — без неё все остальные меры безопасности будут значительно менее эффективными. Со стороны соответствия, неустранение нахождений означает невозможность выявлять, оценивать и исправлять потенциальные проблемы, которые могут привести к неудачам на аудите.

Ручная обработка многочисленных проверок, необходимых для аудитов, быстро становится непосильной задачей, требующей огромных затрат времени. С нашим решением Security Posture Management весь этот процесс автоматизирован, обеспечивая эффективное управление как безопасностью, так и соответствием требованиям.

Игнорирование проблем соответствия несёт риск раскрытия уязвимостей или провала аудита.

### Как исправить проблемы, обнаруженные в среде?

Рекомендации по устранению нахождений см. в разделе [Соблюдение требований с помощью Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### Какие среды можно отслеживать с помощью Security Posture Management?

Список поддерживаемых систем с их версиями и дистрибутивами см. в разделе [Security Posture Management](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

### В каких режимах мониторинга можно развернуть Security Posture Management на Kubernetes?

Работа Security Posture Management на Kubernetes полностью независима от OneAgent и, следовательно, от [режимов мониторинга](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
Анализируемые данные поступают с Kubernetes API Server и Kubernetes Node Configuration Collector через ActiveGate.
Поэтому вы можете использовать ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** с [Kubernetes Platform Monitoring](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring."), где OneAgent не развёрнут.

### Как настроить Security Posture Management для облачных сред?

Настройте Dynatrace [интеграцию с Runecast Analyzer](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").

## Дополнительные ресурсы

* [Основы безопасности Kubernetes: Неправильные конфигурации контейнеров — от теории к эксплуатации](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Революция в облачной безопасности с контекстом наблюдаемости: Dynatrace Cloud Security и CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Расширение возможностей SRE с помощью аналитики уязвимостей во время выполнения и управления состоянием безопасности](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Расширение платформы Dynatrace с помощью CSPM и VSPM](https://www.dynatrace.com/news/blog/extend-the-dynatrace-platform-with-cspm-and-vspm/)
* [Возвращение к Spring4Shell: как Cloud Application Detection and Response (CADR) обеспечивает многоуровневую защиту](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Что такое управление состоянием безопасности Kubernetes? Обеспечение безопасности бизнеса с KSPM](https://www.dynatrace.com/news/blog/kubernetes-security-posture-management-kspm/)
* [Какое решение ИТ-безопасности подходит вашей организации? CSPM vs. KSPM vs. CNAPP](https://dt-url.net/az03zj0)
* [Dynatrace KSPM: трансформация безопасности и соответствия Kubernetes](https://www.dynatrace.com/news/blog/dynatrace-kspm-transforming-kubernetes-security-and-compliance/)
* [Dynatrace Cloud Security Posture Management повышает уровень облачной безопасности с соблюдением требований в реальном времени у гиперскейлеров](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/)

## Связанные темы

* [Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")
