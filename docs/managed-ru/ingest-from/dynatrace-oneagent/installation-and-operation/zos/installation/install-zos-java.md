---
title: Установка модуля z/OS Java
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java
scraped: 2026-03-05T21:29:54.594551
---

* Latest Dynatrace

С помощью модуля z/OS Java вы можете получить наблюдаемость для ваших Java-приложений, включая вызовы IBM MQ и базы данных.

Трассируйте ваши Java-приложения из конца в конец с Dynatrace и быстро обнаруживайте любые аномалии

Анализируйте производительность ваших транзакций из конца в конец с помощью service flow.

![zOS Java 1](https://dt-cdn.net/images/zos-java-1-2772-facc3b2740.png)

Используйте распределённые трассировки PurePath для углубления до уровня кода и оптимизации ваших программ.

![zOS Java 2](https://dt-cdn.net/images/zos-java-2-2729-43a263828d.png)

Быстро обнаруживайте аномалии с помощью горячих точек времени отклика сервиса.

![zOS Java 3](https://dt-cdn.net/images/zos-java-3-2312-97d45f24a2.png)

Анализируйте сбои и исключения с подробными трассировками стека.

![zOS Java 4](https://dt-cdn.net/images/zos-java-4-2674-ebbc7f564d.png)

Понимание состояния и производительности вашей JVM с развёрнутыми на ней приложениями

Получите информацию о вашей JVM с помощью метрик управляемой памяти Dynatrace:

![zOS Java metrics 1](https://dt-cdn.net/images/zos-java-metrics-1-2472-ee3a4ee341.png)

Понимайте состояние и производительность ваших серверов приложений с помощью специфичных для технологии метрик:

![zOS Java metrics 2](https://dt-cdn.net/images/zos-java-metrics-2-2473-4cc98e9473.png)

### Какие метрики JMX и PMI Dynatrace предоставляет по умолчанию?

Специфичные для JVM метрики:

Специфичные для WebSphere Liberty и z/OS Connect метрики:

Специфичные для WebSphere Application Server метрики:

### Можно ли отслеживать пользовательские метрики JMX с модулем z/OS Java?

Да, вы можете использовать модуль z/OS Java для мониторинга пользовательских метрик JMX. Для получения дополнительной информации см. Мониторинг метрик JMX на z/OS.

## Предварительные требования

Активируйте функцию OneAgent **Forward Tag 4 trace context extension**.

## Загрузка

1. Загрузите наборы данных продукта z/OS и извлеките JAR-файл (`dynatrace-oneagent-zos-java.jar`).
2. Перенесите JAR-файл в среду [Unix System Services](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) вашей z/OS в бинарном режиме.
3. Создайте новый файл с именем `dtconfig.json` в папке USS z/OS, где расположен модуль.

   Минимальный файл `dtconfig.json` содержит идентификатор вашей среды Dynatrace (**Tenant**), идентификатор кластера (**ClusterID**) и имя подсистемы zDC (**ZdcName**). Например:

   ```
   {


   "Tenant": "myTenant",


   "ClusterID": myCluster,


   "ZdcName": "DEFAULT"


   }
   ```

   Замените `myTenant` и `myCluster>` на значения вашей среды Dynatrace. Чтобы найти эти значения, в Dynatrace Hub выберите **OneAgent** > **Download OneAgent** или **Set up** (latest Dynatrace) > **z/OS**.

   Если имя zDC определено как `DEFAULT`, модуль будет подключаться к подсистеме zDC по умолчанию. Чтобы использовать другой zDC, замените `DEFAULT` на альтернативный идентификатор подсистемы.

   Вы можете найти имя подсистемы zDC в параметрах SYSIN.") вашего JCL-члена SYSIN `ZDCSYSIN`. Имя подсистемы zDC по умолчанию — `MEPC`.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)


   SUBSYSTEM_ID(MEPC)


   DEFAULT(YES)
   ```

   Если `DEFAULT` установлен в `YES` в параметрах SYSIN."), вы также можете использовать `DEFAULT` в файле `dtconfig.json`.

* Для файла `dtconfig.json` поддерживаются кодировки EBCDIC 1047, UTF-8 и ASCII.
* Модуль автоматически считывает `dtconfig.json`, если он находится в той же папке, что и `dynatrace-oneagent-zos-java.jar`.
* Если вы поместите `dtconfig.json` в другую папку, необходимо указать путь к нему через переменную среды `DT_CONFIG_FILE`. Путь должен включать имя файла. Вы можете использовать абсолютный путь или путь относительно рабочей папки процесса.

## Установка

### Обновление ранее установленной версии Dynatrace

Если у вас уже установлен Dynatrace и вы обновляете до нового релиза, вы можете перейти к разделу [Обновление][#update]

### Сервер приложений

Вам необходимо добавить модуль z/OS Java к аргументам JVM каждого сервера приложений, который вы хотите мониторить.

WebSphere Application Server

WebSphere Liberty

WebSphere Liberty внутри региона CICS

1. Откройте консоль администрирования WebSphere Application Server и перейдите к **Application servers**.
2. Выберите `<ВАШ_СЕРВЕР>` > **Process definition** > **Servant** и выберите **Java Virtual Machine**.
3. Скопируйте аргумент JVM из вашей среды Dynatrace и вставьте его в **Generic JVM arguments**:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
4. Сохраните изменения и перезапустите WebSphere Application Server.

* Модуль необходимо добавлять только к процессам Servant.
* Рекомендуется добавлять модуль как первый аргумент JVM.
* Модуль не должен добавляться в конец командной строки.

1. Создайте файл `jvm.options` в корневой папке вашего WebSphere Liberty (эта папка обычно также содержит файл `server.xml`) или отредактируйте существующий файл.
2. Скопируйте аргумент JVM из вашей среды Dynatrace и вставьте его в файл `jvm.options`:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
3. Добавьте функцию `monitor-1.0` в `featureManager` в файле `server.xml` для сбора дополнительных метрик, таких как пулы соединений или пулы потоков:

   ```
   <server>


   <featureManager>


   <feature>monitor-1.0</feature>


   </featureManager>


   </server>
   ```
4. Сохраните изменения и перезапустите WebSphere Liberty.

* Рекомендуется добавлять модуль как первый аргумент JVM.
* Модуль не должен добавляться в конец командной строки.
* По умолчанию мы используем имя сервера WebSphere Liberty в качестве имени экземпляра группы процессов. Если вы хотите использовать другое имя экземпляра группы процессов, вы можете переопределить его, добавив следующее системное свойство в командную строку JVM: `-Dwlp.server.name=yourServerName`. Замените `yourServerName` на ваше индивидуальное имя.

1. Создайте файл `.jvmprofile` в вашем регионе CICS, относящемся к CICS JVMSERVER, который выполняет WebSphere Liberty, или отредактируйте существующий файл.
2. Скопируйте аргумент JVM из вашей среды Dynatrace и вставьте его в файл `.jvmprofile`:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
3. Добавьте функцию `monitor-1.0` в `featureManager` в файле `server.xml` для сбора дополнительных метрик, таких как пулы соединений или пулы потоков:

   ```
   <server>


   <featureManager>


   <feature>monitor-1.0</feature>


   </featureManager>


   </server>
   ```
4. Сохраните изменения и перезапустите WebSphere Liberty.

* Мониторинг как региона CICS, так и WebSphere Liberty, работающего внутри этого региона CICS, поддерживается только если они отчитываются разным подсистемам zDC. Если они отчитываются разным подсистемам zDC, по крайней мере одна из этих подсистем zDC должна быть запущена как не по умолчанию (см. `SUBSYSTEM_ID` в параметрах SYSIN zDC.")). Однако обе подсистемы zDC могут отчитываться одному модулю zRemote.

  + Для модуля CICS имя подсистемы zDC определяется в параметрах SYSIN CICS.
  + Для модуля z/OS Java имя подсистемы zDC определяется в [файле `dtconfig.json`](#download).
* OneAgent версии 1.281+ Dynatrace версии 1.283+ При работе в регионе CICS имя экземпляра группы процессов будет включать как имя региона CICS, так и имя сервера WebSphere Liberty в формате `CICS region (server name)`.

### Промежуточное ПО

Вам необходимо добавить модуль z/OS Java к каждому продукту, который вы хотите мониторить.

z/OS Connect Enterprise Edition

CICS Transaction Gateway

IMS SOAP Gateway

1. Добавьте модуль в переменную `JVM_OPTIONS STDENV`:

   ```
   JVM_OPTIONS=-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
2. Необязательно. Добавьте функцию `monitor-1.0` в `featureManager` в файле `server.xml` для сбора дополнительных метрик, таких как пулы соединений или пулы потоков:

   ```
   <server>


   <featureManager>


   <feature>monitor-1.0</feature>


   </featureManager>


   </server>
   ```
3. Сохраните изменения и перезапустите z/OS Connect Enterprise Edition.
4. Для провайдера сервисов CICS активируйте функцию OneAgent **z/OS CICS z/OS Connect**.
5. Для провайдера сервисов IMS:

   1. Добавьте модуль IMS в **IMS Connect**, как описано в Установка модуля IMS.
   2. Активируйте функцию OneAgent **z/OS IMS z/OS Connect**.
6. Для провайдера сервисов MQ дополнительная настройка не требуется.

1. Добавьте модуль в член `CTGENV` и в переменную `CTGSTART_OPTS`:

   ```
   -j-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
2. Сохраните изменения и перезапустите CICS Transaction Gateway.

* Поддерживаются только протоколы EXCI и IPIC.
* Конфигурация CICS Transaction Gateway в локальном режиме WAS не поддерживается.

1. Добавьте модуль как опцию `zDT` в параметры IMS SOAP Gateway:

   ```
   zDT="-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar"
   ```

   Замените `PATH_TO` на путь к вашему JAR-файлу.
2. Экспортируйте определённую опцию `zDT`, чтобы `IBM_JAVA_OPTIONS` включала её.

   ```
   export IBM_JAVA_OPTIONS="$zDT $JAVA_OPTS"
   ```
3. Сохраните изменения и перезапустите IMS SOAP Gateway.

## Логирование

По умолчанию логирование для модуля z/OS Java отключено. Чтобы включить логирование, добавьте одну из следующих опций к аргументу JVM:

При необходимости вы можете вести логи в несколько мест. Например:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-stdout=true,log-file=true
```

При необходимости вы можете настроить файловое логирование с помощью следующих опций:

При изменении папки по умолчанию убедитесь, что сервер приложений имеет соответствующие права на запись в папку, в которой модуль должен записывать файлы логов.

### Диагностика OneAgent

Dynatrace рекомендует записывать логи в общую папку логов zDC, чтобы они были включены в рабочий процесс диагностики OneAgent. Например, если бинарный файл `dtzagent` расположен по пути `/u/dt/agent/lib64/dtzagent` в среде USS z/OS, папка логов — `/u/dt/log`. Обычно общая папка логов zDC уже существует и содержит некоторые логи zDC.

Чтобы включить файловое логирование по абсолютному пути, такому как общая папка логов zDC `/u/dt/log`, укажите аргумент JVM следующим образом:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-file=true,log-file-dir=/u/dt/log
```

Если ваш zDC установлен в другом месте, вы должны адаптировать абсолютный путь к общей папке логов zDC.

## Обновление

Чтобы обновить модуль z/OS Java до более новой версии

1. Загрузите наборы данных продукта z/OS и перенесите JAR-файл (`dynatrace-oneagent-zos-java.jar`) в среду USS z/OS в бинарном режиме.
2. Найдите существующий dtconfig.json в папке USS z/OS, где расположена старая версия модуля, и скопируйте его в папку USS z/OS, которую вы использовали на шаге (1).
3. Остановите мониторируемый сервер приложений или промежуточное ПО.
4. Замените текущий JAR-файл на новый JAR-файл.
5. Запустите сервер приложений или промежуточное ПО.

## Часто задаваемые вопросы

Как включить программный контроль для модуля z/OS Java?

Если после запуска сервера приложений на z/OS вы видите сообщения **Not Marked Program Controlled** или ошибки с кодом возврата 139:

```
BPXP015I HFS PROGRAM /tmp/libdynatrace-oneagent-odin-java5848811742465559217.so


IS NOT MARKED PROGRAM CONTROLLED.
```

Вам необходимо включить программный контроль для модуля z/OS Java. Для этого

1. Распакуйте загруженный `dynatrace-oneagent-zos-java.jar` в папку с программным контролем.
2. Отметьте соответствующий файл `.so` (32 или 64 бит) в каталоге `lib/zos-s390/` как программно-контролируемый.

   * Перейдите в каталог, содержащий файлы `.so`.
   * Выполните следующую команду, используя 32- или 64-битный файл:

     ```
     extattr +p libdynatrace-oneagent-odin-java_64.so
     ```
3. Добавьте `zos-native-library-override` к вашему аргументу JVM.

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=zos-native-library-override=<PATH_TO_SO>/libdynatrace-oneagent-odin-java_64.so
   ```

   Где:

   * `<PATH_TO>` — путь к вашему JAR-файлу.
   * `<PATH_TO_SO>` — абсолютный путь к файлу `.so`, который вы хотите контролировать.
4. Перезапустите сервер приложений.

Можно ли отключить сенсоры модуля z/OS Java?

По умолчанию все сенсоры модуля z/OS Java включены. В случае проблем вы можете отключить конкретные сенсоры, установив их значение в `false` в файле `dtconfig.json`.

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
