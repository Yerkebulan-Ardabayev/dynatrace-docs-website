---
title: Соответствие FIPS для ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance
scraped: 2026-03-05T21:34:05.450636
---

# Соответствие ActiveGate стандарту FIPS


* Актуальная версия Dynatrace

ActiveGate версии 1.315+

## Что такое FIPS?

Федеральный стандарт обработки информации (FIPS) — это стандарт, разработанный для принятия и использования федеральными ведомствами и агентствами в Лаборатории информационных технологий и опубликованный NIST, подразделением Министерства торговли США. Стандарт FIPS охватывает определённую тему в области информационных технологий для достижения общего уровня качества или определённого уровня совместимости (источник: [глоссарий NIST](https://csrc.nist.gov/glossary/term/federal_information_processing_standard)).

Соответствие FIPS означает, что продукт соблюдает все требования безопасности, установленные стандартом.

## Режим ActiveGate, совместимый с FIPS

ActiveGate, развёрнутый в режиме совместимости с FIPS, использует криптографические библиотеки, сертифицированные FIPS:

* Amazon Corretto Crypto Provider 2.4.1 (использующий AWS-LC-FIPS 2.x в качестве криптографического модуля, см. [Сертификат #4816](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4816))
* BouncyCastle 2.0.0 (см. [Сертификат #4743](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4743))

## Совместимость назначений ActiveGate

1

исключая [модуль Extension Execution Controller](capabilities/routing-monitoring-purpose.md#extn "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.") (аналогично обычному ActiveGate без FIPS).

2

см. [Требования и ограничения](../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md#fips-compliant-limitation "Узнайте, как создать частную локацию для синтетического мониторинга.") для совместимости синтетического мониторинга с FIPS.

### Развёртывание ActiveGate на хосте

Режим совместимости с FIPS может быть включён во время установки ActiveGate. Подробности см. в разделе [Настройка установки ActiveGate на Linux](installation/linux/linux-customize-installation-for-activegate.md#fips-compliant-mode "Узнайте о параметрах командной строки, которые можно использовать с ActiveGate на Linux.").

#### Требования

* Linux x86-64 или ARM64 (AArch64)
* Операционная система с включённым режимом совместимости с FIPS

  + Установщик ActiveGate проверяет конфигурацию операционной системы, проверяя, равно ли значение статуса режима совместимости FIPS, хранящееся в `/proc/sys/crypto/fips_enabled`, значению `1`
  + Если установщик ActiveGate запущен в режиме совместимости с FIPS, в то время как операционная система не имеет включённого режима совместимости FIPS, установщик останавливается и завершается с ошибкой

### Контейнеризированное развёртывание ActiveGate

Контейнеризированные развёртывания ActiveGate используют образы, совместимые с FIPS, которые доступны для следующих архитектур:

* x86-64
* ARM64 (AArch64)

#### Реестры контейнеров

Образы ActiveGate, совместимые с FIPS, доступны в наших [поддерживаемых публичных реестрах](../setup-on-k8s/guides/container-registries/use-public-registry.md#supported-public-registries "Использование публичного реестра") с суффиксом тега образа `-fips`.

Пример: `public.ecr.aws/dynatrace/dynatrace-activegate:1.315.70.20241127-162512-fips`

См. раздел [Настройка DynaKube для использования образов из публичного реестра](../setup-on-k8s/guides/container-registries/use-public-registry.md#configure-dynakube-to-use-images-from-public-registry "Использование публичного реестра") для получения информации о том, как указать Dynatrace Operator использовать образы из публичного реестра.

### Проверка режима совместимости с FIPS

### Веб-интерфейс

Чтобы проверить, работает ли ActiveGate в режиме совместимости с FIPS:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. Найдите интересующий ActiveGate и раскройте строку таблицы.
3. Найдите свойство **FIPS mode**.

   * Если вы видите **FIPS mode** со значением `True`, ActiveGate работает в режиме совместимости с FIPS.
   * Если вы не видите **FIPS mode**, ActiveGate не работает в режиме совместимости с FIPS.

Чтобы вывести список всех ActiveGate, работающих в режиме совместимости с FIPS:

1. Перейдите в **Deployment Status** > **ActiveGates**.
2. В строке фильтра выберите фильтр **FIPS mode**, затем выберите `True`.

### REST API

Чтобы использовать API Dynatrace для проверки того, работает ли конкретный ActiveGate в режиме совместимости с FIPS, используйте [GET an ActiveGate](../../dynatrace-api/environment-api/activegates/activegate-info/get-activegate.md "Просмотр конфигурации указанного ActiveGate через API Dynatrace.") для проверки значения поля `fipsMode`.

Чтобы использовать API Dynatrace для получения списка всех ActiveGate, работающих в режиме совместимости с FIPS, используйте [GET all ActiveGates](../../dynatrace-api/environment-api/activegates/activegate-info/get-all.md "Список всех ActiveGate, подключённых в данный момент или недавно подключавшихся к среде.") с параметром запроса `fipsMode`.

### Логи

Чтобы проверить, работает ли ActiveGate в режиме совместимости с FIPS, найдите следующую запись в логах ActiveGate (ниже описано, как получить доступ к логам в зависимости от типа развёртывания ActiveGate):

```
2025-06-10 12:16:14 UTC INFO    [<tenant>] [FipsDetector] FIPS mode active: true
```

Когда `FIPS mode active` имеет значение `true`, все библиотеки и конфигурация, связанные с соответствием FIPS, правильно инициализированы, и ActiveGate работает в режиме совместимости с FIPS.

Если ActiveGate был установлен в режиме совместимости с FIPS или использовался образ, совместимый с FIPS, но инициализация библиотек FIPS завершилась неудачей или отсутствует необходимая конфигурация, ActiveGate отменяет запуск и записывает следующие записи в файл лога:

```
ActiveGate FIPS mode initialization failed
```

Кроме того, строка лога описывает конкретную причину сбоя инициализации.

#### Доступ к логам при развёртывании на хосте

Файлы логов ActiveGate имеют шаблон имени `dynatracegateway.0.<number>.log` и находятся в каталоге логов ActiveGate (см. [Каталоги ActiveGate](configuration/where-can-i-find-activegate-files.md#default-activegate-directories "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.")).

#### Доступ к логам при контейнеризированном развёртывании

Логи контейнеризированных ActiveGate можно получить с помощью следующей команды:
`kubectl -n <NAMESPACE> logs statefulset.apps/<DYNAKUBE_NAME>-activegate`
Если настроено несколько реплик, будут возвращены логи одного пода.

Чтобы получить логи конкретного пода, используйте следующую команду:
`kubectl -n <NAMESPACE> logs pod/<DYNAKUBE_NAME>-activegate-<REPLICA_NUMBER>`

## Поддерживаемые наборы шифров
