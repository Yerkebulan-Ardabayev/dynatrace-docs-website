---
title: Поиск угроз и криминалистический анализ
source: https://www.dynatrace.com/docs/secure/use-cases/threat-hunting
scraped: 2026-03-06T21:29:04.027447
---

# Поиск угроз и криминалистический анализ

# Поиск угроз и криминалистический анализ

* Latest Dynatrace
* Руководство
* Опубликовано 14 марта 2024

При поиске угроз время и точность имеют решающее значение. Вам необходимо быть максимально быстрым и точным, чтобы находить информацию и действовать на её основе. Как аналитик безопасности, расследующий инциденты безопасности или занимающийся поиском угроз, вам часто необходимо

* Переключаться между несколькими выполненными запросами и их результатами
* Управлять доказательствами, собранными в ходе расследований, и повторно использовать их при построении дополнительных запросов
* Обеспечивать, чтобы

  + Расследование поддерживалось в контексте.
  + Инструменты для таких действий поддерживали быстрое создание запросов и детальный обзор результатов.

Далее мы демонстрируем, как вы можете достичь этих целей с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследований**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.").

## Целевая аудитория

Эта страница предназначена для команд безопасности, выполняющих поиск угроз или анализирующих инциденты безопасности, таких как команда реагирования на инциденты или аналитики безопасности.

## Сценарий

Далее мы рассмотрим сценарий, в котором вы получаете уведомление от внешнего источника о подозрительно большом количестве несанкционированных запросов к плоскости управления Kubernetes в период с `2024-02-13 16:00:00` по `2024-02-13 18:59:59`. Ваш кластер Kubernetes настроен как кластер AWS EKS, а логи перенаправляются в Dynatrace.

Как аналитик безопасности, вы хотите понять, связано ли это с вредоносной деятельностью или может быть признаком инцидента кибербезопасности. В ходе этого расследования вы будете следовать по следам своих находок, чтобы проиллюстрировать природу поиска угроз и решения инцидентов.

## Предварительные требования

