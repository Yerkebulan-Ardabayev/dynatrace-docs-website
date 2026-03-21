---
title: Обнаружение угроз в облачно-нативных средах с помощью рабочих процессов
source: https://www.dynatrace.com/docs/secure/use-cases/detect-threats-cloud-native-workflows
scraped: 2026-03-03T21:28:43.872463
---

# Обнаружение угроз в облачных средах с помощью Workflows


* Latest Dynatrace
* Tutorial

В этом руководстве вы узнаете, как

* Непрерывно обнаруживать и реагировать на активные угрозы в вашей облачной среде
* Находить злоумышленников, пытающихся эксплуатировать ваши приложения, прежде чем они смогут негативно повлиять на ваш бизнес
* Легко и гибко выполнять поиск по большим объемам данных для выявления признаков подозрительного поведения

## Целевая аудитория

Эта статья предназначена для

* Специалистов DevOps, CloudOps и SRE, ответственных за защиту рабочих нагрузок
* Аналитиков безопасности, ответственных за облачные среды

## Предварительные требования

* Настройте прием журналов аудита Kubernetes, например, через [Amazon Firehose](../../ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput."). Firehose можно использовать для отправки логов из Amazon Elastic Kubernetes Service (EKS), но предоставленный шаблон совместим с любым дистрибутивом Kubernetes.
* Сгенерируйте токен доступа с областью `openpipeline.events_security`, чтобы разрешить прием результатов обнаружения. Для последующего безопасного доступа к токену из рабочего процесса сохраните токен в [хранилище учетных данных](../../../common/manage/credential-vault.md "Store and manage credentials in the credential vault."). Подробности см. в [Dynatrace API — токены и аутентификация](../../dynatrace-api/basics/dynatrace-api-authentication.md "Find out how to get authenticated to use the Dynatrace API.").

## Начало работы

После настройки приема логов вы можете приступить к обнаружению угроз.

1. Настройка запланированных DQL-запросов

Используйте ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** для регулярного выполнения DQL-запросов и поиска подозрительного поведения в ваших данных.

1. Импортируйте наш [шаблон рабочего процесса](https://dt-url.net/s9030m9).
2. Для шага **execute\_query** адаптируйте DQL-запрос под ваши потребности.

   Шаблонный запрос направлен на поиск потенциально скомпрометированных сервисных учетных записей в вашем кластере Kubernetes.

   * Вы можете настроить его, изменить логику или полностью модифицировать для обнаружения других потенциальных угроз.
   * Дополнительные примеры можно найти в [блоге Dynatrace](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/).
3. Для шага **ingest\_findings** перейдите в **Input** > **Authentication** и выберите токен, ранее сохраненный в хранилище учетных данных.

2. Тестирование рабочего процесса

Чтобы вызвать результат обнаружения на основе предоставленного запроса, выполните следующие команды в кластере Kubernetes, отслеживаемом Dynatrace:

1. Создайте тестовую сервисную учетную запись:

   ```
   kubectl create serviceaccount test-sa -n default
   ```
2. Попытайтесь выполнить несанкционированный доступ (должно вызвать обнаружение):

   ```
   kubectl --as=system:serviceaccount:default:test-sa get secret -A
   ```

3. Настройка обнаружения

Вы можете определить исключения из правила, добавив критерии белого списка в шаг **apply\_allowlist** рабочего процесса.

Событие обнаружения не будет создано, если все атрибуты записи совпадают с атрибутами любой отдельной записи в белом списке.

* Сравнение атрибутов следует логике `AND` внутри записи.
* Оценка белого списка использует логику `OR` между записями.

4. Сортировка и расследование

Используйте [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../threats-and-exploits.md "Understand, triage, and investigate detection findings and alerts.") для изучения и приоритизации созданных результатов обнаружения. Богатый контекст наблюдаемости, предоставляемый в результатах обнаружения, обеспечивает быстрый анализ и уверенную оценку ситуации.

**Пример результата**

![sample result in threats and exploits app](https://dt-cdn.net/images/image-58-1667-0a98717d9c.png)

## Примеры рабочих процессов для реагирования на угрозы

Dynatrace предоставляет готовые шаблоны рабочих процессов, которые автоматически запускаются при появлении новых результатов обнаружения угроз Kubernetes и отправляют уведомления через [Slack](../../analyze-explore-automate/workflows/actions/slack.md#workflow "Send messages to Slack Workspaces"), [Microsoft Teams](../../analyze-explore-automate/workflows/actions/microsoft-teams.md#use "Send messages to Microsoft Teams") или [электронную почту](../../analyze-explore-automate/workflows/actions/email.md "Automate sending out-of-the-box emails based on the events and schedules defined for your workflows.").
Используйте их как отправные точки для создания собственных автоматизированных рабочих процессов реагирования:

* [Мгновенное уведомление о критических результатах обнаружения Kubernetes](https://dt-url.net/l9430ds): срабатывает при обнаружениях высокой или критической важности и оповещает ответственную команду.
* [Отправитель уведомлений об обнаружении угроз](https://dt-url.net/hs2301e): многоразовый подпроцесс для централизованной доставки уведомлений.

Эти шаблоны демонстрируют, как обогащать результаты обнаружения контекстом [ответственности](../../deliver/ownership.md "Map team ownership to monitored entities for better collaboration, task assignment, incident and vulnerability response, and service-level management.") и интегрировать оповещения в реальном времени в ваши рабочие процессы реагирования.

## Заключение

Workflows обеспечивают точное обнаружение угроз и реагирование, соответствующее контексту вашей среды. Такие функции, как гибкое планирование, фильтрация на основе DQL, белые списки, тегирование ответственности и интеграция уведомлений, обеспечивают быстрое обнаружение с минимальным количеством ложных срабатываний. Включенный шаблон предлагает модульную отправную точку, которую можно тонко настроить или расширить для удовлетворения конкретных операционных потребностей.
