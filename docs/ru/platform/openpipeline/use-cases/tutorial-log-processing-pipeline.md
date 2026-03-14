---
title: Парсинг строк лога и извлечение метрики
source: https://www.dynatrace.com/docs/platform/openpipeline/use-cases/tutorial-log-processing-pipeline
scraped: 2026-03-06T21:13:39.739379
---

# Разбор строк логов и извлечение метрики

# Разбор строк логов и извлечение метрики

* Latest Dynatrace
* Руководство
* Чтение: 5 мин.
* Обновлено 23 июня 2025 г.

В этом руководстве показано, как разобрать важную информацию из строк логов в отдельные поля и извлечь из неё метрику. Выделенные поля упрощают выполнение запросов и извлечение метрик, позволяя отображать долгосрочные данные на дашборде.

## Для кого это руководство

Эта статья предназначена для администраторов, управляющих конфигурацией приёма логов, хранением и обогащением данных, а также политиками преобразования.

## Чему вы научитесь

В этой статье вы научитесь сужать тысячи строк логов до строк, относящихся к добавлению пользователем товара в корзину, преобразовывать необработанные входные данные в структурированные результаты с новыми выделенными полями (`userId`, `productId` и `quantity`), а также извлекать метрику, измеряющую количество товара по продукту.

Следующая строка лога является примером необработанных данных, на которых сосредоточена данная статья.

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

## Перед началом

Необходимые знания

* [Dynatrace Query Language](../../grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](../concepts/processing.md "Основные концепции обработки в Dynatrace OpenPipeline.")

Предварительные условия

* Среда Dynatrace SaaS на базе Grail и AppEngine.
* Либо лицензия [Dynatrace](../../../license.md "О Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace."), включающая возможности [Log Analytics (DPS)](../../../license/capabilities/log-analytics.md "Узнайте, как рассчитывается потребление Dynatrace Log Analytics с использованием модели Dynatrace Platform Subscription."), либо [DDU для Log Management and Analytics](../../../license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics.md "Узнайте, как рассчитывается объём потребления DDU для Dynatrace Log Management and Analytics.").

