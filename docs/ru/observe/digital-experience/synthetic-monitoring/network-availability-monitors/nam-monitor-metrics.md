---
title: Метрики монитора NAM
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/nam-monitor-metrics
scraped: 2026-03-04T21:29:54.840473
---

# Метрики монитора NAM

# Метрики монитора NAM

* Classic
* Пояснение
* Чтение: 12 мин
* Опубликовано 19 июня 2024 г.

## Метрики и измерения

### Измерения (все мониторы доступности сети)

| Имя | Тип | Описание | Пример значения |
| --- | --- | --- | --- |
| `dt.entity.multiprotocol_monitor` | строка | Идентификатор монитора (идентификатор отслеживаемой сущности) | `MULTIPROTOCOL_MONITOR-3F6C9D500287BBAF` |
| `dt.entity.synthetic_location` | строка | Идентификатор синтетической локации (идентификатор отслеживаемой сущности) | `SYNTHETIC_LOCATION-A4F834D72840EFC1` |
| `dt.entity.host` | строка | Идентификатор отслеживаемой сущности для цели, если доступен | `HOST-024C103F7F86A290` |
| `dt.maintenance_window_ids` | массив | UUID окон обслуживания | `c715d677-eb1b-3e1b-8dbc-db06cad5b8eb` |
| `dt.synthetic.monitored_entity_ids` | массив | Идентификаторы отслеживаемых сущностей | `APPLICATION-EA7C4B59F27D43EB` |
| `dt.security_context` | строка | Контекст безопасности используется в разрешениях доступа для ограничения видимости | `mySecurityContext` |
| `step.id` | числовой | Порядковый идентификатор шага | `1` |
| `request.id` | числовой | Порядковый идентификатор запроса | `2` |
| `request.type` | строка | Тип запроса | `icmp`, `tcp` |
| `request.target_address` | строка | Адрес целевой сущности | `54.171.216.19` |
| `result.state` | строка | Состояние результата выполнения монитора | `SUCCESS`, `FAIL` |
| `result.status.message` | строка | Статус выполнения | `HEALTHY`, `CONSTRAINT_VIOLATED` |
| `result.status.code` | числовой | Числовое представление статуса выполнения | `0`, `1401` |
| `interpolated` | булев | Информация о том, была ли интерполирована доступность монитора | `false` |
| `multi_protocol.step.id` | числовой | Порядковый идентификатор шага (устарело, используйте `step.id`) | `1` |
| `multi_protocol.request.id` | числовой | Порядковый идентификатор запроса (устарело, используйте `request.id`) | `2` |
| `multi_protocol.request.type` | строка | Тип запроса (устарело, используйте `request.type`) | `icmp`, `tcp` |
| `multi_protocol.request.target_address` | строка | Адрес целевой сущности (устарело, используйте `request.target_address`) | `54.171.216.19` |
| `multi_protocol.result.state` | строка | Состояние результата выполнения монитора (устарело, используйте `result.state`) | `SUCCESS` |
| `multi_protocol.result.status` | строка | Статус выполнения (устарело, используйте `result.status.message`) | `HEALTHY`, `CONSTRAINT_VIOLATED` |
| `multi_protocol.result.status.code` | числовой | Числовое представление статуса выполнения (устарело, используйте `result.status.code`) | `0`, `1401` |

