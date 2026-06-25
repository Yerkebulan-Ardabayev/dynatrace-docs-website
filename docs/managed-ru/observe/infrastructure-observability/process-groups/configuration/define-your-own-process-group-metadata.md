---
title: Определение пользовательских метаданных группы процессов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata
scraped: 2026-05-12T11:11:32.984894
---

# Define your own process group metadata

# Определение пользовательских метаданных группы процессов

* How-to guide
* 1-min read
* Updated on Aug 07, 2023

Dynatrace автоматически обнаруживает и отображает многочисленные значения метаданных, связанные с процессами в вашей среде, — в том числе номера версий, номера портов и имя скрипта или JAR-файла, запускающего каждый процесс (см. рисунки ниже).

![Metadata 1](https://dt-cdn.net/images/metadata1-1068-2deabeeefb.png)

Metadata 1

![Metadata 2](https://dt-cdn.net/images/metadata2-1074-353ed0c77a.png)

Metadata 2

Dynatrace позволяет использовать эти значения метаданных для [автоматической расстановки тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically."), а также для [передачи тегов через переменные среды](/managed/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables."). Dynatrace также позволяет определять собственные метаданные в соответствии с уникальными потребностями организации или среды.

## Определение метаданных через переменные среды

Переменную среды `DT_CUSTOM_PROP` можно определить на уровне процесса или хоста. Формат переменной прост: он представляет собой пары «ключ/значение», например `DT_CUSTOM_PROP=Department=Acceptance Stage=Sprint`. Обратите внимание, что переменные среды должны быть видимы [соответствующему процессу при запуске приложения](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection#env "Ways to customize process-group detection").

После настройки значения метаданных отображаются на соответствующих страницах Process и Process group (см. пример ниже).

![Metadata 3](https://dt-cdn.net/images/metadata3-1075-fb5fb788ad.png)

Metadata 3

Определение переменной среды для IIS

#### Настройка переменной среды для IIS версий ниже 10

Для настройки переменной среды в IIS версий ниже 10 выполните следующие действия.

1. Настройте **Advanced Settings** для Application Pool.

   ![Environment variable IIS](https://dt-cdn.net/images/env1-1578-6d669915ad.png)

   Environment variable IIS
2. Установите **Load User Profile** в значение **True**.

   ![Environment variable IIS](https://dt-cdn.net/images/env2-1563-c1584fc0f2.png)

   Environment variable IIS
3. Перезапустите IIS.  
   В командной строке с правами администратора введите `iisreset`.
4. Откройте Registry и перейдите в `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\hivelist`.

   ![Environment variable IIS](https://dt-cdn.net/images/env4-1571-60d8f6ab63.png)

   Environment variable IIS
5. Запустите приложение для инициализации AppPool (или установите **AppPool Start Mode** в значение **Always Running**), обновите `hivelist` и найдите новые записи.

   ![Environment variable IIS](https://dt-cdn.net/images/env5-1580-7e22193123.png)

   Environment variable IIS
6. Проверьте `C:\Users` на наличие имени пользователя, от имени которого работает AppPool.

   ![Environment variable IIS](https://dt-cdn.net/images/env7-557-1acbf9ee8c.png)

   Environment variable IIS
7. В реестре перейдите к идентификатору пользователя в разделе `HKEY_USERS` и добавьте строковое значение **String Value** с именем `DT_CUSTOM_PROP`.

   ![Environment variable IIS](https://dt-cdn.net/images/env8-1590-c013dd318f.png)

   Environment variable IIS
8. Добавьте нужное значение с пробелами между парами «ключ/значение».

   ![Environment variable IIS](https://dt-cdn.net/images/env9-949-0ec6aad7a9.png)

   Environment variable IIS
9. Снова перезапустите IIS и проверьте метаданные среды в процессах Dynatrace.

   ![Environment variable IIS](https://dt-cdn.net/images/env10-1361-e92e945f44.png)

   Environment variable IIS

Определение переменной среды для Windows

Для настройки группировки процессов для служб Windows откройте **Registry Editor** на локальном компьютере и создайте ключ **Environment** типа `REG_MULTI_SZ` в разделе `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<servicename>`. Имя переменной должно начинаться со строки `DT_CUSTOM_PROP`, например `DT_CUSTOM_PROP=NAME_A=valueA`. Ключ может содержать несколько записей.

Пример:

![pg-vars](https://dt-cdn.net/images/2022-02-18-9-49-57-459-fb9fe355b4.png)

pg-vars

## Использование аннотаций в Kubernetes

Dynatrace поддерживает автоматическую расстановку тегов в Kubernetes на основе [меток Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). Аналогичным образом можно использовать [аннотации Kubernetes](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/) — они также будут отображаться на страницах Process и Process group (см. ниже).

![Environment variables 4](https://dt-cdn.net/images/environmentvariables-4-1099-4cd32148af.png)

Environment variables 4

## Связанные темы

* [Ownership](/managed/deliver/ownership "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.")