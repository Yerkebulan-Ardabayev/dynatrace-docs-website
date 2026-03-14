---
title: Failure detection API
source: https://www.dynatrace.com/docs/dynatrace-api/configuration-api/service-api/failure-detection
scraped: 2026-03-05T21:31:58.735333
---

# Failure detection API


* Reference
* Published Jan 11, 2021

[### Список всех наборов параметров

Получить обзор всех наборов параметров для правил обнаружения сбоев.](failure-detection/parameter-set/get-all.md "View all failure detection parameter sets of your monitoring environment via the Dynatrace API.")[### Просмотр набора параметров

Просмотреть конфигурацию всех наборов параметров для правил обнаружения сбоев.](failure-detection/parameter-set/get-parameter-set.md "View a failure detection parameter set via the Dynatrace API.")

[### Создание набора параметров

Создать новый набор параметров для правил обнаружения сбоев.](failure-detection/parameter-set/post-parameter-set.md "Create a failure detection parameter set via the Dynatrace API.")

### Редактирование набора параметров

* [Обновить существующий набор параметров](failure-detection/parameter-set/put-parameter-set.md "Edit a failure detection parameter set via the Dynatrace API.") для правил обнаружения сбоев.
* [Изменить идентификатор](failure-detection/parameter-set/change-id.md "Change the ID of a failure detection parameter set via the Dynatrace API.") набора параметров.

[### Удаление набора параметров

Удалить набор параметров для правил обнаружения сбоев.](failure-detection/parameter-set/delete-parameter-set.md "Delete a failure detection parameter set via the Dynatrace API.")

[### Список всех правил

Получить обзор всех правил обнаружения сбоев.](failure-detection/detection-rules/get-all.md "View all failure detection rules of your monitoring environment via the Dynatrace API.")[### Просмотр правила

Просмотреть конфигурацию правила обнаружения сбоев.](failure-detection/detection-rules/get-rule.md "View a failure detection rule via the Dynatrace API.")[### Изменение порядка правил

Правила обнаружения сбоев оцениваются последовательно одно за другим. Применяется первое совпавшее правило, после чего дальнейшая обработка останавливается.

Измените порядок правил, чтобы добиться нужного порядка вычисления.](failure-detection/detection-rules/reorder-rules.md "Change the order of failure detection rules via the Dynatrace API.")[### Создание правила

Создать новое правило обнаружения сбоев.](failure-detection/detection-rules/post-rule.md "Create a failure detection rule via the Dynatrace API.")

### Редактирование правила

* [Обновить существующее](failure-detection/detection-rules/put-rule.md "Edit a failure detection rule via the Dynatrace API.") правило обнаружения сбоев.
* [Изменить идентификатор](failure-detection/detection-rules/change-id.md "Change the ID of a failure detection rule via the Dynatrace API.") правила.

[### Удаление правила

Удалить ненужное правило обнаружения сбоев.](failure-detection/detection-rules/delete-rule.md "Delete a failure detection rule via the Dynatrace API.")

## Связанные темы

* [Настройка обнаружения сбоев сервисов](../../../observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection.md "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")
