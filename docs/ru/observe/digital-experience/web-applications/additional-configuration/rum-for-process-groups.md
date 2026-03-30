---
title: Real User Monitoring для групп процессов
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups
scraped: 2026-03-05T21:33:02.016377
---

* How-to guide
* 2-min read

По умолчанию RUM включён для всех групп процессов. Для технологий, перечисленных в разделе [Technology support - Real User Monitoring - Web servers and applications](../../../../ingest-from/technology-support.md#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), это позволяет OneAgent выполнять следующее:

* Автоматически внедрять RUM JavaScript в каждую страницу, доставляемую данной группой процессов
* Предоставлять необходимую информацию для связи пользовательских действий с серверными распределёнными трассировками
* Доставлять RUM JavaScript
* Пересылать маяки в кластер Dynatrace

Вы можете отключить RUM для группы процессов. Например, это можно сделать для исключения серверов, которым не требуется мониторинг RUM. Кроме того, отключение RUM для группы процессов может служить временным решением для устранения проблем с вашими приложениями. Тем не менее мы рекомендуем обратиться к специалисту по продуктам Dynatrace через онлайн-чат, чтобы определить первопричину проблемы.

## Отключение RUM для группы процессов

Если вы отключаете RUM для группы процессов, весь перечисленный выше функционал RUM отключается.

Чтобы вручную отключить RUM для группы процессов

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Выберите плитку технологии, включающую группу процессов, в которую должен внедряться RUM JavaScript.
   Соответствующие группы процессов отображаются ниже на странице.
3. Прокрутите вниз и выберите нужную группу процессов.
4. Нажмите **Settings** в правом верхнем углу страницы.
5. В настройках группы процессов выберите **Real User Monitoring**.
6. Отключите **Enable Real User Monitoring**.

## Возможные проблемы

* Если вы предпочитаете вставлять RUM JavaScript вручную, не подавляйте внедрение, отключая Real User Monitoring для своих групп процессов. Это подавляет не только внедрение, но и связь пользовательских действий с распределёнными трассировками. Вместо этого используйте пользовательское правило внедрения, как описано в разделе [Configure automatic injection](../initial-setup/rum-injection.md#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").
* Если ваше приложение состоит из нескольких уровней, включите RUM как минимум на том OneAgent, который инструментирует первый уровень (то есть уровень, ближайший к браузеру), который фиксирует корень распределённой трассировки.
  Например, рассмотрим Apache HTTP server в качестве прокси и сервер приложений Java в качестве бэкенда. Несмотря на то что Dynatrace внедряет RUM JavaScript в группу процессов бэкенда Java, отключение RUM для группы процессов Apache HTTP server вызовет проблемы. В частности, будет невозможно связать пользовательские действия и распределённые трассировки.
