---
title: Определение IP-адресов, геолокаций и user agent в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents
---

# Определение IP-адресов, геолокаций и user agent в RUM Classic

# Определение IP-адресов, геолокаций и user agent в RUM Classic

* Пояснение
* Чтение за 3 минуты
* Обновлено 21 марта 2024 г.

Dynatrace автоматически определяет IP-адреса и геолокации, а также браузеры, устройства и операционные системы.

## IP-адреса

Когда веб-запросы и RUM-маячки отправляются напрямую на инструментированный сервер, Dynatrace определяет IP-адреса устройств конечных пользователей через сокетные соединения.

При использовании неинструментированных компонентов, таких как балансировщики нагрузки, CDN или прокси, удалённый IP-адрес отличается от исходного. В таких случаях Dynatrace также отслеживает определённые HTTP-заголовки. Эти заголовки чаще всего используются для определения исходного IP-адреса, когда клиент подключается к веб-серверу через HTTP-прокси, CDN или балансировщик нагрузки.

Список заголовков, которые Dynatrace использует для определения IP-адресов клиентов ваших приложений, можно посмотреть в разделе **Settings** > **Web and mobile monitoring** > **IP determination**. Dynatrace обрабатывает эти заголовки в определённом порядке, но порядок обработки можно изменить и добавить собственные заголовки для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Change the way Dynatrace determines client IP addresses for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.").

Учитывай, что по умолчанию Dynatrace [маскирует последнюю часть IP-адресов конечных пользователей](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Геолокации

Dynatrace Real User Monitoring Classic пытается присвоить каждой [пользовательской сессии](/managed/observe/digital-experience/rum-classic/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") геолокацию (город, регион и страну), чтобы группировать пользовательские сессии и [действия пользователей](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") по местоположению и показывать их на карте мира для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your mobile application.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Learn how to use Dynatrace to check the user experience metrics of your custom application.").

Для веб-приложений Dynatrace использует [базу данных MaxMind Geo2﻿](https://www.maxmind.com) для сопоставления и определения географического местоположения по IP-адресам.

Для мобильных приложений сопоставление IP-адресов зависит от того, есть ли у мобильного приложения разрешение на доступ к данным геолокации.

* **С разрешением**. Dynatrace использует координаты устройства (GPS или Wi-Fi) и вычисляет город, ближайший к сообщённому GPS-местоположению.
* **Без разрешения**. Dynatrace использует IP-адрес и [базу данных MaxMind Geo2﻿](https://www.maxmind.com) для определения геолокации.

Dynatrace автоматически обновляет базу данных MaxMind Geo2 в вашей среде с выходом каждой новой версии Dynatrace.

Запрос на обновление базы данных MaxMind, если IP-адреса определяются некорректно

Если обнаружена ошибка в сопоставлении MaxMind, можно [запросить у MaxMind обновление их базы данных﻿](https://www.maxmind.com/en/geoip-data-correction-request). После того как MaxMind изменит сопоставление IP-адреса, это сопоставление в вашей среде Dynatrace обновится с версией Dynatrace, следующей за изменением.

Проверить свой IP-адрес по базе данных MaxMind можно в любой момент через форму [GeoIP2 Databases Demo﻿](https://www.maxmind.com/en/geoip-demo).

Для пользовательских местоположений с внутренними или частными IP-адресами, например для разных офисов, можно задать собственные сопоставления IP-адресов. Можно даже переопределить сопоставления IP-адресов по умолчанию с помощью пользовательских правил сопоставления IP-адресов для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.").

По умолчанию Dynatrace также [маскирует координаты GPS](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Браузеры, устройства и операционные системы

Для веб-приложений Dynatrace использует [строку user agent﻿](https://developer.mozilla.org/docs/Web/HTTP/Headers/User-Agent), отправляемую браузером, чтобы отличать пользовательские сессии реальных пользователей от синтетических и роботов (типы пользователей: **Bot**, **Real** и **Synthetic**). Также эта строка используется для определения операционных систем и типов устройств, таких как настольный компьютер, планшет или мобильное устройство. Для классификации браузеров Dynatrace использует базу данных user agent [udger.com﻿](https://udger.com).

Для приложений Android названия устройств предоставляются [Google Play Store﻿](https://support.google.com/googleplay/answer/1727131?hl=en-GB). Для приложений iOS Dynatrace ведёт перекрёстный список сопоставления идентификаторов устройств Apple с их названиями. Операционная система, Android или iOS, предоставляется Dynatrace OneAgent for Mobile.

Провайдеры интернет-услуг (ISP) определяются по их IP-адресам с помощью базы данных MaxMind.