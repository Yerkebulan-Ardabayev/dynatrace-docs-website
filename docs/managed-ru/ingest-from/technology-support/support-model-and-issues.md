---
title: Поддержка Dynatrace Operator и известные проблемы
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/support-model-and-issues
scraped: 2026-05-12T11:23:46.957201
---

# Поддержка Dynatrace Operator и известные проблемы

# Поддержка Dynatrace Operator и известные проблемы

* Чтение: 5 мин
* Обновлено 4 марта 2026 г.

Dynatrace начинает поддержку Kubernetes вскоре после выхода новой версии Kubernetes или OpenShift. Как только становятся доступны версии release candidate новых выпусков Kubernetes/OpenShift, Dynatrace тестирует эти версии, включая последние версии OneAgent, ActiveGate и Dynatrace Operator.

В таблице ниже перечислены проверенные и протестированные версии выпусков:

| Версия Kubernetes upstream | Версия OpenShift | Минимальная версия OneAgent | Минимальная версия ActiveGate | Минимальная версия Dynatrace Operator | Рекомендуемая версия Dynatrace Operator | Конец поддержки (Kubernetes) | Конец поддержки (OpenShift) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.35 |  | 1.329 | 1.329 | v1.6.x | v1.8.0+ | 2028-04-01 |  |
| 1.34 | 4.21[4](#fn-1-4-def) | 1.321 | 1.321 | v1.6.x | v1.8.0+ | 2027-11-01 | 2028-10-01 |
| 1.33 | 4.20[4](#fn-1-4-def) | 1.319 | 1.319 | v1.1.x | v1.8.0+ | 2027-07-01 | 2028-03-01 |
| 1.32 | 4.19[4](#fn-1-4-def) | 1.309 | 1.309 | v1.1.x | v1.8.0+ | 2027-03-01 | 2028-03-01 |
| 1.31 | 4.18[3](#fn-1-3-def) | 1.297 | 1.297 | v1.1.x | v1.8.0+ | 2027-01-01 | 2028-08-01 |
| 1.30 | 4.17[3](#fn-1-3-def) | 1.291 | 1.291 | v1.1.x | v1.8.0+ | 2026-08-01 | 2027-07-01 |
| 1.29 | 4.16[3](#fn-1-3-def) | 1.281 | 1.281 | v0.14.x | v1.8.0+ | 2026-03-01 | 2027-09-01 |
| 1.28 | 4.15 | 1.275 | 1.275 | v0.12.x | v1.8.0+ | 2025-11-01 | 2026-11-01 |
| 1.27 | 4.14 | 1.269 | 1.269 | v0.10.x | v1.8.0+ | 2025-07-01 | 2026-11-01 |
| 1.26 | 4.13 | 1.259 | 1.257 | v0.10.x | v1.8.0+ | 2025-03-01 | 2026-02-01 |
| 1.25 | 4.12 | 1.249 | 1.251 | v0.8.x | v1.4.2+ | 2024-11-01 | 2026-02-01 |
| 1.24 | 4.11 | 1.241 | 1.243 | v0.7.x | v1.3.2+ | 2024-08-01 | 2025-03-01 |
| 1.23 | 4.10 | 1.233 | 1.233 | v0.4.x | v1.0.1[2](#fn-1-2-def) | 2024-04-01 | 2025-03-01 |
| 1.22 | 4.9 | 1.227 | 1.223 | v0.3.x | v1.0.1[2](#fn-1-2-def) | 2024-01-01 | 2024-05-01 |
| 1.21 | 4.8 | 1.217 | 1.215 | v0.3.x | v0.12.1[1](#fn-1-1-def) | 2023-11-01 | 2024-05-01 |
| 1.20 | 4.7 | 1.207 | 1.211 | v0.3.x | v0.6.0 | 2023-08-01 | 2023-08-01 |
| 1.19 | 4.6 | 1.199 | 1.205 | v0.3.x | v0.6.0 | 2023-08-01 | 2023-08-01 |
|  | 3.11 |  |  | v0.2.2 | v0.2.2 | 2023-08-01 | 2023-08-01 |

1

Новая версия Go, используемая в Dynatrace Operator, несовместима с версией CRI-O в OpenShift 4.8 и Kubernetes 1.21.

2

Для Kubernetes 1.22 и 1.23 рекомендуется Dynatrace Operator версии 1.0.1. Для OpenShift 4.8 и выше рекомендуется обновление до версии 1.1.0+.

3

[Мониторинг Classic Full-Stack](/managed/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "Подробное описание мониторинга Classic Full-Stack с помощью Dynatrace Operator.") поддерживается только на рабочих узлах под управлением Red Hat Enterprise Linux. Если же рабочие узлы работают под управлением Red Hat Enterprise Linux CoreOS, поддерживается только [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с помощью Dynatrace Operator.").

4

Поддерживаются только [Application observability](/managed/ingest-from/setup-on-k8s/how-it-works/application-monitoring "Подробное описание Application observability с помощью Dynatrace Operator.") и [Full-stack observability](/managed/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "Подробное описание full-stack observability с помощью Dynatrace Operator."). Это связано с тем, что рабочие узлы могут работать только под управлением Red Hat Enterprise Linux CoreOS. Подробнее см. [примечания к выпуску Red Hat (1.5.13.2)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).

Полная поддержка предоставляется до тех пор, пока версия Kubernetes или OpenShift не достигнет конца жизненного цикла. После этого Dynatrace предоставляет поддержку в режиме сопровождения примерно в течение одного года. Даты окончания поддержки публикуются в разделе [Объявления об окончании поддержки](/managed/whats-new/technology/end-of-support-news#dto "Объявления об окончании поддержки технологий, поддерживаемых Dynatrace.").

Основное различие между полной поддержкой и поддержкой в режиме сопровождения в том, что в период поддержки в режиме сопровождения Dynatrace сокращает ежедневные действия по тестированию.

В периоды полной поддержки и поддержки в режиме сопровождения каждый обнаруженный баг проходит оценку на возможность бэкпорта. В зависимости от серьёзности и риска изменения исправление либо бэкпортируется и выпускается в составе патч-версии, либо исправляется в следующей версии. Подробности см. в соответствующих [примечаниях к выпуску Dynatrace](/managed/whats-new "Читайте новости о продукте и примечания к выпускам и узнавайте, какие разделы документации появились.").

## Поддержка Dynatrace Operator

Dynatrace Operator доступен на следующих архитектурах:

* x86
* ARM
* ppc64le
* s390x [1](#fn-2-1-def)

1

Поддерживаются только [развёртывание cloud native full stack](/managed/ingest-from/setup-on-k8s/deployment/full-stack-managed "Разверните Dynatrace Operator в Kubernetes в режиме cloud-native full-stack"), [application monitoring](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Разверните Dynatrace Operator в Kubernetes в режиме application monitoring") и [host monitoring](/managed/ingest-from/setup-on-k8s/deployment/other/host-monitoring "Разверните Dynatrace Operator в Kubernetes в режиме host monitoring").

Если проблемы, связанные с Dynatrace Operator, не воспроизводятся в Dynatrace на архитектурах x86 или ARM и определены как специфичные для ppc64le, для дальнейшей поддержки необходимо обратиться по адресу `dt-operator@ibm.com`. Дополнительную информацию можно найти в соответствующем open-source pull request для Dynatrace Operator на [GitHub](https://dt-url.net/ev034k3).

Dynatrace Operator отвечает за развёртывание и управление жизненным циклом различных компонентов Dynatrace в Kubernetes и OpenShift (включая ActiveGate и OneAgent). Dynatrace Operator, это проект с открытым исходным кодом, поддерживаемый на [GitHub](https://dt-url.net/d7034gj). Он следует схеме [семантического версионирования](https://semver.org/) `major.minor.patch`, а минорные версии выпускаются примерно раз в 2-3 месяца.

Три последние версии Dynatrace Operator тестируются с последними версиями Kubernetes и OpenShift. Кроме того, мы проводим оценку на возможность бэкпорта для любого бага или уязвимости, чтобы проанализировать серьёзность и риск изменения исправления. Мы рекомендуем использовать последнюю патч-версию, так как вновь реализованные функции увеличивают минорную версию. Подробнее см. [примечания к выпуску Dynatrace Operator](/managed/whats-new/dynatrace-operator "Примечания к выпуску Dynatrace Operator").

Все версии Dynatrace Operator, которые не считаются достигшими конца жизненного цикла, рассматриваются как находящиеся в режиме сопровождения, что включает наши обычные процессы поддержки клиентов. Версии в режиме сопровождения не получают исправлений багов и бэкпортов для уязвимостей. См. объявления об окончании поддержки в разделе [Объявления об окончании поддержки](/managed/whats-new/technology/end-of-support-news#dto "Объявления об окончании поддержки технологий, поддерживаемых Dynatrace.").

## Известные проблемы и их решения

Список известных проблем для версий Dynatrace Operator и того, как они влияют на различные компоненты. Эти проблемы присутствуют в выпущенных версиях Dynatrace Operator и для их устранения может потребоваться обновление минорной версии!

### Внедрение компонентов Dynatrace

Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1 Dynatrace Operator версии 1.7.2

#### Проблема

* Из-за оптимизации внедряемых точек монтирования (их объединения в `/var/lib/dynatrace`) OneAgent больше не может внедряться в компоненты Dynatrace.

* Компоненты Dynatrace содержат конфигурацию в `/var/lib/dynatrace`, которая скрывается точками монтирования, добавляемыми при внедрении через Webhook.

По умолчанию мониторинг пространства имён Dynatrace Operator (и, следовательно, компонентов Dynatrace) не включён. Проблема может проявиться, если флаг функции `feature.dynatrace.com/ignored-namespaces` используется для переопределения игнорируемых пространств имён так, что в них включается пространство имён Dynatrace Operator.

#### Решение

Настройте аннотацию пода `dynatrace.com/split-mounts` (требуется Dynatrace Operator версии 1.8.0+) на затронутых подах.

### Classic full-stack с обогащением метаданными

Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1 Dynatrace Operator версии 1.7.2

#### Проблема

* Classic full-stack и обогащение метаданными несовместимы и не могут использоваться для внедрения в одни и те же поды приложений.

И внедрение OneAgent, и внедрение через Webhook пытаются добавить точку монтирования в каталог `/var/lib/dynatrace` в поде приложения. Эти точки монтирования несовместимы и не могут сосуществовать.

#### Решение

Все версии Dynatrace Operator 1.7 не поддерживаются.

Для версий Dynatrace Operator 1.8+ и версий 1.6 и более ранних может потребоваться дополнительная настройка:

* Если ваша версия OneAgent ниже 1.333, настройте отладочный флаг `remountOperatorEnrichment`.
* Если ваша версия OneAgent 1.333+, этот отладочный флаг OneAgent не требуется.

### Определение доступности хоста

Dynatrace Operator версии 1.6.0 Dynatrace Operator версии 1.6.1 Dynatrace Operator версии 1.6.2 Dynatrace Operator версии 1.7.0 Dynatrace Operator версии 1.7.1

#### Проблема

* В средах Kubernetes, особенно использующих автомасштабирование, есть сложности с надёжным определением того, был ли узел удалён намеренно или произошёл его непредвиденный сбой. Эта неоднозначность может приводить к большому числу ложноположительных оповещений «Host is unavailable», что снижает точность мониторинга и качество оповещений.

#### Решение

Обновитесь до Dynatrace Operator версии 1.7.2+ или 1.6.3.

### Переход на Node image pull с образом code modules

Dynatrace Operator версии 1.5.0 Dynatrace Operator версии 1.5.1 Dynatrace Operator версии 1.6.0 Dynatrace Operator версии 1.6.1 Dynatrace Operator версии 1.6.2

#### Проблема

При переходе от использования CSI-драйвера без `codeModulesImage` к его использованию с [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка node image pull") убедитесь, что файловая система CSI-драйвера не содержит модуль кода для указанного DynaKube. Если содержит, CSI-драйвер завершится с ошибкой и для восстановления потребуется ручное вмешательство.

* Если эта проблема возникла, возврат к работе без `codeModulesImage` снова сделает CSI-драйвер работоспособным.
* Чтобы проверить наличие загруженного модуля кода для DynaKube в файловой системе контейнера CSI `server`, можно использовать команду `find`:

  ```
  > find /data -name latest-codemodule



  /data/_dynakubes/my-dynakube-1/latest-codemodule



  /data/_dynakubes/my-dynakube-2/latest-codemodule
  ```

#### Решение

* Обновитесь до Dynatrace Operator версии 1.7.0+.

Другие способы решить проблему:

* Удалите DynaKube и создайте его заново. Это приведёт к пробелам в мониторинге.

### Несовместимость с определёнными версиями компонентов

Dynatrace Operator версии 1.5.0+

Функция автоматического TLS-сертификата требует ActiveGate версии 1.307.35+.

* Если вы предпочитаете отключить эту функцию, задайте флаг функции `feature.dynatrace.com/automatic-tls-certificate: false` в конфигурации DynaKube.