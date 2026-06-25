---
title: Как передать адрес прокси при установке OneAgent на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-linux
scraped: 2026-05-12T11:05:29.578798
---

# Как передать адрес прокси при установке OneAgent на Linux

# Как передать адрес прокси при установке OneAgent на Linux

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Установщик OneAgent распознаёт параметры `--set-proxy` (рекомендуется начиная с версии 1.185) или `PROXY`. Значением этих параметров является адрес прокси-сервера. Номер порта добавляется после двоеточия, например `172.1.1.128:8080`. Для прокси с аутентификацией можно указать имя пользователя и пароль так: `username:password@172.1.1.128:8080`, где имя пользователя и пароль должны быть в URL-кодировке. Также поддерживаются адреса IPv6.

Имена параметров чувствительны к регистру, поэтому используйте `ALL CAPS` для имён параметров.

## Передача адреса прокси установщику

Предположим, вы используете сервер openSUSE, скачали установщик OneAgent в каталог `/tmp`, а IP-адрес вашего прокси равен `10.1.1.5`. В таком случае установку следует начать так:

```
cd /tmp



chmod +x Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh



su -c 'Dynatrace-OneAgent-Linux-0.5.0-20140217-175809.sh --set-proxy=10.1.1.5'
```

## Изменение прокси после установки

Если требуется изменить адрес прокси после установки, используйте `--set-proxy` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").