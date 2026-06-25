---
title: Интеграция Dynatrace и LoadRunner
source: https://docs.dynatrace.com/managed/deliver/test-automation/dynatrace-and-loadrunner-integration
scraped: 2026-05-12T11:38:36.149838
---

# Dynatrace and LoadRunner integration

# Dynatrace and LoadRunner integration

* Published Apr 12, 2018

[Инструмент LoadRunner Request Tagging для Dynatrace](https://github.com/Dynatrace/Dynatrace-LoadRunner-Request-Tagging) — это инструмент командной строки, автоматически добавляющий соответствующие HTTP-заголовки к запросам, генерируемым Virtual User Generator LoadRunner (проекты типа **Web - HTTP/HTML**). Подробнее об интеграции нагрузочного тестирования с Dynatrace см. в разделе [Интеграция Dynatrace с инструментами нагрузочного тестирования](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.").

![Load Runner integration](https://dt-cdn.net/images/dynatrace-loadrunner-01-1252-0fb9038332.png)

Интеграция с LoadRunner

Инструмент LoadRunner Request Tagging вставляет короткий метод `addDynatraceHeaderTest` в ваш файл `globals.h` или `globals.js`, который заполняет заголовок `x-dynatrace-test`. Также он анализирует ваши файлы `.c` или `.js` и автоматически добавляет вызов этого метода перед одним из ключевых методов `LoadRunner`. Поддерживаются языки сценариев C и JavaScript.

Ключевые методы LoadRunner

Метод `addDynatraceHeaderTest` вызывается перед следующими методами: `web_url`, `web_link`, `web_image`, `web_submit_form`, `web_submit_data`, `web_custom_request`, `web_browser`, `web_button`, `web_check_box`, `web_edit_field`, `web_elementweb_file`, `web_image_link`, `web_image_submit`, `web_list`, `web_map_area`, `web_radio_group`, `web_reg_dialog`, `web_static_image`, `web_table`, `web_text_area` и `web_text_link`.

## Изменение скриптов LoadRunner для Dynatrace

1. Запишите скрипт Virtual User Generator (VUGEN) LoadRunner и адаптируйте его по мере необходимости. Подробности см. в документации LoadRunner.
2. Загрузите последний релиз [инструмента LoadRunner Request Tagging для Dynatrace](https://github.com/Dynatrace/Dynatrace-LoadRunner-Request-Tagging/releases).
3. Примените изменения к скриптам LoadRunner или откатите их.

Инструмент LoadRunner Request Tagging использует следующий синтаксис:

```
java -jar Dt-LoadRunner-request-tagging.jar <mode> <path parameter> <optional parameters>
```

Параметры

|  |  |
| --- | --- |
| **mode** | * `insert`: добавляет HTTP-заголовок Dynatrace к выбранным скриптам LoadRunner. * `delete`: удаляет все изменения, ранее внесённые инструментом LoadRunner Request Tagging. |
| **path parameter** | Выберите `-path` либо `-body` и `-header`  * `-path <filepath>`: используется для сканирования всех директорий и поддиректорий на наличие файлов скриптов и вставки/удаления скриптов в них. * `-body <files> -header <files>`: используется для указания, какие файлы заголовков или тела следует обрабатывать. Разделитель между файлами — `&`. |
| **optional parameters** | * `-LSN <value>`: задаёт имя скрипта нагрузки в значение, переданное после `-LSN`. Если пропущено, имя скрипта берётся из файла `*.usr`. * `-c`: задаёт C в качестве языка сценариев (по умолчанию). * `-js`: задаёт JavaScript в качестве языка сценариев. * `-help`: выводит справку об использовании. |

Примеры

#### Вставка HTTP-заголовков в директорию скриптов C

```
java -jar Dt-LoadRunner-request-tagging.jar insert -path C:\LoadRunnerScripts\EasyTravelBookingProcess
```

#### Удаление HTTP-заголовков из директории скриптов C

```
java -jar Dt-LoadRunner-request-tagging.jar delete -path C:\LoadRunnerScripts\EasyTravelBookingProcess
```

#### Вставка HTTP-заголовков по именам файлов с `&` в качестве разделителя

```
java -jar Dt-LoadRunner-request-tagging.jar insert -header C:\LoadRunnerScripts\EasyTravelBookingProcess\globals.h



-body C:\LoadRunnerScripts\EasyTravelBookingProcess\action.c&C:\LoadRunnerScripts\EasyTravelBookingProcess\action2.c&C:\LoadRunnerScripts\EasyTravelBookingProcess\action3.c
```

#### Вставка HTTP-заголовков с именем скрипта

```
java -jar Dt-LoadRunner-request-tagging.jar insert -LSN "EasyTravelBookingProcessVersion2" -path C:\LoadRunnerScripts\EasyTravelBookingProcess
```

#### Вставка HTTP-заголовков в директорию JavaScript

```
java -jar Dt-LoadRunner-request-tagging.jar insert -js -path C:\LoadRunnerScripts\EasyTravelBookingProcess
```

4. Убедитесь, что метод `addDynatraceHeaderTest` добавлен в ваш скрипт.

![LoadRunner integration](https://dt-cdn.net/images/dynatrace-loadrunner-02-2551-d4ebe82d10.png)

Интеграция с LoadRunner

## Настройка атрибутов запроса

Заголовок `x-dynatrace-test` заполняется инструментом LoadRunner Request Tagging парами ключ/значение, перечисленными ниже. Эти значения может захватывать Dynatrace путём определения [атрибутов запроса](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data."). Не обязательно настраивать все пары ключ/значение; настраивайте только те, что нужны для целевого анализа нагрузочных тестов.

Пары ключ/значение заголовка x-dynatrace-test

| Ключ | Описание | Значение |
| --- | --- | --- |
| TSN | **T**est **S**tep **N**ame — логический шаг теста в скрипте нагрузочного тестирования. | Имя транзакции, определённой в скрипте LoadRunner. При вложенных транзакциях имена транзакций конкатенируются. |
| LSN | **L**oad **S**cript **N**ame — имя скрипта нагрузочного тестирования. | Имя файла `*.usr` или значение необязательного параметра `-LSN`. |
| LTN | **L**oad **T**est **N**ame — уникально идентифицирует выполнение теста. | Значение атрибута времени выполнения `DynatraceLTN`, настроенного в LoadRunner. |
| VU | **V**irtual **U**ser ID — ID виртуального пользователя, отправившего запрос. | Пример: 1, 2, 3, … |
| PC | **P**age **C**ontext — предоставляет информацию о документе, загруженном на текущей обрабатываемой странице. | Содержит значение первого параметра, переданного следующим функциям: `web_url`, `web_link`, `web_image`, `web_submit_form`, `web_submit_data`, `web_custom_request`. |
| SI | **S**ource **I**D — идентифицирует продукт, инициировавший запрос. | `LoadRunner` (фиксированное значение). |

Пример настройки атрибута запроса для имени шага теста (`TSN`):

1. В Dynatrace настройте [правила извлечения](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-web-request-data "Create request attributes based on web request data.") для пользовательских HTTP-заголовков через **Settings** > **Server-side service monitoring** > **Request attributes**.
2. Выберите **HTTP request header** в качестве **Request attribute source** и введите имя вашего пользовательского HTTP-заголовка в поле **Parameter name**. Извлечение имени шага теста `TSN` из `x-dynatrace-test` можно настроить, как показано ниже.

![Request attributes](https://dt-cdn.net/images/jmeter-definerequestattribute-1095-ce93ef5c26.png)

Атрибуты запроса

3. Запустите нагрузочный тест из LoadRunner. Запросы и распределённые трассировки будут тегированы в Dynatrace настроенными атрибутами запросов для целевой диагностики и анализа.

![LoadRunner](https://dt-cdn.net/images/dynatrace-loadrunner-03-1590-82acca3f88.png)

LoadRunner

Существует несколько способов анализа данных. Подход должен быть основан на типе анализа производительности (например, сбои, узкие места по ресурсам и производительности или проблемы масштабируемости). Атрибуты запроса, настроенные для нагрузочного теста, помогут фильтровать данные. В данном примере они используются для анализа времени ответа шага теста поиска рейса в Париж:

![LoadRunner](https://dt-cdn.net/images/dynatrace-loadrunner-04-1611-28ebf55fe0.png)

LoadRunner

## Дополнительное чтение

* [Как интегрировать Dynatrace в процесс нагрузочного тестирования?](/managed/deliver/test-automation "Learn how you can integrate Dynatrace into your load testing process.")
* [Blog: Load testing redefined: From KPI reporting to AI-supported performance engineering](https://www.dynatrace.com/news/blog/load-testing-redefined-a-guide-from-kpi-reporting-to-ai-supported-performance-engineering/)