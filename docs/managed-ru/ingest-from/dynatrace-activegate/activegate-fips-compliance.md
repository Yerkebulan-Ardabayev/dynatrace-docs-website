---
title: ActiveGate Соответствие требованиям FIPS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance
---

# ActiveGate Соответствие требованиям FIPS

# ActiveGate Соответствие требованиям FIPS

* Обновлено 20 июля 2026 г.

ActiveGate версии 1.315+

## Что такое FIPS?

Federal Information Processing Standard (FIPS), это «стандарт, принятый и применяемый федеральными министерствами и ведомствами, разработанный в Лаборатории информационных технологий и опубликованный NIST, подразделением Министерства торговли США. Стандарт FIPS охватывает определённую тему в области информационных технологий с целью достижения общего уровня качества или определённого уровня совместимости» (источник: [глоссарий NIST﻿](https://csrc.nist.gov/glossary/term/federal_information_processing_standard)).

Соответствие требованиям FIPS означает, что продукт соблюдает все требования безопасности, установленные стандартом.

## Режим соответствия FIPS в ActiveGate

ActiveGate, развёрнутый в режиме соответствия FIPS, использует криптографические библиотеки, сертифицированные по FIPS:

ActiveGate 1.341+

ActiveGate до 1.339

* Amazon Corretto Crypto Provider 2.4.1 (использует AWS-LC-FIPS 2.x в качестве криптографического модуля; подробнее: [Certificate #4816﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.1.2 (подробнее: [Certificate #4943﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4943))

* Amazon Corretto Crypto Provider 2.4.1 (использует AWS-LC-FIPS 2.x в качестве криптографического модуля; подробнее: [Certificate #4816﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.0.0 (подробнее: [Certificate #4743﻿](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743))

## Совместимость целей ActiveGate

| Цель | x86-64 | arm64 |
| --- | --- | --- |
| [Routing-monitoring](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl "Learn the capabilities and uses of ActiveGate.") | Применимо | Применимо[1](#fn-1-1-def) |
| [Synthetic monitoring in a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations") | Применимо[2](#fn-1-2-def) | Не применимо |
| [z/OS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.") | Применимо | Не применимо |

1

за исключением [модуля Extension Execution Controller](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.") (аналогично обычному ActiveGate без FIPS).

2

см. [Требования и ограничения](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#fips-compliant-limitation "Learn how to create a private location for synthetic monitoring.") по FIPS-совместимости Synthetic.

### Развёртывание ActiveGate на хосте

Режим соответствия FIPS можно включить во время установки ActiveGate. Подробнее: [Настройка установки ActiveGate на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Learn about the command-line parameters that you can use with ActiveGate on Linux.").

#### Требования

* Linux x86-64 или ARM64 (AArch64)
* Операционная система с включённым режимом соответствия FIPS

  + Установщик ActiveGate проверяет конфигурацию операционной системы, проверяя, равно ли значение статуса режима соответствия FIPS, хранящееся в `/proc/sys/crypto/fips_enabled`, значению `1`
  + Если установщик ActiveGate запускается в режиме соответствия FIPS, а в операционной системе этот режим не включён, установщик прекращает работу и завершается с ошибкой

### Контейнерное развёртывание ActiveGate

Контейнерные развёртывания ActiveGate используют FIPS-совместимые образы, доступные для следующих архитектур:

* x86-64
* ARM64 (AArch64)

#### Реестры контейнеров

FIPS-совместимые образы ActiveGate доступны в [поддерживаемых публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") с суффиксом тега образа `-fips`.

Пример: `public.ecr.aws/dynatrace/dynatrace-activegate:1.315.70.20241127-162512-fips`

Подробнее о том, как указать Dynatrace Operator использовать образы из публичного реестра: [Настройка DynaKube для использования образов из публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#configure-dynakube-to-use-images-from-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

### Проверка режима соответствия FIPS

### Web UI

Dynatrace версии 1.317+

Чтобы проверить, работает ли ActiveGate в режиме соответствия FIPS:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Найдите нужный ActiveGate и разверните строку таблицы.
3. Найдите свойство **FIPS mode**.

   * Если **FIPS mode** имеет значение `True`, ActiveGate работает в режиме соответствия FIPS.
   * Если **FIPS mode** отсутствует, ActiveGate не работает в режиме соответствия FIPS.

Чтобы вывести список всех ActiveGates, работающих в режиме соответствия FIPS:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. В строке фильтра выберите фильтр **FIPS mode**, затем выберите значение `True`.

### REST API

Dynatrace версии 1.317+

Чтобы с помощью Dynatrace API проверить, работает ли конкретный ActiveGate в режиме соответствия FIPS, используйте [GET an ActiveGate](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-activegate "View the configuration of the specified ActiveGate via the Dynatrace API.") и проверьте значение поля `fipsMode`.

Чтобы с помощью Dynatrace API вывести список всех ActiveGates, работающих в режиме соответствия FIPS, используйте [GET all ActiveGates](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all "List all ActiveGates currently or recently connected to the environment.") с параметром запроса `fipsMode`.

### Логи

Чтобы проверить, работает ли ActiveGate в режиме соответствия FIPS, найдите следующую запись в логах ActiveGate (способ доступа к логам зависит от типа развёртывания ActiveGate, см. ниже):

```
2025-06-10 12:16:14 UTC INFO    [<tenant>] [FipsDetector] FIPS mode active: true
```

Если `FIPS mode active` равно `true`, все библиотеки и конфигурация, связанные с соответствием FIPS, инициализированы корректно, и ActiveGate работает в режиме соответствия FIPS.

Если ActiveGate был установлен в режиме соответствия FIPS или использовался FIPS-совместимый образ, но инициализация библиотек FIPS завершилась ошибкой либо отсутствует необходимая конфигурация, ActiveGate отменяет запуск и записывает следующие записи в лог-файл:

```
ActiveGate FIPS mode initialization failed
```

Дополнительно в строке лога указывается конкретная причина сбоя инициализации.

#### Доступ к логам при развёртывании на хосте

Лог-файлы ActiveGate имеют шаблон `dynatracegateway.0.<number>.log` и находятся в каталоге логов ActiveGate (см. [Каталоги ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories "Find out where ActiveGate files are stored on Windows and Linux systems.")).

#### Доступ к логам при контейнерном развёртывании

Логи контейнерных ActiveGates можно получить с помощью следующей команды:
`kubectl -n <NAMESPACE> logs statefulset.apps/<DYNAKUBE_NAME>-activegate`
Если настроено несколько реплик, возвращаются логи одного пода.

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