---
title: RUM manual insertion tags API
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags
scraped: 2026-03-06T21:32:36.491296
---

# API тегов ручной вставки RUM


* Reference

**API тегов ручной вставки RUM** позволяет получать JavaScript для RUM в двух различных сценариях ручной вставки:

* [Мониторинг без агента](../../../observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring.md "Set up agentless monitoring for your web applications.") и
* [Ручная вставка для страниц автоматически внедряемого приложения](../../../observe/digital-experience/web-applications/initial-setup/rum-injection.md#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").

Доступны различные [форматы фрагментов](../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md "Select a format for the RUM JavaScript snippet that best fits your specific use case"), а поддерживаемые атрибуты тегов можно контролировать через параметры API. Интегрируя этот API в свои скрипты сборки, вы можете автоматизировать вставку JavaScript для RUM и гарантировать, что ваше приложение всегда использует актуальную конфигурацию.

Для получения [фрагмента кода](../../../observe/digital-experience/web-applications/initial-setup/snippet-formats.md#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case") в формате фрагмента используйте [API JavaScript для Real User Monitoring](real-user-monitoring-javascript-code.md "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

[### Получить JavaScript-тег

Получите актуальный JavaScript-тег для ручной вставки.](rum-manual-insertion-tags/get-javascript-tag.md "Retrieve the most recent JavaScript tag for manual insertion.")[### Получить JavaScript-тег OneAgent

Получите актуальный JavaScript-тег OneAgent для ручной вставки.](rum-manual-insertion-tags/get-oneagent-javascript-tag.md "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")[### Получить JavaScript-тег OneAgent с SRI

Получите актуальный JavaScript-тег OneAgent с SRI для ручной вставки.](rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri.md "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.")[### Получить встроенный код

Получите актуальный встроенный код для ручной вставки.](rum-manual-insertion-tags/get-inline-code.md "Retrieve the most recent inline code for manual insertion.")
