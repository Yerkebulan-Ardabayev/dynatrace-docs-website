---
title: Изображение Native GraalVM
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/graalvm-native-image
scraped: 2026-03-06T21:17:41.068826
---

# GraalVM Native Image


* Latest Dynatrace
* 8 мин. чтения

OneAgent версии 1.295+ Dynatrace версии 1.295+

[GraalVM Native Image](https://www.graalvm.org/latest/docs/getting-started/) предназначен для достижения высокой производительности при запуске приложений, написанных на Java и других языках, путём предварительной компиляции Java-кода в нативные образы. AOT-компилированные нативные образы содержат только Java-код, необходимый во время выполнения, и исключают всё остальное из библиотек и фреймворков.

Dynatrace обеспечивает сквозную распределённую трассировку для ваших нативных Java-приложений, предварительно скомпилированных как GraalVM Native Image, работающих в виртуализированных, контейнеризированных и Kubernetes-средах. Dynatrace автоматически обнаруживает сервисы ваших нативных Java-приложений и визуализирует их зависимости — от веб-сайта до контейнеров, инфраструктуры и облака. Система диагностирует аномалии в реальном времени с помощью ИИ и определяет первопричину вплоть до неработающего кода. Метрики производительности дают представление об использовании памяти, сборке мусора и потоках.

Поддерживаемые технологии распределённой трассировки описаны в разделе [Java Native Image](../../../technology-support.md#java-native-image "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

Для наблюдаемости GraalVM Native Image в Dynatrace требуется лицензия Full-Stack Monitoring.

## Начало работы

Модуль GraalVM Native Image от Dynatrace состоит из **модуля времени сборки** и **модуля времени выполнения**. Модуль времени сборки должен присутствовать при сборке Native Image. Модуль времени выполнения должен присутствовать при выполнении Native Image для сбора телеметрических данных.

* Оба модуля должны быть одной версии для обеспечения совместимости.
* Версия среды Dynatrace должна быть равна или новее версии модулей GraalVM Native.
* Изменения в коде вашего приложения не требуются.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Интегрируйте Dynatrace в ваш проект**](graalvm-native-image.md#integration "Установка, настройка и управление модулем GraalVM Native Image от Dynatrace.")[![Шаг 2 необязательный](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 необязательный")

**Активируйте наблюдаемость Dynatrace**](graalvm-native-image.md#activate "Установка, настройка и управление модулем GraalVM Native Image от Dynatrace.")

### Шаг 1. Интегрируйте Dynatrace в ваш проект

#### Проекты Maven

Для интеграции Dynatrace в проект Maven:

1. Добавьте следующее в ваш файл `pom.xml`:

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

   Замените `ENVIRONMENT_URL` и `API_TOKEN` в соответствии с вашей средой Dynatrace:

   * `ENVIRONMENT_URL` — это URL-адрес вашей среды мониторинга Dynatrace.
   * `API_TOKEN` — это ваш токен доступа, который, например, можно предоставить через переменную окружения с помощью `<apiToken>${env.DT_API_TOKEN}</apiToken>`. Этот токен доступа требует области видимости **PaaS integration - Installer download**. Чтобы узнать, как сгенерировать токен, см. [Создание токена доступа](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Описание концепции токена доступа и его областей видимости.").

   Это автоматически загрузит и использует последнюю версию модуля GraalVM Native Image, доступную в вашей среде. Чтобы использовать конкретную версию модуля GraalVM Native Image, добавьте `<agentVersion>AGENT_VERSION</agentVersion>` в конфигурацию `agentDownload`.

   Также вы можете [вручную загрузить модуль GraalVM Native Image](graalvm-native-image.md#manual-agent-download "Установка, настройка и управление модулем GraalVM Native Image от Dynatrace.") и использовать

   ```
   <configuration>


   <agentZip>PATH_TO_DOWNLOADED_ZIP</agentZip>


   </configuration>
   ```

   для настройки плагина Dynatrace. Замените `PATH_TO_DOWNLOADED_ZIP` абсолютным или относительным путём к загруженному ZIP-файлу.
2. Выполните `mvnw package -Pnative -Pdynatrace-native`. Это сгенерирует Native Image, включающий Dynatrace. Профиль `native` добавляет [плагин Maven для сборки GraalVM Native Image](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-registering-plugin).

   Как правило, полученный Native Image будет доступен в папке `target`. Помимо Native Image, там будет папка `dynatrace`. Она необходима для мониторинга во время выполнения. Если вы хотите запустить Native Image на другой машине, скопируйте папку `dynatrace` вместе с Native Image.

#### Проекты Gradle

Предварительные требования

* Gradle 8.4+, работающий на поддерживаемой [JVM](../../../technology-support.md#java "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") или [Native Image](../../../technology-support.md#java-native-image "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") Java версии 17+.
* Плагин Gradle `org.graalvm.buildtools:native-gradle-plugin` версии 0.10+ подключён к вашему проекту.

Для интеграции Dynatrace в проект Gradle:

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

   Замените `ENVIRONMENT_URL` и `API_TOKEN` в соответствии с вашей средой Dynatrace:

   * `ENVIRONMENT_URL` — это URL-адрес вашей среды мониторинга Dynatrace.
   * `API_TOKEN` — это ваш токен доступа, который, например, можно предоставить через переменную окружения с помощью `System.getenv("DT_API_TOKEN")`. Этот токен доступа требует области видимости **PaaS integration - Installer download**. Чтобы узнать, как сгенерировать токен, см. [Создание токена доступа](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Описание концепции токена доступа и его областей видимости.").

   Это автоматически загрузит и использует последнюю версию модуля GraalVM Native Image, доступную в вашей среде. Чтобы использовать конкретную версию модуля GraalVM Native Image, добавьте `agentVersion = "AGENT_VERSION"` в конфигурацию `agentDownload`.

   Также вы можете [вручную загрузить модуль GraalVM Native Image](graalvm-native-image.md#manual-agent-download "Установка, настройка и управление модулем GraalVM Native Image от Dynatrace.") и использовать

   ```
   dynatrace {


   agentZip = "PATH_TO_DOWNLOADED_ZIP"


   }
   ```

   для настройки плагина Dynatrace. Замените `PATH_TO_DOWNLOADED_ZIP` абсолютным или относительным путём к загруженному ZIP-файлу.
3. Выполните `gradlew dynatraceNativeCompile` для генерации Native Image, включающего Dynatrace.

   Как правило, полученный Native Image доступен в папке `build/native/nativeCompile`. Помимо Native Image, папка содержит каталог `dynatrace`. Он необходим для мониторинга во время выполнения. Если вы хотите запустить Native Image на другой машине, скопируйте папку `dynatrace` вместе с Native Image.

#### Ручная загрузка модуля GraalVM Native Image

Вы также можете вручную загрузить модуль GraalVM Native Image через Dynatrace OneAgent Deployment API для вашей целевой платформы.

Пример вызова API с использованием `curl`:

```
curl -X GET "$DT_TENANT_URL/api/v1/deployment/installer/agent/$OS_TYPE/paas/latest?flavor=default&arch=$ARCH&bitness=64&include=java-graal-native&skipMetadata=true" -H "accept: application/octet-stream"  -H "Authorization: Api-Token $DT_API_TOKEN" -o agent.zip
```

Замените `$DT_TENANT_URL`, `$OS_TYPE`, `$ARCH` и `$DT_API_TOKEN` значениями вашей среды Dynatrace.

* `$DT_TENANT_URL` — URL-адрес вашей среды Dynatrace.
* `$OS_TYPE` может быть `unix` или `windows`.
* `$ARCH` может быть `x86` или `arm`, при этом `arm` доступен только для типа ОС `unix`.
* `$DT_API_TOKEN` — ваш токен доступа с областью видимости **PaaS integration - Installer download**. Чтобы узнать, как сгенерировать токен, см. [Создание токена доступа](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Описание концепции токена доступа и его областей видимости.").

### Шаг 2 (необязательный). Активируйте наблюдаемость Dynatrace

Если у вас уже установлен OneAgent или вы используете Dynatrace Operator для Kubernetes, параметры подключения Dynatrace применяются автоматически, и наблюдаемость GraalVM Native Image активируется.

Для активации наблюдаемости Dynatrace во время выполнения определите параметры подключения Dynatrace с помощью переменных окружения `DT_TENANT`, `DT_TENANTTOKEN` и `DT_CONNECTION_POINT`. Пример для Dynatrace:

```
export DT_TENANT=$DT_TENANT_ID


export DT_TENANTTOKEN=$DT_TENANTTOKEN


export DT_CONNECTION_POINT=$DT_CONNECTION_POINT


./$YOUR_APP_NAME
```

Замените `$DT_TENANT_ID`, `$DT_TENANTTOKEN` и `$DT_CONNECTION_POINT` вашими параметрами подключения к Dynatrace. Замените `$YOUR_APP_NAME` именем вашего приложения.

Вы можете получить параметры подключения через вызов API Просмотр информации о подключении OneAgent. Вам потребуются следующие поля ответа:

* **tenantUUID** для `$DT_TENANT_ID`
* **tenantToken** для `$DT_TENANTTOKEN`
* **communicationEndpoints** для `$DT_CONNECTION_POINT`

## Настройка плагина

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

Вы можете настроить следующие свойства:

* `agentDownload` используется для настройки автоматической загрузки модуля GraalVM Native Image:

  + `environmentUrl` указывает URL-адрес вашей среды мониторинга Dynatrace.
  + `apiToken` указывает токен доступа с областью видимости **PaaS integration - Installer download**. Чтобы узнать, как сгенерировать токен, см. [Создание токена доступа](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Описание концепции токена доступа и его областей видимости.").
  + `agentVersion` указывает версию модуля GraalVM Native Image. Если не задано, используется последняя версия модуля.
* `agentZip` задаёт абсолютный или относительный путь к вручную загруженному ZIP-файлу.
* `agentOptions` определяет параметры модуля времени сборки Dynatrace (необязательно).

Доступны следующие `agentOptions`:

* `loglevelcon` задаёт уровень журналирования в консоль. Возможные значения: `off` (по умолчанию), `severe`, `warning` и `info`.
* `agentconfigpath` задаёт абсолютный путь к JSON-файлу конфигурации (см. следующий раздел).

### Плагин Gradle

Плагин Gradle настраивается через блок `dynatrace` в `build.gradle`. Например:

```
dynatrace {


agentDownload {


environmentUrl = System.getenv("DT_TENANT_URL")


apiToken = System.getenv("DT_API_TOKEN")


}


agentOptions="loglevelcon=info"


}
```

Вы можете настроить следующие свойства:

* `agentDownload` используется для настройки автоматической загрузки модуля GraalVM Native Image:

  + `environmentUrl` указывает URL-адрес вашей среды мониторинга Dynatrace.
  + `apiToken` указывает токен доступа с областью видимости **PaaS integration - Installer download**. Чтобы узнать, как сгенерировать токен, см. [Создание токена доступа](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#create-api-token "Описание концепции токена доступа и его областей видимости.").
  + `agentVersion` указывает версию модуля GraalVM Native Image. Если не задано, используется последняя версия модуля.
* `agentZip` задаёт абсолютный или относительный путь к вручную загруженному ZIP-файлу.
* `agentOptions` определяет параметры модуля времени сборки Dynatrace (необязательно).

Доступны следующие `agentOptions`:

* `loglevelcon` задаёт уровень журналирования в консоль. Возможные значения: `off` (по умолчанию), `severe`, `warning` и `info`.
* `agentconfigpath` задаёт абсолютный путь к JSON-файлу конфигурации (см. следующий раздел).

## Настройка модуля GraalVM Native Image

### Модуль времени сборки

Модуль времени сборки Dynatrace предварительно настроен с рекомендуемыми параметрами. При необходимости вы можете переопределить значения по умолчанию через JSON-файл конфигурации на этапе сборки. Например:

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

Удалите сенсор из списка `enabledSensors`, чтобы деактивировать его.

### Модуль времени выполнения

#### Режим FIPS

Режим FIPS отключён по умолчанию. Чтобы включить режим FIPS для модуля времени выполнения, удалите файл `agent/dt_fips_disabled.flag` в папке `dynatrace` рядом с Native Image.

## Известные ограничения

### Ограниченный набор функций модуля GraalVM Native Image

Модуль GraalVM Native Image не обладает всеми функциями обычного Java-модуля. Технологии, поддерживаемые модулем GraalVM Native Image, можно найти в разделе [Java Native Image](../../../technology-support.md#java-native-image "Технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.") на странице технической поддержки.

Кроме того, модуль GraalVM Native Image в настоящее время не поддерживает:

* Application Security, включая анализ уязвимостей во время выполнения и защиту приложений во время выполнения
* Обновления в реальном времени для Java-сервисов
* Профилирование CPU
* Профилирование памяти
* Анализ дампов памяти
* Встроенные метрики — ограниченная поддержка; метрики времени приостановки не передаются

### Spring RestTemplate

Ожидается, что это больше не будет необходимо в GraalVM версий 17.0.12+, 21.0.4+ и 22.0.2+.

Если вы используете Spring RestTemplate и получаете несвязанные трассировки, попробуйте следующий обходной путь.

#### Проекты Maven

Настройте в вашем файле `pom.xml`:

```
<jvmArgs>


<arg>--add-opens=java.base/sun.net.www.protocol.http=ALL-UNNAMED</arg>


<arg>--add-opens=java.base/java.net=ALL-UNNAMED</arg>


<arg>--add-exports=java.base/sun.net.www=ALL-UNNAMED</arg>


</jvmArgs>
```

Для справки см. [плагин Maven для сборки GraalVM Native Image](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-options).

#### Проекты Gradle

Настройте в вашем файле `build.gradle`:

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