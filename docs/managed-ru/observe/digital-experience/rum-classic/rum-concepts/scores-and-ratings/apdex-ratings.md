---
title: Оценки Apdex в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings
---

# Оценки Apdex в RUM Classic

# Оценки Apdex в RUM Classic

* Объяснение
* Чтение 3 мин
* Обновлено 27 января 2023 г.

Dynatrace рассчитывает [оценки Apdex﻿](https://en.wikipedia.org/wiki/Apdex), чтобы дать единую метрику, которая показывает производительность приложения и влияние ошибок на пользовательский опыт.

Apdex рассчитывается для каждого отдельного [действия пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Узнайте, что такое действия пользователя и как они помогают понять, что пользователи делают с приложением.") и для приложения в целом. Таким образом он даёт быстрое представление о пользовательском опыте в приложении.

Оценки Apdex по умолчанию в Dynatrace основаны на пороговых значениях, специфичных для приложения.

| Оценка | Уровень производительности |
| --- | --- |
| 0,94–1,0 | Отлично |
| 0,85–0,94 | Хорошо |
| 0,7–0,85 | Удовлетворительно |
| 0,5–0,7 | Плохо |
| < 0,5 | Неприемлемо |

Оценки Apdex можно использовать как ориентир для сравнения двух приложений во времени, даже если пороговые значения времени для этих приложений различаются.

Приложения обычно состоят из множества разных типов действий пользователя. Например, может быть приемлемо, чтобы сложный поиск занимал до 6 секунд, тогда как загрузка домашней страницы в этом же приложении должна занимать менее 2 секунд, чтобы обеспечить удовлетворённость пользователя. Такие различия можно учесть, настроив разные пороги Apdex для разных типов действий пользователя.

Подробнее о стандарте Apdex см. в [Apdex References﻿](https://www.apdex.org/index.php/documents/).

## Настройка параметров Apdex в Dynatrace

Оценки Apdex в Dynatrace можно настроить в соответствии с конкретными требованиями приложения. После настройки они дают быстрый и простой способ оценки производительности всех отслеживаемых действий пользователя: значение `1.0`, это идеально; значения ниже `0.5` неприемлемы. Рекомендуется определить подходящие пороги времени удовлетворённости пользователя и настройки влияния ошибок для каждого отслеживаемого действия пользователя.

Параметры Apdex можно настроить для приложения и для его ключевых действий пользователя.

### Настройка параметров Apdex для приложений

Пороги Apdex можно изменить для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-apdex-web "Настройте пороги производительности удовлетворённости пользователя для веб-приложения и его ключевых действий пользователя."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-apdex-mobile "Настройте пороги производительности удовлетворённости пользователя для мобильного приложения и его ключевых действий пользователя.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороги производительности удовлетворённости пользователя для пользовательского приложения и его ключевых действий пользователя.").

### Настройка параметров Apdex для ключевых действий пользователя

Также можно изменить пороги Apdex для конкретного ключевого действия пользователя для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-key-user-actions-web "Пометьте действие пользователя как ключевое и настройте оценку Apdex для ключевых действий пользователя ваших веб-приложений."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-key-user-actions-mobile "Пометьте действие пользователя как ключевое и настройте оценку Apdex для ключевых действий пользователя ваших мобильных приложений.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-key-user-actions-custom "Пометьте действие пользователя как ключевое и настройте оценку Apdex для ключевых действий пользователя ваших пользовательских приложений.").

## Влияние ошибок на Apdex

Действия пользователя с JavaScript [ошибками](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Узнайте о событиях пользователя и ошибок и о типах событий пользователя и ошибок, которые фиксирует Dynatrace.") получают оценку **Frustrated**. Иногда действия пользователя, которые на самом деле быстрые и укладываются в порог Apdex, отображаются красным и получают оценку **Frustrated**, потому что у некоторых действий пользователя есть JavaScript-ошибки.

То же самое верно для ошибок запросов. Код ответа HTTP, нарушение CSP или запрос ресурса, настроенные в параметрах как фиксируемые в качестве ошибки, приводят к оценке действия пользователя как **Frustrated**.

Ошибки можно исключить из расчёта Apdex. Подробнее см. в [Настройка обнаружения ошибок для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Настройте приложение на фиксацию или игнорирование ошибок запросов, пользовательских и JavaScript-ошибок."), [Настройка параметров Apdex для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-apdex-mobile "Настройте пороги производительности удовлетворённости пользователя для мобильного приложения и его ключевых действий пользователя.") и [Настройка параметров Apdex для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороги производительности удовлетворённости пользователя для пользовательского приложения и его ключевых действий пользователя.").

Пример: правила ошибок

![Application rules for errors](https://dt-cdn.net/images/web-app-settings-for-error-rules-1200-9e80202ff2.png)

Правила приложения для ошибок

## Анализ на основе Apdex

Dynatrace упрощает анализ Apdex приложения по разным измерениям. Можно проверить оценку Apdex для конкретного действия пользователя, местоположения и приложения, а также посмотреть оценку Apdex для каждого действия пользователя в рамках одной пользовательской сессии.

Подробнее см. в [Контекстный анализ Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/apdex-analysis "Проверьте оценку Apdex для действия пользователя, местоположения и приложения.").

## Похожие темы

* [Настройка параметров Apdex для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-apdex-web "Настройте пороги производительности удовлетворённости пользователя для веб-приложения и его ключевых действий пользователя.")
* [Настройка параметров Apdex для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-apdex-mobile "Настройте пороги производительности удовлетворённости пользователя для мобильного приложения и его ключевых действий пользователя.")
* [Настройка параметров Apdex для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороги производительности удовлетворённости пользователя для пользовательского приложения и его ключевых действий пользователя.")
* [Контекстный анализ Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/session-segmentation/apdex-analysis "Проверьте оценку Apdex для действия пользователя, местоположения и приложения.")