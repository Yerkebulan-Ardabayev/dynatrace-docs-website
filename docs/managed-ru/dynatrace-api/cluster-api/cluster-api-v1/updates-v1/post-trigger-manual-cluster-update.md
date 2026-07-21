---
title: Trigger manual cluster update
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/updates-v1/post-trigger-manual-cluster-update
---

# Trigger manual cluster update

# Trigger manual cluster update

* Опубликовано 03 июня 2026 г.

Этот вызов API запускает ручное обновление кластера.

## Аутентификация

Для выполнения этого запроса нужен один из следующих скоупов API-Token:

* `ControlManagement`
* `ServiceProviderAPI`
* `Nodekeeper`

## Endpoint

`/api/v1.0/upgradeManagement/triggerUpgrade`

## Параметр

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успешно запущено. |
| **412** | Запуск обновления не выполнен из-за отсутствия новой версии на всех узлах. |
| **510** | Не удалось запустить обновление. Проверьте логи для получения подробностей... |
| **553** | Обновление приостановлено Dynatrace Mission Control. Сейчас невозможно обновить кластер. |
| **554** | Обновление уже выполняется. |