---
title: Настройка свойств кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-properties
---

# Настройка свойств кластера

# Настройка свойств кластера

* Практическое руководство
* Чтение за 1 минуту
* Обновлено 18 июня 2026 г.

Настраиваемые свойства для Dynatrace Managed хранятся в файле `/opt/dynatrace-managed/server/conf/config.properties`, но менять их в этом файле не нужно. Файл перезаписывается во время обновления.

Если настраивать свойства напрямую в `/opt/dynatrace-managed/server/conf/config.properties`, **пользовательская конфигурация не сохранится при обновлении**.

Вместо изменения `/opt/dynatrace-managed/server/conf/config.properties` все изменения нужно вносить в файл `custom.settings`, расположенный в каталоге `/opt/dynatrace-managed/installer` на каждом узле Managed Cluster. Этот файл можно создать, если он ещё не существует. Во время обновления инсталлятор считывает `custom.settings` и соответствующим образом изменяет `config.properties`.

Файл `custom.settings` определяет:

* Расположение файла, который нужно изменить
* Раздел для изменения
* Свойство и значение, которое нужно установить

## Пример правок custom.settings

Допустим, внесены два изменения в настройки:

* Свойству `connection-timeout` присвоено значение `3000000`
* Свойству `proxy-off` присвоено значение `true`

Чтобы сохранить эти настройки при обновлении:

1. Открыть файл `custom.settings`.

   * Расположение файла: каталог `/opt/dynatrace-managed/installer` на узле.
   * Если файла ещё нет по этому пути, его нужно создать.
2. Добавить одну строку, указывающую конфигурационный файл, который нужно изменить во время установки.

   ```
   <server/conf/config.properties>
   ```

   Угловые скобки (`<` и `>`) нужно включить.
3. Добавить две строки, указывающие раздел, имя свойства и значение свойства, которое нужно изменить для `connection-timeout`, находящегося в разделе `[settings]`.

   ```
   [settings]



   connection-timeout=3000000
   ```
4. Добавить две строки, указывающие раздел, имя свойства и значение свойства, которое нужно изменить для `proxy-off`, находящегося в разделе `[http.client.external]`.

   ```
   [http.client.external]



   proxy-off = true
   ```
5. Итоговый файл `custom.settings` для этого примера теперь должен выглядеть так:

   ```
   <server/conf/config.properties>



   [settings]



   connection-timeout=3000000



   [http.client.external]



   proxy-off = true
   ```

Этот файл `custom.settings` нужно разместить на всех узлах Managed Cluster в каталоге `/opt/dynatrace-managed/installer`. При каждом обновлении узла инсталлятор устанавливает `connection-timeout` в `3000000` и `proxy-off` в `true` в `config.properties`, сохраняя пользовательскую конфигурацию.

Применяется при перезапуске служб

Dynatrace Managed также выполняет это пользовательское действие по конфигурации при каждом перезапуске службы Dynatrace.