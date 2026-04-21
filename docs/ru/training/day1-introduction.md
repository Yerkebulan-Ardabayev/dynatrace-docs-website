---
title: "День 1 — Введение в систему Dynatrace"
description: "Walkthrough-гайд: архитектура, компоненты, интерфейс, ключевые объекты, Problems, дашборды"
---

# День 1 — Введение в систему Dynatrace

> **Формат**: ты сидишь перед открытым Dynatrace Managed environment и рассказываешь коллегам, показывая всё live. Ниже — полный скрипт: что говорить, куда кликать, что объяснять. Всё из головы, никаких слайдов.

---

## 1. Архитектура Dynatrace

???+ tip "Что говорить, открыв главную страницу"

    Итак, перед нами Dynatrace Managed — это on-premise вариант платформы. The point is, что вся архитектура здесь трёхуровневая, и это important понимать с самого начала.

### Три уровня архитектуры

**Уровень 1 — OneAgent (на каждом хосте)**

OneAgent — это lightweight-агент, который устанавливается на каждый хост, будь то bare-metal сервер, VM или контейнер. Его job — собирать все данные: метрики CPU/RAM/disk/network, трейсы запросов внутри процессов, логи. Actually, OneAgent делает deep code-level instrumentation — он инжектится в runtime процессов (Java, .NET, Node.js, Go, PHP, Python и т.д.) и перехватывает вызовы на уровне байткода или native-хуков.

Что это значит на практике? Тебе не нужно менять ни строчки кода в приложении. Поставил агент — и через пару минут Dynatrace уже видит все сервисы, все зависимости, все запросы.

**Уровень 2 — ActiveGate (промежуточный шлюз)**

ActiveGate — это proxy и router между OneAgent-ами и серверной частью. By the way, у него несколько ролей:

- **Communication gateway** — сжимает и маршрутизирует трафик от агентов к серверу. Если у тебя 500 хостов, ты не хочешь, чтобы все 500 били напрямую в кластер — ActiveGate агрегирует это.
- **Monitoring extensions** — запускает плагины для мониторинга того, куда OneAgent не ставится: сетевые устройства (SNMP), базы данных через JDBC, облачные API (AWS CloudWatch, Azure Monitor, GCP).
- **Synthetic monitoring** — если нужно запускать синтетические браузерные тесты из твоей сети, это делает ActiveGate с модулем Synthetic.

В Managed-версии ActiveGate also выполняет роль Cluster ActiveGate — он маршрутизирует трафик внутрь кластера.

**Уровень 3 — Серверная часть (Managed Cluster)**

В случае Dynatrace Managed серверная часть — это кластер нод, которые ты разворачиваешь on-premise. Каждая нода содержит:

- **Server** — обработка данных, аналитика Davis AI, хранение
- **Cassandra** — долговременное хранилище метрик и конфигураций (Cassandra Hypercube в SaaS)
- **Elasticsearch** — индексация для поиска и логов

Minimum — одна нода, для production рекомендуется три ноды (high availability). Anyway, вся эта архитектура работает so, что данные от OneAgent проходят через ActiveGate, попадают на сервер, и Davis AI в real-time анализирует все аномалии.

???+ note "Где это видно в интерфейсе"

    Зайди в **Manage → Deployment Status** — здесь показаны все подключённые OneAgent-ы, их версии, статус связи. А **Manage → OneAgent Health** покажет, если какой-то агент нездоров.

---

## 2. Компоненты системы: OneAgent, ActiveGate, серверная часть

???+ tip "Показывай: Manage → Deploy Dynatrace"

    Кликаем слева в меню **Manage → Deploy Dynatrace**. Вот эта страница — entry point для установки компонентов.

### OneAgent — подробнее

OneAgent работает как один процесс на хосте. No worries — он потребляет мало ресурсов (typically 1-2% CPU, ~100-300 МБ RAM). Вот что он делает:

