# -*- coding: utf-8 -*-
"""L4-AG.1b.1 builder: 2 cluster-api hub-страницы (dynatrace-api).

Состав батча:
  - dynatrace-api/cluster-api/cluster-api-v1.md (85 строк)
  - dynatrace-api/cluster-api/cluster-api-v2.md (90 строк)

Канон взят из L4-AG.1c.1: substring-replace pass для prose-файлов.
  1) TITLE_MAP: frontmatter title + H1 (двойной, как идиома Material) → переведён.
  2) PARA_MAP: целые intro-параграфы и шаги нумерованного списка → RU.
  3) HEADING_MAP: H3/H4 секции → RU.
  4) TOOLTIP_MAP: текст после URL в `"..."` (longest-first).
  5) LINK_LABEL_MAP: видимый текст ссылки в `[...]` (longest-first).
  6) ITEM_REPL / _translate_date_lines: bullet даты.

Lessons L4-AG.1c.1 учтены:
  - tooltip-pass ДО link-label чтобы избежать substring-коллизий
    («cluster proxy configuration» как substring → грам. ошибка в tooltip).
  - longest-first sorting для TOOLTIP_MAP и LINK_LABEL_MAP.
  - устоявшиеся EN-термины (Synthetic, ZIP, REST) остаются.
"""

import re
from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")

PILOT = [
    "dynatrace-api/cluster-api/cluster-api-v1.md",
    "dynatrace-api/cluster-api/cluster-api-v2.md",
]

# Mojibake — БЕЗ defects (raw audit clean).
BOMJ_FLAT = chr(0xEF) + chr(0xBB) + chr(0xBF)


def _normalize(text: str) -> str:
    return text.replace(BOMJ_FLAT, "")


TITLE_MAP = {
    "Cluster API v1": "Cluster API v1",
    "Cluster API v2": "Cluster API v2",
}

# H3/H4 секции — переводим (EN устоявшиеся термины оставляем где надо).
HEADING_MAP = {
    "### Cluster\n": "### Cluster\n",
    "### Internet proxy\n": "### Интернет-прокси\n",
    "#### High Availability deployments\n": "#### High Availability развёртывания\n",
    "### Password policy\n": "### Парольная политика\n",
    "### SSL certificates\n": "### SSL-сертификаты\n",
    "### Users\n": "### Пользователи\n",
    "### User groups\n": "### Группы пользователей\n",
    "### Environments\n": "### Окружения\n",
    "### Synthetic locations and nodes\n": "### Synthetic-локации и узлы\n",
    "### Tokens\n": "### Токены\n",
    "### User management\n": "### Управление пользователями\n",
    "### Remote access\n": "### Удалённый доступ\n",
    "### License\n": "### Лицензия\n",
    "### Log Monitoring\n": "### Log Monitoring\n",
}

# Whole-paragraph переводы.
PARA_MAP = {
    "Dynatrace Managed exposes cluster-wide functionality via REST endpoints. This interactive documentation also acts as a REST client you can use to interact with Dynatrace Managed clusters.": (
        "Dynatrace Managed предоставляет функциональность на уровне кластера через REST-эндпойнты. "
        "Эта интерактивная документация также работает как REST-клиент, через который можно "
        "взаимодействовать с кластерами Dynatrace Managed."
    ),
    "To access the Cluster API": "Чтобы перейти к Cluster API",
    "1. Open the Cluster Management Console.": "1. Откройте Cluster Management Console.",
    "2. Open the User menu by selecting the User icon in the upper-right corner.": (
        "2. Откройте меню пользователя, нажав на иконку пользователя в правом верхнем углу."
    ),
    "2. Open the User menu by clicking the User icon in the upper-right corner.": (
        "2. Откройте меню пользователя, нажав на иконку пользователя в правом верхнем углу."
    ),
    "3. Select **Cluster API v1**.": "3. Выберите **Cluster API v1**.",
    "3. Select **Cluster API v2**.": "3. Выберите **Cluster API v2**.",
}

