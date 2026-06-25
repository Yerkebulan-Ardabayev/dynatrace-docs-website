# -*- coding: utf-8 -*-
"""L4-IF.22 OneAgent Windows family builder.

Text-keyed line-map: for each EN line, if exact text is in the file's MAP -> RU,
else copy EN verbatim (blank, code-fence, code body, frontmatter source/scraped,
intentionally-EN UI-bold lines). Guarantees line-parity, code-fence byte-identity,
frontmatter preservation. Update file is derived from the translated linux brother
by OS substitution (structures are line-identical).

Run: python scripts/_build_windows_l4if22.py
"""

import os
import re
import difflib

BASE = os.path.join(os.path.dirname(__file__), "..", "docs")
ROOT = "ingest-from/dynatrace-oneagent/installation-and-operation"


def lines_of(path):
    with open(path, "rb") as f:
        text = f.read().decode("utf-8").replace("\r\n", "\n")
    return text.split("\n"), text.endswith("\n")


def write_lines(path, lines, trailing_nl):
    text = "\n".join(lines) + ("\n" if trailing_nl else "")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))


def normalize(s):
    """Collapse double-encoded mojibake to clean chars so map keys stay clean."""
    s = s.replace("â\x80\x94", "—")  # em-dash
    s = s.replace("â\x80\x93", "–")  # en-dash
    s = s.replace("â\x80\x99", "'")  # right single quote / apostrophe
    s = s.replace("â\x80\x98", "'")  # left single quote
    s = s.replace("â\x80\x9c", "“").replace("â\x80\x9d", "”")  # quotes
    s = s.replace("â\x80\xa6", "…")  # ellipsis
    s = s.replace("Î£", "Σ")  # mojibaked Greek capital Sigma (sum symbol)
    s = s.replace("ï»¿", "")  # double-encoded BOM
    return s


def _trailing_ws(s):
    m = re.search(r"[ \t]+$", s)
    return m.group(0) if m else ""


def _leftover(ln):
    if ln.startswith(("source:", "scraped:")):
        return False
    t = re.sub(r"`[^`]*`", "", ln)
    t = re.sub(r"\]\([^)]*\)", "", t)
    t = re.sub(r"\*\*[^*]*\*\*", "", t)
    t = re.sub(r"https?://\S+", "", t)
    return bool(re.search(r"[A-Za-z]{2,}\s+[A-Za-z]{2,}\s+[A-Za-z]{2,}", t))


def build_textmap(rel, mapping):
    en_path = os.path.join(BASE, "managed", rel)
    ru_path = os.path.join(BASE, "managed-ru", rel)
    en_lines, tnl = lines_of(en_path)
    out, missed = [], []
    used = set()
    for i, ln in enumerate(en_lines, 1):
        nkey = normalize(ln)
        val = None
        if ln.strip():
            for k in (ln, ln.rstrip(), nkey, nkey.rstrip()):
                if k in mapping:
                    val = mapping[k]
                    used.add(k)
                    break
        if val is not None:
            out.append(val.rstrip() + _trailing_ws(ln))  # preserve EN hard-break
        else:
            out.append(ln)
            if _leftover(ln):
                missed.append((i, ln[:70]))
    write_lines(ru_path, out, tnl)
    unused = [k[:50] for k in mapping if k not in used]
    print(f"[{rel.split('/')[-1]}] lines={len(out)} tnl={tnl}")
    if missed:
        print("   LEFTOVER-EN (verify intentional):")
        for i, s in missed:
            print(f"     L{i}: {s}")
    if unused:
        print("   UNUSED MAP KEYS (typo?):")
        for s in unused:
            print(f"     {s}")


def _fence_set(lines):
    """Indices (0-based) of lines inside ``` code fences."""
    inside, s = False, set()
    for i, ln in enumerate(lines):
        toggled = ln.strip().startswith("```")
        if inside or toggled:
            s.add(i)
        if toggled:
            inside = not inside
    return s


