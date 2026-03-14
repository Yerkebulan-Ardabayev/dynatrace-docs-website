---
title: Автоматическое внедрение глубокого мониторинга кода на AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/enable-auto-injection
scraped: 2026-03-06T21:18:48.563032
---

# Автоматическое внедрение глубокого мониторинга кода на AIX


* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jun 22, 2022

На AIX Dynatrace поддерживает глубокий мониторинг кода для приложений Java, Apache, WebLogic и WebSphere. Начиная с версии OneAgent 1.189 достаточно лишь **разрешить расширение ядра AIX** на странице **Host settings** вашего AIX-хоста в Dynatrace. Для более ранних версий требуется выполнить дополнительную настройку на AIX — см. раздел [Установка OneAgent на AIX](../installation/install-oneagent-on-aix.md "Узнайте, как скачать и установить Dynatrace OneAgent на AIX.").

## Включение автоматического внедрения

Чтобы включить автоматическое внедрение

1. После установки OneAgent и его успешного подключения к Dynatrace перейдите в Dynatrace в раздел **Hosts** и выберите ваш AIX-хост.
2. На странице сведений о хосте выберите **More** (**…**) > **Settings**.
3. Выберите вкладку **AIX kernel extension**.
4. Включите **Allow AIX kernel extension**.
   OneAgent начнёт собирать данные глубокого мониторинга кода.

Для настройки автоматического внедрения можно использовать [Settings API](../../../../../dynatrace-api/environment-api/settings.md "Узнайте, что предлагает Dynatrace Settings API.").

1. Чтобы изучить схему, используйте [GET a schema](../../../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "Просмотр схемы настроек через Dynatrace API.") с `builtin:host.monitoring.aix-kernel-extension` в качестве schemaId.
2. На основе схемы `builtin:host.monitoring.aix-kernel-extension` создайте объект конфигурации.
3. Для создания конфигурации используйте [POST an object](../../../../../dynatrace-api/environment-api/settings/objects/post-object.md "Создание или проверка объекта настроек через Dynatrace API.").

## Обновление OneAgent версии 1.187 и ранее

Если вы вручную настроили AIX-хост для внедрения кодовых модулей OneAgent, рекомендуется очистить переменные среды `LDR_PRELOAD` и `LDR_PRELOAD64` после включения автоматического внедрения. Это позволит удалить OneAgent с помощью [скрипта удаления](uninstall-oneagent-on-aix.md "Узнайте, как удалить OneAgent из вашей системы на базе AIX.") без необходимости вручную очищать переменные среды.
