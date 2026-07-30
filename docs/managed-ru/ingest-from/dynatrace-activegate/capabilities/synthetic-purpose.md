---
title: Запуск синтетических мониторов из приватных локаций
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose
---

# Запуск синтетических мониторов из приватных локаций

# Запуск синтетических мониторов из приватных локаций

* Чтение: 2 мин
* Обновлено 12 июля 2026 г.

**ActiveGates с поддержкой Synthetic** позволяют настраивать приватные Synthetic-локации, из которых можно запускать синтетические мониторы для наблюдения за внутренними и внешними ресурсами.

## Функциональность приватного синтетического мониторинга и модуль Synthetic

(модуль: [Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от потребностей и требований."))

ActiveGates, предназначенные для Dynatrace Synthetic Monitoring, имеют включённый [модуль Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от потребностей и требований.").

ActiveGates с поддержкой Synthetic перечислены в разделе **Deployment Status** > **ActiveGates**.

ActiveGates с поддержкой Synthetic вместе с [Synthetic engine и Chromium](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.") являются элементами приватных Synthetic-локаций, то есть локаций в частной сетевой инфраструктуре.

Приватная локация может включать один или несколько ActiveGates с поддержкой Synthetic. Изучите [требования](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из приватных локаций") и [процесс](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.") настройки приватных локаций. После настройки доступен основанный на Dynatrace [интерфейс управления приватными локациями и мониторами](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Анализ и управление использованием ресурсов в приватных Synthetic-локациях.").

### Важные замечания по оборудованию и ПО

ActiveGates с поддержкой Synthetic предъявляют повышенные требования к оборудованию. Подробнее: [Requirements for private Synthetic locations](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из приватных локаций").

**Если ActiveGate запускает модуль Synthetic, на нём нельзя включать другие функциональные модули**. Запуск других модулей на том же ActiveGate может привести к ситуации, когда синтетические мониторы выполняются, а другие процессы перегружают машину и существенно влияют на метрики производительности мониторов, вызывая ложные алерты о деградации производительности.

## Запуск мониторов

Любой ActiveGate с поддержкой Synthetic способен запускать **как [браузерные, так и HTTP-мониторы](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.")**.

Кроме того, в приватных локациях использование ресурсов отслеживается отдельно для ресурсоёмких HTTP-мониторов: такие мониторы обладают особыми функциями, требующими значительных ресурсов.

Чтобы запускать браузерные мониторы из приватной локации, нужно сначала выполнить зависимости движка до установки Environment или Cluster ActiveGate. Подробные инструкции: [Создание приватной Synthetic-локации](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать приватную локацию для синтетического мониторинга.").

### Варианты использования

Приватные локации позволяют запускать мониторы во внутренней сети тогда, когда использовать Dynatrace [публичные Synthetic-локации](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных на данный момент публичных Synthetic Monitoring Classic-локациях.") для синтетического мониторинга невозможно. С помощью приватных локаций можно:

* Измерять производительность и доступность внутренних веб-страниц.
* Измерять сложные внутренние приложения с помощью мониторов кликпути браузера.

Дополнительно можно также:

* Измерять внешние ресурсы с помощью синтетических мониторов, запускаемых из внутренних локаций.
* Мониторить APIs, как внутренние, так и внешние.