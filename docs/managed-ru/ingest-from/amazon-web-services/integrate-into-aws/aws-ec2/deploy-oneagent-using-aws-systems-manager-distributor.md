---
title: Deploy OneAgent using AWS Systems Manager Distributor
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor
scraped: 2026-05-12T11:14:17.047906
---

# Развёртывание OneAgent через AWS Systems Manager Distributor

# Развёртывание OneAgent через AWS Systems Manager Distributor

* Практическое руководство
* Чтение: 8 мин
* Обновлено 12 января 2024 г.

С помощью [AWS Systems Manager Distributor](https://docs.aws.amazon.com/systems-manager/latest/userguide/distributor.html) можно распространять и автоматически развёртывать OneAgent на ваших EC2-инстансах через AWS Systems Manager Distributor.

## Предварительные условия

Перед развёртыванием пакета дистрибьютора `DynatraceOneAgent` убедитесь, что ваши инстансы Amazon EC2 удовлетворяют следующим требованиям:

### AWS-теги

AWS-теги в метаданных инстанса по умолчанию выключены при запуске. Чтобы их включить, следуйте официальной [документации AWS](https://dt-url.net/k2038k6).

### AWS Systems Manager

AWS Systems Manager должен быть настроен для вашей учётной записи AWS, а AWS Systems Manager Agent (SSM Agent) должен быть установлен на EC2-инстансах, где вы планируете развернуть пакет дистрибьютора `DynatraceOneAgent`. Следуйте [AWS Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html) либо более подробному [Setting up AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up.html).

### Поддерживаемые операционные системы

Пакет дистрибьютора `DynatraceOneAgent` поддерживается в следующих операционных системах:

| Операционная система | Версия | Архитектура |
| --- | --- | --- |
| Windows | [Все поддерживаемые версии OneAgent](/managed/ingest-from/technology-support "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") | x86-64, |
| Amazon Linux | [Все поддерживаемые версии OneAgent](/managed/ingest-from/technology-support "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Ubuntu | 16.04, 18.04, 22.04 | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |
| Red Hat Enterprise Linux | 8.x, 9.x | x86-64 |
| SUSE Enterprise Linux | 15.x | x86-64, ARM64 (AArch64[1](#fn-1-1-def)) |

1

Поддержка архитектуры ARM64, включая [процессоры AWS Graviton](https://aws.amazon.com/ec2/graviton/), находится в стадии [Early Access release](https://www.dynatrace.com/news/blog/get-out-of-the-box-visibility-into-your-arm-platform-early-adopter/).

### Wget

Пакету дистрибьютора Dynatrace OneAgent требуется установленный `Wget` на вашем Linux-инстансе. Если `Wget` не установлен, пакет дистрибьютора OneAgent установит его автоматически. `Wget` нужен для загрузки последней версии OneAgent.

### AWS CLI

AWS CLI обязателен, если вы используете Parameter Store или Secrets Manager для хранения PaaS-токена. Если AWS CLI не установлен, пакет дистрибьютора OneAgent установит последнюю версию.

Если на вашем инстансе работает AWS CLI версии 1, нужно добавить параметр `SSM_DYNATRACE_TOKEN_REGION` со значением региона, в котором запущен инстанс, в конфигурацию SSM Distributor, потому что автоопределение региона через EC2 IMDS доступно только в AWS CLI версии 2.

## Ограничения

Развёртывание OneAgent через AWS Systems Manager Distributor сейчас не поддерживается, если в качестве значения параметра `SSM_DYNATRACE_URL` указан кластер Dynatrace Managed.

## Установка

Чтобы установить пакет дистрибьютора `DynatraceOneAgent`

1. Откройте [консоль AWS Systems Manager](https://dt-url.net/ug6387o).
2. На панели навигации выберите **Distributor**.
3. На странице Distributor выберите **Third party** и пакет `DynatraceOneAgent`.
4. Выберите режим установки. Пакет `DynatraceOneAgent` можно установить или обновить однократно, либо запланировать установку. Подробности об установке пакетов Distributor см. в [документации AWS Systems Manager Distributor](https://dt-url.net/bv438ci).
5. Чтобы настроить установку пакета `DynatraceOneAgent`, добавьте [параметры](#installation-parameters) в поле **Additional Arguments** в **Systems Manager Run Command**.
   Параметрам нужен [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").

   Для передачи PaaS-токена рекомендуется использовать централизованную систему управления облачными секретами, например [AWS Secrets Manager](https://dt-url.net/2803808) или [Parameter Store](https://dt-url.net/3y238xf).

   * Передать PaaS-токен через **AWS Secrets Manager** Рекомендуется

     1. Создайте секрет:

        ```
        aws secretsmanager create-secret --name dynatrace-paas-token --secret-string "paas_token_value"
        ```
     2. Добавьте IAM-политику к IAM-роли, прикреплённой к вашим EC2-инстансам, которая разрешает получать секрет из Secrets Manager. Пример политики, прикреплённой к IAM-роли (другие варианты см. в [AWS User Guide](https://dt-url.net/7k838d2)):

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

        Если ваш секрет зашифрован CMK KMS Key, также нужно выдать права Decrypt и в IAM-роли, и в политике KMS Key. Подробнее см. в [документации AWS Secrets Manager](https://dt-url.net/3pa38cu).
     3. Передайте имя секрета через `SSM_DYNATRACE_TOKEN_SECRET_ID` в **параметрах пакета SSM Distributor**. Пример:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN_SECRET_ID" : "dynatrace-paas-token"



        }
        ```
   * Передать PaaS-токен через **Parameter Store** Рекомендуется

     1. Создайте параметр типа `SecureString`.

        ```
        aws ssm put-parameter --name "dynatrace-paas-token" --value "paas_token_value" --type "SecureString"
        ```
     2. Добавьте IAM-политику к IAM-роли, прикреплённой к вашим EC2-инстансам, которая разрешает получать секрет из Parameter Store. Пример политики. Подробнее см. в [документации AWS Systems Manager](https://dt-url.net/3nc38v5).

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
     3. Передайте имя секрета через `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` в параметрах SSM Distributor. Пример:

        ```
        {



        "SSM_DYNATRACE_URL" : "https://environment.live.dynatrace.com/",



        "SSM_DYNATRACE_TOKEN" : "abcdefghij123456",



        }
        ```
   * Передать PaaS-токен через переменную окружения `SSM_DYNATRACE_TOKEN`. не рекомендуется

     Использование параметра `SSM_DYNATRACE_TOKEN` небезопасно, потому что PaaS-токен будет виден в истории [Run Command](https://dt-url.net/bf038x6).

   Пример: дополнительные аргументы в Systems Manager Run Command

   ![AWS distributor](https://dt-cdn.net/images/aws-distributor-1281-19fb123371.png)

   AWS distributor

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

   * После запуска установки следите за прогрессом в области **Command status**. Статус **Success** означает успешную установку.

   Пример: вывод успешной установки

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
7. Перезапустите все процессы, которые хотите мониторить. Вам покажут список процессов, которые нужно перезапустить. Перезапустить процессы можно в любое время, в том числе во время ближайшего планового обслуживания вашей организации. Однако до перезапуска всех процессов будет виден только ограниченный набор метрик, например потребление CPU или памяти.

## Параметры установки

Пакет дистрибьютора `DynatraceOneAgent` предоставляет ряд параметров, специфичных для Dynatrace, которые напрямую сопоставляются с параметрами установки OneAgent.

Подробнее о настройке установки OneAgent см. для [Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать Linux-установщик с параметрами командной строки.") и [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.").

| Параметр Distributor | Соответствует параметру OneAgent | Значение по умолчанию | Описание |
| --- | --- | --- | --- |
| `SSM_DYNATRACE_URL` | `--set-server` | зависит от окружения | Адрес коммуникационной конечной точки OneAgent, это компонент Dynatrace, в который OneAgent отправляет данные. В зависимости от развёртывания это может быть кластер Dynatrace SaaS или ActiveGate. Кластер Dynatrace Managed сейчас не поддерживается. **Примечание**: убедитесь, что в конце URL добавлен слэш (например, `https://environment.live.dynatrace.com/`). |
| `SSM_DYNATRACE_HOST_GROUP` | `--set-host-group` | не задано | Имя [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью host groups."), к которой нужно отнести хост. |
| `SSM_DYNATRACE_MONITORING_MODE` | `--set-monitoring-mode` | fullstack | При значении `infra-only` активирует [режим инфраструктурного мониторинга](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.") вместо режима Full-Stack Monitoring. При этом подходе вы получаете только инфраструктурные данные о состоянии, без данных о приложениях или производительности пользователей. |
| `SSM_DYNATRACE_APP_LOG_CONTENT_ACCESS` | `--set-app-log-content-access` | true | При значении `true` разрешает OneAgent доступ к лог-файлам для целей [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить Log Monitoring, какие возможности он предоставляет, и многое другое."). |
| `SSM_DYNATRACE_TOKEN_SECRET_ID` [1](#fn-2-1-def) | N/A | N/A | Имя или ARN **секрета** [PaaS-токена](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Ознакомьтесь с концепцией токенов доступа.") в Secrets Manager, используется для получения значения [PaaS-токена](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Ознакомьтесь с концепцией токенов доступа."). |
| `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` [1](#fn-2-1-def) | N/A | N/A | Имя **параметра** [PaaS-токена](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Ознакомьтесь с концепцией токенов доступа.") в Parameter Store, используется для получения значения [PaaS-токена](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Ознакомьтесь с концепцией токенов доступа."). |
| `SSM_DYNATRACE_TOKEN_REGION` | N/A | N/A | Необязательный регион AWS, используется для получения секрета из другого региона. Если не задан, **AWS CLI автоматически определяет регион инстанса**. (Этот параметр **обязателен**, если вы используете AWS CLI v1, потому что он не может определить регион инстанса через EC2 IMDS). |
| `SSM_DYNATRACE_TOKEN` не рекомендуется | N/A | N/A | [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy "Ознакомьтесь с концепцией токенов доступа."), используется для загрузки установщика OneAgent. Использование параметра `SSM_DYNATRACE_TOKEN` небезопасно, потому что PaaS-токен будет виден в истории Run Command. Используйте AWS Secrets Manager или AWS Systems Manager Parameter Store. |

1

Помните, что `SSM_DYNATRACE_TOKEN_PARAMETER_NAME` и `SSM_DYNATRACE_TOKEN_SECRET_ID` взаимоисключающие. Выберите один из них.

## Устранение неполадок

* [My package installation fails with 'You need to specify 'Additional Arguments' error'](https://dt-url.net/mt638ef)
* [My package installation fails with 'ERROR: wrong Dynatrace URL'](https://dt-url.net/lj838gb)
* [My package installation fails with 'ERROR: Can't retrieve Dynatrace PaaS token from secret store'](https://dt-url.net/uga38ao)

## Связанные темы

* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в разных операционных системах и платформах.")