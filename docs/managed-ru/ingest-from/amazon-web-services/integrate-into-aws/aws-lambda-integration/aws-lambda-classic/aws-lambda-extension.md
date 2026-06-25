---
title: Трассировка Lambda-функций на Python, Node.js и Java
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension
scraped: 2026-05-12T12:03:57.549977
---

# Трассировка Lambda-функций на Python, Node.js и Java

# Трассировка Lambda-функций на Python, Node.js и Java

* Практическое руководство
* Чтение: 14 мин
* Обновлено 23 января 2026 г.

Эта страница относится к классической интеграции AWS Lambda. Актуальную версию см. в разделе [Трассировка Lambda-функций](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Мониторинг AWS Lambda-функций.").

Dynatrace предоставляет специализированный AWS Lambda layer, содержащий расширение Dynatrace для AWS Lambda. Нужно добавить публично доступный layer для вашей среды выполнения и региона к вашей функции. После этого, в зависимости от выбранного метода конфигурации, Dynatrace предоставляет шаблон или конфигурацию для вашей AWS Lambda-функции.

## Входящие вызовы

Dynatrace может мониторить входящие вызовы только если они выполнены через:

* AWS SDK Lambda Invoke API
* API gateway
* Lambda function URL
* AWS SQS
* AWS SNS

Для других типов вызовов OneAgent не может зафиксировать специфичную информацию или связать трассировку с любым родителем. Вызовы через AWS SDK требуют, чтобы клиент был инструментирован Dynatrace для связки трассировки.

## Предварительные условия

* Поддерживаемая [среда выполнения](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "Возможности AWS Lambda и варианты интеграции") AWS Lambda. Расширение Dynatrace поддерживает AWS Lambda-функции, написанные на **Node.js**, **Python** или **Java**.
  Поддерживаются обе архитектуры: **64-bit ARM** ([процессоры AWS Graviton2](https://aws.amazon.com/ec2/graviton/)) и **64-bit x86**.
* Java К объёму RAM применяются следующие требования:

  + Если [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) включён и версия OneAgent 1.267+, минимальный объём памяти должен быть 512 МБ.
  + Если [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) не включён и версия OneAgent 1.265 или ниже, минимальный объём памяти должен быть 1 500 МБ.
    Чтобы настроить память в консоли AWS Lambda, перейдите в **General** > **Basic settings** и задайте **Memory**.

  Изменение объёма памяти влияет на доступную функции виртуальную мощность CPU. Подробнее см. ниже раздел [Накладные расходы мониторинга](#monitoring-overhead).

  + Обратите внимание, что требования к RAM для Lambda-функций на Node.js и Python могут быть существенно ниже. Вычислительная мощность в AWS Lambda масштабируется с выделенным объёмом памяти, и при низких настройках памяти время выполнения функции становится значительно медленнее.
* Активируйте функцию OneAgent **Forward Tag 4 trace context extension**. Перейдите в **Settings** > **Preferences** > **OneAgent features**.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Включите AWS Lambda**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#activate-aws-lambda "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Выберите метод конфигурации**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 3 необязательный](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3 необязательный")

**Укажите API-эндпоинт Dynatrace**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-endpoint "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 4 необязательный](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4 необязательный")

**Включите Real User Monitoring**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Задайте имя AWS layer**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-layer "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 6 необязательный](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Шаг 6 необязательный")

**Развёртывание**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#deployment "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

**Параметры конфигурации**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#config-options "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")[![Шаг 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Шаг 8")

**Интеграция Dynatrace AWS**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#aws-integration "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")

## Шаг 1 Включите AWS Lambda

Чтобы начать

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **AWS Lambda**.

3. Следуйте инструкциям, чтобы включить мониторинг AWS Lambda-функций.

## Шаг 2 Выберите метод конфигурации

Dynatrace OneAgent распространяется как Lambda layer, который можно включить и настроить вручную либо с помощью популярных Infrastructure as Code (IaC) решений.
Lambda layer хранится в AWS-аккаунте Dynatrace `725887861453`.

На странице **Enable Monitoring for AWS Lambda Functions** используйте список **How will you configure your AWS Lambda functions?**, чтобы выбрать предпочтительный метод, а затем убедитесь, что вы задали все свойства для выбранного метода, прежде чем копировать сгенерированные конфигурационные сниппеты.

Configure with JSON file

Если вы выбираете этот метод, Dynatrace предоставляет:

* Переменную окружения, которую нужно добавить к вашей AWS Lambda-функции
* JSON-сниппет, который нужно скопировать в файл `dtconfig.json` в корневой папке развёртывания Lambda
* Lambda layer ARN

При использовании этого метода убедитесь, что Dynatrace Lambda layer добавлен к вашей функции. Это можно сделать через консоль AWS (**Add layer** > **Specify an ARN** и вставьте ARN, отображаемый на странице развёртывания) или с помощью выбранного вами автоматизированного решения.

**Введите переменные окружения через консоль AWS**

![Lambda environment variables cropped](https://dt-cdn.net/images/lambda-environment-variables-cropped-776-af551d0520.png)

Lambda environment variables cropped

**Введите Lambda layer ARN через консоль AWS**

![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Specify a layer by providing the ARN

Configure with environment variables

При использовании этого метода убедитесь, что Dynatrace Lambda layer добавлен к вашей функции. Layer, как и переменные окружения, можно задать либо вручную через консоль AWS (**Add layer** > **Specify an ARN** и вставьте ARN, отображаемый на странице развёртывания), либо с помощью выбранного вами автоматизированного решения.

[Клиентское расшифровывание переменных окружения (Security in Transit)](https://dt-url.net/tz234sd) не поддерживается.

Если вы выбираете этот метод, Dynatrace предоставляет:

* Значения для определения переменных окружения для AWS Lambda-функций, которые вы хотите мониторить

  ![Lambda environment variables](https://dt-cdn.net/images/lambda-env-variables-1614-77850f4051.png)

  Lambda environment variables
* Lambda layer ARN

  ![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

  Specify a layer by providing the ARN

Configure and deploy using Terraform

Terraform: популярное решение Infrastructure as Code (IaC). Если вы выбираете этот метод, Dynatrace предоставляет:

* Шаблон для определения AWS Lambda-функции. Он включает всю конфигурацию, необходимую для развёртывания и настройки расширения Dynatrace для AWS Lambda вместе с вашими функциями.
* Lambda layer ARN

Configure and deploy using AWS SAM

AWS Serverless Application Model (SAM): open-source фреймворк для построения serverless-приложений.

Если вы выбираете этот метод, Dynatrace предоставляет шаблон для определения AWS Lambda-функции. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace для AWS Lambda.

Configure and deploy using the serverless framework

Опция Serverless Application: фреймворк для развёртывания serverless-стеков.

Если вы выбираете этот метод, Dynatrace предоставляет шаблон для определения AWS Lambda-функции. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace для AWS Lambda.

Configure and deploy using AWS CloudFormation

AWS CloudFormation: IaC-решение, позволяющее провижионить широкий набор AWS-сервисов.

Если вы выбираете этот метод, Dynatrace предоставляет шаблон для определения AWS Lambda-функции. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace для AWS Lambda.

## Шаг 3 Укажите API-эндпоинт Dynatrace Обязательно

Укажите публичный API-эндпоинт Dynatrace, на который будут отправляться данные мониторинга.

Типичный сценарий: развернуть Dynatrace ActiveGate в непосредственной близости (в том же регионе) к Lambda-функциям, которые вы хотите мониторить, чтобы снизить сетевую задержку, которая может повлиять на время выполнения и холодного старта ваших Lambda-функций (обычно это один сетевой запрос OneAgent на каждый вызов Lambda, который происходит в конце вызова). Типичные значения накладных расходов см. в разделе [Накладные расходы мониторинга](#monitoring-overhead).

## Шаг 4 необязательный Включите Real User Monitoring Необязательно

Это необязательный шаг для использования Real User Monitoring (RUM), который предоставляет глубокую информацию о действиях пользователей и производительности в браузере или мобильных приложениях.

### Настройка AWS

* Убедитесь, что заголовок `x-dtc` разрешён в настройках CORS ваших мониторируемых Lambda-функций.

  Для работы RUM с Lambda-функциями требуется отправка специального заголовка (`x-dtc`) с XHR-запросами к AWS. Чтобы это включить, настройки CORS вашего AWS-развёртывания должны разрешать заголовок `x-dtc` во время предварительных (`OPTIONS`) запросов. Чтобы настроить CORS и разрешить заголовок `x-dtc` для вашей конкретной конфигурации, см. [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

### Настройка Dynatrace

Чтобы настроить заголовок `x-dtc` для вызовов ваших Lambda-функций

1. Перейдите в **Web**, **Mobile**, **Frontend** или **Custom Applications**, в зависимости от типа вашего приложения.
2. Выберите приложение, которое вы хотите связать со своей Lambda-функцией.
3. Выберите меню обзора (**â¦**) в правом верхнем углу и нажмите **Edit**.
4. Выберите **Capturing** > **Async web requests and SPAs**.
5. Убедитесь, что выбранный фреймворк включён. Если вашего фреймворка нет в списке, включите **Capture XmlHttpRequest (XHR)** для общей поддержки `XHR`.
6. Выберите **Capturing** > **Advanced setup**.
7. Прокрутите вниз до раздела **Enable Real User Monitoring for cross-origin XHR calls** и введите паттерн, который соответствует URL ваших Lambda-функций. Пример: `TheAwsUniqueId.execute-api.us-east-1.amazonaws.com`
8. Нажмите **Save**. Через несколько минут заголовок будет добавляться ко всем вызовам вашей Lambda-функции, и запросы из браузера будут связаны с бэкендом.

Неуспешные запросы

Если после включения этой опции запросы начали падать, проверьте настройки CORS. Как настроить CORS, см. в [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

![Service Flow for AWS Lambda function](https://dt-cdn.net/images/aws-lambda1-service-flow-1430-f09d3a9ebe.png)

Service Flow for AWS Lambda function

## Шаг 5 Задайте имя AWS layer

Выберите AWS-регион и среду выполнения Lambda-функции, которую вы хотите мониторить. Эти параметры необходимы для предоставления корректного layer ARN.

## Шаг 6 Развёртывание

Скопируйте конфигурационные сниппеты в ваше развёртывание и используйте выбранный метод развёртывания, чтобы включить layer и задать конфигурацию для ваших Lambda-функций.

## Шаг 7 Параметры конфигурации

### Настройка AWS API Gateway

* Если входящие (не XHR) запросы к вашим Lambda-функциям не связываются с вызывающим приложением, настройте API Gateway, чтобы он пропускал Dynatrace-тег. Для этого включите **Use Lambda Proxy Integration** на странице конфигурации **Integration Request** API Gateway.
* Если API Gateway настраивается со страницы конфигурации Lambda, этот параметр будет включён по умолчанию. Подробнее см. [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).

AWS Lambda также поддерживает [**non-proxy integration**](https://dt-url.net/8u03rh3), что (без дополнительной конфигурации) не даёт Dynatrace:

* Трассировать вызовы от других мониторируемых приложений
* Обнаруживать [RUM](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.") (web и mobile)

Node.jsPython Чтобы трассировка вызовов от других мониторируемых приложений и обнаружение RUM работали в этом сценарии, создайте кастомный mapping-шаблон в конфигурации integration requests.

1. В консоли AWS API Gateway перейдите в **Resources** и выберите HTTP-метод (например, **GET**).
2. Выберите **Mapping Templates**, затем **Add mapping template**.
3. Добавьте в шаблон следующее содержимое:

   ```
   {



   "path": "$context.path",



   "httpMethod": "$context.httpMethod",



   "headers": {



   #foreach($param in ["x-dynatrace", "traceparent", "tracestate", "x-dtc", "referer", "host", "x-forwarded-proto", "x-forwarded-for", "x-forwarded-port"])



   "$param": "$util.escapeJavaScript($input.params().header.get($param))"



   #if($foreach.hasNext),#end



   #end    },



   "requestContext": {



   "stage": "$context.stage"



   }



   }
   ```

   Заголовок `x-dtc` специфичен для сценариев трассировки RUM, тогда как остальные заголовки в целом нужны для связывания трассировок между собой и извлечения релевантной информации, такой как метаданные веб-запроса.
4. Нажмите **Save**, чтобы сохранить вашу конфигурацию.
5. Переразверните ваш API.

### Получение токена из AWS Secrets Manager

Версия OneAgent 1.295+

Вместо явного указания токена аутентификации в конфигурации можно настроить OneAgent на получение токена, хранящегося в [AWS Secrets Manager](https://dt-url.net/r403pii).

Предварительные условия

* Убедитесь, что для ARN секрета токена аутентификации вы предоставили Lambda-функции, которую мониторит OneAgent, разрешение `secretsmanager:GetSecretValue`. Подробности см. в [Аутентификация и контроль доступа для AWS Secrets Manager](https://dt-url.net/7n03p10) в документации AWS Secrets Manager.
* Убедитесь, что значение секрета содержит только plaintext-значение токена аутентификации (без кавычек). Обратите внимание, что

  + Секреты со структурой JSON не поддерживаются. Подробности см. в [Создание секрета AWS Secrets Manager](https://dt-url.net/fy23pdx) в документации AWS Secrets Manager.
  + При получении значения секрета Secrets Manager по умолчанию возвращает только текущую версию секрета (метка `AWSCURRENT`). Подробности см. в [Что содержится в секрете Secrets Manager?](https://dt-url.net/1f43pq8) в документации AWS Secrets Manager.

Чтобы получить токен для соединения трассировки, задайте ARN секрета токена либо в переменной окружения `DT_CONNECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN`, либо в JSON-свойстве `Connection.AuthTokenSecretsManagerArn`.

Эта опция всегда переопределяет `DT_CONNECTION_AUTH_TOKEN` (`Connection.AuthToken`). Если получение не удалось, OneAgent не сможет экспортировать данные трассировки.

Получение обращается к AWS Secrets Manager только один раз, в фазе инициализации Lambda-функции; это вызывает увеличение длительности холодного старта Lambda-функции.

Layer'ы Node.js и Python используют версию AWS SDK, предоставляемую средой выполнения AWS Lambda, для доступа к секрету.

Чтобы [получить токен для сбора логов](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#aws-secrets-manager "Сбор логов из AWS Lambda-функций"), задайте отдельное получение.

### Фильтрация холодных стартов

Одна из важных метрик для Lambda: частота холодных стартов. Холодный старт случается при вызове нового инстанса Lambda-функции. Такие холодные старты занимают больше времени и добавляют задержку к вашим запросам.

Высокая частота холодных стартов может указывать на ошибки или неравномерный паттерн нагрузки, который можно сгладить с помощью provisioned concurrency. Dynatrace сообщает о таких холодных стартах как о свойстве распределённой трассировки.

Чтобы проанализировать холодные старты, выберите **View all requests** на странице деталей сервиса Lambda.

![Service details page for AWS Lambda function](https://dt-cdn.net/images/aws-lambda4-requests-936-7d63249911.png)

Service details page for AWS Lambda function

В фильтре запросов выберите **Function cold start** в разделе **Request property**.

Это отобразит страницу, которую можно отфильтровать по вызовам, содержащим **Only cold start** или **No cold start**.

![Screen to filter by invocations containing a Only cold start or No cold start](https://dt-cdn.net/images/aws-lambda6-cold-starts-1430-4ec4dd6209.png)

Screen to filter by invocations containing a Only cold start or No cold start

### Накладные расходы мониторинга

Включение мониторинга неизбежно добавляет накладные расходы на выполнение мониторируемой функции. Накладные расходы зависят от нескольких факторов, таких как технология среды выполнения функции, конфигурация и конкретные характеристики функции (например, размер кода, длительность и сложность выполнения).

Объём памяти, настроенный для функции, напрямую влияет на вычислительные ресурсы, выделенные инстансу функции. Подробнее см. [Память и вычислительная мощность](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html).

Худший сценарий по измеренным накладным расходам: функция с пустым handler'ом и минимальной конфигурацией памяти.

#### Накладные расходы на холодный старт

* Для **Python** накладные расходы на холодный старт составляют около 1 000 мс.
* Для **Node.js** накладные расходы на холодный старт составляют около 700 мс.
* Для **Java** накладные расходы на холодный старт могут превышать 1 000 мс.

Для процесса бенчмаркинга холодного старта тестировались hello-world функции (возвращающие только ответ) с выделенными 512 МБ памяти. Важно учитывать, что наблюдаемые накладные расходы могут варьироваться в зависимости от нескольких факторов:

* **Настроенная память**: Lambda-функции выделяется CPU пропорционально [настроенной памяти](https://dt-url.net/4w022aa), что может повлиять на производительность холодного старта. Функции с более высоким выделенным объёмом памяти, как правило, имеют более быстрое время инициализации благодаря увеличенному выделению CPU.
* **Реализация функции**: сложность фактической реализации функции (включая внешние зависимости, логику инициализации и среду выполнения) может существенно повлиять на длительность холодного старта.
* **Версия среды выполнения**: конкретная версия среды выполнения или используемого образа контейнера также может повлиять на время холодного старта.

При проведении оценки производительности рекомендуем учитывать эти факторы, так как они могут повлиять на результаты бенчмаркинга в реальных сценариях.

Требования к минимальной конфигурации памяти см. в [Требования для Java Lambda-функций](#lambda-java-rt-mem-limit).

#### Задержка времени отклика

Задержка зависит от реализации функции, но обычно составляет менее 10 %. Это означает, что время до получения ответа вызывающей стороной Lambda-функции может увеличиться на 10 % при добавлении OneAgent layer по сравнению со случаем, когда OneAgent не активен или отсутствует.

#### Накладные расходы по объёму кода

Следующая таблица содержит размеры layer'ов без сжатия.

| Среда выполнения | Объём кода (МБ) | Объём кода с включённым сборщиком логов (МБ) |
| --- | --- | --- |
| Node.js | ~1 МБ | ~16 МБ |
| Python | ~3 МБ | ~18 МБ |
| Java | ~5 МБ | ~20 МБ |

## Шаг 8 Интеграция Dynatrace AWS

Хотя это не обязательно, мы рекомендуем настроить интеграцию Dynatrace с Amazon CloudWatch. Это позволит данным, поступающим через AWS-интеграцию, бесшовно объединяться с данными, собранными расширением Dynatrace для AWS Lambda.

![AWS Lambda metrics Invocations](https://dt-cdn.net/images/aws-lambda3-metric-936-b279d25a8e.png)

AWS Lambda metrics Invocations

## Известные ограничения

* Расширение Dynatrace для AWS Lambda не поддерживает захват [request attributes уровня методов](/managed/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Узнайте, как создавать request attributes на основе аргументов методов Java, .NET или PHP и как использовать их на странице обзора сервиса. Также узнайте, как агрегировать захваченные значения request attributes и как обращаться к объектам, если захватываемое значение является сложным объектом.").
* Большинство расширений Dynatrace для AWS Lambda не захватывают IP-адреса исходящих HTTP-запросов. Это приводит к появлению **unmonitored hosts**, если вызываемый сервис не мониторится Dynatrace.
* Получение токена аутентификации из AWS Secrets Manager не поддерживается, если включён [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).
* **Исходящие запросы к другой AWS Lambda-функции:** в мониторируемой AWS Lambda-функции для исходящих запросов к другой AWS Lambda-функции поддерживаются следующие библиотеки:

  + Для Java: AWS SDK версии 1 для Java
  + Для Node.js: AWS SDK for JavaScript in Node.js:

    - [версия 2](https://www.npmjs.com/package/aws-sdk)
    - [версия 3](https://github.com/aws/aws-sdk-js-v3) (версия OneAgent 1.263+)
  + Для Python: AWS SDK for Python (Boto3)
* **Исходящие HTTP-запросы:** в мониторируемой AWS Lambda-функции для исходящих HTTP-запросов поддерживаются следующие библиотеки и HTTP-клиенты:

  + Для Java: Apache HTTP Client 3.x, 4.x
  + Для Node.js:

    - встроенный [`http.request`](https://nodejs.org/api/http.html#http)
    - встроенный [`fetch API`](https://nodejs.org/docs/latest/api/globals.html#fetch) (версия OneAgent 1.285+)
  + Для Python: `requests`, `aiohttp-client`, `urllib3`, `redis-py` (версия OneAgent 1.289+)
* **Дополнительные требования для входящих вызовов только для Java:**
  Чтобы корректно мониторить настроенный handler-метод

  + Настроенный handler-класс должен сам реализовывать handler-метод. Если handler-метод определён только в базовом классе, нужно добавить override в handler-классе, вызвав в нём базовый handler-метод (обычно `super.handleRequest(...)`).
  + Handler-метод должен иметь параметр `Context` ([`com.amazonaws.services.lambda.runtime.Context`](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java)).
  + Мы рекомендуем [следовать лучшей практике](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html) и наследовать ваш Lambda handler-класс от [com.amazonaws.services.lambda.runtime.RequestHandler](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/RequestHandler.java), переопределяя `handleRequest` и настраивая его как handler-метод.
    Однако, пока соблюдены предыдущие требования, OneAgent поддерживает любую валидную handler-функцию, даже если она не унаследована от этого базового интерфейса.
  + Функция должна использовать [библиотеку AWS Lambda events](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events), поскольку типы, определённые в пакете `com.amazonaws.services.lambda.runtime.events`, используются OneAgent для соответствия [типам вызовов для входящих обращений](#incoming-calls-types).
* **Сенсоры Node.js и инструментации для ES-модулей:**

  + Сенсоры (инструментации) расширения AWS Lambda для Node.js не поддерживают ECMAScript-модули. Это значит, что расширение не сможет корректно мониторить исходящие вызовы (например, HTTP- или AWS SDK-запросы).
  + Инструментации OpenTelemetry по умолчанию не поддерживают ECMAScript-модули.

    Есть способ заставить инструментации OpenTelemetry работать с ECMAScript-модулями, но он экспериментальный и имеет ряд ограничений. Подробности см. [Instrumentation for ES Modules In NodeJS (experimental)](https://dt-url.net/r10379k).
* Режим развёртывания [AWS Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) не поддерживается. Эта новая опция хостинга позволяет разворачивать Lambda-функции на управляемых AWS кластерах EC2-инстансов. Dynatrace Lambda extension и layer'ы code module в настоящее время не поддерживают этот режим развёртывания.

## Связанные темы

* [Ограничение API-вызовов к AWS с помощью тегов](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавление и настройка тегов AWS для ограничения ресурсов AWS.")