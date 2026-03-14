---
title: Передача Kubernetes журналов с помощью Dynatrace модуля журнала
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes
scraped: 2026-03-06T21:25:49.968543
---

# Потоковая передача логов Kubernetes с помощью модуля логирования Dynatrace

# Потоковая передача логов Kubernetes с помощью модуля логирования Dynatrace

* Latest Dynatrace
* Руководство
* Чтение: 13 мин
* Обновлено 8 октября 2025 г.

Dynatrace обеспечивает интегрированное управление и аналитику логов для сред Kubernetes. Мы рекомендуем собирать логи в Kubernetes с помощью полностью управляемого [модуля логирования Dynatrace](../../../../ingest-from/setup-on-k8s/deployment/k8s-log-monitoring.md "Управление логами Kubernetes с помощью Dynatrace."), либо интегрированного в OneAgent, развёрнутый на узле (модуль логирования OneAgent), либо без OneAgent в виде автономного развёртывания (модуль логирования Kubernetes). Dynatrace Operator настраивает и управляет модулем логирования Dynatrace для обоих подходов. Альтернативно вы можете передавать логи в Dynatrace с помощью коллекторов логов, таких как [Fluent Bit](lma-fluent-bit-logs-k8s.md "Интеграция Fluent Bit в Kubernetes для потоковой передачи логов в Dynatrace."), [Dynatrace OpenTelemetry Collector](../../../../ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich.md "Настройка OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes."), [Logstash](../lma-stream-logs-with-logstash.md "Интеграция Logstash для потоковой передачи логов с узлов и подов в Dynatrace.") или [Fluentd](../lma-stream-logs-fluentd-k8s.md "Интеграция Fluentd с Dynatrace для потоковой передачи логов с узлов и подов в Dynatrace.").

На этой странице вы узнаете о расширенной настройке модуля логирования OneAgent и модуля логирования Kubernetes для приёма логов из Kubernetes. Чтобы узнать о различных **вариантах развёртывания, поддерживаемых платформах и средах выполнения**, см. страницу [Мониторинг логов Kubernetes](../../../../ingest-from/setup-on-k8s/deployment/k8s-log-monitoring.md "Управление логами Kubernetes с помощью Dynatrace.").

## Автоматическое обнаружение логов контейнеров Kubernetes

Модуль логирования Dynatrace автоматически обнаруживает логи, записанные в потоки **stdout/stderr** через контейнеризированные приложения, работающие в подах. Эти потоки логов хранятся в виде файлов на узлах Kubernetes, откуда модуль логирования Dynatrace может их подобрать и передать в Dynatrace. Атрибут `log source` для этих логов в Dynatrace устанавливается как `Container Output`. Атрибут `log.iostream` определяет поток логов, в который были записаны записи, например, stdout или stderr.

Модуль логирования Dynatrace не обнаруживает логи, записанные в файловую систему контейнера (в отличие от stdout/stderr). В этом случае вы можете использовать логшиппер для чтения логов из файловой системы контейнера и записи их в stdout/stderr, чтобы модуль логирования Dynatrace мог их подобрать.

