---
title: Kubernetes Security Posture Management
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/security-posture-management
scraped: 2026-03-03T21:32:50.568498
---

# Kubernetes Security Posture Management

# Kubernetes Security Posture Management

* Последняя версия Dynatrace
* Практическое руководство
* 5 мин. чтения
* Обновлено 3 ноября 2025 г.

Dynatrace Kubernetes Security Posture Management позволяет обнаруживать, анализировать и отслеживать неправильные конфигурации, рекомендации по усилению безопасности и потенциальные нарушения соответствия в вашем развёртывании Kubernetes.

Как это работает

Dynatrace принимает конфигурационные данные из ваших кластеров и рабочих нагрузок в [Grail](/docs/platform/grail "Информация о том, что и как можно запрашивать в данных Dynatrace."), где они форматируются в [события соответствия](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.") в соответствии с соглашениями [Семантического словаря](/docs/semantic-dictionary/model/security-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.").

Механизм описан ниже.

![Диаграмма, показывающая, как Security Posture Management работает в Kubernetes](https://dt-cdn.net/images/kspm-how-it-works-v3-1027-60596036f8.png)

1. KSPM настраивается Dynatrace Operator для сбора данных

После включения Dynatrace Kubernetes Node Configuration Collector в Dynatrace Operator он развёртывается как DaemonSet на узлах вашего отслеживаемого кластера для сбора конфигурационных данных кластера и рабочих нагрузок.

2. Данные собираются

* Node Configuration Collector собирает данные с узлов кластера.

  + Частота: каждую минуту
* ActiveGate собирает данные из Kubernetes API.

  + Частота: каждый час

3. Данные отправляются в Dynatrace Cluster

ActiveGate обрабатывает все данные, полученные от узлов и Kubernetes API, и отправляет их в Dynatrace Cluster.

4. Данные сопоставляются

Этот раздел был обновлён в соответствии с новой таблицей событий безопасности Grail. Полный список обновлений и действий, необходимых для выполнения миграции, см. в [руководстве по миграции таблицы безопасности Grail](/docs/secure/threat-observability/migration "Узнайте об изменениях в новой таблице безопасности Grail и о том, как выполнить миграцию.").

Конфигурационные данные кластера и рабочих нагрузок сопоставляются как [события соответствия](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.") в соответствии с [Семантическим словарём](/docs/semantic-dictionary/model/security-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.") и хранятся в бакете `default_securityevents_builtin` (подробнее см. [Встроенные бакеты Grail](/docs/platform/grail/organize-data#built-in-grail-buckets "Информация о модели данных Grail, состоящей из бакетов, таблиц и представлений.")).

5. Результаты соответствия готовы к использованию

После приёма данных в Grail вы можете анализировать состояние безопасности ваших кластеров и оценивать соответствие отраслевым стандартам. Подробнее см. [Что дальше](#next).

## Предварительные требования

Dynatrace версии 1.305+ Dynatrace Operator версии 1.5.0+ ActiveGate версии 1.321+

* [Security Posture Management](/docs/secure/application-security/spm "Оценка, управление и реагирование на неправильные конфигурации и нарушения стандартов безопасности и нормативного соответствия.") лицензируется на основе потребления [хост-часов](/docs/license/capabilities/application-security/security-posture-management "Узнайте, как рассчитывается потребление Dynatrace Security Posture Management (SPM) DPS.") и требует [модели лицензирования Dynatrace Platform Subscription (DPS)](/docs/license "О Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace.").

  Если вы используете [классическое лицензирование Dynatrace](/docs/license/monitoring-consumption-classic "Узнайте, как рассчитывается потребление мониторинга Dynatrace при классическом лицензировании.") или если вы на DPS, но не видите возможность SPM в вашей тарифной карте DPS, пожалуйста, свяжитесь с экспертом Dynatrace через чат.
* Ознакомьтесь с [поддерживаемыми стандартами соответствия и технологиями](/docs/secure/application-security/spm#support "Оценка, управление и реагирование на неправильные конфигурации и нарушения стандартов безопасности и нормативного соответствия.").
* [Настройте мониторинг Kubernetes](/docs/ingest-from/setup-on-k8s "Способы развёртывания и настройки Dynatrace в Kubernetes").

* Поддержка ограничена совместимостью с основной версией Kubernetes и доступна только для процессорных архитектур x86-64.
* Количество реплик подов ActiveGate должно быть установлено в 1 (по умолчанию).
* Если вы используете Dynatrace Operator версии ранее 1.4.0, необходимо [обновить](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#helm "Процедуры обновления и удаления Dynatrace Operator") перед продолжением.

## Развёртывание

Ниже описано, как [настроить](#setup) и [включить](#enable) Kubernetes Security Posture Management.

### Настройка Dynatrace Kubernetes Node Configuration Collector

1. Создание секрета

Если вы уже создали секрет с токеном при предыдущем развёртывании Dynatrace Operator, этот шаг можно пропустить.

1. Создайте токен Dynatrace Operator.

   Инструкции см. в [Токены доступа и разрешения](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга вашего кластера Kubernetes").
2. Создайте секрет для хранения токена доступа, который будет использоваться Dynatrace Operator для связи со средой Dynatrace.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
   ```

2. Настройка DynaKube

1. Создайте пользовательский ресурс DynaKube (минимальная версия `apiVersion: dynatrace.com/v1beta4`), убедившись, что включены следующие параметры:

   * Kubernetes Security Posture Management:

     + `spec.kspm: {}`: Включает DaemonSet KSPM Node Configuration Collector (подробнее см. [Как это работает](/docs/secure/application-security/spm#mechanism "Оценка, управление и реагирование на неправильные конфигурации и нарушения стандартов безопасности и нормативного соответствия."))

     KSPM по умолчанию монтирует корневую файловую систему хоста. Если вы хотите ограничить это определёнными путями, используйте поле `spec.kspm.mappedHostPaths`. Поле `spec.kspm.mappedHostPaths` определяет пути хоста, которые монтируются в контейнер. Список рекомендуемых путей см. в [примере репозитория Dynatrace Operator](https://dt-url.net/ky03zzm).
   * ActiveGate с мониторингом Kubernetes и дополнительной конфигурацией:

     + `spec.activeGate.capabilites`: Должен содержать `kubernetes-monitoring`

       1. Конфигурация для ActiveGate версий ранее 1.311

       Для ActiveGate версий ранее 1.311 убедитесь, что включены следующие параметры:

       - `spec.activeGate.capabilites`: Должен содержать `kubernetes-monitoring`
       - `spec.activeGate.customProperties`: Должен содержать следующее:

         ```
         [kubernetes_monitoring]



         kubernetes_configuration_dataset_pipeline_enabled = true



         kubernetes_configuration_dataset_pipeline_include_node_config = true
         ```
   * Шаблоны с образом Kubernetes Security Posture Management:

     ```
     spec:



     ...



     templates:



     kspmNodeConfigurationCollector:



     imageRef:



     repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



     tag: <tag>
     ```

     Для получения информации о тегах посетите [публичный реестр](https://dt-url.net/4p03ueu).
   * Tolerations для развёртывания Node Configuration Collector на узлах управляющего слоя и мастер-узлах

     + `.spec.templates.kspmNodeConfigurationCollector.tolerations`

   Рекомендации по настройке свойств см. в [Добавление файла пользовательских свойств](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Добавление файла пользовательских свойств").

   Список всех доступных параметров см. в [Параметры DynaKube для Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

   **Пример DynaKube**:

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   tokens: <secret-token>



   kspm:



   mappedHostPaths:



   - /boot



   - /etc



   - /proc/sys/kernel



   - /sys/fs



   - /sys/kernel/security/apparmor



   - /usr/lib/systemd/system



   - /var/lib



   activeGate:



   capabilities:



   - kubernetes-monitoring



   templates:



   kspmNodeConfigurationCollector:



   imageRef:



   repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



   tag: <tag>



   tolerations:



   - effect: NoSchedule



   key: node-role.kubernetes.io/master



   operator: Exists



   - effect: NoSchedule



   key: node-role.kubernetes.io/control-plane



   operator: Exists
   ```

   1. Пример DynaKube для ActiveGate версий ранее 1.311

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   kspm:



   mappedHostPaths:



   - /boot



   - /etc



   - /proc/sys/kernel



   - /sys/fs



   - /sys/kernel/security/apparmor



   - /usr/lib/systemd/system



   - /var/lib



   activeGate:



   capabilities:



   - kubernetes-monitoring



   customProperties:



   value: |



   [kubernetes_monitoring]



   kubernetes_configuration_dataset_pipeline_enabled = true



   kubernetes_configuration_dataset_pipeline_include_node_config = true



   templates:



   kspmNodeConfigurationCollector:



   imageRef:



   repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



   tag: <tag>
   ```
2. Примените пользовательский ресурс DynaKube.

   ```
   kubectl apply -f dynakube.yaml
   ```

3. Проверка конфигурации

1. Проверьте статус вашего пользовательского ресурса DynaKube.

   ```
   kubectl get dks -n dynatrace
   ```

   1. Ожидаемый результат

   Статус DynaKube — `Running`.

   ```
   NAME       APIURL                  STATUS    AGE



   dynakube   <environment-api-url>   Running   3m48s
   ```
2. Проверьте статус развёртывания DaemonSet Node Configuration Collector.

   ```
   kubectl get daemonset -n dynatrace -l app.kubernetes.io/component=kspm
   ```

   1. Ожидаемый результат

   Все поды в состоянии `READY`.

   ```
   NAME                             DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR   AGE



   dynakube-node-config-collector   3         3         3       3            3           <none>          11m
   ```
3. Проверьте статус развёртывания StatefulSet ActiveGate.

   ```
   kubectl get statefulset -n dynatrace -l app.kubernetes.io/component=activegate
   ```

   1. Ожидаемый результат

   ActiveGate в состоянии `READY`.

   ```
   NAME                  READY   AGE



   dynakube-activegate   1/1     14m
   ```

### Включение Kubernetes Security Posture Management

Вы можете включить Kubernetes Security Posture Management в **Settings** для каждой среды или для каждого кластера. Инструкции приведены ниже.

Включение KSPM для среды

Включение KSPM для кластера

Чтобы включить Kubernetes Security Posture Management для всех отслеживаемых кластеров:

1. Перейдите в **Settings Classic** и выберите **Application Security** > **Security Posture Management**.
2. В разделе **Kubernetes** выберите **Enable Security Posture Management**.

Чтобы включить Kubernetes Security Posture Management для конкретного отслеживаемого кластера:

1. Откройте **Kubernetes** ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)").
2. Перейдите в **Clusters** и выберите кластер, для которого хотите включить Security Posture Management.
3. В правом верхнем углу выберите , затем выберите **Settings**.
4. В меню **Open with** выберите **Settings Classic**.
5. Выберите **Security Posture Management**, затем выберите **Enable Security Posture Management**.
6. Для проверки конфигурации выберите **Test configuration**.

## Что дальше

После настройки Kubernetes Security Posture Management вы можете использовать:

* [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Обнаружение, управление и реагирование на находки безопасности и соответствия.") для анализа состояния безопасности ваших кластеров и оценки соответствия отраслевым стандартам
* [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Объединение функций Grail для расследований на основе фактов, включая разрешение инцидентов, анализ первопричин и поиск угроз.") для запроса [событий соответствия](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Ознакомьтесь с моделями Семантического словаря, связанными с событиями безопасности.") для получения дополнительной аналитики
* [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь аналитическими данными наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.") для обмена отчётами о находках с заинтересованными сторонами

## Ограничения

Kubernetes Security Posture Management может охватывать до 100 узлов и 3000 подов на кластер Kubernetes.

## Дополнительные ресурсы

* Пример сценария использования см. в [Соблюдение соответствия с Security Posture Management](/docs/secure/use-cases/stay-compliant "Контроль мер безопасности, политик и практик.").
* Список часто задаваемых вопросов о Kubernetes Security Posture Management см. в [FAQ](/docs/secure/application-security/spm#faq "Оценка, управление и реагирование на неправильные конфигурации и нарушения стандартов безопасности и нормативного соответствия.").
* Список примеров DQL на основе событий соответствия для дальнейшего расследования или отчётности см. в [Запрос событий соответствия](/docs/secure/threat-observability/dql-examples#compliance "Примеры DQL для данных безопасности на основе Grail.").
* Обзор использования данных безопасности см. в [Данные безопасности в Grail](/docs/secure/threat-observability/concepts#security-data "Основные концепции Threat Observability").

## Связанные темы

* [Security Posture Management](/docs/secure/xspm "Обнаружение, управление и реагирование на находки безопасности и соответствия.")