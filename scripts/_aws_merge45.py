# -*- coding: utf-8 -*-
"""Merge L4-IF.45 batch (16 standard AWS files) translations into the shared
cumulative dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).

Translations are keyed by an ASCII-normalized form of the EN text; they are
matched against the real (curly-quote / demoji'd) skeleton keys programmatically
so curly apostrophes never have to be hand-typed. Any skeleton key left without
a translation, or any translation that matches no skeleton key, is reported
(self-validation against typos). Asserts: no em-dash, no mojibake in RU.
Re-runnable: loads existing dict, updates, writes back (1-space indent, UTF-8).
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")
SKEL_P = os.path.join(HERE, "_aws_missing_l4if45.json")


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


# intro templates (verbatim canon, service name swapped)
def en_v1(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view metrics for each service instance, split metrics into multiple dimensions, "
        "and create custom charts that you can pin to your dashboards." % s
    )


def en_v2(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view graphs per service instance, with a set of dimensions, "
        "and create custom graphs that you can pin to your dashboards." % s
    )


def ru_v1(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений "
        "и создавать собственные графики, которые можно закреплять на дашбордах." % s
    )


def ru_v2(s):
    return (
        "Dynatrace принимает метрики для множества предопределённых пространств имён, включая %s. "
        "Можно просматривать графики по каждому экземпляру сервиса с набором измерений "
        "и создавать собственные графики, которые можно закреплять на дашбордах." % s
    )


RU = {}

# ---- intros ----
for svc in [
    "Amazon EventBridge",
    "Amazon Elastic Inference",
    "Amazon Elastic Transcoder",
    "AWS Elemental MediaConvert",
    "AWS Elemental MediaTailor",
    "Amazon QLDB",
]:
    RU[en_v2(svc)] = ru_v2(svc)
for svc in [
    "Amazon Simple Queue Service (Amazon SQS)",
    "Amazon WorkSpaces",
    "AWS IoT Things Graph",
    "Amazon Simple Email Service (Amazon SES)",
    "AWS Certificate Manager Private Certificate Authority",
    "Amazon API Gateway",
    "AWS DataSync",
    "Amazon VPC NAT Gateways",
    "AWS Elemental MediaPackage (Live, Video on Demand)",
    "AWS OpsWorks",
]:
    RU[en_v1(svc)] = ru_v1(svc)

# ---- H1 headings (title with leading "# ") ----
RU.update(
    {
        "# Amazon EventBridge monitoring": "# Мониторинг Amazon EventBridge",
        "# Amazon SQS (Simple Queue Service) monitoring": "# Мониторинг Amazon SQS (Simple Queue Service)",
        "# Amazon Elastic Inference monitoring": "# Мониторинг Amazon Elastic Inference",
        "# Amazon Elastic Transcoder monitoring": "# Мониторинг Amazon Elastic Transcoder",
        "# Amazon WorkSpaces monitoring": "# Мониторинг Amazon WorkSpaces",
        "# AWS IoT Things Graph monitoring": "# Мониторинг AWS IoT Things Graph",
        "# Amazon SES (Simple Email Service) monitoring": "# Мониторинг Amazon SES (Simple Email Service)",
        "# AWS Certificate Manager Private Certificate Authority (ACM PCA) monitoring": "# Мониторинг AWS Certificate Manager Private Certificate Authority (ACM PCA)",
        "# Amazon API Gateway monitoring": "# Мониторинг Amazon API Gateway",
        "# AWS DataSync monitoring": "# Мониторинг AWS DataSync",
        "# AWS Elemental MediaConvert monitoring": "# Мониторинг AWS Elemental MediaConvert",
        "# AWS Elemental MediaTailor monitoring": "# Мониторинг AWS Elemental MediaTailor",
        "# Amazon VPC NAT Gateways monitoring": "# Мониторинг Amazon VPC NAT Gateways",
        "# AWS Elemental MediaPackage (Live, Video on Demand) monitoring": "# Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)",
        "# Amazon QLDB (Quantum Ledger Database) monitoring": "# Мониторинг Amazon QLDB (Quantum Ledger Database)",
        "# AWS OpsWorks monitoring": "# Мониторинг AWS OpsWorks",
    }
)

# ---- boilerplate: read-time, dates, versions, headings kept EN ----
RU.update(
    {
        "* 3-min read": "* Чтение: 3 мин",
        "* 4-min read": "* Чтение: 4 мин",
        "* 5-min read": "* Чтение: 5 мин",
        "* Published May 04, 2021": "* Опубликовано 4 мая 2021 г.",
        "* Updated on Jan 09, 2026": "* Обновлено 9 января 2026 г.",
        "* Dynatrace version 1.217+": "* Dynatrace версия 1.217+",
        "* An Environment or Cluster ActiveGate version 1.197+": "* Environment ActiveGate или Cluster ActiveGate версия 1.197+",
        "* For AWS Elemental MediaPackage Live, Dynatrace version 1.203+": "* Для AWS Elemental MediaPackage Live, Dynatrace версия 1.203+",
        "* For AWS Elemental MediaPackage Video on Demand, Dynatrace version 1.204+": "* Для AWS Elemental MediaPackage Video on Demand, Dynatrace версия 1.204+",
        "* minimum [one agent](https://docs.aws.amazon.com/datasync/latest/userguide/create-agent-cli.html)": "* минимум [один агент](https://docs.aws.amazon.com/datasync/latest/userguide/create-agent-cli.html)",
        "### Example": "### Пример",
        "About dimensions": "Об измерениях",
        # product-edition headings kept EN (identity, matches product-name canon)
        "### AWS Elemental MediaPackage Live": "### AWS Elemental MediaPackage Live",
        "### AWS Elemental MediaPackage Video on Demand (VOD)": "### AWS Elemental MediaPackage Video on Demand (VOD)",
    }
)

# ---- main-dimension notes ----
for dim in [
    "EventBusName",
    "QueueName",
    "InstanceId",
    "PipelineId",
    "WorkspaceId",
    "ApiName",
    "TaskId",
    "Queue",
    "NatGatewayId",
    "Channel",
    "PackagingConfiguration",
    "LedgerName",
    "StackId",
    "PrivateCAArn",
]:
    RU["`%s` is the main dimension." % dim] = "Основное измерение: `%s`." % dim

# ---- EventBridge ----
RU.update(
    {
        "The Amazon EventBridge service is made up of one or multiple event buses. There is a **default event bus**, with service-wide metrics, and you can optionally create additional event buses called **custom event buses**.": "Сервис Amazon EventBridge состоит из одной или нескольких шин событий. Существует **шина событий по умолчанию** с метриками в масштабе всего сервиса, и при желании можно создавать дополнительные шины событий, называемые **пользовательскими шинами событий**.",
        "The default event bus metrics can be viewed in the **Further details** section of the **custom device group** overview page. If you create additional event buses, the custom event bus metrics will show up in the **Further details** section of the **custom device** overview page.": "Метрики шины событий по умолчанию можно просматривать в разделе **Further details** на странице обзора **группы пользовательских устройств**. Если создать дополнительные шины событий, метрики пользовательской шины событий появятся в разделе **Further details** на странице обзора **пользовательского устройства**.",
        "The number of times a rule's target is not invoked in response to an event": "Количество случаев, когда цель правила не вызывается в ответ на событие",
        "The number of invocations that failed permanently": "Количество вызовов, окончательно завершившихся сбоем",
        "The number of times a target is invoked for a rule in response to an event": "Количество случаев вызова цели для правила в ответ на событие",
        "The number of events that matched with any rule": "Количество событий, совпавших с каким-либо правилом",
        "The number of triggered rules that are being throttled": "Количество сработавших правил, подвергаемых регулированию",
        "The number of triggered rules that matched with any event": "Количество сработавших правил, совпавших с каким-либо событием",
        "Amazon EventBridge sends `Invocations` metrics to CloudWatch only if it has a non-zero value. For more information, see [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-monitoring-cloudwatch-metrics.html).": "Amazon EventBridge отправляет метрики `Invocations` в CloudWatch только при ненулевом значении. Дополнительные сведения см. в [документации AWS](https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-monitoring-cloudwatch-metrics.html).",
    }
)

# ---- SQS ----
RU.update(
    {
        "The approximate age of the oldest non-deleted message in the queue": "Приблизительный возраст самого старого неудалённого сообщения в очереди",
        "The number of messages in the queue that are delayed and not available for reading immediately": "Количество сообщений в очереди, которые отложены и недоступны для немедленного чтения",
        "The number of messages that are in flight. Messages are considered to be in flight if they have been sent to a client but haven't yet been deleted or haven't yet reached the end of their visibility window.": "Количество сообщений, находящихся в обработке. Сообщение считается находящимся в обработке, если оно отправлено клиенту, но ещё не удалено или ещё не достигло конца своего окна видимости.",
        "The number of messages available for retrieval from the queue": "Количество сообщений, доступных для извлечения из очереди",
        "The number of `ReceiveMessage` API calls that didn't return a message": "Количество вызовов API `ReceiveMessage`, не вернувших сообщение",
        "The number of messages deleted from the queue": "Количество сообщений, удалённых из очереди",
        "The number of messages returned by calls to the `ReceiveMessage` action": "Количество сообщений, возвращённых вызовами действия `ReceiveMessage`",
        "The number of messages added to a queue": "Количество сообщений, добавленных в очередь",
        "The size of messages added to a queue": "Размер сообщений, добавленных в очередь",
    }
)

# ---- Elastic Inference ----
RU.update(
    {
        "* **ElasticInferenceAcceleratorId** filters the data by the Elastic Inference accelerator.": "* **ElasticInferenceAcceleratorId** фильтрует данные по ускорителю Elastic Inference.",
        "* **InstanceId** filters the data by instance to which the Elastic Inference accelerator is attached.": "* **InstanceId** фильтрует данные по экземпляру, к которому подключён ускоритель Elastic Inference.",
        "Reports whether the Elastic Inference accelerator has passed a status health check in the last minute": "Сообщает, прошёл ли ускоритель Elastic Inference проверку работоспособности статуса за последнюю минуту",
        "The number of inference requests reaching the Elastic Inference accelerator in the last minute that resulted in a 4xx error": "Количество запросов на вывод, достигших ускорителя Elastic Inference за последнюю минуту и приведших к ошибке 4xx",
        "The number of inference requests reaching the Elastic Inference accelerator in the last minute that resulted in a 5xx error": "Количество запросов на вывод, достигших ускорителя Elastic Inference за последнюю минуту и приведших к ошибке 5xx",
        "The memory of the Elastic Inference accelerator used in the last minute": "Объём памяти ускорителя Elastic Inference, использованный за последнюю минуту",
        "The number of successful inference requests reaching the Elastic Inference accelerator in the last minute": "Количество успешных запросов на вывод, достигших ускорителя Elastic Inference за последнюю минуту",
        "The number of inference requests reaching the Elastic Inference accelerator in the last minute": "Количество запросов на вывод, достигших ускорителя Elastic Inference за последнюю минуту",
        "The percentage of the Elastic Inference accelerator used for computation in the last minute": "Процент ускорителя Elastic Inference, использованный для вычислений за последнюю минуту",
        "Reports whether connectivity to the Elastic Inference accelerator is active or has failed in the last minute": "Сообщает, активно ли подключение к ускорителю Elastic Inference или произошёл сбой за последнюю минуту",
    }
)

# ---- Elastic Transcoder ----
RU.update(
    {
        "The number of billable seconds of audio output for a pipeline": "Количество тарифицируемых секунд аудио на выходе конвейера",
        "The number of billable seconds of HD output for a pipeline": "Количество тарифицируемых секунд видео HD на выходе конвейера",
        "The number of billable seconds of SD output for a pipeline": "Количество тарифицируемых секунд видео SD на выходе конвейера",
        "The number of billable seconds of SD output for a pipeline.": "Количество тарифицируемых секунд видео SD на выходе конвейера.",
        "The number of errors caused by invalid operation parameters, such as a request for a job status that does not include the job ID": "Количество ошибок, вызванных недопустимыми параметрами операции, например запросом статуса задания без идентификатора задания",
        "The number of jobs completed by this pipeline": "Количество заданий, выполненных этим конвейером",
        "The number of jobs that failed because of invalid inputs, such as a request to transcode a file that is not in the given input bucket": "Количество заданий, завершившихся сбоем из-за недопустимых входных данных, например запроса на перекодирование файла, отсутствующего в заданной входной корзине",
        "The number of outputs Elastic Transcoder created for a job": "Количество выходных файлов, созданных Elastic Transcoder для задания",
        "The number of seconds before Elastic Transcoder started transcoding a job": "Количество секунд до того, как Elastic Transcoder начал перекодирование задания",
        "The number of times that Elastic Transcoder automatically throttled an operation": "Количество случаев, когда Elastic Transcoder автоматически подвергал операцию регулированию",
        "Amazon Elastic Transcoder doesn't support tagging.": "Amazon Elastic Transcoder не поддерживает тегирование.",
    }
)

# ---- WorkSpaces ----
RU.update(
    {
        "The number of WorkSpaces that returned a healthy status": "Количество WorkSpaces, вернувших исправный статус",
        "The number of connection attempts": "Количество попыток подключения",
        "The number of failed connections": "Количество неудачных подключений",
        "The number of successful connections": "Количество успешных подключений",
        "The round-trip time (RTT) between the WorkSpaces client and the WorkSpace": "Время кругового пути (RTT) между клиентом WorkSpaces и WorkSpace",
        "The number of WorkSpaces that are under maintenance": "Количество WorkSpaces, находящихся на обслуживании",
        "The number of connections that were closed, including user-initiated and failed connections": "Количество закрытых подключений, включая подключения, закрытые пользователем, и неудачные подключения",
        "The amount of time it takes to initiate a WorkSpaces session": "Время, необходимое для инициации сессии WorkSpaces",
        "The number of WorkSpaces that are stopped": "Количество остановленных WorkSpaces",
        "The number of WorkSpaces that returned an unhealthy status": "Количество WorkSpaces, вернувших неисправный статус",
        "The number of WorkSpaces that have a user connected": "Количество WorkSpaces с подключённым пользователем",
    }
)

# ---- IoT Things Graph ----
RU.update(
    {
        "The amount of time a flow execution step takes to complete": "Время, необходимое для завершения шага выполнения потока",
        "The number of flow executions that are aborted": "Количество прерванных выполнений потока",
        "The number of flow execution steps that failed": "Количество шагов выполнения потока, завершившихся сбоем",
        "The number of flow executions that started": "Количество запущенных выполнений потока",
        "The number of flow execution steps that succeeded": "Количество успешно выполненных шагов выполнения потока",
        "The number of flow execution steps that started": "Количество запущенных шагов выполнения потока",
        "The number of flow execution Lambda function steps that failed": "Количество шагов функции Lambda при выполнении потока, завершившихся сбоем",
        "The number of flow execution Lambda function steps that started": "Количество запущенных шагов функции Lambda при выполнении потока",
        "The number of flow execution Lambda function steps that succeeded": "Количество успешно выполненных шагов функции Lambda при выполнении потока",
    }
)

# ---- SES ----
RU.update(
    {
        "The number of times the recipient's mail server permanently rejects the mail (hard bounces)": "Количество случаев, когда почтовый сервер получателя безвозвратно отклоняет письмо (жёсткие отказы)",
        "The number of times the recipient receives the email and clicks on a link": "Количество случаев, когда получатель получает письмо и переходит по ссылке",
        "The number times emails are marked as spam by the recipient": "Количество случаев, когда письма помечаются получателем как спам",
        "The number of emails that were successfully delivered to the recipient's mail server": "Количество писем, успешно доставленных на почтовый сервер получателя",
        "The number of times the recipient receives the email and opens it in the email client": "Количество случаев, когда получатель получает письмо и открывает его в почтовом клиенте",
        "The number of times Amazon SES encounters an error when it tries to execute the configured actions, and no longer retries delivering the email": "Количество случаев, когда Amazon SES сталкивается с ошибкой при попытке выполнить настроенные действия и прекращает повторные попытки доставки письма",
        "The number of times Amazon SES encounters an error when it tries to execute the configured actions": "Количество случаев, когда Amazon SES сталкивается с ошибкой при попытке выполнить настроенные действия",
        "The number of times Amazon SES accepts the sender's request and then determines the message contains a virus and stops processing": "Количество случаев, когда Amazon SES принимает запрос отправителя, затем определяет, что сообщение содержит вирус, и прекращает обработку",
        "The number of times email can't be sent because of a template rendering issue": "Количество случаев, когда письмо не может быть отправлено из-за проблемы с отрисовкой шаблона",
        "The percentage of sent emails that result in hard bounces": "Процент отправленных писем, приводящих к жёстким отказам",
        "The percentage of sent emails that were marked as spam": "Процент отправленных писем, помеченных как спам",
        "The number of successful requests (email sending API calls) to Amazon SES": "Количество успешных запросов (вызовов API отправки писем) к Amazon SES",
    }
)

# ---- ACM PCA ----
RU.update(
    {
        "To [update the AWS IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), use the JSON below, which contains the monitoring policy (permissions) for all supporting services.": "Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON, который содержит политику мониторинга (разрешения) для всех поддерживаемых сервисов.",
        'If you don\'t want to add permissions to all services, and select permissions for only certain services, consult the table below. The table contains the set of permissions that are required for [All AWS cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") and, for each supporting service, a list of optional permissions specific to that service.': 'Если вы не хотите добавлять разрешения для всех сервисов и предпочитаете выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. В таблице приведён набор разрешений, необходимых для [всех облачных сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS в Dynatrace и просмотр доступных метрик."), и для каждого поддерживаемого сервиса приведён список необязательных разрешений, специфичных для этого сервиса.',
        "The following is an example JSON policy for a single service.": "Ниже приведён пример JSON-политики для одного сервиса.",
        "A certificate revocation list (CRL) was generated. This metric applies only to a private CA.": "Список отзыва сертификатов (CRL) был сгенерирован. Эта метрика применяется только к частному CA.",
        "An operation failed. This metric applies only to the `IssueCertificate` operation.": "Операция завершилась сбоем. Эта метрика применяется только к операции `IssueCertificate`.",
        "The S3 bucket specified for the CRL is not correctly configured. Check the bucket policy. This metric applies only to a private CA.": "Корзина S3, указанная для CRL, настроена неправильно. Проверьте политику корзины. Эта метрика применяется только к частному CA.",
        "A certificate was successfully issued. This metric applies only to the `IssueCertificate` operation.": "Сертификат был успешно выпущен. Эта метрика применяется только к операции `IssueCertificate`.",
        "The elapsed time in milliseconds for a certificate to be issued. This metric applies only to the `IssueCertificate` operation.": "Затраченное время в миллисекундах на выпуск сертификата. Эта метрика применяется только к операции `IssueCertificate`.",
    }
)

# ---- API Gateway ----
RU.update(
    {
        "To get metrics in a given dimension set [`ApiName`, `Method`, `Resource`, `Stage`], you need to enable **detailed CloudWatch metrics**. You can do this in the console by selecting **Enable detailed CloudWatch metrics** under a stage **Logs** or **Tracing** tab.": "Чтобы получать метрики в заданном наборе измерений [`ApiName`, `Method`, `Resource`, `Stage`], необходимо включить **детальные метрики CloudWatch**. Это можно сделать в консоли, выбрав **Enable detailed CloudWatch metrics** на вкладке **Logs** или **Tracing** этапа.",
        "Alternatively, you can call the `update-stage` AWS CLI command to update the `metricsEnabled` property to `true`.": "Кроме того, можно вызвать команду AWS CLI `update-stage`, чтобы изменить значение свойства `metricsEnabled` на `true`.",
        "[Amazon API Gateway Version 2 API (WebSocket and HTTP APIs)](https://dt-url.net/dt03xj6) isn't currently supported for Amazon API Gateway. Only [Amazon API Gateway Version 1 API (REST APIs)](https://dt-url.net/l523xes) is supported.": "[Amazon API Gateway Version 2 API (WebSocket and HTTP APIs)](https://dt-url.net/dt03xj6) в настоящее время не поддерживается для Amazon API Gateway. Поддерживается только [Amazon API Gateway Version 1 API (REST APIs)](https://dt-url.net/l523xes).",
        "The number of client-side errors captured in a given period": "Количество ошибок на стороне клиента, зафиксированных за указанный период",
        "The number of server-side errors captured in a given period": "Количество ошибок на стороне сервера, зафиксированных за указанный период",
        "The number of requests served from the API cache in a given period": "Количество запросов, обслуженных из кэша API за указанный период",
        "The number of requests served from the backend in a given period, when API caching is enabled": "Количество запросов, обслуженных из бэкенда за указанный период, когда включено кэширование API",
        "The total number API requests in a given period": "Общее количество запросов API за указанный период",
        "The time between when API Gateway relays a request to the backend and when it receives a response from the backend": "Время между передачей запроса API Gateway в бэкенд и получением ответа от бэкенда",
        "The time between when API Gateway receives a request from a client and when it returns a response to the client. The latency includes the integration latency and other API Gateway overhead.": "Время между получением запроса от клиента API Gateway и возвратом ответа клиенту. Эта задержка включает задержку интеграции и прочие накладные расходы API Gateway.",
    }
)

# ---- DataSync ----
RU.update(
    {
        "The total number of bytes of data that are prepared at the destination location": "Общее количество байт данных, подготовленных в целевом расположении",
        "The total number of bytes of data that are prepared at the source location": "Общее количество байт данных, подготовленных в исходном расположении",
        "The total number of bytes that are transferred over the network when the agent reads from the source location to the destination location": "Общее количество байт, переданных по сети, когда агент читает из исходного расположения в целевое расположение",
        "The total number of bytes of data that are verified at the destination location": "Общее количество байт данных, проверенных в целевом расположении",
        "The total number of bytes of data that are verified at the source location": "Общее количество байт данных, проверенных в исходном расположении",
        "The total logical size of all files that have been transferred to the destination location": "Общий логический размер всех файлов, переданных в целевое расположение",
        "The total number of files that are prepared at the destination location": "Общее количество файлов, подготовленных в целевом расположении",
        "The total number of files that are prepared at the source location": "Общее количество файлов, подготовленных в исходном расположении",
        "The actual number of files or metadata that were transferred over the network": "Фактическое количество файлов или метаданных, переданных по сети",
        "The total number of files that are verified at the destination location": "Общее количество файлов, проверенных в целевом расположении",
        "The total number of files that are verified at the source location": "Общее количество файлов, проверенных в исходном расположении",
    }
)

# ---- MediaConvert ----
RU.update(
    {
        "The number of seconds of audio-only output for a queue": "Количество секунд вывода только аудио для очереди",
        "The number of seconds of high-definition (HD) output for a queue": "Количество секунд вывода высокой чёткости (HD) для очереди",
        "The number of jobs canceled in this queue": "Количество заданий, отменённых в этой очереди",
        "The number of jobs completed in this queue": "Количество заданий, выполненных в этой очереди",
        "The number of jobs that failed because of invalid inputs, such as a request to transcode a file that is not in the specified input bucket": "Количество заданий, завершившихся сбоем из-за недопустимых входных данных, например запроса на перекодирование файла, отсутствующего в указанной входной корзине",
        "The number of seconds of 8K output for a queue": "Количество секунд вывода 8K для очереди",
        "The number of seconds of standard definition (SD) output for a queue": "Количество секунд вывода стандартной чёткости (SD) для очереди",
        "The number of seconds before AWS Elemental MediaConvert starts transcoding a job": "Количество секунд до того, как AWS Elemental MediaConvert начинает перекодирование задания",
        "The number of seconds for AWS Elemental MediaConvert to complete transcoding": "Количество секунд, необходимых AWS Elemental MediaConvert для завершения перекодирования",
        "The number of seconds of ultra-high-definition (UHD) output for a queue": "Количество секунд вывода сверхвысокой чёткости (UHD) для очереди",
        "Dynatrace is currently not gathering any instance attributes for AWS Elemental MediaConvert.": "В настоящее время Dynatrace не собирает атрибуты экземпляров для AWS Elemental MediaConvert.",
    }
)

# ---- MediaTailor ----
RU.update(
    {
        "The count of ads included in ad decision server (ADS) responses for the time period that you specified": "Количество рекламных объявлений, включённых в ответы сервера решений по рекламе (ADS) за указанный вами период времени",
        "The total duration, in milliseconds, of all ads that MediaTailor received from the ADS for the time period that you specified": "Общая продолжительность в миллисекундах всех рекламных объявлений, полученных MediaTailor от ADS за указанный вами период времени",
        "The number of non-HTTP 200 status code responses, empty responses, and timed-out responses that MediaTailor received from the ADS in the time period that you specified": "Количество ответов с кодом состояния, отличным от HTTP 200, пустых ответов и ответов с истёкшим временем ожидания, полученных MediaTailor от ADS за указанный вами период времени",
        "The simple average of the rates at which the responses from the ADS filled the corresponding individual ad avails for the time period that you specified": "Простое среднее значение долей, на которые ответы от ADS заполняли соответствующие отдельные рекламные блоки за указанный вами период времени",
        "The number of timed-out requests to the ADS in the time period that you specified": "Количество запросов к ADS с истёкшим временем ожидания за указанный вами период времени",
        "The number of times that the ADS pointed at an ad that wasn't yet transcoded by the internal transcoder service in the time period that you specified": "Количество случаев, когда ADS указывал на рекламное объявление, ещё не перекодированное внутренним сервисом перекодирования, за указанный вами период времени",
        "The total duration, in milliseconds, of all ad avails that MediaTailor encountered in the time period that you specified": "Общая продолжительность в миллисекундах всех рекламных блоков, обнаруженных MediaTailor за указанный вами период времени",
        "The simple average of the rates at which MediaTailor filled the individual ad avails for the time period that you specified": "Простое среднее значение долей, на которые MediaTailor заполнял отдельные рекламные блоки за указанный вами период времени",
        "The total duration, in milliseconds, of ad avail time that MediaTailor filled with ads in the time period that you specified": "Общая продолжительность в миллисекундах времени рекламных блоков, которое MediaTailor заполнил рекламой за указанный вами период времени",
        "The number of errors received while MediaTailor was generating manifests in the time period that you specified": "Количество ошибок, полученных во время генерации манифестов MediaTailor за указанный вами период времени",
        "The number of non-HTTP 200 status code responses and timed-out responses that MediaTailor received from the origin server in the time period that you specified": "Количество ответов с кодом состояния, отличным от HTTP 200, и ответов с истёкшим временем ожидания, полученных MediaTailor от сервера-источника за указанный вами период времени",
        "The number of timed-out requests to the origin server in the time period that you specified": "Количество запросов к серверу-источнику с истёкшим временем ожидания за указанный вами период времени",
        "`AdDecisionServer.FillRate` and `Avail.FillRate` should be expressed in percentage, however, AWS reports it as a value from `0` to `1`. They are defined for the time being as **Count values**.": "`AdDecisionServer.FillRate` и `Avail.FillRate` должны выражаться в процентах, однако AWS сообщает их как значение от `0` до `1`. Пока они определены как **значения Count**.",
    }
)

# ---- VPC NAT Gateways ----
RU.update(
    {
        "The total number of concurrent active TCP connections through the NAT gateway": "Общее количество одновременных активных TCP-соединений через шлюз NAT",
        "The number of bytes received by the NAT gateway from the destination": "Количество байт, полученных шлюзом NAT из пункта назначения",
        "The number of bytes received by the NAT gateway from clients in your VPC": "Количество байт, полученных шлюзом NAT от клиентов в вашей VPC",
        "The number of bytes sent out through the NAT gateway to the destination": "Количество байт, отправленных через шлюз NAT в пункт назначения",
        "The number of bytes sent through the NAT gateway to the clients in your VPC": "Количество байт, отправленных через шлюз NAT клиентам в вашей VPC",
        "The number of connection attempts made through the NAT gateway": "Количество попыток подключения, совершённых через шлюз NAT",
        "The number of connections established through the NAT gateway": "Количество подключений, установленных через шлюз NAT",
        "The number of times the NAT gateway could not allocate a source port": "Количество случаев, когда шлюзу NAT не удалось выделить исходный порт",
        "The number of connections that transitioned from the active state to the idle state": "Количество подключений, перешедших из активного состояния в состояние простоя",
        "The number of packets dropped by the NAT gateway": "Количество пакетов, отброшенных шлюзом NAT",
        "The number of packets received by the NAT gateway from the destination": "Количество пакетов, полученных шлюзом NAT из пункта назначения",
        "The number of packets received by the NAT gateway from clients in your VPC": "Количество пакетов, полученных шлюзом NAT от клиентов в вашей VPC",
        "The number of packets sent out through the NAT gateway to the destination": "Количество пакетов, отправленных через шлюз NAT в пункт назначения",
        "The number of packets sent through the NAT gateway to the clients in your VPC": "Количество пакетов, отправленных через шлюз NAT клиентам в вашей VPC",
    }
)

# ---- MediaPackage ----
RU.update(
    {
        "Indicates if an input has been used as the source for an endpoint in AWS Elemental MediaPackage (it has been active). A value of `1` indicates that the input was active, and a `0` (zero) indicates that it wasn't.": "Указывает, использовался ли вход в качестве источника для конечной точки в AWS Elemental MediaPackage (был ли он активен). Значение `1` означает, что вход был активен, а `0` (ноль) означает, что нет.",
        "Number of bytes that AWS Elemental MediaPackage successfully sends for each request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.": "Количество байт, которые AWS Elemental MediaPackage успешно отправляет на каждый запрос. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются.",
        "Number of content requests that AWS Elemental MediaPackage receives. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.": "Количество запросов контента, которые получает AWS Elemental MediaPackage. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются.",
        "The time that it takes AWS Elemental MediaPackage to process each output request. If MediaPackage doesn't receive any requests for output in the specified interval, then no data is given.": "Время, которое требуется AWS Elemental MediaPackage для обработки каждого запроса на вывод. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются.",
        "Number of bytes of content that AWS Elemental MediaPackage receives for each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given.": "Количество байт контента, которые AWS Elemental MediaPackage получает на каждый входной запрос. Если MediaPackage не получает входных запросов в течение указанного интервала, данные не предоставляются.",
        "The time that it takes AWS Elemental MediaPackage to process each input request. If MediaPackage doesn't receive any requests for input in the specified interval, then no data is given.": "Время, которое требуется AWS Elemental MediaPackage для обработки каждого входного запроса. Если MediaPackage не получает входных запросов в течение указанного интервала, данные не предоставляются.",
    }
)

# ---- QLDB ----
RU.update(
    {
        "Amazon QLDB service shows on the custom device group page. The service is made up of instances (custom devices) called **ledgers**. You can view metrics for each custom device in the **Further details** section of the custom device overview page, split by **Streams** and **Command types**.": "Сервис Amazon QLDB отображается на странице группы пользовательских устройств. Сервис состоит из экземпляров (пользовательских устройств), называемых **реестрами** (ledgers). Метрики каждого пользовательского устройства можно просматривать в разделе **Further details** на странице обзора пользовательского устройства, с разбивкой по **Streams** и **Command types**.",
        "* **LedgerName** limits the data to a specific ledger. This value can be any ledger name in the current AWS Region and the current AWS account.": "* **LedgerName** ограничивает данные конкретным реестром. Этим значением может быть любое имя реестра в текущем регионе AWS и текущем аккаунте AWS.",
        "* **StreamId** limits the data to a specific journal stream. This value can be any stream ID for a ledger in the current AWS Region and the current AWS account.": "* **StreamId** ограничивает данные конкретным потоком журнала. Этим значением может быть любой идентификатор потока для реестра в текущем регионе AWS и текущем аккаунте AWS.",
        "* **CommandType** limits the data to one of the following QLDB data API commands: `AbortTransaction`, `CommitTransaction`, `EndSession`, `ExecuteStatement`, `FetchPage`, `StartSession`, `StartTransaction`.": "* **CommandType** ограничивает данные одной из следующих команд API данных QLDB: `AbortTransaction`, `CommitTransaction`, `EndSession`, `ExecuteStatement`, `FetchPage`, `StartSession`, `StartTransaction`.",
        "The amount of time taken for data operations, reported in one-minute intervals": "Время, затраченное на операции с данными (регистрируется с интервалом в одну минуту)",
        "The total amount of disk space used by the ledger's tables, indexes, and indexed history, reported in 15-minute intervals": "Общий объём дискового пространства, используемого таблицами, индексами и индексированной историей реестра (регистрируется с интервалом в 15 минут)",
        "The flag that indicates if a journal stream to Kinesis Data Streams is impaired, reported in one-minute intervals": "Флаг, указывающий, нарушена ли работа потока журнала в Kinesis Data Streams (регистрируется с интервалом в одну минуту)",
        "The total amount of disk space used by the ledger's journal, reported in 15-minute intervals": "Общий объём дискового пространства, используемого журналом реестра (регистрируется с интервалом в 15 минут)",
        "The number of requests to QLDB that generate an `OccConflictException`": "Количество запросов к QLDB, генерирующих исключение `OccConflictException`",
        "The number of disk read I/O operations, reported in one-minute intervals": "Количество операций ввода-вывода чтения с диска (регистрируется с интервалом в одну минуту)",
        "The number of requests to QLDB that generate a `SessionRateExceededException`": "Количество запросов к QLDB, генерирующих исключение `SessionRateExceededException`",
        "The number of requests to QLDB that generate an HTTP 4xx error": "Количество запросов к QLDB, генерирующих ошибку HTTP 4xx",
        "The number of requests to QLDB that generate an HTTP 5xx error": "Количество запросов к QLDB, генерирующих ошибку HTTP 5xx",
        "The number of disk write I/O operations, reported in one-minute intervals": "Количество операций ввода-вывода записи на диск (регистрируется с интервалом в одну минуту)",
    }
)

# ---- OpsWorks ----
RU.update(
    {
        "The percentage of time that the CPU is idle": "Процент времени, в течение которого CPU простаивает",
        "The percentage of time that the CPU is handling processes with a positive `nice` value, which have a lower scheduling priority": "Процент времени, в течение которого CPU обрабатывает процессы с положительным значением `nice`, имеющие более низкий приоритет планирования",
        "The percentage of time that an instance is waiting for the hypervisor to allocate physical CPU resources": "Процент времени, в течение которого экземпляр ожидает выделения гипервизором физических ресурсов CPU",
        "The percentage of time that the CPU is handling system operations": "Процент времени, в течение которого CPU обрабатывает системные операции",
        "The percentage of time that the CPU is handling user operations": "Процент времени, в течение которого CPU обрабатывает пользовательские операции",
        "The percentage of time that the CPU is waiting for input/output operations": "Процент времени, в течение которого CPU ожидает операций ввода-вывода",
        "The load averaged over a one-minute window": "Средняя нагрузка за одноминутное окно",
        "The load averaged over a five-minute window": "Средняя нагрузка за пятиминутное окно",
        "The load averaged over a 15-minute window": "Средняя нагрузка за 15-минутное окно",
        "The amount of buffered memory": "Объём буферизованной памяти",
        "The amount of cached memory": "Объём кэшированной памяти",
        "The amount of free memory": "Объём свободной памяти",
        "The amount of swap space": "Объём пространства подкачки",
        "The total amount of memory": "Общий объём памяти",
        "The amount of memory in use": "Объём используемой памяти",
        "The number of active processes": "Количество активных процессов",
    }
)

# ---- frontmatter titles (X monitoring -> Мониторинг X) ----
ADD_TITLES = {
    "Amazon EventBridge monitoring": "Мониторинг Amazon EventBridge",
    "Amazon SQS (Simple Queue Service) monitoring": "Мониторинг Amazon SQS (Simple Queue Service)",
    "Amazon Elastic Inference monitoring": "Мониторинг Amazon Elastic Inference",
    "Amazon Elastic Transcoder monitoring": "Мониторинг Amazon Elastic Transcoder",
    "Amazon WorkSpaces monitoring": "Мониторинг Amazon WorkSpaces",
    "AWS IoT Things Graph monitoring": "Мониторинг AWS IoT Things Graph",
    "Amazon SES (Simple Email Service) monitoring": "Мониторинг Amazon SES (Simple Email Service)",
    "AWS Certificate Manager Private Certificate Authority (ACM PCA) monitoring": "Мониторинг AWS Certificate Manager Private Certificate Authority (ACM PCA)",
    "Amazon API Gateway monitoring": "Мониторинг Amazon API Gateway",
    "AWS DataSync monitoring": "Мониторинг AWS DataSync",
    "AWS Elemental MediaConvert monitoring": "Мониторинг AWS Elemental MediaConvert",
    "AWS Elemental MediaTailor monitoring": "Мониторинг AWS Elemental MediaTailor",
    "Amazon VPC NAT Gateways monitoring": "Мониторинг Amazon VPC NAT Gateways",
    "AWS Elemental MediaPackage (Live, Video on Demand) monitoring": "Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)",
    "Amazon QLDB (Quantum Ledger Database) monitoring": "Мониторинг Amazon QLDB (Quantum Ledger Database)",
    "AWS OpsWorks monitoring": "Мониторинг AWS OpsWorks",
}


def main():
    # guard: no em-dash, no mojibake in any RU value
    bad = []
    for k, v in list(RU.items()) + list(ADD_TITLES.items()):
        if "—" in v:
            bad.append("EM-DASH: " + v[:60])
        if "â" in v or "﻿" in v:
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
