---
title: Устранение неполадок при установке OneAgent на Solaris
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris
scraped: 2026-05-12T11:09:50.774322
---

# Устранение неполадок при установке OneAgent на Solaris

# Устранение неполадок при установке OneAgent на Solaris

* Чтение: 3 мин
* Опубликовано 19 сентября 2018 г.

Узнайте, как решать проблемы, связанные с установкой OneAgent на Solaris.

SSL handshake failed

При загрузке может возникнуть следующая ошибка:

```
Releasing 0x0000000239ae1890 (new refcount 1).



Initiating SSL handshake.



SSL handshake failed.



Closed fd 5



Unable to establish SSL connection.
```

Это может быть вызвано выбором неправильного протокола SSL или TLS при рукопожатии. Поскольку разные операционные системы ведут себя по-разному (как на стороне сервера, так и на стороне клиента), при определённых условиях некоторые протоколы необходимо указывать вручную.

В данном конкретном случае, чтобы выбрать правильный протокол, необходимо указать `--secure-protocol=tlsv1_2` как дополнительный параметр команды `wget`. Команда должна выглядеть следующим образом:

```
wget --secure-protocol=tlsv1_2



-O Dynatrace-OneAgent-Solaris-xxx-1.xxx.xxx.zip



"https://xxx/xxx/api/v1/deployment/installer/agent/solaris/paas/latest?Api-Token=xxx&arch=x86"
```

Это также можно задать постоянно, создав файл `~/.wgetrc` со следующим содержимым:

`secureprotocol = tlsv1_2`

Could not find required opcodes in caller trying to resolve main

При запуске Java-приложения может появиться следующее сообщение об ошибке:

```
severe  [hooking   ] Could not find required opcodes in caller trying to resolve main
```

Это происходит, если вы используете один из унифицированных скриптов мониторинга `dynatrace-agentXX.sh`, но при этом OneAgent дополнительно указан в `JAVA_OPTS`.

* Убедитесь, что `dynatrace-java-env.sh` нигде не вызывается в вашей оболочке, когда вы используете скрипт `dynatrace-agentXX.sh`.
  `dynatrace-java-env.sh` устарел и должен использоваться только как запасной вариант.
* Проверьте наличие и удалите следующий параметр из командной строки Java или скриптов запуска (конкретный каталог может отличаться):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

После этого сообщение об ошибке должно исчезнуть.

LD\_PRELOAD\_64: parameter not set

Подобная ошибка может возникнуть при использовании `dynatrace-agentXX.sh` в скрипте оболочки.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LD_PRELOAD_64: parameter not set
```

Это происходит, если используется `set -u`, чтобы трактовать незаданные переменные и параметры как ошибки. `dynatrace-agentXX.sh` экспортирует переменные, которые, хотя их ещё может не быть в вашем скрипте, тем не менее необходимы и критически важны для корректной работы. Чтобы обойти это, вызовите `set +u` перед `dynatrace-agentXX.sh` в вашем скрипте.

```
# avoid error



set +u



DT_HOME=/opt/dynatrace/oneagent



export DT_HOME



. $DT_HOME/dynatrace-agent64.sh
```

ld.so.1: sudo: warning: /opt/dynatrace/oneagent/agent/lib/liboneagentproc.so: open failed: illegal insecure pathname

Подобная ошибка может возникнуть, когда вы задаёте `LD_PRELOAD` в вашей среде выполнения и вызываете sudo или su. Это происходит потому, что OneAgent не установлен в защищённый каталог `ld_preload`. Это сообщение об ошибке не имеет негативных последствий, и его можно игнорировать. Чтобы избежать этого, не задавайте `LD_PRELOAD` в контексте выполнения, где вы хотите использовать sudo.

См. [Подробнее по этой теме](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)

Почему OneAgent не начинает мониторить процесс Apache после перезапуска?

После установки OneAgent ваш веб-сервер Apache необходимо *полностью* перезапустить, чтобы включить мониторинг. Чтобы сделать это правильно, важно понимать разницу между «частичным» и «полным» перезапусками. При частичном перезапуске главный процесс Apache повторно считывает свои конфигурационные файлы, повторно открывает свои лог-файлы, а затем перезапускает свои рабочие процессы. Однако OneAgent требует полного перезапуска веб-сервера Apache, при котором все рабочие процессы и, что особенно важно, главный процесс Apache полностью завершают работу, а затем перезапускаются.

Подробнее о различных типах доступных перезапусков см. в [Остановка и перезапуск Apache HTTP Server](https://httpd.apache.org/docs/2.4/stopping.html).

## Как выполнить полный перезапуск

Возможно, вы привыкли перезапускать Apache с помощью команды `apachectl restart`. Однако эта команда приводит только к частичному перезапуску Apache.

Чтобы выполнить полный перезапуск Apache и включить глубокий мониторинг с помощью Dynatrace OneAgent, необходимо сначала выполнить полное завершение работы с помощью команды `apachectl stop`. Только после этого шага можно перезапустить сервер с помощью `apachectl start` .

В системах Ubuntu можно использовать `service apache2 restart`. Однако учтите, что какие бы команды вы ни использовали, вам, скорее всего, потребуются права суперпользователя (sudo).

Я использую административный сервер WebLogic для перезапуска управляемых узлов на Solaris. Не удаётся задать переменные окружения.

Если у вас возникают трудности с заданием переменных окружения

1. Завершите работу управляемых узлов и Node Manager (убедитесь, что ни один процесс не выполняется под функциональным ID).
2. Создайте резервную копию скрипта `$Domain_home/startNodeManagerMx.sh`.
3. Измените скрипт `startNodeManagerMx.sh`, добавив приведённые ниже строки.  
   (После запуска `commEnv.sh` обратитесь к скрипту в `/apps/wldomains/wls-aabb-1a` на `aaaabbb01a`).

   ```
   DT_HOME="/opt/dynatrace/oneagent"



   export DT_HOME



   source "$DT_HOME/dynatrace-env.sh"



   LD_PRELOAD="$DT_HOME/agent/lib/liboneagentproc.so"



   export LD_PRELOAD
   ```
4. Запустите новый сеанс.
5. Запустите Node Manager.
6. Получите PID, пока Node Manager работает.

   Используйте командную строку `$ pargs -e pid |grep LD`, чтобы проверить, присутствует ли окружение.

   Пример:

   ```
   aabb@aaaabbb01a:/apps/wldomains/wls-aabb-1a$pargs -e 26531 |grep LD



   envp[27]: envp[28]: LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
   ```
7. Запустите управляемые узлы из консоли.
8. Проверьте каталог логов, чтобы убедиться, что генерируется новый лог:

   ```
   ls -ltr /opt/dynatrace/oneagent/log/java
   ```

Подробнее о настройке мониторинга Oracle WebLogic см. в [Настройка Oracle WebLogic через скрипт запуска](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris#weblogic "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC).")