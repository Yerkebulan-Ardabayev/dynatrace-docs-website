---
title: Исключение IP-адресов, браузеров, ботов и поисковых роботов из мониторинга для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring
scraped: 2026-05-12T11:34:28.111568
---

# Исключение IP-адресов, браузеров, ботов и поисковых роботов из мониторинга для веб-приложений

# Исключение IP-адресов, браузеров, ботов и поисковых роботов из мониторинга для веб-приложений

* How-to guide
* 2-min read
* Updated on Mar 21, 2024

Dynatrace позволяет исключать определённые IP-адреса, типы браузеров, ботов и поисковых роботов из Real User Monitoring.

Трафик, создаваемый [синтетическими мониторами Dynatrace](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types."), нельзя заблокировать с помощью описанных ниже настроек. В частности, исключение IP-адресов Synthetic-локаций, а также исключение ботов и поисковых роботов не заблокирует трафик Synthetic Monitoring.

Вручную назначенные приложения можно отвязать от синтетических мониторов, однако автоматически назначенные приложения — нельзя.

Чтобы исключить данные Synthetic из анализа, используйте фильтр **User type: Real users**, доступный на большинстве страниц сведений о приложениях, в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), при [сегментации сессий](/managed/observe/digital-experience/session-segmentation/new-user-sessions "Learn about user session segmentation and filtering attributes."), в [USQL](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") и в других местах.

## Исключение IP-адресов

В настройках приложения можно исключить отдельный IP-адрес или диапазон IP-адресов.

Чтобы исключить IP-адрес:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Exclusions** > **IP address exclusions**.
5. Выберите **Add an IP address to exclude**.
6. Укажите IP-адреса, которые нужно исключить из Real User Monitoring.

## Исключение браузеров

Если необходимо исключить определённые устаревшие типы браузеров из списка отслеживаемых, создайте правила исключения браузеров.

Чтобы создать правило исключения браузера:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Exclusions** > **Browser exclusions**.
5. Выберите **Add a browser exclusion rule**.
6. В раскрывающемся списке **Browser** выберите браузер, который нужно исключить, и укажите точную версию и тип.

## Исключение трафика ботов и поисковых роботов

Отслеживаемое приложение может сталкиваться с трафиком, создаваемым автоматическими ботами или поисковыми роботами. Этот трафик может инициировать оповещения **Unexpected low traffic**, затрудняющие обнаружение актуальных проблем. Ботов и поисковых роботов можно исключить из RUM.

Чтобы исключить ботов и поисковых роботов из RUM:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Capturing** > **Exclusions** > **Browser exclusions**.
5. Выберите **Add a browser exclusion rule**.
6. В раскрывающемся списке **Browser** выберите **Bots & Spiders**.

Внесённые изменения применяются ко всем экземплярам OneAgent в течение нескольких минут.

В отличие от [классификации пользователей, которую Dynatrace добавляет к захваченным данным RUM](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents#browsers "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems."), эта функция не использует поиск в базе данных, поскольку применяется OneAgent. Вместо этого [строка пользовательского агента](https://developer.mozilla.org/docs/Web/HTTP/Headers/User-Agent) сравнивается с набором шаблонов, что менее точно по сравнению с поиском в базе данных. По этой причине некоторый трафик от ботов и поисковых роботов может всё равно фиксироваться.