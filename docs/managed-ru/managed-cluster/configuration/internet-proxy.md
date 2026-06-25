---
title: Настройка интернет-прокси для кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/internet-proxy
scraped: 2026-05-12T11:37:00.709507
---

# Настройка интернет-прокси для кластера

# Настройка интернет-прокси для кластера

* How-to guide
* 3-min read
* Updated on Dec 16, 2025

Настройте интернет-соединение, чтобы включить [проактивную поддержку Mission Control](/managed/managed-cluster/basics/mission-control-proactive-support "Mission Control proactively monitors your Managed Cluster, provides software updates, and keeps your installation secure and reliable."), получать обновления Mission Control и использовать внешние уведомления о проблемах через такие инструменты, как ServiceNow, Jira и webhooks.

Протоколы аутентификации

Доступны следующие протоколы аутентификации:

* Basic
* NTLMv1 (устарел)

## Настройка интернет-прокси

Существует три способа настройки прокси-соединения для Managed Cluster. Выберите подходящий.

[**При установке Managed**](/managed/managed-cluster/configuration/internet-proxy#during-installation "Configure a proxy connection for your Managed Cluster if you don't have direct internet access.")[**Через Cluster Management Console**](/managed/managed-cluster/configuration/internet-proxy#cluster-management-console "Configure a proxy connection for your Managed Cluster if you don't have direct internet access.")[**Через Cluster API**](/managed/managed-cluster/configuration/internet-proxy#cluster-api "Configure a proxy connection for your Managed Cluster if you don't have direct internet access.")

### При установке Managed

Для настройки прокси-соединения с Mission Control во время установки Managed используйте следующие параметры командной строки:

```
--network-proxy
```

Если ваш компьютер использует сетевой прокси для подключения к интернету, введите адрес в следующем формате:

```
protocol://[user:password@]server-address:port
```

Значение по умолчанию — `none`.

```
--network-proxy-cert-file
```

Если ваш компьютер использует сетевой HTTPS-прокси с самоподписанным сертификатом, расширьте хранилище доверенных сертификатов. После этого параметра укажите полный путь к файлу публичного SSL-сертификата в формате PEM.

### Через Cluster Management Console

1. Войдите в **Cluster Management Console**.
2. Перейдите в **Settings** > **Internet proxy** и отредактируйте **Proxy configuration** для конкретного центра обработки данных.
3. Выберите **Connect via proxy** и введите параметры прокси-сервера:

   * **Scheme**
   * **Proxy address** и **Port**
   * **Username** и **Password**, если анонимный доступ недоступен.

#### Исключение хостов из интернет-прокси

Для исключения хостов из прокси — например, когда интеграции с проблемами через webhooks указывают на хосты внутренней сети — добавьте их в список исключений. Используйте подстановочный символ (`*`) в начале или конце каждой записи хоста для сопоставления со всеми URL внутри домена.

### Через Cluster API

Для установки или обновления конфигурации интернет-прокси Managed Cluster используйте [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration "Learn how to use the Dynatrace API to set or update cluster proxy configuration.").

## Частые вопросы

Можно ли использовать прозрачный прокси?

Да, Dynatrace поддерживает настройку прозрачного прокси.

Прозрачный прокси (также известный как перехватывающий, встроенный или принудительный прокси) может маршрутизировать и перехватывать обмен данными Managed Cluster с Mission Control. Обычно он располагается между Managed Cluster и Mission Control. С помощью прозрачного прокси можно проводить аудит и проверку всех передаваемых данных.

Dynatrace не нужно знать о прокси. Настройте Dynatrace Managed на доверие корневому сертификату, закрытый ключ которого известен прокси. При такой схеме прокси может анализировать содержимое SSL/TLS-транзакций, эффективно выполняя атаку типа «человек посередине», которую Dynatrace авторизует, доверяя корневому сертификату прокси.

Как обновить SSL-сертификат?

Запустите скрипт перенастройки со следующими параметрами:

```
/opt/dynatrace-managed/installer/reconfigure.sh --update-cert --network-proxy-cert-file <proxy_cert_file>
```