# Tooltip (title="...") — substring-pass ДО link-label.
# Longest-first; устоявшиеся EN термины (REST, ZIP, API, Synthetic) сохраняем.
TOOLTIP_MAP = {
    # ----- Cluster -----
    "Learn how to use the Dynatrace API to get cluster information about known nodes.": (
        "Узнайте, как через Dynatrace API получить информацию о кластере для известных узлов."
    ),
    "Learn how to use the Dynatrace API to get cluster nodes configuration.": (
        "Узнайте, как через Dynatrace API получить конфигурацию узлов кластера."
    ),
    "Learn how to configure cluster nodes responsibilities.": (
        "Узнайте, как настроить роли узлов кластера."
    ),
    "Learn how to use the Dynatrace API to get cluster nodes configuration current status.": (
        "Узнайте, как через Dynatrace API получить текущий статус конфигурации узлов кластера."
    ),
    "Learn how to use the Dynatrace API to get the status of cluster node configuration requests.": (
        "Узнайте, как через Dynatrace API получить статус запросов на конфигурацию узлов кластера."
    ),
    "Learn how to use the Dynatrace API to get details about the current cluster maintenance state.": (
        "Узнайте, как через Dynatrace API получить детали текущего режима обслуживания кластера."
    ),
    "Learn how to turn on the maintenance of the cluster.": (
        "Узнайте, как включить режим обслуживания кластера."
    ),
    "Learn how to turn off the maintenance of the cluster.": (
        "Узнайте, как выключить режим обслуживания кластера."
    ),
    # ----- Internet proxy -----
    "Learn how to use the Dynatrace API to get cluster proxy configuration.": (
        "Узнайте, как через Dynatrace API получить конфигурацию прокси кластера."
    ),
    "Learn how to use the Dynatrace API to set or update cluster proxy configuration.": (
        "Узнайте, как через Dynatrace API задать или обновить конфигурацию прокси кластера."
    ),
    "Learn how to use the Dynatrace API to delete cluster proxy configuration.": (
        "Узнайте, как через Dynatrace API удалить конфигурацию прокси кластера."
    ),
    "Learn how to use the Dynatrace API to test cluster proxy configuration.": (
        "Узнайте, как через Dynatrace API проверить конфигурацию прокси кластера."
    ),
    "Learn how to use the Dynatrace API to get proxy configurations for all data centers in premium high availability deployments.": (
        "Узнайте, как через Dynatrace API получить конфигурации прокси для всех дата-центров в premium high availability развёртываниях."
    ),
    "Learn how to use the Dynatrace API to get proxy configuration for specific data center in premium high availability deployments.": (
        "Узнайте, как через Dynatrace API получить конфигурацию прокси для конкретного дата-центра в premium high availability развёртываниях."
    ),
    "Learn how to use the Dynatrace API to set or update proxy configuration in specific data center.": (
        "Узнайте, как через Dynatrace API задать или обновить конфигурацию прокси в конкретном дата-центре."
    ),
    "Learn how to use the Dynatrace API to delete proxy configuration in specific data center.": (
        "Узнайте, как через Dynatrace API удалить конфигурацию прокси в конкретном дата-центре."
    ),
    "Learn how to use the Dynatrace API to test proxy configuration from specific data center.": (
        "Узнайте, как через Dynatrace API проверить конфигурацию прокси из конкретного дата-центра."
    ),
    # ----- Password policy -----
    "Learn how to use the Dynatrace API to get cluster password policy.": (
        "Узнайте, как через Dynatrace API получить парольную политику кластера."
    ),
    "Learn how to use the Dynatrace API to update cluster password policy.": (
        "Узнайте, как через Dynatrace API обновить парольную политику кластера."
    ),
    # ----- SSL certificates -----
    "Learn how to use the Dynatrace API to get cluster SSL certificate details.": (
        "Узнайте, как через Dynatrace API получить детали SSL-сертификата кластера."
    ),
    "Learn how to use the Dynatrace API to get cluster SSL certificate storage status.": (
        "Узнайте, как через Dynatrace API получить статус хранилища SSL-сертификатов кластера."
    ),
    "Learn how to use the Dynatrace API to store cluster SSL certificate.": (
        "Узнайте, как через Dynatrace API сохранить SSL-сертификат кластера."
    ),
    # ----- Users -----
    "Learn how to use the Dynatrace API to get a list of cluster users.": (
        "Узнайте, как через Dynatrace API получить список пользователей кластера."
    ),
    "Learn how to use the Dynatrace API to update cluster user.": (
        "Узнайте, как через Dynatrace API обновить пользователя кластера."
    ),
    "Learn how to use the Dynatrace API to create cluster user.": (
        "Узнайте, как через Dynatrace API создать пользователя кластера."
    ),
    "Learn how to use the Dynatrace API to get specific cluster user.": (
        "Узнайте, как через Dynatrace API получить конкретного пользователя кластера."
    ),
    "Learn how to use the Dynatrace API to delete cluster user.": (
        "Узнайте, как через Dynatrace API удалить пользователя кластера."
    ),
    "Learn how configure multiple cluster user accounts.": (
        "Узнайте, как настроить несколько учётных записей пользователей кластера."
    ),
    # ----- User groups -----
    "Learn how to use the Dynatrace API to get specific cluster user groups.": (
        "Узнайте, как через Dynatrace API получить конкретные группы пользователей кластера."
    ),
    "Learn how to use the Dynatrace API to update cluster user group.": (
        "Узнайте, как через Dynatrace API обновить группу пользователей кластера."
    ),
    "Learn how to use the Dynatrace API to create cluster user group.": (
        "Узнайте, как через Dynatrace API создать группу пользователей кластера."
    ),
    "Learn how configure multiple cluster user groups.": (
        "Узнайте, как настроить несколько групп пользователей кластера."
    ),
    "Learn how to use the Dynatrace API to get management zone permissions for all groups.": (
        "Узнайте, как через Dynatrace API получить разрешения management zone для всех групп."
    ),
    "Learn how to use the Dynatrace API to update management zones for a single user group.": (
        "Узнайте, как через Dynatrace API обновить management zones для одной группы пользователей."
    ),
    "Learn how to use the Dynatrace API to get management zone permissions for specific group.": (
        "Узнайте, как через Dynatrace API получить разрешения management zone для конкретной группы."
    ),
    # ----- v2: Environments -----
    "Use the Dynatrace API to get a list of all existing environments.": (
        "Через Dynatrace API получите список всех существующих окружений."
    ),
    "Use the Dynatrace API to create a new environment.": (
        "Через Dynatrace API создайте новое окружение."
    ),
    "Use the Dynatrace API to get the properties of a specified environment.": (
        "Через Dynatrace API получите свойства указанного окружения."
    ),
    "Use the Dynatrace API to update a specific environment.": (
        "Через Dynatrace API обновите конкретное окружение."
    ),
    "Use the Dynatrace API to delete a specific environment.": (
        "Через Dynatrace API удалите конкретное окружение."
    ),
    # ----- v2: Synthetic locations and nodes -----
    "List all synthetic locations via the Synthetic v2 API on Dynatrace Managed.": (
        "Получите список всех Synthetic-локаций через Synthetic v2 API в Dynatrace Managed."
    ),
    "Create a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.": (
        "Создайте приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed."
    ),
    "Retrieve parameters of a Synthetic location via the Synthetic API v2 in Dynatrace Managed.": (
        "Получите параметры Synthetic-локации через Synthetic API v2 в Dynatrace Managed."
    ),
    "Update a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.": (
        "Обновите приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed."
    ),
    "Delete a private Synthetic location via the Synthetic API v2 in Dynatrace Managed.": (
        "Удалите приватную Synthetic-локацию через Synthetic API v2 в Dynatrace Managed."
    ),
    "List all Synthetic nodes via the Synthetic API v2 in Dynatrace Managed.": (
        "Получите список всех Synthetic-узлов через Synthetic API v2 в Dynatrace Managed."
    ),
    "Retrieve parameters of a Synthetic node via the Synthetic API v2 in Dynatrace Managed.": (
        "Получите параметры Synthetic-узла через Synthetic API v2 в Dynatrace Managed."
    ),
    # ----- v2: Tokens -----
    "Learn how to use the Dynatrace API to get a list of available Dynatrace Cluster API authentication tokens.": (
        "Узнайте, как через Dynatrace API получить список доступных токенов аутентификации Dynatrace Cluster API."
    ),
    "Learn how to create new Dynatrace Cluster token using API.": (
        "Узнайте, как создать новый токен Dynatrace Cluster через API."
    ),
    "Learn how to update Dynatrace Cluster token using API.": (
        "Узнайте, как обновить токен Dynatrace Cluster через API."
    ),
    "Learn how to delete Dynatrace Cluster token using API.": (
        "Узнайте, как удалить токен Dynatrace Cluster через API."
    ),
    "Learn how to list token metadata using token value in request and API.": (
        "Узнайте, как получить метаданные токена по значению токена в запросе через API."
    ),
    "Learn how to list token metadata using token ID and API.": (
        "Узнайте, как получить метаданные токена по ID токена через API."
    ),
    # ----- v2: User management -----
    "Learn how to get user sessions configuration via Cluster API.": (
        "Узнайте, как получить конфигурацию пользовательских сессий через Cluster API."
    ),
    "Learn how to update Dynatrace Cluster user sessions configuration using API.": (
        "Узнайте, как обновить конфигурацию пользовательских сессий Dynatrace Cluster через API."
    ),
    "Learn how to get user sessions via Cluster API.": (
        "Узнайте, как получить пользовательские сессии через Cluster API."
    ),
    "Learn how to delete Dynatrace Cluster user sessions of a given user using API.": (
        "Узнайте, как удалить пользовательские сессии Dynatrace Cluster для конкретного пользователя через API."
    ),
    # ----- v2: Remote access -----
    "Learn how to get all cluster access requests.": (
        "Узнайте, как получить все запросы на доступ к кластеру."
    ),
    "Learn how to grant permission for remote access using the Cluster API v2.": (
        "Узнайте, как выдать разрешение на удалённый доступ через Cluster API v2."
    ),
    "Learn how to get cluster access request.": (
        "Узнайте, как получить запрос на доступ к кластеру."
    ),
    "Learn how to change the state of an access request using the Cluster API v2.": (
        "Узнайте, как изменить состояние запроса на доступ через Cluster API v2."
    ),
    # ----- v2: License -----
    "Learn how to export aggregated hourly license usage as a ZIP file.": (
        "Узнайте, как экспортировать агрегированное по часам использование лицензии в виде ZIP-файла."
    ),
    # ----- v2: Log Monitoring -----
    "Learn how to get Log Monitoring status in Managed deployments using API.": (
        "Узнайте, как получить статус Log Monitoring в развёртываниях Managed через API."
    ),
    "Learn how to update the total log events per cluster limit based on the cluster resources size using API.": (
        "Узнайте, как обновить общий лимит log events на кластер с учётом размера ресурсов кластера через API."
    ),
}

