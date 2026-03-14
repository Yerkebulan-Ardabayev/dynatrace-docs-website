---
title: Устранение неполадок при установке OneAgent на Solaris
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris
scraped: 2026-03-06T21:20:18.314953
---

# Устранение неполадок при установке OneAgent на Solaris

# Устранение неполадок при установке OneAgent на Solaris

* Latest Dynatrace
* 3-min read
* Published Sep 19, 2018

Узнайте, как решить проблемы, связанные с установкой OneAgent на Solaris.

Ошибка SSL handshake

При загрузке вы можете столкнуться со следующей ошибкой:

```
Releasing 0x0000000239ae1890 (new refcount 1).



Initiating SSL handshake.



SSL handshake failed.



Closed fd 5



Unable to establish SSL connection.
```

Это может быть вызвано выбором неправильного протокола SSL или TLS при рукопожатии. Поскольку разные операционные системы ведут себя по-разному (как на стороне сервера, так и на стороне клиента), в определённых условиях необходимо указывать некоторые протоколы вручную.

В данном конкретном случае для выбора правильного протокола необходимо указать `--secure-protocol=tlsv1_2` в качестве дополнительного параметра команды `wget`. Команда должна выглядеть следующим образом:

```
wget --secure-protocol=tlsv1_2



-O Dynatrace-OneAgent-Solaris-xxx-1.xxx.xxx.zip



"https://xxx/xxx/api/v1/deployment/installer/agent/solaris/paas/latest?Api-Token=xxx&arch=x86"
```

Это также можно установить на постоянной основе, создав файл `~/.wgetrc` со следующим содержимым:

`secureprotocol = tlsv1_2`

Не удалось найти требуемые опкоды в вызывающем коде при попытке разрешить main

Вы можете столкнуться со следующим сообщением об ошибке при запуске Java-приложения:

```
severe  [hooking   ] Could not find required opcodes in caller trying to resolve main
```

Это происходит, если вы используете один из унифицированных скриптов мониторинга `dynatrace-agentXX.sh`, но дополнительно имеете ссылку на OneAgent в `JAVA_OPTS`.

* Убедитесь, что `dynatrace-java-env.sh` не вызывается нигде в вашей оболочке, когда вы используете скрипт `dynatrace-agentXX.sh`.
  `dynatrace-java-env.sh` является устаревшим и должен использоваться только в качестве запасного варианта.
* Проверьте и удалите следующий параметр из командной строки Java или скриптов запуска (конкретная директория может отличаться):

  `-agentpath:/opt/dynatrace/oneagent/agent/lib64/liboneagentloader.so`

После этого сообщение об ошибке должно исчезнуть.

LD\_PRELOAD\_64: параметр не установлен

Вы можете столкнуться с подобной ошибкой при использовании `dynatrace-agentXX.sh` в shell-скрипте.

```
Info: using DT_HOME: /opt/dynatrace/oneagent



.profile[33] LD_PRELOAD_64: parameter not set
```

Это происходит, если вы используете `set -u` для обработки неустановленных переменных и параметров как ошибок. `dynatrace-agentXX.sh` экспортирует переменные, которые, хотя ещё могут не существовать в вашем скрипте, тем не менее необходимы для корректной работы. Чтобы это исправить, вызовите `set +u` перед `dynatrace-agentXX.sh` в вашем скрипте.

```
# avoid error



set +u



DT_HOME=/opt/dynatrace/oneagent



export DT_HOME



. $DT_HOME/dynatrace-agent64.sh
```

ld.so.1: sudo: warning: /opt/dynatrace/oneagent/agent/lib/liboneagentproc.so: open failed: illegal insecure pathname

Вы можете столкнуться с подобной ошибкой, когда устанавливаете `LD_PRELOAD` в вашем окружении выполнения и вызываете sudo или su. Это происходит потому, что OneAgent не установлен в безопасной директории `ld_preload`. Это сообщение об ошибке не имеет негативного влияния и может быть проигнорировано. Чтобы избежать этого, убедитесь, что вы не устанавливаете `LD_PRELOAD` в контексте выполнения, где хотите использовать sudo.

См. [Подробнее об этой теме](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)

Почему OneAgent не начинает мониторинг процесса Apache после перезапуска?

После установки OneAgent ваш веб-сервер Apache должен быть *полностью* перезапущен для включения мониторинга. Чтобы сделать это правильно, важно понимать разницу между «частичным» и «полным» перезапуском. В случае частичного перезапуска главный процесс Apache перечитывает свои конфигурационные файлы, повторно открывает файлы журналов и затем перезапускает рабочие процессы. Однако OneAgent требует полного перезапуска веб-сервера Apache, при котором все рабочие процессы и, что наиболее важно, главный процесс Apache полностью останавливаются и затем перезапускаются.

См. [Остановка и перезапуск Apache HTTP Server](https://httpd.apache.org/docs/2.4/stopping.html) для получения дополнительной информации о различных типах доступных перезапусков.

## Как выполнить полный перезапуск

Возможно, вы привыкли перезапускать Apache с помощью команды `apachectl restart`. Однако эта команда приводит лишь к частичному перезапуску Apache.

Чтобы выполнить полный перезапуск Apache и включить глубокий мониторинг с помощью Dynatrace OneAgent, необходимо сначала выполнить полную остановку с помощью команды `apachectl stop`. Только после этого шага можно перезапустить сервер с помощью `apachectl start`.

На системах Ubuntu допустимо использовать `service apache2 restart`. Обратите внимание, что какие бы команды вы ни использовали, вам, вероятно, потребуются права суперпользователя (sudo).

Я использую административный сервер WebLogic для перезапуска управляемых узлов на Solaris. Я не могу установить переменные окружения.

Если у вас возникли проблемы с установкой переменных окружения:

1. Остановите управляемые узлы и Node Manager (убедитесь, что ни один процесс не запущен под функциональным ID).
2. Сделайте резервную копию скрипта `$Domain_home/startNodeManagerMx.sh`.
3. Измените скрипт `startNodeManagerMx.sh`, добавив следующие строки.
   (После выполнения `commEnv.sh`, обратитесь к скрипту в `/apps/wldomains/wls-aabb-1a` на `aaaabbb01a`).

   ```
   DT_HOME="/opt/dynatrace/oneagent"



   export DT_HOME



   source "$DT_HOME/dynatrace-env.sh"



   LD_PRELOAD="$DT_HOME/agent/lib/liboneagentproc.so"



   export LD_PRELOAD
   ```
4. Начните новый сеанс.
5. Запустите Node Manager.
6. Получите PID, пока Node Manager работает.

   Используйте команду `$ pargs -e pid |grep LD`, чтобы проверить наличие переменных окружения.

   Пример:

   ```
   aabb@aaaabbb01a:/apps/wldomains/wls-aabb-1a$pargs -e 26531 |grep LD



   envp[27]: envp[28]: LD_PRELOAD=/opt/dynatrace/oneagent/agent/lib/liboneagentproc.so
   ```
7. Запустите управляемые узлы из консоли.
8. Проверьте директорию логов, чтобы убедиться, что новый лог был создан:

   ```
   ls -ltr /opt/dynatrace/oneagent/log/java
   ```

Для получения дополнительной информации о настройке мониторинга Oracle WebLogic см. [Настройка Oracle WebLogic через скрипт запуска](install-oneagent-on-solaris.md#weblogic "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC).")
