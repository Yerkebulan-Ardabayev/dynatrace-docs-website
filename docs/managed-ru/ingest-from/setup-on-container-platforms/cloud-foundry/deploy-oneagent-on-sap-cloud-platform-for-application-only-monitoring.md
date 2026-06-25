---
title: Развёртывание OneAgent на SAP Business Technology Platform для мониторинга только приложений
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring
scraped: 2026-05-12T11:09:20.847242
---

# Развёртывание OneAgent на SAP Business Technology Platform для мониторинга только приложений

# Развёртывание OneAgent на SAP Business Technology Platform для мониторинга только приложений

* 3-min read
* Published Jul 19, 2017

Приложения, развёрнутые на Cloud Foundry, как правило, запускаются через специфичные для технологии buildpacks, предоставляющие поддержку фреймворков и среды выполнения. Подробнее см. в разделе [как работают buildpacks](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html).

В режиме мониторинга только приложений OneAgent отслеживает потребление памяти, диска, CPU и сети процессами внутри контейнера. Метрики хоста не отслеживаются.

Следующие рекомендации применяются для **SAP Business Technology Platform (SAP BTP)**.

## Предварительные условия

Создайте [Токен доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Концепция токена доступа и его областей видимости.") со следующими разрешениями:

* **Access problem and event feed, metrics, and topology**
* **PaaS integration - Installer download**

## Развёртывание OneAgent на SAP BTP Cloud Foundry Runtime

SAP BTP, Cloud Foundry Environment включает [ряд buildpacks](https://help.sap.com/viewer/4505d0bdaf4948449b7f7379d24d0f0d/2.0.05/en-US/684a8a79827047998b3c1e8519dec10f.html). Данные рекомендации применимы к следующим интеграциям buildpack:

* SAP Java Buildpack
* [Java Buildpack](https://github.com/cloudfoundry/java-buildpack)
* [PHP Buildpack](https://github.com/cloudfoundry/php-buildpack)
* [Staticfile Buildpack](https://github.com/cloudfoundry/staticfile-buildpack)
* [Cloud Foundry Node.js Buildpack](https://github.com/cloudfoundry/nodejs-buildpack).

SAP Java Buildpack поддерживается SAP. При возникновении проблем с SAP Java Buildpack обратитесь к компоненту `BC-XS-JAV` и создайте заявку на SAP Support Portal. Остальные buildpacks поддерживаются Cloud Foundry Foundation на GitHub.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Создание user-provided service в SAP BTP, Cloud Foundry Environment**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring#create-service "Установка OneAgent на SAP Business Technology Platform.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Привязка сервиса Dynatrace к приложению**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring#bind-service-to-app "Установка OneAgent на SAP Business Technology Platform.")

### Шаг 1. Создание user-provided service в SAP BTP, Cloud Foundry Environment

Создайте единственный экземпляр сервиса Dynatrace, имя которого содержит подстроку `dynatrace` (например, `dynatraceservice`). Можно использовать CLI `cf` или создать user-provided service непосредственно через [кокпит SAP Business Technology Platform](https://account.hana.ondemand.com/cockpit).

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen01-1765-0d4d1d9bf6.webp)

SAP BTB Cockpit

Необходимо предоставить валидный JSON-объект, содержащий как минимум `environmentid` и `apitoken`. API-токен соответствует PaaS-токену, описанному выше.

Для Dynatrace Managed также необходимо добавить параметр `apiurl`, указывающий на эндпоинт [Dynatrace API](/managed/dynatrace-api "Узнайте об использовании Dynatrace API."). Например:

#### Dynatrace SaaS

```
{



"environmentid": "YOUR_ENVIRONMENTID",



"apitoken": "YOUR_PAAS_TOKEN",



"tag:SAP BTB": "",



"tag:Region": "Frankfurt"



}
```

#### Dynatrace Managed

```
{



"environmentid": "YOUR_ENVIRONMENTID",



"apitoken": "YOUR_PAAS_TOKEN",



"tag:SAP BTB": "",



"tag:Region": "Frankfurt",



"apiurl": "https://<your-domain>/e/<environmentID>/api"



}
```

### Шаг 2. Привязка сервиса Dynatrace к приложению

Привязать созданный сервис Dynatrace к приложению можно в файле `manifest.yml`. Если приложение уже запущено, необходимо выполнить restage.

Пример для развёртывания Java-приложения:

```
---



applications:



- name: spring-music



memory: 768M



instances: 1



host: spring-music-somerandomstring



path: spring-music.war



buildpack: sap_java_buildpack



services:



- dynatraceservice
```

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen02-2042-7f899341e1.webp)

SAP BTB Cockpit

## Развёртывание OneAgent на SAP BTP Neo Runtime

SAP предоставляет сервис Dynatrace Agent Activation Neo, который позволяет подключить Java-приложения к окружению мониторинга Dynatrace.

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen03-2087-27ddc3be9f.webp)

SAP BTB Cockpit

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen04-2559-95dea005ca.webp)

SAP BTB Cockpit

Подготовьте [ID окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Работа с окружениями мониторинга.") Dynatrace и сгенерированный [PaaS-токен](/managed/discover-dynatrace/get-started/monitoring-environment "Работа с окружениями мониторинга.").

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen05-2556-57631a9d36.webp)

SAP BTB Cockpit

Для Managed введите URL вашего Cluster ActiveGate (включая `/e/<environmentID>`) в поле **Environment URL**.

После перезапуска Java-приложений, развёрнутых на SAP Business Technology Platform, вы получите полный спектр возможностей мониторинга приложений и сервисов Dynatrace (например, **Smartscape** и аналитику уровня сервисов через **Service flow**).

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")