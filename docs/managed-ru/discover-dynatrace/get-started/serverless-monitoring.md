---
title: Мониторинг бессерверных приложений
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/serverless-monitoring
scraped: 2026-05-12T11:09:29.374146
---

# Мониторинг бессерверных приложений

# Мониторинг бессерверных приложений

* 3-min read
* Published Jan 27, 2023

Термин **serverless** (бессерверный) описывает облачные сервисы с общими характеристиками:

* Высокий уровень абстракции, **не требующий управления базовой инфраструктурой**
* Высокая доступность и **эластичное масштабирование** в соответствии с потребностями
* Модель оплаты **по потреблению** (pay-per-use)

Хотя термин нередко используется как синоним Functions-As-A-Service (FaaS), бессерверные облачные сервисы охватывают все виды сервисов. Три наиболее важные категории:

* **Бессерверные вычисления**, включая функции и контейнеры, а также управляемый Kubernetes
* **Бессерверная PaaS** — API-шлюзы, системы обмена сообщениями или очереди
* **Бессерверные базы данных** и кэши

## Проблемы наблюдаемости

Природа бессерверных технологий создаёт определённые трудности для эффективной наблюдаемости таких облачных сервисов:

* Высокая распределённость, что делает распределённую трассировку критически важной возможностью.
* Изолированные среды с ограниченными возможностями для изменений.
* Множество различных способов захвата телеметрии.
* Ограничения нативных средств мониторинга облачных провайдеров:

  + Понимание поведения системы может быть затруднено, так как телеметрия поступает из множества источников данных и распределена по нескольким местам.
  + Получение сквозного представления может быть затруднено, особенно при использовании гибридного или мультиоблачного подхода и сторонних приложений.
  + Ограниченные возможности, отсутствие критически важных функций, таких как мониторинг реальных пользователей или профилирование, требующих дополнительных инструментов.
* Новые паттерны проблем:

  + Поведение холодного запуска
  + Оптимизация выделения облачных сервисов
  + Сложные лимиты и квоты сервисов
  + Переходные сбои

## Наблюдаемость бессерверных приложений с Dynatrace

Обеспечивая глубокую интеграцию с тремя крупнейшими поставщиками публичного облака для захвата метрик, метаданных, событий, журналов и трейсов, Dynatrace унифицирует все источники данных и помещает их в контекст для обеспечения сквозной видимости и анализа этих данных с помощью Davis AI.

![Унифицированная бессерверная телеметрия](https://dt-cdn.net/images/unified-service-descr-630-f2484fd514.png)

Унифицированная бессерверная телеметрия

Располагая более чем [600 интеграциями, расширениями и специализированной поддержкой технологий](https://www.dynatrace.com/hub/), Dynatrace предоставляет обширную поддержку мониторинга, включая ваши [бессерверные технологии](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS)."), работающие на AWS, Azure или Google Cloud.

## Начало работы с мониторингом бессерверных приложений

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Включите мониторинг облачных сервисов**](/managed/discover-dynatrace/get-started/serverless-monitoring#services "Serverless observability with Dynatrace")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Включите расширения Dynatrace для облачных сервисов**](/managed/discover-dynatrace/get-started/serverless-monitoring#extensions "Serverless observability with Dynatrace")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Расширенная видимость**](/managed/discover-dynatrace/get-started/serverless-monitoring#advanced "Serverless observability with Dynatrace")

### Шаг 1 Включите мониторинг облачных сервисов

С помощью единственной интеграции на каждого облачного поставщика Dynatrace автоматически обнаруживает ваши облачные сервисы и отслеживает их для предоставления готового мониторинга работоспособности и доступности:

* [Интеграция Amazon CloudWatch](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")
* [Интеграция Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")
* [Интеграция Google Cloud operations suite](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.")

### Шаг 2 Включите расширения Dynatrace для облачных сервисов с нативным механизмом расширяемости

Ряд облачных вычислительных сервисов допускает простую интеграцию без необходимости повторного развёртывания сервиса. Это упрощает добавление глубокой инструментации сервиса для дополнительной видимости.

Посетите Dynatrace Hub, чтобы просмотреть все сервисы с [облачно-нативной интеграцией](https://www.dynatrace.com/hub/?query=cloud-extension).

### Шаг 3 Расширенная видимость

Инструкции по интеграции Dynatrace в образ контейнера или использованию OpenTelemetry либо расширенной видимости для включения дополнительных подробностей через журналы и другие события телеметрии см. в руководствах по конкретным сервисам в нашей документации:

* [Amazon Web Services](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")
* [Azure Services](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Google Cloud Services](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")

Обязательно обращайте внимание на рекомендации в веб-интерфейсе Dynatrace для включения дополнительных источников телеметрии, которые улучшат наблюдаемость ваших сервисов. Например:

![Рекомендации по наблюдаемости](https://dt-cdn.net/images/observability-hints-871-dd9d927caa.png)

Рекомендации по наблюдаемости