| Capability | Описание |
|---|---|
| **Auto-discovery** | Находит все процессы, сервисы, контейнеры на хосте |
| **Code-level tracing** | Инструментирует bytecode Java, .NET CLR, Node.js V8 и т.д. |
| **Full-stack metrics** | CPU, Memory, Disk I/O, Network — на уровне хоста и процесса |
| **Log collection** | Собирает логи процессов и системные логи |
| **Network monitoring** | Видит TCP/UDP connections, latency между процессами |

Установка — буквально одна команда:

```bash
# Linux
wget -O Dynatrace-OneAgent.sh "https://<your-managed>/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=<TOKEN>"
sudo /bin/sh Dynatrace-OneAgent.sh

# Windows
Invoke-WebRequest -Uri "https://<your-managed>/api/v1/deployment/installer/agent/windows/default/latest?Api-Token=<TOKEN>" -OutFile Dynatrace-OneAgent.exe
.\Dynatrace-OneAgent.exe
```

After installation, агент автоматически стартует, коннектится к серверу через ActiveGate (или напрямую) и начинает discovery.

### ActiveGate — подробнее

ActiveGate ставится separately. В Managed-среде у тебя уже есть встроенный Cluster ActiveGate, но для Production-окружений рекомендуется ставить Environment ActiveGate separately — для routing трафика, extensions, synthetic.

### Серверная часть Managed

The point is — в Managed всё у тебя: данные не уходят наружу. Кластер управляется через **Cluster Management Console (CMC)** — это отдельный web UI для администрирования нод, лицензий, обновлений.

---

## 3. Принцип работы и возможности OneAgent

???+ tip "Показывай: Manage → Deployment Status → OneAgent"

    Вот здесь мы видим список всех хостов с установленным OneAgent, их версии, статус обновления.

### Как OneAgent обнаруживает всё автоматически

Процесс такой:

1. **Process detection** — OneAgent сканирует запущенные процессы на хосте. Для каждого определяет technology (Java, .NET, Apache, nginx, Node.js, Go...) по сигнатурам бинарников и аргументам запуска.

2. **Process Group formation** — одинаковые процессы (например, три инстанса одного Java-сервиса) объединяются в Process Group. Это logical grouping — чтобы не смотреть на каждый PID отдельно.

3. **Service detection** — OneAgent находит entry points в коде (HTTP listeners, message queue consumers, database calls) и создаёт объект Service. Один Process Group может содержать несколько сервисов.

4. **Application mapping** — если процесс обслуживает web-запросы, OneAgent инжектит JavaScript-тег в HTML-ответы (RUM injection). Это даёт end-to-end visibility от браузера пользователя до backend.

5. **Topology building** — все связи (кто кого вызывает) автоматически строятся в Smartscape на основе реальных network connections и code-level traces.

### Что OneAgent НЕ делает

- Не меняет код приложения (zero-code approach)
- Не требует рестарта приложения в большинстве случаев (кроме .NET на Windows)
- Не шлёт данные за пределы твоей сети (в Managed-версии everything stays on-premise)

---

## 4. Цифровой опыт (Digital Experience Monitoring)

???+ tip "Показывай: левое меню → Digital Experience → Web"

    Открываем раздел **Digital Experience → Web**. Здесь мы видим список веб-приложений, которые Dynatrace мониторит с точки зрения реального пользователя.

### Что такое DEM

Digital Experience Monitoring — это approach к мониторингу, где ты смотришь на систему глазами пользователя. Not just "сервер отвечает за 200мс", а "пользователь в Алматы открыл страницу и увидел её через 3.2 секунды, при этом First Contentful Paint был 1.1с".

### Два подхода в Dynatrace

**Real User Monitoring (RUM)** — мониторинг реальных пользователей. OneAgent инжектит JavaScript-сниппет в HTML-страницы. Этот сниппет (called "RUM agent") собирает:

