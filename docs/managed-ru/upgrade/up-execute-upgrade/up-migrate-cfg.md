---
title: Миграция конфигурации
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-cfg
scraped: 2026-05-12T12:14:05.755900
---

# Миграция конфигурации

# Миграция конфигурации

* Updated on Mar 03, 2026

Dynatrace предлагает несколько инструментов для успешной миграции конфигурации из среды Dynatrace Managed в среду SaaS. Приведённая таблица поможет выбрать подходящий инструмент в зависимости от вашей среды, опыта работы с конфигурацией и [выбранного подхода к обновлению](/managed/upgrade/up-plan#which-approach "A detailed overview of what you need to plan, prepare, and consider before upgrading to Dynatrace SaaS.").

Во избежание проблем совместимости конфигурации обновите развёртывание Dynatrace Managed до последней версии. Рекомендуется обновить Dynatrace Managed до той же версии, что и ваша среда SaaS.

## Выбор инструмента

| Название инструмента | Когда использовать? |
| --- | --- |
| [SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant "Import your Dynatrace Managed environment configuration to SaaS.")  Рекомендуется | SaaS Upgrade Assistant позволяет легко импортировать конфигурацию Dynatrace Managed в среду SaaS и редактировать её в удобном интерфейсе. |
| [Обзор Configuration as Code](/managed/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") | Если вы уже используете [Configuration as Code через Monaco](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.") или [Configuration as Code через Terraform](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform."), можно перенаправить цель на вашу среду SaaS. |

## Начало работы

Используйте одну из следующих процедур миграции в зависимости от выбранного инструмента.

### Миграция с помощью SaaS Upgrade Assistant

Рекомендуется

Для миграции конфигурации с помощью SaaS Upgrade Assistant см. раздел [SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant "Import your Dynatrace Managed environment configuration to SaaS.").

При этом подходе вы экспортируете конфигурацию среды Dynatrace Managed в Cluster Management Console и загружаете её в приложение.

### Миграция с помощью Monaco

Для миграции конфигурации с помощью Monaco:

1. [Установите Dynatrace Configuration as Code через Monaco](/managed/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.") на хосте с сетевым доступом к кластеру Dynatrace Managed (например, непосредственно на узел кластера).
2. Создайте [манифест](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest.") развёртывания: `manifest.yaml`
3. Для каждой среды, которую требуется мигрировать, добавьте конфигурацию:

   * В веб-интерфейсе среды перейдите в **Access tokens** и выберите **Generate new token**.
   * Введите имя токена и установите подходящий срок действия.
   * Выберите следующие области применения:

     + **Read configuration**
     + **Read settings**
     + **Read SLO**
     + **Access problem and event feed, metrics, and topology**
     + **Create and read synthetic monitors, locations, and nodes**
   * Сохраните токен в надёжном месте, например в менеджере паролей.
   * Создайте переменную окружения операционной системы со значением токена. Например, в Linux:

     ```
     export ENV_TOKEN_PRODUCTION_FIN= dt0c01.abc123.abcdefjhij1234567890
     ```
   * Добавьте данные среды в `manifest.yaml`:

     + Добавьте имя в поле `projects`
     + В группе сред **managed** укажите URL с токеном

     Пример `manifest.yaml`:

     ```
     manifestVersion: 1.0



     projects:



     - name: production-fin



     - name: production-logistics



     environmentGroups:



     - name: managed



     environments:



     - name: production-fin



     url:



     value: https://foo123.dynatrace-managed.com/e/1231aaa1-1111-434e-8111-11abcd1234a1



     token:



     name: MIGRATION_TOKEN_PROD_FIN



     - name: production-logistics



     url:



     value: https://foo123.dynatrace-managed.com/e/2345bbb3-3333-456b-1566622abcd3456a1



     token:



     name: MIGRATION_TOKEN_PROD_LOGISTICS
     ```
4. Запустите Monaco с командой загрузки:  
   `monaco download manifest manifest.yaml`

5. Создайте конфигурацию среды SaaS. Выполните шаги из пункта 3 выше, задав область применения токена следующим образом:

   * **Read Configuration**
   * **Write Configuration**
   * **Read settings**
   * **Write settings**
   * **Read SLO**
   * **Write SLO**
   * **Access problem and event feed, metrics, and topology**
   * **Create and read synthetic monitors, locations, and nodes**
     Сохраните токен в надёжном месте (например, в менеджере паролей).
6. Измените настройки конфиденциальности данных.

   Пример:

   ```
   environmentGroups:



   - name: saas



   environments:



   - name: abc1234456



   url:



   value: https://abc1234456.live.dynatrace.com



   token:



   name: ENV_TOKEN_SAAS
   ```
7. Запустите Monaco с командой развёртывания:
   `monaco deploy -e saas`
8. Устраните проблемы и конфликты, описанные в журнале вывода.
   Для неподдерживаемых или дублированных конфигураций используйте `skipDeployment: "true"` и воссоздайте их вручную.

Теперь конфигурация должна быть реплицирована в новую среду SaaS.

### Миграция с помощью Terraform

Для миграции конфигурации с помощью Configuration as Code через Terraform следуйте [руководству по миграции](/managed/deliver/configuration-as-code/terraform/guides/migration "Migrate configurations between Dynatrace environments using Dynatrace Configuration as Code via Terraform.").

## Настройки, требующие ручной миграции

SaaS Upgrade Assistant основан на реализации Dynatrace Configuration as Code, которая поддерживает не все используемые вами настройки. Для обеспечения полной миграции конфигурации необходимо проверить и вручную перенести дополнительные настройки, перечисленные ниже.

Ознакомьтесь с [поддерживаемыми типами API конфигурации](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco") в Dynatrace Configuration as Code.

* Конфигурация [Extensions 1.0](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") и [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions."), включая учётные данные конечных точек
* Учётные данные [AWS](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Monitor AWS with Dynatrace")
* Учётные данные [Azure](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")
* Мониторинг [GCP](/managed/observe/infrastructure-observability/cloud-platform-monitoring/gcp-monitoring "Monitor Google Cloud with Dynatrace")
* Учётные данные [Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* Учётные данные [Kubernetes/OpenShift](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")
* [Мониторинг Heroku](/managed/observe/infrastructure-observability/container-platform-monitoring/heroku "Monitor Heroku with Dynatrace.")
* Мониторинг [платформы VMware](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.")
* [Хранилище учётных данных (Credential vault)](/managed/manage/credential-vault "Store and manage credentials in the credential vault.")
* [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") и [персональные токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.")
* Интеграция [уведомлений о проблемах](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace."), такая как Jira, OpsGenie, PagerDuty, Trello, VictorOps и xMatters
* [Push-уведомления](/managed/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Learn how you can connect your Dynatrace environments with the Dynatrace mobile app to receive problem alerts.") через мобильное приложение Dynatrace
* [Метрики](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."), не связанные с экземплярами
* Аналитика удобства использования веб-приложений — [rage clicks](/managed/observe/digital-experience/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [Ошибки JavaScript](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors#configure-javascript-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")
* [Символизация мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")
* Порядок [именования запросов](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.")
* [Объединённые сервисы](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.")
* Ключевые запросы и их ссылки
* Настройки глубокого мониторинга сервисов на стороне сервера: обновления в реальном времени для сервисов Java и PHP
* Настройки глубокого мониторинга сервисов на стороне сервера: исключение шумных исключений
* Настройки глубокого мониторинга сервисов на стороне сервера: исключение входящих URL веб-запросов
* Настройки глубокого мониторинга сервисов на стороне сервера: захват переменных привязки SQL
* Сохранённые представления [многомерного анализа](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")
* Сохранённые запросы [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
* Порядок [правил пользовательских сервисов](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.")
* [Удалённые среды](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.")
* [Управление аккаунтом](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.") — пользователи, группы, разрешения и политики IAM
* Пользовательские устройства
* Теги, применённые к сущностям вручную
* Пользовательские имена и описания сущностей (например, [группы процессов](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."))

Вопросы?

Посетите [форум Upgrade to SaaS](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas), чтобы задать вопросы, получить ответы и поделиться опытом с другими участниками.