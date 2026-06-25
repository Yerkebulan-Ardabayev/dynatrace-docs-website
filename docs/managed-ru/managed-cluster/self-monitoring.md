---
title: Самомониторинг
source: https://docs.dynatrace.com/managed/managed-cluster/self-monitoring
scraped: 2026-05-12T11:11:13.823617
---

# Самомониторинг

# Самомониторинг

* Published Nov 17, 2021

Для обеспечения высочайшего качества проактивной поддержки Dynatrace собирает статистику работоспособности, метрики производительности и данные об использовании служб со всех компонентов развёртывания Dynatrace Managed — OneAgent, ActiveGate (включая расширения) и узлов кластера. Dynatrace Managed обеспечивает готовые многоуровневые данные о работоспособности и производительности развёртывания кластера через самомониторинг. Данные самомониторинга:

* Хранятся как метрики самомониторинга во всех ваших средах мониторинга.
* Хранятся в выделенной локальной среде самомониторинга.
* Отправляются в Dynatrace Mission Control для наблюдения и улучшения продукта.
* Хранятся удалённо в выделенной премиум-среде самомониторинга Dynatrace (только для Enterprise Success and Support).

Вы можете в любое время отказаться от отправки данных самомониторинга в Dynatrace. Этот параметр варьируется в зависимости от вашего лицензирования. Если этот параметр отключён и вы хотите его изменить, обратитесь к эксперту Dynatrace через онлайн-чат. Конфигурация и обмен данными подробно описаны в разделе [Hosted самомониторинг-среда](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Learn how to use hosted self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.").

Для доступа к данным самомониторинга кластера Dynatrace Managed доступны следующие варианты:

### Локальный самомониторинг

Каждый кластер Dynatrace Managed включает выделенную локальную среду самомониторинга, собирающую внутренние метрики работоспособности развёртывания. Эта среда является полноценной доступной средой Dynatrace. Она содержит все метрики самомониторинга, собранные и агрегированные из других сред вашего кластера Dynatrace Managed. Данные хранятся исключительно локально на вашем кластере.

Этот тип самомониторинга обеспечивает высокоуровневые метрики работоспособности и производительности в готовом виде с полным контролем над местом хранения данных и доступом к ним. Подробности см. в разделе [Локальный самомониторинг](/managed/managed-cluster/self-monitoring/local-self-monitoring "Learn how to use local self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.").

### Hosted самомониторинг

Dynatrace предлагает возможность настройки премиум-среды самомониторинга в кластере Dynatrace SaaS. Эта SaaS-среда размещается Dynatrace и отслеживает ваш кластер Dynatrace Managed.

Поддержка

Hosted самомониторинг доступен только для клиентов Enterprise Success and Support.

Этот тип самомониторинга обеспечивает детальные аналитические данные и метрики, управление доступом, данные в среде Dynatrace и наивысший уровень персонализированной проактивной поддержки. Подробности см. в разделе [Hosted самомониторинг-среда](/managed/managed-cluster/self-monitoring/hosted-self-monitoring "Learn how to use hosted self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.").

### Приватный самомониторинг

Если вы отказались от мониторинга работоспособности развёртывания Dynatrace, можно самостоятельно установить OneAgent на узлы кластера. Они будут отчитываться перед выбранной вами средой на том же или другом кластере. Этот вариант потребляет ваши лицензии Dynatrace соответствующим образом.

Этот тип самомониторинга обеспечивает детальные аналитические данные и метрики с полным контролем над местом хранения данных и доступом к ним. Однако уровень проактивной поддержки ограничен, и для него требуется дополнительное лицензирование. Подробности см. в разделе [Приватная самомониторинг-среда](/managed/managed-cluster/self-monitoring/private-self-monitoring "Learn how to set up and configure a private self-monitoring environment to gain additional insights into your Dynatrace Managed cluster health.").