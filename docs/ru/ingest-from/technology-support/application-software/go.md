---
title: Go
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go
scraped: 2026-03-05T21:25:20.925617
---

# Go

# Go

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 19, 2018

Go — это язык программирования, созданный Робертом Гризмером, Робом Пайком и Кеном Томпсоном. Go является предпочтительным языком программирования для облачных приложений во многих организациях.

Dynatrace предоставляет широкие возможности мониторинга Go:

* Автоматическое внедрение и инструментирование 64-разрядных исполняемых файлов Go на x86
* OneAgent версии 1.323+ Автоматическое внедрение и инструментирование исполняемых файлов Go на AArch64
* [Постоянное круглосуточное профилирование CPU производственного уровня](go/configuration-and-analysis/full-code-level-visibility.md "Узнайте, как Dynatrace обеспечивает полную видимость на уровне кода для производительности ваших приложений на основе Golang без изменений кода или приложения.")
* [Метрики, специфичные для Go](go/configuration-and-analysis/analyze-go-metrics.md "Узнайте о различных метриках Go и о том, как их анализировать с помощью Dynatrace."):

  + Приостановка
  + Зафиксированный, используемый, простаивающий и живой размеры кучи в памяти
  + Горутины приложения и системы
  + Управляемые Go кучи памяти: Offheap, Stack и общая зафиксированная или используемая память
  + Выделенные объекты Go
  + Количество вызовов сборщика мусора
  + Системные вызовы среды выполнения Go
  + Вызовы из Go в язык C (cgo)
  + Размер глобальной очереди выполнения горутин
  + Припаркованные, незагруженные и общее число рабочих потоков
  + Количество неактивных контекстов планирования
* [Мониторинг входящих и исходящих веб-запросов](go/configuration-and-analysis/end-to-end-request-monitoring.md "Узнайте, как Dynatrace обеспечивает видимость на уровне запросов для ваших приложений на основе Go.")
* [Сквозная трассировка служб gRPC](../../../whats-new/oneagent/sprint-175.md#go "Примечания к выпуску Dynatrace OneAgent версии 1.175")
* [Мониторинг пользовательских служб](../../../observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services.md "Определите точки входа (метод, класс или интерфейс) для пользовательских служб, не использующих стандартные протоколы.")
* Трассировка служб [`database/sql`](https://dt-url.net/database-sql)
  Список поддерживаемых драйверов см. в разделе [Поддержка технологии Go](../../technology-support.md#go "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.")
* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-go/) для захвата трассировок.
  Дополнительные сведения см. в разделе [Инструментирование приложения Go с помощью OpenTelemetry](../../opentelemetry/walkthroughs/go.md "Узнайте, как инструментировать ваше приложение Go с помощью OpenTelemetry и Dynatrace.")

### Поддержка

* [Поддерживаемые версии Go](go/support/supported-go-versions.md "Узнайте, какие версии Go поддерживаются Dynatrace.")
* [Известные ограничения для поддержки Go](go/support/go-known-limitations.md "Ознакомьтесь с ограничениями для поддержки Go и способами их обхода.")

### Настройка и анализ

* [Включение мониторинга Go](go/configuration-and-analysis/enable-go-monitoring.md "Узнайте, как можно включить мониторинг Go в Dynatrace.")
* [Анализ метрик Go](go/configuration-and-analysis/analyze-go-metrics.md "Узнайте о различных метриках Go и о том, как их анализировать с помощью Dynatrace.")
* [Сквозной мониторинг запросов](go/configuration-and-analysis/end-to-end-request-monitoring.md "Узнайте, как Dynatrace обеспечивает видимость на уровне запросов для ваших приложений на основе Go.")
* [Полная видимость на уровне кода](go/configuration-and-analysis/full-code-level-visibility.md "Узнайте, как Dynatrace обеспечивает полную видимость на уровне кода для производительности ваших приложений на основе Golang без изменений кода или приложения.")

### Смотрите также

[Блог: Представляем полностью автоматизированную поддержку мониторинга приложений на основе Go](https://www.dynatrace.com/news/blog/introducing-fully-automated-support-for-go-based-application-monitoring/)

[Блог: Сквозной мониторинг запросов для приложений Go: изменения кода не требуются](https://www.dynatrace.com/news/blog/end-to-end-request-monitoring-for-go-applications-no-code-changes-required/)

[Блог: Полная видимость на уровне кода теперь доступна для мониторинга приложений Go](https://www.dynatrace.com/news/blog/full-code-level-visibility-now-available-for-go-application-monitoring/)

[Блог: Представляем пользовательские службы для приложений Go](https://www.dynatrace.com/news/blog/introducing-custom-services-for-go-applications/)

[Блог: Получайте автоматические аналитические данные на уровне кода для ваших приложений Go и компонентов облачной платформы](https://www.dynatrace.com/news/blog/automatic-code-level-insights-into-go-applications-without-code-changes/)

[Блог: Первая и единственная в мире полностью автоматическая наблюдаемость для служб Golang теперь распространяется на статически скомпонованные приложения Go](https://www.dynatrace.com/news/blog/worlds-first-and-only-fully-automatic-observability-for-golang-services-now-extended-to-statically-linked-go-applications/)
