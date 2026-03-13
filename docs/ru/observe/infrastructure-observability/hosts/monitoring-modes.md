---
title: Режимы мониторинга Infrastructure и Discovery
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/monitoring-modes
scraped: 2026-02-06T16:20:45.488376
---

# Режимы мониторинга Infrastructure и Discovery

# Режимы мониторинга Infrastructure и Discovery

* Пояснение
* Чтение: 12 мин.
* Обновлено 16 окт. 2025 г.

Если вам не нужно, чтобы OneAgent работал в режиме полного стека мониторинга, можно также использовать один из двух облегчённых режимов, предоставляющих подмножество метрик OneAgent с упором на инфраструктуру хоста:

* Режим Infrastructure Monitoring
* Режим Discovery

В таблице ниже показан обзор доступных параметров мониторинга для каждого из режимов.

|  | Discovery | Infrastructure | Full stack |
| --- | --- | --- | --- |
| Обнаружение топологии (обнаружение гибридного облака и Smartscape) | GA | GA | GA |
| Критичность хоста (обнаружение внешних сервисов и зависимостей приложений) | GA | GA | GA |
| Базовый мониторинг (работоспособность хоста, файловая система, OS Services) | GA | GA | GA |
| Детали процессов хоста |  | GA | GA |
| Детальный анализ дисков |  | GA | GA |
| Анализ сети |  | GA | GA |
| Анализ памяти |  | GA | GA |
| Расширения |  | opt-in | opt-in |
| Пользовательские метрики |  | 100 / хост | 15 / 256 МиБ |
| Log Management | opt-in | opt-in | opt-in |
| Трассировка и профилирование |  |  | GA |
| Внедрение в процессы |  | opt-out | GA |
| Application Security[1](#fn-1-1-def) | opt-in | opt-in | opt-in |
| Live Debugger | opt-in | opt-in | opt-in |

1

Дополнительные сведения о режимах Infrastructure Monitoring и Discovery для Application Security см. в разделе [Режимы мониторинга для Application Security](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

## Режим мониторинга по умолчанию

Можно определить режим мониторинга по умолчанию до установки OneAgent. Это изменит режим мониторинга **Full-Stack** по умолчанию на странице развёртывания OneAgent (для операционных систем Linux, Windows и AIX) и в приложении **Discovery & Coverage** (при развёртывании OneAgent со страницы **Install OneAgent**).

Установка режима мониторинга по умолчанию

1. Перейдите в **Settings** > **Preferences** > **OneAgent default mode**.
2. Выберите **OneAgent default monitoring mode** из раскрывающегося списка.
3. Нажмите **Save changes**.

Выбранное значение будет установлено как значение по умолчанию для выбранного режима развёртывания OneAgent.

## Режим Discovery

OneAgent версии 1.281+

Режим Discovery OneAgent предоставляет базовые метрики, позволяющие обнаруживать ваши хосты и процессы и оценивать потенциал для расширения мониторинга.

Мы рекомендуем развёртывать OneAgent в режиме Full-Stack Monitoring для мониторинга критически важных для бизнеса приложений. Аналогично, рекомендуем отслеживать критическую инфраструктуру, такую как базы данных, очереди и системы обмена сообщениями, с помощью Infrastructure Monitoring. OneAgent в режиме Discovery можно развернуть на остальной части инфраструктуры для полной видимости благодаря его относительно низкой стоимости.

Режим Discovery доступен только при использовании модели Dynatrace Platform Subscription. Потребление лицензии осуществляется через возможность **Foundation & Discovery**. Подробнее см. в разделе [Обзор Application & Infrastructure Observability (DPS)](/docs/license/capabilities/app-infra-observability#discovery "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

В режиме Discovery доступны следующие встроенные метрики:

### CPU

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.cpu.entConfig | AIX Entitlement configured — настроенная мощность AIX. Capacity Entitlement — количество виртуальных процессоров, назначенных разделу AIX. Измеряется в долях процессора, равных 0,1 или 0,01. Подробнее об entitlement см. в [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) в официальной документации IBM. | Соотношение | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used — используемый процент entitlement. Capacity Entitlement — количество виртуальных ядер, назначенных разделу AIX. Подробнее об entitlement см. в [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz) в официальной документации IBM. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.idle | Простой CPU — среднее время CPU, когда CPU не имел задач. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | Ожидание I/O CPU — процент времени, когда CPU простаивал при наличии невыполненного запроса I/O. Недоступно на Windows. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.load | Системная нагрузка — среднее количество процессов, выполняемых или ожидающих выполнения CPU за последнюю минуту. | Соотношение | autoavgmaxmin |
| builtin:host.cpu.load15m | Системная нагрузка за 15 мин. — среднее количество процессов, выполняемых или ожидающих выполнения CPU за последние 15 минут. | Соотношение | autoavgmaxmin |
| builtin:host.cpu.load5m | Системная нагрузка за 5 мин. — среднее количество процессов, выполняемых или ожидающих выполнения CPU за последние 5 минут. | Соотношение | autoavgmaxmin |
| builtin:host.cpu.other | Прочее время CPU — среднее время CPU, потраченное на другие задачи: обслуживание запросов прерываний (IRQ), запуск виртуальных машин под управлением ядра хоста (то есть хост является гипервизором для ВМ). Доступно только для хостов Linux. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed — всего CPU, потреблённых разделом AIX. | Соотношение | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal — среднее время CPU, когда виртуальная машина ждёт получения циклов CPU от гипервизора. В виртуальной среде циклы CPU распределяются между виртуальными машинами на сервере гипервизора. Высокий CPU steal на виртуализированном хосте означает, что циклы CPU отбираются у виртуальной машины для других целей, что может указывать на перегруженный гипервизор. Доступно только для хостов Linux. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.system | Системный CPU — среднее время CPU в режиме ядра. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.usage | Использование CPU % — процент времени CPU, когда CPU был задействован. Значение, близкое к 100%, означает, что большинство ресурсов обработки хоста используется, и CPU хоста не могут взять на себя дополнительную работу. | Процент (%) | autoavgmaxmin |
| builtin:host.cpu.user | Пользовательский CPU — среднее время CPU в пользовательском режиме. | Процент (%) | autoavgmaxmin |
| builtin:host.kernelThreads.blocked | AIX Заблокированные потоки ядра — длина очереди подкачки. Очередь подкачки содержит готовые к выполнению потоки, выгруженные вместе с выполняемыми в данный момент потоками. | Количество | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Потоки ядра в ожидании I/O-события — количество потоков, ожидающих прямого (cio) I/O файловой системы + количество процессов, спящих в ожидании буферизованного I/O. | Количество | autoavgmaxmin |
| builtin:host.kernelThreads.ioMessageWait | AIX Потоки ядра в ожидании I/O-сообщения — количество потоков, спящих и ожидающих операций raw I/O в определённый момент времени. Операция raw I/O позволяет приложениям напрямую записывать на уровень Logical Volume Manager (LVM). | Количество | autoavgmaxmin |
| builtin:host.kernelThreads.running | AIX Работающие потоки ядра — количество готовых к выполнению потоков (выполняющихся или ожидающих времени выполнения). Среднее количество готовых к выполнению потоков отображается в первом столбце вывода команды vmstat. | Количество | autoavgmaxmin |

### Память

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Доступная память — объём памяти (ОЗУ), доступной на хосте. Память, доступная для выделения новым или существующим процессам. Доступная память — это оценка того, сколько памяти доступно без свопинга. | Байт | autoavgmaxmin |
| builtin:host.mem.avail.pct | Доступная память % — процент памяти (ОЗУ), доступной на хосте. Отображает доступную память в процентах. | Процент (%) | autoavgmaxmin |
| builtin:host.mem.kernel | Память ядра — память, используемая системным ядром, включая память, используемую основными компонентами ОС и драйверами устройств. Как правило, значение очень мало. | Байт | autoavgmaxmin |
| builtin:host.mem.recl | Восстанавливаемая память — использование памяти для конкретных целей. Восстанавливаемая память рассчитывается как доступная память минус свободная память. Подробнее о восстанавливаемой памяти см. в [этой статье блога](https://www.dynatrace.com/news/blog/improved-host-memory-metrics-now-include-reclaimable-memory/). | Байт | autoavgmaxmin |
| builtin:host.mem.total | Всего памяти — объём памяти (ОЗУ), установленной в системе. | Байт | autovalue |
| builtin:host.mem.usage | Используемая память % — показывает процент используемой памяти. Используемая память рассчитывается OneAgent следующим образом: used = total - available. Таким образом, метрика используемой памяти, отображаемая в Dynatrace, не равна метрике используемой памяти, отображаемой системными инструментами. Примечание: рассчитывается как 100% - «Доступная память %». | Процент (%) | autoavgmaxmin |
| builtin:host.mem.used | Используемая память — используемая память рассчитывается OneAgent следующим образом: used = total - available. Таким образом, метрика используемой памяти, отображаемая в Dynatrace, не равна метрике используемой памяти, отображаемой системными инструментами. | Байт | autoavgmaxmin |

### Доступность

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.availability.state | Состояние доступности хоста — метрика состояния доступности хоста, отображаемая с интервалом 1 минута. | Количество | autovalue |
| builtin:host.uptime | Время работы хоста — время с последней загрузки хоста. Требуется OneAgent 1.259+. Метрика не поддерживается для развёртываний OneAgent только для приложений. | Секунда | autoavgmaxmin |

### Диск

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.disk.avail | Доступное место на диске — объём свободного места, доступного пользователю в файловой системе. На Linux и AIX — свободное место для непривилегированного пользователя, без части, зарезервированной для root. | Байт | autoavgmaxmin |
| builtin:host.disk.bytesRead | Байт/с чтения с диска — скорость чтения из файловой системы в байтах в секунду. | Байт/с | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Байт/с записи на диск — скорость записи в файловую систему в байтах в секунду. | Байт/с | autoavgmaxmin |
| builtin:host.disk.free | Доступное место на диске % — процент свободного места, доступного пользователю в файловой системе. | Процент (%) | autoavgmaxmin |
| builtin:host.disk.used | Использованное место на диске — объём использованного пространства в файловой системе. | Байт | autoavgmaxmin |

### Сеть

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.net.nic.bytesRx | Полученные байты NIC — байты, полученные сетевым интерфейсом на хосте. | Байт/с | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | Переданные байты NIC — байты, переданные сетевым интерфейсом на хосте. | Байт/с | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | Использование канала приёма NIC — использование канала приёма сетевого интерфейса на хосте. | Процент (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | Использование канала передачи NIC — использование канала передачи сетевого интерфейса на хосте. | Процент (%) | autoavgmaxmin |

### Включение режима Discovery

Режим Discovery включается на уровне хоста — как во время, так и после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим Discovery во время установки OneAgent, используйте параметр `--set-monitoring-mode=discovery`.

Подробнее см. в документации по [установке OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms."), соответствующей вашей среде.

После установки OneAgent

Чтобы включить режим Discovery после установки OneAgent, воспользуйтесь одним из следующих способов:

* В Dynatrace

  1. Перейдите в **Hosts** (предыдущий Dynatrace) или ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
  2. В правом верхнем углу выберите **More** (**…**) > **Settings** для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите в **Monitoring Mode** и в раскрывающемся меню выберите **Discovery**.
  5. Нажмите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-monitoring-mode=discovery`.

### Внедрение кодового модуля

Для работы [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") и [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.") в режиме Discovery требуется внедрение кодового модуля. По умолчанию внедрение кодового модуля отключено.

После [включения режима Discovery](#enable-discovery-mode) можно включить внедрение кодового модуля для отдельного хоста.

1. Перейдите на страницу настроек нужного хоста и выберите **Host monitoring**.
2. Перейдите в **Advanced settings**.
3. Включите **CodeModule Injection**, затем нажмите **Save changes**.
4. Перезапустите отслеживаемые процессы на хосте.

Подробнее о работе Application Security в режиме Discovery см. в разделе [Application Security: Discovery mode](/docs/secure/application-security#discovery "Access the Dynatrace Application Security functionalities.").

## Режим Infrastructure Monitoring

Автоматическое внедрение OneAgent

OneAgent в режиме Infrastructure Monitoring автоматически внедряется в процессы для мониторинга вспомогательных сервисов, написанных на Java, и метрик среды выполнения для поддерживаемых языков. Узнайте, как [отключить автоматическое внедрение](#disable-auto-injection).

Хотя режим Full-Stack обеспечивает полный мониторинг производительности приложений, видимость на уровне кода, глубокий мониторинг процессов и Infrastructure Monitoring (включая PaaS-платформы) для случаев, когда требуется меньший объём видимости, можно настроить OneAgent в режиме Infrastructure Monitoring, который обеспечивает мониторинг физической и виртуальной инфраструктуры, мониторинг логов и AIOps.

### Включение режима Infrastructure Monitoring

Режим Infrastructure Monitoring включается на уровне хоста — как во время, так и после установки OneAgent.

Во время установки OneAgent

Чтобы включить режим Infrastructure Monitoring во время установки OneAgent, используйте параметр `--set-monitoring-mode=infra-only`.

Подробнее см. в документации по [установке OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms."), соответствующей вашей среде.

После установки OneAgent

Чтобы включить режим Infrastructure Monitoring после установки OneAgent, воспользуйтесь одним из следующих способов:

* В Dynatrace

  1. Перейдите в **Hosts** (предыдущий Dynatrace) или ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
  2. В правом верхнем углу выберите **More** (**…**) > **Settings** для отображения страницы **Host settings**.
  3. Выберите **Host monitoring**.
  4. Перейдите в **Monitoring Mode** и в раскрывающемся меню выберите **Infrastructure**.
  5. Нажмите **Save changes**.
* Используйте [интерфейс командной строки OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-monitoring-mode=infra-only`.
* Используйте [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") для включения режима Infrastructure Monitoring в масштабе.
* Для загрузки схемы используйте [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") с `builtin:host.monitoring` в качестве schemaId и создайте объект конфигурации с помощью [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

### Внедрение в процессы

Внедрение в процессы предоставляет дополнительные данные для Infrastructure Monitoring. Внедрение в процессы включено по умолчанию.

Если вы запускаете OneAgent как контейнер с включённым режимом Infrastructure Monitoring, внедрение в процессы выполняться не будет.

Режим Infrastructure Monitoring позволяет отслеживать любой компонент инфраструктуры и вспомогательный сервис, написанный на Java. Вы можете отслеживать вспомогательные сервисы, поддерживаемые по умолчанию (например, Kafka или ActiveMQ), а также создавать собственные [расширения JMX и PMI](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Learn how to extend Dynatrace monitoring to include applications you've instrumented with JMX.") для компонентов инфраструктуры и использовать их в режиме Infrastructure Monitoring.

Кроме того, с внедрением в процессы режим Infrastructure Monitoring предоставляет метрики среды выполнения для:

* Java
* .NET
* Node.js
* Golang
* PHP
* Веб-серверов, таких как Apache HTTP, Nginx или Microsoft IIS.

### Отключение автоматического внедрения в процессы

Мы не рекомендуем отключать автоматическое внедрение, но если это необходимо из-за строгих требований безопасности, можно выбрать один из нескольких вариантов. Отключение автоматического внедрения также предотвращает обнаружение Dynatrace уязвимостей или живую отладку в вашей среде, даже если вы включили [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.") или [Live Debugger](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace."). Автоматическое внедрение можно отключить на уровне хоста или среды.

#### Отключение автоматического внедрения для отдельного хоста

После установки OneAgent через UI

1. Перейдите в **Hosts** (предыдущий Dynatrace) или ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и откройте страницу обзора хоста.
2. В правом верхнем углу выберите **More** (**…**) > **Settings** для отображения страницы **Host settings**.
3. Выберите **Host Monitoring**.
4. Перейдите в **Advanced settings**.
5. Отключите **ProcessAgent Injection**, затем нажмите **Save changes**.
6. Перезапустите отслеживаемые процессы на хосте.

После установки OneAgent через командную строку

Используйте [интерфейс командной строки OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") для установки параметра `--set-auto-injection-enabled=false`.

Если вы используете oneagentctl для отключения автоматического внедрения, вы не сможете управлять автоматическим внедрением в режиме Infrastructure Monitoring через веб-интерфейс Dynatrace в разделе **Settings > Monitoring > Monitored technologies** или через [API конфигурации мониторинга OneAgent](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.").

#### Отключение автоматического внедрения для среды

Определение пользовательских правил мониторинга процессов

Вы можете отключить внедрение в процессы для определённых групп процессов с помощью пользовательских правил мониторинга процессов.

Пользовательские правила мониторинга процессов предоставляют детальный контроль над тем, в какие процессы внедряется OneAgent, с подходом, который легко масштабируется в больших средах. Не нужно изменять конфигурацию системы, а несколько правил могут охватывать тысячи процессов.

Подробнее см. в разделе [Глубокий мониторинг процессов](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring").

Отключение метрик среды выполнения

Вы можете отключить сбор метрик JMX/PMI и среды выполнения, что приведёт к отключению автоматического внедрения в режиме Infrastructure Monitoring.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. В списке поддерживаемых технологий найдите запись **Java/.NET/Node.js/Golang/PHP runtime metrics + WebServer metrics in Infrastructure Mode**.
3. Выберите значок карандаша ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для редактирования и отключите его.
4. Перезапустите все процессы на хостах в режиме Infrastructure Monitoring.

Отключение выбранных расширений

Вы также можете отключить выбранные расширения, собирающие метрики на уровне среды.

1. Перейдите в **Settings** > **Monitoring** > **Monitored technologies**.
2. Поддерживаемые технологии

   Пользовательские расширения

   1. В списке поддерживаемых технологий найдите технологии, отмеченные как **JMX monitoring** в столбце **Type**.
   2. Выберите значок карандаша ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для редактирования нужного расширения.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   1. В списке пользовательских расширений найдите расширения, отмеченные как **JMX** или **PMI** в столбце **Extension type**.
   2. Выберите название нужного расширения.
   3. Отключите **Monitor the environment for hosts in infrastructure-only monitoring mode**.

   Настройка на уровне хоста имеет приоритет над настройками среды. Если хост настроен на **Use host configuration** для расширения, и расширение не активировано на этом хосте, конфигурация среды применяться не будет. Чтобы убедиться, что расширение активно на уровне отдельного хоста:

   1. Перейдите в **Hosts** (предыдущий Dynatrace) или ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** и найдите хост в режиме Infrastructure Monitoring. Можно фильтровать по **Monitoring mode: Infrastructure only**.
   2. Откройте страницу хоста.
   3. В правом верхнем углу выберите **More** (**…**) > **Settings** для отображения страницы **Host settings**.
   4. В таблице **Monitored technologies** найдите расширения типа **JMX extension**, **JMX monitoring** или **PMI extension**.
   5. Нажмите **Edit**. Используйте элемент управления **Activate `<extension name>` on this host**.

### Фильтрация хостов по статусу внедрения

При отключении автоматического внедрения такие хосты можно найти с помощью фильтра **Auto-injection** на странице **Deployment Status** или через [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Использование веб-интерфейса Dynatrace

1. Перейдите в **Deployment Status** и выберите вкладку **OneAgents**.
2. Выберите поле **Filter by**, выберите **Auto-injection** и **Disabled manually**. Также можно использовать один из фильтров ниже для проверки других причин. Фильтр отображается только при наличии хоста с соответствующим статусом в вашем развёртывании.

* **Enabled**
  Автоматическое внедрение успешно включено.
* **Disabled manually**
  Автоматическое внедрение было отключено [после установки OneAgent](#after-install) — через веб-интерфейс Dynatrace или `oneagentctl`.
* **Disabled on installation**
  Автоматическое внедрение было отключено [во время установки OneAgent](#during-install).
* **Disabled on sanity check**
  Автоматическое внедрение не было включено из-за неудачного теста, выполненного установщиком OneAgent до начала установки. Проверьте лог установщика OneAgent для получения подробной информации.
* **Failed on installation**
  Автоматическое внедрение завершилось ошибкой во время установки OneAgent. Проверьте лог установщика OneAgent для получения подробной информации.

Использование Dynatrace API

Выполните вызов [OneAgent on a host - GET a list of hosts with OneAgent details](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") с параметром `autoInjection`, установленным в `DISABLED_MANUAL`. Возвращаемые данные содержат список OneAgent с отключённым автоматическим внедрением [после установки OneAgent](#after-install) — через веб-интерфейс Dynatrace или `oneagentctl`.

## Мониторинг виртуализации

Dynatrace поддерживает [мониторинг виртуализации](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). Для мониторинга виртуальных компонентов в вашей среде необходимо выполнить дополнительный шаг помимо начальной настройки. Подробнее см. в разделе [Настройка мониторинга виртуализации](/docs/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.").

## Часто задаваемые вопросы

Что происходит, когда OneAgent внедряется в отслеживаемую технологию?

При внедрении внедрённый модуль становится динамически связанным с отслеживаемой технологией. Следовательно, он становится неотъемлемой частью отслеживаемого процесса и может быть удалён только с перезапуском процесса. В зависимости от ОС (Windows/Linux/AIX) внедрение выполняется несколько по-разному, но результат примерно одинаков.

Я отключил внедрение, но вижу, что глубокие кодовые модули Dynatrace по-прежнему внедрены в отслеживаемые технологии.

Правила внедрения относятся к моменту запуска процесса поддерживаемой технологии. После запуска глубокий кодовый модуль мониторинга OneAgent остаётся динамически связанным с отслеживаемой технологией и может быть выгружен только путём перезапуска отслеживаемого процесса.

Я перезапустил/отключил/остановил OneAgent, но внедрённые модули остаются активными. В чём причина?

При внедрении внедрённый модуль становится динамически связанным с отслеживаемой технологией. Следовательно, он становится неотъемлемой частью отслеживаемого процесса и может быть удалён только путём перезапуска отслеживаемого процесса.

Как OneAgent отслеживает процессы?

OneAgent внедряется в процесс при каждом запуске нового процесса в системе. OneAgent идентифицирует запущенный процесс (по имени, расположению, пользовательскому пространству и т. д.) и, если он поддерживается для внедрения и правила внедрения его не исключают, создаёт динамическую связь между отслеживаемым процессом и одним из глубоких кодовых модулей мониторинга OneAgent.

Я отключил OneAgent в веб-интерфейсе, но всё ещё вижу активный процесс на хосте и определённый сетевой трафик между OneAgent и кластером Dynatrace. Я думал, что отключённые OneAgent прекращают всю активность.

Отключённые OneAgent фактически прекращают мониторинг вашей среды. Однако ядро OneAgent, ответственное за связь с кластером Dynatrace, остаётся активным. Поскольку связь между OneAgent и кластерами Dynatrace всегда инициируется на стороне OneAgent, OneAgent должен продолжать отправлять свой статус и запрашивать у кластера, нужно ли ему снова начать мониторинг.
