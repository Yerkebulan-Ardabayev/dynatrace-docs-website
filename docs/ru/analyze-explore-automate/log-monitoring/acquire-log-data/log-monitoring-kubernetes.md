---
title: Log Monitoring in Kubernetes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes
scraped: 2026-03-06T21:37:52.324824
---

# Мониторинг логов в Kubernetes (Logs Classic)

# Мониторинг логов в Kubernetes (Logs Classic)

* Classic
* Руководство
* Время чтения: 10 мин
* Обновлено 08 октября 2025

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Потоковая передача логов Kubernetes с помощью Dynatrace Log Module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace поддерживает сбор данных логов из систем оркестрации контейнеров Kubernetes через OneAgent Log Module или Kubernetes Log Module.").

Dynatrace Log Monitoring поддерживает сбор логов из систем оркестрации контейнеров Kubernetes через OneAgent.

В качестве альтернативы сбору логов на основе OneAgent вы можете передавать логи в Dynatrace через [API приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api "Потоковая передача данных логов в Dynatrace с помощью API для преобразования их в осмысленные сообщения логов.") с использованием интеграции, такой как [Fluent Bit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Интеграция Fluent Bit для потоковой передачи логов в Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Интеграция Fluentd с Dynatrace для потоковой передачи логов из узлов и подов в Dynatrace."), [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Интеграция Logstash для потоковой передачи логов из узлов и подов в Dynatrace.") или [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Узнайте о Dynatrace OTel Collector.").

## Поддерживаемые возможности

Dynatrace Log Monitoring поддерживает различные контейнерные платформы на основе Kubernetes, такие как Upstream Kubernetes или Red Hat OpenShift, использующие **containerd** или **CRI-O** в качестве среды выполнения контейнеров.

**Docker** не соответствует CRI — интерфейсу среды выполнения контейнеров. По этой причине конфигурации Kubernetes, использующие **Docker**, поддерживаются лишь частично. Kubernetes объявил **Docker** устаревшим в качестве среды выполнения контейнеров после версии v1.20.

Подробнее о поддерживаемых версиях Kubernetes см. [Поддержка и известные проблемы Dynatrace Operator](/docs/ingest-from/technology-support/support-model-and-issues "Как Dynatrace поддерживает версии Kubernetes и Red Hat OpenShift, а также известные проблемы").

## Автоматическое обнаружение логов Kubernetes

OneAgent автоматически обнаруживает логи, записываемые контейнеризированным приложением в потоки **stdout**/**stderr**. Kubernetes Engine сохраняет эти потоки логов в файл на узле Kubernetes. OneAgent автоматически обнаруживает эти файлы логов и передаёт логи контейнера под источником `Container Output`.

Логи, записываемые непосредственно в файловую систему пода, не обнаруживаются OneAgent. В этом случае используйте интеграцию для доставки логов, например Fluent Bit.

## Обогащение логов метаданными Kubernetes

Модуль логов OneAgent дополняет принимаемые логи следующими метаданными Kubernetes: `k8s.cluster.name`, `k8s.cluster.uid`, `k8s.namespace.name`, `k8s.workload.name`, `k8s.workload.kind`, `dt.entity.kubernetes_cluster`, `k8s.pod.name`, `k8s.pod.uid`, `k8s.container.name`, `dt.entity.kubernetes_node`. Эти метаданные используются для сопоставления логов с моделью сущностей кластеров, пространств имён, рабочих нагрузок и подов Kubernetes.

Также любые аннотации подов, начинающиеся с префикса `metadata.dynatrace.com/`, добавляются к записям логов.

Подробнее см. [Обогащение метаданными для Kubernetes](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Руководства по обогащению телеметрии в Kubernetes").

### Управление приёмом логов с помощью метаданных Kubernetes

Вы можете управлять приёмом логов из Kubernetes с помощью правил приёма логов в Dynatrace. Вы можете настроить эти правила на уровне кластера Kubernetes для обеспечения приёма логов, специфичного для кластера. Правила используют сопоставители для метаданных Kubernetes и других общих атрибутов записей логов для определения того, какие логи должны приниматься.
Стандартные функции обработки логов OneAgent, включая [маскирование конфиденциальных данных](/docs/analyze-explore-automate/log-monitoring/methods-of-masking-sensitive-data "Выберите оптимальный метод для маскирования конфиденциальных данных."), [настройку временных меток](/docs/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration "Определение правил мониторинга логов, управляющих временными метками данных логов.") и [автоматическое обогащение](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation "Универсальный приём логов автоматически преобразует данные логов в выходные значения для атрибута loglevel.") записей логов, также доступны и включены здесь.

Используйте следующие рекомендуемые атрибуты сопоставления при настройке приёма логов из Kubernetes.

1

Может измениться в будущих версиях OneAgent. Будут доступны отдельные сопоставители для каждого вида рабочей нагрузки. Мы рекомендуем использовать имя рабочей нагрузки Kubernetes и вид рабочей нагрузки Kubernetes вместо этого.

2

Атрибут уровня записи лога, преобразованный модулем логов OneAgent, отличается от атрибута `status` лога, преобразованного сервером Dynatrace. Подробнее на странице [Автоматическое обогащение логов](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation#transform-all-types-of-logs "Универсальный приём логов автоматически преобразует данные логов в выходные значения для атрибута loglevel.").

## Настройка приёма логов из Kubernetes

Приём логов из Kubernetes требует определения правил приёма логов. Конфигурация основана на иерархии правил, использующих сопоставители для атрибутов Kubernetes и других общих атрибутов записей логов. Эти правила определяют, какие файлы логов среди обнаруженных OneAgent должны приниматься.

Используйте следующие рекомендуемые атрибуты сопоставления при настройке приёма логов из Kubernetes.

1

Атрибут уровня записи лога, преобразованный OneAgent, отличается от атрибута `status` лога, преобразованного сервером Dynatrace. Подробнее на странице [Автоматическое обогащение логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Универсальный приём логов автоматически преобразует данные логов в выходные значения для атрибута loglevel.").

2

Минимальная требуемая версия OneAgent — 1.273.

Вы также можете использовать следующие общие атрибуты сопоставления при настройке приёма логов из Kubernetes.

### Иерархия правил приёма логов

Правила приёма логов могут быть определены на уровне окружения, а также на уровне хоста или группы хостов. Иерархия сопоставления следующая:

1. Правила конфигурации хоста;
2. Правила конфигурации группы хостов;
3. Правила конфигурации тенанта.

Сопоставление происходит в предопределённой иерархии, и правила выполняются сверху вниз. Это означает, что если правило выше в списке соответствует определённым данным логов, то нижестоящие правила будут пропущены. Элементы, сопоставленные в конфигурациях более высокого уровня, перезаписываются в конфигурациях более низкого уровня, если они соответствуют тем же данным логов. Если ни одно правило не совпало, файл не отправляется.

Ознакомьтесь с [Областями конфигурации](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#configuration-scopes "Включение и исключение определённых источников логов, уже известных OneAgent, для хранения и анализа.") для четырёх областей иерархии конфигурации.

## Сценарии использования

Изучите следующие сценарии использования для приёма логов из окружений Kubernetes с помощью Dynatrace. Настраивая приём логов с различными сопоставителями, вы можете управлять тем, какие логи захватываются в системе. Приведённые ниже сценарии содержат рекомендации по настройке Dynatrace для захвата логов в соответствии с вашими конкретными потребностями мониторинга, будь то из определённого пространства имён, контейнера или по другим критериям.

### Приём всех логов из определённого пространства имён

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **K8s namespace name**.
5. Выберите пространство имён из выпадающего списка в поле **Value** и нажмите **Add matcher**.
6. Выберите **Save changes**.

Теперь вы можете анализировать логи в средстве просмотра логов или ноутбуках, отфильтровав нужное пространство имён. Вы также можете найти логи в контексте в приложении Kubernetes, выбрав вкладку **Logs**.

### Приём логов из определённого пространства имён и контейнера

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **K8s namespace name**.
5. Выберите пространство имён из выпадающего списка в поле **Value** и нажмите **Add matcher**.
6. Добавьте новый сопоставитель, на этот раз выберите **K8s container name** и введите имя контейнера в поле **Value**. Вы можете добавить несколько имён контейнеров на этом шаге настройки.
7. Выберите **Save changes**.

Теперь вы можете анализировать логи в средстве просмотра логов или ноутбуках, отфильтровав нужное пространство имён и контейнер. Вы также можете найти логи в контексте в приложении Kubernetes, выбрав вкладку **Logs**.

### Приём всех логов Kubernetes за исключением определённых пространств имён

1. Перейдите в **Settings** и выберите **Log Monitoring** > **Log ingest rules**.
2. Выберите **Add rule** и укажите имя конфигурации в поле **Rule name**.
   Убедитесь, что кнопка **Include in storage** включена, чтобы логи, соответствующие этой конфигурации, сохранялись в Dynatrace.
3. Выберите **Add condition**.
4. В выпадающем списке **Matcher attribute** выберите **K8s namespace name**.
5. Вставьте звёздочку (\*) в поле **Value** как подстановочный знак для всех доступных пространств имён кластера.
6. Выберите **Add matcher**.
7. Выберите **Save changes**.
8. Вернувшись на экран **Log ingest rules**, добавьте ещё одно правило и выберите опцию **Exclude from storage**.
9. В поле **Value** добавьте пространства имён, которые вы хотите исключить при приёме логов Kubernetes.
10. Выберите **Add matcher**.
11. Выберите **Save changes**.

На экране **Log ingest rules** расположите настроенные правила так, чтобы правило исключения пространств имён было наверху, а правило включения всех пространств имён — внизу.

## REST API

Вы можете использовать Settings API для управления правилами приёма логов:

* Просмотр схемы;
* Список сохранённых объектов конфигурации;
* Просмотр одного объекта конфигурации;
* Создание нового, редактирование или удаление существующего объекта конфигурации.

Чтобы проверить текущую версию схемы для правил приёма логов, просмотрите список всех доступных схем и найдите идентификатор схемы `builtin:logmonitoring.log-storage-settings`.

Объекты правил приёма логов могут быть настроены для следующих областей:

* `tenant` — объект конфигурации влияет на все хосты данного тенанта.
* `host_group` — объект конфигурации влияет на все хосты, назначенные данной группе хостов.
* `host` — объект конфигурации влияет только на данный хост.

Чтобы создать правило приёма логов с помощью API:

1. [Создайте токен доступа](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Узнайте, как пройти аутентификацию для использования Dynatrace API.") с областями **Write settings** (`settings.write`) и **Read settings** (`settings.read`).
2. Используйте конечную точку [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "Просмотр схемы настроек через Dynatrace API."), чтобы узнать формат JSON, необходимый для отправки конфигурации. Идентификатор схемы правил приёма логов (`schemaId`) — `builtin:logmonitoring.log-storage-settings`. Вот пример полезной нагрузки JSON с правилами приёма логов:

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

Приведённые ниже примеры демонстрируют результаты различных комбинаций правил и сопоставителей.

### Пример 1: Приём всех логов из определённого пространства имён

Эта задача требует настройки одного правила с одним сопоставителем.

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

### Пример 2: Отправка логов из определённого пространства имён и контейнеров с содержимым, содержащим 'ERROR'

Эта задача требует настройки одного правила с тремя сопоставителями.

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

### Пример 3: Приём всех логов Kubernetes за исключением определённых пространств имён в области конкретной группы хостов

Эта задача требует настройки двух правил.

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

## Часто задаваемые вопросы

Каковы предварительные требования для автоматического обнаружения и приёма логов Kubernetes через OneAgent?

Требования для автоматического обнаружения и приёма логов Kubernetes следующие:

* Используется среда выполнения контейнеров **containerd** или **CRI-O**;
* Процесс, работающий в контейнере, является [важным процессом](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Отображение наиболее важных процессов для мониторинга и группировки процессов.");
* Логи записываются в потоки **stdout**/**stderr** контейнера;
* Файл лога на узле Kubernetes существует не менее одной минуты после завершения выполнения контейнера.

Можно ли дополнять логи метками и аннотациями Kubernetes?

Нет, OneAgent пока не предоставляет такой функциональности, хотя это запланировано в будущих выпусках.

Для получения дополнительных часто задаваемых вопросов о приёме данных ознакомьтесь со страницей [Правила приёма логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration#faq "Включение и исключение определённых источников логов, уже известных OneAgent, для хранения и анализа.").

## Устранение неполадок

Посетите сообщество Dynatrace для получения руководств по устранению неполадок, а также см. [Устранение неполадок Log Monitoring (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/lmc-troubleshooting "Исправление проблем, связанных с настройкой и конфигурацией Log Monitoring Classic.").

* [Почему мои логи не отображаются в Dynatrace?](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [Приём логов в K8s с Dynatrace](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)
