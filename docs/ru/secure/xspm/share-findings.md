---
title: Сотрудничество с приложениями и обмен результатами
source: https://www.dynatrace.com/docs/secure/xspm/share-findings
scraped: 2026-03-05T21:36:42.257441
---

# Совместная работа с приложениями и обмен результатами


* Latest Dynatrace
* How-to guide

Dynatrace предоставляет вам гибкость для выполнения следующих задач:

* Взаимодействие с другими приложениями: вы можете либо [преобразовать результаты в DQL-запросы](#dql), либо [выполнять DQL-запросы для событий соответствия в вашем любимом приложении](#run)
* Обмен данными с заинтересованными сторонами: вы можете [поделиться URL-адресом результатов](#url) или [скачать результаты в виде файла CSV](#dwld)

Подробнее см. ниже.

## Преобразование результатов в DQL-запросы

Вы можете преобразовать результаты приложения в DQL-запросы и открыть их в других приложениях Dynatrace для продолжения расследования.

1. На странице **Assessment results** выберите правило.
2. В разделе **Assessed resources** у вас есть два варианта:

   * **Вариант 1**: Выберите **Open in Notebooks**, чтобы открыть новый документ в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**
   * **Вариант 2**: В меню выберите **Open with** и укажите приложение из доступных вариантов

     ![open with](https://dt-cdn.net/images/2025-02-12-17-23-12-511-fac7e1d101.png)

## Выполнение DQL-запросов для событий соответствия

Вы можете выполнять DQL-запросы для [событий соответствия](../threat-observability/dql-examples.md#compliance "DQL examples for security data powered by Grail.") в [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.") для получения дополнительных сведений или обмена результатами с другими пользователями.

* Руководство по использованию DQL см. в разделе Использование DQL-запросов.
* Список примеров DQL-запросов на основе событий соответствия см. в разделе [Примеры DQL для данных безопасности](../threat-observability/dql-examples.md#compliance "DQL examples for security data powered by Grail.").
* Список полей событий соответствия, сопоставленных с Grail, см. в разделе Dynatrace Semantic Dictionary.

## Поделиться URL-адресом

Вы можете передать URL-адрес отфильтрованных результатов или конкретных правил членам команды.

Для просмотра результатов у пользователей должны быть включены необходимые разрешения. Подробнее см. в разделе [Предварительные требования](../xspm.md#prereq "Detect, manage, and take action on security and compliance findings.").

## Скачать в формате CSV

Вы можете скачать результаты в виде файла CSV для обмена с другими пользователями.

1. На странице **Assessment results** используйте панель фильтров для выбора нужных результатов.
2. В правом верхнем углу таблицы уязвимостей выберите > **Download as CSV** > **All**.

   ![download as csv](https://dt-cdn.net/images/2024-11-17-12-40-34-1865-7ac81cfa63.png)

## Связанные темы

* Kubernetes Security Posture Management
