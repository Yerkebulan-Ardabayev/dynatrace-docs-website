---
title: Установка
source: https://docs.dynatrace.com/managed/managed-cluster/installation
scraped: 2026-05-12T11:11:15.011604
---

# Установка

# Установка

* 1-min read
* Updated on May 09, 2026

Установите и настройте Managed Cluster Dynatrace. Сначала ознакомьтесь с требованиями к аппаратному обеспечению, операционной системе и сети, затем запустите установщик кластера. После установки можно добавить узлы, установить Cluster ActiveGate и настроить SSL-сертификаты. Для сред без доступа к интернету в разделе «Офлайн-режим» описаны все необходимые шаги.

## Предварительные требования

[### Аппаратные требования

Ознакомьтесь с требованиями к CPU, RAM, хранилищу и масштабированию в многоузловых конфигурациях.](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.")[### Требования к операционной системе

Ознакомьтесь с поддерживаемыми дистрибутивами Linux и требованиями к хосту.](/managed/managed-cluster/installation/operating-system-requirements "Review the operating system, host, and network requirements you need to meet before installing Dynatrace Managed on a Linux host.")[### Настройка SELinux

Включите или отключите SELinux на хосте кластера перед установкой.](/managed/managed-cluster/installation/selinux "Configure Dynatrace Managed to run on a system with SELinux enabled in enforcing mode, or disable SELinux on your host.")[### Порты узлов кластера

Настройте правила фаервола для необходимых входящих и исходящих портов.](/managed/managed-cluster/installation/cluster-node-ports "Review the network ports required by Dynatrace Managed and configure your firewall for inbound and outbound communication.")[### Аппаратные требования для облачных развёртываний

Найдите рекомендуемые размеры виртуальных машин для AWS, Azure и Google Cloud.](/managed/managed-cluster/installation/managed-cloud-requirements "Find the required virtual machine sizes for deploying Dynatrace Managed on Amazon Web Services, Microsoft Azure, and Google Cloud.")

## Установка

[### Установка Managed Cluster

Загрузите, проверьте и запустите установщик Managed Cluster.](/managed/managed-cluster/installation/install-managed-cluster "Install a Managed Cluster by downloading and verifying the installer, running it, and completing the initial configuration.")[### Кастомизация установки

Настройте параметры установки: пути, порты и параметры SSL.](/managed/managed-cluster/installation/customize-managed-cluster-install "Use command line parameters to customize or automate a Managed Cluster installation, with options for datastores, system users, and SSL certificates.")[### Добавление узла кластера

Расширьте существующий кластер, добавив новый узел.](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.")[### Сертификат Managed Cluster

Настройте пользовательский SSL-сертификат на узле Managed Cluster.](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.")[### Установка Cluster ActiveGate

Установите и настройте Cluster ActiveGate для внешнего взаимодействия.](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.")[### Сертификат Cluster ActiveGate

Настройте пользовательский SSL-сертификат на Cluster ActiveGate.](/managed/managed-cluster/installation/ssl-certificate-cluster-activegate "Configure a custom SSL certificate on a Cluster ActiveGate instead of relying on Dynatrace-managed certificate automation.")

## Офлайн-режим

[### Dynatrace Managed в офлайн-режиме

Установите и обновите Dynatrace Managed без подключения к интернету.](/managed/managed-cluster/installation/dynatrace-managed-offline "Install and update Dynatrace Managed in offline mode using an offline license that disables all internet-dependent features.")[### Перевод Managed Cluster из офлайн-режима в онлайн

Переключите Managed Cluster из офлайн-режима в онлайн.](/managed/managed-cluster/installation/cluster-offline-to-online "Convert a Managed Cluster from offline to online mode by running the conversion script on each node and configuring Mission Control updates.")