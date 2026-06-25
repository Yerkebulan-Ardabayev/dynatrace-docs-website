---
title: Миграция ActiveGate
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-ag
scraped: 2026-05-12T12:14:03.764840
---

# Миграция ActiveGate

# Миграция ActiveGate

* Published Dec 07, 2023

Существуют три основных подхода к миграции ActiveGate с Dynatrace Managed на SaaS:

1. Рекомендуется Параллельное развёртывание новых экземпляров ActiveGate на новом оборудовании
2. Перенастройка ActiveGate
3. Переустановка ActiveGate на том же оборудовании

### Каковы преимущества и недостатки параллельного развёртывания новых ActiveGate на новом оборудовании?

Рекомендуется

| Преимущества | Недостатки |
| --- | --- |
| * Потенциально минимальное время простоя мониторинга (переключение выполняется на стороне агента) * Возможность протестировать настройку ActiveGate перед выводом из эксплуатации существующей инфраструктуры * Хорошо подходит для сред с жёсткими требованиями к соответствию нормативным требованиям | * Дополнительные затраты на развёртывание и управление большей инфраструктурой * Требует больше времени * Может потребоваться повторное применение пользовательских настроек из `custom.properties` и `launcheruserconfig.conf` |

Для установки нового ActiveGate параллельно на новом оборудовании:

1. Подготовьте новое оборудование для ActiveGate из новой среды SaaS.
2. Создайте резервные копии файлов пользовательской конфигурации: `custom.properties`, `launcheruserconfig.conf`, а также хранилищ ключей и доверенных сертификатов.

   Подробнее об этих файлах см. в разделе [Свойства конфигурации и параметры ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
3. Следуйте выбранной процедуре [установки ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate"). Настройте команду установки для применения файлов хранилищ ключей и доверенных сертификатов.
4. [Остановите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
5. Добавьте или замените исходные файлы конфигурации `custom.properties` и `launcheruserconfig.conf` по пути установки нового ActiveGate.
6. [Запустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
7. Старый ActiveGate можно удалить после миграции всех OneAgent, которые передавали данные через него. Проверить, какие OneAgent используют данный ActiveGate, можно в разделе [Обзор работоспособности OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-health "Discover deployed OneAgent modules at scale and detect anomalies before they turn into problems.").

### Каковы преимущества и недостатки перенастройки ActiveGate?

| Преимущества | Недостатки |
| --- | --- |
| * Меньшее время простоя и меньший объём передаваемых данных (не нужно загружать и запускать установщики) * Повторное использование существующей инфраструктуры * Отсутствие необходимости повторно развёртывать пакеты расширений | * Риск ошибок из-за ручного изменения конфигурации * Возможные перебои в мониторинге при отсутствии резервного варианта для OneAgent * Требует ротации токена среды |

Для перенастройки существующего ActiveGate на направление трафика OneAgent в новую среду SaaS:

1. [Остановите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
2. Создайте резервные копии файлов конфигурации: `connectivity.history`, `config.properties`, `cluster.properties`, `custom.properties`, `launcheruserconfig.conf`, а также хранилищ ключей и доверенных сертификатов.

   Подробнее об этих файлах см. в разделе [Свойства конфигурации и параметры ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
3. Обновите `config.properties`: укажите параметр **seedServerUrl** и установите **configured=false** с URL вашей среды SaaS.
4. Если между ActiveGate и кластером Dynatrace Managed используется балансировщик нагрузки и применялся параметр `--ignore-cluster-runtime`, удалите его из файла `custom.properties`.

   Подробнее см. в разделе [Обратный прокси или балансировщик нагрузки для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/set-up-reverse-proxy-for-activegate "Learn how to configure ActiveGate properties to set up a reverse proxy or a load balancer.").
5. Измените файл `authorization.properties`: замените текущее поле `tenantToken` на [токен тенанта](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it."), полученный из среды, к которой должен подключаться ActiveGate.
6. [Создайте новый токен ActiveGate](/managed/dynatrace-api/environment-api/tokens-v2/activegate-tokens/post-activegate-token "Create a new ActiveGate token via Dynatrace API.") в целевом тенанте и используйте его для замены токена в файле `authorization.properties` (тенант-источник). В противном случае запуск ActiveGate завершится с ошибками следующего вида:

   ```
   2024-04-12 13:58:46 UTC WARNING [<rtc43848>] [<collector.core>, InitialCollectorSetupPoller] Initial collector setup received with error:REQUEST_REJECTED, reason=Invalid ActiveGate Token source=ANY_SERVER 0x0000000000000000 [Suppressing further messages for 1 hour]



   2024-04-12 13:59:18 UTC INFO    [<rtc43848>] [<WatchDog>, WatchDogImpl] Connected successfully to native watchdog on 127.0.0.1:50000
   ```
7. [Запустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").

### Каковы преимущества и недостатки переустановки ActiveGate на том же оборудовании?

| Преимущества | Недостатки |
| --- | --- |
| * Меньше риск ошибок, так как нет необходимости изменять существующие файлы конфигурации * Повторное использование существующей инфраструктуры * Можно использовать существующие инструменты автоматизации | * Простой при запуске установщика * Возможные перебои в мониторинге при отсутствии резервного варианта для OneAgent * Может потребоваться повторное применение пользовательских настроек из `custom.properties` и `launcheruserconfig.conf` |

Для переустановки ActiveGate на том же оборудовании с перенаправлением трафика OneAgent в новую среду SaaS:

1. Создайте резервные копии пользовательских настроек, включая `custom.properties` и `launcheruserconfig.conf`.
   Подробнее об этих файлах см. в разделе [Свойства конфигурации и параметры ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
2. [Удалите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/uninstall-activegate "Learn how to remove ActiveGate from Windows or Linux-based systems.").
3. Следуйте выбранной процедуре [установки ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate"). Настройте команду установки для применения файлов хранилищ ключей и доверенных сертификатов.
4. [Остановите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
5. Добавьте или замените исходные файлы конфигурации `custom.properties` и `launcheruserconfig.conf` по пути установки нового ActiveGate.
6. [Запустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").