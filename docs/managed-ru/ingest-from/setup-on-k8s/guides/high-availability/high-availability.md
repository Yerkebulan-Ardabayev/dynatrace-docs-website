---
title: Настройка высокой доступности для вебхука Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/high-availability
scraped: 2026-05-12T12:09:29.945714
---

# Настройка высокой доступности для вебхука Dynatrace Operator

# Настройка высокой доступности для вебхука Dynatrace Operator

* Чтение: 1 мин
* Обновлено 27 февраля 2026 г.

## Настройка высокой доступности

Dynatrace Operator версии 1.9.0+

Вы можете настраивать значения `replicas`, `topologySpreadConstraints` и `podDisruptionBudget` независимо друг от друга:

В примерах ниже используются значения Helm. Если вы развёртываете с помощью манифестов, того же можно добиться, напрямую изменив соответствующие разделы в вашем манифесте развёртывания.

```
webhook:



# highAvailability: true # Deprecated, use the following values instead



replicas: 2



topologySpreadConstraints:



- maxSkew: 1



topologyKey: "topology.kubernetes.io/zone"



whenUnsatisfiable: ScheduleAnyway



labelSelector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook



- maxSkew: 1



topologyKey: "kubernetes.io/hostname"



whenUnsatisfiable: ScheduleAnyway



nodeTaintsPolicy: Honor



labelSelector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook



podDisruptionBudget:



minAvailable: 1



selector:



matchLabels:



internal.dynatrace.com/app: webhook



internal.dynatrace.com/component: webhook
```

Чтобы значения `replicas`, `topologySpreadConstraints` и `podDisruptionBudget` вступили в силу, необходимо оставить `highAvailability` в значении `true` (значение по умолчанию). Если задать для `highAvailability` значение `false`, эти поля игнорируются. Это обеспечивает обратную совместимость для пользователей, которые ранее отключали режим высокой доступности.

### Изменения в ограничениях распределения по топологии

Теперь значением по умолчанию для `topologySpreadConstraints` является `whenUnsatisfiable: ScheduleAnyway` вместо прежнего `whenUnsatisfiable: DoNotSchedule`. Это изменение делает планирование менее агрессивным, поэтому поды вебхука по-прежнему могут планироваться в средах, где доступно лишь несколько узлов (один или два). Раньше значение `DoNotSchedule` могло препятствовать планированию подов, если ограничения топологии не удавалось полностью удовлетворить.

## Прежнее значение Helm `highAvailability` (**устарело**)

Dynatrace Operator версии 0.6.0+

Начиная с версии Operator 1.9.0, значение `highAvailability` устарело в пользу значений `replicas`, `topologySpreadConstraints` и `podDisruptionBudget`. Рекомендуемый подход см. в разделе [Настройка высокой доступности](#configure-high-availability).

Прежнее значение Helm `highAvailability` предоставляло следующие возможности:

* Увеличивает число реплик до двух для развёртывания вебхука.
* Добавляет [ограничения распределения подов по топологии](https://dt-url.net/xc03ysw):

  + Поды распределяются по разным узлам, причём узлы по возможности находятся в разных зонах.
  + В одной зоне допускается несколько подов.
* Добавляет [бюджет прерывания работы подов](https://dt-url.net/m303yfk):

  + Он ограничивает корректное завершение работы пода вебхука, если это последний оставшийся под.