- Page load timings (W3C Navigation Timing API)
- XHR/Fetch calls — AJAX-запросы
- JavaScript errors
- User actions — клики, ввод текста, скролл
- Session data — вся цепочка действий пользователя

**Synthetic Monitoring** — ты создаёшь скрипты, которые эмулируют поведение пользователя (открой URL, кликни кнопку, проверь что страница загрузилась). Эти скрипты запускаются по расписанию с ActiveGate. Useful для:

- Мониторинг доступности 24/7 (даже когда реальных пользователей нет)
- SLA-мониторинг
- Проверка critical user journeys

### Ключевые метрики DEM

| Метрика | Что значит |
|---|---|
| **Apdex** | Application Performance Index: 0-1, где 1 = все довольны. Считается на основе порогов response time |
| **Visually Complete** | Когда пользователь видит полностью отрисованную страницу |
| **Speed Index** | Как быстро контент появляется в viewport |
| **First Input Delay** | Задержка от первого клика до реакции |
| **Load Event End** | Когда браузерный load event завершился |
| **Actions per minute** | Интенсивность взаимодействий пользователей |

---

## 5. Обзор интерфейса и навигации

???+ tip "Показывай: главный экран, левое меню"

    Ок, давайте пройдёмся по интерфейсу. Смотрите на левую панель — это основная навигация. Пойдём сверху вниз.

### Левая навигационная панель

Вот все секции, which you can see прямо сейчас:

**Favorites** — здесь пины, которые ты добавил для быстрого доступа. По дефолту: Dashboards, Deploy Dynatrace, Problems.

**Observe and explore** — основной раздел для ежедневной работы:

- **Dashboards** — пользовательские и системные дашборды
- **Data Explorer** — построение кастомных графиков по любым метрикам
- **Metrics** — каталог всех метрик в системе (built-in + custom)
- **Logs** — централизованный просмотр логов
- **Problems** — автоматически детектированные инциденты (Davis AI)
- **Smartscape Topology** — визуальная карта зависимостей
- **Reports** — сгенерированные отчёты

**Infrastructure Observability** — всё про инфраструктуру:

- **Hosts** — серверы, VM-ки с метриками OS
- **Technologies & Processes** — процессы сгруппированные по технологии
- **Kubernetes** — кластеры, ноды, поды, ворклоады
- **Containers** — контейнеры Docker/containerd
- **Cloud providers** — AWS, Azure, GCP, VMware
- **Extensions** — мониторинг через плагины (SNMP, JMX, SQL и т.д.)

**Application Observability** — backend и traces:

- **Services** — все обнаруженные сервисы
- **Frontend** — web/mobile фронтенды
- **Distributed Traces** — сквозные трейсы запросов
- **Database Services** — база данных как сервис
- **Synthetic** — синтетические мониторы

**Application Security** — уязвимости и атаки

**Digital Experience** — пользовательский опыт (RUM и Synthetic)

**Business Analytics** — бизнес-события и пользовательские сессии

**Manage** — администрирование:

- **Dynatrace Hub** — маркетплейс расширений
- **Deploy Dynatrace** — установка агентов
- **Settings** — все настройки

### Верхняя панель

- **Search bar** (Ctrl+Shift+F) — глобальный поиск по entities, metrics, settings
- **Time selector** — выбор временного диапазона (дефолт: Last 2 hours)
- **Management zone filter** — фильтрация по зонам управления (сегментация данных)
- **Problems indicator** — красный badge с количеством активных проблем

???+ example "Live demo: покажи поиск"

    Нажми Ctrl+Shift+F или кликни на строку поиска. Начни набирать имя хоста или сервиса — Dynatrace ищет по всем entities в real-time. Это самый быстрый способ навигации.

---

## 6. Топология Smartscape

???+ tip "Показывай: Observe and explore → Smartscape Topology"

    Кликаем **Smartscape Topology** в левом меню. Вот она — визуальная карта всей нашей среды.

### Что такое Smartscape

