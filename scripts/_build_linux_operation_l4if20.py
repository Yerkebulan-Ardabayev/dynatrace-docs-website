#!/usr/bin/env python3
"""L4-IF.20 builder: OneAgent linux/operation/ subtree (5 files).

1:1 line-map method: copy EN byte-for-byte for blank lines, code fences,
code content, and frontmatter source/scraped; translate prose by line index.
Guarantees line-parity (== EN), byte-identical code blocks, LF, no BOM,
no trailing newline. update-oneagent-on-linux is derived from the already
hand-translated AIX sibling (bodies are identical except 3 spots).
"""

from pathlib import Path

EN = Path("docs/managed/ingest-from/dynatrace-oneagent/installation-and-operation")
RU = Path("docs/managed-ru/ingest-from/dynatrace-oneagent/installation-and-operation")


def read_lines(p):
    lines = p.read_text(encoding="utf-8").split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    return lines


def write_lines(p, lines):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes("\n".join(lines).encode("utf-8"))


def build(en_rel, ru_rel, tr):
    en = read_lines(EN / en_rel)
    out = [tr.get(i, en[i]) for i in range(len(en))]
    write_lines(RU / ru_rel, out)
    print(f"{ru_rel}: EN {len(en)} -> RU {len(out)} lines")


# ---------------------------------------------------------------- file 1
stop_restart = {
    1: "title: Остановка/перезапуск OneAgent на Linux",
    6: "# Остановка/перезапуск OneAgent на Linux",
    8: "# Остановка/перезапуск OneAgent на Linux",
    10: "* Чтение: 1 мин",
    11: "* Опубликовано 19 сентября 2018 г.",
    13: "Если вы не хотите использовать OneAgent внутри определённого процесса Java (или другого), можно легко отключить мониторинг Dynatrace для отдельных хостов, групп процессов или приложений:",
    15: "1. Перейдите в **Settings > Monitoring overview**.",
    16: "2. Откройте вкладку **Hosts**, **Process groups** или **Applications**, чтобы получить доступ к переключателям мониторинга для отдельных сущностей.",
    17: "3. Переведите переключатель **Monitoring** в положение **Off**.",
    18: "4. Перезапустите все процессы, для которых мониторинг был отключён.",
    20: "Горячее клонирование",
    22: "Горячее клонирование, как правило, не поддерживается OneAgent из-за требований к генерации идентификатора хоста. При горячем клонировании хоста с установленным OneAgent выполните следующие шаги, чтобы обеспечить корректную работу:",
    24: "1. Остановите OneAgent на исходном хосте.",
    25: "2. Клонируйте хост.",
    26: "3. Запустите OneAgent.",
    27: "4. Выполните перезапуск процессов на новом хосте.",
    29: "## Перезапуск через интерфейс командной строки OneAgent",
    31: "При использовании параметров `set` необходимо перезапустить службу OneAgent, чтобы изменения вступили в силу. Можно использовать параметр `--restart-service` с командой, которая запускает перезапуск автоматически. В некоторых случаях также потребуется перезапустить мониторируемые приложения. Параметр перезапуска можно использовать и сам по себе, без других параметров. См. пример команды ниже.",
    37: 'Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").',
    39: "## Остановка OneAgent через командную строку",
    41: "Если вы используете инструменты управления конфигурацией, такие как Puppet или Ansible, можно также остановить службу OneAgent с помощью следующей команды:",
    43: "* для систем с SystemV: `service oneagent stop`",
    44: "* для систем с systemd: `systemctl stop oneagent`",
    46: "где `oneagent` является скриптом `init.d` для OneAgent.",
    48: "Если вы остановите службу OneAgent, мониторинг будет отключён до перезапуска службы.",
    50: "## Запуск OneAgent через командную строку",
    52: "Чтобы снова запустить Dynatrace OneAgent, используйте следующую команду:",
    54: "* для систем с SystemV: `service oneagent start`",
    55: "* для систем с systemd: `systemctl start oneagent`",
    57: "где `oneagent` является скриптом `init.d` для OneAgent.",
    59: 'Подробнее о том, [как Dynatrace взаимодействует с вашей ОС](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux "Узнайте о безопасности Dynatrace OneAgent и изменениях, вносимых в вашу систему на базе Linux").',
}
build(
    "linux/operation/stop-restart-oneagent-on-linux.md",
    "linux/operation/stop-restart-oneagent-on-linux.md",
    stop_restart,
)


