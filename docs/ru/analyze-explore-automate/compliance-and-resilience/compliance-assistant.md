---
title: Помощник соответствия
source: https://www.dynatrace.com/docs/analyze-explore-automate/compliance-and-resilience/compliance-assistant
scraped: 2026-03-05T21:30:24.955360
---

# Compliance Assistant


* Последняя Dynatrace
* Приложение
* 3 мин. чтения
* Обновлено 28 января 2026 г.
* Предварительная версия

О приложении

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** собирает информацию из различных источников и приложений для поддержания видимости статуса соответствия по критическим приложениям и системам в реальном времени.

Он использует возможности платформы Dynatrace в области наблюдаемости, безопасности и другие функции, усиленные Dynatrace Intelligence, для укрепления операционной устойчивости и состояния безопасности.

Предварительные требования

## Настройка источников и приложений

* Чтобы в полной мере воспользоваться ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Управлением состоянием безопасности**, см. [Предварительные требования](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md#prereq "Настройка и включение Security Posture Management в Kubernetes.") и как [Начать работу](../../secure/xspm.md#start "Обнаружение, управление и принятие мер по результатам безопасности и соответствия.").
* Настройте [Dynatrace Runtime Vulnerability Analytics](../../secure/application-security/vulnerability-analytics.md "Мониторинг, визуализация, анализ и устранение уязвимостей сторонних компонентов и уровня кода, отслеживание прогресса устранения и создание правил мониторинга.")
* Настройте [Dynatrace Runtime Application Protection](../../secure/application-security/application-protection.md "Настройте Dynatrace Runtime Application Protection для мониторинга атак и уязвимостей на уровне кода, генерируемых атаками.")
* [Установите](../../manage/hub.md#install "Информация о Dynatrace Hub.") ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**

## Установка

Убедитесь, что приложение [установлено в вашей среде](../../manage/hub.md#install "Информация о Dynatrace Hub.").

Начало работы

Концепции

Варианты использования

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** помогает вам достичь и управлять соответствием нормативным требованиям и сертификациям «из коробки», начиная с [DORA (Закон о цифровой операционной устойчивости)](#dora).

![Обзор Compliance Assistant](https://dt-cdn.net/hub/Compliance_Assistant_Preview_qb0fIUx.png)

1 из 1

## Навигация по Compliance Assistant

![Compliance Assistant](https://dt-cdn.net/images/compliance-assistant-app-256-a136b783a7.png "Compliance Assistant") **Compliance Assistant** предоставляет следующие возможности взаимодействия:

* Открыть шаблон отчёта
  Нажмите **ICT incident reporting notebook** в верхнем правом углу страницы, чтобы получить доступ к шаблону отчёта об инцидентах в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.

  Обратите внимание, что это [готовый документ](../dashboards-and-notebooks/ready-made-documents.md "Используйте готовые документы прямо из коробки.").
* Открыть регламент DORA

  В каждом виджете вы можете найти главу регламента DORA, к которой он относится.

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Исследуйте в Dynatrace Hub

Управляйте соответствием с помощью автоматизированных проверок и обработки инцидентов «из коробки».

[Dynatrace Hub](https://www.dynatrace.com/hub/detail/compliance-assistant/?query=compl&filter=all)

Чтобы помочь достичь прочной позиции соответствия DORA, Dynatrace:

* Консолидирует данные со всей платформы безопасности и наблюдаемости Dynatrace для создания комплексного обзора соответствия в соответствии с главами DORA.
* Поддерживает видимость статуса соответствия в реальном времени по всем мониторируемым системам.
* Поддерживает отчётность об инцидентах в соответствии с требованиями DORA.

## Соответствие DORA

DORA — это регламент ЕС, повышающий цифровую операционную устойчивость финансового сектора. Он стремится обеспечить, чтобы финансовые организации могли выдержать и восстановиться после серьёзных операционных нарушений, включая кибератаки.

## Соответствие конфигурации ИКТ

Виджет соответствия конфигурации ИКТ собирает информацию из **Runecast** и **Security Posture Management** для непрерывного сканирования конфигураций и получения обзора их соответствия требованиям DORA.

## Уязвимости ИКТ

Виджет уязвимостей ИКТ собирает информацию из ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Уязвимостей** (с применённым фильтром `Уровень риска`).

## Инциденты критических сервисов ИКТ

Виджет инцидентов критических сервисов ИКТ собирает информацию из:

* **Атаки** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks") — при наличии инцидента безопасности помогает обнаружить и классифицировать атаку на вашу среду в реальном времени.
* **Проблемы** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") — при наличии инцидента устойчивости анализирует аномальное поведение системы и проблемы производительности, обнаруженные Dynatrace Intelligence.
* Используйте [сегменты](../../manage/segments.md "Используйте сегменты для логической структуризации и удобной фильтрации данных наблюдаемости между приложениями.") для удобной фильтрации инцидентов наблюдаемости и безопасности, влияющих на критический сервис по DORA.

Виджет **Уязвимости ИКТ** показывает самые последние инциденты устойчивости и безопасности, но вы можете просмотреть все инциденты наблюдаемости ИКТ в **Проблемах** ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") и все инциденты безопасности ИКТ в **Атаках** ![Attacks](https://dt-cdn.net/images/attacks-512-b922840b12.png "Attacks").

## Покрытие мониторинга ИКТ

Виджет покрытия мониторинга ИКТ собирает информацию из:

* ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage** — предотвращает неожиданные сбои путём обнаружения и устранения пробелов в мониторинговом покрытии.

## Варианты использования

Compliance Assistant позволяет легко достигать и управлять соответствием DORA:

* Поддерживать видимость статуса соответствия DORA в реальном времени по критическим приложениям и системам.
* Консолидировать аналитику со всей платформы Dynatrace, оптимизированную для конкретных нормативных требований, в адаптированном представлении.
* Выявлять критические инциденты и поддерживать вашу команду своевременной и точной отчётностью по требованиям DORA.
* Автоматизировать отчётность, предоставляя автоматизированные рабочие процессы и шаблоны, предписанные регуляторами.