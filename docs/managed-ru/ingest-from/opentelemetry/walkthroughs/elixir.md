---
title: Инструментирование Elixir-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/elixir
scraped: 2026-05-12T12:04:19.980203
---

# Инструментирование Elixir-приложения с OpenTelemetry

# Инструментирование Elixir-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 4 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Elixir-приложение с помощью библиотек и инструментов OpenTelemetry для Elixir.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Нет |
| Traces | Да |
| Metrics | Нет |
| Logs | Нет |

## Предварительные требования

* Dynatrace версии 1.222+
* Для трассировки включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Настройка OpenTelemetry

1. Добавьте текущие версии [следующих зависимостей](https://hex.pm/packages?search=opentelemetry&sort=recent_downloads) в `mix.exs`.

   ```
   defp deps do



   [



   # Add any additional dependancies here



   {:httpoison, version: :latest},



   {:plug_cowboy, version: :latest},



   {:jason, version: :latest},



   {:plug, version: :latest},



   {:opentelemetry_exporter, version: :latest},



   {:opentelemetry_api, version: :latest},



   {:opentelemetry, version: :latest}



   ]



   end
   ```
2. Добавьте секцию `release` в определение приложения в `mix.exs`.

   ```
   releases: [



   <project_name>: [



   version: "<project_version>",



   applications: [opentelemetry_exporter: :permanent, opentelemetry: :temporary]



   ]



   ]
   ```
3. Включите зависимости context propagation следующей строкой в `runtime.exs`.

   ```
   text_map_propagators: [:baggage, :trace_context],
   ```
4. Добавьте следующую конфигурацию в `config/runtime.exs` и замените `[URL]` и `[TOKEN]` на соответствующие значения для [URL Dynatrace](#base-url) и [токена доступа](#access-token).

   ```
   import Config



   config :opentelemetry,



   resource: [service: %{name: "elixir-quickstart", version: "1.0.1"}], #TODO Replace with the name and version of your application



   span_processor: :batch,



   traces_exporter: :otlp,



   # Add your text map propagator from previous step here



   resource_detectors: [



   :otel_resource_app_env,



   :otel_resource_env_var,



   ExtraMetadata



   ]



   config :opentelemetry_exporter,



   otlp_protocol: :http_protobuf,



   otlp_traces_endpoint: "[URL]", #TODO Replace [URL] to your SaaS/Managed URL as mentioned in the next step



   otlp_traces_headers: [{"Authorization", "Api-Token [TOKEN]"}] #TODO Replace [TOKEN] with your API Token as mentioned in the next step
   ```
5. Сохраните следующий код в `lib/extra_metadata.ex`.

   ```
   defmodule ExtraMetadata do



   @behaviour :otel_resource_detector



   def get_resource(_) do



   metadata = read_file("/var/lib/dynatrace/enrichment/dt_metadata.properties") |> unwrap_lines



   file_path = read_file("dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties") |> unwrap_lines



   metadata2 = read_file(file_path) |> unwrap_lines



   attributes = get_attributes(Enum.concat(metadata, metadata2))



   metadata3 = read_file("/var/lib/dynatrace/enrichment/dt_host_metadata.properties") |> unwrap_lines



   attributes = get_attributes(Enum.concat(metadata, metadata2) ++ metadata3)



   :otel_resource.create(attributes)



   end



   defp unwrap_lines({:ok, metadata}), do: metadata



   defp unwrap_lines({:error, _}), do: []



   defp read_file(file_name) do



   try do



   {:ok, String.split(File.read!(file_name), "\n")}



   rescue



   File.Error ->



   {:error, "File does not exist, safe to continue"}



   end



   end



   defp get_attributes(metadata) do



   Enum.map(metadata, fn(line) ->



   if String.length(line) > 0 do



   [key, value] = String.split(line, "=")



   {key, value}



   else



   {:error, "EOF"}



   end



   end)



   end



   end
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей соответствующей информации о топологии в Dynatrace.

## Шаг 3 Инструментирование приложения

### Добавление трассировки

Спаны запускаются макросом [`with_span`](https://hexdocs.pm/opentelemetry_api/OpenTelemetry.Tracer.html#with_span/3) и принимают необязательный список атрибутов спана, а также блок кода для этого спана. Спан автоматически завершается, когда блок кода возвращает управление.

```
require OpenTelemetry.Tracer, as: Tracer



def hello do



Tracer.with_span "my-span", %{attributes: [{<<"my-key-1">>, <<"my-value-1">>}]} do #TODO add attributes at span creation



Tracer.set_attributes([{"another-key-1", "another-value-1"}]) #TODO add attributes after span creation



# Your code goes here



end



end
```

### Сбор метрик

Примера пока нет, так как OpenTelemetry для Elixir пока не имеет стабильной поддержки метрик.

### Подключение логов

Примера пока нет, так как OpenTelemetry для Elixir пока не имеет стабильной поддержки логов.

В зависимости от состояния OpenTelemetry SDK предварительная версия тем не менее может уже позволять приём ваших логов.

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

#### Извлечение контекста при получении запроса

Чтобы извлечь информацию о существующем контексте, мы передаём заголовки в функцию `otel_propagator_text_map.extract`, которая разбирает информацию о контексте, предоставленную заголовками, и устанавливает текущий контекст на её основе.

```
# Extract headers



:otel_propagator_text_map.extract(conn.req_headers)



span_ctx = OpenTelemetry.Tracer.start_span(<<"span-name">>)



ctx = OpenTelemetry.Ctx.get_current()



task = Task.async(fn ->



OpenTelemetry.Ctx.attach(ctx)



OpenTelemetry.Tracer.set_current_span(span_ctx)



# Do work here



OpenTelemetry.Tracer.end_span(span_ctx)



end)
```

#### Внедрение контекста при отправке запросов

В следующем примере используется `otel_propagator_text_map:inject`, чтобы предоставить HTTP-заголовки (необходимые для context propagation) в `merged_headers`. Затем заголовки передаются в `HTTPoison.get`, что позволяет принимающему эндпоинту продолжить трассировку с предоставленной информацией.

```
OpenTelemetry.Tracer.with_span "span-name" do



# ...



# do work here



# ...



headers = [{"content-type", "application/json"}, {"X-Custom-Header", "some-value"}]



merged_headers = :otel_propagator_text_map.inject(headers)



case HTTPoison.get(URL, merged_headers, []) do



{:ok, res} -> IO.puts("Response: #{inspect(res)}")



{:error, _} -> raise "request failed"



end



end
```

## Шаг 4 Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 5 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")