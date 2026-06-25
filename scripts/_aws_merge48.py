# -*- coding: utf-8 -*-
"""Merge L4-IF.48 batch (7 standard AWS compute/integration files: AppSync,
CodeBuild, Connect, Lambda (new), Step Functions, Simple Workflow Service (SWF),
CloudHSM v2) translations into the shared cumulative dicts
(_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Same mechanism as L4-IF.45/46/47: translations keyed by an ASCII-normalized form
of the EN text, matched against the real skeleton keys programmatically. asciinorm
also folds markdown escapes (\\_ \\*) and curly punctuation. Any skeleton key left
without a translation, or any translation matching no skeleton key, is reported
(self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Re-runnable.
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if48.json")


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
        ("\\_", "_"),
        ("\\*", "*"),
    ]:
        s = s.replace(a, b)
    return s


# ---- intro template (verbatim shipped canon V1, service name swapped) ----
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

# intros (all V1)
for svc in [
    "AWS AppSync",
    "AWS CodeBuild",
    "Amazon Connect",
    "AWS Lambda",
    "AWS Step Functions",
    "Amazon Simple Workflow Service (Amazon SWF)",
    "AWS CloudHSM (V2)",
]:
    RU[en_v1(svc)] = ru_v1(svc)

# H1 headings (body)
RU.update(
    {
        "# AWS AppSync monitoring": "# Мониторинг AWS AppSync",
        "# AWS CodeBuild monitoring": "# Мониторинг AWS CodeBuild",
        "# Amazon Connect monitoring": "# Мониторинг Amazon Connect",
        "# AWS Lambda monitoring": "# Мониторинг AWS Lambda",
        "# AWS Step Functions monitoring": "# Мониторинг AWS Step Functions",
        "# Amazon SWF (Simple Workflow Service) monitoring": "# Мониторинг Amazon SWF (Simple Workflow Service)",
        "# AWS CloudHSM (V2) monitoring": "# Мониторинг AWS CloudHSM (V2)",
    }
)

# main-dimension notes (InstanceId / ClusterId already in shared dict)
for dim in ["GraphQLAPIId", "ProjectName", "FunctionName", "Domain"]:
    RU["`%s` is the main dimension." % dim] = "Основное измерение: `%s`." % dim

# date bullet (Lambda)
RU["* Updated on Nov 15, 2023"] = "* Обновлено 15 ноября 2023 г."

# ---- special prose ----
RU.update(
    {
        "For information about differences between classic services and other services, see [Migrate from AWS classic (formerly 'built-in') services to cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide \"Migrate AWS classic services to their new versions.\").": 'Сведения о различиях между классическими сервисами и другими сервисами см. в разделе [Переход с классических (ранее «встроенных») сервисов AWS на облачные сервисы](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Переход с классических сервисов AWS на их новые версии.").',
        "This service monitors a part of AWS Lambda (AWS/Lambda). While you have this service configured, you can't have AWS Lambda (built-in) service turned on.": "Этот сервис отслеживает часть AWS Lambda (AWS/Lambda). Пока этот сервис настроен, нельзя включить сервис AWS Lambda (built-in).",
        "While Dynatrace doesn't support WebSocket traffic, the AppSync integration shows the WebSocket URL as part of the properties for the custom devices that are created.": "Хотя Dynatrace не поддерживает трафик WebSocket, интеграция AppSync отображает URL-адрес WebSocket в составе свойств создаваемых пользовательских устройств.",
        "Dynatrace gathers metrics for AWS Step Functions at the custom device group level instead of the custom device level (metrics are service-wide).": "Dynatrace собирает метрики для AWS Step Functions на уровне группы пользовательских устройств, а не на уровне пользовательского устройства (метрики действуют в масштабе всего сервиса).",
        "CloudHSM Classic isn't supported.": "CloudHSM Classic не поддерживается.",
    }
)

# ---- AppSync metric cells ----
RU.update(
    {
        "The number of concurrent WebSocket connections from clients to AWS AppSync in 1 minute": "Количество одновременных подключений WebSocket от клиентов к AWS AppSync за 1 минуту",
        "The number of concurrent subscriptions from clients in 1 minute": "Количество одновременных подписок от клиентов за 1 минуту",
        "The number of WebSocket connections that were rejected by AWS AppSync because of client-side errors": "Количество подключений WebSocket, отклонённых AWS AppSync из-за ошибок на стороне клиента",
        "The number of errors that originated from AWS AppSync while processing connections": "Количество ошибок, возникших в AWS AppSync при обработке подключений",
        "The number of successful WebSocket connections to AWS AppSync": "Количество успешных подключений WebSocket к AWS AppSync",
        "The amount of time that the connection stays open": "Время, в течение которого подключение остаётся открытым",
        "The number of errors that originated from AWS AppSync when disconnecting WebSocket connections due to client-side errors": "Количество ошибок, возникших в AWS AppSync при разрыве подключений WebSocket из-за ошибок на стороне клиента",
        "The number of errors that originated from AWS AppSync when disconnecting WebSocket connections while processing connections": "Количество ошибок, возникших в AWS AppSync при разрыве подключений WebSocket в процессе обработки подключений",
        "The number of successful WebSocket disconnections from AWS AppSync": "Количество успешных разрывов подключений WebSocket в AWS AppSync",
        "The time between when AWS AppSync receives a request from a client and when it returns a response to the client": "Время между получением AWS AppSync запроса от клиента и возвратом ответа клиенту",
        "The number of subscription event messages that failed to publish because of client-side errors": "Количество сообщений о событиях подписки, которые не удалось опубликовать из-за ошибок на стороне клиента",
        "The number of errors that originated from AWS AppSync while publishing subscription event messages": "Количество ошибок, возникших в AWS AppSync при публикации сообщений о событиях подписки",
        "The size of subscription event messages published": "Размер опубликованных сообщений о событиях подписки",
        "The number of subscription event messages that were successfully published": "Количество успешно опубликованных сообщений о событиях подписки",
        "The number of errors that originated from AWS AppSync while processing subscriptions": "Количество ошибок, возникших в AWS AppSync при обработке подписок",
        "The number of subscriptions that were successfully registered to AWS AppSync through WebSocket": "Количество подписок, успешно зарегистрированных в AWS AppSync через WebSocket",
        "The number of unsubscriptions that were rejected by AWS AppSync because of client-side errors": "Количество отписок, отклонённых AWS AppSync из-за ошибок на стороне клиента",
        "The number of errors that originated from AWS AppSync while processing unsubscriptions": "Количество ошибок, возникших в AWS AppSync при обработке отписок",
        "The number of unsubscriptions that were successfully processed from AWS AppSync": "Количество отписок, успешно обработанных в AWS AppSync",
    }
)

# ---- CodeBuild metric cells ----
RU.update(
    {
        "Measures the duration of the build's `BUILD` phase": "Измеряет длительность фазы `BUILD` сборки",
        "Measures the number of builds triggered": "Измеряет количество запущенных сборок",
        "The number of CPU units of allocated processing used by the build container": "Количество единиц CPU выделенной вычислительной мощности, используемых контейнером сборки",
        "The percentage of allocated processing used by the build container": "Процент выделенной вычислительной мощности, используемой контейнером сборки",
        "Measures the duration of the build's `DOWNLOAD_SOURCE` phase": "Измеряет длительность фазы `DOWNLOAD_SOURCE` сборки",
        "Measures the duration of all builds over time": "Измеряет длительность всех сборок за период времени",
        "Measures the number of builds that failed because of client error or a timeout": "Измеряет количество сборок, завершившихся сбоем из-за ошибки клиента или тайм-аута",
        "Measures the duration of the build's `FINALIZING` phase": "Измеряет длительность фазы `FINALIZING` сборки",
        "Measures the duration of the build's `INSTALL` phase": "Измеряет длительность фазы `INSTALL` сборки",
        "The number of megabytes of memory used by the build container": "Количество мегабайт памяти, используемых контейнером сборки",
        "The percentage of allocated memory used by the build container": "Процент выделенной памяти, используемой контейнером сборки",
        "Measures the duration of the build's `POST_BUILD` phase": "Измеряет длительность фазы `POST_BUILD` сборки",
        "Measures the duration of the build's `PRE_BUILD` phase": "Измеряет длительность фазы `PRE_BUILD` сборки",
        "Measures the duration of the build's `PROVISIONING` phase": "Измеряет длительность фазы `PROVISIONING` сборки",
        "Measures the duration of the build's `QUEUED` phase": "Измеряет длительность фазы `QUEUED` сборки",
        "The storage read speed used by the build container": "Скорость чтения из хранилища, используемая контейнером сборки",
        "The storage write speed used by the build container": "Скорость записи в хранилище, используемая контейнером сборки",
        "Measures the duration of the build's `SUBMITTED` phase": "Измеряет длительность фазы `SUBMITTED` сборки",
        "Measures the number of successful builds": "Измеряет количество успешных сборок",
        "Measures the duration of the build's `UPLOAD_ARTIFACTS` phase": "Измеряет длительность фазы `UPLOAD_ARTIFACTS` сборки",
    }
)

# ---- Connect metric cells ----
RU.update(
    {
        "The number of times a queued callback to a customer could not be dialed because the customer's number is in a country for which outbound calls are not allowed for the instance": "Количество случаев, когда поставленный в очередь обратный вызов клиенту не удалось набрать, поскольку номер клиента находится в стране, для которой исходящие вызовы для экземпляра не разрешены",
        "The number of call recordings that failed to upload to the Amazon S3 bucket configured for your instance": "Количество записей вызовов, которые не удалось загрузить в корзину Amazon S3, настроенную для вашего экземпляра",
        "The total number of voice calls that exceeded the concurrent calls quota for the instance": "Общее количество голосовых вызовов, превысивших квоту одновременных вызовов для экземпляра",
        "The number of voice calls, both inbound and outbound, received or placed per second in the instance": "Количество голосовых вызовов, как входящих, так и исходящих, принятых или совершённых в секунду в экземпляре",
        "The number of concurrent active voice calls in the instance at the time the data is displayed on the dashboard": "Количество одновременных активных голосовых вызовов в экземпляре на момент отображения данных на дашборде",
        "The percentage of the concurrent active voice calls service quota used in the instance": "Процент использованной в экземпляре сервисной квоты на одновременные активные голосовые вызовы",
        "The number of times the error branch for a contact flow was executed": "Количество случаев выполнения ветви ошибки для потока обращений",
        "The number of times a contact flow failed to execute due to a system error": "Количество случаев, когда поток обращений не удалось выполнить из-за системной ошибки",
        "The longest amount of time, in seconds, that a contact waited in a queue": "Наибольшее время в секундах, в течение которого обращение ожидало в очереди",
        "The number of calls that failed because the phone number is not associated with a contact flow": "Количество вызовов, завершившихся сбоем, поскольку номер телефона не связан с потоком обращений",
        "The number of voice calls that were missed by agents during the refresh interval selected, such as 1 minute or 5 minutes. A missed call is one that is not answered by an agent within 20 seconds.": "Количество голосовых вызовов, пропущенных операторами в течение выбранного интервала обновления, например 1 минуты или 5 минут. Пропущенным считается вызов, на который оператор не ответил в течение 20 секунд.",
        "The number of times a contact flow security key (public signing key) was used to encrypt customer input in a contact flow": "Количество случаев использования ключа безопасности потока обращений (открытого ключа подписи) для шифрования вводимых клиентом данных в потоке обращений",
        "The number of calls that were rejected because the queue was full": "Количество вызовов, отклонённых из-за заполненности очереди",
        "The number of contacts in the queue": "Количество обращений в очереди",
        "The number of voice calls that were rejected because the rate of calls per second exceeded the maximum supported quota": "Количество голосовых вызовов, отклонённых из-за того, что частота вызовов в секунду превысила максимально поддерживаемую квоту",
        "The ratio of packet loss for calls in the instance, reported every 10 seconds. Each data point is between 0 and 1, which represents the ratio of packets lost for the instance.": "Доля потерь пакетов для вызовов в экземпляре; регистрируется каждые 10 секунд. Каждая точка данных находится в диапазоне от 0 до 1 и представляет долю потерянных пакетов для экземпляра.",
    }
)

# ---- Lambda metric cells ----
RU.update(
    {
        "The time between when Lambda successfully queues the event and when the function is invoked.": "Время между моментом, когда Lambda успешно ставит событие в очередь, и моментом вызова функции.",
        "The number of events that are dropped without successfully executing the function.": "Количество событий, которые отбрасываются без успешного выполнения функции.",
        "The number of events that Lambda successfully queues for processing.": "Количество событий, которые Lambda успешно ставит в очередь на обработку.",
        "The number of function instances that are processing events.": "Количество экземпляров функции, обрабатывающих события.",
        "For asynchronous invocation, the number of times that Lambda attempts to send an event to a dead-letter queue (DLQ) but fails.": "Для асинхронного вызова: количество случаев, когда Lambda пытается отправить событие в очередь недоставленных сообщений (DLQ), но безуспешно.",
        "For asynchronous invocation and supported event source mappings, the number of times that Lambda attempts to send an event to a destination but fails.": "Для асинхронного вызова и поддерживаемых сопоставлений источников событий: количество случаев, когда Lambda пытается отправить событие в место назначения, но безуспешно.",
        "The amount of time that your function code spends processing an event.": "Время, которое код вашей функции тратит на обработку события.",
        "The number of invocations that result in a function error.": "Количество вызовов, приводящих к ошибке функции.",
        "The number of times that your function code is invoked, including successful invocations and invocations that result in a function error.": "Количество вызовов кода вашей функции, включая успешные вызовы и вызовы, приводящие к ошибке функции.",
        "For DynamoDB, Kinesis, and Amazon DocumentDB event sources, the age of the last record in the event.": "Для источников событий DynamoDB, Kinesis и Amazon DocumentDB: возраст последней записи в событии.",
        "For self-managed Apache Kafka and Amazon Managed Streaming for Apache Kafka (Amazon MSK) event sources, the difference in offset between the last record written to a topic and the last record that your function's consumer group processed.": "Для источников событий самоуправляемого Apache Kafka и Amazon Managed Streaming for Apache Kafka (Amazon MSK): разница в смещении между последней записью, записанной в топик, и последней записью, обработанной группой потребителей вашей функции.",
        "The cumulative amount of time that the runtime spends running code for extensions after the function code has completed.": "Совокупное время, которое среда выполнения тратит на выполнение кода расширений после завершения кода функции.",
        "The number of times that your function code is invoked using provisioned concurrency.": "Количество вызовов кода вашей функции с использованием подготовленного параллелизма.",
        "The number of times that your function code is invoked using standard concurrency when all provisioned concurrency is in use.": "Количество вызовов кода вашей функции с использованием стандартного параллелизма, когда весь подготовленный параллелизм задействован.",
        "For a version or alias, the value of ProvisionedConcurrentExecutions divided by the total amount of provisioned concurrency allocated.": "Для версии или псевдонима: значение ProvisionedConcurrentExecutions, делённое на общий объём выделенного подготовленного параллелизма.",
        "The number of function instances that are processing events using provisioned concurrency.": "Количество экземпляров функции, обрабатывающих события с использованием подготовленного параллелизма.",
        "The number of times that Lambda has stopped invocation of your function because it's detected that your function is part of an infinite recursive loop.": "Количество случаев, когда Lambda остановила вызов вашей функции, обнаружив, что ваша функция является частью бесконечного рекурсивного цикла.",
        "The number of invocation requests that are throttled.": "Количество запросов на вызов, подвергнутых регулированию.",
        "For a Region, the number of events that functions without reserved concurrency are processing.": "Для региона: количество событий, обрабатываемых функциями без зарезервированного параллелизма.",
    }
)

# ---- Step Functions metric cells ----
RU.update(
    {
        "The number of failed activities": "Количество действий, завершившихся сбоем",
        "The number of activities that time out due to a heartbeat timeout": "Количество действий, для которых истекает тайм-аут из-за тайм-аута контрольного сигнала",
        "The number of scheduled activities": "Количество запланированных действий",
        "The number of started activities": "Количество запущенных действий",
        "The number of successfully completed activities": "Количество успешно завершённых действий",
        "The number of activities that time out on close": "Количество действий, для которых истекает тайм-аут при закрытии",
        "The interval, in milliseconds, between the time the activity starts and the time it closes": "Интервал в миллисекундах между моментом запуска действия и моментом его закрытия",
        "The interval, in milliseconds, for which the activity stays in the schedule state": "Интервал в миллисекундах, в течение которого действие остаётся в состоянии планирования",
        "The interval, in milliseconds, between the time the activity is scheduled and the time it closes": "Интервал в миллисекундах между моментом планирования действия и моментом его закрытия",
        "The count of requests per second": "Количество запросов в секунду",
        "The number of StateEntered events and retries that have been throttled": "Количество событий StateEntered и повторных попыток, подвергнутых регулированию",
        "The interval, in milliseconds, between the time the execution starts and the time it closes": "Интервал в миллисекундах между моментом запуска выполнения и моментом его закрытия",
        "The number of aborted or terminated executions": "Количество прерванных или прекращённых выполнений",
        "The number of failed executions": "Количество выполнений, завершившихся сбоем",
        "The number of started executions": "Количество запущенных выполнений",
        "The number of successfully completed executions": "Количество успешно завершённых выполнений",
        "The number of executions that time out for any reason": "Количество выполнений, для которых истекает тайм-аут по любой причине",
        "The interval, in milliseconds, between the time the Lambda function starts and the time it closes": "Интервал в миллисекундах между моментом запуска функции Lambda и моментом её закрытия",
        "The interval, in milliseconds, for which the Lambda function stays in the schedule state": "Интервал в миллисекундах, в течение которого функция Lambda остаётся в состоянии планирования",
        "The interval, in milliseconds, between the time the Lambda function is scheduled and the time it closes": "Интервал в миллисекундах между моментом планирования функции Lambda и моментом её закрытия",
        "The number of failed Lambda functions": "Количество функций Lambda, завершившихся сбоем",
        "The number of scheduled Lambda functions": "Количество запланированных функций Lambda",
        "The number of started Lambda functions": "Количество запущенных функций Lambda",
        "The number of successfully completed Lambda functions": "Количество успешно завершённых функций Lambda",
        "The number of Lambda functions that time out on close": "Количество функций Lambda, для которых истекает тайм-аут при закрытии",
        "The count of available requests per second": "Количество доступных запросов в секунду",
        "The count of requests per second that are allowed into the bucket": "Количество запросов в секунду, допускаемых в сегмент",
        "The interval, in milliseconds, between the time the service task starts and the time it closes": "Интервал в миллисекундах между моментом запуска сервисной задачи и моментом её закрытия",
        "The interval, in milliseconds, for which the service task stays in the schedule state": "Интервал в миллисекундах, в течение которого сервисная задача остаётся в состоянии планирования",
        "The interval, in milliseconds, between the time the service task is scheduled and the time it closes": "Интервал в миллисекундах между моментом планирования сервисной задачи и моментом её закрытия",
        "The number of failed service tasks": "Количество сервисных задач, завершившихся сбоем",
        "The number of scheduled service tasks.": "Количество запланированных сервисных задач.",
        "The number of started service tasks": "Количество запущенных сервисных задач",
        "The number of successfully completed service tasks": "Количество успешно завершённых сервисных задач",
        "The number of service tasks that time out on close": "Количество сервисных задач, для которых истекает тайм-аут при закрытии",
        "The count of requests that have been throttled": "Количество запросов, подвергнутых регулированию",
    }
)

# ---- SWF metric cells ----
RU.update(
    {
        "The time interval, in milliseconds, between the time when the activity was scheduled and when it closed": "Интервал времени в миллисекундах между моментом, когда действие было запланировано, и моментом, когда оно было закрыто",
        "The time interval, in milliseconds, between the time when the activity task was scheduled and when it started": "Интервал времени в миллисекундах между моментом, когда задача действия была запланирована, и моментом, когда она была запущена",
        "The time interval, in milliseconds, between the time when the activity task started and when it closed": "Интервал времени в миллисекундах между моментом, когда задача действия была запущена, и моментом, когда она была закрыта",
        "The count of activity tasks that were canceled": "Количество отменённых задач действий",
        "The count of activity tasks that completed": "Количество завершённых задач действий",
        "The count of activity tasks that failed": "Количество задач действий, завершившихся сбоем",
        "The time interval, in milliseconds, between the time that the decision task was scheduled and when it was picked up by a worker and started": "Интервал времени в миллисекундах между моментом, когда задача принятия решения была запланирована, и моментом, когда она была взята исполнителем и запущена",
        "The time interval, in milliseconds, between the time that the decision task was started and when it closed": "Интервал времени в миллисекундах между моментом, когда задача принятия решения была запущена, и моментом, когда она была закрыта",
        "The count of decision tasks that have been completed": "Количество завершённых задач принятия решений",
        "The count of pending tasks in a one minute interval for a specific task list": "Количество ожидающих задач за интервал в одну минуту для конкретного списка задач",
        "The count of activity tasks that were scheduled but timed out on close": "Количество задач действий, которые были запланированы, но завершились по тайм-ауту при закрытии",
        "The count of activity tasks that were scheduled but timed out on start": "Количество задач действий, которые были запланированы, но завершились по тайм-ауту при запуске",
        "The count of activity tasks that were started but timed out on close": "Количество задач действий, которые были запущены, но завершились по тайм-ауту при закрытии",
        "The count of activity tasks that were started but timed out due to a heartbeat timeout": "Количество задач действий, которые были запущены, но завершились по тайм-ауту из-за тайм-аута контрольного сигнала",
        "The count of decision tasks that started but timed out on closing": "Количество задач принятия решений, которые были запущены, но завершились по тайм-ауту при закрытии",
        "The time, in milliseconds, between the time the workflow started and when it closed": "Время в миллисекундах между моментом запуска рабочего процесса и моментом его закрытия",
        "The count of workflows that were canceled": "Количество отменённых рабочих процессов",
        "The count of workflows that completed": "Количество завершённых рабочих процессов",
        "The count of workflows that continued as new": "Количество рабочих процессов, продолженных как новые",
        "The count of workflows that failed": "Количество рабочих процессов, завершившихся сбоем",
        "The count of workflows that were terminated": "Количество прекращённых рабочих процессов",
        "The count of workflows that timed out, for any reason": "Количество рабочих процессов, завершившихся по тайм-ауту по любой причине",
    }
)

# ---- CloudHSM v2 metric cells ----
RU.update(
    {
        "The HSM instance is not performing properly": "Экземпляр HSM работает некорректно",
        "Junction temperature of the hardware processor": "Температура перехода аппаратного процессора",
        "Number of session keys being used by the HSM instance": "Количество сеансовых ключей, используемых экземпляром HSM",
        "Number of token keys being used by the HSM instance and the cluster": "Количество ключей токенов, используемых экземпляром HSM и кластером",
        "Number of end-to-end encrypted channels currently established for the HSM instance": "Количество каналов со сквозным шифрованием, установленных в настоящее время для экземпляра HSM",
        "Number of open connections to the HSM instance": "Количество открытых подключений к экземпляру HSM",
        "Number of additional users that can be created": "Количество дополнительных пользователей, которых можно создать",
        "Maximum number of users that can be created on the HSM instance": "Максимальное количество пользователей, которых можно создать на экземпляре HSM",
        "Number of dropped packets on input": "Количество отброшенных пакетов на входе",
        "Number of error packets on input": "Количество пакетов с ошибками на входе",
        "Cumulative sum of traffic to the HSM to date": "Накопительная сумма трафика к HSM на текущий момент",
        "Total number of packets on input": "Общее количество пакетов на входе",
        "Number of dropped packets on output": "Количество отброшенных пакетов на выходе",
        "Number of error packets on output": "Количество пакетов с ошибками на выходе",
        "Cumulative sum of traffic from the HSM to date": "Накопительная сумма трафика от HSM на текущий момент",
        "Total number of packets on output": "Общее количество пакетов на выходе",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "AWS AppSync monitoring": "Мониторинг AWS AppSync",
    "AWS CodeBuild monitoring": "Мониторинг AWS CodeBuild",
    "Amazon Connect monitoring": "Мониторинг Amazon Connect",
    "AWS Lambda monitoring": "Мониторинг AWS Lambda",
    "AWS Step Functions monitoring": "Мониторинг AWS Step Functions",
    "Amazon SWF (Simple Workflow Service) monitoring": "Мониторинг Amazon SWF (Simple Workflow Service)",
    "AWS CloudHSM (V2) monitoring": "Мониторинг AWS CloudHSM (V2)",
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
    for k in skel:  # k = real skeleton key (byte-identical with EN source)
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
            print("  MISS:", k[:110])
    if unused_mine:
        print(f"--- UNUSED my translations ({len(unused_mine)}) ---")
        for k in unused_mine:
            print("  EXTRA:", k[:110])
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
