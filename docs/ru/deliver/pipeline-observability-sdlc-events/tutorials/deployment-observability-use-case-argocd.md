---
title: Наблюдение за развертыванием Argo CD и работоспособностью приложений с помощью Dashboards и событий SDLC
source: https://www.dynatrace.com/docs/deliver/pipeline-observability-sdlc-events/tutorials/deployment-observability-use-case-argocd
scraped: 2026-03-03T21:24:45.170541
---

# Наблюдение за развёртыванием Argo CD и состоянием приложений с помощью дашбордов и событий SDLC


* Latest Dynatrace
* Руководство
* Чтение: 7 мин
* Обновлено 23 июня 2025 г.
* Предварительный просмотр

В этом сценарии вы

* Интегрируете [Argo CD](https://argo-cd.readthedocs.io/en/stable) и Dynatrace.
* Используете дашборды для наблюдения за развёртываниями Argo CD и состоянием приложений.
* Используете эту информацию для оптимизации развёртываний с помощью Argo CD.

Ниже показан пример того, как может выглядеть ваш дашборд Argo CD.

![Снимок экрана жизненного цикла приложения Dynatrace ArgoCD.](https://dt-cdn.net/images/argocd-sync-deployment-overview-2892-ac512e11e1.png)

## Концепции

События жизненного цикла разработки программного обеспечения (SDLC)
:   [События SDLC](../../pipeline-observability-sdlc-events.md#sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.")

Почему уведомления Argo CD были преобразованы в события SDLC?
:   Основные преимущества — нормализация данных, независимость от инструментов и отсутствие привязки к конкретным инструментам.
    В результате дашборды Dynatrace, приложения и рабочие процессы могут опираться на [события SDLC](../../pipeline-observability-sdlc-events.md#sdlc-events "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.") с чётко определёнными свойствами, а не на специфику отдельных инструментов.

## Целевая аудитория

Это руководство предназначено для платформенных инженеров, которые управляют внутренней платформой разработки (IDP), включая Argo CD, в развёртываниях на основе GitOps.

## Результат обучения

В этом руководстве вы узнаете, как

* Перенаправлять уведомления Argo CD в Dynatrace.
* Отправлять метрики Prometheus в Dynatrace.
* Нормализовать загруженные данные событий.
* Использовать дашборды для анализа данных и выявления улучшений.

При желании вы можете следовать [руководству по Argo CD непосредственно на GitHub](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples/blob/main/argocd_observability/README.md).

## Предварительные требования

[Установка Dynatrace Configuration as Code через Monaco](../../configuration-as-code/monaco/installation.md "Download and install Dynatrace Configuration as Code via Monaco.")

## Инструкция

1. Подготовка: настройка конфигурации Monaco

1. [Создайте OAuth-клиент для Dynatrace Monaco CLI](../../configuration-as-code/monaco/guides/create-oauth-client.md "Create an OAuth client for Dynatrace Configuration as Code via Monaco.") со следующими разрешениями

   * Запуск приложений: `app-engine:apps:run`
   * Просмотр конфигураций OpenPipeline: `openpipeline:configurations:read`
   * Редактирование конфигураций OpenPipeline: `openpipeline:configurations:write`
   * Создание и редактирование документов: `document:documents:write`
   * Просмотр документов: `document:documents:read`
2. Сохраните полученные идентификатор клиента и секрет как отдельные переменные окружения.

   Windows

   Linux

   `$env:OAUTH_CLIENT_ID='<YOUR_CLIENT_ID>'`

   `$env:OAUTH_CLIENT_SECRET='<YOUR_CLIENT_SECRET>'`

   `export OAUTH_CLIENT_ID='<YOUR_CLIENT_ID>'`

   `export OAUTH_CLIENT_SECRET='<YOUR_CLIENT_SECRET>'`
3. Клонируйте репозиторий [примеров конфигурации Dynatrace as code](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples) и перейдите в директорию `argocd_observability`.

   ```
   git clone https://github.com/Dynatrace/dynatrace-configuration-as-code-samples.git


   cd dynatrace-configuration-as-code-samples/argocd_observability
   ```
4. Отредактируйте `manifest.yaml`, заменив плейсхолдер `<YOUR-DT-ENV-ID>` на идентификатор вашей среды Dynatrace в свойстве name и в URL свойства value.

   ```
   manifestVersion: 1.0


   projects:


   - name: pipeline_observability


   environmentGroups:


   - name: group


   environments:


   - name: <YOUR-DT-ENV-ID>


   url:


   type: value


   value: https://<YOUR-DT-ENV-ID>.apps.dynatrace.com


   auth:


   oAuth:


   clientId:


   name: OAUTH_CLIENT_ID


   clientSecret:


   name: OAUTH_CLIENT_SECRET
   ```

2. Подготовка: проверка конфигурации OpenPipeline для событий SDLC

Эти шаги изменяют конфигурацию OpenPipeline для [событий SDLC](../sdlc-events.md "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.").
Если ваша конфигурация OpenPipeline содержит только значения по умолчанию/встроенные значения, вы можете непосредственно применить конфигурацию Monaco.
Если у вас есть пользовательские источники загрузки, динамические маршруты или пайплайны, вам сначала нужно скачать вашу конфигурацию и вручную объединить её с конфигурацией Monaco.

Шаг 3 покажет, требуется ли объединение конфигураций, или вы можете напрямую применить предоставленную конфигурацию.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Events** > **Software development lifecycle**.
2. Проверьте **Ingest sources**, **Dynamic routing** и **Pipelines**.

   * В разделе **Ingest sources** есть ли другие источники, кроме **Default API**?
   * В разделе **Dynamic routing** есть ли другие маршруты, кроме **Default route**?
   * В разделе **Pipelines** есть ли другие пайплайны, кроме **events.sdlc**?
3. Если ответ на один из этих вопросов «да», выполните шаги ниже. В противном случае перейдите к шагу 4.

   * Скачайте конфигурацию OpenPipeline.

     `monaco download -e <YOUR-DT-ENV-ID> --only-openpipeline`
   * Откройте следующие файлы:

     + Ваш скачанный файл конфигурации, `download_<DATE>_<NUMBER>/project/openpipline/events.sdlc.json`.
     + Предоставленный файл конфигурации, `pipeline_observability/openpipline/events.sdlc.argocd.json`.
   * Объедините содержимое `events.sdlc.json` в `events.sdlc.argocd.json`, а затем сохраните файл.
4. Примените конфигурацию Monaco.

   Конфигурация состоит из

   * Дашбордов для анализа активности Argo CD.
   * Конфигурации OpenPipeline для нормализации [уведомлений Argo CD](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/) в [события SDLC](../sdlc-events.md "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.").

   Выполните эту команду для применения предоставленной конфигурации Monaco:

   `monaco deploy manifest.yaml`

3. Подготовка: создание токена доступа

Для генерации токена доступа:

1. Перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Выберите **Generate new token**.
3. Введите имя для вашего токена.
   Dynatrace не требует уникальности имён токенов. Вы можете создавать несколько токенов с одинаковым именем. Убедитесь, что вы даёте осмысленное имя каждому создаваемому токену. Правильные имена помогут вам эффективно управлять токенами и, при необходимости, удалять их.
4. Выберите необходимые области действия для токена.
5. Выберите **Generate token**.
6. Скопируйте сгенерированный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.

   Вы можете получить доступ к токену только один раз при создании. После этого его нельзя будет отобразить снова.

7. Выберите эти области действия:

   * **OpenPipeline - Ingest Software Development Lifecycle Events (Built-in) (`openpipeline.events_sdlc`)**
   * **OpenPipeline - Ingest Software Development Lifecycle Events (Custom) (`openpipeline.events_sdlc.custom`)**

4. Подготовка: настройка уведомлений Argo CD

[Уведомления Argo CD](https://argo-cd.readthedocs.io/en/stable/operator-manual/notifications/) предоставляют гибкий способ оповещения пользователей о важных изменениях в состоянии приложений, управляемых Argo CD. Для настройки уведомлений Argo CD необходимо создать секрет уведомлений, применить конфигурацию и подписать приложения на уведомления.

1. Создание секрета уведомлений.

   1. Обновите `argocd-notifications-secret` следующим содержимым:

      ```
      apiVersion: v1


      kind: Secret


      metadata:


      name: argocd-notifications-secret


      stringData:


      dt-base-url: https://{your-environment-id}.live.dynatrace.com


      dt-access-token: <YOUR-ACCESS-TOKEN>
      ```
   2. Примените конфигурацию.

      `kubectl apply -f <secret_file_name>.yaml -n argocd`
2. Создание шаблона и триггера уведомлений.

   1. Если у вас нет конфигураций уведомлений, создайте новую карту конфигурации с именем `argocd-notification-cm`, как показано ниже. В противном случае расширьте вашу карту конфигурации, добавив секции service, template и trigger из примера.

      ```
      apiVersion: v1


      kind: ConfigMap


      metadata:


      name: argocd-notifications-cm


      data:


      service.webhook.dynatrace-webhook: |


      url: $dt-base-url


      headers:


      - name: "Authorization"


      value: Api-Token $dt-access-token


      - name: "Content-Type"


      value: "application/json; charset=utf-8"


      template.dynatrace-webhook-template: |


      webhook:


      dynatrace-webhook:


      method: POST


      path: /platform/ingest/custom/events.sdlc/argocd


      body: |


      {


      "app": {{toJson .app}}


      }


      trigger.dynatrace-webhook-trigger: |


      - when: app.status.operationState.phase in ['Succeeded'] and app.status.health.status in ['Healthy', 'Degraded']


      send: [dynatrace-webhook-template]


      - when: app.status.operationState.phase in ['Failed', 'Error']


      send: [dynatrace-webhook-template]


      - when: app.status.operationState.phase in ['Running']


      send: [dynatrace-webhook-template]
      ```

      Вот объяснение именования в конфигурации.

      * `dynatrace-webhook` — это имя сервиса, `$dt-access-token` ссылается на токен доступа Dynatrace, а `$dt-base-url` — это ссылка на конечную точку загрузки событий Dynatrace, хранящуюся в секрете `argocd-notifications-secret`.
      * `dynatrace-webhook-template` — это имя шаблона, а `dynatrace-webhook` ссылается на созданный выше сервис.
      * `dynatrace-webhook-trigger` — это имя триггера, а `dynatrace-webhook-template` ссылается на созданный выше шаблон.
   2. Примените конфигурацию следующей командой.

      `kubectl apply -f <config_map_file_name>.yaml -n argocd`
   3. Подписка приложений на уведомления.

      Измените аннотации приложения Argo CD, используя пользовательский интерфейс Argo CD или [определение приложения Argo CD](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#applications), добавив следующие аннотации:

      ```
      apiVersion: argoproj.io/v1alpha1


      kind: Application


      metadata:


      annotations:


      notifications.argoproj.io/subscribe.dynatrace-webhook-trigger.dynatrace-webhook: ""
      ```

      Добавленная аннотация `notifications.argoproj.io` подписывает приложение Argo CD на настройку уведомлений, которую вы создали выше.

5. Подготовка: отправка метрик Prometheus из Argo CD в Dynatrace

Argo CD предоставляет различные наборы метрик Prometheus для разных сервисов.
Настройте ваши сервисы Argo CD для предоставления этой информации, чтобы Dynatrace мог её собирать.
Вы можете использовать либо [Dynatrace ActiveGate](../../../ingest-from/dynatrace-activegate.md "Understand the basic concepts related to ActiveGate."), установленный на кластере Kubernetes, на котором размещён Argo CD, либо [Dynatrace OTel Collector](../../../ingest-from/opentelemetry/collector.md#dt-collector-dist "Learn about the Dynatrace OTel Collector.").

Для использования [Dynatrace ActiveGate](../../../ingest-from/dynatrace-activegate.md "Understand the basic concepts related to ActiveGate.")

1. Включите [мониторинг метрик Prometheus](../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

   1. Перейдите в **Kubernetes** и выберите отслеживаемый кластер с установкой Argo CD.
   2. В правом верхнем углу перейдите в  > **Connection settings**.
   3. Выберите **Monitoring Settings**.
   4. Включите **Monitor annotated Prometheus exporters**.
   5. **Сохраните**.
2. В пространстве имён вашей установки Argo CD добавьте следующие две аннотации для каждого из сервисов, перечисленных в таблице ниже.
   Замените `{METRICS_PORT}` соответствующим номером порта.

   ```
   metrics.dynatrace.com/port: {METRICS_PORT}


   metrics.dynatrace.com/scrape: 'true'
   ```

   | Сервис | Порт метрик |
   | --- | --- |
   | argocd-applicationset-controller | 8080 |
   | argocd-metrics | 8082 |
   | argocd-server-metrics | 8083 |
   | argocd-repo-server | 8084 |
   | argocd-notifications-controller-metrics | 9001 |
   | argocd-dex-server | 5558 |

   Просмотрите загрузку данных [гистограмм](https://www.dynatrace.com/news/blog/opentelemetry-histograms-reveal-patterns-outliers-and-trends/), перейдя в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Metrics** > **Histograms**. Настройка **Ingest complete explicit bucket histograms**, которая вам нужна, включена автоматически.

6. Расширенная аналитика развёртываний с дашбордами Argo CD

Теперь, когда вы успешно настроили Argo CD и Dynatrace, вы можете использовать дашборды и события SDLC для наблюдения за развёртываниями Argo CD.

### Анализ

В Dynatrace откройте дашборд **ArgoCD Application Lifecycle**, чтобы

* Исследовать выполняющиеся синхронизации и точки концентрации большого количества операций синхронизации.
* Анализировать продолжительность операций синхронизации.
* Видеть статус развёртывания и состояние приложений.

### Оптимизация

Используйте полученную информацию для следующих направлений улучшения:

* Повышение производительности: оптимизация синхронизаций может сократить время развёртывания изменений, делая процесс развёртывания более эффективным. Эффективные синхронизации также помогают лучше использовать ресурсы, снижая нагрузку на инфраструктуру.
* Повышение надёжности: оптимизация синхронизаций может минимизировать вероятность ошибок при развёртывании, что приведёт к более стабильным и надёжным релизам.
  Обеспечение оптимизации синхронизаций помогает поддерживать согласованность между различными средами.

### Непрерывное улучшение

Регулярно проверяйте операции синхронизации Argo CD и корректируйте конфигурацию для обеспечения их оптимальной производительности.

В Dynatrace настройте временной диапазон дашбордов **ArgoCD Application Lifecycle** для отслеживания долгосрочного влияния ваших улучшений.

## Призыв к действию

Мы высоко ценим вашу обратную связь по наблюдаемости Argo CD. Ваши отзывы критически важны для улучшения наших инструментов и сервисов. Посетите страницу Dynatrace Community, чтобы поделиться своим опытом, предложениями и идеями в [канале обратной связи по наблюдаемости CI/CD-пайплайнов](https://community.dynatrace.com/t5/Platform-Engineering/Feedback-channel-for-CI-CD-Pipeline-Observability/m-p/269193).

## Дополнительные материалы

* [Наблюдаемость на протяжении всего жизненного цикла разработки ПО повышает эффективность доставки](https://www.dynatrace.com/news/blog/observability-throughout-the-software-development-lifecycle/)
* [Наблюдаемость пайплайнов](../../pipeline-observability-sdlc-events.md "With insights into your pipelines and processes, you can observe and analyze software engineering practices within an organization.")

## Связанные темы

* [Как загружать данные (события)](../../../platform/openpipeline/getting-started/how-to-ingestion.md "How to ingest data for a configuration scope in OpenPipeline.")
* [События жизненного цикла разработки программного обеспечения (SDLC)](../../../semantic-dictionary/model/sdlc-events.md "Get to know the Semantic Dictionary models related to Software development lifecycle (SDLC) events.")
* [Загрузка событий SDLC](../sdlc-events.md "You can observe your pipeline through software development lifecycle (SDLC) events which you can then ingest to use to generate analytics.")
* [Автоматическое обновление Dynatrace Operator](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update.md "Enable automatic updates of Dynatrace Operator following a GitOps approach.")