---
title: Выборочное развёртывание RUM Classic для приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout
---

# Выборочное развёртывание RUM Classic для приложений

# Выборочное развёртывание RUM Classic для приложений

* Практическое руководство
* Опубликовано 04 марта 2025

В следующих инструкциях используется настройка включения RUM на уровне приложения. Хотя [настройка включения RUM на уровне группы процессов](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring Classic for process groups.") в принципе тоже позволяет реализовать выборочное развёртывание RUM, этот подход, как правило, сложнее и более подвержен ошибкам, особенно в многоуровневых средах. По этой причине рекомендуется использовать настройку на уровне приложения.

После развёртывания OneAgent в режиме мониторинга full-stack на хосте веб-приложения, работающие на этом хосте, по умолчанию автоматически отслеживаются с помощью RUM. Это означает, что JavaScript RUM внедряется в веб-страницы, а специфичные для RUM заголовки и cookie добавляются как к HTTP-запросам, так и к ответам. Если правила определения приложений, применимые к этим веб-приложениям, ещё не заданы, захваченные данные RUM относятся к приложению-«коллектору», которое по умолчанию называется «My web application».

Однако бывают случаи, когда после развёртывания OneAgent RUM нужно развернуть более выборочно или поэтапно. Шаги для этого зависят от того, захватывала ли среда данные RUM ранее или нет. Следующие разделы описывают оба сценария.

## Если среда уже захватывала данные RUM

Если среда уже захватывала данные RUM, для выборочного развёртывания RUM выполни следующие действия.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Определить приложение-«коллектор»**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-identify-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Перенести релевантный трафик из приложения-«коллектора»**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-move-relevant-data-out-of-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Заранее отключить RUM перед развёртыванием OneAgent**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Развернуть RUM для приложения**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Шаг 1. Определить приложение-«коллектор»

Чтобы определить приложение-«коллектор»

1. Перейди в раздел **Web**.
2. В списке приложений найди **My web application**, это имя по умолчанию для приложения-«коллектора».
3. Если найти его не удаётся, возможно, кто-то его переименовал. Чтобы найти его, открой любое другое приложение и замени ID приложения в URL на `EA7C4B59F27D43EB`. Произойдёт переход на приложение-«коллектор».

### Шаг 2. Перенести релевантный трафик из приложения-«коллектора»

Для поэтапного развёртывания RUM важно, чтобы приложение-«коллектор» не содержало релевантного трафика и чтобы его отключение было безопасным. Этого можно добиться, перенеся весь релевантный трафик в одно или несколько выделенных приложений, как описано в [Определение приложений для Real User Monitoring | Рекомендуемый подход](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#automated-approach "Learn how to define your applications following the suggested, manual, or application detection rules approach.") или [Определение приложений для Real User Monitoring | Подход на основе правил определения приложений](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Убедись, что правила определения приложений используют достаточно специфичные шаблоны, позволяющие различать приложения. Например, если создаётся правило определения для `www.example.com`, использование более широкого шаблона вроде `example.com` может оказаться слишком общим, особенно если домены всех приложений компании заканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

### Шаг 3. Заранее отключить RUM перед развёртыванием OneAgent

Чтобы заранее отключить RUM для всех веб-приложений, работающих на хостах, где OneAgent ещё не развёрнут

1. Перейди в раздел **Web**.
2. Выбери приложение-«коллектор».
3. В правом верхнем углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **General settings** > **Enablement and cost control**.
5. Отключи **Enable Real User Monitoring**.

### Шаг 4 (опционально). Развернуть RUM для приложения. Опционально

Когда наступит готовность развернуть RUM для приложения, определи новое RUM-приложение, как описано в [Определение приложений для Real User Monitoring | Подход на основе правил определения приложений](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Как уже рекомендовано в шаге 2, выбирай шаблоны, достаточно специфичные для различения приложений.

## Если среда ещё не захватывала данные RUM

Если среда ещё не захватывала данные RUM, для выборочного развёртывания RUM выполни следующие действия.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Заранее отключить RUM перед развёртыванием OneAgent**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-2-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Развернуть RUM для приложения**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-2-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Шаг 1. Заранее отключить RUM перед развёртыванием OneAgent

Чтобы заранее отключить RUM для всех веб-приложений, работающих на хостах, где OneAgent ещё не развёрнут

1. Перейди в раздел **Settings**.
2. В настройках выбери **Web and mobile monitoring** > **Enablement and cost control**.
3. Отключи **Enable Real User Monitoring**.

### Шаг 2 (опционально). Развернуть RUM для приложения. Опционально

Когда наступит готовность развернуть RUM для приложения, определи новое RUM-приложение, как описано в [Определение приложений для Real User Monitoring | Подход на основе правил определения приложений](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Убедись, что правила определения приложений используют достаточно специфичные шаблоны, позволяющие различать приложения. Например, если создаётся правило определения для `www.example.com`, использование более широкого шаблона вроде `example.com` может оказаться слишком общим, особенно если домены всех приложений компании заканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

Чтобы включить RUM для только что созданного приложения

1. Перейди в раздел **Web**.
2. Выбери приложение.
3. В правом верхнем углу страницы обзора приложения выбери **More** (**…**) > **Edit**.
4. В настройках приложения выбери **General settings** > **Enablement and cost control**.
5. Включи **Enable Real User Monitoring**.