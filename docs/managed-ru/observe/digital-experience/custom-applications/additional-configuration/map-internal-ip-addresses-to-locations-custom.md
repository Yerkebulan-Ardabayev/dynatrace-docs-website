---
title: Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom
scraped: 2026-05-12T11:17:58.931329
---

# Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях

# Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях

* How-to guide
* 1-min read
* Published Jan 30, 2023

Мониторинг реальных пользователей Dynatrace группирует [сессии и действия пользователей по местоположению](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокации (город, регион, страну), а также браузеры, устройства и операционные системы.") и отображает их на [карте мира](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения.").

Если данные о некоторых пользователях вашего приложения отсутствуют на карте мира, возможно, у этих пользователей частные IP-адреса. Вы можете сопоставить такие внутренние IP-адреса с реальными географическими местоположениями. Детализация регионального анализа производительности повышается по мере роста числа обнаруженных запросов пользователей в конкретном регионе (континент, страна, штат или город). При необходимости для повышения точности сопоставления можно переопределить автоматически определённые IP-адреса.

Чтобы добавить правило сопоставления IP-адресов:

1. Перейдите в **Settings** > **Web and mobile monitoring** > **Map IP addresses to locations**.
2. В разделе **IP address mapping rules** нажмите **Add item**.
3. Укажите IP-адрес или диапазон IP-адресов, а также задайте **Country**, **Region** и **City**.

Если у вас большое количество пользовательских IP-адресов для импорта, удобнее использовать Dynatrace API: метод [IP address mapping rules - PUT configuration](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Обновляйте конфигурацию сопоставления IP-адресов через Dynatrace API.").

## Связанные темы

* [Geographic regions - IP address mapping rules API](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address "Узнайте, что предлагает Dynatrace configuration API для правил сопоставления IP-адресов.")