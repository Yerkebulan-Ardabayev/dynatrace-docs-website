---
title: Настройка параметров конфиденциальности данных для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr
scraped: 2026-05-12T11:08:39.820577
---

# Настройка параметров конфиденциальности данных для веб-приложений

# Настройка параметров конфиденциальности данных для веб-приложений

* How-to guide
* 2-min read
* Updated on Apr 27, 2026

Обеспечение конфиденциальности персональных данных клиентов является ключевым элементом успеха цифрового бизнеса. Dynatrace предоставляет многочисленные улучшения в области конфиденциальности, которые позволяют легко настроить соответствующие параметры для защиты персональных данных клиентов и соблюдения требований GDPR или иных законодательных актов о конфиденциальности данных.

Подробнее о глобальных параметрах конфиденциальности данных см. раздел [Настройка параметров конфиденциальности данных](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

Чтобы получить доступ к параметрам конфиденциальности данных для веб-приложения:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Data privacy** > **General**. Откроется страница **Data privacy**.

На этой странице доступны следующие параметры:

* [Маскирование персональных данных в URI](#mask-uris)
* [Маскирование пользовательских действий](#mask-user-actions)
* [Отслеживание пользователей](#user-tracking)
* [Режим opt-in](#user-opt-in-mode-gdpr)
* [Do Not Track](#do-not-track-gdpr)
* [Маскирование IP-адресов и GPS-координат](#mask-ip-and-gps)

Подробное описание каждого параметра приведено в соответствующих разделах ниже.

## Маскирование персональных данных в URI

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** в настройках приложения.

По умолчанию отключено

Dynatrace фиксирует полные URI запросов, отправляемых из браузеров на настольных и мобильных устройствах, а также URI запросов, отправляемых и получаемых в мониторируемых серверных процессах. URI могут содержать персональные данные, например имена пользователей, пароли или идентификаторы.

При включении параметра **Mask personal data in URIs** Dynatrace обнаруживает персональные данные — адреса электронной почты, IBAN, номера платёжных карт, IP-адреса, UUID и другие идентификаторы — в URI, заголовках, сообщениях исключений и данных, захваченных для атрибутов запросов. При хранении эти данные маскируются путём замены строкой `<masked>`. Значения параметров запроса также заменяются строкой `<masked>`. Идентификаторы и числа должны содержать не менее 5 десятичных или шестнадцатеричных цифр для маскирования.

Примеры маскирования URI

| Тип персональных данных | Пример до маскирования | Пример после маскирования |
| --- | --- | --- |
| Адрес электронной почты | `https://example.com/user/john.doe@example.com/profile` | `https://example.com/user/<masked>/profile` |
| Значение параметра запроса | `https://example.com?country=Austria&city=Linz` | `https://example.com?country=<masked>&city=<masked>` |
| Номер платёжной карты | `https://example.com/checkout?card=4111111111111111` | `https://example.com/checkout?card=<masked>` |
| IP-адрес | `https://192.168.10.25/dashboard` | `https://<masked>/dashboard` |

В результате персональные данные маскируются при анализе распределённых трассировок, анализе ошибок, именах пользовательских действий для RUM и в других местах Dynatrace.

Следует отметить разницу между данными, маскированными звёздочками `*****`, и данными, замененными строкой `<masked>`. Подробнее см. раздел [Маскирование при отображении](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#masking-at-display "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Маскирование пользовательских действий

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** в настройках приложения.

По умолчанию отключено

Параметр **Mask user actions (web applications only)** влияет на Real User Monitoring только для веб-приложений. При включении этого параметра Dynatrace использует обобщённые значения для имён пользовательских действий.

Когда Dynatrace обнаруживает пользовательское действие, инициирующее загрузку страницы или AJAX/XHR-действие, он формирует имя пользовательского действия на основе:

* типа пользовательского события, например `click on...`, `loading of page...` или `keypress on...`;
* заголовка, подписи, метки, значения, идентификатора, класса или другого доступного свойства связанного HTML-элемента, например изображения, кнопки, флажка или текстового поля ввода.

В большинстве случаев стандартный подход к именованию пользовательских действий работает хорошо, формируя имена вида:

* `click on "Search" on page /search.html`
* `keypress on "Feedback" on page /contact.html`
* `touch on "Homescreen" of page /list.jsf`

В редких случаях адреса электронной почты, имена пользователей или другие конфиденциальные данные могут непреднамеренно включаться в имена пользовательских действий. Это происходит, когда конфиденциальные данные содержатся в метке, атрибуте или другом значении HTML-элемента, что приводит к именам пользовательских действий вида `click on "My Account Number: 1231231"`. Если такие конфиденциальные данные присутствуют в именах пользовательских действий вашего приложения, включите **Mask user actions (web applications only)**. Этот параметр заменяет конкретные имена и значения HTML-элементов обобщёнными именами.

При включённом маскировании имён пользовательских действий приведённые выше имена отображаются как:

* `click on INPUT on page /search.html`
* `keypress on TEXTAREA on page /contact.html`
* `touch on DIV of page /list.jsf`

## Отслеживание пользователей

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** в настройках приложения.

По умолчанию отключено

Параметр **Use persistent cookies for user tracking** позволяет включить или отключить использование постоянных cookie для идентификации возвращающихся пользователей.

При включении RUM JavaScript устанавливает постоянный cookie `rxVisitor` в браузерах конечных пользователей, указывающий, что этот браузер ранее использовался для доступа к вашему приложению. При отключении RUM Classic больше не может связывать сессии с одним и тем же пользователем между перезапусками браузера. Узнайте подробнее о [хранении этого cookie](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.").

### Настройка срока действия cookie

По умолчанию cookie `rxVisitor` хранится в течение двух лет. Если применимые законы о конфиденциальности данных требуют более короткого срока действия постоянных cookie, используйте пользовательское свойство конфигурации для уменьшения срока действия cookie `rxVisitor`.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Custom configuration properties**.
5. Выберите **Add a custom configuration property** и введите пару ключ-значение `rvcl=<time-in-months>`, чтобы задать желаемый срок действия cookie. Максимальное значение — 24 месяца.

   Например, `rvcl=12` соответствует 12 месяцам.

## Режим opt-in

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** в настройках приложения.

По умолчанию отключено

Чтобы предоставить конечным пользователям возможность решать, отслеживать ли их действия, включите режим opt-in.

По умолчанию RUM автоматически создаёт [cookie](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage#dynatrace-rum-cookies "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB."). При включении **Data-collection and opt-in mode** ни OneAgent, ни RUM JavaScript не устанавливают cookie, и RUM JavaScript не собирает никаких данных. После того как конечный пользователь принял вашу политику использования cookie, можно активировать RUM для этого пользователя с помощью вызова JavaScript API [`dtrum.enable()`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enable). С помощью вызова API [`dtrum.disable()`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#disable) можно реализовать диалоговое окно, позволяющее конечным пользователям прекратить отправку данных мониторинга в Dynatrace даже после того, как они ранее дали согласие и `dtrum.enable()` уже был вызван.

## Do Not Track

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** в настройках приложения.

По умолчанию включено

Ещё одним методом защиты конфиденциальности конечных пользователей является функция «Do Not Track». При включении этой функции браузер добавляет HTTP-заголовок `DNT` ко всем исходящим веб-запросам. Этот заголовок указывает, что пользователь предпочитает не отслеживаться.

После включения **Comply with "Do Not Track" browser settings** можно выбрать один из двух вариантов:

* **Capture anonymous user sessions for "Do Not Track"-enabled browsers**: при обнаружении заголовка `DNT` Dynatrace фиксирует данные RUM, исключая всю персональную информацию, способную идентифицировать пользователя. IP-адрес маскируется, информация о [теге пользователя](/managed/observe/digital-experience/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.") не отправляется.

  При включённом параметре [**User tracking**](#user-tracking) Dynatrace по-прежнему устанавливает постоянный cookie для обнаружения возвращающихся пользователей.
* **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**: при обнаружении заголовка `DNT` Dynatrace не собирает данные из браузеров с включённым параметром «Do Not Track».

Если отключить **Comply with "Do Not Track" browser settings**, Dynatrace игнорирует настройку «Do Not Track» браузера и заголовок `DNT`.

Параметр **Comply with "Do Not Track" browser settings** — **Capture anonymous user sessions for "Do Not Track"-enabled browsers** включён по умолчанию для всех сред и приложений.

## Маскирование IP-адресов и GPS-координат

Чтобы получить доступ к этому параметру, выберите **General settings** > **Data privacy** > **General** > **IP masking** в настройках приложения.

Для определения региона, из которого конечные пользователи обращаются к веб- и мобильным интерфейсам, Dynatrace фиксирует их IP-адреса. GPS-координаты фиксируются только для мобильных интерфейсов.

При включении параметра **Mask end-user IP addresses and GPS coordinates** IP-адреса маскируются на [конечной точке маяка](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server."). Последний октет отслеживаемых IPv4-адресов и последние 80 бит IPv6-адресов заменяются нулями. [Геолокационный поиск](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#geolocations "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.") выполняется с использованием маскированных IP-адресов.

## Связанные темы

* [Настройка Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Configure monitoring consumption and data privacy settings for Session Replay.")