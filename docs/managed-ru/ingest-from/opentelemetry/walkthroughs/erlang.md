---
title: Инструментирование Erlang-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/erlang
scraped: 2026-05-12T11:23:08.656499
---

# Инструментирование Erlang-приложения с OpenTelemetry

# Инструментирование Erlang-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 4 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Erlang-приложение с помощью библиотек и инструментов OpenTelemetry для Erlang.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Нет |
| Трассировки | Да |
| Метрики | Нет |
| Логи | Нет |

## Предварительные требования

* Dynatrace версии 1.222+
* Для трассировки включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Настройка OpenTelemetry

1. Добавьте текущие версии [следующих зависимостей](https://hex.pm/packages?search=opentelemetry&sort=recent_downloads) в `rebar.config`.

   ```
   {deps, [



   %TODO add any additional dependancies here



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter



   ]}.
   ```
2. Добавьте следующие зависимости в файл `.app.src` в каталоге `src`.

   ```
   {applications, [kernel,



   stdlib,



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter]}
   ```
3. Добавьте следующую конфигурацию в `config/sys.config` и замените `[URL]` и `[TOKEN]` на соответствующие значения для [URL Dynatrace](#base-url) и [токена доступа](#access-token).

   ```
   [



   {otel_getting_started, []},



   {opentelemetry,



   [{span_processor, batch},



   {traces_exporter, otlp},



   {resource,



   [{service,



   #{name => "erlang-quickstart", version => "1.0.1"} %%TODO Replace with the name and version of your application



   }]



   },



   {resource_detectors, [



   otel_resource_env_var,



   otel_resource_app_env,



   extra_metadata



   ]}



   ]



   },



   {opentelemetry_exporter,



   [{otlp_protocol, http_protobuf},



   {otlp_traces_endpoint, "[URL]"}, %%TODO Replace [URL] to your SaaS/Managed URL as mentioned in the next step



   {otlp_headers, [{"Authorization", "Api-Token [TOKEN]"}]} %%TODO Replace [TOKEN] with your API Token as mentioned in the next step



   ]}



   ].
   ```
4. Сохраните следующий код в `src/extra_metadata.erl`.

   ```
   -module(extra_metadata).



   -behaviour(otel_resource_detector).



   -export([get_resource/1]).



   get_resource(_) ->



   Metadata = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_metadata.properties")), []),



   {ok, MetadataFilePath} = file:read_file("dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties"),



   Metadata2 = otel_resource:create(otel_resource_app_env:parse(get_metadata(MetadataFilePath)), []),



   Metadata3 = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_host_metadata.properties")), []),



   otel_resource:merge(otel_resource:merge(Metadata, Metadata2), Metadata3),



   otel_resource:merge(Metadata, Metadata2).



   get_metadata(FileName) ->



   try



   {ok, MetadataFile} = file:read_file(FileName),



   Lines = binary:split(MetadataFile, <<"\n">>, [trim, global]),



   make_tuples(Lines, [])



   catch _:_ -> "Metadata not found, safe to continue"



   end.



   make_tuples([Line|Lines], Acc) ->



   [Key, Value] = binary:split(Line, <<"=">>),



   make_tuples(Lines, [{Key, Value}|Acc]);



   make_tuples([], Acc) -> Acc.
   ```

   Операции чтения файлов, разбор файлов `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей соответствующей информации о топологии в Dynatrace.

## Шаг 3 Инструментирование приложения

### Добавление трассировки

Спаны запускаются макросом [`with_span`](https://hexdocs.pm/opentelemetry_api/OpenTelemetry.Tracer.html#with_span/3) и принимают необязательный список атрибутов спана, а также блок кода для этого спана. Спан автоматически завершится, когда блок кода вернёт управление.

```
-export([init/2]).



-include_lib("opentelemetry_api/include/otel_tracer.hrl").



-include_lib("opentelemetry/include/otel_resource.hrl").



init( Req, State ) ->



?with_span(<<"parent_span">>, #{attributes => [ %%TODO Add span name



{<<"my-key-1">>, <<"my-value-1">>}] %%TODO Add attributes at span creation



}, fun child_function/1),



%% Your code goes here



child_function(_SpanCtx) ->



?with_span(<<"child_span">>, #{},



fun(_ChildSpanCtx) ->



?set_attributes([{<<"child-key-1">>, <<"child-value-1">>}]) %%TODO Add attributes after span creation



end).
```

### Сбор метрик

Пример пока отсутствует, так как OpenTelemetry для Erlang ещё не имеет стабильной поддержки метрик.

### Подключение логов

Пример пока отсутствует, так как OpenTelemetry для Erlang ещё не имеет стабильной поддержки логов.

В зависимости от состояния OpenTelemetry SDK предварительная версия тем не менее может уже допускать приём ваших логов.

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

#### Извлечение контекста при получении запроса

Для извлечения информации о существующем контексте мы передаём заголовки в функцию `otel_propagator_text_map.extract`, которая разбирает информацию о контексте, предоставленную заголовками, и устанавливает текущий контекст на её основе.

```
%% Get Headers from incoming request



Headers = maps:get(headers, Req),



otel_propagator_text_map:extract(maps:to_list(Headers)),



SpanCtx = ?start_span(<<"span-name">>),



%% As we used `otel_propagator_text_map` the current context is from the parent span



Ctx = otel_ctx:get_current(),



proc_lib:spawn_link(fun() ->



%% Start span and set as current



otel_ctx:attach(Ctx),



?set_current_span(SpanCtx),



%% Create response



Resp = cowboy_req:reply(



200,



#{<<"content-type">> => <<"application/json">>},



<<"{\"message\": \"hello world\"}">>,



Req



),



{ok, Resp, State},



?end_span(SpanCtx)
```

#### Внедрение контекста при отправке запросов

В следующем примере используется `otel_propagator_text_map:inject`, чтобы предоставить HTTP-заголовки (необходимые для context propagation) в `NewHeaders`, которые мы в итоге объединяем с существующим объектом заголовков `Headers` и передаём в вызов `httpc:request`, что позволяет принимающему эндпоинту продолжить трассировку с предоставленной информацией.

```
?with_span(<<"span-name">>, #{},



fun(_ChildSpanCtx) ->



%% A custom header example



Headers = [{"content-type", "application/json"}, {"X-Custom-Header", "some-value"}],



%% We convert the traceparent information and merge the 2 headers as



%% Httpc:request requires tuples of strings



Tmp = [],



NewHeaders = headers_list(otel_propagator_text_map:inject(opentelemetry:get_text_map_injector(), Tmp)),



MergedHeaders = lists:append(Headers, NewHeaders),



{ok, Res} = httpc:request(get, {URL, MergedHeaders}, [], []),



io:format("Response: ~p~n", [Res])



end).



headers_list(Headers) ->



[{binary_to_list(Name), binary_to_list(Value)} || {Name, Value} <- Headers].
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