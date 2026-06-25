---
title: Настраиваемые свойства Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configurable-properties-of-dynatrace-managed
scraped: 2026-05-12T11:52:58.100050
---

# Настраиваемые свойства Dynatrace Managed

# Настраиваемые свойства Dynatrace Managed

* Updated on Nov 04, 2025

Настраиваемые свойства Dynatrace Managed хранятся в файле `/opt/dynatrace-managed/server/conf/config.properties`, однако редактировать их непосредственно в этом файле не следует — он перезаписывается при обновлении.

Если вы настраиваете свойства непосредственно в `/opt/dynatrace-managed/server/conf/config.properties`, **ваша пользовательская конфигурация не сохранится при обновлении**.

Вместо редактирования `/opt/dynatrace-managed/server/conf/config.properties` вносите все изменения в файл `custom.settings`, расположенный в каталоге `/opt/dynatrace-managed/installer` на каждом узле кластера. Если файл не существует, его можно создать. При обновлении установщик читает `custom.settings` и соответствующим образом изменяет `config.properties`.

В файле `custom.settings` указывается:

* Расположение файла, подлежащего изменению
* Раздел, который необходимо изменить
* Свойство и значение, которые необходимо задать

## Примеры изменений custom.settings

Предположим, вы внесли два изменения в настройки:

* Установили значение свойства `connection-timeout` равным `3000000`
* Установили значение свойства `proxy-off` равным `true`

Для сохранения этих настроек при обновлении:

1. Откройте файл `custom.settings` для редактирования.

   * Расположение файла: каталог `/opt/dynatrace-managed/installer` на узле кластера.
   * Если файл не существует — создайте его в этом каталоге.
2. Добавьте одну строку, указывающую файл конфигурации, который необходимо изменить при установке.

   ```
   <server/conf/config.properties>
   ```

   Обязательно включите угловые скобки (`<` и `>`).
3. Добавьте две строки, указывающие раздел, имя и значение свойства, которое необходимо изменить для `connection-timeout` (свойство находится в разделе `[settings]`).

   ```
   [settings]



   connection-timeout=3000000
   ```
4. Добавьте две строки, указывающие раздел, имя и значение свойства, которое необходимо изменить для `proxy-off` (свойство находится в разделе `[http.client.external]`).

   ```
   [http.client.external]



   proxy-off = true
   ```
5. Итоговый файл `custom.settings` для данного примера должен выглядеть следующим образом:

   ```
   <server/conf/config.properties>



   [settings]



   connection-timeout=3000000



   [http.client.external]



   proxy-off = true
   ```

При наличии данного файла `custom.settings` на всех узлах кластера в каталоге `/opt/dynatrace-managed/installer` каждый раз при обновлении узла установщик будет устанавливать `connection-timeout` равным `3000000`, а `proxy-off` — равным `true` в файле `config.properties`, сохраняя тем самым вашу пользовательскую конфигурацию.

Применяется при перезапуске сервисов

Dynatrace Managed также выполняет это действие по пользовательской конфигурации при каждом перезапуске сервиса Dynatrace.