## Шаги

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Найти релевантные строки логов в Grail**](tutorial-log-processing-pipeline.md#logs "Настройка обработки OpenPipeline для строк логов.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Настроить конвейер для разбора и извлечения метрик**](tutorial-log-processing-pipeline.md#pipeline "Настройка обработки OpenPipeline для строк логов.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Направить данные в конвейер**](tutorial-log-processing-pipeline.md#route "Настройка обработки OpenPipeline для строк логов.")[![Шаг 4 (необязательно)](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4 (необязательно)")

**Проверить конфигурацию**](tutorial-log-processing-pipeline.md#verify "Настройка обработки OpenPipeline для строк логов.")

### Шаг 1. Найти релевантные строки логов в Grail

1. Перейдите в **Notebooks**.
2. Используйте DQL-запрос для сужения выборки до релевантных строк логов.

   Следующий пример запроса извлекает первые 250 логов из пространства `online-boutique`, содержащих `AddItemAsync` и имеющих временную метку.

   ```
   fetch logs



   | filter k8s.namespace.name == "online-boutique"



   | filter matchesValue(content, "AddItemAsync*")



   | fields timestamp, content



   | limit 250
   ```

   ![Поиск релевантных строк логов с помощью DQL-запроса](https://dt-cdn.net/images/log-processing-dql-query-1200-d1966f2ef5.png)

### Шаг 2. Создание конвейера для разбора и извлечения

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Pipelines**.
2. Чтобы создать новый конвейер, нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** и введите имя (`Online Boutique`).
3. Для настройки разбора

   1. Перейдите в **Processing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **DQL** и определите процессор, указав:

      * Описательное имя (`Parse product, user, and quantity`).
      * Условие соответствия.

        В нашем примере условие соответствия:

        ```
        matchesValue(content, "AddItemAsync*")
        ```
      * Определение процессора.
        В нашем примере определение процессора:

        ```
        parse content, "\"AddItemAsync called with userId=\"LD:userId\", productId=\"LD:productId, \"quantity=\"INT:quantity"
        ```
   2. Необязательно: для проверки процессора

      1. Введите образец данных.
         В нашем примере образец данных:

         ```
         {



         "content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4", "k8s.namespace.name": "online-boutique"



         }
         ```
      2. Нажмите **Run sample data**.
      3. Просмотрите результат предварительного просмотра и при необходимости измените условие соответствия и/или определение процессора.

         ![Разбор данных логов в структурированный формат через OpenPipeline](https://dt-cdn.net/images/log-processing-parsing-processor-1920-44ef93f030.png)
4. Для настройки извлечения метрик перейдите в **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Value metric** и определите процессор, указав:

   * Описательное имя (`Extract quantity by product for AddItem`).
   * То же условие соответствия, которое вы использовали для разбора.
   * Имя поля, из которого извлекается значение (`quantity`).
   * Ключ метрики для поля (`add_item_product_quantity_by_product`).
   * Измерение метрики

     1. Выберите **Custom** dimensions.
     2. Введите измерение метрики (`productId`).
     3. Нажмите **Add**.

   ![Извлечение метрики через OpenPipeline](https://dt-cdn.net/images/log-processing-metric-extraction-1200-f4550a4cd6.png)
5. Нажмите **Save**.

Вы успешно настроили новый конвейер с двумя процессорами — одним для разбора и одним для извлечения метрик. Новый конвейер отображается в списке конвейеров.

### Шаг 3. Направить данные в конвейер

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**: > **Logs** > **Dynamic routing**.
2. Чтобы создать новый маршрут, нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** и укажите:

   * Описательное имя (`Online Boutique`).
   * Условие соответствия.

     В нашем примере условие соответствия:

     ```
     k8s.namespace.name == "online-boutique"
     ```
   * Конвейер, содержащий инструкции обработки (`Online Boutique`).

   ![Настройка динамического маршрута для обработки логов в OpenPipeline](https://dt-cdn.net/images/log-processing-dynamic-route-1200-ef7c422264.png)
3. Нажмите **Add**.

Вы успешно настроили новый маршрут. Новый маршрут отображается в списке маршрутов.

### Шаг 4 (необязательно). Проверка конфигурации

1. Сгенерируйте токен доступа.

   1. Перейдите в **Access Tokens** > **Generate new token** и укажите:

      * Имя токена.
      * Область действия токена — **Ingest logs** (`logs.ingest`).
   2. Нажмите **Generate token**.
   3. Нажмите **Copy**, а затем вставьте токен в безопасное место. Это длинная строка, которую вам нужно скопировать и вставить обратно в Dynatrace позже.
2. Отправьте запись лога.

   Выполните следующую команду для отправки записи лога на конечную точку вашей среды `/api/v2/logs/ingest` через `POST`-запрос.

   Эта команда указывает тип содержимого JSON и предоставляет JSON-данные события с помощью параметра `-d`. Обязательно замените:

   * `{your-environment-id}` на идентификатор вашей среды.
   * `<your-API-token>` на сгенерированный вами токен.

   ```
   curl -i -X POST "https://{your-environment-id}.live.dynatrace.com/api/v2/logs/ingest" \



   -H "Content-Type: application/json" \



   -H "Authorization: Api-Token <your API token>" \



   -d "{\"k8s.namespace.name\":\"online-boutique\",\"content\":\"AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4\"}"
   ```

   Ваш запрос успешен, если вывод содержит код ответа 204.
3. Проверьте разбор, запросив запись лога и метрику в блокноте (notebook).

   1. Откройте существующий или новый блокнот в **Notebooks**.
   2. Нажмите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") > **DQL** и добавьте два новых раздела с полем ввода DQL-запроса.

      * Для проверки записи лога добавьте раздел с полем ввода DQL-запроса.

        В нашем примере DQL-запрос:

        ```
        fetch logs



        | filter userId == "6517055a-9fcc-4707-8786-e33a767a90c4"
        ```
      * Для проверки метрики добавьте ещё один раздел с полем ввода DQL-запроса.

        В нашем примере DQL-запрос:

        ```
        timeseries avg(log.add_item_product_quantity_by_product), by:{productId}



        | fieldsAdd sum = arraySum(`avg(log.add_item_product_quantity_by_product)`)



        | fields sum, productId
        ```

      ![Проверка результатов обработки OpenPipeline](https://dt-cdn.net/images/log-processing-verification-1200-4ccb7afb6a.png)

## Заключение

Вы успешно создали конвейер для разбора данных логов и извлечения метрики. Записи логов о добавлении пользователем товара в корзину преобразованы из необработанной информации в структурированную информацию в соответствии с вашими правилами. Теперь они содержат выделенные поля (`userId`, `productId` и `quantity`), из которых вы извлекли новую метрику для улучшенной аналитики.

**Необработанная запись лога**

```
{



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"k8s.namespace.name": "online-boutique"



}
```

**Структурированная запись лога**

```
{



"k8s.namespace.name": "online-boutique",



"quantity" : 4,



"productId": "OLJCESPC7Z",



"userId": "6517055a-9fcc-4707-8786-e33a767a90c4",



"content": "AddItemAsync called with userId=6517055a-9fcc-4707-8786-e33a767a90c4, productId=OLJCESPC7Z, quantity=4",



"timestamp": "2024-06-19T15:29:54.125000000Z"



}
```
