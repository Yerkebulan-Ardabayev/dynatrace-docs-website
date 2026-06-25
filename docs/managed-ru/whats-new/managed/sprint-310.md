---
title: Заметки о выпуске Dynatrace Managed версии 1.310
source: https://docs.dynatrace.com/managed/whats-new/managed/sprint-310
scraped: 2026-05-12T11:07:50.714448
---

# Заметки о выпуске Dynatrace Managed версии 1.310

# Заметки о выпуске Dynatrace Managed версии 1.310

* Заметки о выпуске
* Updated on Apr 10, 2025

Начало развёртывания: Mar 18, 2025

На этой странице представлены новые функции, изменения и исправления ошибок в Dynatrace Managed версии 1.310.

## Несовместимые изменения

Несовместимое изменение · Infrastructure Observability | OS services monitoring

### Политика мониторинга служб ОС теперь требует правила обнаружения

Новые или изменённые политики мониторинга служб ОС требуют определения хотя бы одного правила обнаружения. Существующие политики будут применяться без изменений.

Кроме того, правила обнаружения теперь поддерживают оператор `$match()`.

Несовместимое изменение · Platform | Settings

### Изменения в журнале аудита настроек

Скорректирована генерация журнала аудита настроек для улучшения читаемости и снижения количества избыточных записей.

Изменения ранга объектов из-за их переупорядочивания в ранжированном списке теперь будут отражаться следующим образом:

* В API журнала аудита: `REORDER` (вместо `UPDATE`), если само значение не изменилось, или `UPDATE` (как прежде), если само значение изменилось.

## Новые функции и улучшения

Обновление функции · Infrastructure Observability | Application Observability | Vulnerability Analytics

### Наблюдаемость и защита стеков Python

Начиная с Dynatrace Managed версии 1.310+ и OneAgent версии 1.309+, можно отслеживать процессы Python, трассировать приложения и сервисы Python от начала до конца, а также анализировать среду выполнения Python и сторонние библиотеки на наличие уязвимостей.

Полный список поддерживаемых технологий Python см. в разделах [Поддержка технологий](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.") и [Кодовый модуль Python](/managed/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.").

#### Infrastructure Observability

Отслеживайте работоспособность и доступность процессов Python, выявляйте узкие места сборки мусора Python для всех поколений и неправильное поведение потоков. Доступны следующие метрики процессов Python:

* Python GC collections count (gen0, gen1, gen2)
* Python GC collected objects (gen0, gen1, gen2)
* Python GC uncollectable objects (gen0, gen1, gen2)
* Python GC time (gen0, gen1, gen2)
* Количество активных потоков Python
* Количество выделенных блоков памяти (heap)

Начало работы:

