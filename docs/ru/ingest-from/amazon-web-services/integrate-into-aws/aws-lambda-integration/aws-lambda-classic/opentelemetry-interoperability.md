---
title: Совместимость OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability
scraped: 2026-03-06T21:36:18.576681
---

# Совместимость с OpenTelemetry

# Совместимость с OpenTelemetry

* Classic
* 1-min read
* Updated on Apr 24, 2023

Благодаря совместимости Dynatrace с OpenTelemetry вы можете использовать пакеты инструментирования от OpenTelemetry для мониторинга технологий (например, баз данных или фреймворков обмена сообщениями), которые не поддерживаются расширением Dynatrace AWS Lambda из коробки. Расширение Dynatrace AWS Lambda автоматически захватывает дополнительное инструментирование спанов и интегрирует его с другими данными телеметрии без необходимости настраивать дополнительные экспортёры OpenTelemetry.

[OpenTelemetry](https://dt-url.net/y903u4j) — это набор инструментов, API и SDK. Его можно использовать для инструментирования, генерации, сбора и экспорта данных телеметрии (метрик, журналов и трасс) для анализа и получения сведений о производительности и поведении программного обеспечения. Совместимость с OpenTelemetry обеспечивает подключение [расширения Dynatrace AWS Lambda](aws-lambda-extension.md "Monitor Lambda functions written in Python, Node.js, and Java.") к OpenTelemetry API для соответствующего инструментирования.

## Включение совместимости с OpenTelemetry

* Для [метода настройки через переменные среды](aws-lambda-extension.md#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") установите значение переменной среды `DT_OPEN_TELEMETRY_ENABLE_INTEGRATION` равным `true`.
* Для [метода настройки через JSON-файл](aws-lambda-extension.md#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") установите соответствующее свойство равным `true` в файле `dtconfig.json`. Например:

  ```
  {



  ...other configuration properties...



  "OpenTelemetry": {



  "EnableIntegration": true



  }



  }
  ```

## Подробнее

Чтобы узнать больше о том, как работает совместимость с OpenTelemetry, см.:

* [OpenTelemetry interoperability in Python](opentelemetry-interoperability/lambda-otel-bridge-python.md "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Python instrumentation via OpenTelemetry interoperability.")
* [OpenTelemetry interoperability in Node.js](opentelemetry-interoperability/lambda-otel-bridge-nodejs.md "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Node.js instrumentation via OpenTelemetry interoperability.")
* [OpenTelemetry interoperability in Java](opentelemetry-interoperability/lambda-otel-bridge-java.md "Connect Dynatrace AWS Lambda extension to the OpenTelemetry Java API via OpenTelemetry interoperability.")

## Связанные темы

* [Trace Python, Node.js, and Java Lambda functions](aws-lambda-extension.md "Monitor Lambda functions written in Python, Node.js, and Java.")
