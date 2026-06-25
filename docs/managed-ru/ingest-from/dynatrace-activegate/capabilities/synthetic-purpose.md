---
title: Запуск синтетических мониторов из частных расположений
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose
scraped: 2026-05-12T11:08:04.971251
---

# Запуск синтетических мониторов из частных расположений

# Запуск синтетических мониторов из частных расположений

* 2-min read
* Updated on Jun 01, 2022

**ActiveGate с поддержкой Synthetic** позволяют создавать частные синтетические расположения, из которых можно запускать синтетические мониторы для проверки как внутренних, так и внешних ресурсов.

## Функциональность частного синтетического мониторинга и модуль Synthetic

(модуль: [Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей."))

У ActiveGate, предназначенных для синтетического мониторинга Dynatrace, включён [модуль Synthetic](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Узнайте, какие свойства ActiveGate можно настраивать в зависимости от ваших потребностей.").

ActiveGate с поддержкой Synthetic совместно с [движком Synthetic и Chromium](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") являются элементами частных синтетических расположений, которые представляют собой расположения в вашей частной сетевой инфраструктуре.

Частное расположение может включать один или несколько ActiveGate с поддержкой Synthetic. Смотрите [требования](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений") и [процедуру](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.") создания частных расположений. После настройки вы можете использовать [интерфейс управления частными расположениями и мониторами](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Анализируйте и управляйте использованием ресурсов в ваших частных синтетических расположениях.") на базе Dynatrace.

### Важные примечания по аппаратному и программному обеспечению

ActiveGate с поддержкой Synthetic предъявляют повышенные требования к аппаратному обеспечению. Смотрите [Требования к частным синтетическим расположениям](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые ОС, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений").

**Если ActiveGate запускает модуль Synthetic, на нём не может быть включён ни один другой функциональный модуль.** Запуск других модулей на том же ActiveGate может привести к ситуации, когда синтетические мониторы выполняются, но другие процессы перегружают машину, оказывая значительное влияние на метрики производительности мониторов и вызывая ложные оповещения о снижении производительности.

## Выполнение мониторов

Любой ActiveGate с поддержкой Synthetic способен выполнять **как [браузерные, так и HTTP-мониторы](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.")**.

Кроме того, в частных расположениях использование ресурсов отдельно отслеживается для ресурсоёмких HTTP-мониторов, имеющих специальные функции с интенсивным потреблением ресурсов.

Для запуска браузерных мониторов из частного расположения необходимо сначала удовлетворить зависимости движка до установки Environment или Cluster ActiveGate. Подробные инструкции смотрите в разделе [Создание частного синтетического расположения](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

### Сценарии использования

Частные расположения позволяют запускать мониторы в вашей внутренней сети, когда использование [публичных синтетических расположений](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте о всех доступных публичных расположениях синтетического мониторинга.") Dynatrace невозможно. С помощью частных расположений вы можете:

* Измерять производительность и доступность внутренних веб-страниц.
* Измерять сложные внутренние приложения с помощью браузерных мониторов с clickpath.

Кроме того, вы также можете:

* Измерять внешние ресурсы с помощью синтетических мониторов, запущенных из внутренних расположений.
* Мониторить API, как внутренние, так и внешние.