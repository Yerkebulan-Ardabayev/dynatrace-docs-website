# -*- coding: utf-8 -*-
"""L4-AG.1b.2 builder: 2 финальных dynatrace-api JSON-models файла.

Состав батча (закрывает корпус dynatrace-api 1142/1142 = 100%):
  - dynatrace-api/configuration-api/automatically-applied-tags-api/models.md (1376 строк)
  - dynatrace-api/configuration-api/management-zones-api/json-models.md (1371 строк)

Twin-pair: 99% содержимого идентично (различаются только title/H1/Deprecated
ссылки/intro параграф/Published date/Related topics в одном).

Канон взят из L4-AG.1c.1 / L4-AG.1b.1: substring-replace pass для prose-файлов.
  1) TITLE_MAP: frontmatter title + H1 (двойной) → переведён.
  2) DATE_MAP: «Published Aug 13, 2019» → «Опубликовано: 13 августа 2019».
  3) PARA_MAP: целые intro/deprecated/H2-intro параграфы → RU.
  4) HEADING_MAP: H2 секции → RU.
  5) H4_OBJECT_MAP: «#### The `Name` object» → «#### Объект `Name`» (35 имён).
  6) COMPARISON_MAP: «Comparison for `X` attributes.» → «Сравнение для атрибутов `X`.».
  7) KEY_TYPE_MAP: «The key for dynamic attributes of the `X` type.» → RU.
  8) STANDALONE_LINE_MAP: одиночные «Parameters» / «JSON model».
  9) TABLE_HEADER_MAP: «| Element | Type | Description |» → RU.
 10) TOOLTIP_MAP / LINK_LABEL_MAP: для Related topics (longest-first).

Lessons L4-AG.1b.1 / L4-AG.1c.1 учтены:
  - longest-first sorting для конкурирующих substrings.
  - устоявшиеся API-имена (Settings API, builtin:..., Dynatrace) остаются EN.
  - имена JSON-классов (ApplicationTypeComparison и т.д.) НЕ переводим.
  - ENUM-значения (APPLICATION_TYPE и т.д.) в H3 не трогаем.
  - JSON-блоки (60 ``` code fences) не пересекаются с substring-маппингами:
    содержат только «operator/value/negate/type» = английские JSON-ключи,
    которые в RU-тексте не используются как substring-цели.
  - CLAUDE.md #0: em-dash «—» в РУ-переводах ЗАПРЕЩЕН; везде заменён на двоеточие.
"""

import re
from pathlib import Path

EN = Path("docs/managed")
RU = Path("docs/managed-ru")

PILOT = [
    "dynatrace-api/configuration-api/automatically-applied-tags-api/models.md",
    "dynatrace-api/configuration-api/management-zones-api/json-models.md",
]

# Mojibake — раw audit clean (0 BOM / 0 single / 0 triple / 0 double-B).
BOMJ_FLAT = chr(0xEF) + chr(0xBB) + chr(0xBF)


def _normalize(text: str) -> str:
    return text.replace(BOMJ_FLAT, "")


# ─────────────────────────────────────────────────────────────────────────────
# TITLE (frontmatter + H1 twin) — line-level substring-replace
# ─────────────────────────────────────────────────────────────────────────────
TITLE_MAP = {
    "Automatically applied tags API - JSON models": "Automatically applied tags API - JSON-модели",
    "Management zones API - JSON models": "Management zones API - JSON-модели",
}

# Published bullet
DATE_MAP = {
    "* Published Aug 13, 2019": "* Опубликовано: 13 августа 2019",
    "* Published Apr 29, 2020": "* Опубликовано: 29 апреля 2020",
}

# ─────────────────────────────────────────────────────────────────────────────
# H2 + Related topics
# ─────────────────────────────────────────────────────────────────────────────
HEADING_MAP = {
    "## Variations of the `ConditionKey` object\n": "## Варианты объекта `ConditionKey`\n",
    "## Variations of the `ComparisonBasic` object\n": "## Варианты объекта `ComparisonBasic`\n",
    "## Related topics\n": "## Связанные темы\n",
}

