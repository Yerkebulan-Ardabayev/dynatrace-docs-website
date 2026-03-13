---
title: Link cross-origin XHR user actions and their distributed traces
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/initial-setup/link-cross-origin-xhrs
scraped: 2026-03-06T21:28:47.854342
---

# Связывание кросс-доменных XHR-действий пользователей и их распределённых трассировок

# Связывание кросс-доменных XHR-действий пользователей и их распределённых трассировок

* Classic
* How-to guide
* 4-min read
* Updated on Oct 01, 2025

Если у вас возникают проблемы со связыванием действий пользователей с соответствующими трассировками, также обратитесь к [Устранение проблем корреляции RUM для веб-приложений](https://dt-url.net/io63ls2).

Dynatrace связывает действия пользователей и их соответствующие [распределённые трассировки](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time."), обеспечивая непрерывную сквозную видимость. Например, это позволяет определить [топ-3 веб-запроса-контрибьютора](/docs/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions#top-3-web-request-contributors "Understand how you can access user action detail pages and analyze user actions.") на странице деталей действия пользователя или перейти из [каскадной диаграммы анализа](/docs/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis#purepath-drilldown "Learn how to analyze all user action monitoring data through waterfall analysis.") к распределённым трассировкам.

Связывание действий пользователей и их распределённых трассировок работает автоматически при выполнении следующих условий:

* Веб-запрос является запросом с одним источником (same-origin): целевой URL веб-запроса и страница, с которой запрос был отправлен, имеют одинаковый протокол, хост и порт. В этом случае браузеры включают RUM-cookies в веб-запрос, которые необходимы для корреляции действия пользователя с распределённой трассировкой.
* Технология, используемая на первом инструментированном уровне (ближайшем к браузеру), указана в [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."). Для этих технологий OneAgent добавляет и обрабатывает RUM-cookies.

Dynatrace не может автоматически связать кросс-доменные XHR-действия и их соответствующие распределённые трассировки. Чтобы включить такую корреляцию, воспользуйтесь одним из подходов:

* [Включение cookies в кросс-доменные XHR-вызовы](#include-cookies-in-cross-origin-xhr-calls-cookies-in-xhr-calls)
* [Использование заголовка `x-dtc`](#use-the-x-dtc-header-x-dtc-header)

## Включение cookies в кросс-доменные XHR-вызовы

По умолчанию браузеры не включают cookies в кросс-доменные запросы из-за [политики одного источника](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), которая ограничивает взаимодействие вашей страницы с ресурсами другого источника. Вы можете использовать [CORS-запросы с учётными данными](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS#requests_with_credentials), чтобы добавить RUM-cookies и таким образом связать кросс-доменные XHR и их распределённые трассировки.

Для этого подхода должны быть выполнены следующие предварительные условия:

* Технология, используемая на первом инструментированном уровне, указана в [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Два задействованных домена имеют как минимум общий [эффективный домен верхнего уровня плюс один (eTLD+1)](https://web.dev/same-site-same-origin/), что позволяет указать общий [домен cookie](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain "Learn when and how to configure the cookie domain.").

Чтобы включить cookies в кросс-доменные XHR-вызовы

1. В вашем JavaScript-коде установите свойство [`withCredentials`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) объекта XMLHttpRequest в значение `true`. Если вы используете Fetch, установите свойство [`credentials`](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials) в значение `include`.
2. Настройте сервер, обрабатывающий веб-запрос, чтобы он отвечал заголовком `Access-Control-Allow-Credentials: true` и заголовком `Access-Control-Allow-Origin`, содержащим конкретный источник (то есть не подстановочный знак).
3. Если вы [настраиваете домен cookie вручную](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#manual-cookie-domain-config "Learn when and how to configure the cookie domain."), убедитесь, что выбранный домен охватывает оба задействованных домена. Если используется [автоматическое определение домена cookie](/docs/observe/digital-experience/web-applications/additional-configuration/configure-the-cookie-domain#automatic-cookie-domain-determination "Learn when and how to configure the cookie domain.") (настройка по умолчанию), то определённый домен cookie уже соответствует этому требованию.

Если кросс-доменное XHR-действие использует HTTP-метод, заголовок запроса или тип содержимого, требующий от браузера отправки [предварительного запроса (preflight)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), Dynatrace не сможет связать этот предварительный запрос, поскольку предварительные запросы не содержат cookies.

## Использование заголовка `x-dtc`

Для использования описанного выше подхода на основе cookies задействованные домены должны позволять указание общего домена cookie. Подход на основе заголовка не имеет этого ограничения. Этот подход поддерживается для технологий, перечисленных в [Поддержка технологий - Real User Monitoring - Веб-серверы и приложения](/docs/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), а также [расширением OneAgent для AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension#lambda-cfg-rum "Monitor Lambda functions written in Python, Node.js, and Java.").

Заголовок `x-dtc` — это пользовательский HTTP-заголовок, добавляемый RUM JavaScript, содержащий информацию, которая в противном случае передаётся через RUM-cookies. Его добавление необходимо явно включить, поскольку конечные точки, обрабатывающие кросс-доменные запросы, должны быть настроены для приёма этого заголовка.

Не включайте добавление заголовка `x-dtc`, если вы не подтверждаете следующее:

* Добавление заголовка `x-dtc` для связывания кросс-доменных XHR-действий пользователей и их распределённых трассировок является необязательным.
* Вы понимаете шаги, необходимые для подготовки ваших конечных точек.
* Если вы не настроите конечные точки правильно перед включением добавления заголовка, ваше веб-приложение может перестать работать.
* Вы полностью принимаете, что Dynatrace не несёт ответственности за любые сбои приложения, вызванные неправильной конфигурацией.
* Вы всегда должны сначала включать добавление заголовка `x-dtc` в тестовой среде.

Чтобы связать кросс-доменные XHR-действия пользователей и их распределённые трассировки с помощью заголовка `x-dtc`, настройте конечные точки для приёма `x-dtc`, а затем добавьте регулярное выражение, соответствующее XHR-вызовам.

1. Настройте конечные точки, обрабатывающие кросс-доменные запросы, для приёма заголовка `x-dtc`. Конечные точки должны обрабатывать [предварительные запросы (preflight)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Preflighted_requests), которые браузер отправляет при добавлении заголовка. В частности, ответы на предварительные запросы должны содержать заголовок `Access-Control-Allow-Headers: x-dtc`. В противном случае XHR завершится с ошибкой CORS.
2. В Dynatrace перейдите в **Web**.
3. Выберите приложение, которое вы хотите настроить.
4. В правом верхнем углу страницы обзора приложения выберите **More** (**...**) > **Edit**.
5. В настройках приложения выберите **Capturing** > **Advanced setup**.
6. В разделе **Enable Real User Monitoring for cross-origin XHR calls** укажите регулярное выражение, соответствующее XHR-вызовам.

Если заголовок `x-dtc` не добавляется к запросу после выполнения приведённых выше инструкций, проверьте ваше регулярное выражение и убедитесь, что [RUM настроен для захвата XHR-действий](/docs/observe/digital-experience/web-applications/initial-setup/configure-dynatrace-real-user-monitoring-to-capture-xhr-actions "Understand why you need to activate specific JavaScript frameworks for XHR-action support and learn how to configure Real User Monitoring for XHR actions.").

Связать можно только фактический запрос, но не предварительный запрос (preflight).