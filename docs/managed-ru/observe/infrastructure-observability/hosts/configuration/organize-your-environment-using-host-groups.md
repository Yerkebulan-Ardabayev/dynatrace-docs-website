---
title: Организация среды с помощью групп хостов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups
scraped: 2026-05-12T11:22:15.591894
---

# Organize your environment using host groups

# Организация среды с помощью групп хостов

* How-to guide
* 3-min read
* Updated on Aug 21, 2023

Группы хостов позволяют категоризировать и управлять несколькими хостами с похожими характеристиками или назначением в рамках вашей среды.

## Проверка принадлежности к группе хостов

Чтобы определить, к какой группе хостов принадлежит хост:

1. Перейдите в **Hosts** и выберите интересующий хост.
2. На странице обзора хоста выберите **Properties and tags**.
3. На панели **Properties and tags** найдите свойство **Host group**, чтобы увидеть имя группы хостов, к которой принадлежит выбранный хост.

   Свойство **Host group** не отображается, если выбранный хост не принадлежит ни одной группе хостов.
4. Выберите имя группы хостов, чтобы просмотреть список всех хостов в этой группе. Откроется страница **OneAgent deployment**, отфильтрованная по выбранной группе хостов. Каждый перечисленный хост имеет ссылку **Host group:** `<имя группы>`, где `<имя группы>` — имя группы хостов, которую нужно настроить.
5. Выберите имя группы хостов в любой строке.

## Просмотр всех хостов в группе хостов

Чтобы просмотреть список всех хостов в группе хостов:

1. Перейдите в **Deployment Status** и выберите **OneAgents**.
   Откроется список всех хостов в вашем развёртывании.
2. В строке фильтров выберите **Host group** и имя нужной группы хостов.
   Откроется список всех хостов в выбранной группе хостов.

## Назначение хоста группе хостов

Хост можно назначить группе хостов во время или после [установки OneAgent](/managed/ingest-from "Learn how to install and configure ActiveGate and OneAgent on various platforms.").

* **Во время** установки OneAgent

  Чтобы назначить хост группе хостов при установке OneAgent, используйте параметр `--set-host-group`, как показано в примере ниже.

  `/bin/sh Dynatrace-OneAgent-Linux-1.177.65.sh --set-host-group=MyHostGroup`

  В Windows имя группы также можно ввести в интерфейсе инсталлятора.
* **После** установки OneAgent

  Чтобы назначить хост группе хостов после установки OneAgent:

  CLI

  Dynatrace UI

  Используйте инструмент командной строки [oneagentctl](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#host-groups "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

  1. Перейдите в **Deployment Status** и установите флажок напротив нужного хоста.
  2. В нижней части страницы выберите **modify host group**.
  3. Нажмите **Run action**.
  4. Выберите **Specify host group to be assigned** или **Remove current host group assignment**.
  5. Нажмите **Next**.
  6. Проверьте изменения и нажмите **Apply changes**.

  Обратите внимание, что OneAgent автоматически перезапустится после применения изменений.

Требования к строке группы хостов

* Может содержать только буквенно-цифровые символы, дефисы, символы подчёркивания и точки.
* Не должна начинаться с `dt.`.
* Максимальная длина — 100 символов.

Группа хостов статически назначается хосту. Каждый хост принадлежит не более чем одной группе хостов, и группу хостов можно изменить с помощью команды `oneagentctl`, [управления удалённой конфигурацией](/managed/ingest-from/bulk-configuration#configure-oneagents "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") или переустановки OneAgent. Группы хостов отображаются, например, на странице **Hosts** приложения [**Infrastructure & Operations**](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") и на странице **Monitoring overview**, где можно выбрать ссылку **Host group** для редактирования настроек всех хостов в группе.

![Host groups](https://dt-cdn.net/images/host-groups-1200-d314d1729f.png)

Группы хостов

## Влияние групп хостов на среду мониторинга

Группы хостов — это наборы хостов. Каждую группу можно настраивать на уровне группы хостов, что упрощает изменение настроек для большого числа хостов. Пороги оповещений и настройки обновления OneAgent можно определять для каждой группы хостов отдельно. В примере ниже группа хостов принимает глобально настроенные пороги аномалий без их переопределения.

![Host groups](https://dt-cdn.net/images/host-groups2-1422-845f78e968.png)

Группы хостов

Также можно определить настройки обновления OneAgent и запустить обновление для всех установок OneAgent в одной группе хостов, как показано в примере ниже. Здесь глобальные настройки переопределяются и все установки OneAgent обновляются автоматически при выходе новой версии.

![Host groups](https://dt-cdn.net/images/host-groups3-1426-aa75a3847f.png)

Группы хостов

Кроме того, группы хостов влияют на обнаружение групп процессов. Когда один и тот же процесс работает в двух разных группах хостов, Dynatrace создаёт по одной группе процессов для каждой группы хостов. Это означает, что группы процессов также можно по-разному настраивать в зависимости от группы хостов. Соответственно, сервисы также группируются по группам хостов, что позволяет по-разному настраивать сервисы для каждой группы хостов.

Группы хостов также можно использовать в [правилах расстановки тегов](/managed/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") и для определения [зон управления](/managed/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones."), что позволяет применять дополнительный контекст к различным сущностям в Dynatrace на основе групп хостов. Как показано в примере ниже, можно расставлять теги сущностям на основе группы хостов, к которой они принадлежат.

![Host groups](https://dt-cdn.net/images/host-groups4-1414-8039d74ee9.png)

Группы хостов