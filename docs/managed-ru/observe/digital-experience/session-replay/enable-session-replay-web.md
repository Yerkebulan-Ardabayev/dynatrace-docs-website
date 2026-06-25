---
title: Включение Session Replay для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-replay/enable-session-replay-web
scraped: 2026-05-12T11:33:36.332544
---

# Включение Session Replay для веб-приложений

# Включение Session Replay для веб-приложений

* How-to guide
* 2-min read
* Updated on Feb 13, 2024

На этой странице описаны предварительные условия и процедура включения [Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.").

## Предварительные условия

Убедитесь, что ваша система соответствует следующим требованиям:

* OneAgent версии 1.241+ на всех мониторируемых хостах среды
* Real User Monitoring включён для вашего приложения
* Действующая лицензия Dynatrace Digital Experience Monitoring
* Межсетевые экраны настроены на разрешение контента application/octet-stream из вашего приложения (некоторые beacon, отправляемые Session Replay, являются бинарными)
* URL веб-интерфейса имеет доверенный сертификат
* Функция **Frontend Agents - Improved server node balancing** включена в **Settings** > **Preferences** > **OneAgent features**

* Настроен вторичный диск для хранения данных сессий пользователей

Настройка вторичного диска

Данные Session Replay необходимо хранить на отдельном разделе, известном как вторичный диск. Поэтому каждый узел кластера должен иметь такой выделенный раздел.

Предполагается, что большинство сессий занимают около 500 КБ, срок хранения по умолчанию составляет 35 дней, и всегда полезно иметь запас. Используя эти оценки, Dynatrace рекомендует рассчитывать размер вторичного хранилища по следующей формуле:

**Размер хранилища =  
Сессий в день × Средний размер сессии (500 КБ) × Процент записываемых сессий × Срок хранения (35) × Буфер (1.5)**

Для настройки вторичного диска:

1. Смонтируйте каталог за пределами хранилища транзакций. Папки хранилища транзакций и Session Replay не должны быть вложены, а должны находиться на одном уровне. Например, если каталог `transaction` находится по пути `/mnt1/dynatrace/transaction`, то каталог `session_replay` должен находиться по пути `/mnt2/dynatrace/session_replay`.
2. Назначьте владельцем каталога пользователя `dynatrace:dynatrace`.
3. Установите значение свойства `SERVER_REPLAY_DATASTORE_PATH` в файле `/etc/dynatrace.conf` равным каталогу, смонтированному на шаге 1. Например: `SERVER_REPLAY_DATASTORE_PATH = /mnt2/dynatrace/session_replay`.
4. Последовательно запустите реконфигурацию на каждом узле с помощью файла `reconfigure.sh`. Путь к этому файлу зависит от среды. Пример команды: `[Path]/dynatrace/install/dynatrace-managed/installer/reconfigure.sh`.

Dynatrace Managed будет реконфигурирован и перезапущен. После перезапуска будет использоваться новое расположение хранилища Session Replay.

## Включение Session Replay

Для включения Session Replay:

1. Перейдите в **Web**.
2. Выберите приложение, которое хотите настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**...**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Enablement and cost control**.
5. Включите **Enable Session Replay**.

После включения Session Replay наступает время его [настроить](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Настройте потребление мониторинга и параметры конфиденциальности данных для Session Replay.").

Дополнительная настройка для [мониторинга без агента](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройте мониторинг без агента для ваших веб-приложений.") не требуется.

## Связанные темы

* [Session Replay](/managed/observe/digital-experience/session-replay "Узнайте, как использовать Session Replay для лучшего понимания и устранения ошибок, с которыми сталкиваются клиенты.")
* [Настройка Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/configure-session-replay-web "Настройте потребление мониторинга и параметры конфиденциальности данных для Session Replay.")
* [Технические ограничения Session Replay для веб-приложений](/managed/observe/digital-experience/session-replay/session-replay-restrictions-web "Узнайте об ограничениях, применяемых к Session Replay.")