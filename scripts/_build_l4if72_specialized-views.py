# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../addon-for-vscode/specialized-views.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/addon-for-vscode"

TRANS = {
    "* Reference": "* Справочник",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 16, 2025": "* Опубликовано 16 июня 2025 г.",
    "**Dynatrace Extensions** creates its entry in the VS Code activity bar. This entry provides two specialized views to help you manage Extension projects at scale and become more efficient.": "**Dynatrace Extensions** создаёт свою запись на панели действий VS Code. Эта запись предоставляет два специализированных представления для эффективного управления проектами расширений в масштабе.",
    "## Extension 2.0 workspaces": "## Рабочие пространства Extension 2.0",
    "This view is intended to help you keep track of all Extension 2.0 projects and their workspaces, no matter where they're stored on your filesystem. Each registered workspace is shown by its root folder name, and your currently opened workspace is shown in green, whereas others are in blue.": "Это представление помогает отслеживать все проекты Extension 2.0 и их рабочие пространства независимо от места хранения в файловой системе. Каждое зарегистрированное рабочее пространство отображается по имени корневой папки: текущее открытое рабочее пространство выделено зелёным, остальные синим.",
    "In this view, you can do the following:": "В этом представлении доступны следующие действия:",
    "* Use the plus button to register a new workspace.": "* Нажмите кнопку «плюс», чтобы зарегистрировать новое рабочее пространство.",
    "* Use the plus button to register a new environment.": "* Нажмите кнопку «плюс», чтобы зарегистрировать новое окружение.",
    "* Use the refresh button to update the list.": "* Нажмите кнопку обновления, чтобы обновить список.",
    "Top-level items in this list represent your Extension projects. For each one, you can do the following:": "Элементы верхнего уровня этого списка представляют проекты расширений. Для каждого из них доступны следующие действия:",
    "* Use the folder button to open the associated workspace in the VS Code editor.": "* Нажмите кнопку папки, чтобы открыть связанное рабочее пространство в редакторе VS Code.",
    "* Use the bin button to un-register the project. It'll not delete the workspace from your filesystem.": "* Нажмите кнопку корзины, чтобы отменить регистрацию проекта. Рабочее пространство не будет удалено из файловой системы.",
    "* Select the label to see the extension's name within that workspace, along with its version.": "* Выберите метку, чтобы увидеть имя расширения в данном рабочем пространстве и его версию.",
    "+ Use the file button to open the extension's manifest for a quick look. It'll open in the same window.": "+ Нажмите кнопку файла, чтобы быстро открыть манифест расширения. Он откроется в том же окне.",
    "This view lets you easily update some Dynatrace Extensions behavior settings associated with each workspace. You can do this by right-clicking on any registered workspace label.": "Это представление позволяет легко обновлять некоторые настройки поведения Dynatrace Extensions, связанные с каждым рабочим пространством. Для этого щёлкните правой кнопкой мыши на метке любого зарегистрированного рабочего пространства.",
    "## Environments": "## Окружения",
    "As its name implies, this view is focused on Dynatrace environments and your deployed extensions. Your currently connected Dynatrace environment is shown in green, while others are in blue.": "Как следует из названия, это представление сосредоточено на окружениях Dynatrace и развёрнутых расширениях. Текущее подключённое окружение Dynatrace выделено зелёным, остальные синим.",
    "Top-level items in this list are your registered Dynatrace environments. For each one, you can do the following:": "Элементы верхнего уровня этого списка: зарегистрированные окружения Dynatrace. Для каждого из них доступны следующие действия:",
    "* Use the pen button to change any details.": "* Нажмите кнопку карандаша, чтобы изменить любые сведения.",
    "* Use the bin button to remove this environment.": "* Нажмите кнопку корзины, чтобы удалить это окружение.",
    "* Select the label to expand a list of deployed extensions.": "* Выберите метку, чтобы развернуть список развёрнутых расширений.",
    "Children items to an environment are its deployed extensions. Select any extension to expand the list further and show the extension's monitoring configurations (the status is indicated next to its name). You can do the following:": "Дочерние элементы окружения: его развёрнутые расширения. Выберите любое расширение, чтобы развернуть список дальше и отобразить конфигурации мониторинга расширения (статус указан рядом с именем). Доступны следующие действия:",
    "* Use the plus button to create a new monitoring configuration.": "* Нажмите кнопку «плюс», чтобы создать новую конфигурацию мониторинга.",
    "* Use the pen button to make changes to a configuration.": "* Нажмите кнопку карандаша, чтобы внести изменения в конфигурацию.",
    "* Use the bin button to delete the configuration.": "* Нажмите кнопку корзины, чтобы удалить конфигурацию.",
    "* Use the file button to save this configuration to a file. It'll be saved in your workspace's `./config` folder.": "* Нажмите кнопку файла, чтобы сохранить эту конфигурацию в файл. Файл будет сохранён в папке `./config` рабочего пространства.",
}

PASS = {
    "title: Specialized views",
    "# Specialized views",
}

if __name__ == "__main__":
    build_one(REL, "specialized-views.md", TRANS, PASS)
    qa_one(REL, "specialized-views.md")
