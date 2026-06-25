---
title: Учебное руководство WMI: метаданные метрик
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-03
scraped: 2026-05-12T12:16:27.449098
---

# WMI tutorial - метаданные метрик

# WMI tutorial - метаданные метрик

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 30 марта 2022 г.

Если в расширении определён только источник данных, сбор метрик минимален: все метрики идентифицируются только по ключу и отображаются без единиц измерения, что затрудняет их восприятие.

Раздел `metrics` расширения служит для определения дополнительных метаданных метрик. Доступны следующие поля:

* `displayName`: понятное имя метрики
* `description`: описание того, что измеряет данная метрика
* `unit`: единица измерения метрики
* `tags`: теги для быстрого поиска метрики в каталоге метрик
* `metricProperties`

  + `minValue`: минимально возможное значение метрики
  + `maxValue`: максимально возможное значение метрики
  + `impactRelevant`: указывает, зависит ли данная метрика от аномалий других метрик для формирования первопричины проблемы
  + `rootCauseRelevant`: указывает, может ли данная метрика самостоятельно быть первопричиной проблемы
  + `valueType`: определяет, являются ли высокие значения положительными (`score`) или отрицательными (`error`)

## Определение метаданных

1. Добавьте раздел `metrics` в файл `extension.yaml` по приведённому шаблону.
2. Определите метаданные для каждой собираемой метрики.
3. Укажите как минимум `displayName`, `description` и `unit`.
4. Соберите и загрузите новую версию пакета расширения.
5. Проверьте метаданные.

```
metrics:



- key: custom.demo.host-observability.network.bytes.persec



metadata:



displayName: Traffic bytes/s



description: Network traffic bytes per second



unit: BytePerSecond



#



# add content here, for all other metrics



#
```

Дополнительные сведения о синтаксисе источника данных WMI см. в разделе [Справочник по источнику данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-schema-reference "Узнайте о расширениях WMI в платформе Extensions framework.").

## Результаты

Метаданные должны отобразиться в [браузере метрик](/managed/analyze-explore-automate/dashboards-classic/metrics-browser "Просматривайте метрики в браузере метрик Dynatrace."):

![result](https://dt-cdn.net/images/wmi-tutorial-metadata-1280-c5b9547495.png)

result

**Следующий шаг**: [Пользовательская топология](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Узнайте о расширениях WMI в платформе Extensions framework.")