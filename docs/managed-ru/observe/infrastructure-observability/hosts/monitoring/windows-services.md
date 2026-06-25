---
title: Классический мониторинг служб Windows
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/monitoring/windows-services
scraped: 2026-05-12T12:11:58.138818
---

# Classic Windows services monitoring

# Классический мониторинг служб Windows

* How-to guide
* 6-min read
* Published Jul 10, 2020

Устарело

Функция классического мониторинга служб Windows, описанная ниже, устарела. Вместо неё рекомендуется использовать [OS services monitoring](/managed/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.").

Dynatrace предоставляет готовый мониторинг доступности служб Windows.

Для мониторинга доступности службы укажите `Service name` и `Display name`. Для упрощения управления в крупных средах настройте параметры на уровне группы хостов.

Изменения в мониторинге служб ОС

В Dynatrace версий 1.214–1.218 конфигурация мониторинга доступности служб Windows на уровне хоста имела приоритет над конфигурацией группы хостов, которая, в свою очередь, имела приоритет над конфигурацией среды. В Dynatrace version 219+ это поведение изменено. Конфигурации на уровнях среды, группы хостов и хоста объединяются, как описано ниже.

Мониторинг служб можно настраивать на уровнях среды, группы хостов и хоста. Мониторинг служб представляет собой совокупность настроек, заданных на любом из трёх уровней.

Пример

Предположим, что у вас есть:

* Службы A, B, C, D и E
* Группы хостов J и K
* Хосты X и Y
* Хост X является членом группы хостов J
* Хост Y не входит ни в одну группу хостов

Если настроено следующее:

* Мониторинг служб A и B на уровне среды
* Мониторинг служб B и C для группы хостов J
* Мониторинг служб A и D для хоста X
* Мониторинг служб A и E для хоста Y

То будет выполняться следующий мониторинг:

* Службы A и B — на всех хостах
* Службы A, B и C — на всех хостах группы J
* Службы A, B, C и D — на хосте X
* Службы A, B и E — на хосте Y

## Мониторинг службы

Чтобы настроить мониторинг службы ОС:

1. Определите имя службы. Необходимо использовать точное имя службы, предоставленное ОС, поскольку именно по нему Dynatrace идентифицирует вашу службу.

   Определение имени службы Windows

   1. В Windows откройте **Services** и найдите нужную службу.
   2. Проверьте свойства службы. В данном примере отображаются свойства Windows License Manager Service, откуда видно, что имя службы Windows — `LicenseManager`.

      ![Windows services availability: example service name](https://dt-cdn.net/images/windowsservicenameexample-1212-546952d557.png)

      Windows services availability: example service name
2. В Dynatrace перейдите в **OS service monitoring** для нужного уровня настройки.

   Уровень хоста

   1. Перейдите в **Hosts**.
   2. Необязательно: отфильтруйте по `Operating system` (Windows).
   3. Найдите хост и выберите его для отображения страницы хоста.
   4. На странице хоста откройте меню просмотра (**…**) и выберите **Settings**.
   5. Выберите вкладку **OS service monitoring**.

   Уровень группы хостов

   1. Перейдите в **Hosts**.
   2. Необязательно: отфильтруйте по `Operating system` (Windows).
   3. Отфильтруйте по `Host group` и начните вводить имя группы хостов для её поиска и выбора.
   4. Откройте любой хост из данной группы.
   5. На странице хоста раскройте раздел **Properties and tags** и выберите имя группы хостов.
   6. Выберите вкладку **OS service monitoring**.

   Уровень среды

   Перейдите в **Settings** > **Monitoring** > **OS services monitoring**.
3. На странице **OS service monitoring** для нужного уровня выберите **Add new service** и укажите службу для мониторинга.

   * **Service name** — точное имя службы, определённое на шаге 1.
   * **Display name** — произвольная метка, которая будет отображаться в таблице отслеживаемых служб.
4. Выберите **Save changes**.

## Управление отслеживаемыми службами ОС

Для управления отслеживаемыми службами ОС:

1. В Dynatrace перейдите в **OS service monitoring** для нужного уровня.

   Уровень хоста

   1. Перейдите в **Hosts**.
   2. Необязательно: отфильтруйте по `Operating system` (Windows).
   3. Найдите хост и выберите его для отображения страницы хоста.
   4. На странице хоста откройте меню просмотра (**…**) и выберите **Settings**.
   5. Выберите вкладку **OS service monitoring**.

   Уровень группы хостов

   6. Перейдите в **Hosts**.
   7. Необязательно: отфильтруйте по `Operating system` (Windows).
   8. Отфильтруйте по `Host group` и начните вводить имя группы хостов для её поиска и выбора.
   9. Откройте любой хост из данной группы.
   10. На странице хоста раскройте раздел **Properties and tags** и выберите имя группы хостов.
   11. Выберите вкладку **OS service monitoring**.

   Уровень среды

   Перейдите в **Settings** > **Monitoring** > **OS services monitoring**.
2. Отслеживаемые службы ОС отображаются в таблице под кнопкой **Add new service**.

   * Для фильтрации таблицы введите строку поиска в поле **Filter items…**
   * Чтобы прекратить мониторинг указанной службы, отключите параметр **Enabled**.
   * Для удаления службы из таблицы нажмите кнопку удаления в столбце **Delete**.
   * Для просмотра и редактирования деталей выберите элемент управления раскрытием в столбце **Details**. Можно изменить имя службы или отображаемое имя.

## Метрические события для оповещений о доступности служб

После добавления службы можно создать пользовательское событие для отслеживания её доступности на основе метрики **OS Service availability**.

Укажите следующую информацию:

* **Category** — Hosts
* **Metric** — OS Service availability
* **Aggregation** — Average
* **Dimension** — выбранное имя службы

Подробнее о создании и настройке метрических событий для оповещений см. в разделе [Metric events for alerting](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Конфигурация в масштабе через Settings API

Для масштабной настройки мониторинга доступности служб можно использовать [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

1. Для изучения схемы используйте [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") со значением `builtin:os.services.monitoring` в качестве schemaId.
2. На основе схемы `builtin:os.services.monitoring` создайте объект конфигурации.
3. Для создания конфигурации используйте [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").