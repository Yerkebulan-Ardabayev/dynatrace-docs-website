# Документация Dynatrace: dynatrace-intelligence/copilot
Язык: Русский (RU)
Сгенерировано: 2026-03-05
Файлов в разделе: 9
---

## dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters.md

---
title: Встроенные стартовые разговоры
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters
scraped: 2026-03-03T21:32:11.784815
---

# Встроенные стартовые разговоры

# Встроенные стартовые разговоры

* Последнее Dynatrace
* Справка
* 1-минутное чтение
* Обновлено 30 января 2026 г.

Приложения Dynatrace, такие как ![Kubernetes (новое)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (новое)") **Kubernetes**, ![Уязвимости](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Уязвимости") **Уязвимости**, ![Угрозы и эксплуатация](https://dt-cdn.net/images/attacks-512-b922840b12.png "Угрозы и эксплуатация") **Угрозы и эксплуатация**, ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Управление безопасностью**, ![Базы данных](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Базы данных") **Базы данных**, и ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы** позволяют запустить предварительно определенный, контекстный запрос Dynatrace Assist для увеличения производительности и эффективности разговора.

## Предварительные условия

Чтобы получить доступ к интеграциям приложений, убедитесь в следующем:

* Dynatrace Intelligence генеративный ИИ включен на уровне окружения. Для подробностей см. [Включение Dynatrace Intelligence генеративного ИИ в вашем окружении](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").
* У вас есть разрешения на доступ к навыку рекомендаций разговора. Для подробностей см. [Разрешения пользователей](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

## Dynatrace Assist в Kubernetes

Вы можете быстро получить объяснение любых сигналов предупреждения с помощью генеративного ИИ в Kubernetes, работающего на основе **Dynatrace Assist**. Это позволяет получить представление о подробностях события, типичных коренных причинах и общих шагах по исправлению без прямого доступа к документации или другим источникам, связанным с Dynatrace.

Чтобы получить доступ к этой функциональности:

1. Перейдите на любую страницу списка в приложении Kubernetes (например, кластеры, узлы, пространства имен или рабочие нагрузки).
2. Выберите любой сигнал предупреждения, а затем выберите **Объяснить сигнал предупреждения**.
3. **Dynatrace Assist** откроется и автоматически выполнит предварительно определенный запрос.
4. Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

   * Общее объяснение события.
   * Типичные коренные причины события, начиная с наиболее распространенных.
   * Общие шаги по исправлению для каждой из коренных причин.

## Dynatrace Assist в Уязвимостях

Dynatrace Intelligence генеративный ИИ предоставляет объяснения уязвимостей для поддержки понимания и исправления.

Чтобы получить доступ к функциональности

1. В [![Уязвимости](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Уязвимости") **Уязвимости**](/docs/secure/vulnerabilities "Приоритизируйте и эффективно управляйте уязвимостями в ваших контролируемых окружениях.") выберите уязвимость.
2. В правом верхнем углу панели подробностей уязвимости выберите **Объяснить уязвимость**.

Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

* Описание уязвимости и ее основной причины
* Потенциальное воздействие и условия, при которых она может быть эксплуатирована
* Затронутые библиотеки, службы или местоположения кода
* Релевантные точки входа или пути выполнения
* Рекомендуемые действия по исправлению, такие как обновления библиотек или изменения конфигурации

Структура и уровень детализации варьируются в зависимости от типа уязвимости и доступного контекста. Объяснения адаптированы к характеристикам каждой уязвимости для поддержки оценки и исправления.

## Dynatrace Assist в Угрозах и эксплуатации

Dynatrace Intelligence генеративный ИИ может предоставить контекстные, понятные объяснения результатов обнаружения для ускорения понимания и реагирования.

Чтобы получить доступ к функциональности

1. В [![Угрозы и эксплуатация](https://dt-cdn.net/images/attacks-512-b922840b12.png "Угрозы и эксплуатация") **Угрозы и эксплуатация**](/docs/secure/threats-and-exploits "Понимайте, классифицируйте и исследуйте результаты обнаружения и оповещения.") выберите результат.
2. В правом верхнем углу панели подробностей результата выберите **Объяснить результат**.

Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

* Описание угрозы или эксплуатации и ее основные условия
* Потенциальное воздействие и вероятность эксплуатации
* Затронутые сущности и релевантные пути атаки
* Индикаторы, которые способствуют оценке угрозы
* Рекомендуемые действия для снижения уязвимости или проверки результата

Структура и уровень детализации варьируются в зависимости от типа угрозы, доступного контекста и характера эксплуатации. Объяснения адаптированы к характеристикам каждого результата для поддержки оценки и реагирования.

## Dynatrace Assist в Управлении безопасностью

Dynatrace Intelligence генеративный ИИ предоставляет объяснения оценок конфигурации для поддержки понимания результатов соответствия и неправильной конфигурации.

Чтобы получить доступ к функциональности

1. В [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Управление безопасностью**](/docs/secure/xspm "Обнаруживайте, управляйте и принимайте меры по результатам безопасности и соответствия.") на странице **Результаты оценки** выберите правило.
2. На вкладке **Оцененные ресурсы** выберите **Объяснить оценку**.

Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

* Намерение и требования правила конфигурации
* Конкретные значения конфигурации, которые привели к неудаче оценки
* Потенциальные риски безопасности или операционные риски, связанные с неправильной конфигурацией
* Затронутые ресурсы
* Рекомендуемые шаги по исправлению или корректировке конфигурации

Структура и уровень детализации варьируются в зависимости от типа правила, доступных данных конфигурации и того, является ли оценка автоматической или ручной. Объяснения адаптированы к характеристикам каждого правила для поддержки оценки и исправления.

## Dynatrace Assist в Базах данных

В **Базах данных** ![Базы данных](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Базы данных") Dynatrace Intelligence генеративный ИИ может предоставить объяснения планов выполнения, разбивку релевантных подробностей и рекомендации по улучшению производительности оператора.

Планы выполнения запросов предоставляют подробную информацию о том, как база данных будет выполнять запрос SQL. Хотя эти планы предоставляют сырые данные о том, как улучшить производительность запроса и снизить потребление ресурсов, они требуют экспертных знаний для чтения и интерпретации. С помощью интеграции генеративного ИИ непрофессиональные пользователи баз данных, такие как разработчики, получают знания, необходимые для оптимизации производительности приложения и использования базы данных.

Чтобы суммировать план выполнения с помощью генеративного ИИ:

1. В **Базах данных** ![Базы данных](https://dt-cdn.net/images/dynatrace-database-256-1afe08286e.webp "Базы данных") перейдите в **Обозреватель**.
2. В правом столбце выберите значок производительности оператора.
3. Разверните оператор, который вы хотите улучшить. Если план выполнения еще не доступен, вы можете запросить его.
4. Выберите вкладку **План выполнения** и выберите **Суммировать план выполнения**.
5. **Dynatrace Assist** откроется и автоматически выполнит предварительно определенный запрос.
6. Генеративный ИИ предоставит ответ с информацией о выбранном плане выполнения базы данных.

## Dynatrace Assist в Проблемах

В **Проблемах** ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") Dynatrace Intelligence генеративный ИИ может предоставить четкие суммирования проблем, их коренных причин и предложенных шагов по исправлению. Генеративный ИИ объясняет отдельные проблемы на ясном языке со страницы подробностей проблемы и может выполнить сравнительный анализ, когда несколько проблем выбраны из списка. Это помогает выявить общие коренные причины и предложить корректирующие шаги без привлечения команды экспертов или ожидания критических сведений.

Чтобы объяснить одну проблему с помощью генеративного ИИ

1. Перейдите на любую страницу подробностей проблемы.
2. Выберите **Объяснить** в правом верхнем углу страницы.
3. **Dynatrace Assist** откроется и автоматически выполнит предварительно определенный запрос.
4. Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

   * Объяснение того, что произошло.
   * Почему проблема возникла.
   * Действенные шаги по исправлению проблемы.

Чтобы объяснить несколько проблем с помощью генеративного ИИ

1. Перейдите на страницу списка проблем.
2. Выберите до 5 проблем.
3. Выберите **Объяснить** выше таблицы.
4. **Dynatrace Assist** откроется и автоматически выполнит предварительно определенный запрос.
5. Генеративный ИИ предоставит ответ, в котором будут подробно описаны:

   * Объяснение каждой проблемы и почему она возникла
   * Действенные шаги по исправлению проблемы
   * Любые отношения между проблемами

## Dynatrace Assist в Панелях управления

Вы можете использовать возможности DQL, чтобы интегрировать **Dynatrace Assist** в ваши [![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") плитки.

Добавив команды `| fieldsAdd prompt` и `| fieldsAdd execute`, вы можете предварительно определить и автоматически выполнить подсказки в **Dynatrace Assist**, что позволит вам быстро получить объяснение результатов запроса или получить предложения по улучшению запроса или решению проблемы.

Вы также можете предоставить дополнительную информацию **Dynatrace Assist** через дополнительный контекст, добавив следующее:

```
| parse "{\"result\":[{\"type\":\"supplementary\", \"value\":\"Символ `*` часто представляет собой чувствительные данные, которые были замаскированы\"}]}", "LD JSON_ARRAY:contexts"



// или для динамического контекста
```

Хотя дополнительный контекст скрыт в интерфейсе чата, он может помочь генеративному ИИ предоставить лучшие ответы для вашего случая. Например, вы можете попросить **Dynatrace Assist** использовать информацию из определенного поля при ответе на вашу подсказку:

```
| fieldsAdd supplementaryContext = concat("{\"result\":[{\"type\":\"supplementary\", \"value\":\"Используйте следующую информацию для ответа на вопрос: ", record.summary, "\"}]}")



| parse supplementaryContext , "LD JSON_ARRAY:contexts"
```

Чтобы интегрировать **Dynatrace Assist** в ваши [![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") плитки

1. Перейдите в [![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени.") и откройте панель, которую можно редактировать.
2. Выберите плитку панели, содержащую запрос DQL.
3. Выберите **Редактировать**, чтобы открыть меню редактирования справа.
4. В разделе **DQL** меню редактирования добавьте следующее в ваш стандартный запрос:

   ```
   | fieldsAdd prompt = concat("{ваш вопрос}",  your.field.name)



   | fieldsAdd execute = true
   ```

   * Если вы хотите предварительно определить подсказку без автоматического выполнения, удалите `| fieldsAdd execute = true`.
   * Эта интеграция не работает для запросов с командой `makeTimeseries`.

Чтобы открыть интегрированный **Dynatrace Assist**

1. Выберите  рядом с выбранным вами полем.
2. Выберите **Открыть с помощью...** >  **Задать вопрос**.

Если вы добавили `| fieldsAdd execute = true` в ваш запрос, предварительно определенная подсказка будет выполнена сразу после открытия **Dynatrace Assist**. В противном случае вы сможете изменить или отредактировать подсказку в окне сообщения перед ручным выполнением.

## Dynatrace Assist в тетрадях

Вы можете использовать возможности DQL, чтобы интегрировать **Dynatrace Assist** в ваши [![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.").

Добавив команды `| fieldsAdd prompt` и `| fieldsAdd execute`, вы можете предварительно определить и автоматически выполнить подсказки в **Dynatrace Assist**, что позволит вам быстро получить объяснение результатов запроса или получить предложения по улучшению запроса или решению проблемы.

Вы также можете предоставить дополнительную информацию **Dynatrace Assist** через дополнительный контекст, добавив следующее:

```
| parse "{\"result\":[{\"type\":\"supplementary\", \"value\":\"Символ `*` часто представляет собой чувствительные данные, которые были замаскированы\"}]}", "LD JSON_ARRAY:contexts"



// или для динамического контекста
```

Хотя дополнительный контекст скрыт в интерфейсе чата, он может помочь генеративному ИИ предоставить лучшие ответы для вашего случая. Например, вы можете попросить **Dynatrace Assist** использовать информацию из определенного поля при ответе на вашу подсказку:

```
| fieldsAdd supplementaryContext = concat "{\"result\":[{\"type\":\"supplementary\", \"value\":\"Используйте следующую информацию для ответа на вопрос: ", record.summary, "\"}]}")



| parse supplementaryContext , "LD JSON_ARRAY:contexts"
```

Чтобы интегрировать **Dynatrace Assist** в ваши [![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.").

1. Перейдите в [![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь идеями из ваших данных наблюдаемости — все в одном совместном, настраиваемом рабочем пространстве.") и откройте тетрадь, которую можно редактировать.
2. Выберите раздел тетради, содержащий запрос DQL.
3. Выберите поле запроса и добавьте следующее в ваш стандартный запрос:

   ```
   | fieldsAdd prompt = concat("{ваш вопрос}",  your.field.name)



   | fieldsAdd execute = true
   ```

   * Если вы хотите предварительно определить подсказку без автоматического выполнения, удалите `| fieldsAdd execute = true`.
   * Эта интеграция не работает для запросов с командой `makeTimeseries`.

Чтобы открыть интегрированный **Dynatrace Assist**

1. Выберите  рядом с выбранным вами полем.
2. Выберите **Открыть с помощью...** >  **Задать вопрос**.

Если вы добавили `| fieldsAdd execute = true` в ваш запрос, предварительно определенная подсказка будет выполнена сразу после открытия **Dynatrace Assist**. В противном случае вы сможете изменить или отредактировать подсказку в окне сообщения перед ручным выполнением.

## Обратная связь

Если у вас есть какие-либо замечания, вы можете предоставить их直接 в окне чата. Для получения дополнительной информации см. [Оставить обратную связь](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot#feedback "Задайте вопросы на естественном языке и получите быстрые ответы от Dynatrace Assist, вашего генеративного помощника ИИ.").

## Связанные темы

* [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.")
* [Часто задаваемые вопросы о Dynatrace Intelligence генеративном ИИ](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")

---

## dynatrace-intelligence/copilot/chat-with-davis-copilot.md

---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-03-02T21:33:22.887033
---

# Dynatrace Assist

# Dynatrace Assist

* Последнее Dynatrace
* Приложение
* 2-минутное чтение
* Обновлено 11 февраля 2026 г.

**Dynatrace Assist** позволяет вам общаться с Dynatrace Intelligence и задавать вопросы о данных в вашей среде, а также общие вопросы, чтобы помочь вам с настройкой Dynatrace и пониманием наших основных концепций.

### Разрешения

В следующей таблице описаны необходимые разрешения.

document:documents:write

хранить разговоры в хранилище документов

document:documents:read

читать разговоры из хранилища документов

document:documents:delete

удалять разговоры из хранилища документов

davis-copilot:conversations:execute

использовать функцию разговора с пилотом

hub:catalog:read

чтение каталога для отображения приложения, которое запустило разговор

davis-copilot:nl2dql:execute

использовать функцию агента пилота

davis-copilot:dql2nl:execute

использовать функцию агента пилота

mcp-gateway:servers:invoke

использовать функцию агента пилота

mcp-gateway:servers:read

использовать функцию агента пилота

davis:analyzers:read

использовать функцию агента пилота

Чтобы использовать **Dynatrace Assist** с функциями генеративного ИИ, вам необходимы только следующие разрешения:

* `document:documents:write`
* `document:documents:read`
* `document:documents:delete`
* `davis-copilot:conversations:execute`
* `hub:catalog:read`

Остальные разрешения в таблице необходимы только в том случае, если вы хотите использовать все возможности агентного Dynatrace Assist. Для получения дополнительной информации см. [Разрешения агентного Dynatrace Assist](#assist-agentic-permissions).

Для получения дополнительной информации см. [Начало работы с Dynatrace Intelligence генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence генеративный ИИ.").

## Начало работы

![Начните работать быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/efd72baf-d142-45ee-b52a-51aea2450093.png)![Попросите Dynatrace Assist суммировать все открытые проблемы, чтобы получить быстрый обзор вашей среды.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/8d9a51ac-e9a7-4152-9158-235e6e1fef66.png)![Попросите Dynatrace Assist объяснить ваши журналы, чтобы быстро получить информацию, потенциальное влияние, вероятные причины и рекомендуемые следующие шаги.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/e9aa5b44-ceb3-4113-894c-4cdc32f5d94e.png)![Получите помощь в выявлении и исправлении уязвимостей, таких как SQL-инъекции.](https://cdn.hub.central.dynatrace.com/hub/console/dynatrace.davis.copilot/media/9282285e-db29-48d0-b368-92ac20460a5f.png)

1 из 4Начните работать быстро и легко, задав Dynatrace Assist вопрос. Попробуйте один из примеров, чтобы увидеть, что возможно.

### Использование интерфейса разговора Dynatrace Assist

После включения Dynatrace Intelligence генеративного ИИ в вашей среде и настройки разрешений пользователя, вы должны увидеть новую иконку ниже **Поиск** в доке.

1. В Dynatrace, выберите **Dynatrace Assist**.
2. Откроется новое окно с интерфейсом разговора.
3. Введите свой вопрос. См. [Примеры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.") для вдохновения.
4. Выберите **Выполнить** ![Выполнить](https://dt-cdn.net/images/run-c2f8c2f63c.svg "Выполнить") и подождите, пока ответ будет сгенерирован.

* Вы можете задавать дополнительные вопросы.
* Каждый ответ содержит список источников, которые были получены для генерации ответа. Вы можете ознакомиться с этими [источниками](#sources) для получения дополнительной информации.
* Разговоры сохраняются автоматически. Их можно переименовать или удалить из списка разговоров.
* Вы можете отменить генерацию ответа, уточнить свою подсказку и затем повторно отправить вопрос.
* Вы можете использовать интерфейс разговора поверх любого приложения.

Ответы генерируются на основе ресурсов, связанных с Dynatrace. Если модель не может ответить на ваш вопрос, вы увидите сообщение об ошибке:

* Извините, но я не могу ответить на этот запрос. Пожалуйста, попробуйте перефразировать его или добавить дополнительный контекст.

### Использование агентного Dynatrace Assist

**Dynatrace Assist** позволяет вам использовать Dynatrace агентный ИИ и [инструменты и возможности MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.") для доступа и анализа данных вашей среды и использования их для выполнения задач (таких как перечисление проблем или генерация и выполнение запросов DQL) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** делится некоторой дополнительной информацией, такой как результаты вызовов инструментов, с поставщиками предприятий, которые размещают LLM, на основе которых построены Dynatrace агентный и генеративный ИИ. Для получения дополнительной информации о третьих сторонах см. [Используется ли моя информация для обучения Dynatrace Intelligence генеративного ИИ?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Узнайте о часто задаваемых вопросах и найдите ответы.").

С включенным агентным ИИ вы можете попросить **Dynatrace Assist** проанализировать и предоставить информацию о данных и безопасности вашей среды. Для примеров см. [Спросите о данных в вашей среде](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts#assist-ask-about-the-data "Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.").

#### Разрешения агентного Dynatrace Assist

**Dynatrace Assist** уважает ваши разрешения пользователя. Это означает, что все вызовы агентного **Dynatrace Assist** выполняются в рамках ваших разрешений пользователя, и результаты не будут включать ничего вне этого.

Чтобы использовать агентный **Dynatrace Assist**, вам необходимо:

* Иметь достаточные разрешения.
* Включить агентный ИИ для **Dynatrace Assist**. Чтобы включить агентный ИИ:

  1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** > **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
  2. Убедитесь, что **Включить генеративный ИИ** включен.
  3. Включите **Включить агентный ИИ**.

Агентный **Dynatrace Assist** может быть недоступен для вас, если вы не соответствуете вышеуказанным предварительным требованиям или если вы доступ к **Dynatrace Assist** из [Встроенных запускаемых разговоров](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запускать предопределенные подсказки в различных приложениях Dynatrace.").

Вам также потребуются дополнительные разрешения для вызова инструментов агентного ИИ. Для списка инструментов и необходимых им разрешений см. [Инструменты MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и том, как вы можете подключиться к нему.").

#### Маскирование ПII

Агентный **Dynatrace Assist** не предоставляет никакого маскирования ПII. Чтобы защитить ваши данные, когда **Dynatrace Assist** обнаруживает ПII в подсказке пользователя, запрос автоматически блокируется и подсказка не отправляется в LLM для обработки.

#### Вызов нескольких инструментов

При взаимодействии с **Dynatrace Assist** в агентном режиме **Assist** может вызвать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** вызвать более 10 инструментов одновременно, он не сможет выполнить взаимодействие.

### Оставить отзыв

Вы можете оставить отзыв, используя встроенный механизм отзыва.

Выберите ![Большой палец вверх](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Большой палец вверх"), если Dynatrace Assist сгенерировал ответ, который соответствует вашим ожиданиям и правильно интерпретировал вашу подсказку.

Выберите ![Большой палец вниз](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Большой палец вниз"), если Dynatrace Assist сгенерировал ответ, который не соответствует вашим ожиданиям или неправильно интерпретировал вашу подсказку. Пожалуйста, предоставьте дополнительный контекст, чтобы мы могли понять, как улучшить эту функцию, чтобы она соответствовала вашим потребностям и ожиданиям.

Ваш отзыв не используется для автоматического обучения моделей. Он рассматривается только командой продукта для мониторинга качества ответов и улучшения основного продукта.

### Источники, использованные для генерации ответов

**Dynatrace Assist** обогащает свои ответы на основе официальных источников Dynatrace, таких как:

* Документация Dynatrace
* [Разработчик Dynatrace](https://developer.dynatrace.com/)
* [Сообщество Dynatrace](https://community.dynatrace.com/)
* [Хаб Dynatrace](https://www.dynatrace.com/hub/)
* [Новости и ресурсы Dynatrace](https://www.dynatrace.com/news/product-news/)
* [Сайт Dynatrace](https://www.dynatrace.com/)

## Концепции

Пройдите следующий процесс, чтобы научиться использовать **Dynatrace Assist**

[01Встроенные запускаемые разговоры

* Справка
* Узнайте, как запускать предопределенные подсказки в различных приложениях Dynatrace.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)[02Примеры подсказок Dynatrace Assist

* Справка
* Узнайте, какие типы подсказок работают хорошо в Dynatrace Assist.](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts)

## Сценарии использования

Вы можете использовать агентный **Dynatrace Assist** для:

* Задания общих вопросов о продукте Dynatrace.
* Использования инструментов и возможностей MCP.
* Выполнения задач без необходимости открывать приложение или перехода к другому приложению.
* Объединения инструментов в одном запросе для выполнения нескольких задач.
* Объединения инструментов для выполнения задач и получения ответов на общие вопросы одновременно.

## Связанные темы

* [Начало работы с Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence generative AI.")
* [Встроенные стартовые разговоры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace. ")
* [Часто задаваемые вопросы о Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.")
* [Сервер Dynatrace MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp "Узнайте о сервере Dynatrace MCP и о том, как можно к нему подключиться.")

---

## dynatrace-intelligence/copilot/copilot-data-privacy.md

---
title: Dynatrace Intelligence agentic and generative AI data privacy and security
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-data-privacy
scraped: 2026-03-04T21:31:24.088421
---

# Dynatrace Intelligence agentic and generative AI data privacy and security

# Dynatrace Intelligence agentic and generative AI data privacy and security

* Latest Dynatrace
* Explanation
* 3-min read
* Updated on Jan 28, 2026

At Dynatrace, we take our responsibility to safeguard your data seriously. Understand how Dynatrace Intelligence agentic and generative AI uses your data and understand your responsibility to keep your data secure.

## Prompt data

Although we mask Personally Identifiable Information (PII), we still recommend exercising caution when including personal or confidential information in your prompts.

Your prompts are sent to LLMs hosted by enterprise vendors such as Microsoft Azure AI and AWS Bedrock, which power Dynatrace Intelligence agentic and generative AI. Enterprise vendors don't store the data you submit or the responses you receive. The prompts you submit and the responses you receive are used only to serve your experience. Enterprise vendors also don't use the prompts to fine-tune or improve any models or services, or to train models across customers or environments.

Each data request is sent to the LLM individually, over an SSL-encrypted service, processed by respective enterprise vendors, and sent back to Dynatrace. If your environment is located in EMEA, your prompts are processed in an EU region. If your environment is located in NORAM, LATAM, or APAC, your prompts are processed in a US region.

Dynatrace may store the prompts submitted to Dynatrace Intelligence agentic and generative AI and the responses provided by the LLMs to understand the use cases, contextualize the feedback on the responses, and identify additional user expectations.

Learn more about the [Dynatrace Intelligence agentic and generative AI architecture and data flow](/docs/dynatrace-intelligence/copilot/copilot-overview#copilot-data-flow "Learn about data security and other aspects of Dynatrace Intelligence agentic and generative AI.").

## PII masking

Dynatrace version 1.305+

PII masking is in place for user prompts interacting with all standard generative AI functionality. This ensures that sensitive information included in your prompts won't be forwarded to LLMs hosted by enterprise vendors.

Currently masked fields include:

* Email address
* Phone number
* IBAN information
* Credit card number
* IP address
* US bank number
* US social security number
* US ABA routing numbers
* URL query parameters (only parameters with more than two characters are considered)
* Canadian Social Insurance Number (SIN)

In our logs and calls to LLM models, we replace values from the identified patterns above with fake patterns. This means that you'll be able see IBANs in logs, for example, but they'll be made up of random numbers, replacing the original values included in your prompts.

Agentic  **Dynatrace Assist** doesn't provide any PII masking. In order to protect your data, when  **Dynatrace Assist** detects PII in the user prompt, the request is automatically blocked and the prompt isn't sent to the LLM for processing.

## Related topics

* [Dynatrace Intelligence agentic and generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence agentic and generative AI.")
* [Get started with Dynatrace Intelligence agentic and generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence agentic and generative AI.")
* [Dynatrace Intelligence agentic and generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")

---

## dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides.md

---
title: Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence агентного и генеративного ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides
scraped: 2026-03-05T21:14:19.401741
---

# Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence агентного и генеративного ИИ

# Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence агентного и генеративного ИИ

* Последнее Dynatrace
* Учебник
* Обновлено 28 января 2026 г.

Dynatrace Intelligence агентный и генеративный ИИ помогает вам быстрее решать проблемы, автоматически выделяя релевантные руководства по устранению неполадок, такие как тетради или панели управления, созданные вашей командой.

Чтобы уменьшить среднее время ремонта (MTTR), вы можете использовать предложения документов Dynatrace Intelligence агентного и генеративного ИИ в приложении ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы**, чтобы проверить, создала ли ваша команда какие-либо руководства по устранению неполадок для проблем, подобных той, с которой вы столкнулись.

## Для кого это

Эта статья предназначена для всех пользователей, которые хотят быстро и эффективно устранять и исправлять активные проблемы в своей среде.

## Что вы узнаете

В этой статье вы узнаете, как Dynatrace Intelligence агентный и генеративный ИИ может предложить релевантные руководства по устранению неполадок, чтобы помочь в решении проблем.

## Прежде чем начать

Dynatrace Intelligence агентный и генеративный ИИ периодически индексирует тетради и панели управления, которые были помечены как руководства по устранению неполадок и共享ены в среде.

* По умолчанию, семантическая векторная индексация руководств происходит каждые 6 часов.
* Чтобы Dynatrace Intelligence агентный и генеративный ИИ мог индексировать и предлагать ваш документ, вы должны поделиться им со всеми пользователями в вашей среде. Dynatrace Intelligence агентный и генеративный ИИ не будет индексировать или предлагать какие-либо приватные документы или документы, поделиться которыми можно только с конкретными пользователями. Чтобы узнать больше о поделиться документами, см. [Поделиться документами](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Поделиться документами Dynatrace (панелями управления, тетрадями и запусками) с другими пользователями Dynatrace в вашей компании.").

### Предварительные знания

* [Обзор Dynatrace Intelligence агентного и генеративного ИИ](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence агентного и генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence агентным и генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence агентный и генеративный ИИ.")
* [Приложение Проблемы](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро добраться до коренной причины инцидентов в вашей среде.")

### Предварительные условия

* Окружение Dynatrace SaaS.
* Вы завершили настройку Dynatrace Intelligence агентного и генеративного ИИ, описанную в [Начало работы с Dynatrace Intelligence агентным и генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence агентный и генеративный ИИ.").
* У вас включены предложения документов в вашей среде. Включение индексации документов является частью руководства [Включить Dynatrace Intelligence агентный и генеративный ИИ в вашей среде](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Узнайте, как настроить Dynatrace Intelligence агентный и генеративный ИИ.").
* У вас есть разрешение `ALLOW davis-copilot:document-search:execute;`. Чтобы узнать, как настроить разрешения, см. [Разрешения в Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Узнайте, как назначить разрешения для бакетов и таблиц в Grail.").

## Получить предложения документов для решения проблем

1. Перейдите в приложение ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы** и откройте проблему, которую необходимо решить.
2. На странице деталей проблемы выберите **Устранение неполадок**. Вы сможете увидеть любые руководства по устранению неполадок, которые вы создали для проблемы, а также любые релевантные документы, предложенные Dynatrace Intelligence агентным и генеративным ИИ.

   Dynatrace Intelligence агентный и генеративный ИИ индексирует только документы, которые распознаются как руководства по устранению неполадок. Панели управления и тетради, созданные直接 из приложения ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы**, автоматически распознаются как руководства по устранению неполадок и не требуют префикса `[TSG]`.

   Если вы создаете руководство по устранению неполадок напрямую из ![Панели управления](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели управления") **Панели управления** или ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради**, вы должны добавить префикс `[TSG]` к названию документа, чтобы указать, что это руководство по устранению неполадок.

   Независимо от того, как был создан документ, он должен быть поделен на уровне среды, чтобы быть проиндексированным Dynatrace Intelligence агентным и генеративным ИИ.
3. Необязательно Введите ключевые слова или часть ключевого слова в поле поиска **Имя**, чтобы отфильтровать предложенные документы по имени.
4. Необязательно Выберите **Тип** (`Тетради`, `Панели управления`), чтобы отфильтровать предложенные документы по типу. По умолчанию, оба типа выбраны для предложений документов.
5. Выберите **Просмотр...** на документ, который вы хотите просмотреть. Это действие перенесет вас к руководству по устранению неполадок для дальнейшего расследования.

## Закрепить документы непосредственно к проблеме

Когда вы создаете документ из страницы деталей проблемы, он автоматически закрепляется к этой конкретной проблеме. Закрепленные документы не включены в список предложенных документов. Вместо этого, руководства по устранению неполадок связаны с проблемой, из которой они были созданы. Это гарантирует, что документы, созданные в проблеме, остаются прикрепленными и предотвращает сценарии, в которых ИИ может исключить их из предложенного списка из-за отсутствия сходства.

Документы закрепляются к проблемам, установкой поля `id` в хранилище документов. Шаблон, используемый для закрепления проблем, состоит из:

* Строки `problem-TSG`.
* Тире `-`.
* Идентификатора проблемы (`event.id` в записи Проблемы Grail).
* Тире `-`.
* Случайного UUID, представленного строкой.

Вы можете увидеть общий шаблон в примере ниже:

`problem-TSG-{problem_ID}-{random-UUID}`

Поскольку подчеркивание `_` в идентификаторе проблемы не поддерживается идентификатором документа, оно должно быть заменено тире `-`, как показано в примере ниже:

`problem-TSG-1589269324049748129-1747888020000V2-225b65bd-ab67-4efe-9d71-742de9b87387`

Случайный UUID, добавленный в конец шаблона, гарантирует уникальность каждого документа и позволяет нескольким документам быть закрепленными к одной и той же проблеме без конфликтов.

Закрепление документов к проблемам позволяет вам прикрепить дополнительные результаты анализа и специфические знания непосредственно к обнаруженным проблемам. Вы можете закрепить документ к проблеме через рабочие процессы или API для бесшовной внешней интеграции.

### Создать и прикрепить тетрадь к обнаруженной проблеме через Рабочие процессы

Используя действие рабочего процесса JavaScript, вы можете автоматически создать и прикрепить документ (тетрадь или панель управления) со своими специфическими результатами анализа к обнаруженной проблеме.

1. Перейдите в **Рабочие процессы** ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Рабочие процессы") и выберите , чтобы создать новый рабочий процесс.
2. Выберите предпочитаемый тип триггера.
3. Выберите  **Добавить задачу**.
4. В разделе **Выберите действие** выберите **Выполнить JavaScript**.
5. В разделе **Ввод** введите следующий скрипт:

   ```
   import { documentsClient } from "@dynatrace-sdk/client-document";



   import { credentialVaultClient } from '@dynatrace-sdk/client-classic-environment-v2';



   import { execution } from '@dynatrace-sdk/automation-utils';



   function generateGUID() {



   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c)?



   const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);



   return v.toString(16);



   });



   }



   export default async function ()?



   const ex = await execution();



   const problem_event = ex.params.event;



   var problem_id = problem_event['event.id'];



   problem_id = problem_id.replace('_', '-'); // Замените неподдерживаемый символ



   // Создайте новую тетрадь и закрепите ее к обнаруженной проблеме



   try?



   const notebookContent =?



   defaultTimeframe: { from: "now()-2h", to: "now()" },?



   defaultSegments: [],?



   sections:?



   {"id":"19ebed94-69a9-4a6e-b392-7bb7b0deb330","type":"markdown","markdown":"# Результаты анализа домена\n\nЗдесь находятся внешние, специфические результаты анализа"?



   ],?



   };



   const generatedNotebook = await documentsClient.createDocument?



   body?



   name: "[TSG] Результаты анализа домена",?



   type: "notebook",?



   description: "Тетрадь, содержащая специфические результаты анализа домена",?



   id: "problem-TSG-" + problem_id + "-" + generateGUID(),?



   content: new Blob([JSON.stringify(notebookContent)], { type: "application/json" }),?



   },?



   });



   // Сделайте документ публичным



   const updated = await documentsClient.updateDocument?



   id: generatedNotebook.id,



   optimisticLockingVersion: generatedNotebook.version,



   body?



   isPrivate: false,



   }



   } catch (error)?



   console.error("Ошибка создания тетради:", error);



   }



   return { };



   }
   ```

Как только созданная тетрадь будет прикреплена к обнаруженной проблеме, вы сможете увидеть ее в разделе устранения неполадок. Документ также будет предложен вам для подобных проблем в будущем.

![Пример результатов анализа в приложении Проблемы.](https://dt-cdn.net/images/problems-analysis-results-2147-303c6e5b9b.png)

## Связанные темы

* [Dynatrace Intelligence агентное и генеративное ИИ обзор](/docs/dynatrace-intelligence/copilot/copilot-overview "Узнайте о безопасности данных и других аспектах Dynatrace Intelligence агентного и генеративного ИИ.")
* [Начало работы с Dynatrace Intelligence агентным и генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence агентное и генеративное ИИ.")
* [Проблемы приложения](/docs/dynatrace-intelligence/davis-problems-app "Используйте приложение Проблемы, чтобы быстро найти коренную причину инцидентов в вашей среде.")

---

## dynatrace-intelligence/copilot/copilot-getting-started.md

---
title: Начало работы с Dynatrace Intelligence агентным и генеративным ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-03-05T21:23:14.793631
---

# Начало работы с Dynatrace Intelligence агентным и генеративным ИИ

# Начало работы с Dynatrace Intelligence агентным и генеративным ИИ

* Последнее Dynatrace
* Руководство по началу работы
* 3-минутное чтение
* Обновлено 03 марта 2026 г.

Dynatrace Intelligence агентный и генеративный ИИ включен на уровне учетной записи по умолчанию, что означает, что все ваши среды автоматически имеют доступ к нему. Однако функциональность ИИ должна быть включена на уровне среды через страницу настроек, которая предлагает вам полный контроль над тем, как Dynatrace Intelligence агентный и генеративный ИИ включен и настроен в вашей среде.

## Включение Dynatrace Intelligence генеративного ИИ в вашей среде

Чтобы включить Dynatrace Intelligence генеративный ИИ в вашей среде

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить генеративный ИИ**.

![Включение генеративного ИИ в настройках](https://dt-cdn.net/images/generative-ai-settings-1913-24ab3b085b.png)

Если вы не видите страницы настроек, убедитесь, что у вас есть политики `Setting Reader` и `Setting Writer`. Для получения дополнительной информации см. [разрешения на чтение и запись](/docs/manage/identity-access-management/use-cases/access-settings#example-read-and-write-permissions "Предоставление доступа к настройкам").

### Разрешения пользователей

После включения Dynatrace Intelligence генеративного ИИ на уровне среды вам все равно придется предоставить доступ к различным навыкам генеративного ИИ вашим пользователям. Для этого необходимо привязать группу, к которой они принадлежат, к политике с следующим утверждением, которое позволяет доступ к генеративному ИИ:

* **Перевод естественного языка в DQL** (`ALLOW davis-copilot:nl2dql:execute;`)
* **Перевод DQL в естественный язык** (`ALLOW davis-copilot:dql2nl:execute;`)
* **Рекомендатель по разговорам** (`ALLOW davis-copilot:conversations:execute;`)

Для получения дополнительной информации о управлении вашими политиками см. [Управление политиками IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Создание, редактирование, копирование и удаление политик IAM для управления разрешениями пользователей Dynatrace").

## Включение агентного ИИ для Dynatrace Assist

**Dynatrace Assist** позволяет вам использовать Dynatrace агентный ИИ и [инструменты и возможности MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и о том, как вы можете подключиться к нему.") для доступа и анализа данных вашей среды и использования их для выполнения задач (таких как перечисление проблем или генерация и выполнение запросов DQL) в дополнение к ответам на общие вопросы о Dynatrace.

Агентный **Dynatrace Assist** делится некоторой дополнительной информацией, такой как результаты вызовов инструментов, с корпоративными поставщиками, которые размещают LLM, на основе которых построены Dynatrace агентный и генеративный ИИ. Для получения дополнительной информации о третьих сторонах см. [Используется ли моя информация для обучения Dynatrace Intelligence генеративному ИИ?](/docs/dynatrace-intelligence/copilot/copilot-faq#copilot-training-on-data "Узнайте о часто задаваемых вопросах и найдите ответы на них").

Чтобы использовать агентный **Dynatrace Assist**, вам необходимо

* Иметь достаточные разрешения.
* Иметь агентный ИИ, включенный для **Dynatrace Assist**. Чтобы включить агентный ИИ

  1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
  2. Убедитесь, что **Включить генеративный ИИ** включен.
  3. Включите **Включить агентный ИИ**.

Агентный **Dynatrace Assist** может быть недоступен для вас, если вы не соответствуете вышеуказанным предварительным требованиям или если вы доступ к **Dynatrace Assist** из [встроенных стартовых разговоров](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные подсказки в различных приложениях Dynatrace").

### Разрешения агентного Dynatrace Assist

Вам также понадобятся дополнительные разрешения для вызова инструментов агентного ИИ. Для списка инструментов и необходимых им разрешений см. [инструменты MCP](/docs/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp#server "Узнайте о сервере Dynatrace MCP и о том, как вы можете подключиться к нему.").

### Маскирование ПII

Агентный **Dynatrace Assist** не предоставляет никакого маскирования ПII. Чтобы защитить ваши данные, когда **Dynatrace Assist** обнаруживает ПII в запросе пользователя, запрос автоматически блокируется и запрос не отправляется в LLM для обработки.

### Вызов нескольких инструментов

При взаимодействии с агентным **Dynatrace Assist** он может вызывать до 10 внутренних инструментов MCP за один ответ. Если ваш запрос требует от **Dynatrace Assist** вызвать более 10 инструментов одновременно, он не сможет завершить взаимодействие.

## Доступ к данным на основе пользователей

Dynatrace Intelligence агентный и генеративный ИИ уважает привилегии и разрешения пользователей. Это означает, что

* Он может предоставлять разные ответы разным пользователям на основе их прав доступа.
* Все вызовы агентного **Dynatrace Assist** выполняются в рамках прав доступа пользователя, и результаты не будут включать ничего вне его.

## Включение предложения документов

Предложение документов — это навык Dynatrace Intelligence агентного и генеративного ИИ, который позволяет ему рекомендовать вам руководства по устранению неполадок, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов** на основе векторной подобия. Вы можете использовать предложение документов Dynatrace Intelligence агентного и генеративного ИИ в ![Проблемы - новое](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Проблемы - новое") **Проблемы**, чтобы быстро получить руководства по устранению неполадок, написанные вами или вашей командой для подобных проблем, и уменьшить среднее время ремонта (MTTR).

Если вы хотите, чтобы Dynatrace Intelligence агентный и генеративный ИИ предлагал руководства по устранению неполадок для подобных или повторяющихся проблем, вам необходимо разрешить ему искать и индексировать документы, созданные в ![Тетради](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Тетради") **Тетради** и ![Панели приборов](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Панели приборов") **Панели приборов**, и общие со всеми пользователями в вашей среде. Чтобы обеспечить полный контроль над безопасностью ваших данных, эта функциональность является опциональной и выключена по умолчанию.

Чтобы Dynatrace Intelligence агентный и генеративный ИИ мог индексировать и предлагать ваш документ, он должен быть общим со всеми пользователями в вашей среде. Dynatrace Intelligence агентный и генеративный ИИ не будет индексировать или предлагать никакие частные документы или документы, общие только с определенными пользователями. Чтобы узнать больше о обмене документами, см. [Обмен документами](/docs/discover-dynatrace/get-started/dynatrace-ui/share "Обмен документами Dynatrace (панелями приборов, тетрадями и запусками) с другими пользователями Dynatrace в вашей компании.").

Чтобы включить предложение документов

1. Перейдите к ![Настройки](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Настройки") **Настройки** >  **Dynatrace Intelligence** > **Генеративный и агентный ИИ**.
2. Включите **Включить предложения документов**, чтобы разрешить Dynatrace Intelligence агентному и генеративному ИИ ингестировать руководства по устранению неполадок и предлагать их вам.

По умолчанию Dynatrace Intelligence агентный и генеративный ИИ индексирует руководства по устранению неполадок каждые 6 часов.

### Семантическое векторное индексирование

Dynatrace Intelligence агентный и генеративный ИИ использует семантическое векторное индексирование, чтобы предлагать соответствующие панели приборов и тетради по устранению неполадок, общие в среде. Он непрерывно индексирует содержимое панелей приборов и тетрадей, признанных руководствами по устранению неполадок. Когда пользователь доступ к представлению устранения неполадок для конкретной проблемы, генеративный ИИ сравнивает описание проблемы с индексированными данными, используя семантическое подобие, чтобы предлагать наиболее релевантные руководства.

Этот процесс основан на векторных представлениях как описания проблемы, так и индексированного содержимого документа или панели приборов. Чем меньше семантическое расстояние между описанием проблемы и документом, тем выше его релевантность. Это означает, что документ с большей вероятностью будет предложен Dynatrace Intelligence агентным и генеративным ИИ в качестве релевантного руководства по устранению неполадок.

## Включение запросов, осведомленных о среде



Environment-aware queries can enrich Dynatrace Intelligence agentic and generative AI with your environment's data. This lets you generate more accurate queries that identify and reference relevant entities, events, spans, logs, and metrics from your environment.

If you want Dynatrace Intelligence agentic and generative AI to be aware of the details and structures of your environment's data, you'll need to allow access to Grail. To ensure you have full control over the security of your data, this functionality is opt-in, and admin users can specify which data tables and buckets Dynatrace Intelligence agentic and generative AI is not allowed to access.

To enable environment-aware queries

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Turn on **Enable environment-aware queries**.

It can take up to 24 hours for Dynatrace Intelligence agentic and generative AI to build or amend the semantic index after changes are made. If environment-aware queries are disabled and the semantic index already exists, Dynatrace Intelligence agentic and generative AI purges all environment-specific data within 24 hours, and returns to using publicly available sources for building DQL queries. The semantic index is stored only on your Dynatrace tenant.

To learn more about semantic indexing and environment-aware queries, see [Environment-aware queries](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#environment-aware-queries "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries").

### Configure your data access

After enabling environment-aware queries, you'll be able to see the settings for configuring data that Dynatrace Intelligence agentic and generative AI isn't allowed to access.

To configure your data access

1. Go to **Configure data access**.
2. Select **Add a new rule**.
3. Select the type of data you want to exclude from Dynatrace Intelligence access in the **Type** field.
4. Type the name of the bucket or table in the **Name** field.
5. Select **Save changes**.

## Related topics

* [Dynatrace Intelligence agentic and generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Dynatrace Intelligence agentic and generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")

---

## dynatrace-intelligence/copilot/copilot-overview.md

---
title: Dynatrace Intelligence агентное и генеративное ИИ обзор
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-overview
scraped: 2026-03-05T21:23:12.989599
---

# Dynatrace Intelligence агентное и генеративное ИИ обзор

# Dynatrace Intelligence агентное и генеративное ИИ обзор

* Последнее Dynatrace
* Объяснение
* 5-минутное чтение
* Обновлено 4 февраля 2026 г.

Dynatrace Intelligence агентное и генеративное ИИ предназначено для повышения производительности, помощи в обучении и обеспечения возможности изучения данных с помощью естественного языка.

## Dynatrace Intelligence агентное и генеративное ИИ

Dynatrace Intelligence агентное и генеративное ИИ основано на большой языковой модели (LLM). Модель, используемая Dynatrace ИИ, генерирует ответы на основе ваших входных данных и является вероятностной. Это означает, что ответы генерируются путем прогнозирования наиболее вероятного следующего слова или текста, основанного на данных, с которыми они были созданы, и на предоставленном контексте. Dynatrace Intelligence генеративное ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте).

Из-за этого подхода эти модели иногда могут表现аться неточно, неполно или ненадежно. Это означает, что существует риск того, что ответ, который вы получите, не точно отражает запрос, который вы предоставили, или что сгенерированный контент звучит разумно, но является неполным или неточным.

Мы рекомендуем вам тщательно оценить ответы, которые вы получаете от Dynatrace Intelligence агентного и генеративного ИИ. Если генеративное или агентное ИИ отвечает неточно, пожалуйста, предоставьте обратную связь напрямую из ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** или  **Dynatrace Assist**.

## Обзор навыков генеративного ИИ

Dynatrace Intelligence агентное и генеративное ИИ предлагает различные и специализированные навыки. В настоящее время генеративное ИИ предлагает четыре навыка:

* NL2DQL: этот навык обеспечивает функциональность быстрого анализа **Prompt**, доступную в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. NL2DQL переводит ваши естественные языковые запросы в DQL запросы. Для получения подробной информации см. [Запрос с помощью естественного языка](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Используйте Dynatrace Intelligence генеративное ИИ для перевода ваших естественных языковых вопросов в DQL запросы").
* DQL2NL: этот навык обеспечивает функциональность **Объяснить запрос** в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. DQL2NL предоставляет резюме и объяснение существующих DQL запросов, чтобы помочь вам лучше понять DQL. Для получения подробной информации см. [Резюмировать и объяснить запросы](/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot "Узнайте, как резюмировать и объяснить запросы с помощью Dynatrace Intelligence агентного и генеративного ИИ DQL2NL навыка.").
* Рекомендатель разговора: этот навык обеспечивает  **Dynatrace Assist**, наш глобальный интерфейс разговора. Рекомендатель разговора может отвечать на ваши вопросы Dynatrace, обучения и использования. Для получения подробной информации см. [Dynatrace Assist](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot "Задавайте вопросы с помощью естественного языка и получайте быстрые ответы от Dynatrace Assist, вашего генеративного ИИ помощника.").

  + **Dynatrace Assist** также предлагает контекстно-зависимые разговоры в приложениях, таких как ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**, или ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**. Контекстно-зависимые разговоры запускают предопределенные, контекстно-зависимые запросы и предоставляют вам контекстное объяснение, шаги по исправлению и резюме. Для получения подробной информации см. [Dynatrace Assist контекстно-зависимые разговоры](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters "Узнайте, как запустить предопределенные запросы в различных приложениях Dynatrace.").
* Предложения документов: этот навык обеспечивает функциональность предложения руководства по устранению неполадок в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**. Рекомендация руководства по устранению неполадок улучшает решение проблем путем автоматического предоставления релевантных руководств по устранению неполадок, таких как тетради или панели управления, созданные вашей командой. Для получения подробной информации см. [Обнаружение релевантных руководств по устранению неполадок с помощью Dynatrace Intelligence агентного и генеративного ИИ](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides "Узнайте, как Dynatrace Intelligence агентное и генеративное ИИ может предложить руководства по устранению неполадок для исправления проблем.").

Поскольку навыки, предлагаемые Dynatrace Intelligence генеративным ИИ, высоко специализированы, быстрый анализ в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** не может ответить на общие вопросы, и  **Dynatrace Assist** может производить неточные DQL запросы.

Dynatrace Intelligence агентное ИИ способно на это, поскольку оно вызывает агентные инструменты и может объединять их вывод. Для получения более подробной информации см. [Включение агентного ИИ для Dynatrace Assist](/docs/dynatrace-intelligence/copilot/copilot-getting-started#assist-agentic "Узнайте, как настроить Dynatrace Intelligence агентное и генеративное ИИ.").

## Dynatrace Intelligence агентное и генеративное ИИ архитектура и поток данных

Dynatrace Intelligence агентное и генеративное ИИ использует подход Retrieval Augmented Generation (RAG) для предоставления основной LLM с правильным контекстом для преобразования естественного языка в DQL запрос (обучение в контексте). Это означает, что Dynatrace Intelligence агентное и генеративное ИИ будет обогащать ваш запрос релевантным дополнительным контентом или контекстом, который отправляется в основную LLM для генерации подходящего ответа. Контент или контекст, используемый для обогащения вашего запроса, зависит от того, какой основной навык запрашивается.

Данные и дополнительный контекст используются только для обогащения запросов; модель не учится на этом. Данные клиентов не используются для автоматического уточнения, обучения или улучшения моделей или услуг. Для получения более подробной информации см. [Как генерируются ответы NL2DQL?](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql#nl2dql-answers-generation "Используйте Dynatrace Intelligence генеративное ИИ для перевода ваших естественных языковых вопросов в DQL запросы")

## Dynatrace Intelligence агентное и генеративное ИИ ограничения использования

Не существует ограничения на количество взаимодействий, которые вы можете иметь с генеративным ИИ. Однако существует ограничение на пропускную способность. Это означает, что каждый пользователь может задать 25 вопросов в течение 15-минутного интервала.

Существует аналогичное ограничение на количество вопросов, которые могут быть заданы всеми пользователями в вашей среде одновременно. Ваша среда может обрабатывать до 60 вопросов в течение 15-минутного интервала.

Если вы превысили любое из ограничений, вы увидите сообщение об ошибке: "Мне жаль, но я не смог сгенерировать ответ для вас из-за необычно высокого спроса. Пожалуйста, попробуйте еще раз через минуту."

## Часто задаваемые вопросы

Если вы хотите узнать больше о Dynatrace Intelligence агентном и генеративном ИИ, посетите нашу [страницу часто задаваемых вопросов](/docs/dynatrace-intelligence/copilot/copilot-faq "Узнайте о часто задаваемых вопросах и найдите ответы.").

## Связанные темы

* [Начало работы с Dynatrace Intelligence агентным и генеративным ИИ](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Узнайте, как настроить Dynatrace Intelligence агентное и генеративное ИИ.")

---

## dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips.md

---
title: Dynatrace Intelligence generative AI - Tips for writing better prompts
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips
scraped: 2026-03-02T21:27:09.087228
---

# Dynatrace Intelligence generative AI - Tips for writing better prompts

# Dynatrace Intelligence generative AI - Tips for writing better prompts

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence generative AI is a helpful tool for getting insights from your data without needing to learn DQL. However, as generative AI, it sometimes needs a bit of structure to ensure you get the best results. The following are tips for writing better prompts for quickly analyzing data in Notebooks and Dashboards.

## Tip 1: Make your prompt clear

Natural language is often nuanced and ambiguous, but making your prompt clear should generate better DQL queries:

* Remove and rewrite any words or phrases that aren't clear or could be interpreted in different ways.
* Avoid the use of subjective language like "interesting findings" that is open to interpretation.
* Write in short, simple sentences. You can combine multiple short sentences in a prompt; Dynatrace Intelligence generative AI understands this better than a single long or complex sentence.
* Start your prompt with **"Show me"** instead of phrases such as **"I would like to see"** and **"Tell me about"**.
* Ask yourself if a DQL expert could create a query from your prompt. If not, it probably needs to be clearer.

**Try:**

* Show me the average CPU usage for each host.

**Avoid:**

* CPU usage.
* I want to see an overall summary of the CPU usage for each host over the last week.

## Tip 2: Make your prompt specific

If you know the table where your data is located, specify it. It is especially helpful to be specific about elements such as "events" or "bizevents".

**Try:**

* Show me the number of new trip bizevents for the last day.
* Show me all error logs.

**Avoid:**

* Show me new trips.
* Show me errors.

## Tip 3: Sequence your prompt

When you're writing a complex prompt, it's good practice to make the order of the individual steps clear. Try writing the process in a step-by-step manner.

**Try:**

* First get all logs with errors, then extract the host ID only. Then lookup the CPU usage for the host IDs.

**Avoid:**

* Get the host ID from all logs with errors and lookup CPU usage.

## Tip 4: Try to gradually refine your prompt

If your prompt doesn't seem to work, try refining it to identify where Dynatrace Intelligence generative AI is getting stuck. Start with a simple statement, then gradually add more details.

For example, start with writing only the main part, such as **"Show all logs"**.

Optional If the prompt doesn't give you the intended results, gradually change it until it does. For example, **"Show me the number of logs by status"**.

Once the simpler steps work, add additional steps one by one, for example, **"Show me the number of logs by status as a timeseries"**.

## Tip 5: Use DQL syntax in your prompt

Using keywords from the DQL syntax keywords in your prompts will often generate better DQL queries. Some of the most common keywords are:

* Fetch
* Filter
* Sort
* Summarize
* Lookup

**Try:**

* Fetch all error logs and lookup the host name.

**Avoid:**

* Look at logs with errors and add matching results from the host names.

## Tip 6: Follow the DQL hierarchy in your prompt

We recommend that you get familiar with the [DQL documentation](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."). The more you can reflect the DQL syntax hierarchy in your prompt, including command order, the more effective your prompts will be. For example:

* Mention filters at the beginning of your prompt
* Mention sort orders at the end of your prompt

## Known limitations

We are actively working on improving and extending the Dynatrace Intelligence generative AI abilities. You might run into issues with some of the use cases that are still in progress, for example:

* Requesting a specific visualization in your prompt. Prompts like **"Show me logs by status as pie chart"** aren't supported yet and will not work.
* Running forecasts with Dynatrace Intelligence data analyzers. Prompts like **"Forecast whenâ¦"** aren't supported yet and will not work. However, you can provide Dynatrace Intelligence generative AI with a prompt starting with **"Show meâ¦"**, and then enable a Dynatrace Intelligence data analyzer on this section or tile.
* Specifying management zones via the prompt.

## Related topics

* [Dynatrace Intelligence generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Query with natural language](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql "Use Dynatrace Intelligence generative AI to translate your natural language questions into DQL queries")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence generative AI.")

---

## dynatrace-intelligence/copilot/quick-analysis-copilot-dql.md

---
title: Query with natural language
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql
scraped: 2026-03-04T21:30:33.891937
---

# Query with natural language

# Query with natural language

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Jan 28, 2026

You can use Dynatrace Intelligence generative AI in Dashboards and Notebooks to explore your data through natural language. It allows you to translate your conversational prompts directly into DQL queries that reflect the context of your environment. You can choose to auto-execute generated queries or generate DQL only.

## Prerequisites

We assume that you have completed the setup described in [Getting started with Dynatrace Intelligence agentic and generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

## Use generative AI in Notebooks

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and open or create a notebook you can edit.
2. Open the  **Add** menu and select  **Prompt**. A new Generative AI notebook section is created with an empty prompt box.
3. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
4. Optional If your prompt doesn't specify the timeframe, you can still specify it in your section header. The default is **Last 2 hours**.
5. Select **Run**. Generative AI creates and runs the query for you.

   Optional If you want to see the generated query before running it, open the  menu next to the **Run** button and select **Generate DQL only**.
6. Review the results.

   * You can review the query by expanding **DQL**  on the right.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the section header and select **Create DQL section** to create a DQL section from this query.
   * You can edit your original prompt, regenerate the query, and run it to update the results.  
     If you select **Rerun sections**, the Notebooks app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
7. Optional Select the  **Options** in the section header to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

   Automatically select visualization

   To have Dynatrace automatically select a visualization for your query, turn on **Auto select** in the upper-right corner of your visualization settings pane.

   * If you manually select a different visualization, the **Auto select** switch will turn off.
   * To have Dynatrace once again automatically select a visualization, turn **Auto select** back on.

## Use generative AI in Dashboards

1. Go to [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and open or create a dashboard you can edit.
2. Open the  **Add** menu and select  **Prompt**.

   * A new Dynatrace Intelligence generative AI dashboard tile is created
   * A panel on the right displays:

     + An empty tile title field you can customize
     + A prompt box followed by some examples you can select to try
     + A **Run** button
3. Optional At the top of the prompt definition panel, enter a tile title.
4. In the prompt box, type a prompt. Try `average cpu usage percentage by host` or see the examples displayed in the web UI for inspiration.
5. Optional If your prompt doesn't specify a timeframe, you can still specify it for the dashboard in your dashboard header (default is **Last 2 hours**) or the **Custom timeframe** settings (for a tile-specific timeframe).
6. Select **Run**. Generative AI creates and runs the query for you.
7. Review the results.

   * To review the query, expand **DQL**  under the prompt box.
   * Optional You can't edit the query directly in Dynatrace Intelligence generative AI, but you have two options for reusing it:

     + Copy the query and paste it elsewhere manually.
     + Open the  menu in the tile header and select **Create DQL tile** to create a DQL tile from this query.
   * You can edit your original prompt and run it to update the query and results.  
     If you refresh your dashboard, the Dashboards app will first check if any prompts have been edited.

     + If a prompt has been edited, the DQL will first be regenerated and then run.
     + If no prompts have been edited, the existing generated DQL will simply be run.
8. Optional Select the **Visual** tab to change the visualization (refer to the [visualization-specific documentation](/docs/analyze-explore-automate/dashboards-and-notebooks/edit-visualizations "Create, edit, and view visualizations on your Dynatrace dashboards and notebooks.") for more information).

Even though Dynatrace Intelligence generative AI is not charged for, all queries that are executed by generative AI are subject to licensing consumption according to your existing licensing agreement.

## Environment-aware queries

Environment-aware queries enrich Dynatrace Intelligence generative AI with your environment data. This lets you generate more accurate queries that identify and reference relevant entities, events, spans, logs, and metrics from your environment. You can also run more complex data analyses by asking Dynatrace Intelligence generative AI about the specifics of your data. To learn more about how to control and manage which data Dynatrace Intelligence generative AI has access to and how to enable environment-aware queries, see [Enable environment-aware queries](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-environment-aware-queries "Learn how to set up Dynatrace Intelligence agentic and generative AI.").

### Dynatrace Intelligence generative AI semantic index

Once enabled, Dynatrace Intelligence generative AI periodically scans your Grail data to create its own semantic index. Certain data fragments are sent to Microsoft Azure OpenAI during the semantic indexing. Examples of such data fragments include metric keys, dimensions, and field names. When a user provides a prompt, Dynatrace Intelligence generative AI first identifies the most relevant fragments from the data it has indexed. OUr generative AI then sends the user prompt, the relevant data fragments, and some examples of field values observed in your environment to Microsoft Azure OpenAI for processing.

Having environment-aware queries enabled allows Dynatrace Intelligence generative AI to identify unique data fields and custom metrics in your environment and helps you do your analysis by combining your prompt with the relevant, unique data fields and types.

Let's assume you're tracking travel bookings for new trips. In this case, you'd want to track:

* profit made on each booking as a bizevent
* applicable discounts as a bizevent
* length of time it takes customers to complete a booking as a custom metric

With this in mind, you could give Dynatrace Intelligence generative AI the following command: **"Show me the average money made and the price reduction for new trips, over the last month"**.

If you have environment-aware queries enabled, the following DQL will be generated, providing you with results relevant to your environment:

```
fetch bizevents , from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {profit= avg(profit), discount= avg(discount)}
```

Dynatrace Intelligence generative AI is capable of inferring that "money made" refers to the profit field, and that "price reduction" refers to the discount field, even if your prompt didn't use the correct field names.

If you don't have environment-aware queries enabled, Dynatrace Intelligence generative AI will try to refer to the fields by the names you provided. The following, incorrect DQL would be generated since the fields don't exist in your environment:

```
fetch bizevents, from:now() â 30d



| filter event.type ==  "new trip"



| makeTimeseries interval:1h, {avg_money_made = avg(money_made), avg_price_reduction = avg(price_reduction)}
```

Alternatively, you could ask Dynatrace Intelligence generative AI the following question: **"On average, how long does it take customers to book new trips?"**

If you have environment-aware queries enabled, the following DQL will be generated, providing you with results relevant to your environment:

```
timeseries avg(new_trip_booking_duration)
```

If you don't have environment-aware queries enabled, you'll likely get an error message since Dynatrace Intelligence generative AI would be unable to correctly map your question to your custom metric key. In this case, our generative AI can't provide a valid DQL query because it can't find a matching generic, built-in metric.

### User-based data access

Since Dynatrace Intelligence generative AI respects user privileges, it may provide different responses to different users based on their access rights.

## How are NL2DQL responses generated?



![Dynatrace Intelligence generative AI diagram explaining how NL2QL responses are generated](https://dt-cdn.net/images/davis-copilot-nl2dql-responses-1920-1a15aa1055.png)

Dynatrace Intelligence generative AI NL2DQL response process can be summarized in 4 steps.

1. Dynatrace Intelligence generative AI receives a request from a user.
2. If the request is well-formulated and recognized (see [Dynatrace Intelligence agentic and generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.") for more information), Dynatrace Intelligence generative AI matches the user request with the Dynatrace-owned content, such as documentation and curated query examples, and passes the prompt to LLM.

   If you have enabled environment-aware queries, the relevant data fragments will be used enrich the prompt alongside Dynatrace-owned content.
3. The LLM generates a response and checks if the DQL is valid.
4. The response is returned to the relevant app, Notebooks or Dashboards, and the output is displayed to the user.

## Give feedback

To help us improve Dynatrace Intelligence generative AI, you can provide feedback directly from your notebook or dashboard. Under the prompt box:

* Select ![Thumb up](https://dt-cdn.net/images/thumbsup-65185abaeb.svg "Thumb up") if Dynatrace Intelligence generative AI has interpreted your prompt correctly and has generated and run a DQL query that meets your expectations.
* Select ![Thumb down](https://dt-cdn.net/images/thumbsdown-b83de466e8.svg "Thumb down") if Dynatrace Intelligence generative AI has generated and run a DQL query that has failed to meet your expectations or has incorrectly interpreted your prompt. Please provide additional context for us to understand how we can improve this functionality to meet your needs and expectations.

Do not share personal or confidential information in your feedback.

## Related topics

* [Dynatrace Intelligence agentic and generative AI overview](/docs/dynatrace-intelligence/copilot/copilot-overview "Learn about data security and other aspects of Dynatrace Intelligence agentic and generative AI.")
* [Get started with Dynatrace Intelligence agentic and generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started "Learn how to set up Dynatrace Intelligence agentic and generative AI.")
* [Dynatrace Intelligence agentic and generative AI FAQ](/docs/dynatrace-intelligence/copilot/copilot-faq "Learn about frequently asked questions and find your answers.")
* [Dynatrace Intelligence agentic and generative AI - Tips for writing better prompts](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips "Learn best practices for writing more accurate prompts.")
* [Generative AI quick analysis examples](/docs/dynatrace-intelligence/use-cases/copilot-examples "Learn more about what kind of prompts work well in Dynatrace Intelligence agentic and generative AI.")

---

## dynatrace-intelligence/copilot.md

---
title: Agentic и генеративный ИИ
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot
scraped: 2026-03-05T21:22:23.299824
---

# Agentic и генеративный ИИ

# Agentic и генеративный ИИ

* Последнее Dynatrace
* Приложение
* 2-минутное чтение
* Обновлено 03 марта 2026 г.

Интеллект Dynatrace с агентным и генеративным ИИ, разработанный Dynatrace, позволяет исследовать данные с помощью естественного языка, помогая в настройке и повышении производительности. Интеллект Dynatrace с агентным и генеративным ИИ принимает ваш запрос и переводит его в DQL, и способен автоматически выполнять сгенерированные запросы DQL.

## Случаи использования

* Быстрее ознакомьтесь с DQL, переводя запросы на естественном языке в готовые к использованию запросы.
* Сэкономьте время, генерируя и выполняя сгенерированные запросы DQL вместо ручного написания.
* Получите ответы на ваши вопросы о помощи и настройке быстро, без необходимости доступа к документации или другим ресурсам поддержки Dynatrace.
* Получите лучшее понимание существующих DQL, получая краткие описания и объяснения запросов.
* Попросите Dynatrace Assist предоставить контекстные сведения:

  + Получите четкие описания проблем, их коренных причин и предложенных шагов по исправлению в приложении Problems.
  + Получите объяснения сигналов предупреждения в приложении Kubernetes.
  + Получите объяснения планов выполнения на естественном языке в приложении Databases.
* Откройте для себя руководства по устранению неполадок, чтобы ускорить исправление проблем.

Интеллект Dynatrace с агентным и генеративным ИИ

[#### Обзор интеллекта Dynatrace с агентным и генеративным ИИ

Узнайте о безопасности данных и других аспектах интеллекта Dynatrace с агентным и генеративным ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-overview)[#### Начало работы с интеллектом Dynatrace с агентным и генеративным ИИ

Узнайте, как настроить интеллект Dynatrace с агентным и генеративным ИИ.

* Руководство

Прочитайте это руководство](/docs/dynatrace-intelligence/copilot/copilot-getting-started)

## Анализ данных с помощью генеративного ИИ

[#### Запрос с помощью естественного языка

Используйте интеллект Dynatrace с генеративным ИИ, чтобы перевести ваши вопросы на естественном языке в запросы DQL

* Обзор

Прочитайте обзор](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql)[#### Советы по написанию лучших запросов для интеллекта Dynatrace с агентным и генеративным ИИ

Узнайте лучшие практики для написания более точных запросов.

* Справка

Прочитайте эту справку](/docs/dynatrace-intelligence/copilot/quick-analysis-copilot-dql/copilot-tips)[#### Примеры быстрого анализа с помощью генеративного ИИ

Узнайте больше о том, какие запросы работают хорошо в интеллекте Dynatrace с агентным и генеративным ИИ.

* Справка

Прочитайте эту справку](/docs/dynatrace-intelligence/use-cases/copilot-examples)[#### Суммирование и объяснение запросов

Узнайте, как суммировать и объяснять запросы с помощью навыка DQL2NL интеллекта Dynatrace с агентным и генеративным ИИ.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/copilot/explain-queries-with-davis-copilot)

## Спросите Dynatrace Assist

[#### Dynatrace Assist

Задайте вопросы на естественном языке и получите быстрые ответы от Dynatrace Assist, вашего генеративного ИИ-помощника.

* Приложение

Изучите это приложение](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot)[#### Встроенные стартовые разговоры

Узнайте, как запустить предопределенные запросы в различных приложениях Dynatrace.

* Справка

Прочитайте эту справку](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/copilot-conv-starters)

Для получения дополнительной информации о том, какие запросы работают хорошо в **Dynatrace Assist**, см. [примеры запросов](/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot/dynatrace-assist-prompts "Узнайте, какие запросы работают хорошо в Dynatrace Assist.").

## Сопоставление документов на основе векторов

[#### Откройте для себя руководства по устранению неполадок с помощью интеллекта Dynatrace с агентным и генеративным ИИ

Узнайте, как интеллект Dynatrace с агентным и генеративным ИИ может предложить руководства по устранению неполадок для исправления проблем.

* Учебник

Прочитайте этот учебник](/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides)

## Узнайте больше

[#### Политика безопасности и конфиденциальности данных интеллекта Dynatrace с агентным и генеративным ИИ

Узнайте о политике безопасности и конфиденциальности данных интеллекта Dynatrace с агентным и генеративным ИИ.

* Объяснение

Прочитайте это объяснение](/docs/dynatrace-intelligence/copilot/copilot-data-privacy)[#### Часто задаваемые вопросы об интеллекте Dynatrace с агентным и генеративным ИИ

Узнайте о часто задаваемых вопросах и найдите ответы.

* Устранение неполадок

Прочитайте это руководство по устранению неполадок](/docs/dynatrace-intelligence/copilot/copilot-faq)

---
