---
title: GraalVM Native Image
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/graalvm-native-image
scraped: 2026-05-12T11:23:48.763412
---

# GraalVM Native Image

# GraalVM Native Image

* Чтение: 8 мин
* Опубликовано 2 июля 2024 г.

OneAgent версии 1.295+ Dynatrace версии 1.295+

[GraalVM Native Image](https://www.graalvm.org/latest/docs/getting-started/) предназначен для достижения высокой производительности при запуске приложений, написанных на Java и других языках, путём предварительной компиляции Java-кода в native images. Native images, скомпилированные с помощью AOT, содержат только тот Java-код, который требуется во время выполнения, и исключают всё остальное из библиотек и фреймворков.

Dynatrace обеспечивает сквозную распределённую трассировку нативных Java-приложений, предварительно скомпилированных как GraalVM Native Image, работающих в виртуализированных, контейнеризированных средах и средах K8s. Dynatrace автоматически обнаруживает сервисы нативных Java-приложений и визуализирует их зависимости от веб-сайта до контейнеров, инфраструктуры и облака. Система диагностирует аномалии в реальном времени с помощью ИИ и определяет первопричину вплоть до неисправного кода. Метрики производительности дают представление об использовании памяти, сборке мусора и потоках.

Поддерживаемые технологии распределённой трассировки перечислены в разделе [Java Native Image](/managed/ingest-from/technology-support#java-native-image "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").

Наблюдаемость Dynatrace GraalVM Native Image требует лицензии [Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Узнайте, как рассчитывается потребление возможности Full-Stack Monitoring DPS в Dynatrace.").

## Начало работы

Модуль Dynatrace GraalVM Native Image состоит из **модуля времени сборки** и **модуля времени выполнения**. Модуль времени сборки должен присутствовать во время сборки Native Image. Модуль времени выполнения должен присутствовать при выполнении Native Image для сбора телеметрических данных.

* Оба модуля должны быть одной версии из соображений совместимости.
* Версия среды Dynatrace должна быть равна версии модулей GraalVM Native или превышать её.
* Изменения в коде приложения не требуются.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Интегрируйте Dynatrace в свой проект**](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image#integration "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.")[![Шаг 2 (необязательно)](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 (необязательно)")

**Активируйте наблюдаемость Dynatrace**](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image#activate "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.")

### Шаг 1: интеграция Dynatrace в проект

#### Проекты Maven

Чтобы интегрировать Dynatrace в проект Maven:

1. Добавьте следующее в файл `pom.xml`:

   ```
   <profile>



   <id>dynatrace-native</id>



   <build>



   <plugins>



   <plugin>



   <groupId>com.dynatrace.buildtools.graalnative</groupId>



   <artifactId>dynatrace-native-maven-plugin</artifactId>



   <version>2.1.0</version>



   <executions>



   <execution>



   <goals>



   <goal>setup-build-agent</goal>



   <goal>copy-runtime-agent</goal>



   </goals>



   <configuration>



   <agentDownload>



   <environmentUrl>ENVIRONMENT_URL</environmentUrl>



   <apiToken>API_TOKEN</apiToken>



   </agentDownload>



   </configuration>



   </execution>



   </executions>



   <extensions>true</extensions>



   </plugin>



   </plugins>



   </build>



   </profile>
   ```

   Замените `ENVIRONMENT_URL` и `API_TOKEN` в соответствии с настройками вашей среды Dynatrace:

   * `ENVIRONMENT_URL`: URL среды Dynatrace вашей [среды мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о среде мониторинга и работе с ней.").
   * `API_TOKEN`: токен доступа, который можно передать, например, через переменную среды: `<apiToken>${env.DT_API_TOKEN}</apiToken>`. Токен доступа должен иметь область действия **PaaS integration - Installer download**. Сведения о создании токена: [Создать токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Общие сведения о токенах доступа и их областях действия.").

   Будет автоматически загружена и использована последняя версия модуля GraalVM Native Image, доступная в вашей среде. Чтобы использовать конкретную версию модуля GraalVM Native Image, добавьте `<agentVersion>AGENT_VERSION</agentVersion>` в конфигурацию `agentDownload`.

   Кроме того, можно [вручную загрузить модуль GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.") и использовать

   ```
   <configuration>



   <agentZip>PATH_TO_DOWNLOADED_ZIP</agentZip>



   </configuration>
   ```

   для настройки плагина Dynatrace. Замените `PATH_TO_DOWNLOADED_ZIP` абсолютным или относительным путём к загруженному ZIP-файлу.
2. Запустите `mvnw package -Pnative -Pdynatrace-native`. Будет создан Native Image, включающий Dynatrace. Профиль `native` добавляет [Maven-плагин для сборки GraalVM Native Image](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-registering-plugin).

   Как правило, полученный Native Image будет доступен в папке `target`. Помимо Native Image, там будет папка `dynatrace`. Она необходима для мониторинга во время выполнения. Если нужно запустить Native Image на другой машине, скопируйте папку `dynatrace` вместе с Native Image.

#### Проекты Gradle

Предварительные требования

* Gradle 8.4+ работает на поддерживаемой [JVM](/managed/ingest-from/technology-support#java "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") или [Native Image](/managed/ingest-from/technology-support#java-native-image "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") Java версии 17+.
* К проекту применён плагин Gradle `org.graalvm.buildtools:native-gradle-plugin` версии 0.10+.

Чтобы интегрировать Dynatrace в проект Gradle:

1. Добавьте следующий код в `settings.gradle`:

   ```
   pluginManagement {



   repositories {



   mavenCentral()



   }



   }
   ```
2. Добавьте следующий код в `build.gradle`:

   ```
   plugins {



   id 'com.dynatrace.buildtools.graalnative' version '2.1.0'



   }



   dynatrace {



   agentDownload {



   environmentUrl = "ENVIRONMENT_URL"



   apiToken = "API_TOKEN"



   }



   }
   ```

   Замените `ENVIRONMENT_URL` и `API_TOKEN` в соответствии с настройками вашей среды Dynatrace:

   * `ENVIRONMENT_URL`: URL среды Dynatrace вашей [среды мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о среде мониторинга и работе с ней.").
   * `API_TOKEN`: токен доступа, который можно передать, например, через переменную среды: `System.getenv("DT_API_TOKEN")`. Токен доступа должен иметь область действия **PaaS integration - Installer download**. Сведения о создании токена: [Создать токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Общие сведения о токенах доступа и их областях действия.").

   Будет автоматически загружена и использована последняя версия модуля GraalVM Native Image, доступная в вашей среде. Чтобы использовать конкретную версию модуля GraalVM Native Image, добавьте `agentVersion = "AGENT_VERSION"` в конфигурацию `agentDownload`.

   Кроме того, можно [вручную загрузить модуль GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Установка, настройка и управление модулем Dynatrace GraalVM Native Image.") и использовать

   ```
   dynatrace {



   agentZip = "PATH_TO_DOWNLOADED_ZIP"



   }
   ```

   для настройки плагина Dynatrace. Замените `PATH_TO_DOWNLOADED_ZIP` абсолютным или относительным путём к загруженному ZIP-файлу.
3. Запустите `gradlew dynatraceNativeCompile` для создания Native Image с включением Dynatrace.

   Как правило, полученный Native Image доступен в папке `build/native/nativeCompile`. Помимо Native Image, папка содержит папку `dynatrace`. Она необходима для мониторинга во время выполнения. Если нужно запустить Native Image на другой машине, скопируйте папку `dynatrace` вместе с Native Image.

#### Загрузка модуля GraalVM Native Image вручную

Модуль GraalVM Native Image также можно вручную загрузить из [Dynatrace OneAgent Deployment API](/managed/dynatrace-api/environment-api/deployment/oneagent "Загрузка установщиков OneAgent через Dynatrace API.") для целевой платформы.

Пример вызова API с помощью `curl`:

```
curl -X GET "$DT_TENANT_URL/api/v1/deployment/installer/agent/$OS_TYPE/paas/latest?flavor=default&arch=$ARCH&bitness=64&include=java-graal-native&skipMetadata=true" -H "accept: application/octet-stream"  -H "Authorization: Api-Token $DT_API_TOKEN" -o agent.zip
```

Замените `$DT_TENANT_URL`, `$OS_TYPE`, `$ARCH` и `$DT_API_TOKEN` значениями вашей среды Dynatrace.

* `$DT_TENANT_URL`: URL вашей среды Dynatrace.
* `$OS_TYPE` может принимать значение `unix` или `windows`.
* `$ARCH` может принимать значение `x86` или `arm`; при этом `arm` доступен только для типа ОС `unix`.
* `$DT_API_TOKEN`: токен доступа с областью действия **PaaS integration - Installer download**. Сведения о создании токена: [Создать токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Общие сведения о токенах доступа и их областях действия.").

### Шаг 2 (необязательно): активация наблюдаемости Dynatrace

Если OneAgent уже установлен или используется Dynatrace Operator для Kubernetes, сведения о подключении Dynatrace применяются автоматически и наблюдаемость GraalVM Native Image активируется.

Для активации наблюдаемости Dynatrace во время выполнения определите сведения о подключении Dynatrace с помощью переменных среды `DT_TENANT`, `DT_TENANTTOKEN` и `DT_CONNECTION_POINT`. Пример для Dynatrace SaaS:

```
export DT_TENANT=$DT_TENANT_ID



export DT_TENANTTOKEN=$DT_TENANTTOKEN



export DT_CONNECTION_POINT=$DT_CONNECTION_POINT



./$YOUR_APP_NAME
```

Замените `$DT_TENANT_ID`, `$DT_TENANTTOKEN` и `$DT_CONNECTION_POINT` сведениями о подключении к вашей среде Dynatrace. Замените `$YOUR_APP_NAME` именем вашего приложения.

Сведения о подключении можно получить с помощью вызова API [Просмотр информации о подключении OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "Просмотр информации о подключении OneAgent через Dynatrace API."). Необходимы следующие поля ответа:

* **tenantUUID** для `$DT_TENANT_ID`
* **tenantToken** для `$DT_TENANTTOKEN`
* **communicationEndpoints** для `$DT_CONNECTION_POINT`

## Конфигурация плагина

### Плагин Maven

Плагин Maven настраивается через профиль `dynatrace-native` в файле `pom.xml`. Например:

```
<configuration>



<agentDownload>



<environmentUrl>${env.DT_TENANT_URL}</environmentUrl>



<apiToken>${env.DT_API_TOKEN}</apiToken>



</agentDownload>



<agentOptions>loglevelcon=info</agentOptions>



</configuration>
```

Доступны следующие свойства для настройки:

* `agentDownload` используется для настройки автоматической загрузки модуля GraalVM Native Image:

  + `environmentUrl`: URL среды Dynatrace вашей [среды мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о среде мониторинга и работе с ней.").
  + `apiToken`: токен доступа с областью действия **PaaS integration - Installer download**. Сведения о создании токена: [Создать токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Общие сведения о токенах доступа и их областях действия.").
  + `agentVersion`: версия модуля GraalVM Native Image. Если не задано, используется последняя доступная версия.
* `agentZip`: абсолютный или относительный путь к вручную загруженному ZIP-файлу.
* `agentOptions`: параметры для модуля Dynatrace времени сборки (необязательно).

Доступны следующие параметры `agentOptions`:

* `loglevelcon` задаёт уровень ведения журнала консоли. Возможные значения: `off` (по умолчанию), `severe`, `warning` и `info`.
* `agentconfigpath` задаёт абсолютный путь к конфигурационному файлу JSON (см. следующий раздел).

### Плагин Gradle

Плагин Gradle настраивается через блок `dynatrace` в файле `build.gradle`. Например:

```
dynatrace {



agentDownload {



environmentUrl = System.getenv("DT_TENANT_URL")



apiToken = System.getenv("DT_API_TOKEN")



}



agentOptions="loglevelcon=info"



}
```

Доступны следующие свойства для настройки:

* `agentDownload` используется для настройки автоматической загрузки модуля GraalVM Native Image:

  + `environmentUrl`: URL среды Dynatrace вашей [среды мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Общие сведения о среде мониторинга и работе с ней.").
  + `apiToken`: токен доступа с областью действия **PaaS integration - Installer download**. Сведения о создании токена: [Создать токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Общие сведения о токенах доступа и их областях действия.").
  + `agentVersion`: версия модуля GraalVM Native Image. Если не задано, используется последняя доступная версия.
* `agentZip`: абсолютный или относительный путь к вручную загруженному ZIP-файлу.
* `agentOptions`: параметры для модуля Dynatrace времени сборки (необязательно).

Доступны следующие параметры `agentOptions`:

* `loglevelcon` задаёт уровень ведения журнала консоли. Возможные значения: `off` (по умолчанию), `severe`, `warning` и `info`.
* `agentconfigpath` задаёт абсолютный путь к конфигурационному файлу JSON (см. следующий раздел).

## Конфигурация модуля GraalVM Native Image

### Модуль времени сборки

Модуль Dynatrace времени сборки предварительно настроен с рекомендуемыми параметрами. При необходимости можно переопределить значения по умолчанию через конфигурационный файл JSON во время сборки. Например:

```
{



"enabledSensors": [



"servlet"



]



}
```

Доступны следующие `enabledSensors` (точки инструментирования):

* `servlet`: входящие HTTP-запросы через Servlet API
* `netty`: входящие HTTP-запросы через Netty
* `httpclient`: исходящие HTTP-запросы
* `threading`: распространение контекста для потоков и исполнителей
* `mongo`: вызовы базы данных MongoDB

Для деактивации датчика удалите его из списка `enabledSensors`.

### Модуль времени выполнения

#### Режим FIPS

Режим FIPS по умолчанию отключён. Для включения режима FIPS для модуля времени выполнения удалите файл `agent/dt_fips_disabled.flag` в папке `dynatrace` рядом с Native Image.

## Известные ограничения

### Ограниченный набор функций модуля GraalVM Native Image

Модуль GraalVM Native Image не обладает всеми функциями обычного модуля Java. Технологии, поддерживаемые модулем GraalVM Native Image, перечислены в разделе [Java Native Image](/managed/ingest-from/technology-support#java-native-image "Технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.") страницы поддержки технологий.

Кроме того, модуль GraalVM Native Image в настоящее время не поддерживает:

* Application Security, включая аналитику уязвимостей во время выполнения и защиту приложений во время выполнения
* обновления Java-сервисов в режиме реального времени
* профилирование CPU
* профилирование памяти
* анализ дампов памяти
* встроенные метрики: ограниченная поддержка; метрики времени приостановки не передаются

### Spring RestTemplate

Ожидается, что это ограничение станет неактуальным в GraalVM версий 17.0.12+, 21.0.4+ и 22.0.2+.

Если вы используете Spring RestTemplate и получаете несвязанные трассы, попробуйте следующее обходное решение.

#### Проекты Maven

Настройте в файле `pom.xml`:

```
<jvmArgs>



<arg>--add-opens=java.base/sun.net.www.protocol.http=ALL-UNNAMED</arg>



<arg>--add-opens=java.base/java.net=ALL-UNNAMED</arg>



<arg>--add-exports=java.base/sun.net.www=ALL-UNNAMED</arg>



</jvmArgs>
```

Для справки см. [Maven-плагин для сборки GraalVM Native Image](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-options).

#### Проекты Gradle

Настройте в файле `build.gradle`:

```
graalvmNative {



binaries {



main {



jvmArgs.addAll(



'--add-opens', 'java.base/sun.net.www.protocol.http=ALL-UNNAMED',



'--add-opens', 'java.base/java.net=ALL-UNNAMED',



'--add-exports', 'java.base/sun.net.www=ALL-UNNAMED'



)



}



}



}
```