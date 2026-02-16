---
title: Концепции анализа коренной причины
source: https://www.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis/concepts
scraped: 2026-02-16T21:10:18.127897
---

# Концепции анализа коренной причины

# Концепции анализа коренной причины

* Latest Dynatrace
* Объяснение
* 11-минутное чтение
* Обновлено 28 января 2026 г.

По мере увеличения сложности и масштаба архитектур динамических систем команды ИТ сталкиваются с возрастающим давлением, чтобы быстро обнаруживать и реагировать на инциденты, критически важные для бизнеса, в своих многооблачных средах. Инциденты могут повлиять на один или несколько компонентов ИТ, что в конечном итоге приводит к крупным сбоям, которые выводят из строя критически важные бизнес-сервисы и приложения. Такие сервисы и приложения (например, системы учета или веб-магазины) состоят из многих разных компонентов, которые зависят друг от друга, чтобы работать надежно и обеспечивать отличный опыт пользователя. Если критический компонент выходит из строя, эффект домино негативно влияет на многие другие зависимые компоненты, что приводит к крупномасштабному инциденту.

Концепции, такие как Цели уровня обслуживания (SLO), устанавливают основу доверия между отдельными компонентами и смещают ответственность в сторону команд, которые разрабатывают и владеют этими компонентами. Хотя SLO отлично подходят для получения машинно-читаемого понимания того, что такое нормальные границы работы для отдельных сервисов, они не обеспечивают более глубокого понимания причины проблемы и лучшего исправления.

Анализ коренной причины призван заполнить этот пробел, используя всю доступную контекстную информацию для оценки инцидента и определения его точной коренной причины. Также важно оценить влияние инцидента, что позволяет команде операций быстро классифицировать инцидент и сократить среднее время ремонта (MTTR).

Эта страница знакомит с следующими основными концепциями:

