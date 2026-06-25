---
title: Обновление OneAgent на PPC BE Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-ppc-be-linux
scraped: 2026-05-12T11:05:25.916422
---

# Обновление OneAgent на PPC BE Linux

# Обновление OneAgent на PPC BE Linux

* Чтение: 1 мин
* Опубликовано 21 августа 2019 г.

Чтобы обновить установленный экземпляр OneAgent на PPC BE, следуйте приведённым ниже инструкциям:

1. Повторите все шаги [первоначальной установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Узнайте, как скачать и установить Dynatrace OneAgent на PPC BE Linux."), но установите OneAgent в новый каталог.
2. Остановите все мониторируемые процессы.
3. Переименуйте текущий каталог установки OneAgent (например, `/opt/dynatrace/oneagent` в `/opt/dynatrace/oneagent-old`) с помощью следующей команды:

   ```
   mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old
   ```

   Эту папку можно удалить после обновления OneAgent.
4. Переименуйте обновлённую папку OneAgent так, чтобы она указывала на исходный каталог установки (например, с `/opt/dynatrace/oneagent-update` на `/opt/dynatrace/oneagent`), с помощью следующей команды:

   ```
   mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent
   ```
5. Перезапустите все процессы, которые требуется мониторить.

## Проверка установленной версии OneAgent

Используйте один из этих методов, чтобы проверить, какая версия OneAgent установлена у вас в настоящее время.

### Интерфейс командной строки OneAgent

Запустите `oneagentctl` с параметром `--version`. Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").

### Обзор хоста

1. Перейдите в **Hosts**.
2. Щёлкните интересующий вас хост.
3. Разверните **Properties** под именем хоста. Установленная версия OneAgent указана в перечисленных свойствах.

### Статус развёртывания

1. Перейдите в **Deployment Status**.
2. Откройте вкладку **All hosts** или **Recently connected hosts**.
3. Разверните интересующую вас запись хоста. Установленная версия OneAgent включена в отображаемую информацию.