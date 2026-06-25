---
title: Настройка загрузки образов на узле
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull
scraped: 2026-05-12T12:03:38.167936
---

# Настройка загрузки образов на узле

# Настройка загрузки образов на узле

* Чтение: 6 мин
* Обновлено 27 января 2026 г.

Dynatrace Operator версии 1.5

cloudNativeFullStack applicationMonitoring

Функция загрузки образов на узле добавляет новые возможности для загрузки образа Dynatrace code modules, а также повышает производительность и безопасность в Dynatrace Operator. Эти улучшения обеспечивают следующие преимущества и сценарии использования:

* Мониторинг Cloud-Native Full-Stack работает независимо от CSI driver [1](#fn-1-1-def)

  + Мониторинг Cloud-Native Full-Stack можно развернуть через OpenShift OperatorHub
* Мониторинг Application работает в сочетании с публичными подписанными образами
* Сочетание внедрения Dynatrace code module без CSI и на основе CSI (подробнее см. [Принудительный мониторинг Application без CSI](#mixed-mode)) [1](#fn-1-1-def)

  + для смешанных конфигураций с доступом к узлам и без него, например AWS Elastic Kubernetes Service с узлами EC2 и Fargate
  + для использования преимуществ CSI driver, с отдельными исключениями для [инструментирования NGINX](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Узнайте, как принудительно инструментировать пропатченные/нестандартные двоичные файлы NGINX во время выполнения.")

1

Развёртывания в режиме Cloud-Native Full-Stack требуют Dynatrace Operator версии 1.6+ и OneAgent версии 1.317+.

При включённой функции загрузки образов на узле значительно упрощается нативная для Kubernetes интеграция с инструментами безопасности цепочки поставок. Кроме того, эта функция настраивает оператор всегда загружать образы через узлы Kubernetes, снижая потребность в `customPullSecret` при получении образов из частных реестров.

Развёртывания Dynatrace Operator, не использующие CSI driver, имеют повышенные требования к хранилищу из-за текущих концепций Kubernetes. О том, как минимизировать потребление хранилища, см. [Оптимизация хранилища без CSI driver](#storage-optimization).

## Предварительные требования

* Dynatrace OneAgent версии 1.311.72+

  + Рекомендуемая версия Dynatrace OneAgent: 1.317+
* Образ Dynatrace code modules, полученный из наших [поддерживаемых публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра") или вашего [частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра").

При использовании частного реестра необходимо убедиться, что все узлы аутентифицированы для доступа к реестру.

В качестве альтернативы для предоставления учётных данных реестра доступны следующие варианты:

* **С CSI driver**: можно указать `customPullSecret` в конфигурации DynaKube, чтобы предоставить необходимые учётные данные для загрузки образов.
* **Без CSI driver**: `customPullSecret` не добавляется во внедряемые поды приложений. По соображениям безопасности Dynatrace Operator не реплицирует предоставленные pull secret в пространства имён приложений и не монтирует их в поды вне контроля Dynatrace Operator. Вместо этого необходимо вручную настроить pull secret на одном из следующих уровней:

  + **Уровень узла**: настройте аутентификацию в реестре непосредственно на каждом узле.
  + **Уровень пространства имён**: добавьте pull secret в пространство имён, где развёрнуты поды приложений.
  + **Уровень пода**: настройте pull secret через поле `imagePullSecrets` в спецификации пода ваших подов приложений.

Подробнее о ручной настройке pull secret см. [документацию Kubernetes по загрузке образов из частных реестров](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).

### Ограничения

Обратите внимание, что следующие конфигурации не поддерживаются:

* Из-за того что GKE Autopilot динамически выделяет узлы и определяет их размеры на основе совокупных запросов ресурсов подов для оптимизации использования ресурсов, GKE Autopilot не подходит для функции загрузки образов на узле в сочетании с CSI driver.

  + Мы рекомендуем использовать эту функцию без CSI driver в системах GKE Autopilot или, в качестве альтернативы, использовать CSI driver в стандартной конфигурации с отключённой загрузкой образов на узле.

## Поведение и настройка

Известная проблема в Dynatrace Operator версии 1.5

Мы выявили проблему с Cloud-Native Full-Stack без использования CSI driver, подробности приведены в [примечаниях к выпуску Dynatrace Operator версии 1.5.1](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "Примечания к выпуску Dynatrace Operator версии 1.5.1.").

**Эта проблема устранена в Dynatrace Operator версии 1.6.0 и OneAgent версии 1.317+.**

Функция активируется через флаг функции в DynaKube. Следующие два пункта описывают поведение и преимущества функции в зависимости от того, был ли CSI driver развёрнут как часть оператора:

* **С CSI driver**: вместо загрузки code modules в под CSI driver образы Dynatrace code modules загружаются напрямую через узел. Каждый под CSI driver создаёт для узла задание на загрузку code modules в файловую систему хоста, где они будут использоваться CSI driver как обычно. Такой подход снижает потребность в `customPullSecret` при получении образов из частных реестров. [1](#fn-2-1-def)
* **Без CSI driver** [2](#fn-2-2-def): если CSI driver не установлен в вашем кластере, можно использовать функцию загрузки образов на узле с образом code modules для повышения производительности и устойчивости внедрения. Такой подход отдаёт приоритет производительности внедрения для более быстрого и устойчивого внедрения по сравнению с оптимизациями хранилища, обеспечиваемыми CSI driver. **Примечание:** `customPullSecret` не поддерживается функцией загрузки образов на узле при использовании без CSI driver. При использовании частных реестров необходимо вручную настроить pull secret на уровне узла, пространства имён или пода (см. [Предварительные требования](#prerequisites)).

1

Начиная с [Dynatrace Operator версии 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Примечания к выпуску Dynatrace Operator версии 1.8.0."), задания загрузки наследуют тот же `PriorityClass`, что и CSI driver, чтобы обеспечить быстрое планирование и вытеснение в перегруженных кластерах. Значение можно настроить через `csidriver.priorityClassValue` в файле значений Helm. Указания см. в [Использование priorityClass для критически важных компонентов Dynatrace](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Использование priorityClass для критически важных компонентов Dynatrace").

2

Развёртывания в режиме Cloud-Native Full-Stack требуют Dynatrace Operator версии 1.6+ и OneAgent версии 1.317+.

О том, как минимизировать потребление хранилища, см. [Оптимизация хранилища без CSI driver](#storage-optimization).

### Настройка DynaKube

Для настройки флага функции и указания образа Dynatrace code modules из [поддерживаемого публичного](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Использование публичного реестра") или [частного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра") см. следующий фрагмент DynaKube:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack:



codeModulesImage: <dynatrace-codemodules-image>
```

Известная проблема

Существует известная проблема с версиями OneAgent >= 1.313.0 и < 1.313.45. Используйте Dynatrace code modules версии 1.313.45+.

Пример тега образа для поля `codeModulesImage`:

```
public.ecr.aws/dynatrace/dynatrace-codemodules:1.313.45.20250521-164818
```

Подробнее о репозиториях и информации о тегах см. наши [поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

## Оптимизация хранилища без CSI driver

OneAgent версии 1.315+

Без CSI driver внедрение code module потребляет эфемерное хранилище при каждом внедрении. Двоичные файлы OneAgent хранятся и монтируются в под приложения в томе `emptyDir`. Чтобы минимизировать потребление хранилища, можно либо добавить аннотации к отдельным подам приложений, либо настроить этот параметр на уровне DynaKube, в зависимости от ситуации. Эти аннотации должны указывать технологию приложения (например, Java), что обеспечивает точный контроль над внедрением code module в контейнеры приложений и предотвращает копирование ненужных двоичных файлов code module.

Если CSI driver развёрнут на узле, можно также вручную настроить внедрение code module так, чтобы оно не использовало CSI driver.
Подробнее см. [Принудительный мониторинг Application без CSI](#mixed-mode).

Если оптимизация хранилища не настроена (то есть аннотация `oneagent.dynatrace.com/technologies` отсутствует), потребление хранилища будет следовать рекомендациям, изложенным в [требованиях к хранилищу](/managed/ingest-from/setup-on-k8s/reference/storage "Полный обзор требований к хранилищу для различных режимов развёртывания Dynatrace Operator в окружениях Kubernetes").

Каждая настроенная технология, указанная по отдельности или в виде списка через запятую, будет скопирована в общий том, потребляя эфемерное хранилище.

### Идентификаторы технологий

Ниже приведён список идентификаторов, которые можно использовать для каждой технологии:

| Технология | Идентификатор |
| --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга Java-приложений.") | `java` |
| [.NET, .NET Core и .NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений .NET.") | `dotnet` |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Прочитайте о поддержке Dynatrace для приложений Node.js.") | `nodejs` |
| [Python](/managed/ingest-from/technology-support/application-software/python "Узнайте, как инструментировать Python-приложение с OpenTelemetry в качестве источника данных для Dynatrace.") | `python` |
| [PHP](/managed/ingest-from/technology-support/application-software/php "Прочитайте о поддержке Dynatrace для приложений PHP.") | `php` |
| [Go](/managed/ingest-from/technology-support/application-software/go "Обзор поддержки Dynatrace для приложений Go.") | `go` |
| Apache, IBM HTTP Server | `apache` |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx "Узнайте подробности поддержки NGINX в Dynatrace.") | `nginx` |

### Добавление аннотации к поду приложения

Чтобы сократить объём данных, копируемых в поды приложений, можно указать, какие технологии OneAgent актуальны для вашего приложения. Добавьте аннотации к вашим подам приложений, как показано во фрагменте пода ниже:

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"
```

При указании списка идентификаторов технологий через запятую убедитесь, что в значении аннотации нет пробельных символов.

Значения аннотаций должны использовать точные идентификаторы технологий, перечисленные в таблице выше.

Если `oneagent.dynatrace.com/technologies` не указан, в поды приложений будут скопированы все технологии.

Если во всём кластере используется одна технология или если нужно задать технологию по умолчанию для внедрения Dynatrace code module, её можно настроить на уровне DynaKube, чтобы она применялась ко всем внедряемым подам приложений.

Настройка на уровне DynaKube

Измените конфигурацию DynaKube, включив функцию и ограничив её определённой технологией или набором из нескольких технологий:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



oneagent.dynatrace.com/technologies: "java"



spec:



...
```

При указании списка идентификаторов технологий через запятую убедитесь, что в значении аннотации нет пробельных символов.

Подробнее о репозиториях и информации о тегах см. наши [поддерживаемые публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра").

## Принудительный мониторинг Application без CSI

applicationMonitoring cloudNativeFullStack OneAgent version 1.315+

Можно выборочно настроить внедрение Dynatrace code module без участия CSI driver, даже если драйвер доступен на узле.
В этом случае внедрение code module ведёт себя так, как описано в [Оптимизация хранилища без CSI driver](#storage-optimization).

Для этого используйте аннотацию `oneagent.dynatrace.com/volume-type: "ephemeral"`, как показано в блоке кода ниже.
(Аннотация `oneagent.dynatrace.com/technologies` является дополнительной и необязательной, см. [Добавление аннотации к поду приложения](#technologies).)

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "ephemeral" # no CSI driver involved



oneagent.dynatrace.com/technologies: "nginx"    # minimize storage consumption
```

Чтобы вручную принудительно задать поведение по умолчанию, установите аннотацию `oneagent.dynatrace.com/volume-type: "csi"`.

В этом случае для работы внедрения code module на узле должен быть доступен [CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Компоненты Dynatrace Operator").

Такой подход позволяет сочетать лучшее из обоих методов: оптимизации хранилища, обеспечиваемые CSI driver, и прирост производительности и повышенную устойчивость внедрения без CSI driver для выбранных подов и приложений.

Примеры сценариев:

* [Инструментирование NGINX](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Узнайте, как принудительно инструментировать пропатченные/нестандартные двоичные файлы NGINX во время выполнения.") и предварительное внедрение рекомендуются без CSI driver для более высокой устойчивости, тогда как другие рабочие нагрузки можно внедрять с использованием CSI driver, что устраняет необходимость в каких-либо специфичных для поставщика аннотациях.
* Можно учитывать смешанные конфигурации с доступом к узлам и без него, например AWS Elastic Kubernetes Service (EKS) с узлами EC2 и Fargate. Убедитесь, что CSI driver доступен на всех узлах, где может происходить внедрение code module на основе CSI driver.