Smartscape — это real-time topology map всей среды. Think of it как Google Maps, но для IT-инфраструктуры. Dynatrace строит её автоматически на основе данных от OneAgent — никакой ручной конфигурации.

### Горизонтальные слои

Smartscape организован по слоям (tiers), снизу вверх:

| Слой | Что содержит | Пример |
|---|---|---|
| **Data Centers** | Дата-центры, облачные зоны | AWS eu-west-1, On-prem DC1 |
| **Hosts** | Серверы, VM | linux-prod-01, win-app-02 |
| **Process Groups** | Группы процессов | java-easytravel-backend (x3) |
| **Services** | Логические сервисы | BookingService, PaymentGateway |
| **Applications** | Web-приложения (frontend) | EasyTravel Angular |

### Вертикальные связи

Каждый уровень связан с соседним:

- Application **вызывает** → Service
- Service **выполняется в** → Process Group
- Process Group **работает на** → Host
- Host **расположен в** → Data Center

Эти связи — не configuration, а **реальные discovered dependencies**. Если BookingService вызывает PaymentService, ты увидишь стрелку между ними. Если ProcessGroup работает на трёх хостах — увидишь три линии вниз.

### Зачем это нужно

1. **Impact analysis** — если хост деградирует, ты сразу видишь, какие процессы, сервисы и приложения затронуты
2. **Root cause analysis** — от проблемы на уровне приложения проваливаешься вниз до конкретного хоста
3. **Change tracking** — Smartscape показывает, когда появились новые сервисы или изменились зависимости

???+ example "Live demo: кликни на любой узел"

    Кликни на любой сервис или хост в Smartscape. Откроется карточка с деталями — и ты можешь drill down в метрики этого entity.

---

## 7. Хосты, процессы, сервисы, приложения — обзор ключевых объектов

???+ tip "Показывай: Infrastructure → Hosts"

    Открываем **Infrastructure Observability → Hosts**. Это список всех хостов, на которых стоит OneAgent.

### Host (Хост)

Хост — это физический или виртуальный сервер. Каждый хост в Dynatrace — это entity с уникальным ID. Что ты видишь на странице хоста:

- **CPU usage** — загрузка процессора (total и per-core)
- **Memory usage** — использование оперативной памяти
- **Disk I/O** — чтение/запись на диски
- **Network** — входящий/исходящий трафик
- **Running processes** — все запущенные процессы с группировкой
- **Problems** — активные проблемы, связанные с этим хостом
- **Properties** — OS version, IP, cloud provider metadata, tags

???+ example "Live demo: кликни на любой хост"

    Выбери хост из списка. Обрати внимание: справа сразу видны Technology overview (какие технологии запущены) и связанные entities.

### Process Group (Группа процессов)

???+ tip "Показывай: Infrastructure → Technologies & Processes"

    Переходим в **Technologies & Processes**. Здесь процессы сгруппированы по технологии: Java, .NET, Node.js, Apache, nginx...

Process Group — это логическое объединение одинаковых процессов. Например, если у тебя 3 инстанса Java-приложения на разных хостах, Dynatrace объединяет их в один Process Group. Это удобно — ты видишь метрики агрегированно по группе, а не ковыряешься по каждому PID.

На странице Process Group видны:

- Resource consumption (CPU, Memory)
- Suspension & IO wait time
- Связанные Services
- Хосты, на которых запущены инстансы

### Service (Сервис)

???+ tip "Показывай: Application Observability → Services"

    Открываем **Application Observability → Services**. Вот список всех automatically detected сервисов.

Service — это the most important entity в Dynatrace для APM. Сервис — это логический endpoint, который обрабатывает запросы. Dynatrace автоматически создаёт сервис, когда обнаруживает:

- HTTP/HTTPS listener
- Message queue consumer (Kafka, RabbitMQ, JMS)
- Database query handler
- RPC/gRPC endpoint
- Custom SDK entry points

На странице сервиса ты видишь:

