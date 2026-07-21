---
title: Настройка записей DNS кластера
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-dns-entries
---

# Настройка записей DNS кластера

# Настройка записей DNS кластера

* Практическое руководство
* Чтение за 1 минуту
* Обновлено 18 июня 2026 г.

Если нужно настроить собственный SSL-сертификат (см. [Установка собственного SSL-сертификата](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation."), также нужно создать собственное доменное имя для домена Managed Cluster. Укажи публичную конечную точку и обнови локальную систему доменных имён (DNS).

Некорректная конфигурация может привести к простою Managed Cluster

Некорректная конфигурация DNS может привести к несоответствию данных или к простою Managed Cluster. Никакой конфигурации, кроме описанных ниже шагов, не требуется.

## Укажи публичную конечную точку

Перейди в **Settings** > **Public endpoints** и введи адрес, который обычно используется для доступа к веб-интерфейсу Dynatrace (собственное доменное имя).

## Добавь записи в локальный DNS

Для каждого узла Dynatrace Managed добавь запись с его IP-адресом и доменом.
Если используется сопоставление имён хостов с IP-адресами, создай записи `A` в следующем формате:
`Host Type IP`

Например:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3
```

Чтобы разрешить маршрутизацию балансировщика нагрузки по отдельным узлам, добавь отдельные поддомены для каждого узла.

Например:

```
dynatrace.mycompany.com  A 10.176.0.1, 10.176.0.2, 10.176.0.3



n01.dynatrace.mycompany.com  A 10.176.0.1



n02.dynatrace.mycompany.com  A 10.176.0.2



n03.dynatrace.mycompany.com  A 10.176.0.3
```