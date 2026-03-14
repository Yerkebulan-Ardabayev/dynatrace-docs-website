---
title: Анализ журналов AWS CloudTrail с помощью Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator
scraped: 2026-03-06T21:28:49.736649
---

# Анализ логов AWS CloudTrail с помощью Investigations

# Анализ логов AWS CloudTrail с помощью Investigations

* Latest Dynatrace
* Руководство
* Опубликовано 26 ноября 2024

[AWS CloudTrail](https://dt-url.net/ax63uwp) — это сервис AWS, который помогает обеспечить операционный аудит и аудит рисков, управление и соответствие требованиям вашей учётной записи AWS. Действия, выполняемые пользователем, ролью или сервисом AWS в среде Amazon AWS, записываются как события в CloudTrail. События включают действия, выполненные в AWS Management Console, AWS Command Line Interface, а также через AWS SDK и API.

Далее вы узнаете, как [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") могут помочь вам

* [Мониторинг сбоев входа в консоль AWS](#sign-in)
* [Создание метрик для несанкционированных вызовов API](#metrics)
* [Мониторинг ограничения AWS API](#monitor)
* [Обнаружение внешне сгенерированных ключей в AWS KMS](#keys)

## Целевая аудитория

Эта статья предназначена для инженеров по безопасности и инженеров по надёжности сайтов, которые участвуют в обслуживании и защите облачных приложений в AWS.

## Предварительные требования

* Сохраняйте логи CloudTrail в бакет S3 или [CloudWatch](https://dt-url.net/mr03u6p).
* Отправляйте логи CloudTrail в Dynatrace. Есть два варианта потоковой передачи логов:

  + [Amazon S3](https://dt-url.net/c703wc8) (рекомендуется)
  + [Amazon Data Firehose](../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет загружать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.")
* Знание

  + [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.") и [как использовать DQL-запросы](../../platform/grail/dynatrace-query-language/dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
  + [Dynatrace Pattern Language](../../platform/grail/dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью сопоставителей.")

## Прежде чем начать

Выполните следующие шаги для получения логов AWS CloudTrail из Grail с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** и подготовки их к анализу.

1. Получение логов AWS CloudTrail из Grail

После загрузки логов CloudTrail в Dynatrace выполните следующие шаги для их получения.

1. Откройте [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations.md "Объедините функциональность Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.").
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation** для создания сценария расследования.
3. В разделе ввода запроса вставьте DQL-запрос ниже.

   ```
   fetch logs, from: -30min



   | filter aws.service == "cloudtrail"
   ```
4. Выберите ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") **Run** для отображения результатов.

   Запрос выполнит поиск логов за последние 30 минут, которые были переданы из группы логов AWS, содержащей слово `cloudtrail`.

   Если вы знаете, в каком бакете Grail хранятся логи CloudTrail, используйте фильтры для указания бакета для улучшения производительности запроса.

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"
   ```

   Подробности см. в [лучших практиках DQL](../../platform/grail/dynatrace-query-language/dql-best-practices.md "Лучшие практики использования Dynatrace Query Language.").

   Таблица результатов будет заполнена событиями в формате JSON.
5. Щёлкните правой кнопкой мыши по событию и выберите **View field details** для просмотра события в формате JSON в структурированном виде. Это позволяет исследователям быстрее понять содержимое события.

   ![results table](https://dt-cdn.net/images/image-20241109-145818-3100-3e65568b52.png)
6. Перемещайтесь между событиями в таблице результатов с помощью клавиш со стрелками на клавиатуре или кнопок навигации в верхней части окна **View field details**.

   ![field details](https://dt-cdn.net/images/image-20241106-153049-1-2040-9f9e875bf6.png)

2. Подготовка данных к анализу

Выполните следующие шаги для упрощения анализа логов, ускорения расследований и поддержания необходимой точности для аналитических задач.

1. Добавьте к вашему DQL-запросу [команду parse](../../platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands.md "Команды извлечения DQL") для извлечения необходимых данных из записей логов в отдельные поля.
2. Добавьте [JSON-сопоставитель](../../platform/grail/dynatrace-pattern-language/log-processing-json-object.md "Изучите синтаксис DPL для работы с JSON-объектами.") для извлечения содержимого лога в формате JSON как JSON-объекта в отдельное поле `event`.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"
   ```
3. Дважды щёлкните по любой записи в таблице результатов для просмотра объекта в представлении **Record details**. Разверните элементы JSON для более быстрой навигации по объекту и добавления фильтров на основе его содержимого.

   ![Record details](https://dt-cdn.net/images/image-20241106-155245-1-2288-9851882d34.png)

## Начало работы

Далее приведены сценарии использования, демонстрирующие, как построить вышеуказанный запрос для анализа логов AWS CloudTrail с помощью Dynatrace.

1. Мониторинг сбоев входа в консоль AWS

Сбои в логах аутентификации могут указывать на потенциальную атаку на вашу инфраструктуру. Злоумышленник может пытаться перебирать имена пользователей или пароли, чтобы получить доступ к вашей среде AWS и взять под контроль ваш бизнес.

Для мониторинга сбоев входа в консоль AWS с помощью логов CloudTrail

1. Добавьте оператор фильтрации для получения только результатов с `signin.amazonaws.com` в качестве источника события и `ConsoleLogin` в качестве имени события.
2. Добавьте команду фильтрации для подэлемента `responseElements.ConsoleLogin` в JSON-объекте со значением `Failure`, чтобы видеть только неудачные попытки входа.

   Вы можете использовать фрагмент DQL ниже.

   ```
   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName] == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"
   ```
3. Добавьте команду `summarize` с выбранными полями для получения агрегированного обзора событий.

   Вы можете использовать фрагмент DQL ниже.

   ```
   | summarize event_count = count(), by: {



   source  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

   Ваш финальный DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"



   | filter event[eventSource] == "signin.amazonaws.com"



   and event[eventName]   == "ConsoleLogin"



   and event[responseElements][ConsoleLogin] == "Failure"



   | summarize count(), by: {



   ipAddr  = event[sourceIPAddress],



   reason  = event[errorMessage],



   region  = event[awsRegion],



   userARN = event[userIdentity][arn],



   MFAUsed = event[additionalEventData][MFAUsed]



   }
   ```

2. Создание метрик для несанкционированных вызовов API

Несанкционированные вызовы API могут указывать на попытку взлома или сбой системы. Такого рода аномалии следует расследовать для предотвращения непредвиденных расходов или захвата системы злоумышленниками.

Для определения «основных целей» из списка API

1. Создайте фильтр для получения только событий с кодом ошибки `AccessDenied` или `UnauthorizedOperation`.
2. Добавьте [команду makeTimeseries](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#makeTimeseries "Команды агрегации DQL") для преобразования результатов логов в метрики.
3. Добавьте значение `event[eventName]` из логов в качестве измерения метрики.
4. Отсортируйте результаты, чтобы увидеть только топ-10 API, и ограничьте результаты 10 записями.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter in(event[errorCode], { "AccessDenied", "UnauthorizedOperation" })



   | makeTimeseries event_count = count(), by: { eventName = event[eventName] }



   | sort arrayAvg(event_count) desc



   | limit 10
   ```

   Для большей детализации вы можете добавить больше измерений в команду `makeTimeseries`.

   Например, чтобы увидеть графики вызовов API на основе пользователя и конечной точки API, команда агрегации будет выглядеть следующим образом.

   ```
   | makeTimeseries count(), by: {



   user      = event[userIdentity][arn],



   eventName = event[eventName]



   }
   ```

   Пример результатов, визуализированных в виде линейного графика:

   ![ results visualized to a line-chart ](https://dt-cdn.net/images/image-20241108-135013-2334-7d17f90671.png)

3. Мониторинг ограничения AWS API

Мониторинг количества запросов к API важен с точки зрения доступности, стоимости и безопасности. Ограничение API может указывать на атаку методом перебора, атаку типа «отказ в обслуживании» или текущую эксфильтрацию данных злоумышленником.

Для мониторинга ограничения AWS API из логов AWS CloudTrail в Dynatrace

1. Создайте фильтр для получения только событий с кодом ошибки `Client.RequestLimitExceeded`.
2. Добавьте [команду makeTimeseries](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#makeTimeseries "Команды агрегации DQL") для преобразования результатов логов в метрики.
3. Добавьте значение `event[eventName]` из логов в качестве измерения метрики.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[errorCode] == "Client.RequestLimitExceeded"



   | makeTimeseries count(), by: { eventName = event[eventName] }
   ```

4. Обнаружение внешне сгенерированных ключей в AWS KMS

При создании нового ключа в [AWS Key Management Service (KMS)](https://dt-url.net/4g23uoc) вы можете выбрать источник материала ключа: будут ли ключи находиться под контролем AWS или обрабатываться внешне.

По умолчанию источник материала ключа — `AWS_KMS`, что означает, что KMS создаёт материал ключа.

Когда ключи обрабатываются внешне, существует повышенный риск утечки ключей, что ставит под угрозу данные, защищённые этим ключом: ключ может быть скомпрометирован из другого источника, и его местоположение может быть неизвестно.

Для обнаружения таких создаваемых ключей, где использовался внешний материал ключа

1. Создайте фильтр для получения только событий с именем `CreateKey`.
2. Добавьте оператор в фильтр для исключения всех источников, начинающихся с `AWS_`.

   В настоящее время есть два варианта (`AWS_KMS` и `EXTERNAL`), поэтому вы можете фильтровать по источнику `External`, но фильтрация по исключению может быть более универсальной для будущих изменений.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "CreateKey"



   | filterOut startsWith(event[requestParameters][origin], "AWS_")



   | fields {



   eventName = event[eventName],



   origin    = event[requestParameters][origin],



   keyUsage  = event[responseElements][keyMetadata][keyUsage],



   region    = event[awsRegion],



   userARN   = event[userIdentity][arn],



   keyId     = event[responseElements][keyMetadata][keyId]



   }
   ```

В результате вы получите таблицу со следующей информацией:

* **eventName**: CreateKey
* **origin**: EXTERNAL
* **keyUsage**: ENCRYPT\_DECRYPT
* **region**: us-east-1
* **userARN**: имя пользователя
* **keyId**: 123acb

## Итоги

Это некоторые из сценариев использования, которые можно решить с помощью логов CloudTrail и Dynatrace ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**. Эти логи являются неисчерпаемым источником информации, который позволяет инженерам по безопасности и DevOps проводить различные расследования инфраструктуры AWS.

## Связанные темы

* [Анализ логов доступа Amazon API Gateway с помощью Investigations](analyze-aws-api-gateway-access-logs-with-security-investigator.md "Мониторинг и выявление ошибок в логах доступа Amazon API Gateway с помощью Dynatrace.")
* [Обнаружение угроз для секретов AWS с помощью Investigations](detect-threats-against-aws-secrets-with-security-investigator.md "Мониторинг и выявление потенциальных угроз для секретов AWS с помощью Dynatrace.")
* [Поиск угроз и криминалистика](threat-hunting.md "Сценарий использования для поиска угроз и криминалистики с помощью Investigations.")
* [Операционализация результатов DQL-запросов с помощью Investigations](operationalize-query-results.md "Создавайте DQL-запросы на основе результатов запросов быстрее и удобнее с помощью Dynatrace Investigations.")
* [Ускорение разрешения инцидентов с помощью шаблонов Investigations](resolve-incidents-faster-with-templates.md "Ускорьте расследования, связанные с логами, с помощью шаблонов Investigations.")