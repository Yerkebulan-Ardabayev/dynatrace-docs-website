# -*- coding: utf-8 -*-
from _otel_canon import S, SUB, build_one, qa_one

TRANS = {
    # title / H1
    "title: Apply memory limits to the OTel Collector": "title: Применение ограничений памяти к OTel Collector",
    "# Apply memory limits to the OTel Collector": "# Применение ограничений памяти к OTel Collector",
    # metadata
    "* Updated on Jan 08, 2026": "* Обновлено 08 января 2026 г.",
    # intro
    "The following configuration example shows how you configure a Collector instance and its native memory limiter processor to guarantee memory allocation keeps within the specified parameters.": "В следующем примере конфигурации показано, как настроить экземпляр Collector и его встроенный processor memory_limiter, чтобы гарантировать, что выделение памяти остаётся в пределах указанных параметров.",
    # recommended configuration callout (wrapped over 3 lines)
    "Recommended configuration": "Рекомендуемая конфигурация",
    "For optimal memory usage with your Collector instance, we recommend that you": "Для оптимального использования памяти вашим экземпляром Collector мы рекомендуем",
    "apply this configuration with most containerized setups. See the section on": "применять эту конфигурацию в большинстве контейнеризированных установок. Дополнительные сведения см. в разделе о",
    "[deployment considerations](#deployment-considerations) for more information.": "[вопросах развёртывания](#deployment-considerations).",
    # prerequisites distribution bullet (mojibake stripped by norm)
    "* One of the following Collector distributions with the [memory limiter processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor):": "* Один из следующих дистрибутивов Collector с [processor memory limiter](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor):",
    # Receivers prose
    "Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.": "В разделе `receivers` мы указываем стандартный receiver `otlp` в качестве активного компонента receiver для нашего экземпляра Collector.",
    "This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).": "Это сделано в основном в демонстрационных целях. Здесь можно указать любой другой допустимый receiver (например, `zipkin`).",
    # Processors prose
    "Under `processors`, we specify the [`memory_limiter` processor](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor) with the following parameters:": "В разделе `processors` мы указываем [processor `memory_limiter`](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.151.0/processor/memorylimiterprocessor) со следующими параметрами:",
    "* `check_interval` configured to check the memory status every second": "* `check_interval` настроен на проверку состояния памяти каждую секунду",
    "* `limit_percentage` configured to allow a maximum memory allocation of 90 percent": "* `limit_percentage` настроен на разрешение максимального выделения памяти в 90 процентов",
    "* `spike_limit_percentage` configured to allow a maximum spike memory usage of 20 percent": "* `spike_limit_percentage` настроен на разрешение максимального пикового использования памяти в 20 процентов",
    # soft/hard limit paragraph (wrapped)
    "With this configuration, the OTel Collector checks the memory allocation every second": "При такой конфигурации OTel Collector проверяет выделение памяти каждую секунду",
    "and starts to apply pressure using separate mechanisms after the following": "и начинает применять давление с помощью отдельных механизмов после достижения следующих",
    "limits are reached:": "пределов:",
    "* Soft limit (`limit_percentage - spike_limit_percentage`): After this limit is": "* Мягкий предел (`limit_percentage - spike_limit_percentage`): после достижения этого предела",
    "reached, the processor rejects payloads until memory usage is under the limit.": "processor отклоняет полезные нагрузки, пока использование памяти не опустится ниже предела.",
    "It is up to the receiver upstream of the processor to send the proper": "Отправка надлежащих сообщений об отклонении возлагается на receiver, расположенный выше processor",
    "rejection messages.": "по конвейеру.",
    "* Hard limit: (`limit_percentage`): After this limit is reached, the processor": "* Жёсткий предел: (`limit_percentage`): после достижения этого предела processor",
    "will force garbage Collection until memory usage is under the limit. Data will": "принудительно запускает сборку мусора, пока использование памяти не опустится ниже предела. Данные",
    "continue to be rejected until usage is under the soft limit.": "продолжают отклоняться, пока использование не опустится ниже мягкого предела.",
    # GOMEMLIMIT paragraph (wrapped)
    "In addition to the memory limiter processor, we highly recommend you set the": "В дополнение к processor memory limiter мы настоятельно рекомендуем задать",
    "`GOMEMLIMIT` environment variable to a value 80% of the hard limit. Note that": "переменной окружения `GOMEMLIMIT` значение, равное 80% от жёсткого предела. Обратите внимание, что",
    "`GOMEMLIMIT` requires an absolute value in bytes to be set. For example, you": "для `GOMEMLIMIT` требуется задавать абсолютное значение в байтах. Например, можно",
    "could set `GOMEMLIMIT=1024MiB` to start increasing the frequency of garbage": "задать `GOMEMLIMIT=1024MiB`, чтобы начать увеличивать частоту циклов сборки",
    "collection cycles once the Collector reaches 1024 MiB of memory used on the Go": "мусора, когда Collector достигает 1024 МиБ памяти, используемой в куче Go",
    "VM heap. For more information, see the [Go package": "VM. Дополнительные сведения см. в [документации пакета Go",
    "documentation](https://pkg.go.dev/runtime#hdr-Environment_Variables) describing": "](https://pkg.go.dev/runtime#hdr-Environment_Variables), описывающей",
    "how the environment variable works.": "работу этой переменной окружения.",
    # Deployment considerations
    "#### Deployment considerations": "#### Вопросы развёртывания",
    "In containerized environments, or other places where the host environment sets": "В контейнеризированных средах или других случаях, когда хост-среда задаёт",
    "the Collector's maximum allowed memory, we recommend you use the": "максимально допустимый объём памяти Collector, мы рекомендуем использовать параметры",
    "`limit_percentage` and `spike_limit_percentage` options.": "`limit_percentage` и `spike_limit_percentage`.",
    "For deployments on virtual machines or bare metal where the Collector is not": "Для развёртываний на виртуальных машинах или физических серверах, где Collector не",
    "given an explicit memory quota, we instead recommend you use the `limit_mib` and": "получает явную квоту памяти, мы вместо этого рекомендуем использовать параметры `limit_mib` и",
    "`spike_limit_mib` options.": "`spike_limit_mib`.",
    # Service pipelines prose
    "Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our memory limiter processor by referencing it under `processors` for each respective pipeline.": "В разделе `service` мы собираем наши объекты receiver и exporter в конвейеры для трассировок, метрик и логов и включаем наш processor memory limiter, ссылаясь на него в разделе `processors` для каждого соответствующего конвейера.",
    **S,
}

PASS = {"### Receivers", "### Processors", "### Exporters"}

if __name__ == "__main__":
    build_one(SUB, "memory.md", TRANS, PASS)
    qa_one(SUB, "memory.md")
