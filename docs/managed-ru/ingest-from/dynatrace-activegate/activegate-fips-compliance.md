---
title: Соответствие FIPS для ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance
---

# Соответствие FIPS для ActiveGate

# Соответствие FIPS для ActiveGate

* Обновлено 12 мая 2026 г.

ActiveGate версии 1.315+

## Что такое FIPS?

Federal Information Processing Standard (FIPS), это «стандарт для принятия и использования федеральными департаментами и агентствами, разработанный в Information Technology Laboratory и опубликованный NIST, подразделением Министерства торговли США. FIPS охватывает ту или иную тему в области информационных технологий для достижения единого уровня качества или определённого уровня совместимости» (источник: [глоссарий NIST﻿](https://csrc.nist.gov/glossary/term/federal_information_processing_standard)).

Соответствие FIPS означает, что продукт отвечает всем требованиям безопасности, установленным этим стандартом.

## Режим ActiveGate, совместимый с FIPS

ActiveGate, развёрнутый в режиме, совместимом с FIPS, использует криптографические библиотеки, сертифицированные по FIPS:

ActiveGate 1.341+

ActiveGate до версии 1.339

* Amazon Corretto Crypto Provider 2.4.1 (использует AWS-LC-FIPS 2.x в качестве криптографического модуля; подробности см. в [сертификате №4816﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.1.2 (подробности см. в [сертификате №4943﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4943))

* Amazon Corretto Crypto Provider 2.4.1 (использует AWS-LC-FIPS 2.x в качестве криптографического модуля; подробности см. в [сертификате №4816﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.0.0 (подробности см. в [сертификате №4743﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743))

## Совместимость назначений ActiveGate

| Назначение | x86-64 | arm64 |
| --- | --- | --- |
| [Routing-monitoring](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Узнайте о возможностях и способах использования ActiveGate.") | Применимо | Применимо[1](#fn-1-1-def) |
| [Synthetic monitoring в приватной локации](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate, предназначенные для synthetic-мониторинга внутренних и внешних ресурсов из приватных Synthetic-локаций") | Применимо[2](#fn-1-2-def) | Не применимо |
| [Мониторинг z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS.") | Применимо | Не применимо |

1

за исключением модуля [Extension Execution Controller](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Узнайте о возможностях маршрутизации и мониторинга и способах использования ActiveGate.") (так же, как и для обычного, не-FIPS ActiveGate).

2

требования и ограничения для соответствия FIPS в Synthetic см. в разделе [Требования и ограничения](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#fips-compliant-limitation "Узнайте, как создать приватную локацию для synthetic-мониторинга.").

### Развёртывание ActiveGate на хосте

Режим, совместимый с FIPS, можно включить во время установки ActiveGate. Подробности см. в разделе [Настройка установки ActiveGate в Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate в Linux.").

#### Требования

* Linux x86-64 или ARM64 (AArch64)
* Операционная система с включённым режимом, совместимым с FIPS

  + Установщик ActiveGate проверяет конфигурацию операционной системы, проверяя, равен ли статус режима, совместимого с FIPS, хранящийся в `/proc/sys/crypto/fips_enabled`, значению `1`
  + Если установщик ActiveGate запущен в режиме, совместимом с FIPS, а в операционной системе этот режим не включён, установщик останавливается и завершается с ошибкой

### Контейнеризованное развёртывание ActiveGate

Контейнеризованные развёртывания ActiveGate опираются на образы, совместимые с FIPS, доступные для следующих архитектур:

* x86-64
* ARM64 (AArch64)

#### Реестры контейнеров

Образы ActiveGate, совместимые с FIPS, доступны в наших [поддерживаемых публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройте Operator Dynatrace на использование образов из публичного реестра для себя и своих управляемых компонентов. Это можно сделать вручную или через автоматическое разрешение из вашего окружения Dynatrace.") с суффиксом тега образа `-fips`.

Пример: `public.ecr.aws/dynatrace/dynatrace-activegate:1.315.70.20241127-162512-fips`

Подробности о том, как указать Operator Dynatrace использовать образы из публичного реестра, см. в разделе [Настройка DynaKube на использование образов из публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#configure-dynakube-to-use-images-from-public-registry "Настройте Operator Dynatrace на использование образов из публичного реестра для себя и своих управляемых компонентов. Это можно сделать вручную или через автоматическое разрешение из вашего окружения Dynatrace.").

### Проверка режима, совместимого с FIPS

### Web UI

Dynatrace версии 1.317+

Чтобы проверить, работает ли ActiveGate в режиме, совместимом с FIPS

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Найдите нужный ActiveGate и разверните строку таблицы.
3. Найдите свойство **FIPS mode**.

   * Если свойство **FIPS mode** имеет значение `True`, ActiveGate работает в режиме, совместимом с FIPS.
   * Если свойство **FIPS mode** отсутствует, ActiveGate не работает в режиме, совместимом с FIPS.

Чтобы вывести список всех ActiveGate, работающих в режиме, совместимом с FIPS

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. В строке фильтра выберите фильтр **FIPS mode** и затем выберите `True`.

### REST API

Dynatrace версии 1.317+

Чтобы с помощью API Dynatrace проверить, работает ли конкретный ActiveGate в режиме, совместимом с FIPS, используйте [GET an ActiveGate](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-activegate "Просмотрите конфигурацию указанного ActiveGate через API Dynatrace.") и проверьте значение поля `fipsMode`.

Чтобы с помощью API Dynatrace вывести список всех ActiveGate, работающих в режиме, совместимом с FIPS, используйте [GET all ActiveGates](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all "Выведите список всех ActiveGate, которые в настоящее время или недавно были подключены к окружению.") с параметром запроса `fipsMode`.

### Логи

Чтобы проверить, работает ли ActiveGate в режиме, совместимом с FIPS, найдите следующую запись в логах ActiveGate (ниже описано, как получить доступ к логам в зависимости от типа развёртывания ActiveGate):

```
2025-06-10 12:16:14 UTC INFO    [<tenant>] [FipsDetector] FIPS mode active: true
```

Если `FIPS mode active` имеет значение `true`, все библиотеки и конфигурация, связанные с соответствием FIPS, корректно инициализированы, и ActiveGate работает в режиме, совместимом с FIPS.

Если ActiveGate был установлен в режиме, совместимом с FIPS, или использовался образ, совместимый с FIPS, но инициализация библиотек FIPS завершилась ошибкой либо отсутствует необходимая конфигурация, ActiveGate прерывает запуск и записывает в лог-файл следующие строки:

```
ActiveGate FIPS mode initialization failed
```

Дополнительно строка лога описывает конкретную причину ошибки инициализации.

#### Доступ к логам при развёртывании на хосте

Файлы логов ActiveGate имеют шаблон имени `dynatracegateway.0.<number>.log` и находятся в каталоге логов ActiveGate (см. [Каталоги ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.")).

#### Доступ к логам при контейнеризованном развёртывании

Логи контейнеризованных ActiveGate можно получить с помощью следующей команды:
`kubectl -n <NAMESPACE> logs statefulset.apps/<DYNAKUBE_NAME>-activegate`
Если настроено несколько реплик, будут возвращены логи одного пода.

Чтобы получить логи конкретного пода, используйте следующую команду:
`kubectl -n <NAMESPACE> logs pod/<DYNAKUBE_NAME>-activegate-<REPLICA_NUMBER>`

## Поддерживаемые наборы шифров

| Набор шифров | Версия TLS |
| --- | --- |
| [`TLS_AES_256_GCM_SHA384`﻿](https://ciphersuite.info/cs/TLS_AES_256_GCM_SHA384) | TLS1.3 |
| [`TLS_AES_128_GCM_SHA256`﻿](https://ciphersuite.info/cs/TLS_AES_128_GCM_SHA256) | TLS1.3 |
| [`TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`﻿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`﻿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384`﻿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256`﻿](https://ciphersuite.info/cs/TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`﻿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`﻿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`﻿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384) | TLS1.2, TLS1.3 |
| [`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`﻿](https://ciphersuite.info/cs/TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256) | TLS1.2, TLS1.3 |