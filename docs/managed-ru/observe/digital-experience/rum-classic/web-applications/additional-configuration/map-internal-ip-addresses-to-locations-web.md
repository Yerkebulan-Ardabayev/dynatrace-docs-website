---
title: Сопоставление внутренних IP-адресов с местоположением для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web
---

# Сопоставление внутренних IP-адресов с местоположением для веб-приложений в RUM Classic

# Сопоставление внутренних IP-адресов с местоположением для веб-приложений в RUM Classic

* Практическое руководство
* Чтение за 1 минуту
* Опубликовано 19 июля 2017 г.

Dynatrace Real User Monitoring Classic группирует [пользовательские сессии и действия пользователей по местоположению](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокацию, такую как город, регион и страна, а также браузеры, устройства и операционные системы.") и показывает их на [карте мира](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Узнать, как представление World map даёт информацию о показателях Apdex, действиях пользователей, длительности действий и ошибках JavaScript.").

Если данные по некоторым пользователям приложения не отображаются на карте мира, причина может быть в том, что у этих пользователей приватные IP-адреса. Такие внутренние IP-адреса можно сопоставить с реальными географическими местоположениями. Детализация анализа производительности по регионам растёт по мере увеличения числа обнаруженных пользовательских запросов в конкретном регионе (континент, страна, штат/область или город). При необходимости можно даже переопределить автоматически обнаруженные IP-адреса, чтобы повысить точность сопоставления.

Чтобы добавить правило сопоставления IP-адресов

1. Перейти в **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. В разделе **IP address mapping rules** выбрать **Add item**.
3. Указать IP-адрес или диапазон IP-адресов, затем задать **Country**, **Region** и **City**.

Если нужно импортировать множество пользовательских IP-адресов, удобнее использовать Dynatrace API, а именно метод [IP address mapping rules - PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Обновление конфигурации сопоставления IP-адресов через Dynatrace API.").

## Смежные темы

* [Geographic regions - IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнать, что предлагает конфигурационный API Dynatrace для правил сопоставления IP-адресов.")