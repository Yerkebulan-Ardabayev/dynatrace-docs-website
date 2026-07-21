---
title: Настройка параметров конфиденциальности данных для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr
---

# Настройка параметров конфиденциальности данных для веб-приложений в RUM Classic

# Настройка параметров конфиденциальности данных для веб-приложений в RUM Classic

* Практическое руководство
* 2 мин на чтение
* Обновлено 27 апреля 2026 г.

Обеспечение конфиденциальности персональных данных клиентов сегодня, это ключевой элемент успеха цифрового бизнеса. Dynatrace предоставляет множество усовершенствований в области конфиденциальности, которые упрощают настройку параметров, защищающих персональные данные клиентов и обеспечивающих соответствие организации требованиям GDPR или других нормативных актов о защите данных.

Подробнее о глобальных настройках конфиденциальности данных см. в разделе [Настройка параметров конфиденциальности данных](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Узнайте, как настроить маскирование данных о конфиденциальности для IP-адресов конечных пользователей, геолокации и имён пользовательских действий.").

Чтобы получить доступ к настройкам конфиденциальности данных для веб-приложения

1. Перейти в раздел **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **General settings** > **Data privacy** > **General**. Откроется страница **Data privacy**.

На этой странице доступны следующие настройки:

* [Маскирование персональных данных в URI](#mask-uris)
* [Маскирование пользовательских действий](#mask-user-actions)
* [Отслеживание пользователей](#user-tracking)
* [Режим Opt-in](#user-opt-in-mode-gdpr)
* [Do Not Track](#do-not-track-gdpr)
* [Маскирование IP-адресов и GPS-координат](#mask-ip-and-gps)

Подробное описание каждой настройки приведено в разделах ниже.

## Маскирование персональных данных в URI

Чтобы получить доступ к этой опции, в настройках приложения нужно выбрать **General settings** > **Data privacy** > **General**.

🔴 Отключено по умолчанию

Dynatrace фиксирует полные URI запросов, отправляемых из настольных и мобильных браузеров, а также URI запросов, отправляемых и получаемых в рамках отслеживаемых серверных процессов. URI могут содержать персональные данные, такие как имена пользователей, пароли или идентификаторы.

Когда включена опция **Mask personal data in URIs**, Dynatrace обнаруживает персональные данные, адреса электронной почты, IBAN, номера платёжных карт, IP-адреса, UUID и другие идентификаторы, в URI, заголовках, сообщениях об исключениях и данных, собранных для атрибутов запросов. При сохранении эти данные маскируются заменой на строку `<masked>`. Значения параметров запроса также заменяются строкой `<masked>`. Чтобы идентификаторы и числа были замаскированы, они должны содержать не менее 5 десятичных или шестнадцатеричных цифр.

Примеры маскирования URI

| Тип персональных данных | Пример до маскирования | Пример после маскирования |
| --- | --- | --- |
| Адрес электронной почты | `https://example.com/user/john.doe@example.com/profile` | `https://example.com/user/<masked>/profile` |
| Значение параметра запроса | `https://example.com?country=Austria&city=Linz` | `https://example.com?country=<masked>&city=<masked>` |
| Номер платёжной карты | `https://example.com/checkout?card=4111111111111111` | `https://example.com/checkout?card=<masked>` |
| IP-адрес | `https://192.168.10.25/dashboard` | `https://<masked>/dashboard` |

В результате персональные данные маскируются в анализе распределённой трассировки, анализе ошибок, именах пользовательских действий для RUM и в других местах Dynatrace.

Обратите внимание: есть разница между данными, замаскированными звёздочками `*****`, и данными, заменёнными на `<masked>`. Подробнее см. в разделе [Маскирование при отображении](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Узнайте, как настроить маскирование данных о конфиденциальности для IP-адресов конечных пользователей, геолокации и имён пользовательских действий.").

## Маскирование пользовательских действий

Чтобы получить доступ к этой опции, в настройках приложения нужно выбрать **General settings** > **Data privacy** > **General**.

🔴 Отключено по умолчанию

Опция **Mask user actions (web applications only)** влияет на Real User Monitoring только для веб-приложений. При включении этой опции Dynatrace использует обобщённые значения для имён пользовательских действий.

Когда Dynatrace обнаруживает пользовательское действие, вызывающее загрузку страницы или AJAX/XHR-действие, он формирует имя пользовательского действия на основе:

* типа пользовательского события, например, `click on...`, `loading of page...` или `keypress on...`;
* заголовка, подписи, метки, значения, ID, className или другого доступного свойства связанного HTML-элемента, например, изображения, кнопки, флажка или текстового поля ввода.

В большинстве случаев подход по умолчанию к именованию пользовательских действий работает хорошо, в результате получаются такие имена пользовательских действий:

* `click on "Search" on page /search.html`
* `keypress on "Feedback" on page /contact.html`
* `touch on "Homescreen" of page /list.jsf`

В редких случаях адреса электронной почты, имена пользователей или другие конфиденциальные данные могут непреднамеренно попадать в имена пользовательских действий. Это происходит, когда конфиденциальные данные содержатся в метке, атрибуте или другом значении HTML-элемента, в результате чего появляются такие имена пользовательских действий, как `click on "My Account Number: 1231231"`. Если такие конфиденциальные данные появляются в именах пользовательских действий приложения, нужно включить **Mask user actions (web applications only)**. Эта настройка заменяет конкретные имена и значения HTML-элементов обобщёнными именами HTML-элементов.

При включённом маскировании имён пользовательских действий указанные выше имена пользовательских действий будут выглядеть так:

* `click on INPUT on page /search.html`
* `keypress on TEXTAREA on page /contact.html`
* `touch on DIV of page /list.jsf`

## Отслеживание пользователей

Чтобы получить доступ к этой опции, в настройках приложения нужно выбрать **General settings** > **Data privacy** > **General**.

🔴 Отключено по умолчанию

Настройка **Use persistent cookies for user tracking** позволяет включить или отключить использование постоянных cookie-файлов для идентификации возвращающихся пользователей.

При включении этой настройки RUM JavaScript устанавливает в браузерах конечных пользователей постоянный cookie-файл `rxVisitor`, указывающий на то, что браузер уже использовался ранее для доступа к приложению. При отключении RUM Classic больше не может связывать сеансы одного и того же пользователя между перезапусками браузера. Подробнее о том, [как хранится этот cookie-файл](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#web-storage "Узнайте, как Dynatrace RUM и Session Replay используют cookie-файлы, web storage и IndexedDB.").

### Настройка времени жизни cookie-файла

По умолчанию cookie-файл `rxVisitor` хранится два года. Если применимое законодательство о защите данных требует более короткого срока хранения постоянных cookie-файлов, для сокращения времени жизни cookie-файла `rxVisitor` нужно использовать пользовательское свойство конфигурации.

1. Перейти в раздел **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Capturing** > **Custom configuration properties**.
5. Выбрать **Add a custom configuration property** и ввести пару ключ-значение `rvcl=<time-in-months>`, чтобы задать нужное время жизни cookie-файла. Максимальное значение составляет 24 месяца.

   Например, `rvcl=12` означает 12 месяцев.

## Режим Opt-in

Чтобы получить доступ к этой опции, в настройках приложения нужно выбрать **General settings** > **Data privacy** > **General**.

🔴 Отключено по умолчанию

Чтобы дать конечным пользователям возможность самим решать, следует ли отслеживать их действия, нужно включить режим opt-in.

По умолчанию RUM автоматически создаёт [cookie-файлы](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#dynatrace-rum-cookies "Узнайте, как Dynatrace RUM и Session Replay используют cookie-файлы, web storage и IndexedDB."). Когда включена опция **Data-collection and opt-in mode**, ни OneAgent, ни RUM JavaScript не устанавливают cookie-файлы, и RUM JavaScript не собирает никаких данных. После того как конечный пользователь принимает политику использования cookie-файлов, можно активировать RUM для этого пользователя с помощью вызова JavaScript API [`dtrum.enable()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enable). С помощью вызова API [`dtrum.disable()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disable) можно реализовать диалоговое окно, позволяющее конечным пользователям прекратить отправку данных мониторинга в Dynatrace, даже если они ранее уже дали согласие и `dtrum.enable()` уже был вызван.

## Do Not Track

Чтобы получить доступ к этой опции, в настройках приложения нужно выбрать **General settings** > **Data privacy** > **General**.

🟢 Включено по умолчанию

Ещё один способ защиты конфиденциальности конечных пользователей, это функция «Do Not Track». Когда пользователь включает эту функцию, его браузер добавляет HTTP-заголовок запроса `DNT` ко всем исходящим веб-запросам. Этот заголовок указывает, что пользователь предпочитает, чтобы его не отслеживали.

После включения опции **Comply with "Do Not Track" browser settings** можно выбрать один из двух вариантов:

* **Capture anonymous user sessions for "Do Not Track"-enabled browsers**: при обнаружении заголовка `DNT` Dynatrace собирает данные RUM, но исключает всю персональную информацию, которая может привести к идентификации пользователя. IP-адрес маскируется, и информация [тега пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Узнайте о пользовательских событиях и событиях ошибок, а также о типах пользовательских событий и событий ошибок, фиксируемых Dynatrace.") не отправляется.

  При включённой [настройке **User tracking**](#user-tracking) Dynatrace по-прежнему устанавливает постоянный cookie-файл для обнаружения возвращающихся пользователей.
* **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**: при обнаружении заголовка `DNT` Dynatrace не собирает никаких данных из браузеров, у которых включена настройка «Do Not Track».

Если опция **Comply with "Do Not Track" browser settings** отключена, Dynatrace игнорирует настройку браузера «Do Not Track» и заголовок `DNT`.

Опция **Comply with "Do Not Track" browser settings** с вариантом **Capture anonymous user sessions for "Do Not Track"-enabled browsers** включена по умолчанию для всех сред и приложений.

## Маскирование IP-адресов и GPS-координат

Чтобы получить доступ к этой настройке, в настройках приложения выбери **General settings** > **Data privacy** > **General** > **IP masking**.

Чтобы определить регион, из которого конечные пользователи обращаются к веб- и мобильным фронтендам, Dynatrace фиксирует их IP-адреса. GPS-координаты фиксируются только для мобильных фронтендов.

Когда включена опция **Mask end-user IP addresses and GPS coordinates**, IP-адреса маскируются на [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Последний октет отслеживаемых IPv4-адресов и последние 80 бит IPv6-адресов заменяются нулями. [Geolocation lookups](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#geolocations "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") выполняются с использованием замаскированных IP-адресов.

## Похожие темы

* [Configure Session Replay Classic for web applications](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay Classic.")