---
title: Связывание XHR-действий между разными источниками и их распределённых трассировок
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs
scraped: 2026-05-12T11:23:50.009958
---

# Связывание XHR-действий между разными источниками и их распределённых трассировок

# Связывание XHR-действий между разными источниками и их распределённых трассировок

* How-to guide
* 4-min read
* Updated on Oct 01, 2025

Если возникают проблемы со связыванием пользовательских действий с соответствующими трассировками, также обратитесь к разделу [Troubleshooting RUM correlation issues for web applications](https://dt-url.net/io63ls2).

Dynatrace связывает пользовательские действия и соответствующие им [распределённые трассировки](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") для обеспечения сквозной видимости. Например, это позволяет определять [топ-3 факторов веб-запросов](/managed/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#top-3-web-request-contributors "Understand how you can access user action detail pages and analyze user actions.") на странице сведений о пользовательском действии или детализировать из [графика анализа водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis#purepath-drilldown "Learn how to analyze all user action monitoring data through waterfall analysis.") в распределённые трассировки.

Связывание пользовательских действий и их распределённых трассировок работает автоматически при выполнении следующих условий:

* Веб-запрос является запросом того же источника: целевой URL веб-запроса и страница, с которой он был отправлен, имеют одинаковый протокол, хост и порт. В этом случае браузеры включают RUM cookies в веб-запрос, необходимые для корреляции пользовательских действий с распределёнными трассировками.
* Технология, используемая на первом инструментированном уровне (ближайшем к браузеру), указана в разделе [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). Для этих технологий OneAgent добавляет и анализирует RUM cookies.

Dynatrace не может автоматически связывать XHR-действия между разными источниками и их распределённые трассировки. Для включения такой корреляции используйте один из следующих подходов:

* [Включение cookie в запросы XHR между разными источниками](#include-cookies-in-cross-origin-xhr-calls-cookies-in-xhr-calls)
* [Использование заголовка `x-dtc`](#use-the-x-dtc-header-x-dtc-header)

## Включение cookie в запросы XHR между разными источниками

По умолчанию браузеры не включают cookie в запросы между разными источниками в соответствии с [политикой одного источника](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), ограничивающей взаимодействие страницы с ресурсами из другого источника. Для добавления RUM cookies и связывания XHR между разными источниками с их распределёнными трассировками можно использовать [CORS-запросы с учётными данными](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#requests_with_credentials).

Для этого подхода должны быть выполнены следующие предварительные условия:

* Технология первого инструментированного уровня указана в разделе [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Два задействованных домена имеют общий [effective top-level domain plus one (eTLD+1)](https://web.dev/same-site-same-origin/) для указания общего [домена cookie](/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes "Learn which RUM cookie attributes you can configure and how.").

Чтобы включить cookie в запросы XHR между разными источниками:

1. В JavaScript-коде установите [свойство `withCredentials`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) объекта XMLHttpRequest в `true`. При использовании Fetch установите [свойство `credentials`](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials) в `include`.
2. Настройте сервер, обрабатывающий веб-запрос, для ответа с заголовками `Access-Control-Allow-Credentials: true` и `Access-Control-Allow-Origin`, содержащим конкретный источник (не wildcard).
3. При [ручной настройке домена cookie](/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes#manual-cookie-domain-config "Learn which RUM cookie attributes you can configure and how.") убедитесь, что он охватывает оба задействованных домена. При использовании [автоматического определения домена cookie](/managed/observe/digital-experience/web-applications/additional-configuration/configure-cookie-attributes#default-cookie-domain "Learn which RUM cookie attributes you can configure and how.") (по умолчанию) определённый домен уже удовлетворяет этому требованию.

Если XHR-действие между разными источниками использует HTTP-метод, заголовок запроса или тип содержимого, требующий от браузера отправки [предварительного запроса](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), Dynatrace не может связать этот предварительный запрос, поскольку предварительные запросы не содержат cookie.

## Использование заголовка `x-dtc`

Для использования подхода на основе cookie задействованные домены должны допускать указание общего домена cookie. Подход на основе заголовка не имеет этого ограничения. Этот подход поддерживается для технологий, перечисленных в разделе [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), и [расширением OneAgent для AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.").

Заголовок `x-dtc` — пользовательский HTTP-заголовок, добавляемый RUM JavaScript и содержащий информацию, которая иначе передаётся через RUM cookies. Его добавление необходимо явно включить, поскольку конечные точки, обрабатывающие запросы между разными источниками, должны быть настроены для принятия этого заголовка.

Не включайте добавление заголовка `x-dtc`, не учитывая следующее:

* Добавление заголовка `x-dtc` для связывания XHR-действий между разными источниками и их распределённых трассировок является необязательным.
* Вы понимаете шаги, необходимые для подготовки конечных точек.
* Если конечные точки не настроены правильно до включения добавления заголовка, веб-приложение может сломаться.
* Dynatrace не несёт ответственности за любые неисправности приложения, вызванные неправильной настройкой.
* Следует всегда сначала включать добавление заголовка `x-dtc` в тестовой среде.

Чтобы связать XHR-действия между разными источниками и их распределённые трассировки с использованием заголовка `x-dtc`, настройте конечные точки для принятия `x-dtc`, а затем добавьте regex, соответствующий XHR-вызовам.

1. Настройте конечные точки, обрабатывающие запросы между разными источниками, для принятия заголовка `x-dtc`. Конечные точки должны обрабатывать [предварительные запросы](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), которые браузер отправляет из-за добавления заголовка. В частности, ответы на предварительные запросы должны содержать заголовок `Access-Control-Allow-Headers: x-dtc`. В противном случае XHR завершится ошибкой CORS.
2. В Dynatrace перейдите в **Web**.
3. Выберите приложение, которое нужно настроить.
4. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
5. В настройках приложения выберите **Capturing** > **Advanced setup**.
6. В разделе **Enable Real User Monitoring for cross-origin XHR calls** укажите регулярное выражение, соответствующее XHR-вызовам.

Если заголовок `x-dtc` не добавляется к запросу после выполнения приведённых инструкций, проверьте регулярное выражение и убедитесь, что [RUM настроен для захвата XHR-действий](/managed/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

Можно связать только фактический запрос, а не предварительный.