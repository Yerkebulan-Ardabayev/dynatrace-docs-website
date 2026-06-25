---
title: Определение IP-адресов, геолокаций и user agent'ов
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents
scraped: 2026-05-12T11:08:44.948599
---

# Определение IP-адресов, геолокаций и user agent'ов

# Определение IP-адресов, геолокаций и user agent'ов

* Explanation
* 3-min read
* Updated on Mar 21, 2024

Dynatrace автоматически определяет IP-адреса и геолокации, а также браузеры, устройства и операционные системы.

## IP-адреса

Когда веб-запросы и RUM beacon напрямую отправляются на инструментированный сервер, Dynatrace определяет IP-адреса устройств конечных пользователей через socket-соединения.

При использовании неинструментированных компонентов, таких как балансировщики нагрузки, CDN или прокси-серверы, удалённый IP-адрес отличается от исходного. В таких случаях Dynatrace также анализирует определённые HTTP-заголовки. Эти заголовки чаще всего используются для определения исходного IP-адреса, когда клиент подключается к веб-серверу через HTTP-прокси, CDN или балансировщик нагрузки.

Вы можете просмотреть список заголовков, которые Dynatrace использует для определения IP-адресов клиентов ваших приложений. Для этого перейдите в **Settings** > **Web and mobile monitoring** > **IP determination**. Dynatrace обрабатывает эти заголовки в определённом порядке, который можно изменить, а также добавить собственные заголовки для [веб-](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Измените способ определения Dynatrace IP-адресов клиентов в веб-приложениях."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Измените способ определения Dynatrace IP-адресов клиентов в мобильных приложениях.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Измените способ определения Dynatrace IP-адресов клиентов в пользовательских приложениях.").

Учтите, что по умолчанию Dynatrace [маскирует последнюю часть IP-адресов конечных пользователей](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Узнайте, как настроить маскирование данных конфиденциальности для IP-адресов, геолокаций и имён пользовательских действий.").

## Геолокации

Мониторинг реальных пользователей Dynatrace пытается назначить каждой [сессии пользователя](/managed/observe/digital-experience/rum-concepts/user-session "Узнайте, как определяется сессия пользователя, когда она начинается и заканчивается, как рассчитывается её продолжительность и многое другое.") геолокацию (город, регион и страна) для группировки сессий и [пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions "Узнайте, что такое пользовательские действия и как они помогают понять, что пользователи делают в вашем приложении.") по местоположению и отображения их на карте мира для ваших [веб-](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Узнайте, как карта мира даёт представление о рейтингах Apdex, действиях пользователей, длительности действий и ошибках JavaScript."), [мобильных](/managed/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего мобильного приложения.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения.").

Для веб-приложений Dynatrace использует [базу данных MaxMind Geo2](https://www.maxmind.com) для сопоставления и преобразования IP-адресов в географические местоположения.

Для мобильных приложений сопоставление IP-адресов зависит от того, предоставлено ли мобильному приложению разрешение на доступ к информации о геолокации.

* **С разрешением**. Dynatrace использует координаты устройства (GPS или Wi-Fi) и вычисляет ближайший к указанному GPS-местоположению город.
* **Без разрешения**. Dynatrace использует IP-адрес и [базу данных MaxMind Geo2](https://www.maxmind.com) для определения геолокации.

Dynatrace автоматически обновляет базу данных MaxMind Geo2 в вашей среде при каждом выпуске новой версии Dynatrace.

Запрос обновлений базы данных MaxMind при некорректном определении IP-адресов

Если вы обнаружили ошибку в сопоставлении MaxMind, вы можете [запросить обновление базы данных MaxMind](https://www.maxmind.com/en/geoip-data-correction-request). После изменения сопоставления IP-адреса MaxMind сопоставление в вашей среде Dynatrace обновляется в следующей версии Dynatrace после изменения.

Вы можете проверить свой IP-адрес в базе данных MaxMind в любое время через форму [GeoIP2 Databases Demo](https://www.maxmind.com/en/geoip-demo).

Для пользовательских местоположений с внутренними или частными IP-адресами (например, ваших офисов) вы можете определить пользовательское сопоставление IP-адресов. Вы даже можете переопределить сопоставления IP-адресов по умолчанию с помощью пользовательских правил сопоставления для ваших [веб-](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace на использование локальных адресов для определения местонахождения пользователей веб-приложений."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace на использование локальных адресов для определения местонахождения пользователей мобильных приложений.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов для определения местонахождения пользователей пользовательских приложений.").

Dynatrace также по умолчанию [маскирует GPS-координаты](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Узнайте, как настроить маскирование данных конфиденциальности для IP-адресов, геолокаций и имён пользовательских действий.").

## Браузеры, устройства и операционные системы

Для веб-приложений Dynatrace использует [строку user agent](https://developer.mozilla.org/docs/Web/HTTP/Headers/User-Agent), отправляемую браузером, для разграничения сессий реальных пользователей и синтетических/роботов (типы пользователей: **Bot**, **Real** и **Synthetic**). Также эта строка используется для идентификации операционных систем и типов устройств (десктоп, планшет или мобильное устройство). Для классификации браузеров Dynatrace использует базу данных user agent [udger.com](https://udger.com).

Для Android-приложений имена устройств предоставляются [Google Play Store](https://support.google.com/googleplay/answer/1727131?hl=en-GB). Для iOS-приложений Dynatrace поддерживает перекрёстный справочник, сопоставляющий идентификаторы устройств Apple с их именами. Операционная система (Android или iOS) предоставляется Dynatrace OneAgent для мобильных устройств.

Интернет-провайдеры (ISP) определяются на основе их IP-адресов по базе данных MaxMind.