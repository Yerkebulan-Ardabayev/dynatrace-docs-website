---
title: Проактивная поддержка Mission Control
source: https://docs.dynatrace.com/managed/managed-cluster/basics/mission-control-proactive-support
scraped: 2026-05-12T11:08:25.759496
---

# Проактивная поддержка Mission Control

# Проактивная поддержка Mission Control

* Explanation
* 3-min read
* Updated on May 08, 2026

Dynatrace Managed проактивно отслеживается и удалённо управляется командой Dynatrace Mission Control, чтобы ваш Managed Cluster оставался безопасным, надёжным и актуальным. После предоставления необходимых разрешений команда Mission Control может удалённо получить доступ к вашему Managed Cluster для помощи с обновлениями и устранением неполадок. Вы полностью контролируете настройки конфиденциальности данных.

Подробности см. в [Dynatrace Managed Mission Control и Соглашении об уровне обслуживания](https://www.dynatrace.com/company/trust-center/sla/managed/?_ga=2.93129118.22206741.1563254436-509254238.1563254436).

## Как работает Mission Control

Managed Cluster автоматически отправляет [данные самомониторинга и лицензирования](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category.") в Mission Control. На основе этих данных команда Mission Control может проактивно анализировать и выявлять неправильные конфигурации или потенциальные несовместимости в вашей установке Managed. Команда Mission Control никогда не имеет доступа к вашей операционной системе или файловой системе, не связанным с установкой Managed.

При наличии соответствующих разрешений команда Mission Control может отслеживать качество обслуживания и использование аппаратного обеспечения в вашей установке Managed и уведомлять вас в случае необходимости дополнительных ресурсов. Команда Mission Control также может настраивать конфигурацию вашей установки Managed для обеспечения наивысшего качества обслуживания и наилучшего использования предоставленного оборудования. Все изменения конфигурации полностью фиксируются в журнале аудита, а вы полностью контролируете [настройки конфиденциальности данных](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences and privacy settings").

Mission Control предоставляет обновления программного обеспечения для Managed Cluster. Эти обновления являются обязательными и, как правило, выпускаются каждые четыре недели. Вы можете настроить [время обновлений](/managed/managed-cluster/operation/update-cluster "Learn how to update a Managed cluster and how to schedule an automatic update.") в соответствии с вашими потребностями.

## Что происходит при потере подключения к Mission Control

Для обеспечения проактивной поддержки вашей установки Managed требуется постоянное подключение к Mission Control. При прерывании соединения критически важные запросы (например, запросы биллинга или проверки лицензии) будут автоматически повторно отправлены после восстановления подключения.

Поведение Managed Cluster при прерывании подключения зависит от модели лицензирования.

| Модель лицензирования | Поведение кластера при прерывании подключения |
| --- | --- |
| [Классическое лицензирование](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") | Если прерывание подключения к Mission Control длится более 14 дней (7 дней для бесплатных пробных аккаунтов), Managed Cluster запрещает возможность превышения лимита лицензии (overage). Однако мониторинг ваших приложений в рамках лицензионных квот не зависит от прерывания подключения.  Например: если приобретена лицензия на 10 хостов и overage ещё на 2 хоста, можно отслеживать 10 хостов в течение всего срока действия лицензии. Только overage больше не разрешены. |
| [Dynatrace Platform Subscription](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") | При потере подключения к Mission Control Managed Cluster собирает данные об использовании и отправляет их в Mission Control сразу после восстановления соединения. Мониторинг ваших приложений не зависит от прерывания подключения. |

## Связанные темы

* [Обмен данными с Mission Control](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category.")