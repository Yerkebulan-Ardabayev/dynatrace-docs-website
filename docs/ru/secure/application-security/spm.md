---
title: Security Posture Management
source: https://www.dynatrace.com/docs/secure/application-security/spm
scraped: 2026-03-06T21:17:09.176526
---

# Security Posture Management

# Security Posture Management

* Последняя Dynatrace
* Практическое руководство
* Обновлено 23 февраля 2026 г.

Содержание страницы

* [Изучите возможности Security Posture Management](#capabilities)
* [Как SPM оценивает и анализирует вашу позицию](#mechanism)
* [Проверьте поддерживаемые стандарты и технологии](#support)
* [Как начать работу с SPM](#start)
* [Что можно сделать с SPM далее](#next)
* [Обзор типичных сценариев использования](#use-cases)
* [Часто задаваемые вопросы](#faq)

Dynatrace Security Posture Management (SPM) позволяет оценивать, управлять и принимать меры в отношении неправильных конфигураций и нарушений руководств по усилению безопасности и стандартов нормативного соответствия.

## Возможности

Security Posture Management обеспечивает всестороннюю видимость состояния безопасности ваших сред Kubernetes, облака и VMware. В зависимости от вашей инфраструктуры доступны следующие варианты:

* **Dynatrace Kubernetes Security Posture Management (KSPM)**: Позволяет обнаруживать, анализировать и отслеживать неправильные конфигурации, руководства по усилению безопасности и потенциальные нарушения соответствия в ваших развёртываниях Kubernetes.
* **Runecast Cloud Security Posture Management (CSPM)**: Предоставляет глубокую видимость состояния безопасности ваших сред AWS, Azure и GCP.
* **Runecast VMware Security Posture Management (VSPM)**: Предоставляет глубокую видимость состояния безопасности ваших сред VMware, включая vCenter и NSX-T.

Во всех вариантах SPM предоставляет единый набор ключевых возможностей:

* Автоматизированные оценки по [поддерживаемым стандартам соответствия](#support), позволяющие управлять и отчитываться по наиболее критичным результатам.
* Непрерывный анализ и создание свидетельств для целей внутреннего и внешнего аудита.
* Действенные результаты, помогающие:

  + Приоритизировать усилия по обеспечению соответствия
  + Создавать свидетельства и отчёты для аудиторов и внутренних команд безопасности и соответствия

## Как это работает

Security Posture Management непрерывно оценивает вашу среду на предмет неправильных конфигураций, нарушений политик и рисков соответствия. Dynatrace собирает конфигурационные данные из вашей инфраструктуры и облачных платформ, передаёт их в Grail и нормализует в события безопасности. Затем они оцениваются на соответствие руководствам по усилению безопасности и стандартам соответствия. Результаты обновляются в реальном времени по мере изменения вашей среды, помогая поддерживать безопасность и готовность к аудиту.

Для быстрого ознакомления см. [Dynatrace Cloud Security Posture Management повышает облачную безопасность с помощью соответствия в реальном времени для гиперскейлеров](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/).

## Матрица поддержки

Security Posture Management поддерживает ряд стандартов соответствия через два типа покрытия: нативная поддержка Dynatrace и поддержка через интеграцию с Runecast. Нативные стандарты поддерживаются непосредственно Dynatrace и поддерживаются в актуальном состоянии.

В таблице ниже показано, какие стандарты поддерживаются и как обеспечивается каждый из них.

Для подробных описаний каждого стандарта соответствия и как Dynatrace его поддерживает, см. [Стандарты соответствия Security Posture Management](spm/compliance-standards.md "Технические подробности о поддерживаемых стандартах соответствия.").

| **Стандарты соответствия** | **Kubernetes[1](#fn-1-1-def)** | **AWS** | **Azure** | **GCP** | **vSphere[2](#fn-1-2-def)** | **NSX-T[3](#fn-1-3-def)** |
| --- | --- | --- | --- | --- | --- | --- |
| [BSI C5](spm/compliance-standards.md#bsic5 "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [BSI IT-Grundschutz](spm/compliance-standards.md#bsi-it "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [CIS](spm/compliance-standards.md#cis "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [Cyber Essentials](spm/compliance-standards.md#cyber "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [DISA STIG](spm/compliance-standards.md#stig "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [DORA](spm/compliance-standards.md#dora "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [Essential Eight](spm/compliance-standards.md#essential "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [GDPR](spm/compliance-standards.md#gdpr "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [HIPAA](spm/compliance-standards.md#hipaa "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [ISO 27001](spm/compliance-standards.md#iso "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [KVKK](spm/compliance-standards.md#kvkk "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [NIST](spm/compliance-standards.md#nist "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [PCI DSS](spm/compliance-standards.md#pci "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [TISAX](spm/compliance-standards.md#tisax "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |
| [VMware SCG](spm/compliance-standards.md#vmware "Технические подробности о поддерживаемых стандартах соответствия.") |  |  |  |  |  |  |

1

Поддержка включает upstream Kubernetes, Amazon EKS и Azure AKS. Совместимость ограничена архитектурами процессоров x86-64 и требует версии Kubernetes в соответствии с жизненным циклом поддержки Dynatrace (если не определено иное для конкретного стандарта).

2

Поддерживаемые версии: VMware ESXi 8.0 v1.1.0, VMware ESXi 7.0 v1.4.0, VMware ESXi 6.7 v1.2.0 и VMware ESXi 6.5 v1.0.0.

3

Поддержка NSX-T ограничена версией 3.2 и более поздними.

## Начало работы

* Для начала работы с Kubernetes Security Posture Management см. [Kubernetes Security Posture Management](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes.").

* Для начала работы с Cloud Security Posture Management и/или VMware Security Posture Management см. [Приём результатов Runecast Analyzer](../threat-observability/security-events-ingest/ingest-runecast-analyzer.md "Приём результатов соответствия из Runecast Analyzer и их анализ на платформе Dynatrace.").

## Дальнейшие шаги

### Далее с KSPM

После настройки Kubernetes Security Posture Management вы можете:

* Обнаруживать, управлять и принимать меры по результатам безопасности и соответствия с помощью [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](../xspm.md "Обнаружение, управление и принятие мер по результатам безопасности и соответствия.")
* Запрашивать [события соответствия](../../semantic-dictionary/model/security-events.md#compliance-finding-events "Ознакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.") с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональности Grail для расследований на основе доказательств.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости.")

  + Для списка примеров DQL на основе событий соответствия см. [Запрос событий соответствия](../threat-observability/dql-examples.md#compliance "Примеры DQL для данных безопасности на основе Grail.").

Попробуйте ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** и [поделитесь отзывом](https://dt-url.net/1m03u6q), чтобы помочь нам улучшить продукт.

### Далее с CSPM/VSPM

После настройки CSPM/VSPM вы можете:

* Визуализировать данные с помощью панели **Security Posture Overview**. Подробнее см. [Дальнейшие шаги](../threat-observability/security-events-ingest/ingest-runecast-analyzer.md#next "Приём результатов соответствия из Runecast Analyzer и их анализ на платформе Dynatrace.").
* Запрашивать [события соответствия](../../semantic-dictionary/model/security-events.md#compliance-finding-events "Ознакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.") с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональности Grail для расследований на основе доказательств.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь выводами из данных наблюдаемости.").

  + Для списка примеров DQL на основе событий соответствия см. [Запрос событий соответствия](../threat-observability/dql-examples.md#compliance "Примеры DQL для данных безопасности на основе Grail.").

## Сценарии использования

[Обеспечение соответствия с помощью Security Posture Management](../use-cases/stay-compliant.md "Контролируйте свои меры безопасности, политики и практики.")

## Часто задаваемые вопросы

### Как проверить мой кластер Kubernetes на соответствие стандартам безопасности?

* Для просмотра статуса соответствия вашего кластера см. [Просмотр статуса соответствия по системам](../xspm/assess-coverage.md#systems "Просмотрите покрытие Security Posture Management ваших систем.").
* Для просмотра результатов по вашему кластеру вы можете [фильтровать и сортировать результаты](../xspm/review-findings.md "Ищите релевантную информацию для эффективного анализа результатов безопасности и соответствия.").
* Для контекстной информации, помогающей исправить результаты, см. [Получение информации](../xspm/gain-insights.md "Углубитесь в результаты для исправления неправильных конфигураций и несоответствий.").

### Можно ли включить или отключить стандарты соответствия?

* Для [Dynatrace Kubernetes Security Posture Management (KSPM)](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes.") вы можете управлять стандартами соответствия в **Settings** Dynatrace, см. [Настройка области оценки](../xspm.md#configure-assessment "Обнаружение, управление и принятие мер по результатам безопасности и соответствия.").
* Для Runecast Cloud Security Posture Management (CSPM) и Runecast VMware Security Posture Management (VSPM) настройте выбор стандартов непосредственно в [Runecast Analyzer](https://www.dynatrace.com/platform/runecast-analyzer/).

### Что делать с результатами, сгенерированными Dynatrace?

Для обзора работы с результатами соответствия см. [Обеспечение соответствия с помощью Security Posture Management](../use-cases/stay-compliant.md "Контролируйте свои меры безопасности, политики и практики.").

### Как обеспечить соответствие по результатам высокой серьёзности?

Для руководства по повышению соответствия см. [Обеспечение соответствия с помощью Security Posture Management](../use-cases/stay-compliant.md "Контролируйте свои меры безопасности, политики и практики.").

### Как улучшить покрытие Security Posture Management?

Для инструкций см. [Улучшение покрытия](../xspm/assess-coverage.md#improve "Просмотрите покрытие Security Posture Management ваших систем.").

### Почему я получаю неудовлетворительные результаты для моей системы?

Ресурсы вашей системы оцениваются как `Failed` (не соответствует) согласно правилам, указанным в [поддерживаемых стандартах](spm.md#support "Оценка, управление и принятие мер в отношении неправильных конфигураций и нарушений.").

* Для лучшего понимания конфигурации ресурсов и просмотра источника правила см. [Получение информации](../xspm/gain-insights.md "Углубитесь в результаты для исправления неправильных конфигураций и несоответствий.").
* Для понимания типов результатов см. [Концепции: Результаты](../xspm/concepts.md#concept-results "Концепции, специфичные для приложения Dynatrace Security Posture Management.").

### Что произойдёт, если не исправить систему на основе результатов?

Поддержание вашего состояния безопасности является основой общей стратегии безопасности. Думайте об этом как о базовой гигиене безопасности — без неё все другие меры безопасности будут значительно менее эффективны. С точки зрения соответствия, игнорирование этих результатов означает, что вы не сможете выявить, оценить и исправить потенциальные проблемы, которые могут привести к провалу аудита.

Ручная обработка многочисленных проверок, необходимых для аудитов, быстро становится непосильной задачей. С нашим решением Security Posture Management весь этот процесс автоматизирован, обеспечивая эффективное управление как безопасностью, так и соответствием.

Игнорирование проблем соответствия создаёт потенциальный риск компрометации или провала соответствия.

### Как исправить обнаруженные проблемы в моей среде?

Для руководства по исправлению результатов см. [Обеспечение соответствия с помощью Security Posture Management](../use-cases/stay-compliant.md "Контролируйте свои меры безопасности, политики и практики.").

### Какие среды можно мониторить с помощью Security Posture Management?

Для списка поддерживаемых систем и их версий см. [Security Posture Management](spm.md#support "Оценка, управление и принятие мер в отношении неправильных конфигураций и нарушений.").

### В каких режимах мониторинга можно развернуть Security Posture Management на Kubernetes?

Запуск Security Posture Management на Kubernetes полностью независим от OneAgent и, следовательно, от [режимов мониторинга](../application-security.md#monitoring-modes "Доступ к функциональности Dynatrace Application Security.").
Анализируемые данные поступают с Kubernetes API Server и Kubernetes Node Configuration Collector через ActiveGate.
Поэтому вы можете использовать ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** с [мониторингом платформы Kubernetes](../../ingest-from/setup-on-k8s/deployment/platform-observability.md "Развёртывание Dynatrace Operator для мониторинга платформы Kubernetes."), где OneAgent не развёрнут.

### Как настроить Security Posture Management для облачных сред?

Настройте [интеграцию с Runecast Analyzer](../threat-observability/security-events-ingest/ingest-runecast-analyzer.md "Приём результатов соответствия из Runecast Analyzer и их анализ на платформе Dynatrace.") от Dynatrace.

## Дополнительные ресурсы

* [Основы безопасности Kubernetes: неправильные конфигурации контейнеров — от теории до эксплуатации](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Революция в облачной безопасности с контекстом наблюдаемости: Dynatrace Cloud Security и CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Поддержка SRE с помощью аналитики уязвимостей и управления состоянием безопасности](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Расширение платформы Dynatrace с помощью CSPM и VSPM](https://www.dynatrace.com/news/blog/extend-the-dynatrace-platform-with-cspm-and-vspm/)
* [Возвращение к Spring4Shell: многоуровневая защита с CADR](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Что такое Kubernetes security posture management? Обеспечение безопасности бизнеса с KSPM](https://www.dynatrace.com/news/blog/kubernetes-security-posture-management-kspm/)
* [Какое решение ИТ-безопасности подходит вашей организации? CSPM vs. KSPM vs. CNAPP](https://dt-url.net/az03zj0)
* [Dynatrace KSPM: трансформация безопасности и соответствия Kubernetes](https://www.dynatrace.com/news/blog/dynatrace-kspm-transforming-kubernetes-security-and-compliance/)
* [Dynatrace Cloud Security Posture Management повышает облачную безопасность](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/)

## Связанные темы

* [Security Posture Management](../xspm.md "Обнаружение, управление и принятие мер по результатам безопасности и соответствия.")