---
title: FIPS-совместимость ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance
scraped: 2026-05-12T11:36:38.406404
---

# FIPS-совместимость ActiveGate

# FIPS-совместимость ActiveGate

* Updated on Jul 15, 2025

ActiveGate версии 1.315+

## Что такое FIPS?

Federal Information Processing Standard (FIPS) — «стандарт для принятия и использования федеральными департаментами и агентствами, разработанный в Information Technology Laboratory и опубликованный NIST, частью Министерства торговли США. FIPS охватывает некоторую тему в информационных технологиях для достижения общего уровня качества или определённого уровня совместимости» (источник: [Глоссарий NIST](https://csrc.nist.gov/glossary/term/federal_information_processing_standard)).

FIPS-совместимость означает, что продукт соответствует всем требованиям безопасности, предусмотренным стандартом.

## Режим FIPS-совместимости ActiveGate

ActiveGate, развёрнутый в режиме FIPS-совместимости, использует FIPS-сертифицированные криптографические библиотеки:

* Amazon Corretto Crypto Provider 2.4.1 (использует AWS-LC-FIPS 2.x в качестве криптографического модуля, смотрите [Сертификат #4816](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.0.0 (смотрите [Сертификат #4743](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743))

## Совместимость назначений ActiveGate

| Назначение | x86-64 | arm64 |
| --- | --- | --- |
| [Routing-monitoring](/managed/ingest-from/dynatrace-activegate/capabilities#functional_tbl) | Применимо | Применимо (кроме Extension Execution Controller) |
| [Синтетический мониторинг в частном расположении](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose) | Применимо (см. ограничения) | Не применимо |
| [Мониторинг z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose) | Применимо | Не применимо |

### Развёртывание ActiveGate на основе хоста

Режим FIPS-совместимости можно включить во время установки ActiveGate. Подробнее смотрите в разделе [Настройка установки ActiveGate на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#fips-compliant-mode "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.").

#### Требования

* Linux x86-64 или ARM64 (AArch64)
* Операционная система с включённым режимом FIPS-совместимости

  + Установщик ActiveGate проверяет конфигурацию ОС, проверяя, равно ли значение статуса режима FIPS-совместимости, хранящегося в `/proc/sys/crypto/fips_enabled`, значению `1`
  + Если установщик ActiveGate запущен в режиме FIPS-совместимости, а ОС не имеет включённого режима FIPS-совместимости, установщик останавливается и завершается с ошибкой

### Контейнерное развёртывание ActiveGate

Контейнерные развёртывания ActiveGate используют FIPS-совместимые образы, доступные для следующих архитектур:

* x86-64
* ARM64 (AArch64)

#### Реестры контейнеров

FIPS-совместимые образы ActiveGate доступны в поддерживаемых [публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использовать публичный реестр") с суффиксом тега образа `-fips`.

Пример: `public.ecr.aws/dynatrace/dynatrace-activegate:1.315.70.20241127-162512-fips`

Подробнее о настройке DynaKube для использования образов из публичного реестра смотрите в разделе [Настройка DynaKube для использования образов из публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#configure-dynakube-to-use-images-from-public-registry "Использовать публичный реестр").

### Проверка режима FIPS-совместимости

### Веб-интерфейс

Dynatrace версии 1.317+

Чтобы проверить, работает ли ActiveGate в режиме FIPS-совместимости:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Найдите интересующий ActiveGate и разверните строку таблицы.
3. Найдите свойство **FIPS mode**.

   * Если вы находите **FIPS mode** со значением `True`, ActiveGate работает в режиме FIPS-совместимости.
   * Если **FIPS mode** не найден, ActiveGate не работает в режиме FIPS-совместимости.

Чтобы получить список всех ActiveGate, работающих в режиме FIPS-совместимости:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. В строке фильтра выберите фильтр **FIPS mode** и затем выберите `True`.

### REST API

Dynatrace версии 1.317+

Для проверки через Dynatrace API, работает ли конкретный ActiveGate в режиме FIPS-совместимости, используйте [GET an ActiveGate](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-activegate "Просмотрите конфигурацию указанного ActiveGate через Dynatrace API.") и проверьте значение поля `fipsMode`.

Для получения списка всех ActiveGate, работающих в режиме FIPS-совместимости, используйте [GET all ActiveGates](/managed/dynatrace-api/environment-api/activegates/activegate-info/get-all "Список всех ActiveGate, подключённых или недавно подключавшихся к окружению.") с параметром запроса `fipsMode`.

### Логи

Для проверки режима FIPS-совместимости ActiveGate найдите следующую запись в логах ActiveGate:

```
2025-06-10 12:16:14 UTC INFO    [<tenant>] [FipsDetector] FIPS mode active: true
```

Когда `FIPS mode active` имеет значение `true`, все библиотеки и конфигурации, связанные с FIPS-совместимостью, правильно инициализированы и ActiveGate работает в режиме FIPS-совместимости.

Если ActiveGate был установлен в режиме FIPS-совместимости или использовался FIPS-совместимый образ, но инициализация FIPS-библиотек завершилась неудачей или необходимая конфигурация отсутствует, ActiveGate отменяет запуск и записывает в лог файл следующие записи:

```
ActiveGate FIPS mode initialization failed
```

Дополнительно в строке лога описывается конкретная причина сбоя инициализации.

#### Доступ к логам при развёртывании на основе хоста

Файлы логов ActiveGate имеют шаблон `dynatracegateway.0.<number>.log` и находятся в директории логов ActiveGate (смотрите [Директории ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories "Узнайте, где хранятся файлы ActiveGate на Windows и Linux.")).

#### Доступ к логам при контейнерном развёртывании

Логи контейнерных ActiveGate можно получить следующей командой:
`kubectl -n <NAMESPACE> logs statefulset.apps/<DYNAKUBE_NAME>-activegate`

Для получения логов из конкретного пода:
`kubectl -n <NAMESPACE> logs pod/<DYNAKUBE_NAME>-activegate-<REPLICA_NUMBER>`

## Поддерживаемые наборы шифров

| Набор шифров | Версия TLS |
| --- | --- |
| `TLS_AES_256_GCM_SHA384` | TLS1.3 |
| `TLS_AES_128_GCM_SHA256` | TLS1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384` | TLS1.2, TLS1.3 |
| `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256` | TLS1.2, TLS1.3 |