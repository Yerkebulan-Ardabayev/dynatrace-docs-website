---
title: Определение тегов на основе переменных окружения
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables
scraped: 2026-05-12T11:06:21.023107
---

# Определение тегов на основе переменных окружения

# Определение тегов на основе переменных окружения

* How-to guide
* 2-min read
* Updated on Aug 07, 2023

Dynatrace предоставляет возможность определять теги в виде переменных окружения для процессов и групп процессов.

## Рекомендация

Определение тегов непосредственно в окружении имеет свои применения. Однако это не рекомендуется как универсальное решение, поскольку является трудоёмким и требует тщательного планирования. Кроме того, это затрудняет внесение изменений в дальнейшем. Поэтому использовать данный подход следует осторожно.

Рекомендуется определять дополнительные метаданные на уровне развёрнутой системы. Как правило, следует думать о дополнительных и стандартных метаданных, а не о тегах (метках).

Используйте переменную окружения [`DT_CUSTOM_PROP`](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Настройте собственные метаданные, связанные с процессами.") для определения метаданных. Это позволяет использовать [правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Узнайте, как определять и применять теги вручную и автоматически.") на основе существующих или пользовательских метаданных для определения наборов фильтров для диаграмм, оповещений и других целей. Эти теги и правила можно изменять и адаптировать в любое время; они применяются практически мгновенно без каких-либо изменений в отслеживаемом окружении или приложениях.

## Определение тегов в виде переменных окружения

Переменную окружения `DT_TAGS` можно определить на уровне процесса или хоста. Формат переменной прост: она может содержать простые строки или пары «ключ/значение» (например, `DT_TAGS=MikesStuff easyTravel=Mike`). Как видно в примере для Windows ниже, можно определять несколько тегов. Для разделения значений тегов используются пробелы.

Для настройки группы процессов IIS необходимо определить переменную окружения, которую можно использовать в области действия правила. Чтобы настроить переменную окружения в IIS версии 10 и выше, см. документацию [Environment variables](https://www.iis.net/configreference/system.applicationhost/applicationpools/add/environmentvariables).

Настройка переменной окружения для IIS версий ниже 10

#### Настройка переменной окружения для IIS версий ниже 10

Чтобы настроить переменную окружения в IIS версий ниже 10, выполните следующие шаги.

1. Настройте **Advanced Settings** для пула приложений.

   ![Environment variable IIS](https://dt-cdn.net/images/env1-1578-6d669915ad.png)

   Переменная окружения IIS
2. Установите **Load User Profile** в значение **True**.

   ![Environment variable IIS](https://dt-cdn.net/images/env2-1563-c1584fc0f2.png)

   Переменная окружения IIS
3. Перезапустите IIS.  
   В командной строке с правами администратора введите `iisreset`.
4. Откройте реестр и перейдите в `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`

   ![Environment variable IIS](https://dt-cdn.net/images/env4-1571-60d8f6ab63.png)

   Переменная окружения IIS
5. Запустите приложение для инициализации AppPool (или установите **AppPool Start Mode** в значение **Always Running**), обновите `hivelist` и найдите новые записи.

   ![Environment variable IIS](https://dt-cdn.net/images/env5-1580-7e22193123.png)

   Переменная окружения IIS
6. В папке `C:\Users` найдите имя пользователя, от имени которого работает AppPool.

   ![Environment variable IIS](https://dt-cdn.net/images/env7-557-1acbf9ee8c.png)

   Переменная окружения IIS
7. В реестре перейдите к идентификатору пользователя в `HKEY_USERS` и добавьте **String Value** с именем `DT_CUSTOM_PROP`.

   ![Environment variable IIS](https://dt-cdn.net/images/env8-1590-c013dd318f.png)

   Переменная окружения IIS
8. Добавьте нужное значение, разделяя пары «ключ/значение» пробелами.

   ![Environment variable IIS](https://dt-cdn.net/images/env9-949-0ec6aad7a9.png)

   Переменная окружения IIS
9. Ещё раз перезапустите IIS и проверьте метаданные окружения в процессе Dynatrace.

   ![Environment variable IIS](https://dt-cdn.net/images/env10-1361-e92e945f44.png)

   Переменная окружения IIS

Настройка переменной окружения для Windows

Для настройки группировки процессов для служб Windows откройте **Редактор реестра** на локальном компьютере и создайте ключ **Environment** типа `REG_MULTI_SZ` в `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<servicename>`. Имя переменной должно начинаться со строки `DT_CUSTOM_PROP`, например `DT_CUSTOM_PROP=NAME_A=valueA`. Ключ может содержать несколько записей.

Пример:

![pg-vars](https://dt-cdn.net/images/2022-02-18-9-49-57-459-fb9fe355b4.png)

pg-vars

Применение [тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Узнайте, как определять и применять теги вручную и автоматически.") к хостам (вместо тщательной настройки переменных окружения, как описано здесь) не рекомендуется. То же относится к приложениям и процессам. Подробнее о настройке переменной окружения `DT_CUSTOM_PROP` для Tomcat или WebSphere, аннотациях Kubernetes для развёртываний на базе Kubernetes или тегировании AWS см. раздел [Метаданные приложений и тегирование](/managed/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging#application-metadata-and-tagging "Узнайте, когда рекомендуется использовать теги на основе метаданных, а также лучшие практики обогащения мониторинга Dynatrace дополнительными метаданными.").

![Env tagging 1](https://dt-cdn.net/images/env-tagging1-433-ef2e38dad8.png)

Env tagging 1

## Фильтрация объектов по переменным окружения

В интерфейсе Dynatrace приведённая выше пример переменной окружения отображается в виде новых фильтров на странице обзора связанного процесса (см. ниже). На страницах обзора групп процессов отображается сумма всех тегов всех процессов в группе.

![Env tagging 2](https://dt-cdn.net/images/env-tagging2-1414-289c172a71.png)

Env tagging 2

![Env tagging 3](https://dt-cdn.net/images/env-tagging3-1272-0d740c7cb8.png)

Env tagging 3

![Env tagging 4](https://dt-cdn.net/images/env-tagging4-1113-971391db79.png)

Env tagging 4

В настоящее время эта функция доступна только для процессов, глубоко отслеживаемых через OneAgent (Java, Apache Webserver, NGINX, .NET, Node.js, PHP, Go и IIS).