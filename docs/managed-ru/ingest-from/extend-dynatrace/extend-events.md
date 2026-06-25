---
title: Отправка событий в Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-events
scraped: 2026-05-12T11:37:59.140301
---

# Отправка событий в Dynatrace

# Отправка событий в Dynatrace

* 3-min read
* Updated on Mar 16, 2023

С помощью Events API v2 вы можете отправлять события в Dynatrace через ActiveGate или локальный эндпоинт OneAgent.

## Отправка событий через ActiveGate

Для отправки событий используется аутентификация через API-токен.

```bash
curl -X POST "https://<your-environment>/api/v2/events/ingest" \
  -H "Authorization: Api-Token <token>" \
  -H "Content-Type: application/json" \
  -d '{
    "eventType": "CUSTOM_INFO",
    "title": "Deployment completed",
    "entitySelector": "type(SERVICE),tag(production)"
  }'
```

## Отправка событий через локальный эндпоинт OneAgent

OneAgent предоставляет локальный HTTP-эндпоинт для приёма событий:

```bash
curl -X POST "http://localhost:<port>/api/v2/events/ingest" \
  -H "Content-Type: application/json" \
  -d '{
    "eventType": "CUSTOM_INFO",
    "title": "Deployment event"
  }'
```

## Настройка Extension Execution Controller (EEC)

EEC управляет выполнением расширений и может быть настроен через конфигурационные файлы OneAgent.

## Связанные темы

* [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Узнайте об Events API v2.")
* [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Узнайте о концепции токена доступа и его областях видимости.")