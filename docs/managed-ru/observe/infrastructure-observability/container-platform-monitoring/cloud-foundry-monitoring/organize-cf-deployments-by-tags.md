---
title: Организация развёртываний Cloud Foundry с помощью тегов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/organize-cf-deployments-by-tags
scraped: 2026-05-12T11:11:29.170818
---

# Organize Cloud Foundry deployments by tags

# Организация развёртываний Cloud Foundry с помощью тегов

* How-to guide
* 3-min read
* Published Sep 21, 2017

Dynatrace позволяет определять теги для групп процессов и сервисов приложений CloudFoundry с помощью любого пользовательского сервиса Dynatrace [Cloud Foundry](https://docs.run.pivotal.io/devguide/services/), привязанного к вашему приложению. Это позволяет автоматически организовывать и фильтровать все отслеживаемые компоненты приложений Cloud Foundry.

## Рекомендация

Определение тегов непосредственно в среде имеет свои преимущества. Однако в качестве универсального решения это не рекомендуется — подход трудоёмок и требует значительного предварительного планирования. Вносить изменения впоследствии также непросто. Используйте его с осторожностью.

Рекомендуется определять дополнительные метаданные на уровне развёртываемой системы. Для приложений CloudFoundry это также можно сделать через пользовательский сервис Dynatrace [Cloud Foundry](https://docs.run.pivotal.io/devguide/services/), привязанный к вашему приложению.

Это позволяет использовать [правила автоматической расстановки тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags#automatic "Find out how to define and apply tags manually and automatically.") на основе существующих или пользовательских метаданных для определения наборов фильтров для диаграмм, оповещений и других задач. Эти теги и правила можно изменять и адаптировать в любое время — они применяются практически мгновенно без каких-либо изменений в отслеживаемой среде или приложениях.

## Определение тегов сервиса Cloud Foundry для нескольких приложений

Для определения тегов Dynatrace можно использовать один или несколько экземпляров сервиса Cloud Foundry, имя которых содержит подстроку `dynatrace`. Например:

```
cf cups dynatrace-tags -p '{ "tag key": "tag value", "tag key": "tag value"}'
```

Система автоматически предложит ввести значения для определённых тегов (например, `tag:region>eu-central-1`). Dynatrace поддерживает как метки Cloud Foundry, так и теги Cloud Foundry в формате «ключ-значение». Например, тег `tanzu` в приведённом примере служит для маркировки всех приложений, работающих в среде VMware Tanzu, — поэтому он не содержит значения. Тег «ключ-значение» `region` содержит регион учётной записи AWS, использованной для развёртывания среды Cloud Foundry.

Пользовательские сервисы Cloud Foundry можно легко обновлять, добавляя новые значения (например, `tag:region>eu-west-2`) или дополнительные теги:

```
cf uups dynatrace-tags -p "tag:tanzu, tag:region, tag:newtag"
```

Чтобы задействовать приведённый выше экземпляр сервиса `dynatrace-tags`, необходимо привязать его к приложению (например, `spring-music`):

```
cf bs spring-music dynatrace-tags
```

## Определение тегов для конкретных приложений Cloud Foundry

Кроме того, Dynatrace автоматически обнаруживает теги, передаваемые приложениям через [переменные среды Cloud Foundry](https://docs.pivotal.io/pivotalcf/1-12/devguide/deploy-apps/manifest.html#env-block). Например, переменную среды `DT_TAGS` можно указать в блоке `env` манифеста приложения или задать с помощью команды `cf` `set-env`:

```
---



applications:



- name: spring-music



memory: 1G



random-route: true



path: build/libs/spring-music.jar



services:



- dynatrace-service



env:



DT_TAGS: hotfix
```

```
cf set-env spring-music DT_TAGS "hotfix"
```

Оба примера выше присваивают тег `hotfix` всем отслеживаемым процессам, связанным с приложением `spring-music`.

## Использование тегов Cloud Foundry в окружении Dynatrace

Теги Cloud Foundry доступны для поиска через поиск Dynatrace. Это позволяет легко находить и анализировать результаты мониторинга связанных процессов, работающих в среде Cloud Foundry.

Теги Cloud Foundry также легко интегрируются с фильтрами Dynatrace. Например, с их помощью можно фильтровать технологии или проблемы. Теги Cloud Foundry также можно использовать при настройке детальных [профилей оповещений о проблемах](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").

## Ограничения

Интеграция buildpack Dynatrace для IBM WebSphere Liberty в настоящее время поддерживает только один экземпляр сервиса, имя которого содержит подстроку `dynatrace`. Однако теги можно легко передать при создании этого единственного экземпляра сервиса для Dynatrace:

```
cf cups dynatrace-service -p "environmentid, apitoken, tag:tanzu, tag:region"
```

Если экземпляр сервиса Dynatrace уже существует, его можно обновить, добавив новые значения или дополнительные теги:

```
cf uups dynatrace-service -p "environmentid, apitoken, tag:tanzu, tag:region, tag:newtag"
```

Подробнее о создании пользовательского сервиса для Dynatrace см. в разделе [Мониторинг приложений Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.").

Интеграции buildpack Dynatrace для Node.js, Java, PHP и Staticfile позволяют использовать не один, а несколько экземпляров сервисов для определения тегов Dynatrace.

## Связанные темы

* [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")