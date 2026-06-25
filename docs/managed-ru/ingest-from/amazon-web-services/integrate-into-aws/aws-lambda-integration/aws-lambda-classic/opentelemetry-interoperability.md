---
title: OpenTelemetry interoperability
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability
scraped: 2026-05-12T12:11:07.637749
---

# OpenTelemetry interoperability

# OpenTelemetry interoperability

* Чтение: 1 мин
* Обновлено 24 апреля 2023 г.

С помощью Dynatrace interoperability для OpenTelemetry можно использовать пакеты инструментации, доступные в OpenTelemetry, для мониторинга технологий (например, баз данных или фреймворков обмена сообщениями), которые расширение Dynatrace AWS Lambda не поддерживает из коробки. Расширение Dynatrace AWS Lambda автоматически собирает дополнительную инструментацию span и интегрирует её с любой другой собранной телеметрией без необходимости настраивать дополнительные экспортёры OpenTelemetry.

[OpenTelemetry](https://dt-url.net/y903u4j) представляет собой набор инструментов, API и SDK. С его помощью можно инструментировать, генерировать, собирать и экспортировать телеметрические данные (метрики, журналы и трассировки) для анализа, чтобы получить представление о производительности и поведении вашего программного обеспечения. OpenTelemetry interoperability связывает [расширение Dynatrace AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") с OpenTelemetry API для соответствующей инструментации.

## Включение OpenTelemetry interoperability

* Для [метода конфигурации через переменные окружения](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") задайте переменной окружения `DT_OPEN_TELEMETRY_ENABLE_INTEGRATION` значение `true`.
* Для [метода конфигурации через JSON-файл](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") задайте соответствующему свойству значение `true` в файле `dtconfig.json`. Например:

  ```
  {



  ...other configuration properties...



  "OpenTelemetry": {



  "EnableIntegration": true



  }



  }
  ```

## Подробнее

Подробнее о том, как работает OpenTelemetry interoperability, см.

* [OpenTelemetry interoperability в Python](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-python "Подключение расширения Dynatrace AWS Lambda к инструментации OpenTelemetry для Python через OpenTelemetry interoperability.")
* [OpenTelemetry interoperability в Node.js](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-nodejs "Подключение расширения Dynatrace AWS Lambda к инструментации OpenTelemetry для Node.js через OpenTelemetry interoperability.")
* [OpenTelemetry interoperability в Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/lambda-otel-bridge-java "Подключение расширения Dynatrace AWS Lambda к OpenTelemetry Java API через OpenTelemetry interoperability.")

## Связанные темы

* [Трассировка Lambda-функций на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.")