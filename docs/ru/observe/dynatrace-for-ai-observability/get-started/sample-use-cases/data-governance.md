---
title: AI data governance with Amazon Bedrock
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/get-started/sample-use-cases/data-governance
scraped: 2026-02-18T05:48:43.190195
---

# Управление данными ИИ с помощью Amazon Bedrock

# Управление данными ИИ с помощью Amazon Bedrock

* Последняя версия Dynatrace
* Руководство
* Чтение: 5 мин
* Обновлено 10 декабря 2025

Появляющиеся нормативные акты в области ИИ, такие как [Закон Европейского Союза об искусственном интеллекте](https://dt-url.net/xv038bv), предоставляют средства для реализации комплексной стратегии, сочетающей организационный контроль и контроль моделей ИИ, охватывающей все аспекты от обучения модели до взаимодействия ИИ с пользователем.

При работе с моделями ИИ через Amazon Bedrock Dynatrace помогает соблюдать нормативные требования к ведению записей.

## Что вы узнаете

В этом руководстве мы сначала настроим наблюдаемость обучения и развертывания вашей модели. Затем мы настроим ваше приложение для наблюдения за запросами вывода пользователей.

## Шаги

Общие шаги следующие:

1. Настройка Dynatrace
2. Настройка вашей учетной записи AWS для отправки данных в ваш тенант Dynatrace
3. Настройка вашего приложения

Подробности каждого шага приведены ниже.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройка Dynatrace**](#preparation)[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настройка учетной записи AWS**](#aws)[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Настройка приложения**](#app)

### Шаг 1: Настройка Dynatrace

На этом шаге мы создаем токен Dynatrace и настраиваем [OpenPipeline](../../../../platform/openpipeline.md "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.") для хранения данных в течение 5+ лет.

#### Создание токена Dynatrace

Чтобы создать токен Dynatrace

1. В Dynatrace перейдите в **Access Tokens**.
   Чтобы найти **Access Tokens**, нажмите **CTRL+K** для поиска и выберите **Access Tokens**.
2. В разделе **Access Tokens** выберите **Generate new token**.
3. Введите **Token name** для нового токена.
4. Предоставьте новому токену следующие разрешения:
5. Найдите и выберите все следующие области действия.

   * **Ingest bizevents** (`bizevents.ingest`)
   * **Ingest metrics** (`metrics.ingest`)
   * **Ingest logs** (`logs.ingest`)
   * **Ingest events** (`events.ingest`)
   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
6. Выберите **Generate token**.
7. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Вы можете получить доступ к токену только один раз при его создании. Впоследствии вы не сможете его просмотреть.

#### Настройка OpenPipeline

Период хранения BizEvents по умолчанию составляет 35 дней. В зависимости от нормативных требований этого может быть недостаточно.

Чтобы изменить период хранения, вы можете создать пользовательский бакет Grail.

1. Перейдите в **Settings** > **Storage management** > **Bucket storage management**.
2. В разделе **Bucket Storage Management** выберите **Bucket**.
3. В окне **New bucket**:

   * Задайте **Bucket name** (например, `gen_ai_events`)
   * Задайте **Retention period (in days)** (например, `1,825`, что составляет примерно 5 лет)
   * Установите **Bucket table type** в значение `bizevents`
4. Выберите **Save**.

![Создание бакета Grail](https://dt-cdn.net/images/bucket-creation-1380-125022930c.png)

Когда бакет станет доступен, мы можем настроить OpenPipeline для перенаправления событий, связанных с ИИ, на хранение в нем.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Business events** > **Pipelines**.
2. На вкладке **Pipelines** выберите **Pipeline** и назовите свой конвейер (например, `AI Data Governance`).
3. На вкладке **Storage** выберите **Processor** > **Bucket assignment**.
4. Настройте процессор:

   1. Введите **Name** для процессора
   2. Установите **Matching condition** в значение `true`
   3. Установите **Storage** на бакет, созданный в предыдущей процедуре
5. Выберите **Save**.

![Назначение бакета OpenPipeline](https://dt-cdn.net/images/pipeline-creation-1383-70370d9b88.png)

Наконец, мы направляем прием событий ИИ в конвейер.

1. Все еще находясь в **OpenPipeline** > **Business events**, выберите вкладку **Dynamic routing**.
2. На вкладке **Dynamic routing** выберите **Dynamic route**, чтобы **добавить новый динамический маршрут**.

   * Введите **Name** для нового маршрута (например, `AI Event Routing`)
   * Установите **Matching condition** в значение `matchesValue(event.type,"gen_ai.auditing")`
   * Установите **Pipeline** на конвейер, созданный в предыдущей процедуре.
3. Выберите **Add**.
4. Выберите **Save**.

Наконец, чтобы отметить его как первый срабатывающий конвейер, перетащите его вверх, чтобы он стал первой строкой в таблице.

![Маршрутизация OpenPipeline](https://dt-cdn.net/images/pipeline-routing-1381-ec77347761.png)

### Шаг 2: Настройка учетной записи AWS

Amazon Bedrock генерирует события для каждого выполненного действия по конфигурации, например, когда вы развертываете новую модель или когда завершается тонкая настройка вашей модели.

Мы можем настроить правило для перенаправления этих событий в Dynatrace. Обратитесь к нашей [интеграции с Amazon EventBridge с использованием BizEvent](https://github.com/dynatrace-oss/cloud-snippets/tree/main/aws/eventbridge-events-to-dynatrace#ingest-as-bizevents) для настройки правила.

Единственное изменение заключается в [поле `InputTemplate`](https://github.com/dynatrace-oss/cloud-snippets/blob/8785beb90e9d5c53de4f8420bf5e68b6ac673a09/aws/eventbridge-events-to-dynatrace/biz-events.yaml#L115), где свойство `"type"` должно быть установлено в значение `gen_ai.auditing`. Это изменение необходимо для соответствия значениям, которые OpenPipeline использует для перенаправления событий в наш бакет Grail.

Разверните, чтобы увидеть, как должна выглядеть конфигурация AWS

![Связь AWS <-> Dynatrace](https://dt-cdn.net/images/aws-dynatrace-connection-3352-4347fe5fc8.png)

![Конфигурация AWS CloudTrail Transformer](https://dt-cdn.net/images/aws-cloudtrail-transformer-1610-501eddb13f.png)

![Конфигурация AWS CloudTrail Target](https://dt-cdn.net/images/aws-cloudtrail-target-2744-0f4e467998.png)

### Шаг 3: Настройка приложения

Мы можем использовать OpenTelemetry для обеспечения автоматической инструментации, которая собирает трассировки и метрики ваших рабочих нагрузок ИИ, в частности наш форк [OpenLLMetry](https://dt-url.net/0sa3uau).

Важное замечание

Библиотеки, используемые в этом примере, в настоящее время находятся в стадии разработки и имеют статус альфа-версии. Они могут содержать ошибки или подвергаться значительным изменениям. Используйте их на свой страх и риск.
Мы высоко ценим ваши отзывы для улучшения этих библиотек. Пожалуйста, сообщайте о любых проблемах, ошибках или предложениях на нашей странице GitHub issues.

Для установки используйте следующую команду:

```
pip install -i https://test.pypi.org/simple/ dynatrace-openllmetry-sdk==0.0.1a4
```

После этого добавьте следующий код в начало вашего основного файла:

```
from traceloop.sdk import Traceloop



headers = { "Authorization": "Api-Token <YOUR_DT_API_TOKEN>" }



Traceloop.init(



app_name="<your-service>",



api_endpoint="https://<YOUR_ENV>.live.dynatrace.com/api/v2/otlp",



headers=headers



)
```

Вот и все! ![Progressive delivery](https://cdn.bfldr.com/B686QPH3/at/r898jztffhg3nzc7fxwh6pf/DT1015.svg?auto=webp&width=72&height=72 "Progressive delivery")

Теперь вы можете:

* Получать все взаимодействия пользователя с ИИ, статус обучения и многое другое по запросу.
* Использовать [Notebooks](../../../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") или [Dashboards](../../../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") для создания документов на основе данных для пользовательской аналитики.

![Аудит соответствия GenAI](https://dt-cdn.net/images/gen-ai-auditing-7680-1f44c8a6bf.png)
