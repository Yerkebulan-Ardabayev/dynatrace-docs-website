---
title: Execute synthetic monitors from private locations
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose
scraped: 2026-03-06T21:25:02.237729
---

# Запуск синтетических мониторов из частных локаций

# Запуск синтетических мониторов из частных локаций

* Последняя версия Dynatrace
* Чтение: 2 минуты
* Обновлено 1 июня 2022 г.

**ActiveGate с поддержкой Synthetic** позволяет настроить частные локации для Synthetic, из которых можно запускать синтетические мониторы для отслеживания как внутренних, так и внешних ресурсов.

## Функциональность приватного синтетического мониторинга и модуль Synthetic

(модуль: [Synthetic](../configuration/configure-activegate.md#synth_mod "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований."))

ActiveGate, предназначенные для Dynatrace Synthetic Monitoring, имеют включённый [модуль Synthetic](../configuration/configure-activegate.md#synth_mod "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований.").

ActiveGate с поддержкой Synthetic, вместе с [движком Synthetic и Chromium](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать частную локацию для синтетического мониторинга."), являются элементами частных локаций Synthetic — локаций в вашей частной сетевой инфраструктуре.

Частная локация может состоять из одного или нескольких ActiveGate с поддержкой Synthetic. Ознакомьтесь с [требованиями](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Поддерживаемые операционные системы, версии Chromium и требования к аппаратному обеспечению для запуска синтетических мониторов из частных локаций") и [процессом](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать частную локацию для синтетического мониторинга.") настройки частных локаций. После настройки вы можете использовать [интерфейс управления частными локациями и мониторами](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md "Анализируйте и управляйте использованием ресурсов в ваших частных локациях Synthetic.") на базе Dynatrace.

### Важные замечания по аппаратному и программному обеспечению

ActiveGate с поддержкой Synthetic предъявляют более высокие требования к аппаратному обеспечению. См. [Требования для частных локаций Synthetic](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Поддерживаемые операционные системы, версии Chromium и требования к аппаратному обеспечению для запуска синтетических мониторов из частных локаций").

**Если ActiveGate выполняет модуль Synthetic, на нём не может быть включено никаких других функциональных модулей**. Если запустить другие модули на том же ActiveGate, может возникнуть ситуация, когда синтетические мониторы выполняются, но другие процессы перегружают машину и существенно влияют на метрики производительности мониторов, что приводит к ложным предупреждениям о деградации производительности.

## Запуск мониторов

Любой ActiveGate с поддержкой Synthetic способен выполнять **как [браузерные, так и HTTP-мониторы](../../../observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors.md "Узнайте о типах синтетических мониторов Dynatrace.")**.

Кроме того, в частных локациях использование ресурсов отслеживается отдельно для HTTP-мониторов с высоким потреблением ресурсов — эти мониторы имеют специальные ресурсоёмкие функции.

Для запуска браузерных мониторов из частной локации необходимо сначала удовлетворить зависимости движка перед установкой Environment или Cluster ActiveGate. Подробные инструкции см. в разделе [Создание частной локации Synthetic](../../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Узнайте, как создать частную локацию для синтетического мониторинга.").

### Варианты использования

Частные локации позволяют запускать мониторы во внутренней сети, когда вы не можете использовать [публичные локации Synthetic](../../../observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations.md "Узнайте обо всех доступных публичных локациях Synthetic Monitoring.") Dynatrace для синтетического мониторинга. С помощью частных локаций вы можете:

* Измерять производительность и доступность внутренних веб-страниц.
* Измерять сложные внутренние приложения с помощью браузерных мониторов по сценарию кликов.

Кроме того, вы также можете:

* Измерять внешние ресурсы с помощью синтетических мониторов, запущенных из внутренних локаций.
* Отслеживать API — как внутренние, так и внешние.
