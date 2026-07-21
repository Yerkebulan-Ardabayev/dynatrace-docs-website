---
title: Использование OneAgent в качестве конечной точки beacon для пользовательских приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/oneagent-as-beacon-forwarder-custom
---

# Использование OneAgent в качестве конечной точки beacon для пользовательских приложений в RUM Classic

# Использование OneAgent в качестве конечной точки beacon для пользовательских приложений в RUM Classic

* Практическое руководство
* Чтение за 1 мин
* Опубликовано 30 января 2023 г.

OneAgent можно использовать как альтернативную конечную точку beacon для плавного перехода на mobile RUM Dynatrace.

Это особенно полезно в случаях, когда Cluster ActiveGate доступен только внутри сети и не может использовать публично доступный IP-адрес. Dynatrace Managed в таких средах установить нельзя, поэтому он не может управлять доменом и создать доверенный сертификат.

Инструментированный сервер OneAgent должен быть настроен с использованием одной из следующих технологий:

* Apache HTTP Server
* IBM HTTP Server
* Oracle HTTP Server
* Веб-приложения на основе Java servlet (например, Tomcat и Wildfly)
* IIS
* NGINX
* Node.js

Чтобы использовать OneAgent в качестве конечной точки beacon для приложения

1. Перейти в **Frontend**.
2. Выбрать приложение, которое нужно настроить.
3. Выбрать **More** (**…**) > **Edit** в верхнем правом углу плитки с названием приложения.
4. В настройках приложения выбрать **General** > **Beacon Endpoint**.
5. В выпадающем списке **Type** выбрать **Instrumented web server**.
6. Ввести URL веб-сервера или сервера Java-приложений (на основе servlet) в следующем формате:  
   `http(s)://<my-instrumented-server>:port/dtmb`
7. Выбрать **Save changes**.
8. В настройках приложения выбрать **Instrumentation wizard** и выбрать нужную операционную систему.
9. Собрать и протестировать мобильное приложение, чтобы убедиться в корректности внесённых изменений в конфигурацию.