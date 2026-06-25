---
title: Трассировка Lambda-функций
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions
scraped: 2026-05-12T11:22:50.161523
---

# Трассировка Lambda-функций

# Трассировка Lambda-функций

* Практическое руководство
* Чтение: 8 мин
* Обновлено 23 апреля 2026 г.

Dynatrace предоставляет специализированный AWS Lambda layer, содержащий расширение Dynatrace для AWS Lambda. Нужно добавить публично доступный layer для вашей среды выполнения и региона к вашей функции. После этого, в зависимости от выбранного метода конфигурации, Dynatrace предоставляет шаблон или конфигурацию для вашей AWS Lambda-функции.

## Возможности

Dynatrace предоставляет широкие возможности мониторинга для Python, Node.js, Java и Go:

* Автоматическая распределённая трассировка между сервисами AWS, такими как [API Gateway](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway "Мониторинг Amazon API Gateway и просмотр доступных метрик."), [SQS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-queue-service-sqs "Мониторинг Amazon Simple Queue Service (Amazon SQS) и просмотр доступных метрик."), [SNS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-notification-service-sns "Мониторинг Amazon Simple Notification Service (Amazon SNS) и просмотр доступных метрик."), а также бесшовная интеграция с другими сервисами AWS. Подробнее см. [Интеграция AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws "Узнайте, как интегрировать Dynatrace с платформой AWS.").

