---
title: Обработка текста
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/text-processing
scraped: 2026-03-06T21:36:02.786540
---

# Обработка текста


* Latest Dynatrace
* Overview
* 1-min read
* Published Oct 08, 2025

Обработка текста предоставляет действия `set` и `get`, с помощью которых можно создавать, изменять или получать свойства из содержимого в формате JSON или YAML.
Действия для YAML поддерживают многодокументные YAML-файлы через необязательный параметр индекса документа.

Вы можете комбинировать действия по обработке текста с другими действиями коннекторов, например, с [действием GitHub Connector](github.md "Integrate Workflows with GitHub for handling common developer tasks.") или [действием GitLab Connector](gitlab.md "Integrate Workflows with GitLab."), чтобы получать JSON- или YAML-файлы из репозитория или проекта, манипулировать ими с помощью действий коннектора обработки текста и обновлять их через pull request или merge request.

Дополнительные сведения о том, как запустить рабочий процесс для использования обработки текста, см. в [Кратком руководстве по Workflows](../quickstart.md "Build and run your first workflow.").

## Связанные темы

* [Действия для коннектора обработки текста](text-processing/automation-workflows-text-processing-actions.md "Learn about the type of actions you use as part of a workflow for text processing a JSON or YAML file.")
* [Коннекторы Workflows](../actions.md "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.")
