---
title: Обновление OneAgent на Solaris
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/update-oneagent-on-solaris
scraped: 2026-05-12T11:09:46.871186
---

# Обновление OneAgent на Solaris

# Обновление OneAgent на Solaris

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Чтобы обновить установленный экземпляр OneAgent на Solaris (x86 и SPARC), следуйте приведённым ниже инструкциям:

1. Повторите все шаги [первоначальной установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC)."), но установите OneAgent в новый каталог.
2. Остановите все мониторируемые процессы.
3. Переименуйте текущий каталог установки OneAgent (например, `/opt/dynatrace/oneagent-old`) с помощью следующей команды:

   `mv /opt/dynatrace/oneagent /opt/dynatrace/oneagent-old`.

   Этот каталог можно удалить после обновления OneAgent.
4. Переименуйте обновлённую папку OneAgent так, чтобы она указывала на исходный каталог установки (например, `/opt/dynatrace/oneagent`), с помощью следующей команды:

   `mv /opt/dynatrace/oneagent-update /opt/dynatrace/oneagent`
5. Перезапустите все процессы, которые должны мониториться.

## Проверка установленной версии OneAgent

Используйте один из этих методов, чтобы проверить, какая версия OneAgent установлена у вас в настоящее время.

### Обзор хоста

1. Перейдите в **Hosts**.
2. Щёлкните интересующий вас хост.
3. Разверните **Properties** под именем хоста. Установленная версия OneAgent указана в перечисленных свойствах.

### Статус развёртывания

1. Перейдите в **Deployment Status**.
2. Откройте вкладку **All hosts** или **Recently connected hosts**.
3. Разверните интересующую вас запись хоста. Установленная версия OneAgent включена в отображаемую информацию.