Для модуля логирования OneAgent мы рекомендуем проверить флаг функции [Сбор всех логов контейнеров](lma-feature-flags.md#collect-all-container-logs "Включение или отключение определённых функций модуля логирования OneAgent и модуля логирования Dynatrace для Kubernetes.") в настройках, чтобы обеспечить наилучший охват логов в Kubernetes. Модуль логирования Kubernetes всегда собирает все логи контейнеров.

## Обогащение логов метаданными Kubernetes

Модуль логирования Dynatrace дополняет принятые логи следующими метаданными Kubernetes: `k8s.cluster.name`, `k8s.cluster.uid`, `k8s.namespace.name`, `k8s.workload.name`, `k8s.workload.kind`, `dt.entity.kubernetes_cluster`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `dt.entity.kubernetes_node`.

Кроме того, любые аннотации подов, начинающиеся с префикса `metadata.dynatrace.com/`, добавляются к записям логов.

Дополнительно вы можете использовать существующие аннотации и метки Kubernetes для обогащения логов. Подробнее см. [Обогащение метаданными для Kubernetes](../../../../ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment.md "Руководства по обогащению телеметрии в Kubernetes").

## Управление приёмом логов с помощью метаданных Kubernetes

Вы можете управлять приёмом логов из Kubernetes с помощью правил приёма логов в Dynatrace. Эти правила можно настраивать на уровне кластера Kubernetes для специфического приёма логов по кластерам. Правила используют условия сопоставления для метаданных Kubernetes и других общих атрибутов записей логов, чтобы определить, какие логи должны быть приняты.
Стандартные функции обработки логов OneAgent, включая [маскирование конфиденциальных данных](lma-sensitive-data-masking.md "Маскирование конфиденциальной информации в данных логов."), [настройку меток времени](lma-timestamp-configuration.md "Определение конкретного формата даты с помощью правил меток времени."), [определение границ записей логов](lma-log-entry-boundary.md "Определение конкретного формата даты с помощью правил меток времени.") и [автоматическое обогащение](lma-log-data-transformation-oa.md "Автоматическое преобразование данных логов для атрибута уровня лога.") записей логов, также доступны и включены здесь.

Используйте следующие рекомендуемые атрибуты сопоставления при настройке приёма логов из Kubernetes.

1

Может измениться в будущих версиях OneAgent. Будут доступны отдельные условия сопоставления для каждого типа рабочей нагрузки. Мы рекомендуем использовать имя и тип рабочей нагрузки Kubernetes.

2

Атрибут уровня записи лога, преобразованный модулем логирования Dynatrace, отличается от атрибута `status` лога, преобразованного сервером Dynatrace. Подробнее см. на странице [Автоматическое обогащение логов](lma-log-data-transformation-oa.md#transform-all-types-of-logs "Автоматическое преобразование данных логов для атрибута уровня лога.").

### Иерархия правил приёма логов

Правила приёма логов могут быть определены на уровне среды, а также на более детальном уровне, например кластера Kubernetes. Иерархия сопоставления следующая:

1. Правила конфигурации хоста;
2. Правила конфигурации кластера Kubernetes;
3. Правила конфигурации группы хостов;
4. Правила конфигурации среды.

Сопоставление выполняется в предопределённой иерархии, и правила исполняются сверху вниз. Это означает, что если правило, стоящее выше в списке, соответствует определённым данным лога, нижестоящие правила будут пропущены. Элементы, совпавшие в конфигурациях более высокого уровня, перезаписываются конфигурациями более низкого уровня, если они соответствуют тем же данным лога. Если ни одно правило не совпало, файл не отправляется.

Чтобы предотвратить непреднамеренный приём всех логов из-за правила **Ingest all**, включённого на уровне среды, мы рекомендуем добавить правило **Exclude everything** в конце конфигурации на уровне кластера. Это гарантирует, что любые несопоставленные логи будут явно исключены. Без этого правила приёма логов, определённые на уровне среды, будут далее обрабатываться модулем логирования Dynatrace, и логи будут приняты, если условия совпадут.

Ознакомьтесь с [областями конфигурации](lma-log-storage-configuration.md#configuration-scopes "Включение и исключение конкретных источников логов для хранения и анализа.") для трёх областей иерархии конфигурации.

## Сценарии использования

Изучите следующие сценарии использования для приёма логов из сред Kubernetes с помощью Dynatrace. Настраивая приём логов с различными условиями сопоставления, вы можете контролировать, какие логи фиксируются в системе. Приведённые ниже сценарии помогут настроить Dynatrace для сбора логов в соответствии с вашими конкретными потребностями мониторинга — будь то из определённого пространства имён, контейнера или по другим критериям.

Подробные инструкции по настройке приёма логов см. в [Правила приёма логов](lma-log-storage-configuration.md "Включение и исключение конкретных источников логов для хранения и анализа.").

### Приём всех логов из определённого пространства имён

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **Kubernetes namespace name**.
5. Выберите пространство имён из выпадающего списка в поле **Value** и нажмите **Add matcher**.
6. Выберите **Save changes**.

Теперь вы можете анализировать логи в средстве просмотра логов или в блокнотах после фильтрации по нужному пространству имён. Вы также можете найти логи в контексте в приложении Kubernetes, выбрав вкладку **Logs**.

### Приём логов из определённого пространства имён и контейнера

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **Kubernetes namespace name**.
5. Выберите пространство имён из выпадающего списка в поле **Value** и нажмите **Add matcher**.
6. Добавьте новое условие, на этот раз выберите **K8s container name** и введите имя контейнера в поле **Value**. Вы можете добавить несколько имён контейнеров на этом этапе настройки.
7. Выберите **Save changes**.

Теперь вы можете анализировать логи в средстве просмотра логов или в блокнотах после фильтрации по нужному пространству имён и контейнеру. Вы также можете найти логи в контексте в приложении Kubernetes, выбрав вкладку **Logs**.

### Приём всех логов Kubernetes за исключением определённых пространств имён

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **Kubernetes namespace name**.
5. Введите звёздочку (\*) в поле **Value** в качестве подстановочного символа для всех доступных пространств имён кластера.
6. Выберите **Add matcher**.
7. Выберите **Save changes**.
8. Вернувшись на экран **Log ingest rules**, добавьте ещё одно правило и выберите опцию **Exclude from storage**.
9. В поле **Value** добавьте пространства имён, которые вы хотите исключить при приёме логов Kubernetes.
10. Выберите **Add matcher**.
11. Выберите **Save changes**.

### Приём логов об ошибках из определённого кластера и пространства имён Kubernetes

1. Перейдите в приложение **Kubernetes** и выберите **Clusters**.
2. Выберите кластер, который хотите настроить.
3. Перейдите в > **Connection settings** > **Log Monitoring** > **Log ingest rules**.
4. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
5. Выберите **Add condition**.
6. В выпадающем списке **Matcher attribute** выберите **Kubernetes namespace name**.
7. Выберите одно или несколько пространств имён из выпадающего списка в поле **Value**. Вы можете ввести звёздочку (\*) в качестве подстановочного символа для всех доступных пространств имён кластера.
8. Выберите **Add matcher**.
9. Добавьте ещё одно условие и установите **Matcher attribute** как **Log record level**.
10. В выпадающем списке **Value** выберите **Error**.
11. Выберите **Add matcher**.
12. Выберите **Save changes**.

На экране **Log ingest rules** расположите настроенные правила так, чтобы правило исключения пространств имён было вверху, а правило включения всех пространств имён — внизу.

## REST API

Вы можете использовать Settings API для управления правилами приёма логов:

* Просмотр схемы;
* Список сохранённых объектов конфигурации;
* Просмотр отдельного объекта конфигурации;
* Создание нового, редактирование или удаление существующего объекта конфигурации.

Чтобы проверить текущую версию схемы для правил приёма логов, выведите список всех доступных схем и найдите идентификатор схемы `builtin:logmonitoring.log-storage-settings`.

Объекты правил приёма логов могут быть настроены для следующих областей:

* `tenant` — объект конфигурации влияет на все хосты в данной среде.
* `host_group` — объект конфигурации влияет на все хосты, назначенные данной группе хостов.
* `host` — объект конфигурации влияет только на данный хост.

Чтобы создать правило приёма логов с помощью API:

1. [Создайте токен доступа](../../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с областями **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте эндпоинт [GET a schema](../../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "Просмотр схемы настроек через Dynatrace API."), чтобы узнать формат JSON, необходимый для отправки конфигурации. Идентификатор схемы правил приёма логов (`schemaId`) — `builtin:logmonitoring.log-storage-settings`. Пример JSON-полезной нагрузки с правилами приёма логов:

   ```
   {
   "items": [
   {
   "objectId": "vu9U3hXa3q0AAAABACpidWlsdGluOmxvZ21vbml0b3JpbmcubG9nLXN0b3JhZ2Utc2V0dGluZ3MABEhPU1QAEEFEMDVFRDZGQUUxNjQ2MjMAJDZkZGU3YzY5LTMzZjEtMzNiZC05ZTAwLWZlNDFmMjUxNzUzY77vVN4V2t6t",
   "value": {
   "enabled": true,
   "config-item-title": "Send kube-system logs",
   "send-to-storage": true,
   "matchers": [
   {
   "attribute": "k8s.container.name",
   "operator": "MATCHES",
   "values": [
   "kubedns",
   "kube-proxy"
   ]
   },
   {
   "attribute": "k8s.namespace.name",
   "operator": "MATCHES",
   "values": [
   "kube-system"
   ]
   }
   ]
   }
   }
   ],
   "totalCount": 1,
   "pageSize": 100
   }
   ```

## Примеры

Приведённые ниже примеры показывают результаты различных комбинаций правил и условий сопоставления.

### Пример 1: Приём всех логов из определённого пространства имён

Для этой задачи требуется одно правило с одним условием сопоставления.

```
[{
"schemaId": "builtin:logmonitoring.log-storage-settings",
"scope": "tenant",
"value": {
"enabled": true,
"config-item-title": "All logs from kube-system namespace",
"send-to-storage": true,
"matchers": [
{
"attribute": "k8s.namespace.name",
"operator": "MATCHES",
"values": [
"kube-system"
]
}
]
}
}]
```

### Пример 2: Отправка логов из определённого пространства имён и контейнеров с содержимым, включающим 'ERROR'

Для этой задачи требуется одно правило с тремя условиями сопоставления.

```
[{
"schemaId": "builtin:logmonitoring.log-storage-settings",
"scope": "tenant",
"value": {
"enabled": true,
"config-item-title": "Error logs from kube-proxy and kube-dns containers",
"send-to-storage": true,
"matchers": [
{
"attribute": "k8s.namespace.name",
"operator": "MATCHES",
"values": [
"kube-system"
]
},
{
"attribute": "k8s.container.name",
"operator": "MATCHES",
"values": [
"kubedns",
"kube-proxy"
]
},
{
"attribute": "log.content",
"operator": "MATCHES",
"values": [
"*ERROR*"
]
}
]
}
}]
```

### Пример 3: Приём всех логов Kubernetes за исключением определённых пространств имён на уровне группы хостов

Для этой задачи требуется два правила.

```
[{
"schemaId": "builtin:logmonitoring.log-storage-settings",
"scope": "HOST_GROUP-1D91E46493049D07",
"value": {
"enabled": true,
"config-item-title": "Exclude logs from kube-system namespace",
"send-to-storage": false,
"matchers": [
{
"attribute": "k8s.namespace.name",
"operator": "MATCHES",
"values": [
"kube-system"
]
}
]
}
},{
"schemaId": "builtin:logmonitoring.log-storage-settings",
"scope": "HOST_GROUP-1D91E46493049D07",
"value": {
"enabled": true,
"config-item-title": "All Kubernetes logs",
"send-to-storage": true,
"matchers": [
{
"attribute": "k8s.namespace.name",
"operator": "MATCHES",
"values": [
"*"
]
}
]
}
}]
```

Подробнее о приёме логов см. на странице [Правила приёма логов](lma-log-storage-configuration.md#faq "Включение и исключение конкретных источников логов для хранения и анализа.").

## Устранение неполадок

Посетите Dynatrace Community для руководств по устранению неполадок, а также см. [Устранение неполадок Log Management and Analytics](../../lma-troubleshooting.md "Решение проблем, связанных с настройкой и конфигурацией Log Management and Analytics.").

* [Почему мои логи не видны в Dynatrace?](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Приём логов в K8s с Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)
