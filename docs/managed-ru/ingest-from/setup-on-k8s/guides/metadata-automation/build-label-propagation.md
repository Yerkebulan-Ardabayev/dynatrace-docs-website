---
title: Настройка распространения меток сборки
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/build-label-propagation
scraped: 2026-05-12T12:07:50.118077
---

# Настройка распространения меток сборки

# Настройка распространения меток сборки

* Чтение: 2 мин
* Опубликовано 28 июля 2023 г.

Распространение меток сборки позволяет передавать внедрённому OneAgent информацию о метаданных сборки и версии недавно развёрнутых подов. Эта информация затем отображается в разделе **Properties and tags** на страницах ваших сущностей.

## Как это работает

Значение поля метаданных можно [указать в переменной окружения](https://dt-url.net/cy035by).

```
env:



- name: MY_POD_NAMESPACE



valueFrom:



fieldRef:



fieldPath: metadata.namespace
```

Затем OneAgent внедряется в недавно развёрнутые поды и собирает метаданные, предоставленные через переменные окружения.

## Включение распространения меток сборки

Чтобы включить распространение меток сборки, необходимо задать для `feature.dynatrace.com/label-version-detection` значение `true` в DynaKube. Обратите внимание, что поскольку включение распространения меток сборки требует внедрения через вебхук, оно работает только с развёртываниями `applicationMonitoring` и `cloudNativeFullStack`.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/label-version-detection: "true"



...



spec:



oneAgent:



cloudNativeFullStack: {}
```

## Поведение по умолчанию

* Переменная окружения `DT_RELEASE_VERSION` получает значение из `metadata.labels['app.kubernetes.io/version']`.
* Переменная окружения `DT_RELEASE_PRODUCT` получает значение из `metadata.labels['app.kubernetes.io/part-of']`.

Например, если у вашего приложения есть следующий под:

```
apiVersion: v1



kind: Pod



metadata:



...



labels:



app.kubernetes.io/version: "1.0.0"



app.kubernetes.io/part-of: "store"



spec:



...
```

значения меток добавляются в переменные окружения внедрённых контейнеров:

```
apiVersion: v1



kind: Pod



metadata:



...



labels:



app.kubernetes.io/version: "1.0.0"



app.kubernetes.io/part-of: "Store"



spec:



...



containers:



- name: app



...



env:



- name: "DT_RELEASE_VERSION"



valueFrom:



fieldRef:



fieldPath: metadata.labels['app.kubernetes.io/version']



- name: "DT_RELEASE_PRODUCT"



valueFrom:



fieldRef:



fieldPath: metadata.labels['app.kubernetes.io/part-of']
```

Если переменные окружения `DT_RELEASE_VERSION` или `DT_RELEASE_PRODUCT` уже заданы для контейнера до внедрения OneAgent, они не будут перезаписаны.

## Параметры настройки

Можно добавить аннотации к пространству имён, чтобы задать дополнительные сопоставления или переопределить значения по умолчанию для подов в этом пространстве имён.

* Каждый ключ аннотации сопоставляется с определённой переменной окружения.
* Каждое значение аннотации является ссылочным путём в `fieldPath`.
* Доступная информация для `fieldPath` та же, что и для [`fieldRef`](https://dt-url.net/0m235nn).

Пример переопределения значений по умолчанию для `version` и `product` и включения `stage` и `build-version`:

```
annotations:



mapping.release.dynatrace.com/version: "metadata.annotations['my-version']"



mapping.release.dynatrace.com/product: "metadata.labels['app.kubernetes.io/name']"



mapping.release.dynatrace.com/stage: "metadata.namespace"



mapping.release.dynatrace.com/build-version: "metadata.labels['release.dynatrace.com/stage']"
```

Каждая из этих аннотаций настраивает свою переменную окружения:

|  |  |
| --- | --- |
| `mapping.release.dynatrace.com/version` | Содержит `fieldPath`, используемый для `DT_RELEASE_VERSION`.  Если эта аннотация отсутствует, сопоставление возвращается к [поведению по умолчанию](#default-behavior). |
| `mapping.release.dynatrace.com/product` | Содержит `fieldPath`, используемый для `DT_RELEASE_PRODUCT`.  Если эта аннотация отсутствует, сопоставление возвращается к [поведению по умолчанию](#default-behavior). |
| `mapping.release.dynatrace.com/stage` | Содержит `fieldPath`, используемый для `DT_RELEASE_STAGE`. |
| `mapping.release.dynatrace.com/build-version` | Содержит `fieldPath`, используемый для `DT_RELEASE_BUILD_VERSION`. |

Значения не проверяются Dynatrace Operator или вебхуком, поэтому убедитесь, что они корректны.