---
title: Что такое среда мониторинга?
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/monitoring-environment
scraped: 2026-05-12T11:06:42.123479
---

# Что такое среда мониторинга?

# Что такое среда мониторинга?

* Explanation
* 4-min read
* Published Dec 05, 2017

Среда мониторинга Dynatrace — это место, где выполняется весь анализ производительности Dynatrace. [Dynatrace OneAgent](/managed/platform/oneagent "Learn the monitoring capabilities of OneAgent.") отправляет все захваченные данные мониторинга в вашу среду мониторинга для анализа. Среда мониторинга аналогична серверу анализа, предоставляющему все функции анализа производительности приложений Dynatrace, включая все дашборды, диаграммы, отчёты и другие инструменты.

![Архитектура Dynatrace](https://dt-cdn.net/images/dynatrace-architecture-1743-fab92236e8.png)

Архитектура Dynatrace

## Расположение среды мониторинга

Расположение среды мониторинга зависит от типа развёртывания.

| Тип развёртывания | Расположение среды мониторинга |
| --- | --- |
| Dynatrace Managed | В вашем собственном центре обработки данных |
| Dynatrace for Government | В облаке с авторизацией FedRAMP moderate |

## Идентификатор среды

Весь внешний доступ к вашей среде мониторинга Dynatrace основан на двух типах учётных данных: *идентификатор среды* и [токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").

Каждая отслеживаемая среда Dynatrace идентифицируется уникальной строкой символов — идентификатором среды. Dynatrace API активно использует идентификаторы сред для обеспечения получения данных мониторинга из правильных сред Dynatrace и передачи в них соответствующих внешних событий.

В Dynatrace Managed и Dynatrace for Government идентификатор среды — это строка после `/e/` в URL вашей среды Dynatrace:

```
https://{your-domain}/e/{your-environment-id}/
```

Например, для URL `https://managed-cluster/e/abc123a` идентификатор среды — `abc123a`.

## Несколько сред мониторинга

Можно настроить отдельные среды мониторинга с одним кластером Dynatrace Managed.

При настройке нескольких сред мониторинга:

* Каждая среда мониторинга использует общую базу пользователей и другие настройки учётной записи.
* Данные, собранные из каждой среды мониторинга, хранятся отдельно.
* Легко переключаться между представлениями мониторинга для разных сред для отслеживания производительности и доступности каждой среды.

### Варианты использования

Существует несколько причин для создания отдельных сред мониторинга.

Например:

* Возможно, вам потребуется отдельно отслеживать среды разработки, промежуточную и производственную среды вашей организации.
* Возможно, вам потребуется поддерживать отдельную среду мониторинга для каждого центра обработки данных вашей организации.

### Настройка нескольких сред мониторинга

Способ настройки различных сред мониторинга зависит от того, используете ли вы Dynatrace Managed или Dynatrace for Government.

| Тип развёртывания | Способ настройки различных сред мониторинга |
| --- | --- |
| Dynatrace Managed | Можно использовать Cluster Management Console. Подробнее см. в разделе [Управление средами мониторинга](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments."). |
| Dynatrace for Government | Обратитесь к представителю Dynatrace. |

### Соединение нескольких сред

При использовании нескольких сред данные мониторинга строго разделены по умолчанию. Среды не получают информацию друг от друга автоматически.

Однако в некоторых сценариях может потребоваться соединить ваши среды. Например:

* Для трассировки вызовов между сервисами, отслеживаемыми в разных средах Dynatrace, можно настроить межсредовую трассировку. Подробнее см. в разделе [Настройка межсредовой трассировки](/managed/observe/application-observability/distributed-traces/analysis/connect-environments "Analyze requests across environment boundaries.").
* Для отображения метрик из удалённых сред на дашбордах локальной среды можно настроить плитки дашборда для межсредовой работы. Подробнее см. в разделе [Создание удалённых/многосредовых дашбордов Dynatrace](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.").