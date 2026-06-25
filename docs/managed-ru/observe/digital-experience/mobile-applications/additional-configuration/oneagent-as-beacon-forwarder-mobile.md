---
title: Использование OneAgent в качестве beacon-эндпоинта для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/oneagent-as-beacon-forwarder-mobile
scraped: 2026-05-12T11:32:38.750632
---

# Использование OneAgent в качестве beacon-эндпоинта для мобильных приложений

# Использование OneAgent в качестве beacon-эндпоинта для мобильных приложений

* How-to guide
* 1-min read
* Published Jan 21, 2020

OneAgent можно использовать в качестве альтернативного beacon-эндпоинта для обеспечения плавного перехода на мобильный RUM Dynatrace.

Это особенно полезно в случаях, когда ваш Cluster ActiveGate является внутренним и не может использовать общедоступный IP-адрес. Dynatrace Managed нельзя устанавливать в таких средах, а значит, нельзя управлять доменом и создавать доверенный сертификат.

Инструментированный сервер OneAgent должен быть настроен с одной из следующих технологий:

* Apache HTTP Server
* IBM HTTP Server
* Oracle HTTP Server
* Веб-приложения на основе сервлетов Java (например, Tomcat и Wildfly)
* IIS
* NGINX
* Node.js

Чтобы использовать OneAgent в качестве beacon-эндпоинта для вашего приложения:

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **General** > **Beacon Endpoint**.
5. В раскрывающемся списке **Type** выберите **Instrumented web server**.
6. Введите URL веб-сервера или сервера приложений Java (на основе сервлетов) в следующем формате:  
   `http(s)://<my-instrumented-server>:port/dtmb`
7. Нажмите **Save changes**.
8. В настройках приложения выберите **Instrumentation wizard** и выберите нужную операционную систему.
9. Соберите и протестируйте мобильное приложение для проверки изменения конфигурации.