- **Response time** — среднее, медиана, перцентили (P90, P95, P99)
- **Throughput** — requests per minute
- **Failure rate** — процент ошибок
- **Service flow** — visual map: кто вызывает этот сервис и кого вызывает он
- **Top requests** — самые частые/медленные запросы
- **Backtrace** — кто вызывает этот сервис
- **Database statements** — какие SQL-запросы выполняются

### Application (Приложение)

???+ tip "Показывай: Digital Experience → Web"

    Переходим в **Digital Experience → Web**. Это frontend applications — то, что видит конечный пользователь.

Application в Dynatrace — это web или mobile приложение, которое мониторится через RUM (Real User Monitoring). OneAgent inject-ит JavaScript snippet в HTML-ответы сервера, и этот snippet собирает данные о real user experience.

На странице приложения:

- **Apdex score** — satisfaction index
- **User actions** — загрузки страниц, XHR, клики
- **JavaScript errors** — ошибки на стороне клиента
- **Sessions** — количество пользовательских сессий
- **Geographic distribution** — откуда приходят пользователи
- **Top pages / User actions** — самые популярные действия

---

## 8. Встроенные метрики и Data Explorer

???+ tip "Показывай: Observe and explore → Data Explorer"

    Открываем **Data Explorer**. Это наш main tool для ad-hoc анализа метрик.

### Встроенные метрики (Built-in Metrics)

Dynatrace out-of-the-box собирает тысячи метрик. The main categories:

| Категория | Примеры метрик | Prefix |
|---|---|---|
| **Host** | CPU usage, Memory used, Disk read/write bytes | `builtin:host.*` |
| **Process** | CPU time, Memory RSS, Suspension time | `builtin:tech.*` |
| **Service** | Response time, Throughput, Failure rate | `builtin:service.*` |
| **Application** | Action duration, JavaScript errors, Apdex | `builtin:apps.*` |
| **Synthetic** | Availability, Response time, Step duration | `builtin:synthetic.*` |
| **Network** | Retransmissions, Connectivity, Round-trip time | `builtin:host.net.*` |
| **Kubernetes** | Pod CPU, Node memory, Container restarts | `builtin:cloud.kubernetes.*` |

### Работа в Data Explorer

Data Explorer — это visual query builder для метрик. Вот как он работает:

1. **Выбор метрики** — начни набирать имя (например, `cpu`) и увидишь все подходящие метрики. Можно фильтровать по категориям.

2. **Пространственная агрегация (Space aggregation)** — как агрегировать по dimensions. Если метрика `host.cpu.usage` имеет dimension `host`, ты выбираешь: Average, Max, Min, Sum, Count. По дефолту — Auto.

3. **Split by** — разбить по измерению. Например, `host.cpu.usage` split by `dt.entity.host` покажет линию для каждого хоста.

4. **Filter** — фильтрация. Можно по тегам, management zones, конкретным entities.

5. **Visualization** — выбор типа графика: Line, Bar, Area, Single Value, Table, Heatmap, Honeycomb, Pie, Top list.

6. **Pin to Dashboard** — любой построенный график можно одним кликом закрепить на дашборд.

???+ example "Live demo: построй график CPU"

    В Data Explorer набери `builtin:host.cpu.usage`, выбери Split by → Host, визуализация → Graph. Вот — загрузка CPU по каждому хосту за последние 2 часа. Теперь поменяй timeframe на Last 24 hours — видишь daily pattern?

### Metrics Browser

???+ tip "Показывай: Observe and explore → Metrics"

    Отдельно есть **Metrics** — это каталог (browser) всех доступных метрик. Можно искать, фильтровать по source, смотреть описание и dimensions каждой метрики. Useful когда ты не знаешь exact metric name.

---

## 9. Построение базовых линий и работа с порогами

???+ tip "Объясняй теорию, потом покажи: Settings → Anomaly Detection"

    Это одна из самых powerful фич Dynatrace. The point is — тебе не нужно вручную задавать пороги для alert-ов. Davis AI делает это автоматически.

