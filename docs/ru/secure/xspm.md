---
title: Управление безопасностью позicíи
source: https://www.dynatrace.com/docs/secure/xspm
scraped: 2026-03-06T21:29:55.059316
---

# Security Posture Management


О приложении

### Что вы узнаете

* Обзор охвата Security Posture Management ваших систем.
* Поиск релевантной информации для эффективного устранения результатов безопасности и несоответствий.
* Детальный анализ результатов для получения рекомендаций по исправлению неправильных конфигураций и несоответствий.
* Преобразование результатов в DQL-запрос или их загрузка в формате CSV для обмена с коллегами.

### Целевая аудитория

![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** предназначен для инженеров по безопасности (Security Ops Engineers), DevOps, DevSecOps и инженеров по надёжности (SRE).

Основные сценарии использования:

* Мгновенное получение информации об общем состоянии безопасности вашей контролируемой среды
* Лёгкое обнаружение и устранение проблем безопасности и неправильных конфигураций
* Получение практических рекомендаций по результатам
* Обеспечение безопасной и эффективной конфигурации вашей среды
* Повышение общей надёжности системы
* Поддержание непрерывного соответствия стандартам безопасности

Предварительные требования

* Ознакомьтесь с [поддерживаемыми стандартами соответствия и технологиями](application-security/spm.md#support "Оценивайте, управляйте и принимайте меры по неправильным конфигурациям и нарушениям руководств по усилению безопасности и нормативных стандартов соответствия.").
* Для полного использования [функциональности Security Posture Management](application-security/spm.md "Оценивайте, управляйте и принимайте меры по неправильным конфигурациям и нарушениям руководств по усилению безопасности и нормативных стандартов соответствия.") необходимо [развернуть Kubernetes Security Posture Management](../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes.").
* Разрешения: для получения списка необходимых разрешений перейдите в **Hub**, выберите ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** и откройте **Technical information**.
* Предварительные знания: понимание Kubernetes.

## Начало работы

![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** создан для того, чтобы предоставить организациям видимость, контроль и соответствие требованиям для своей среды. Он предоставляет высокоуровневый отчёт о состоянии соответствия по выбранным стандартам.

![Страница обзора показывает высокоуровневую информацию о состоянии безопасности и соответствия в вашей среде.](https://dt-cdn.net/images/overview-4008-06620e65ce.png)![Страница результатов оценки предоставляет представление соответствия всех оценённых правил из поддерживаемых стандартов безопасности. Доступные фильтры позволяют быстро выбрать по среде, состоянию результата, серьёзности и другим критериям.](https://dt-cdn.net/images/assessment-4008-8563f10902.png)![Оценённые ресурсы вашей среды помечены как «Passed», если в контексте данного правила не обнаружено неправильных конфигураций.](https://dt-cdn.net/images/passed-rules-4008-eccb9b527d.png)![Оценённые ресурсы вашей среды помечены как «Failed», если в контексте данного правила обнаружены неправильные конфигурации. Раздел оценки правил содержит подробности о соответствующих свойствах конфигурации.](https://dt-cdn.net/images/failed-rules-4008-e7eb504699.png)

1 из 4

Чтобы начать работу, выполните следующие шаги.

### 1. Установка приложения

1. В Dynatrace откройте [**Hub**](../manage/hub.md "Информация о Dynatrace Hub.").
2. Найдите ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** и нажмите **Install**.

### 2. Настройка охвата SPM

Необязательно

Вы можете настроить, какие из ваших систем (или кластеров в случае [Kubernetes Security Posture Management](../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes.")), отслеживаемых Dynatrace, охватываются [Security Posture Management](application-security/spm.md "Оценивайте, управляйте и принимайте меры по неправильным конфигурациям и нарушениям руководств по усилению безопасности и нормативных стандартов соответствия.").

1. Откройте ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**.
2. На странице **Overview** в таблице **My systems** включите или отключите нужные системы.

   Системы, не охваченные Security Posture Management, помечены `Not enabled`.

   Включение систем

   Отключение систем

   Чтобы включить охват для системы

   1. Для нужной системы нажмите **Enable SPM**.
   2. На открывшейся странице **Settings** включите **Enable Security Posture Management**.

   Чтобы отключить охват для системы

   1. Для нужной системы нажмите **Settings**.
   2. На открывшейся странице **Settings** отключите **Enable Security Posture Management**.

### 3. Настройка области оценки

Необязательно

Kubernetes Security Posture Management (KSPM)

Стандарт **CIS** включён по умолчанию в оценке вашей среды Kubernetes и не может быть отключён.
Однако вы можете настроить, какие из других поддерживаемых стандартов соответствия (**DORA**, **NIST** и **DISA STIG**) должны быть включены в будущие оценки.

Чтобы настроить область оценки

1. Откройте меню настроек в правом верхнем углу ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**.
2. Включите или отключите нужные стандарты.

Альтернативно, вы можете включить или отключить стандарты непосредственно из ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**:

1. Перейдите в **Settings** > **Analyze and alert** > **Application Security** > **Security Posture Management**.
2. Включите или отключите нужные стандарты.

Dynatrace оценивает данные, полученные от ваших систем, и ищет неправильные конфигурации по [поддерживаемым стандартам соответствия](application-security/spm.md#support "Оценивайте, управляйте и принимайте меры по неправильным конфигурациям и нарушениям руководств по усилению безопасности и нормативных стандартов соответствия."). Результаты отображаются в приложении.

Попробуйте ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** и [поделитесь обратной связью](https://dt-url.net/1m03u6q), чтобы помочь нам улучшить продукт.

## Учебные модули

[01Концепции Security Posture Management

* Описание
* Концепции, специфичные для приложения Dynatrace Security Posture Management.](xspm/concepts.md)[02Оценка охвата

* Обзор охвата Security Posture Management ваших систем.](xspm/assess-coverage.md)[03Анализ результатов

* Поиск релевантной информации для эффективного анализа результатов безопасности и соответствия.](xspm/review-findings.md)[04Получение аналитики

* Детальный анализ результатов, которые помогут исправить неправильные конфигурации и несоответствия.](xspm/gain-insights.md)[05Совместная работа с приложениями и обмен результатами

* Взаимодействие с другими приложениями для получения дополнительной аналитики и обмен результатами с заинтересованными сторонами.](xspm/share-findings.md)

Сценарии использования

Часто задаваемые вопросы

Связанные блоги

[Поддержание соответствия с помощью Security Posture Management](use-cases/stay-compliant.md "Контролируйте ваши меры безопасности, политики и практики.")

Список часто задаваемых вопросов по Security Posture Management см. в [FAQ](application-security/spm.md#faq "Оценивайте, управляйте и принимайте меры по неправильным конфигурациям и нарушениям руководств по усилению безопасности и нормативных стандартов соответствия.").

* [Kubernetes security essentials: Container misconfigurations -- From theory to exploitation](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Which IT security solution is right for your organization? CSPM vs. KSPM vs. CNAPP](https://dt-url.net/az03zj0)
* [Extend the Dynatrace platform with CSPM and VSPM](https://www.dynatrace.com/news/blog/extend-the-dynatrace-platform-with-cspm-and-vspm/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protection](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [What is Kubernetes security posture management? Driving business security with KSPM](https://www.dynatrace.com/news/blog/kubernetes-security-posture-management-kspm/)
* [Empowering SREs with runtime vulnerability analytics and security posture management](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace KSPM: Transforming Kubernetes security and compliance](https://www.dynatrace.com/news/blog/dynatrace-kspm-transforming-kubernetes-security-and-compliance/)
* [Dynatrace Cloud Security Posture Management elevates cloud security with real-time compliance across hyperscalers](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/)

## Связанные темы

* [Kubernetes Security Posture Management](../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Настройка и включение Security Posture Management в Kubernetes.")
