---
title: Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile
scraped: 2026-05-12T11:18:00.114234
---

# Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений

# Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений

* How-to guide
* 1-min read
* Published Jan 30, 2023

Real User Monitoring в Dynatrace группирует [пользовательские сессии и действия по местоположению](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокации (город, регион, страну), а также браузеры, устройства и операционные системы.") и отображает их на [карте мира](/managed/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта мобильного приложения.").

Если данные некоторых пользователей вашего приложения не отображаются на карте мира, возможно, эти пользователи имеют частные IP-адреса. Вы можете сопоставить такие внутренние IP-адреса с реальными географическими местоположениями. Детализация регионального анализа производительности увеличивается по мере роста числа обнаруженных запросов пользователей в конкретном регионе (континент, страна, штат/область или город). При необходимости вы также можете переопределить автоматически определённые IP-адреса для повышения точности сопоставления.

Чтобы добавить правило сопоставления IP-адресов:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. В разделе **IP address mapping rules** нажмите **Add item**.
3. Укажите IP-адрес или диапазон IP-адресов, затем задайте **Country**, **Region** и **City**.

Если у вас много пользовательских IP-адресов для импорта, удобнее использовать Dynatrace API, а именно метод [IP address mapping rules — PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Обновляйте конфигурацию сопоставления IP-адресов через Dynatrace API.").

## Связанные темы

* [Geographic regions — IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает API конфигурации Dynatrace для правил сопоставления IP-адресов.")