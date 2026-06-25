---
title: Поддерживаемые методы аутентификации в Synthetic Monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication
scraped: 2026-05-12T11:32:13.609593
---

# Поддерживаемые методы аутентификации в Synthetic Monitoring

# Поддерживаемые методы аутентификации в Synthetic Monitoring

* How-to guide
* 9-min read
* Updated on Mar 30, 2026

Dynatrace Synthetic Monitoring предлагает различные методы мониторинга веб-приложений или API-эндпоинтов, требующих аутентификации. Ниже приведён обзор наиболее распространённых сценариев и подходящих методов.

## Браузерные мониторы

Методы [**HTTP-аутентификации**](#http-bm) и [**аутентификации по сертификату**](#certificate-bm) поддерживаются как для [браузерных мониторов по одному URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как настроить браузерный монитор по одному URL для проверки доступности сайта."), так и для [браузерных clickpath-ов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.").

[**Веб-форма** (**HTML-based**)](#web-form-bm) поддерживается только для браузерных clickpath-ов.

### Аутентификация через веб-форму (HTML-based) для веб-приложений

Наиболее распространённый сценарий: страница с веб-формой (HTML-based) аутентификации, где нужно ввести имя пользователя и пароль.

![Web application with HTML-based authentication](https://dt-cdn.net/images/htmlbasedauthentication-2048-c9fcf36a82.png)

Web application with HTML-based authentication

Вы можете отслеживать транзакцию в [браузерном clickpath-е](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения."), записав учётные данные в веб-форме.

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Укажите имя монитора, начальный URL и другие параметры, затем нажмите **Record clickpath** внизу страницы.
3. Во время записи вручную введите имя пользователя и пароль для аутентификации; Dynatrace автоматически захватит учётные данные.
4. После записи можно сохранить учётные данные в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").
5. [Завершите настройку](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") вашего clickpath-а.

#### Мониторы по одному URL с аутентификацией через веб-форму

Устарело

Аутентификация через веб-форму больше не поддерживается для браузерных мониторов по одному URL. Вместо этого создайте [браузерный clickpath](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.") для сценариев, требующих веб-формы входа. Ранее настроенные мониторы по одному URL продолжат работу, однако рекомендуется перезаписать их как clickpath-ы, чтобы чётко разделить каждый шаг входа.

Перезапись обязательна, если вы хотите изменить любую часть настроек монитора. Сохранить изменения в текущем формате больше нельзя.

Начиная с Dynatrace версии 1.324+, мониторы по одному URL с формой входа будут автоматически обновлены путём добавления бесплатного шага JavaScript для поддержки процесса входа.

### Аутентификация Basic, Digest, NTLM или Negotiate (Kerberos) для веб-приложений

Если вам нужно отслеживать страницу с собственным диалогом браузера (не являющимся частью веб-приложения) для аутентификации, скорее всего, в фоне используются методы Basic, Digest, NTLM или Negotiate.

Authenticate (Kerberos) поддерживается для браузерных мониторов, выполняемых в [частных расположениях](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#kerberos-client-setup "Узнайте, как создать частное расположение для синтетического мониторинга."):

* Windows
* ActiveGate версии 1.311+ Linux
* ActiveGate версии 1.311+ [Containerized](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations#kerberos "Разворачивайте и управляйте контейнеризированными, автомасштабируемыми частными расположениями Synthetic на Kubernetes/RedHat OpenShift.")

![Native browser login dialog box](https://dt-cdn.net/images/nativebrowserlogindialogbox-1837-c1502c0fdf.png)

Native browser login dialog box

Мониторинг одной страницы

Транзакция в записанном clickpath-е

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. В разделе **Additional options** включите **Enable global login authentication**.
3. Выберите:

   * **HTTP authentication**, если вход осуществляется через собственный диалог браузера
   * **Kerberos authentication**, если вход осуществляется через протокол Kerberos. Заполните дополнительные обязательные поля:

     + Domain: доменное имя пользователя
     + Auth server allow list: список разрешённых серверов для Kerberos-аутентификации. Допускаются символы подстановки. Подробности в [документации Chrome Enterprise](https://dt-url.net/p803wkm)
4. Используйте существующие учётные данные из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") (**Select credentials**) или нажмите **Create new credentials**.
5. [Завершите настройку](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") браузерного монитора по одному URL.

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Укажите имя монитора, начальный URL и другие параметры, затем нажмите **Record clickpath** внизу страницы.
3. Во время записи вручную введите имя пользователя и пароль в собственном диалоге браузера.
4. После записи откройте первое [событие Navigate](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events#navigate "Узнайте о типах событий при записи браузерного clickpath-а.") вашего clickpath-а и включите **Enable HTTP authentication**.

   ![Navigate event HTTP authentication](https://dt-cdn.net/images/navigatehttpauthentication-652-d4048163be.png)

   Navigate event HTTP authentication
5. Используйте существующие учётные данные из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") (**Select credentials**) или нажмите **Create new credentials**.

   Ваш clickpath автоматически будет использовать эти учётные данные для аутентификации через собственный диалог входа браузера.
6. Для использования Kerberos-аутентификации выберите **Kerberos authentication**. Аутентификация выполняется путём получения Kerberos-билетов для указанных учётных данных от Kerberos Key Distribution Center.

   ![Kerberos Authentication](https://dt-cdn.net/images/kerberosauth-608-429fe9ac73.png)

   Kerberos Authentication

   * Domain: доменное имя пользователя
   * Auth server allow list: список разрешённых серверов для Kerberos-аутентификации. Допускаются символы подстановки. Подробности в [документации Chrome Enterprise](https://dt-url.net/p803wkm)
7. [Завершите настройку](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") браузерного clickpath-а.

Поддерживаемые форматы имени пользователя

* Браузерные мониторы: `<username>` и `<domain>\<username>`
* HTTP-мониторы: `<username>`
* **NTLM-аутентификация** в браузерных и HTTP-мониторах: `<username>`

### Аутентификация по клиентскому сертификату для веб-приложений

Аутентификация по сертификату доступна для браузерных мониторов, выполняемых из любого [публичного расположения](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.") и на Linux-based [частных расположениях](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга."). После настройки монитора необходимо указать данные клиентского сертификата на вкладке **Advanced setup** в настройках монитора в режиме редактирования.

Мониторинг одной страницы

Транзакция в записанном clickpath-е

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
2. Укажите URL и имя монитора.

   Указать клиентский сертификат при первоначальной настройке монитора по одному URL нельзя.
3. [Завершите настройку](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.") браузерного монитора по одному URL.

1. Перед записью clickpath-а на сайте, требующем аутентификации по сертификату, убедитесь, что нужный сертификат установлен в Chrome.
2. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create a browser monitor**.
3. Укажите имя монитора, начальный URL и другие параметры, затем нажмите **Record clickpath** внизу страницы.
4. При переходе на сайт в окне записи собственный диалог браузера выбирает правильный сертификат, установленный в Chrome. После записи clickpath-а необходимо указать сертификат для выполнения монитора, как описано ниже.

Далее в режиме редактирования добавьте клиентские сертификаты для выполнения браузерного монитора.

1. Откройте вкладку **Advanced setup** в настройках браузерного монитора.
2. Включите **Use client certificates**.
3. Нажмите **Add client certificate**.
4. Введите **Domain**, для которого действителен сертификат.
5. Выберите сертификат из списка сертификатных учётных данных. Или нажмите **Create new credential**, чтобы загрузить и использовать новый клиентский сертификат. Любой созданный сертификатный credential автоматически помечается как [только для владельца](/managed/manage/credential-vault#work-with-credentials "Храните и управляйте учётными данными в хранилище.") и сохраняется в [хранилище учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.").

   Можно загрузить файлы сертификатов в формате PFX, P12 или PEM.

   ![Certificate authentication setting for browser monitors](https://dt-cdn.net/images/bm-client-certificates-788-4347c846d7.png)

   Certificate authentication setting for browser monitors
6. Нажмите **Add entry**.
7. Повторите эти шаги для добавления нескольких сертификатов в clickpath. Каждый сертификат должен быть привязан к одному домену.
8. **Save changes**.

## HTTP-мониторы

HTTP-мониторы поддерживают аутентификацию Basic, NTLM, Kerberos token, OAuth 2.0 или по сертификату.

### Basic или NTLM аутентификация для эндпоинтов

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor**.
2. Нажмите **Add HTTP request** и выберите тип **HTTP request**.
3. В разделе **Additional options** запроса нажмите **Set authentication/authorization**.
4. Выберите **Basic authentication**, **Kerberos** или **NTLM**. При выборе **Kerberos** укажите также **Realm name** и **KDC IP**.
5. Используйте существующие учётные данные из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") (**Select credentials**) или нажмите **Create new credentials**.

   Dynatrace автоматически генерирует необходимый заголовок `Authorization` с указанными данными.

   Поддерживаемые форматы имени пользователя

   * Браузерные мониторы: `<username>` и `<domain>\<username>`
   * HTTP-мониторы: `<username>`
   * **NTLM-аутентификация** в браузерных и HTTP-мониторах: `<username>`
6. Завершите [настройку HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.").

### Bearer или токен-аутентификация для эндпоинтов

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor**.
2. Нажмите **Add HTTP request** и выберите тип **HTTP request**.
3. В разделе **Additional options** запроса нажмите **Set additional HTTP headers**.
4. Нажмите **Add header**.
5. Заполните заголовок, например:

   **Header name** = `Authorization`

   **Header value** = `Bearer <your-token>`

   или

   **Header name** = `Authorization`

   **Header value** = `Api-Token <your-token>`
6. Завершите [настройку HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.").

### Авторизация OAuth 2.0 для эндпоинтов

Авторизация OAuth 2.0 доступна для HTTP-мониторов и чаще всего используется при запросах к API-эндпоинтам. Dynatrace предоставляет тип запроса **OAuth2 authorization request** — специализированный шаблон HTTP-запроса для OAuth 2.0.

Сначала нужно настроить запрос OAuth 2.0 для получения токена доступа, который затем используется во всех последующих HTTP-запросах монитора к API-эндпоинту. Полученный токен не сохраняется в хранилище учётных данных, но легко доступен как вариант автодополнения в последующих запросах.

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor** и укажите **Name**.
2. Нажмите **Add HTTP request** и выберите тип **OAth2 authorization request**.
3. Введите URL для получения токена авторизации (**Access token URL**) и **Name** запроса.
4. Нажмите **Add HTTP request**, чтобы увидеть расширенные настройки. Обратите внимание: запрос OAuth 2.0 автоматически создаётся как `POST`.
5. Заполните или отредактируйте важные настройки в деталях запроса.

   1. В зависимости от настроек сервера аутентификации выберите **Add authorization data to** — **Request body** или **Request URL**. Заполните POST-параметры (`grant_Type`, `scope`, `client_id`, `username`, `password`) в **Request body** или **Request URL**. Параметры можно добавлять и изменять.

      ![OAuth parameters in request body](https://dt-cdn.net/images/oauthparamsbody1-1171-5bbbc6be5d.png)

      OAuth parameters in request body

      ![OAuth parameters in request URL](https://dt-cdn.net/images/oauthparamsurl-1314-353802a4b5.png)

      OAuth parameters in request URL
   2. Автоматически включается **post-execution script**, в котором:

      * Запрос завершается ошибкой, если возвращённый статус-код не равен `200`.
      * Метод `api.fail()` определяет **Failure message**, отображаемое при сбое в карточке **Events** на [странице деталей HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице деталей синтетических HTTP-мониторов.") и в [деталях выполнения](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Узнайте о странице деталей синтетических HTTP-мониторов.").
      * При успешном запросе тело ответа (JSON-строка) сохраняется в JavaScript-объекте (в данном примере `bearToken-2`).
      * Метод `api.info()` отправляет информацию в лог-файл, доступный в [частных расположениях Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.").

      Пользовательские лог-сообщения также отображаются в атрибуте `customLogs` в [деталях выполнения HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic#analyze-last-execution "Узнайте о странице деталей синтетических HTTP-мониторов.").

      ![Post-execution script](https://dt-cdn.net/images/oauthpostexecutionscript-812-911fe199bc.png)

      Post-execution script
   3. **Set token request authentication** позволяет указать дополнительные данные аутентификации (**Basic authentication**, **NTLM** или **Kerberos**) для сервера, за которым находится OAuth-приложение.

Для последующих HTTP-запросов

1. Создайте дополнительный HTTP-запрос для нужного эндпоинта (**Add HTTP request**).
2. В разделе **Additional options** второго запроса:

   * Включите **Set authentication/authorization** и выберите метод **OAuth2**. Обратите внимание: эта опция доступна только после создания запроса авторизации OAuth 2.0 (описано выше).

     Отображается автоматически сгенерированный **pre-execution script** с ссылкой на токен OAuth из запроса выше.

     ![OAuth method in HTTP request](https://dt-cdn.net/images/oauthtokeninsert1-1129-0244726c35.png)

     OAuth method in HTTP request
   * Как альтернатива: задайте HTTP-заголовок `Authorization`, указав JavaScript-объект с токеном OAuth в качестве **Header value**.

     ![OAuth method in HTTP request](https://dt-cdn.net/images/oauthtokeninsert2-1214-783de8da93.png)

     OAuth method in HTTP request
3. Завершите [настройку HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.").

### Аутентификация по клиентскому сертификату для эндпоинтов

1. Перейдите в **Synthetic Classic** > **Create a synthetic monitor** > **Create an HTTP monitor** и укажите **Name**.
2. Нажмите **Add HTTP request** и выберите тип **HTTP request**.
3. В разделе **Additional options** запроса нажмите **Add client certificate**.
4. Используйте существующий сертификат из [хранилища учётных данных](/managed/manage/credential-vault "Храните и управляйте учётными данными в хранилище.") (**Select credentials**) или нажмите **Create new credentials**.
5. Завершите [настройку HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.").

Для полной взаимной аутентификации отключите [**Accept any SSL certificate**](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic#ssl-accept "Узнайте о настройке HTTP-мониторов.") при использовании аутентификации по сертификату.