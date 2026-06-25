---
title: Проверка подписей образов Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature
scraped: 2026-05-12T12:06:14.953057
---

# Проверка подписей образов Dynatrace

# Проверка подписей образов Dynatrace

* Чтение: 4 мин
* Обновлено 16 апреля 2026 г.

В современных условиях атаки на цепочку поставок стали распространённым вектором угроз. Наш подход к противодействию этому риску заключается в поставке неизменяемых и подписанных образов, которые служат основой для усиления мер безопасности.

На этой странице описан процесс проверки подписей образов Dynatrace, что позволяет установить подлинность и защитить целостность ПО.

## Предварительные требования

Прежде чем начать, убедитесь, что выполнены следующие предварительные требования:

* Обязательно [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) для проверки подписи образов
* Необязательно [GitHub CLI](https://cli.github.com/) для проверки происхождения SLSA через GitHub attestation API
* Обязательно Доступ на чтение к репозиториям образов Dynatrace при использовании частного реестра

## Проверка подписей образов с помощью Cosign

В следующих разделах описано, как проверять подписи образов Dynatrace с помощью Cosign. Для простоты во всех примерах используются репозитории компонентов Dynatrace в публичном Amazon ECR, однако они верны и применимы к любому реестру, содержащему образы Dynatrace.

Если вы ищете альтернативы Amazon ECR, см. [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

Подписание образов выполняется только для образов Dynatrace из поддерживаемых публичных реестров. Образы во встроенном реестре Dynatrace не подписываются.

Dynatrace подписывает образы с помощью Cosign, но в публичный журнал прозрачности Sigstore выгружаются данные о подписи только для Dynatrace Operator. Это позволяет выполнять стандартную проверку для Operator. Для остальных образов при проверке требуется флаг `--insecure-ignore-tlog`.

### Dynatrace Operator

Dynatrace Operator является проектом с открытым исходным кодом, который размещается и собирается на GitHub. Поэтому подписание и проверка немного отличаются от других компонентов Dynatrace.

Проверка без ключа

Проверка по открытому ключу

Следующая команда показывает способ проверки подписи образа Dynatrace Operator без ключа:

```
cosign verify --certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

Следующая команда показывает, как проверить подпись образа Dynatrace Operator с помощью открытого ключа соответствующего релиза GitHub:

```
cosign verify --key https://github.com/Dynatrace/dynatrace-operator/releases/download/<tag>/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

### Dynatrace ActiveGate

Следующая команда показывает, как проверить подпись образа Dynatrace ActiveGate с помощью открытого ключа из `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-activegate:<tag>
```

### Dynatrace Code Modules

Следующая команда показывает, как проверить подпись образа Dynatrace Code Modules с помощью открытого ключа из `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>
```

### Dynatrace OneAgent

Следующая команда показывает, как проверить подпись образа Dynatrace OneAgent с помощью открытого ключа из `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

### Dynatrace Kubernetes Node Configuration Collector

Следующая команда показывает, как проверить подпись образа Dynatrace Kubernetes Node Configuration Collector с помощью открытого ключа из `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag>
```

### Dynatrace EdgeConnect

Следующая команда показывает, как проверить подпись образа Dynatrace EdgeConnect с помощью открытого ключа из `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

## Проверка аттестации спецификации состава ПО (SBOM)

Аттестации позволяют пользователям подтвердить, что спецификация состава ПО (SBOM) поступает из доверенного источника в цепочке поставок ПО. Доверяя заявлению производителя образа контейнера о включённом ПО, пользователи могут безопасно интегрировать SBOM в свои рабочие процессы.

### Dynatrace Operator

Используйте следующую команду для проверки аттестации спецификации состава ПО (SBOM)[1](#fn-1-1-def) образа Dynatrace Operator[2](#fn-1-2-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Поддерживается с версии Dynatrace Operator 0.12.0.

2

Образ Dynatrace Operator доступен в Amazon ECR начиная с версии 1.0.0. Дополнительные сведения см. в разделе [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

Извлечение файла SBOM из вывода проверки

SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив приведённую выше команду фильтрами `jq`[3](#fn-2-3-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

3

[jq CLI](https://jqlang.github.io/jq/) является полезным инструментом для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace Operator.

### Dynatrace ActiveGate

ActiveGate версии 1.303+

Используйте следующую команду для проверки аттестации спецификации состава ПО (SBOM) образа Dynatrace ActiveGate.
Обязательно укажите нужную архитектуру ЦП. Доступны варианты `amd64`, `arm64` и `s390x`.

```
digest=$(docker manifest inspect public.ecr.aws/dynatrace/dynatrace-activegate:<tag> | \



jq -r '.manifests[] | select(.platform.architecture=="amd64") | .digest')



cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest
```

Извлечение файла SBOM из вывода проверки

SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив приведённую выше команду фильтрами `jq`[1](#fn-3-1-def):

```
cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

[jq CLI](https://jqlang.github.io/jq/) является полезным инструментом для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace ActiveGate.

### Dynatrace EdgeConnect

EdgeConnect версии 1.473+

Используйте следующую команду для проверки аттестации спецификации состава ПО (SBOM) образа Dynatrace EdgeConnect.

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

Извлечение файла SBOM из вывода проверки

SBOM в формате CycloneDX можно извлечь из аттестации in-toto, дополнив приведённую выше команду фильтрами `jq`[1](#fn-4-1-def):

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

[jq CLI](https://jqlang.github.io/jq/) является полезным инструментом для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace EdgeConnect.

## Проверка аттестации происхождения сборки SLSA

Аттестации происхождения сборки [SLSA](https://slsa.dev) предоставляют проверяемую запись о том, где и как был собран образ контейнера. Проверка этих аттестаций подтверждает, что образ создан ожидаемым исходным репозиторием и рабочим процессом сборки, защищая от подмены в процессе сборки и распространения.

### Dynatrace Operator

Cosign

GitHub CLI

Используйте следующую команду для проверки аттестации происхождения сборки SLSA[1](#fn-5-1-def) образа Dynatrace Operator[2](#fn-5-2-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Поддерживается с версии Dynatrace Operator 1.9.0.

2

Образ Dynatrace Operator доступен в Amazon ECR начиная с версии 1.0.0. Дополнительные сведения см. в разделе [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

В случае успеха Cosign подтверждает, что сертификат подписи, запись в журнале прозрачности и издатель OIDC действительны, а аттестация создана доверенным рабочим процессом сборки Dynatrace.

Извлечение сведений о происхождении из вывода проверки

Полезную нагрузку [SLSA Provenance v1](https://slsa.dev/spec/v1.0/provenance) можно извлечь из аттестации in-toto, дополнив приведённую выше команду фильтрами `jq`[3](#fn-6-3-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson'
```

3

[jq CLI](https://jqlang.github.io/jq/) является полезным инструментом для работы с JSON.

Вывод содержит полный предикат SLSA Provenance v1, включая исходный репозиторий, рабочий процесс сборки, git-коммит и вызов GitHub Actions, создавший образ.

Кроме того, можно использовать [GitHub CLI](https://cli.github.com/) для проверки аттестации напрямую через GitHub attestation API:

```
gh attestation verify \



--owner Dynatrace \



oci://public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

В случае успеха команда выводит `Verification succeeded!` и перечисляет совпавшие аттестации, включая репозиторий сборки, рабочий процесс и идентификацию подписавшего.

## Связанные темы

* [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Использование публичного реестра")
* [Использование частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра")
* [Хранение образов Dynatrace в частных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Хранение образов Dynatrace в частных реестрах")