def build_difflib(rel, brother_rel, override):
    """Derive RU from translated brother via difflib (L4-IF.21).
    equal blocks -> copy brother RU (line-parity guarantees index match);
    replace/insert -> override[normalized win line] OR copy EN + flag.
    Frontmatter source/scraped + code-fence lines copied from EN-windows."""
    en_path = os.path.join(BASE, "managed", rel)
    en_bro_path = os.path.join(BASE, "managed", brother_rel)
    ru_bro_path = os.path.join(BASE, "managed-ru", brother_rel)
    ru_path = os.path.join(BASE, "managed-ru", rel)
    en_win, tnl = lines_of(en_path)
    en_bro, _ = lines_of(en_bro_path)
    ru_bro, _ = lines_of(ru_bro_path)
    if len(en_bro) != len(ru_bro):
        print(f"[ABORT {rel}] brother EN={len(en_bro)} RU={len(ru_bro)} not parity")
        return
    fences = _fence_set(en_win)
    out = [None] * len(en_win)
    missed, used = [], set()
    sm = difflib.SequenceMatcher(None, en_bro, en_win, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(j2 - j1):
                out[j1 + k] = ru_bro[i1 + k]
        elif tag in ("replace", "insert"):
            for j in range(j1, j2):
                ln = en_win[j]
                if (
                    ln.startswith(("source:", "scraped:"))
                    or j in fences
                    or not ln.strip()
                ):
                    out[j] = ln
                    continue
                val = None
                for key in (ln, ln.rstrip(), normalize(ln), normalize(ln).rstrip()):
                    if key in override:
                        val = override[key]
                        used.add(key)
                        break
                if val is not None:
                    out[j] = val.rstrip() + _trailing_ws(ln)
                else:
                    out[j] = ln
                    if _leftover(ln):
                        missed.append((j + 1, ln[:75]))
        # delete: brother-only lines, skip
    write_lines(ru_path, out, tnl)
    unused = [k[:50] for k in override if k not in used]
    print(f"[{rel.split('/')[-1]}] difflib lines={len(out)} tnl={tnl}")
    if missed:
        print(f"   NEEDS-TRANSLATION ({len(missed)} lines):")
        for i, s in missed:
            print(f"     L{i}: {s}")
    if unused:
        print("   UNUSED OVERRIDE KEYS:")
        for s in unused:
            print(f"     {s}")


def build_derive(rel, brother_rel, line_overrides):
    """Derive RU from translated brother by index; brother must be line-parity.
    line_overrides: {1-based-index: ru_text} applied AFTER substitution.
    Substitution: Linux->Windows, linux->windows. Frontmatter source/scraped
    copied from EN-windows (byte-exact)."""
    en_path = os.path.join(BASE, "managed", rel)
    ru_bro_path = os.path.join(BASE, "managed-ru", brother_rel)
    ru_path = os.path.join(BASE, "managed-ru", rel)
    en_lines, tnl = lines_of(en_path)
    bro_lines, _ = lines_of(ru_bro_path)
    if len(en_lines) != len(bro_lines):
        print(f"[ABORT {rel}] EN={len(en_lines)} brother={len(bro_lines)} not parity")
        return
    out = []
    for i, (en_ln, bro_ln) in enumerate(zip(en_lines, bro_lines), 1):
        if i in line_overrides:
            out.append(line_overrides[i])
        elif en_ln.startswith(("source:", "scraped:")):
            out.append(en_ln)  # frontmatter byte-exact from EN-windows
        else:
            out.append(bro_ln.replace("Linux", "Windows").replace("linux", "windows"))
    write_lines(ru_path, out, tnl)
    print(
        f"[{rel.split('/')[-1]}] derived from {brother_rel.split('/')[-1]} lines={len(out)} tnl={tnl}"
    )


# ---------------- windows.md (hub) ----------------
HUB = {
    "title: OneAgent on Windows": "title: OneAgent на Windows",
    "# OneAgent on Windows": "# OneAgent на Windows",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Sep 19, 2018": "* Опубликовано 19 сентября 2018 г.",
    'You can install OneAgent on Windows using installer provided as a self-extracting EXE fileâ\x80\x94for single-server installationâ\x80\x94and also as an MSI package, for Group Policy deployments. For analytical information about the supported OneAgent capabilities for Windows, see the [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms."). For the supported Windows versions, check the [OneAgent supported technologies and versions](/managed/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").': 'OneAgent можно установить на Windows с помощью установщика, предоставляемого в виде самораспаковывающегося EXE-файла (для установки на одном сервере), а также в виде MSI-пакета для развёртываний через групповые политики. Аналитические сведения о поддерживаемых возможностях OneAgent для Windows см. в [матрице поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."). Поддерживаемые версии Windows см. в [Поддерживаемые технологии и версии OneAgent](/managed/ingest-from/technology-support "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").',
    "### Installation": "### Установка",
    '[Disk space requirements](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.")': '[Требования к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.")',
    '[OneAgent security](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")': '[Безопасность OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows")',
    '[Install OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Learn how to download and install Dynatrace OneAgent on Windows.")': '[Установка OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows "Узнайте, как скачать и установить Dynatrace OneAgent на Windows.")',
    '[Customize installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.")': '[Настройка установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.")',
    '[How to pass a proxy address](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows "Find out how to force Dynatrace OneAgent on Windows to use a proxy for communication with your environment.")': '[Как передать адрес прокси](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows "Узнайте, как заставить Dynatrace OneAgent на Windows использовать прокси для связи с вашим окружением.")',
    "### Operation": "### Эксплуатация",
    '[OneAgent files and logs](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.")': '[Файлы и журналы OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.")',
    '[Update OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.")': '[Обновление OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Узнайте о различных способах обновления Dynatrace OneAgent на Windows.")',
    '[Stop/restart OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Learn how to stop and restart OneAgent on Windows.")': '[Остановка/перезапуск OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/stop-restart-oneagent-on-windows "Узнайте, как остановить и перезапустить OneAgent на Windows.")',
    '[Uninstall OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows "Learn how you can remove Dynatrace OneAgent from your system.")': '[Удаление OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/uninstall-oneagent-on-windows "Узнайте, как удалить Dynatrace OneAgent из вашей системы.")',
    "### See also": "### См. также",
    '[OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")': '[Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.")',
    '[Troubleshoot](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation "Learn how to troubleshoot OneAgent installation on AIX, Linux, and Windows.")': '[Устранение неполадок](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-installation "Узнайте, как устранять неполадки установки OneAgent на AIX, Linux и Windows.")',
}

# ---------------- stop-restart ----------------
STOP = {
    "title: Stop/restart OneAgent on Windows": "title: Остановка/перезапуск OneAgent на Windows",
    "# Stop/restart OneAgent on Windows": "# Остановка/перезапуск OneAgent на Windows",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Sep 19, 2018": "* Опубликовано 19 сентября 2018 г.",
    "In case you don't want to use OneAgent inside a particular Java (or other) process, you can easily disable Dynatrace monitoring for individual hosts, process groups, or applications:": "Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), можно легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:",
    "1. Go to **Settings > Monitoring overview**.": "1. Перейдите в **Settings > Monitoring overview**.",
    "2. Click the **Hosts**, **Process groups**, or **Applications** tab to access the monitoring switches for individual entities.": "2. Откройте вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных сущностей.",
    "3. Slide the **Monitoring** switch to the **Off** position.": "3. Переведите переключатель **Monitoring** в положение **Off**.",
    "4. Restart all processes for which monitoring has been disabled.": "4. Перезапустите все процессы, для которых мониторинг был отключён.",
    "## Restart using OneAgent command-line interface": "## Перезапуск через интерфейс командной строки OneAgent",
    "When you use the `set` parameters, you need to restart OneAgent service to apply changes. You can use the `--restart-service` parameter with the command that triggers the restart automatically. In some cases you'll also need to restart monitored applications. You can also use the restart parameter on its own, without other parameters. See an example command below.": "При использовании параметров `set` необходимо перезапустить службу OneAgent, чтобы изменения вступили в силу. Можно использовать параметр `--restart-service` с командой, которая запускает перезапуск автоматически. В некоторых случаях также потребуется перезапустить мониторируемые приложения. Параметр перезапуска можно использовать и сам по себе, без других параметров. Пример команды приведён ниже.",
    'For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").': 'Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").',
    "## Stop OneAgent using the command line": "## Остановка OneAgent через командную строку",
    'If you use configuration management tools like Puppet or Ansible, you can stop the OneAgent service using the `net stop "Dynatrace OneAgent"` command, where `Dynatrace OneAgent` is the service name for OneAgent.': 'Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, остановить службу OneAgent можно с помощью команды `net stop "Dynatrace OneAgent"`, где `Dynatrace OneAgent` является именем службы OneAgent.',
    "You can't stop the OneAgent service using the command line if that service is a part of another process, such as Java bytecode instrumentation. If you stop OneAgent service, monitoring will be disabled until the service is restarted.": "Остановить службу OneAgent через командную строку невозможно, если эта служба является частью другого процесса, например инструментирования байт-кода Java. Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.",
    "## Start OneAgent using the command line": "## Запуск OneAgent через командную строку",
    "To start OneAgent again, use the following command:": "Чтобы снова запустить OneAgent, используйте следующую команду:",
    '`net start "Dynatrace OneAgent"`, where `Dynatrace OneAgent` is the service name for OneAgent.': '`net start "Dynatrace OneAgent"`, где `Dynatrace OneAgent` является именем службы OneAgent.',
    'Learn more about [how Dynatrace interacts with your OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").': 'Подробнее о том, [как Dynatrace взаимодействует с вашей ОС](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").',
}

# ---------------- uninstall ----------------
UNINSTALL = {
    "title: Uninstall Dynatrace OneAgent on Windows": "title: Удаление Dynatrace OneAgent на Windows",
    "# Uninstall Dynatrace OneAgent on Windows": "# Удаление Dynatrace OneAgent на Windows",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Sep 19, 2018": "* Опубликовано 19 сентября 2018 г.",
    "Your OneAgent has a dedicated uninstall program. You'll need to run it to remove OneAgent from your system.": "OneAgent имеет специальную программу удаления. Для удаления OneAgent из системы необходимо запустить её.",
    "## Uninstall OneAgent using Windows Control Panel": "## Удаление OneAgent через панель управления Windows",
    "Use the Windows **Control Panel** to remove OneAgent.": "Используйте **Control Panel** Windows для удаления OneAgent.",
    "After all OneAgent files have been removed from your system, you'll need to reboot your machine to remove the agent libraries from memory.": "После того как все файлы OneAgent будут удалены из системы, потребуется перезагрузить компьютер, чтобы выгрузить библиотеки агента из памяти.",
    "## Uninstall OneAgent silently": "## Тихое удаление OneAgent",
    "### Command line": "### Командная строка",
    "To silently uninstall OneAgent using Windows command line, run the following WMIC commands as an administrator.": "Чтобы тихо удалить OneAgent через командную строку Windows, выполните следующие команды WMIC с правами администратора.",
    "You can omit `/l*vx uninstall.log` if the log file is not relevant to you.": "Можно опустить `/l*vx uninstall.log`, если лог-файл вам не нужен.",
    "### PowerShell": "### PowerShell",
    "## After you uninstall OneAgent": "## После удаления OneAgent",
    "Following uninstallation, log files, the user running OneAgent, and part of the configuration are preserved in the OneAgent installation directory. These can be removed manually. Note however that if the configuration files have been removed, and OneAgent is re-installed, the host will show up as a new host with a different internal identifier.": "После удаления лог-файлы, пользователь, от имени которого работает OneAgent, и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Обратите внимание, что если конфигурационные файлы были удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.",
    "For a complete OneAgent uninstallation, remove the following:": "Для полного удаления OneAgent удалите следующее:",
    "* Log files located at `%PROGRAMDATA%\\dynatrace\\oneagent\\log`.": "* Лог-файлы, расположенные по адресу `%PROGRAMDATA%\\dynatrace\\oneagent\\log`.",
    "* Configuration files located at `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config`.": "* Конфигурационные файлы, расположенные по адресу `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config`.",
}

# ---------------- how-to-pass-proxy ----------------
PROXY = {
    "title: How to pass a proxy address during OneAgent installation on Windows": "title: Как передать адрес прокси при установке OneAgent на Windows",
    "# How to pass a proxy address during OneAgent installation on Windows": "# Как передать адрес прокси при установке OneAgent на Windows",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Sep 19, 2018": "* Опубликовано 19 сентября 2018 г.",
    "The Windows installer allows you to enter a proxy address during installation, so in the majority of cases you don't need to worry about adding extra command line parameters. Command line parameters are particularly useful when you're deploying a [Group Policy installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows \"Learn how to use the OneAgent installer for Windows.\") or other automated task.": 'Установщик Windows позволяет ввести адрес прокси во время установки, поэтому в большинстве случаев можно не беспокоиться о добавлении дополнительных параметров командной строки. Параметры командной строки особенно полезны при развёртывании [установки через групповые политики](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.") или другой автоматизированной задачи.',
    "The OneAgent installer recognizes the `--set-proxy` parameter. The value of the parameter is the proxy server address. Add the port number following a colon (for example, `172.1.1.128:8080`). For an authenticating proxy, you can specify the username and password like this `username:password@172.1.1.128:8080`, where both username and password need to be URL encoded. Dynatrace also supports IPv6 addresses.": "Установщик OneAgent распознаёт параметр `--set-proxy`. Значением параметра является адрес прокси-сервера. Номер порта добавляется после двоеточия, например `172.1.1.128:8080`. Для прокси с аутентификацией можно указать имя пользователя и пароль так: `username:password@172.1.1.128:8080`, где имя пользователя и пароль должны быть в URL-кодировке. Dynatrace также поддерживает адреса IPv6.",
    "Parameter names are case-sensitive, so use `ALL CAPS` for parameter names.": "Имена параметров чувствительны к регистру, поэтому используйте `ALL CAPS` для имён параметров.",
    "## Passing a proxy address to the installer": "## Передача адреса прокси установщику",
    "Let's say you've downloaded your OneAgent installer to the `C:\\Users\\Admin\\Downloads` folder and your proxy IP address is `10.1.1.5`. In such a scenario you would begin the installation like this:": "Предположим, вы скачали установщик OneAgent в папку `C:\\Users\\Admin\\Downloads`, а IP-адрес вашего прокси равен `10.1.1.5`. В таком случае установку следует начать так:",
    "## Change proxy after installation": "## Изменение прокси после установки",
    'If you need to change the proxy address after installation, use `--set-proxy` in the [OneAgent command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").': 'Если требуется изменить адрес прокси после установки, используйте `--set-proxy` в [интерфейсе командной строки OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").',
}


# ---------------- install ----------------
INSTALL = {
    "title: Install OneAgent on Windows": "title: Установка OneAgent на Windows",
    "# Install OneAgent on Windows": "# Установка OneAgent на Windows",
    "* How-to guide": "* Практическое руководство",
    "* 7-min read": "* Чтение: 7 мин",
    "* Updated on Mar 05, 2026": "* Обновлено 05 марта 2026 г.",
    "This page describes how to download and install Dynatrace OneAgent on Windows.": "На этой странице описано, как загрузить и установить Dynatrace OneAgent на Windows.",
    'To get started, access the [Cluster Management Console and choose the environment](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.") you want to monitor, then continue with the installation steps below.': 'Для начала откройте [Cluster Management Console и выберите окружение](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними."), которое нужно мониторить, затем перейдите к шагам установки ниже.',
    "Dynatrace provides an Ansible collection that you can use to orchestrate OneAgent deployment in your environment.": "Dynatrace предоставляет коллекцию Ansible, которую можно использовать для оркестрации развёртывания OneAgent в вашем окружении.",
    'For more information, see [Install OneAgent using Ansible](/managed/ingest-from/dynatrace-oneagent/deployment-orchestration/ansible "Learn how to deploy OneAgent using Dynatrace-provided Ansible playbook.").': 'Дополнительные сведения см. в [Установка OneAgent с помощью Ansible](/managed/ingest-from/dynatrace-oneagent/deployment-orchestration/ansible "Узнайте, как развернуть OneAgent с помощью предоставляемого Dynatrace плейбука Ansible.").',
    "## Requirements and prerequisites": "## Требования и предварительные условия",
    '* You need [administrator rights](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system") for the servers where OneAgent will be installed as well as for changing firewall settings (necessary only if your internal routing policy may prevent Dynatrace software from reaching the Internet).': '* Вам нужны [права администратора](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows") на серверах, где будет установлен OneAgent, а также для изменения настроек брандмауэра (необходимо только если ваша внутренняя политика маршрутизации может препятствовать доступу программного обеспечения Dynatrace в Интернет).',
    "* You need permissions and credentials for restarting all your application services.": "* Вам нужны разрешения и учётные данные для перезапуска всех ваших сервисов приложений.",
    '* You need to check also the [disk space requirements](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.").': '* Также ознакомьтесь с [требованиями к дисковому пространству](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.").',
    "* The host on which you install OneAgent needs at least 200 MB RAM.": "* Хост, на котором устанавливается OneAgent, должен иметь не менее 200 МБ оперативной памяти.",
    "* OneAgent installation isn't supported on networked storage mount points that are managed by standards such as NFS or iSCSI.": "* Установка OneAgent не поддерживается на сетевых точках монтирования хранилищ, управляемых такими стандартами, как NFS или iSCSI.",
    '* All hosts that are to be monitored need to be able to send data to the Dynatrace cluster. Depending on your Dynatrace deployment and on your network layout and security settings, you may choose to either provide direct access to Dynatrace cluster or to [set up an ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").': '* Все хосты, которые должны мониториться, должны иметь возможность отправлять данные в кластер Dynatrace. В зависимости от вашего развёртывания Dynatrace, а также от схемы сети и настроек безопасности можно либо предоставить прямой доступ к кластеру Dynatrace, либо [настроить ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите базовые концепции, связанные с ActiveGate.").',
    '* For OneAgent version 1.253 and earlier, we recommend that you [uninstall any existing `WinPcap` driver](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#uninstall-winpcap-driver-to-allow-npcap-installation "Learn how to download and install Dynatrace OneAgent on Windows.") to allow `Npcap` installation—do this on all Windows versions, except for `Windows Server 2019 build 1809 without hotfix KB5066187`.': '* Для OneAgent версии 1.253 и более ранних рекомендуется [удалить любой существующий драйвер `WinPcap`](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#uninstall-winpcap-driver-to-allow-npcap-installation "Узнайте, как скачать и установить Dynatrace OneAgent на Windows."), чтобы разрешить установку `Npcap`: делайте это на всех версиях Windows, кроме `Windows Server 2019 build 1809 without hotfix KB5066187`.',
    '  For OneAgent version 1.255+, `Npcap` is installed by default and may cause a network disruption on `Windows Server 2016`, `Windows Server 2019 build 1809`, and `Windows Server 2019 build 1809 without hotfix KB5066187`. To prevent it, upgrade your hosts with the hotfix [KB5066187](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5066187) or use [other documented options](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#potential-network-disruption-during-oneagent-installation-on-windows "Learn more about troubleshooting network monitoring.").': '  Для OneAgent версии 1.255+ `Npcap` устанавливается по умолчанию и может вызвать нарушение работы сети на `Windows Server 2016`, `Windows Server 2019 build 1809` и `Windows Server 2019 build 1809 without hotfix KB5066187`. Чтобы это предотвратить, обновите ваши хосты с помощью исправления [KB5066187](https://www.catalog.update.microsoft.com/Search.aspx?q=KB5066187) или используйте [другие документированные варианты](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#potential-network-disruption-during-oneagent-installation-on-windows "Узнайте больше об устранении неполадок мониторинга сети.").',
    "### Allow connections through firewall": "### Разрешите подключения через брандмауэр",
    "Ensure that your firewall settings allow communication to Dynatrace.": "Убедитесь, что настройки вашего брандмауэра разрешают связь с Dynatrace.",
    "Depending on your firewall policy, you may need to explicitly allow certain outgoing connections. **The remote Dynatrace addresses to add to the allow list are given on the installation page for OneAgent.**": "В зависимости от политики вашего брандмауэра вам может потребоваться явно разрешить определённые исходящие подключения. **Удалённые адреса Dynatrace, которые нужно добавить в список разрешённых, указаны на странице установки OneAgent.**",
    "## Uninstall WinPcap driver to allow Npcap installation": "## Удаление драйвера WinPcap для установки Npcap",
    "If you have the `WinPcap` driver installed, we recommend that you remove it prior to OneAgent installation and let the OneAgent installer install the appropriate packet capture driver as packaged with the OneAgent installer: `Npcap` is the recommended packet capture driver for OneAgent.": "Если у вас установлен драйвер `WinPcap`, рекомендуется удалить его перед установкой OneAgent и позволить установщику OneAgent установить подходящий драйвер захвата пакетов, входящий в комплект установщика OneAgent: `Npcap` является рекомендуемым драйвером захвата пакетов для OneAgent.",
    "`Npcap` is the successor to `WinPcap` and is best suited for Dynatrace network analysis. The `Npcap` driver provided with the OneAgent installer is packaged in such a way that its DLL library files are integrated with Dynatrace software, which allows for unattended updates.": "`Npcap` является преемником `WinPcap` и лучше всего подходит для анализа сети Dynatrace. Драйвер `Npcap`, поставляемый с установщиком OneAgent, упакован таким образом, что файлы его DLL-библиотек интегрированы с программным обеспечением Dynatrace, что позволяет выполнять обновления без вмешательства пользователя.",
    "For more information, see:": "Дополнительные сведения см.:",
    '* [OneAgent security on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")': '* [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows")',
    '* [Customize OneAgent installation on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.")': '* [Настройка установки OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.")',
    'During the upgrade from `WinPcap` to `Npcap`, you might encounter network disruptions that can be mitigated by upgrading your Windows Server version and/or disabling `Microsoft Network Monitor Driver`. For details, see [Potential network disruptions during OneAgent installation on Windows](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#disruptionnetwork "Learn more about troubleshooting network monitoring.")': 'При обновлении с `WinPcap` на `Npcap` возможны нарушения работы сети; их можно смягчить, обновив версию Windows Server и/или отключив `Microsoft Network Monitor Driver`. Подробнее см. [Возможные нарушения работы сети при установке OneAgent на Windows](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring#disruptionnetwork "Узнайте больше об устранении неполадок мониторинга сети.")',
    "## Re-installation or repair of installation": "## Переустановка или восстановление установки",
    "OneAgent installer for Windows doesn't support the `modify` and `repair` operations. You can't reinstall OneAgent using the same installer version as was used to install the currently installed OneAgent. To reinstall OneAgent, uninstall it first or install a newer version.": "Установщик OneAgent для Windows не поддерживает операции `modify` и `repair`. Переустановить OneAgent с помощью той же версии установщика, которая использовалась для установки текущего OneAgent, невозможно. Чтобы переустановить OneAgent, сначала удалите его или установите более новую версию.",
    "## Installation": "## Установка",
    "1. Go to **Deploy Dynatrace**.": "1. Перейдите в **Deploy Dynatrace**.",
    "2. Select **Start installation** > **Windows**.": "2. Выберите **Start installation** > **Windows**.",
    '3. Paste a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") into **Installer download token** or select **Generate token** to generate a token now and automatically paste it into **Installer download token**. This token is required to download the OneAgent installer from your environment. The token is automatically appended to the download and installation commands you\'ll use later.': '3. Вставьте [PaaS-токен](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его областей.") в поле **Installer download token** или выберите **Generate token**, чтобы сгенерировать токен сейчас и автоматически вставить его в **Installer download token**. Этот токен необходим для загрузки установщика OneAgent из вашего окружения. Токен автоматически добавляется к командам загрузки и установки, которые вы будете использовать далее.',
    "4. Download the installer. There are two options:": "4. Скачайте установщик. Есть два варианта:",
    "   * Select **Download OneAgent installer** to download the installer for Windows (EXE file) for single-server installation.": "   * Выберите **Download OneAgent installer**, чтобы скачать установщик Windows (EXE-файл) для установки на одном сервере.",
    "   * Download via Windows Command Prompt. Copy and run the `powershell` command. It is generated automatically when you provide the PaaS token.": "   * Загрузка через командную строку Windows. Скопируйте и выполните команду `powershell`. Она генерируется автоматически при вводе PaaS-токена.",
    "     This command will only work with PowerShell 3.0 and TLS 1.2 (or later).": "     Эта команда работает только с PowerShell 3.0 и TLS 1.2 (или новее).",
    "   Get MSI package": "   Получение MSI-пакета",
    "   If you want to use Group Policy to automatically distribute OneAgent to your Windows hosts, you'll need the MSI package along with the batch file. To get the MSI package:": "   Если вы хотите использовать групповые политики для автоматического распространения OneAgent на ваши хосты Windows, вам понадобится MSI-пакет вместе с пакетным файлом. Чтобы получить MSI-пакет:",
    "   1. Download the OneAgent installer provided as an EXE file.": "   1. Скачайте установщик OneAgent, предоставляемый в виде EXE-файла.",
    "   2. Run it with the `--unpack-msi` parameter. This extracts the MSI package and the installation batch file. Optionally, you can specify an existing path. If you skip the path, the files are saved to a working directory. For example:": "   2. Запустите его с параметром `--unpack-msi`. Это извлечёт MSI-пакет и пакетный файл установки. При необходимости можно указать существующий путь. Если путь пропущен, файлы сохраняются в рабочий каталог. Например:",
    '   When using the `--unpack-msi` parameter, no other [installation parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.") are allowed. Add the `--quiet` parameter to run the MSI package extraction in quiet mode. Use the `--help` parameter to display a pop-up window with a list of available parameters.': '   При использовании параметра `--unpack-msi` другие [параметры установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.") не допускаются. Добавьте параметр `--quiet`, чтобы выполнить извлечение MSI-пакета в тихом режиме. Используйте параметр `--help`, чтобы отобразить всплывающее окно со списком доступных параметров.',
    '   Copy and paste the MSI package and the batch file when configuring Group Policy for Dynatrace installation. The default installation should work in most cases, but if you need to customize it, you can modify the [installation parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows."). Then, you have to create a distribution point, assign a package (the OneAgent MSI package with parameters), specify a command to install the MSI package as [silent installation](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#silent-installation "Learn how to use the OneAgent installer for Windows."), and publish your policy.': '   Скопируйте и вставьте MSI-пакет и пакетный файл при настройке групповой политики для установки Dynatrace. Установка по умолчанию должна работать в большинстве случаев, но если её требуется настроить, можно изменить [параметры установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows."). Затем необходимо создать точку распространения, назначить пакет (MSI-пакет OneAgent с параметрами), указать команду для установки MSI-пакета в режиме [тихой установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#silent-installation "Узнайте, как использовать установщик OneAgent для Windows.") и опубликовать вашу политику.',
    "5. Optional **Set customized options**": "5. Необязательно **Set customized options**",
    "   At this point, the Dynatrace UI allows you to customize your OneAgent installation: You can specify a number of customizations interactively on-screen. Based on your entries, an installation command will be generated and displayed, for use in the next step of installation (see below).": "   На этом этапе интерфейс Dynatrace позволяет настроить установку OneAgent: ряд настроек можно задать интерактивно на экране. На основе введённых данных будет сгенерирована и отображена команда установки для использования на следующем шаге установки (см. ниже).",
    "   You can:": "   Вы можете:",
    '   * Set a [network zone](/managed/manage/network-zones#deploy-network-zones "Find out how network zones work in Dynatrace.") for this host.': '   * Задать [сетевую зону](/managed/manage/network-zones#deploy-network-zones "Узнайте, как работают сетевые зоны в Dynatrace.") для этого хоста.',
    '   * Organize your hosts into [host groups](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups."), if your environment is segmented (for example, into development and production).': '   * Организовать ваши хосты в [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), если ваше окружение сегментировано (например, на разработку и продакшен).',
    '   * Override automatically detected [host name](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."). This is useful in large and dynamic environments, where defined host names can be unintuitive or can change frequently.': '   * Переопределить автоматически определённое [имя хоста](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Узнайте, как изменить имя мониторируемого хоста."). Это полезно в крупных и динамичных окружениях, где заданные имена хостов могут быть неинтуитивными или часто меняться.',
    '   * Apply [tags](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") to the host to organize your monitored environments in a meaningful way.': '   * Применить [теги](/managed/manage/tags-and-metadata "Используйте теги и метаданные для организации данных в вашем окружении Dynatrace.") к хосту, чтобы осмысленно организовать ваши мониторируемые окружения.',
    '   * Change the OneAgent mode to Infrastructure Monitoring or Discovery in place of Full-Stack Monitoring. For more information, see [OneAgent monitoring modes](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.").': '   * Изменить режим OneAgent на Infrastructure Monitoring или Discovery вместо Full-Stack Monitoring. Дополнительные сведения см. в [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").',
    '   * Disable [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.").': '   * Отключить [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить Log Monitoring, какие сведения он может предоставить, и многое другое.").',
    '   **If further customizations are required, you can specify [additional options on the command line](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Learn how to use the OneAgent installer for Windows.").**': '   **Если требуются дополнительные настройки, можно указать [дополнительные параметры в командной строке](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows "Узнайте, как использовать установщик OneAgent для Windows.").**',
    "6. If you have not specified any custom options, run the executable file and follow the instructions as displayed.": "6. Если вы не указали никаких пользовательских параметров, запустите исполняемый файл и следуйте отображаемым инструкциям.",
    "   If you have specified custom options above, use the generated command, and run it from the download directory. The command will contain all the installation parameters reflecting the custom settings you have specified.": "   Если вы указали пользовательские параметры выше, используйте сгенерированную команду и запустите её из каталога загрузки. Команда будет содержать все параметры установки, отражающие указанные вами пользовательские настройки.",
    "7. Restart all processes that you want to monitor. You'll be prompted with a list of the processes that need to be restarted. Note that you can restart your processes at any time, even during your organization's next planned maintenance period. Though until all processes have been restarted, you'll only see a limited set of metrics, for example CPU or memory consumption.": "7. Перезапустите все процессы, которые требуется мониторить. Вам будет показан список процессов, которые нужно перезапустить. Обратите внимание, что перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации. Однако пока не перезапущены все процессы, вы будете видеть лишь ограниченный набор метрик, например потребление CPU или памяти.",
    "What happens during installation?": "Что происходит во время установки?",
    "OneAgent is a set of specialized services that have been configured specifically for your monitoring environment. The role of these services is to monitor various aspects of your hosts, including hardware, operating system, and application processes.": "OneAgent представляет собой набор специализированных служб, настроенных специально для вашего окружения мониторинга. Роль этих служб состоит в мониторинге различных аспектов ваших хостов, включая аппаратное обеспечение, операционную систему и процессы приложений.",
    "During the installation process, the installer:": "В процессе установки установщик:",
    "* Installs executable code and libraries that are used by OneAgent.": "* Устанавливает исполняемый код и библиотеки, используемые OneAgent.",
    "* Creates entries in the Windows Registry that start OneAgent as a `SYSTEM` service. Additionally, the `oneagentmon` device and (optionally) `Npcap` or `WinPcap` are installed to allow better integration with the operating system and to facilitate the capture of network statistics.": "* Создаёт записи в реестре Windows, которые запускают OneAgent как службу `SYSTEM`. Кроме того, устанавливаются устройство `oneagentmon` и (опционально) `Npcap` или `WinPcap` для улучшения интеграции с операционной системой и упрощения сбора сетевой статистики.",
    "* Checks the system's global proxy settings.": "* Проверяет глобальные настройки прокси системы.",
    "* Checks for a connection to Dynatrace Server or ActiveGate (if you installed ActiveGate and downloaded the OneAgent installer after ActiveGate was connected to Dynatrace).": "* Проверяет подключение к Dynatrace Server или ActiveGate (если вы установили ActiveGate и скачали установщик OneAgent после того, как ActiveGate был подключён к Dynatrace).",
    "* OneAgent version 1.193 and earlier Creates its own user (`dtuser`) to run OneAgent extensions. This user is a member of the **Performance Monitoring Users** group, and can only log in as a service. The password is randomly generated during installation and stored encrypted. You can't change the password. For security purposes, the `dtuser` is not allowed to:": "* OneAgent версии 1.193 и более ранних Создаёт собственного пользователя (`dtuser`) для запуска расширений OneAgent. Этот пользователь входит в группу **Performance Monitoring Users** и может входить в систему только как служба. Пароль генерируется случайным образом во время установки и хранится в зашифрованном виде. Изменить пароль невозможно. В целях безопасности пользователю `dtuser` запрещено:",
    "  + Access computer from the network.": "  + Доступ к компьютеру из сети.",
    "  + Log in as a batch job.": "  + Вход в систему как пакетное задание.",
    "  + Log in locally.": "  + Локальный вход в систему.",
    "  + Log in through Remote Desktop Services.": "  + Вход в систему через Remote Desktop Services.",
    "    The `dtuser` is required for Dynatrace to operate properly, therefore you must not delete it. If, for some reason, the `dtuser` was deleted, next update will recreate it.": "    Пользователь `dtuser` необходим для правильной работы Dynatrace, поэтому удалять его нельзя. Если по какой-либо причине `dtuser` был удалён, следующее обновление создаст его заново.",
    "* OneAgent version 1.195+ For fresh OneAgent 1.195+ installations, the default `LocalSystem account` is used to run OneAgent extensions.": "* OneAgent версии 1.195+ Для новых установок OneAgent 1.195+ для запуска расширений OneAgent используется учётная запись `LocalSystem account` по умолчанию.",
    '  For a summarized view of the changes made to your system by OneAgent installation, see [OneAgent security on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").': '  Сводку изменений, внесённых в вашу систему при установке OneAgent, см. в [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").',
    "## You've arrived!": "## Вы на месте!",
    "Great, the setup is complete! You can now take a look around your new monitoring environment.": "Отлично, настройка завершена! Теперь можно осмотреться в своём новом окружении мониторинга.",
    'You can access your monitoring environment through the [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Find out how to create, configure, access, delete, disable, and switch between monitoring environments.").': 'Доступ к окружению мониторинга можно получить через [Cluster Management Console](/managed/managed-cluster/operation/manage-your-monitoring-environments "Узнайте, как создавать, настраивать, открывать, удалять, отключать окружения мониторинга и переключаться между ними.").',
    "![Arrived](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)": "![Вы на месте](https://dt-cdn.net/images/arrive-1533-e7eb3573a6.png)",
    "Arrived": "Вы на месте",
    "One last thing: to monitor your processes, you need to restart them. You can restart your processes at any time, even during your organization's next planned maintenance period.": "И последнее: чтобы мониторить ваши процессы, их нужно перезапустить. Перезапустить процессы можно в любое время, даже во время следующего планового периода обслуживания в вашей организации.",
}

# ---------------- oneagent-security ----------------
SECURITY = {
    "title: OneAgent security on Windows": "title: Безопасность OneAgent на Windows",
    "# OneAgent security on Windows": "# Безопасность OneAgent на Windows",
    "* 5-min read": "* Чтение: 5 мин",
    "* Published Nov 12, 2020": "* Опубликовано 12 ноября 2020 г.",
    "To fully automate the monitoring of your operating systems, processes, and network interfaces, Dynatrace requires privileged access to your operating system during both installation and operation.": "Для полной автоматизации мониторинга ваших операционных систем, процессов и сетевых интерфейсов Dynatrace требуется привилегированный доступ к вашей операционной системе как во время установки, так и во время эксплуатации.",
    'OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").': 'OneAgent проходит обширное тестирование, чтобы гарантировать минимальное влияние на производительность вашей системы и [соответствие высочайшим стандартам безопасности](/managed/manage/data-privacy-and-security "Узнайте, как Dynatrace применяет различные меры безопасности, необходимые для защиты приватных данных.").',
    "## Permissions": "## Разрешения",
    "OneAgent requires admin privileges on Windows, for both installation and operation.": "OneAgent требует прав администратора на Windows как для установки, так и для эксплуатации.",
    "### Installation": "### Установка",
    "OneAgent installer requires admin privileges to:": "Установщику OneAgent требуются права администратора, чтобы:",
    "* Create the OneAgent service.": "* Создать службу OneAgent.",
    "* Modify certain registry keys.": "* Изменять определённые ключи реестра.",
    '* Install packet capture driver (Npcap or WinPcap) for network metrics collection. For more information, see [Packet capture driver (pcap)](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Learn how to use the OneAgent installer for Windows.").': '* Установить драйвер захвата пакетов (Npcap или WinPcap) для сбора сетевых метрик. Дополнительные сведения см. в [Драйвер захвата пакетов (pcap)](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.").',
    '* Install [oneagentmon device](/managed/discover-dynatrace/get-started/glossary#o "Get acquainted with Dynatrace terminology.").': '* Установить [устройство oneagentmon](/managed/discover-dynatrace/get-started/glossary#o "Познакомьтесь с терминологией Dynatrace.").',
    "### Operation": "### Эксплуатация",
    "OneAgent requires admin privileges to:": "OneAgent требуются права администратора, чтобы:",
    "* List all processes.": "* Получать список всех процессов.",
    "* Get memory statistics for all processes.": "* Получать статистику памяти для всех процессов.",
    "* Read each process command line and environment.": "* Читать командную строку и окружение каждого процесса.",
    "* View the descriptions of executable files.": "* Просматривать описания исполняемых файлов.",
    "* Read application configuration for Apache and IIS": "* Читать конфигурацию приложений для Apache и IIS",
    "* View the list of libraries loaded for each process.": "* Просматривать список библиотек, загруженных для каждого процесса.",
    "* Read Windows registry keys.": "* Читать ключи реестра Windows.",
    "* Read .NET application domain for .NET 2.0, 3.0, and 3.5.": "* Читать домен приложений .NET для .NET 2.0, 3.0 и 3.5.",
    "* Start monitoring network traffic.": "* Запускать мониторинг сетевого трафика.",
    "* Parse executables for Go Discovery.": "* Анализировать исполняемые файлы для Go Discovery.",
    "* Gather monitoring data related to Docker containers.": "* Собирать данные мониторинга, связанные с контейнерами Docker.",
    "## Operating system changes": "## Изменения операционной системы",
    "OneAgent performs the following changes to your system:": "OneAgent вносит в вашу систему следующие изменения:",
    "OneAgent installer modifies the following aspects of your system:": "Установщик OneAgent изменяет следующие аспекты вашей системы:",
    '* Starting with version 1.195, no user account is created to run OneAgent extensions. Instead, the `NT AUTHORITY\\SYSTEM` privileged system account is used. For more information, see [OneAgent extension user](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Learn how to use the OneAgent installer for Windows.").': '* Начиная с версии 1.195, для запуска расширений OneAgent не создаётся учётная запись пользователя. Вместо этого используется привилегированная системная учётная запись `NT AUTHORITY\\SYSTEM`. Дополнительные сведения см. в [Пользователь расширений OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#oneagent-extension-user "Узнайте, как использовать установщик OneAgent для Windows.").',
    "* The `Dynatrace OneAgent` service is created.": "* Создаётся служба `Dynatrace OneAgent`.",
    "* The Dynatrace OneAgent program is registered with Windows Installer.": "* Программа Dynatrace OneAgent регистрируется в Windows Installer.",
    "* `oneagentmon` driver is installed and `OneAgentMon` device is created. It's required to enable automatic injection into processes.": "* Устанавливается драйвер `oneagentmon` и создаётся устройство `OneAgentMon`. Это необходимо для включения автоматической инъекции в процессы.",
    "* Registry sub-trees are created:": "* Создаются поддеревья реестра:",
    "* [Troubleshooting: Network Agent initialization failure on Windows](https://dt-url.net/7c438ee)": "* [Устранение неполадок: сбой инициализации Network Agent на Windows](https://dt-url.net/7c438ee)",
    "* The `Npcap` driver is installed with the `/admin_only` flag set, which restricts Npcap's packet reading and writing to users with Administrator privileges only. Unprivileged users can't access Npcap's functionality on a monitored host. Note that WinPcap doesn't offer this restriction. For more information, see [Customize OneAgent installation on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver \"Learn how to use the OneAgent installer for Windows.\").": '* Драйвер `Npcap` устанавливается с установленным флагом `/admin_only`, который ограничивает чтение и запись пакетов Npcap только пользователями с правами администратора. Непривилегированные пользователи не могут получить доступ к функциональности Npcap на мониторируемом хосте. Обратите внимание, что WinPcap не предлагает такого ограничения. Дополнительные сведения см. в [Настройка установки OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#packet_capture_driver "Узнайте, как использовать установщик OneAgent для Windows.").',
    "  Make sure these Npcap and WinPcap operations are permitted in your system's security settings:": "  Убедитесь, что следующие операции Npcap и WinPcap разрешены в настройках безопасности вашей системы:",
    "  + **Npcap:** Writing registry values to `SYSTEM\\CurrentControlSet\\Services\\npcap`": "  + **Npcap:** Запись значений реестра в `SYSTEM\\CurrentControlSet\\Services\\npcap`",
    "  + **Npcap:** Reading and writing registry values to `SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\NpcapInst`": "  + **Npcap:** Чтение и запись значений реестра в `SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\NpcapInst`",
    "  + **Winpcap:** Reading and writing registry values to `SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\WinPcapInst` and `SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\WinPcapInst`": "  + **Winpcap:** Чтение и запись значений реестра в `SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\WinPcapInst` и `SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\WinPcapInst`",
    "  + **Npcap and Winpcap:** Loading `wpcap.dll` and `packet.dll` located in `C:\\WINDOWS\\system32\\Npcap` / `C:\\WINDOWS\\system32\\WinPcap`": "  + **Npcap and Winpcap:** Загрузка `wpcap.dll` и `packet.dll`, расположенных в `C:\\WINDOWS\\system32\\Npcap` / `C:\\WINDOWS\\system32\\WinPcap`",
    "  + **Npcap and Winpcap:** Reading registry values regarding present network interfaces in [`SYSTEM\\CurrentControlSet\\Control\\Network\\{Network-Service-GUID}`](https://dt-url.net/lz036sy)\\*": "  + **Npcap and Winpcap:** Чтение значений реестра о текущих сетевых интерфейсах в [`SYSTEM\\CurrentControlSet\\Control\\Network\\{Network-Service-GUID}`](https://dt-url.net/lz036sy)\\*",
    "## Files added": "## Добавленные файлы",
    "OneAgents installer adds the following files to your system:": "Установщик OneAgent добавляет в вашу систему следующие файлы:",
    '* OneAgent binaries and configuration files are saved in `%PROGRAMFILES%\\dynatrace\\oneagent`. Note that you can change the location using the [INSTALL\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") parameter.': '* Бинарные и конфигурационные файлы OneAgent сохраняются в `%PROGRAMFILES%\\dynatrace\\oneagent`. Обратите внимание, что расположение можно изменить с помощью параметра [INSTALL\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Узнайте, как использовать установщик OneAgent для Windows.").',
    "* Installer temporary files are saved in `C:\\AI_RecycleBin`. The folder is deleted after the installation is complete.": "* Временные файлы установщика сохраняются в `C:\\AI_RecycleBin`. Папка удаляется после завершения установки.",
    "* OneAgent temporary files and runtime configuration are saved in `%PROGRAMDATA%\\dynatrace\\oneagent\\runtime`.": "* Временные файлы OneAgent и конфигурация времени выполнения сохраняются в `%PROGRAMDATA%\\dynatrace\\oneagent\\runtime`.",
    "* OneAgent persistent configuration is saved in `%PROGRAMDATA%\\dynatrace\\oneagent\\config`.": "* Постоянная конфигурация OneAgent сохраняется в `%PROGRAMDATA%\\dynatrace\\oneagent\\config`.",
    '* Large runtime data, such as memory dumps, is saved in `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage`. Note that you can change the location of large runtime data using the [DATA\\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") parameter.': '* Крупные данные времени выполнения, такие как дампы памяти, сохраняются в `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage`. Обратите внимание, что расположение крупных данных времени выполнения можно изменить с помощью параметра [DATA\\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Узнайте, как использовать установщик OneAgent для Windows.").',
    "## System logs downloaded by OneAgent": "## Системные логи, скачиваемые OneAgent",
    "OneAgent downloads Security, System, and Application system logs from the last 14 days so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or automatic updates.": "OneAgent скачивает системные логи Security, System и Application за последние 14 дней, чтобы Dynatrace мог диагностировать проблемы, которые могут быть вызваны условиями в вашем окружении. Чаще всего такие проблемы связаны с глубоким мониторингом или автоматическими обновлениями.",
    "Revoking access to system logs": "Отзыв доступа к системным логам",
    "To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.": "Чтобы отозвать доступ к системным логам, используйте команду `oneagentctl` с параметром `--set-system-logs-access-enabled`, установленным в `false`.",
    'For more information, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")': 'Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.")',
    "## Globally writable directories": "## Глобально доступные для записи каталоги",
    'The [OneAgent directory structure](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") contains globally writable directories (directories where the `Everyone` user group can write, modify, or execute). Changing these permissions by users is not supported.': '[Структура каталогов OneAgent](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.") содержит глобально доступные для записи каталоги (каталоги, в которые группа пользователей `Everyone` может записывать, изменять или выполнять). Изменение этих прав пользователями не поддерживается.',
    "### OneAgent injection mechanism": "### Механизм инъекции OneAgent",
    "Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.": "Такие права на выбранном наборе каталогов необходимы для успешной инъекции OneAgent в процессы на мониторируемых хостах. Когда OneAgent внедряется в процесс, кодовый модуль, отвечающий за инъекцию, выполняется в контексте исходного процесса, в который произошла инъекция. Следовательно, пользователям, под которыми запускаются эти процессы, должно быть разрешено выполнять запись в структуру каталогов OneAgent, что и является причиной глобальных прав на запись, которые делают это возможным.",
    "Similarly, certain log files require global write permissions to allow applications running under various users to write to them.": "Аналогично, некоторым файлам логов требуются глобальные права на запись, чтобы приложения, работающие под разными пользователями, могли в них писать.",
    "### System security": "### Безопасность системы",
    "We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.": "Нам известно, что глобальные права на чтение и запись для каталогов OneAgent помечаются эвристиками сканеров безопасности, но мы можем заверить вас, что они полностью безопасны.",
    "* We keep the number of globally writable directories as limited as possible.": "* Мы держим количество глобально доступных для записи каталогов настолько ограниченным, насколько это возможно.",
    "* We leverage advanced file permissions and use the `Creator Owner` permission to limits access to files.": "* Мы используем расширенные права доступа к файлам и применяем разрешение `Creator Owner` для ограничения доступа к файлам.",
    "## Installer signing": "## Подписывание установщика",
    "The OneAgent installer is signed against one or more [DigiCert root certificates](https://www.digicert.com/kb/digicert-root-certificates.htm). For regularly maintained systems, Windows verifies that the OneAgent installer has been published by a verified publisher.": "Установщик OneAgent подписан одним или несколькими [корневыми сертификатами DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm). На регулярно обслуживаемых системах Windows проверяет, что установщик OneAgent был опубликован проверенным издателем.",
    "If your Windows-based system has been offline since March 2021 or longer, Windows won't be able to verify the installer and the OneAgent installer publisher will appear as **Unknown publisher** when you attempt an installation or update. In such a case, you need to download the latest certificate from [DigiCert root certificates](https://www.digicert.com/kb/digicert-root-certificates.htm) and add it to your system. Among all the DigiCert certificates, the `DigiCert Global Root G3` is mandatory for successful verification of the OneAgent installer.": "Если ваша система на базе Windows находилась офлайн с марта 2021 года или дольше, Windows не сможет проверить установщик, и издатель установщика OneAgent будет отображаться как **Unknown publisher** при попытке установки или обновления. В таком случае необходимо скачать последний сертификат с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm) и добавить его в вашу систему. Среди всех сертификатов DigiCert сертификат `DigiCert Global Root G3` обязателен для успешной проверки установщика OneAgent.",
    "* See [How to: View certificates with the MMC snap-in](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) in Microsoft docs to learn which root certificates are installed in your system.": "* См. [Как просмотреть сертификаты с помощью оснастки MMC](https://docs.microsoft.com/en-us/dotnet/framework/wcf/feature-details/how-to-view-certificates-with-the-mmc-snap-in) в документации Microsoft, чтобы узнать, какие корневые сертификаты установлены в вашей системе.",
    "* Download the latest root certificates from [DigiCert root certificates](https://www.digicert.com/kb/digicert-root-certificates.htm).": "* Скачайте последние корневые сертификаты с [корневых сертификатов DigiCert](https://www.digicert.com/kb/digicert-root-certificates.htm).",
    "### Windows 2008 R2": "### Windows 2008 R2",
    "Starting with OneAgent version 1.225, the installer is signed using the SHA-2 algorithm. Consequently, Windows 2008 R2 hosts are required to have SHA-2 code signing support installed. If you use Windows Update, the updates were offered to you automatically (KB4474419 and KB4490628). If, however, your Windows 2008 R2 system doesn't support verifying SHA-2 signed installers, OneAgent auto-update and installation won't work if `Applocker` is configured to block unknown publishers and/or security warnings may be displayed. For more information, see the Microsoft [2019 SHA-2 Code Signing Support requirement for Windows and WSUS](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f) announcement.": "Начиная с OneAgent версии 1.225, установщик подписывается с использованием алгоритма SHA-2. Следовательно, на хостах Windows 2008 R2 должна быть установлена поддержка подписывания кода SHA-2. Если вы используете Windows Update, обновления были предложены вам автоматически (KB4474419 и KB4490628). Однако если ваша система Windows 2008 R2 не поддерживает проверку установщиков, подписанных SHA-2, автообновление и установка OneAgent не будут работать, если `Applocker` настроен на блокировку неизвестных издателей, и/или могут отображаться предупреждения безопасности. Дополнительные сведения см. в объявлении Microsoft [Требование поддержки подписывания кода SHA-2 2019 для Windows и WSUS](https://support.microsoft.com/en-us/topic/2019-sha-2-code-signing-support-requirement-for-windows-and-wsus-64d1c82d-31ee-c273-3930-69a4cde8e64f).",
}


# ---------------- disk-space ----------------
DISK = {
    "title: OneAgent files and disk space requirements on Windows": "title: Файлы OneAgent и требования к дисковому пространству на Windows",
    "# OneAgent files and disk space requirements on Windows": "# Файлы OneAgent и требования к дисковому пространству на Windows",
    "* 4-min read": "* Чтение: 4 мин",
    "* Updated on Jun 25, 2025": "* Обновлено 25 июня 2025 г.",
    "This page provides information about the OneAgent directory structure and disk space requirements for OneAgent full-stack installation and updates. Note that exact values may vary based on OneAgent version.": "Эта страница содержит информацию о структуре каталогов OneAgent и требованиях к дисковому пространству для full-stack установки и обновлений OneAgent. Обратите внимание, что точные значения могут различаться в зависимости от версии OneAgent.",
    "## Full-stack and Infrastructure Monitoring mode": "## Режим Full-stack и Infrastructure Monitoring",
    "The same disk space requirements apply to both Full-stack and Infrastructure monitoring modes.": "Одни и те же требования к дисковому пространству применяются как к режиму Full-stack, так и к режиму Infrastructure monitoring.",
    "## OneAgent directories and their sizes": "## Каталоги OneAgent и их размеры",
    "|  |  | Default directory | Can be modified? |": "|  |  | Каталог по умолчанию | Можно изменить? |",
    "| Size of installation (with temporary installation files removed) | ~775 MB | `%PROGRAMFILES%\\dynatrace\\oneagent` | Yes [1](#fn-1-1-def) |": "| Размер установки (с удалёнными временными файлами установки) | ~775 МБ | `%PROGRAMFILES%\\dynatrace\\oneagent` | Да [1](#fn-1-1-def) |",
    "| Persistent configuration | ~10 MB | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config` | No |": "| Постоянная конфигурация | ~10 МБ | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\config` | Нет |",
    "| Temporary files, runtime configuration | 200 MB | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\runtime` | No |": "| Временные файлы, конфигурация времени выполнения | 200 МБ | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\runtime` | Нет |",
    "| Logs | 1 GB | `%PROGRAMDATA%\\dynatrace\\oneagent\\log` | Yes [2](#fn-1-2-def) |": "| Логи | 1 ГБ | `%PROGRAMDATA%\\dynatrace\\oneagent\\log` | Да [2](#fn-1-2-def) |",
    "| Crash reports, memory dumps | 3 GB | `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage` | Yes [3](#fn-1-3-def) |": "| Отчёты о сбоях, дампы памяти | 3 ГБ | `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage` | Да [3](#fn-1-3-def) |",
    "| Log analytics persistence | ~1 GB [4](#fn-1-4-def) | `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage\\loganalytics` | Yes [3](#fn-1-3-def) |": "| Хранение данных Log analytics | ~1 ГБ [4](#fn-1-4-def) | `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage\\loganalytics` | Да [3](#fn-1-3-def) |",
    "| EEC logs retransmission persistence file | 600 MB + 1.5 GB buffer | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\runtime\\extensions\\persistence` | Yes [5](#fn-1-5-def) [6](#fn-1-6-def) |": "| Файл хранения данных для повторной передачи логов EEC | 600 МБ + 1,5 ГБ буфер | `%PROGRAMDATA%\\dynatrace\\oneagent\\agent\\runtime\\extensions\\persistence` | Да [5](#fn-1-5-def) [6](#fn-1-6-def) |",
    "| Additional space required for updates | ~3.4 GB | See [Space required for installation and updates](#updates) |  |": "| Дополнительное место, необходимое для обновлений | ~3,4 ГБ | См. [Место, необходимое для установки и обновлений](#updates) |  |",
    "| **Total** | **~11.5 GB** |  |  |": "| **Всего** | **~11,5 ГБ** |  |  |",
    'Use the [INSTALL\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Learn how to use the OneAgent installer for Windows.") installation parameter.': 'Используйте параметр установки [INSTALL\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#installation-path "Узнайте, как использовать установщик OneAgent для Windows.").',
    'Use the [LOG\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#log-path "Learn how to use the OneAgent installer for Windows.") installation parameter.': 'Используйте параметр установки [LOG\\_PATH](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#log-path "Узнайте, как использовать установщик OneAgent для Windows.").',
    'Use the [DATA\\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows.") installation parameter.': 'Используйте параметр установки [DATA\\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Узнайте, как использовать установщик OneAgent для Windows.").',
    "The size depends on the number of ingested logs.": "Размер зависит от количества принятых логов.",
    'Applicable only if you use Dynatrace Extensions that [define the log metrics, events, or add their own log processing rules](/managed/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Learn how to instrument your extensions to customize how the ingested data is handled by Dynatrace."). Can be changed via support request.': 'Применимо только если вы используете Dynatrace Extensions, которые [определяют метрики логов, события или добавляют свои правила обработки логов](/managed/ingest-from/extensions/advanced-configuration/extension-customize#log-metrics-events-and-processing-rules "Узнайте, как инструментировать ваши расширения, чтобы настроить обработку принимаемых данных в Dynatrace."). Может быть изменено через запрос в поддержку.',
    "The reliability mechanism does not work if the requirement is not met. For more information, see [Persistence details](#persistence).": "Механизм надёжности не работает, если требование не выполнено. Подробнее см. [Подробности хранения данных](#persistence).",
    'For a complete list of files and directories added to your system by OneAgent, see [OneAgent security on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Learn about Dynatrace OneAgent security and modifications to your Windows-based system").': 'Полный список файлов и каталогов, добавляемых OneAgent в вашу систему, см. в [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows").',
    "## OneAgent files aging mechanism": "## Механизм устаревания файлов OneAgent",
    'OneAgent in full-stack monitoring mode uses a built-in aging mechanism to ensure that the OneAgent files, including log files and runtime data, are kept within a reasonable size. For more information, see [OneAgent file aging mechanism](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage.").': 'OneAgent в режиме full-stack monitoring использует встроенный механизм устаревания для того, чтобы файлы OneAgent, включая файлы логов и данные времени выполнения, оставались в пределах разумного размера. Подробнее см. [Механизм устаревания файлов OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Узнайте, как OneAgent удаляет старые файлы для минимизации использования дискового пространства.").',
    "## Space required for updates": "## Место, необходимое для обновлений",
    "When calculating the space required for updates, we take into account the compressed EXE installer file size, the extracted MSI package, and the size of the installation process (the space required to deploy OneAgent files).": "При расчёте места, необходимого для обновлений, мы учитываем размер сжатого EXE-установщика, распакованный MSI-пакет и размер процесса установки (место, необходимое для развёртывания файлов OneAgent).",
    "|  | Size | Description | Removed after | Claimed by | Path |": "|  | Размер | Описание | Удаляется после | Кем занято | Путь |",
    "| 1 | ~130 MB | EXE installer downloaded by AutoUpdate | OneAgent restart or next version installed [1](#fn-2-1-def) | AutoUpdate | `%PROGRAMDATA%\\dynatrace\\oneagent` |": "| 1 | ~130 МБ | EXE-установщик, скачанный AutoUpdate | Перезапуск OneAgent или установка следующей версии [1](#fn-2-1-def) | AutoUpdate | `%PROGRAMDATA%\\dynatrace\\oneagent` |",
    "| 2 | ~750 MB | Extracted MSI installer | End of the installation | OneAgent Installation | `%PROGRAMDATA%\\dynatrace\\oneagent` |": "| 2 | ~750 МБ | Распакованный MSI-установщик | Конец установки | Установка OneAgent | `%PROGRAMDATA%\\dynatrace\\oneagent` |",
    "| 3 | ~750 MB | Extra storage for temporary installation files | End of the installation | OneAgent Installation | `%APPDATA%` |": "| 3 | ~750 МБ | Дополнительное хранилище для временных файлов установки | Конец установки | Установка OneAgent | `%APPDATA%` |",
    "| 4 | ~750 MB | Copy of the MSI installer saved by Windows | Next version installed | Windows installer | `%WINDIR%\\Installer` |": "| 4 | ~750 МБ | Копия MSI-установщика, сохранённая Windows | Установка следующей версии | Windows installer | `%WINDIR%\\Installer` |",
    "| 5 | ~750 MB | Installed files | Next version installed | OneAgent Installation | `[Installation path]` |": "| 5 | ~750 МБ | Установленные файлы | Установка следующей версии | Установка OneAgent | `[Installation path]` |",
    "| Σ | ~3130 MB |  |  |  |  |": "| Σ | ~3130 МБ |  |  |  |  |",
    "If you download the EXE installer manually, the installation process won't remove it.": "Если вы скачиваете EXE-установщик вручную, процесс установки не будет его удалять.",
    "Additional space required for installation and updates is calculated using the 10% safety margin:": "Дополнительное место, необходимое для установки и обновлений, рассчитывается с запасом 10%:",
    "`(size of the installation process [2+3+4+5] + installer files size [1]) * 1.1`": "`(размер процесса установки [2+3+4+5] + размер файлов установщика [1]) * 1.1`",
    "Required disk space for OneAgent installation and update on a single drive is ~3.4 GB calculated using this formula.": "Необходимое дисковое пространство для установки и обновления OneAgent на одном диске составляет ~3,4 ГБ согласно этой формуле.",
    "Note that the EXE installer is compressed, which explains the difference in size in comparison to the MSI installer.": "Обратите внимание, что EXE-установщик сжат, что объясняет разницу в размере по сравнению с MSI-установщиком.",
    "In terms of space requirements, there's no real difference between manual installation of the new version (when an older version is already installed), automatic update, and updates that are triggered by restarting the OneAgent container. In all these cases, the installation process is performed exactly the same way. What differs is the method through which the update is triggered.": "С точки зрения требований к дисковому пространству нет реальной разницы между ручной установкой новой версии (когда уже установлена более старая версия), автоматическим обновлением и обновлениями, запускаемыми перезапуском контейнера OneAgent. Во всех этих случаях процесс установки выполняется одинаково. Различается только метод запуска обновления.",
    "## Persistence details": "## Подробности хранения данных",
    "The reliability mechanism ensures the persistence of Extension Execution Controller (EEC) logs in case ActiveGate or OneAgent is unavailable, there are network problems, or EEC experiences a data ingest overload. This minimizes gaps in log coverage.": "Механизм надёжности обеспечивает хранение логов Extension Execution Controller (EEC) на случай недоступности ActiveGate или OneAgent, проблем с сетью или перегрузки EEC при приёме данных. Это минимизирует пробелы в покрытии логами.",
    "### General information": "### Общая информация",
    "* Persistent storage of data requires 2136 MB of free disk space:": "* Постоянное хранение данных требует 2136 МБ свободного дискового пространства:",
    "  + 600 MB of free disk space to be used by the reliability mechanism": "  + 600 МБ свободного дискового пространства для использования механизмом надёжности",
    "  + 1.5 GB of free disk space to be used as a buffer": "  + 1,5 ГБ свободного дискового пространства для использования в качестве буфера",
    "* The requirement is checked periodically, and if not met, the persistence will be turned off and log ingestion will be transmitted without the reliability mechanism.": "* Требование проверяется периодически, и если оно не выполняется, хранение данных будет отключено, а приём логов будет передаваться без механизма надёжности.",
    "* The volume is used proportionally to the load of logs ingest.": "* Объём используется пропорционально нагрузке приёма логов.",
    "* If the requirement can't be met on the host, you can modify the configuration of logs persistence. For more information, see [Persistence configuration](#persistence_config).": "* Если требование не может быть выполнено на хосте, можно изменить конфигурацию хранения логов. Подробнее см. [Конфигурация хранения данных](#persistence_config).",
    "### Configuration": "### Конфигурация",
    "Windows configuration file: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\extensionsuser.conf`": "Файл конфигурации для Windows: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\extensionsuser.conf`",
    "Linux configuration file: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`": "Файл конфигурации для Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`",
    "| **Variable** | **Description** |": "| **Переменная** | **Описание** |",
    "| `persistence.reliable_mode` | `true` - reliable mode turned on; SFM logs genereted if space requirement not met `false` - reliable mode turned off; log ingest will be transmitted without the reliability mechanism |": "| `persistence.reliable_mode` | `true` - надёжный режим включён; SFM-логи генерируются, если требование к месту не выполнено `false` - надёжный режим отключён; приём логов будет передаваться без механизма надёжности |",
    "| `persistence.total_limit_kb` | Maximum volume limit for Extensions Log Persistence in kilobytes. By default: 600 MB Can be modified manually if the requirement can't be met on the host. |": "| `persistence.total_limit_kb` | Максимальный лимит объёма для Extensions Log Persistence в килобайтах. По умолчанию: 600 МБ Может быть изменён вручную, если требование не может быть выполнено на хосте. |",
}


CUSTOMIZE = {
    "title: Customize OneAgent installation on Windows": "title: Настройка установки OneAgent на Windows",
    "# Customize OneAgent installation on Windows": "# Настройка установки OneAgent на Windows",
    "* Updated on Jan 21, 2026": "* Обновлено 21 января 2026 г.",
    "* 9-min read": "* Чтение: 9 мин",
    "### Command line": "### Командная строка",
    "### Changing location": "### Изменение расположения",
    "For example:": "Например:",
    "## Silent installation": "## Тихая установка",
    "#### Command shell": "#### Командная оболочка",
    "**Possible values:**": "**Возможные значения:**",
    "OneAgent version 1.229+": "OneAgent версии 1.229+",
    "**Default value**: `%PROGRAMFILES%\\dynatrace\\oneagent`": "**Значение по умолчанию**: `%PROGRAMFILES%\\dynatrace\\oneagent`",
    "**Default value**: `%PROGRAMDATA%\\dynatrace\\oneagent\\log`": "**Значение по умолчанию**: `%PROGRAMDATA%\\dynatrace\\oneagent\\log`",
    "**Default value**: `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage`": "**Значение по умолчанию**: `%PROGRAMDATA%\\dynatrace\\oneagent\\datastorage`",
    "**Default value**: `npcap`": "**Значение по умолчанию**: `npcap`",
    "The **Default value**: `LocalSystem` (OneAgent version 1.195+)": "**Значение по умолчанию**: `LocalSystem` (OneAgent версии 1.195+)",
    'OneAgent installer for Windows is provided and used as a self-extracting EXE file. The installer can also be extracted and used directly—as an MSI package. This later approach is mostly used in [Group Policy deployment](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Learn how to download and install Dynatrace OneAgent on Windows.").': 'Установщик OneAgent для Windows предоставляется и используется в виде самораспаковывающегося EXE-файла. Установщик также можно распаковать и использовать напрямую: в виде MSI-пакета. Этот второй подход чаще всего используется при [развёртывании через групповые политики](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Узнайте, как скачать и установить Dynatrace OneAgent на Windows.").',
    "You can customize the installation by specifying command-line parameters for selected settings, or you can rely on default settings.": "Установку можно настроить, указав параметры командной строки для выбранных настроек, либо положиться на настройки по умолчанию.",
    "However, note that parameters marked below as `environment-specific`—that is, parameters that set the communication endpoint, environment ID, and token—are:": "Однако обратите внимание, что параметры, помеченные ниже как `environment-specific` (то есть параметры, задающие эндпоинт связи, идентификатор окружения и токен), являются:",
    "* pre-configured only for the EXE version of the installer.": "* предварительно настроены только для EXE-версии установщика.",
    "  Therefore, when using the installer as and MSI package, you must specify these parameters explicitly.": "  Поэтому при использовании установщика в виде MSI-пакета эти параметры необходимо указывать явно.",
    "For example, for the EXE version of the installer:": "Например, для EXE-версии установщика:",
    'When using the installer as an MSI package, you can directly append only the `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER`, and `SKIP_OS_SUPPORT_CHECK` parameters. This type of installation is usually run in silent mode, as part of [Group Policy deployment](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Learn how to download and install Dynatrace OneAgent on Windows."). The `--set-param=<value>` has to be placed inside of `ADDITIONAL_CONFIGURATION` (`ADDITIONAL_CONFIGURATION="--set-param=<value>"`).': 'При использовании установщика в виде MSI-пакета напрямую можно добавлять только параметры `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER` и `SKIP_OS_SUPPORT_CHECK`. Этот тип установки обычно выполняется в тихом режиме, в рамках [развёртывания через групповые политики](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#installation "Узнайте, как скачать и установить Dynatrace OneAgent на Windows."). `--set-param=<value>` необходимо помещать внутри `ADDITIONAL_CONFIGURATION` (`ADDITIONAL_CONFIGURATION="--set-param=<value>"`).',
    "For more information on command-line syntax, see [Silent installation](#silent-installation).": "Дополнительные сведения о синтаксисе командной строки см. в [Тихая установка](#silent-installation).",
    "You can also add the `--set-param=<value>` parameters in the **Configure OneAgent settings** installation screen.": "Параметры `--set-param=<value>` можно также добавить на экране установки **Configure OneAgent settings**.",
    "![OneAgent windows customize](https://dt-cdn.net/images/windows-customize-495-ec2f24e000.png)": "![Настройка OneAgent для Windows](https://dt-cdn.net/images/windows-customize-495-ec2f24e000.png)",
    "OneAgent windows customize": "Настройка OneAgent для Windows",
    "Parameters supported by the installer UI": "Параметры, поддерживаемые интерфейсом установщика",
    "The UI of the OneAgent installer for Windows supports only the `--set-param=<value>` parameters.": "Интерфейс установщика OneAgent для Windows поддерживает только параметры `--set-param=<value>`.",
    "The following parameters are NOT supported by the installer UI: `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER`, and `SKIP_OS_SUPPORT_CHECK`.": "Следующие параметры НЕ поддерживаются интерфейсом установщика: `INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER`, `USER` и `SKIP_OS_SUPPORT_CHECK`.",
    "Starting with version 1.213, the following parameters are only accepted if specified using the `--set-param=<value>` syntax. For these specific parameters, the equivalent `PARAM=<value>` syntax is no longer supported:": "Начиная с версии 1.213, следующие параметры принимаются только если указаны с использованием синтаксиса `--set-param=<value>`. Для этих конкретных параметров эквивалентный синтаксис `PARAM=<value>` больше не поддерживается:",
    "## MSI installation parameters": "## Параметры установки MSI",
    "`INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER` and `USER` are a special kind of parameter adhering to [MSI public property syntax](https://docs.microsoft.com/en-us/windows/win32/msi/public-properties). They won't be replaced by equivalent `--set-param=<value>` parameters. You can use them only on the installer command line, not in the installer UI.": "`INSTALL_PATH`, `LOG_PATH`, `DATA_STORAGE`, `PCAP_DRIVER` и `USER` представляют собой особый вид параметров, соответствующих [синтаксису публичных свойств MSI](https://docs.microsoft.com/en-us/windows/win32/msi/public-properties). Они не будут заменены эквивалентными параметрами `--set-param=<value>`. Использовать их можно только в командной строке установщика, но не в интерфейсе установщика.",
    "## Installation path": "## Путь установки",
    "The **`INSTALL_PATH`** parameter allows OneAgent installation to a directory of your choice.": "Параметр **`INSTALL_PATH`** позволяет установить OneAgent в выбранный вами каталог.",
    "This parameter is not supported by the installer UI.": "Этот параметр не поддерживается интерфейсом установщика.",
    'The `INSTALL_PATH` parameter doesn\'t control the OneAgent [log and configuration files](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Windows.") directories. To customize the log path, use the `LOG_PATH` parameter.': 'Параметр `INSTALL_PATH` не управляет каталогами [файлов логов и конфигурации](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows "Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Windows.") OneAgent. Чтобы настроить путь к логам, используйте параметр `LOG_PATH`.',
    "Make sure that your custom installation path meets the following requirements:": "Убедитесь, что путь к вашему пользовательскому каталогу установки соответствует следующим требованиям:",
    "* The value must not be a child directory of `%PROGRAMDATA%\\dynatrace`.": "* Значение не должно быть дочерним каталогом `%PROGRAMDATA%\\dynatrace`.",
    "## Log path": "## Путь к логам",
    "The **`LOG_PATH`** parameter allows you to customize your OneAgent log directory.": "Параметр **`LOG_PATH`** позволяет настроить каталог логов OneAgent.",
    "* After you set or change the `LOG_PATH` parameter, you must restart deep-monitored processes so that OneAgents monitoring them can pick up the new path to store logs. You will be notified to restart a corresponding process on the **Process overview** page.": "* После установки или изменения параметра `LOG_PATH` необходимо перезапустить процессы с глубоким мониторингом, чтобы наблюдающие за ними OneAgent восприняли новый путь для хранения логов. Вы получите уведомление о необходимости перезапустить соответствующий процесс на странице **Process overview**.",
    "### Custom directory requirements": "### Требования к пользовательскому каталогу",
    "Make sure that your custom data storage path meets the following requirements:": "Убедитесь, что путь к вашему пользовательскому каталогу хранения данных соответствует следующим требованиям:",
    "* The directory must be dedicated to OneAgent purposes only. No other software can have access to it. One reason is security, while the other is automatic cleanup performed periodically by OneAgent, which could remove files created by other applications.": "* Каталог должен использоваться исключительно для нужд OneAgent. Никакое другое программное обеспечение не должно иметь к нему доступа. Одна причина связана с безопасностью, другая с автоматической очисткой, периодически выполняемой OneAgent, которая может удалить файлы, созданные другими приложениями.",
    "* You must not share or nest in one another the [installation](#installation-path), [storage](#data-storage), and [log](#log-path) directories.": "* Нельзя делать общими или вкладывать друг в друга каталоги [установки](#installation-path), [хранилища](#data-storage) и [логов](#log-path).",
    "* The value must be an absolute path and must not point to the root volume directory.": "* Значение должно быть абсолютным путём и не должно указывать на каталог корневого тома.",
    "If you use the parameter to change the location for an already installed OneAgent:": "Если вы используете этот параметр, чтобы изменить расположение для уже установленного OneAgent:",
    "* Existing files are not migrated to the new location": "* Существующие файлы не переносятся в новое расположение",
    "* After you set or change the `DATA_STORAGE` parameter, you must restart deep-monitored processes, so that OneAgents monitoring them can pick up the new path to store runtime data. Otherwise, memory dumps and other runtime data won't be saved. You will be notified to restart a corresponding process on the **Process overview** page.": "* После установки или изменения параметра `DATA_STORAGE` необходимо перезапустить процессы с глубоким мониторингом, чтобы наблюдающие за ними OneAgent могли применить новый путь для хранения данных времени выполнения. Иначе дампы памяти и другие данные времени выполнения не будут сохраняться. На странице **Process overview** вы получите уведомление о необходимости перезапустить соответствующий процесс.",
    "OneAgent can download system logs for the purpose of diagnosing issues that may be caused by conditions in your environment. OneAgent doesn't currently download any Windows system logs, but this can change in future releases.": "OneAgent может скачивать системные логи с целью диагностики проблем, которые могут быть вызваны условиями в вашем окружении. В настоящее время OneAgent не скачивает никаких системных логов Windows, но это может измениться в будущих релизах.",
    "`--set-system-logs-access-enabled=false` disables access to logs": "`--set-system-logs-access-enabled=false` отключает доступ к логам",
    "`--set-system-logs-access-enabled=true` enables access to logs": "`--set-system-logs-access-enabled=true` включает доступ к логам",
    "Note that this is a self-diagnostics setting that is not related to [Log Monitoring](#log-monitoring).": "Обратите внимание, что это настройка самодиагностики, не связанная с [Log Monitoring](#log-monitoring).",
    "## OneAgent extension user": "## Пользователь расширений OneAgent",
    'Use the **`USER`** parameter to define the user running the process responsible for [Dynatrace extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") functionality. For example:': 'Используйте параметр **`USER`**, чтобы определить пользователя, от имени которого выполняется процесс, отвечающий за функциональность [Dynatrace extensions](/managed/ingest-from/extensions "Узнайте, как создавать расширения Dynatrace и управлять ими."). Например:',
    "If you don't add the `USER` parameter:": "Если вы не добавляете параметр `USER`:",
    "* For fresh OneAgent 1.195+ installations, the default `LocalSystem` account will be used to run OneAgent extensions, but Python extensions will be spawned as `LocalService`.": "* Для новых установок OneAgent 1.195+ для запуска расширений OneAgent будет использоваться учётная запись `LocalSystem` по умолчанию, но Python-расширения будут запускаться как `LocalService`.",
    "* For fresh OneAgent deployments prior to version 1.195, OneAgent will use the `dtuser` account.": "* Для новых развёртываний OneAgent до версии 1.195 OneAgent будет использовать учётную запись `dtuser`.",
    "* Updating the OneAgent preserves the previously configured user account. To change it, you must reinstall OneAgent setting the `USER` parameter to a new value.": "* При обновлении OneAgent ранее настроенная учётная запись пользователя сохраняется. Чтобы изменить её, необходимо переустановить OneAgent, задав параметру `USER` новое значение.",
    "The `USER` parameter can have one of the following values:": "Параметр `USER` может принимать одно из следующих значений:",
    "* Recommended `LocalSystem` is the default user account used to run OneAgent extensions starting with OneAgent version 1.195. Applied automatically when the `USER` parameter isn't used. This parameter value makes OneAgent use the `NT AUTHORITY\\SYSTEM` privileged system account to run OneAgent extensions. Effectively, no local user account is created. As a result, all OneAgent modules, including all extensions except Python extensions, are fully functional. Python extensions will run as `LocalService`.": "* Рекомендуется `LocalSystem`. Это учётная запись по умолчанию, используемая для запуска расширений OneAgent начиная с версии OneAgent 1.195. Применяется автоматически, когда параметр `USER` не используется. Это значение параметра заставляет OneAgent использовать привилегированную системную учётную запись `NT AUTHORITY\\SYSTEM` для запуска расширений OneAgent. Фактически локальная учётная запись пользователя не создаётся. В результате все модули OneAgent, включая все расширения, кроме Python-расширений, полностью функциональны. Python-расширения будут выполняться как `LocalService`.",
    "* `LocalService`: This parameter makes OneAgent use the `NT AUTHORITY\\LOCAL SERVICE` system account to run OneAgent extensions. While this reduced set of privileges is enough for most of the extensions to operate, there are some that won't be able to produce data effectively (namely, extensions that collect Performance Monitor counters, such as MS SQL or .NET extensions). If you're unsure about which extensions you might use, it's best to use the `LocalSystem` parameter value instead.": "* `LocalService`: это значение параметра заставляет OneAgent использовать системную учётную запись `NT AUTHORITY\\LOCAL SERVICE` для запуска расширений OneAgent. Хотя этого сокращённого набора привилегий достаточно для работы большинства расширений, есть и такие, которые не смогут эффективно выдавать данные (а именно расширения, собирающие счётчики Performance Monitor, такие как расширения MS SQL или .NET). Если вы не уверены, какие расширения будете использовать, лучше использовать значение параметра `LocalSystem`.",
    "* Deprecated `no_create` disabled user creation when installing OneAgent prior to OneAgent version 1.209. Starting with the version 1.209, when you use the `no_create` parameter, the OneAgent installer applies the `LocalSystem` parameter without any warning. The `no_create` setting is not converted to `LocalSystem` for existing installations when running an update. To convert, you must reinstall OneAgent setting the `USER` parameter to a new value.": "* Устарело `no_create` отключал создание пользователя при установке OneAgent до версии OneAgent 1.209. Начиная с версии 1.209, при использовании параметра `no_create` установщик OneAgent применяет параметр `LocalSystem` без какого-либо предупреждения. Настройка `no_create` не преобразуется в `LocalSystem` для существующих установок при выполнении обновления. Чтобы выполнить преобразование, необходимо переустановить OneAgent, задав параметру `USER` новое значение.",
    "* Deprecated `dtuser` was the default user account used to run OneAgent extensions prior to OneAgent version 1.195. It made the installer create a local user account with the same name in the system. Starting with the version 1.209, when you use the `dtuser` parameter, the OneAgent installer applies the `LocalSystem` parameter without any warning. Starting with OneAgent version 1.239, the `dtuser` setting is converted to `LocalSystem` for existing installations when running an update.": "* Устарело `dtuser` был учётной записью по умолчанию, используемой для запуска расширений OneAgent до версии OneAgent 1.195. Он заставлял установщик создавать в системе локальную учётную запись пользователя с тем же именем. Начиная с версии 1.209, при использовании параметра `dtuser` установщик OneAgent применяет параметр `LocalSystem` без какого-либо предупреждения. Начиная с версии OneAgent 1.239, настройка `dtuser` преобразуется в `LocalSystem` для существующих установок при выполнении обновления.",
    "When deploying Dynatrace on Windows Server Domain Controller, make sure the `USER` parameter is set to `LocalSystem`, or alternatively `LocalService`, to avoid propagation of `dtuser` across the domain, which can cause interference with existing `dtuser` accounts on hosts that have Dynatrace installed.": "При развёртывании Dynatrace на контроллере домена Windows Server убедитесь, что параметр `USER` установлен в `LocalSystem` или, как вариант, `LocalService`, чтобы избежать распространения `dtuser` по домену, что может вызвать конфликты с существующими учётными записями `dtuser` на хостах с установленным Dynatrace.",
    "When using the silent installation mode, the OneAgent installer should be pre-configured with appropriate parameter values, since interactive dialogs and prompts will not be displayed during installation.": "При использовании тихого режима установки установщик OneAgent следует предварительно настроить с соответствующими значениями параметров, так как интерактивные диалоги и запросы во время установки отображаться не будут.",
    "The environment specific parameters are preconfigured only for the EXE version of the installer. When using the installer in the form of an MSI package, you must specify all of these parameters yourself.": "Параметры environment specific предварительно настроены только для EXE-версии установщика. При использовании установщика в виде MSI-пакета все эти параметры необходимо указывать самостоятельно.",
    "### MSI package—silent installation": "### MSI-пакет: тихая установка",
    "### EXE installer—silent installation": "### EXE-установщик: тихая установка",
    "To set up silent command-line installation when using an MSI package, add `/quiet /qn` as in these examples:": "Чтобы настроить тихую установку из командной строки при использовании MSI-пакета, добавьте `/quiet /qn`, как в этих примерах:",
    "Note the `--%` stop-parsing symbol used in the PowerShell command.": "Обратите внимание на символ остановки разбора `--%`, используемый в команде PowerShell.",
    "To set up silent command-line installation for an EXE version of the installer, add `--quiet` as in this example:": "Чтобы настроить тихую установку из командной строки для EXE-версии установщика, добавьте `--quiet`, как в этом примере:",
    "## Packet capture driver (pcap)": "## Драйвер захвата пакетов (pcap)",
    "The `PCAP_DRIVER` parameter allows you to specify which packet capture driver will be installed and used for network metrics collection.": "Параметр `PCAP_DRIVER` позволяет указать, какой драйвер захвата пакетов будет установлен и использован для сбора сетевых метрик.",
    "| `npcap` | `PCAP_DRIVER=npcap` installs the `Npcap` driver.  This option uninstalls any installation of WinPcap or outdated Npcap previously installed by OneAgent. If you installed WinPcap or Npcap manually, however, you'll need to uninstall it yourself. |": "| `npcap` | `PCAP_DRIVER=npcap` устанавливает драйвер `Npcap`.  Этот вариант удаляет любую установку WinPcap или устаревшего Npcap, ранее установленного OneAgent. Однако если вы устанавливали WinPcap или Npcap вручную, удалить его придётся самостоятельно. |",
    "| `winpcap` | `PCAP_DRIVER=winpcap` installs the `WinPcap` driver.  This option does **NOT** uninstall or overlay any existing installation of `Npcap` or `WinPcap`. |": "| `winpcap` | `PCAP_DRIVER=winpcap` устанавливает драйвер `WinPcap`.  Этот вариант **НЕ** удаляет и не накладывается на любую существующую установку `Npcap` или `WinPcap`. |",
    "| `auto` | Deprecated with OneAgent version 1.255+  `PCAP_DRIVER=auto` automatically determines which driver to install. This option does **NOT** uninstall or overlay any existing installation of `Npcap` or `WinPcap`. During installation, if no packet capture driver is found, `Npcap` is installed by default. |": "| `auto` | Устарело с версии OneAgent 1.255+  `PCAP_DRIVER=auto` автоматически определяет, какой драйвер устанавливать. Этот вариант **НЕ** удаляет и не накладывается на любую существующую установку `Npcap` или `WinPcap`. Во время установки, если драйвер захвата пакетов не найден, по умолчанию устанавливается `Npcap`. |",
    "| `disabled` | Available with OneAgent version 1.249+  `PCAP_DRIVER=disabled` disables the installation of any packet capture driver and disables the OneAgent network monitoring module. If any packet capture driver is already installed on the host, you'll need to uninstall manually. |": "| `disabled` | Доступно с версии OneAgent 1.249+  `PCAP_DRIVER=disabled` отключает установку любого драйвера захвата пакетов и отключает модуль мониторинга сети OneAgent. Если на хосте уже установлен какой-либо драйвер захвата пакетов, удалить его придётся вручную. |",
    "* This parameter is not supported by the installer web UI.": "* Этот параметр не поддерживается веб-интерфейсом установщика.",
    "* The value of this parameter persists through updates.": "* Значение этого параметра сохраняется при обновлениях.",
    "* If you install `Npcap` during OneAgent installation, the installer creates a scheduled task called `npcapwatchdog`.": "* Если вы устанавливаете `Npcap` во время установки OneAgent, установщик создаёт запланированную задачу с именем `npcapwatchdog`.",
    "  + This task ensures that the `Npcap` driver functions correctly after Windows feature updates. The task runs in the background and has no effect on the performance or functionality of the system.": "  + Эта задача обеспечивает корректную работу драйвера `Npcap` после обновлений компонентов Windows. Задача выполняется в фоновом режиме и не влияет на производительность или функциональность системы.",
    "  + While the `npcapwatchdog` task is meant to prevent issues with Windows updates, you can remove it. However, if removed, the Npcap driver may need to be reinstalled before it can be used again.": "  + Хотя задача `npcapwatchdog` предназначена для предотвращения проблем с обновлениями Windows, её можно удалить. Однако в случае удаления драйвер Npcap, возможно, потребуется переустановить, прежде чем его можно будет снова использовать.",
    "For more information, see": "Дополнительные сведения см.:",
    '* [OneAgent security on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows#installation "Learn about Dynatrace OneAgent security and modifications to your Windows-based system")': '* [Безопасность OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/oneagent-security-windows#installation "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Windows")',
    '* [Install OneAgent on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#winpcapuninstall "Learn how to download and install Dynatrace OneAgent on Windows.")': '* [Установка OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/install-oneagent-on-windows#winpcapuninstall "Узнайте, как скачать и установить Dynatrace OneAgent на Windows.")',
    'For information about the OneAgent auto-update mechanism, see [Update Dynatrace OneAgent on Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Learn about the different ways to update Dynatrace OneAgent on Windows.").': 'Сведения о механизме автоматического обновления OneAgent см. в [Обновление Dynatrace OneAgent на Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows/operation/update-oneagent-on-windows "Узнайте о различных способах обновления Dynatrace OneAgent на Windows.").',
    'For supported platforms, see [Technology support](/managed/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.").': 'Поддерживаемые платформы см. в [Поддержка технологий](/managed/ingest-from/technology-support#windows "Найдите технические подробности о поддержке Dynatrace конкретных платформ и фреймворков разработки.").',
}


if __name__ == "__main__":
    build_textmap(f"{ROOT}/windows.md", HUB)
    build_textmap(f"{ROOT}/windows/operation/stop-restart-oneagent-on-windows.md", STOP)
    build_textmap(
        f"{ROOT}/windows/operation/uninstall-oneagent-on-windows.md", UNINSTALL
    )
    build_textmap(
        f"{ROOT}/windows/installation/how-to-pass-a-proxy-address-during-oneagent-installation-on-windows.md",
        PROXY,
    )
    build_textmap(
        f"{ROOT}/windows/installation/install-oneagent-on-windows.md", INSTALL
    )
    build_textmap(f"{ROOT}/windows/installation/oneagent-security-windows.md", SECURITY)
    build_textmap(
        f"{ROOT}/windows/installation/disk-space-requirements-for-oneagent-installation-and-update-on-windows.md",
        DISK,
    )
    build_difflib(
        f"{ROOT}/windows/installation/customize-oneagent-installation-on-windows.md",
        f"{ROOT}/linux/installation/customize-oneagent-installation-on-linux.md",
        CUSTOMIZE,
    )
    # update: derive from translated linux brother (line-parity), OS-substitute
    build_derive(
        f"{ROOT}/windows/operation/update-oneagent-on-windows.md",
        f"{ROOT}/linux/operation/update-oneagent-on-linux.md",
        {
            2: "title: Обновление OneAgent на Windows",
        },
    )
