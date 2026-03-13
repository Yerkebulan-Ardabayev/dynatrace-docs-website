---
title: Update OneAgent on PPC BE Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-ppc-be-linux
scraped: 2026-03-06T21:18:51.882688
---

# Обновление OneAgent на PPC BE Linux

# Обновление OneAgent на PPC BE Linux

* Latest Dynatrace
* 1-min read
* Published Aug 21, 2019

Чтобы обновить установленный экземпляр OneAgent на PPC BE, следуйте приведённым ниже инструкциям:

1. Повторите все шаги [первоначальной установки](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Learn how to download and install Dynatrace OneAgent on PPC BE Linux."), но установите OneAgent в новый каталог.
2. Остановите все отслеживаемые процессы.
3. Переименуйте текущий каталог установки OneAgent (например, `/opt/dynatrace/oneagent` в `/opt/dynatrace/oneagent-old`), используя следующую команду:

   ```
   mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old
   ```

   Эту папку можно удалить после обновления OneAgent.
4. Переименуйте обновлённую папку OneAgent, чтобы она указывала на исходный каталог установки (например, с `/opt/dynatrace/oneagent-update` на `/opt/dynatrace/oneagent`), используя следующую команду:

   ```
   mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent
   ```
5. Перезапустите все процессы, которые должны отслеживаться.

## Проверка установленной версии OneAgent

Используйте один из следующих методов, чтобы проверить текущую установленную версию OneAgent.

### Интерфейс командной строки OneAgent

Запустите `oneagentctl` с параметром `--version`. Дополнительную информацию см. в разделе [Настройка OneAgent через интерфейс командной строки](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### Обзор хостов

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Нажмите на интересующий вас хост.
3. Разверните раздел **Properties** под именем хоста. Установленная версия OneAgent включена в список отображаемых свойств.

### Статус развёртывания

1. Перейдите в **Deployment Status**.
2. Нажмите на вкладку **All hosts** или **Recently connected hosts**.
3. Разверните запись интересующего вас хоста. Установленная версия OneAgent включена в отображаемую информацию.
