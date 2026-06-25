---
title: Добавление SSL-сертификата в TrustStore кластера Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/how-to-add-a-certificate-to-server-trust-store
scraped: 2026-05-12T11:53:05.491075
---

# Добавление SSL-сертификата в TrustStore кластера Dynatrace Managed

# Добавление SSL-сертификата в TrustStore кластера Dynatrace Managed

* Published Jan 08, 2018

Иногда может потребоваться вручную добавить SSL-сертификат в TrustStore кластера Dynatrace Managed — например, если кластер отказывается принимать SSL-сертификат при отправке email или webhook-уведомлений. Это обычно происходит при использовании самоподписанного сертификата.

## Как определить, что кластер не принимает сертификаты

Если кластер испытывает проблемы с отправкой уведомлений, просмотрите файлы в [каталоге журналов](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.") установки узла кластера, имена которых соответствуют шаблону `Server.*.*.log`.

Если в каталоге журналов присутствуют файлы с таким именем, найдите в них следующую запись:

```
sun.security.validator.ValidatorException: PKIX path building failed:



sun.security.provider.certpath.SunCertPathBuilderException
```

Подобные записи в журнале свидетельствуют о том, что сертификат, предоставленный получателем уведомлений, не был принят узлом кластера. Причина обычно заключается в том, что сертификат не является доверенным.

## Добавление пользовательского сертификата в TrustStore узла кластера

Используйте сертификат PEM (`.crt`, `.pem`, `.cer`) и выполните скрипт перенастройки на каждом узле кластера с параметрами `--update-cert` и `--network-proxy-cert-file`. Используйте команду `nohup`, чтобы предотвратить прерывание выполнения скрипта (например, при разрыве сессии) во время важных операций.

`nohup <PRODUCT_PATH>/installer/reconfigure.sh --update-cert --network-proxy-cert-file <cert_file>.cer &`

Параметр прокси

Параметр `--network-proxy-cert-file` предназначен для предоставления прокси-сертификата для Managed, однако его также можно использовать для предоставления сертификата любого защищённого подключения к кластеру Managed.