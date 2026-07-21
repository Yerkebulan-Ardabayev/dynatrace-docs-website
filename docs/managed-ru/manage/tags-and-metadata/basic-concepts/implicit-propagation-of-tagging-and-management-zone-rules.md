---
title: Неявное распространение правил тегирования и management zone
source: https://docs.dynatrace.com/managed/manage/tags-and-metadata/basic-concepts/implicit-propagation-of-tagging-and-management-zone-rules
---

# Неявное распространение правил тегирования и management zone

# Неявное распространение правил тегирования и management zone

* Объяснение
* 5 минут на чтение
* Опубликовано 18 мая 2026

При определении [правила автоматического тегирования](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") или [правила management zone](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.") для конкретного типа сущности, Dynatrace может автоматически распространить действие этого правила на связанные типы сущностей через неявное распространение. Эти пути распространения фиксированы и встроены в движок правил Dynatrace, дополнительная настройка не требуется.

Неявное распространение означает, что метаданные, применённые правилом к исходному типу сущности, автоматически наследуются одним или несколькими целевыми типами сущностей без какой-либо дополнительной настройки правил. Распространение действует и на вновь создаваемые сущности: дочерняя сущность, появившаяся после того, как правило уже активно, сразу наследует назначения родителя.

Неявное распространение запускают только правила автоматического тегирования и правила management zone. Правила условного именования и правила на основе entity selector его не запускают.

## Пути распространения

В следующей таблице перечислены все пути неявного распространения, целевые типы сущностей, наследующие метаданные, и типы правил, для которых распространение активно.

| Исходный тип сущности | Распространяется на | Доступно для | Примечания |
| --- | --- | --- | --- |
| Process group | Process group instance | Auto-tagging, Management zones | Гарантирует, что теги и назначения management zone, применённые к логической process group, автоматически доходят до её runtime-экземпляров. |
| Process group | Process group instance, Container group | Management zones | Метаданные management zone передаются экземплярам и container group, связанным с process group. |
| Process group | Container group instance | Management zones | Гарантирует, что контейнеризированные runtime-экземпляры получают данные management zone уровня process group. |
| Host | Kubernetes node | Auto-tagging, Management zones | Метаданные уровня host распространяются на узел Kubernetes, который представляет данный host. |
| Host | EC2 instance, Container group instance | Management zones | Метаданные уровня host распространяются на представления облачных инстансов и экземпляры container group, работающие на этом host. |
| Hypervisor | vCenter | Management zones | Метаданные уровня hypervisor видны на связанном объекте vCenter. |
| AWS credentials | AWS availability zone, AWS Lambda function, AWS application load balancer, AWS network load balancer, EC2 instance, Custom device, Custom device group, Auto scaling group, Relational database service | Management zones | Теги и метки уровня credentials широко распространяются на все типы ресурсов AWS, обнаруженные с использованием этих credentials. При нацеливании на сущности уровня credentials стоит ожидать широкой области распространения. |
| Cloud application | Cloud application instance | Management zones | Метаданные cloud application передаются его конкретным запущенным экземплярам. |
| Synthetic test | Application | Management zones | Метаданные synthetic test могут передаваться приложению, на которое нацелен тест. |

## Важные замечания

* **Распространение направленное и не настраиваемое.** Метаданные передаются только по перечисленным выше связям «источник → цель». Возможности отключить отдельные пути неявного распространения нет.
* **Распространение не ретроактивно при удалении правила.** Удаление правила останавливает дальнейшее распространение, но не отменяет автоматически назначение тегов или management zone, уже применённых к целевым сущностям.
* **AWS credentials имеют широкую область действия.** При применении правила тегирования или management zone к сущности AWS credentials результат одновременно распространяется на множество типов ресурсов AWS. Продумывать правила стоит внимательно, чтобы избежать непреднамеренно широких назначений.
* **Не все пути применимы к auto-tagging.** Некоторые пути неявного распространения активны только для management zone. Перед тем как полагаться на конкретный путь, стоит проверить столбец *Доступно для*.
* **Правила условного именования и на основе entity selector исключены.** Неявное распространение запускается только правилами автоматического тегирования и правилами management zone.

## Связанные темы

* [Определение и применение тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.")
* [Правила management zone](/managed/manage/identity-access-management/permission-management/management-zones/management-zone-rules "Define rules to limit the entities accessible within a management zone.")
* [Management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Лучшие практики и рекомендации по тегированию](/managed/manage/tags-and-metadata/basic-concepts/best-practices-and-recommendations-for-tagging "Learn when it's recommended to use tags that leverage auto-detected metadata, as well as best practices for enriching Dynatrace monitoring with additional metadata.")