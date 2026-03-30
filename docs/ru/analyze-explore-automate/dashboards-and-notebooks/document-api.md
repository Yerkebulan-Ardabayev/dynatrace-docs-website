---
title: API для панелей мониторинга и ноутбуков
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/document-api
scraped: 2026-03-06T21:31:09.703615
---

# API для панелей управления и ноутбуков

Для управления документами (дашбордами и ноутбуками) через API используется [сервис документов](https://dt-url.net/x403ua9) платформы Dynatrace.

## Доступ к данным документов

Приложения **Dashboards** и **Notebooks** сохраняют данные через API сервиса документов. Документы имеют общие метаданные: уникальный ID, имя и описание. Атрибут `type` (`dashboard` или `notebook`) определяет тип документа.

#### Список всех панелей управления

```
https://environment/platform/document/v1/documents?filter=type='dashboard'
```

#### Список всех ноутбуков

```
https://environment/platform/document/v1/documents?filter=type='notebook'
```

## Полная документация API

1. Перейдите на страницу [Сервис документов](https://dt-url.net/x403ua9) на [Dynatrace Developer](https://developer.dynatrace.com/).
2. В разделе **Связанные ссылки** выберите **Swagger API**.
