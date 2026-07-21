---
title: Связывание кросс-доменных пользовательских действий XHR и их распределённых трасс в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs
---

# Связывание кросс-доменных пользовательских действий XHR и их распределённых трасс в RUM Classic

# Связывание кросс-доменных пользовательских действий XHR и их распределённых трасс в RUM Classic

* Практическое руководство
* Чтение 4 мин
* Обновлено 01 октября 2025 г.

Если возникают проблемы со связыванием пользовательских действий с соответствующими трассами, см. также [Устранение проблем корреляции RUM для веб-приложений﻿](https://dt-url.net/io63ls2).

Dynatrace связывает пользовательские действия и соответствующие им [распределённые трассы](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time."), обеспечивая сквозную видимость без разрывов. Например, это позволяет определить [3 главных источника веб-запросов](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/analyze-individual-user-actions#top-3-web-request-contributors "Understand how you can access user action detail pages and analyze user actions.") на странице сведений о пользовательском действии или перейти от [диаграммы каскадного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis#purepath-drilldown "Learn how to analyze all user action monitoring data through waterfall analysis.") к распределённым трассам.

Связывание пользовательских действий и их распределённых трасс работает без дополнительной настройки при выполнении следующих условий:

* Веб-запрос является запросом того же источника: целевой URL веб-запроса и страница, с которой был отправлен запрос, имеют одинаковый протокол, хост и порт. В этом случае браузеры включают в веб-запрос RUM-cookie, которые необходимы для корреляции пользовательского действия с распределённой трассой.
* Технология, используемая на первом инструментированном уровне (уровне, ближайшем к браузеру), указана в разделе [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). Для этих технологий OneAgent добавляет и оценивает RUM-cookie.

Dynatrace не может автоматически связать кросс-доменные действия XHR с соответствующими распределёнными трассами. Чтобы включить такую корреляцию, нужно воспользоваться одним из подходов:

* [Включение cookie в кросс-доменные вызовы XHR](#include-cookies-in-cross-origin-xhr-calls-cookies-in-xhr-calls)
* [Использование заголовка `x-dtc`](#use-the-x-dtc-header-x-dtc-header)

## Включение cookie в кросс-доменные вызовы XHR

По умолчанию браузеры не включают cookie в кросс-доменные запросы из-за [политики единого источника﻿](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), которая ограничивает взаимодействие страницы с ресурсами другого источника. Можно использовать [CORS-запросы с учётными данными﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#requests_with_credentials), чтобы добавить RUM-cookie и таким образом связать кросс-доменные XHR с их распределёнными трассами.

Для этого подхода должны выполняться следующие предварительные условия:

* Технология, используемая на первом инструментированном уровне, указана в разделе [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Два задействованных домена имеют как минимум общий [эффективный домен верхнего уровня плюс один (eTLD+1)﻿](https://web.dev/same-site-same-origin/), что позволяет указать общий [домен cookie](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes "Learn which RUM cookie attributes you can configure and how.").

Чтобы включить cookie в кросс-доменные вызовы XHR

1. В коде JavaScript установите значение `true` для [свойства `withCredentials`﻿](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) объекта XMLHttpRequest. Если используется Fetch, установите для [свойства `credentials`﻿](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials) значение `include`.
2. Настройте сервер, обрабатывающий веб-запрос, так, чтобы он отвечал заголовком `Access-Control-Allow-Credentials: true` и заголовком `Access-Control-Allow-Origin`, содержащим конкретный источник (то есть не подстановочный знак).
3. При [настройке домена cookie вручную](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#manual-cookie-domain-config "Learn which RUM cookie attributes you can configure and how.") нужно выбрать домен, который охватывает оба задействованных домена. Если используется [автоматическое определение домена cookie](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#default-cookie-domain "Learn which RUM cookie attributes you can configure and how."), а это вариант по умолчанию, то определённый домен cookie уже удовлетворяет этому требованию.

Если кросс-доменное действие XHR использует HTTP-метод, заголовок запроса или тип содержимого, требующие от браузера отправки [предварительного запроса﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), Dynatrace не может связать этот предварительный запрос, поскольку предварительные запросы не содержат cookie.

## Использование заголовка `x-dtc`

Чтобы следовать описанному выше подходу на основе cookie, задействованные домены должны допускать указание общего домена cookie. Подход на основе заголовка этого ограничения не имеет. Он поддерживается для технологий, перечисленных в разделе [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), а также [расширением OneAgent для AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.").

Заголовок `x-dtc`, это пользовательский HTTP-заголовок, добавляемый JavaScript RUM, содержащий информацию, которая иначе передаётся через RUM-cookie. Его добавление нужно включать явно, поскольку конечные точки, обрабатывающие кросс-доменные запросы, должны быть настроены на приём этого заголовка.

Не включайте добавление заголовка `x-dtc`, пока не примете во внимание следующее:

* Добавление заголовка `x-dtc` для связывания кросс-доменных пользовательских действий XHR с их распределёнными трассами необязательно.
* Нужно понимать шаги, необходимые для подготовки конечных точек.
* Если конечные точки не настроены правильно до включения добавления заголовка, веб-приложение может перестать работать.
* Нужно полностью принять, что Dynatrace не несёт ответственности за какие-либо сбои приложения, вызванные неправильной настройкой.
* Добавление заголовка `x-dtc` всегда следует сначала включать в тестовой среде.

Чтобы связать кросс-доменные пользовательские действия XHR с их распределёнными трассами с помощью заголовка `x-dtc`, настройте конечные точки на приём `x-dtc`, а затем добавьте регулярное выражение, соответствующее вызовам XHR.

1. Настройте конечные точки, обрабатывающие кросс-доменные запросы, на приём заголовка `x-dtc`. Конечные точки должны обрабатывать [предварительные запросы﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), которые браузер отправляет из-за добавления заголовка. В частности, ответы на предварительные запросы должны содержать заголовок `Access-Control-Allow-Headers: x-dtc`. В противном случае XHR завершится ошибкой CORS.
2. В Dynatrace перейдите в **Web**.
3. Выберите приложение, которое нужно настроить.
4. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
5. В настройках приложения выберите **Capturing** > **Advanced setup**.
6. В разделе **Enable Real User Monitoring for cross-origin XHR calls** укажите регулярное выражение, соответствующее вызовам XHR.

Если после выполнения указанных выше действий заголовок `x-dtc` не добавляется к запросу, проверьте регулярное выражение и убедитесь, что [RUM настроен на захват действий XHR](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring Classic for XHR actions.").

Связать можно только фактический запрос, но не предварительный запрос.