# ---------------------------------------------------------------- file 2
uninstall = {
    1: "title: Удаление OneAgent на Linux",
    6: "# Удаление OneAgent на Linux",
    8: "# Удаление OneAgent на Linux",
    10: "* Чтение: 1 мин",
    11: "* Обновлено 20 октября 2025 г.",
    13: "У OneAgent есть отдельная программа удаления. Чтобы удалить OneAgent из системы, потребуется её запустить.",
    15: "Перейдите в каталог `/opt/dynatrace/oneagent/agent` и с правами root запустите скрипт `uninstall.sh`.",
    17: "## После удаления",
    19: "После удаления файлы журналов, пользователь, под которым работает OneAgent, и часть конфигурации сохраняются в каталоге установки OneAgent. Их можно удалить вручную. Однако обратите внимание, что если конфигурационные файлы удалены и OneAgent установлен повторно, хост будет отображаться как новый с другим внутренним идентификатором.",
    21: "Для полного удаления OneAgent удалите следующее:",
    23: "* Файлы журналов, расположенные в:",
    25: "  + OneAgent версии 1.203+: `/var/log/dynatrace/oneagent`",
    26: "  + OneAgent версии 1.201 и более ранние: `/opt/dynatrace/oneagent/log`",
    27: "* Конфигурационные файлы, расположенные в `/var/lib/dynatrace/oneagent/agent/config`.",
    28: "* Пользователь, под которым работает OneAgent, `dtuser`.",
    29: "* Необязательно Если вы используете пользовательский путь установки, установщик создаёт символическую ссылку в каталоге по умолчанию (`/opt/dynatrace/oneagent`) на пользовательский путь установки.",
    30: "  Эту символическую ссылку необходимо удалить вручную после удаления OneAgent.",
    31: '  Дополнительные сведения см. в [Путь установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Узнайте, как использовать установщик Linux с параметрами командной строки.").',
}
build(
    "linux/operation/uninstall-oneagent-on-linux.md",
    "linux/operation/uninstall-oneagent-on-linux.md",
    uninstall,
)


# ---------------------------------------------------------------- file 4
ppc = {
    1: "title: Обновление OneAgent на PPC BE Linux",
    6: "# Обновление OneAgent на PPC BE Linux",
    8: "# Обновление OneAgent на PPC BE Linux",
    10: "* Чтение: 1 мин",
    11: "* Опубликовано 21 августа 2019 г.",
    13: "Чтобы обновить установленный экземпляр OneAgent на PPC BE, следуйте приведённым ниже инструкциям:",
    15: '1. Повторите все шаги [первоначальной установки](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-ppc-be-linux "Узнайте, как скачать и установить Dynatrace OneAgent на PPC BE Linux."), но установите OneAgent в новый каталог.',
    16: "2. Остановите все мониторируемые процессы.",
    17: "3. Переименуйте текущий каталог установки OneAgent (например, `/opt/dynatrace/oneagent` в `/opt/dynatrace/oneagent-old`) с помощью следующей команды:",
    23: "   Эту папку можно удалить после обновления OneAgent.",
    24: "4. Переименуйте обновлённую папку OneAgent так, чтобы она указывала на исходный каталог установки (например, с `/opt/dynatrace/oneagent-update` на `/opt/dynatrace/oneagent`), с помощью следующей команды:",
    29: "5. Перезапустите все процессы, которые требуется мониторить.",
    31: "## Проверка установленной версии OneAgent",
    33: "Используйте один из этих методов, чтобы проверить, какая версия OneAgent установлена у вас в настоящее время.",
    35: "### Интерфейс командной строки OneAgent",
    37: 'Запустите `oneagentctl` с параметром `--version`. Дополнительные сведения см. в [Настройка OneAgent через интерфейс командной строки](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#display-oneagent-version "Узнайте, как выполнять некоторые задачи настройки OneAgent без переустановки OneAgent.").',
    39: "### Обзор хоста",
    41: "1. Перейдите в **Hosts**.",
    42: "2. Щёлкните интересующий вас хост.",
    43: "3. Разверните **Properties** под именем хоста. Установленная версия OneAgent указана в перечисленных свойствах.",
    45: "### Статус развёртывания",
    47: "1. Перейдите в **Deployment Status**.",
    48: "2. Откройте вкладку **All hosts** или **Recently connected hosts**.",
    49: "3. Разверните интересующую вас запись хоста. Установленная версия OneAgent включена в отображаемую информацию.",
}
build(
    "linux/operation/update-oneagent-on-ppc-be-linux.md",
    "linux/operation/update-oneagent-on-ppc-be-linux.md",
    ppc,
)


