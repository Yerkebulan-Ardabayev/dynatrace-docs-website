---
title: Конфигурация DNS для Dynatrace Managed
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/dns-configuration-in-managed
scraped: 2026-05-12T11:53:01.709124
---

# Конфигурация DNS для Dynatrace Managed

# Конфигурация DNS для Dynatrace Managed

* Published Aug 06, 2020

Если вам необходимо настроить собственный SSL-сертификат (см. раздел [Установка собственного SSL-сертификата](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")), также потребуется создать собственное доменное имя для домена кластера. Для этого необходимо указать публичную конечную точку и изменить локальный DNS.

Неправильная конфигурация может привести к отказу кластера

Неправильная конфигурация DNS может привести к несоответствию данных или отказу кластера. Никакой дополнительной настройки, помимо шагов, описанных ниже, не требуется.

#### Указание публичной конечной точки

Перейдите в **Settings** > **Public endpoints** и введите адрес, который вы обычно используете для доступа к веб-интерфейсу кластера Dynatrace (ваше собственное доменное имя).

#### Добавление записей в локальный DNS

Для каждого узла Dynatrace Managed добавьте запись его IP-адреса и вашего домена.
Если вы используете сопоставление имён хостов с IP-адресами, добавьте записи типа `A` в следующем формате:  
`Host Type IP`

Например:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3
```

Дополнительно можно добавить отдельные поддомены для каждого узла в целях маршрутизации балансировщика нагрузки.

Например:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3



n01.dynatrace.mycompany.com  A 10.176.0.1



n02.dynatrace.mycompany.com  A 10.176.0.2



n03.dynatrace.mycompany.com  A 10.176.0.3
```