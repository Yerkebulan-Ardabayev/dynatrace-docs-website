---
title: Использование priorityClass для критически важных компонентов Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/priority
scraped: 2026-05-12T12:09:28.023605
---

# Использование priorityClass для критически важных компонентов Dynatrace

# Использование priorityClass для критически важных компонентов Dynatrace

* Чтение: 1 мин
* Опубликовано 28 июля 2023 г.

Начиная с Dynatrace Operator версии 0.8.0+, при установке Dynatrace Operator по умолчанию создаётся объект `priorityClass`. Этому классу приоритета изначально присваивается высокое значение, чтобы компоненты, которые его используют, имели более высокий приоритет, чем другие поды, и чтобы такие критически важные компоненты, как CSI-драйвер, планировались Kubernetes. Подробнее см. [документацию Kubernetes по PriorityClass](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass).

Вы можете изменить значение этого параметра по умолчанию в соответствии с вашей средой и индивидуальным использованием классов приоритета в вашем кластере. Учтите, что понижение значения по умолчанию может повлиять на планирование подов, создаваемых Dynatrace. По умолчанию `priorityClass` применяется к подам CSI-драйвера, но его также можно использовать для подов OneAgent (см. параметр `priorityClassName` в разделе [Параметры DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")).