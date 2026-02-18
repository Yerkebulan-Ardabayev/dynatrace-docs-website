# Документация Dynatrace: analyze-explore-automate/logs
Язык: Русский (RU)
Сгенерировано: 2026-02-18
Файлов в разделе: 8
---

## analyze-explore-automate/logs/lma-logs-app/facets.md

---
title: Filter with facets
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/facets
scraped: 2026-02-06T16:00:17.300826
---

# Фильтр с гранями

# Фильтр с гранями

* Последняя версия Dynatrace
* Практическое руководство
* 3-минутное чтение
* Опубликовано 15 июня 2025 г.

Фасеты — это быстрые фильтры для данных журнала.
Они соответствуют парам «ключ-значение» атрибутов журнала, обнаруженным в вашей среде, и сгруппированы по категориям фасетов.
Наиболее важные идентификаторы полей DQL по умолчанию сгруппированы в предопределенные категории.
Фасеты также помогают оценить объем данных журнала, соответствующих каждому атрибуту.

## Фильтрация данных с помощью фасетов

Запрос журналов в вашей среде с помощью фасетов

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. Разверните группы аспектов, например «Ядро» или «Источник журнала».
3. Разверните аспект, соответствующий вашему запросу, например «Статус».
4. Выберите значения, соответствующие вашему запросу, например «Ошибка» и «Предупреждение».
5. Посмотрите, как генерируются фильтры в поле фильтра.
6. Выберите столько фасетов, сколько необходимо для вашего запроса.

В пределах одного фасета выбранные значения объединяются с помощью оператора `OR`.Это означает, что будут включены журналы, соответствующие любому из выбранных значений для этого аспекта.
Значения между различными фасетами объединяются с помощью оператора `AND`.Это означает, что для включения журналы должны соответствовать хотя бы одному значению из каждого выбранного фасета.
7. Нажмите **Выполнить запрос**, чтобы просмотреть журналы вашей среды на основе вашего фильтра.

## Оценка объема данных с помощью фасетов

Чтобы получить представление о том, сколько журналов с определенными атрибутами имеется в вашей среде.

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. Разверните группы фасетов и фасеты, соответствующие вашему запросу.
3. Посмотрите приблизительные значения для каждого значения.

Числа, отображаемые для каждого значения фасета, представляют приблизительное количество журналов на основе фильтров последнего запроса.Если вы видите символ «~», это означает, что Dynatrace использует выборку при чтении данных журнала для повышения скорости реагирования.

Пример:

* Вы запрашиваете журналы ошибок из пространства имен Kubernetes «astroshop» со следующими фильтрами: `k8s.namespace.name = "astroshop"` `status = "Error"`
* После выполнения запроса посмотрите на фасет `k8s.container.name`.
* Вы увидите только имена контейнеров для журналов, поступающих из пространства имен Kubernetes «astroshop» со статусом «Ошибка».
* Число, отображаемое рядом с именем каждого контейнера, показывает приблизительное количество журналов с пространством имен Kubernetes «astroshop», статусом «Ошибка» и соответствующим именем контейнера.

## Управление всеми аспектами

Чтобы управлять отображением аспектов вашей среды

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. Выберите **Значок редактирования фасетов** рядом с панелью поиска фасетов.
3. Выберите или отмените выбор элементов из предопределенных категорий.

* Установите флажок категории, чтобы выбрать или отменить выбор всех аспектов в категории.
* Выберите, чтобы просмотреть фасеты в категории и выбрать их или отменить выбор.
4. Выберите **Сохранить**.

## Вернуться к настройкам по умолчанию

Если вы ранее изменяли фасеты, чтобы вернуться к настройкам по умолчанию для фасетов в вашей среде.

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. Выберите **Значок редактирования фасетов** рядом с панелью поиска фасетов.
3. Выберите **Сбросить настройки по умолчанию**.
4. Выберите **Сохранить**.

---

## analyze-explore-automate/logs/lma-logs-app/limits.md

---
title: Limits in Logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/limits
scraped: 2026-02-06T16:00:23.763085
---

# Ограничения в журналах

# Ограничения в журналах

* Последняя версия Dynatrace
* Ссылка
* 1 минута чтения
* Опубликовано 19 января 2026 г.

