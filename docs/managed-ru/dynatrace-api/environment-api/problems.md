---
title: Problems API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/problems
scraped: 2026-05-12T11:38:33.700956
---

# Problems API v1

# Problems API v1

* Reference
* Updated on Jun 13, 2022
* Deprecated

Этот API устарел. Используйте [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Узнайте, что предлагает Dynatrace Problems v2 API.") вместо него.

API **Problems** возвращает детали о [problems](/managed/dynatrace-intelligence "Знакомство с возможностями Davis AI."), которые Dynatrace обнаруживает в вашем окружении. Одна проблема обычно содержит сводную информацию, анализ влияния и список событий, скоррелированных с этой проблемой.

[### Количество проблем

Узнайте, сколько открытых проблем существует.](/managed/dynatrace-api/environment-api/problems/problems/get-status "Просмотр статуса проблемы через Problems v1 API.")[### Получить ленту проблем

Получить высокоуровневые детали открытых проблем.](/managed/dynatrace-api/environment-api/problems/problems/get-feed "Получение списка проблем через Problems v1 API.")[### Получить детали проблемы

Когда нашли проблему для расследования, получите подробные сведения о ней.](/managed/dynatrace-api/environment-api/problems/problems/get-details "Просмотр деталей проблемы через Problems v1 API.")[### Закрыть проблему

Когда проблема перестала быть актуальной, закройте её и добавьте закрывающий комментарий одним запросом.](/managed/dynatrace-api/environment-api/problems/problems/post-close "Закрытие проблемы и добавление закрывающего комментария через Problems v1 API.")

[### Список комментариев

Просмотр всех комментариев к проблеме.](/managed/dynatrace-api/environment-api/problems/comments/get-all "Просмотр всех комментариев к проблеме через Problems v1 API.")[### Добавить комментарий

Добавить комментарий к указанной проблеме.](/managed/dynatrace-api/environment-api/problems/comments/post-comment "Добавление комментария к проблеме через Problems v1 API.")

[### Редактировать комментарий

Редактировать комментарий к указанной проблеме.](/managed/dynatrace-api/environment-api/problems/comments/put-comment "Редактирование комментария к проблеме через Problems v1 API.")[### Удалить комментарий

Удалить комментарий из указанной проблемы.](/managed/dynatrace-api/environment-api/problems/comments/del-comment "Удаление комментария к проблеме через Problems v1 API.")

## Связанные темы

* [DavisÂ® AI](/managed/dynatrace-intelligence "Знакомство с возможностями Davis AI.")