# Link labels (visible text inside `[...]`).
# Longest-first; устоявшиеся «Synthetic», «cluster nodes», «proxy», «management zones» сохранены.
LINK_LABEL_MAP = {
    # ----- Cluster -----
    "Get cluster information about known cluster nodes": "Получить информацию о кластере по известным узлам",
    "Get cluster nodes configuration current status": "Получить текущий статус конфигурации узлов кластера",
    "Get cluster nodes configuration request status": "Получить статус запроса на конфигурацию узлов кластера",
    "Get cluster nodes configuration": "Получить конфигурацию узлов кластера",
    "Configure cluster nodes responsibilities": "Настроить роли узлов кластера",
    "Get details about the current cluster maintenance state": "Получить детали текущего режима обслуживания кластера",
    "Turn on the maintenance of the cluster": "Включить режим обслуживания кластера",
    "Turn off the maintenance of the cluster": "Выключить режим обслуживания кластера",
    # ----- Internet proxy (longest-first внутри HA-группы) -----
    "HA - Get proxy configurations for all data centers": "HA: получить конфигурации прокси для всех дата-центров",
    "HA - Get proxy configuration for specific data center": "HA: получить конфигурацию прокси для конкретного дата-центра",
    "HA - Set or update proxy configuration for specific data center": "HA: задать или обновить конфигурацию прокси для конкретного дата-центра",
    "HA - Delete proxy configuration in specific data center": "HA: удалить конфигурацию прокси в конкретном дата-центре",
    "HA - Test proxy configuration from specific data center": "HA: проверить конфигурацию прокси из конкретного дата-центра",
    "Get proxy configurations for all data centers": "Получить конфигурации прокси для всех дата-центров",
    "Get proxy configuration for specific data center": "Получить конфигурацию прокси для конкретного дата-центра",
    "Set or update proxy configuration for specific data center": "Задать или обновить конфигурацию прокси для конкретного дата-центра",
    "Delete proxy configuration in specific data center": "Удалить конфигурацию прокси в конкретном дата-центре",
    "Test proxy configuration from specific data center": "Проверить конфигурацию прокси из конкретного дата-центра",
    "Get cluster proxy configuration": "Получить конфигурацию прокси кластера",
    "Set or update cluster proxy configuration": "Задать или обновить конфигурацию прокси кластера",
    "Delete cluster proxy configuration": "Удалить конфигурацию прокси кластера",
    "Test cluster proxy configuration": "Проверить конфигурацию прокси кластера",
    # ----- Password policy -----
    "Get cluster password policy": "Получить парольную политику кластера",
    "Update cluster password policy": "Обновить парольную политику кластера",
    # ----- SSL certificates -----
    "Get cluster SSL certificate details": "Получить детали SSL-сертификата кластера",
    "Get cluster SSL certificate storage status": "Получить статус хранилища SSL-сертификатов кластера",
    "Store cluster SSL certificate": "Сохранить SSL-сертификат кластера",
    # ----- Users -----
    "Create cluster user accounts": "Создать учётные записи пользователей кластера",
    "Get users": "Получить список пользователей",
    "Update user": "Обновить пользователя",
    "Create user": "Создать пользователя",
    "Get user": "Получить пользователя",
    "Delete user": "Удалить пользователя",
    # ----- User groups -----
    "Get management zones for user groups": "Получить management zones для групп пользователей",
    "Update management zones for user group": "Обновить management zones для группы пользователей",
    "Get management zones for user group": "Получить management zones для группы пользователей",
    "Create user groups": "Создать группы пользователей",
    "Get user groups": "Получить группы пользователей",
    "Update user group": "Обновить группу пользователей",
    "Create user group": "Создать группу пользователей",
    "Get user group": "Получить группу пользователей",
    "Delete user group": "Удалить группу пользователей",
    # ----- v2: Environments -----
    "List properties for specific environment": "Получить свойства конкретного окружения",
    "Update specific environment": "Обновить конкретное окружение",
    "Delete specific environment": "Удалить конкретное окружение",
    "List all existing environments": "Получить список всех существующих окружений",
    "Create a new environment": "Создать новое окружение",
    # ----- v2: Synthetic locations and nodes -----
    "List all cluster private Synthetic locations": "Получить список всех приватных Synthetic-локаций кластера",
    "Create new private Synthetic locations": "Создать новые приватные Synthetic-локации",
    "Get properties of specified cluster locations": "Получить свойства указанных локаций кластера",
    "Update specified private Synthetic cluster location": "Обновить указанную приватную Synthetic-локацию кластера",
    "Delete specified private Synthetic cluster location": "Удалить указанную приватную Synthetic-локацию кластера",
    "List all Synthetic cluster nodes": "Получить список всех Synthetic-узлов кластера",
    "List properties of specified Synthetic cluster nodes": "Получить свойства указанных Synthetic-узлов кластера",
    # ----- v2: Tokens -----
    "List available cluster tokens": "Получить список доступных токенов кластера",
    "Create new cluster token": "Создать новый токен кластера",
    "Update cluster token": "Обновить токен кластера",
    "Delete cluster token": "Удалить токен кластера",
    "List cluster token metadata with request": "Получить метаданные токена кластера по запросу",
    "List cluster token metadata with ID": "Получить метаданные токена кластера по ID",
    # ----- v2: User management -----
    "Get cluster user sessions configuration": "Получить конфигурацию пользовательских сессий кластера",
    "Update cluster user sessions configuration": "Обновить конфигурацию пользовательских сессий кластера",
    "Get cluster user sessions": "Получить пользовательские сессии кластера",
    "Delete user sessions of a given user": "Удалить пользовательские сессии конкретного пользователя",
    # ----- v2: Remote access -----
    "Get all cluster access requests": "Получить все запросы на доступ к кластеру",
    "Grant remote access permission": "Выдать разрешение на удалённый доступ",
    "Get Cluster access request": "Получить запрос на доступ к кластеру",
    "Change state of access request": "Изменить состояние запроса на доступ",
    # ----- v2: License -----
    "Export license data": "Экспортировать данные лицензии",
    # ----- v2: Log Monitoring -----
    "Update log events per cluster for Log Monitoring": "Обновить лимит log events на кластер для Log Monitoring",
    "Get Log Monitoring status": "Получить статус Log Monitoring",
}

