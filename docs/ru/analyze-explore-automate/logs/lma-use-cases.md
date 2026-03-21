---
title: Управление журналами и аналитикой использования __KEEP000__
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases
scraped: 2026-03-06T21:15:16.527467
---

# Сценарии использования Log Management and Analytics


Следующие сценарии использования демонстрируют лишь некоторые из способов применения Log Management and Analytics для работы с данными логов.

### Наблюдение за сетевым трафиком облака с помощью логов

В этом сценарии вам необходимо использовать логи VPC Flow для мониторинга и анализа входящего HTTP(S)-трафика в вашем виртуальном частном облаке (VPC) в Amazon Web Services (AWS).

* [Наблюдение за сетевым трафиком облака с помощью логов](lma-use-cases/lma-e2e-observability.md "Observability using logs, metrics and dashboards.")

### Использование логов в контексте для устранения неполадок

В этом сценарии вам нужно выполнить проактивную проверку состояния и производительности приложений, работающих на обслуживаемом кластере, и узнать об ошибках в логах, вызванных другим компонентом.

* [Использование логов в контексте для устранения неполадок Kubernetes (K8s)](lma-use-cases/lma-e2e-troubleshooting.md "Faster troubleshooting with logs, metrics and traces on Kubernetes.")

### Расследование инцидентов безопасности в кластерах Kubernetes — поиск угроз

Реагирование на инциденты

В этом сценарии вы работаете с [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") для анализа неавторизованных запросов в журналах аудита Kubernetes. Узнайте, как можно управлять и повторно использовать доказательства, собранные в ходе расследования, перемещаться между выполненными запросами, сохраняя контекст расследования, и получать подробный обзор результатов в исходном формате.

* [Поиск угроз и цифровая криминалистика](../../secure/use-cases/threat-hunting.md "Use case scenario for threat hunting and forensics with Investigations.")

### Анализ логов AWS CloudTrail

Реагирование на инциденты

В этом сценарии вы работаете с [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") для анализа данных событий CloudTrail, мониторинга и выявления активности в вашей учётной записи AWS на предмет угроз безопасности и потенциальных отклонений от нормальной деятельности.

* [Анализ логов AWS CloudTrail с помощью Investigations](../../secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator.md "Analyze CloudTrail logs and find potential security issues with Dynatrace.")

### Анализ логов доступа Amazon API Gateway

Реагирование на инциденты

В этом сценарии вы работаете с [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") для мониторинга и выявления ошибок в логах доступа Amazon API Gateway.

* [Анализ логов доступа Amazon API Gateway с помощью Investigations](../../secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator.md "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")

### Обнаружение угроз для ваших секретов AWS

Реагирование на инциденты

В этом сценарии вы работаете с [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../secure/investigations.md "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") для мониторинга и выявления потенциальных угроз для ваших секретов AWS путём анализа логов CloudTrail.

* [Обнаружение угроз для ваших секретов AWS с помощью Investigations](../../secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator.md "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")

### Разрешение зависимостей между командами

В этом сценарии вы создаёте панель анализа логов, которая отвечает за выявление ошибок из логов, а также за их группировку, приоритизацию и распределение в систему отслеживания ошибок, что проясняет неоднозначные зоны ответственности и взаимозависимости.

* [Автоматическая приоритизация ошибок и создание тикетов](lma-use-cases/lma-e2e-resolve-dependencies.md "Explore a Log Management and Analytics use case for resolving team dependencies.")

### Наблюдаемость в реальном времени с помощью логов и DQL

В этом сценарии вы хотите наблюдать за критически важной информацией во времени, содержащейся в ваших логах, которые отправляются через API приёма логов.

* [Наблюдение за логами в реальном времени](lma-use-cases/lma-e2e-real-time-observability-logs-dql.md "Explore the Log Management and Analytics use case for real-time observability with logs.")

### Контроль стоимости запросов к логам с помощью Retain with Included Queries

В этом сценарии вы используете возможность DPS **Retain with Included Queries** для контроля и прогнозирования потребления логов.

* [Контроль стоимости запросов к логам с помощью Retain with Included Queries](lma-use-cases/lma-e2e-included-log-queries.md "How to use the Retain with Included Queries capability to control and predict log consumption.")

### Настройка пользовательских оповещений на основе событий, извлечённых из логов

С помощью событий Davis, основанных на логах, вы получите немедленные оповещения при приёме определённой вами записи лога.

* [Настройка оповещений на основе событий, извлечённых из логов](lma-use-cases/lma-alert-log-based-events.md "How to create and configure Davis problems and alerts with events based on logs.")

### Настройка пользовательских оповещений на основе метрик, извлечённых из логов

Используя комбинацию метрик, основанных на логах, и [пользовательских оповещений](../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app."), вы можете использовать возможности различных анализаторов данных Dynatrace Intelligence для решения задач от простого оповещения по пороговым значениям до сезонных базовых линий.

* [Настройка пользовательских оповещений на основе метрик, извлечённых из логов](lma-use-cases/lma-alert-log-based-metrics.md "How to create and configure Davis problems and custom alerts with metrics based on logs.")

## Связанные темы

* [Dynatrace Query Language](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.")