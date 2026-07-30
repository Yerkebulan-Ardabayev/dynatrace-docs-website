---
title: Обновление ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/operation/update-activegate
---

# Обновление ActiveGate

# Обновление ActiveGate

* Практическое руководство
* 5 мин. чтения
* Обновлено 14 июля 2026 г.

Ограничения

**Auto-update** и ручное действие **Update now** поддерживают только хостовые развёртывания, установленные с помощью установщика.

* [Поведение ActiveGate в контейнере при обновлении](/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences#auto-update "Learn how containerized ActiveGate differs from host-based ActiveGate")

## Просмотр установленных ActiveGate и статуса обновления

Чтобы посмотреть список установленных ActiveGate, перейдите в **Deployment Status** > **ActiveGates**. Для каждого ActiveGate в списке отображаются текущая **Version** и **Update status** (up to date, pending или in progress).

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Жёлтый значок предупреждения означает, что ActiveGate отстаёт более чем на пять версий. Такие ActiveGate нужно обновить как можно скорее.

ActiveGate в контейнерах разворачиваются и загружаются с помощью облачных инструментов. Например, Kubernetes использует [custom resource definitions](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

### Автоматическое обновление

Чтобы управлять функцией обновления конкретного ActiveGate в списке, выберите ActiveGate для раскрытия подробностей.

## Настройка автоматических обновлений

Чтобы настроить порядок обновления Environment ActiveGate:

* Перейдите в **Settings** > **Deployment** > **ActiveGate updates**.

### Режим обновления

Режим обновления определяет, когда Environment ActiveGate применяет ожидающее обновление.

* **Automatic (earliest convenience)** (по умолчанию для новых сред):
  ActiveGate загружает и устанавливает новые версии сразу после их появления. Проверка доступности запускается каждые 30 минут.
* **Automatic (during update window)**:
  ActiveGate обновляется только в течение настроенного [окна обновления](/managed/ingest-from/dynatrace-oneagent/oneagent-update#maintenance-windows "Learn how to update OneAgent."). Обновления, ставшие доступными вне активного окна, откладываются до его открытия. Одни и те же окна обновления управляют как OneAgent, так и ActiveGate; см. раздел [Окна обновления](#update-windows) ниже.
* **No automatic updates**:
  ActiveGate не обновляется самостоятельно. Если задана [целевая версия](#target-version) и ActiveGate находится на более старой версии, обновление можно запустить вручную в настройках обновления этого конкретного ActiveGate. См. раздел [Update now to target version](#update-now-to-target-version) ниже.

Для существующих сред режим обновления сохраняет прежнее поведение: если auto-update был включён, он становится **Automatic (earliest convenience)**; если был выключен, становится **No automatic updates**.

### Целевая версия

Выбирает, на какую версию ActiveGate должен перейти Dynatrace.

* **Latest stable** (по умолчанию):
  Самая новая стабильная версия ActiveGate, доступная на кластере.
* **Previous stable**:
  На одну основную версию ниже последней стабильной.
* **Older stable**:
  На две основные версии ниже последней стабильной.
* **Specific main version** (например, `1.327`):
  Фиксирует ActiveGate на выбранной основной версии. Dynatrace автоматически применяет последнюю дополнительную версию этой основной версии. В отличие от OneAgent, ActiveGate не предоставляет выбор дополнительной версии; всегда применяется последняя дополнительная версия выбранной основной версии.

Рядом с каждым стабильным пресетом в селекторе отображается текущая основная версия (например, `Latest stable (currently 1.343)`), чтобы было видно, какую сборку резолвит каждый пресет.

**Environment** [Deployment API](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-latest "Download the latest ActiveGate installer via Dynatrace API.") рассматривает настроенную целевую версию как последнюю доступную для среды. Защита build-unit не позволяет кластеру удалить установщик для любой версии, настроенной в качестве целевой.

Откат запрещён: настроенная целевая версия никогда не используется для возврата ActiveGate к более низкой версии.

### Окна обновления

Окна обновления настраиваются один раз и используются совместно OneAgent и Environment ActiveGate. Информацию о создании, изменении, включении, отключении, удалении и применении окон см. в разделе [Configure update windows](/managed/ingest-from/dynatrace-oneagent/oneagent-update#maintenance-windows "Learn how to update OneAgent.") на странице обновления OneAgent.

Когда одно окно применяется к ActiveGate, Dynatrace ограничивает количество одновременных обновлений в пуле (см. раздел [Параллелизм и безопасность](#concurrency-and-safety) ниже).

### Иерархия области действия

Настройки auto-update ActiveGate следуют данному порядку переопределения:

1. Настройки отдельного ActiveGate (настроены для конкретного ActiveGate в **Settings** > **Deployment** > **ActiveGate updates**)
2. Настройки по умолчанию Environment

По умолчанию (новая установка среды) ActiveGate обновляются при первой возможности до последней подходящей версии.

### Update now to target version

Устаревшее действие Update now

Устаревшее действие **Update now**, которое принудительно обновляло Environment ActiveGate немедленно без выбора версии и поддержки окон обновления, объявлено устаревшим. Оно заменено функциональностью целевой версии, режима обновления и окна обновления, описанной на этой странице. Переходите на новую конфигурацию auto-update, чтобы сохранить контроль над обновлениями ActiveGate.

Обновление отдельного ActiveGate вручную выполняется в его собственных настройках обновления, а не в общих настройках среды: откройте настройки **ActiveGate updates** для нужного ActiveGate. Для ActiveGate с режимом **No automatic updates**, версия которого старше настроенной **целевой версии**, в настройках отображается версия, до которой будет выполнено обновление, и доступна кнопка **Update now to target version**. Нажмите кнопку, чтобы немедленно запустить обновление.

**Update now to target version** недоступно, если настроенная целевая версия не может быть определена (например, сборка больше не присутствует на кластере).

### Параллелизм и безопасность

Чтобы сохранить пропускную способность маршрутизации для отслеживаемых хостов, Dynatrace ограничивает количество одновременных обновлений ActiveGate в каждом **пуле**. Пул определяется сочетанием сетевой зоны, группы ActiveGate и назначения ActiveGate (например, маршрутизация по умолчанию или synthetic). По умолчанию:

* Если пул содержит **два и более** ActiveGate, **одновременно обновляется не более одного**. Остальные ActiveGate ожидают завершения текущего обновления (или истечения его окна отслеживания).
* Если пул содержит **только один** ActiveGate, он обновляется без ожидания: резервного варианта нет.
* ActiveGate в **разных** пулах (например, в разных сетевых зонах или группах) могут обновляться параллельно, поскольку каждый пул регулируется независимо.

Дополнительные меры защиты:

* Dynatrace обновляет только те ActiveGate, у которых включён auto-update.
* Предварительные проверки перед обновлением валидируют совместимость до его применения.
* В случае сбоя обновления ActiveGate автоматически откатывается к предыдущей рабочей версии.
* Результат обновлений (успех или сбой) отображается через существующие каналы оповещения Dynatrace и значения [статуса обновления](#update-status) в **Deployment Status** > **ActiveGates**.

### Ограничения и область применения

* [Контейнеризированные ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container/differences#auto-update "Learn how containerized ActiveGate differs from host-based ActiveGate") не поддерживают режим обновления, целевую версию и окна обновления: их жизненным циклом управляет среда выполнения контейнера.
* [Cluster ActiveGate](/managed/managed-cluster/operation/update-dynatrace-managed-activegate "Learn about manual and one-click cluster ActiveGate updates.") обновляются вместе с Dynatrace Managed и не используют эти настройки.
* Multi-environment ActiveGate следуют конфигурации своей **основной среды**.

### Программный доступ

* Настроить auto-update программно можно через [ActiveGate auto-update configuration API](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API.").
* Схема окна обновления определена в [`builtin:deployment.management.update-windows`](/managed/dynatrace-api/environment-api/settings/schemas/builtin-deployment-management-update-windows "View builtin:deployment.management.update-windows settings schema table of your monitoring environment via the Dynatrace API.").
* Эндпоинты Environment Deployment API [download-activegate-latest](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-latest "Download the latest ActiveGate installer via Dynatrace API.") (который также охватывает `…/latest/metainfo`) и [download-activegate-version](/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-version "Download the ActiveGate installer of the specific version via Dynatrace API.") учитывают настроенную целевую версию.

## Ручная загрузка и обновление

### Загрузка и обновление вручную

Также можно загрузить и обновить ActiveGate вручную. Удалять текущую версию ActiveGate не нужно. Достаточно установить новую версию поверх старой, и конфигурация ActiveGate будет перенесена.

* [Установить Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate").

При обновлении конфигурация ActiveGate сохраняется в файлах `custom.properties` и `launcheruserconfig.conf`. Эти два файла не перезаписываются при обновлении, но перед обновлением ActiveGate рекомендуется создать их резервные копии.

* Свойства файла `custom.properties` описаны в разделе [Настройка ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований.").
* Свойства `launcheruserconfig.conf` описаны в разделе [Настройка launcher ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований.").

## Статус обновления

Dynatrace Classic

Статус обновления ActiveGate может принимать следующие значения:

**Up to date**  
На соответствующем хосте установлена последняя доступная версия ActiveGate.

**Update available**  
Для данной версии ActiveGate доступно обновление.

**Update pending**  
Сразу после нажатия **Update ActiveGate** статус меняется на **Update pending** и остаётся таким до начала процесса обновления.
Статус также может быть указан как `pending` в следующих случаях:

* Кластер в данный момент обновляется.
* Достигнуто максимальное количество одновременных загрузок обновлений, и ActiveGate ожидает возможности возобновить загрузку.

**Update in progress**  
ActiveGate запросил и загрузил новый установочный пакет с сервера и в данный момент выполняет его установку или восстанавливает соединение с сервером.

**Update problem**  
В этом случае для ActiveGate отображается старый номер версии.  
Возможные причины:

* ActiveGate загрузил новый установщик, но установка не была выполнена или завершилась с ошибкой; в результате ActiveGate по-прежнему работает на старой версии.
  Следует проверить журналы автообновления ActiveGate и журналы установщика для выяснения причины, по которой установка не была выполнена или завершилась с ошибкой.
* ActiveGate загрузил новый установщик, но затем потерял соединение с сервером (был потерян).
  Следует проверить журналы установщика ActiveGate для выяснения причины сбоя установки.
* Для ActiveGate нет доступных установщиков.
* Обновление приостановлено, так как на другом Environment возникли проблемы с обновлением до предложенной версии ActiveGate.

**Unknown**  
Соединение с этим ActiveGate потеряно, и определить статус невозможно.  
Этот статус также может отображаться, если ActiveGate был успешно удалён; в этом случае удалённый ActiveGate продолжает отображаться со статусом обновления `Unknown` в течение семи дней.