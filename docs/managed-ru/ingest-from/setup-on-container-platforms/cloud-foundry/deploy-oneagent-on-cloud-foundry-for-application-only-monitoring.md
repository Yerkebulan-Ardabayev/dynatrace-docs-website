---
title: Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring
scraped: 2026-05-12T11:09:23.289014
---

# Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений

# Развёртывание OneAgent на Cloud Foundry для мониторинга только приложений

* 2-min read
* Published Jul 19, 2017

Приложения, развёрнутые на Cloud Foundry, как правило, запускаются через специфичные для технологии buildpacks, предоставляющие поддержку фреймворков и среды выполнения. Подробнее см. в разделе [как работают buildpacks](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html).

В режиме мониторинга только приложений OneAgent отслеживает потребление памяти, диска, CPU и сети процессами внутри контейнера. Метрики хоста не отслеживаются.

## Предварительные условия

* Создайте [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Концепция токена доступа и его областей видимости.").
* Ознакомьтесь с [поддерживаемыми приложениями и версиями](/managed/ingest-from/technology-support#applications-services-and-databases "Техническая информация о поддержке платформ и фреймворков в Dynatrace.").

## Развёртывание OneAgent

1. Создайте сервис Dynatrace в вашем окружении Cloud Foundry.
   Существует два способа определения экземпляра сервиса, выберите один:

   Вариант 1: Создание user-provided service

   Создайте единственный экземпляр сервиса Dynatrace, имя которого содержит подстроку `dynatrace` (как в примере ниже). Вам будет предложено ввести ID окружения и API-токен. API-токен соответствует токену, описанному выше.

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, apiurl"
   ```

   Параметр `apiurl` указывает API-эндпоинт вашего кластера Dynatrace и должен быть равен `https://<YourDynatraceClusterURL>/e/<environmentID>/api`. Этот параметр необязателен. Если он не указан, будет использован стандартный SaaS-эндпоинт. При отсутствии прямого соединения с SaaS-эндпоинтом можно использовать ActiveGate: `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/`.

   Вариант 2: Создание service instance через service broker

   Для централизованного хранения учётных данных Dynatrace используйте service broker. Подробнее см. на [GitHub](https://github.com/dynatrace-innovationlab/dynatrace-service-broker).
   Необходимо настроить и запустить broker как приложение, добавить service broker в Cloud Foundry, предоставить пользователям доступ к сервису и создать экземпляр сервиса.

2. Привяжите сервис Dynatrace к приложению.

   Привязать созданный сервис Dynatrace к приложению можно в файле `manifest.yml`. Если приложение уже запущено, необходимо выполнить restage.

   ```
   ---



   applications:



   - name: demo-helloworld



   path: target/JavaHelloWorldApp.war



   buildpack: https://github.com/cloudfoundry/java-buildpack.git



   memory: 512M



   instances: 1



   host: hello-world-${random-word}



   disk_quota: 1024M



   services:



   - dynatrace-service
   ```

3. Необязательно: настройте поток логов OneAgent по умолчанию для Cloud Foundry.

   По умолчанию логи OneAgent записываются в поток стандартных ошибок Cloud Foundry. Установите переменную окружения `DT_LOGSTREAM` в `stdout` или `stderr`.

   ```
   cf set-env APP_NAME DT_LOGSTREAM stdout
   ```

4. Необязательно: настройте адрес прокси.

   Если в окружении используется прокси, установите переменную окружения `DT_PROXY`:

   ```
   cf set-env <application> DT_PROXY <proxy address>
   ```

5. Необязательно: настройте сетевые зоны.

   Настройка сетевых зон возможна двумя способами:

   * Через `UserProvidedService`:

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, networkzone"
   ```

   * Как переменная окружения для приложения:

   ```
   cf set-env <application> DT_NETWORK_ZONE <your_network_zone>
   ```

   Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Принцип работы сетевых зон в Dynatrace.").

6. Необязательно: настройте дополнительные кодовые модули.

   Дополнительные кодовые модули можно настроить через `UserProvidedService`:

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, addtechnologies"
   ```

   Параметр `addtechnologies` принимает список через запятую (без пробелов).
   Допустимые значения см. в строке «include» раздела [параметров](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version#parameters "Загрузка установщика OneAgent конкретной версии через Dynatrace API.").

   Это необходимо для мониторинга дополнительных технологий при использовании multi-buildpack и sidecar deployment в Cloud Foundry.

   **Важно**:

   * Указание неподдерживаемых значений нарушит развёртывание, так как это напрямую влияет на инструкции загрузки.
   * Добавление кодовых модулей увеличивает требования к дисковому пространству.

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")