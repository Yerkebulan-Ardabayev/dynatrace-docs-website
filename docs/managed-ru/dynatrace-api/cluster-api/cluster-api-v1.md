---
title: Cluster API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1
scraped: 2026-05-12T12:04:47.499302
---

# Cluster API v1

# Cluster API v1

* Опубликовано: 18 ноября 2020

Dynatrace Managed предоставляет функциональность на уровне кластера через REST-эндпойнты. Эта интерактивная документация также работает как REST-клиент, через который можно взаимодействовать с кластерами Dynatrace Managed.

Чтобы перейти к Cluster API

1. Откройте Cluster Management Console.
2. Откройте меню пользователя, нажав на иконку пользователя в правом верхнем углу.
3. Выберите **Cluster API v1**.

### Cluster

* [Получить информацию о кластере по известным узлам](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-info-known-servers "Узнайте, как через Dynatrace API получить информацию о кластере для известных узлов.")
* [Получить конфигурацию узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration "Узнайте, как через Dynatrace API получить конфигурацию узлов кластера.")
* [Настроить роли узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities "Узнайте, как настроить роли узлов кластера.")
* [Получить текущий статус конфигурации узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-current-status "Узнайте, как через Dynatrace API получить текущий статус конфигурации узлов кластера.")
* [Получить статус запроса на конфигурацию узлов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-request-status "Узнайте, как через Dynatrace API получить статус запросов на конфигурацию узлов кластера.")
* [Получить детали текущего режима обслуживания кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-maintenance "Узнайте, как через Dynatrace API получить детали текущего режима обслуживания кластера.")
* [Включить режим обслуживания кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-on "Узнайте, как включить режим обслуживания кластера.")
* [Выключить режим обслуживания кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-off "Узнайте, как выключить режим обслуживания кластера.")

### Интернет-прокси

* [Получить конфигурацию прокси кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration "Узнайте, как через Dynatrace API получить конфигурацию прокси кластера.")
* [Задать или обновить конфигурацию прокси кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration "Узнайте, как через Dynatrace API задать или обновить конфигурацию прокси кластера.")
* [Удалить конфигурацию прокси кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration "Узнайте, как через Dynatrace API удалить конфигурацию прокси кластера.")
* [Проверить конфигурацию прокси кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration "Узнайте, как через Dynatrace API проверить конфигурацию прокси кластера.")
* [HA: получить конфигурации прокси для всех дата-центров](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha-all "Узнайте, как через Dynatrace API получить конфигурации прокси для всех дата-центров в premium high availability развёртываниях.")
* [HA: получить конфигурацию прокси для конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API получить конфигурацию прокси для конкретного дата-центра в premium high availability развёртываниях.")
* [HA: задать или обновить конфигурацию прокси для конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API задать или обновить конфигурацию прокси в конкретном дата-центре.")
* [HA: удалить конфигурацию прокси в конкретном дата-центре](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API удалить конфигурацию прокси в конкретном дата-центре.")
* [HA: проверить конфигурацию прокси из конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API проверить конфигурацию прокси из конкретного дата-центра.")

#### High Availability развёртывания

[Получить конфигурации прокси для всех дата-центров](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha-all "Узнайте, как через Dynatrace API получить конфигурации прокси для всех дата-центров в premium high availability развёртываниях.")

[Получить конфигурацию прокси для конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API получить конфигурацию прокси для конкретного дата-центра в premium high availability развёртываниях.")

[Задать или обновить конфигурацию прокси для конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API задать или обновить конфигурацию прокси в конкретном дата-центре.")

[Удалить конфигурацию прокси в конкретном дата-центре](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API удалить конфигурацию прокси в конкретном дата-центре.")

[Проверить конфигурацию прокси из конкретного дата-центра](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration-ha "Узнайте, как через Dynatrace API проверить конфигурацию прокси из конкретного дата-центра.")

### Парольная политика

* [Получить парольную политику кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/get-cluster-password-policy "Узнайте, как через Dynatrace API получить парольную политику кластера.")
* [Обновить парольную политику кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/put-cluster-password-policy "Узнайте, как через Dynatrace API обновить парольную политику кластера.")

### SSL-сертификаты

* [Получить детали SSL-сертификата кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-details "Узнайте, как через Dynatrace API получить детали SSL-сертификата кластера.")
* [Получить статус хранилища SSL-сертификатов кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-storage-status "Узнайте, как через Dynatrace API получить статус хранилища SSL-сертификатов кластера.")
* [Сохранить SSL-сертификат кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Узнайте, как через Dynatrace API сохранить SSL-сертификат кластера.")

### Пользователи

* [Получить список пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-users "Узнайте, как через Dynatrace API получить список пользователей кластера.")
* [Обновить пользователя](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/put-update-user "Узнайте, как через Dynatrace API обновить пользователя кластера.")
* [Создать пользователя](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-user "Узнайте, как через Dynatrace API создать пользователя кластера.")
* [Получить пользователя](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-user "Узнайте, как через Dynatrace API получить конкретного пользователя кластера.")
* [Удалить пользователя](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/delete-user "Узнайте, как через Dynatrace API удалить пользователя кластера.")
* [Создать учётные записи пользователей кластера](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-users "Узнайте, как настроить несколько учётных записей пользователей кластера.")

### Группы пользователей

* [Получить группы пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-user-groups "Узнайте, как через Dynatrace API получить конкретные группы пользователей кластера.")
* [Обновить группу пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-user-groups "Узнайте, как через Dynatrace API обновить группу пользователей кластера.")
* [Создать группу пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-user-group "Узнайте, как через Dynatrace API создать группу пользователей кластера.")
* [Получить группу пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group "Узнайте, как через Dynatrace API получить конкретного пользователя кластера.")
* [Удалить группу пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/delete-group "Узнайте, как через Dynatrace API удалить пользователя кластера.")
* [Создать группы пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-users-groups "Узнайте, как настроить несколько групп пользователей кластера.")
* [Получить management zones для групп пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-groups-mz "Узнайте, как через Dynatrace API получить разрешения management zone для всех групп.")
* [Обновить management zones для группы пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-group-mz "Узнайте, как через Dynatrace API обновить management zones для одной группы пользователей.")
* [Получить management zones для группы пользователей](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group-mz "Узнайте, как через Dynatrace API получить разрешения management zone для конкретной группы.")