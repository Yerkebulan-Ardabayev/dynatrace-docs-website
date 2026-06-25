---
title: Варианты развёртывания Managed
source: https://docs.dynatrace.com/managed/managed-cluster/basics/managed-deployments
scraped: 2026-05-12T11:06:40.968782
---

# Managed deployments

# Managed deployments

* Explanation
* 5-min read
* Updated on May 08, 2026

Развёртывания Dynatrace Managed могут эволюционировать от базовой внутренней конфигурации до полностью интегрированной корпоративной архитектуры с высокой доступностью и автоматическим восстановлением. Каждый этап строится на предыдущем, добавляя компоненты по мере роста требований. На каждой диаграмме показаны задействованные компоненты и необходимые коммуникационные порты. Направление стрелки указывает, какой компонент инициирует соединение.

Сводную диаграмму всех возможных соединений и портов см. в разделе [Поддерживаемые схемы подключения для ActiveGates](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").

## Этап 1: базовая внутренняя конфигурация

Установка Dynatrace Managed с несколькими узлами кластера Managed формирует основу для всех последующих этапов развёртывания. Без дополнительной настройки кластер Managed доступен только внутри сети и открывает порт 443 для REST API, трафика OneAgent и доступа к веб-интерфейсу ([Cluster Management Console](/managed/managed-cluster/basics/cluster-management-console "Manage your Managed Cluster infrastructure, environments, users, settings, and licensing from the Cluster Management Console.") и [окружение мониторинга](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")). По умолчанию включён удалённый доступ к [Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable.") для проактивной поддержки. Каждый канал связи защищён с помощью TLS.

![Этап 1: базовое внутреннее развёртывание Dynatrace Managed с узлами кластера Managed и Mission Control](https://dt-cdn.net/images/con-man-basic-001-1200-d2345ce291.png)

Этап 1: базовое внутреннее развёртывание Dynatrace Managed с узлами кластера Managed и Mission Control

## Этап 2: внешний трафик и сервисы Digital Experience Monitoring

Расширение развёртывания за пределы внутренней сети позволяет получать данные из внешних источников: OneAgents, Environment ActiveGates или сервисов Digital Experience Monitoring (DEM). На этом этапе добавляется Environment ActiveGate для более эффективной поддержки нескольких локальных OneAgents.

Сервисы DEM могут включать:

* [Synthetic monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Agentless Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.")
* [Mobile Real User Monitoring](/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring "Learn how to set up real user monitoring for your mobile apps and use with Dynatrace Managed.")

Для получения внешнего трафика необходимо открыть кластер Managed для внешних сетей и настроить публичный IP-адрес. Прямое подключение кластера Managed к внешним сетям не рекомендуется по соображениям безопасности. Вместо этого следует использовать один или несколько [Cluster ActiveGates](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.") в качестве посредников для предварительной обработки трафика OneAgent и DEM. Cluster ActiveGates распознаются кластером Managed и могут быть настроены через Cluster Management Console аналогично узлам кластера Managed.

![Этап 2: развёртывание Dynatrace Managed, расширенное Cluster ActiveGates для внешнего трафика OneAgent и DEM](https://dt-cdn.net/images/con-man-pure-005-1200-f44d093c51.png)

Этап 2: развёртывание Dynatrace Managed, расширенное Cluster ActiveGates для внешнего трафика OneAgent и DEM

Веб-интерфейс доступен по HTTPS, для чего требуется TLS-сертификат. Можно использовать самоподписанный сертификат, однако для безопасного трафика веб-интерфейса и администрирования кластера рекомендуется предоставить доменное имя и действующий SSL-сертификат или позволить Dynatrace сгенерировать их автоматически. По умолчанию каждый кластер Managed получает поддомен вида `*.dynatrace-managed.com` с действующим сертификатом от Let's Encrypt.

Для каждого Cluster ActiveGate требуется:

* Публично доступный IP-адрес

  Необходим для приёма трафика из внешних источников.
* Доменное имя с действующим [SSL-сертификатом](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")

  Внешняя связь поддерживается только по HTTPS (порт 443). Домен должен отличаться от домена веб-интерфейса Dynatrace. Можно предоставить собственный домен и SSL-сертификат или позволить Dynatrace сгенерировать их. Cluster ActiveGates не поддерживают проксирование трафика веб-интерфейса.

Для высоконагруженных инсталляций с большим количеством внешних хостов, приложений, сессий и синтетических мониторов следует настроить несколько Cluster ActiveGates с балансировкой нагрузки, использующих одно доменное имя и один сертификат.

По умолчанию Environment ActiveGate подключается напрямую к кластеру Managed (если не используются пользовательские сетевые зоны). Настройте подключение через Cluster ActiveGate, если кластер Managed недоступен напрямую из сети Environment ActiveGate.

Если Environment ActiveGate подключается к кластеру Managed через Cluster ActiveGate, то Cluster ActiveGate должен быть работоспособен, доступен и настроен с подходящим IP-адресом (локальным или публичным) до начала установки.

## Этап 3: интеграция с существующей инфраструктурой

При встраивании Dynatrace Managed в существующую ИТ-инфраструктуру можно задействовать уже имеющиеся устройства. На диаграмме показан балансировщик нагрузки, предоставленный клиентом, перед доменом Cluster ActiveGate, и прокси-сервер, предоставленный клиентом, для исходящего трафика к Mission Control.

![Этап 3: развёртывание Dynatrace Managed, интегрированное с балансировщиком нагрузки клиента и исходящим прокси](https://dt-cdn.net/images/con-man-integr-005-1200-6b2f5c5afb.png)

Этап 3: развёртывание Dynatrace Managed, интегрированное с балансировщиком нагрузки клиента и исходящим прокси

## Этап 4: высокая доступность с автоматическим восстановлением

Развёртывание с высокой доступностью охватывает распределённые сети и обеспечивает почти нулевое время простоя, непрерывный мониторинг без потери данных при переключении при отказе, а также экономию за счёт исключения резервных хостов восстановления и инфраструктуры для передачи резервных копий. При планировании ёмкости узлы дополнительного центра обработки данных следует рассматривать как резервные, а не как расширение основной ёмкости, и обеспечивать равномерную нагрузку между обоими центрами. Подробнее см. в разделе [Premium high availability](/managed/managed-cluster/high-availability "Understand how Dynatrace Managed achieves high availability through data replication, node redundancy, and multi-data center failover.").

![Этап 4: развёртывание Dynatrace Managed с Premium High Availability, охватывающее два центра обработки данных](https://dt-cdn.net/images/con-man-global-005-1200-aa4bbfc45b.png)

Этап 4: развёртывание Dynatrace Managed с Premium High Availability, охватывающее два центра обработки данных

## Требования к конфигурации по типу трафика

Каждый тип трафика имеет различные требования к сетевому доступу и сертификатам. Хотя Real User Monitoring (RUM), agentless RUM и mobile RUM, как правило, относятся к трафику из-за пределов вашей сети, те же требования применяются, когда этот трафик поступает из внутренней сети.

| Тип трафика | Публичный IP | Действующий SSL-сертификат |
| --- | --- | --- |
| OneAgent (локальный) |  |  |
| OneAgent (внешний) | обязателен |  |
| RUM (локальный) |  |  |
| RUM (внешний) |  |  |
| Agentless RUM (локальный) |  | обязателен |
| Agentless RUM (внешний) | обязателен | обязателен |
| Mobile RUM (локальный) |  | обязателен |
| Mobile RUM (внешний) | обязателен | обязателен |
| Synthetic | обязателен |  |

[Agentless Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), [мониторинг мобильных приложений](/managed/offline-doc/how-do-i-set-up-mobile-apps-for-real-user-monitoring "Learn how to set up real user monitoring for your mobile apps and use with Dynatrace Managed.") и [синтетические мониторы](/managed/offline-doc/how-do-i-enable-synthetic-monitors "Learn how to enable synthetic monitors on Dynatrace Managed.") используют одну и ту же конечную точку для передачи данных мониторинга в Dynatrace Managed.