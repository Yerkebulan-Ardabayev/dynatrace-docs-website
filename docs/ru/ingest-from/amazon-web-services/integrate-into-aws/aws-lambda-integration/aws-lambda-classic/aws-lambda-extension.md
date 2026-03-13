---
title: Трассировка Lambda-функций на Python, Node.js и Java
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension
scraped: 2026-03-05T21:29:41.920596
---

# Трассировка Lambda-функций на Python, Node.js и Java

# Трассировка Lambda-функций на Python, Node.js и Java

* Classic
* Практическое руководство
* Время чтения: 14 мин
* Обновлено 23 января 2026

Эта страница относится к классической интеграции AWS Lambda. Для последней версии см. [Трассировка Lambda-функций](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Мониторинг функций AWS Lambda.").

Dynatrace предоставляет вам специальный слой AWS Lambda, содержащий расширение Dynatrace для AWS Lambda. Вам необходимо добавить общедоступный слой для вашей среды выполнения и региона к вашей функции. Затем, в зависимости от метода конфигурации, Dynatrace предоставит шаблон или конфигурацию для вашей функции AWS Lambda.

## Входящие вызовы

Dynatrace может мониторить входящие вызовы, только если они инициированы через:

* AWS SDK Lambda Invoke API
* API gateway
* Lambda function URL
* AWS SQS
* AWS SNS

Для других типов вызовов OneAgent не может захватить специфическую информацию или связать трассировку с родительским элементом. Вызовы через AWS SDK требуют, чтобы клиент был инструментирован Dynatrace для связывания трассировки.

## Предварительные требования

* Поддерживаемая [среда выполнения](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "Возможности AWS Lambda и варианты интеграции") AWS Lambda. Расширение Dynatrace поддерживает функции AWS Lambda, написанные на **Node.js**, **Python** или **Java**.
  Поддерживаются архитектуры **64-битная ARM** ([процессоры AWS Graviton2](https://aws.amazon.com/ec2/graviton/)) и **64-битная x86**.
* Java Необходимо выполнить следующие требования к оперативной памяти:

  + Если [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) включен и версия OneAgent 1.267+, объем памяти должен быть установлен минимум на 512 МБ.
  + Если [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) не включен и версия OneAgent 1.265 или ранее, объем памяти должен быть установлен минимум на 1 500 МБ.
    Для настройки памяти в консоли AWS Lambda перейдите в **General** > **Basic settings** и установите **Memory**.

  Новая конфигурация объема памяти влияет на количество виртуальных процессоров, доступных функции; подробнее об этом см. в разделе [Накладные расходы мониторинга](#monitoring-overhead) ниже.

  + Обратите внимание, что требования к оперативной памяти для Lambda-функций на Node.js и Python могут быть значительно ниже. Вычислительная мощность в AWS Lambda масштабируется вместе с выделенной памятью, и при низких настройках памяти время выполнения функции значительно увеличивается.
* Активируйте функцию OneAgent **Forward Tag 4 trace context extension**. Перейдите в **Settings** > **Preferences** > **OneAgent features**.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Включение AWS Lambda**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#activate-aws-lambda "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Выбор метода конфигурации**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 3 (необязательно)](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Шаг 3 (необязательно)")

**Указание конечной точки API Dynatrace**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-endpoint "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 4 (необязательно)](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4 (необязательно)")

**Включение мониторинга реальных пользователей**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

**Определение имени слоя AWS**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-layer "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 6 (необязательно)](https://dt-cdn.net/images/dotted-step-6-fbd29ea893.svg "Шаг 6 (необязательно)")

**Развертывание**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#deployment "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

**Параметры конфигурации**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#config-options "Мониторинг Lambda-функций на Python, Node.js и Java.")[![Шаг 8](https://dt-cdn.net/images/step-8-72c2162189.svg "Шаг 8")

**Интеграция Dynatrace с AWS**](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#aws-integration "Мониторинг Lambda-функций на Python, Node.js и Java.")

## Шаг 1: Включение AWS Lambda

Для начала

1. В Dynatrace Hub выберите **AWS Lambda**.
2. Выберите **Set up**.

3. Следуйте инструкциям для включения мониторинга функций AWS Lambda.

## Шаг 2: Выбор метода конфигурации

Dynatrace OneAgent распространяется в виде Lambda-слоя, который можно включить и настроить вручную или с помощью известных решений Infrastructure as Code (IaC).
Lambda-слой хранится в учетной записи Dynatrace AWS `725887861453`.

На странице **Enable Monitoring for AWS Lambda Functions** используйте список **How will you configure your AWS Lambda functions?**, чтобы выбрать предпочтительный метод, а затем убедитесь, что вы установили все свойства для выбранного метода перед копированием сгенерированных фрагментов конфигурации.

Конфигурация с помощью JSON-файла

Если вы выберете этот метод, Dynatrace предоставит вам:

* Переменную окружения для добавления к вашей функции AWS Lambda
* JSON-фрагмент, который необходимо скопировать в файл `dtconfig.json` в корневую папку вашего развертывания Lambda
* ARN Lambda-слоя

При использовании этого метода убедитесь, что вы добавили Lambda-слой Dynatrace к вашей функции. Вы можете сделать это через консоль AWS (**Add layer** > **Specify an ARN** и вставьте ARN, отображенный на странице развертывания) или используя автоматизированное решение по вашему выбору.

**Ввод переменных окружения через консоль AWS**

![Переменные окружения Lambda (обрезано)](https://dt-cdn.net/images/lambda-environment-variables-cropped-776-af551d0520.png)

**Ввод ARN Lambda-слоя через консоль AWS**

![Указание слоя путем предоставления ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Конфигурация с помощью переменных окружения

При использовании этого метода убедитесь, что вы добавили Lambda-слой Dynatrace к вашей функции. Слой, а также переменные окружения можно установить вручную через консоль AWS (**Add layer** > **Specify an ARN** и вставьте ARN, отображенный на странице развертывания) или используя автоматизированное решение по вашему выбору.

[Клиентское дешифрование переменных окружения (Security in Transit)](https://dt-url.net/tz234sd) не поддерживается.

Если вы выберете этот метод, Dynatrace предоставит вам:

* Значения для определения переменных окружения для функций AWS Lambda, которые вы хотите мониторить

  ![Переменные окружения Lambda](https://dt-cdn.net/images/lambda-env-variables-1614-77850f4051.png)
* ARN Lambda-слоя

  ![Указание слоя путем предоставления ARN](https://dt-cdn.net/images/lambda-add-layer-822-ab8535b8d9.jpg)

Конфигурация и развертывание с помощью Terraform

Terraform -- это популярное решение Infrastructure as Code (IaC). Если вы выберете этот метод, Dynatrace предоставит вам:

* Шаблон для определения функции AWS Lambda. Он включает всю конфигурацию, необходимую для развертывания и настройки расширения Dynatrace AWS Lambda вместе с вашими функциями.
* ARN Lambda-слоя

Конфигурация и развертывание с помощью AWS SAM

AWS Serverless Application Model (SAM) -- это фреймворк с открытым исходным кодом для создания бессерверных приложений.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения функции AWS Lambda. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace AWS Lambda.

Конфигурация и развертывание с помощью serverless framework

Serverless Application -- это фреймворк для развертывания бессерверных стеков.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения функции AWS Lambda. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace AWS Lambda.

Конфигурация и развертывание с помощью AWS CloudFormation

AWS CloudFormation -- это IaC-решение, позволяющее провизировать широкий спектр сервисов AWS.

Если вы выберете этот метод, Dynatrace предоставит вам шаблон для определения функции AWS Lambda. Он включает всю конфигурацию, необходимую для интеграции расширения Dynatrace AWS Lambda.

## Шаг 3 (необязательно): Указание конечной точки API Dynatrace

Это необязательный шаг, позволяющий указать конечную точку API Dynatrace, на которую будут отправляться данные мониторинга.

Типичный сценарий -- развернуть Dynatrace ActiveGate в непосредственной близости (в том же регионе) от Lambda-функций, которые вы хотите мониторить, чтобы снизить сетевую задержку, которая может повлиять на время выполнения и холодного старта ваших Lambda-функций для, как правило, одного сетевого запроса OneAgent за вызов Lambda (который происходит в конце вызова). Типичные показатели накладных расходов см. в разделе [Накладные расходы мониторинга](#monitoring-overhead).

## Шаг 4 (необязательно): Включение мониторинга реальных пользователей

Это необязательный шаг для использования мониторинга реальных пользователей (RUM), который предоставляет глубокие данные о действиях и производительности пользователей через браузер или мобильные приложения.

### Настройка AWS

* Убедитесь, что заголовок `x-dtc` разрешен в настройках CORS ваших мониторируемых Lambda-функций.

  RUM для Lambda-функций требует отправки специфического заголовка (`x-dtc`) с XHR-вызовами к AWS. Для его включения настройки CORS вашего развертывания AWS должны разрешать заголовок `x-dtc` во время предварительных (`OPTIONS`) запросов. Для настройки CORS и разрешения заголовка `x-dtc` для вашей конкретной конфигурации см. [Включение CORS для ресурса с помощью консоли API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

### Настройка Dynatrace

Для настройки заголовка `x-dtc` для вызовов ваших Lambda-функций

1. Перейдите в **Web**, **Mobile**, **Frontend** или **Custom Applications** в зависимости от типа вашего приложения.
2. Выберите приложение, которое вы хотите связать с вашей Lambda-функцией.
3. Выберите меню навигации (**...**) в правом верхнем углу и выберите **Edit**.
4. Выберите **Capturing** > **Async web requests and SPAs**.
5. Убедитесь, что ваш фреймворк включен. Если ваш фреймворк отсутствует в списке, включите **Capture XmlHttpRequest (XHR)** для общей поддержки `XHR`.
6. Выберите **Capturing** > **Advanced setup**.
7. Прокрутите вниз до раздела **Enable Real User Monitoring for cross-origin XHR calls** и введите шаблон, соответствующий URL ваших Lambda-функций. Пример: `TheAwsUniqueId.execute-api.us-east-1.amazonaws.com`
8. Выберите **Save**. Через несколько минут заголовок будет прикреплен ко всем вызовам вашей Lambda-функции, и запросы из вашего браузера будут связаны с бэкендом.

Неудачные запросы

Если запросы начинают завершаться с ошибкой после включения этой опции, проверьте настройки CORS. Для настройки CORS см. [Включение CORS для ресурса с помощью консоли API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html) в документации AWS.

![Поток сервисов для функции AWS Lambda](https://dt-cdn.net/images/aws-lambda1-service-flow-1430-f09d3a9ebe.png)

## Шаг 5: Определение имени слоя AWS

Выберите регион AWS и среду выполнения Lambda-функции, которую необходимо мониторить. Эти настройки необходимы для предоставления правильного ARN слоя.

## Шаг 6: Развертывание

Скопируйте фрагменты конфигурации в ваше развертывание и используйте выбранный метод развертывания для включения слоя и установки конфигурации для ваших Lambda-функций.

## Шаг 7: Параметры конфигурации

### Настройка AWS API Gateway

* Если входящие (не-XHR) запросы к вашим Lambda-функциям не связаны с вызывающим приложением, настройте API Gateway для передачи тега Dynatrace. Для этого включите **Use Lambda Proxy Integration** на странице конфигурации **Integration Request** API Gateway.
* Если API Gateway настроен со страницы конфигурации Lambda, эта настройка будет включена по умолчанию. Для получения дополнительной информации см. [Включение CORS для ресурса с помощью консоли API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors-console.html).

AWS Lambda также поддерживает [**непроксированную интеграцию**](https://dt-url.net/8u03rh3), которая -- без дополнительной конфигурации -- не позволяет Dynatrace

* Трассировать вызовы из других мониторируемых приложений
* Обнаруживать [RUM](/docs/observe/digital-experience/rum-concepts/rum-overview "Узнайте о мониторинге реальных пользователей, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.") (веб и мобильные)

Node.js Python Для работы трассировки вызовов из других мониторируемых приложений / обнаружения RUM в этом сценарии создайте пользовательский шаблон сопоставления в конфигурации запросов интеграции.

1. В консоли AWS API Gateway перейдите в **Resources** и выберите метод запроса (например, **GET**).
2. Выберите **Mapping Templates**, затем выберите **Add mapping template**.
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

   Заголовок `x-dtc` специфичен для сценариев трассировки RUM, тогда как остальные заголовки обычно необходимы для связывания трассировок и извлечения релевантной информации, такой как метаданные веб-запросов.
4. Выберите **Save** для сохранения конфигурации.
5. Повторно разверните ваш API.

### Получение токена из AWS Secrets Manager

OneAgent версии 1.295+

Вместо явного указания токена аутентификации в конфигурации вы можете настроить OneAgent для получения токена, хранящегося в [AWS Secrets Manager](https://dt-url.net/r403pii).

Предварительные требования

* Убедитесь, что вы предоставили разрешение `secretsmanager:GetSecretValue` для ARN секрета токена аутентификации Lambda-функции, мониторируемой OneAgent. Подробности см. в [Аутентификация и управление доступом для AWS Secrets Manager](https://dt-url.net/7n03p10) в документации AWS Secrets Manager.
* Убедитесь, что значение секрета содержит только текстовое значение токена аутентификации (без кавычек). Обратите внимание, что

  + Секреты со структурой JSON не поддерживаются. Подробности см. в [Создание секрета AWS Secrets Manager](https://dt-url.net/fy23pdx) в документации AWS Secrets Manager.
  + При получении значения секрета Secrets Manager по умолчанию возвращает только текущую версию секрета (метка `AWSCURRENT`). Подробности см. в [Что содержится в секрете Secrets Manager?](https://dt-url.net/1f43pq8) в документации AWS Secrets Manager.

Для получения токена для трассировочного подключения установите ARN секрета токена в переменную окружения `DT_CONNECTION_AUTH_TOKEN_SECRETS_MANAGER_ARN` или в JSON-свойство `Connection.AuthTokenSecretsManagerArn`.

Эта опция всегда переопределяет `DT_CONNECTION_AUTH_TOKEN` (`Connection.AuthToken`). Если получение не удастся, OneAgent не сможет экспортировать данные трассировки.

Получение обращается к AWS Secrets Manager только один раз, во время фазы инициализации Lambda-функции; это вызывает увеличение длительности холодного старта Lambda-функции.

Слои Node.js и Python используют версию AWS SDK, предоставляемую средой выполнения AWS Lambda, для доступа к секрету.

Для [получения токена для сбора логов](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#aws-secrets-manager "Сбор логов из функций AWS Lambda") настройте другое получение.

### Фильтрация холодных стартов

Одна из важных метрик для Lambda -- частота холодных стартов. Холодный старт происходит при вызове нового экземпляра Lambda-функции. Такие холодные старты занимают больше времени и добавляют задержку к вашим запросам.

Высокая частота холодных стартов может указывать на ошибки или неравномерный паттерн нагрузки, который можно смягчить с помощью provisioned concurrency. Dynatrace сообщает о таких холодных стартах как свойство распределенной трассировки.

Для анализа холодных стартов выберите **View all requests** на странице деталей сервиса Lambda.

![Страница деталей сервиса для функции AWS Lambda](https://dt-cdn.net/images/aws-lambda4-requests-936-7d63249911.png)

В фильтре запросов выберите **Function cold start** в разделе **Request property**.

Отображается страница, которую можно фильтровать по вызовам, содержащим **Only cold start** или **No cold start**.

![Экран фильтрации по вызовам, содержащим Only cold start или No cold start](https://dt-cdn.net/images/aws-lambda6-cold-starts-1430-4ec4dd6209.png)

### Накладные расходы мониторинга

Включение мониторинга неизбежно вызывает накладные расходы при выполнении мониторируемой функции. Накладные расходы зависят от нескольких факторов, таких как технология среды выполнения функции, конфигурация и конкретные характеристики функции, такие как размер кода или длительность и сложность выполнения.

Объем памяти, настроенный для функции, напрямую влияет на вычислительные ресурсы, назначенные экземпляру функции. Подробности см. в [Память и вычислительная мощность](https://docs.aws.amazon.com/lambda/latest/operatorguide/computing-power.html).

Наихудший сценарий измеренных накладных расходов -- функция с пустым обработчиком и минимальной конфигурацией памяти.

#### Накладные расходы холодного старта

* Для **Python** накладные расходы холодного старта составляют около 1 000 мс.
* Для **Node.js** накладные расходы холодного старта составляют около 700 мс.
* Для **Java** накладные расходы холодного старта могут превышать 1 000 мс.

Для процесса бенчмаркинга холодного старта функции hello-world (возвращающие только ответ) были протестированы с выделенной памятью 512 МБ. Важно отметить, что наблюдаемые накладные расходы могут варьироваться в зависимости от нескольких факторов:

* **Настроенная память**: Lambda-функции выделяется CPU пропорционально [настроенной памяти](https://dt-url.net/4w022aa), что может влиять на производительность холодного старта. Функции с большим объемом выделенной памяти обычно демонстрируют более быстрое время инициализации из-за увеличенного выделения CPU.
* **Реализация функции**: сложность фактической реализации функции, включая внешние зависимости, логику инициализации и среду выполнения, может существенно влиять на длительность холодного старта.
* **Версия среды выполнения**: конкретная версия среды выполнения или образ контейнера также могут влиять на время холодного старта.

При проведении оценки производительности мы рекомендуем учитывать эти факторы, поскольку они могут повлиять на результаты бенчмаркинга в реальных сценариях.

Минимальные требования к памяти см. в разделе [Требования для Java Lambda-функций](#lambda-java-rt-mem-limit).

#### Задержка времени ответа

Задержка зависит от реализации функции, но обычно составляет менее 10%. Это означает, что время до получения вызывающей стороной ответа Lambda-функции может увеличиться на 10% при добавлении слоя OneAgent по сравнению с ситуацией, когда OneAgent неактивен/отсутствует.

#### Накладные расходы на кодовое пространство

В следующей таблице указаны размеры несжатых слоев.

| Среда выполнения | Кодовое пространство (МБ) | Кодовое пространство с включенным сборщиком логов (МБ) |
| --- | --- | --- |
| Node.js | ~1 МБ | ~16 МБ |
| Python | ~3 МБ | ~18 МБ |
| Java | ~5 МБ | ~20 МБ |

## Шаг 8: Интеграция Dynatrace с AWS

Хотя это не обязательно, мы рекомендуем настроить интеграцию Dynatrace с Amazon CloudWatch. Это позволяет бесшовно объединять данные, полученные через интеграцию AWS, с данными, собранными расширением Dynatrace AWS Lambda.

![Метрики AWS Lambda: вызовы](https://dt-cdn.net/images/aws-lambda3-metric-936-b279d25a8e.png)

## Известные ограничения

* Расширение Dynatrace AWS Lambda не поддерживает захват [атрибутов запросов на уровне методов](/docs/observe/application-observability/services/request-attributes/capture-request-attributes-based-on-method-arguments "Узнайте, как создавать атрибуты запросов на основе аргументов методов Java, .NET или PHP и как использовать их на обзорной странице сервиса. Также узнайте, как агрегировать захваченные значения атрибутов запросов, а также как обращаться к объектам, если захватываемое значение является сложным объектом.").
* Большинство расширений Dynatrace AWS Lambda не захватывают IP-адреса исходящих HTTP-запросов. Это приводит к появлению **немониторируемых хостов**, если вызываемый сервис не мониторится Dynatrace.
* Получение токена аутентификации из AWS Secrets Manager не поддерживается, если [Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) включен.
* **Исходящие запросы к другой функции AWS Lambda:** В мониторируемой функции AWS Lambda поддерживаются следующие библиотеки для исходящих запросов к другой функции AWS Lambda:

  + Для Java: AWS SDK версии 1 для Java
  + Для Node.js: AWS SDK для JavaScript в Node.js:

    - [версия 2](https://www.npmjs.com/package/aws-sdk)
    - [версия 3](https://github.com/aws/aws-sdk-js-v3) (OneAgent версии 1.263+)
  + Для Python: AWS SDK для Python (Boto3)
* **Исходящие HTTP-запросы:** В мониторируемой функции AWS Lambda поддерживаются следующие библиотеки/HTTP-клиенты для исходящих HTTP-запросов:

  + Для Java: Apache HTTP Client 3.x, 4.x
  + Для Node.js:

    - Встроенный [`http.request`](https://nodejs.org/api/http.html#http)
    - Встроенный [`fetch API`](https://nodejs.org/docs/latest/api/globals.html#fetch) (OneAgent версии 1.285+)
  + Для Python: `requests`, `aiohttp-client`, `urllib3`, `redis-py` (OneAgent версии 1.289+)
* **Дополнительные требования для входящих вызовов только для Java:**
  Для правильного мониторинга настроенного метода обработчика

  + Настроенный класс обработчика должен самостоятельно реализовывать метод обработчика. Если метод обработчика определен только в базовом классе, необходимо добавить переопределение в класс обработчика, вызывающее метод базового обработчика (обычно `super.handleRequest(...)`).
  + Метод обработчика должен иметь параметр `Context` ([`com.amazonaws.services.lambda.runtime.Context`](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/Context.java)).
  + Мы рекомендуем [следовать лучшим практикам](https://docs.aws.amazon.com/lambda/latest/dg/java-handler.html), наследуя класс Lambda-обработчика от [com.amazonaws.services.lambda.runtime.RequestHandler](https://github.com/aws/aws-lambda-java-libs/blob/main/aws-lambda-java-core/src/main/java/com/amazonaws/services/lambda/runtime/RequestHandler.java), переопределяя `handleRequest` и настраивая его как метод обработчика.
    Однако, если предыдущие требования выполнены, OneAgent поддерживает любую допустимую функцию обработчика, даже если она не наследуется от этого базового интерфейса.
  + [Библиотека событий AWS Lambda](https://github.com/aws/aws-lambda-java-libs/tree/master/aws-lambda-java-events) должна использоваться вашей функцией, поскольку типы, определенные в пакете `com.amazonaws.services.lambda.runtime.events`, используются OneAgent для сопоставления соответствующих [типов вызовов для входящих вызовов](#incoming-calls-types).
* **Сенсоры и инструментации Node.js для ES-модулей:**

  + Сенсоры (инструментации) расширения Node.js AWS Lambda не поддерживают модули ECMAScript. Это означает, что расширение не будет корректно мониторить исходящие вызовы (например, HTTP или запросы AWS SDK).
  + Инструментации OpenTelemetry не поддерживают модули ECMAScript по умолчанию.

    Существует способ заставить инструментации OpenTelemetry работать с модулями ECMAScript, но он экспериментальный и имеет некоторые ограничения. Подробности см. в [Инструментация для ES-модулей в Node.js (экспериментально)](https://dt-url.net/r10379k).
* Режим развертывания [AWS Lambda Managed Instances](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances.html) не поддерживается. Эта новая опция хостинга позволяет развертывать Lambda-функции на управляемых AWS кластерах экземпляров EC2. Расширение Dynatrace Lambda и слои кодовых модулей в настоящее время не поддерживают этот режим развертывания.

## Связанные темы

* [Ограничение вызовов API к AWS с помощью тегов](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags "Добавление и настройка тегов AWS для ограничения ресурсов AWS.")