* Поддержка OpenTelemetry для приёма трассировок и метрик.
* Нативный приём логов из Lambda-функций. Dynatrace поддерживает приём логов напрямую через AWS Lambda Telemetry API, что уменьшает зависимость от CloudWatch. Подробнее см. [Сбор логов AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Сбор логов из AWS Lambda-функций").
* Обнаружение и оптимизация [холодных стартов](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions#filter-cold-start "Мониторинг AWS Lambda-функций.").
* Поддержка Infrastructure-as-Code (Terraform, AWS SAM, Serverless Framework).

См. нашу [матрицу поддерживаемых технологий](/managed/ingest-from/technology-support#aws-monitor-hub "Найдите технические сведения о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") для деталей о поддерживаемых фреймворках и [средах выполнения](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) для сред выполнения, поддерживаемых AWS.

### Входящие вызовы

Для вызовов AWS Lambda Dynatrace предоставляет общую поддержку всех типов триггеров. OneAgent может зафиксировать специфичную информацию или связать трассировку с любым родителем (и тем самым добавить дополнительную информацию) только для вызовов, сделанных через:

* AWS SDK Lambda Invoke API
* API gateway
* Lambda function URL
* AWS SQS
* AWS SNS
* AWS Application Load Balancer

Для других типов вызовов OneAgent не может зафиксировать специфичную информацию или связать трассировку с родителем. Вызовы через AWS SDK требуют, чтобы клиент был инструментирован Dynatrace для связи трассировки.

## Шаги

### Включите мониторинг AWS Lambda-функций

Чтобы начать

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **AWS Lambda**.

3. Следуйте инструкциям, чтобы включить мониторинг AWS Lambda-функций.

#### Выберите метод конфигурации

Dynatrace OneAgent поставляется в виде Lambda layer, который можно включить и настроить вручную или через известные решения Infrastructure as Code (IaC).
Lambda layer хранится в AWS-аккаунте Dynatrace `585768157899`.

Мастер предоставляет различные варианты конфигурации и сниппеты, которые вы можете использовать в вашем процессе автоматизации развёртывания.

Configure with JSON file

Если вы выберете этот метод, Dynatrace предоставит вам:

* Переменную окружения, которую нужно добавить к вашей AWS Lambda-функции
* JSON-сниппет, который нужно скопировать в файл `dtconfig.json` в корневой папке развёртывания Lambda
* Lambda layer ARN

При использовании этого метода убедитесь, что Lambda layer Dynatrace добавлен к вашей функции. Это можно сделать через консоль AWS (**Add layer** > **Specify an ARN** и вставить ARN, отображённый на странице развёртывания), либо с помощью автоматизированного решения по вашему выбору.

**Введите переменные окружения через консоль AWS**

![Lambda environment variables cropped](https://dt-cdn.net/images/lambda-environment-variables-cropped-776-af551d0520.png)

Lambda environment variables cropped

**Введите Lambda layer ARN через консоль AWS**

![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Specify a layer by providing the ARN

Configure with environment variables

Переменные окружения можно использовать для конфигурации, однако мы рекомендуем использовать Secrets Manager как предпочтительный способ получения токена безопасности. Подробнее см. [Получение токена из AWS Secrets Manager](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions#aws-secrets-manager "Мониторинг AWS Lambda-функций.").

При использовании этого метода убедитесь, что Lambda layer Dynatrace добавлен к вашей функции. Layer, как и переменные окружения, можно задать вручную через консоль AWS (**Add layer** > **Specify an ARN** и вставить ARN, отображённый на странице развёртывания), либо через автоматизированное решение по вашему выбору.

[Расшифровка переменных окружения на стороне клиента (Security in Transit)](https://dt-url.net/tz234sd) не поддерживается.

Если вы выберете этот метод, Dynatrace предоставит вам:

* Значения для определения переменных окружения AWS Lambda-функций, которые вы хотите мониторить

  ![AWS Lambda environment variables](https://dt-cdn.net/images/lambda-env-variables-updated-1614-488fcb4f1c.png)

  AWS Lambda environment variables
* Lambda layer ARN

  ![Specify a layer by providing the ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

  Specify a layer by providing the ARN

Configure and deploy using Terraform

Terraform: популярное решение Infrastructure as Code (IaC). Если вы выберете этот метод, Dynatrace предоставит вам:

* Шаблон для определения AWS Lambda-функции. В него включена вся конфигурация, необходимая для развёртывания и настройки расширения Dynatrace AWS Lambda вместе с вашими функциями.
* Lambda layer ARN

Configure and deploy using AWS SAM

AWS Serverless Application Model (SAM): open-source-фреймворк для построения бессерверных приложений.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения AWS Lambda-функции. В него включена вся конфигурация, необходимая для интеграции расширения Dynatrace AWS Lambda.

Configure and deploy using the serverless framework

Опция Serverless Application: фреймворк для развёртывания бессерверных стеков.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения AWS Lambda-функции. В него включена вся конфигурация, необходимая для интеграции расширения Dynatrace AWS Lambda.

Configure and deploy using AWS CloudFormation

AWS CloudFormation: IaC-решение, позволяющее провижинить широкий спектр сервисов AWS.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения AWS Lambda-функции. В него включена вся конфигурация, необходимая для интеграции расширения Dynatrace AWS Lambda.

#### Укажите конечную точку API Dynatrace

Обязательно

Укажите публичную конечную точку API Dynatrace, в которую будут отправляться данные мониторинга.

Это должен быть URL на основе ActiveGate с идентификатором среды (например, `https://<public-active-gate>:9999/e/<environment-id>`).

Типичный сценарий: разворачивать Dynatrace ActiveGate в непосредственной близости (в том же регионе), что и Lambda-функции, которые вы хотите мониторить, чтобы уменьшить сетевую задержку. Сетевая задержка может влиять на время выполнения и холодного старта ваших Lambda-функций при (обычно одном) сетевом запросе OneAgent на каждый вызов Lambda (этот запрос происходит в конце вызова). Типичные значения накладных расходов см. в разделе <#monitoring-overhead>.

### Включите Real User Monitoring

Необязательно

Это необязательный шаг для использования Real User Monitoring (RUM), который даёт глубокое понимание действий пользователей и производительности через браузер или мобильные приложения.

#### Настройте AWS API Gateway

* Если входящие (не-XHR) запросы к вашим Lambda-функциям не связаны с вызывающим приложением, настройте API Gateway для проброса тега Dynatrace. Для этого включите **Use Lambda Proxy Integration** на странице конфигурации **Integration Request** в API Gateway.
* Если API Gateway настраивается со страницы конфигурации Lambda, эта настройка будет включена по умолчанию. Подробнее см. [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).

AWS Lambda также поддерживает [**non-proxy integration**](https://dt-url.net/8u03rh3), которая (без дополнительной конфигурации) не позволяет Dynatrace

* Трассировать вызовы из других мониторируемых приложений
* Обнаруживать [RUM](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и т. д.") (веб и мобильные)

Чтобы трассировка вызовов из других мониторируемых приложений и обнаружение RUM работали в таком сценарии, создайте кастомный mapping template в конфигурации integration requests.

1. В AWS API Gateway Console перейдите в **Resources** и выберите метод запроса (например, **GET**).
2. Выберите **Mapping Templates** и затем **Add mapping template**.
3. Добавьте следующее содержимое в шаблон:

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

   Заголовок `x-dtc` специфичен для сценариев трассировки RUM, тогда как остальные заголовки обычно нужны, чтобы связать трассировки и извлечь релевантную информацию, например метаданные веб-запроса.
4. Выберите **Save**, чтобы сохранить конфигурацию.
5. Передеплойте ваш API.

#### Настройте AWS

Убедитесь, что заголовок `x-dtc` разрешён в настройках CORS ваших мониторируемых Lambda-функций.

RUM для Lambda-функций требует, чтобы специальный заголовок (`x-dtc`) отправлялся с XHR-вызовами к AWS. Чтобы это включить, настройки CORS вашего развёртывания AWS должны разрешать заголовок `x-dtc` в preflight-запросах (`OPTIONS`). Чтобы настроить CORS и разрешить заголовок `x-dtc` для вашей конкретной конфигурации, см. [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

#### Настройте Dynatrace

Чтобы настроить заголовок `x-dtc` для вызовов к вашим Lambda-функциям

1. Перейдите в **Web**, **Mobile**, **Frontend** или **Custom Applications**, в зависимости от типа вашего приложения.
2. Выберите приложение, которое хотите связать с вашей Lambda-функцией.
3. Выберите меню браузера (**â¦**) в правом верхнем углу и выберите **Edit**.
4. Выберите **Capturing** > **Async web requests and SPAs**.
5. Убедитесь, что выбранный фреймворк включён. Если ваш фреймворк отсутствует в списке, включите **Capture XmlHttpRequest (XHR)** для общей поддержки `XHR`.
6. Выберите **Capturing** > **Advanced setup**.
7. Прокрутите до раздела **Enable Real User Monitoring for cross-origin XHR calls** и введите шаблон, соответствующий URL ваших Lambda-функций. Например: `TheAwsUniqueId.execute-api.us-east-1.amazonaws.com`
8. Выберите **Save**. Через несколько минут заголовок будет добавлен ко всем вызовам вашей Lambda-функции, а запросы из браузера будут связаны с бэкендом.

Failed requests

Если после включения этой опции запросы начинают завершаться с ошибкой, проверьте настройки CORS. Чтобы узнать, как настроить CORS, см. [Включение CORS для ресурса через консоль API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

### Развёртывание

Скопируйте конфигурационные сниппеты в ваше развёртывание и используйте предпочитаемый метод развёртывания, чтобы включить layer и задать конфигурацию для ваших Lambda-функций.

### Параметры конфигурации

#### Получение токена из AWS Secrets Manager

OneAgent версии 1.295+

Вместо явного указания токена аутентификации в конфигурации можно настроить OneAgent на получение токена, хранящегося в [AWS Secrets Manager](https://dt-url.net/r403pii).

Предварительные условия

* Убедитесь, что вы выдали разрешение `secretsmanager:GetSecretValue` для ARN секрета токена аутентификации Lambda-функции, мониторируемой OneAgent. Подробнее см. [Аутентификация и контроль доступа для AWS Secrets Manager](https://dt-url.net/7n03p10) в документации AWS Secrets Manager.
* Убедитесь, что значение секрета содержит только текстовый токен аутентификации (без кавычек). Обратите внимание:

  + Секреты со структурой JSON не поддерживаются. Подробнее см. [Создание секрета AWS Secrets Manager](https://dt-url.net/fy23pdx) в документации AWS Secrets Manager.
  + При получении значения секрета Secrets Manager по умолчанию возвращает только текущую версию секрета (метка `AWSCURRENT`). Подробнее см. [Что содержится в секрете Secrets Manager?](https://dt-url.net/1f43pq8) в документации AWS Secrets Manager.

Чтобы получить токен для трассировочного соединения, задайте ARN секрета токена либо в переменной окружения `DT_CONNECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN`, либо в JSON-свойстве `Connection.AuthTokenSecretsManagerArn`.

Эта опция всегда переопределяет `DT_CONNECTION_AUTH_TOKEN` (`Connection.AuthToken`). Если получение завершается с ошибкой, OneAgent не сможет экспортировать данные трассировки.

Получение обращается к AWS Secrets Manager только один раз, во время фазы инициализации Lambda-функции; это увеличивает длительность холодного старта Lambda-функции.

Подробнее о получении токена для сбора логов см. [Получение токена из AWS Secrets Manager](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#aws-secrets-manager "Сбор логов из AWS Lambda-функций").

## Накладные расходы на мониторинг

Включение мониторинга неизбежно создаёт накладные расходы для выполнения мониторируемой функции. Накладные расходы зависят от нескольких факторов, таких как технология среды выполнения функции, её конфигурация и конкретные характеристики функции, например размер кода или длительность и сложность выполнения.

Объём памяти, настроенный для функции, напрямую влияет на вычислительные ресурсы, выделенные инстансу функции. Подробнее см. [Память и вычислительная мощность](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html).

Наихудший сценарий измеренных накладных расходов: функция с пустым handler и минимальной настройкой памяти.

### Накладные расходы холодного старта

* Для **Node.js** накладные расходы холодного старта составляют около 900 мс.
* Для **Java** накладные расходы холодного старта составляют около 1 500 мс.
* Для **Python** накладные расходы холодного старта составляют около 1 000 мс.
* Для **Go** накладные расходы холодного старта составляют около 600 мс.

Для процесса бенчмаркинга холодного старта тестировались hello-world-функции (только возвращающие ответ) с выделенной памятью 512 МБ. Важно отметить, что наблюдаемые накладные расходы могут варьироваться в зависимости от нескольких факторов:

* **Настроенная память**: Lambda-функции выделяется CPU пропорционально [настроенной памяти](https://dt-url.net/4w022aa), что может влиять на производительность холодного старта. Функции с большей выделенной памятью обычно демонстрируют более быструю инициализацию благодаря увеличенному выделению CPU.
* **Реализация функции**: сложность реальной реализации функции, включая внешние зависимости, логику инициализации и среду выполнения, может существенно влиять на длительность холодного старта.
* **Версия среды выполнения**: конкретная версия среды выполнения или образа контейнера также может влиять на время холодного старта.

При оценке производительности рекомендуем учитывать эти факторы, поскольку они могут влиять на результаты бенчмаркинга в реальных сценариях.

### Задержка времени ответа

Задержка зависит от реализации функции, но обычно составляет менее 10 %. Это значит, что время до получения ответа вызывающей стороной Lambda-функции может увеличиться на 10 % при добавлении OneAgent layer, по сравнению с ситуацией, когда OneAgent не активен или отсутствует.

### Затраты на размер кода

В таблице ниже указаны несжатые размеры layer.

| Среда выполнения | Размер кода | Размер кода с включённым сборщиком логов |
| --- | --- | --- |
| Node.js | ~23 МБ | ~32 МБ |
| Java | ~25 МБ | ~32 МБ |
| Python | ~16 МБ | ~24 МБ |
| Go | ~25 МБ | ~28 МБ |

## Интеграция AWS с Dynatrace

Хотя это не обязательно, мы рекомендуем настроить интеграцию Dynatrace с Amazon CloudWatch. Это позволяет бесшовно объединять данные, поступающие через интеграцию AWS, с данными, собранными расширением Dynatrace AWS Lambda.

Подробнее см. [Amazon CloudWatch Metric Streams](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/cloudwatch-metric-streams "Приём метрик из ваших AWS-аккаунтов с помощью Amazon CloudWatch Metric Streams.").

## Фильтрация холодных стартов

Одна из важных метрик для Lambda: частота холодных стартов. Холодный старт происходит при вызове нового инстанса Lambda-функции. Такие холодные старты длятся дольше и добавляют задержку к вашим запросам.

Высокая частота холодных стартов может указывать на ошибки или неравномерный паттерн нагрузки, который можно смягчить с помощью provisioned concurrency. Dynatrace сообщает о таких холодных стартах как о свойстве распределённой трассировки.

Чтобы проанализировать холодные старты

1. Выберите **View all requests** на странице с подробной информацией о сервисе Lambda.

2. В фильтре запросов выберите **Function cold start** в разделе **Request property**.

3. Отфильтруйте по вызовам, содержащим **Only cold start** или **No cold start**.

## Известные ограничения

### Общие ограничения

* Таймауты HTTP-подключения, таймауты flush и пороги backoff не настраиваются.
* OneAgent, работающий на AWS Lambda, не поддерживает функциональность, требующую переконфигурации OneAgent через серверный пользовательский интерфейс.
* OneAgent для AWS Lambda использует только локальные настройки, заданные через переменные окружения или конфигурационные файлы, вместо подтягивания конфигурации из кластера Dynatrace. В результате любые настройки, заданные на уровне кластера, игнорируются, и применяются значения по умолчанию, если не переопределены явно.
* Большинство расширений Dynatrace AWS Lambda не фиксируют IP-адреса исходящих HTTP-запросов. Это приводит к **unmonitored hosts**, если вызываемый сервис не мониторится через Dynatrace.
* Режим развёртывания [AWS Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) не поддерживается. Эта новая опция хостинга позволяет разворачивать Lambda-функции на управляемых AWS EC2-кластерах. Расширение Dynatrace Lambda и слои code module в настоящее время не поддерживают этот режим развёртывания.

### Ограничения .NET

* .NET: ASP.NET core, оценка атак и уязвимостей на уровне кода, а также ряд метрик не поддерживаются в AWS Lambda.

### Ограничения Node.js

* Поддержка трассировки `aws-sdk` доступна только для CommonJS. В развёртываниях ECMAScript Lambda трассировка AWS-SDK будет недоступна.
* Необходимо включить мониторинг для ESM Lambda-функций. Эта функция в настоящее время `opt-in`. Чтобы включить поддержку ESM для входящих вызовов AWS Lambda, задайте переменной окружения `DT_ENABLE_ESM_LOADERS` значение `true`. Включение поддержки ESM увеличивает потребление памяти.
* Node.js handler'ы из бандлеров (например, [esbuild](https://esbuild.github.io/) или [vite](https://vite.dev/)) могут быть невидимы для OneAgent из-за изменённой структуры экспорта в процессе бандлинга.

  Как включить авто-инструментирование для Node.js handler'ов, собранных через бандлер

  Можно использовать простой wrapper-скрипт для включения авто-инструментирования.

  Вот пример AWS Lambda handler, написанного на TypeScript (`index.ts`):

  ```
  import { Context, APIGatewayProxyResult, APIGatewayEvent } from 'aws-lambda';



  export const handler = async (event: APIGatewayEvent, context: Context): Promise<APIGatewayProxyResult> => {



  console.log(`Event: ${JSON.stringify(event, null, 2)}`);



  console.log(`Context: ${JSON.stringify(context, null, 2)}`);



  return {



  statusCode: 200,



  body: JSON.stringify({



  message: 'hello world',



  }),



  };



  };
  ```

  1. Соберите код функции бандлером по вашему выбору.
  2. Если в результате получается код, который не может быть автоматически инструментирован OneAgent, создайте wrapper-файл (например, `handler_wrap.mjs`), чтобы экспортировать handler в форме, доступной для инструментирования OneAgent.

     Для развёртываний ESM Lambda:

     ```
     // handler_wrap.mjs



     export { handler } from "./index.mjs";
     ```

     Для развёртываний CommonJS Lambda:

     ```
     const bundleDist = require("./dist/index");



     exports.handler = bundleDist.handler;
     ```
  3. В конфигурации среды выполнения AWS Lambda задайте handler как `handler_wrap.handler`.

  Теперь OneAgent сможет корректно обнаруживать и инструментировать функцию.
  Использование бандлера вносит дополнительные ограничения на видимость зависимостей. Подробнее см. [Известные ограничения OneAgent Node.js](/managed/ingest-from/technology-support/application-software/nodejs#limitations "Прочтите о поддержке приложений Node.js в Dynatrace.").

### Ограничения Go

#### Общие ограничения:

* Go-приложения для AWS Lambda должны собираться с включённой динамической компоновкой. Чтобы включить динамическую компоновку, задайте `CGO_ENABLED=1` и используйте системный линкер.

  Пример

  ```
  CGO_ENABLED=1



  go build -ldflags '-linkmode=external' -o myapp main.go
  ```
* Go-приложения не требуют специальной среды выполнения. Используется среда выполнения OS-only. Среда выполнения `Go 1.x` объявлена устаревшей и не поддерживается.

#### Ограничения по версиям

* Поддержка Go для AWS Lambda требует OneAgent версии 1.333+. Она не обратно-совместима со старыми версиями OneAgent.
* Поддержка [внешних метаданных](/managed/ingest-from/technology-support/application-software/go/support/supported-go-versions#external-metadata "Узнайте, какие версии Go поддерживаются Dynatrace.") для Go в AWS Lambda не поддерживается. В результате новые версии сторонних библиотек или недавно выпущенные версии Go не поддерживаются автоматически. Поддержка новых версий поставляется в обычном цикле релизов OneAgent и требует обновления OneAgent, чтобы вступить в силу.
* Для Go-приложений требуется [AWS-Lambda-Go](https://github.com/aws/aws-lambda-go) SDK версии 1.18.0+.

#### Ограничения развёртывания

* Развёртывание возможно через образ контейнера или ZIP-файл. В обоих случаях должна быть включена динамическая компоновка.

  Архив ZIP

  Архив должен содержать бинарник, а приложение должно быть скомпоновано с glibc v2.34 или старее. Поскольку статически скомпонованные приложения не поддерживаются, компоновка с такой старой версией glibc требует сборки в Ubuntu 20.04 или более ранней.

  Образ контейнера

  Приложение должно быть скомпилировано с совместимой версией glibc. Поддерживаются как базовые образы AWS, так и не-AWS базовые образы.
* Чтобы задать путь к библиотеке OneAgent, используйте переменную окружения `LD_PRELOAD`.

  ```
  LD_PRELOAD=/opt/dynatrace_layer/agent/lib64/liboneagentproc.so
  ```

### Ограничения Dynatrace Managed

* Managed offline clusters не поддерживаются.