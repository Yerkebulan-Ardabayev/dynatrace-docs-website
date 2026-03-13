---
title: Detect threats against your AWS Secrets with Investigations
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator
scraped: 2026-03-06T21:38:02.748633
---

# Обнаружение угроз для ваших секретов AWS с помощью Investigations

# Обнаружение угроз для ваших секретов AWS с помощью Investigations

* Latest Dynatrace
* Руководство
* Опубликовано 26 нояб. 2024

В современном цифровом мире защита криптографических секретов в облачной среде важна как никогда. Секреты, такие как API-ключи, пароли и ключи шифрования, используемые в ваших приложениях, являются жизненно важными компонентами, утечка которых может поставить под угрозу весь бизнес. Вот почему анализ угроз для секретов необходим для обеспечения целостности, конфиденциальности и доступности ваших данных.

Далее вы узнаете, как [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объединение возможностей Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.") может помочь вам:

* [Обнаружить внешне сгенерированные ключи в AWS KMS](#keys)
* [Обнаружить непривилегированные запросы на чтение секретов](#requests)
* [Обнаружить запросы к несуществующим секретам](#secrets)

## Целевая аудитория

Эта статья предназначена для инженеров по безопасности и инженеров по надёжности (SRE), которые участвуют в обслуживании и обеспечении безопасности облачных приложений в AWS.

## Предварительные требования

* Сохраняйте логи CloudTrail в S3-бакет или [CloudWatch](https://dt-url.net/mr03u6p).
* Отправляйте логи CloudTrail в Dynatrace. Есть два варианта потоковой передачи логов:

  + [Amazon S3](https://dt-url.net/c703wc8) Рекомендуется
  + [Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Интеграция Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры, с более высокой пропускной способностью.")
* Знание:

  + [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.") и [работы с DQL-запросами](/docs/platform/grail/dynatrace-query-language/dql-guide "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
  + [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Использование Dynatrace Pattern Language для описания шаблонов с помощью сопоставителей.")

## Перед началом

Выполните приведённые ниже шаги, чтобы получить логи AWS CloudTrail из Grail с помощью ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** и подготовить их к анализу.

1. Получение логов AWS CloudTrail из Grail

После приёма логов CloudTrail в Dynatrace выполните следующие шаги для их получения.

1. Откройте [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объединение возможностей Grail для расследований на основе доказательств, включая разрешение инцидентов, анализ первопричин и поиск угроз.").
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Investigation**, чтобы создать сценарий расследования.
3. В поле ввода запроса вставьте следующий DQL-запрос.

   ```
   fetch logs, from: -30min



   | filter aws.service == "cloudtrail"
   ```
4. Выберите ![Run](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Run") **Run** для отображения результатов.

   Запрос выполнит поиск логов за последние 30 минут, которые были переданы из группы логов AWS, содержащей слово `cloudtrail`.

   Если вы знаете, в каком бакете Grail хранятся логи CloudTrail, используйте фильтры для указания бакета, чтобы улучшить производительность запроса.

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"
   ```

   Подробнее см. [Лучшие практики DQL](/docs/platform/grail/dynatrace-query-language/dql-best-practices "Лучшие практики использования Dynatrace Query Language.").

   Таблица результатов будет заполнена событиями в формате JSON.
5. Щёлкните правой кнопкой мыши по событию и выберите **View field details**, чтобы увидеть событие в формате JSON в структурированном виде. Это позволяет следователям быстрее понять содержание события.

   ![таблица результатов](https://dt-cdn.net/images/image-20241109-145818-3100-3e65568b52.png)
6. Переключайтесь между событиями в таблице результатов с помощью клавиш со стрелками или кнопок навигации в верхней части окна **View field details**.

   ![детали полей](https://dt-cdn.net/images/image-20241106-153049-1-2040-9f9e875bf6.png)

2. Подготовка данных к анализу

Выполните приведённые ниже шаги, чтобы упростить анализ логов, ускорить расследования и сохранить необходимую точность для аналитических задач.

1. Добавьте к DQL-запросу [команду parse](/docs/platform/grail/dynatrace-query-language/commands/extraction-and-parsing-commands "Команды извлечения DQL") для извлечения необходимых данных из записей логов в отдельные поля.
2. Добавьте [JSON-сопоставитель](/docs/platform/grail/dynatrace-pattern-language/log-processing-json-object "Изучите синтаксис DPL для работы с JSON-объектами."), чтобы извлечь содержимое лога в формате JSON как JSON-объект в отдельное поле `event`.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "JSON:event"
   ```
3. Дважды щёлкните по любой записи в таблице результатов, чтобы просмотреть объект в представлении **Record details**. Разверните элементы JSON для быстрой навигации по объекту и добавления фильтров на основе его содержимого.

   ![Детали записи](https://dt-cdn.net/images/image-20241106-155245-1-2288-9851882d34.png)

## Начало работы

Ниже приведены сценарии использования, демонстрирующие, как строить описанный выше запрос для анализа секретов AWS с помощью Dynatrace.

1. Обнаружение внешне сгенерированных ключей в AWS KMS

При создании нового ключа в [AWS Key Management Service (KMS)](https://dt-url.net/4g23uoc) вы можете выбрать источник материала ключа: находятся ли ключи под контролем AWS или обрабатываются внешне.

По умолчанию источник материала ключа -- `AWS_KMS`, что означает, что KMS создаёт материал ключа.

Когда ключи обрабатываются внешне, существует повышенный риск утечки ключей, что ставит под угрозу защищённые ими данные: ключ может утечь из другого места, и его местоположение может быть неизвестно.

Чтобы обнаружить создание ключей с использованием внешнего материала:

1. Создайте фильтр для получения только событий с именем `CreateKey`.
2. Добавьте условие в фильтр для исключения всех источников, начинающихся с `AWS_`.

   В настоящее время существует два варианта (`AWS_KMS` и `EXTERNAL`), поэтому можно фильтровать по источнику `External`, но фильтрация исключением более перспективна.

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
* **userARN**: username
* **keyId**: 123acb

2. Обнаружение непривилегированных запросов на чтение секретов

Неавторизованные запросы на чтение секретов являются признаком попытки взлома или неправильной конфигурации системы. Неавторизованные запросы могут означать, что злоумышленник скомпрометировал учётные данные вашей системы и пытается извлечь секреты из вашей учётной записи AWS (но, к счастью, безуспешно).

В этом сценарии мы рассматриваем два случая, нацеленных на различные попытки непривилегированного доступа к вашим секретам: [запросы без привилегий KMS](#no-kms-privilege) и [запросы к неавторизованным секретам](#unauthorized-secret).

#### Запросы без привилегий KMS

В случае отсутствия привилегий KMS можно предположить, что эти учётные записи не должны были иметь доступ к каким-либо секретам в вашей среде. Если это всё же происходит, это (злонамеренное или случайное) злоупотребление учётными данными или неправильная конфигурация. В любом случае это требует вашего внимания.

Чтобы проверить, пытается ли кто-то получить доступ к таким событиям в логах CloudTrail:

1. Создайте фильтр для получения только событий `GetSecretValue` с кодом ошибки `AccessDenied`.
2. Добавьте новое условие фильтрации, чтобы видеть только ошибки с сообщением `Access to KMS is not allowed`.
3. Агрегируйте результаты по `sourceIPAddress`, `awsRegion` и `ARN` пользователя неавторизованных попыток.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   and event[errorMessage] == "Access to KMS is not allowed"



   | summarize event_count = count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn]



   }
   ```

Если запрос вернёт результаты, они будут выглядеть так:

| **sourceIPAddress** | **region** | **arn** | **event\_count** |
| --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 3 |

#### Запросы к неавторизованным секретам

В этом случае учётная запись пытается загрузить привилегии, к которым у неё нет доступа. Конфигурация секрета может быть неправильной, или учётная запись может использоваться для секретов, для которых она не предназначена. Последний вариант представляет потенциальную угрозу безопасности, если намерение является злонамеренным.

Чтобы проверить, происходят ли такие события в логах CloudTrail:

1. Создайте фильтр для получения только событий `GetSecretValue` с кодом ошибки `AccessDenied`.
2. Если запрашиваемый секрет не существует или у пользователя нет к нему доступа, ARN секрета упоминается в сообщении об ошибке. Извлеките `secretID` из сообщения об ошибке.
3. Отобразите только события, в которых `secretID` присутствует.
4. Агрегируйте результаты по `sourceIPAddress`, `awsRegion` и `userARN` пользователя неавторизованных попыток.

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "AccessDenied"



   | parse event[errorMessage], "LD ':secret:' STRING:secretId"



   | filter isNotNull(secretId)



   | summarize count(), by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN = event[userIdentity][arn],



   secretId



   }
   ```

Если запрос вернёт результаты, они будут выглядеть так:

| **sourceIPAddress** | **awsRegion** | **arn** | **secretId** | **event\_count** |
| --- | --- | --- | --- | --- |
| 1.2.3.4 | us-east-1 | username | 123abc | 3 |

3. Обнаружение запросов к несуществующим секретам

Запросы к несуществующим секретам могут указывать на проблему безопасности (например, когда кто-то пытается перебрать ваши секреты для их извлечения и пробует различные секреты, которые могут не существовать) или на операционную проблему (секреты, используемые сервисом, больше не доступны, что создаёт проблемы в работе сервиса).

Чтобы проверить, присутствуют ли такие события в логах CloudTrail:

1. Создайте фильтр для получения событий `GetSecretValue`.
2. Добавьте условия фильтра для получения только событий с сообщением об ошибке `ResourceNotFoundException`.
3. Агрегируйте результаты по `sourceIPAddress`, `awsRegion` и `userARN` и подсчитайте количество событий и уникальных секретов, запрошенных данным пользователем в соответствующем регионе AWS с конкретного IP-адреса.

   Если вы видите большое количество уникальных секретов, запрашиваемых с одного `userARN`, это может быть перебором секретов. Если количество различных секретов невелико, вероятно, что-то произошло с самим секретом (неправильный набор привилегий, секрет был удалён или подобное).

   Ваш DQL-запрос должен выглядеть так:

   ```
   fetch logs, from: -30min



   | filter dt.system.bucket == "my_aws_bucket"



   | filter aws.service == "cloudtrail"



   | parse content, "json:event"



   | filter event[eventName] == "GetSecretValue"



   and event[errorCode] == "ResourceNotFoundException"



   | summarize {



   event_count = count(),



   distinct_secrets = countDistinct(event[requestParameters][secretId])



   }, by: {



   sourceIPAddress = event[sourceIPAddress],



   awsRegion = event[awsRegion],



   userARN   = event[userIdentity][arn]



   }



   | sort distinct_secrets desc
   ```

## Связанные темы

* [Поиск угроз и криминалистика](/docs/secure/use-cases/threat-hunting "Сценарий использования для поиска угроз и криминалистики с помощью Investigations.")
* [Анализ логов AWS CloudTrail с помощью Investigations](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Анализ логов CloudTrail и поиск потенциальных проблем безопасности с помощью Dynatrace.")
* [Анализ логов доступа Amazon API Gateway с помощью Investigations](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Мониторинг и выявление ошибок в логах доступа Amazon API Gateway с помощью Dynatrace.")
* [Ускорение разрешения инцидентов с помощью шаблонов Investigations](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Ускорьте расследования, связанные с логами, с помощью шаблонов Investigations.")
* [Операционализация результатов DQL-запросов с помощью Investigations](/docs/secure/use-cases/operationalize-query-results "Быстрее и удобнее создавайте DQL-запросы из результатов запросов с помощью Dynatrace Investigations.")
