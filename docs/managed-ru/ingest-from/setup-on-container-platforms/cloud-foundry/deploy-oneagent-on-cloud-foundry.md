---
title: Развёртывание BOSH release для полного стекового мониторинга на Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry
scraped: 2026-05-12T11:11:01.027325
---

# Развёртывание BOSH release для полного стекового мониторинга на Cloud Foundry

# Развёртывание BOSH release для полного стекового мониторинга на Cloud Foundry

* 6-min read
* Updated on Oct 12, 2022

Следующие рекомендации применяются при развёртывании Dynatrace OneAgent на виртуальных машинах Cloud Foundry, включая компоненты Cloud Foundry, Diego cells и Windows Diego cells.

Существует два подхода к развёртыванию BOSH release OneAgent: immutable и lightweight. Ознакомьтесь со [стратегиями развёртывания](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Настройка Dynatrace на Cloud Foundry."), чтобы определить наиболее подходящий для ваших задач.

Immutable release

Lightweight release

1. [Создайте PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Концепция токена доступа и его областей видимости.").
2. [Разверните Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Настройка ActiveGate") (только для клиентов SaaS).
3. Найдите URL загрузки — проверьте документацию [Deployment API](/managed/dynatrace-api/environment-api/deployment "Загрузка установщиков OneAgent и ActiveGate через Dynatrace API."), входящего в состав Environment API v1.
4. Получите последние версии BOSH release.

   ```
   curl -X GET https://{api-url}/api/v1/deployment/boshrelease/versions/unix -H /



   'Authorization: Api-Token {paas-token}'
   ```

5. Загрузите BOSH release.

   Для Dynatrace SaaS замените `{api-url}` адресом Environment ActiveGate.

   ```
   wget  -O dynatrace-release.tgz --header="Authorization: Api-Token {paas-token}" /



   https://{api-url}/api/v1/deployment/boshrelease/agent/unix/version/{version}?skipMetadata=true
   ```

   Загрузка Windows BOSH release

   ```
   wget  -O dynatrace-release.tgz --header="Authorization: Api-Token {paas-token}" /



   https://{api-url}/api/v1/deployment/boshrelease/agent/windows/version/{version}?skipMetadata=true
   ```

6. Проверьте контрольную сумму release.

   Для Dynatrace SaaS замените `{api-url}` адресом Environment ActiveGate.

   ```
   curl -H "Authorization: Api-Token {paas-token}"  /



   https://{api-url}/api/v1/deployment/boshrelease/agent/windows/version/{version}/checksum?skipeMetadata=true



   # пример ответа:



   {"sha256":"13658655d922aedc93951b545e8b881b76a77545ba6f8442828cfed53ffac3a8"}



   # проверьте контрольную сумму файла:



   echo "13658655d922aedc93951b545e8b881b76a77545ba6f8442828cfed53ffac3a8 dynatrace-release.tgz" | sha256sum -c



   # если контрольная сумма совпадает:



   dynatrace-release.tgz: OK



   # если не совпадает:



   # dynatrace-release.tgz FAILED



   # sha256sum: WARNING: 1 computed checksum did NOT match
   ```

7. Убедитесь, что BOSH CLI подключён к BOSH Director. Подробнее см. в документации Cloud Foundry или VMware Tanzu.
8. Загрузите BOSH release OneAgent в BOSH Director.

   ```
   bosh -e my-env upload-release PATH-TO-BINARY/dynatrace-release.tgz
   ```

9. Создайте файл конфигурации среды выполнения `runtime-config-dynatrace.yml` и адаптируйте настройки:

   * Ключ `apiurl`:

   Для Dynatrace SaaS с подключением к интернету

   Замените `ENVIRONMENTID` в `https://ENVIRONMENTID.live.dynatrace.com/api` на ваш ID окружения.

   Для Dynatrace SaaS без доступа к интернету

   Используйте `https://YourActiveGateIP` или `FQDN:9999/e/<ENVIRONMENTID>/api` для загрузки OneAgent и маршрутизации трафика через ActiveGate.

   Рекомендуется использовать ActiveGate в качестве конечной точки подключения. По умолчанию ActiveGate использует самоподписанный сертификат. Если вы хотите использовать доверенный CA вместо самоподписанного сертификата или получаете ошибки SSL, следуйте [инструкциям по настройке ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate.").

   Для Dynatrace Managed

   Используйте `https://YourActiveGateIP`, или `FQDN/e/<ENVIRONMENTID>/api`, или IP-адрес сервера ActiveGate для прямого подключения.
   В зависимости от настроек может потребоваться указать порт.

   Рекомендуется использовать ActiveGate в качестве конечной точки подключения. По умолчанию ActiveGate использует самоподписанный сертификат. Если вы хотите использовать доверенный CA или получаете ошибки SSL, следуйте [инструкциям по настройке ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Настройка SSL-сертификата на ActiveGate.").

   * Необязательно: настройте сетевые зоны:
     Для настройки сетевых зон используйте аргумент установщика: `--set-network-zone=<your.network.zone>`.
     Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Принцип работы сетевых зон в Dynatrace.").

   ```
   releases:



   - name: dynatrace-oneagent



   version: 1.187.100.20200217-114813



   addons:



   - name: dynatrace-oneagent-addon



   jobs:



   - name: dynatrace-oneagent



   release: dynatrace-oneagent



   properties:



   dynatrace:



   environmentid: <environmentId>



   # Следующие ключи обязательны для immutable release 1.177+



   apitoken: <paas-token>



   ###



   # необязательные свойства



   ###



   # Замените на URL Dynatrace Managed, включая ID окружения



   apiurl: https://{your-managed-cluster.com}/e/{environmentid}/api



   # Установите 'all' для принятия всех самоподписанных SSL-сертификатов



   sslmode: all



   # Укажите прокси для связи (только для BOSH)



   proxy: https://your-proxy-url



   # Укажите группу хостов для ВМ в этом развёртывании



   hostgroup: example_hostgroup



   # Определите теги хостов для ВМ в этом развёртывании



   hosttags: landscape=production team=my_team



   # Определите пользовательские свойства для ВМ в этом развёртывании



   hostprops: Department=Acceptance Stage=Sprint



   # Включить режим мониторинга только инфраструктуры (1 = включено)



   infraonly: 0



   # Включить проверку загрузки через сертификат (true = включено)



   validatedownload: false



   # Передача аргументов установщика



   installerargs: USER=vcap GROUP=vcap --set-network-zone=<your.network.zone>



   include:



   deployments:



   - name-of-your-deployment



   stemcell:



   - os: ubuntu-xenial



   exclude:



   lifecycle: errand
   ```

10. Обновите конфигурацию среды выполнения BOSH Director.

    Замените `PATH` на путь к файлу `runtime-config-dynatrace.yml`.

    ```
    bosh -e my-env update-runtime-config PATH/runtime-config-dynatrace.yml
    ```

    Эта конфигурация применяется ко всем новым BOSH-развёртываниям.

    При наличии нескольких конфигураций с разными версиями OneAgent удалите старые с помощью `bosh delete-config`.

11. Примените изменения.

    Поскольку существующие BOSH-развёртывания не обновляются автоматически, необходимо выполнить повторное развёртывание.

    ```
    bosh -e my-env -d deployment deploy
    ```

Эта версия не рекомендуется для контролируемых production-окружений, так как автоматически загружает последний release OneAgent при каждом `bosh deploy`.

Последний release OneAgent можно контролировать в разделе [обновлений OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Способы обновления OneAgent на Linux.").

1. Загрузите lightweight OneAgent BOSH release из [репозитория GitHub Dynatrace](https://github.com/Dynatrace/bosh-oneagent-release).
2. Убедитесь, что BOSH CLI подключён к BOSH Director.
3. Загрузите BOSH release OneAgent в BOSH Director.

   ```
   bosh -e my-env upload-release PATH-TO-BINARY/dynatrace-release.tgz
   ```

4. Создайте файл `runtime-config-dynatrace.yml` и настройте параметры (аналогично описанному выше для immutable release).

5. Обновите конфигурацию среды выполнения BOSH Director.

   ```
   bosh -e my-env update-runtime-config PATH/runtime-config-dynatrace.yml
   ```

6. Примените изменения.

   ```
   bosh -e my-env -d deployment deploy
   ```

## Связанные темы

* [Мониторинг Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Мониторинг Cloud Foundry с помощью Dynatrace.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Поддерживаемые возможности OneAgent на разных ОС и платформах.")