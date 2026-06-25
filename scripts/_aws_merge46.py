# -*- coding: utf-8 -*-
"""Merge L4-IF.46 batch (6 standard AWS files: SNS, Direct Connect, DMS,
MediaConnect, SageMaker, GameLift) translations into the shared cumulative
dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Same mechanism as L4-IF.45: translations keyed by an ASCII-normalized form of
the EN text, matched against the real skeleton keys programmatically. Any
skeleton key left without a translation, or any translation matching no
skeleton key, is reported (self-validation against typos). Asserts: no em-dash,
no mojibake in RU. Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if46.json")


def asciinorm(s):
    for a, b in [
        ("’", "'"),
        ("‘", "'"),
        ("“", '"'),
        ("”", '"'),
        ("…", "..."),
        ("–", "-"),
        ("—", "-"),
        ("×", "x"),
    ]:
        s = s.replace(a, b)
    return s


# intro template V1 (verbatim canon, service name swapped) -- all 6 use V1
def en_v1(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view metrics for each service instance, split metrics into multiple dimensions, "
        "and create custom charts that you can pin to your dashboards." % s
    )


def ru_v1(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений "
        "и создавать собственные графики, которые можно закреплять на дашбордах." % s
    )


RU = {}

# ---- intros ----
for svc in [
    "Amazon Simple Notification Service (Amazon SNS)",
    "AWS Direct Connect",
    "AWS DMS",
    "AWS Elemental MediaConnect",
    "Amazon SageMaker",
    "Amazon GameLift",
]:
    RU[en_v1(svc)] = ru_v1(svc)

# ---- H1 headings (title with leading "# ") ----
RU.update(
    {
        "# Amazon SNS (Simple Notification Service) monitoring": "# Мониторинг Amazon SNS (Simple Notification Service)",
        "# AWS Direct Connect monitoring": "# Мониторинг AWS Direct Connect",
        "# AWS DMS (Database Migration Service) monitoring": "# Мониторинг AWS DMS (Database Migration Service)",
        "# AWS Elemental MediaConnect monitoring": "# Мониторинг AWS Elemental MediaConnect",
        "# Amazon SageMaker (Batch Transform Jobs, Endpoint Instances, Endpoints, Ground Truth, Processing Jobs, Training Jobs) monitoring": "# Мониторинг Amazon SageMaker (Batch Transform Jobs, Endpoint Instances, Endpoints, Ground Truth, Processing Jobs, Training Jobs)",
        "# Amazon GameLift monitoring": "# Мониторинг Amazon GameLift",
    }
)

# ---- boilerplate: read-time, dates ----
RU.update(
    {
        "* 9-min read": "* Чтение: 9 мин",
        "* 10-min read": "* Чтение: 10 мин",
        "* 14-min read": "* Чтение: 14 мин",
        "* Updated on May 09, 2024": "* Обновлено 9 мая 2024 г.",
        "* Published Aug 12, 2020": "* Опубликовано 12 августа 2020 г.",
        # product/feature section headings kept EN (identity, product-name canon)
        "### Amazon SageMaker Batch Transform Jobs": "### Amazon SageMaker Batch Transform Jobs",
        "### Amazon SageMaker Processing Jobs, Amazon SageMaker Training Jobs": "### Amazon SageMaker Processing Jobs, Amazon SageMaker Training Jobs",
        "### Amazon SageMaker Endpoint Instances": "### Amazon SageMaker Endpoint Instances",
        "### Amazon SageMaker Endpoints": "### Amazon SageMaker Endpoints",
        "### Amazon SageMaker Ground Truth": "### Amazon SageMaker Ground Truth",
    }
)

# ---- main-dimension notes ----
for dim in [
    "TopicName",
    "ConnectionId",
    "ReplicationInstanceIdentifier",
    "FlowARN",
    "EndpointName",
    "FleetId",
]:
    RU["`%s` is the main dimension." % dim] = "Основное измерение: `%s`." % dim

# ---- SNS ----
RU.update(
    {
        "The number of messages published to the Amazon SNS topics": "Количество сообщений, опубликованных в топиках Amazon SNS",
        "The number of messages successfully delivered from the Amazon SNS topics to subscribing endpoints": "Количество сообщений, успешно доставленных из топиков Amazon SNS в подписанные конечные точки",
        "The number of messages that Amazon SNS failed to deliver": "Количество сообщений, которые Amazon SNS не удалось доставить",
        "The number of messages rejected by subscription filter policies because the message attributes are invalid": "Количество сообщений, отклонённых политиками фильтрации подписок из-за недопустимых атрибутов сообщения",
        "The number of messages rejected by subscription filter policies because the messages have no attributes": "Количество сообщений, отклонённых политиками фильтрации подписок из-за отсутствия атрибутов у сообщений",
        "The number of messages rejected by subscription filter policies": "Количество сообщений, отклонённых политиками фильтрации подписок",
        "The size of published messages": "Размер опубликованных сообщений",
        "The charges accrued since the start of the current calendar month for sending SMS messages": "Плата, начисленная с начала текущего календарного месяца за отправку SMS-сообщений",
        "The rate of successful SMS message deliveries": "Доля успешных доставок SMS-сообщений",
        "When CloudWatch displays your `SMSMonthToDateSpentUSD` metric as `Metrics with no dimensions`, enable the metric with a single `Region` dimension.": "Когда CloudWatch отображает метрику `SMSMonthToDateSpentUSD` как `Metrics with no dimensions`, включите метрику с единственным измерением `Region`.",
    }
)

# ---- Direct Connect ----
RU.update(
    {
        "The bitrate for outbound data from the AWS side of the connection": "Битрейт исходящих данных со стороны AWS этого соединения",
        "The bitrate for inbound data to the AWS side of the connection": "Битрейт входящих данных на сторону AWS этого соединения",
        "The total error count for all types of MAC level errors on the AWS device": "Общее количество ошибок всех типов уровня MAC на устройстве AWS",
        "The health of the fiber connection for inbound (ingress) traffic to the AWS side of the connection": "Состояние оптоволоконного соединения для входящего (ingress) трафика на сторону AWS этого соединения",
        "The health of the fiber connection for outbound (egress) traffic from the AWS side of the connection": "Состояние оптоволоконного соединения для исходящего (egress) трафика со стороны AWS этого соединения",
        "The packet rate for outbound data from the AWS side of the connection": "Частота пакетов исходящих данных со стороны AWS этого соединения",
        "The packet rate for inbound data to the AWS side of the connection": "Частота пакетов входящих данных на сторону AWS этого соединения",
        "The state of the connection (up or down)": "Состояние соединения (активно или неактивно)",
        "The bitrate for outbound data from the AWS side of the virtual interface": "Битрейт исходящих данных со стороны AWS виртуального интерфейса",
        "The bitrate for inbound data to the AWS side of the virtual interface": "Битрейт входящих данных на сторону AWS виртуального интерфейса",
        "The packet rate for outbound data from the AWS side of the virtual interface": "Частота пакетов исходящих данных со стороны AWS виртуального интерфейса",
        "The packet rate for inbound data to the AWS side of the virtual interface": "Частота пакетов входящих данных на сторону AWS виртуального интерфейса",
    }
)

# ---- DMS ----
RU.update(
    {
        "Amount of rows accumulating on disk and waiting to be committed from the source": "Количество строк, накапливающихся на диске и ожидающих фиксации из источника",
        "Amount of rows accumulating on disk and waiting to be committed to the target": "Количество строк, накапливающихся на диске и ожидающих фиксации в целевой системе",
        "Amount of rows accumulating in memory and waiting to be committed from the source": "Количество строк, накапливающихся в памяти и ожидающих фиксации из источника",
        "Amount of rows accumulating in memory and waiting to be committed to the target": "Количество строк, накапливающихся в памяти и ожидающих фиксации в целевой системе",
        "The total number of change events at a point in time that are waiting to be applied to the target": "Общее количество событий изменения на определённый момент времени, ожидающих применения в целевой системе",
        "The gap, in seconds, between the last event captured from the source endpoint and the current system timestamp of the AWS DMS instance. CDCLatencySource represents the latency between source and replication instance.": "Промежуток в секундах между последним событием, захваченным из исходной конечной точки, и текущей системной отметкой времени экземпляра AWS DMS. CDCLatencySource представляет задержку между источником и экземпляром репликации.",
        "The gap, in seconds, between the first event timestamp waiting to commit on the target and the current timestamp of the AWS DMS instance. CDCLatencyTarget represents the latency between replication instance and target.": "Промежуток в секундах между отметкой времени первого события, ожидающего фиксации в целевой системе, и текущей отметкой времени экземпляра AWS DMS. CDCLatencyTarget представляет задержку между экземпляром репликации и целевой системой.",
        "Incoming data received for the source in KB per second": "Входящие данные, полученные для источника, в КБ в секунду",
        "Outgoing data transmitted for the target in KB per second": "Исходящие данные, переданные для целевой системы, в КБ в секунду",
        "Incoming task changes from the source in rows per second": "Входящие изменения задачи из источника, строк в секунду",
        "Outgoing task changes for the target in rows per second": "Исходящие изменения задачи для целевой системы, строк в секунду",
        "The percentage of CPU maximally allocated for the task (0 means no limit)": "Процент CPU, максимально выделенный для задачи (0 означает отсутствие ограничения)",
        "The amount of CPU used": "Объём используемого CPU",
        "The number of outstanding I/Os (read/write requests) waiting to access the disk": "Количество незавершённых операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску",
        "The amount of available storage space": "Объём доступного дискового пространства",
        "The amount of available RAM": "Объём доступной оперативной памяти",
        "Incoming data received from a full load from the source in kilobytes (KB) per second": "Входящие данные, полученные при полной загрузке из источника, в килобайтах (КБ) в секунду",
        "Outgoing data transmitted from a full load for the target in kilobytes (KB) per second": "Исходящие данные, переданные при полной загрузке для целевой системы, в килобайтах (КБ) в секунду",
        "Incoming changes from a full load from the source in rows per second": "Входящие изменения при полной загрузке из источника, строк в секунду",
        "Outgoing changes from a full load for the target in rows per second": "Исходящие изменения при полной загрузке для целевой системы, строк в секунду",
        "The maximum allocation of memory for the task (0 means no limits)": "Максимальное выделение памяти для задачи (0 означает отсутствие ограничений)",
        "The resident set size (RSS) occupied by a task. It indicates the portion of memory occupied by a task held in main memory (RAM).": "Размер резидентной памяти (RSS), занятой задачей. Указывает на долю памяти, занятой задачей и удерживаемой в основной памяти (RAM).",
        "The incoming (receive) network traffic on the replication instance, including both customer database traffic and AWS DMS traffic used for monitoring and replication": "Входящий (принимаемый) сетевой трафик на экземпляре репликации, включая как трафик клиентской базы данных, так и трафик AWS DMS, используемый для мониторинга и репликации",
        "The outgoing (transmit) network traffic on the replication instance, including both customer database traffic and AWS DMS traffic used for monitoring and replication": "Исходящий (передаваемый) сетевой трафик на экземпляре репликации, включая как трафик клиентской базы данных, так и трафик AWS DMS, используемый для мониторинга и репликации",
        "The average number of disk read I/O operations per second": "Среднее количество операций ввода-вывода чтения с диска в секунду",
        "The average amount of time taken per disk I/O (input) operation": "Среднее время, затрачиваемое на одну операцию ввода-вывода с диска (ввод)",
        "The average number of bytes read from disk per second": "Среднее количество байт, считываемых с диска в секунду",
        "The amount of swap space used on the replication instance": "Объём пространства подкачки, используемого на экземпляре репликации",
        "Number of rows that validation was attempted, per minute": "Количество строк, для которых выполнялась попытка проверки, в минуту",
        "AWS DMS can do data validation in bulk, especially in certain scenarios during a full-load or ongoing replication when there are many changes. This metric indicates the latency required to read a bulk set of data from the source endpoint.": "AWS DMS может выполнять проверку данных массово, особенно в определённых сценариях во время полной загрузки или непрерывной репликации при большом количестве изменений. Эта метрика показывает задержку, необходимую для чтения массового набора данных из исходной конечной точки.",
        "AWS DMS can do data validation in bulk, especially in certain scenarios during a full-load or ongoing replication when there are many changes. This metric indicates the latency required to read a bulk set of data on the target endpoint.": "AWS DMS может выполнять проверку данных массово, особенно в определённых сценариях во время полной загрузки или непрерывной репликации при большом количестве изменений. Эта метрика показывает задержку, необходимую для чтения массового набора данных на целевой конечной точке.",
        "Number of rows where validation failed": "Количество строк, для которых проверка завершилась неудачно",
        "During ongoing replication, data validation can identify ongoing changes and validate those changes. This metric indicates the latency in reading those changes from the source.": "Во время непрерывной репликации проверка данных может выявлять текущие изменения и проверять их. Эта метрика показывает задержку при чтении этих изменений из источника.",
        "During ongoing replication, data validation can identify ongoing changes and validate the changes row by row. This metric gives us the latency in reading those changes from the target.": "Во время непрерывной репликации проверка данных может выявлять текущие изменения и проверять их построчно. Эта метрика показывает задержку при чтении этих изменений из целевой системы.",
        "Number of rows where the validation is still pending": "Количество строк, для которых проверка ещё ожидается",
        "Number of rows that AWS DMS validated, per minute": "Количество строк, проверенных AWS DMS, в минуту",
        "Number of rows where validation was suspended": "Количество строк, для которых проверка была приостановлена",
        "The average number of disk write I/O operations per second": "Среднее количество операций ввода-вывода записи на диск в секунду",
        "The average amount of time taken per disk I/O (output) operation": "Среднее время, затрачиваемое на одну операцию ввода-вывода с диска (вывод)",
        "The average number of bytes written to disk per second": "Среднее количество байт, записываемых на диск в секунду",
        "To collect metrics about changes captured by the migration task (CDC metrics) on MySQL, the binary logging and automatic backup settings should be enabled.": "Для сбора метрик об изменениях, захваченных задачей миграции (метрики CDC), в MySQL должны быть включены настройки двоичного журналирования и автоматического резервного копирования.",
    }
)

# ---- MediaConnect ----
RU.update(
    {
        "The number of dropped packets that were recovered by automatic repeat request (ARQ)": "Количество отброшенных пакетов, восстановленных с помощью автоматического запроса повторной передачи (ARQ)",
        "The number of retransmitted packets that were requested through automatic repeat request (ARQ) and received": "Количество повторно переданных пакетов, запрошенных через автоматический запрос повторной передачи (ARQ) и полученных",
        "The number of times that a conditional access table (CAT) error occurred. This error indicates that the CAT is not present.": "Количество случаев возникновения ошибки таблицы условного доступа (CAT). Эта ошибка указывает на отсутствие CAT.",
        "The status of the source. A value of one indicates that the source is connected and a value of zero indicates that the source is disconnected.": "Статус источника. Значение, равное единице, означает, что источник подключён, а значение, равное нулю, означает, что источник отключён.",
        "The number of times that a continuity error occurred": "Количество случаев возникновения ошибки непрерывности",
        "The number of times that the source status changed from connected to disconnected": "Количество случаев изменения статуса источника с «подключён» на «отключён»",
        "The number of packets that were lost during transit": "Количество пакетов, потерянных при передаче",
        "The number of packets that were transmitted using forward error correction (FEC) and received": "Количество пакетов, переданных с использованием прямой коррекции ошибок (FEC) и полученных",
        "The number of packets that were transmitted using forward error correction (FEC), lost during transit, and recovered": "Количество пакетов, переданных с использованием прямой коррекции ошибок (FEC), потерянных при передаче и восстановленных",
        "The number of packets that were lost during transit and were not recovered by error correction": "Количество пакетов, потерянных при передаче и не восстановленных коррекцией ошибок",
        "The number of packets that were lost in transit because the video required more buffer than was available": "Количество пакетов, потерянных при передаче из-за того, что для видео потребовалось больше буфера, чем было доступно",
        "The number of times that a program association table (PAT) error occurred": "Количество случаев возникновения ошибки таблицы ассоциаций программ (PAT)",
        "The number of times that a program clock register (PCR) accuracy error occurred": "Количество случаев возникновения ошибки точности регистра часов программы (PCR)",
        "The number of times that a PCR error occurred": "Количество случаев возникновения ошибки PCR",
        "The number of times that a packet identifier (PID) error occurred": "Количество случаев возникновения ошибки идентификатора пакета (PID)",
        "The number of times that a program map table (PMT) error occurred": "Количество случаев возникновения ошибки таблицы карты программ (PMT)",
        "The number of times that a presentation timestamp (PTS) error occurred": "Количество случаев возникновения ошибки метки времени представления (PTS)",
        "The percentage of packets that were lost during transit, even if they were recovered": "Процент пакетов, потерянных при передаче, даже если они были восстановлены",
        "The number of packets that were lost during transit, but recovered": "Количество пакетов, потерянных при передаче, но восстановленных",
        "The amount of time it takes for the source to send a signal and receive an acknowledgment from AWS Elemental MediaConnect": "Время, которое требуется источнику для отправки сигнала и получения подтверждения от AWS Elemental MediaConnect",
        "The bitrate of the incoming (source) video": "Битрейт входящего (исходного) видео",
        "The number of times that a transport stream (TS) byte error occurred": "Количество случаев возникновения ошибки байта транспортного потока (TS)",
        "The number of times that a transport stream (TS) sync loss error occurred": "Количество случаев возникновения ошибки потери синхронизации транспортного потока (TS)",
        "The total number of packets that were received": "Общее количество полученных пакетов",
        "The number of times that a primary transport error occurred": "Количество случаев возникновения ошибки основного транспорта",
    }
)

# ---- SageMaker ----
RU.update(
    {
        "The percentage of CPU units that are used by the containers on an instance. The value can range between `0%` and `100%`, and is multiplied by the number of CPUs. For example, if there are four CPUs, `CPUUtilization` can range from `0%` to `400%'.": "Процент единиц CPU, используемых контейнерами на экземпляре. Значение может варьироваться от `0%` до `100%` и умножается на количество CPU. Например, при четырёх CPU `CPUUtilization` может варьироваться от `0%` до `400%'.",
        "The percentage of memory that is used by the containers on an instance. This value can range between `0%` and `100%`.": "Процент памяти, используемой контейнерами на экземпляре. Это значение может варьироваться от `0%` до `100%`.",
        "The percentage of GPU memory used by the containers on an instance. The value can range between `0%` and `100%` and is multiplied by the number of GPUs. For example, if there are four GPUs, `GPUMemoryUtilization` can range from `0%` to `400%'.": "Процент памяти GPU, используемой контейнерами на экземпляре. Значение может варьироваться от `0%` до `100%` и умножается на количество GPU. Например, при четырёх GPU `GPUMemoryUtilization` может варьироваться от `0%` до `400%'.",
        "The percentage of GPU units that are used by the containers on an instance. The value can range between `0%` and `100%`and is multiplied by the number of GPUs. For example, if there are four GPUs, `GPUUtilization` can range from `0%` to `400%'.": "Процент единиц GPU, используемых контейнерами на экземпляре. Значение может варьироваться от `0%` до `100%` и умножается на количество GPU. Например, при четырёх GPU `GPUUtilization` может варьироваться от `0%` до `400%'.",
        "The percentage of disk space used by the containers on an instance uses. This value can range between `0%` and `100%`. This metric is not supported for batch transform jobs.": "Процент дискового пространства, используемого контейнерами на экземпляре. Это значение может варьироваться от `0%` до `100%`. Эта метрика не поддерживается для заданий пакетного преобразования.",
        "The number of models loaded in the containers of the multi-model endpoint. This metric is emitted per instance.": "Количество моделей, загруженных в контейнеры мультимодельной конечной точки. Эта метрика выдаётся для каждого экземпляра.",
        "The number of `InvokeEndpoint` requests where the model returned a `4xx` HTTP response code. For each `4xx` response, `1` is sent; otherwise, `0` is sent.": "Количество запросов `InvokeEndpoint`, при которых модель вернула код ответа HTTP `4xx`. Для каждого ответа `4xx` отправляется `1`, в противном случае отправляется `0`.",
        "The number of `InvokeEndpoint` requests where the model returned a `5xx` HTTP response code. For each `5xx` response, `1` is sent; otherwise, `0` is sent.": "Количество запросов `InvokeEndpoint`, при которых модель вернула код ответа HTTP `5xx`. Для каждого ответа `5xx` отправляется `1`, в противном случае отправляется `0`.",
        "The number of `InvokeEndpoint` requests sent to a model endpoint": "Количество запросов `InvokeEndpoint`, отправленных в конечную точку модели",
        "The number of invocations sent to a model, normalized by `InstanceCount` in each `ProductionVariant`. `1/numberOfInstances` is sent as the value on each request, where `numberOfInstances` is the number of active instances for the `ProductionVariant` behind the endpoint at the time of the request.": "Количество вызовов, отправленных в модель, нормализованное по `InstanceCount` в каждом `ProductionVariant`. В качестве значения для каждого запроса отправляется `1/numberOfInstances`, где `numberOfInstances` означает количество активных экземпляров для `ProductionVariant` за конечной точкой на момент запроса.",
        "The number of `InvokeEndpoint` requests sent to the multi-model endpoint for which the model was already loaded": "Количество запросов `InvokeEndpoint`, отправленных в мультимодельную конечную точку, для которых модель уже была загружена",
        "The interval of time taken by a model to respond as viewed from SageMaker. This interval includes the local communication times taken to send the request and to fetch the response from the container of a model and the time taken to complete the inference in the container.": "Интервал времени, затраченный моделью на ответ, с точки зрения SageMaker. Этот интервал включает время локального обмена данными, затраченное на отправку запроса и получение ответа из контейнера модели, а также время, затраченное на завершение вывода в контейнере.",
        "The interval of time that it took to load the model through the container's `LoadModel` API call.": "Интервал времени, затраченный на загрузку модели через вызов API `LoadModel` контейнера.",
        "The interval of time that an invocation request has waited for the target model to be downloaded, or loaded, or both in order to perform inference": "Интервал времени, в течение которого запрос на вызов ожидал скачивания, загрузки или того и другого для целевой модели, чтобы выполнить вывод",
        "The interval of time that it took to download the model from Amazon Simple Storage Service (Amazon S3)": "Интервал времени, затраченный на скачивание модели из Amazon Simple Storage Service (Amazon S3)",
        "The interval of time that it took to unload the model through the container's `UnloadModel` API call": "Интервал времени, затраченный на выгрузку модели через вызов API `UnloadModel` контейнера",
        "The interval of time added to the time taken to respond to a client request by SageMaker overheads. This interval is measured from the time SageMaker receives the request until it returns a response to the client, minus the `ModelLatency`.": "Интервал времени, добавленный к времени ответа на запрос клиента из-за накладных расходов SageMaker. Этот интервал измеряется с момента получения запроса SageMaker до возврата ответа клиенту, за вычетом `ModelLatency`.",
        "The number of workers on a private work team performing a labeling job": "Количество работников в частной рабочей группе, выполняющих задание разметки",
        "The number of dataset objects auto-annotated in a labeling job. This metric is only emitted when automated labeling is enabled.": "Количество объектов набора данных, автоматически аннотированных в задании разметки. Эта метрика выдаётся только при включённой автоматической разметке.",
        "The number of dataset objects annotated by a human in a labeling job": "Количество объектов набора данных, аннотированных человеком в задании разметки",
        "The number of dataset objects that failed labeling in a labeling job": "Количество объектов набора данных, для которых разметка завершилась неудачно в задании разметки",
        "The number of labeling jobs that failed": "Количество заданий разметки, завершившихся неудачно",
        "The number of labeling jobs that were stopped": "Количество остановленных заданий разметки",
        "The number of labeling jobs that succeeded": "Количество успешно выполненных заданий разметки",
        "The number of tasks submitted/completed by a private work team": "Количество задач, отправленных/выполненных частной рабочей группой",
        "Time spent on a task completed by a private work team": "Время, затраченное на задачу, выполненную частной рабочей группой",
        "The number of dataset objects labeled successfully in a labeling job": "Количество объектов набора данных, успешно размеченных в задании разметки",
    }
)

# ---- GameLift ----
RU.update(
    {
        "Game sessions with `Activating` status, which means they are in the process of starting up": "Игровые сессии со статусом `Activating`, что означает, что они находятся в процессе запуска",
        "Game sessions with `Active` status, which means they are able to host players, and are hosting zero or more players": "Игровые сессии со статусом `Active`, что означает, что они способны принимать игроков и обслуживают ноль или более игроков",
        "Instances with `Active` status, which means they are running active server processes": "Экземпляры со статусом `Active`, что означает, что на них выполняются активные серверные процессы",
        "Server processes with `Active` status, which means they are running and able to host game session": "Серверные процессы со статусом `Active`, что означает, что они выполняются и способны обслуживать игровую сессию",
        "Active, healthy server processes that are not currently being used to host a game session and can start a new game session without a delay to spin up new server processes or instances": "Активные, исправные серверные процессы, которые в настоящее время не используются для обслуживания игровой сессии и могут запустить новую игровую сессию без задержки на развёртывание новых серверных процессов или экземпляров",
        "Average amount of time that game session placement requests in the queue in `Pending` status have been waiting to be fulfilled": "Среднее время, в течение которого запросы на размещение игровых сессий в очереди со статусом `Pending` ожидали выполнения",
        "Player sessions with either `Active` status (player is connected to an active game session) or `Reserved` status (player has been given a slot in a game session but hasn't yet connected)": "Сессии игроков со статусом `Active` (игрок подключён к активной игровой сессии) или `Reserved` (игроку выделен слот в игровой сессии, но он ещё не подключился)",
        "Matchmaking requests currently being processed or waiting to be processed": "Запросы на подбор игроков, которые в настоящее время обрабатываются или ожидают обработки",
        "Target number of active instances that GameLift is working to maintain in the fleet": "Целевое количество активных экземпляров, которое GameLift стремится поддерживать во флоте",
        "Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet isn't considered viable (such as a spot fleet with a high interruption rate)": "Игровые сессии, успешно размещённые, но не во флоте первого выбора, поскольку этот флот не считается жизнеспособным (например, spot-флот с высокой частотой прерываний)",
        "Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet doesn't have any available resources": "Игровые сессии, успешно размещённые, но не во флоте первого выбора, поскольку у этого флота нет доступных ресурсов",
        "Number of game sessions on spot instances that have been interrupted": "Количество игровых сессий на spot-экземплярах, которые были прерваны",
        "Active server processes that are reporting healthy": "Активные серверные процессы, сообщающие об исправном состоянии",
        "Active instances that are currently hosting zero (0) game sessions. This metric measures capacity that is available but unused.": "Активные экземпляры, которые в настоящее время обслуживают ноль (0) игровых сессий. Эта метрика измеряет доступную, но неиспользуемую ёмкость.",
        "Number of spot instances that have been interrupted": "Количество spot-экземпляров, которые были прерваны",
        "Game sessions that were successfully placed in a region that offers the queue's lowest possible latency for the players": "Игровые сессии, успешно размещённые в регионе, который обеспечивает наименьшую возможную задержку очереди для игроков",
        "Game sessions that were successfully placed in a fleet with the queue's lowest possible price for the chosen region": "Игровые сессии, успешно размещённые во флоте с наименьшей возможной ценой очереди для выбранного региона",
        "For matchmaking configurations that require acceptance, the potential matches that timed out during acceptance since the last report": "Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, время ожидания которых истекло во время принятия с момента последнего отчёта",
        "For matchmaking configurations that require acceptance, the potential matches that were accepted since the last report": "Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, принятые с момента последнего отчёта",
        "Potential matches that were created since the last report": "Потенциальные матчи, созданные с момента последнего отчёта",
        "Matches that were successfully placed into a game session since the last report": "Матчи, успешно размещённые в игровой сессии с момента последнего отчёта",
        "For matchmaking configurations that require acceptance, the potential matches that were rejected by at least one player since the last report": "Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, отклонённые хотя бы одним игроком с момента последнего отчёта",
        "Maximum number of instances that are allowed for the fleet": "Максимальное количество экземпляров, разрешённое для флота",
        "Minimum number of instances allowed for the fleet": "Минимальное количество экземпляров, разрешённое для флота",
        "Percentage of game session slots on all active server processes (healthy or unhealthy) that are not currently being used (calculated as `AvailableGameSessions` / [`ActiveGameSessions` + `AvailableGameSessions` + unhealthy server processes])": "Процент слотов игровых сессий на всех активных серверных процессах (исправных или неисправных), которые в настоящее время не используются (рассчитывается как `AvailableGameSessions` / [`ActiveGameSessions` + `AvailableGameSessions` + неисправные серверные процессы])",
        "Percentage of all active server processes that are reporting healthy (calculated as `HealthyServerProcesses` / `ActiveServerProcesses`)": "Процент всех активных серверных процессов, сообщающих об исправном состоянии (рассчитывается как `HealthyServerProcesses` / `ActiveServerProcesses`)",
        "Percentage of all active instances that are idle (calculated as `IdleInstances` / `ActiveInstances`)": "Процент всех активных экземпляров, простаивающих (рассчитывается как `IdleInstances` / `ActiveInstances`)",
        "Game session placement requests canceled before timing out since the last report": "Запросы на размещение игровых сессий, отменённые до истечения времени ожидания, с момента последнего отчёта",
        "Game session placement requests that failed for any reason since the last report": "Запросы на размещение игровых сессий, завершившиеся неудачно по любой причине, с момента последнего отчёта",
        "New game session placement requests added to the queue since the last report": "Новые запросы на размещение игровых сессий, добавленные в очередь с момента последнего отчёта",
        "Game session placement requests that resulted in a new game session since the last report": "Запросы на размещение игровых сессий, приведшие к созданию новой игровой сессии, с момента последнего отчёта",
        "Game session placement requests that reached the queue's timeout limit without being fulfilled since the last report": "Запросы на размещение игровых сессий, достигшие предела времени ожидания очереди без выполнения, с момента последнего отчёта",
        "Player sessions that transitioned from `Reserved` to `Active` status since the last report": "Сессии игроков, перешедшие из статуса `Reserved` в `Active` с момента последнего отчёта",
        "Players in matchmaking tickets that were added since the last report": "Игроки в тикетах подбора игроков, добавленные с момента последнего отчёта",
        "Number of game session placement requests in the queue with `Pending` status": "Количество запросов на размещение игровых сессий в очереди со статусом `Pending`",
        "Server processes that were shut down due to abnormal circumstances since the last report": "Серверные процессы, остановленные из-за нештатных обстоятельств, с момента последнего отчёта",
        "Server processes that successfully transitioned from `Activating` to `Active` status since the last report": "Серверные процессы, успешно перешедшие из статуса `Activating` в `Active` с момента последнего отчёта",
        "Server processes that were shut down since the last report": "Серверные процессы, остановленные с момента последнего отчёта",
        "Matchmaking requests that resulted in failure since the last report": "Запросы на подбор игроков, завершившиеся неудачно, с момента последнего отчёта",
        "New matchmaking requests that were created since the last report": "Новые запросы на подбор игроков, созданные с момента последнего отчёта",
        "Matchmaking requests that reached the timeout limit since the last report": "Запросы на подбор игроков, достигшие предела времени ожидания, с момента последнего отчёта",
        "For matchmaking requests that were put into a potential match before the last report, the amount of time between ticket creation and potential match creation": "Для запросов на подбор игроков, помещённых в потенциальный матч до последнего отчёта, время между созданием тикета и созданием потенциального матча",
        "For matchmaking requests that were canceled before the last report, the amount of time between ticket creation and cancellation": "Для запросов на подбор игроков, отменённых до последнего отчёта, время между созданием тикета и отменой",
        "For matchmaking requests that succeeded before the last report, the amount of time between ticket creation and successful match placement": "Для запросов на подбор игроков, успешно выполненных до последнего отчёта, время между созданием тикета и успешным размещением матча",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon SNS (Simple Notification Service) monitoring": "Мониторинг Amazon SNS (Simple Notification Service)",
    "AWS Direct Connect monitoring": "Мониторинг AWS Direct Connect",
    "AWS DMS (Database Migration Service) monitoring": "Мониторинг AWS DMS (Database Migration Service)",
    "AWS Elemental MediaConnect monitoring": "Мониторинг AWS Elemental MediaConnect",
    "Amazon SageMaker (Batch Transform Jobs, Endpoint Instances, Endpoints, Ground Truth, Processing Jobs, Training Jobs) monitoring": "Мониторинг Amazon SageMaker (Batch Transform Jobs, Endpoint Instances, Endpoints, Ground Truth, Processing Jobs, Training Jobs)",
    "Amazon GameLift monitoring": "Мониторинг Amazon GameLift",
}


def main():
    # guard: no em-dash, no mojibake in any RU value
    bad = []
    for k, v in list(RU.items()) + list(ADD_TITLES.items()):
        if "—" in v:
            bad.append("EM-DASH: " + v[:60])
        if "â" in v or "﻿" in v:
            bad.append("MOJIBAKE/BOM: " + v[:60])
    if bad:
        for b in bad:
            print("  GUARD-FAIL:", b)
        return 1

    skel = json.load(open(SKEL_P, encoding="utf-8"))
    norm2ru = {asciinorm(k): v for k, v in RU.items()}
    if len(norm2ru) != len(RU):
        print("  WARN: asciinorm collision in RU keys")
    add_trans = {}
    unmatched_skel = []
    used = set()
    for k in skel:  # k = real (curly) key
        ak = asciinorm(k)
        if ak in norm2ru:
            add_trans[k] = norm2ru[ak]
            used.add(ak)
        else:
            unmatched_skel.append(k)
    unused_mine = [k for k in norm2ru if k not in used]

    print(f"skeleton keys: {len(skel)} | matched: {len(add_trans)}")
    if unmatched_skel:
        print(f"--- UNMATCHED skeleton keys ({len(unmatched_skel)}) ---")
        for k in unmatched_skel:
            print("  MISS:", k[:90])
    if unused_mine:
        print(f"--- UNUSED my translations ({len(unused_mine)}) ---")
        for k in unused_mine:
            print("  EXTRA:", k[:90])
    if unmatched_skel:
        print("ABORT: not all skeleton keys covered; fix before merging.")
        return 1

    def merge(path, add):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        before = len(d)
        d.update(add)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=1)
        print(
            f"{os.path.basename(path)}: {before} -> {len(d)} (+{len(d) - before} net; {len(add)} offered)"
        )

    merge(TRANS_P, add_trans)
    merge(TITLE_P, ADD_TITLES)
    print("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
