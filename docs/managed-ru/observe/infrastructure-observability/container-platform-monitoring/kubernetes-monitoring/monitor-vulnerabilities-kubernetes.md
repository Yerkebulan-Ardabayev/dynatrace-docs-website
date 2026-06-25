---
title: Мониторинг уязвимостей в Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes
scraped: 2026-05-12T12:07:37.263410
---

# Monitor vulnerabilities in Kubernetes/OpenShift

# Мониторинг уязвимостей в Kubernetes/OpenShift

* 1-min read
* Published Aug 24, 2022

Отслеживать уязвимости безопасности в средах Kubernetes можно на страницах кластера и нагрузок.

## Предварительные требования

* В Dynatrace перейдите на страницу настроек кластера Kubernetes и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.
* [Активируйте и включите Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")
* Для просмотра уязвимостей на уровне кода [активируйте и включите Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

## Раздел «Уязвимости»

Раздел **Vulnerabilities** отображается на следующих страницах Kubernetes:

* Страница сведений о кластере
* Страница нагрузок

В нём показаны пять наиболее серьёзных связанных [уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.") и [уязвимостей уровня кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities "Monitor the code-level vulnerabilities in your environment.").

* Выберите уязвимость для просмотра подробностей и понимания серьёзности и влияния уязвимости в вашей среде.
* Для получения полного списка обнаруженных уязвимостей в вашей среде Kubernetes выберите **Show all third-party vulnerabilities** / **Show all code-level vulnerabilities**.

Примеры уязвимостей сторонних компонентов:

![Kubernetes workload: TPV](https://dt-cdn.net/images/workload-tpv-766-510d3cb4aa.png)

Kubernetes workload: TPV

Примеры уязвимостей уровня кода:

![Kubernetes workload: CLV](https://dt-cdn.net/images/workload-clv-767-ba23d97d54.png)

Kubernetes workload: CLV

Если у вас нет [прав безопасности](/managed/secure/application-security#permissions "Access the Dynatrace Application Security functionalities.") для выбранной зоны управления:

* На странице **Kubernetes cluster** раздел **Vulnerabilities** не отображается.
* На странице **Kubernetes workload** вкладка **Vulnerabilities** на панели уведомлений показывает `Not analyzed`.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")