---
title: Hosts
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts
scraped: 2026-02-06T16:29:11.779328
---

# Хосты

# Хосты

* Latest Dynatrace
* Overview
* Чтение: 3 мин
* Опубликовано 25 сентября 2018 г.

Производительность хостов отслеживается на нескольких страницах Dynatrace, начиная с высокоуровневых метрик состояния на плитках дашборда и заканчивая специализированными страницами для каждого из ваших хостов. Полностековый мониторинг инфраструктуры начинается автоматически, как только Dynatrace OneAgent начинает работу и приступает к сбору информации о производительности и событиях на ваших хостах.

Краткий обзор

### Группы хостов

По мере того как многие окружения, контролируемые Dynatrace, становятся всё более крупными и сложными, нередко охватывая различные центры обработки данных и множество приложений, [группы хостов](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.") приобретают всё большую важность. Группы хостов позволяют настраивать хосты по группам, выборочно развёртывать версии OneAgent по группам и по-разному отслеживать метрики сервисов в зависимости от платформы, на которой они работают.

### Аналитика производительности виртуализации

Dynatrace показывает, как виртуальные машины в вашем окружении влияют на производительность ваших приложений и сервисов. После включения виртуализации в мониторинг производительности Dynatrace вы получаете представление о полном стеке инфраструктуры и его поведении.

### Теги в файле конфигурации хоста

В динамических или крупных окружениях ручная маркировка хостов тегами может быть непрактичной. Для динамических развёртываний с часто изменяющимися экземплярами хостов и именами (например, AWS или MS Azure) вы можете [использовать специальный файл конфигурации для программного назначения тегов вашим хостам](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Узнайте, как назначать теги и задавать дополнительные свойства контролируемого хоста.").

### Пользовательские имена хостов

Dynatrace, как правило, именует обнаруженные хосты в вашем окружении на основе их DNS-имён, точно так, как они обнаружены Dynatrace OneAgent. Для улучшения читаемости вы можете [создавать пользовательские имена хостов](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя контролируемого хоста.") для отображения вместо обнаруженных имён хостов.

## Основные понятия

[![Infrastructure Monitoring](https://cdn.bfldr.com/B686QPH3/at/jftqtgccnb2wt3h4ngf6z/Infrastructure_Observability.svg?auto=webp&width=72&height=72 "Infrastructure Monitoring")

### Режимы мониторинга

Узнайте, что включено и как активировать режимы Infrastructure Monitoring и Discovery.](/docs/observe/infrastructure-observability/hosts/monitoring-modes "Узнайте, что включено в режим Infrastructure Monitoring Dynatrace.")[### Насколько эффективен мониторинг только инфраструктуры?

Узнайте, как мониторинг только инфраструктурного уровня вашего окружения может привести к неполной картине состояния ваших приложений и пользовательского опыта.](/docs/observe/infrastructure-observability/hosts/monitoring-modes/how-effective-is-infrastructure-monitoring-on-its-own "Узнайте, как мониторинг только инфраструктурного уровня вашего окружения может привести к неполной картине состояния ваших приложений и пользовательского опыта.")

## Конфигурация

[### Обнаружение аномалий хостов

Настройте обнаружение аномалий хостов, включая пороговые значения проблем и событий.](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Настройте обнаружение аномалий хостов, включая пороговые значения проблем и событий.")[### Определение тегов и метаданных для хостов

Назначайте теги и задавайте дополнительные свойства контролируемого хоста.](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Узнайте, как назначать теги и задавать дополнительные свойства контролируемого хоста.")[### Исключение дисков и сетевого трафика из мониторинга хостов

Исключите выбранные диски и сетевой трафик из мониторинга хостов.](/docs/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic "Узнайте, как исключить выбранные диски и сетевой трафик из мониторинга хостов.")[### Организация окружения с помощью групп хостов

Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.](/docs/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов.")[### Установка пользовательских имён хостов

Изменение имени контролируемого хоста.](/docs/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя контролируемого хоста.")

## Мониторинг

[### Мониторинг хостов с помощью Dynatrace

Мониторинг хостов с помощью Dynatrace.](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Мониторинг хостов с помощью Dynatrace.")[### Мониторинг служб ОС

Улучшите видимость вашей инфраструктуры, отслеживая доступность служб операционной системы.](/docs/observe/infrastructure-observability/hosts/monitoring/os-services "Улучшите видимость вашей инфраструктуры, отслеживая доступность служб операционной системы.")[### Классический мониторинг служб Windows

Улучшите видимость вашей инфраструктуры, отслеживая доступность служб Windows.](/docs/observe/infrastructure-observability/hosts/monitoring/windows-services "Узнайте, как улучшить видимость вашей инфраструктуры, отслеживая доступность служб Windows.")[### Доступность процессов

Мониторинг доступности и производительности ключевых процессов на ваших хостах.](/docs/observe/infrastructure-observability/hosts/monitoring/process-availability "Мониторинг доступности и производительности ключевых процессов на ваших хостах.")

## Диагностика

[![OneAgent](https://cdn.bfldr.com/B686QPH3/at/g8mmkkpfmgwbxcjz54pvfsx/OneAgent.svg?auto=webp&width=72&height=72 "OneAgent")

### Диагностика OneAgent

Узнайте, как запускать диагностику OneAgent.](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Узнайте, как запускать диагностику OneAgent.")
