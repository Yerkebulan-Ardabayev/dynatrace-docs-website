---
title: Сопоставление внутренних IP-адресов с расположениями для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web
scraped: 2026-05-12T11:18:02.579269
---

# Сопоставление внутренних IP-адресов с расположениями для веб-приложений

# Сопоставление внутренних IP-адресов с расположениями для веб-приложений

* How-to guide
* 1-min read
* Published Jul 19, 2017

Dynatrace Real User Monitoring группирует [пользовательские сессии и действия по расположению](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") и отображает их на [карте мира](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.").

Если данные некоторых пользователей приложения не отображаются на карте мира, возможно, это связано с тем, что у них частные IP-адреса. Такие внутренние IP-адреса можно сопоставить с реальными географическими расположениями. Детализация регионального анализа производительности возрастает по мере увеличения количества обнаруженных пользовательских запросов в конкретном регионе (континент, страна, штат/область или город). При необходимости для повышения точности сопоставления можно также переопределить автоматически определённые IP-адреса.

Чтобы добавить правило сопоставления IP-адреса:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. В разделе **IP address mapping rules** выберите **Add item**.
3. Укажите IP-адрес или диапазон IP-адресов, затем задайте **Country**, **Region** и **City**.

При наличии большого количества пользовательских IP-адресов для импорта удобнее использовать Dynatrace API, а именно метод [IP address mapping rules — PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Update the configuration of IP address mapping via the Dynatrace API.").

## Связанные темы

* [Geographic regions — IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Learn what the Dynatrace configuration API for IP address mapping rules offers.")