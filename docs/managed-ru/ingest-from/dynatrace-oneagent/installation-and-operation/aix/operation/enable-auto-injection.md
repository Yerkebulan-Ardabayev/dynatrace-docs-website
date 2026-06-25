---
title: Автоматическая инъекция глубокого мониторинга кода на AIX
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/enable-auto-injection
scraped: 2026-05-12T11:10:51.299729
---

# Автоматическая инъекция глубокого мониторинга кода на AIX

# Автоматическая инъекция глубокого мониторинга кода на AIX

* Практическое руководство
* Чтение: 1 мин
* Обновлено 22 июня 2022 г.

На AIX Dynatrace поддерживает глубокий мониторинг кода для приложений Java, Apache, WebLogic и Websphere. Начиная с версии OneAgent 1.189, достаточно включить **Allow AIX kernel extension** на странице **Host settings** вашего хоста AIX в Dynatrace. Для более ранних версий необходимо выполнить некоторую настройку на AIX, см. [Установка OneAgent на AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Узнайте, как скачать и установить Dynatrace OneAgent на AIX.").

## Включение автоматической инъекции

Чтобы включить автоматическую инъекцию

1. После установки OneAgent и его успешного подключения к Dynatrace откройте в Dynatrace раздел **Hosts** и выберите ваш хост AIX.
2. На странице сведений о хосте выберите **More** (**…**) > **Settings**.
3. Откройте вкладку **AIX kernel extension**.
4. Включите **Allow AIX kernel extension**.  
   После этого OneAgent начнёт собирать данные глубокого мониторинга кода.

Для настройки автоматической инъекции можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

1. Чтобы узнать схему, используйте [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API.") с `builtin:host.monitoring.aix-kernel-extension` в качестве schemaId.
2. На основе схемы `builtin:host.monitoring.aix-kernel-extension` создайте объект конфигурации.
3. Чтобы создать конфигурацию, используйте [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Создание или проверка объекта настроек через Dynatrace API.").

## Обновление OneAgent версии 1.187 и ниже

Если вы вручную настроили хост AIX для инъекции кодовых модулей OneAgent, рекомендуется очистить переменные окружения `LDR_PRELOAD` и `LDR_PRELOAD64` после включения автоматической инъекции. Это позволит удалить OneAgent простым запуском [скрипта удаления](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix "Узнайте, как удалить OneAgent из вашей системы на базе AIX.") без необходимости очищать переменные окружения.