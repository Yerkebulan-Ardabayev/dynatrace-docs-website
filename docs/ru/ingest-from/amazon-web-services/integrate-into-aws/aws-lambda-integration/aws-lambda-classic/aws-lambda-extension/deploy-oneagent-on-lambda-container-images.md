---
title: Интеграция Dynatrace Lambda Layer в образы контейнеров
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images
scraped: 2026-03-05T21:31:40.930635
---

# Интеграция Dynatrace Lambda Layer в контейнерные образы


В дополнение к развертыванию Lambda-функций в виде ZIP-файла, AWS Lambda предлагает [развертывание Lambda-функций в виде контейнерных образов](https://aws.amazon.com/de/blogs/aws/new-for-aws-lambda-container-image-support/).

Контейнерный образ должен содержать файлы и конфигурацию, необходимые для выполнения кода функции. То же самое относится к файлам и конфигурации Dynatrace AWS Lambda Layer после включения мониторинга для контейнеризированной Lambda-функции.

При развертывании функции в виде ZIP-файла артефакты Dynatrace подключаются к функции с помощью [расширения AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html) (которое представляет собой Lambda-слой со структурой папок, специфичной для расширений).

Lambda-слой, как и пакет функции, представляет собой ZIP-файл, который извлекается при холодном запуске функции в папку `/opt` экземпляра AWS Lambda-функции.

Ниже описано, как включить мониторинг Dynatrace для контейнеризированной Lambda-функции.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Конфигурация**](deploy-oneagent-on-lambda-container-images.md#configuration "Развертывание Dynatrace Lambda Layer при развертывании через контейнерный образ.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Копирование фрагмента конфигурации Lambda-слоя**](deploy-oneagent-on-lambda-container-images.md#copy-layer-snippet "Развертывание Dynatrace Lambda Layer при развертывании через контейнерный образ.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавление расширения Dynatrace AWS Lambda в контейнерный образ**](deploy-oneagent-on-lambda-container-images.md#add-oneagent-extension "Развертывание Dynatrace Lambda Layer при развертывании через контейнерный образ.")

## Шаг 1 Конфигурация

1. Перейдите в раздел [Трассировка Lambda-функций на Python, Node.js и Java](../aws-lambda-extension.md#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") и следуйте инструкциям раздела **Настройка с помощью переменных окружения**.
2. Откройте файл `Dockerfile` проекта в редакторе и скопируйте переменные окружения с экрана развертывания. Каждая
   строка должна начинаться с префикса `ENV`, а пробелы вокруг знаков равенства должны быть удалены.

```
ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace


ENV DT_TENANT=abcd1234


ENV DT_CLUSTER_ID=1234567890


ENV DT_CONNECTION_BASE_URL=https://abcd1234.live.dynatrace.com


ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...
```

## Шаг 2 Копирование фрагмента конфигурации Lambda-слоя

1. В Dynatrace Hub выберите **AWS Lambda**.
2. Выберите **Set up**.

3. На странице **Enable Monitoring for AWS Lambda Functions** скопируйте фрагмент конфигурации Lambda-слоя.

## Шаг 3 Добавление расширения OneAgent в контейнерный образ

1. Чтобы загрузить содержимое расширения Dynatrace AWS Lambda на локальную файловую систему, используйте следующий пример кода для [dt-awslayertool](#dt-awslayertool) или [AWS CLI](#aws-cli).

   Через dt-awslayertool

   Через AWS CLI

   Для использования следующего примера кода замените `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` на [скопированный фрагмент Lambda-слоя](#copy-layer-snippet).

   ```
   dt-awslayertool pull <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --extract DynatraceOneAgentExtension
   ```

   Пример команды

   Следующий пример команды загружает слой `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` и извлекает его содержимое в локальную папку `DynatraceOneAgentExtension`.

   ```
   dt-awslayertool pull arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --extract DynatraceOneAgentExtension
   ```

   Подробнее о dt-awslayertool см. на [Github](https://github.com/dynatrace-oss/dt-awslayertool).

   Для использования следующего примера кода замените `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` на [скопированный фрагмент Lambda-слоя](#copy-layer-snippet), а `<YOUR_LAMBDA_LAYER_REGION>` -- на регион Lambda-слоя, указанный в фрагменте.

   ```
   curl $(aws --region <YOUR_LAMBDA_LAYER_REGION> lambda get-layer-version-by-arn --arn <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --query 'Content.Location' --output text) --output layer.zip


   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   Пример команды

   Следующий пример кода загружает и извлекает содержимое `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` в локальную папку `DynatraceOneAgentExtension`.

   ```
   curl $(aws --region us-east-1 lambda get-layer-version-by-arn --arn arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --query 'Content.Location' --output text) --output layer.zip


   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   Подробнее об AWS CLI см. в [документации AWS](https://docs.aws.amazon.com/cli/index.html).
2. Чтобы скопировать загруженное содержимое расширения в контейнерный образ и сделать shell-скрипт `/opt/dynatrace` исполняемым, используйте следующие команды `Dockerfile`.

   ```
   COPY DynatraceOneAgentExtension/ /opt/


   RUN chmod +x /opt/dynatrace
   ```

### Пример `Dockerfile` с включенным расширением Dynatrace AWS Lambda

Этот пример проекта создает контейнеризированную Lambda-функцию на Node.js.

Папка проекта содержит следующие файлы и папки:

```
containerized-lambda-sample


--- Dockerfile


--- DynatraceOneAgentExtension


--- index.js
```

Предполагается, что содержимое Dynatrace AWS Lambda Layer загружено и извлечено (как описано выше) в папку `DynatraceOneAgentExtension`.

Функция-обработчик экспортируется файлом `index.js`:

```
exports.handler = async () => {


return "hello world";


}
```

`Dockerfile` с внесенными изменениями для интеграции расширения Dynatrace AWS Lambda в контейнеризированную функцию:

```
FROM public.ecr.aws/lambda/nodejs:18


COPY index.js ${LAMBDA_TASK_ROOT}


# --- Begin of enable Dynatrace OneAgent monitoring section


# environment variables copied from Dynatrace AWS Lambda deployment screen


# (prefix with ENV and remove spaces around equal signs)


ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace


ENV DT_TENANT=abcd1234


ENV DT_CLUSTER_ID=1234567890


ENV DT_CONNECTION_BASE_URL=https://abcd1234.live.dynatrace.com


ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...


# copy Dynatrace OneAgent extension download and extracted to local disk into container image


COPY DynatraceOneAgentExtension/ /opt/


# make /opt/dynatrace shell script executable


RUN chmod +x /opt/dynatrace


# --- End of enable Dynatrace OneAgent monitoring section


CMD [ "index.handler" ]
```

## Ограничения

Мониторинг через расширение Dynatrace AWS Lambda для контейнерных образов поддерживается только для образов, [созданных на основе базового образа AWS для Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-1), и только для [сред выполнения, которые мы поддерживаем для неконтейнеризированных функций](../../../aws-lambda-integration.md#support-lifecycle "Возможности AWS Lambda и варианты интеграции").

## Дополнительные ресурсы

Дополнительную информацию о контейнерных образах Lambda см. в:

* [Создание контейнерных образов Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
* [Работа со слоями и расширениями Lambda в контейнерных образах](https://aws.amazon.com/de/blogs/compute/working-with-lambda-layers-and-extensions-in-container-images/)
