---
title: Метаданные группы процессов для Cloud Foundry
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/define-process-group-metadata-for-cloud-foundry-applications
scraped: 2026-05-12T11:37:38.161316
---

# Process group metadata for Cloud Foundry

# Метаданные группы процессов для Cloud Foundry

* 2-min read
* Published Feb 25, 2019

Dynatrace позволяет [определять собственные метаданные](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.") в соответствии с потребностями вашей организации или среды. Метаданные группы процессов также можно определять с помощью сервиса Cloud Foundry и повторно использовать их в нескольких приложениях.

## Определение метаданных сервиса Cloud Foundry

Для определения собственных метаданных группы процессов можно использовать один или несколько экземпляров сервиса Cloud Foundry, имя которых содержит подстроку `dynatrace`. Например:

```
cf cups dynatrace-metadata -p "meta-data:owner"
```

Система автоматически предложит ввести значения для определённых метаданных. Чтобы указать несколько сразу, разделите их запятой.

```
cf cups dynatrace-metadata -p "meta-data:owner, meta-data:github-source, meta-data:step"
```

Если отслеживаемое приложение Cloud Foundry размещено на GitHub, можно легко добавить ссылку на соответствующий репозиторий с помощью пользовательских метаданных группы процессов. Как показано в примере ниже, для монолитного приложения TicketMonster заданы пользовательские метаданные группы процессов (подробнее об этом — в записи блога [Fearless Monolith to Microservices Migration — A guided journey](https://www.dynatrace.com/news/blog/fearless-monolith-to-microservices-migration-a-guided-journey/) автора Johannes Bräuer). Добавлена ссылка на [репозиторий GitHub приложения TicketMonster](https://github.com/dynatrace-innovationlab/monolith-to-microservice-cloudfoundry/tree/master/monolith) как свойство `github-source`, а само приложение идентифицировано как монолитная отправная точка пути «разбиения» к архитектуре микросервисов.

![Cloud Foundry metadata](https://dt-cdn.net/images/cf-metadata-example-1-1713-4b8cbb3f14.png)

Метаданные Cloud Foundry

Если для интеграции Dynatrace OneAgent в приложение используются [Cloud Foundry buildpacks](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry."), полезно указать версию buildpack, применявшуюся при развёртывании приложения, — это помогает понять, какие возможности доступны в рамках конкретного релиза buildpack.

```
cf cups dynatrace-apps-only-metadata -p "meta-data:buildpack, meta-data:version"
```

Для сравнения поведения двух версий приложения при [Blue-Green развёртывании](https://docs.cloudfoundry.org/devguide/deploy-apps/blue-green.html) можно также использовать пользовательские метаданные группы процессов для идентификации разных версий приложения.

Чтобы задействовать экземпляр сервиса `dynatrace-metadata` (или `dynatrace-*-metadata`), необходимо привязать его к приложению (например, `ticket-monster`):

```
cf bs ticket-monster dynatrace-metadata
```

## Использование пользовательских метаданных группы процессов для организации приложений Cloud Foundry

Метаданные группы процессов Cloud Foundry можно использовать в качестве заменителя при создании автоматически применяемых тегов (как показано в примере ниже) или для именования групп процессов. Приведённый ниже тег на основе правил будет добавлен к монолитному приложению TicketMonster и всем связанным сервисам. В этом примере для значения тега задано пользовательское свойство группы процессов `meta-data:step>monolith`.

![Cloud foundry metadata](https://dt-cdn.net/images/cf-metadata-example-2-1713-d1d3894ed6.png)

Метаданные Cloud Foundry

![Cloud foundry metadata](https://dt-cdn.net/images/cf-metadata-example-3-1665-3c163aaccf.png)

Метаданные Cloud Foundry

## Связанные темы

* [Настройка Dynatrace на Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")