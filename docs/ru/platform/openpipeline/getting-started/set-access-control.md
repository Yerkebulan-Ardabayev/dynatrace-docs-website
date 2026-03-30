---
title: Настройка контроля доступа в OpenPipeline
source: https://www.dynatrace.com/docs/platform/openpipeline/getting-started/set-access-control
scraped: 2026-03-06T21:37:26.951279
---

# Настройка управления доступом в OpenPipeline


* 3 мин. чтения

Это руководство объясняет, как владельцы пайплайнов и пользовательских источников приёма данных, а также администраторы могут настраивать и управлять доступом через веб-интерфейс или API.

## Предварительные требования

* Dynatrace версии 1.322 и более ранние: вы перенесли конфигурации OpenPipeline на Settings API.
* Убедитесь, что разрешения пользователя или группы пользователей достаточны для типа доступа, который вы хотите предоставить.
* Для выполнения процедур через API убедитесь, что свойство `ownerBasedAccessControl` установлено в `true` для схемы Settings API OpenPipeline, которую вы намерены использовать.

  Значения API управления доступом по умолчанию

  При первой установке свойства автоматически добавляются следующие значения по умолчанию.

  | Свойство | Описание | Поддерживаемые значения | Значение по умолчанию |
  | --- | --- | --- | --- |
  | `owner` | Пользователь, который первым изменил объект настроек. | Пользователь, группа пользователей или `all-users`. | `all-users` |
  | `accessor` | Пользователи, которые могут получить доступ к объекту в зависимости от их разрешений. | Один или несколько пользователей или групп пользователей, или `all-users` | `all-users` |

  Доступные схемы Settings API

  + builtin:openpipeline.bizevents.ingest-sources
  + builtin:openpipeline.bizevents.pipelines
  + builtin:openpipeline.bizevents.routing
  + builtin:openpipeline.davis.events.ingest-sources
  + builtin:openpipeline.davis.events.pipelines
  + builtin:openpipeline.davis.events.routing
  + builtin:openpipeline.davis.problems.ingest-sources
  + builtin:openpipeline.davis.problems.pipelines
  + builtin:openpipeline.davis.problems.routing
  + builtin:openpipeline.events.ingest-sources
  + builtin:openpipeline.events.pipelines
  + builtin:openpipeline.events.routing
  + builtin:openpipeline.events.sdlc.ingest-sources
  + builtin:openpipeline.events.sdlc.pipelines
  + builtin:openpipeline.events.sdlc.routing
  + builtin:openpipeline.events.security.ingest-sources
  + builtin:openpipeline.events.security.pipelines
  + builtin:openpipeline.events.security.routing
  + builtin:openpipeline.logs.ingest-sources
  + builtin:openpipeline.logs.pipelines
  + builtin:openpipeline.logs.routing
  + builtin:openpipeline.metrics.ingest-sources
  + builtin:openpipeline.metrics.pipelines
  + builtin:openpipeline.metrics.routing
  + builtin:openpipeline.security.events.ingest-sources
  + builtin:openpipeline.security.events.pipelines
  + builtin:openpipeline.security.events.routing
  + builtin:openpipeline.spans.ingest-sources
  + builtin:openpipeline.spans.pipelines
  + builtin:openpipeline.spans.routing
  + builtin:openpipeline.system.events.ingest-sources
  + builtin:openpipeline.system.events.pipelines
  + builtin:openpipeline.system.events.routing
  + builtin:openpipeline.user.events.ingest-sources
  + builtin:openpipeline.user.events.pipelines
  + builtin:openpipeline.user.events.routing
  + builtin:openpipeline.user.sessions.ingest-sources
  + builtin:openpipeline.user.sessions.pipelines
  + builtin:openpipeline.user.sessions.routing

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

После того как администраторы установят разрешения, а владельцы настроят доступ, пользователи смогут управлять элементами и получать к ним доступ соответствующим образом. Команды разработки могут приступить к настройке обработки для своих сценариев использования. Подробнее об обработке см. Настройка пайплайна обработки.

## Связанные темы

* [Разработчик — управление доступом на основе владения](https://developer.dynatrace.com/develop/data/store-app-settings/#owner-based-access-control)