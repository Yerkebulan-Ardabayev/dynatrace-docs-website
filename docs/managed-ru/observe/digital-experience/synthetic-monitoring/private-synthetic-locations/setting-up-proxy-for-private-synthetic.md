---
title: Настройка прокси для частного синтетического мониторинга
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic
scraped: 2026-05-12T11:32:09.378104
---

# Настройка прокси для частного синтетического мониторинга

# Настройка прокси для частного синтетического мониторинга

* How-to guide
* 3-min read
* Updated on Mar 06, 2026

Вы можете использовать [прокси, балансировщики нагрузки и обратные прокси в своём развёртывании Dynatrace](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#proxies "Узнайте о приоритетах подключения между типами ActiveGate и OneAgent-ами."). В частности, конфигурация ActiveGate позволяет определить один или несколько прокси для исходящих соединений.

* Для настройки прокси для связи с тестируемым ресурсом отредактируйте файл [`custom.properties`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Узнайте, какие свойства ActiveGate можно настроить.") и задайте свойства в секции `[synthetic]`.
* Для настройки прокси только для внутренней связи с Dynatrace Cluster см. [настройки только для связи с Dynatrace Cluster](/managed/ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate#internal "Узнайте, как настроить свойства ActiveGate для работы через прокси.").
* Для настройки одного прокси как для тестируемого ресурса, так и для Dynatrace Cluster задайте свойства в секции `[http.client]`.

## Свойства конфигурации прокси

При настройке прокси для Synthetic-enabled ActiveGate вы можете использовать следующие свойства:

| Свойство | Описание |
| --- | --- |
| `proxy-server` | Адрес сервера (имя хоста или IP-адрес) |
| `proxy-port` | Порт. Опционально. Если не задан, используется порт `8080` по умолчанию. |
| `proxy-scheme` | Схема. Опционально. Если не задана, используется схема `http` по умолчанию. Это соответствует наиболее распространённой настройке, при которой соединение с прокси инициируется по HTTP и автоматически переводится на защищённое. Всё дальнейшее взаимодействие ActiveGate через прокси защищено SSL/TLS. Необходимо установить в `https` для прокси, не поддерживающих HTTP вообще. |
| `proxy-user` | Имя пользователя. Опционально. |
| `proxy-domain` | Домен пользователя при аутентификации NTLM. |
| `proxy-password` | Пароль. Опционально. Пароль, указанный в свойстве `proxy-password`, обфусцируется после перезапуска ActiveGate, и обфусцированный пароль сохраняется в свойстве `proxy-password-encr`. Если запятая (`,`) является частью значения, необходимо добавить экранирующий обратный слеш (`\`) перед запятой. Например, `proxy-password = foo\,bar`. |
| `proxy-off` | Если установлено в `true`, прокси отключается для данного типа связи. |
| `proxy-non-proxy-hosts` | Список хостов, для связи с которыми ActiveGate не должен использовать прокси. Хосты в списке должны разделяться символами `|`. Можно также использовать звёздочку `*` в качестве символа подстановки для соответствия любой строке. Допускается только один символ подстановки: в начале или в конце имени хоста. Например, `proxy-non-proxy-hosts=*.foo.com|localhost` означает, что каждый хост в домене `foo.com` и `localhost` должны быть доступны напрямую, даже если указан прокси-сервер. Полное описание допустимого синтаксиса см. в описании параметра `http.nonProxyHosts` в [Networking Properties](https://dt-url.net/kk02v8r). |
| `proxy-authentication-schemes` | ActiveGate версии 1.271+. Список схем аутентификации прокси. Опционально. Это приоритизированный список схем аутентификации прокси, которые ActiveGate должен использовать при аутентификации на прокси-сервере. Начиная с первой схемы в списке, ActiveGate будет пытаться аутентифицироваться и в случае неудачи переходить к следующей схеме. Если это свойство не определено, ActiveGate попытается аутентифицироваться, используя все доступные схемы. Поддерживаемые значения: `NTLM`, `BASIC`. |

## Сценарии подключения через прокси

Ниже представлены возможные сценарии конфигурации прокси. Доступ к тестируемому ресурсу через прокси поддерживается только для браузерных мониторов и HTTP-мониторов.

### Подключение к Dynatrace Cluster

```
[http.client]



proxy-server=<proxy>



proxy-port=8080



proxy-user=username



proxy-password=password



[synthetic]



proxy-off=true
```

### Подключение к Dynatrace Cluster и тестируемому ресурсу

```
[http.client]



proxy-server=<proxy>



proxy-port=8080



proxy-user=username



proxy-password=password
```

### Подключение к Dynatrace Cluster и тестируемым ресурсам через разные прокси

* Подключение к Dynatrace Cluster

  ```
  [http.client]



  proxy-server=<proxy>



  proxy-port=8080



  proxy-user=username



  proxy-password=password
  ```
* Подключение к тестируемому ресурсу

  ```
  [synthetic]



  proxy-server=<proxy between AG and tested resource>



  proxy-port=9090



  proxy-user=username_two



  proxy-password=password_two
  ```

### Подключение к тестируемому ресурсу и/или Amazon S3

Synthetic-enabled ActiveGate требует доступ к сервису Amazon S3 для загрузки и доступа к скриншотам браузерных мониторов в частных расположениях.

```
[synthetic]



proxy-server=<proxy between AG and tested resource>



proxy-port=8080



proxy-user=username



proxy-password=password
```

Дополнительную информацию см. в разделе [Файлы Proxy Auto-Configuration (PAC)](#proxy-auto-configuration-pac-files).

### Настройка синтетического мониторинга с прямым подключением к другим ресурсам

```
[synthetic]



proxy-server=<proxy between AG and tested resource>



proxy-port=8080



proxy-user=username



proxy-password=password



proxy-non-proxy-hosts=my.corp.org|*.gdansk.dynatrace.com
```

## Файлы Proxy Auto-Configuration (PAC)

Вы можете использовать файлы Proxy Auto-Configuration (PAC) для управления сложной конфигурацией прокси в частных браузерных мониторах.

### Что такое PAC-файл?

Файл Proxy Auto-Configuration (PAC) — это функция JavaScript, которая определяет, поступают ли запросы веб-браузера (HTTP, HTTPS и FTP) напрямую к целевому адресу или перенаправляются на прокси-сервер (подробности см. в статье [Proxy Auto-Configuration (PAC) file](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_%28PAC%29_file) на [developer.mozilla.org](https://developer.mozilla.org/en-US/)).

### Как предоставить PAC-файл браузерным мониторам

PAC-файл можно предоставить вручную только в режиме скрипта в предыдущей версии Dynatrace.

Используйте [режим скрипта](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте или редактируйте браузерные мониторы в формате JSON.") для браузерных мониторов с одним URL и браузерных clickpath-ов.

* Для новых мониторов переключитесь из **Visual mode** в **Script mode**.
* Для существующих мониторов выберите **Edit** для открытия настроек и выберите **Recorded clickpath** для clickpath-ов. Затем переключитесь в режим **Script**.

  Для существующих браузерных мониторов с одним URL выберите **Monitor script**.

Вам потребуется добавить следующее в объект `configuration` JSON-файла:

```
"proxy": {



"pacUrl": "https://www.example.com/test.pac"



}
```

где `pacUrl` указывает на ваш размещённый PAC-файл.

![PAC file script definition](https://dt-cdn.net/images/pac-script-1122-2933677ee4.png)

Определение PAC-файла в скрипте

Дополнительную информацию о режиме скрипта см. в разделе [Script mode для настройки браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте или редактируйте браузерные мониторы в формате JSON.").

### Совместимость конфигурации PAC-файла

* Конфигурация PAC-файла применяется только к частным расположениям Synthetic, но не к публичным.
* Конфигурация PAC-файла применяется только к монитору, для которого она настроена: каждый отдельный монитор должен иметь PAC-файл, настроенный в своём скрипте; глобальной настройки для использования PAC-файла всеми мониторами нет.

* При задании PAC-файла прокси для скрипта одного синтетического монитора это применяется только к данному монитору.

* Если указан PAC-файл, он переопределяет настройки прокси, заданные на уровне ActiveGate для связи с тестируемым ресурсом. А именно, он переопределяет свойства в секции `[synthetic]`.
* PAC-файл должен обслуживаться по протоколу HTTP/S.

## Настройка прокси для режима FIPS

Если расположение Synthetic установлено в режиме FIPS, трафик браузерного монитора должен маршрутизироваться через локальный перехватывающий прокси, чтобы весь трафик, покидающий хост, шифровался с использованием сертифицированной по FIPS криптографической библиотеки:

![Proxy configuration for FIPS mode](https://cdn.bfldr.com/B686QPH3/as/3vgr8q644bgf8ns2gtz3x4/Set_up_a_proxy_-_For_FIPS_mode_-_Light_Mode?auto=webp&format=png&position=1)

Настройка прокси для режима FIPS

В этом примере используется прокси Squid, связанный с системной библиотекой OpenSSL, однако вы можете использовать другое программное обеспечение прокси при условии, что его криптографическая библиотека сертифицирована по FIPS.

1. Установите прокси на том же хосте, что и Synthetic engine:

   Red Hat

   Ubuntu Pro

   ```
   sudo dnf install squid
   ```

   ```
   sudo apt install squid-openssl
   ```
2. Предоставьте CA-сертификат для [повторной подписи](https://wiki.squid-cache.org/Features/DynamicSslCert) перехваченных запросов:

   Red Hat

   Ubuntu Pro

   ```
   sudo mkdir /etc/squid/ssl_cert



   sudo mv ~/prepared_ca_cert.pem /etc/squid/ssl_cert/squid.pem



   sudo chown --recursive squid:squid /etc/squid/ssl_cert



   sudo chmod 700 /etc/squid/ssl_cert



   sudo chmod 600 /etc/squid/ssl_cert/squid.pem
   ```

   ```
   sudo mkdir /etc/squid/ssl_cert



   sudo mv ~/prepared_ca_cert.pem /etc/squid/ssl_cert/squid.pem



   sudo chown --recursive proxy:proxy /etc/squid/ssl_cert



   sudo chmod 700 /etc/squid/ssl_cert



   sudo chmod 600 /etc/squid/ssl_cert/squid.pem
   ```

   Если SELinux включён, может потребоваться настройка меток файлов. Подробности см. в документации Red Hat для [Red Hat Enterprise Linux 8](https://dt-url.net/wx039i1) или [Red Hat Enterprise Linux 9](https://dt-url.net/b62392n).

3. Создайте временный кеш сертификатов:

   Red Hat

   Ubuntu Pro

   ```
   sudo /usr/lib64/squid/security_file_certgen -c -s /var/spool/squid/ssl_db -M 4MB



   sudo chown --recursive squid:squid /var/spool/squid/ssl_db
   ```

   ```
   sudo /usr/lib/squid/security_file_certgen -c -s /var/spool/squid/ssl_db -M 4MB



   sudo chown --recursive proxy:proxy /var/spool/squid/ssl_db
   ```
4. Настройте прокси для выполнения [перехвата SSL](https://wiki.squid-cache.org/Features/SslPeekAndSplice) (по умолчанию `/etc/squid/squid.conf`):

   ```
   acl SSL_ports port 443



   acl Safe_ports port 80 443 1025-65535



   acl CONNECT method CONNECT



   http_access deny !Safe_ports



   http_access deny CONNECT !SSL_ports



   http_access allow localhost



   http_access deny all



   http_port 3128 ssl-bump generate-host-certificates=on dynamic_cert_mem_cache_size=4MB cert=/etc/squid/ssl_cert/squid.pem



   acl step1 at_step SslBump1



   ssl_bump peek step1



   ssl_bump bump all



   cache deny all
   ```
5. Перезапустите прокси для применения конфигурации:

   ```
   sudo systemctl enable squid



   sudo systemctl restart squid
   ```
6. Проверьте корректность работы прокси:

   ```
   curl --proxy localhost:3128 https://example.com
   ```
7. Опционально. Если вы выбрали другой порт прокси, необходимо скорректировать конфигурацию Synthetic (по умолчанию `/var/lib/dynatrace/synthetic/config/user.properties`):

   ```
   com.vuc.fips.proxy.port=3128
   ```

### Настройка прокси для режима FIPS с корпоративным прокси

Если ваша организация требует использования корпоративного прокси, необходимо настроить второй локальный экземпляр Squid из-за ограничений Squid:

![Proxy configuration for FIPS mode with corporate proxy](https://cdn.bfldr.com/B686QPH3/as/jkkncgwjs9q8nbtwkck9p38p/For_FIPS_mode_with_corporate_proxy_-_Light_Mode?auto=webp&format=png&position=1)

Настройка прокси для режима FIPS с корпоративным прокси

Если вы используете другое программное обеспечение прокси, это может не применяться к вам.

1. Настройте прокси для FIPS, как описано в предыдущем разделе.

   Требуется Squid версии `5+`, поэтому Red Hat версии `8` и Ubuntu версии `20` не поддерживаются.
2. На том же хосте создайте второй service definition для squid:

   Red Hat

   Ubuntu Pro

   `/usr/lib/systemd/system/squid2.service`

   ```
   [Unit]



   Description=Squid with upstream proxy



   After=network.target network-online.target nss-lookup.target



   [Service]



   Type=notify



   LimitNOFILE=16384



   PIDFile=/run/squid2.pid



   ExecStart=/usr/sbin/squid --foreground -n squid2 -f "/etc/squid/squid2.conf"



   ExecReload=/usr/bin/kill -HUP $MAINPID



   KillMode=mixed



   NotifyAccess=all



   [Install]



   WantedBy=multi-user.target
   ```

   `/lib/systemd/system/squid2.service`

   ```
   [Unit]



   Description=Squid with upstream proxy



   After=network.target network-online.target nss-lookup.target



   [Service]



   Type=notify



   PIDFile=/run/squid2.pid



   Group=proxy



   RuntimeDirectory=squid2



   RuntimeDirectoryMode=0775



   ExecStart=/usr/sbin/squid --foreground -sYC -n squid2 -f "/etc/squid/squid2.conf"



   ExecReload=/bin/kill -HUP $MAINPID



   KillMode=mixed



   NotifyAccess=all



   [Install]



   WantedBy=multi-user.target
   ```
3. Создайте второй конфигурационный файл прокси (`/etc/squid/squid2.conf`) и укажите хост, порт и [аутентификацию](https://www.squid-cache.org/Doc/config/cache_peer) вашего корпоративного прокси:

   ```
   acl SSL_ports port 443



   acl Safe_ports port 80 443 1025-65535



   acl CONNECT method CONNECT



   http_access deny !Safe_ports



   http_access deny CONNECT !SSL_ports



   http_access allow localhost



   http_access deny all



   http_port 3129



   access_log daemon:/var/log/squid/access2.log squid



   cache_log /var/log/squid/cache2.log



   pid_filename /run/squid2.pid



   cache_peer upstream-proxy.example.com parent 443 0 default no-digest proxy-only login=proxyuser:proxypass tls tls-min-version=1.2 tls-options=NO_SSLv3



   never_direct allow all



   visible_hostname squid2



   cache deny all
   ```
4. Обновите конфигурацию первого прокси (`/etc/squid/squid.conf`), чтобы использовать второй прокси в качестве [родительского](https://wiki.squid-cache.org/Features/CacheHierarchy), добавив следующие строки:

   ```
   cache_peer localhost parent 3129 0 default no-digest proxy-only



   never_direct allow all



   visible_hostname squid1
   ```
5. Перезапустите оба сервиса squid:

   ```
   sudo systemctl daemon-reload



   sudo systemctl enable squid2



   sudo systemctl start squid2



   sudo systemctl restart squid
   ```
6. Проверьте корректность работы цепочки прокси:

   ```
   curl --proxy localhost:3128 https://example.com
   ```

### Соображения по ресурсам

* Каждый сервис Squid требует дополнительно 500 МиБ оперативной памяти, что необходимо учитывать при выборе размера экземпляра для конкретной нагрузки.
* Запросы, проходящие через несколько прокси, будут занимать больше времени, поэтому показатели производительности будут хуже, чем у экземпляра без FIPS.