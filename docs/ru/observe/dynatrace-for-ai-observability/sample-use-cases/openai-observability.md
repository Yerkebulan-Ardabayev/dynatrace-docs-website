---
title: Наблюдаемость OpenAI
source: https://www.dynatrace.com/docs/observe/dynatrace-for-ai-observability/sample-use-cases/openai-observability
scraped: 2026-03-05T21:31:04.024459
---

* 6 мин. чтения

Dynatrace позволяет предприятиям автоматически собирать, визуализировать и получать оповещения о потреблении запросов OpenAI Agent и API, задержках и информации о стабильности в сочетании со всеми другими сервисами, используемыми для создания их AI-приложений. Сюда входят сервисы [OpenAI](https://openai.com/) и [Azure OpenAI](https://azure.microsoft.com/en-us/products/cognitive-services/openai-service), такие как GPT-5.2, Codex, DALL-E и ChatGPT.

Пример дашборда ниже визуализирует потребление токенов OpenAI, показывая критические SLO для задержки и доступности, а также наиболее важные метрики генеративных AI-сервисов OpenAI, такие как время отклика, количество ошибок и общее число запросов.

![Дашборд OpenAI](https://dt-cdn.net/images/openai-dashboard-v11-2560-987f66adf6.png)

Dynatrace с OpenTelemetry или OpenLLMetry помогает:

* Раскрыть полный контекст используемых технологий.
* Показать топологию взаимодействия сервисов.
* Анализировать уязвимости безопасности.
* Наблюдать за метриками, трассировками, логами и бизнес-событиями в реальном времени.

В разделах ниже описано, как:

* Трассировать запросы к моделям OpenAI/GPT.
* Строить графики ключевых сигналов OpenAI на дашборде.
* Использовать Dynatrace Intelligence для автоматического обнаружения аномального поведения сервисов, такого как замедление запросов к OpenAI/GPT, как основной причины масштабных ситуаций.

## Пример приложения OpenAI Agents SDK

Используйте [пример OpenAI Agents SDK](https://github.com/dynatrace-oss/dynatrace-ai-agent-instrumentation-examples/tree/main/openai-agent-sample), чтобы увидеть наблюдаемость AI в действии. Пример представляет собой интерфейс агента поддержки клиентов, построенный на [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) и основанный на [openai-cs-agents-demo](https://github.com/openai/openai-cs-agents-demo). Бэкенд использует OpenLLMetry OpenTelemetry SDK от Traceloop для отправки трассировок и метрик в Dynatrace.

В примере вы:

1. Настраиваете OpenLLMetry в `python-backend/api.py`.
2. Указываете `api_endpoint` на ваш OTLP-эндпоинт Dynatrace.
3. Выполняете аутентификацию с помощью API-токена Dynatrace (в примере он считывается из `/etc/secrets/dynatrace_otel`).

Дополнительные параметры конфигурации см. в руководстве Начало работы с наблюдаемостью AI.

### Запуск примера

1. Задайте учётные данные OpenAI или Azure OpenAI в качестве переменных окружения.

   ```
   export OPENAI_API_KEY=your_api_key
   ```

   ```
   export AZURE_OPENAI_API_KEY=your_api_key


   export AZURE_OPENAI_API_VERSION='2024-08-01-preview'


   export AZURE_OPENAI_ENDPOINT=your_endpoint


   export AZURE_OPENAI_DEPLOYMENT=your_deployment
   ```

   Альтернативно задайте переменные окружения в файле `.env` в каталоге `python-backend` и загрузите их с помощью `python-dotenv`.
2. Установите зависимости бэкенда.

   ```
   cd python-backend


   python3.12 -m venv .venv


   source .venv/bin/activate


   pip install -r requirements.txt
   ```
3. Установите зависимости пользовательского интерфейса.

   ```
   cd ui


   npm install
   ```
4. Запустите приложение.

   ```
   npm run dev
   ```

   Фронтенд доступен по адресу `http://localhost:3000`. Эта команда также запускает бэкенд.

## Наблюдение за стоимостью запросов OpenAI с помощью логов

Использование логов для сбора и наблюдения за стоимостью запросов OpenAI является простым и эффективным подходом. Он позволяет владельцу сервиса записывать строку лога с помощью стандартного фреймворка логирования Node.js, такого как [Winston](https://www.npmjs.com/package/winston), а также собирать и анализировать эти логи в Dynatrace.

Следующий фрагмент кода записывает строку лога Winston, содержащую количество токенов запроса OpenAI.

```
logger.log('info', `OpenAI response promt_tokens:${response.data.usage.prompt_tokens} completion_tokens:${response.data.usage.completion_tokens} total_tokens:${response.data.usage.total_tokens}`);
```

Строки лога запросов OpenAI можно просматривать в средстве просмотра логов Dynatrace.

Мы рекомендуем также включить обогащение контекста трассировки для логов Node.js (перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Preferences** > **OneAgent features** и включите **Node.js Trace/span context enrichment for logs**), чтобы автоматически сопоставлять все строки логов с захваченными трассировками запросов.

![Настройка обогащения контекста трассировки](https://dt-cdn.net/images/openai-logs-2912-9de465dc73.png)

При включённом обогащении **Node.js Trace/span context enrichment for logs** вы получаете удобное сопоставление всех трассировок OpenAI со строками логов. Их можно просматривать в ![AI Observability](https://dt-cdn.net/images/ai-obs-1024-c755ef8af6.png "AI Observability") **AI Observability** > **Explorer** > **Logs**.

![Обозреватель логов](https://dt-cdn.net/images/open-ai-logs-prev-2912-b5ac096261.png)

## Наблюдение за стоимостью запросов OpenAI путём отправки пользовательских метрик

Каждый запрос к модели OpenAI, такой как GPT-5.2 или GPT-5.1, возвращает информацию о том, сколько токенов было использовано для запроса (длина текстового вопроса) и сколько токенов модель сгенерировала в ответ.

Извлекая измерения токенов из возвращаемых данных и передавая их через OneAgent, пользователи могут наблюдать за потреблением токенов во всех сервисах с поддержкой OpenAI в своей среде мониторинга.

Для извлечения количества токенов из ответа OpenAI и передачи этих измерений в локальный OneAgent добавьте следующую инструментацию в ваш сервис Node.js.

```
function report_metric(openai_response) {


var post_data = "openai.promt_token_count,model=" + openai_response.model + " " + openai_response.usage.prompt_tokens + "\n";


post_data += "openai.completion_token_count,model=" + openai_response.model + " " + openai_response.usage.completion_tokens + "\n";


post_data += "openai.total_token_count,model=" + openai_response.model + " " + openai_response.usage.total_tokens + "\n";


console.log(post_data);


var post_options = {


host: 'localhost',


port: '14499',


path: '/metrics/ingest',


method: 'POST',


headers: {


'Content-Type': 'text/plain',


'Content-Length': Buffer.byteLength(post_data)


}


};


var metric_req = http.request(post_options, (resp) => {}).on("error", (err) => { console.log(err); });


metric_req.write(post_data);


metric_req.end();


}
```

Три новые метрики потребления токенов OpenAI доступны в Dynatrace.

![Метрики потребления токенов OpenAI, собранные в Dynatrace](https://dt-cdn.net/images/openai-dashboard-2-2551-f433fa0e84.png)

## Dynatrace Intelligence автоматически определяет GPT как первопричину

Dynatrace Intelligence автоматически изучает типичное поведение отслеживаемых сервисов.

При обнаружении аномального замедления или увеличения количества ошибок Dynatrace Intelligence запускает анализ первопричин для выявления причины сложных ситуаций.

В нашем простом примере сервис Node.js полностью зависит от ответа модели ChatGPT. Когда задержка ответа модели ухудшается или запрос к модели возвращается с ошибкой, Dynatrace Intelligence автоматически это обнаруживает.