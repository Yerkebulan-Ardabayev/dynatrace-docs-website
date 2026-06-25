---
title: Real User Monitoring для групп процессов
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups
scraped: 2026-05-12T11:34:47.856111
---

# Real User Monitoring для групп процессов

# Real User Monitoring для групп процессов

* How-to guide
* 2-min read
* Updated on Apr 01, 2026

По умолчанию RUM включён для всех групп процессов. Для технологий, перечисленных в разделе [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), это позволяет OneAgent выполнять следующее:

* Автоматически инжектировать RUM JavaScript в каждую страницу, обрабатываемую данной группой процессов
* Предоставлять необходимую информацию для связи пользовательских действий с [серверными распределёнными трассировками](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* Доставлять RUM JavaScript
* Пересылать маяки в Dynatrace Cluster

Можно отключить RUM для группы процессов. Например, это позволяет исключить серверы, которые не требуют мониторинга RUM. Кроме того, отключение RUM для группы процессов может использоваться как временное решение при устранении проблем с приложениями. Тем не менее рекомендуется обратиться к эксперту Dynatrace через чат для определения первопричины проблемы.

## Отключение RUM для группы процессов

При отключении RUM для группы процессов вся перечисленная выше функциональность RUM отключается.

Чтобы вручную отключить RUM для группы процессов:

1. Перейдите в **Technologies & Processes**.
2. Выберите плитку технологии, которая включает группу процессов, в которую инжектируется RUM JavaScript.
   Соответствующие группы процессов отображаются ниже на странице.
3. Прокрутите страницу вниз и выберите нужную группу процессов.
4. В правом верхнем углу страницы выберите **Settings**.
5. В настройках группы процессов выберите **Real User Monitoring**.
6. Отключите **Enable Real User Monitoring**.

## Важные замечания

* Если требуется вставлять RUM JavaScript вручную, не подавляйте инъекцию путём отключения Real User Monitoring для групп процессов. Это подавит не только инъекцию, но и связь пользовательских действий с распределёнными трассировками. Вместо этого используйте пользовательское правило инъекции, как описано в разделе [Configure automatic injection](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").
* Если требуется поэтапно развернуть RUM после установки OneAgent на хосты, рекомендуется использовать подход, описанный в разделе [Roll out RUM selectively for your applications](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts"). В принципе, настройка включения RUM на уровне группы процессов также допускает поэтапное развёртывание, однако это может быть сложным и чреватым ошибками.
* Если приложение состоит из нескольких уровней, включите RUM по крайней мере на том OneAgent, который инструментирует первый уровень (то есть уровень, ближайший к браузеру), — он захватывает корень распределённой трассировки.
  Например, рассмотрим сервер Apache HTTP в качестве прокси и Java-сервер приложений в качестве бэкенда. Даже если Dynatrace инжектирует RUM JavaScript в группу процессов Java-бэкенда, отключение RUM для группы процессов сервера Apache HTTP вызовет проблемы. В частности, станет невозможно связать пользовательские действия с распределёнными трассировками.