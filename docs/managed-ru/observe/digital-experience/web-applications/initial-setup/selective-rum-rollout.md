---
title: Выборочное развёртывание RUM для приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout
scraped: 2026-05-12T11:34:23.862043
---

# Выборочное развёртывание RUM для приложений

# Выборочное развёртывание RUM для приложений

* How-to guide
* Published Mar 04, 2025

Следующие инструкции используют настройку включения RUM на уровне приложения. Хотя [настройка включения RUM на уровне группы процессов](/managed/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring for process groups.") в принципе также позволяет реализовать подход выборочного развёртывания RUM, это может быть сложным и подверженным ошибкам — особенно в многоуровневых средах. По этой причине рекомендуется использовать настройку на уровне приложения.

После развёртывания OneAgent в режиме полного стека мониторинга на хосте веб-приложения, работающие на этом хосте, по умолчанию автоматически отслеживаются с помощью RUM. Это означает, что RUM JavaScript инжектируется в веб-страницы, а специфичные для RUM заголовки и cookie добавляются как к HTTP-запросам, так и к ответам. Если для этих веб-приложений ещё не определены правила обнаружения, захваченные RUM-данные связываются с универсальным приложением, которое по умолчанию называется «My web application».

Однако в некоторых случаях может потребоваться более выборочное или поэтапное развёртывание RUM после установки OneAgent. Последовательность действий зависит от того, были ли в среде уже захвачены RUM-данные. Следующие разделы описывают оба сценария.

## Если RUM-данные уже захвачены в среде

Если RUM-данные уже захвачены в вашей среде, выполните следующие действия для реализации выборочного развёртывания RUM.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Identify your catch-all application**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-1-identify-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Move relevant traffic out of your catch-all application**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-1-move-relevant-data-out-of-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Disable RUM in advance before you deploy OneAgent**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-1-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Roll out RUM for an application**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-1-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Шаг 1: Определите своё универсальное приложение

Чтобы определить универсальное приложение:

1. Перейдите в **Web**.
2. В списке приложений найдите **My web application** — это имя по умолчанию для универсального приложения.
3. Если приложение не найдено, возможно, оно было переименовано. Для его обнаружения откройте любое другое приложение и замените идентификатор приложения в URL на `EA7C4B59F27D43EB`. Вы будете перенаправлены на своё универсальное приложение.

### Шаг 2: Перенесите соответствующий трафик из универсального приложения

Для реализации поэтапного развёртывания RUM необходимо убедиться, что универсальное приложение не содержит значимого трафика и его отключение безопасно. Этого можно достичь, перенеся весь значимый трафик в одно или несколько выделенных приложений, как описано в разделах [Define applications for Real User Monitoring | Suggested approach](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#automated-approach "Learn how to define your applications following the suggested, manual, or application detection rules approach.") или [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Убедитесь, что правила обнаружения приложений используют шаблоны, достаточно конкретные для различения приложений. Например, если вы создаёте правило обнаружения для `www.example.com`, использование более широкого шаблона, такого как `example.com`, может быть слишком общим — особенно если все домены приложений вашей компании оканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

### Шаг 3: Заблаговременно отключите RUM перед развёртыванием OneAgent

Чтобы заблаговременно отключить RUM для всех веб-приложений, работающих на хостах, где OneAgent ещё не развёрнут:

1. Перейдите в **Web**.
2. Выберите своё универсальное приложение.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Enablement and cost control**.
5. Отключите параметр **Enable Real User Monitoring**.

### Шаг 4 (необязательный): Развёртывание RUM для приложения

Когда вы будете готовы к развёртыванию RUM для приложения, определите новое RUM-приложение, как описано в разделе [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Как уже рекомендовалось в шаге 2, выбирайте шаблоны, достаточно конкретные для различения приложений.

## Если RUM-данные ещё не захвачены в среде

Если в вашей среде RUM-данные ещё не захвачены, выполните следующие действия для реализации выборочного развёртывания RUM.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Disable RUM in advance before you deploy OneAgent**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-2-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Roll out RUM for an application**](/managed/observe/digital-experience/web-applications/initial-setup/selective-rum-rollout#method-2-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Шаг 1: Заблаговременно отключите RUM перед развёртыванием OneAgent

Чтобы заблаговременно отключить RUM для всех веб-приложений, работающих на хостах, где OneAgent ещё не развёрнут:

1. Перейдите в **Settings**.
2. В настройках выберите **Web and mobile monitoring** > **Enablement and cost control**.
3. Отключите параметр **Enable Real User Monitoring**.

### Шаг 2 (необязательный): Развёртывание RUM для приложения

Когда вы будете готовы к развёртыванию RUM для приложения, определите новое RUM-приложение, как описано в разделе [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Убедитесь, что правила обнаружения приложений используют шаблоны, достаточно конкретные для различения приложений. Например, если вы создаёте правило обнаружения для `www.example.com`, использование более широкого шаблона, такого как `example.com`, может быть слишком общим — особенно если все домены приложений вашей компании оканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

Чтобы включить RUM для нового созданного приложения:

1. Перейдите в **Web**.
2. Выберите приложение.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Enablement and cost control**.
5. Включите параметр **Enable Real User Monitoring**.