[Инциденты и проблемы](#инциденты-проблемы)  
[События Davis](#события-davis)  
[Анализ коренной причины](#анализ-коренной-причины)  
[Анализ дерева неисправностей](#анализ-дерева-неисправностей)  
[Анализ влияния](#анализ-влияния)  
[Жизненный цикл проблемы](#жизненный-цикл-проблемы)  
[Время проблемы](#время-проблемы)  
[Дублирующиеся проблемы](#дублирующиеся-проблемы)

## Инциденты и проблемы

**Инцидент** - это аномалия в вашей среде - в приложении, инфраструктуре и т. д. **Проблема** - это сущность, представляющая инцидент в Dynatrace. Проблема является результатом автоматического анализа коренной причины и влияния Dynatrace Intelligence инцидента. Проблемы (как и лежащие в их основе инциденты) могут охватывать несколько зависимых компонентов, имеющих одно и то же влияние и коренную причину.

Проблема может возникнуть из одного или нескольких событий Davis, происходящих одновременно в одной и той же топологии, что часто бывает в сложных средах. Чтобы предотвратить чрезмерное оповещение, Dynatrace коррелирует все события Davis с одной и той же коренной причиной в одну проблему.

Все обнаруженные проблемы перечислены в ленте проблем, и Dynatrace автоматически обновляет их в режиме реального времени со всеми входящими событиями Davis и результатами.

## События Davis

События представляют собой различные типы единичных аномалий, такие как превышение метрики порога, ухудшение базовой линии или события Davis в определенный момент времени, такие как крах процесса. Dynatrace также обнаруживает и обрабатывает информационные события Davis, такие как новые развертывания программного обеспечения, изменения конфигурации и другие типы событий Davis.

Dynatrace получает и хранит события Davis из нескольких источников. Эти события могут запустить анализ коренной причины, автоматизацию или служить сырыми данными для панелей мониторинга и отчетов. Вместе с журналами, метриками и трассами события Davis обеспечивают ввод для анализа коренной причины и влияния.

Большинство событий Davis не указывают на аномальные или нездоровые состояния, поэтому только небольшая часть событий Davis учитывается в проблемах.

## Анализ коренной причины

Анализ коренной причины использует всю доступную контекстную информацию - такую как топологическая, транзакционная и кодовая информация - для определения событий Davis, которые имеют одну и ту же коренную причину и влияние.

Для определения коренной причины проблем время корреляции alone не достаточно. Dynatrace следует контекстно-чувствительному подходу, обнаруживая взаимозависимые события Davis во времени, процессах, хостах, сервисах, приложениях и как вертикальных, так и горизонтальных перспективах мониторинга. Этот подход объединяет несколько отдельных аномалий в одну последовательную проблему, что значительно снижает нагрузку оповещений.

Изображение ниже иллюстрирует, как Dynatrace Intelligence анализирует все горизонтальные и вертикальные зависимости проблемы. В этом примере приложение демонстрирует аномальное поведение, в то время как лежащая в основе вертикальная стека работает нормально. Анализ следует транзакциям приложения, обнаруживая зависимость от сервиса (`Сервис 1`), который также демонстрирует аномальное поведение. В свою очередь, все зависимости сервиса ведут себя аномально и являются частью одной и той же проблемы.

![Диаграмма корреляции](https://dt-cdn.net/images/correlation-diagram-1256-6a1abf3bdb.png)

Dynatrace Intelligence включает все актуальные аномалии и ранжирует все вкладчики коренной причины, определяя, какая из них является основным негативным влиянием. Вы можете углубиться до уровня компонента и проанализировать коренную причину до уровня исходного кода. Например, Dynatrace может показать неудачные методы в вашем сервисном коде или высокую активность GC в лежащих в основе Java-процессах.

Почему контекстная корреляция важна?

Проблема редко является единичным событием Davis. Часто они появляются в регулярных узорах и являются симптомами более крупных проблем в вашей среде. Если несколько сущностей, зависящих от затронутого компонента, испытывают проблемы примерно в одно и то же время, все эти сущности включаются в анализ коренной причины.

Корреляция времени alone, однако, не достаточно, чтобы определить коренную причину многих проблем приложений и сервисов. Рассмотрим, например, простую корреляцию времени, в которой сервис `Бронирование` вызывает сервис `Верификация`, и сервис `Верификация` испытывает замедление. Первое событие Davis в эволюции проблемы - это замедление сервиса `Верификация`. Затем сервис `Бронирование` испытывает замедление, вызванное зависимостью от сервиса `Верификация`. В этом случае корреляция времени работает хорошо для обнаружения коренной причины проблемы: замедления сервиса `Верификация`. Однако это упрощенное описание того, что происходит в реальных приложениях.

Что, если события Davis в последовательности эволюции проблемы более тонкие и открыты для интерпретации? Что, если, например, сервис `Бронирование` имеет долгую историю проблем с производительностью? Без полного контекста становится невозможным решительно заключить, что замедление сервиса `Бронирование` вызвано замедлением сервиса `Верификация`. Существует возможность, что сервис `Бронирование` испытывает другую проблему с производительностью, не связанную с сервисом `Верификация`.

Анализ коренной причины Dynatrace Intelligence использует все связанные данные мониторинга для определения взаимозависимостей между проблемой и другими компонентами, которые произошли примерно в одно и то же время и в зависимости от топологии. То есть все топологические зависимости, вертикальные и горизонтальные, являются частью анализа.

## Анализ дерева неисправностей

Модель контекста Dynatrace Intelligence построена на основе известной информации о зависимостях из Smartscape, OneAgent и облачной интеграции. Dynatrace Intelligence использует эту информацию, чтобы быстро провести анализ дерева неисправностей для анализа миллионов зависимостей и определения наиболее вероятной коренной причины проблемы.

## Анализ влияния

Влияние проблемы столь же важно, как и его коренная причина, поскольку оба представляют собой важную информацию для классификации и исправления лежащего в основе инцидента - проблемы, которые угрожают вашему бизнесу, имеют более высокий приоритет для решения.

Анализ влияния определяет, какие сервисы входных точек приложений затронуты инцидентом, и размер общего "радиуса поражения" в терминах общего количества затронутых сущностей. Анализ влияния также обеспечивает количество затронутых SLO и количество потенциально затронутых реальных пользователей.

В конечном итоге анализ влияния стремится определить, насколько сильно инцидент влияет на ваш бизнес.

## Жизненный цикл проблемы

Dynatrace открывает проблему при получении первого индикатора инцидента, который обычно является единичным событием Davis, представляющим аномальное поведение, такое как замедление сервиса, насыщение узла или крах и перезапуск рабочей нагрузки.

Проблема автоматически проходит жизненный цикл и остается в активном состоянии, пока существует хотя бы одна затронутая сущность в нездоровом или аномальном состоянии, в основном указанном активным событием Davis.

В следующем сценарии проблема, которая имеет инцидент производительности на уровне инфраструктуры, является коренной причиной.

![Срок жизни проблемы](https://dt-cdn.net/images/problemlifespan-2275-dfec42340b.png)

1. Dynatrace обнаруживает инцидент производительности на уровне инфраструктуры и создает новую проблему для целей отслеживания. Также отправляется уведомление.
2. Через несколько минут проблема инфраструктуры приводит к появлению проблемы ухудшения производительности в одном из сервисов приложения.
3. Дополнительные проблемы ухудшения производительности на уровне сервиса начинают появляться. То, что началось как изолированная проблема только на уровне инфраструктуры, выросло в серию проблем на уровне сервиса, каждая из которых имеет свою коренную причину в исходном инциденте на уровне инфраструктуры.
4. В конечном итоге проблемы на уровне сервиса начинают влиять на опыт пользователя клиентов, которые взаимодействуют с приложением через настольные или мобильные браузеры. На этом этапе срока жизни проблемы у вас есть проблема приложения с одной коренной причиной на уровне инфраструктуры и дополнительными коренными причинами на уровне сервиса.
5. Поскольку Dynatrace понимает все зависимости в вашей среде, она коррелирует проблему ухудшения производительности, которую испытывают ваши клиенты, с исходной проблемой производительности на уровне инфраструктуры, что облегчает быстрое решение проблемы.

## Problem timing

The Dynatrace Intelligence root-cause engine collects all Davis events that belong to the same incident. As a result, Dynatrace Intelligence causal AI generates a problem that references all incident-relevant information such as individual Davis events that were detected on the impacted topology graph.

The following shows how two individual Davis events are analyzed within one problem generated by Dynatrace Intelligence causal AI.

* Each Davis event comes with its own start and end timestamps.
* Each Davis event producer uses various observation sliding time windows, which we call event analysis time (shown in yellow).

![Problem timing](https://dt-cdn.net/images/problem-lifecycle-drawio-2d5919c652.svg)

Consider an example of a metric Davis event configured to use a five-minute sliding window where three one-minute samples need to violate the threshold to raise a Davis event. In that case, the metric starts violating the threshold three minutes before the timestamp when the event is raised.

* The **event start analysis timestamp** is the earliest point in time when the violating state was observed.
* The **event end analysis timestamp** is the point in time after all necessary violation samples are collected and a problem is opened.
* Because each Davis event involved in the problem uses a sliding window, each problem has a trailing period during which a closed problem might be reopened. This is called the **reopening period**, and its maximum length is 30 minutes.
* If a problem remains open for longer than 90 minutes, no new events are merged into it after the 90-minute point. This prevents Dynatrace Intelligence causal AI from collecting unrelated information for long-lasting incidents (for example, a synthetic test constantly failing and keeping problems open for weeks).

#### Summary of the problem lifecycle timings:

* Individual Davis events use variable analysis sliding windows.
* A problem is raised at the **event end analysis timestamp**.
* A problem lifespan is defined by the lifespans of individual Davis events in the problem.
* A problem is closed when all Davis events in the problem are closed.
* A closed problem can be reopened during a reopening period of 30 minutes.
* If a problem lasts for longer than 90 minutes, no new Davis events will be merged after the 90-minute pointâa new problem will be raised instead.
* If the time gap between creation (start timestamp) of the first Davis events is longer than 5 minutes, the Davis events won't be merged into the same problem. Instead, they will be identified as two different problems.

## Duplicate problems

The detection and analysis of a large-scale incident always requires a balance between fast alerting and having a complete picture of the situation. Data collection is asynchronous by nature due to different observation windows, different synthetic check schedules, and different latencies of information originating from various data sources.

The asynchronous processing of incoming information leads to situations where root-cause detection identifies two problems that share the same root cause.

* At the time of detection, the root cause analysis might lack the necessary information to connect both problems into a single incident.
* After the delayed information is considered, and one main problem is identified, other identical problems are marked as duplicates (`dt.davis.is_duplicate=true`).

Duplicates could be avoided entirely by waiting for a longer period (for example, 30 minutes) to receive all possible information, but this would delay alerts to the operation teams.

Due to the criticality of real-time alerting, potentially incomplete information and problem duplicates are accepted to allow the fastest possible alerting.

## Problem processing state

After Dynatrace Intelligence causal AI detects a problem, it enters the `Processing` state. This means that the causal AI analyzes the Davis event to see if it needs to be merged into a more significant problem. The `Processing` state aims to avoid duplicate issues and false alarms, so no alerts are sent until the state changes. Analysis and information gathering necessary for causal AI to make a decision usually take up to 3 minutes.

Below, you can find the example of a problem in the `Processing` state.

![Detected Problem going through the "Processing" state](https://dt-cdn.net/images/problem-processing-state-934-2c9e3ab22e.png)

If you want to receive alerts immediately after the problem is detected, you can use Custom alert with [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace"). In this case, the Davis event flags `dt.davis.trigger_delay` and `dt.davis.analysis_time` will be set to `0`. The problem won't enter the `Processing` state, and no causal AI analysis will be performed.

Alternatively, you can set the processing state per Davis event source in [Log events](/docs/analyze-explore-automate/logs/lma-analysis "Explore log data with a log viewer or create custom attributes, log events, and metrics to process and analyze your log data in Dynatrace.") configuration.