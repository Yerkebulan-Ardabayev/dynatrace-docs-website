---
title: Обработка бизнес-событий
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing
scraped: 2026-03-06T21:34:23.823960
---

# Обработка бизнес-событий

# Обработка бизнес-событий

* Последняя версия Dynatrace
* Объяснение
* 4 минуты чтения
* Опубликовано 11 декабря 2025 г.

Бизнес-события, получаемые из различных источников, могут быть обработаны перед анализом.

Рекомендуется использовать OpenPipeline как масштабируемое и мощное решение для управления и обработки бизнес-событий. Если у вас нет доступа к OpenPipeline, воспользуйтесь классическим конвейером.

## OpenPipeline

OpenPipeline — это решение платформы Dynatrace для управления и обработки данных из различных источников. Оно обеспечивает беспрепятственную обработку данных любого масштаба и формата на платформе Dynatrace и предоставляет следующие преимущества:

* Контекстное преобразование данных: OpenPipeline извлекает данные с контекстом и преобразует их в более эффективные форматы.
* Единый язык обработки: [Dynatrace Query Language (DQL)](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.") используется как язык обработки, предоставляя единый синтаксис для всех функций Dynatrace и более широкие возможности обработки.
* Концепция конвейеров: можно разделить входящий трафик бизнес-событий на различные конвейеры с выделенной обработкой, извлечением данных и метрик, правами доступа и хранилищем.
* Дополнительные процессоры: можно использовать дополнительные процессоры, например для добавления или удаления полей.
* Расширенное извлечение данных: извлечение бизнес-событий из журналов с большим количеством вариантов извлечения данных.
* Улучшенная производительность и более высокая пропускная способность.

Чтобы начать работу, см. раздел [OpenPipeline](../../platform/openpipeline.md "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.").

## Классический конвейер

Обработка бизнес-событий через классический конвейер — это устаревшее решение для обработки бизнес-событий в Dynatrace.

Несмотря на то что классический конвейер обработки бизнес-событий по-прежнему доступен в некоторых средах, рекомендуется перейти на обработку бизнес-событий с помощью OpenPipeline. Обработка бизнес-событий через классический конвейер в какой-то момент будет упразднена.

Подробнее см. в разделе [Business event processing via classic pipeline](bo-event-processing/bo-processing-classic-pipeline.md "Process business event data in Dynatrace via the classic pipeline.").

### Классический конвейер и OpenPipeline

Если вы создали правила обработки через классический конвейер, рекомендуется вручную перенести их в OpenPipeline.

Чтобы перенести правила обработки бизнес-событий в OpenPipeline:

1. В OpenPipeline [создайте новые пользовательские конвейеры и маршруты](../../platform/openpipeline/getting-started/tutorial-configure-processing.md "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
2. В классическом конвейере удалите свои правила обработки.

Если вы не переносите существующие правила, по-прежнему можно использовать OpenPipeline совместно с классическим конвейером. Процесс обработки в этом случае выглядит следующим образом:

1. В OpenPipeline [создайте новые пользовательские конвейеры и маршруты](../../platform/openpipeline/getting-started/tutorial-configure-processing.md "Configure ingest sources, routes, and processing for your data in OpenPipeline.").
2. Данные обрабатываются [пользовательскими конвейерами](../../platform/openpipeline/concepts/processing.md#types "Learn the core concepts of Dynatrace OpenPipeline processing.").
3. Если данные не совпадают ни с одним маршрутом, они направляются по маршруту по умолчанию в [классический конвейер](../../platform/openpipeline/concepts/processing.md#types "Learn the core concepts of Dynatrace OpenPipeline processing.").
4. Бизнес-события обрабатываются в соответствии с правилами классического конвейера.

## Варианты использования

* Разбор данных в оптимальный формат для ваших задач.
* Извлечение метрик.
* Указание периодов хранения.
* Назначение контекста безопасности.

## Связанные темы

* [OpenPipeline processing examples](../../platform/openpipeline/use-cases/processing-examples.md "Explore scenarios of how to use OpenPipeline processing in Dynatrace powered by Grail.")
* [DQL matcher in OpenPipeline](../../platform/openpipeline/reference/dql-matcher-in-openpipeline.md "Examine specific DQL functions and logical operators for log processing.")
