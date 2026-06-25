---
title: Как передать адрес прокси при установке OneAgent на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows
scraped: 2026-05-12T11:07:36.136612
---

# Как передать адрес прокси при установке OneAgent на Windows

# Как передать адрес прокси при установке OneAgent на Windows

* Чтение: 1 мин
* Опубликовано 19 сентября 2018 г.

Установщик Windows позволяет ввести адрес прокси во время установки, поэтому в большинстве случаев можно не беспокоиться о добавлении дополнительных параметров командной строки. Параметры командной строки особенно полезны при развёртывании [установки через групповые политики](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.") или другой автоматизированной задачи.

Установщик OneAgent распознаёт параметр `--set-proxy`. Значением параметра является адрес прокси-сервера. Номер порта добавляется после двоеточия, например `172.1.1.128:8080`. Для прокси с аутентификацией можно указать имя пользователя и пароль так: `username:password@172.1.1.128:8080`, где имя пользователя и пароль должны быть в URL-кодировке. Dynatrace также поддерживает адреса IPv6.

Имена параметров чувствительны к регистру, поэтому используйте `ALL CAPS` для имён параметров.

## Передача адреса прокси установщику

Предположим, вы скачали установщик OneAgent в папку `C:\Users\Admin\Downloads`, а IP-адрес вашего прокси равен `10.1.1.5`. В таком случае установку следует начать так:

```
C:\Users\Admin\Downloads>Dynatrace-OneAgent-Windows-1.171.0.exe  --set-proxy=10.1.1.5
```

## Изменение прокси после установки

Если требуется изменить адрес прокси после установки, используйте `--set-proxy` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").