# ─────────────────────────────────────────────────────────────────────────────
# H4 объекты: «#### The `Name` object» → «#### Объект `Name`»
# ─────────────────────────────────────────────────────────────────────────────
H4_OBJECT_NAMES = [
    "ApplicationTypeComparison",
    "AzureComputeModeComparison",
    "AzureSkuComparision",  # typo источника (Comparision вместо Comparison)
    "BitnessComparision",  # typo источника
    "CloudTypeComparison",
    "CustomApplicationTypeComparison",
    "CustomHostMetadataConditionKey",
    "CustomHostMetadataKey",
    "CustomProcessMetadataConditionKey",
    "CustomProcessMetadataKey",
    "DatabaseTopologyComparison",
    "DcrumDecoderComparison",
    "EntityIdComparison",
    "HypervisorTypeComparision",  # typo источника
    "IndexedNameComparison",
    "IndexedStringComparison",
    "IndexedTagComparison",
    "IntegerComparison",
    "IpAddressComparison",
    "MobilePlatformComparison",
    "OsArchitectureComparison",
    "OsTypeComparison",
    "PaasTypeComparison",
    "ProcessMetadataConditionKey",
    "ServiceTopologyComparison",
    "ServiceTypeComparison",
    "SimpleHostTech",
    "SimpleHostTechComparison",
    "SimpleTech",
    "SimpleTechComparison",
    "StringComparison",
    "StringConditionKey",
    "SyntheticEngineTypeComparison",
    "TagComparison",
    "TagInfo",
]
H4_OBJECT_MAP = {
    f"#### The `{n}` object\n": f"#### Объект `{n}`\n" for n in H4_OBJECT_NAMES
}

# ─────────────────────────────────────────────────────────────────────────────
# Comparison for `X` attributes. — 26 ENUM-типов
# ─────────────────────────────────────────────────────────────────────────────
COMPARISON_TYPES = [
    "APPLICATION_TYPE",
    "AZURE_COMPUTE_MODE",
    "AZURE_SKU",
    "BITNESS",
    "CLOUD_TYPE",
    "CUSTOM_APPLICATION_TYPE",
    "DATABASE_TOPOLOGY",
    "DCRUM_DECODER_TYPE",
    "ENTITY_ID",
    "HYPERVISOR_TYPE",
    "INDEXED_NAME",
    "INDEXED_STRING",
    "INDEXED_TAG",
    "INTEGER",
    "IP_ADDRESS",
    "MOBILE_PLATFORM",
    "OS_ARCHITECTURE",
    "OS_TYPE",
    "PAAS_TYPE",
    "SERVICE_TOPOLOGY",
    "SERVICE_TYPE",
    "SIMPLE_HOST_TECH",
    "SIMPLE_TECH",
    "STRING",
    "SYNTHETIC_ENGINE_TYPE",
    "TAG",
]
COMPARISON_MAP = {
    f"Comparison for `{t}` attributes.": f"Сравнение для атрибутов `{t}`."
    for t in COMPARISON_TYPES
}

# ─────────────────────────────────────────────────────────────────────────────
# The key for dynamic attributes of the `X` type. — 4 KEY-типа
# ─────────────────────────────────────────────────────────────────────────────
KEY_TYPES = [
    "HOST_CUSTOM_METADATA_KEY",
    "PROCESS_CUSTOM_METADATA_KEY",
    "PROCESS_PREDEFINED_METADATA_KEY",
    "STRING",
]
KEY_TYPE_MAP = {
    f"The key for dynamic attributes of the `{t}` type.": f"Ключ для динамических атрибутов типа `{t}`."
    for t in KEY_TYPES
}