### Метрики монитора (все мониторы доступности сети)

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.availability` (последняя Dynatrace) `builtin:synthetic.multiProtocol.availability` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `interpolated` | Доступность, рассчитанная на основе статуса выполнения посещений — 100% для кода=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` — 0% для кодов ошибок, например `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.execution_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.executionTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` | Продолжительность между временем начала и окончания выполнения посещения (в миллисекундах). Метрика доступна только при выполнении посещения; необходимо наличие как времени начала, так и времени окончания. |
| `dt.synthetic.multi_protocol.executions` (последняя Dynatrace) `builtin:synthetic.multiProtocol.executions` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `dt.maintenance_window_ids` `result.state` `result.status.code` `result.status.message` `multi_protocol.result.state` (устарело, используйте `result.state`) `multi_protocol.result.status.code` (устарело, используйте `result.status.code`) `multi_protocol.result.status` (устарело, используйте `result.status.message`) | Количество выполнений монитора за период времени |
| `dt.synthetic.multi_protocol.success_rate` (последняя Dynatrace) `builtin:synthetic.multiProtocol.successRate` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` | Отношение выполненных шагов, не завершившихся сбоем (успехи + пропуски), ко всем выполненным шагам. Учитываются шаги, которые фактически были выполнены, а не шаги, которые предполагалось выполнить. Например, при 2 успешных шагах, 1 неуспешном и 8 не начатых отношение равно 2/3, или 66,67%. |

### Метрики шагов (все мониторы доступности сети)

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.step.availability` (последняя Dynatrace) `builtin:synthetic.multiProtocol.step.availability` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Доступность, рассчитанная на основе статуса выполнения шагов — 100% для кода=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` — 0% для кодов ошибок, например `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.step.execution_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.step.executionTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Продолжительность между временем начала и окончания выполнения шага (в миллисекундах). Метрика доступна только при выполнении шага с чётко определённым временем окончания; поэтому она недоступна для [пропущенных](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-setup "Узнайте, как настроить монитор NAM для проверки производительности и доступности вашего сайта.") шагов. |
| `dt.synthetic.multi_protocol.step.executions` (последняя Dynatrace) `builtin:synthetic.multiProtocol.step.executions` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `result.state` `result.status.code` `result.status.message` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.type` (устарело, используйте `request.type`) `multi_protocol.result.state` (устарело, используйте `result.state`) `multi_protocol.result.status` (устарело, используйте `result.status.message`) `multi_protocol.result.status.code` (устарело, используйте `result.status.code`) | Количество выполнений шагов за период времени |
| `dt.synthetic.multi_protocol.step.success_rate` (последняя Dynatrace) `builtin:synthetic.multiProtocol.step.successRate` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Отношение выполненных запросов, не завершившихся сбоем, ко всем выполненным запросам. Если у шага нет выполненных запросов (потому что [ничто не соответствует](/docs/observe/digital-experience/synthetic-monitoring/network-availability-monitors/create-a-nam-monitor#nam-setup "Узнайте, как настроить монитор NAM для проверки производительности и доступности вашего сайта.") его определению в конфигурации монитора), возвращается значение 100%. Например, при 2 успешных запросах и 1 неуспешном отношение равно 2/3, или 66,67%. |

### Метрики запросов (все мониторы доступности сети)

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.request.availability` (последняя Dynatrace) `builtin:synthetic.multiProtocol.request.availability` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Доступность, рассчитанная на основе статуса выполнения запросов — 100% для кода=`0`: `HEALTHY`, `SCRIPT_FINISH`, `SKIPPED` — 0% для кодов ошибок, например `1401 - CONSTRAINT_VIOLATED` |
| `dt.synthetic.multi_protocol.request.executions` (последняя Dynatrace) `builtin:synthetic.multiProtocol.request.executions` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.synthetic.monitored_entity_ids` `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `result.state` `result.status.code` `result.status.message` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) `multi_protocol.result.state` (устарело, используйте `result.state`) `multi_protocol.result.status` (устарело, используйте `result.status.message`) `multi_protocol.result.status.code` (устарело, используйте `result.status.code`) | Количество выполнений запросов за период времени |

