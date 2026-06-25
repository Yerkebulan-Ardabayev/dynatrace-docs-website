---
title: События «Мониторинг недоступен»
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/monitoring-unavailable-events
scraped: 2026-05-12T12:06:42.345262
---

# События «Мониторинг недоступен»

# События «Мониторинг недоступен»

* Explanation
* 2-min read
* Updated on Feb 27, 2026

Событие `monitoring unavailable` указывает на масштабное прерывание мониторинга, когда большинство установленных OneAgent теряют связь с сервером Dynatrace.

## Симптомы

Обычно это проявляется в отсутствии видимости как в плане мониторинга доступности, так и производительности. В случае прерывания мониторинга:

* Dynatrace автоматически подавляет все отдельные проблемы **Host unavailable** и оповещает вас о прерывании мониторинга.
* Всем хостам устанавливается состояние доступности **Unmonitored** на время перебоя мониторинга.

## Возможные причины

Прерывания мониторинга могут иметь различные первопричины в зависимости от типа развёртывания Dynatrace:

* Среды Dynatrace SaaS администрируются командой DevOps Dynatrace, которая публикует все операционные проблемы на [dynatrace.status.io](https://dynatrace.status.io/).
* Для сред, работающих в развёртываниях Dynatrace Managed, наиболее вероятно, что прерывание мониторинга вызвано проблемой в вашем собственном центре обработки данных или конфигурации сети.

Независимо от типа развёртывания Dynatrace, распространённой причиной прерываний мониторинга являются проблемы в работе ActiveGate. Чтобы минимизировать риск прерываний из-за ActiveGate, можно использовать [метрики самомониторинга ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-sfm-metrics "Изучите метрики самомониторинга ActiveGate.") для своевременной оценки состояния ваших ActiveGate.

## Устранение неполадок

Для устранения неполадок события `monitoring unavailable` см. [Устранение неполадок прерываний мониторинга](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-monitoring-interruptions "Узнайте, как справляться с различными типами прерываний мониторинга в зависимости от типа развёртывания Dynatrace.").

## Фильтрация проблем и оповещений

Уровень серьёзности `monitoring unavailable` позволяет фильтровать эти критически важные оповещения и быстро направлять их командам операций мониторинга.

### Проблемы

Чтобы просмотреть проблемы `monitoring unavailable`

1. Перейдите в раздел **Problems**.
2. В поле **Filter by** выберите `Severity`: `Monitoring unavailable`.

Подробнее о проблемах см. в разделе [Davis® AI](/managed/dynatrace-intelligence "Ознакомьтесь с возможностями Davis AI.").