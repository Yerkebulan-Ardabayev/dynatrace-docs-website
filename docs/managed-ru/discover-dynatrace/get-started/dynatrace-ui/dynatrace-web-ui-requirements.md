---
title: Требования к веб-интерфейсу Dynatrace
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/dynatrace-ui/dynatrace-web-ui-requirements
scraped: 2026-05-12T12:05:49.920004
---

# Требования к веб-интерфейсу Dynatrace

# Требования к веб-интерфейсу Dynatrace

* Reference
* 2-min read
* Published Dec 19, 2025

Узнайте о требованиях к браузерам для использования Dynatrace.

## Поддерживаемые браузеры для веб-интерфейса Dynatrace

Доступ к веб-интерфейсу Dynatrace возможен с помощью следующих браузеров.

| Браузер | Версии |
| --- | --- |
| Microsoft Edge | Последняя версия (настольная и мобильная) |
| Mozilla Firefox | Последняя версия (настольная) |
| Google Chrome | Последняя версия (настольная и мобильная) |
| Safari | Последняя версия (OS X и iOS) |

### Требования к HTTPS

Начиная с 30 июня 2019 года для доступа к веб-интерфейсу Dynatrace необходимо включить в браузере протокол TLS 1.2. Все современные браузеры используют TLS 1.2 по умолчанию.

После 30 июня 2019 года доступ к веб-интерфейсу Dynatrace через TLS 1.0 или TLS 1.1 будет невозможен.

## Поддерживаемые браузеры для Session Replay

Для воспроизведения пользовательских сессий, записанных с помощью [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers."), можно использовать любой браузер, поддерживаемый для веб-интерфейса Dynatrace.

## Поддерживаемые браузеры для Synthetic Monitoring

Поддерживаемым браузером для Dynatrace Synthetic Recorder является Google Chrome (последняя версия, совместимая с предыдущими).

Браузер, используемый для выполнения браузерных мониторов из общедоступных локаций, указан на странице частоты и локаций при создании или редактировании браузерного монитора.

Версии браузеров для установки на Synthetic-совместимый ActiveGate для выполнения браузерных мониторов из частных локаций см. в разделе [Браузерные мониторы в частных локациях](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").