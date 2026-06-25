#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build RU translations for OneAgent Solaris troubleshoot + install via exact EN-line match.

WARNING: one-shot generation tool. The .md files received +19 post-build critical-review
edits (calque «вы можете»→«можно», term «мониторируемые», env consistency). Re-running this
WILL revert those. Treat the .md files in docs/managed-ru/.../solaris/ as source of truth.


Lines not present in the pairs are copied verbatim from EN (covers code blocks, fences,
blank lines, and deliberately-kept-EN literal error strings). Guarantees line-parity and
byte-identical code blocks. Output: LF, no BOM, no trailing newline (matches OneAgent family canon)."""

from pathlib import Path
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(
    "docs/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris"
)
RU_BASE = Path(
    "docs/managed-ru/ingest-from/dynatrace-oneagent/installation-and-operation/solaris"
)

# ---- troubleshoot pairs (literal error/log accordion titles intentionally kept EN) ----
T_PAIRS = [
    (
        "title: Troubleshooting OneAgent installation on Solaris",
        "title: Устранение неполадок при установке OneAgent на Solaris",
    ),
    (
        "# Troubleshooting OneAgent installation on Solaris",
        "# Устранение неполадок при установке OneAgent на Solaris",
    ),
    ("* 3-min read", "* Чтение: 3 мин"),
    ("* Published Sep 19, 2018", "* Опубликовано 19 сентября 2018 г."),
    (
        "Find out how to solve problems related to installing OneAgent on Solaris.",
        "Узнайте, как решать проблемы, связанные с установкой OneAgent на Solaris.",
    ),
    (
        "While downloading, you may encounter the following error:",
        "При загрузке вы можете столкнуться со следующей ошибкой:",
    ),
    (
        "This can be caused by selecting the wrong SSL or TLS protocol on handshake. As different operating systems act differently (both server and client side), you must specify some protocols manually under certain conditions.",
        "Это может быть вызвано выбором неправильного протокола SSL или TLS при рукопожатии. Поскольку разные операционные системы ведут себя по-разному (как на стороне сервера, так и на стороне клиента), при определённых условиях некоторые протоколы необходимо указывать вручную.",
    ),
    (
        "For this specific case, to select the correct protocol, you must specify `--secure-protocol=tlsv1_2` as an additional parameter of the `wget` command. The command should appear as follows:",
        "В данном конкретном случае, чтобы выбрать правильный протокол, необходимо указать `--secure-protocol=tlsv1_2` как дополнительный параметр команды `wget`. Команда должна выглядеть следующим образом:",
    ),
    (
        "It can also be set permanently by creating the file `~/.wgetrc` with the following content:",
        "Это также можно задать постоянно, создав файл `~/.wgetrc` со следующим содержимым:",
    ),
    (
        "You may encounter the following error message when you start your Java application:",
        "Вы можете столкнуться со следующим сообщением об ошибке при запуске вашего Java-приложения:",
    ),
    (
        "This happens if you use one of the unified monitoring scripts `dynatrace-agentXX.sh` but additionally have OneAgent referenced in `JAVA_OPTS`.",
        "Это происходит, если вы используете один из унифицированных скриптов мониторинга `dynatrace-agentXX.sh`, но при этом OneAgent дополнительно указан в `JAVA_OPTS`.",
    ),
    (
        "* Ensure that `dynatrace-java-env.sh` isn't called anywhere in your shell when you use the `dynatrace-agentXX.sh` script.",
        "* Убедитесь, что `dynatrace-java-env.sh` нигде не вызывается в вашей оболочке, когда вы используете скрипт `dynatrace-agentXX.sh`.",
    ),
    (
        "  `dynatrace-java-env.sh` is deprecated and should only be used as a fallback.",
        "  `dynatrace-java-env.sh` устарел и должен использоваться только как запасной вариант.",
    ),
    (
        "* Check for and remove the following parameter from your Java command line or startup scripts (specific directory may vary):",
        "* Проверьте наличие и удалите следующий параметр из командной строки Java или скриптов запуска (конкретный каталог может отличаться):",
    ),
    (
        "Following this, the error message should go away.",
        "После этого сообщение об ошибке должно исчезнуть.",
    ),
    (
        "You may encounter an error like this when you use `dynatrace-agentXX.sh` in a shell script.",
        "Вы можете столкнуться с подобной ошибкой при использовании `dynatrace-agentXX.sh` в скрипте оболочки.",
    ),
    (
        "This happens if use `set -u` to treat unset variables and parameters as errors. `dynatrace-agentXX.sh` does export variables which, though they may not yet exist in your script, are nevertheless needed and key to proper function. To overcome this, call `set +u` ahead of `dynatrace-agentXX.sh` in your script.",
        "Это происходит, если используется `set -u`, чтобы трактовать незаданные переменные и параметры как ошибки. `dynatrace-agentXX.sh` экспортирует переменные, которые, хотя их ещё может не быть в вашем скрипте, тем не менее необходимы и критически важны для корректной работы. Чтобы обойти это, вызовите `set +u` перед `dynatrace-agentXX.sh` в вашем скрипте.",
    ),
    (
        "You may encounter an error like this when you set `LD_PRELOAD` in your execution environment and call sudo or su. This happens because OneAgent isn't installed in the secure `ld_preload` directory. This error message has no negative impact and can be ignored. To avoid this, ensure that you don't set `LD_PRELOAD` in an execution context where you want to use sudo.",
        "Вы можете столкнуться с подобной ошибкой, когда задаёте `LD_PRELOAD` в вашей среде выполнения и вызываете sudo или su. Это происходит потому, что OneAgent не установлен в защищённый каталог `ld_preload`. Это сообщение об ошибке не имеет негативных последствий, и его можно игнорировать. Чтобы избежать этого, не задавайте `LD_PRELOAD` в контексте выполнения, где вы хотите использовать sudo.",
    ),
    (
        "See [Further detail on this topicï»¿](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)",
        "См. [Подробнее по этой темеï»¿](https://docs.oracle.com/cd/E19253-01/816-5165/ld.so.1-1/index.html#Security)",
    ),
    (
        "Why doesn't OneAgent start to monitor Apache process after restart?",
        "Почему OneAgent не начинает мониторить процесс Apache после перезапуска?",
    ),
    (
        'Following installation of OneAgent, your Apache web server must be *completely* restarted to enable monitoring. To do this correctly, it\'s important to understand the difference between "partial" and "complete" restarts. In the case of partial restarts, the main Apache process re-reads its configuration files, re-opens its log files, and then restarts its worker processes. OneAgent however, requires a complete Apache web server restart in which all workers andâmost importantlyâthe main Apache process are shut down entirely and then restarted.',
        "После установки OneAgent ваш веб-сервер Apache необходимо *полностью* перезапустить, чтобы включить мониторинг. Чтобы сделать это правильно, важно понимать разницу между «частичным» и «полным» перезапусками. При частичном перезапуске главный процесс Apache повторно считывает свои конфигурационные файлы, повторно открывает свои лог-файлы, а затем перезапускает свои рабочие процессы. Однако OneAgent требует полного перезапуска веб-сервера Apache, при котором все рабочие процессы и, что особенно важно, главный процесс Apache полностью завершают работу, а затем перезапускаются.",
    ),
    (
        "See [Stopping and Restarting Apache HTTP Serverï»¿](https://httpd.apache.org/docs/2.4/stopping.html) for more information on the different types of available restarts.",
        "Подробнее о различных типах доступных перезапусков см. в [Остановка и перезапуск Apache HTTP Serverï»¿](https://httpd.apache.org/docs/2.4/stopping.html).",
    ),
    ("## How to perform a complete restart", "## Как выполнить полный перезапуск"),
    (
        "You may be accustomed to restarting Apache by issuing an `apachectl restart` command. However, this command only results in a partial Apache restart.",
        "Возможно, вы привыкли перезапускать Apache с помощью команды `apachectl restart`. Однако эта команда приводит только к частичному перезапуску Apache.",
    ),
    (
        "To execute a complete Apache restart and enable deep monitoring with Dynatrace OneAgent, you need to first invoke a complete shutdown using the `apachectl stop` command. Only following this step can you restart the server using `apachectl start` .",
        "Чтобы выполнить полный перезапуск Apache и включить глубокий мониторинг с помощью Dynatrace OneAgent, необходимо сначала выполнить полное завершение работы с помощью команды `apachectl stop`. Только после этого шага можно перезапустить сервер с помощью `apachectl start` .",
    ),
    (
        "It's fine to use `service apache2 restart` on Ubuntu systems. Note however that whatever commands you use, you'll likely need superuser rights (sudo).",
        "В системах Ubuntu можно использовать `service apache2 restart`. Однако учтите, что какие бы команды вы ни использовали, вам, скорее всего, потребуются права суперпользователя (sudo).",
    ),
    (
        "I use WebLogic admin server to restart the managed nodes on Solaris. I can't set environment variables.",
        "Я использую административный сервер WebLogic для перезапуска управляемых узлов на Solaris. Не удаётся задать переменные окружения.",
    ),
    (
        "If you have trouble setting the environment variables",
        "Если у вас возникают трудности с заданием переменных окружения",
    ),
    (
        "1. Shut down the managed nodes and Node Manager (make sure no process is running under the functional ID).",
        "1. Завершите работу управляемых узлов и Node Manager (убедитесь, что ни один процесс не выполняется под функциональным ID).",
    ),
    (
        "2. Back up the `$Domain_home/startNodeManagerMx.sh` script.",
        "2. Создайте резервную копию скрипта `$Domain_home/startNodeManagerMx.sh`.",
    ),
    (
        "3. Modify the `startNodeManagerMx.sh` script to add the lines below.  ",
        "3. Измените скрипт `startNodeManagerMx.sh`, добавив приведённые ниже строки.  ",
    ),
    (
        "   (After running `commEnv.sh`, refer to the script under `/apps/wldomains/wls-aabb-1a` on `aaaabbb01a`).",
        "   (После запуска `commEnv.sh` обратитесь к скрипту в `/apps/wldomains/wls-aabb-1a` на `aaaabbb01a`).",
    ),
    ("4. Start a new session.", "4. Запустите новый сеанс."),
    ("5. Start Node Manager.", "5. Запустите Node Manager."),
    (
        "6. Get a PID while Node Manager is working.",
        "6. Получите PID, пока Node Manager работает.",
    ),
    (
        "   Use the command line `$ pargs -e pid |grep LD` to see if the environment is there.",
        "   Используйте командную строку `$ pargs -e pid |grep LD`, чтобы проверить, присутствует ли окружение.",
    ),
    ("   Example:", "   Пример:"),
    (
        "7. Start managed nodes from the console.",
        "7. Запустите управляемые узлы из консоли.",
    ),
    (
        "8. Check the log directory to make sure a new log is generated:",
        "8. Проверьте каталог логов, чтобы убедиться, что генерируется новый лог:",
    ),
    (
        'For more details on setting up Oracle WebLogic monitoring, see [Configure Oracle WebLogic via startup script](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris#weblogic "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).")',
        'Подробнее о настройке мониторинга Oracle WebLogic см. в [Настройка Oracle WebLogic через скрипт запуска](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris#weblogic "Узнайте, как настроить Dynatrace для мониторинга приложений различных технологий, работающих на Solaris (x86 и SPARC).")',
    ),
]

# ---- install pairs ("Apache HTTP Server" standalone tab label kept EN as product name) ----
I_PAIRS = [
    ("title: Install OneAgent on Solaris", "title: Установка OneAgent на Solaris"),
    ("# Install OneAgent on Solaris", "# Установка OneAgent на Solaris"),
    ("* 7-min read", "* Чтение: 7 мин"),
    ("* Updated on Jan 22, 2026", "* Обновлено 22 января 2026 г."),
    (
        "This page describes how to download and install Dynatrace OneAgent on Solaris.",
        "На этой странице описано, как загрузить и установить Dynatrace OneAgent на Solaris.",
    ),
    (
        'To get started, access the [Cluster Management Console and choose the environment](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.") you want to monitor, then continue with the installation steps below.',
        'Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.',
    ),
    ("## Requirements", "## Требования"),
    ("### Permissions", "### Разрешения"),
    (
        "* You need administrator rights for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).",
        "* Вам нужны права администратора на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если ваша внутренняя политика маршрутизации может препятствовать доступу программного обеспечения Dynatrace в Интернет).",
    ),
    (
        "* You need permissions and credentials for restarting all your application services.",
        "* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.",
    ),
    ("### Resources", "### Ресурсы"),
    (
        'All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").',
        'Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности вы можете либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").',
    ),
    ("### Limitations", "### Ограничения"),
    (
        "* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.",
        "* Установка OneAgent не поддерживается на сетевых точках монтирования хранилищ, управляемых такими стандартами, как NFS или iSCSI.",
    ),
    (
        '* [Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") mode isn\'t supported on Solaris hosts.',
        '* Режим [Infrastructure Monitoring](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.") не поддерживается на хостах Solaris.',
    ),
    (
        "### Allow connections through firewall",
        "### Разрешите подключения через брандмауэр",
    ),
    (
        "Ensure that your firewall settings allow communication to Dynatrace.  ",
        "Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.  ",
    ),
    (
        "Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**",
        "В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**",
    ),
    ("## Installation", "## Установка"),
    ("1. Go to **Deploy Dynatrace**.", "1. Перейдите в **Deploy Dynatrace**."),
    (
        "2. Select **Start installation** > **Solaris**.",
        "2. Выберите **Start installation** > **Solaris**.",
    ),
    (
        "3. Choose the CPU architecture of your environment.",
        "3. Выберите архитектуру ЦП вашего окружения.",
    ),
    (
        "4. Provide a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token \"Learn the concept of an access token and its scopes.\"). This token is required to download the OneAgent installer from your environment. If you don't have a PaaS token, you can generate one right in the UI. The token is automatically appended to the download command you'll use later.",
        '4. Укажите [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей."). Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Если у вас нет PaaS-токена, вы можете сгенерировать его прямо в интерфейсе. Токен автоматически добавляется к команде загрузки, которую вы будете использовать далее.',
    ),
    (
        "5. Click **Copy** to copy the `wget` command.",
        "5. Нажмите **Copy**, чтобы скопировать команду `wget`.",
    ),
    (
        "6. Log into your Solaris host and execute the `wget` command.",
        "6. Войдите на ваш хост Solaris и выполните команду `wget`.",
    ),
    (
        "   * The `wget` command isn't installed on Solaris by default. Either install it or use an alternative means of downloading OneAgent.",
        "   * Команда `wget` не установлена на Solaris по умолчанию. Установите её или используйте альтернативный способ загрузки OneAgent.",
    ),
    (
        "7. Create a folder on your local system for OneAgent (for example, `/opt/dynatrace/oneagent`) and unzip the zip-archive into the folder.",
        "7. Создайте на локальной системе папку для OneAgent (например, `/opt/dynatrace/oneagent`) и распакуйте zip-архив в эту папку.",
    ),
    (
        "   In contrast to other platforms, root access isn't required for installation of OneAgent on Solaris. OneAgent can be installed in any directory.",
        "   В отличие от других платформ, для установки OneAgent на Solaris не требуется доступ root. OneAgent можно установить в любой каталог.",
    ),
    (
        "   * As all monitored applications need to be able to read the library, ensure that the permissions allow this.",
        "   * Поскольку все мониторируемые приложения должны иметь возможность читать библиотеку, убедитесь, что разрешения это позволяют.",
    ),
    (
        "     + Give global read permissions to `/opt/dynatrace/oneagent`",
        "     + Предоставьте глобальные разрешения на чтение для `/opt/dynatrace/oneagent`",
    ),
    (
        "     + Give global write permissions to `/opt/dynatrace/oneagent/logs`",
        "     + Предоставьте глобальные разрешения на запись для `/opt/dynatrace/oneagent/logs`",
    ),
    (
        "   * Be sure to reference the folder correctly in the subsequent steps of your deployment.",
        "   * Обязательно правильно указывайте эту папку на последующих шагах развёртывания.",
    ),
    (
        "8. On Solaris, Dynatrace only supports Java and Apache HTTP Server applications and as such you need to decide which applications to monitor. You can do this just for a single application, or shell wide. Just follow the relative instructions below.",
        "8. На Solaris Dynatrace поддерживает только приложения Java и Apache HTTP Server, поэтому вам нужно решить, какие приложения мониторить. Это можно сделать как для одного приложения, так и в рамках всей оболочки. Следуйте соответствующим инструкциям ниже.",
    ),
    ("   Monitoring a single application", "   Мониторинг одного приложения"),
    (
        "   To monitor a single application, execute your command and prepend it with the following commands.",
        "   Чтобы мониторить одно приложение, выполните вашу команду, предварив её следующими командами.",
    ),
    (
        "   The `DT_HOME` variable points to your OneAgent installation folder. You can omit either the 32-bit or 64-bit entry, depending on your environment.",
        "   Переменная `DT_HOME` указывает на папку установки OneAgent. Вы можете опустить запись для 32-бит или 64-бит в зависимости от вашего окружения.",
    ),
    (
        "   Configure WebSphere Application Server via the Administrative console",
        "   Настройка WebSphere Application Server через административную консоль",
    ),
    (
        "   The unified approach works just as well for WebSphere, however you may want to configure your WebSphere via the Administrative console. This works for OneAgent v1.141 and above.",
        "   Унифицированный подход одинаково хорошо работает и для WebSphere, однако вы можете предпочесть настроить WebSphere через административную консоль. Это работает для OneAgent v1.141 и выше.",
    ),
    (
        "   1. Start the WebSphere server via the WebSphere UI or the command line. For example: `/opt/ibm/WebSphere<version>/AppServer/bin/sh startServer.sh server1`",
        "   1. Запустите сервер WebSphere через интерфейс WebSphere или командную строку. Например: `/opt/ibm/WebSphere<version>/AppServer/bin/sh startServer.sh server1`",
    ),
    (
        "   2. Open the Administrative Console via the WebSphere UI or enter the URL in your web browser. For example:`http://localhost:9060/ibm/console`. When accessing the server remotely, specify the machine's hostname rather than `localhost`.",
        "   2. Откройте административную консоль через интерфейс WebSphere или введите URL в веб-браузере. Например:`http://localhost:9060/ibm/console`. При удалённом доступе к серверу укажите имя хоста машины вместо `localhost`.",
    ),
    (
        "   3. Enter your user ID and password and then log in.",
        "   3. Введите ваш идентификатор пользователя и пароль, затем войдите в систему.",
    ),
    (
        "   4. Navigate to **Server** > **Application servers** > `[yourprofilename]`> **Java and Process Management** > **Process Definition** > **Environment Entries** > **New**.",
        "   4. Перейдите в **Server** > **Application servers** > `[yourprofilename]`> **Java and Process Management** > **Process Definition** > **Environment Entries** > **New**.",
    ),
    ("   5. Add 3 entries to the list.", "   5. Добавьте в список 3 записи."),
    (
        "      You can omit either the 32-bit or 64-bit entry, depending on your environment. The `DT_HOME` variable must point to your OneAgent installation folder.",
        "      Вы можете опустить запись для 32-бит или 64-бит в зависимости от вашего окружения. Переменная `DT_HOME` должна указывать на папку установки OneAgent.",
    ),
    (
        "   6. Apply the changes and save the configuration.",
        "   6. Примените изменения и сохраните конфигурацию.",
    ),
    (
        "   Configure Oracle WebLogic via the startup script",
        "   Настройка Oracle WebLogic через скрипт запуска",
    ),
    (
        "   To monitor Oracle WebLogic you need to add the following lines to the WebLogic startup script (`startWebLogic.sh`)",
        "   Чтобы мониторить Oracle WebLogic, нужно добавить следующие строки в скрипт запуска WebLogic (`startWebLogic.sh`)",
    ),
    (
        "   You can omit either the 32-bit or 64-bit entry, depending on your environment. The `DT_HOME` variable must point to your OneAgent installation folder.",
        "   Вы можете опустить запись для 32-бит или 64-бит в зависимости от вашего окружения. Переменная `DT_HOME` должна указывать на папку установки OneAgent.",
    ),
    (
        "   Monitoring every Java and Apache HTTP service in your execution context",
        "   Мониторинг каждого сервиса Java и Apache HTTP в вашем контексте выполнения",
    ),
    (
        "   You can set up OneAgent to monitor every application in your current application context. To do this, add the following lines to the startup script of the application you want to monitor. Ensure that they're executed prior to the application itself. You should not do this system-wide or for login users.",
        "   Вы можете настроить OneAgent на мониторинг каждого приложения в текущем контексте приложений. Для этого добавьте следующие строки в скрипт запуска приложения, которое вы хотите мониторить. Убедитесь, что они выполняются до самого приложения. Не делайте это в масштабе всей системы или для пользователей входа в систему.",
    ),
    ("   OneAgent v1.141 and above", "   OneAgent v1.141 и выше"),
    ("   OneAgent v1.137 to v1.139", "   OneAgent с v1.137 по v1.139"),
    (
        "   `LD_PRELOAD` will not carry over into `sudo` or `su` calls. Moreover, calling `sudo` in an execution context that has `LD_PRELOAD` set will lead to an error message that the library is in a non-secure location. This has no negative impact. This message can be ignored.",
        "   `LD_PRELOAD` не переносится в вызовы `sudo` или `su`. Более того, вызов `sudo` в контексте выполнения, где задан `LD_PRELOAD`, приведёт к сообщению об ошибке о том, что библиотека находится в небезопасном расположении. Это не имеет негативных последствий. Это сообщение можно игнорировать.",
    ),
    (
        'If you use the WebLogic admin server to restart managed nodes on Solaris, see [Troubleshoot OneAgent installation on Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris#weblogic-admin "Find out how to solve problems related to installing OneAgent on Solaris.") to learn how to modify the startup script.',
        'Если вы используете административный сервер WebLogic для перезапуска управляемых узлов на Solaris, см. [Устранение неполадок при установке OneAgent на Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/troubleshoot-oneagent-installation-on-solaris#weblogic-admin "Узнайте, как решать проблемы, связанные с установкой OneAgent на Solaris."), чтобы узнать, как изменить скрипт запуска.',
    ),
    (
        "## OneAgent versions older than v1.137 and fallback",
        "## Версии OneAgent старше v1.137 и запасной вариант",
    ),
    (
        "If your OneAgent is older than v1.137, or if you have problems with the unified monitoring approach, you can inject OneAgent manually.",
        "Если ваш OneAgent старше v1.137 или если у вас возникают проблемы с унифицированным подходом к мониторингу, вы можете внедрить OneAgent вручную.",
    ),
    ("Manual OneAgent injection", "Ручное внедрение OneAgent"),
    ("Generic Java applications", "Стандартные Java-приложения"),
    (
        "Modify the command line of your Java application:",
        "Измените командную строку вашего Java-приложения:",
    ),
    (
        "Make sure that you include the `$JAVA_OPTS` variable in your command. For 32-bit Java processes, omit the `64` parameter.",
        "Убедитесь, что вы включили переменную `$JAVA_OPTS` в свою команду. Для 32-битных процессов Java опустите параметр `64`.",
    ),
    (
        "The following steps are required to configure Dynatrace to monitor Apache HTTP server or running on Solaris:",
        "Для настройки Dynatrace на мониторинг Apache HTTP server, работающего на Solaris, требуются следующие шаги:",
    ),
    (
        "Edit your `httpd.conf` and add the following two lines in a location of your choice:",
        "Отредактируйте ваш `httpd.conf` и добавьте следующие две строки в выбранном вами месте:",
    ),
    (
        "Alternatively, if you prefer to leave your `httpd.conf` unchanged, you can specify the same directives using the command line:",
        "Кроме того, если вы предпочитаете оставить `httpd.conf` без изменений, вы можете указать те же директивы с помощью командной строки:",
    ),
    (
        "* `tenantUUID` is the environment ID of your Dynatrace environment that should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantUUID` parameter is represented in the script as `DT_TENANT`.",
        "* `tenantUUID` является идентификатором окружения вашей среды Dynatrace, который следует взять из `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent). Параметр `tenantUUID` представлен в скрипте как `DT_TENANT`.",
    ),
    (
        "* `tenantToken` is the token that OneAgent uses to connect to Dynatrace Server. It should be pulled from `dynatrace-env.sh` (located in the OneAgent installation root directory). The `tenantToken` parameter is represented in the script as `DT_TENANTTOKEN`.",
        "* `tenantToken` является токеном, который OneAgent использует для подключения к Dynatrace Server. Его следует взять из `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent). Параметр `tenantToken` представлен в скрипте как `DT_TENANTTOKEN`.",
    ),
    (
        "  This token should not be confused with Dynatrace API or PaaS tokens. Those tokens can't be used here.",
        "  Этот токен не следует путать с токенами Dynatrace API или PaaS. Те токены здесь использовать нельзя.",
    ),
    (
        "* `communicationEndpoints` corresponds to one or multiple HTTP addresses that represent Dynatrace Servers or ActiveGates. The `communicationEndpoints` parameter is represented in the script as `DT_CONNECTION_POINT`. For example, the `dynatrace-env.sh` (located in the OneAgent installation root directory) may contain the following:",
        "* `communicationEndpoints` соответствует одному или нескольким HTTP-адресам, представляющим Dynatrace Server или ActiveGate. Параметр `communicationEndpoints` представлен в скрипте как `DT_CONNECTION_POINT`. Например, `dynatrace-env.sh` (находится в корневом каталоге установки OneAgent) может содержать следующее:",
    ),
    (
        "  In this case, the parameter would be",
        "  В этом случае параметр будет следующим",
    ),
    ("## You've arrived!", "## Вы на месте!"),
    (
        "Great, the setup is complete! You can now take a look around your new monitoring environment.",
        "Отлично, настройка завершена! Теперь вы можете осмотреться в своём новом окружении мониторинга.",
    ),
    (
        'You can access your monitoring environment through the [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").',
        'Вы можете получить доступ к своему окружению мониторинга через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними.").',
    ),
    (
        "![Arrived](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)",
        "![Вы на месте](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)",
    ),
    ("Arrived", "Вы на месте"),
    (
        "One last thing: to monitor your processes, you need to restart them. You can restart your processes at any time, even during your organization's next planned maintenance period.",
        "И последнее: чтобы мониторить ваши процессы, их нужно перезапустить. Вы можете перезапустить процессы в любое время, даже во время следующего планового периода обслуживания в вашей организации.",
    ),
]


def build(en_path: Path, ru_path: Path, pairs):
    mapping = {}
    for en, ru in pairs:
        if en in mapping and mapping[en] != ru:
            print(f"  !! duplicate EN key with different RU: {en[:60]!r}")
        mapping[en] = ru
    raw = en_path.read_bytes()
    if raw[:3] == b"\xef\xbb\xbf":
        print(f"  note: source has leading BOM ({en_path.name})")
    text = raw.decode("utf-8")
    en_lines = [ln.rstrip("\r") for ln in text.split("\n")]
    used = set()
    out = []
    leftover = []
    for ln in en_lines:
        if ln in mapping:
            out.append(mapping[ln])
            used.add(ln)
        else:
            out.append(ln)
            # flag potential missed prose (latin letters, not code/fence/blank)
            s = ln.strip()
            if (
                s
                and not s.startswith("```")
                and any("a" <= c.lower() <= "z" for c in s)
            ):
                leftover.append(ln)
    unused = [k for k in mapping if k not in used]
    result = "\n".join(out)
    ru_path.parent.mkdir(parents=True, exist_ok=True)
    ru_path.write_bytes(result.encode("utf-8"))
    print(f"== {ru_path.name}")
    print(
        f"   EN lines={len(en_lines)}  RU lines={len(result.split(chr(10)))}  bytes={len(result.encode('utf-8'))}"
    )
    if unused:
        print(f"   !! UNUSED keys (typo in EN match) = {len(unused)}:")
        for k in unused:
            print(f"      {k!r}")
    if leftover:
        print(f"   leftover EN-ish lines (verify intentional) = {len(leftover)}:")
        for k in leftover:
            print(f"      {k!r}")
    return len(unused) == 0


ok1 = build(
    BASE.parent / "solaris" / "troubleshoot-oneagent-installation-on-solaris.md",
    RU_BASE / "troubleshoot-oneagent-installation-on-solaris.md",
    T_PAIRS,
)
ok2 = build(
    BASE.parent / "solaris" / "install-oneagent-on-solaris.md",
    RU_BASE / "install-oneagent-on-solaris.md",
    I_PAIRS,
)
sys.exit(0 if (ok1 and ok2) else 1)
