---
title: Anomaly Detection app
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app
scraped: 2026-03-06T21:14:57.037010
---

# Приложение Anomaly Detection

# Приложение Anomaly Detection

* Последняя версия Dynatrace
* Приложение
* Чтение: 3 мин
* Обновлено 26 марта 2025 г.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** предоставляет единый обзор всех конфигураций обнаружения аномалий в вашей среде Dynatrace.

Предварительные требования

### Разрешения

В следующей таблице описаны необходимые разрешения.

settings:schemas:read

Доступ на чтение схем настроек.

settings:objects:read

Доступ на чтение объектов настроек.

settings:objects:write

Доступ на запись объектов настроек.

iam:bindings:read

Доступ на чтение привязки политики, определяющей авторизацию имперсонации службы автоматизации.

iam:bindings:write

Доступ на запись привязки политики для определения авторизации имперсонации службы автоматизации.

iam:service-users:use

Разрешает использование сервисных пользователей

davis:analyzers:read

Чтение списка анализаторов

state:user-app-states:write

Запись пользовательских настроек

state:user-app-states:read

Чтение пользовательских настроек

davis:analyzers:execute

Выполнение анализатора предложений пороговых значений

Разрешения пользователей могут быть изменены только вашим администратором Dynatrace в разделе **Account Management** > **Identity and Access Management**. Чтобы узнать больше о группах пользователей и назначении разрешений, см. [Работа с политиками](../../manage/identity-access-management/permission-management/manage-user-permissions-policies.md "Working with policies").

### Установка

Убедитесь, что приложение [установлено в вашей среде](../../manage/hub.md#install "See the information about Dynatrace Hub.").

## Включение или редактирование настроек авторизации Anomaly Detection

Прежде чем пытаться запустить или создать пользовательское оповещение, убедитесь, что у вас есть все необходимые разрешения в **Account Management**. Если вы запускаете ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** впервые, вам необходимо включить настройки авторизации.

Чтобы включить или отредактировать настройки авторизации ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**

1. В ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** перейдите в **Settings** > **Authorization settings**.
2. Выберите необходимые разрешения в списке **Permissions**.

Начало работы

Концепции

Сценарии использования

![Get an overview of all available anomaly detectors.](https://cdn.hub.central.dynatrace.com/hub/9ec596c7-2bdf-4951-9668-27a3f8f9dab7.png)![Create anomaly detectors according to your business requirements.](https://cdn.hub.central.dynatrace.com/hub/e8af56a1-f9d3-44df-aa8e-c8a61c6df2ba.png)![Start to verify convertible metric selector configurations from metric events and transform it to an anomaly detector.](https://cdn.hub.central.dynatrace.com/hub/202cfb44-efed-4d9b-ba18-a6bc462c9d3c.png)

1 из 3Обзор всех доступных детекторов аномалий.

При открытии приложения вы можете увидеть информацию о существующих конфигурациях обнаружения аномалий, такую как:

* Статус -- если есть ошибка, статус отображается как **Error**; выберите его, чтобы открыть подробный отчёт в [блокноте](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").
* Источник
* Тип модели прогнозирования аномалий

Чтобы показать или скрыть столбцы, выберите **Column settings**, а затем выберите столбцы, которые хотите отобразить. Вы также можете фильтровать таблицу по любому из этих параметров.

## Обучающие модули

Пройдите следующие процессы, чтобы научиться использовать ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**:

[01Руководство по написанию DQL для Anomaly Detection

* Практическое руководство
* Лучшие практики создания DQL-запросов для пользовательских оповещений Anomaly Detection.](anomaly-detection-app/davis-ad-dql-best-practice.md)[02Руководство по оптимизации DQL для Anomaly Detection

* Практическое руководство
* Лучшие практики оптимизации DQL-запросов Anomaly Detection.](anomaly-detection-app/davis-ad-dql-optimization.md)[03Настройка простого пользовательского оповещения

* Практическое руководство
* Узнайте, как создавать и редактировать простые пользовательские оповещения в приложении Anomaly Detection.](anomaly-detection-app/configure-a-simple-ad.md)[04Настройка расширенного пользовательского оповещения

* Практическое руководство
* Узнайте, как создавать и редактировать расширенные пользовательские оповещения в приложении Anomaly Detection](../../../common/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad.md)[05Типы статусов Anomaly Detection

* Описание
* Описание типов статусов Anomaly Detection](anomaly-detection-app/anomaly-detection-status-types.md)

## Акторы пользовательских оповещений

Каждое выполнение пользовательского оповещения производится в контексте пользователя. Если вы являетесь администратором или имеете разрешение на использование предопределённого сервисного пользователя, при создании или редактировании пользовательского оповещения вы увидите два типа пользователей на выбор: актор и сервисный пользователь. В противном случае вы будете единственным видимым актором.

### Актор

Актор -- это пользователь, используемый для выполнения пользовательского оповещения. Если у вас нет прав администратора или разрешения на использование предопределённого сервисного пользователя, у вас будет возможность назначить только себя в качестве актора для новой или обновлённой конфигурации пользовательского оповещения.

Если вы редактируете существующее пользовательское оповещение, созданное другим актором, Dynatrace будет рассматривать изменённую конфигурацию как новое пользовательское оповещение с профилями разрешений нового актора.

#### Сервисный пользователь

Мы рекомендуем использовать сервисных пользователей в качестве акторов для пользовательских оповещений, созданных для отдела или организации. Это делает пользовательское оповещение независимым от статуса пользователя, который его поддерживает.

Для сервисного пользователя нет специальных настроек авторизации. Разрешения, предоставленные сервисному пользователю, должны следовать принципу минимальных привилегий. Чтобы узнать больше об управлении сервисными пользователями, см. [Сервисные пользователи](../../manage/identity-access-management/user-and-group-management/access-service-users.md "Service users").

![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

## Обзор в Dynatrace Hub

Обнаруживайте аномалии во временных рядах с помощью ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

[Dynatrace Hub](https://www.dynatrace.com/hub/detail/davis-anomaly-detection/)

## Связанные темы

* [Типы статусов Anomaly Detection](anomaly-detection-app/anomaly-detection-status-types.md "An explanation of Anomaly Detection status types")
* [Ограничения Dynatrace Intelligence](../reference/davis-ai-limits.md "Reference limits of Dynatrace Intelligence components.")
* [[Видео] Повышение безопасности с помощью Anomaly Detection](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Видео] Anomaly Detection и наблюдаемость данных](https://www.youtube.com/watch?v=HPQi63mQg3w)
