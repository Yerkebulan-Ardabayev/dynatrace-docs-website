---
title: Проверка подписей образов Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature
---

# Проверка подписей образов Dynatrace

# Проверка подписей образов Dynatrace

* Чтение: 4 мин
* Обновлено 16 апреля 2026 г.

В современных условиях атаки на цепочку поставок стали распространённым вектором угроз. Наш подход к противодействию этому риску заключается в поставке неизменяемых и подписанных образов, что служит основой для усиления мер безопасности.

На этой странице описан процесс проверки подписей образов Dynatrace, который устанавливает подлинность и обеспечивает целостность программного обеспечения.

## Предварительные требования

Прежде чем начать, убедись, что выполнены следующие предварительные требования:

* Обязательно: [Cosign﻿](https://docs.sigstore.dev/cosign/system_config/installation/) для проверки подписи образа
* Опционально: [GitHub CLI﻿](https://cli.github.com/) для проверки происхождения SLSA через GitHub attestation API
* Обязательно: доступ на чтение к репозиториям образов Dynatrace при использовании приватного реестра

## Проверка подписей образов с помощью Cosign

В следующих разделах описано, как можно проверить подписи образов Dynatrace с помощью Cosign. Для простоты во всех примерах используются репозитории компонентов Dynatrace в публичном Amazon ECR, но они действительны и применимы к любому реестру, содержащему образы Dynatrace.

Если нужны альтернативы Amazon ECR, см. [Поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного реестра для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из окружения Dynatrace.").

Подписание образов выполняется только для образов Dynatrace из поддерживаемых публичных реестров. Образы во встроенном реестре Dynatrace не подписываются.

Dynatrace подписывает образы с помощью Cosign, но только данные подписи для Dynatrace Operator загружаются в публичный журнал прозрачности Sigstore. Это позволяет выполнять стандартную проверку для Operator. Для остальных образов при проверке требуется флаг `--insecure-ignore-tlog`.

### Dynatrace Operator

Dynatrace Operator, это проект с открытым исходным кодом, размещённый и собираемый на GitHub. Из-за этого подписание и проверка немного отличаются от других компонентов Dynatrace.

Проверка без ключа

Проверка по публичному ключу

Следующая команда показывает способ проверки подписи образа Dynatrace Operator без использования ключа:

```
cosign verify --certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

Следующая команда показывает, как проверить подпись образа Dynatrace Operator с помощью публичного ключа соответствующего релиза GitHub:

```
cosign verify --key https://github.com/Dynatrace/dynatrace-operator/releases/download/<tag>/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

### Dynatrace ActiveGate

Следующая команда показывает, как проверить подпись образа Dynatrace ActiveGate с помощью публичного ключа с `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-activegate:<tag>
```

### Dynatrace Code Modules

Следующая команда показывает, как проверить подпись образа Dynatrace Code Modules с помощью публичного ключа с `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>
```

### Dynatrace OneAgent

Следующая команда показывает, как проверить подпись образа Dynatrace OneAgent с помощью публичного ключа с `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

### Dynatrace Kubernetes Node Configuration Collector

Следующая команда показывает, как проверить подпись образа Dynatrace Kubernetes Node Configuration Collector с помощью публичного ключа с `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag>
```

### Dynatrace EdgeConnect

Следующая команда показывает, как проверить подпись образа Dynatrace EdgeConnect с помощью публичного ключа с `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

## Проверка Attestation Software Bill of Materials (SBOM)

Attestation позволяет пользователям убедиться, что Software Bill of Materials (SBOM) поступает из доверенного источника в цепочке поставок программного обеспечения. Доверяя заявлению производителя образа контейнера о включённом ПО, пользователи могут безопасно интегрировать SBOM в свои рабочие процессы.

### Dynatrace Operator

Используй следующую команду для проверки attestation Software Bill of Materials (SBOM)[1](#fn-1-1-def) образа Dynatrace Operator[2](#fn-1-2-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Поддерживается начиная с Dynatrace Operator версии 0.12.0.

2

Образ Dynatrace Operator доступен в Amazon ECR начиная с версии 1.0.0. Подробнее см. [поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator для использования образов из публичного реестра для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение из окружения Dynatrace.").

Получение файла SBOM из результата проверки

SBOM в формате CycloneDX можно извлечь из attestation in-toto, дополнив приведённую выше команду фильтрами `jq`[3](#fn-2-3-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

3

[jq CLI﻿](https://jqlang.github.io/jq/), это полезный инструмент для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace Operator.

### Dynatrace ActiveGate

ActiveGate версии 1.303+

Используй следующую команду для проверки attestation Software Bill of Materials (SBOM) образа Dynatrace ActiveGate.
Обязательно укажи нужную архитектуру CPU. Варианты: `amd64`, `arm64` и `s390x`.

```
digest=$(docker manifest inspect public.ecr.aws/dynatrace/dynatrace-activegate:<tag> | \



jq -r '.manifests[] | select(.platform.architecture=="amd64") | .digest')



cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest
```

Получение файла SBOM из результата проверки

SBOM в формате CycloneDX можно извлечь из attestation in-toto, дополнив приведённую выше команду фильтрами `jq`[1](#fn-3-1-def):

```
cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

[jq CLI﻿](https://jqlang.github.io/jq/), это полезный инструмент для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace ActiveGate.

### Dynatrace EdgeConnect

EdgeConnect версии 1.473+

Используй следующую команду для проверки attestation Software Bill of Materials (SBOM) образа Dynatrace EdgeConnect.

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

Получение файла SBOM из результата проверки

SBOM в формате CycloneDX можно извлечь из attestation in-toto, дополнив приведённую выше команду фильтрами `jq`[1](#fn-4-1-def):

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

[jq CLI﻿](https://jqlang.github.io/jq/), это полезный инструмент для работы с JSON.

Выполнение команды создаёт файл `sbom.json` в локальной файловой системе, содержащий SBOM образа Dynatrace EdgeConnect.

## Проверка Attestation происхождения сборки SLSA

Attestation происхождения сборки [SLSA﻿](https://slsa.dev) предоставляет проверяемую запись о том, где и как был собран образ контейнера. Проверка таких attestation подтверждает, что образ был создан ожидаемым исходным репозиторием и рабочим процессом сборки, защищая от подделки в процессе сборки и распространения.

### Оператор Dynatrace

Cosign

GitHub CLI

Используй следующую команду, чтобы проверить SLSA build provenance attestation[1](#fn-5-1-def) образа Dynatrace Operator[2](#fn-5-2-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Поддерживается начиная с Dynatrace Operator версии 1.9.0.

2

Образ Dynatrace Operator доступен на Amazon ECR начиная с версии 1.0.0. Подробнее см. [поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

При успешном выполнении Cosign подтверждает, что сертификат подписи, запись в журнале прозрачности и OIDC-издатель действительны, и что attestation создан доверенным build workflow Dynatrace.

Получение сведений о происхождении из вывода проверки

Полезную нагрузку [SLSA Provenance v1﻿](https://slsa.dev/spec/v1.0/provenance) можно извлечь из in-toto attestation, дополнив приведённую выше команду фильтрами `jq`[3](#fn-6-3-def):

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson'
```

3

[jq CLI﻿](https://jqlang.github.io/jq/), это полезный инструмент для работы с JSON.

Вывод содержит полный предикат SLSA Provenance v1, включая репозиторий исходного кода, build workflow, git-коммит и вызов GitHub Actions, который создал образ.

В качестве альтернативы можно использовать [GitHub CLI﻿](https://cli.github.com/), чтобы проверить attestation напрямую по GitHub attestation API:

```
gh attestation verify \



--owner Dynatrace \



oci://public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

При успешном выполнении команда выводит `Verification succeeded!` и перечисляет совпавшие attestation, включая репозиторий сборки, workflow и идентификатор подписавшего.

## Связанные темы

* [Использование публичного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* [Использование приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Хранение образов Dynatrace в приватных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")