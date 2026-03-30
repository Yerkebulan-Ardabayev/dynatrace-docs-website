---
title: Установка OneAgent на сервер
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-03-06T21:09:37.289101
---

Руководство по первичной установке Dynatrace OneAgent на хост.

Инструкции для конкретных ОС: [AIX](installation-and-operation/aix.md) | [Linux](installation-and-operation/linux.md) | [Solaris](installation-and-operation/solaris.md) | [Windows](installation-and-operation/windows.md) | [zOS](installation-and-operation/zos.md)

## Предварительные требования

- Среда Dynatrace
- Доступ администратора к хосту (без существующих установок OneAgent)
- Сеть с поддержкой SSL

## Установка

1. В **Dynatrace Hub** выберите **OneAgent** > **Set up**.
2. Укажите параметры:
   - **OS type** — Linux, Windows или AIX
   - **Architecture** (только Linux)
   - **Monitoring mode** — Full-Stack, Infrastructure или Discovery
   - **Custom host name** (опционально)
3. Нажмите **Generate token** — скопируйте и сохраните токен.
4. Скачайте OneAgent (CLI-команда или кнопка **Download**).
5. Проверьте подпись (только Linux/AIX).
6. Установите OneAgent через CLI или GUI. Для GUI добавьте параметры:
   `--set-monitoring-mode=fullstack --set-app-log-content-access=true`
7. После установки перезапустите процессы, которые нужно мониторить.
8. Проверьте: **Infrastructure & Operations** > **Host** — хост должен появиться в таблице.

## Связанные темы

- Функции OneAgent
- Infrastructure & Operations
- Настройки на уровне хоста
- Режимы мониторинга OneAgent
