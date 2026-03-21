---
title: Анализ журналов доступа Amazon API Gateway с помощью Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator
scraped: 2026-03-06T21:29:02.173566
---

# Анализ логов доступа Amazon API Gateway с помощью Investigations


* Latest Dynatrace

[Amazon API Gateway](https://dt-url.net/dm03wn5) — это мощный сервис, позволяющий создавать бессерверные веб-API с использованием функций Lambda или добавлять дополнительный уровень безопасности для существующих сервисов. Возможности варьируются от простых действий, таких как [применение TLS-шифрования](https://dt-url.net/q823w6q) или [кэширования](https://dt-url.net/bj43w6c), до более сложных мер, таких как [контроль доступа](https://dt-url.net/iq63wsn), [троттлинг API](https://dt-url.net/km83wry) или [логирование безопасности](https://dt-url.net/vqa3w97). API Gateway обеспечивает дополнительный уровень безопасности, который можно быстро применить к вашим сервисам без изменения базового кода.

Далее вы узнаете, как [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональные возможности Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ причин и поиск угроз.") может помочь вам отслеживать и выявлять ошибки в логах доступа Amazon API Gateway.

## Целевая аудитория

Эта статья предназначена для инженеров по безопасности и инженеров по надёжности (SRE), участвующих в обслуживании и защите облачных приложений в AWS. Она показывает, как максимально эффективно использовать логи Amazon API Gateway, загружаемые в Dynatrace, для обнаружения проблем безопасности.

## Предварительные требования

* Создайте [группу логов Amazon CloudWatch](https://dt-url.net/r8c3wk1) для логов доступа Amazon API Gateway
* [Настройте Amazon Data Firehose](../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет напрямую загружать облачные логи без дополнительной инфраструктуры и с более высокой пропускной способностью.") для отправки логов из группы логов в Dynatrace
* Знание

  + [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.") и [как использовать запросы DQL](../../platform/grail/dynatrace-query-language/dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
  + [Dynatrace Pattern Language](../../platform/grail/dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью матчеров.")

## Перед началом

Включите логирование и убедитесь, что логи сохраняются в группу логов CloudWatch (в этом примере `/aws/apigateway/my-gateway-demo`) и отправляются в вашу среду Dynatrace.

1. Включите логирование Amazon API Gateway

1. В AWS перейдите на страницу сервиса **API Gateway**.
2. Выберите ваш **API Gateway API** из списка API.

   В этом примере использовался HTTP API (API Gateway поддерживает несколько типов API, и конфигурации логирования различаются для каждого из них).
3. В боковом меню выберите **Monitor** > **Logging**.
4. Выберите **Choose a stage** для настройки логирования, затем выберите **Edit**.
5. Включите **Access logging**.
6. В поле **Log destination** введите ARN группы логов `/aws/apigateway/my-gateway-demo`.
7. В поле **Log format** выберите `JSON` для упрощения разбора записей логов.
8. В разделе **Additional fields** настройте формат лога, затем выберите **Save**.

   Список доступных полей см. в [Настройка логов доступа HTTP API](https://dt-url.net/hk03wez).

   В этом примере используется следующий формат лога:

   ```
   {


   "requestId": "$context.requestId",


   "ip": "$context.identity.sourceIp",


   "requestTime": "$context.requestTime",


   "httpMethod": "$context.httpMethod",


   "routeKey": "$context.routeKey",


   "path": "$context.path",


   "status": "$context.status",


   "protocol": "$context.protocol",


   "responseLength": "$context.responseLength",


   "responseLatency": "$context.responseLatency",


   "integrationLatency": "$context.integrationLatency",


   "integrationStatus": "$context.integrationStatus",


   "errorMessage": "$context.error.message",


   "integrationErrorMessage": "$context.integrationErrorMessage"


   }
   ```

2. Проверьте, что запросы API Gateway логируются

1. В Dynatrace откройте ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** и выберите **Investigation**, чтобы создать новый сценарий расследования.
2. Чтобы проверить, что логи из группы логов Amazon CloudWatch поступают в вашу среду Dynatrace, выполните следующий запрос:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```

   Пример результата:

   ![fetch logs](https://dt-cdn.net/images/2025-01-27-11-45-07-1546-309fa661f3.png)

   Если логи не отображаются, проверьте фильтр подписки CloudWatch и настройки Data Firehose (включая метрики производительности, настройки тенанта и буфера).

## Начало работы

Анализируйте логи Amazon API Gateway с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональные возможности Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ причин и поиск угроз.").

1. Обнаружение проблем бэкенда с помощью метрик задержки

1. Как выбрать метрику для анализа

Логи API Gateway содержат много полезной информации для отладки ваших бэкенд-приложений. Одной из стандартных метрик для мониторинга API Gateway является задержка. Из логов API Gateway можно отслеживать два типа задержки:

* **Задержка интеграции**: Время между передачей запроса API Gateway на бэкенд и получением ответа от бэкенда.
* **Задержка ответа**: Время между получением запроса от клиента API Gateway и возвратом ответа клиенту. Включает задержку интеграции и прочие накладные расходы API Gateway.

Выбор метрики для мониторинга производительности зависит от вашего сценария использования. Поскольку данный пример фокусируется на производительности бэкенда, а не на всём цикле запроса, будет использоваться задержка интеграции.

Следуйте шагам ниже для анализа и выявления сервисов с наибольшей задержкой.

1. Получите логи API Gateway из Grail:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"
   ```
2. В таблице результатов запроса щёлкните правой кнопкой мыши по полю и выберите **View field details**, чтобы [просмотреть запись лога в исходном формате](../investigations/enhance-results.md#view-details "Организация и интерпретация результатов запросов в расследованиях — от анализа производительности до обнаружения угроз.").

   Пример записи лога в формате JSON:

   ```
   {


   "requestId": "Dzfa6gNrrks42Tw=",


   "ip": "14.21.74.45",


   "requestTime": "03/Jan/2025:09:22:13 +0000",


   "httpMethod": "GET",


   "routeKey": "ANY /",


   "path": "/getStuff",


   "status": "200",


   "protocol": "HTTP/1.1",


   "responseLength": "33",


   "responseLatency": "1671",


   "integrationLatency": "1665",


   "integrationStatus": "200",


   "errorMessage": "-",


   "integrationErrorMessage": "-"


   }
   ```
3. Добавьте следующую [команду parse](../../platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands.md "Команды извлечения DQL") к запросу DQL для извлечения свойств `path` и `integrationLatency` из записи JSON.

   ```
   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"
   ```

   В этом примере используются [Dynatrace Pattern Language](../../platform/grail/dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью матчеров.") и [JSON-матчер](../../platform/grail/dynatrace-pattern-language/log-processing-json-object.md "Синтаксис DPL для обработки JSON-объектов.") для извлечения [выбранных матчеров](../../platform/grail/dynatrace-pattern-language/log-processing-json-object.md#parse-selected "Синтаксис DPL для обработки JSON-объектов.") в отдельные поля.

   Используемый шаблон DPL:

   ```
   JSON{


   STRING:path,


   INT:integrationLatency


   }(flat=true)
   ```

   После выполнения запроса вы увидите два новых столбца — **path** и **integrationLatency** — в таблице результатов.
4. Для упрощения просмотра результатов добавьте следующую [команду `makeTimeseries`](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#makeTimeseries "Команды агрегации DQL") к запросу DQL для создания метрики из логов API Gateway. Метрика должна использовать path в качестве измерения и среднюю задержку в минуту в качестве значений.

   ```
   | makeTimeseries {


   latency = avg(integrationLatency, default:0)


   },


   by: { path },


   interval:1m
   ```

   Ваш запрос DQL должен выглядеть так:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"


   | parse content, "JSON{ STRING:path, INT:integrationLatency }(flat=true)"


   | makeTimeseries {


   latency = avg(integrationLatency, default:0)


   }, by: { path }, interval:1m
   ```

   Пример результата в виде графика:

   ![chart1](https://dt-cdn.net/images/2025-01-27-15-02-11-1530-a85e8ff3a0.png)

   Обнаруживается, что вы испытываете периодические проблемы с задержкой для обоих эндпоинтов сервиса.

2. Выявление проблем с задержкой и отладка кодов ответа

Следуйте шагам ниже для углублённого анализа кодов ответа.

1. Извлеките коды ответа как дополнительный столбец с [INT-матчером](../../platform/grail/dynatrace-pattern-language/log-processing-numeric.md#int "Синтаксис DPL для обработки числовых данных."), поскольку ожидается целочисленное значение поля.

   Используемый шаблон DPL:

   ```
   JSON{ STRING:path, INT:status, INT:integrationLatency }(flat=true)
   ```

   Видно, что код ответа называется `status`.
2. Чтобы добавить статус как одно из измерений метрики, добавьте поле `status` в параметр `by` команды `maketimeseries`.

   ```
   | makeTimeseries {


   latency = avg(integrationLatency, default:0)


   },


   by: { path, status },


   interval:1m
   ```

   Ваш запрос DQL должен выглядеть так:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"


   | parse content, "JSON{ STRING:path, INT:status INT:integrationLatency }(flat=true)"


   | makeTimeseries {


   latency = avg(integrationLatency, default:0)


   }, by: { path, status }, interval:1m
   ```

   Пример результата в виде графика:

   ![chart 2](https://dt-cdn.net/images/2025-01-27-15-07-19-1529-0f585fe086.png)

   Обнаруживается, что успешных ответов нет: запросы выполняются дольше, и все ответы возвращают ошибку сервера (HTTP/500).

3. Отладка ошибок интеграции

Следуйте шагам ниже для продолжения отладки ошибок интеграции.

1. Для анализа сообщений об ошибках извлеките дополнительное поле **integrationErrorMessage** из записи лога с помощью строкового матчера.

   Используемый шаблон DPL:

   ```
   JSON{


   STRING:path,


   INT:status,


   INT:integrationLatency,


   STRING:integrationErrorMessage


   }(flat=true)
   ```
2. Добавьте следующий фрагмент к запросу DQL для агрегации сообщений об ошибках и сортировки их по количеству:

   ```
   | summarize count(), by: { integrationErrorMessage }


   | sort `count()` desc
   ```

   Ваш запрос DQL должен выглядеть так:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"


   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"


   | summarize count(), by: { integrationErrorMessage }


   | sort `count()` desc
   ```

   В результатах выделяется характерное сообщение об ошибке тайм-аута: `The Lambda function returned the following error: RequestId: 01fe3839-4974-40d5-960a-173fcb5ec786 Error: Task timed out after 5.00 seconds. Check your Lambda function code and try again.`
3. Извлеките часть `Error` из записи лога без идентификатора запроса для сравнения этого сообщения с другими.

   Используемый шаблон DPL:

   ```
   LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error
   ```

   Теперь у вас есть два поля (**error** и **integrationErrorMessage**), которые могут содержать сообщение об ошибке.
4. Добавьте следующий фрагмент к запросу DQL для объединения двух полей в один столбец с помощью функции `if` и агрегации по этому полю.

   ```
   | fields error = if(isnull(error), integrationErrorMessage, else: error)


   | summarize count(), by: { error }
   ```

   Ваш запрос DQL должен выглядеть так:

   ```
   fetch logs


   | filter aws.log_group == "/aws/apigateway/my-gateway-demo"


   | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"


   | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"


   | fields error = if(isnull(error), integrationErrorMessage, else: error)


   | summarize count(), by: { error }
   ```

   Пример результатов:

   ![results](https://dt-cdn.net/images/2025-01-27-15-55-59-1538-7994d7382c.png)

   Обнаруживается, что ошибки тайм-аута являются наиболее частыми.
5. Чтобы увидеть, как сообщения об ошибках распределяются за тот же период, создайте метрику на основе ошибок тайм-аута следующим образом:

* Добавьте [команду `filterOut`](../../platform/grail/dynatrace-query-language/commands/filtering-commands.md#filterOut "Команды фильтрации и поиска DQL") для удаления успешных событий
* Добавьте поле `timestamp` в [команду `fields`](../../platform/grail/dynatrace-query-language/commands/selection-and-modification-commands.md#fields "Команды выбора и модификации DQL")
* Создайте команду `makeTimeseries` для агрегации ошибок по количеству с минутным интервалом.

  Ваш итоговый запрос должен выглядеть так:

  ```
  fetch logs


  | filter aws.log_group == "/aws/apigateway/my-gateway-demo"


  | parse content, "JSON{ STRING:path, INT:status, INT:integrationLatency, STRING:integrationErrorMessage }(flat=true)"


  | parse integrationErrorMessage, "LD ': RequestId: ' UUIDSTRING ' Error: ' LD:error"


  | fields timestamp, error = if(isnull(error), integrationErrorMessage, else: error)


  | filterOut error == "-"


  | makeTimeseries count(default: 0), by: { error }, interval: 1m
  ```

  Пример результата в виде графика:

  ![chart 3](https://dt-cdn.net/images/2025-01-27-15-50-54-1509-00bad2a7dc.png)

  Обнаруживается, что вы испытываете проблемы с тайм-аутами Lambda, которые создают задержки и ошибки сервера в логах API Gateway.

  Для дальнейшего расследования необходимо изучить функцию Lambda и выяснить, почему это поведение возникает именно в эти моменты. Причинами могут быть запланированные задания, блокировка или перегрузка ресурсов, а также другие зависимости.

## Связанные темы

* [Анализ логов AWS CloudTrail с помощью Investigations](analyze-aws-cloudtrail-logs-with-security-investigator.md "Анализируйте логи CloudTrail и находите потенциальные проблемы безопасности с помощью Dynatrace.")
* [Обнаружение угроз для ваших секретов AWS с помощью Investigations](detect-threats-against-aws-secrets-with-security-investigator.md "Отслеживайте и выявляйте потенциальные угрозы для ваших секретов AWS с помощью Dynatrace.")
* [Поиск угроз и цифровая криминалистика](threat-hunting.md "Сценарий использования для поиска угроз и цифровой криминалистики с Investigations.")
* [Операционализация результатов запросов DQL с помощью Investigations](operationalize-query-results.md "Быстрее и удобнее создавайте запросы DQL из результатов с помощью Dynatrace Investigations.")
* [Ускорение разрешения инцидентов с помощью шаблонов Investigations](resolve-incidents-faster-with-templates.md "Ускорьте расследования, связанные с логами, с помощью шаблонов Investigations.")