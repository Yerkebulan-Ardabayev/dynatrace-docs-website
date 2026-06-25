# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions.md (hub how-to page)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions"

TRANS = {
    "title: Develop your own Extensions": "title: Разработка собственных расширений",
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 16, 2025": "* Опубликовано 16 июня 2025 г.",
    "Dynatrace can ingest data from [hundreds of tools](https://www.dynatrace.com/hub/), which means you get:": "Dynatrace может принимать данные из [сотен инструментов](https://www.dynatrace.com/hub/), что даёт:",
    "* A single source of truth for observability.": "* Единый источник достоверных данных для наблюдаемости.",
    "* A continuous flow of actionable data to help you fix problems quickly, maintain complex systems, improve code quality, and accelerate digital transformation.": "* Непрерывный поток актуальных данных для быстрого устранения проблем, поддержки сложных систем, улучшения качества кода и ускорения цифровой трансформации.",
    "If we don't have a pre-built solution for your situation, you can declaratively bring metrics into Dynatrace that feed platform analytics and monitoring capabilities. Dynatrace links your data in a meaningful way so you can explore it, build instrumentation, and set up alerting.": "Если готового решения для конкретной ситуации нет, метрики можно декларативно передавать в Dynatrace для питания аналитических и мониторинговых возможностей платформы. Dynatrace связывает данные структурированным образом, что позволяет исследовать их, создавать инструментарий и настраивать оповещения.",
    "Extensions support policy": "Политика поддержки расширений",
    "Dynatrace support staff are committed to aiding within the defined scope of support. However, specific topics fall outside our support capabilities, including:": "Сотрудники службы поддержки Dynatrace оказывают помощь в рамках определённой области поддержки. Однако ряд вопросов выходит за её пределы:",
    "* **Custom Extensions**: Technical support can only aid customers with extensions that are available on Dynatrace Hub and marked as **Supported by Dynatrace**, unless the problem is related to the extensions framework itself.": "* **Пользовательские расширения**: техническая поддержка помогает только с расширениями, доступными в Dynatrace Hub и отмеченными как **Supported by Dynatrace**, если только проблема не связана с самой платформой Extensions framework.",
    "* **Custom Extension Files**: Technical support cannot support with the analysis of custom configuration or code, and requests to create such files are not within the support scope.": "* **Файлы пользовательских расширений**: техническая поддержка не анализирует пользовательские конфигурации или код, а запросы на создание таких файлов не входят в область поддержки.",
    "Customers needing help with unsupported extensions or extension files can request paid assistance from our services department.": "Клиенты, которым нужна помощь с неподдерживаемыми расширениями или файлами расширений, могут запросить платную помощь в нашем сервисном отделе.",
    "## Before you begin": "## Перед началом работы",
    'Get familiar with the [Dynatrace Extensions concepts](/managed/ingest-from/extensions/concepts#concepts "Learn more about the concept of Dynatrace Extensions.").': 'Ознакомьтесь с [концепциями Dynatrace Extensions](/managed/ingest-from/extensions/concepts#concepts "Подробнее о концепции Dynatrace Extensions.").',
    "## Security best practices": "## Рекомендации по безопасности",
    'Dynatrace applies [secure development controls](/managed/manage/data-privacy-and-security/data-security/secure-development-controls "Learn how we ensure complete security for all Dynatrace software components and development practices.") in its Security Development Lifecycle (SDL).': 'Dynatrace применяет [средства контроля безопасной разработки](/managed/manage/data-privacy-and-security/data-security/secure-development-controls "Узнайте, как обеспечивается полная безопасность всех программных компонентов и методов разработки Dynatrace.") в рамках жизненного цикла безопасной разработки (SDL).',
    "Follow these best practices to ensure your extensions are secure, reliable, and compliant with your environment’s security standards.": "Следуйте приведённым рекомендациям, чтобы расширения были безопасными, надёжными и соответствовали стандартам безопасности окружения.",
    "### Certificate management": "### Управление сертификатами",
    "* Use signed extensions to ensure integrity and prevent tampering.": "* Используйте подписанные расширения для обеспечения целостности и предотвращения несанкционированных изменений.",
    "* Assign different signing certificates for different categories of extensions (for example, sensitive data vs. general monitoring).": "* Назначайте разные сертификаты подписи для разных категорий расширений (например, конфиденциальные данные и общий мониторинг).",
    "* Store and manage root and developer certificates separately.": "* Храните корневые и разработческие сертификаты раздельно и управляйте ими независимо.",
    "* Replace leaked certificates immediately and re-sign affected extensions.": "* Немедленно заменяйте скомпрометированные сертификаты и повторно подписывайте затронутые расширения.",
    "### Extension code": "### Код расширения",
    "* Review and validate all extension logic, including scripts, queries, and third-party components.": "* Проверяйте и валидируйте всю логику расширения, включая скрипты, запросы и сторонние компоненты.",
    "* Avoid embedding code from untrusted sources without proper inspection.": "* Не внедряйте код из ненадёжных источников без надлежащей проверки.",
    "### Least-privilege access": "### Доступ по принципу минимальных привилегий",
    "* Create dedicated user accounts (for example, for SQL or SNMP) with minimal permissions.": "* Создавайте выделенные учётные записи (например, для SQL или SNMP) с минимальными разрешениями.",
    "* Avoid using shared or admin-level credentials for extension data collection.": "* Не используйте общие учётные данные или учётные данные уровня администратора для сбора данных расширениями.",
    "* When using the API to manage extensions, use personal tokens instead of tokens that have global extension write access.": "* При управлении расширениями через API используйте персональные токены вместо токенов с глобальным доступом на запись расширений.",
    "* Set up security policies that allow editing extension settings, and assign them only to trusted user groups.": "* Настройте политики безопасности, разрешающие изменение настроек расширений, и назначайте их только доверенным группам пользователей.",
    '+ Use the [Extensions IAM service](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#extensions "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.") to restrict who can edit settings, based on specific scopes like extensions, zones, or host groups. This helps you create detailed, secure policies.': '+ Используйте [сервис Extensions IAM](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#extensions "Полный справочник политик IAM и соответствующих условий для всех сервисов Dynatrace."), чтобы ограничить круг пользователей, которые могут изменять настройки, на основе конкретных областей: расширения, зоны или группы хостов. Это позволяет создавать детализированные и безопасные политики.',
    "### Sensitive data sources": "### Источники конфиденциальных данных",
    "* Make sure your extension doesn't retrieve sensitive information (for example, executing SQL queries).": "* Убедитесь, что расширение не извлекает конфиденциальную информацию (например, не выполняет SQL-запросы с доступом к личным данным).",
    "* Audit your extensions to ensure they do not access or transmit private data unintentionally.": "* Регулярно проводите аудит расширений, чтобы они не получали доступ к персональным данным и не передавали их непреднамеренно.",
    "## Troubleshooting in Dynatrace Community": "## Устранение неполадок в Dynatrace Community",
    "Find solutions to common issues with our expert-written troubleshooting articles.": "Найдите решения распространённых проблем в статьях по устранению неполадок, написанных экспертами.",
    "[Go to troubleshooting forum](https://dt-url.net/6303zdg)": "[Перейти на форум устранения неполадок](https://dt-url.net/6303zdg)",
}

PASS = {
    "# Develop your own Extensions",
}

if __name__ == "__main__":
    build_one(REL, "develop-your-extensions.md", TRANS, PASS)
    qa_one(REL, "develop-your-extensions.md")
