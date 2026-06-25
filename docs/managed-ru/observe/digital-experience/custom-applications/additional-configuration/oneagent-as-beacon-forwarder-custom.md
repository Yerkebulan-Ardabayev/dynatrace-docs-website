---
title: Использование OneAgent в качестве конечной точки beacon для пользовательских приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom
scraped: 2026-05-12T11:34:04.731345
---

# Использование OneAgent в качестве конечной точки beacon для пользовательских приложений

# Использование OneAgent в качестве конечной точки beacon для пользовательских приложений

* How-to guide
* 1-min read
* Published Jan 30, 2023

OneAgent можно использовать в качестве альтернативной конечной точки beacon для плавного перехода на мобильный RUM Dynatrace.

Это особенно полезно в случаях, когда Cluster ActiveGate является внутренним и не может использовать публично доступный IP-адрес. В таких средах невозможно установить Dynatrace Managed, а следовательно, управлять доменом и создавать доверенный сертификат.

Инструментированный сервер с OneAgent должен работать на одной из следующих технологий:

* Apache HTTP Server
* IBM HTTP Server
* Oracle HTTP Server
* Веб-приложения на основе Java servlet (например, Tomcat и Wildfly)
* IIS
* NGINX
* Node.js

Чтобы использовать OneAgent в качестве конечной точки beacon для вашего приложения:

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **General** > **Beacon Endpoint**.
5. В раскрывающемся списке **Type** выберите **Instrumented web server**.
6. Введите URL веб-сервера или Java-сервера приложений (на основе servlet) в следующем формате:  
   `http(s)://<my-instrumented-server>:port/dtmb`
7. Нажмите **Save changes**.
8. В настройках приложения выберите **Instrumentation wizard** и выберите нужную операционную систему.
9. Соберите и протестируйте мобильное приложение для проверки изменений конфигурации.