# ---------------------------------------------------------------- file 5
apparmor = {
    1: "title: Как включить глубокий мониторинг для приложений, ограниченных AppArmor",
    6: "# Как включить глубокий мониторинг для приложений, ограниченных AppArmor",
    8: "# Как включить глубокий мониторинг для приложений, ограниченных AppArmor",
    10: "* Чтение: 2 мин",
    11: "* Опубликовано 8 августа 2017 г.",
    13: "AppArmor представляет собой систему мандатного управления доступом, которая ограничивает приложения определённым набором ресурсов. Для каждого ограниченного приложения существует профиль, который задаёт, какие операции разрешено выполнять приложению, а также пути в файловой системе, к которым приложению разрешён доступ. Чтобы включить глубокий мониторинг приложений, ограниченных AppArmor, в профили этих приложений необходимо добавить пользовательский набор правил для OneAgent.",
    15: "Определение набора правил, а также пошаговое описание добавления набора правил в существующий профиль приведены в примере ниже. В этом примере мы включаем глубокий мониторинг веб-сервера Apache Tomcat, для которого загрузочный скрипт находится в `/usr/sbin/tomcat-sysd`.",
    17: "Предполагается, что структура каталогов AppArmor следующая:",
    27: "Здесь `usr.sbin.tomcat-sysd` это файл, определяющий профиль AppArmor для Tomcat.",
    29: "1. Создайте новый каталог и новый набор правил для OneAgent внутри этого каталога с именем `agentinjection`.",
    46: "2. Содержимое `/etc/apparmor.d/dynatrace-oneagent/agentinjection` должно быть следующим:",
    180: '   Если для определения пользовательского каталога, предназначенного для хранения больших объёмов данных времени выполнения, вы использовали параметр установки [DATA\\_STORAGE](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Узнайте, как использовать установщик Linux с параметрами командной строки."), отредактируйте следующую строку и добавьте свой пользовательский каталог',
    189: "3. Включите набор правил в профиль Tomcat (`/etc/apparmor.d/usr.sbin.tomcat-sysd`).",
    206: "4. Убедитесь, что заданный профиль работает корректно:",
    208: "   1. Перезагрузите службу AppArmor.",
    209: "   2. Перезапустите Tomcat.",
    210: "   3. Убедитесь в веб-интерфейсе, что глубокий мониторинг работает для процесса Tomcat.",
    211: "   4. Просмотрите журналы аудита, чтобы убедиться в отсутствии отказов AppArmor.",
    213: "Обратите внимание, что хотя набор правил, приведённый в этом примере, был тщательно протестирован, его может потребоваться расширить или изменить из-за различий в окружениях. Кроме того, пользовательский путь установки OneAgent не поддерживается.",
    215: "### Предупреждения об отказах в доступе в журналах аудита",
    217: "Если вы столкнётесь с отказами, связанными с OneAgent, для других процессов в системе, добавьте в профили этих процессов следующее подмножество правил.",
    235: "Этот шаг необязателен, поскольку неудачные инъекции OneAgent в другие процессы не влияют на работу ваших приложений. Тем не менее он может потребоваться, если вы используете IDS или другую автоматизированную систему, которая сообщает о предупреждениях об отказах в доступе, найденных в журналах аудита.",
}
build(
    "linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor.md",
    "linux/operation/how-to-enable-deep-monitoring-for-applications-confined-by-apparmor.md",
    apparmor,
)


# ---------------------------------------------------------------- file 3 (derive from AIX sibling)
aix = read_lines(RU / "aix/operation/update-oneagent-on-aix.md")
assert aix[10].strip() == "* Практическое руководство", repr(aix[10])
lin = aix[:10] + aix[11:]  # drop the 'How-to guide' tag line (linux EN lacks it)
lin[1] = "title: Обновление OneAgent на Linux"
lin[2] = (
    "source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux"
)
lin[3] = "scraped: 2026-05-12T11:05:36.728819"
lin[6] = "# Обновление OneAgent на Linux"
lin[8] = "# Обновление OneAgent на Linux"
hits = 0
for i, l in enumerate(lin):
    if "disk-space-requirements-for-oneagent-installation-and-update-on-aix" in l:
        lin[i] = (
            "Подробнее см. [Файлы OneAgent и требования к дисковому пространству]"
            "(/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/"
            "disk-space-requirements-for-oneagent-installation-and-update-on-linux "
            '"Узнайте о структуре каталогов OneAgent и требованиях к дисковому пространству для установки OneAgent на Linux.")'
        )
        hits += 1
assert hits == 1, f"disk-space line hits={hits}"
write_lines(RU / "linux/operation/update-oneagent-on-linux.md", lin)
en_lin = read_lines(EN / "linux/operation/update-oneagent-on-linux.md")
print(
    f"linux/operation/update-oneagent-on-linux.md: EN {len(en_lin)} -> RU {len(lin)} lines"
)
print("DONE")
