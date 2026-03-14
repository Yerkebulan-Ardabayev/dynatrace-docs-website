---
title: Включение нового опыта RUM для веб-приложений RUM Classic
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps
scraped: 2026-03-05T21:39:52.367065
---

# Включение нового RUM Experience для классических RUM веб-приложений


* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 28 января 2026 г.

Если вы уже отслеживаете свои веб-интерфейсы с помощью RUM Classic, переход на новый RUM Experience требует только изменения конфигурации. В этом руководстве описаны предварительные требования и необходимые шаги.

## Предварительные требования

Перед включением нового RUM Experience убедитесь, что выполнены следующие условия.

#### Требуется для включения настройки

* RUM Classic включён на уровне — интерфейса или среды, — на котором вы хотите включить новый RUM Experience.
* Версия RUM JavaScript — 1.317+.
* Формат сниппета «фрагмент кода», который не поддерживается новым RUM Experience, не используется. Для альтернативных вариантов см. [Рекомендации по выбору формата сниппета](snippet-formats.md#snippet-format-recommendations "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").

#### Требуется для сбора и приёма данных

* Версия OneAgent — 1.301+.
* Поскольку новые функции добавляются регулярно, рекомендуется поддерживать OneAgent и RUM JavaScript в актуальном состоянии. Версию RUM JavaScript следует настроить на **Последняя стабильная** или **Предыдущая стабильная**, как описано в разделе [Настройка версии RUM JavaScript для интерфейса](../additional-configuration/rum-javascript-version.md#configure-js-version "Learn how to control the RUM JavaScript version used to monitor your frontends in the New RUM Experience.").

## Включение нового RUM Experience для веб-интерфейса

Чтобы включить новый RUM Experience для веб-интерфейса

1. Перейдите в раздел ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Обзор**.
2. Выберите **Веб**, чтобы просмотреть все веб-интерфейсы.
3. Выберите интерфейс, который хотите настроить.
4. Перейдите на вкладку **Настройки**.
5. В разделе **Включение и управление стоимостью** включите **RUM**.
6. При необходимости включите **Пользовательские взаимодействия** для захвата взаимодействий пользователей, таких как клики и прокрутка.

Если вы используете автоматическую инъекцию, новая конфигурация применяется в течение 5 минут. При ручной вставке RUM JavaScript может потребоваться обновить сниппет в зависимости от используемого [формата сниппета](snippet-formats.md "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."):

* **JavaScript tag**: Новая конфигурация применяется автоматически, но из-за кэширования может вступить в силу не сразу. Файл, содержащий код мониторинга и конфигурацию, кэшируется на один час в CDN Dynatrace. Кроме того, браузеры соблюдают [настроенную продолжительность кэширования](snippet-formats.md#cache-duration "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.").
* **OneAgent JavaScript tag**, **OneAgent JavaScript tag with SRI** или **встроенный код**: Как и при любом изменении конфигурации, необходимо обновить вставленный сниппет.

## Включение нового RUM Experience на уровне среды

Чтобы включить новый RUM Experience для веб-интерфейсов на уровне среды

1. Перейдите в раздел ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Настройки** > **Сбор и захват данных** > **Real User Monitoring** > **Трафик и управление стоимостью** > **Веб-интерфейсы**.
2. Включите **Включить новый Real User Monitoring Experience**. Обратите внимание, что этот параметр отображается только при включённом параметре **Включить классический Real User Monitoring**; см. [Предварительные требования](#prerequisites).

## Включение нового RUM Experience через API

API Settings позволяет включить новый RUM Experience либо для веб-интерфейса, либо на уровне среды. Подробнее см. в разделе [Settings API — таблица схемы включения и управления стоимостью](../../../../../dynatrace-api/environment-api/settings/schemas/builtin-rum-web-enablement.md "View builtin:rum.web.enablement settings schema table of your monitoring environment via the Dynatrace API.").

Если вы не используете формат сниппета **JavaScript tag**, после включения нового RUM Experience необходимо обновить сниппет, если он был вставлен вручную. Дополнительные сведения см. в разделе [Включение нового RUM Experience для веб-интерфейса](#enable-new-rum-for-web-frontend). Для получения обновлённого сниппета используйте [API тегов ручной вставки RUM](../../../../../dynatrace-api/environment-api/rum/rum-manual-insertion-tags.md "Learn how you can download the RUM manual insertion tags via API").

## Связанные темы

* [Переход с RUM Classic на новый RUM Experience](../../transition-from-rum-classic.md "Learn how to transition from RUM Classic to the New RUM Experience.")