1. Перейдите в **Settings** > **Monitoring** > **Monitoring technologies**.
2. Найдите Python и включите **Monitor Python**.
3. [Создайте правило мониторинга процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring") для включения глубокого мониторинга выбранных процессов.

#### Application Observability

Автоматически обнаруживайте приложения Python на всех уровнях и диагностируйте аномалии с помощью Davis AI для определения первопричины вплоть до неисправного кода. Сквозная наблюдаемость сервисов в сочетании с аналитикой на уровне кода и анализом исключений поможет обеспечить надёжность производственной среды.

Полный список поддерживаемых технологий Python см. в разделе [Поддержка технологий](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Начало работы:

1. Убедитесь, что мониторинг Python включён (см. [Infrastructure Observability](#infrastructure-observability) выше).
2. Перейдите в **Settings** > **Preferences** > **OneAgent features**, найдите и включите все нужные сенсоры Python, затем перезапустите процессы.

#### Vulnerability Analytics

Автоматически обнаруживайте уязвимости среды выполнения Python и сторонних библиотек в приложениях Python, быстро оценивайте их влияние на отслеживаемую среду и расставляйте приоритеты для устранения.

Начало работы:

1. Убедитесь, что мониторинг Python включён (см. [Infrastructure Observability](#infrastructure-observability) выше).
2. Перейдите в **Settings** > **Preferences** > **OneAgent features**, найдите и включите отчётность о программных компонентах Python, затем перезапустите процессы.
3. Перейдите в **Settings** > **Application Security** > **Vulnerability Analytics** > **General settings** и включите Python.

Обновление функции · Platform | Davis

### Объединение проблем: теперь учитывается обобщённая связь `is same as`

Объединение проблем теперь учитывает обобщённую связь `is same as`, которую можно определить в модели топологии в настройках обобщённых связей.

Два события на разных сущностях будут объединены в одну проблему, если:

* Два события связаны через `is same as`
* Два события явно не отключают объединение
* Времена начала двух событий близки друг к другу

Обновление функции · Platform | Platform Services

### Лимит окружения для сетевых зон

Теперь по умолчанию установлен лимит окружения для сетевых зон: `10 000`.

Обновление функции · Infrastructure Observability

### Устойчивые обновления для Environment ActiveGates

Представлены улучшения механизма автоматического обновления ActiveGate. Новый процесс обновления обеспечивает поэтапное выполнение обновлений в рамках сетевых зон, групп ActiveGate и синтетических приватных локаций. Эти улучшения приносят следующие преимущества:

* **Минимизация простоев**: Поочерёдное обновление ActiveGate снижает риск прерывания сервиса.
* **Повышенная стабильность**: Поэтапные обновления гарантируют, что в любой момент времени обновляется только часть ActiveGate, обеспечивая общую стабильность системы.
* **Улучшенная надёжность**: Этот метод обеспечивает более качественный мониторинг и возможность быстрого прерывания в случае возникновения проблем в процессе обновления.

Эти изменения существенно повысят производительность и надёжность развёртываний ActiveGate.

## Dynatrace API

Сведения об изменениях в Dynatrace API в этом выпуске см. в:

* [Журнал изменений Dynatrace API версии 1.309](/managed/whats-new/dynatrace-api/sprint-309 "Changelog for Dynatrace API version 1.309")
* [Журнал изменений Dynatrace API версии 1.310](/managed/whats-new/dynatrace-api/sprint-310 "Changelog for Dynatrace API version 1.310")

## Поддержка операционных систем

### Предстоящие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы перестанут поддерживаться с 01 June 2026

* Linux: Oracle Linux 9.6

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.6

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы перестанут поддерживаться с 01 July 2026

* Linux: SUSE Enterprise Linux 15.3

  + x86-64
  + [Объявление поставщика](https://www.suse.com/lifecycle/)

##### Следующие операционные системы перестанут поддерживаться с 01 November 2026

* Linux: Red Hat Enterprise Linux 9.4, 9.7

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Ubuntu 16.04

  + x86-64
  + [Объявление поставщика](https://ubuntu.com/about/release-cycle)

##### Следующие операционные системы перестанут поддерживаться с 01 January 2027

* Linux: Amazon Linux 2

  + x86-64
  + [Объявление поставщика](https://aws.amazon.com/linux/)

### Прошедшие изменения поддержки операционных систем в Dynatrace Managed

##### Следующие операционные системы больше не поддерживаются с 01 December 2025

* Linux: Red Hat Enterprise Linux 8.8, 9.2, 9.5

  + x86-64
  + [Объявление поставщика](https://access.redhat.com/support/policy/updates/errata)
* Linux: Oracle Linux 9.5

  + x86-64
  + [Объявление поставщика](https://www.oracle.com/a/ocom/docs/elsp-lifetime-069338.pdf)
* Linux: Rocky Linux 9.5

  + x86-64
  + [Объявление поставщика](https://endoflife.date/rocky-linux)

##### Следующие операционные системы больше не поддерживаются с 01 January 2026

* Linux: Debian 10

  + x86-64
  + [Объявление поставщика](https://wiki.debian.org/DebianReleases)

## Исправленные ошибки