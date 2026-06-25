---
title: Установка модуля z/OS Java
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java
scraped: 2026-05-12T11:24:09.591624
---

# Установка модуля z/OS Java

# Установка модуля z/OS Java

* Чтение: 15 мин
* Обновлено 18 ноября 2025 г.

Модуль z/OS Java позволяет получить наблюдаемость для Java-приложений, включая IBM MQ и вызовы к базам данных.

| Наблюдаемость для | Включает |
| --- | --- |
| WebSphere Application Server  WebSphere Liberty | * Входящие веб-запросы в WebSphere Application Server и Liberty * Исходящие веб-запросы из WebSphere Application Server и Liberty через Apache HttpClient * Исходящие запросы CICS Transaction Gateway из WebSphere Application Server и Liberty через CTG-клиент * Метрики, специфичные для WebSphere Application Server и WebSphere Liberty (PMI и JMX) * Управляемые метрики памяти JVM (JMX) |
| z/OS Connect | * Входящие веб-запросы в z/OS Connect * Исходящие запросы из z/OS Connect через поставщиков услуг CICS, IMS и IBM MQ * Метрики, специфичные для z/OS Connect (JMX) * Управляемые метрики памяти JVM (JMX) |
| Транзакции CICS/IMS | Транзакции, инициированные через * IBM MQ и JMS * CICS SOAP и CICS Transaction Gateway * IMS SOAP Gateway |
| Вызовы к базам данных | Вызовы к Db2 с SQL-операторами из Java-приложений через JDBC |

Отслеживайте Java-приложения сквозь всю цепочку вызовов с помощью Dynatrace и быстро обнаруживайте аномалии

Анализируйте производительность транзакций сквозь всю цепочку с помощью [потока служб](/managed/observe/application-observability/services-classic/service-backtrace "Отслеживайте последовательность вызовов служб вплоть до щелчка в браузере, который её инициировал.").

