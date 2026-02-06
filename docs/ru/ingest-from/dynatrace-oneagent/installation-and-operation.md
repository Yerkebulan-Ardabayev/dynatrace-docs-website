---
title: Install OneAgent on a server
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-02-06T16:18:55.331928
---

# Установите OneAgent на сервер

# Установите OneAgent на сервер

* Последняя версия Dynatrace
* 3-минутное чтение
* Обновлено 22 января 2026 г.

Следуйте этому руководству, чтобы установить Dynatrace OneAgent в первый раз.

После выполнения этого руководства OneAgent будет установлен на хосте и вы сможете использовать Dynatrace для мониторинга этого хоста и его процессов.

Информация на этой странице не зависит от платформы.

Для получения информации об установке OneAgent и дополнительных функциях для конкретной ОС выберите свою ОС, чтобы получить подробные инструкции.

[ЭКС](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Линукс](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Солярис](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Окна](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [зОС](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

## Предварительные условия

В этом руководстве предполагается, что у вас есть:

* Среда Dynatrace.
* Доступ администратора к хосту Linux, Windows или AIX (на котором не установлено ни одного агента OneAgent).
* Сеть, поддерживающая связь SSL.

## Настройка OneAgent

Чтобы загрузить и установить OneAgent на хосте:

1. В **Dynatrace Hub** выберите **OneAgent**.
2. Выберите **Настроить**.
Откроется окно **Установить OneAgent**.
3. Введите или выберите соответствующие параметры (пример см. на скриншоте ниже).

* **Тип ОС**

Выберите **Linux**, **Windows** или **AIX** в зависимости от операционной системы вашего хоста.

* **Архитектура** (только Linux)
* **Режим мониторинга**
Варианты: **Полный стек**, **Инфраструктура** или **Обнаружение**.
Если вы используете бесплатную пробную версию Dynatrace, выберите **Полный пакет**, чтобы увидеть все, что Dynatrace способен отслеживать.
Вы всегда можете изменить режим мониторинга после установки.
* Для **Необязательных параметров** вы можете добавить **Пользовательское имя хоста** для упрощения идентификации.
Остальные параметры выходят за рамки данного руководства.

![Параметры настройки OneAgent](https://dt-cdn.net/images/screenshot-2025-02-05-at-15-06-49-2992-637e933241.png)
4. Выберите **Создать токен**, чтобы создать токен API, который позволит вашей среде Dynatrace получить доступ к OneAgent.
Скопируйте токен и сохраните его в безопасном месте, потому что вы не сможете снова получить к нему доступ.
Вам больше ничего делать с этим токеном прямо сейчас не нужно.

5. Загрузите OneAgent.
Либо используйте предоставленную команду CLI, либо выберите **Загрузить**.
6. Проверьте подпись.
Используйте предоставленную команду CLI.
(Примечание: только для Linux и AIX.)
7. Установите OneAgent.
Либо используйте предоставленную команду CLI, либо запустите исполняемый файл, выбрав его в графическом интерфейсе.
Следуйте инструкциям, описанным в установщике.

При установке через графический интерфейс необходимо добавить следующие параметры на экран **Необязательно: дополнительные настройки командной строки**:
`--set-monitoring-mode=fullstack --set-app-log-content-access=true`
8. Когда программа установки отобразит **Поздравляем!Dynatrace OneAgent успешно установлен!** означает, что OneAgent установлен на хосте.
Выберите **Готово**, чтобы выйти из программы установки.
9. Поскольку OneAgent не может внедряться в запущенные процессы, вам потребуется перезапустить все процессы, которые вы хотите отслеживать с помощью OneAgent.
10. Чтобы убедиться, что OneAgent отслеживает ваш хост, откройте Dynatrace и перейдите в раздел **Инфраструктура и операции** > **Хост**.
Если все работает правильно, вы увидите имя вашего хоста в таблице **Хосты**.
Пример смотрите на скриншоте ниже.

![Представление инфраструктуры и операций недавно добавленного OneAgent на хосте](https://dt-cdn.net/images/screenshot-2025-02-04-at-13-32-36-2598-439524d1f9.png)

Теперь OneAgent настроен и контролирует ваш хост.См. [Начните работу с Dynatrace](/docs/discover-dynatrace/get-started "Learn about Dynatrace monitoring capabilities, concepts, and deployment models and find out how to get started with SaaS and Managed deployments."), чтобы продолжить свое первое путешествие с Dynatrace.

## Похожие темы

* [Возможности OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")
* [Инфраструктура и операции](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor host and data center health to detect issues and improve infrastructure performance.")
* [Настройки на уровне хоста](/docs/observe/infrastructure-observability/hosts/configuration "Host-level settings")
* [Режимы мониторинга инфраструктуры и обнаружения](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Find out what's included in Dynatrace Infrastructure Monitoring mode.")