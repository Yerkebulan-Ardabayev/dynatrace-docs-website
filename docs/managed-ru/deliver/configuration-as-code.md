---
title: Обзор: Configuration as Code
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code
scraped: 2026-05-12T11:03:01.245854
---

# Configuration as Code overview

# Configuration as Code overview

* Overview
* 2-min read
* Updated on Jul 27, 2025

![Configuration as Code](https://dt-cdn.net/images/configuration-as-code-highresolution-1025-29c909e912.png "Configuration as Code") Configuration as Code (CaC) обеспечивает Observability as Code и Security as Code для полной автоматизации настройки платформы Dynatrace в любом масштабе:

* Автоматизация и стандартизация конфигураций наблюдаемости.
* Включение наблюдаемости в процесс доставки программного обеспечения.
* Обеспечение стандартов при демократизации наблюдаемости.
* Соответствие требованиям Security-as-code в процессе подключения сервисов и приложений.

![Set up Open Pipeline configurations via Terraform](https://cdn.hub.central.dynatrace.com/hub/Terraform-screenshot-intro.png)![Automate the service monitoring configuration via Monaco CLI](https://cdn.hub.central.dynatrace.com/hub/Monaco-Screenshot-Intro.png)

1 из 2: настройка конфигураций Open Pipeline через Terraform

## Сценарии использования

Управляйте любой конфигурацией Dynatrace параллельно с исходным кодом — в YAML-файлах, организованных в Git-репозиториях.

Например:

* Ресурсы IAM
* Мониторинг сервисов / подключение сервисов
* Дашборды SLO

Вы можете управлять любой конфигурацией Dynatrace параллельно с любым исходным кодом — в YAML-файлах, организованных в Git-репозиториях.
Ознакомьтесь с [примерами на GitHub](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples).

## Концепции

Подход Dynatrace к CaC позволяет управлять задачами наблюдаемости в окружении Dynatrace через конфигурационные файлы вместо графического интерфейса.

Модель самообслуживания CaC позволяет командам разработчиков быстро и эффективно настраиваться даже для крупномасштабных приложений:

* Мониторинг
* Наблюдаемость
* Политики безопасности

Это устраняет необходимость разработки собственных решений и снижает ручную работу команд наблюдаемости.

CaC позволяет:

* Создавать шаблоны конфигурации для нескольких окружений.
* Управлять взаимозависимостями между конфигурациями без необходимости хранить уникальные идентификаторы.
* Применять одну конфигурацию к сотням окружений Dynatrace и обновлять все их одновременно.
* Переносить конфигурации, специфичные для приложений, между окружениями после развёртываний на каждом стейдже.
* Поддерживать все механизмы и лучшие практики рабочих процессов на основе Git: pull-запросы, слияние и утверждения.
* Фиксировать конфигурацию в системе контроля версий и совместно работать над изменениями.

## Зачем использовать Configuration as Code

Использование CaC позволяет иметь конфигурационные файлы для:

* Создания,
* Обновления и
* Безопасного, последовательного и воспроизводимого управления конфигурациями наблюдаемости.

Их можно повторно использовать, версионировать и передавать команде.

Стандартизированный подход к настройке Dynatrace как кода даёт множество преимуществ.
Помимо всех достоинств подхода на основе Git, таких как:

* Контроль версий
* Воспроизводимость

Применение CaC обеспечивает:

* Самообслуживание при настройке конфигураций наблюдаемости
* Оптимизацию и стандартизацию процессов подключения
* Синхронизацию конфигураций между разными окружениями

## Использование разработки на основе наблюдаемости в рамках платформы разработчика

* Сократите время развёртывания, интегрировав CaC для оптимизации процесса подключения приложений через Golden Paths.
* Внедрите стандарты наблюдаемости и безопасности в своё окружение, интегрировав их в CI/CD-пайплайны, например через образы контейнеров, обеспечивая согласованность на всех стейджах.
* Предоставьте возможности самообслуживания, интегрировав наблюдаемость, автоматизацию и контроль качества в ваш SDLC.
  Подробнее см. [Platform Engineering](/managed/discover-dynatrace/get-started/platform-engineering "Use observability and security to drive analytics and automation at scale.").

## Инструменты

Для настройки Dynatrace и управления им с помощью CaC доступны два инструмента:

* [Terraform](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform.") — отраслевой стандарт CaC.
* [Monaco](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.") — собственный CLI-инструмент CaC от Dynatrace.

Выбор инструмента зависит от используемого стека и требований.

Рекомендуем Terraform с провайдером Dynatrace Terraform, если:

* Вы уже знакомы с Terraform и уверенно с ним работаете.
* Вы хотите управлять инфраструктурой и конфигурацией нескольких провайдеров в едином рабочем пространстве.
* Вы хотите воспользоваться внешним управлением состоянием, которое выявляет расхождения между планом и реальностью, и совместной работой через удалённые бэкенды состояния, например GitHub.
* Вы планируете использовать динамические конфигурации с вычислениями и условной логикой, поддерживаемыми выражениями HCL (Hashicorp Configuration Language).

Если вы не хотите или не можете использовать Terraform, доступен собственный CLI-инструмент CaC от Dynatrace — Monaco.
Monaco — независимое от сторонних инструментов решение, работающее в автономном режиме и использующее нативный JSON для описания конфигураций Dynatrace.

## Связанные темы

* [Обзор Configuration as Code через Terraform](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform.")
* [Обзор Configuration as Code через Monaco](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.")
* [[Блог] Автоматизация наблюдаемости, безопасности и надёжности в масштабе](https://www.dynatrace.com/news/blog/automated-observability-security-and-reliability-at-scale/)