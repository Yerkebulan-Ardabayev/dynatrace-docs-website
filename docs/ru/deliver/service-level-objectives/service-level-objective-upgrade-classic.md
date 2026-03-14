---
title: Обновление Classic SLOs
source: https://www.dynatrace.com/docs/deliver/service-level-objectives/service-level-objective-upgrade-classic
scraped: 2026-03-04T21:37:42.817794
---

# Обновление классических SLO

# Обновление классических SLO

* Latest Dynatrace
* Практическое руководство
* Время чтения: 7 мин
* Обновлено 10 ноября 2025 г.

Обновление классических SLO

Мы настоятельно рекомендуем обновить ваши классические SLO из ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic** в ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**, чтобы максимально использовать возможности и воспользоваться новейшими улучшениями.

Dynatrace предлагает улучшенное приложение ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** (SLO), позволяющее определять индивидуальные индикаторы уровня обслуживания (SLI) с использованием всех доступных точек данных. Это обновление обеспечивает большую гибкость, возможности настройки и интеграцию с Grail.

Dynatrace предоставляет два типа приложений для целей уровня обслуживания:

* [![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives**](../service-level-objectives.md "Откройте для себя функциональные возможности нового приложения Service-Level Objectives на базе Grail.") — наше новейшее приложение на базе Grail, предлагающее расширенные возможности гибкости и настройки.
* [![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**](../service-level-objectives-classic.md "Мониторинг и оповещение о целях уровня обслуживания в Dynatrace с помощью Service-Level Objectives Classic.") — предыдущее приложение с ограниченными возможностями.

Следующие примеры показывают SLO в ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** и несколько SLO в ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

![SLO в Dashboards](https://dt-cdn.net/images/2025-06-18-12-55-59-2870-02bc549b90.png)![SLO доступности сервиса](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-3-2705-04466642b4.png)![SLO коэффициента конверсии пользователей](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-4-2638-97d276e660.png)

1 из 3

## Зачем обновлять?

Таблица ниже описывает новую функциональность и показывает множество причин для обновления. Она сравнивает возможности SLO в ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** и ![SLOs Classic](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs Classic") **Service-Level Objectives Classic**.

| Возможность | SLOs Classic **Service-Level Objectives Classic** | SLOs **Service-Level Objectives** | Влияние на бизнес |
| --- | --- | --- | --- |
| Поддерживаемые входные данные для определения SLI | Ограничено встроенными или пользовательскими вычисляемыми метриками | Поддержка всех типов данных в Grail, включая бизнес-события, логи, спаны и временные ряды | SLO позволяют более детальную настройку и индивидуальное определение SLI. |
| Сегментация, фильтрация данных для оценки SLO | Зоны управления | [Сегменты](../../manage/segments.md "Используйте сегменты для логической структуризации и удобной фильтрации данных наблюдаемости в приложениях.") | [Сегменты](../../manage/segments.md "Используйте сегменты для логической структуризации и удобной фильтрации данных наблюдаемости в приложениях.") позволяют детально фильтровать набор данных, используемый для оценки SLO. |
| Добавление тегов SLO | — | Теги SLO | Добавляйте теги SLO (пары ключ-значение), а затем используйте их для фильтрации SLO при запросе через API. |
| Настраиваемые плитки дашборда | Классическая плитка дашборда | Новые [плитки SLO для дашборда](service-level-objective-tile-view.md "Просматривайте детали плитки целей уровня обслуживания (SLO) непосредственно в вашем дашборде.") | Новые [плитки SLO для дашборда](service-level-objective-tile-view.md "Просматривайте детали плитки целей уровня обслуживания (SLO) непосредственно в вашем дашборде.") предлагают больше визуальных возможностей настройки, включая отображаемые данные и цветовое оформление. Дополнительный мастер создания SLO позволяет создавать и редактировать SLO в Dashboards **Dashboards**. |
| Интеграция с другими приложениями Dynatrace | Интеграция с классическими приложениями Dynatrace | Интеграция с новейшими приложениями Dynatrace |  |

### Различие между SLO и классическим SLO

Основное различие между SLO и классическим SLO заключается в том, что SLI в SLO представлен в виде одного DQL-запроса.
DQL-запрос допускает обширные возможности настройки, в отличие от селекторов метрик и сущностей в классическом SLO.

Преимущества SLO на основе DQL:

* Использование любых данных телеметрии в Grail. Подробнее см. [Обновление метрик](../../analyze-explore-automate/metrics/upgrade.md "Обновите классические метрики до метрик на базе Grail, чтобы продолжить использование данных, полученных с помощью селекторов метрик, но с дополнительными возможностями Grail и DQL.").
* Применение пользовательских фильтров и расширенных возможностей [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Использование Dynatrace Query Language.").
* Упрощённые расчёты соотношений для SLI.

#### Как определяются основные компоненты SLO в SLO и классическом SLO

SLO обычно имеет определённые характеристики, которые можно настраивать различными способами.

Основные компоненты SLO:

* **Индикатор уровня обслуживания (SLI)**: временной ряд, показывающий процентные значения (100% = идеальный показатель)
* **Целевой показатель SLO**: пороговое значение для успеха
* **Период оценки**: обычно от 1 до 4 недель
* **Статус SLO**: агрегированный результат за период оценки
* **Бюджет ошибок**: допустимое отклонение (100% - целевой показатель SLO)

Можно установить следующие параметры:

* SLI

  + Какие типы данных необходимы?
  + Какая доля данных должна учитываться?
* Период оценки
* Целевой показатель SLO (пороговое значение)

В ![SLOs](https://dt-cdn.net/images/service-level-objectives-256-3d3d62c9a8.png "SLOs") **Service-Level Objectives** SLI представлен в виде запроса [DQL (Dynatrace Query Language)](../../platform/grail/dynatrace-query-language.md "Использование Dynatrace Query Language.").
Он гибок и использует контекстные данные для представления целей.

### Пример классического SLO с использованием селекторов метрик

Ниже приведён пример классического SLO с использованием классических селекторов метрик, аналогичных DQL-запросу.

![Скриншот классического SLO](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-classic-settings-ui-settings-builtin-monitoring-slo-gtf-2h-gf-all-id-ce2ea422-2364-3dd2-bb04-46dba36f44bc-1-1847-1327f5cb0a.png)

### Пример SLO с использованием DQL

SLO состоит из двух основных частей: **Custom DQL** и **Preview**. В **Custom DQL** вы определяете свой DQL-запрос. В **Preview** вы визуализируете SLO.

#### Custom DQL

DQL-запрос SLO структурирован определённым образом для определения SLO и SLI. Пример DQL-запроса SLO, определённого во вкладке **Critical services or entities**, имеет следующие характеристики:

* Определение точек данных.

  ```
  timeseries {total=sum(dt.service.request.count), failures=sum(dt.service.request.failure_count)},
  ```
* Указание области сущностей.

  ```
  by: { dt.entity.service }
  ```
* Отображение необходимой информации с помощью фильтров DQL.

  ```
  | fieldsAdd name = entityName(dt.entity.service)



  | filter in(name, "astroshop-checkoutservice", "astroshop-cartservice", "astroshop-paymentservice", "astroshop-shippingservice", "astroshop-currencyservice", "astroshop-frontend", "astroshop-recommendationservice")
  ```
* Вычисление SLI.

  ```
  | fieldsAdd sli = (((total[] - failures[]) / total[]) * 100)



  | fields timeframe, interval, dt.entity.service, name, sli
  ```

#### Preview

Проверьте в **Preview** статусы SLO и SLI.

![Скриншот интерфейса Dynatrace, показывающий SLI и SLO.](https://dt-cdn.net/images/guu84124-apps-dynatrace-com-ui-apps-dynatrace-service-level-objectives-6-2658-349ab1cff7.png)

## Обновление классических SLO до SLO

Чтобы обновить классический SLO до SLO:

1. Сопоставьте выражение метрики вашего классического SLO с Grail.

   1. Ознакомьтесь с исчерпывающим списком в разделе [Обновление метрик](../../analyze-explore-automate/metrics/upgrade.md "Обновите классические метрики до метрик на базе Grail, чтобы продолжить использование данных, полученных с помощью селекторов метрик, но с дополнительными возможностями Grail и DQL.").
   2. Используйте [руководство по конвертации селекторов метрик](../../analyze-explore-automate/metrics/upgrade/metric-selector-conversion.md "Узнайте о различных метриках, предлагаемых Dynatrace.").

   Для сложных выражений метрик может потребоваться ручная адаптация DQL-запросов.
2. Преобразуйте селекторы сущностей в соответствующие [операторы DQL](../../platform/grail/dynatrace-query-language.md "Использование Dynatrace Query Language."). Подробнее см. [Лучшие практики DQL](../../platform/grail/dynatrace-query-language/dql-best-practices.md "Лучшие практики использования Dynatrace Query Language.").

   В следующей таблице показаны типичные селекторы сущностей для классических SLO и их эквиваленты в DQL.

   Если вы используете зоны управления для управления разрешениями и контролем доступа, см. [Предоставление доступа к сущностям с контекстом безопасности](../../manage/identity-access-management/use-cases/access-security-context.md "Предоставление доступа к сущностям с контекстом безопасности").
3. Улучшите определение SLI.

   Хотя вы можете обновить большинство классических SLO до полного соответствия в Grail, рассмотрите возможность улучшения определений SLI, используя опции, недоступные в традиционных выражениях метрик.

   Воспользуйтесь новыми возможностями:

   * Рабочие часы
   * Ключевые запросы/эндпоинты в DQL
   * Расширенные математические операции
   * Использование бизнес-событий в качестве опережающих индикаторов
   * Добавление тегов SLO для фильтрации и группировки
   * Использование сегментов для динамической области сущностей

## Обновление API-интеграции

Для автоматизации управления и оценки SLO используйте выделенные эндпоинты API. Обратитесь к таблице ниже для обновления вашей API-интеграции с классического SLO на SLO с использованием публичного API сервиса SLO.

## Обновление через Configuration as Code

Для масштабируемого управления и оценки SLO используйте [обзор Configuration as Code](../configuration-as-code.md "Используйте конфигурацию Dynatrace как код через Monaco или Terraform.") поверх публичного API сервиса SLO.

Чтобы получить доступ к публичному API сервиса SLO в вашем тенанте:

1. Перейдите в Dynatrace.
2. В [поиске по платформе](../../discover-dynatrace/get-started/dynatrace-ui.md#search "Навигация в новейшем Dynatrace") введите `API`. В результатах поиска найдите раздел **Support resources** и **Dynatrace API** в нём.
3. Выберите **Dynatrace API** для доступа к документации Dynatrace API. Откроется новая страница с определениями Dynatrace API.
4. В правом верхнем углу перейдите к **Select a definition**.
5. Из выпадающего списка выберите эндпоинт.

* [Обзор Configuration as Code через Terraform](../configuration-as-code/terraform.md "Управляйте своей средой Dynatrace с помощью Dynatrace Configuration as Code через Terraform.") поддерживает публичный API сервиса SLO начиная с версии v1.78.0, а провайдер Dynatrace Terraform доступен как `dynatrace-oss/dynatrace | Terraform Registry`.
* [Обзор Configuration as Code через Monaco](../configuration-as-code/monaco.md "Управляйте своей средой Dynatrace с помощью Dynatrace Configuration as Code через Monaco.") поддерживает публичный API сервиса SLO начиная с версии v2.22.

## Что дальше?

Автоматизированный процесс обновления рассматривается; однако из-за высокой степени настройки SLO ручная проверка, как ожидается, даст наилучшие результаты.
Используйте эту возможность для переоценки и улучшения ваших SLI, а не просто копирования их один к одному.

Для дальнейшей оптимизации и рекомендаций обратитесь к команде поддержки Dynatrace, чтобы максимизировать бизнес-эффект от ваших целей уровня обслуживания.

## Связанные темы

* [Знакомство с Dynatrace](../../discover-dynatrace.md "Знакомство с Dynatrace")
* [Шаблоны целей уровня обслуживания](service-level-objective-templates.md "Ознакомьтесь с готовыми шаблонами целей уровня обслуживания.")
* [Примеры целей уровня обслуживания](service-level-objective-examples.md "Ознакомьтесь с готовыми определениями целей уровня обслуживания на примерах.")
