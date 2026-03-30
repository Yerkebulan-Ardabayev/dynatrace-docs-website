---
title: Контекст выполнения Guardian
source: https://www.dynatrace.com/docs/deliver/site-reliability-guardian/execution-context
scraped: 2026-03-06T21:37:23.233559
---

Ваш инструмент непрерывной интеграции (CI), например Jenkins, может отправлять бизнес-события в Dynatrace. Эти события затем могут инициировать проверки Site Reliability Guardian в рамках рабочего процесса.

Disclaimer

Описанные ниже шаги используют бизнес-события для интеграции в конвейер CI/CD и получения результатов проверки. Этот подход актуален сейчас, однако в будущем мы планируем ввести новый тип событий для событий, возникающих в процессе жизненного цикла разработки программного компонента. Этот новый тип событий заменит бизнес-события в будущем.

Если вы хотите фильтровать события проверки Site Reliability Guardian по источнику триггера, созданные бизнес-события должны содержать контекстную информацию из внешнего инструмента. Контекстная информация может передаваться через externalId, номер версии, номер сборки или любой параметр, позволяющий идентифицировать инструмент.

## Распространение контекста

Для распространения контекста выполнения событие, инициирующее выполнение рабочего процесса, должно содержать поле `execution_context`, как в примере ниже.

```
{


"timeframe.to": "2023-03-08T06:29:08.809Z",


"timeframe.from": "2023-03-08T05:29:08.809Z",


"errors": "[]",


"status": "fail",


"event.id": "d08a70d8-f6de-4d0d-bd34-5d416a20ba6a",


"timestamp": 1678256963078000000,


"event.kind": "BIZ_EVENT",


"event.type": "guardian.validation.triggered",


"tag.stage": "hardening",


"tag.service": "carts",


"event.provider": "Jenkins",


"dt.system.bucket": "default_bizevents_short"


"execution_context": {


"buildId": "4711",


"version": "0.1.0"


}


}
```

Контекст выполнения передаётся в бизнес-событие проверки Guardian. События `guardian.validation.started`, `guardian.validation.finished` и `guardian.validation.objective` содержат переданное поле `execution_context`.

## Запрос данных Guardian с использованием контекста выполнения

Следующий DQL-запрос показывает первое бизнес-событие `guardian.validation.objective` с конкретным идентификатором Guardian и разбирает поле контекста выполнения для извлечения конкретного значения из JSON события.

```
fetch bizevents |


filter event.type == "guardian.validation.objective" AND guardian.id == "vu9U3hXa3q0AAAABADFhcHA6ZHluYXRyYWNlLnNpdGUucmVsaWFiaWxpdHkuZ3VhcmRpYW46Z3VhcmRpYW5zAAZ0ZW5hbnQABnRlbmFudAAkMWNiZDVkYWYtZThhNi0zMDkxLWFkOGQtMmU5NDNmNWJmZWJmvu9U3hXa3q0" |


limit 1 |


parse execution_context, "JSON:parsed_execution_context"
```

Следующий DQL-запрос показывает все бизнес-события `guardian.validation.finished`, в которых контекст выполнения определён значением `buildid`, равным `4711`.

```
fetch bizevents


| filter event.type == "guardian.validation.finished"


| parse execution_context, "JSON:parsed_execution_context"


| filter parsed_execution_context[buildId] == "4711"
```
