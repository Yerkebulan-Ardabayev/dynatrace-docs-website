---
title: Get offline bundle
source: https://docs.dynatrace.com/managed/dynatrace-api/mission-control-api/offline-bundle-packages/get-offline-package-update-bundle
scraped: 2026-05-12T12:14:11.605256
---

# Get offline bundle

# Get offline bundle

* Published Apr 02, 2020

Этот API-вызов возвращает конкретный deployment package и обновление как Offline Bundle.

## Endpoint

`/public/downloads/offline-bundle/published`

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Список Offline Bundles успешно сгенерирован |
| **401** | Невалидные учётные данные |
| **404** | Кластер не найден |

## Пример

В этом примере скачивается offline update bundle для релиза OneAgent 1.214.0.20210305-194131.

#### URL запроса

```
https://mcsvc.dynatrace.com/rest/public/downloads/offline-bundle?bundle=agent:1.214.0.20210305-194131&token=aaA0aAAaAaAAA0AaAAAaaAaaAaAAAaA0AaA0.eyJzdWIiOiJjbHVzdGVyLTBhMDBhMGEwLTkyZWMtMTFlNy1iMWU2LTEyZmJkMWZiMzczMkBkeW5hdHJhY2UtbWFuYWdlZC5jb20iLCJhdWQiOiJkdDBzMDQuTFFWT1FQQVMiLCJ1aWQiOiI5N2Y0OGFhMy1jYmRiLTRkMzEtOGE2YS02NjUyNTQxMzY5MTIiLCJzY29wZSI6InNzbzIwLW1hbmFnZWQtY2x1c3Rlci1vZmZsaW5lLWJ1bmRsZSIsImlzcyI6Imh0dHBzOi8vc3NvLXNwcmludC5keW5hdHJhY2VsYWJzLmNvbTo0NDMiLCJleHAiOjE2MTU0NzcxNTIsImdyYW50VHlwZSI6ImNsaWVudF9jcmVkZW50aWFscyIsImlhdCI6MTYxNTQ2OTk1Mn0.svn34bJEZbziHVyV7cKW9OWwvBwakzH0Ke_Iu19GV743zrC4zHuX4YQFts-JkEHRYmnVvnQRwPPCakuq0LHVjA
```

#### Тело ответа

ZIP-файл с обновлением для OneAgent 1.214.0.20210305-194131