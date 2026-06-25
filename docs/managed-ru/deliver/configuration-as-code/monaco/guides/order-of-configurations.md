---
title: Обеспечение порядка конфигураций
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/guides/order-of-configurations
scraped: 2026-05-12T12:03:00.691578
---

# Ensure order of configurations

# Ensure order of configurations

* How-to guide
* 2-min read
* Updated on Jul 14, 2023

Данное руководство показывает, как обеспечить порядок конфигураций с помощью Dynatrace Configuration as Code через Monaco (Dynatrace Monaco CLI).

## Цель

Хотя веб-интерфейс позволяет определять порядок определённых конфигураций, это невозможно сделать через Dynatrace Monaco CLI или Dynatrace API.

* При прямом использовании API можно управлять добавлением правил в начало или конец списка, но не точным порядком.
* В Dynatrace Monaco CLI такое управление недоступно.

Однако можно использовать механизм обработки зависимостей между конфигурациями в Dynatrace Monaco CLI для обеспечения порядка правил.

## Определение порядка правил с помощью зависимостей

Создавая фиктивные зависимости между правилами, Dynatrace Monaco CLI гарантирует, что правило будет создано до другого правила, зависящего от него. Это обходное решение работает только в случае, если все правила создаются из Dynatrace Monaco CLI и ещё не существуют.

Если правила уже существуют, их можно переупорядочить вручную — будущие развёртывания конфигурации не повлияют на порядок.

Поскольку новые правила добавляются в начало перед существующими, зависимости, вероятно, потребуется определять в обратном порядке по отношению к ожидаемому. Следующий пример демонстрирует обеспечение порядка с помощью зависимостей.

Рассмотрим пример с файлом `config.yaml`, содержащим два правила обнаружения приложений: `rule1` и `rule2`.

```
configs:



- id: rule2



config:



name: rule2



template: rule2.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment



- id: rule1



config:



name: rule1



template: rule1.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment
```

В процессе развёртывания `rule2`, вероятно, будет развёрнуто до `rule1`. Однако чтобы гарантировать, что `rule1` всегда развёртывается до `rule2`, можно ввести псевдо-параметр ссылки внутри `rule2`, указывающий на его зависимость от `rule1`. Это обеспечивает развёртывание `rule2` после `rule1`.

```
configs:



- id: rule2



config:



name: rule2



template: rule2.json



skip: false



parameters:



order:



configId: rule1



property: id



type: reference



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment



- id: rule1



config:



name: rule1



template: rule1.json



skip: false



type:



settings:



schema: builtin:rum.web.app-detection



schemaVersion: 2.0.1



scope: environment
```