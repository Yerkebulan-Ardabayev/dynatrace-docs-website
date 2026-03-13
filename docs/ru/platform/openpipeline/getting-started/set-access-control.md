---
title: Set access control in OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/set-access-control
scraped: 2026-03-06T21:37:26.951279
---

# Настройка управления доступом в OpenPipeline

# Настройка управления доступом в OpenPipeline

* Последняя версия Dynatrace
* Практическое руководство
* 3 мин. чтения
* Опубликовано 9 января 2026 г.

Это руководство объясняет, как владельцы пайплайнов и пользовательских источников приёма данных, а также администраторы могут настраивать и управлять доступом через веб-интерфейс или API.

## Предварительные требования

* Dynatrace версии 1.322 и более ранние: вы [перенесли конфигурации OpenPipeline на Settings API](/docs/platform/openpipeline/migration-settings "Узнайте, как перенести конфигурации OpenPipeline на новый Settings API.").
* Убедитесь, что разрешения пользователя или группы пользователей достаточны для типа доступа, который вы хотите предоставить.
* Для выполнения процедур через API убедитесь, что свойство `ownerBasedAccessControl` установлено в `true` для схемы Settings API OpenPipeline, которую вы намерены использовать.

  Значения API управления доступом по умолчанию

  При первой установке свойства автоматически добавляются следующие значения по умолчанию.

  | Свойство | Описание | Поддерживаемые значения | Значение по умолчанию |
  | --- | --- | --- | --- |
  | `owner` | Пользователь, который первым изменил объект настроек. | Пользователь, группа пользователей или `all-users`. | `all-users` |
  | `accessor` | Пользователи, которые могут получить доступ к объекту в зависимости от их разрешений. | Один или несколько пользователей или групп пользователей, или `all-users` | `all-users` |

  Доступные схемы Settings API

  + [builtin:openpipeline.bizevents.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.bizevents.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.bizevents.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.bizevents.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.bizevents.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-bizevents-routing "Просмотр таблицы схемы настроек builtin:openpipeline.bizevents.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.davis.events.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.davis.events.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-events-routing "Просмотр таблицы схемы настроек builtin:openpipeline.davis.events.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.problems.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.davis.problems.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.problems.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.davis.problems.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.davis.problems.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-davis-problems-routing "Просмотр таблицы схемы настроек builtin:openpipeline.davis.problems.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.events.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.events.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-routing "Просмотр таблицы схемы настроек builtin:openpipeline.events.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.events.sdlc.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.events.sdlc.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.sdlc.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-sdlc-routing "Просмотр таблицы схемы настроек builtin:openpipeline.events.sdlc.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.security.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.events.security.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.security.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.events.security.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.events.security.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-events-security-routing "Просмотр таблицы схемы настроек builtin:openpipeline.events.security.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.logs.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.logs.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.logs.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.logs.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.logs.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-routing "Просмотр таблицы схемы настроек builtin:openpipeline.logs.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.metrics.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.metrics.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.metrics.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.metrics.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.metrics.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-metrics-routing "Просмотр таблицы схемы настроек builtin:openpipeline.metrics.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.security.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.security.events.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.security.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.security.events.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.security.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-security-events-routing "Просмотр таблицы схемы настроек builtin:openpipeline.security.events.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.spans.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.spans.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.spans.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.spans.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.spans.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-spans-routing "Просмотр таблицы схемы настроек builtin:openpipeline.spans.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.system.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.system.events.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.system.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.system.events.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.system.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-system-events-routing "Просмотр таблицы схемы настроек builtin:openpipeline.system.events.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.events.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.user.events.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.events.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.user.events.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.events.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-user-events-routing "Просмотр таблицы схемы настроек builtin:openpipeline.user.events.routing вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.sessions.ingest-sources](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-ingest-sources "Просмотр таблицы схемы настроек builtin:openpipeline.usersessions.ingest-sources вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.sessions.pipelines](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-pipelines "Просмотр таблицы схемы настроек builtin:openpipeline.usersessions.pipelines вашей среды мониторинга через Dynatrace API.")
  + [builtin:openpipeline.user.sessions.routing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-usersessions-routing "Просмотр таблицы схемы настроек builtin:openpipeline.usersessions.routing вашей среды мониторинга через Dynatrace API.")

## Предоставление доступа

Когда вы создаёте пайплайн или пользовательский источник приёма данных, вы являетесь владельцем, и только вы и администратор имеете к нему доступ. Чтобы предоставить доступ другому пользователю или группе пользователей Dynatrace:

Через интерфейс

Через API

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** и выберите область конфигурации.
2. Найдите пользовательский источник приёма данных или пайплайн в таблице.
3. Откройте меню  и выберите  **Share**.
4. Найдите и выберите нового получателя доступа.
5. Выберите тип доступа:  **View** или  **Edit**.
6. Выберите **Save**.

Для изменения или отзыва доступа:

1. Перейдите к  (**Manage access**).
2. Разверните тип доступа для пользователя, чтобы изменить его, или нажмите **Remove**.

Установите значение свойства `accessor` для пользователей или групп пользователей, которым вы хотите предоставить доступ.

## Сделать публичным (или приватным)

Когда вы создаёте пайплайн или пользовательский источник приёма данных, вы являетесь владельцем и можете предоставить доступ всем пользователям. Чтобы сделать публичным:

Через интерфейс

Через API

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** и выберите область конфигурации.
2. Найдите пользовательский источник приёма данных или пайплайн в таблице.
3. Откройте  и выберите  **Share**.
4. Перейдите к  (**Manage access**) и включите **Visible to anyone in your environment (Read only)**.

Чтобы вернуть в приватный режим, выполните одно из следующих действий:

* Выключите **Visible to anyone in your environment (Read only)**, чтобы сохранить конкретных получателей доступа.
* Выберите  **Remove all access**, чтобы удалить все типы доступа для всех пользователей и групп пользователей.

Установите значение свойства `accessor` в `all-users`.

## Передача владения

Когда вы создаёте пайплайн или пользовательский источник приёма данных, вы являетесь владельцем. Чтобы передать владение другому пользователю или группе пользователей Dynatrace:

Через интерфейс

Через API

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** и выберите область конфигурации.
2. Найдите пользовательский источник приёма данных или пайплайн в таблице.

1. Откройте меню  и выберите  **Change owner**.
2. Найдите и выберите нового владельца, затем выберите **Change owner**.

   Учтите, что вы потеряете весь доступ, если новый владелец не предоставит вам разрешения.
3. После завершения передачи новый владелец получит уведомление по электронной почте о передаче владения.

Установите значение свойства `owner` для пользователя или группы пользователей, которым вы хотите передать владение.

Учтите, что вы потеряете весь доступ, если новый владелец не предоставит вам разрешения.

## Дальнейшие шаги

После того как администраторы установят разрешения, а владельцы настроят доступ, пользователи смогут управлять элементами и получать к ним доступ соответствующим образом. Команды разработки могут приступить к настройке обработки для своих сценариев использования. Подробнее об обработке см. [Настройка пайплайна обработки](/docs/platform/openpipeline/getting-started/tutorial-configure-processing "Настройка источников приёма данных, маршрутов и обработки для ваших данных в OpenPipeline.").

## Связанные темы

* [Разработчик — управление доступом на основе владения](https://developer.dynatrace.com/develop/data/store-app-settings/#owner-based-access-control)