На этой странице описаны ограничения, которые применяются при запросе и просмотре журналов в ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**, а также способы изменения ограничений по умолчанию.

## Строки результатов запроса (**Ограничение количества записей**)

По умолчанию ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** отображают максимум 1000 строк в результате вашего запроса.

Вы можете настроить параметр **Лимит записи** до 50 000 строк, чтобы просмотреть больше результатов в одном запросе.

## Сканированные данные на каждый запрос (**Ограничение количества прочитанных данных**)

![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** считывают максимум 500 ГБ данных на каждый запрос.Запрос останавливается после достижения этого предела.

Вы можете настроить параметр **Лимит чтения данных** на желаемое значение, чтобы сканировать больше данных, но вы не можете установить для него неограниченное значение.

## Размер данных результата (**Ограничение размера результата**)

Размер результата данных, возвращаемых запросом, по умолчанию ограничен 100 МБ.

Вы можете уменьшить параметр **Предел размера результата** и выбрать значение от 1 до 100 МБ в зависимости от ваших потребностей.

## Настройка ограничений

Чтобы настроить ограничения для ваших запросов в ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. В правом верхнем углу рядом с пунктом **Выполнить запрос** выберите (**Меню Действия**) > **Настройки приложения**.
3. На панели **Настройки приложения** настройте нужные ограничения.

---

## analyze-explore-automate/logs/lma-logs-app/log-distribution-chart.md

---
title: Spot trends with the log distribution chart
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart
scraped: 2026-02-06T16:00:15.178106
---

# Выявляйте тенденции с помощью диаграммы распределения журналов

# Выявляйте тенденции с помощью диаграммы распределения журналов

* Последняя версия Dynatrace
* Практическое руководство
* 2 минуты чтения
* Опубликовано 2 июля 2025 г.

Используйте диаграмму распределения журналов, доступную в разделе ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**, чтобы выявить тенденции в ваших журналах.Ты можешь:

* Быстро выявляйте тенденции и аномалии.Например, внезапное увеличение количества журналов `ERROR` может означать инцидент или регресс.
* Детализация по конкретным состояниям журнала или временным диапазонам.
* Выполняйте целевые запросы, не выходя из визуализации.Взаимодействуя с диаграммой, вы можете выбрать статус журнала и более точные сроки для вашего следующего запроса.

![Приложение журналов, показывающее диаграмму распределения журналов](https://dt-cdn.net/images/logs-app-chart-3840-33eaf4738e.png)

## Обзор диаграммы

Диаграмма распределения журналов обеспечивает визуальный обзор записей журнала с течением времени.

Записи журнала сгруппированы по статусу.Каждый статус представлен отдельным цветом для облегчения различения.Доступны следующие статусы:

* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__

Эти статусы соответствуют атрибуту `status`, который создается во время приема журнала.Подробнее см. информацию об автоматическом пополнении журнала для [OneAgent-](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#transform-all-types-of-logs "Generic log ingestion automatically transforms log data into output values for the loglevel attribute.") или [Журналы, полученные через API](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-log-data-transformation#transform-all-types-of-logs "Log ingestion API automatically transforms log data into output values for the loglevel attribute.").

## Взаимодействие с диаграммой распределения журналов

Вы можете взаимодействовать с диаграммой распределения журналов, чтобы уточнить свой анализ.

* **Выделение определенных статусов журнала**.

+ Выберите статус на диаграмме или легенде, чтобы сосредоточиться только на этом статусе.
+ Для отображения нескольких статусов используйте легенду диаграммы.
* **Увеличение временного диапазона**.Выделите часть диаграммы, а затем выберите **Приблизить к выделенному**.
* **Используйте панель инструментов диаграммы**.Наведите указатель мыши на диаграмму, чтобы отобразить панель инструментов.

+ Выберите (**Изменить режим**), чтобы переключаться между **Режимом исследования** (выделение отдельных статусов), **Режимом масштабирования** и **Режимом панорамирования** (исследование диаграммы по горизонтали).
+ Увеличение или уменьшение масштаба диаграммы.
+ Выберите (**Сброс**), чтобы вернуть диаграмму в исходное состояние.

Для более быстрого и удобного взаимодействия с диаграммой распределения бревен используйте сочетания клавиш.Они отображаются при наведении курсора на значки панели инструментов.

## Влияние на выставление счетов

Загрузка диаграммы распределения журналов и взаимодействие с ней не требует лицензии на запросы.

Диаграмма распределения журналов может быть основана на выборочных данных, что означает, что отображаемые данные являются репрезентативными, и не отображаются все записи журнала.

---

## analyze-explore-automate/logs/lma-logs-app/message.md

---
title: Adjust the log message
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/message
scraped: 2026-02-06T16:00:21.678181
---

# Настройте сообщение журнала

# Настройте сообщение журнала

* Последняя версия Dynatrace
* Практическое руководство
* 3-минутное чтение
* Опубликовано 10 октября 2025 г.

Приложение ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** автоматически извлекает и выделяет сообщение журнала из записи и отображает его в отдельном столбце в таблице результатов.

Хотя полное содержимое и все атрибуты записи журнала могут быть важны для понимания основной причины, возможность быстрого сканирования сообщений может ускорить поиск соответствующих журналов и диагностику проблемы.

## Что такое сообщение журнала?

Во многих случаях журналы облачных приложений или платформ содержат определенное поле, содержащее фактическое сообщение.

Столбец **Сообщение журнала** – это динамически создаваемое поле, в котором, если возможно, отображается читаемая часть записи журнала.

### Примеры

Запись журнала

Записать сообщение

```
{



"timestamp": "2025-10-13T10:50:03.205",



"level": "WARN",



"logger": "org.apache.activemq.artemis.core.server",



"message": "AMQ222165: No Dead Letter Address configured for queue answer_queue in AddressSettings",



"context": "default"



}
```

AMQ222165: Для очереди ответ\_очередь в настройках адреса не настроен адрес недоставленного письма.

```
{



"timestamp": "2025-10-13T08:54:02.009817Z",



"severity": "INFO",



"insertId": "238n5ebl11v8lc1x",



"jsonPayload": {



"message": "\"Starting watch\" path=\"/api/v1/namespaces/external-accounts \" resourceVersion=\"17603423543179000\" timeout=\"7m10s\""



},



"logName": "projects/prod-gke-apigw/logs/container.googleapis.com%2Fapiserver",



"resource": {



"labels": {



"location": "europe-west3",



"project_id": "prod-gke-apigw "



},



"type": "k8s_control_plane_component"



},



"sourceLocation": {



"file": "get.go",



"line": "278"



}



}
```

"Начало просмотра" path="/api/v1/namespaces/external-accounts " resourcesVersion="17603423543179000" timeout="7m10s"

```
{



"time":"2025-11-01T13:03:00Z",



level":"INFO",



"content":"time=\"2025-10-13T08:44:57Z\" level=info msg=\"No status changes. Skipping patch\" application=argocd/unguard-dev-root",



"userId":123



}
```

Никаких изменений статуса.Пропуск патча

## Отображение или скрытие столбца **Сообщение журнала**

По умолчанию:

* Отображается столбец **Сообщение журнала**.
* Столбец **содержание** скрыт.

Чтобы отобразить или скрыть столбец **Сообщение журнала** (или любые другие доступные столбцы)

1. Перейдите в раздел ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.
2. Запустите запрос для получения журналов.
3. В правом верхнем углу таблицы результатов выберите **Настройки столбца**.
4. В окне **Столбцы** установите или снимите флажки, чтобы отобразить или скрыть соответствующие столбцы в ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журнала**.

* Используйте поле поиска, чтобы найти столбцы.
* Используйте элементы управления и для изменения порядка отображения столбцов.
5. Нажмите **Применить**, чтобы сохранить изменения и закрыть окно **Столбцы**.

## Как извлекается сообщение журнала

Сообщение журнала извлекается из записи журнала как часть выполнения запроса и не влечет за собой дополнительных затрат по вашей лицензии.Если сообщение по атрибутам, перечисленным ниже, не найдено, поле **content** отображается как резервное.

### Атрибуты первого уровня

Для определенных технологий или в результате ваших правил синтаксического анализа поле с сообщением журнала доступно как атрибут первого уровня в записи журнала.Сообщение журнала извлекается из следующих атрибутов первого уровня:

* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__

Для источников журналов, передаваемых в Dynatrace через API, для достижения наилучших результатов запишите сообщение журнала в любой из предыдущих атрибутов во время регистрации.

В качестве альтернативы извлеките эту читаемую информацию в атрибут первого уровня всего за несколько шагов в процессоре OpenPipeline.Подробную информацию см. в [Обработка журналов с помощью OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Process logs using Dynatrace OpenPipeline.").

### Структурированные журналы JSON

Многие средства ведения журнала, такие как GCP, Serilog и log4net, или платформы облачного ведения журналов предоставляют информацию в виде структурированного JSON.Когда этот структурированный журнал хранится в поле **content** в Dynatrace, сообщение журнала извлекается из следующих стандартных ключей JSON:

* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__
* __КОД_0__

### Неструктурированные журналы

Когда ваш источник журнала выводит информацию в соответствии с популярным стилем logfmt, сообщение журнала извлекается из неструктурированного журнала в **content**.

Сообщение журнала обнаруживается в паре ключ/значение для следующих ключей:

* __КОД_0__
* __КОД_0__
* __КОД_0__

---

## analyze-explore-automate/logs/lma-logs-app/query-and-filter.md

---
title: Query and filter logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter
scraped: 2026-02-06T16:00:13.052335
---

# Журналы запросов и фильтров

# Журналы запросов и фильтров

* Последняя версия Dynatrace
* Практическое руководство
* 4-минутное чтение
* Опубликовано 2 июля 2025 г.

В ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** вы можете создавать запросы, использовать фильтры, искать определенные строки журнала и многое другое.

## Создайте запрос в журналах **Logs**

Запросите журналы, указав оператор сегмента и фильтра с ключами и значениями с вашими условиями поиска, компараторами и логическими операторами.

* **Сегмент**: общий фильтр для данных наблюдения в приложениях на платформе Dynatrace.
* **Ключ**: поле или атрибут, по которому требуется фильтровать.
* **Значение**: конкретное значение, которое вы ищете.
* **Логический оператор**: соединяет несколько операторов фильтра.

По умолчанию все операторы фильтра подключены к `AND`.
* **Компаратор**: определяет тип сравнения.

![Поле фильтра в приложении «Журналы»](https://dt-cdn.net/images/untitled-001-1835-80e79a2919.png)

[Фильтр с гранями](/docs/analyze-explore-automate/logs/lma-logs-app/facets "Filter with facets in the Dynatrace Logs app."), чтобы автоматически добавлять ключи и значения в фильтр.

Используйте средство выбора даты, чтобы применить правильный временной интервал для вашего запроса.

Выберите **Выполнить запрос**, чтобы выполнить запрос.

После того как ваш запрос вернет записи в таблицу результатов, вы можете выполнить поиск по ключевым словам в этих данных.Используйте поле **Искать в результатах**, чтобы отфильтровать таблицу по ключевому слову.Эта фильтрация не выполняет новый запрос, а только показывает уже возвращенные и загруженные результаты в вашем браузере.

## Использовать сегменты **Сегменты**

По возможности применяйте сегментный фильтр к вашему запросу.

* Сегменты позволяют фильтровать журналы и другие наблюдаемые данные с помощью единого фильтра.
* Сегменты удобны для ограничения ваших запросов только определенными сегментами Grail, что уменьшает объем данных, которые необходимо сканировать для получения релевантных результатов.

Дополнительные сведения см. в [Сегментировать журналы по сегментам](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket "Segment logs by bucket with segments") и [лучшие практики для журналов](/docs/analyze-explore-automate/logs/lma-best-practices#use-bucket-filters "Best practices for setting up Log Management and Analytics with Dynatrace.").
* Сегменты позволяют сохранять и повторно использовать часто используемые фильтры, которые применимы в ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналах** и в других приложениях Dynatrace.

## Изучите последние фильтры и фильтры-штифты

![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** сохраняют недавно использованные фильтры, чтобы вы могли повторно применить их одним щелчком мыши.Вы также можете сохранить фильтры, закрепив их.

Выберите поле фильтра и проверьте раздел **Недавно использованные фильтры**.В этом разделе отображаются недавно примененные вами фильтры, причем самые последние находятся вверху.Когда вы вводите новый оператор фильтра, этот список сокращается до аналогичных операторов из недавно использованных фильтров.

Выберите (**Закрепить фильтр**), чтобы закрепить любой созданный вами фильтр.Если поле фильтра пусто, выберите его и прокрутите вниз до раздела **Закрепленные фильтры**, чтобы просмотреть ранее закрепленные фильтры.Открепите фильтр, снова выбрав (**Закрепить фильтр**).

## Поиск фразы в логах

Если вам нужно найти журналы, содержащие определенную фразу, у вас есть несколько вариантов: от самой широкой до более узкой фильтрации.

### Поиск по всем полям

Используйте `*` вместо ключевого имени и `~` в качестве компаратора для поиска вашей фразы во всех полях записи журнала, соответствующих вашим фильтрам.

Например, фильтр `* ~ "failed to charge card"` соответствует журналам, которые содержат эту фразу в любом поле.

Это эквивалентно использованию команды DQL [`search`](/docs/platform/grail/dynatrace-query-language/commands/filtering-commands#search «Команды фильтрации и поиска DQL»).

### Поиск по `content`

Обычно исходные полезные данные журнала сохраняются в поле `content` записи журнала.Ограничьте поиск этим полем, чтобы повысить производительность запроса.

Например, фильтр `content ~ "failed to charge card"` соответствует журналам, которые содержат эту фразу в поле `content`.

Это эквивалентно использованию строковой функции [`matchesPhrase`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesPhrase «Список строковых функций DQL.») DQL.

### Подстановочный знак в значении

Вы также можете указать только часть значения с помощью подстановочного знака, используя `*` в поисковом запросе.

Например, фильтр `content = "*card*"` соответствует журналам, содержащим фразу `card` в поле `content`.

Это эквивалентно использованию строковой функции [`matchesValue`](/docs/platform/grail/dynatrace-query-language/functions/string-functions#matchesValue «Список строковых функций DQL.»).

Полную информацию см. в [Поле фильтра](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.").

## Фильтрация по полю с несколькими значениями

По умолчанию все операторы фильтра связаны с логическим оператором `AND`.Например, `status = ERROR` `status = WARN` не возвращает результатов, поскольку одна запись журнала не может иметь два статуса.

Для запроса по полю с разными значениями используйте оператор `in`.Например, `status in (ERROR, WARN)` возвращает журналы со статусом `ERROR` или `WARN`.Альтернативно вы можете использовать `OR` для объединения нескольких операторов фильтра.

## Используйте автоматические предложения для фильтров журналов

![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** предоставляют предложения по автозаполнению ключей, компараторов и значений.

* Выберите поле фильтра, чтобы получить список предложений для наиболее распространенных или релевантных полей для фильтрации.
* После выбора поля вы получаете список предложений для компараторов.
* После выбора компаратора вы получаете список предлагаемых значений для этого поля.Это не поддерживается для поля `content`.

Обратите внимание, что предложения представлены на основе фактических значений, запрошенных в фоновом режиме из данных журнала, но стоимость запроса для контекстно релевантных предложений не взимается.

## Похожие темы

* [Поле фильтра](/docs/discover-dynatrace/get-started/dynatrace-ui/ui-filter-field "The filter field is a powerful tool that allows you to quickly find relevant information or narrow down results within apps.")
* [Фильтр с гранями](/docs/analyze-explore-automate/logs/lma-logs-app/facets "Filter with facets in the Dynatrace Logs app.")
* [Сегментировать журналы по сегментам](/docs/manage/segments/use-cases/segments-use-cases-logs-by-bucket "Segment logs by bucket with segments")
* [Лучшие практики управления журналами и аналитики](/docs/analyze-explore-automate/logs/lma-best-practices "Best practices for setting up Log Management and Analytics with Dynatrace.")

---

## analyze-explore-automate/logs/lma-logs-app/surrounding-logs.md

---
title: View surrounding logs
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs
scraped: 2026-02-06T16:00:10.985968
---

# Просмотр окружающих журналов

# Просмотр окружающих журналов

* Последняя версия Dynatrace
* Практическое руководство
* 1 минута чтения
* Опубликовано 2 июля 2025 г.

Просмотрите окружающие журналы для каждой записи журнала, чтобы лучше понять контекст данных.

![Окружающие журналы ошибок журнала на основе корреляции идентификаторов трассировки](https://dt-cdn.net/images/surroundinglogs-1907-40995092b7.png)

Чтобы просмотреть окружающие журналы

1. В ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** найдите соответствующую строку журнала в таблице результатов и откройте ее сведения.
2. Выберите **Показать окружающие журналы**.

Окружающие журналы отображаются в контексте, предоставленном записью журнала.

* Если присутствует параметр `trace_id`, вы должны увидеть другие записи с тем же идентификатором трассировки.

Дополнительную информацию об автоматической корреляции см. в разделе [Подключите данные журнала к трассировкам](/docs/analyze-explore-automate/logs/lma-log-enrichment "Connect your incoming log data to traces for more precise Dynatrace analysis.").
* Альтернативно вы можете просмотреть окружающие журналы на предмет того же объекта топологии, например хоста.

Выберите **Выполнить запрос для 15 журналов до** или **Выполнить запрос для 15 журналов после**, чтобы расширить контекст, загрузив дополнительные данные до или после временной метки оригинала.

---

## analyze-explore-automate/logs/lma-logs-app.md

---
title: Logs app
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app
scraped: 2026-02-06T15:59:38.914707
---

# Приложение журналов

# Приложение журналов

* Последняя версия Dynatrace
* Приложение
* 4-минутное чтение
* Обновлено 1 июля 2025 г.

Предварительные условия

### Разрешения

В следующей таблице описаны необходимые разрешения.

Разрешение

Описание

хранилище: промежутки: чтение

разрешить чтение интервалов, переменных сегментов (необязательно)

хранилище: bizevents: читать

разрешить чтение бизнес-событий, переменных сегментов (необязательно)

хранилище: метрики: чтение

разрешить чтение показателей, переменных сегментов (необязательно)

хранилище: события: чтение

разрешить чтение событий, переменных сегментов (необязательно)

хранилище:security.events:прочитать

разрешить чтение событий безопасности, переменных сегментов (необязательно)

хранилище: журналы: чтение

разрешить читать логи

хранилище: user.sessions: читать

разрешить чтение пользовательских сессий, переменных сегментов (необязательно)

хранилище: user.events: читать

разрешить чтение пользовательских событий

хранилище: ведра: читать

разрешить читать логи

хранилище: файлы: чтение

разрешить выполнять соединения в таблицах поиска

10

строк на странице

Страница

1

из 1

## Установка

Убедитесь, что это приложение [установлен в вашей среде](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Начать

Концепции

![Динамическая гистограмма с интуитивно понятным фильтром «укажи и щелкни» предоставляет уникальные возможности для упрощенного и своевременного изучения журналов.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/3.png)![Функция «Объяснение журналов» предоставляет практические шаги и аналитическую информацию, позволяющую сократить анализ первопричин и сократить время на действия, что позволяет быстрее устранять проблемы.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/2.png)![Четкие, упорядоченные тенденции серьезности с быстрыми и интуитивно понятными параметрами фильтрации помогают легко исследовать журналы со структурой JSON и другие журналы.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/1.png)![Сократите MTTR, превратив необработанные журналы в управляемую информацию — в контексте вашей трассировки или окружающих объектов топологии.](https://dt-cdn.net/hub/logs-hub-4.png)![Подробности журнала отображаются в богатом контексте одним щелчком мыши — доступ к связанным трассировкам, топологии и многому другому.Мгновенные фильтры превращают информацию в точный поиск.](https://cdn.hub.central.dynatrace.com/hub/console/drafts/85/media/4.png)

1 из 5Динамическая гистограмма с интуитивно понятным фильтром «укажи и щелкни» предоставляет уникальные возможности для упрощенного и своевременного просмотра журналов.

[01Журналы запросов и фильтров

* Практическое руководство
* Изучите журналы с помощью запросов DQL и операторов фильтрации в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/query-and-filter)[02Выявляйте тенденции с помощью диаграммы распределения журналов.

* Практическое руководство
* Получите визуальный обзор записей журнала, сгруппированных по статусу, чтобы выявлять тенденции, выявлять аномалии и выполнять целевые запросы, не выходя из визуализации.](/docs/analyze-explore-automate/logs/lma-logs-app/log-distribution-chart)[03Просмотр окружающих журналов

* Практическое руководство
* Используйте окружающие журналы для понимания данных журналов в контексте приложения Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/surrounding-logs)[04Фильтр с фасетами

* Практическое руководство
* Фильтр с помощью фасетов в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/facets)[05Настройте сообщение журнала

* Практическое руководство
* Настройте сообщение журнала в приложении Dynatrace Logs.](/docs/analyze-explore-automate/logs/lma-logs-app/message)[06Ограничения в журналах

* Ссылка
* Узнайте об ограничениях, применимых к приложению «Журналы», и о том, как их изменить.](/docs/analyze-explore-automate/logs/lma-logs-app/limits)

## О журналах

![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы** — это отправная точка для поиска соответствующих записей журнала без написания запросов.

* Найдите нужные журналы.
Легко фильтруйте журналы без написания DQL и находите нужные журналы.
* Проактивное расследование.
Выявляйте проблемы и получайте ценную информацию, исследуя диаграмму распределения журналов с течением времени.
* Откройте для себя основную причину проблем из контекста.
Изучите окружающие интересующие журналы, чтобы понять контекст и основную причину ошибок:

+ Найдите основную причину и проверьте, не является ли журнал только признаком проблемы.
+ На основе трассировок: отображать детали транзакций в распределенной среде.
+ На основе источника: анализируйте выбранную запись в контексте одного компонента.
* Расширьте свой анализ.
Быстро перемещайтесь между деталями журнала и связанными хостами, кластерами Kubernetes, трассировками или другими объектами.
Это поможет вам понять влияние отдельной записи в контексте связанных метрик и трассировок.
* Поделитесь своими выводами.
Продолжайте свое путешествие, войдя в ![Ноутбуки](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Блокноты**, ![Панели мониторинга](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Панели мониторинга**, ![Расследования](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Расследования** или автоматизируйте их с помощью ![Рабочие процессы](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Рабочие процессы**.

## ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ

Могу ли я редактировать запрос DQL?

В меню выберите **Редактировать запрос DQL** рядом с кнопкой **Выполнить запрос**.

Как лицензируются журналы?

Запрос журналов работает на основе того же лицензирования, что и другие функции управления журналами и аналитики.

* Если у вас есть **Сохранять** и **Запрос** как отдельные элементы прейскуранта, вы используете лицензию только для запрашиваемого тома журнала в байтах.
Для получения дополнительной информации см. [Рассчитайте потребление Log Management & Analytics – Query (DPS)](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").
* Если в прейскуранте указано **Сохранять с включенными запросами**, за включенные запросы плата не взимается.
Для получения дополнительной информации см. [Аналитика журналов (DPS)](/docs/license/capabilities/log-analytics#log-retain-included-queries "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

Следующие действия бесплатны:

* Фасеты и предложения полей фильтра.
* Формирование диаграммы распределения журналов.
* Поиск ранее полученных результатов (с помощью поля поиска над таблицей).

Лицензия используется только тогда, когда вы нажимаете кнопку **Выполнить запрос** или используете **Окружающие журналы**.

Как настроить доступ к журналам?

Пользователи должны иметь доступ к платформе Dynatrace и журналам, хранящимся в Grail ([посмотреть встроенные политики доступа](/docs/platform/upgrade#built-in-policies "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.") для данных журналов).Приложение заменяет экран **Журналы и события**, поэтому пользователи, которые ранее обращались к журналам, могут использовать ![Журналы](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Журналы**.

[![Центр](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследуйте в Dynatrace Hub

Найдите соответствующие записи журнала без написания запросов DQL.](https://www.dynatrace.com/hub/detail/logs/?internal_source=doc&internal_medium=link&internal_campaign=cross/)

---

## analyze-explore-automate/logs.md

---
title: Log Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs
scraped: 2026-02-18T05:31:27.617179
---

# Log Analytics

# Log Analytics

* Latest Dynatrace
* Explanation
* 6-min read
* Updated on Jan 28, 2026

Log Management and Analytics powered by [Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") provides a unified approach to unlocking the value of log data in the Dynatrace platform.

Hassle-free management of your log data lets you [ingest](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.") petabytes of data without schemas, indexing, or rehydration. All of that data is usable at any time for any analytics task. Thanks to schema on-read and the [Dynatrace Query Language (DQL)](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language."), there's no need to decide what you want to query during data ingestion. Select the retention period for your data that suits your business and compliance needs, whether for debugging or audit purposes.

Put Dynatrace Log Management and Analytics into use:

* **Enhance unified observability**: Integrate logs with traces and metrics for comprehensive observability in Kubernetes and cloud. Use Grail, DQL, and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** for unified exploration and visualization with dashboards.
* **Accelerate problem resolution**: Utilize logs for detailed troubleshooting, leveraging Dynatrace Intelligence to pinpoint relevant logs and reduce mean time to repair. Perform instant queries with Grail and DQL for rapid issue resolution.
* **Close monitoring gaps**: Track metrics, health, performance, and business indicators from hybrid cloud and mainframe deployments. Automate log collection with OneAgent, parse and process logs at scale with OpenPipeline, and transform logs into metrics with Grail and DQL.

## Get started

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Quick start guide**

Take the first steps to onboard and explore your logs.](/docs/analyze-explore-automate/logs/lma-use-cases/lma-e2e-real-time-observability-logs-dql "Explore the Log Management and Analytics use case for real-time observability with logs.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Ingest logs**

Set up log collection to automatically bring logs from different sources.](/docs/analyze-explore-automate/logs/lma-log-ingestion "Stream log data to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Set up buckets and permissions**

Configure storage and define retention and access controls.](/docs/analyze-explore-automate/logs/lma-bucket-assignment "Your log data can be stored in data retention buckets based on specific retention periods.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Configure processing in OpenPipeline**

Define how ingested logs are processed and stored.](/docs/analyze-explore-automate/logs/lma-log-processing "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** **app**

Learn how to leverage ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**.](/docs/analyze-explore-automate/logs/lma-logs-app "Search, filter, and analyze logs with Dynatrace Logs app to quickly investigate and share insights.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Alerting, Problems, and automations**

Create anomaly detection and alerts, as well as automate the detection process.](/docs/analyze-explore-automate/logs/alerting-on-logs "Create, or let Dynatrace create, alerts-based log data in Dynatrace log monitoring")

Log data can come from diverse sources, including Kubernetes, technology stacks, cloud services, hyperscalers, custom API integrations, or Dynatrace extensions. Dynatrace employs OneAgent and API as key methods for ingesting logs from these sources.

The ingested logs are channeled to Dynatrace OpenPipeline for processing, analysis, and storage.

![Dynatrace Platform Overview](https://dt-cdn.net/images/logs-overview-2678-9573941b3e.png)

The Grail data lakehouse serves as a single unified storage solution where log data is interconnected within a real-time model that reflects the topology and dependencies within a monitored environment.

You can analyze the ingested data in ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs**, run queries in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** to gather a comprehensive understanding of your log data, or use ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** for real-time visualization and monitoring.

## Consumption model

The consumption model for Log Management and Analytics is based on three dimensions of data usage (Ingest & Process, Retain, and Query). The unit of measure for consumed data volume is gibibytes (GiB). In addition, **Retain with Included queries** is an available option combining the dimensions of Query and Retention. For details, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

## Availability and previous versions

Log Management and Analytics is the latest log offering available in Dynatrace SaaS with Grail.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Explore in Dynatrace Hub

Make smarter, faster decisions when troubleshooting and measuring the health of your environments: automatically unify logs, traces, and metrics of events in real time, monitor Kubernetes, optimize storage costs by extracting metrics from logs at ingest or read time, and resolve incidents faster.](https://www.dynatrace.com/hub/?filter=log-management-and-analytics&internal_source=doc&internal_medium=link&internal_campaign=cross)

## Related topics

* [Upgrade to Log Management and Analytics](/docs/analyze-explore-automate/log-monitoring/logs-upgrade/lmc-logs-upgrade-to-lma "Log Management and Analytics is the latest Dynatrace log monitoring solution. We encourage you to upgrade to this latest log monitoring offer.")
* [Log Management and Analytics use cases](/docs/analyze-explore-automate/logs/lma-use-cases "Explore common Log Management and Analytics use cases in Dynatrace deployments.")
* [Log on Grail examples](/docs/analyze-explore-automate/logs/logs-on-grail-examples "Explore basic Log Management and Analytics examples of how to use log data in Dynatrace powered by Grail.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")

---
