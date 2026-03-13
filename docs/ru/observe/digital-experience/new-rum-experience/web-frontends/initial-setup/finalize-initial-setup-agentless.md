---
title: Finalize the initial setup for your agentless frontend
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-agentless
scraped: 2026-03-06T21:26:15.702725
---

# Завершение начальной настройки безагентного фронтенда

# Завершение начальной настройки безагентного фронтенда

* Latest Dynatrace
* Практическое руководство
* Обновлено 5 марта 2026 г.

После [настройки нового безагентного фронтенда](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring "Узнайте, как настроить безагентный RUM для ваших веб-фронтендов в New RUM Experience.") графики в [![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**](/docs/observe/digital-experience/new-rum-experience/experience-vitals "Приложение Experience Vitals предоставляет точку входа для мониторинга веб- и мобильных фронтендов.") должны начать отображать данные в течение десяти минут, если ваш фронтенд получает трафик. Если этого не произошло, вашей настройке могут потребоваться дополнительные шаги конфигурации. Это руководство проведёт вас через ряд проверок, которые помогут определить необходимую конфигурацию.

## Проверка успешной загрузки кода мониторинга

Если вы не выбрали формат фрагмента [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Узнайте, как выбрать формат JavaScript-фрагмента RUM, наиболее подходящий для вашего конкретного случая использования в New RUM Experience."), код мониторинга загружается как отдельный файл. В средах, где не настроен [пользовательский префикс имени файла кода мониторинга](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-monitoring-code-source#configure-custom-monitoring-code-filename-prefix "Настройте источник кода Real User Monitoring в New RUM Experience в соответствии с вашими конкретными требованиями."), имя файла начинается с префикса `ruxitagent_`.

Если инструменты разработчика браузера показывают ответ `200 OK` для этого запроса, загрузка прошла успешно, и вы можете перейти к [Проверке отправки RUM-маяков в Dynatrace](#beacons). В противном случае требуется дополнительная конфигурация.

![Успешная загрузка кода мониторинга RUM в безагентном фронтенде](https://dt-cdn.net/images/rum-monitoring-code-successful-download-agentless-1416-42fa2db754.png)

### Нарушения правил CSP

Если вы видите нарушения правил CSP в консоли браузера, связанные с загрузкой кода мониторинга, скорректируйте правила CSP, определённые в вашем приложении. Подробнее см. [Разрешение загрузки внешнего кода мониторинга](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules#allow-external-monitoring-code "Узнайте, как адаптировать правила CSP для New RUM Experience.").

### Запросы заблокированы компонентами инфраструктуры

Запросы кода мониторинга могут быть заблокированы компонентами инфраструктуры, такими как брандмауэры и прокси-серверы. Убедитесь, что ваша инфраструктура разрешает прохождение этих запросов; см. [Ограничения брандмауэра для RUM](/docs/observe/digital-experience/new-rum-experience/rum-firewall-latest "Узнайте, как обеспечить прохождение данных Real User Monitoring через ваш брандмауэр.").

## Проверка отправки RUM-маяков в Dynatrace

JavaScript RUM отправляет маяки (beacons) с захваченными данными на [конечную точку маяков](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/configure-beacon-endpoint "Узнайте, как настроить конечную точку маяков для веб-фронтендов в соответствии с вашими конкретными требованиями."). По умолчанию конечная точка маяков для безагентного фронтенда — это Cluster ActiveGate, являющийся частью инфраструктуры Dynatrace SaaS. Если New RUM Experience активирован, маяки в новом формате отправляются вместе с маяками RUM Classic на ту же конечную точку.

Чтобы идентифицировать RUM-маяки в инструментах разработчика браузера, ищите запросы с URL-путём `/bf` или `/bf/<id>`. Маяки в новом формате включают параметр строки запроса `pv=4`.

![RUM-маяки в новом формате, отправленные в инфраструктуру SaaS](https://dt-cdn.net/images/rum-beacon-new-format-agentless-1414-5c74d390ad.png)

### Маяки не отправляются

Если инструменты разработчика браузера не показывают маяки, проверьте следующие аспекты вашей настройки:

* Если вы включили [режим сбора данных и согласия](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/data-privacy-web#data-collection-and-opt-in-mode "Узнайте о доступных настройках, которые помогут обеспечить соответствие ваших веб-фронтендов требованиям конфиденциальности данных.") во время настройки, ваш код должен вызвать [`dtrum.enable()`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enable) из JavaScript API после того, как пользователь примет вашу политику конфиденциальности данных. Только после этого JavaScript RUM начнёт отправлять данные.
* Если вы выбрали формат фрагмента [inline code](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#inline-code "Узнайте, как выбрать формат JavaScript-фрагмента RUM, наиболее подходящий для вашего конкретного случая использования в New RUM Experience."), консоль вашего браузера может отображать нарушение правил CSP, указывающее, что встроенный скрипт был заблокирован. В этом случае скорректируйте правила CSP, как описано в [Разрешение выполнения встроенного кода](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules#allow-the-execution-of-inline-code "Узнайте, как адаптировать правила CSP для New RUM Experience.").

### Маяки заблокированы из-за нарушений правил CSP

Если вы видите нарушения правил CSP в консоли, указывающие, что соединение с конечной точкой маяков было заблокировано, скорректируйте правила CSP в вашем приложении. Подробнее см. [Разрешение отправки RUM-маяков](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/adapt-csp-rules#allow-sending-rum-beacons "Узнайте, как адаптировать правила CSP для New RUM Experience.").

### Источник маяков не в списке разрешённых

Если консоль браузера показывает ошибки CORS и запросы маяков возвращают ответ `403 Forbidden`, в вашей среде настроен список разрешённых источников маяков, который не разрешает маяки со страницы, которую вы инструментируете. Добавьте правило, разрешающее их, как описано в [Добавление правил в список разрешённых источников маяков](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/configure-beacon-origin-allowlist#add-rules "Укажите источники, с которых должны приниматься кросс-доменные RUM-маяки.").

### RUM отключён для браузеров с включённым «Do Not Track»

Если запросы маяков в новом формате возвращают код ответа `202 Accepted` и тело ответа JSON с полем `"errorReason":"Do Not Track"`, это означает, что в [настройках конфиденциальности данных](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/data-privacy-web#comply-with-dnt "Узнайте о доступных настройках, которые помогут обеспечить соответствие ваших веб-фронтендов требованиям конфиденциальности данных.") включена опция **Turn Real User Monitoring off for "Do Not Track"-enabled browsers**, и ваш браузер настроен на включение заголовка `DNT`. В этом случае маяки не пересылаются в Dynatrace конечной точкой маяков.

![RUM-маяк отклонён из-за Do Not Track](https://dt-cdn.net/images/rum-beacon-rejected-dnt-1120-d28b4cf9bd.png)

При проверке настройки настройте браузер так, чтобы он не включал заголовок `DNT`.

### Запросы заблокированы компонентами инфраструктуры

Запросы маяков могут быть заблокированы компонентами инфраструктуры, такими как брандмауэры и прокси-серверы. Вы можете определить, где был обработан запрос маяка, по телу ответа:

* Запросы маяков, завершившиеся ошибкой на конечной точке маяков, возвращают JSON-ответ, содержащий поля `status`, `handler`, `errorCode` и `errorReason`.
* Маяки, перехваченные брандмауэром или аналогичным компонентом, не включают этот JSON-ответ.

Второй сценарий можно предотвратить, обеспечив соответствие вашей инфраструктуры [ограничениям брандмауэра для RUM](/docs/observe/digital-experience/new-rum-experience/rum-firewall-latest "Узнайте, как обеспечить прохождение данных Real User Monitoring через ваш брандмауэр."). Исключением является код ошибки `429 Too Many Requests`, который также может быть возвращён инфраструктурой SaaS; в этом случае обратитесь в службу поддержки Dynatrace.

### Маяки в новом формате не отправляются

Если маяки отправляются, но вы не можете найти маяки в новом формате, New RUM Experience, возможно, не был активирован. См. [Включение New RUM Experience для ваших веб-приложений RUM Classic](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/enable-new-rum-for-web-apps "Узнайте, как активировать New RUM Experience для ваших веб-приложений RUM Classic."), чтобы узнать, как его активировать.
