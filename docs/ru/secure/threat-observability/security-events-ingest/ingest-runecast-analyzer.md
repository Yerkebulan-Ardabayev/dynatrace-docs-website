---
title: Прием результатов проверки соответствия Runecast Analyzer
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer
scraped: 2026-03-06T21:23:45.187175
---

# Приём результатов проверки соответствия Runecast Analyzer


Эта страница была обновлена в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и необходимых действий для выполнения миграции см. в [руководстве по миграции таблицы безопасности Grail](../migration.md "Ознакомьтесь с изменениями в новой таблице безопасности Grail и узнайте, как выполнить миграцию на неё.").

Принимайте результаты проверки соответствия из Runecast Analyzer и анализируйте их на платформе Dynatrace.

## Начало работы

### Обзор

Интеграция Dynatrace с [Runecast Analyzer](https://www.dynatrace.com/platform/runecast-analyzer/) позволяет получать доступ к данным, относящимся к управлению состоянием безопасности облака (CSPM) и управлению состоянием безопасности VMware (VSPM), на платформе Dynatrace. Она предоставляет возможности для единообразной визуализации, анализа и автоматизации работы с результатами проверки соответствия.

Runecast Analyzer обеспечивает непрерывное соответствие стандартам посредством анализа конфигурации, генерируя результаты, связанные с безопасностью, для облачных (AWS, Azure, GCP) и VMware (vSphere, NSX-T) сред.

### Требования

Ниже приведены требования для [Runecast](#runecast) и [Dynatrace](#dt).

#### Требования Runecast

* Развёрнутый [Runecast Analyzer](https://www.dynatrace.com/platform/runecast-analyzer/) версии 6.9.12.0+ с активными лицензиями для каждого типа системы.
* Разрешения: для настройки интеграции необходим доступ с ролью `Global Admin`.
* Включены профили безопасности для поддерживаемых систем (AWS, Azure, GCP, vCenter и NSX-T).

#### Требования Dynatrace

* Dynatrace версии 1.313+
* Поддержка:

  + Ознакомьтесь с [поддерживаемыми стандартами соответствия и технологиями](../../application-security/spm.md#support "Оценивайте, управляйте и принимайте меры по устранению ошибок конфигурации и нарушений рекомендаций по усилению безопасности и нормативных стандартов соответствия.").
* Разрешения:

  + Для запроса принятых данных: `storage:security.events:read`.
* Токены:

  + Сгенерируйте токен доступа с областью `openpipeline.events_security` и сохраните его для дальнейшего использования. Подробнее см. [Dynatrace API — Токены и аутентификация](../../../dynatrace-api/basics/dynatrace-api-authentication.md "Узнайте, как пройти аутентификацию для использования Dynatrace API.").
* Для визуализации результатов в нашем готовом дашборде убедитесь, что [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** установлен](../../xspm.md#start "Обнаруживайте, управляйте и принимайте меры по устранению проблем безопасности и соответствия.").

## Активация и настройка

Для настройки приёма данных Runecast Analyzer выполните следующие шаги.

1. Подключение Runecast Analyzer к системам мониторинга

1. Войдите в экземпляр Runecast Analyzer.
2. Перейдите в **Menu** в правом верхнем углу и выберите **System settings** > **Connected systems**.
3. Подключите Runecast Analyzer к системам, которые вы хотите мониторить на соответствие.

2. Настройка интеграции с Dynatrace

1. Перейдите в Menu в правом верхнем углу и выберите **System settings** > **Integrations**.
2. Для **Dynatrace** включите **Use Dynatrace Integration**.
3. Выберите **Edit** и настройте интеграцию следующим образом:

   * Введите вашу конечную точку OpenPipeline и API-токен Dynatrace, полученный в разделе [Предварительные требования](#dt)
   * Выберите системы, для которых вы хотите отправлять результаты в Dynatrace.
4. Выберите **Save**.

   ![настройка интеграции](https://dt-cdn.net/images/2025-04-25-11-37-04-761-31b9d23552.png)

3. Начало приёма данных

1. Перейдите в **Dashboard** и выберите **Run Analysis** в верхней панели меню. После каждого анализа результаты для выбранных систем отправляются в Dynatrace.

   Существует несколько способов запуска анализа: по запросу, по периодическому расписанию или через API Runecast.
2. По завершении анализа вы можете увидеть статус в **Notifications**.

![анализ завершён](https://dt-cdn.net/images/2025-04-25-12-15-58-1079-0aefaa16ad.png)

## Подробности

### Как это работает

![как работает C/VSPM](https://dt-cdn.net/images/cspm-1-1570-dca4a64b0c.png)

1. Runecast Analyzer мониторит среды

После развёртывания и настройки Runecast Analyzer он непрерывно выполняет анализ конфигурации мониторируемых сред, связанных с управлением состоянием безопасности облака (CSPM) и управлением состоянием безопасности VMware (VSPM).

2. Результаты анализа принимаются в Dynatrace

Когда интеграция с Dynatrace настроена для мониторируемой среды, все результаты проверки соответствия принимаются в Dynatrace через выделенную конечную точку приёма событий безопасности [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.") при каждом анализе.

3. Результаты проверки соответствия безопасности обрабатываются и сохраняются в Grail

Конечная точка OpenPipeline обрабатывает и сопоставляет результаты с результатами проверки соответствия безопасности в соответствии с [соглашениями Semantic Dictionary](https://dt-url.net/3q03pb0). Они сохраняются в бакете `default_securityevents` (подробнее см.: [Встроенные бакеты Grail](../../../platform/grail/organize-data.md#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

4. Результаты проверки соответствия готовы к использованию

После приёма данных в Grail вы можете

* Анализировать состояние безопасности ваших сред и оценивать соответствие отраслевым стандартам
* Визуализировать состояние с помощью готового дашборда, который является частью [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](../../xspm.md "Обнаруживайте, управляйте и принимайте меры по устранению проблем безопасности и соответствия.")

### Дальнейшие шаги

После настройки интеграции с Runecast Analyzer вы можете

* Визуализировать данные с помощью дашборда **Security Posture Overview**

  + Пример дашборда

    ![обзор состояния безопасности](https://dt-cdn.net/images/2025-04-23-11-05-22-1899-8eeee3d9e4.png)
  + Как получить доступ к дашборду

    Есть два способа доступа к дашборду:

    - Через ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (на панели **Dashboards** выберите **Ready-made**)
    - Через  **Hub** (выберите ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, затем найдите дашборд во вкладке **Contents**)
* Запрашивать [события соответствия](../../../semantic-dictionary/model/security-events.md#compliance-finding-events "Ознакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.") с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../investigations.md "Объединяйте функции Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") или [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь данными наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.").

  + Список примеров DQL на основе событий соответствия, которые можно использовать для дальнейшего расследования или отчётности, см. в разделе [Запрос событий соответствия](../dql-examples.md#compliance "Примеры DQL для данных безопасности на базе Grail.").

### Лицензирование и стоимость

Информацию о тарификации см. в разделе [События на базе Grail](../../../license/capabilities/events.md "Узнайте, как рассчитывается потребление событий Dynatrace на базе Grail в рамках модели подписки Dynatrace Platform Subscription.").

## Связанные темы

* [OpenPipeline](../../../platform/openpipeline.md "Масштабируйте обработку данных платформы Dynatrace с помощью Dynatrace OpenPipeline.")
* [Dynatrace Query Language](../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [События безопасности](../../../semantic-dictionary/model/security-events.md "Ознакомьтесь с моделями Semantic Dictionary, связанными с событиями безопасности.")
