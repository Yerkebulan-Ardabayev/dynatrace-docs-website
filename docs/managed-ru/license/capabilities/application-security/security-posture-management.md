---
title: Расчёт потребления Security Posture Management (SPM) (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/application-security/security-posture-management
scraped: 2026-05-12T12:00:43.264559
---

# Расчёт потребления Security Posture Management (SPM) (DPS)

# Расчёт потребления Security Posture Management (SPM) (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Security Posture Management.
Обзор возможности и основных функций см. в [Security Posture Management (SPM)](/managed/license/capabilities/application-security#spm "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: хост-час

Единица измерения для Kubernetes Security Posture Management — хост-час.

В средах Kubernetes каждый узел, проверенный в течение часа, считается хост-часом независимо от количества выполненных проверок.
Kubernetes Security Posture Management можно включать на уровне отдельных кластеров.

Пример: расчёт потребления

* Kubernetes Security Posture Management включён для кластера Kubernetes с 10 узлами.
* Анализ Kubernetes Security Posture Management инициирован и ведётся непрерывно.
* Через пять дней к кластеру добавляется 5 узлов, и теперь в кластере 15 узлов.
* Через 10 дней общее потребление рассчитывается как `(10 узлов × 5 дней × 24 часа) + (15 узлов × 5 дней × 24 часа) = 3000 хост-часов`.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления и затрат в Account Management

Отслеживать использование можно также в Account Management.

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview**.
2. В разделе **Cost and usage details** выберите **Usage summary**.
3. Найдите `Security Posture Management` и выберите **View details**.

### Отслеживание потребления и затрат с помощью Data Explorer

* В [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") введите `DPS` в поле **Search**.

### Отслеживание потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Обзор Application Security (DPS)](/managed/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)