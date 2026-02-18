---
title: Compliance Assistant
source: https://www.dynatrace.com/docs/analyze-explore-automate/compliance-and-resilience/compliance-assistant
scraped: 2026-02-18T05:45:46.424578
---

# Compliance Assistant

* Последняя версия Dynatrace
* Приложение
* 3 мин на чтение
* Обновлено 28 января 2026 г.
* Предварительный просмотр

О приложении

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** собирает информацию из различных источников и приложений для поддержания видимости в реальном времени статуса соответствия требованиям для критически важных приложений и систем.

Он использует возможности наблюдаемости, безопасности и другие возможности платформы Dynatrace, усиленные Dynatrace Intelligence, для повышения операционной устойчивости и безопасности.

Предварительные условия

## Настройка источников и приложений

* Чтобы в полной мере воспользоваться преимуществами **Security Posture Management** ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM"), ознакомьтесь с разделом [Предварительные условия](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management#prereq "Настройка и включение Security Posture Management в Kubernetes.") и инструкциями по [Началу работы](/docs/secure/xspm#start "Обнаружение, управление и принятие мер в отношении проблем безопасности и соответствия требованиям.").
* Настройте [Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уязвимостей на уровне кода, отслеживание хода устранения и создание правил мониторинга.").
* Настройте [Dynatrace Runtime Application Protection](/docs/secure/application-security/application-protection "Настройка и конфигурирование Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, вызванных атаками.").
* [Установите](/docs/manage/hub#install "См. информацию о Dynatrace Hub.") ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**

## Установка

Убедитесь, что приложение [установлено в вашей среде](/docs/manage/hub#install "См. информацию о Dynatrace Hub.").

Начните работу

Основные понятия

Варианты использования

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** поддерживает вас в достижении и управлении соответствием нормативным требованиям и сертификациям "из коробки", начиная с [DORA (Digital Operational Resilience Act)](#dora).

![Compliance Assistant overview](https://dt-cdn.net/hub/Compliance_Assistant_Preview_qb0fIUx.png)

1 из 1

## Навигация в Compliance Assistant

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** предоставляет следующие возможности:

* Открыть шаблон отчета
  Выберите **ICT incident reporting notebook** в правом верхнем углу страницы, чтобы получить доступ к шаблону отчета об инциденте в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

  Обратите внимание, что это [готовый документ](/docs/analyze-explore-automate/dashboards-and-notebooks/ready-made-documents "Используйте готовые документы прямо из коробки.").
* Открыть нормативный акт DORA

  В каждом виджете вы можете найти главу нормативного акта DORA, к которой он относится.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Изучите в Dynatrace Hub

Управляйте соответствием требованиям с помощью автоматизированных проверок и обработки инцидентов "из коробки".

[Dynatrace Hubï»¿](https://www.dynatrace.com/hub/detail/compliance-assistant/?query=compl&filter=all)

Чтобы помочь достичь надежной позиции соответствия требованиям DORA, Dynatrace:

* Объединяет данные из всей платформы безопасности и наблюдаемости Dynatrace для создания комплексного обзора соответствия требованиям в соответствии с главами DORA.
* Поддерживает видимость в реальном времени статуса соответствия требованиям для отслеживаемых систем.
* Поддерживает отчетность об инцидентах, как того требует DORA.

## Соответствие требованиям DORA

DORA — это нормативный акт ЕС, который повышает цифровую операционную устойчивость финансового сектора. Он стремится обеспечить способность финансовых организаций выдерживать и восстанавливаться после серьезных операционных сбоев, включая кибератаки.

## Соответствие конфигурации ИКТ

Виджет соответствия конфигурации ИКТ собирает информацию из **Runecast** и **Security Posture Management** для непрерывного сканирования конфигураций и получения обзора их соответствия требованиям DORA.

## Уязвимости ИКТ

Виджет уязвимостей ИКТ собирает информацию из ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** (с примененным фильтром `Уровень риска`).

## Инциденты, связанные с критически важными службами ИКТ

Виджет инцидентов, связанных с критически важными службами ИКТ, собирает информацию из:

* **Атаки** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks") — если произошел инцидент безопасности, помогает обнаружить и классифицировать атаку на вашу среду в реальном времени.
* **Проблемы** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") — если произошел инцидент, связанный с устойчивостью, анализирует аномальное поведение системы и проблемы с производительностью, обнаруженные Dynatrace Intelligence.
* Используйте [сегменты](/docs/manage/segments "Сегменты логически структурируют данные мониторинга в Grail и функционируют как удобные фильтры для данных, к которым пользователи имеют доступ на основе разрешений."), чтобы удобно фильтровать инциденты наблюдаемости и безопасности, влияющие на критически важную службу в соответствии с DORA.

Виджет **Уязвимости ИКТ** показывает вам последние инциденты, связанные с устойчивостью и безопасностью, но вы можете просмотреть все инциденты наблюдаемости ИКТ в **Проблемах** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") и просмотреть все инциденты безопасности ИКТ в **Атаках** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks").

## Покрытие мониторинга ИКТ

Виджет покрытия мониторинга ИКТ собирает информацию из:

* ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** — предотвращает неожиданные сбои, обнаруживая и устраняя пробелы в покрытии мониторингом.

## Варианты использования

Compliance Assistant позволяет вам легко достичь и управлять соответствием требованиям DORA:

* Поддерживайте видимость в реальном времени статуса соответствия требованиям DORA для критически важных приложений и систем.
* Объединяйте информацию со всей платформы Dynatrace, оптимизированную для конкретных нормативных требований, отображаемую в адаптированном представлении.
* Определяйте критические инциденты и поддерживайте свою команду своевременными и точными отчетами в соответствии с требованиями DORA.
* Автоматизируйте отчетность, предоставляя автоматизированные рабочие процессы и шаблоны, предписанные регулирующими органами.