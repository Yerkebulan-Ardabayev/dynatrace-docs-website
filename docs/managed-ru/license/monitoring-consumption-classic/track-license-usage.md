---
title: Отслеживание использования лицензии
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/track-license-usage
---

# Отслеживание использования лицензии

# Отслеживание использования лицензии

* Пояснение
* Чтение за 3 минуты
* Обновлено 15 мая 2026 г.

Отслеживать использование лицензии по единицам хостов, единицам данных Davis и единицам Digital Experience Monitoring при классическом лицензировании можно двумя способами:

* Через **Cluster Management Console**
* В окружении **Local-Self-Monitoring**

## Cluster Management Console

Чтобы отследить использование лицензии Managed Cluster, войти в **Cluster Management Console** и выбрать **Licensing** в меню.

Страница **Licensing** отображает метаданные лицензии, квоту на единицу лицензии и текущее потребление. Также видно, применяется ли квота превышения (overage) и сколько из неё уже израсходовал Managed Cluster.

Все данные, отображаемые здесь, также доступны через [Cluster API v2 - Cluster License](/managed/dynatrace-api/cluster-api/cluster-api-v2/cluster-license/get-cluster-license-usage "Использовать API для получения сведений о лицензии кластера и оплачиваемом использовании.").

![Страница лицензирования Cluster Management Console](https://dt-cdn.net/images/cmc-licensing-1990-836a6a9a72.png)

Страница лицензирования Cluster Management Console

## Окружение Local-Self-Monitoring

Dynatrace Managed версии 1.330+

Чтобы отследить использование лицензии Managed Cluster, перейти в окружение [**Local-Self-Monitoring**](/managed/managed-cluster/self-monitoring/local-self-monitoring "Узнать об окружении local self-monitoring, которое собирает внутренние метрики состояния Dynatrace Managed Cluster и хранит все данные исключительно локально (on-premises).") и выбрать **Dashboards** > **Cluster license usage**.

Дашборд **Cluster license usage** отображает несколько графиков по каждой единице лицензии, показывающих её квоту и процент потребления. Также видно, применяется ли квота превышения (overage) и сколько из неё уже израсходовал Managed Cluster.

![Дашборд Cluster license usage](https://dt-cdn.net/images/managed330-cluster-license-usage-2335-1d3ae4be6a.png)

Дашборд Cluster license usage

### Метрики биллинга

Каждый график использует метрики биллинга самомониторинга (self-monitoring). Для каждой единицы лицензии доступно шесть метрик биллинга. Использовать metric events для генерации оповещений о лицензионных событиях, например когда единицы вот-вот закончатся.

#### Единицы хостов

Доступны следующие метрики биллинга самомониторинга.

| Название метрики | Ключ метрики |
| --- | --- |
| Cluster - Billing - Hostunit - Quota | `isfm:cluster.billing.hostunit.quota` |
| Cluster - Billing - Hostunit - Quota - Used | `isfm:cluster.billing.hostunit.quota.used` |
| Cluster - Billing - Hostunit - Quota - Used Percent | `isfm:cluster.billing.hostunit.quota.used_percent` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota | `isfm:cluster.billing.hostunit.overage.hours.quota` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota - Used | `isfm:cluster.billing.hostunit.overage.hours.quota.used` |
| Cluster - Billing - Hostunit - Overage - Hours - Quota - Used Percent | `isfm:cluster.billing.hostunit.overage.hours.quota.used_percent` |

#### Единицы данных Davis

Доступны следующие метрики биллинга самомониторинга.

| Название метрики | Ключ метрики |
| --- | --- |
| Cluster - Billing - Ddu - Quota | `isfm:cluster.billing.ddu.quota` |
| Cluster - Billing - Ddu - Quota - Used | `isfm:cluster.billing.ddu.quota.used` |
| Cluster - Billing - Ddu - Quota - Used Percent | `isfm:cluster.billing.ddu.quota.used_percent` |
| Cluster - Billing - Ddu - Overage - Quota | `isfm:cluster.billing.ddu.overage.quota` |
| Cluster - Billing - Ddu - Overage - Quota - Used | `isfm:cluster.billing.ddu.overage.quota.used` |
| Cluster - Billing - Ddu - Overage - Quota - Used Percent | `isfm:cluster.billing.ddu.overage.quota.used_percent` |

#### Единицы Digital Experience Monitoring

Доступны следующие метрики биллинга самомониторинга.

| Название метрики | Ключ метрики |
| --- | --- |
| Cluster - Billing - Dem - Quota | `isfm:cluster.billing.dem.quota` |
| Cluster - Billing - Dem - Quota - Used | `isfm:cluster.billing.dem.quota.used` |
| Cluster - Billing - Dem - Quota - Used Percent | `isfm:cluster.billing.dem.quota.used_percent` |
| Cluster - Billing - Dem - Overage - Quota | `isfm:cluster.billing.dem.overage.quota` |
| Cluster - Billing - Dem - Overage - Quota - Used | `isfm:cluster.billing.dem.overage.quota.used` |
| Cluster - Billing - Dem - Overage - Quota - Used Percent | `isfm:cluster.billing.dem.overage.quota.used_percent` |

### Лицензионные события

Чтобы настроить лицензионное событие (например, когда Managed Cluster израсходует 80% единиц данных Davis):

1. Перейти в окружение **Local-Self-Monitoring** и выбрать **Settings** > **Anomaly detection** > **Metric events**.
2. Выбрать **Add metric event**.
3. Задать свойства **Query definition**:

   * Тип запроса: **Metric selector**
   * Metric selector: ключ метрики с преобразованиями `max` и `rollup`. Например:

     `isfm:cluster.billing.ddu.quota.used_percent:max:rollup(max,10m)`
4. Задать свойства **Monitoring strategy**:

   * Тип модели: **Static threshold**
   * Порог (Threshold): `80`
   * Единица порогового значения: **percent**
   * Условие оповещения: **Alert if metric is above**
5. Задать свойства **Advanced model**:

   * Violating samples: `3`
   * Sliding window: `5`
   * Dealerting samples: `5`
6. Проверить конфигурацию с помощью **Alert preview**.
7. Задать **Event template** и установить тип события **Error**.
8. Выбрать **Save changes**.

Когда Managed Cluster превышает 80% единиц данных Davis, Dynatrace открывает проблему. В разделе **Problems** появится, например, такое оповещение:

![Израсходовано 80% единиц данных Davis](https://dt-cdn.net/images/license-problem-80percent-1398-0b3f1b9fe2.png)

Израсходовано 80% единиц данных Davis