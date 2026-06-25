---
title: Управление проектом Monaco
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/monaco/configuration/projects
scraped: 2026-05-12T12:02:52.411398
---

# Manage a Monaco project

# Manage a Monaco project

* Explanation
* 3-min read
* Updated on Nov 24, 2025

Проект — это папка, содержащая подпапки со специальными именами, представляющие API. Папки API содержат ещё один уровень папок, определяющих конфигурации. Папки конфигурации содержат YAML-файлы, задающие, что будет развёрнуто.

## API

Для получения списка всех поддерживаемых API и имён папок см. [Типы конфигурации и права доступа](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco").

## Конфигурации

Конфигурация состоит из двух частей:

* YAML-файл, определяющий параметры, зависимости, имя и шаблон
* JSON-файл шаблона

### Файл конфигурации YAML

Файл конфигурации YAML содержит базовую информацию о развёртываемой конфигурации: имя конфигурации, расположение файла шаблона и параметры, доступные в файле шаблона. Параметры можно переопределять в зависимости от текущей группы или окружения развёртывания.

### Файл шаблона JSON

Шаблон JSON содержит полезную нагрузку, которая будет загружена в конечные точки Dynatrace API. В нём можно ссылаться на все определённые параметры конфигурации с помощью синтаксиса `{{ .PARAMETER_NAME }}`. Например:

`template.json`:

```
{



"name": "{{ .name }}",



"type": "{{ .type }}",



"value": {{ .numericValue }}



}
```

`config.yaml`:

```
configs:



- id: sample



config:



name: "Sample"



parameters:



type: "simple"



numericValue: 42



[...]
```

Как видно, можно также ссылаться на имя конфигурации.

Dynatrace Monaco CLI использует шаблоны Go, которые теоретически позволяют создавать более сложные шаблоны, однако **настоятельно** рекомендуется сохранять шаблоны максимально простыми. Ссылок на переменные через `{{ .PARAMETER_NAME }}` должно быть достаточно.

Подробнее о продвинутых сценариях использования шаблонов см. [Продвинутые сценарии с шаблонами Go](/managed/deliver/configuration-as-code/monaco/guides/configuration-as-code-advanced-use-case "Effectively utilize Go templating in projects with Dynatrace Configuration as Code via Monaco.").

Некоторые конфигурации используют те же символы шаблонизации, что и Dynatrace Monaco CLI: `{{ ... }}`.

Символы шаблонизации в нужных JSON-файлах необходимо экранировать следующим образом:

* `{{` заменяется на `` {{`{{`}} ``
* `}}` заменяется на `` {{`}}`}} ``

При использовании [`monaco download`](/managed/deliver/configuration-as-code/monaco/reference/commands#download "Command reference for Dynatrace Configuration as Code via Monaco (Dynatrace Monaco CLI)") эти символы будут экранированы автоматически для всех типов конфигурации.

Например:

```
{



"value": "{{someValue}}"



}
```

становится:

```
{



"value": "{{`{{`}}someValue{{`}}`}}"



}
```