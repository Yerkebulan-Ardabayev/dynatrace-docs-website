---
title: Validate integration
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/troubleshoot-lambda
scraped: 2026-03-04T21:30:20.410674
---

# Проверка интеграции

# Проверка интеграции

* Classic
* Troubleshooting
* 1-min read
* Published Aug 30, 2021

Этот раздел посвящён классической интеграции AWS Lambda. Ознакомьтесь с разделом [Трассировка функций Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/trace-lambda-functions "Monitor AWS Lambda functions.") для получения актуальных сведений.

Для устранения проблем с интеграцией расширения Dynatrace AWS Lambda начните с анализа журналов и сообщений об ошибках.

## Журналы

Чтобы получить подробный вывод журналов для Lambda, добавьте приведённые ниже переменные.

* Для **Node.js**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_NODEJS_FLAGS: Exporter=true,LambdaSensor=true
  ```
* Для **Python**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_PYTHON_FLAGS: dynatrace=True
  ```
* Для **Java**

  ```
  DT_LOGGING_DESTINATION: stdout



  DT_LOGGING_JAVA_FLAGS: log-Transformer=true,log-OpenTelemetryUtils=true,log-AsyncClassRetransformer=true,log-ClassValue=true
  ```

  `logOpenTelemetryUtils=true` требуется для `use-inmemory-exporter` (для отладки проблем, связанных со спанами).

## Сообщения об ошибках

* **WARNING [...] Unexpectedly got HTTP response with Content-Length (...)**

  Это сообщение об ошибке отображается, если порт 9999 не включён для вашего ActiveGate. Перейдите в раздел [AWS PrivateLink и конечные точки VPC](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) и настройте VPC, разрешающий исходящие подключения через порт 9999 к конечной точке ActiveGate.

## Совместимость с OpenTelemetry

### Python

OneAgent не включит совместимость с OpenTelemetry, если обнаружит, что установленная версия OpenTelemetry API несовместима. В этом случае в журнал будет записана строка, аналогичная следующей:

```
[Dynatrace] 2022-07-27 08:55:01.852 UTC [9-dfaf4836] INFO    [dynatrace.inject.agent] opentelemetry-api version (1.10.0) is not compatible with Dynatrace SDK (1.9.1).
```

Можно переопределить проверку совместимости через конфигурацию. Например, при настройке OneAgent с использованием [переменных среды](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Monitor Lambda functions written in Python, Node.js, and Java.") добавьте:

`DT_OPEN_TELEMETRY_OVERRIDE_MAX_API_VERSION=1.11.1`

чтобы разрешить использование OpenTelemetry API вплоть до версии `1.11.1`.

Переопределение проверки совместимости версий может привести к ошибкам во время выполнения и должно применяться с **осторожностью**. Проверьте, возникают ли эти ошибки при использовании официально поддерживаемой версии OpenTelemetry API или при временном отключении совместимости с OpenTelemetry. Если это решает проблему, используйте более старую версию OpenTelemetry API до тех пор, пока более новая версия не будет официально поддержана.
