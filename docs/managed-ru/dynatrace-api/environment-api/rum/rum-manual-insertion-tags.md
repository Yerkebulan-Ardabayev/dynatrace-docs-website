---
title: RUM manual insertion tags API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags
scraped: 2026-05-12T11:56:03.238302
---

# RUM manual insertion tags API

# RUM manual insertion tags API

* Reference

API **RUM manual insertion tags** позволяет получать RUM JavaScript для двух разных сценариев ручного внедрения:

* [безагентный мониторинг](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройте безагентный мониторинг для ваших веб-приложений.") и
* [Ручное внедрение для страниц приложения с автоматической инжекцией](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Настройте автоматическое внедрение RUM JavaScript в страницы ваших приложений").

Доступны различные [snippet formats](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария."), а поддерживаемые атрибуты тега можно контролировать через параметры API. Интегрировав этот API в свои сборочные скрипты, вы можете автоматизировать внедрение RUM JavaScript и гарантировать, что ваше приложение всегда использует текущую конфигурацию.

Чтобы получить формат фрагмента [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария."), используйте [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как использовать Dynatrace API для настройки и сопровождения ваших приложений с ручным внедрением через Real User Monitoring JavaScript API.").

[### Получить тег JavaScript

Получить самый последний тег JavaScript для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Получить самый последний тег JavaScript для ручного внедрения.")[### Получить тег OneAgent JavaScript

Получить самый последний тег OneAgent JavaScript для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Получить самый последний тег OneAgent JavaScript для ручного внедрения.")[### Получить тег OneAgent JavaScript с SRI

Получить самый последний тег OneAgent JavaScript с SRI для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Получить самый последний тег OneAgent JavaScript с SRI для ручного внедрения.")[### Получить встроенный код

Получить самый последний встроенный код для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Получить самый последний встроенный код для ручного внедрения.")