### Метрики монитора ICMP

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.icmp.success_rate` (последняя Dynatrace) `builtin:synthetic.multiProtocol.icmp.successRate` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Отношение полученных пакетов к отправленным пакетам. Не учитывает настроенное количество пакетов для отправки. Например, из 10 пакетов для отправки, если было отправлено 5 и получено 4, отношение равно 4/5, или 80,00%. |
| `dt.synthetic.multi_protocol.icmp.packets_sent` (последняя Dynatrace) `builtin:synthetic.multiProtocol.icmp.packetsSent` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Общее количество отправленных пакетов |
| `dt.synthetic.multi_protocol.icmp.packets_received` (последняя Dynatrace) `builtin:synthetic.multiProtocol.icmp.packetsReceived` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Количество успешно возвращённых пакетов |
| `dt.synthetic.multi_protocol.icmp.round_trip_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.icmp.roundTripTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Время кругового обхода (RTT) для полученных пакетов |
| `dt.synthetic.multi_protocol.icmp.request_execution_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.icmp.requestExecutionTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) | Продолжительность между временем начала и окончания обработки запроса (в миллисекундах). Эта метрика всегда предоставляется, даже если фактическое выполнение запроса не произошло (например, из-за исключений или таймаутов). Диагностическая метрика — позволяет проверить время выполнения внешнего процесса ping. |

### Измерения монитора TCP

| Имя | Тип | Описание | Пример значения |
| --- | --- | --- | --- |
| `request.tcp_port_number` | строка | Номер порта TCP-запроса в соответствии с конфигурацией монитора | `665` |
| `multi_protocol.request.tcp_port_number` | строка | Номер порта TCP-запроса в соответствии с конфигурацией монитора (устарело, используйте `request.tcp_port_number`) | `665` |

### Метрики монитора TCP

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.tcp.connection_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.tcp.connectionTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) `request.tcp_port_number` `multi_protocol.request.tcp_port_number` (устарело, используйте: `request.tcp_port_number`) | Продолжительность между временем начала (создание и подключение сокета) и временем окончания (успешное установление соединения) в миллисекундах. Метрика доступна только при выполнении запроса (без исключений или таймаутов) с чётко определённым временем окончания. |

### Измерения монитора DNS

| Имя | Тип | Описание | Пример значения |
| --- | --- | --- | --- |
| `request.dns_record_type` | строка | Тип DNS-записи для запроса в соответствии с конфигурацией | `A`, `AAAA`, `CNAME` |
| `multi_protocol.request.dns_record_type` | строка | Тип DNS-записи для запроса в соответствии с конфигурацией (устарело, используйте `request.dns_record_type`) | `A`, `AAAA`, `CNAME` |

### Метрики монитора DNS

| Имя | Тип | Измерения | Описание |
| --- | --- | --- | --- |
| `dt.synthetic.multi_protocol.dns.resolution_time` (последняя Dynatrace) `builtin:synthetic.multiProtocol.dns.resolutionTime` (предыдущая Dynatrace) | числовой | `dt.entity.multiprotocol_monitor` `dt.entity.synthetic_location` `dt.entity.host` (только для мониторов с определённым фильтром) `dt.security_context` `step.id` `request.id` `request.target.address` `request.type` `multi_protocol.step.id` (устарело, используйте `step.id`) `multi_protocol.request.id` (устарело, используйте `request.id`) `multi_protocol.request.target_address` (устарело, используйте `request.target.address`) `multi_protocol.request.type` (устарело, используйте `request.type`) `request.dns_record_type` `multi_protocol.request.dns_record_type` (устарело, используйте: request.dns\_record\_type) | Продолжительность между временем начала и окончания запроса к DNS-серверу в миллисекундах. Метрика доступна только при выполнении запроса (без исключений или таймаутов) с чётко определённым временем окончания. |

## Запросы DQL для извлечения данных

Используйте запросы [DQL](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.") для извлечения данных с метриками и измерениями.

Следующие примеры используют [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь наблюдениями из ваших данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") для демонстрации работы с результатами мониторов доступности сети. В качестве отправной точки используются метрики результатов для исследования возможностей извлечения и интерпретации данных с помощью DQL.

### Статус сущности хоста для ICMP-запросов

Монитор `MULTIPROTOCOL_MONITOR-5C2F92334DF71A90` выполняет ICMP-запросы и фильтрует отслеживаемые хосты с помощью `"targetFilter": "hostGroup == e2e-synthetic-private-location"` (что соответствует примерно 26 хостам).

Используя метрику `dt.synthetic.multi_protocol.request.executions` и разбивая её по измерениям `dt.entity.host` и `result.status.message`, можно отобразить статус соединения с конкретной отслеживаемой сущностью хоста в этой группе хостов. Некоторые хосты не выполняют ожидаемый процент успешных; вместо статуса `HEALTHY` их запросы помечены как `CONSTRAINT_VIOLATED`.

```
Timeseries status = avg(dt.synthetic.multi_protocol.request.executions),



by:{dt.entity.host, result.status.message},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-5C2F92334DF71A90"
```

![Статус сущности хоста для ICMP-запросов](https://dt-cdn.net/images/nam-tcp-connect-ports-notebooks-dql-1920-06e2eeb631.webp)

### Количество отправленных и полученных ICMP-пакетов

Монитор `MULTIPROTOCOL_MONITOR-548C3CD54183CED9` выполняет ICMP-запросы к хостам с явно заданными IP-адресами: `18.x.x.x`, `10.x.x.x` и `34.x.x.x`. Каждый из этих IP-адресов соответствует отдельному хосту.

Мы используем суммы метрик `dt.synthetic.multi_protocol.icmp.packets_sent` и `dt.synthetic.multi_protocol.icmp.packets_received`, чтобы узнать, сколько пакетов было отправлено и получено.

Результаты разбиваются по измерению `request.target_address` и фильтруются только для `18.x.x.x` и `10.x.x.x`.

Для `18.x.x.x` количество полученных пакетов совпадает с количеством отправленных, но для `10.x.x.x` все пакеты потеряны и ни одного не получено.

```
timeseries {



packets_sent = sum(dt.synthetic.multi_protocol.icmp.packets_sent),



packets_received= sum(dt.synthetic.multi_protocol.icmp.packets_received)



},



by:{request.target_address},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-548C3CD54183CED9"



