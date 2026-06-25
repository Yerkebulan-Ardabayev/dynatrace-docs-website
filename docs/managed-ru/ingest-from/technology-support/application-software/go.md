---
title: Go
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/go
scraped: 2026-05-12T11:22:48.584864
---

# Go

# Go

* Справочник
* Чтение: 1 мин
* Опубликовано: 19 марта 2018

Go является языком программирования, созданным Робертом Гризмером, Робом Пайком и Кеном Томпсоном. Для многих организаций Go стал предпочтительным cloud-native языком программирования.

Dynatrace предоставляет широкие возможности мониторинга Go:

* Автоматическая инъекция и инструментирование 64-битных исполняемых файлов Go на x86
* OneAgent версии 1.323+: автоматическая инъекция и инструментирование исполняемых файлов Go на AArch64
* [Постоянное круглосуточное профилирование CPU производственного уровня](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/full-code-level-visibility "Узнайте, как Dynatrace обеспечивает полную видимость на уровне кода для производительности ваших Golang-приложений без каких-либо изменений в коде или приложении.")
* [Метрики, специфичные для Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/analyze-go-metrics "Узнайте о различных метриках Go и о том, как анализировать их с помощью Dynatrace."):

  + Приостановка
  + Размеры выделенной, используемой, простаивающей и «живой» памяти кучи
  + Прикладные и системные горутины
  + Кучи управляемой памяти Go: Offheap, Stack и общий объём выделенной или используемой памяти
  + Выделенные объекты Go
  + Количество вызовов сборщика мусора
  + Системные вызовы среды выполнения Go
  + Вызовы из Go в язык C (cgo)
  + Размер глобальной очереди выполнения горутин
  + Припаркованные, оставшиеся без работы и общее число рабочих потоков
  + Количество простаивающих контекстов планирования
* [Мониторинг входящих и исходящих веб-запросов](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring "Узнайте, как Dynatrace обеспечивает видимость на уровне запросов для ваших Go-приложений.")
* [Мониторинг пользовательских сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Определите точки входа (метод, класс или интерфейс) для пользовательских сервисов, не использующих стандартные протоколы.")
* Трассировка сервисов [`database/sql`](https://dt-url.net/database-sql)  
  Список поддерживаемых драйверов см. в разделе [Поддержка технологии Go](/managed/ingest-from/technology-support#go "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.")
* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-go/) для захвата traces.  
  Подробнее см. [Инструментирование Go-приложения с OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/go "Узнайте, как инструментировать Go-приложение с помощью OpenTelemetry и Dynatrace.")

### Поддержка

* [Поддерживаемые версии Go](/managed/ingest-from/technology-support/application-software/go/support/supported-go-versions "Узнайте, какие версии Go поддерживаются Dynatrace.")
* [Известные ограничения поддержки Go](/managed/ingest-from/technology-support/application-software/go/support/go-known-limitations "Узнайте об ограничениях поддержки Go и способах их обхода.")

### Настройка и анализ

* [Включение мониторинга Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring "Узнайте, как включить мониторинг Go в Dynatrace.")
* [Анализ метрик Go](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/analyze-go-metrics "Узнайте о различных метриках Go и о том, как анализировать их с помощью Dynatrace.")
* [Сквозной мониторинг запросов](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring "Узнайте, как Dynatrace обеспечивает видимость на уровне запросов для ваших Go-приложений.")
* [Полная видимость на уровне кода](/managed/ingest-from/technology-support/application-software/go/configuration-and-analysis/full-code-level-visibility "Узнайте, как Dynatrace обеспечивает полную видимость на уровне кода для производительности ваших Golang-приложений без каких-либо изменений в коде или приложении.")

### См. также

[Блог: Представляем полностью автоматизированную поддержку мониторинга Go-приложений](https://www.dynatrace.com/news/blog/introducing-fully-automated-support-for-go-based-application-monitoring/)

[Блог: Сквозной мониторинг запросов для Go-приложений: без изменений в коде](https://www.dynatrace.com/news/blog/end-to-end-request-monitoring-for-go-applications-no-code-changes-required/)

[Блог: Полная видимость на уровне кода теперь доступна для мониторинга Go-приложений](https://www.dynatrace.com/news/blog/full-code-level-visibility-now-available-for-go-application-monitoring/)

[Блог: Представляем пользовательские сервисы для Go-приложений](https://www.dynatrace.com/news/blog/introducing-custom-services-for-go-applications/)

[Блог: Получайте автоматические инсайты на уровне кода для ваших Go-приложений и компонентов облачной платформы](https://www.dynatrace.com/news/blog/automatic-code-level-insights-into-go-applications-without-code-changes/)

[Блог: Первая и единственная в мире полностью автоматическая наблюдаемость для Golang-сервисов теперь распространяется на статически слинкованные Go-приложения](https://www.dynatrace.com/news/blog/worlds-first-and-only-fully-automatic-observability-for-golang-services-now-extended-to-statically-linked-go-applications/)