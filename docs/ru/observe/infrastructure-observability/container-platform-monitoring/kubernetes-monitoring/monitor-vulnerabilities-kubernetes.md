---
title: Мониторинг уязвимостей в Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-vulnerabilities-kubernetes
scraped: 2026-03-06T21:22:01.751523
---

# Monitor vulnerabilities in Kubernetes/OpenShift


Вы можете отслеживать уязвимости безопасности в ваших средах Kubernetes на страницах кластера и рабочих нагрузок.

## Предварительные требования

* В Dynatrace перейдите на страницу настроек вашего кластера Kubernetes и убедитесь, что включён параметр **Monitor Kubernetes namespaces, services, workloads, and pods**.
* [Активируйте и включите Application Security](../../../../secure/application-security.md "Access the Dynatrace Application Security functionalities.")
* Для просмотра уязвимостей на уровне кода [активируйте и включите Runtime Application Protection](../../../../secure/application-security/application-protection.md "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

## Раздел уязвимостей

Раздел **Vulnerabilities** отображается в Kubernetes на следующих страницах:

* Страница сведений о кластере
* Страница рабочих нагрузок (Workloads)

В нём отображаются пять наиболее серьёзных связанных [уязвимостей сторонних компонентов](../../../../secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities.md "Monitor the security issues of your third-party libraries.") и [уязвимостей на уровне кода](../../../../secure/vulnerabilities.md "Prioritize and efficiently manage vulnerabilities in your monitored environments.").

* Выберите уязвимость, чтобы просмотреть подробную информацию и оценить серьёзность и влияние уязвимости на вашу среду.
* Чтобы получить полный список обнаруженных уязвимостей для вашей среды Kubernetes, выберите **Show all third-party vulnerabilities** / **Show all code-level vulnerabilities**.

Пример уязвимостей сторонних компонентов:

![Kubernetes workload: TPV](https://dt-cdn.net/images/workload-tpv-766-510d3cb4aa.png)

Пример уязвимостей на уровне кода:

![Kubernetes workload: CLV](https://dt-cdn.net/images/workload-clv-767-ba23d97d54.png)

Если у вас отсутствуют [разрешения безопасности](../../../../secure/application-security.md#permissions "Access the Dynatrace Application Security functionalities.") для выбранной зоны управления,

* На странице **Kubernetes cluster** раздел **Vulnerabilities** не отображается.
* На странице **Kubernetes workload** вкладка **Vulnerabilities** на панели уведомлений показывает `Not analyzed`.

## Связанные темы

* [Set up Dynatrace on Kubernetes](../../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
