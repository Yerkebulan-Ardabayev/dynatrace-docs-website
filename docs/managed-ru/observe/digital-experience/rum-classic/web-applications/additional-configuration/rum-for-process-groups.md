---
title: Real User Monitoring Classic для групп процессов
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-for-process-groups
---

# Real User Monitoring Classic для групп процессов

# Real User Monitoring Classic для групп процессов

* Практическое руководство
* Чтение за 2 мин.
* Обновлено 01 апр. 2026 г.

По умолчанию RUM включён для всех групп процессов. Для технологий, перечисленных в разделе [Поддержка технологий Real User Monitoring: веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), это позволяет OneAgent делать следующее:

* Автоматически внедрять RUM JavaScript в каждую страницу, доставляемую данной группой процессов
* Предоставлять информацию, необходимую для связывания действий пользователей с [распределёнными трассировками на стороне сервера](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* Доставлять RUM JavaScript
* Пересылать бикны в кластер Dynatrace

Можно отключить RUM для группы процессов. Например, это можно сделать, чтобы исключить серверы, не требующие мониторинга RUM. Кроме того, отключение RUM для группы процессов может служить обходным решением при устранении проблем с приложениями. Однако рекомендуется обратиться к эксперту по продуктам Dynatrace через чат, чтобы он помог определить первопричину проблемы.

## Отключение RUM для группы процессов

При отключении RUM для группы процессов вся перечисленная выше функциональность RUM отключается полностью.

Чтобы вручную отключить RUM для группы процессов

1. Перейти в раздел **Technologies & Processes**.
2. Выбрать плитку технологии, включающую группу процессов, в которую нужно внедрить RUM JavaScript.
   Соответствующие группы процессов отображаются далее на странице.
3. Прокрутить вниз и выбрать нужную группу процессов.
4. Выбрать **Settings** в верхнем правом углу страницы.
5. В настройках группы процессов выбрать **Real User Monitoring**.
6. Отключить **Enable Real User Monitoring**.

## Важные замечания

* Если предпочтительно вставлять RUM JavaScript вручную, не следует подавлять внедрение, отключая Real User Monitoring для групп процессов. Это подавляет не только внедрение, но и связывание действий пользователей с распределёнными трассировками. Вместо этого нужно использовать пользовательское правило внедрения, как описано в разделе [Настройка автоматического внедрения в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").
* Если требуется развернуть RUM выборочно после развёртывания OneAgent на хостах, рекомендуется использовать подход, описанный в разделе [Выборочное развёртывание RUM Classic для приложений](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts"). В принципе, настройка включения RUM на уровне группы процессов также допускает выборочное развёртывание, но такой подход обычно сложен и подвержен ошибкам.
* Если приложение состоит из нескольких уровней, нужно включить RUM как минимум на OneAgent, инструментирующем первый уровень (то есть уровень, ближайший к браузеру), который фиксирует корень распределённой трассировки.  
  Например, рассмотрим Apache HTTP server в роли прокси и Java app server в роли бэкенда. Даже несмотря на то, что Dynatrace внедряет RUM JavaScript в группу процессов Java-бэкенда, отключение RUM для группы процессов Apache HTTP server приведёт к проблемам. В частности, станет невозможно связывать действия пользователей с распределёнными трассировками.