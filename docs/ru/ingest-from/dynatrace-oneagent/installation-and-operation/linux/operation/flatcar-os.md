---
title: Поддержка Flatcar на SELinux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/flatcar-os
scraped: 2026-03-06T21:19:03.893393
---

# Поддержка Flatcar в SELinux


* Latest Dynatrace
* 1-min read

OneAgent теперь можно развернуть на [Flatcar](https://dt-url.net/u5034bo). Однако из-за определённых ограничений в работе SELinux на этой операционной системе необходимо учесть следующие ограничения конфигурации:

* Flatcar работает на файловой системе только для чтения. Поэтому, если вы планируете использовать SELinux с OneAgent, требуется специальная конфигурация. Дополнительные сведения о совместимости контейнеров с политикой SELinux см. в документации Flatcar: [Проверка совместимости контейнера с политикой SELinux](https://dt-url.net/ns0342m).
* Используйте путь по умолчанию для установки OneAgent с включённым SELinux.

* По умолчанию Flatcar использует политику Multi-Category Security (MCS). Для обеспечения совместимости необходимо изменить этот параметр на политику `targeted` в файле `/etc/selinux/config`.

  ```
  SELINUXTYPE=targeted
  ```
