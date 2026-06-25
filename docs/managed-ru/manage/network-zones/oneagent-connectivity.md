---
title: Подключение OneAgent в сетевых зонах
source: https://docs.dynatrace.com/managed/manage/network-zones/oneagent-connectivity
scraped: 2026-05-12T11:10:48.870460
---

# Подключение OneAgent в сетевых зонах

# Подключение OneAgent в сетевых зонах

* Пояснение
* Чтение 1 мин
* Обновлено 26 сен 2023 г.

Сетевые зоны определяют порядок подключения для OneAgent и ActiveGate. На этой странице описывается приоритет подключения для OneAgent. Информацию об ActiveGate смотрите в разделе [Подключение ActiveGate в сетевых зонах](/managed/manage/network-zones/activegate-connectivity "Узнайте, как сетевые зоны расставляют приоритеты ActiveGate для подключения Environment ActiveGate.").

## Группы приоритетов

Сетевая зона указывает OneAgent взаимодействовать с ActiveGate из той же сетевой зоны. Если это невозможно, OneAgent пытается подключиться к другому ActiveGate. Для организации таких резервных подключений все ActiveGate сортируются по группам приоритетов:

* Группа 1 — ActiveGate из той же сетевой зоны.
* Группа 2 — ActiveGate из альтернативной сетевой зоны.
* Группа 3 — ActiveGate из зоны по умолчанию.
* Группа 4 — Все остальные ActiveGate.

В каждой группе ActiveGate дополнительно расставляются по приоритетам в зависимости от типа:

* Индекс 1 — Environment ActiveGate
* Индекс 2 — Cluster ActiveGate
* Индекс 3 — Встроенные ActiveGate (Embedded)

![Приоритет ActiveGate](https://dt-cdn.net/images/ag-priority-1532-2ffac1c718.png)

Приоритет ActiveGate

OneAgent распределяется с балансировкой нагрузки на ActiveGate с наименьшим возможным индексом. То есть, если доступны несколько ActiveGate с низким индексом, OneAgent будет регулярно переключаться между доступными ActiveGate.

Если предпочтительный ActiveGate недоступен, OneAgent пробует следующий более высокий индекс до установления соединения. В таком случае OneAgent регулярно проверяет в фоновом режиме доступность ActiveGate с более низким индексом.

[Multi-environment ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Прочитайте пошаговую процедуру настройки единого Environment ActiveGate для поддержки нескольких окружений.") может иметь только одну зону, которая действует для всех подключённых окружений.

Например, предположим, что доступны следующие три ActiveGate:

* Environment ActiveGate из той же сетевой зоны (индекс 1.1)
* Environment ActiveGate из альтернативной сетевой зоны (индекс 2.1)
* Cluster ActiveGate из той же сетевой зоны (индекс 1.2)

Используется ActiveGate с индексом 1.1. Если он становится недоступным, следующим выбором является ActiveGate с индексом 1.2. Если OneAgent не может подключиться к нему, используется ActiveGate с индексом 2.1.

## Режимы резервирования для сетевых зон

При определении резервных подключений для OneAgent учитываются следующие режимы (со ссылкой на [группы приоритетов](#priority-groups), описанные выше):

* **Any ActiveGate (default)** соответствует группам приоритетов 1, 2, 3 и 4.
* **Only DefaultZone** соответствует группам приоритетов 1, 2 и 3.
* **None (drop traffic)** соответствует группам приоритетов 1 и 2.

## Ненастроенные OneAgent

OneAgent без настроенной сетевой зоны (включая все OneAgent из сетевой зоны **Default**) работают как если бы сетевой зоны не существовало.

Такие OneAgent пытаются подключиться к любому ActiveGate в случайном порядке и выбирают первый откликающийся Environment ActiveGate. Для балансировки нагрузки через несколько минут они пытаются переключиться на следующий откликающийся Environment ActiveGate.

В Dynatrace Managed, если ни один Environment ActiveGate недоступен, OneAgent подключаются к первому откликающемуся Cluster ActiveGate. Для балансировки нагрузки через несколько минут они пытаются переключиться на следующий откликающийся Cluster ActiveGate. В этом случае трафик OneAgent передаётся в кластер Dynatrace Managed без сжатия.

## Связанные разделы

* [Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent.")