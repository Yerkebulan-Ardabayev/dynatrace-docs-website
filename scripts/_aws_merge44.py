#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge L4-IF.44 batch-1 (17 standard AWS files) translations into the
shared cumulative dicts (_aws_trans_l4if43.json + _aws_titles_l4if43.json).
Re-runnable: loads existing, updates, writes back (1-space indent, UTF-8).
"""

import os, json, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TRANS_P = os.path.join(HERE, "_aws_trans_l4if43.json")
TITLE_P = os.path.join(HERE, "_aws_titles_l4if43.json")

# intro templates (verbatim canon from shipped dict, service name swapped)
V1 = (
    "Dynatrace принимает метрики для множества предопределённых пространств имён, включая {S}. "
    "Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений "
    "и создавать собственные графики, которые можно закреплять на дашбордах."
)
V2 = (
    "Dynatrace принимает метрики для множества предопределённых пространств имён, включая {S}. "
    "Можно просматривать графики по каждому экземпляру сервиса с набором измерений "
    "и создавать собственные графики, которые можно закреплять на дашбордах."
)


def intro_en_v1(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view metrics for each service instance, split metrics into multiple dimensions, "
        "and create custom charts that you can pin to your dashboards." % s
    )


def intro_en_v2(s):
    return (
        "Dynatrace ingests metrics for multiple preselected namespaces, including %s. "
        "You can view graphs per service instance, with a set of dimensions, "
        "and create custom graphs that you can pin to your dashboards." % s
    )


ADD_TITLES = {
    "AWS WAF Classic monitoring": "Мониторинг AWS WAF Classic",
    "AWS Site-to-Site VPN monitoring": "Мониторинг AWS Site-to-Site VPN",
    "Amazon Lex monitoring": "Мониторинг Amazon Lex",
    "Amazon Polly monitoring": "Мониторинг Amazon Polly",
    "Amazon Textract monitoring": "Мониторинг Amazon Textract",
    "AWS Chatbot monitoring": "Мониторинг AWS Chatbot",
    "Amazon Route 53 Resolver monitoring": "Мониторинг Amazon Route 53 Resolver",
    "Amazon CloudWatch Logs monitoring": "Мониторинг Amazon CloudWatch Logs",
    "Amazon FSx monitoring": "Мониторинг Amazon FSx",
    "Amazon Translate monitoring": "Мониторинг Amazon Translate",
    "Amazon Rekognition monitoring": "Мониторинг Amazon Rekognition",
    "Amazon Inspector monitoring": "Мониторинг Amazon Inspector",
    "Amazon AppStream 2.0 monitoring": "Мониторинг Amazon AppStream 2.0",
    "Amazon Athena monitoring": "Мониторинг Amazon Athena",
    "Amazon Redshift monitoring": "Мониторинг Amazon Redshift",
    "Amazon Route 53 monitoring": "Мониторинг Amazon Route 53",
    "Amazon EFS (Elastic File System) monitoring": "Мониторинг Amazon EFS (Elastic File System)",
}

# H1 headings (frontmatter title prefixed with "# ")
ADD_TRANS = {t_en if False else ("# " + k): ("# " + v) for k, v in ADD_TITLES.items()}

# intros
ADD_TRANS[intro_en_v1("AWS WAF Classic")] = V1.format(S="AWS WAF Classic")
ADD_TRANS[intro_en_v2("AWS Site-to-Site VPN")] = V2.format(S="AWS Site-to-Site VPN")
ADD_TRANS[intro_en_v1("Amazon Lex")] = V1.format(S="Amazon Lex")
ADD_TRANS[intro_en_v2("Amazon Polly")] = V2.format(S="Amazon Polly")
ADD_TRANS[intro_en_v2("Amazon Textract")] = V2.format(S="Amazon Textract")
ADD_TRANS[intro_en_v1("AWS Chatbot")] = V1.format(S="AWS Chatbot")
ADD_TRANS[intro_en_v1("Amazon Route 53 Resolver")] = V1.format(
    S="Amazon Route 53 Resolver"
)
ADD_TRANS[intro_en_v1("Amazon CloudWatch Logs")] = V1.format(S="Amazon CloudWatch Logs")
ADD_TRANS[intro_en_v1("Amazon FSx")] = V1.format(S="Amazon FSx")
ADD_TRANS[intro_en_v1("Amazon Translate")] = V1.format(S="Amazon Translate")
ADD_TRANS[intro_en_v1("Amazon Rekognition")] = V1.format(S="Amazon Rekognition")
ADD_TRANS[intro_en_v1("Amazon Inspector")] = V1.format(S="Amazon Inspector")
ADD_TRANS[intro_en_v1("Amazon AppStream 2.0")] = V1.format(S="Amazon AppStream 2.0")
ADD_TRANS[intro_en_v1("Amazon Athena")] = V1.format(S="Amazon Athena")
ADD_TRANS[intro_en_v1("Amazon Redshift")] = V1.format(S="Amazon Redshift")
ADD_TRANS[intro_en_v1("Amazon Route 53")] = V1.format(S="Amazon Route 53")
ADD_TRANS[intro_en_v1("Amazon Elastic File System (EFS)")] = V1.format(
    S="Amazon Elastic File System (EFS)"
)

# dates (new ones not yet in dict)
ADD_TRANS["* Published Oct 12, 2020"] = "* Опубликовано 12 октября 2020 г."
ADD_TRANS["* Published Oct 16, 2020"] = "* Опубликовано 16 октября 2020 г."

# main-dimension notes
ADD_TRANS["`FileSystemId` is the main dimension."] = (
    "Основное измерение: `FileSystemId`."
)
ADD_TRANS["`VpnId` is the main dimension."] = "Основное измерение: `VpnId`."
ADD_TRANS["`BotName` is the main dimension."] = "Основное измерение: `BotName`."
ADD_TRANS["`ConfigurationName` is the main dimension."] = (
    "Основное измерение: `ConfigurationName`."
)
ADD_TRANS["`EndpointId` is the main dimension."] = "Основное измерение: `EndpointId`."
ADD_TRANS["`LogGroupName` is the main dimension."] = (
    "Основное измерение: `LogGroupName`."
)
ADD_TRANS["`AssessmentTemplateArn` is the main dimension."] = (
    "Основное измерение: `AssessmentTemplateArn`."
)
ADD_TRANS["`Fleet` is the main dimension."] = "Основное измерение: `Fleet`."
ADD_TRANS["`WorkGroup` is the main dimension."] = "Основное измерение: `WorkGroup`."
ADD_TRANS["`ClusterIdentifier` is the main dimension."] = (
    "Основное измерение: `ClusterIdentifier`."
)
ADD_TRANS["`HostedZoneId` is the main dimension."] = (
    "Основное измерение: `HostedZoneId`."
)

# per-file notes / prose
ADD_TRANS["This service monitors AWS Lex V1 (AWS Lex V2 is **not** supported)."] = (
    "Этот сервис отслеживает AWS Lex V1 (AWS Lex V2 **не** поддерживается)."
)
ADD_TRANS[
    "For Amazon Polly, there are no instances (custom devices) on the custom device group overview page, the service itself being just an API that you can call. The service metrics are under the **Further details** section of the custom device group overview page, split **By Operation and Region**."
] = "Для Amazon Polly на странице обзора группы пользовательских устройств нет экземпляров (пользовательских устройств), так как сам сервис, это просто API, который можно вызывать. Метрики сервиса находятся в разделе **Further details** на странице обзора группы пользовательских устройств, с разбивкой **By Operation and Region**."
ADD_TRANS[
    "Because Amazon Textract provides OCR APIs, there is no **Main Dimension**."
] = "Поскольку Amazon Textract предоставляет API для OCR, **основное измерение** отсутствует."
ADD_TRANS[
    "The metrics for throttled events are region-wide and have no dimension for any specific configuration."
] = "Метрики для событий, подвергнутых регулированию, действуют в масштабе региона и не имеют измерения для какой-либо конкретной конфигурации."
ADD_TRANS[
    "Route 53 is a global service; hosted zone metrics (for example, `DNSQueries`) are available only in the `us-east-1` region. To get hosted zone metrics, credentials must have at least following permissions set for the `us-east-1` region:"
] = "Route 53, это глобальный сервис: метрики размещённой зоны (например, `DNSQueries`) доступны только в регионе `us-east-1`. Чтобы получать метрики размещённой зоны, учётные данные должны иметь как минимум следующий набор разрешений для региона `us-east-1`:"
ADD_TRANS[
    "Route 53 is a global service; hosted zone metrics (for example, `DNSQueries`) are available only in the `us-east-1` region. To get hosted zone metrics, credentials must have at least the following permissions set for the `us-east-1` region:"
] = "Route 53, это глобальный сервис: метрики размещённой зоны (например, `DNSQueries`) доступны только в регионе `us-east-1`. Чтобы получать метрики размещённой зоны, учётные данные должны иметь как минимум следующий набор разрешений для региона `us-east-1`:"
ADD_TRANS[
    "For Amazon Translate, there are no instances (custom devices) on the custom device group overview page. The service metrics are under the **Further details** section of the custom device group overview page."
] = "Для Amazon Translate на странице обзора группы пользовательских устройств нет экземпляров (пользовательских устройств). Метрики сервиса находятся в разделе **Further details** на странице обзора группы пользовательских устройств."
ADD_TRANS[
    "To [update the AWS IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), use the JSON below."
] = "Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON."
ADD_TRANS["Predefined policy in JSON"] = "Предопределённая политика в формате JSON"
ADD_TRANS[
    "* An [S3 bucket for the results](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)"
] = "* [Корзина S3 для результатов](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)"
ADD_TRANS[
    "The default or primary workgroup for Amazon Athena doesn't support gathering metrics. You need to select or create a workgroup."
] = "Рабочая группа по умолчанию или основная рабочая группа Amazon Athena не поддерживает сбор метрик. Необходимо выбрать или создать рабочую группу."

# ---- metric descriptions (CELL) ----
CELL = {
    # waf-classic
    "The number of throttled requests": "Количество запросов, подвергнутых регулированию",
    "The number of passed requests for a rule group": "Количество пропущенных запросов для группы правил",
    # site-to-site-vpn
    "The bytes received through the VPN tunnel": "Байты, полученные через VPN-туннель",
    "The bytes sent through the VPN tunnel": "Байты, отправленные через VPN-туннель",
    "The state of the tunnel. For static VPNs, 0 indicates DOWN and 1 indicates UP. For BGP VPNs, 1 indicates ESTABLISHED and 0 is used for all other states": "Состояние туннеля. Для статических VPN 0 означает DOWN, а 1 означает UP. Для BGP VPN 1 означает ESTABLISHED, а 0 используется для всех остальных состояний",
    # lex
    "The number of utterances that were not recognized in the specified period": "Количество высказываний, которые не были распознаны за указанный период",
    "The number of runtime requests in the specified period": "Количество запросов среды выполнения за указанный период",
    "The latency for successful requests between the time that the request was made and the response was passed back": "Задержка для успешных запросов между моментом отправки запроса и моментом возврата ответа",
    # polly
    "HTTP 400 level error code returned upon an error": "Код ошибки уровня HTTP 400, возвращаемый при ошибке",
    "HTTP 200 level code returned upon a successful response": "Код уровня HTTP 200, возвращаемый при успешном ответе",
    "HTTP 500 level error code returned upon an error": "Код ошибки уровня HTTP 500, возвращаемый при ошибке",
    "The number of characters in the request": "Количество символов в запросе",
    "The latency between the time when the request was made and the start of the streaming response": "Задержка между моментом отправки запроса и началом потокового ответа",
    # textract
    "The time in milliseconds for Amazon Textract to compute the response": "Время в миллисекундах, за которое Amazon Textract вычисляет ответ",
    "The number of server errors": "Количество серверных ошибок",
    "The number of successful requests": "Количество успешных запросов",
    "The number of user errors (invalid parameters, invalid image, no permission, and so on)": "Количество пользовательских ошибок (неверные параметры, неверное изображение, отсутствие прав и т. д.)",
    # chatbot
    "The number of event notifications received by AWS Chatbot": "Количество уведомлений о событиях, полученных AWS Chatbot",
    "The number of throttled notifications": "Количество уведомлений, подвергнутых регулированию",
    "The number of messages that failed to deliver to the chat client": "Количество сообщений, которые не удалось доставить чат-клиенту",
    "The number of messages successfully delivered to the chat client": "Количество сообщений, успешно доставленных чат-клиенту",
    "The number of unsupported events or messages attempted": "Количество попыток обработки неподдерживаемых событий или сообщений",
    # route-53-resolver
    "The number of elastic network interfaces in the `OPERATIONAL` status.": "Количество эластичных сетевых интерфейсов в статусе `OPERATIONAL`.",
    "The number of elastic network interfaces in the `AUTO_RECOVERING` status.": "Количество эластичных сетевых интерфейсов в статусе `AUTO_RECOVERING`.",
    "The number of DNS queries forwarded from your network to your VPCs through the endpoint specified by `EndpointId` (for inbound endpoints)": "Количество DNS-запросов, перенаправленных из вашей сети в ваши VPC через конечную точку, заданную `EndpointId` (для входящих конечных точек)",
    "The total number of DNS queries forwarded from Amazon VPCs to your network (for outbound endpoints)": "Общее количество DNS-запросов, перенаправленных из Amazon VPC в вашу сеть (для исходящих конечных точек)",
    "The number of DNS queries forwarded from your VPCs to your network through the endpoint specified by `EndpointId` (for outbound endpoints)": "Количество DNS-запросов, перенаправленных из ваших VPC в вашу сеть через конечную точку, заданную `EndpointId` (для исходящих конечных точек)",
    # cloudwatch-logs
    "The number of log events for which CloudWatch Logs received an error when forwarding data to the subscription destination": "Количество событий журнала, для которых CloudWatch Logs получил ошибку при пересылке данных в место назначения подписки",
    "The number of log events for which CloudWatch Logs was throttled when forwarding data to the subscription destination": "Количество событий журнала, для которых CloudWatch Logs был подвергнут регулированию при пересылке данных в место назначения подписки",
    "The volume of log events in compressed bytes forwarded to the subscription destination": "Объём событий журнала в сжатых байтах, пересланных в место назначения подписки",
    "The number of log events forwarded to the subscription destination": "Количество событий журнала, пересланных в место назначения подписки",
    "The volume of log events in uncompressed bytes uploaded to CloudWatch Logs. When used with the `LogGroupName` dimension, this is the volume of log events in uncompressed bytes uploaded to the log group.": "Объём событий журнала в несжатых байтах, загруженных в CloudWatch Logs. При использовании с измерением `LogGroupName` это объём событий журнала в несжатых байтах, загруженных в группу журналов.",
    "The number of log events uploaded to CloudWatch Logs. When used with the `LogGroupName` dimension, this is the number of log events uploaded to the log group.": "Количество событий журнала, загруженных в CloudWatch Logs. При использовании с измерением `LogGroupName` это количество событий журнала, загруженных в группу журналов.",
    # fsx (DataReadBytes = identifier echo, mirror byte-identical)
    "DataReadBytes": "DataReadBytes",
    "The number of read operations": "Количество операций чтения",
    "The number of bytes for file system write operations": "Количество байт для операций записи в файловую систему",
    "The number of write operations": "Количество операций записи",
    "The amount of available storage capacity": "Объём доступной ёмкости хранилища",
    "The number of metadata operations": "Количество операций с метаданными",
    # translate
    "The number of billable characters in requests": "Количество тарифицируемых символов в запросах",
    "The time that it took to respond to a request": "Время, затраченное на ответ на запрос",
    "The number of server errors. The HTTP response code range for a server error is `500`-`599`": "Количество серверных ошибок. Диапазон кодов HTTP-ответа для серверной ошибки: `500`-`599`",
    "The number of successful translation requests. The response code for a successful request is `200`-`299`": "Количество успешных запросов на перевод. Код ответа для успешного запроса: `200`-`299`",
    "The number of requests subject to throttling": "Количество запросов, подвергнутых регулированию",
    "The number of user errors that occurred. The HTTP response code range for a user error is `400`-`499`": "Количество возникших пользовательских ошибок. Диапазон кодов HTTP-ответа для пользовательской ошибки: `400`-`499`",
    # rekognition
    "The number of faces detected with the `IndexFaces` or `DetectFaces` operation": "Количество лиц, обнаруженных с помощью операции `IndexFaces` или `DetectFaces`",
    "The number of labels detected with the `DetectLabels` operation": "Количество меток, обнаруженных с помощью операции `DetectLabels`",
    "The time in milliseconds for Rekognition to compute the response": "Время в миллисекундах, за которое Rekognition вычисляет ответ",
    "The number of server errors. The response code range for a server error is 500-599.": "Количество серверных ошибок. Диапазон кодов ответа для серверной ошибки: 500-599.",
    "The number of successful requests. The response code range for a successful request is 200-299.": "Количество успешных запросов. Диапазон кодов ответа для успешного запроса: 200-299.",
    "The number of user errors (such as invalid parameters, invalid image, or no permission). The response code range for a user error is 400-499.": "Количество пользовательских ошибок (например, неверные параметры, неверное изображение или отсутствие прав). Диапазон кодов ответа для пользовательской ошибки: 400-499.",
    # inspector
    "Number of assessment runs for this target": "Количество запусков оценки для этой цели",
    "Number of findings for this template": "Количество результатов для этого шаблона",
    "Number of agents that match this target that are healthy": "Количество исправных агентов, соответствующих этой цели",
    "Number of agents that match this template": "Количество агентов, соответствующих этому шаблону",
    # appstream-2 (× normalized by demoji)
    "The total number of instances that are available for streaming or are currently streaming. `ActualCapacity` = `AvailableCapacity` + `InUseCapacity`.": "Общее количество экземпляров, доступных для потоковой передачи или ведущих её в данный момент. `ActualCapacity` = `AvailableCapacity` + `InUseCapacity`.",
    "The number of idle instances currently available for user sessions. `AvailableCapacity` = `ActualCapacity` - `InUseCapacity`.": "Количество простаивающих экземпляров, доступных в данный момент для пользовательских сессий. `AvailableCapacity` = `ActualCapacity` - `InUseCapacity`.",
    "The percentage of instances in a fleet that are being used, using the following formula. `CapacityUtilization` = (`InUseCapacity`/`ActualCapacity`) × 100.": "Процент используемых экземпляров во флоте, рассчитываемый по следующей формуле. `CapacityUtilization` = (`InUseCapacity`/`ActualCapacity`) × 100.",
    "The total number of instances that are either running or pending. This represents the total number of concurrent streaming sessions your fleet can support in a steady state. `DesiredCapacity` = `ActualCapacity` + `PendingCapacity`.": "Общее количество экземпляров, которые работают или ожидают запуска. Это общее количество одновременных потоковых сессий, которые ваш флот может поддерживать в устойчивом состоянии. `DesiredCapacity` = `ActualCapacity` + `PendingCapacity`.",
    "The number of instances currently being used for streaming sessions. One `InUseCapacity` count represents one streaming session.": "Количество экземпляров, используемых в данный момент для потоковых сессий. Одна единица `InUseCapacity` соответствует одной потоковой сессии.",
    "The number of session requests rejected due to lack of capacity.": "Количество запросов на сессию, отклонённых из-за нехватки ёмкости.",
    "The number of instances being provisioned by AppStream 2.0. Represents the additional number of streaming sessions the fleet can support after provisioning is complete. When provisioning starts, it usually takes 10-20 minutes for an instance to become available for streaming.": "Количество экземпляров, подготавливаемых AppStream 2.0. Представляет дополнительное количество потоковых сессий, которые флот сможет поддерживать после завершения подготовки. После начала подготовки экземпляр обычно становится доступным для потоковой передачи через 10-20 минут.",
    # athena
    "The number of milliseconds that the query took to run": "Количество миллисекунд, затраченных на выполнение запроса",
    "The amount of data in megabytes that Athena scanned per DML query. For queries that were canceled (either by the users, or automatically, if they reached the limit), this includes the amount of data scanned before the cancellation time.": "Объём данных в мегабайтах, просканированных Athena на один DML-запрос. Для запросов, которые были отменены (пользователями или автоматически, при достижении лимита), включает объём данных, просканированных до момента отмены.",
    "The number of milliseconds that Athena took to plan the query processing flow. This includes the time spent retrieving table partitions from the data source.": "Количество миллисекунд, затраченных Athena на планирование потока обработки запроса. Включает время на получение партиций таблицы из источника данных.",
    "The number of milliseconds that the query was in the query queue waiting for resources": "Количество миллисекунд, в течение которых запрос находился в очереди запросов в ожидании ресурсов",
    "Number of milliseconds that Athena took to process the query results after the query engine finished running the query": "Количество миллисекунд, затраченных Athena на обработку результатов запроса после того, как механизм запросов завершил его выполнение",
    "The number of milliseconds that Athena took to run a DDL or DML query. TotalExecutionTime includes QueryQueueTime, QueryPlanningTime, EngineExecutionTime, and ServiceProcessingTime.": "Количество миллисекунд, затраченных Athena на выполнение DDL- или DML-запроса. TotalExecutionTime включает QueryQueueTime, QueryPlanningTime, EngineExecutionTime и ServiceProcessingTime.",
    # redshift
    "The percentage of CPU utilization. For clusters, this metric represents an aggregation of all nodes (leader and compute) CPU utilization values.": "Процент использования CPU. Для кластеров эта метрика представляет агрегацию значений использования CPU по всем узлам (ведущим и вычислительным).",
    "The number of database connections to a cluster": "Количество подключений к базе данных кластера",
    "Indicates the health of the cluster. Every minute the cluster connects to its database and performs a simple query. If it's able to perform this operation successfully, the cluster is considered healthy. Otherwise, the cluster is unhealthy. An unhealthy status can occur when the cluster database is under extremely heavy load or if there's a configuration problem with a database on the cluster.": "Указывает на работоспособность кластера. Каждую минуту кластер подключается к своей базе данных и выполняет простой запрос. Если эта операция выполняется успешно, кластер считается работоспособным. В противном случае кластер неработоспособен. Статус неработоспособности может возникать, когда база данных кластера находится под крайне высокой нагрузкой или при наличии проблемы с конфигурацией базы данных на кластере.",
    "Indicates whether the cluster is in maintenance mode.": "Указывает, находится ли кластер в режиме обслуживания.",
    "The rate at which the node or cluster receives data.": "Скорость, с которой узел или кластер получает данные.",
    "The rate at which the node or cluster writes data.": "Скорость, с которой узел или кластер записывает данные.",
    "The percent of disk space used": "Процент использованного дискового пространства",
    # route-53
    "The number of health checks that are healthy among the health checks that Route 53 is monitoring": "Количество исправных проверок работоспособности среди проверок работоспособности, отслеживаемых Route 53",
    "The average time, in milliseconds, that it took Route 53 health checkers to establish a TCP connection with the endpoint": "Среднее время в миллисекундах, затраченное средствами проверки работоспособности Route 53 на установление TCP-соединения с конечной точкой",
    "The total number of DNS queries that Route 53 responds to for a hosted zone": "Общее количество DNS-запросов, на которые Route 53 отвечает для размещённой зоны",
    "The percentage of Route 53 health checkers that consider the selected endpoint to be healthy": "Процент средств проверки работоспособности Route 53, которые считают выбранную конечную точку исправной",
    "The status of the health check endpoint that CloudWatch is checking. `1` indicates healthy, and `0` indicates unhealthy": "Статус конечной точки проверки работоспособности, которую проверяет CloudWatch. `1` означает исправность, а `0` означает неисправность",
    "The average time, in milliseconds, that it took Route 53 health checkers to complete the SSL handshake": "Среднее время в миллисекундах, затраченное средствами проверки работоспособности Route 53 на завершение SSL-рукопожатия",
    "The average time, in milliseconds, that it took Route 53 health checkers to receive the first byte of the response to an HTTP or HTTPS request": "Среднее время в миллисекундах, затраченное средствами проверки работоспособности Route 53 на получение первого байта ответа на HTTP- или HTTPS-запрос",
    # efs
    "The number of burst credits that a file system has": "Количество кредитов всплеска, имеющихся у файловой системы",
    "The number of client connections to a file system. When using a standard client, there is one connection per mounted Amazon EC2 instance.": "Количество клиентских подключений к файловой системе. При использовании стандартного клиента на каждый смонтированный экземпляр Amazon EC2 приходится одно подключение.",
    "The number of bytes for each file system read operation": "Количество байт для каждой операции чтения файловой системы",
    "The number of bytes for each file write operation": "Количество байт для каждой операции записи в файл",
    "The number of bytes for each metadata operation": "Количество байт для каждой операции с метаданными",
    "Shows how close a file system is to reaching the I/O limit of the general purpose performance mode": "Показывает, насколько файловая система близка к достижению лимита ввода-вывода в режиме производительности общего назначения",
    "The maximum amount of throughput a file system is allowed": "Максимальная допустимая пропускная способность файловой системы",
    "The number of bytes for each file system operation, including data read, data write, and metadata operations": "Количество байт для каждой операции файловой системы, включая операции чтения данных, записи данных и операции с метаданными",
}
ADD_TRANS.update(CELL)


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


merge(TRANS_P, ADD_TRANS)
merge(TITLE_P, ADD_TITLES)
print("done")
