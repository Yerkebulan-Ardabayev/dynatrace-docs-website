---
title: Поддержка Flatcar в SELinux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/flatcar-os
scraped: 2026-05-12T11:05:21.237495
---

# Поддержка Flatcar в SELinux

# Поддержка Flatcar в SELinux

* Чтение: 1 мин
* Опубликовано 30 мая 2023 г.

OneAgent теперь можно развернуть на [Flatcar](https://dt-url.net/u5034bo). Однако из-за определённых ограничений, связанных с работой SELinux в данной операционной системе, необходимо учитывать следующие ограничения конфигурации:

* Flatcar использует файловую систему только для чтения. Поэтому, если вы планируете использовать SELinux совместно с OneAgent, требуется специальная конфигурация. Подробнее о совместимости контейнеров с политикой SELinux см. в документации Flatcar: [Check a containerâs compatibility with SELinux policy](https://dt-url.net/ns0342m).
* Используйте путь по умолчанию при установке OneAgent с включённым SELinux.

* По умолчанию Flatcar использует политику Multi-Category Security (MCS). Для обеспечения совместимости необходимо изменить этот параметр на политику `targeted` в файле `/etc/selinux/config`.

  ```
  SELINUXTYPE=targeted
  ```