AND (



request.target_address == "18.x.x.x"



OR request.target_address == "10.x.x.x"



)
```

![Отправленные и полученные ICMP-пакеты](https://dt-cdn.net/images/nam-icmp-packets-notebooks-dql-1638-3577d87f09.webp)

### Статус цели для TCP-запросов

Монитор `MULTIPROTOCOL_MONITOR-74E68F22FF5E9227` выполняет TCP-запросы к хостам из группы хостов, соответствующей IP-адресам `18.x.x.x`, `34.x.x.x` и `44.x.x.x`.

Для отображения статуса TCP-соединения для пары IP-порт используем метрику `dt.synthetic.multi_protocol.request.executions`, разбивая её по измерениям:

* `request.target_address`
* `request.tcp_port_number`
* `result.status.message`

В этом примере:

* На каждом хосте открыты порты `22` (SSH) и `8080` (HTTP-сервер), и каждое соединение с хостами по этим портам завершается со статусом `HEALTHY`.
* Ни одна служба не использует стандартный HTTP-порт `80`. Поэтому соединения со всеми хостами по этому порту завершаются со статусом `TCP socket connection error`.

Обратите внимание, что результаты этого запроса можно ограничить только успешными запросами, фильтруя по измерению `multi_protocol.result.status.code` (`code == 0`).

```
timeseries status = sum(dt.synthetic.multi_protocol.request.executions),



by: {request.target_address, request.tcp_port_number, result.status.message},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-74E68F22FF5E9227"



//  and result.status.code == 0
```

![Статус цели для TCP-запросов](https://dt-cdn.net/images/nam-target-status-tcp-requests-notebooks-dql-1727-4326a4411c.webp)

### Время TCP-соединения с целевым портом

Монитор `MULTIPROTOCOL_MONITOR-74E68F22FF5E9227` выполняет TCP-запросы к хостам из группы хостов, соответствующей IP-адресам `18.x.x.x`, `34.x.x.x` и `44.x.x.x`.

В этом примере вместо IP-адресов результаты разбиваются по идентификаторам отслеживаемых сущностей хостов.

Для проверки типичного времени успешного соединения с целевым портом для хоста используем среднее значение метрики `dt.synthetic.multi_protocol.tcp.connection_time`, разбивая по измерениям:

* `dt.entity.host`
* `request.target_address`
* `request.tcp_port_number`

Открыты только порты `22` (SSH) и `8080` (HTTP-сервер), и только для них доступна метрика `dt.synthetic.multi_protocol.tcp.connection_time`. Хосты эффективно находятся в разных географических местах (Огайо, Орегон и Северная Вирджиния в США), поэтому разница в времени соединения ожидаема.

```
timeseries duration = avg(dt.synthetic.multi_protocol.tcp.connection_time),



by:{dt.entity.host, request.target_address, request.tcp_port_number},



filter: dt.entity.multiprotocol_monitor == "MULTIPROTOCOL_MONITOR-74E68F22FF5E9227"
```

![Время TCP-соединения с целевым портом](https://dt-cdn.net/images/nam-tcp-connect-time-notebooks-dql-1720-3e3235b23d.webp)

## Статусы выполнения

### Все мониторы доступности сети

| Код / сообщение | Пример | Описание |
| --- | --- | --- |
| `0 HEALTHY` | - | Всё в порядке. |
| `-1 UNEXPECTED_ERROR` | Насыщение ресурсов | Неожиданная проблема, обычно связанная с компонентами выполнения монитора. |
| `1401 CONSTRAINT_VIOLATED` | - | Условия ограничений, определённые в конфигурации монитора, не выполнены. |
| `1604 VALIDATION_ERROR` | - | Обнаружена некорректная конфигурация монитора. |
| `12013 UNKNOWN_HOST` | Ошибка в имени хоста | Невозможно определить IP-адрес хоста. Возможные причины: — Неверное имя хоста — DNS-сервер недоступен — Проблемы с кешем DNS — Вмешательство брандмауэра или прокси |
| `12033 Execution timeout` | Сервер работает медленно. | Таймаут выполнения запроса. Возможные причины: — Сетевые проблемы — Медленный или не отвечающий сервер или служба — Соединение заблокировано правилами брандмауэра — Слишком маленький таймаут. |

### Статусы выполнения монитора TCP

| Код / сообщение | Пример | Описание |
| --- | --- | --- |
| `22000 TCP socket connection error` | Служба не прослушивает указанный порт. | Этот статус означает, что хост был идентифицирован и доступен, но TCP-соединение не удалось установить или было неожиданно закрыто. Предоставляется дополнительное пояснение для конкретного исключения. Статус используется, если при попытке соединения выбрасывается исключение `java.net.SocketException`. Возможные причины: — Служба не прослушивает указанный порт. — Служба достигла лимита ресурсов или соединений. — Служба стала недоступна в процессе установки соединения через сокет. |