![zOS Java 1](https://dt-cdn.net/images/zos-java-1-2772-facc3b2740.png)

zOS Java 1

Используйте [распределённые трассировки PurePath](/managed/observe/application-observability/distributed-traces "Получите наблюдаемость в высокораспределённых, облачно-ориентированных архитектурах для эффективной трассировки и анализа транзакций в реальном времени."), чтобы детализировать данные до уровня кода и оптимизировать программы.

![zOS Java 2](https://dt-cdn.net/images/zos-java-2-2729-43a263828d.png)

zOS Java 2

Быстро обнаруживайте аномалии с помощью [горячих точек времени ответа службы](/managed/observe/application-observability/services-classic/service-response-time-hotspots "Определите действия, потребляющие наибольшее время ответа для каждой службы.").

![zOS Java 3](https://dt-cdn.net/images/zos-java-3-2312-97d45f24a2.png)

zOS Java 3

Анализируйте сбои и исключения с подробными стек-трейсами.

![zOS Java 4](https://dt-cdn.net/images/zos-java-4-2674-ebbc7f564d.png)

zOS Java 4

Оценивайте работоспособность и производительность JVM с развёрнутыми на ней приложениями

Получайте информацию о JVM с помощью управляемых метрик памяти Dynatrace:

![zOS Java metrics 1](https://dt-cdn.net/images/zos-java-metrics-1-2472-ee3a4ee341.png)

zOS Java metrics 1

Оценивайте работоспособность и производительность серверов приложений с помощью технологически специфичных метрик:

![zOS Java metrics 2](https://dt-cdn.net/images/zos-java-metrics-2-2473-4cc98e9473.png)

zOS Java metrics 2

### Какие метрики JMX и PMI Dynatrace предоставляет из коробки?

Метрики, специфичные для JVM:

| Группа метрик | Метрика | Источник |
| --- | --- | --- |
| JVM memory | Garbage collection total activation count | JMX |
| JVM memory | Garbage collection total collection time | JMX |
| JVM memory pool | Garbage collection count | JMX |
| JVM memory pool | Garbage collection time | JMX |
| JVM memory pool | Heap memory pool maximum bytes | JMX |
| JVM memory pool | Heap memory pool committed bytes | JMX |
| JVM memory pool | Heap memory pool used bytes | JMX |
| JVM memory runtime | Runtime maximum memory | JMX |
| JVM memory runtime | Runtime total memory | JMX |
| JVM memory runtime | Runtime free memory | JMX |
| JVM threads | Thread count | JMX |
| JVM classes | Total number of loaded classes | JMX |
| JVM classes | Number of loaded classes | JMX |
| JVM classes | Number of unloaded classes | JMX |

Метрики, специфичные для WebSphere Liberty и z/OS Connect:

| Группа метрик | Метрика | Описание метрики | Источник |
| --- | --- | --- | --- |
| JDBC connection pool | In use connections | Количество используемых соединений. Это число может включать несколько соединений, совместно использующих одно управляемое соединение. | JMX |
| JDBC connection pool | Free connections | Количество управляемых соединений в свободном пуле. | JMX |
| JDBC connection pool | Managed connections | Общее количество управляемых соединений в свободном, общем и выделенном пулах. | JMX |
| JDBC connection pool | In use time | Среднее время использования соединения в миллисекундах. | JMX |
| JDBC connection pool | Wait time | Среднее время ожидания соединения в миллисекундах, если соединение временно недоступно. | JMX |
| Thread pool | Pool size | Среднее количество потоков в пуле. | JMX |
| Thread pool | Active threads | Количество активных потоков, обрабатывающих запросы. | JMX |
| Servlet | Request count | Общее количество запросов, обработанных сервлетом. | JMX |

Метрики, специфичные для WebSphere Application Server:

| Группа метрик | Метрика | Описание метрики | Источник |
| --- | --- | --- | --- |
| JDBC connection pool | Pool size | Размер пула соединений. | PMI |
| JDBC connection pool | Free pool size | Количество управляемых соединений в свободном пуле. | PMI |
| JDBC connection pool | Concurrent waiters | Количество потоков, ожидающих соединения в данный момент. | PMI |
| JDBC connection pool | Average wait time | Среднее время ожидания соединения в миллисекундах, если соединение временно недоступно. | PMI |
| JDBC connection pool | Average use time | Среднее время использования соединения в миллисекундах. | PMI |
| JDBC connection pool | Percent used | Доля используемого пула в процентах. | PMI |
| Thread pool | Pool size | Среднее количество потоков в пуле. | PMI |
| Thread pool | Active threads | Количество одновременно активных потоков. | PMI |
| Servlet | Live sessions | Количество локальных сеансов, кэшированных в памяти с момента включения этой метрики. | PMI |
| Servlet | Total requests | Общее количество запросов, обработанных сервлетом. | PMI |

### Можно ли отслеживать пользовательские метрики JMX с помощью модуля z/OS Java?

Да, модуль z/OS Java позволяет отслеживать пользовательские метрики JMX. Подробнее см. раздел [Мониторинг метрик JMX в z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Узнайте, как настроить мониторинг метрик JMX для Java-приложений в z/OS.").

## Предварительное условие

Активируйте [функцию OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управляйте функциями OneAgent глобально и для каждой группы процессов.") **Forward Tag 4 trace context extension**.

## Загрузка

1. [Скачайте наборы данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Скачайте и установите наборы данных продукта Dynatrace для z/OS.") и извлеките JAR-файл (`dynatrace-oneagent-zos-java.jar`).
2. Перенесите JAR-файл в окружение z/OS [Unix System Services](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) в бинарном режиме.
3. Создайте новый файл с именем `dtconfig.json` в папке z/OS USS, где расположен модуль.

   Минимальный файл `dtconfig.json` содержит идентификатор окружения Dynatrace (**Tenant**), идентификатор кластера (**ClusterID**) и имя подсистемы zDC (**ZdcName**). Например:

   ```
   {



   "Tenant": "myTenant",



   "ClusterID": myCluster,



   "ZdcName": "DEFAULT"



   }
   ```

   Замените `myTenant` и `myCluster>` значениями вашего окружения Dynatrace. Чтобы найти эти значения, перейдите в **Deploy Dynatrace**, выберите **Start installation** > **z/OS**.

   Если имя zDC задано как `DEFAULT`, модуль подключится к стандартному идентификатору подсистемы zDC. Чтобы использовать другую zDC, замените `DEFAULT` на альтернативный идентификатор подсистемы.

   Имя подсистемы zDC можно найти в [параметрах SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).") элемента JCL SYSIN `ZDCSYSIN`. Стандартное имя подсистемы zDC: `MEPC`.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   SUBSYSTEM_ID(MEPC)



   DEFAULT(YES)
   ```

   Если в [параметрах SYSIN](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).") параметр `DEFAULT` имеет значение `YES`, в файле `dtconfig.json` также можно использовать `DEFAULT`.

* Для файла `dtconfig.json` поддерживаются кодировки EBCDIC 1047, UTF-8 и ASCII.
* Модуль автоматически читает `dtconfig.json`, если файл находится в той же папке, что и `dynatrace-oneagent-zos-java.jar`.
* Если `dtconfig.json` размещён в другой папке, укажите путь к нему через переменную окружения `DT_CONFIG_FILE`. Путь должен включать имя файла. Допустимы как абсолютный путь, так и путь относительно рабочей папки процесса.

## Установка

### Обновление ранее установленной версии Dynatrace

Если Dynatrace уже установлен и вы переходите на новую версию, перейдите к разделу [Обновление][#update]

### Сервер приложений

Необходимо добавить модуль z/OS Java в аргументы JVM каждого сервера приложений, который требуется отслеживать.

WebSphere Application Server

WebSphere Liberty

WebSphere Liberty внутри региона CICS

1. Откройте Admin Console WebSphere Application Server и перейдите в раздел **Application servers**.
2. Выберите `<YOUR_SERVER>` > **Process definition** > **Servant** и откройте **Java Virtual Machine**.
3. Скопируйте аргумент JVM из окружения Dynatrace и вставьте его в поле **Generic JVM arguments**:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
4. Сохраните изменения и перезапустите WebSphere Application Server.

* Модуль необходимо добавлять только в процессы Servant.
* Мы рекомендуем добавлять модуль первым в списке аргументов JVM.
* Модуль не должен быть добавлен в конец командной строки.

1. Создайте файл `jvm.options` в корневой папке WebSphere Liberty (в этой папке, как правило, также находится файл `server.xml`) или отредактируйте существующий файл.
2. Скопируйте аргумент JVM из окружения Dynatrace и вставьте его в файл `jvm.options`:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
3. Добавьте функцию `monitor-1.0` в `featureManager` файла `server.xml`, чтобы собирать дополнительные метрики, такие как пулы соединений или пулы потоков:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
4. Сохраните изменения и перезапустите WebSphere Liberty.

* Мы рекомендуем добавлять модуль первым в списке аргументов JVM.
* Модуль не должен быть добавлен в конец командной строки.
* По умолчанию в качестве имени экземпляра группы процессов используется имя сервера WebSphere Liberty. Чтобы задать другое имя экземпляра группы процессов, добавьте следующее системное свойство в командную строку JVM: `-Dwlp.server.name=yourServerName`. Замените `yourServerName` нужным именем.

1. Создайте файл `.jvmprofile` в регионе CICS, принадлежащем CICS JVMSERVER, который выполняет WebSphere Liberty, или отредактируйте существующий файл.
2. Скопируйте аргумент JVM из окружения Dynatrace и вставьте его в файл `.jvmprofile`:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
3. Добавьте функцию `monitor-1.0` в `featureManager` файла `server.xml`, чтобы собирать дополнительные метрики, такие как пулы соединений или пулы потоков:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
4. Сохраните изменения и перезапустите WebSphere Liberty.

* Одновременный мониторинг региона CICS и работающего внутри него WebSphere Liberty поддерживается только при условии, что они отправляют данные в разные подсистемы zDC. Если они используют разные подсистемы zDC, хотя бы одна из них должна быть запущена как нестандартная (см. `SUBSYSTEM_ID` в [параметрах SYSIN zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Настройка подсистемы сбора данных z/OS (zDC).")). При этом обе подсистемы zDC могут отправлять данные в один модуль zRemote.

  + Для кодового модуля CICS имя подсистемы zDC задаётся в [параметрах SYSIN CICS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Установка кодового модуля CICS Dynatrace.").
  + Для модуля z/OS Java имя подсистемы zDC задаётся в [файле `dtconfig.json`](#download).
* OneAgent версии 1.281+ Dynatrace версии 1.283+ При работе в регионе CICS имя экземпляра группы процессов будет включать как имя региона CICS, так и имя сервера WebSphere Liberty в формате `CICS region (server name)`.

### Промежуточное программное обеспечение

Необходимо добавить модуль z/OS Java в каждый продукт, который требуется отслеживать.

z/OS Connect Enterprise Edition

CICS Transaction Gateway

IMS SOAP Gateway

1. Добавьте модуль в переменную `JVM_OPTIONS STDENV`:

   ```
   JVM_OPTIONS=-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
2. Необязательно. Добавьте функцию `monitor-1.0` в `featureManager` файла `server.xml`, чтобы собирать дополнительные метрики, такие как пулы соединений или пулы потоков:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
3. Сохраните изменения и перезапустите z/OS Connect Enterprise Edition.
4. Для поставщика услуг CICS активируйте [функцию OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управляйте функциями OneAgent глобально и для каждой группы процессов.") **z/OS CICS z/OS Connect**.
5. Для поставщика услуг IMS:

   1. Добавьте модуль IMS в **IMS Connect**, как описано в разделе [Установка модуля IMS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims#install "Установка кодового модуля IMS Dynatrace.").
   2. Активируйте [функцию OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управляйте функциями OneAgent глобально и для каждой группы процессов.") **z/OS IMS z/OS Connect**.
6. Для поставщика услуг MQ дополнительная настройка не требуется.

1. Добавьте модуль в элемент `CTGENV` и переменную `CTGSTART_OPTS`:

   ```
   -j-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
2. Сохраните изменения и перезапустите CICS Transaction Gateway.

* Поддерживаются только протоколы EXCI и IPIC.
* Конфигурация CICS Transaction Gateway в локальном режиме WAS не поддерживается.

1. Добавьте модуль как параметр `zDT` в параметры IMS SOAP Gateway:

   ```
   zDT="-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar"
   ```

   Замените `PATH_TO` путём к вашему JAR-файлу.
2. Экспортируйте определённый параметр `zDT`, чтобы он вошёл в состав `IBM_JAVA_OPTIONS`.

   ```
   export IBM_JAVA_OPTIONS="$zDT $JAVA_OPTS"
   ```
3. Сохраните изменения и перезапустите IMS SOAP Gateway.

## Журналирование

По умолчанию журналирование для модуля z/OS Java отключено. Чтобы включить его, добавьте один из следующих параметров в аргумент JVM:

| Параметр | Значение по умолчанию | Описание |
| --- | --- | --- |
| log-stdout | `false` | Если `true`, логи записываются в стандартный поток вывода. |
| log-stderr | `false` | Если `true`, логи записываются в стандартный поток ошибок. |
| log-file | `false` | Если `true`, логи записываются в файл с ротацией (файл с индексом 0 сохраняется). Схема именования: `dynatrace-oneagent-java.<PID>.<LPAR>.<INDEX>.log`. |

При необходимости запись логов можно вести сразу в несколько мест. Например:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-stdout=true,log-file=true
```

При необходимости запись логов в файл можно настроить с помощью следующих параметров:

| Параметр | Значение по умолчанию | Описание |
| --- | --- | --- |
| log-file-dir | `<CODEMODULE_FOLDER>/logs` | По умолчанию файлы логов записываются в папку модуля z/OS Java. Также поддерживается запись по абсолютному пути (схема: `/<PATH_TO>/logs`) или по пути относительно рабочей папки процесса (схема: `<PATH_TO>/logs`). |

При изменении папки по умолчанию убедитесь, что сервер приложений имеет права на запись в папку, в которую модуль должен записывать файлы логов.

### Диагностика OneAgent

Dynatrace рекомендует записывать логи в общую папку логов zDC, чтобы они включались в рабочий процесс [диагностики OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как запускать диагностику OneAgent."). Например, если бинарный файл `dtzagent` расположен по пути `/u/dt/agent/lib64/dtzagent` в окружении z/OS USS, папка логов: `/u/dt/log`. Как правило, общая папка логов zDC уже существует и содержит часть логов zDC.

Чтобы включить запись логов в файл по абсолютному пути, например в общую папку логов zDC `/u/dt/log`, задайте аргумент JVM следующим образом:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-file=true,log-file-dir=/u/dt/log
```

Если zDC установлен в другом расположении, укажите соответствующий абсолютный путь к общей папке логов zDC.

## Обновление

Чтобы обновить модуль z/OS Java до новой версии

1. [Скачайте наборы данных продукта z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Скачайте и установите наборы данных продукта Dynatrace для z/OS.") и перенесите JAR-файл (`dynatrace-oneagent-zos-java.jar`) в окружение z/OS USS в бинарном режиме.
2. Найдите существующий файл dtconfig.json в папке z/OS USS, где расположена старая версия модуля, и скопируйте его в папку z/OS USS, использованную на шаге 1.
3. Остановите отслеживаемый сервер приложений или промежуточное программное обеспечение.
4. Замените текущий JAR-файл новым.
5. Запустите сервер приложений или промежуточное программное обеспечение.

## Вопросы и ответы

Как включить program control для модуля z/OS Java?

Если после запуска сервера приложений в z/OS отображаются сообщения **Not Marked Program Controlled** или ошибки с кодом возврата 139:

```
BPXP015I HFS PROGRAM /tmp/libdynatrace-oneagent-odin-java5848811742465559217.so



IS NOT MARKED PROGRAM CONTROLLED.
```

Необходимо включить program control для модуля z/OS Java. Для этого

1. Распакуйте загруженный файл `dynatrace-oneagent-zos-java.jar` в папку с program control.
2. Пометьте соответствующий файл `.so` (31- или 64-разрядный) в каталоге `lib/zos-s390/` как program-controlled.

   * Перейдите в путь, содержащий файлы `.so`.
   * Выполните следующую команду, используя 31- или 64-разрядный файл:

     ```
     extattr +p libdynatrace-oneagent-odin-java_64.so
     ```
3. Добавьте `zos-native-library-override` в аргумент JVM.

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=zos-native-library-override=<PATH_TO_SO>/libdynatrace-oneagent-odin-java_64.so
   ```

   Где:

   * `<PATH_TO>`: путь к вашему JAR-файлу.
   * `<PATH_TO_SO>`: абсолютный путь к файлу `.so`, для которого требуется program control.
4. Перезапустите сервер приложений.

Можно ли отключить сенсоры модуля z/OS Java?

По умолчанию все сенсоры модуля z/OS Java включены. В случае проблем можно отключить конкретные сенсоры, установив их значение на `false` в файле `dtconfig.json`.

```
{



"Sensors": {



"Enable": {



"CTG": {



"Server": "false",



"Client": "false"



},



"HttpClient": {



"Apache": "false"



},



"JDBC": "false",



"JMS": "false",



"IbmMQ": "false",



"Servlet": "false",



"ZosConnect": "false"



}



}



}
```