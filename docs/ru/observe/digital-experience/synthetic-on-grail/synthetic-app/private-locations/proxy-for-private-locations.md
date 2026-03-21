---
title: Прокси для частных локаций
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/proxy-for-private-locations
scraped: 2026-03-02T21:20:36.386068
---

# Прокси для приватных локаций


* Latest Dynatrace

Вы можете использовать [прокси, балансировщики нагрузки и обратные прокси в вашем развёртывании Dynatrace](../../../../../ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates.md#proxies "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent."). В частности, конфигурация ActiveGate позволяет определить один или несколько прокси для исходящих соединений.

* Для настройки прокси для связи с тестируемым ресурсом отредактируйте файл [`custom.properties`](../../../../../ingest-from/dynatrace-activegate/configuration/configure-activegate.md "Узнайте, какие свойства ActiveGate вы можете настроить в соответствии с вашими потребностями и требованиями.") и задайте свойства в разделе `[synthetic]`.
* Для настройки прокси только для внутренней связи с кластером Dynatrace см. [настройки только для связи с кластером Dynatrace](../../../../../ingest-from/dynatrace-activegate/configuration/set-up-proxy-authentication-for-activegate.md#internal "Узнайте, как настроить свойства ActiveGate для настройки прокси.").
* Для настройки одного прокси как для тестируемого ресурса, так и для кластера Dynatrace задайте свойства в разделе `[http.client]`.

## Свойства конфигурации прокси

Вы можете использовать следующие свойства при настройке прокси для вашего ActiveGate с поддержкой Synthetic:

## Сценарии подключения через прокси

Далее описаны возможные сценарии конфигурации прокси. Доступ к тестируемому ресурсу через прокси поддерживается только для браузерных мониторов и HTTP-мониторов.

### Подключение к кластеру Dynatrace

```
[http.client]


proxy-server=<proxy>


proxy-port=8080


proxy-user=username


proxy-password=password


[synthetic]


proxy-off=true
```

### Подключение к кластеру Dynatrace и тестируемому ресурсу

```
[http.client]


proxy-server=<proxy>


proxy-port=8080


proxy-user=username


proxy-password=password
```

### Подключение к кластеру Dynatrace и тестируемым ресурсам через разные прокси

* Подключение к кластеру Dynatrace

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

ActiveGate с поддержкой Synthetic нуждается в доступе к сервису Amazon S3 для загрузки и доступа к снимкам экрана для браузерных мониторов на приватных локациях.

```
[synthetic]


proxy-server=<proxy between AG and tested resource>


proxy-port=8080


proxy-user=username


proxy-password=password
```

Дополнительную информацию см. в разделе [Файлы автоматической настройки прокси (PAC)](#proxy-auto-configuration-pac-files).

### Настройка синтетического мониторинга с прямым подключением к другим ресурсам

```
[synthetic]


proxy-server=<proxy between AG and tested resource>


proxy-port=8080


proxy-user=username


proxy-password=password


proxy-non-proxy-hosts=my.corp.org|*.gdansk.dynatrace.com
```

## Файлы автоматической настройки прокси (PAC)

Вы можете использовать файлы автоматической настройки прокси (PAC) для управления сложной конфигурацией прокси для приватных браузерных мониторов.

### Что такое PAC-файл?

Файл автоматической настройки прокси (PAC) — это JavaScript-функция, которая определяет, направляются ли запросы веб-браузера (HTTP, HTTPS и FTP) непосредственно к месту назначения или перенаправляются на прокси-сервер (подробности см. в разделе [Proxy Auto-Configuration (PAC) file](https://developer.mozilla.org/en-US/docs/Web/HTTP/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_%28PAC%29_file) на [developer.mozilla.org](https://developer.mozilla.org/en-US/)).

### Предоставление PAC-файла для браузерных мониторов

1. Перейдите в ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.
2. (Необязательно) Для фильтрации таблицы по браузерным мониторам выберите **Browser** в разделе **Filter options** слева.
3. В списке браузерных мониторов выберите монитор, для которого вы хотите предоставить PAC-файл. Справа появится панель предварительного просмотра.
4. Нажмите **Edit** в правом верхнем углу панели предварительного просмотра.

   С этого момента вы будете перенаправлены в предыдущую версию Dynatrace, где можете указать URL PAC-файла.
5. Переключитесь в [режим скрипта](../../../synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration.md "Создание или редактирование браузерных мониторов в формате JSON.").

   * Для сценария clickpath выберите **Recorded clickpath** > **Script**.
   * Для монитора с одним URL выберите **Monitor script**.
6. Добавьте следующее в объект `configuration` JSON-файла:

   ```
   "proxy": {


   "pacUrl": "https://www.example.com/test.pac"


   }
   ```

   `pacUrl` указывает на ваш размещённый PAC-файл.

   ![Добавление PAC-файла к браузерному монитору.](https://dt-cdn.net/images/screenshot-2025-09-18-145741-826-11ee737f0f.png)

   Дополнительную информацию о режиме скрипта см. в разделе [Режим скрипта для настройки браузерного монитора](../../../synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration.md "Создание или редактирование браузерных мониторов в формате JSON.").

### Совместимость конфигурации PAC-файлов

* Конфигурация PAC-файлов применяется только к приватным локациям Synthetic, а не к публичным.
* Конфигурация PAC-файлов применяется только к настроенному монитору — для каждого отдельного монитора PAC-файл должен быть настроен в его скрипте; глобальной настройки для использования PAC-файла всеми мониторами не существует.

* Когда вы задаёте прокси через PAC-файл для одного скрипта синтетического монитора, это применяется только к этому монитору.

* Если указан PAC-файл, он переопределяет настройки прокси, заданные на уровне ActiveGate для связи с тестируемым ресурсом. В частности, он переопределяет свойства в разделе `[synthetic]`.
* PAC-файл должен быть доступен по HTTP/S.

## Конфигурация прокси для режима FIPS

Когда локация Synthetic установлена в режиме FIPS, трафик браузерного монитора должен маршрутизироваться через локальный перехватывающий прокси, чтобы весь трафик, покидающий хост, шифровался с помощью криптографической библиотеки, сертифицированной по FIPS:

![FIPS прокси](https://dt-cdn.net/images/syn-proxy-for-fips-811-26fb991173.png)

В этом примере настройки мы используем прокси Squid, связанный с системной библиотекой OpenSSL, но вы можете использовать другое прокси-ПО, если его криптографическая библиотека сертифицирована по FIPS.

1. Установите прокси на том же хосте, что и движок Synthetic:

   Red Hat

   Ubuntu Pro

   ```
   sudo dnf install squid
   ```

   ```
   sudo apt install squid-openssl
   ```
2. Предоставьте сертификат ЦС для [переподписания](https://wiki.squid-cache.org/Features/DynamicSslCert) перехваченных запросов:

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

   Если SELinux включён, может потребоваться настройка [меток файлов](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/sect-security-enhanced_linux-working_with_selinux-selinux_contexts_labeling_files) для предотвращения ошибок доступа.
3. Создайте временный кэш сертификатов:

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
4. Настройте прокси для выполнения [SSL-перехвата](https://wiki.squid-cache.org/Features/SslPeekAndSplice) (по умолчанию `/etc/squid/squid.conf`):

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
6. Убедитесь, что прокси работает корректно:

   ```
   curl --proxy localhost:3128 https://example.com
   ```
7. (Необязательно) Если вы выбрали другой порт прокси, вам нужно изменить конфигурацию Synthetic (по умолчанию `/var/lib/dynatrace/synthetic/config/user.properties`):

   ```
   com.vuc.fips.proxy.port=3128
   ```

### Конфигурация прокси для режима FIPS с корпоративным прокси

Если ваша организация требует использования корпоративного прокси, необходимо настроить второй локальный экземпляр Squid из-за ограничений Squid:

![Цепочка FIPS-прокси](https://dt-cdn.net/images/syn-proxy-for-fips-upstream-1141-ebd20f3425.png)

Если вы используете другое прокси-ПО, это может быть неприменимо к вам.

1. Настройте прокси для FIPS, как описано в предыдущем разделе.

   Требуется Squid версии `5+`, поэтому Red Hat версии `8` и Ubuntu версии `20` не поддерживаются.
2. На том же хосте создайте второе определение сервиса squid:

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
3. Создайте вторую конфигурацию прокси (`/etc/squid/squid2.conf`) и укажите хост, порт и [аутентификацию](https://www.squid-cache.org/Doc/config/cache_peer) вашего корпоративного прокси:

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
4. Обновите первую конфигурацию прокси (`/etc/squid/squid.conf`), чтобы использовать второй прокси как [родительский прокси](https://wiki.squid-cache.org/Features/CacheHierarchy), добавив следующие строки:

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
6. Убедитесь, что цепочка прокси работает корректно:

   ```
   curl --proxy localhost:3128 https://example.com
   ```

### Требования к ресурсам

* Каждый сервис Squid требует дополнительно 500 МиБ оперативной памяти, что необходимо учитывать при выборе размера экземпляра для конкретной нагрузки.
* Запросы, проходящие через несколько прокси, будут выполняться дольше, поэтому показатели производительности будут хуже, чем у экземпляра без FIPS.
