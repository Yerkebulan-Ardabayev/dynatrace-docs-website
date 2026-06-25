---
title: Использование Subresource Integrity (SRI) для кода Real User Monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity
scraped: 2026-05-12T11:35:10.217596
---

# Использование Subresource Integrity (SRI) для кода Real User Monitoring

# Использование Subresource Integrity (SRI) для кода Real User Monitoring

* How-to guide
* 2-min read
* Published Mar 04, 2025

Интеграция сторонних ресурсов в веб-страницы, например с Content Delivery Network (CDN), сопряжена с риском того, что злоумышленник может получить контроль над сторонним хостом и изменить эти ресурсы. Функция браузера [Subresource Integrity (SRI)](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) снижает этот риск, гарантируя использование только неизменённых ресурсов. Для этого включается криптографический хэш, которому должен соответствовать полученный ресурс.

Dynatrace RUM поддерживает SRI через специальный формат фрагмента [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case"). Он содержит хэш для кода мониторинга RUM. Если хэш не совпадает с кодом мониторинга, полученным браузером, код не будет выполнен.

Когда Session Replay включён, код мониторинга Session Replay инжектируется в страницу RUM JavaScript как внешний ресурс, что приводит к отдельному запросу. Начиная с версии RUM JavaScript 1.309, при использовании OneAgent JavaScript tag with SRI RUM JavaScript будет инжектировать как код мониторинга Session Replay, так и криптографический хэш для обеспечения его целостности.

SRI не поддерживается для форматов фрагментов JavaScript tag и code snippet из-за несовместимости с динамическими механизмами обновления, присущими этим форматам.

## Настройка автоматически инжектируемого приложения для использования SRI

Обратите внимание, что все подключённые ActiveGate должны работать на версии ActiveGate 1.310+ не менее 30 дней, прежде чем эта функция станет доступна.

Для автоматически инжектируемых приложений код Real User Monitoring по умолчанию доставляется OneAgent. Для использования SRI необходимо настроить приложение для запроса кода мониторинга с вашего CDN или Cluster ActiveGate, как описано в разделе
[Configure the Real User Monitoring code source](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source#request-rum-monitoring-code-from-cdn "Configure the Real User Monitoring code source for your specific requirements."). Это позволит выбрать необходимый формат фрагмента.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Automatic injection**.
5. В раскрывающемся списке **Real User Monitoring code source** выберите **CDN**.
6. В раскрывающемся списке **Snippet format** выберите **OneAgent JavaScript Tag with SRI**.

## Настройка агентлесс-приложения для использования SRI

Оптимальный подход к использованию SRI для агентлесс-приложения — интегрировать вставку OneAgent JavaScript tag with SRI в процесс сборки через [API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion."). Это обеспечивает постоянную работу приложения с актуальной конфигурацией.

Чтобы получить OneAgent JavaScript tag with SRI из веб-интерфейса:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript Tag with SRI** выберите **Copy** для копирования тега в буфер обмена.

Использование OneAgent JavaScript tag with SRI из веб-интерфейса не рекомендуется, если своевременность обновлений конфигурации не является критичной.