# Bullet даты — преобразуются через _translate_date_lines.
MONTH = {
    "Jan": "января",
    "Feb": "февраля",
    "Mar": "марта",
    "Apr": "апреля",
    "May": "мая",
    "Jun": "июня",
    "Jul": "июля",
    "Aug": "августа",
    "Sep": "сентября",
    "Oct": "октября",
    "Nov": "ноября",
    "Dec": "декабря",
}


def _translate_date_lines(line: str) -> str:
    """`* Published Nov 18, 2020` → `* Опубликовано: 18 ноября 2020`."""
    s = line
    m = re.match(r"\* Published (\w+) (\d+), (\d{4})\s*$", s)
    if m:
        mon, day, year = m.group(1), m.group(2), m.group(3)
        if mon in MONTH:
            return f"* Опубликовано: {int(day)} {MONTH[mon]} {year}\n"
    m = re.match(r"\* Updated on (\w+) (\d+), (\d{4})\s*$", s)
    if m:
        mon, day, year = m.group(1), m.group(2), m.group(3)
        if mon in MONTH:
            return f"* Обновлено: {int(day)} {MONTH[mon]} {year}\n"
    return s


def translate_file(en_path: Path, ru_path: Path) -> int:
    raw = en_path.read_text(encoding="utf-8")
    text = _normalize(raw)

    # 1) Frontmatter title + H1 (двойной)
    for en_t, ru_t in TITLE_MAP.items():
        text = text.replace(f"title: {en_t}\n", f"title: {ru_t}\n")
        text = text.replace(f"# {en_t}\n", f"# {ru_t}\n")

    # 2) Headings (H3/H4 секции)
    for k, v in HEADING_MAP.items():
        text = text.replace(k, v)

    # 3) Целые параграфы / шаги
    for k, v in PARA_MAP.items():
        text = text.replace(k, v)

    # 4) Tooltip ДО link-labels (longest-first во избежание substring-конфликтов)
    for k in sorted(TOOLTIP_MAP, key=len, reverse=True):
        text = text.replace(f'"{k}"', f'"{TOOLTIP_MAP[k]}"')

    # 5) Link labels (longest-first)
    for k in sorted(LINK_LABEL_MAP, key=len, reverse=True):
        text = text.replace(f"[{k}]", f"[{LINK_LABEL_MAP[k]}]")

    # 6) Bullet даты (Published / Updated on)
    out_lines = []
    for line in text.splitlines(keepends=True):
        out_lines.append(_translate_date_lines(line))
    text = "".join(out_lines)

    ru_path.parent.mkdir(parents=True, exist_ok=True)
    ru_path.write_text(text, encoding="utf-8", newline="\n")
    return text.count("\n")


def main():
    total_in = total_out = 0
    for rel in PILOT:
        en_p = EN / rel
        ru_p = RU / rel
        en_lines = en_p.read_text(encoding="utf-8").count("\n")
        ru_lines = translate_file(en_p, ru_p)
        marker = "OK" if en_lines == ru_lines else f"DIFF en={en_lines} ru={ru_lines}"
        print(f"  {rel:75} {marker}")
        total_in += en_lines
        total_out += ru_lines
    print(f"\nTotal: en={total_in} lines, ru={total_out} lines, files={len(PILOT)}")


if __name__ == "__main__":
    main()
