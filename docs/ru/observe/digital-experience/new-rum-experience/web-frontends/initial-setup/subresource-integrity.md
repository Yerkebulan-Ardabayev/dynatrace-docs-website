---
title: Использование Subresource Integrity (SRI) в новом опыте RUM
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/subresource-integrity
scraped: 2026-03-03T21:25:12.585695
---

# Использование Subresource Integrity (SRI) в новом интерфейсе RUM


* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

Интеграция сторонних ресурсов на веб-страницы, например с сети доставки контента (CDN), создаёт риск того, что злоумышленник может получить контроль над сторонним хостом и манипулировать этими ресурсами. Функция браузера [Subresource Integrity (SRI)](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) снижает этот риск, гарантируя использование только неизменённых ресурсов. Это достигается путём включения криптографического хеша, которому должен соответствовать загруженный ресурс.

Dynatrace RUM поддерживает SRI через специальный формат сниппета — [тег OneAgent JavaScript с SRI](snippet-formats.md#oneagent-js-tag-sri "Узнайте, как выбрать формат JavaScript-сниппета RUM, наиболее подходящий для вашего сценария в новом интерфейсе RUM."). Он содержит криптографический хеш для кода мониторинга RUM. Если криптографический хеш не совпадает с кодом мониторинга, полученным браузером, код не будет выполнен.

Если включён Session Replay Classic, код мониторинга Session Replay Classic внедряется на вашу страницу JavaScript-кодом RUM в виде внешнего ресурса, что приводит к отдельному запросу. При использовании тега OneAgent JavaScript с SRI JavaScript-код RUM внедряет как код мониторинга Session Replay, так и криптографический хеш для обеспечения его целостности.

SRI не поддерживается для формата сниппета JavaScript tag из-за несовместимости с механизмом динамического обновления, присущим этому формату.

## Автоматически внедряемый фронтенд — настройка автоматически внедряемого фронтенда для использования SRI

Обратите внимание, что все подключённые ActiveGate должны работать на версии ActiveGate 1.310+ не менее 30 дней, прежде чем эта функция станет доступна.

Для автоматически внедряемых фронтендов код Real User Monitoring по умолчанию доставляется OneAgent. Чтобы использовать SRI, необходимо [настроить фронтенд для получения кода мониторинга из Dynatrace CDN](configure-monitoring-code-source.md#request-rum-monitoring-code-from-cdn "Настройте источник кода Real User Monitoring в новом интерфейсе RUM в соответствии с вашими требованиями."), что позволит выбрать необходимый формат сниппета.

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который нужно настроить.
4. На вкладке **Settings** выберите **Automatic injection**.
5. В разделе **Real User Monitoring code source** выберите **CDN**.
6. В разделе **Snippet format** выберите **OneAgent JavaScript Tag with SRI**.
7. Нажмите **Save**.

## Безагентный фронтенд — настройка безагентного фронтенда для использования SRI

Оптимальный подход к использованию SRI для безагентного фронтенда — это интеграция вставки тега OneAgent JavaScript с SRI в ваш процесс сборки через [API](../../../../../dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri.md "Получите последний тег OneAgent JavaScript с SRI для ручной вставки."). Это гарантирует, что ваш фронтенд всегда работает с актуальной конфигурацией.

Получение тега OneAgent JavaScript с SRI через веб-интерфейс

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который нужно инструментировать.
4. На вкладке **Settings** выберите **Manual insertion**.
5. Прокрутите до раздела **OneAgent JavaScript Tag with SRI** и нажмите кнопку копирования, чтобы скопировать JavaScript-код RUM в буфер обмена.

Не рекомендуется использовать тег OneAgent JavaScript с SRI из веб-интерфейса, если своевременное обновление конфигурации не является критически важным.

## Связанные темы

* [Выбор формата сниппета в новом интерфейсе RUM](snippet-formats.md "Узнайте, как выбрать формат JavaScript-сниппета RUM, наиболее подходящий для вашего сценария в новом интерфейсе RUM.")
* [Настройка автоматического внедрения в новом интерфейсе RUM](configure-auto-injection.md "Настройте автоматическое внедрение JavaScript-кода RUM на страницы ваших фронтендов в новом интерфейсе RUM.")
* [Настройка безагентного RUM в новом интерфейсе RUM](set-up-agentless-monitoring.md "Узнайте, как настроить безагентный RUM для ваших веб-фронтендов в новом интерфейсе RUM.")
