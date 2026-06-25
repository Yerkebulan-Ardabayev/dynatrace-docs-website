---
title: Импорт сертификатов Kubernetes API
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/api-certificates
scraped: 2026-05-12T12:09:10.726489
---

# Импорт сертификатов Kubernetes API

# Импорт сертификатов Kubernetes API

* Чтение: 1 мин
* Опубликовано 28 июля 2023 г.

Сертификаты Kubernetes API импортируются автоматически для проверки валидации сертификатов. Kubernetes автоматически создаёт configmap `kube-root-ca.crt` в каждом пространстве имён. Этот сертификат автоматически монтируется в каждый контейнер по пути `/var/run/secrets/kubernetes.io/serviceaccount/ca.crt` и объединяется с файлом хранилища доверенных сертификатов ActiveGate с помощью `initContainer`.
Чтобы воспользоваться этой функцией, необходимо [обновить Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#update "Процедуры обновления и удаления Dynatrace Operator"), если вы используете более раннюю версию.