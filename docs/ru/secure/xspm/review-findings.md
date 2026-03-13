---
title: Review findings
source: https://www.dynatrace.com/docs/secure/xspm/review-findings
scraped: 2026-03-06T21:29:51.619326
---

# Просмотр результатов

# Просмотр результатов

* Latest Dynatrace
* How-to guide
* Updated on Oct 13, 2025

Для эффективного управления и анализа результатов проверки безопасности и соответствия требованиям вы можете [фильтровать](#filter) и [сортировать](#sort) результаты, чтобы расставить приоритеты для наиболее релевантных находок.

## Фильтрация

Выберите, какая информация должна отображаться.

### Фильтрация по стандарту

Доступны два варианта:

Из обзора

Из результатов оценки

1. Перейдите на страницу **Overview**.
2. Из списка доступных карточек стандартов соответствия выберите интересующий вас стандарт. Это перенаправит вас на страницу **Assessment results**, отфильтрованную по соответствующему стандарту.

![filter by standard](https://dt-cdn.net/images/2024-11-10-11-32-31-1491-79379f31bf.png)

1. Перейдите на страницу **Assessment results**.
2. В строке фильтра выберите **Standard** (краткое название) и/или **Standard name** (полное название стандарта), чтобы сузить результаты.

![filter by standard](https://dt-cdn.net/images/2025-10-13-15-28-08-1920-94cd4524a0.png)

### Фильтрация по системе

Доступны два варианта:

Из обзора

Из результатов оценки

1. Перейдите на страницу **Overview**.
2. В таблице **My systems** найдите и выберите интересующую вас систему. Это перенаправит вас на страницу **Assessment results**, отфильтрованную по соответствующей системе.

![filter by system](https://dt-cdn.net/images/2024-11-10-12-06-27-860-9e7c4d01d1.png)

Для выбора доступны только системы, на которых включено управление состоянием безопасности.

1. Перейдите на страницу **Assessment results**.
2. В фильтре **System** выберите интересующую вас систему.

   ![filter by system](https://dt-cdn.net/images/2025-10-13-15-34-33-1357-5c705ed4d4.png)

   Отображаются только системы, на которых включено управление состоянием безопасности.
3. Выберите **Update** рядом со строкой фильтра систем, чтобы обновить результаты на основе вашего выбора.

### Фильтрация по представлению оценки

На странице **Assessment results** используйте фильтр **Assessment view** для управления областью отображаемых правил:

* **Complete results**: отображает все правила, оценённые для выбранных систем, включая помеченные как `Not relevant`.
* **Recommended**: отображает только результаты, релевантные для вашей среды: `Failed`, `Manual` или `Passed`.

![assessment view filter](https://dt-cdn.net/images/2025-10-13-14-37-49-1920-1a11441c0c.png)

### Фильтрация по результатам, серьёзности и правилу

На странице **Assessment results** отфильтруйте интересующие вас параметры:

* [Result](concepts.md#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Failed`, `Manual`, `Passed`, `Not relevant`)
* [Severity](concepts.md#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Critical`, `High`, `Medium`, `Low`)
* Rule (полное или частичное совпадение с названием правила)

Фильтры можно комбинировать.

![combined filters](https://dt-cdn.net/images/2025-10-13-15-38-12-1920-a0e9d073f1.png)

## Сортировка

На страницах **Overview** и **Assessment results** выберите любой из столбцов со значком сортировки, чтобы изменить порядок результатов на возрастающий или убывающий по данному критерию.

![sorting](https://dt-cdn.net/images/2024-11-10-11-16-35-579-3bd762be27.png)

## Связанные темы

* [Kubernetes Security Posture Management](../../ingest-from/setup-on-k8s/deployment/security-posture-management.md "Configure and enable Security Posture Management in Kubernetes.")
