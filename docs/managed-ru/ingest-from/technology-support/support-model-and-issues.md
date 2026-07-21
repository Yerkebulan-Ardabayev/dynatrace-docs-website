---
title: Поддержка и известные проблемы Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/support-model-and-issues
---

# Поддержка и известные проблемы Dynatrace Operator

# Поддержка и известные проблемы Dynatrace Operator

* 5 минут чтения
* Обновлено 04 марта 2026 г.

Dynatrace предлагает поддержку Kubernetes вскоре после выхода нового релиза Kubernetes или OpenShift. Как только становятся доступны кандидаты релиза Kubernetes/OpenShift, Dynatrace тестирует эти версии, включая последние версии OneAgent, ActiveGate и Dynatrace Operator.

В таблице ниже перечислены проверенные и протестированные версии релизов:

| Версия Kubernetes upstream | Версия OpenShift | Минимальная версия OneAgent | Минимальная версия ActiveGate | Минимальная версия Dynatrace Operator | Рекомендуемая версия Dynatrace Operator | Окончание поддержки (Kubernetes) | Окончание поддержки (OpenShift) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.36 |  | 1.335 | 1.335 | v1.6.x | v1.9.0+ | 1 июля 2028 г. |  |
| 1.35 | 4.22[4](#fn-1-4-def) | 1.329 | 1.329 | v1.6.x | v1.9.0+ | 1 апреля 2028 г. | 1 ноября 2028 г. |
| 1.34 | 4.21[4](#fn-1-4-def) | 1.321 | 1.321 | v1.6.x | v1.9.0+ | 1 ноября 2027 г. | 1 октября 2028 г. |
| 1.33 | 4.20[4](#fn-1-4-def) | 1.319 | 1.319 | v1.1.x | v1.9.0+ | 1 июля 2027 г. | 1 марта 2028 г. |
| 1.32 | 4.19[4](#fn-1-4-def) | 1.309 | 1.309 | v1.1.x | v1.9.0+ | 1 марта 2027 г. | 1 марта 2028 г. |
| 1.31 | 4.18[3](#fn-1-3-def) | 1.297 | 1.297 | v1.1.x | v1.9.0+ | 1 января 2027 г. | 1 августа 2028 г. |
| 1.30 | 4.17[3](#fn-1-3-def) | 1.291 | 1.291 | v1.1.x | v1.9.0+ | 1 августа 2026 г. | 1 июля 2027 г. |
| 1.29 | 4.16[3](#fn-1-3-def) | 1.281 | 1.281 | v0.14.x | v1.9.0+ | 1 марта 2026 г. | 1 сентября 2027 г. |
| 1.28 | 4.15 | 1.275 | 1.275 | v0.12.x | v1.9.0+ | 1 ноября 2025 г. | 1 ноября 2026 г. |
| 1.27 | 4.14 | 1.269 | 1.269 | v0.10.x | v1.9.0+ | 1 июля 2025 г. | 1 ноября 2026 г. |

1

Новая версия Go, используемая в Dynatrace Operator, несовместима с версией CRI-O в OpenShift 4.8 и Kubernetes 1.21.

2

Для Kubernetes 1.22 и 1.23 рекомендуется Dynatrace Operator версии 1.0.1. Для OpenShift 4.8 и выше предлагается обновление до версии 1.1.0+.

3

[Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "Подробное описание Classic Full-Stack monitoring с использованием Dynatrace Operator.") поддерживается только на worker-узлах, работающих под управлением Red Hat Enterprise Linux. Если worker-узлы вместо этого работают под управлением Red Hat Enterprise Linux CoreOS, поддерживается только [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с использованием Dynatrace Operator.").

4

Поддерживаются только [Application observability](/managed/ingest-from/setup-on-k8s/how-it-works/application-monitoring "Подробное описание Application observability с использованием Dynatrace Operator.") и [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с использованием Dynatrace Operator."). Причина в том, что worker-узлы могут работать только под управлением Red Hat Enterprise Linux CoreOS. Подробнее см. в [примечаниях к релизу Red Hat (1.5.13.2)﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).

Полная поддержка предоставляется до тех пор, пока версия Kubernetes или OpenShift не достигнет конца жизненного цикла. После этого Dynatrace предоставляет поддержку в режиме обслуживания примерно в течение одного года. Даты окончания поддержки объявляются в разделе [Объявления об окончании поддержки](/managed/whats-new/technology/end-of-support-news#dto "Объявления об окончании поддержки технологий, поддерживаемых Dynatrace.").

Главное отличие между полной поддержкой и поддержкой в режиме обслуживания в том, что Dynatrace сокращает объём ежедневных тестовых работ в период поддержки в режиме обслуживания.

В периоды полной поддержки и поддержки в режиме обслуживания каждая обнаруженная ошибка проходит оценку на предмет бэкпорта. В зависимости от серьёзности и риска изменений исправление либо переносится (бэкпортится) и выпускается с патч-версией, либо исправляется в следующей версии. Подробности см. в соответствующих [примечаниях к релизу Dynatrace](/managed/whats-new "Читайте новости продукта и примечания к релизам, а также узнавайте, какие разделы документации появились недавно.").

## Поддержка Dynatrace Operator

Dynatrace Operator доступен на следующих архитектурах:

* x86
* ARM
* ppc64le
* s390x [1](#fn-2-1-def)

1

Поддерживаются только [cloud native full stack deployment](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Развёртывание Dynatrace Operator в режиме cloud-native full-stack в Kubernetes"), [application monitoring](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме application monitoring в Kubernetes") и [host monitoring](/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring "Развёртывание Dynatrace Operator в режиме host monitoring в Kubernetes").

В случаях, когда проблемы, связанные с Dynatrace Operator, не удаётся воспроизвести силами Dynatrace на архитектурах x86 или ARM и они определены как специфичные для ppc64le, нужно обратиться по адресу `dt-operator@ibm.com` за дальнейшей поддержкой. Дополнительную информацию можно найти в соответствующем открытом pull request для Dynatrace Operator на [GitHub﻿](https://dt-url.net/ev034k3).

Dynatrace Operator отвечает за развёртывание и управление жизненным циклом различных компонентов Dynatrace в Kubernetes и OpenShift (включая ActiveGate и OneAgent). Dynatrace Operator, это проект с открытым исходным кодом, поддерживаемый на [GitHub﻿](https://dt-url.net/d7034gj). Он следует схеме семантического версионирования `major.minor.patch` ([semantic versioning﻿](https://semver.org/)), с выпуском минорных версий примерно каждые 2–3 месяца.

Три последние версии Dynatrace Operator тестируются с последними версиями Kubernetes и OpenShift. Кроме того, для каждой ошибки или уязвимости выполняется оценка на предмет бэкпорта, чтобы проанализировать серьёзность и риск изменений исправления. Рекомендуется использовать последнюю патч-версию, поскольку новые реализованные функции увеличивают минорную версию. Подробности см. в [примечаниях к релизу Dynatrace Operator](/managed/whats-new/dynatrace-operator "Примечания к релизу Dynatrace Operator").

Все версии Dynatrace Operator, которые не считаются достигшими конца жизненного цикла, рассматриваются как находящиеся в режиме обслуживания, что включает обычные процессы поддержки клиентов. Версии в режиме обслуживания не получают исправлений ошибок и бэкпортов уязвимостей. См. объявления об окончании поддержки в разделе [Объявления об окончании поддержки](/managed/whats-new/technology/end-of-support-news#dto "Объявления об окончании поддержки технологий, поддерживаемых Dynatrace.").

## Известные проблемы и их решения

Список известных проблем для версий Dynatrace Operator и их влияния на различные компоненты. Эти проблемы присутствуют в выпущенных версиях Dynatrace Operator, и для их устранения может потребоваться обновление минорной версии!

### Внедрение компонентов Dynatrace

Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1 Dynatrace Operator версии 1.7.2

#### Проблема

* Из-за оптимизации внедряемых точек монтирования (их объединения под `/var/lib/dynatrace`) компоненты Dynatrace больше не могут внедряться с помощью OneAgent.

* Компоненты Dynatrace содержат конфигурацию в `/var/lib/dynatrace`, которая скрывается точками монтирования, добавляемыми при внедрении через Webhook.

По умолчанию мониторинг для пространства имён Dynatrace Operator (а значит, и компонентов Dynatrace) не включён. Проблема может проявиться, если флаг функции `feature.dynatrace.com/ignored-namespaces` используется для переопределения игнорируемых пространств имён с включением в них пространства имён Dynatrace Operator.

#### Решение

Настроить аннотацию pod'а `dynatrace.com/split-mounts` (требуется Dynatrace Operator версии 1.8.0+) на затронутых pod'ах.

### Classic full-stack с обогащением метаданных

Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1 Dynatrace Operator версии 1.7.2

#### Проблема

* Classic full-stack и обогащение метаданных несовместимы и не могут использоваться для внедрения в одни и те же pod'ы приложений.

И OneAgent, и внедрение через Webhook пытаются добавить точку монтирования в каталог `/var/lib/dynatrace` в pod'е приложения. Эти точки монтирования несовместимы и не могут сосуществовать.

#### Решение

Все версии Dynatrace Operator 1.7 не поддерживаются.

Для версий Dynatrace Operator 1.8+ и версий 1.6 и более ранних может потребоваться дополнительная настройка:

* Если версия OneAgent ниже 1.333, настроить отладочный флаг `remountOperatorEnrichment`.
* Если версия OneAgent 1.333+, этот отладочный флаг OneAgent не требуется.

### Определение доступности хоста

Dynatrace Operator версии 1.6.0 Dynatrace Operator версии 1.6.1 Dynatrace Operator версии 1.6.2 Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1

#### Проблема

* В средах Kubernetes, особенно использующих автомасштабирование, надёжно определить, был ли узел удалён намеренно или вышел из строя неожиданно, затруднительно. Эта неоднозначность может приводить к большому числу ложноположительных оповещений «Host is unavailable», что влияет на точность мониторинга и качество оповещений.

#### Решение

Обновиться до Dynatrace Operator версии 1.7.2+ или 1.6.3.

### Переход на загрузку образа Node с образом Code modules

Dynatrace Operator версии 1.5.0 Dynatrace Operator версии 1.5.1 Dynatrace Operator версии 1.6.0 Dynatrace Operator версии 1.6.1 Dynatrace Operator версии 1.6.2

#### Проблема

При переходе с использования CSI-драйвера без `codeModulesImage` на использование его с [загрузкой образа на узле](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), нужно убедиться, что в файловой системе CSI-драйвера нет code module для указанного DynaKube. Если он есть, CSI-драйвер выйдет из строя и потребуется ручное вмешательство для восстановления.

* Если возникла эта проблема, откат к варианту без `codeModulesImage` снова сделает CSI-драйвер работоспособным.
* Можно использовать команду `find`, чтобы проверить наличие загруженного code module для DynaKube в файловой системе контейнера CSI `server`:

  ```
  > find /data -name latest-codemodule



  /data/_dynakubes/my-dynakube-1/latest-codemodule



  /data/_dynakubes/my-dynakube-2/latest-codemodule
  ```

#### Решение

* Обновиться до Dynatrace Operator версии 1.7.0+.

Другие способы решения проблемы:

* Удалить DynaKube и создать его заново. Это приведёт к пробелам в мониторинге.

### Несовместимости с определёнными версиями компонентов

Dynatrace Operator версии 1.5.0+

Функция автоматического TLS-сертификата требует ActiveGate версии 1.307.35+.

* Если нужно отключить эту функцию, установите feature flag `feature.dynatrace.com/automatic-tls-certificate: false` в конфигурации DynaKube.