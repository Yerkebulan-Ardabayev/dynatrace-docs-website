---
title: Использование Subresource Integrity (SRI) для кода Real User Monitoring Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/subresource-integrity
---

# Использование Subresource Integrity (SRI) для кода Real User Monitoring Classic

# Использование Subresource Integrity (SRI) для кода Real User Monitoring Classic

* Практическое руководство
* Чтение 2 мин
* Опубликовано 04 марта 2025 г.

Встраивание сторонних ресурсов в веб-страницы, например ресурсов из Content Delivery Network (CDN), несёт риск того, что злоумышленник сможет получить контроль над сторонним хостом и изменить эти ресурсы. Функция браузера [Subresource Integrity (SRI)﻿](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) снижает этот риск, гарантируя использование только неизменённых ресурсов. Она делает это за счёт включения криптографического хеша, которому должен соответствовать загружаемый ресурс.

Dynatrace RUM поддерживает SRI через отдельный формат сниппета [JavaScript-тег OneAgent с SRI](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Выбрать формат JavaScript-сниппета RUM, наиболее подходящий для конкретного случая использования"). Он содержит хеш для кода мониторинга RUM. Если хеш не совпадает с кодом мониторинга, полученным браузером, код не будет выполнен.

Когда Session Replay включён, код мониторинга Session Replay внедряется на страницу с помощью JavaScript RUM в виде внешнего ресурса, что приводит к отдельному запросу. Начиная с версии JavaScript RUM 1.309, при использовании JavaScript-тега OneAgent с SRI JavaScript RUM внедряет как код мониторинга Session Replay, так и криптографический хеш для обеспечения его целостности.

SRI не поддерживается для форматов сниппета JavaScript tag и code snippet из-за несовместимости с механизмами динамического обновления, присущими этим форматам.

## Auto-injected app Настройка автоматически внедряемого приложения для использования SRI

Обратите внимание, что все подключённые ActiveGate должны иметь версию ActiveGate 1.310+ в течение как минимум 30 дней, прежде чем эта функция станет доступна.

Для автоматически внедряемых приложений код Real User Monitoring по умолчанию доставляется через OneAgent. Чтобы использовать SRI, нужно настроить приложение на запрос кода мониторинга с CDN или Cluster ActiveGate, как описано в разделе
[Настройка источника кода Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Настроить источник кода Real User Monitoring Classic под конкретные требования."). Это позволит выбрать необходимый формат сниппета.

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Real User Monitoring code source** выбрать **CDN**.
6. В раскрывающемся списке **Snippet format** выбрать **OneAgent JavaScript Tag with SRI**.

## Agentless app Настройка agentless-приложения для использования SRI

Оптимальный подход к использованию SRI для agentless-приложения, это встроить вставку JavaScript-тега OneAgent с SRI в процесс сборки через [API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Получить самый актуальный JavaScript-тег OneAgent с SRI для ручной вставки."). Это гарантирует, что приложение постоянно работает с актуальной конфигурацией.

Чтобы получить JavaScript-тег OneAgent с SRI через веб-интерфейс

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript Tag with SRI** выбрать **Copy**, чтобы скопировать тег в буфер обмена.

Не рекомендуется использовать JavaScript-тег OneAgent с SRI из веб-интерфейса, если только своевременные обновления конфигурации не являются критичными.