* [Настройка наблюдаемости Kubernetes с Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* Настройка логирования AWS в CloudWatch:

  + [Настройка логирования кластера EKS](https://dt-url.net/va038gi)
  + [Настройка логирования VPC Flow](https://dt-url.net/ya238ol)
  + [Настройка логирования K8S DNS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks/k8s-dns-logs "Learn how to ingest Kubernetes-related DNS logs from AWS to Dynatrace.")
* [Потоковая передача логов через Amazon Data Firehose](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* Базовые знания

  + [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
  + [Dynatrace Pattern Language (DPL)](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")
  + Как работает разрешение DNS-имён в кластерах Kubernetes

## Путь расследования 1: Анализ журналов аудита Kubernetes

Сначала вы хотите понять, какие действия вызвали уведомление о большом количестве несанкционированных запросов в журналах аудита Kubernetes.
Откройте [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследования**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") и создайте новое расследование.

1. Установите временной диапазон

В [разделе временного диапазона](/docs/secure/investigations/define-timeframes#selector "Adjust time ranges for data analysis and event correlation in Investigations.") установите период с `2024-02-13 16:00:00` по `2024-02-13 18:59:59`, когда происходили несанкционированные запросы.

![установка временного диапазона](https://dt-cdn.net/images/2024-03-06-08-15-45-1914-2f0de669a4.png)

2. Получение журналов аудита кластера Kubernetes

1. Журналы аудита Kubernetes перенаправляются в Dynatrace с прикреплёнными значениями `aws.log_group` и `log_stream`. Чтобы получить все уникальные группы логов AWS CloudWatch, загруженные в Dynatrace, скопируйте и вставьте следующий [DQL-запрос](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") в поле ввода запроса.

   ```
   fetch logs



   | summarize count(), by: aws.log_group
   ```
2. Нажмите **Run** для выполнения запроса.

   ![получение журналов аудита кластера Kubernetes](https://dt-cdn.net/images/2024-03-06-08-45-30-1910-d1342717df.png)

   На этом этапе вы заметите, что в разделе **Query tree** в правом верхнем углу появился круг. Это называется корневым узлом и отмечает начальную точку вашего расследования. С этого момента каждый раз, когда вы изменяете и выполняете запрос, в дереве запросов будет добавляться новый узел, позволяющий перемещаться между запросами, сохраняя историю расследования. Подробности см. в разделе [дерево запросов](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis.").

3. Фильтрация по имени группы логов

1. В результатах запроса найдите запись с группой логов, собирающей логи плоскости управления EKS (в нашем примере `/aws/eks/unguard-secla-demo/cluster`), и [добавьте её как фильтр](/docs/secure/investigations#fields "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") к вашему DQL-запросу.

   ![Добавление фильтра для имени группы логов](https://dt-cdn.net/images/2024-03-06-09-01-16-1530-51987a9960.png)
2. Чтобы просмотреть только события аудита плоскости управления, измените команду `filter` в поле ввода запроса, добавив [оператор `and`](/docs/platform/grail/dynatrace-query-language/operators#dql-logical-or-equality-operators "A list of DQL Operators.") и [строковую функцию `contains`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#contains "A list of DQL string functions.") следующим образом:

   ```
   | filter aws.log_group == "/aws/eks/unguard-secla-demo/cluster" and contains(aws.log_stream, "audit")
   ```
3. В поле ввода запроса удалите команду `summarize` и нажмите **Run** для выполнения запроса.

   ![просмотр только событий аудита плоскости управления](https://dt-cdn.net/images/2024-03-06-09-19-12-1919-c2f0267459.png)

4. Проверка содержимого

В таблице результатов запроса щёлкните правой кнопкой мыши на любой ячейке в поле **content** и выберите **View field details**, чтобы просмотреть необработанное содержимое поля. Подробности см. в разделе [Исследование данных в исходном формате](/docs/secure/investigations/enhance-results#view-details "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").

![Проверка содержимого](https://dt-cdn.net/images/2024-03-07-16-43-25-1546-aa18860a77.png)

5. Извлечение полей из JSON

1. В таблице результатов запроса щёлкните правой кнопкой мыши на любой ячейке в поле **Content** и выберите [**Extract fields**](/docs/secure/investigations/extract-fields#field "Pull specific data points from logs in Investigations.") для перехода в [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.").
2. Выберите **Saved patterns**.
3. В **Dynatrace patterns** выберите **k8s** > **audit**.

   ![извлечение полей](https://dt-cdn.net/images/2024-03-06-18-41-50-1547-0df2e723b3.png)

   При извлечении полей из JSON-структуры вы можете определить только частичную схему для полей, релевантных для вашего сценария. Для продолжения расследования вам нужно выбрать только нужные поля.
4. В поле ввода запроса DPL Architect замените шаблон следующим образом:

   ```
   JSON{



   STRING:verb,



   JSON{string:username}(flat=true):user,



   JSON_ARRAY{ipaddr}(typed=true):sourceIPs,



   JSON{string+:resource}(flat=true):objectRef,



   JSON{int:code}(flat=true):responseStatus



   }(flat=true)
   ```
5. Выберите **Results** для обзора полей, которые будут извлечены из [набора данных предварительного просмотра](/docs/platform/grail/dynatrace-pattern-language/dpl-architect#match-preview "Extract fields with Dynatrace Pattern Language Architect.").

   ![отображение результатов](https://dt-cdn.net/images/2024-03-06-14-28-54-816-6ec66c1606.png)
6. Выберите **Insert pattern**, чтобы добавить шаблон к вашему DQL-запросу.

   ![Вставка шаблона в DPL Architect](https://dt-cdn.net/images/2024-03-11-08-59-35-613-d01beb3deb.png)
7. Нажмите **Run** для выполнения запроса.

6. Фильтрация событий

Чтобы выяснить, какие IP-адреса имеют несанкционированную активность, вам необходимо

* [Развернуть](/docs/platform/grail/dynatrace-query-language/commands/structuring-commands#expand "DQL structuring commands") массив IP-адресов источника
* [Суммировать](/docs/platform/grail/dynatrace-query-language/commands/aggregation-commands#summarize "DQL aggregation commands") результаты с ранее извлечёнными релевантными полями
* [Отфильтровать](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#filter "DQL filter and search commands") результаты, чтобы видеть только несанкционированные запросы (`401`) и запрещённые запросы (`403`)

1. В поле ввода запроса добавьте следующий фрагмент DQL, затем нажмите **Run** для выполнения запроса.

   ```
   | expand sourceIPs



   | summarize count(), by: {sourceIPs, username, verb, resource=objectRef, responseStatus}



   | filter in(responseStatus, {401, 403})
   ```
2. В меню таблицы результатов отсортируйте результаты по количеству, чтобы увидеть, какие IP-адреса имели наибольшее количество подключений.

   ![фильтрация релевантных событий](https://dt-cdn.net/images/2024-03-07-08-11-17-1448-777bfa0c1e.png)

Похоже, вы нашли источник уведомления о безопасности:

* Несанкционированный внешний IP-адрес пытается получить секреты из вашей плоскости управления (в нашем примере `198.51.100.2`, с кодом ответа `401` и 122 подключениями). Это неудивительно, так как сканеры безопасности ежедневно пытаются делать это из интернета.
* Частный IP-адрес многократно пытается перечислить поды (в нашем примере `172.31.29.138`, с кодом ответа `403` и 2090 подключениями). Похоже, это один из подов в вашем кластере Kubernetes, и такое поведение может указывать на скомпрометированный под!

7. Добавление IP-адресов как доказательств

Оба IP-адреса требуют дальнейшего анализа, но тот, у которого ответ `403` и 2090 попыток, является более критическим и требует особого внимания.

Чтобы сохранить IP-адреса как [доказательства](/docs/secure/investigations/manage-evidence "Collect and preserve investigation artifacts in Investigations."), вы можете добавить первый IP (`198.51.100.2`) в предустановленный список доказательств, а второй (`172.31.29.138`) — в новый пользовательский список доказательств:

1. Щёлкните правой кнопкой мыши на `198.51.100.2`, затем выберите **Add to evidence list** > **Suspicious IPs**.
2. Щёлкните правой кнопкой мыши на `172.31.29.138`, выберите **Add to evidence list** > **New evidence list** и введите имя, например, "Suspicious pod".

   ![добавление в коллекции IP](https://dt-cdn.net/images/2024-03-07-08-32-32-357-51a8b2b145.png)

## Путь расследования 2: Исследование потенциальной цели

Чтобы понять, что делал под и какие логи других сервисов нужны для расследования, вы можете начать с сетевых логов. Для AWS лучшее место для начала — [логи сетевых потоков VPC](https://dt-url.net/6c0385l).

1. Получение логов VPC flow

1. Используя [дерево запросов](/docs/secure/investigations/concepts#query-tree "Key concepts for using Dynatrace Investigations across security, operations, and performance analysis."), созданное в ходе расследования, перейдите к шагу [Получение журналов аудита кластера Kubernetes](#fetch-k8s-logs).
2. В результатах запроса найдите запись с группой логов, содержащей логи VPC flow (в нашем примере `/aws/vpc/unguard-secla-demo/vpc-flow-logs`), и добавьте её как фильтр к DQL-запросу.

   ![Логи VPC flow](https://dt-cdn.net/images/2024-03-06-16-11-40-1905-ed76689a2c.png)

   Иконка узла в дереве запросов изменилась, что означает, что вы находитесь в процессе редактирования запроса. Вы можете либо вернуться к исходному запросу для обновления таблицы результатов, либо выполнить изменённый запрос. При выполнении изменённого запроса создаётся новый узел с соответствующим запросом и результатами. Вы можете [присвоить узлу отличительное имя и цвет](/docs/secure/investigations/query-tree "Visualize and structure complex queries in Investigations."), чтобы распознать его позже.
3. В поле ввода запроса удалите команду `summarize`, затем нажмите **Run** для выполнения изменённого запроса.

   ![выполнение изменённого запроса](https://dt-cdn.net/images/2024-03-07-18-21-06-1913-6f988f1771.png)

   Это создаёт вторую ветку в дереве запросов. Ветка — это визуальное представление пути расследования. Посмотрим, куда приведёт нас этот новый путь.

2. Извлечение полей

Для более точных результатов необходимо извлечь поля из записей логов с помощью DPL Architect.

1. В таблице результатов запроса щёлкните правой кнопкой мыши на любой ячейке в поле **content** и выберите **Extract fields**.
2. В DPL Architect выберите **Saved patterns**.
3. В **Dynatrace patterns** выберите **aws** > **vpc-flow-full**.
4. Выберите **Insert pattern**.
5. Нажмите **Run** для выполнения запроса.

3. Фильтрация результатов

Поскольку вас интересуют только результаты от подозрительного пода, вы можете добавить фильтр к DQL-запросу на основе доказательств, созданных на шаге [Добавление доказательств для последующего использования](#evidence).

1. Перейдите в **Evidence lists** и выберите меню доказательств для списка `Suspicious pod`, чтобы увидеть параметры фильтрации и подходящие имена полей, соответствующие типу `IPADDR`.
2. Выберите **Filter for** > **Filter within field `pkt_srcaddr`**. Это добавит фильтр к вашему DQL-запросу.

   ![Фильтрация по доказательствам](https://dt-cdn.net/images/2024-03-07-08-51-47-790-18cc53cc6c.png)
3. Для лучшего обзора сетевых подключений добавьте следующую команду к DQL-запросу в поле ввода:

   ```
   | summarize count(), by: { pkt_dstaddr, protocol, action, dstport}



   | sort `count()` desc
   ```
4. Нажмите **Run** для выполнения запроса.

Вы можете видеть, что подозрительный под чаще всего подключался к DNS-сервису кластера через UDP-порт 53.

![Лучший обзор сетевых подключений](https://dt-cdn.net/images/2024-03-07-09-20-38-1421-bf0a76a211.png)

Возможно, это неправильная конфигурация приложения, или с этим подом происходит что-то подозрительное.

## Путь расследования 3: Определение данных, отправленных подом

Чтобы посмотреть DNS-имена, разрешённые подом, необходимо проверить логи CoreDNS. При правильной настройке логи запросов видны в логах контейнера CoreDNS.

1. Получение логов CoreDNS

1. Чтобы получить логи контейнера CoreDNS, перейдите к шагу [Получение журналов аудита кластера Kubernetes](#fetch-k8s-logs) и измените запрос в поле ввода следующим образом:

   ```
   fetch logs



   | filter k8s.container.name == "coredns"
   ```
2. Нажмите **Run** для выполнения запроса. Это создаёт третью ветку в дереве запросов.

   ![Получение логов CoreDNS](https://dt-cdn.net/images/2024-03-07-19-14-29-1919-bdcb4fef59.png)

2. Извлечение полей

1. В таблице результатов запроса щёлкните правой кнопкой мыши на любой ячейке в поле **content** и выберите **Extract fields**.
2. В DPL Architect выберите **Saved patterns**.
3. В **Dynatrace patterns** выберите **k8s** > **coredns-query**.
4. Выберите **Insert pattern**.
5. Нажмите **Run** для выполнения запроса.

3. Фильтрация результатов

Чтобы просмотреть только записи, содержащие DNS-запросы от вашего подозрительного пода, выберите заголовок столбца **source\_ip**, затем выберите **Filter for** > **Suspicious pod**.

![Фильтрация поля source_ip по подозрительному поду](https://dt-cdn.net/images/2024-03-07-09-52-47-539-9ece6d7f6f.png)

4. Извлечение доменного имени

В таблице результатов может быть довольно много DNS-запросов. Для лучшего понимания разрешённых имён хостов необходимо извлечь доменную часть из поля name и суммировать результаты на её основе.

1. В поле ввода запроса добавьте следующий фрагмент к DQL-запросу:

   ```
   | parse name, "ld* '.'? ( (ld '.' ld):domain '.' eos)"



   | summarize count = count(), by: {domain}
   ```
2. Нажмите **Run** для выполнения запроса.

   Вы замечаете, что помимо внутренних или локальных доменов, один подозрительный домен (`tiitha-maliciousdomain.com`) разрешается очень часто!

   ![обнаружен подозрительный домен](https://dt-cdn.net/images/2024-03-07-10-01-49-503-598f18f1d7.png)

5. Добавление домена как доказательства

1. В таблице результатов запроса щёлкните правой кнопкой мыши на подозрительном доменном имени, затем выберите **Add to evidence list** > **New evidence list**.
2. Введите имя для нового списка доказательств, например, **Attacker domain**.

   ![Добавление домена атакующего как доказательства](https://dt-cdn.net/images/2024-03-07-18-32-15-488-857db7fc3a.png)

6. Фильтрация по домену атакующего

1. В таблице результатов запроса выберите ячейку с подозрительным доменом, затем выберите **Filter for**, чтобы добавить фильтр к запросу, который получает только запросы, включающие домен атакующего.

   ![Фильтрация по вредоносному домену](https://dt-cdn.net/images/2024-03-07-10-17-10-1039-fc84720720.png)
2. В поле ввода запроса удалите команду `summarize` и нажмите **Run** для выполнения запроса.

   Похоже, существует некий обмен данными между подозрительным подом и доменом атакующего. Глядя на имена запросов и учитывая их количество, данные, по-видимому, извлекаются через DNS-туннелирование.

   ![данные извлекаются через DNS-туннелирование](https://dt-cdn.net/images/2024-03-07-10-24-01-1450-8d1cdc2027.png)

7. Анализ DNS-запросов

Поскольку к этому конкретному домену направлены тысячи DNS-запросов, вы можете агрегировать данные, чтобы определить дальнейшие действия.

1. В результатах запроса выберите заголовок столбца **type**, затем выберите [**Summarize**](/docs/secure/investigations/enhance-results#aggregate "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.").
2. Нажмите **Run** для выполнения запроса.

   ![Суммирование по типу](https://dt-cdn.net/images/2024-03-07-10-40-41-399-c7c4bf8285.png)

   Вы замечаете множество запросов A, AAAA и TXT от пода. Вы начинаете исследовать запросы A.
3. В таблице результатов запроса щёлкните правой кнопкой мыши на ячейке **A** и выберите **Filter for**, чтобы добавить фильтр к DQL-запросу.
4. В поле ввода запроса удалите команду `summarize` и нажмите **Run** для выполнения запроса.

   Чтобы определить, какие данные отправляются, необходимо извлечь поддоменную часть домена. Для этого нужно проанализировать один из DNS-запросов, разрешающих домен атакующего.
5. Дважды щёлкните на любой ячейке в таблице результатов запроса.
6. В окне **Details (...)** проверьте данные в поле **name**.

   Похоже, что DNS-имя структурировано по идентификатору, за которым следует полезная нагрузка, закодированная в hex, и эти части разделены `.`.

   ![Проверка имени](https://dt-cdn.net/images/2024-03-07-11-09-13-997-28d0d5a17a.png)
7. Чтобы разобрать и декодировать полезную нагрузку, добавьте следующий фрагмент DQL к запросу:

   ```
   | parse name, """ld:id '.' ld:payload '.tiitha-maliciousdomain'"""



   | fieldsAdd payload=replaceString(payload,".","")



   | fields timestamp, id, payload=decodeBase16ToString(payload)



   | sort timestamp, id
   ```

   Результат подтверждает, что данные из вашего пода определённо извлекаются и отправляются наружу!

   ![данные из пода извлекаются и отправляются](https://dt-cdn.net/images/2024-03-07-11-11-40-1106-e7433155ee.png)

## Путь расследования 4: Выяснение способа отправки команд поду

Вы точно знаете, что под отправляет информацию на внешний DNS-сервер, но вы ещё не выяснили, как он получает команды. Поскольку TXT-тип DNS-запросов позволяет получать более крупные ответы и иногда также используется для вредоносных транзакций, необходимо изучить эти запросы. Поскольку записи CoreDNS не содержат полезную нагрузку ответа, вы обращаетесь к логам Route53.

1. Анализ TXT-записей

1. Используя дерево запросов, перейдите к шагу [Получение журналов аудита кластера Kubernetes](#fetch-k8s-logs).
2. В результатах запроса найдите запись с вашей группой логов Route53 (в нашем примере `/aws/route53/unguard-secla-demo/resolver-logs`) и добавьте её как фильтр к DQL-запросу.
3. В поле ввода запроса удалите команду `summarize` и нажмите **Run** для выполнения запроса. Это создаёт четвёртую ветку в дереве запросов.

   ![Анализ TXT-записей](https://dt-cdn.net/images/2024-03-07-18-55-59-1919-a0b7fff314.png)

2. Извлечение полей из записей логов

1. В таблице результатов запроса щёлкните правой кнопкой мыши на любой ячейке в поле **content** и выберите **Extract fields**.
2. В DPL Architect выберите **Saved patterns**.
3. В **Dynatrace patterns** выберите **aws** > **route53-query**.
4. Вам необходимо извлечь значения `query_name`, `query_type`, `srcaddr` и `answers` из записи лога. В поле ввода запроса вы можете заменить шаблон следующим образом:

   ```
   json{



   string:query_name,



   string:query_type,



   json_array:answers,



   ipaddr:srcaddr



   }(flat=true)
   ```
5. Выберите **Insert pattern**.
6. Нажмите **Run** для выполнения запроса.

3. Фильтрация данных

1. В результатах запроса выберите заголовок столбца `query_name`, затем выберите **Filter for** > **Attacker domain**.
2. Нажмите **Run** для выполнения запроса.

   Вас интересуют только запросы с типом TXT, поэтому вы можете дополнить фильтр соответствующим выражением. Поскольку часть answers является массивом, разверните поле так, чтобы каждое значение в массиве было отдельной записью. Единственные нужные вам поля — это `srcaddr`, `query_name` и элемент `Rdata` из объекта ответа.
3. В поле ввода запроса измените команду `filter`, добавив следующий фрагмент:

   ```
   | filter endsWith(query_name, "tiitha-maliciousdomain.com.") and query_type == "TXT"



   | expand answers



   | fields srcaddr, uery_name, answer=answers[Rdata]
   ```
4. Нажмите **Run** для выполнения запроса.

   Ваша гипотеза подтвердилась: TXT DNS-запросы использовались для получения команд. Выполненные команды (включая запросы к плоскости управления Kubernetes в виде curl-команд) отображаются как ответы в ваших DNS-логах!

   ![Подтверждение гипотезы: TXT DNS-запросы использовались для получения команд](https://dt-cdn.net/images/2024-03-07-19-02-39-1919-08659833f4.png)

## Заключение

Вы выяснили, что произошло, но ещё не разобрались, что ещё делал под, какой процесс или действие запускает DNS-запросы, кто контролирует извлечение данных, как и когда под был заражён, и другие важные аспекты инцидента безопасности.

С этого момента сложность расследования будет только расти, и возможность навигации между различными этапами расследования становится ещё более важной. Все эти вопросы могут вызвать появление новой ветки в дереве запросов, если не отдельного расследования. Наше расследование поднимает множество дополнительных вопросов, требующих ответов.

## Связанные темы

* [Анализ логов AWS CloudTrail с помощью расследований](/docs/secure/use-cases/analyze-aws-cloudtrail-logs-with-security-investigator "Analyze CloudTrail logs and find potential security issues with Dynatrace.")
* [Анализ логов доступа Amazon API Gateway с помощью расследований](/docs/secure/use-cases/analyze-aws-api-gateway-access-logs-with-security-investigator "Monitor and identify errors in your Amazon API Gateway access logs with Dynatrace.")
* [Обнаружение угроз для ваших секретов AWS с помощью расследований](/docs/secure/use-cases/detect-threats-against-aws-secrets-with-security-investigator "Monitor and identify potential threats against your AWS Secrets with Dynatrace.")
* [Ускорение разрешения инцидентов с помощью шаблонов расследований](/docs/secure/use-cases/resolve-incidents-faster-with-templates "Speed up your log-related investigations with Investigations templates.")
* [Операционализация результатов DQL-запросов с помощью расследований](/docs/secure/use-cases/operationalize-query-results "Build DQL queries from your query results faster and more conveniently with Dynatrace Investigations.")
