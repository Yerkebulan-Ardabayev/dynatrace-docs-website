---
title: Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile
---

# Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений в RUM Classic

# Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение 1 мин.
* Опубликовано 30 января 2023 г.

Dynatrace Real User Monitoring Classic группирует [пользовательские сессии и пользовательские действия по местоположению](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокацию, такую как город, регион и страна, а также браузеры, устройства и операционные системы.") и отображает их на [карте мира](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего мобильного приложения.").

Если данные по некоторым пользователям приложения не отображаются на карте мира, это может быть связано с тем, что у этих пользователей приватные IP-адреса. Такие внутренние IP-адреса можно сопоставить с реальными географическими местоположениями. Детализация регионального анализа производительности увеличивается по мере роста числа обнаруженных пользовательских запросов в конкретном регионе (континент, страна, штат или город). При необходимости можно даже переопределить автоматически определённые IP-адреса, чтобы повысить точность сопоставления.

Чтобы добавить правило сопоставления IP-адресов

1. Перейти в **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. В разделе **IP address mapping rules** выбрать **Add item**.
3. Указать IP-адрес или диапазон IP-адресов, затем задать **Country**, **Region** и **City**.

Если нужно импортировать множество пользовательских IP-адресов, удобнее использовать Dynatrace API, а именно метод [IP address mapping rules - PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Обновление конфигурации сопоставления IP-адресов через Dynatrace API.").

## Похожие темы

* [Geographic regions - IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает конфигурационный API Dynatrace для правил сопоставления IP-адресов.")