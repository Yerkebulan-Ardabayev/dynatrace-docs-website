---
title: Интеграция Dynatrace Lambda Layer в образы контейнеров
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/deploy-oa-latest-lambda-container-images
scraped: 2026-05-12T12:01:30.966151
---

# Интеграция Dynatrace Lambda Layer в образы контейнеров

# Интеграция Dynatrace Lambda Layer в образы контейнеров

* Практическое руководство
* Чтение: 4 мин
* Обновлено 22 января 2026 г.

Помимо развёртывания Lambda-функций в виде ZIP-файла, AWS Lambda поддерживает [развёртывание Lambda-функций в виде образов контейнеров](https://aws.amazon.com/de/blogs/aws/new-for-aws-lambda-container-image-support/).

Образ контейнера должен включать файлы и конфигурацию, необходимые для запуска кода функции. То же относится и к файлам и конфигурации Dynatrace AWS Lambda Layer, после того как для контейнеризованной Lambda-функции будет включён мониторинг.

При развёртывании функции в виде ZIP-файла артефакты Dynatrace подключаются к функции с помощью [расширения AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/using-extensions.html) (это Lambda layer со специфичной для расширения структурой папок).

Lambda layer, как и пакет функции, представляет собой ZIP-файл, который распаковывается при холодном старте функции в папку `/opt` инстанса AWS Lambda.

Ниже описано, как включить мониторинг Dynatrace для контейнеризованной Lambda-функции.

## Конфигурация

1. Перейдите в раздел [Трассировка Lambda-функций на Python, Node.js и Java](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-method "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.") и следуйте инструкциям **Configure with environment variables**.
2. Откройте `Dockerfile` проекта в редакторе и скопируйте переменные окружения с экрана развёртывания. Перед каждой
   строкой нужно добавить префикс `ENV`, а пробелы вокруг знака равенства нужно убрать.

```
ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace



ENV DT_TENANT=5f92a04b-404b-41cb-be4a-59114ddeae06



ENV DT_CLUSTER=1234567890



ENV DT_CONNECTION_BASE_URL=https://activegate.dynatrace.com:9999/e/5f92a04b-404b-41cb-be4a-59114ddeae06



ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...
```

## Скопируйте конфигурационный сниппет Lambda layer

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation** > **AWS Lambda**.

3. На странице **Enable Monitoring for AWS Lambda Functions** скопируйте конфигурационный сниппет Lambda layer.

## Добавьте расширение OneAgent в образ контейнера

1. Чтобы скачать содержимое расширения Dynatrace AWS Lambda в локальную файловую систему, используйте приведённый ниже пример кода для [dt-awslayertool](#dt-awslayertool) или [AWS CLI](#aws-cli).

   Через dt-awslayertool

   Через AWS CLI

   В приведённом ниже примере замените `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` на [скопированный сниппет Lambda layer](#copy-layer-snippet).

   ```
   dt-awslayertool pull <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --extract DynatraceOneAgentExtension
   ```

   Пример команды

   Следующая команда скачивает layer `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` и распаковывает его содержимое в локальную папку `DynatraceOneAgentExtension`.

   ```
   dt-awslayertool pull arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --extract DynatraceOneAgentExtension
   ```

   Подробнее о dt-awslayertool см. [Github](https://github.com/dynatrace-oss/dt-awslayertool).

   В приведённом ниже примере замените `<YOUR_LAMBDA_LAYER_ARN_SNIPPET>` на [скопированный сниппет Lambda layer](#copy-layer-snippet), а `<YOUR_LAMBDA_LAYER_REGION>` на регион Lambda layer, указанный в сниппете.

   ```
   curl $(aws --region <YOUR_LAMBDA_LAYER_REGION> lambda get-layer-version-by-arn --arn <YOUR_LAMBDA_LAYER_ARN_SNIPPET> --query 'Content.Location' --output text) --output layer.zip



   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   Пример команды

   Следующий пример кода скачивает и распаковывает содержимое `arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1` в локальную папку `DynatraceOneAgentExtension`.

   ```
   curl $(aws --region us-east-1 lambda get-layer-version-by-arn --arn arn:aws:lambda:us-east-1:725887861453:layer:Dynatrace_OneAgent_1_207_6_20201127-103507_nodejs:1 --query 'Content.Location' --output text) --output layer.zip



   unzip -d DynatraceOneAgentExtension layer.zip
   ```

   Подробнее об AWS CLI см. [документацию AWS](https://docs.aws.amazon.com/cli/index.html).
2. Чтобы скопировать скачанное содержимое расширения в образ контейнера и убедиться, что shell-скрипт `/opt/dynatrace` исполняемый, используйте следующие команды `Dockerfile`.

   ```
   COPY DynatraceOneAgentExtension/ /opt/



   RUN chmod +x /opt/dynatrace
   ```

### Пример `Dockerfile` с включённым расширением Dynatrace AWS Lambda

Этот пример проекта создаёт контейнеризованную Node.js Lambda-функцию.

Папка проекта содержит следующие файлы и папки:

```
containerized-lambda-sample



âââ Dockerfile



âââ DynatraceOneAgentExtension



âââ index.js
```

Предполагается, что содержимое Dynatrace AWS Lambda Layer уже скачано и распаковано (как описано выше) в папку `DynatraceOneAgentExtension`.

Функция-обработчик экспортируется из файла `index.js`:

```
exports.handler = async () => {



return "hello world";



}
```

`Dockerfile` с изменениями для интеграции расширения Dynatrace AWS Lambda в контейнеризованную функцию:

```
FROM public.ecr.aws/lambda/nodejs:18



COPY index.js ${LAMBDA_TASK_ROOT}



# --- Begin of enable Dynatrace OneAgent monitoring section



# environment variables copied from Dynatrace AWS Lambda deployment screen



# (prefix with ENV and remove spaces around equal signs)



ENV AWS_LAMBDA_EXEC_WRAPPER=/opt/dynatrace



ENV DT_TENANT=5f92a04b-404b-41cb-be4a-59114ddeae06



ENV DT_CLUSTER=1234567890



ENV DT_CONNECTION_BASE_URL=https://activegate.dynatrace.com:9999/e/5f92a04b-404b-41cb-be4a-59114ddeae06



ENV DT_CONNECTION_AUTH_TOKEN=dt0a01...



# copy Dynatrace OneAgent extension download and extracted to local disk into container image



COPY DynatraceOneAgentExtension/ /opt/



# make /opt/dynatrace shell script executable



RUN chmod +x /opt/dynatrace



# --- End of enable Dynatrace OneAgent monitoring section



CMD [ "index.handler" ]
```

## Ограничения

Мониторинг через расширение Dynatrace AWS Lambda на образах контейнеров поддерживается только для образов, [созданных на основе базового образа AWS для Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html#images-create-1), и только для [сред выполнения, которые мы поддерживаем для неконтейнеризованных функций](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "Возможности AWS Lambda и варианты интеграции").

## Дополнительные ресурсы

Подробнее об образах контейнеров Lambda см.:

* [Создание образов контейнеров Lambda](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html)
* [Работа с Lambda-слоями и расширениями в образах контейнеров](https://aws.amazon.com/de/blogs/compute/working-with-lambda-layers-and-extensions-in-container-images/)