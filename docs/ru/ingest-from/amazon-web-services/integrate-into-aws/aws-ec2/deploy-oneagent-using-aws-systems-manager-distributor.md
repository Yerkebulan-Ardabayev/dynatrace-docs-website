---
title: Развертывание OneAgent с помощью AWS Systems Manager Distributor
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor
scraped: 2026-03-02T21:20:06.387958
---

# Развёртывание OneAgent с помощью AWS Systems Manager Distributor

# Развёртывание OneAgent с помощью AWS Systems Manager Distributor

* How-to guide
* 8-min read
* Updated on Jan 12, 2024

С помощью [AWS Systems Manager Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html) вы можете распространять и автоматически развёртывать OneAgent на ваших EC2-инстансах, используя AWS Systems Manager Distributor.

## Предварительные требования

Перед началом развёртывания пакета `DynatraceOneAgent` через дистрибьютор убедитесь, что ваши EC2-инстансы Amazon соответствуют следующим требованиям:

### Теги AWS

Теги AWS в метаданных инстансов по умолчанию отключены при запуске. Чтобы их разрешить, следуйте официальной [документации AWS](https://dt-url.net/k2038k6).

### AWS Systems Manager

AWS Systems Manager должен быть настроен для вашей учётной записи AWS, а AWS Systems Manager Agent (SSM Agent) должен быть установлен на EC2-инстансах, на которых вы хотите развернуть пакет дистрибьютора `DynatraceOneAgent`. Следуйте инструкциям [быстрой настройки AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) или более подробному руководству [Настройка AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html).

### Поддерживаемые операционные системы

Пакет дистрибьютора `DynatraceOneAgent` поддерживается на следующих операционных системах:

| Операционная система | Версия | Архитектура |
| --- | --- | --- |
| Windows | [Все версии, поддерживаемые OneAgent](../../../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | x86-64, |
| Amazon Linux | [Все версии, поддерживаемые OneAgent](../../../technology-support.md "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Ubuntu | 16.04, 18.04, 22.04 | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Red Hat Enterprise Linux | 8.x, 9.x | x86-64 |
| SUSE Enterprise Linux | 15.x | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |

1

Поддержка архитектуры ARM64, включая [процессоры AWS Graviton](https://aws.amazon.com/ec2/graviton/), доступна в режиме [раннего доступа (Early Adopter)](https://www.dynatrace.com/news/blog/get-out-of-the-box-visibility-into-your-arm-platform-early-adopter/).

### Wget

Для пакета дистрибьютора Dynatrace OneAgent требуется установленный `Wget` на вашем Linux-инстансе. Если `Wget` не установлен, пакет дистрибьютора OneAgent установит его автоматически. `Wget` необходим для загрузки последней версии OneAgent.

### AWS CLI

AWS CLI необходим, если вы используете Parameter Store или Secrets Manager для хранения PaaS-токена. Если AWS CLI не установлен, пакет дистрибьютора OneAgent установит последнюю версию.

Если ваш инстанс работает с AWS CLI версии 1, необходимо добавить параметр `SSM_DYNATRACE_TOKEN_REGION` с регионом, в котором работает ваш инстанс, в конфигурацию SSM Distributor, так как автоматическое определение региона через EC2 IMDS доступно только в AWS CLI версии 2.

## Ограничения

Развёртывание OneAgent с помощью AWS Systems Manager Distributor в настоящее время не поддерживается, если в качестве значения параметра `SSM_DYNATRACE_URL` указан Dynatrace Managed Cluster.

## Установка

Для установки пакета дистрибьютора `DynatraceOneAgent`:

1. Откройте [консоль AWS Systems Manager](https://dt-url.net/ug6387o).
2. На панели навигации выберите **Distributor**.
3. На странице Distributor выберите **Third party** и выберите пакет `DynatraceOneAgent`.
4. Выберите режим установки. Вы можете установить или обновить пакет `DynatraceOneAgent` однократно или запланировать установку. Подробнее об установке пакетов Distributor см. в [документации AWS Systems Manager Distributor](https://dt-url.net/bv438ci).
5. Для настройки установки пакета `DynatraceOneAgent` добавьте [параметры](#installation-parameters) в поле **Additional Arguments** команды **Systems Manager Run Command**.
   Параметры требуют наличия [PaaS-токена](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Learn the concept of an access token and its scopes.").

   Для предоставления PaaS-токена мы рекомендуем использовать централизованную систему управления секретами в облаке, такую как [AWS Secrets Manager](https://dt-url.net/2803808) или [Parameter Store](https://dt-url.net/3y238xf).

   * Предоставление PaaS-токена через **AWS Secrets Manager** Recommended

     1. Создайте секрет:

        ```
        aws secretsmanager create-secret --name dynatrace-paas-token --secret-string "paas_token_value"
        ```
     2. Добавьте IAM-политику к IAM-роли, привязанной к вашему EC2-инстансу(-ам), которая предоставляет доступ для получения секрета из Secrets Manager. Ниже приведён пример политики, привязанной к IAM-роли (другие варианты можно найти в [руководстве пользователя AWS](https://dt-url.net/7k838d2)):

        ```
        {



        "Version": "2012-10-17",



        "Statement": [



        {



        "Effect": "Allow",



        "Action": "secretsmanager:GetSecretValue",



        "Resource": "arn:aws:secretsmanager:us-east-2:123456789012:secret:dynatrace-paas-token"



        }



        ]



        }
        ```

        Если ваш секрет зашифрован с помощью CMK KMS Key, вам также необходимо предоставить разрешения на расшифровку как для IAM-роли, так и для политики KMS Key. Подробнее см. в [документации AWS Secrets Manager](https://dt-url.net/3pa38cu).
     3. Укажите имя секрета через `SSM_DYNATRACE_TOKEN_SECRET_ID` в **параметрах пакета SSM Distributor**. Пример:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN_SECRET_ID" : "dynatrace-paas-token"



        }
        ```
   * Предоставление PaaS-токена через **Parameter Store** Recommended

     1. Создайте параметр типа `SecureString`.

        ```
        aws ssm put-parameter --name "dynatrace-paas-token" --value "paas_token_value" --type "SecureString"
        ```
     2. Добавьте IAM-политику к IAM-роли, привязанной к вашему EC2-инстансу(-ам), которая предоставляет доступ для получения секрета из Parameter Store. Ниже приведён пример политики. Подробнее см. в [документации AWS Systems Manager](https://dt-url.net/3nc38v5).

        ```
        {



        "Version": "2012-10-17",



        "Statement": [



        {



        "Effect": "Allow",



        "Action": [



        "ssm:GetParameter"



        ],



        "Resource": "arn:aws:ssm:us-east-2:123456789012:parameter/dynatrace-paas-token"



        }



        ]



        }
        ```
     3. Укажите имя секрета через `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` в параметрах SSM Distributor. Пример:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN" : "abcdefghij123456",



        }
        ```
   * Предоставление PaaS-токена через переменную окружения `SSM_DYNATRACE_TOKEN`. not-recommended

     Использование параметра `SSM_DYNATRACE_TOKEN` небезопасно, так как PaaS-токен будет виден в истории [Run Command](https://dt-url.net/bf038x6).

   Пример: дополнительные аргументы в Systems Manager Run Command

   ![AWS distributor](https://dt-cdn.net/images/aws-distributor-1281-19fb123371.png)

   ```
   {



   "SSM_DYNATRACE_URL" : "https://your-tenant.live.dynatrace.com/",



   "SSM_DYNATRACE_HOST_GROUP" : "MY-HOST-GROUP",



   "SSM_DYNATRACE_MONITORING_MODE" : "infra-only",



   "SSM_DYNATRACE_APP_LOG_CONTENT_ACCESS" : "true",



   "SSM_DYNATRACE_TOKEN_SECRET_ID" : "dynatrace-paas-token"



   }
   ```
6. Проверьте установку.

   * После запуска установки проверьте ход выполнения в области **Command status**. Когда вы увидите статус **Success**, это означает, что установка прошла успешно.

   Пример: успешный вывод установки

   ```
   Initiating DynatraceOneAgent_ 1.0.51 install



   Plugin aws:runPowerShellScript ResultStatus Success



   install output: Running install.ps1



   Installing Dynatrace OneAgent on Windows...



   script version: 1.0.51



   Configuration parameters:



   - Dynatrace URL: https://environment.live.dynatrace.com/



   --quiet



   Installing Dynatrace Package on Windows...



   - downloading agent from: https://environment.live.dynatrace.com/ to: %PROGRAMDATA%\Amazon\SSM\Packages\DynatraceOneAgent_\1.0.51\Dynatrace-OneAgent-Windows.exe



   - running installation



   - cleaning up



   Done



   Successfully installed DynatraceOneAgent_ 1.0.51
   ```

   * В Dynatrace перейдите в **Deployment Status**. Найдите недавно подключённые EC2-хосты, чтобы проверить результат установки.
7. Перезапустите все процессы, которые вы хотите мониторить. Вам будет показан список процессов, которые необходимо перезапустить. Обратите внимание, что вы можете перезапустить процессы в любое время, даже во время следующего планового окна обслуживания. Однако до перезапуска всех процессов вы будете видеть только ограниченный набор метрик, например использование ЦП или памяти.

## Параметры установки

Пакет дистрибьютора `DynatraceOneAgent` предоставляет ряд параметров, специфичных для Dynatrace, которые напрямую соответствуют параметрам установки OneAgent.

Узнайте больше о настройке установки OneAgent для [Linux](../../../dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux.md "Learn how to use the Linux installer with command line parameters.") и [Windows](../../../dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows.md "Learn how to use the OneAgent installer for Windows.").

1

Помните, что `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` и `SSM_DYNATRACE_TOKEN_SECRET_ID` являются взаимоисключающими. Выберите один из них.

## Устранение неполадок

* [Установка пакета завершается с ошибкой 'You need to specify 'Additional Arguments' error'](https://dt-url.net/mt638ef)
* [Установка пакета завершается с ошибкой 'ERROR: wrong Dynatrace URL'](https://dt-url.net/lj838gb)
* [Установка пакета завершается с ошибкой 'ERROR: Can't retrieve Dynatrace PaaS token from secret store'](https://dt-url.net/uga38ao)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](../../../technology-support/oneagent-platform-and-capability-support-matrix.md "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")