### Что такое Baseline (базовая линия)

Dynatrace применяет **automated multidimensional baselining**. Это значит:

- Для каждого сервиса, для каждого хоста, для каждой метрики Dynatrace автоматически строит "нормальный" паттерн поведения
- Baseline учитывает **время суток**, **день недели**, **сезонность**
- Например, если твой сервис обычно отвечает за 50мс утром и за 120мс в пик-часы — это два разных baseline

Davis AI использует AI-алгоритмы для определения нормального коридора значений. Если значение выходит за границы — создаётся аномалия.

### Типы порогов

**Auto-adaptive thresholds (адаптивные пороги)** — дефолтный режим. Dynatrace сам считает upper и lower bounds на основе исторических данных. No configuration needed.

**Static thresholds (статические пороги)** — ты задаёшь конкретное значение. Например: "алерт если CPU > 90%". Это classic monitoring approach, иногда нужен для compliance.

**Metric events** — кастомные правила алертинга на основе метрик с DQL-запросами и complex conditions. Это для advanced use cases.

### Настройка чувствительности

???+ tip "Показывай: Settings → Anomaly detection"

    В Settings можно настроить sensitivity для каждого типа entity: Services, Infrastructure, Applications, Databases и т.д.

Для каждого типа entity (сервисы, хосты, приложения) ты можешь:

- Повысить или понизить чувствительность (slider: Low → Medium → High)
- Отключить определённые типы аномалий
- Задать minimum absolute threshold (чтобы не алертить на noise)

Actually, для начала рекомендую оставить всё по дефолту — Davis AI surprisingly хорошо работает out of the box.

---

## 10. Функционал Problems: автоматическая детекция инцидентов

???+ tip "Показывай: Observe and explore → Problems"

    Открываем **Problems**. Это центральное место для работы с инцидентами.

### Как Davis AI создаёт Problem

Процесс detection работает так:

1. **Anomaly detected** — Davis видит, что метрика вышла за baseline (например, response time сервиса вырос в 5 раз)
2. **Event created** — создаётся событие аномалии
3. **Correlation** — Davis ищет другие аномалии, которые happened в то же время и topologically связаны через Smartscape
4. **Problem created** — все связанные аномалии объединяются в один Problem
5. **Root cause identified** — Davis определяет первопричину, "проваливаясь" по Smartscape вниз от пользователя к инфраструктуре

### Анатомия Problem-карточки

Когда ты открываешь Problem, ты видишь:

- **Title** — автоматически сгенерированное описание (например: "Response time degradation on BookingService")
- **Status** — Open / Resolved
- **Duration** — как долго длится проблема
- **Impact** — что затронуто: приложения, сервисы, инфраструктура. Visual impact level: Application, Service, Infrastructure, Environment
- **Root cause** — highlighted entity, который Davis определил как причину
- **Affected entities** — все затронутые entities с drill-down ссылками
- **Events timeline** — хронология всех связанных аномалий на timeline

### Impact Level

Davis классифицирует problems по уровню impact:

| Level | Значение |
|---|---|
| **Application** | Проблема влияет на пользователей (видна на уровне приложения) |
| **Service** | Проблема на уровне backend-сервисов |
| **Infrastructure** | Проблема на уровне хостов/процессов |
| **Environment** | Глобальная проблема среды |

### Почему это лучше traditional мониторинга

В classical мониторинге: у тебя 50 alert-ов, и ты сидишь, разбираешься — это одна проблема или 50 разных? Davis AI автоматически коррелирует все события и создаёт **один Problem** с root cause. Это принципиально другой approach — от alert storm к intelligent incident management.

???+ example "Live demo: открой любой Problem"

    Кликни на любой Problem в списке. Смотри на Root cause section — Davis показывает, какой именно entity является причиной. Потом посмотри на Affected entities — это всё, что was impacted. Обрати внимание на timeline — видишь, как аномалии развивались во времени?

