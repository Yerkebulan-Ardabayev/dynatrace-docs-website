---
title: Анализ дампов памяти
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis
scraped: 2026-03-04T21:32:39.693962
---

Dynatrace может сохранять и анализировать дампы памяти для приложений Java, .NET и Node.js.

Дампы памяти сохраняются OneAgent локально на диске машины контролируемого сервера приложений в течение ограниченного времени.

Если настроен ActiveGate, OneAgent автоматически загружает дампы памяти на ActiveGate, который выступает в качестве центра долгосрочного хранения дампов памяти. Такой подход гарантирует, что дампы памяти доступны только пользователям, имеющим доступ к сетевому расположению вашего ActiveGate. Эта мера предосторожности обеспечивает дополнительный уровень безопасности, гарантируя, что персональные данные не покинут ваш центр обработки данных, если вы не настроите это иначе.

![Страница дампов памяти](https://dt-cdn.net/images/memory-dumps-1181-d3e7b9b87e.png)

## Прежде чем начать

* Для запуска создания дампов памяти вам необходимо разрешение пользователя [**View sensitive request data**](../../../manage/identity-access-management/permission-management/role-based-permissions.md#environment "Role-based permissions").
* Для хранения дампов памяти на сервере приложений должно быть достаточно свободного места.
* Для доступа к сохраненным дампам памяти через веб-интерфейс Dynatrace [настройте ActiveGate для хранения дампов памяти в централизованном расположении](memory-dump-analysis/configure-an-activegate-for-memory-dump-storage.md "Learn how to enable storage of memory dumps on an ActiveGate."). Подробнее о сроках хранения дампов памяти см. в разделе [Сроки хранения данных](../../../manage/data-privacy-and-security/data-privacy/data-retention-periods.md#memory-dumps "Check retention times for various data types.").

## Запуск создания дампов памяти

Чтобы запустить создание дампа памяти:

1. Перейдите на страницу **Memory dumps**:

   * На странице сущности, которую вы хотите проанализировать, выберите **More** (**...**) > **Memory dump details**.
   * Перейдите в ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Выберите процесс, который хотите проанализировать, и нажмите **Trigger new dump**, чтобы сгенерировать новый дамп памяти.
   Генерация дампа памяти занимает несколько минут. Необходимое время значительно варьируется в зависимости от типа приложения. Для приложений Java с несколькими гигабайтами heap-памяти может потребоваться несколько минут; дампы меньшего размера доступны практически сразу.

   Java

   Dynatrace использует [JVM Tool Interface (JVM TI)](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html) для генерации дампов памяти. По этой причине ваша JVM может приостановиться во время создания дампа памяти. Пожалуйста, перезапустите Java-приложение после запуска создания дампа памяти.
3. Через несколько минут обновите страницу. Только что созданный дамп появится в списке.

## Скачивание и просмотр дампов памяти

Чтобы скачать дампы памяти:

1. Перейдите на страницу **Memory dumps**:

   * На странице сущности, которую вы хотите проанализировать, выберите **More** (**...**) > **Memory dump details**.
   * Перейдите в ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Разверните запись вашего дампа памяти.
3. В списке **Download link** выберите ActiveGate, с которого вы хотите скачать дамп памяти, и нажмите **Download**.

   Если вы не можете скачать дамп памяти через интерфейс, скачайте файл вручную по локальному пути, указанному в веб-интерфейсе. Обратите внимание, что дампы памяти, хранящиеся OneAgent локально, доступны ограниченное время; когда OneAgent периодически очищает директорию, размер файла может быть 0 байт.

В случае приложений Java скачивание предоставляет дамп памяти в формате [hprof](https://dt-url.net/kh03s1r), который можно анализировать с помощью ряда инструментов, включая [Eclipse Memory analyzer](https://dt-url.net/uq23syk) и [VisualVM](https://dt-url.net/mz43sws). IBM JVM не поддерживает hprof, но имеет собственный формат IBM Portable Heap Dump (PHD). Его также можно анализировать с помощью Eclipse Memory analyzer.

Дампы памяти Node.js можно открыть во встроенном инструменте анализа снимков heap-памяти Google Chrome.

Дампы памяти .NET можно открыть в [PerfView](https://dt-url.net/fb03syb) или Visual Studio.

## Ограничения

* Дампы памяти .NET не поддерживаются в контейнерах на базе Alpine Linux.
* Загрузка дампов памяти не поддерживается ни для [мониторинга только приложений в Kubernetes](../../../ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), ни для [облачного мониторинга полного стека в Kubernetes](../../../ingest-from/setup-on-k8s/deployment/full-stack-observability.md "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes").

  Это связано с тем, что OneAgent работает в контейнере с файловой системой только для чтения (каталог двоичных файлов OneAgent `/opt/dynatrace/oneagent-paas` смонтирован в режиме только для чтения), поэтому Dynatrace не может записать необходимые файлы дампов памяти. В то же время параметр установки `DATA_STORAGE`, используемый для переопределения каталога дампов, [не поддерживается в контейнерных развертываниях](../../../ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container.md#limitations "Install and update Dynatrace OneAgent as a Docker container."). Таким образом, невозможно изменить расположение дампов на путь с правами на запись. В результате сбор дампов памяти невозможен в средах Kubernetes с мониторингом только приложений или облачным мониторингом полного стека.

## Часто задаваемые вопросы

Если я включу анализ дампов памяти на нескольких ActiveGate, какой ActiveGate выполнит создание дампа памяти?

Приоритет назначается ActiveGate автоматически. Если несколько ActiveGate имеют одинаковый приоритет, конечная точка выбирается случайным образом.

Что произойдет, если передача файла на ActiveGate завершится с ошибкой?

OneAgent пытается отправить список дампов на все доступные конечные точки, пока не найдет работающую. Этот процесс повторяется до тех пор, пока не будет успешным или пока дампы не будут удалены задачами устаревания (например, если их слишком много или они слишком старые).

Что произойдет, если на ActiveGate закончится место для дампов памяти?

ActiveGate сначала удаляет устаревшие дампы. Если устаревших дампов нет, ActiveGate удаляет сначала самые старые дампы.

Могу ли я настроить место хранения дампов памяти OneAgent?

Да. OneAgent хранит дампы памяти локально и гарантирует, что дампы не покинут вашу локальную сеть. Вы можете [настроить расположение дампов памяти](../../../ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux.md#data-storage "Learn how to use the Linux installer with command line parameters.").

Конечный пользователь не может получить доступ ни к одной из конечных точек ActiveGate. Могу ли я все-таки предоставить доступ к файлу дампа памяти?

Да. Поскольку время от времени конечная точка ActiveGate может быть недоступна для конечного пользователя, ActiveGate могут иметь несколько IP-адресов, а значит, несколько конечных точек. Если все существующие конечные точки одновременно недоступны для конечного пользователя, вы все равно можете предоставить доступ к файлу дампа памяти.

* Вы можете включить удаленный доступ к ActiveGate, изменив публичные конечные точки.
  Чтобы узнать, как настроить новую конечную точку, см.:

  + [Включение модуля дампов памяти](../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md#mem_dump_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.")
  + [Настройка ActiveGate для хранения дампов памяти](memory-dump-analysis/configure-an-activegate-for-memory-dump-storage.md "Learn how to enable storage of memory dumps on an ActiveGate.")
* Если удаленный доступ к ActiveGate невозможен, вы можете скачать файл дампа памяти вручную с хоста ActiveGate.

  + Для доступа к хосту ActiveGate используйте протокол, позволяющий передавать файлы (например, sFTP или SSH).
  + Чтобы скачать файл дампа памяти, вам необходимо [узнать расположение файла](memory-dump-analysis/configure-an-activegate-for-memory-dump-storage.md#specify-dedicated-dump-directory "Learn how to enable storage of memory dumps on an ActiveGate.").
  + Чтобы идентифицировать дамп памяти, распакуйте его файл через протокол, включающий `summary.json` (например, sFTP или SSH).

## Связанные темы

* [Dynatrace ActiveGate](../../../ingest-from/dynatrace-activegate.md "Understand the basic concepts related to ActiveGate.")
* [Разрешения на основе ролей](../../../manage/identity-access-management/permission-management/role-based-permissions.md "Role-based permissions")