# ─────────────────────────────────────────────────────────────────────────────
# Whole-paragraph переводы (substring-replace, longest-first)
# ─────────────────────────────────────────────────────────────────────────────
PARA_MAP = {
    # ── Deprecated параграфы (различаются ссылками на builtin: schema) ──
    'This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "View builtin:tags.auto-tagging settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:tags.auto-tagging`) schema instead.': 'Этот API устарел. Используйте вместо него [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со схемой [Automatically applied tags](/managed/dynatrace-api/environment-api/settings/schemas/builtin-tags-auto-tagging "Просмотр таблицы schema builtin:tags.auto-tagging вашего окружения мониторинга через Dynatrace API.") (`builtin:tags.auto-tagging`).',
    'This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the [Management zones settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "View builtin:management-zones settings schema table of your monitoring environment via the Dynatrace API.") (`builtin:management-zones`) schema instead.': 'Этот API устарел. Используйте вместо него [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со схемой [Management zones settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-management-zones "Просмотр таблицы schema builtin:management-zones вашего окружения мониторинга через Dynatrace API.") (`builtin:management-zones`).',
    # ── Intro к файлу (2 варианта) ──
    "Some JSON models of the **Automatically applied tags** API vary depending on the **type** of the model. The JSON models for each variation are listed below.": "Некоторые JSON-модели API **Automatically applied tags** различаются в зависимости от **type** модели. Ниже перечислены JSON-модели для каждого варианта.",
    "Some JSON models of the **Management zones** API vary, depending on the **type** of some objects. Here you can find JSON models for each variation.": "Некоторые JSON-модели API **Management zones** различаются в зависимости от **type** некоторых объектов. Здесь приведены JSON-модели для каждого варианта.",
    # ── Standalone label «Deprecated» ──
    "Deprecated\n": "Устарел\n",
    # ── H2-introductions (one-paragraph each) ──
    "The `ConditionKey` object is the base for all conditions. The actual set of fields depends on the **type** of the condition.": "Объект `ConditionKey` является базовым для всех условий. Конкретный набор полей зависит от **type** условия.",
    "The `ComparisonBasic` object is the base for all comparison operations. The actual set of fields depends on the **type** of the comparison.": "Объект `ComparisonBasic` является базовым для всех операций сравнения. Конкретный набор полей зависит от **type** сравнения.",
    # ── «Key» параграф (twin для CustomHostMetadataKey / CustomProcessMetadataKey) ──
    "The key of the attribute, which need dynamic keys.\n": "Ключ атрибута, требующий динамических ключей.\n",
    "Not applicable otherwise, as the attibute itself acts as a key.\n": "В остальных случаях не применяется, поскольку сам атрибут выступает в роли ключа.\n",
    # ── TagInfo description (одиночный H4-параграф) ──
    "Tag of a Dynatrace entity.\n": "Тег сущности Dynatrace.\n",
    # ── SimpleHostTech / SimpleTech description (одиночный H4-параграф) ──
    "The value to compare to.\n": "Значение для сравнения.\n",
    # ── ДЛИННЫЙ operator-description (substring-replace, longest-first) ──
    "Operator of the comparison. You can reverse it by setting **negate** to `true`.  Possible values depend on the **type** of the comparison. Find the list of actual models in the description of the **type** field and check the description of the model you need. The element can hold these values": "Оператор сравнения. Можно инвертировать, установив **negate** в `true`. Возможные значения зависят от **type** сравнения: список доступных моделей смотрите в описании поля **type** и сверяйтесь с описанием нужной модели. Поле может содержать следующие значения",
    # ── Общие фразы в табличных ячейках ──
    "The element can hold these values": "Поле может содержать следующие значения",
    "The comparison is case-sensitive (`true`) or insensitive (`false`).": "Сравнение чувствительно к регистру (`true`) или нечувствительно (`false`).",
    "The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value.": "Источник тега, например AWS или Cloud Foundry. Пользовательские теги используют значение `CONTEXTLESS`.",
    "The key of the tag.  Custom tags have the tag value here.": "Ключ тега. Для пользовательских тегов здесь располагается значение тега.",
    "The value of the tag.  Not applicable to custom tags.": "Значение тега. К пользовательским тегам не применяется.",
    "Predefined technology, if technology is not predefined, then the verbatim type must be set": "Предопределённая технология; если технология не предопределена, должен быть задан verbatim-тип",
    "Non-predefined technology, use for custom technologies.": "Не предопределённая технология, используется для пользовательских технологий.",
    "The actual key of the custom metadata.": "Фактический ключ пользовательских метаданных.",
    "The source of the custom metadata.": "Источник пользовательских метаданных.",
    "Tag of a Dynatrace entity.": "Тег сущности Dynatrace.",
    "The value to compare to.": "Значение для сравнения.",
    # ── «The key of the attribute, which need dynamic keys.  Not applicable
    #    otherwise, as the attibute itself acts as a key.» — в составе ячейки
    #    таблицы (CustomHostMetadataConditionKey/CustomProcessMetadataConditionKey
    #    dynamicKey). Подмена через две короткие фразы выше: первая «.\n» вариант
    #    для standalone-параграфа; для cell-ячейки нужна inline-форма без «\n».
    "The key of the attribute, which need dynamic keys.  Not applicable otherwise, as the attibute itself acts as a key.": "Ключ атрибута, требующий динамических ключей. В остальных случаях не применяется, поскольку сам атрибут выступает в роли ключа.",
}

