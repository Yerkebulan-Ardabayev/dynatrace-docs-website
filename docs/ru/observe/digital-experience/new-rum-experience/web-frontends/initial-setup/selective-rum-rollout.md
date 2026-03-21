---
title: Выборочное развёртывание RUM для фронтендов в новом опыте RUM
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout
scraped: 2026-03-05T21:37:59.716367
---

# Поэтапное развертывание RUM для ваших фронтендов в New RUM Experience


* Latest Dynatrace

Следующие инструкции используют настройку включения RUM на уровне фронтенда. Хотя [настройка включения RUM на уровне группы процессов](../../../web-applications/additional-configuration/rum-for-process-groups.md "Learn how to configure Real User Monitoring for process groups.") в принципе также позволяет реализовать подход поэтапного развертывания RUM, это, как правило, сложно и подвержено ошибкам, особенно в многоуровневых средах. По этой причине мы рекомендуем использовать настройку на уровне фронтенда.

После развертывания OneAgent в режиме мониторинга полного стека на хосте веб-приложения, работающие на этом хосте, по умолчанию автоматически мониторятся с помощью RUM. Это означает, что JavaScript-код RUM внедряется в веб-страницы, а специфические для RUM заголовки и cookie добавляются как к HTTP-запросам, так и к ответам. Если вы еще не определили правила обнаружения фронтендов, применимые к этим веб-приложениям, собранные данные RUM ассоциируются с фронтендом-перехватчиком, который по умолчанию имеет имя **My web application**.

Однако могут быть случаи, когда вы предпочитаете развертывать RUM более избирательно или поэтапно после установки OneAgent. Шаги для этого зависят от того, были ли в вашей среде уже собраны данные RUM или нет. Следующие разделы проведут вас через оба сценария.

## Если в вашей среде уже собраны данные RUM

Если в вашей среде уже собраны данные RUM -- даже если до сих пор это исключительно данные RUM Classic -- выполните следующие действия для реализации поэтапного развертывания RUM.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Определите ваш фронтенд-перехватчик**](selective-rum-rollout.md#method-1-identify-your-catch-all-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Переместите релевантный трафик из фронтенда-перехватчика**](selective-rum-rollout.md#method-1-move-relevant-data-out-of-your-catch-all-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Отключите RUM заранее перед развертыванием OneAgent**](selective-rum-rollout.md#method-1-disable-rum-before-deploying-oneagent "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Шаг 4 (необязательный)](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Шаг 4 (необязательный)")

**Разверните RUM для фронтенда**](selective-rum-rollout.md#method-1-roll-out-rum-for-a-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

### Шаг 1. Определите ваш фронтенд-перехватчик

Чтобы определить ваш фронтенд-перехватчик:

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. В списке фронтендов найдите **My web application** -- это имя фронтенда-перехватчика по умолчанию.
4. Если вы не можете его найти, возможно, кто-то его переименовал. Чтобы найти его, введите ID `EA7C4B59F27D43EB` в поле **Search frontends**.

### Шаг 2. Переместите релевантный трафик из фронтенда-перехватчика

Для реализации поэтапного развертывания RUM крайне важно, чтобы ваш фронтенд-перехватчик не содержал релевантного трафика и его отключение было безопасным. Вы можете добиться этого, переместив любой релевантный трафик в один или несколько выделенных фронтендов, как описано в разделе [Настройка автоматически внедряемого фронтенда в New RUM Experience](set-up-auto-injected-frontend.md "Learn how to set up an auto-injected web frontend in the New RUM Experience."). Если вы еще не включили New RUM Experience для вашего фронтенда-перехватчика, изучите собранные данные в RUM Classic.

Убедитесь, что ваши правила обнаружения фронтендов используют достаточно специфичные шаблоны для различения фронтендов. Например, если вы создаете правило обнаружения для `www.example.com`, использование более широкого шаблона, такого как `example.com`, может быть слишком общим, особенно если все домены приложений вашей компании заканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

### Шаг 3. Отключите RUM заранее перед развертыванием OneAgent

Чтобы отключить RUM заранее для всех веб-приложений, работающих на хостах, где OneAgent еще не развернут:

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите ваше приложение-перехватчик.
4. На вкладке **Settings** выберите **Enablement and cost control**.
5. Отключите **RUM Classic**. Это отключает и RUM Classic, и New RUM Experience.
6. Выберите **Save**.

### Шаг 4 (необязательный). Разверните RUM для фронтенда

Когда вы будете готовы развернуть RUM для фронтенда, определите новый фронтенд RUM и правила обнаружения фронтендов, как описано в разделе [Настройка автоматически внедряемого фронтенда в New RUM Experience](set-up-auto-injected-frontend.md "Learn how to set up an auto-injected web frontend in the New RUM Experience."). Как уже рекомендовалось на шаге 2, выбирайте шаблоны, достаточно специфичные для различения фронтендов.

## Если в вашей среде еще не собраны данные RUM

Если в вашей среде еще не собраны данные RUM, выполните следующие действия для реализации поэтапного развертывания RUM.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Отключите RUM заранее перед развертыванием OneAgent**](selective-rum-rollout.md#method-2-disable-rum-before-deploying-oneagent "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Шаг 2 (необязательный)](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Шаг 2 (необязательный)")

**Разверните RUM для фронтенда**](selective-rum-rollout.md#method-2-roll-out-rum-for-a-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

### Шаг 1. Отключите RUM заранее перед развертыванием OneAgent

Чтобы отключить RUM заранее для всех веб-приложений, работающих на хостах, где OneAgent еще не развернут:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Traffic and cost control** > **Web frontends**.
2. Отключите **Enable Real User Monitoring Classic**. Это отключает и RUM Classic, и New RUM Experience.
3. Выберите **Save changes**.

### Шаг 2 (необязательный). Разверните RUM для фронтенда

Когда вы будете готовы развернуть RUM для фронтенда, определите новый фронтенд и правила обнаружения фронтендов, как описано в разделе [Настройка автоматически внедряемого фронтенда в New RUM Experience](set-up-auto-injected-frontend.md "Learn how to set up an auto-injected web frontend in the New RUM Experience.").

Убедитесь, что ваши правила обнаружения фронтендов используют достаточно специфичные шаблоны для различения фронтендов. Например, если вы создаете правило обнаружения для `www.example.com`, использование более широкого шаблона, такого как `example.com`, может быть слишком общим, особенно если все домены приложений вашей компании заканчиваются на `example.com`. В этом случае `www.example.com` будет более точным и подходящим выбором.

Чтобы включить RUM для вашего вновь созданного фронтенда:

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите ваше приложение-перехватчик.
4. На вкладке **Settings** выберите **Enablement and cost control**.
5. Включите **RUM Classic** и **RUM**.
6. Выберите **Save**.