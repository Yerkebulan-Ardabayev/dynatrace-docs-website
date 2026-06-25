---
title: Настройка атрибутов RUM cookie
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes
scraped: 2026-05-12T11:34:14.311788
---

# Настройка атрибутов RUM cookie

# Настройка атрибутов RUM cookie

* How-to guide
* 4-min read
* Updated on Apr 22, 2026

Dynatrace Real User Monitoring использует набор HTTP-cookie; подробнее см. раздел [Cookies и клиентское хранилище для RUM и Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB."). Некоторые атрибуты cookie можно настраивать.

Чтобы получить доступ к этим параметрам:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Cookie**.

В следующих разделах описаны доступные параметры.

## Настройка атрибутов cookie, связанных с конфиденциальностью данных

Если политика безопасности вашей компании требует атрибутов cookie `Secure` и `SameSite`, необходимо настроить RUM для их установки, поскольку по умолчанию они не задаются.

Dynatrace RUM не поддерживает атрибут `HttpOnly`. Поскольку cookie с атрибутом `HttpOnly` недоступны для JavaScript, RUM JavaScript не может их читать или изменять. Убедитесь, что ваша инфраструктура не добавляет атрибут `HttpOnly`, так как это нарушит работу мониторинга.

### Установка атрибута Secure

Атрибут cookie `Secure` гарантирует, что браузеры отправляют cookie только по защищённым соединениям.

Перед включением атрибута cookie `Secure` убедитесь, что ваше приложение полностью работает через защищённые соединения. В противном случае вы потеряете видимость незашифрованных HTTP-соединений.

Чтобы задать атрибут cookie `Secure`, включите **Cookie** > **Use the Secure cookie attribute for cookies set by Dynatrace**.

### Установка атрибута SameSite

Атрибут cookie `SameSite` контролирует, отправляет ли браузер cookie с межсайтовыми запросами. Подробное описание этого атрибута и его значений см. в статье [SameSite cookies explained](https://web.dev/samesite-cookies-explained/).

Чтобы задать атрибут cookie `SameSite`, перейдите в **Cookie** > **SameSite cookie attribute** и выберите одно из значений: **None**, **Lax** или **Strict**.

## Настройка атрибута Domain

Атрибуты cookie `Domain` и `Path` определяют область действия cookie. Эта область определяет, отправляет ли браузер cookie с запросом и может ли клиентский JavaScript получить к нему доступ для заданного URL.

* Dynatrace всегда задаёт атрибут `Path` RUM-cookie равным `/`, поэтому область действия cookie распространяется на все URL-пути в рамках домена. Настройка атрибута `Path` недоступна.
* По умолчанию атрибут `Domain` определяется автоматически, однако его можно настроить вручную для каждого приложения.

В следующих разделах объясняется, как Dynatrace определяет домен cookie по умолчанию и когда может потребоваться его ручная настройка.

### Домен cookie по умолчанию

По умолчанию Dynatrace автоматически определяет домен cookie, выбирая [эффективный домен верхнего уровня плюс один (eTLD+1)](https://web.dev/same-site-same-origin/) URL запроса. Например, для `www.example.com` Dynatrace выбирает домен cookie `example.com`, а для `www.example.co.uk` — `example.co.uk`. Это позволяет Dynatrace регистрировать непрерывную сессию даже тогда, когда пользователи перемещаются между поддоменами при взаимодействии с вашими приложениями, например с `www.example.com` на `shop.example.com`.

Домен cookie определяется на стороне сервера (OneAgent) или на стороне клиента (RUM JavaScript).

* Если RUM JavaScript [инжектируется автоматически](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), домен cookie обычно определяет OneAgent, используя в качестве отправной точки результат определения имени хоста. Если неинструментированный компонент переписывает часть URL с именем хоста, убедитесь, что [определение имени хоста настроено правильно](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach.").
* При использовании [безагентного RUM](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") домен cookie определяет RUM JavaScript.

### Ручная настройка домена cookie

В большинстве случаев ручная настройка домена cookie не требуется. Однако она может быть полезна в следующих ситуациях:

* Необходимо разделить пользовательские действия разных поддоменов по отдельным пользовательским сессиям.
* Автоматическое определение домена cookie не работает, поскольку неинструментированный компонент переписывает часть URL с именем хоста и не передаёт исходную информацию о хосте в заголовке запроса. Предпочтительное решение — настроить компонент для добавления такого заголовка; см. раздел [Что делать, если неинструментированный компонент переписывает части URL?](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#rum-appdetection-uninstrumentedcomponent "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Ручная настройка домена cookie также может служить обходным решением.

Чтобы настроить домен cookie, перейдите в **Cookie** > **Domain to be used for cookie placement** и введите нужный домен.

Типичные ошибки и ограничения ручной настройки

##### Настроенный домен cookie является публичным суффиксом

Браузеры не позволяют устанавливать cookie с атрибутом `Domain`, выходящим за пределы одной организации. Поэтому задать домен cookie равным [публичному суффиксу](https://publicsuffix.org/list/) не удастся.

##### Несколько доменов без общего eTLD+1 сопоставлены с настроенным приложением

Поскольку домен cookie настраивается на уровне приложения, все домены, сопоставленные с вашим приложением, должны иметь хотя бы общий eTLD+1.

Например, нельзя вручную настроить домен cookie для приложения, с которым сопоставлены как `www.example.com`, так и `www.example.co.uk`. Если выбрать домен cookie `example.com`, браузер отклонит RUM-cookie для запросов к `www.example.co.uk`.

##### Вложенные домены cookie

Если вы вручную настраиваете домен cookie для всех или некоторых приложений, необходимо убедиться, что домены cookie ваших приложений не являются вложенными.

Рассмотрим следующий пример. Домен `www.example.com` сопоставлен с приложением **Example app**, а домен `shop.example.com` — с приложением **Shopping app**. По умолчанию для обоих приложений автоматически определяется домен cookie `example.com`. Если вручную задать домен cookie `shop.example.com` для приложения **Shopping app** и пользователи будут переходить между двумя приложениями, могут возникнуть неоднозначные ситуации. RUM-cookie для приложения **Example app** используют домен cookie `example.com` и поэтому применяются также к приложению **Shopping app**, у которого есть собственный набор RUM-cookie с доменом `shop.example.com`. При такой конфигурации Dynatrace может произвольно разбивать собранные RUM-данные на короткие пользовательские сессии, а пользовательские действия и распределённые трассировки могут не связываться должным образом.