# ─────────────────────────────────────────────────────────────────────────────
# Standalone single-word lines (line-level)
# ─────────────────────────────────────────────────────────────────────────────
STANDALONE_LINE_MAP = {
    "Parameters\n": "Параметры\n",
    "JSON model\n": "JSON-модель\n",
}

# Table header
TABLE_HEADER_MAP = {
    "| Element | Type | Description |\n": "| Поле | Тип | Описание |\n",
}

# Reference bullet
SHORT_MAP = {
    "* Reference\n": "* Справочник\n",
}

# ─────────────────────────────────────────────────────────────────────────────
# Tooltips (text after URL inside "...") — longest-first
# ─────────────────────────────────────────────────────────────────────────────
TOOLTIP_MAP = {
    "Find out how to define and apply tags manually and automatically.": "Узнайте, как задавать и применять теги вручную и автоматически.",
    "Use tags and metadata to organize data in your Dynatrace environment.": "Используйте теги и метаданные для упорядочивания данных в окружении Dynatrace.",
}

LINK_LABEL_MAP = {
    "Define and apply tags": "Определение и применение тегов",
    "Tags and metadata": "Теги и метаданные",
}


def _apply_longest_first(text: str, mapping: dict) -> str:
    """Substring-replace, longest key first to avoid partial-overlap conflicts."""
    for en, ru in sorted(mapping.items(), key=lambda kv: -len(kv[0])):
        text = text.replace(en, ru)
    return text


def translate(text: str) -> str:
    text = _normalize(text)
    # Длинные → короткие, по убыванию длины ключей
    # 1. PARA_MAP (длинные параграфы и intro)
    text = _apply_longest_first(text, PARA_MAP)
    # 2. Comparison + Key types (среднедлинные)
    text = _apply_longest_first(text, COMPARISON_MAP)
    text = _apply_longest_first(text, KEY_TYPE_MAP)
    # 3. H4 объекты (line-level)
    text = _apply_longest_first(text, H4_OBJECT_MAP)
    # 4. H2 / Related topics headings
    text = _apply_longest_first(text, HEADING_MAP)
    # 5. Tooltips (ДО link labels — longest-first)
    text = _apply_longest_first(text, TOOLTIP_MAP)
    # 6. Link labels (longest-first)
    text = _apply_longest_first(text, LINK_LABEL_MAP)
    # 7. Standalone single-word lines
    text = _apply_longest_first(text, STANDALONE_LINE_MAP)
    # 8. Table header
    text = _apply_longest_first(text, TABLE_HEADER_MAP)
    # 9. Reference bullet
    text = _apply_longest_first(text, SHORT_MAP)
    # 10. Published date
    text = _apply_longest_first(text, DATE_MAP)
    # 11. Title (frontmatter + H1)
    text = _apply_longest_first(text, TITLE_MAP)
    return text


def main() -> None:
    for rel in PILOT:
        en_path = EN / rel
        ru_path = RU / rel
        ru_path.parent.mkdir(parents=True, exist_ok=True)
        en_text = en_path.read_text(encoding="utf-8")
        ru_text = translate(en_text)
        ru_path.write_text(ru_text, encoding="utf-8")
        en_lines = en_text.count("\n")
        ru_lines = ru_text.count("\n")
        parity = "EXACT" if en_lines == ru_lines else f"DRIFT {en_lines}→{ru_lines}"
        print(f"[OK] {rel}: {en_lines}/{ru_lines} ({parity})")


if __name__ == "__main__":
    main()
