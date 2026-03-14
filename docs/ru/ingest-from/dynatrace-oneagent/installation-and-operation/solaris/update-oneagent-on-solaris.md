---
title: Обновление OneAgent на Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/update-oneagent-on-solaris
scraped: 2026-03-06T21:20:19.993240
---

# Update OneAgent on Solaris

# Update OneAgent on Solaris

* Latest Dynatrace
* 1-min read
* Published Sep 19, 2018

Чтобы обновить установленный экземпляр OneAgent на Solaris (x86 и SPARC), выполните следующие инструкции:

1. Повторите все шаги [первоначальной установки](install-oneagent-on-solaris.md "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC)."), но установите OneAgent в новый каталог.
2. Остановите все отслеживаемые процессы.
3. Переименуйте текущий каталог установки OneAgent (например, `/opt/dynatrace/oneagent-old`) с помощью следующей команды:

   `mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old`.

   Эту папку можно удалить после обновления OneAgent.
4. Переименуйте обновлённую папку OneAgent, указав на исходный каталог установки (например, `/opt/dynatrace/oneagent`) с помощью следующей команды:

   `mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent`
5. Перезапустите все процессы, которые необходимо отслеживать.

## Проверка установленной версии OneAgent

Используйте один из следующих методов, чтобы проверить, какая версия OneAgent у вас установлена.

### Host Overview

1. Перейдите в ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Нажмите на интересующий вас хост.
3. Разверните раздел **Properties** под именем хоста. Установленная версия OneAgent будет указана в списке свойств.

### Deployment status

1. Перейдите в **Deployment Status**.
2. Нажмите вкладку **All hosts** или **Recently connected hosts**.
3. Разверните запись интересующего вас хоста. Установленная версия OneAgent будет отображена в появившейся информации.
