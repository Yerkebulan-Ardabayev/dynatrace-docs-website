---
title: Реестры контейнеров
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries
---

# Реестры контейнеров

# Реестры контейнеров

* Чтение: 2 мин
* Опубликовано 28 июля 2023 г.

Чтобы обеспечить бесшовную интеграцию с инструментами и адаптивность под нужды, образы контейнеров предоставляются несколькими способами для максимальной гибкости:

* Встроенный реестр Dynatrace (по умолчанию)
* Публичные реестры
* Собственный приватный реестр (рекомендуется)

## Встроенный реестр Dynatrace

По умолчанию

В качестве поведения по умолчанию Dynatrace Operator получает образы из встроенного реестра Dynatrace, что даёт приоритет удобству и минимизирует сложность конфигурации для настройки cloud-native мониторинга.

При этом одновременное получение нескольких образов из встроенного реестра Dynatrace повышает вероятность ограничения частоты запросов (rate limiting). Поэтому рекомендуется использовать одобренные публичные реестры или, в идеале, настроить собственный приватный реестр. Использование публичных и приватных реестров повышает эксплуатационную эффективность и производительность, особенно в условиях высокой нагрузки.

## Публичные реестры

Чтобы учесть разнообразные требования инфраструктуры и предпочтения организаций, образы Dynatrace доступны в [выбранных публичных реестрах](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). Эти образы соответствуют лучшим практикам, обеспечивая неизменяемость и подписание для повышенной безопасности и устойчивости к потенциальным рискам цепочки поставок.

Если нужен больший контроль над средой размещения образов, Dynatrace предлагает возможность реплицировать образы и подписи в приватные реестры.

## Собственный приватный реестр

Рекомендуется

Для оптимальной производительности в условиях высокой нагрузки и динамичных сред рекомендуется использовать [приватный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry"). Кроме того, для соответствия стандартам безопасности и обеспечения целостности ПО при снижении рисков цепочки поставок рекомендуется сканирование образов и [проверка подписи](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures") образов Dynatrace.

Реплицируя образы Dynatrace в приватный реестр, можно совместить отличную производительность доставки с гарантией безопасных, подписанных и неизменяемых образов.

## Подробнее

[### Использование публичного реестра Dynatrace

Настройка Dynatrace Operator и DynaKube на использование образов из поддерживаемых публичных реестров.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")[### Использование собственного приватного реестра

Настройка Dynatrace Operator и DynaKube на использование образов из собственного приватного реестра.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")[### Хранение образов Dynatrace в приватных реестрах

Как реплицировать образы Dynatrace в приватные реестры.](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")[### Проверка подписей образов Dynatrace

Проверка подписей образов Dynatrace для обеспечения целостности и безопасности цепочки поставок ПО.](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")