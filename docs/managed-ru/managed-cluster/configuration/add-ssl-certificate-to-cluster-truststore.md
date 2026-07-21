---
title: Добавление сертификата в хранилище доверенных сертификатов
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/add-ssl-certificate-to-cluster-truststore
---

# Добавление сертификата в хранилище доверенных сертификатов

# Добавление сертификата в хранилище доверенных сертификатов

* Практическое руководство
* Чтение 1 мин.
* Обновлено 18 июня 2026 г.

Добавь SSL-сертификат в хранилище доверенных сертификатов Managed Cluster, если Managed Cluster не может проверить SSL-соединения. Добавление сертификата обычно требуется при отправке уведомлений по электронной почте или через webhook с самоподписанным сертификатом.

## Проверка отклонения сертификата

Если у Managed Cluster возникают проблемы с отправкой уведомлений, найди [файлы в каталоге журналов](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") установки узла Managed Cluster, имя которых соответствует шаблону `Server.*.*.log`.

Если в папке журналов есть файлы с таким именем, поищи в этих файлах журнала следующую запись:

```
sun.security.validator.ValidatorException: PKIX path building failed:



sun.security.provider.certpath.SunCertPathBuilderException
```

Отклонение сертификата обычно происходит, когда сертификат, предоставленный получателем уведомления, не принимается узлом Managed Cluster. Причина этого, как правило, в том, что сертификату не доверяют.

## Добавление сертификата в хранилище доверенных сертификатов

Используй PEM-сертификат (`.crt`, `.pem`, `.cer`) и запусти скрипт переконфигурации на каждом узле Managed Cluster с параметрами `--update-cert` и `--network-proxy-cert-file`. Используй команду `nohup`, чтобы предотвратить прерывание выполнения скрипта (например, из-за разрыва сессии) во время важных операций.

```
nohup <PRODUCT_PATH>/installer/reconfigure.sh --update-cert --network-proxy-cert-file <cert_file>.cer &
```

Замени `<PRODUCT_PATH>` на путь установки Dynatrace Managed (по умолчанию: `/opt/dynatrace-managed`), а `<cert_file>` на имя файла своего сертификата.

Параметр прокси

Параметр `--network-proxy-cert-file` передаёт сертификат прокси для Dynatrace Managed, но его также можно использовать для передачи сертификата для любого защищённого соединения с Managed Cluster.