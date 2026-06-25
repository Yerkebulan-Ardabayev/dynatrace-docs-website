---
title: Подключение ActiveGate в сетевых зонах
source: https://docs.dynatrace.com/managed/manage/network-zones/activegate-connectivity
scraped: 2026-05-12T11:10:41.442921
---

# Подключение ActiveGate в сетевых зонах

# Подключение ActiveGate в сетевых зонах

* Пояснение
* Чтение 1 мин
* Опубликовано 30 мар 2020 г.

Сетевые зоны определяют порядок подключения для OneAgent и ActiveGate. На этой странице описывается приоритет подключения для ActiveGate. Информацию о OneAgent смотрите в разделе [Подключение OneAgent в сетевых зонах](/managed/manage/network-zones/oneagent-connectivity "Узнайте, как сетевые зоны расставляют приоритеты ActiveGate для подключения OneAgent.").

* Группа 1 — ActiveGate из той же сетевой зоны.
* Группа 2 — ActiveGate из альтернативной сетевой зоны.
* Группа 3 — ActiveGate из зоны по умолчанию.
* Группа 4 — Все остальные ActiveGate.

В каждой группе ActiveGate дополнительно расставляются по приоритетам в зависимости от типа:

* Индекс 1 — Встроенные ActiveGate (Embedded)
* Индекс 2 — Кластерные ActiveGate (Cluster)

![Приоритет ActiveGate](https://dt-cdn.net/images/ag-routing-1532-4db537c11f.png)

Приоритет ActiveGate

Предпочтительным является ActiveGate с наименьшим возможным индексом. Для балансировки нагрузки Environment ActiveGate поочерёдно обходит все доступные конечные точки ActiveGate с наименьшим возможным индексом.

Если предпочтительный ActiveGate недоступен, Environment ActiveGate пробует следующий более высокий индекс до установления соединения. В таком случае Environment ActiveGate регулярно проверяет в фоновом режиме доступность ActiveGate с более низким индексом.

Например, если доступны три ActiveGate:

* Встроенный ActiveGate из той же сетевой зоны (индекс 1.1)
* Встроенный ActiveGate из альтернативной сетевой зоны (индекс 2.1)
* Кластерный ActiveGate из той же сетевой зоны (индекс 1.2)

то используется ActiveGate с индексом 1.1. Если он становится недоступным, следующим выбором является ActiveGate с индексом 1.2. Если Environment ActiveGate не может подключиться к нему, используется ActiveGate с индексом 2.1.

## Ненастроенные ActiveGate

Environment ActiveGate без настроенной сетевой зоны (включая все ActiveGate из сетевой зоны **Default**) работают как если бы сетевой зоны не существовало. Такие ActiveGate пытаются подключиться к первому доступному ActiveGate на основе следующего приоритета:

* Индекс 1 — Встроенные ActiveGate (Embedded)
* Индекс 2 — Кластерные ActiveGate (Cluster)

Для балансировки нагрузки через несколько минут они пытаются переключиться на следующий откликающийся ActiveGate с наименьшим возможным индексом.

## Связанные разделы

* [Поддерживаемые схемы подключения для ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent.")