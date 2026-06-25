---
title: Расчёт потребления Runtime Application Protection (RAP) (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/application-security/runtime-application-protection
scraped: 2026-05-12T12:00:45.595262
---

# Расчёт потребления Runtime Application Protection (RAP) (DPS)

# Расчёт потребления Runtime Application Protection (RAP) (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Runtime Application Protection.
Обзор возможности и основных функций см. в [Runtime Application Protection (RAP)](/managed/license/capabilities/application-security#rap "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: GiB-час

Единица измерения для Runtime Application Protection — GiB-час (также называемый «memory-gibibyte-hour» в прайс-листе).

Dynatrace создан для динамичных облачных сред, где хосты и сервисы быстро запускаются и уничтожаются.
Поэтому детализация тарификации потребления GiB-часов рассчитывается в четырёх 15-минутных интервалах в час.
Если хост или контейнер мониторируется менее 15 минут в интервале, потребление GiB-часов округляется до 15 минут перед расчётом.

### Расчёт потребления для хостов

Каждый экземпляр, на котором включён Runtime Application Protection, потребляет GiB-часы на основе физической или виртуальной оперативной памяти мониторируемого хоста, рассчитываемой в 15-минутных интервалах.

Пример: расчёт GiB-часов для физических хостов и виртуальных машин (VM)

ОЗУ каждой VM или хоста округляется до ближайшего кратного 0,25 GiB (что соответствует 256 MiB) перед расчётом потребления мониторинга.
Для физических хостов и виртуальных машин применяется минимум 4 GiB при расчёте GiB-часов.

Например, хост с 8,3 GiB памяти считается хостом 8,5 GiB (ближайшее кратное 0,25 GiB), а хост с 2 GiB памяти считается хостом 4 GiB (округление не нужно, но применяется минимум 4 GiB).

Пример: расчёт потребления

![Consumption calculation for Runtime Application Protection](https://dt-cdn.net/images/rap-consumption-5040-914c9fdd96.jpg)

Расчёт потребления для Runtime Application Protection

В примере выше каждый интервал делится на 4 для получения единицы измерения memory-gibibyte-hour.

* Host 1: работает в первом интервале; 2 GiB памяти (применяется минимум 4 GiB) = 1,0 GiB/ч RVA; 1,0 GiB/ч RAP
* Host 2: работает в первом, втором и третьем интервале; 8,3 GiB памяти (округляется до 8,5 GiB) = 6,375 GiB/ч RVA; 6,375 GiB/ч RAP
* Container 1: работает в первом и втором интервале; 780 MiB памяти (округляется до 1 GiB) = 0,5 GiB/ч RVA; 0,5 GiB/ч RAP
* Container 2: работает в третьем и четвёртом интервале; 100 MiB памяти (округляется до 0,25 GiB) = 0,125 GiB/ч RVA и 0,125 GiB/ч RAP

Итого Runtime Vulnerability Analysis: 0,5 + 0,5 + 6,375 + 0,125 = 8,0 GiB/ч

Итого Runtime Application Protection: 0,5 + 0,5 + 6,375 + 0,125 = 8,0 GiB/ч

### Расчёт потребления для контейнеров (мониторинг только приложений)

Расчёт объёма памяти для контейнеров, мониторируемых в режиме «только приложение», основывается на используемой памяти каждого контейнера.

Расчёт на основе используемой памяти контейнера требует OneAgent версии 1.275+ (для контейнеров Kubernetes) или OneAgent версии 1.283+ (для других бессерверных контейнеров).

Более старые версии OneAgent используют заданный пользователем лимит памяти.
Если лимит памяти не задан, используется память нижележащей виртуальной машины.

#### Исключения

* Для Azure App Services на плане App Service (Dedicated) для Windows экземпляры считаются хостами и определённая память всех экземпляров суммируется для определения общей памяти — вне зависимости от количества запущенных приложений.
* Для Azure App Service на Linux и Azure App Service for Linux Containers с OneAgent версии 1.283+ потребление памяти рассчитывается с использованием памяти каждого экземпляра плана. В этих случаях невозможно задать лимиты ресурсов контейнера.
* Solaris Zones считаются хостами.
* Мониторируемые контейнеры, не обнаруженные как контейнеры, считаются хостами.

Пример: расчёт GiB-часов для мониторинга контейнеров в режиме «только приложение»

В облачных средах сервисы и хосты часто недолговечны.
Поэтому расчёт потребления мониторинга в 15-минутных интервалах лучше отражает фактическое использование, чем полные часы.
Контейнеры в облачных средах, как правило, имеют меньший объём памяти, чем хосты.
Поэтому минимальный порог памяти для контейнеров составляет 256 MiB, а не 4 GiB (как для хостов).
Применяется то же округление, что и для хостов, — до ближайшего кратного 0,25 GiB.
Например, контейнер с 780 MiB памяти считается контейнером 1 GiB (780 MiB = 0,76 GiB округляется до 1 GiB).

Поскольку Runtime Application Protection основан на анализе на уровне кода, в фоновом режиме одновременно должен работать Runtime Vulnerability Analytics.
Даже если хост настроен только на Runtime Application Protection, среда будет потреблять GiB-часы для обоих: Runtime Application Protection и Runtime Vulnerability Analytics.

## Отслеживание потребления

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет следующие встроенные метрики использования для анализа потребления Runtime Application Protection в вашей организации.

(DPS) Runtime Application Protection billing usage
:   Ключ: `builtin:billing.runtime_application_protection.usage`

    Измерение:

    Разрешение: 15 мин

    Описание: Общее число хост-часов, мониторируемых Runtime Application Protection.

(DPS) Runtime Application Protection billing usage per host
:   Ключ: `builtin:billing.runtime_application_protection.usage_per_host`

    Измерение: `Host (dt.entity.host)`

    Разрешение: 15 мин

    Описание: Общее число хост-часов, мониторируемых Runtime Application Protection, с разбивкой по хостам.

Пример: мониторинг потребления memory-GiB-часов

Суммарное потребление memory-GiB-часов по всем хостам с Runtime Application Protection можно отслеживать для различных интервалов (15 мин, час, день или неделя) за любой выбранный период с помощью метрики `builtin:billing.runtime_application_protection.usage`.
В примере ниже показано потребление memory GiB-часов в 1-часовых интервалах.
С 11:00 до 14:00 потреблялось от 59,3 до 67 memory-GiB-часов каждый час.

![Application Security (DPS)](https://dt-cdn.net/images/image025-1032-e42a101535.png)

Application Security (DPS)

Суммарное потребление хост-часов можно детализировать с помощью метрики `builtin:billing.runtime_application_protection.usage_per_host`.
В примере ниже показан список всех хостов, зафиксировавших потребление.

![Runtime Application Protection (DPS)](https://dt-cdn.net/images/rap-blurred-1056-cfdb2d02d7.png)

Runtime Application Protection (DPS)

### Отслеживание потребления и затрат в Account Management

Отслеживать использование можно также в Account Management.

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview**.
2. В разделе **Cost and usage details** выберите **Usage summary**.
3. Найдите `Runtime Application Protection` и выберите **View details**.

![rap metric by host](https://dt-cdn.net/images/2-4200-80ce0c0179.png)

rap metric by host

### Отслеживание потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Обзор Application Security (DPS)](/managed/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)