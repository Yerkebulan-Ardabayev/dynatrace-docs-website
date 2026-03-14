---
title: Тома контейнеризованного ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container/ag-container-persistence
scraped: 2026-03-02T21:29:57.548368
---

# Тома контейнеризованного ActiveGate


* Latest Dynatrace
* 3-min read
* Published Sep 01, 2023

Во время работы контейнер ActiveGate записывает данные в определённые каталоги корневой файловой системы.

## Доступные для записи каталоги

### Требования к размеру

Сведения об ориентировочных требованиях к размеру для каждого каталога см. в разделе [Каталоги ActiveGate](../configuration/where-can-i-find-activegate-files.md "Узнайте, где хранятся файлы ActiveGate в системах Windows и Linux.").

## Усиленная безопасность

[Пример развёртывания](../activegate-in-container.md#deployment-example "Развернуть контейнеризованный ActiveGate.") ActiveGate защищён для минимизации возможных атак: параметр `securityContext.readOnlyRootFilesystem` установлен в значение `true`.

Это предотвращает изменение контейнером содержимого образа, поэтому [каталоги](#directories) необходимо настраивать с использованием томов.

### Контекст безопасности

```
securityContext:


allowPrivilegeEscalation: false


capabilities:


drop:


- all


privileged: false


readOnlyRootFilesystem: true


runAsNonRoot: true


seccompProfile:


type: RuntimeDefault
```

### Тома

```
volumeMounts:


- name: server-certs-storage


mountPath: /var/lib/dynatrace/gateway/ssl


- name: ag-lib-gateway-config


mountPath: /var/lib/dynatrace/gateway/config


- name: ag-lib-gateway-temp


mountPath: /var/lib/dynatrace/gateway/temp


- name: ag-lib-gateway-data


mountPath: /var/lib/dynatrace/gateway/data


- name: ag-log-gateway


mountPath: /var/log/dynatrace/gateway


- name: ag-tmp-gateway


mountPath: /var/tmp/dynatrace/gateway
```

Информацию о размерах томов см. в разделе [Требования к хранилищу ActiveGate](../installation/linux/linux-activegate-hardware-and-system-requirements.md#space-requirements "Узнайте, какие требования к оборудованию и операционной системе необходимо учитывать перед установкой ActiveGate на Linux для целей маршрутизации и мониторинга.").