---

## 11. Системные и пользовательские дашборды

???+ tip "Показывай: Observe and explore → Dashboards"

    Открываем **Dashboards**. Здесь ты видишь список всех дашбордов — и preset (системные), и custom (твои).

### Системные дашборды (Preset)

Dynatrace идёт с набором ready-made дашбордов. Они помечены как "Preset" и содержат best-practice визуализации:

- **Kubernetes workload overview** — обзор K8s ворклоадов (CPU, Memory, Pod status)
- **Real User Monitoring** — обзор пользовательского опыта
- **Application Overview** — состояние приложений
- и другие

Preset-дашборды нельзя редактировать напрямую, но можно **Clone** и кастомизировать копию.

### Создание пользовательского дашборда

Для создания нового дашборда:

1. Нажми **Create dashboard**
2. Дай имя
3. Добавляй тайлы (tiles) из палитры справа

### Типы тайлов

Вот основные tiles, которые ты можешь добавить:

**Data tiles (визуализация данных):**

- Graph, Pie, Top list, Single value, Table
- Stacked column, Stacked area, Heatmap, Honeycomb

**Infrastructure tiles:**

- Host health, Network metrics, Database health

**Application tiles:**

- Service health, Application health, User behavior, World map

**Monitoring tiles:**

- Problems — отображает текущие проблемы
- Smartscape — мини-карта топологии
- SLO — статус Service Level Objectives

**Content tiles:**

- Markdown — текст, ссылки, форматирование
- Header — заголовок секции
- Image — вставка изображения

### Management Zones на дашбордах

Important concept — Management Zones. Это способ сегментации данных. Например:

- Management Zone "Production" — только production хосты и сервисы
- Management Zone "Frontend Team" — только фронтенд-приложения и их backend

Дашборд можно фильтровать по Management Zone — и все тайлы автоматически покажут только данные из этой зоны. Это makes sense для мульти-тимных окружений.

### Timeframe

Сверху на дашборде — time selector. Можно выбрать:

- Presets: Last 30 min, 1h, 2h, 6h, 24h, 7d, 30d
- Custom: точный диапазон дат
- Relative expressions: `-2h`, `-7d to now`, `yesterday`
- Business hours: `-1d/d+9h00m to -1d/d+17h00m`

Каждый тайл может also иметь свой собственный timeframe (override дашбордного).

???+ example "Live demo: клонируй Preset дашборд"

    Найди Preset-дашборд (например, Kubernetes workload overview). Нажми кнопку **Clone**. Теперь у тебя есть своя копия — можешь редактировать, добавлять тайлы, менять layout. Try to add a Markdown tile с описанием.

---

## Итоги Дня 1

Сегодня мы прошли фундамент:

| Тема | Key takeaway |
|---|---|
| Архитектура | Три уровня: OneAgent → ActiveGate → Server |
| OneAgent | Zero-code, auto-discovery, full-stack из коробки |
| DEM | Мониторинг глазами пользователя: RUM + Synthetic |
| Навигация | Левое меню — основная навигация, Search — быстрый доступ |
| Smartscape | Автоматическая topology map, 5 слоёв от DC до Application |
| Ключевые объекты | Host → Process Group → Service → Application |
| Метрики и Data Explorer | Thousands built-in метрик, visual query builder |
| Baselines | Автоматические baseline-ы, Davis AI определяет "нормально" |
| Problems | AI-driven incident detection, автокорреляция, root cause |
| Дашборды | Preset + custom, tiles, Management Zones, time selectors |

???+ success "Next step"

    Завтра (День 2) мы нырнём глубже в **инфраструктурный мониторинг**: CPU/RAM/IO на уровне хостов, Kubernetes, контейнеры, базы данных. А пока — покликайте по интерфейсу, попробуйте открыть разные entities, построить графики в Data Explorer.
