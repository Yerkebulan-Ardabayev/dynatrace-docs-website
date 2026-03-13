---
title: Run JavaScript action for Workflows
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/default-workflow-actions/run-javascript-workflow-action
scraped: 2026-03-04T21:33:36.756619
---

# Действие Run JavaScript для Workflows

# Действие Run JavaScript для Workflows

* Latest Dynatrace
* Справочник
* Чтение: 6 мин.
* Обновлено 25 июня 2025 г.

Действие **Run JavaScript** для Workflows позволяет создавать пользовательские задачи, выполняющие JavaScript-код в рабочем процессе.

Платформа Dynatrace предоставляет [среду выполнения JavaScript](https://dt-url.net/mf03qa8) для пользовательских скриптов в Workflows.

Пользовательские JavaScript-задачи в рабочих процессах получают `executionId`, `actionExecutionId` и `loopItemValue`, которые в сочетании с [SDK автоматизации](https://dt-url.net/vq23qax) обеспечивают доступ к результатам задач, выполнению рабочих процессов и параметрам элементов цикла непосредственно как JavaScript-объекты, без использования выражений Jinja.

Для использования SDK автоматизации импортируйте их в пользовательскую задачу скрипта. После этого их можно инициализировать с контекстом выполнения.

Мы предоставляем как [клиентский SDK автоматизации](https://dt-url.net/j343q5k), который обеспечивает полный доступ к Automation API, так и [SDK утилит автоматизации](https://dt-url.net/0n63qgu), ориентированный на удобство использования.

Выполнение действия Run JavaScript для Workflows аналогично запуску кода в [Function executor](https://dt-url.net/cp83qh8). Результаты можно найти на вкладке **Result** раздела **Execution**, и они могут быть использованы в последующих задачах.

## Безопасность действия Run JavaScript

* Действие **Run JavaScript** не поддерживает [выражения](/docs/analyze-explore-automate/workflows/reference "Изучите выражения Workflows") во входных данных, чтобы исключить возможность внедрения кода.
* Все HTTP-вызовы проверяются по глобальному списку разрешённых адресов.
* Если вы импортируете [сторонние библиотеки](#third-party) для вашего JavaScript-действия, домены CDN из списка разрешённых предоставляют доступ ко всему портфелю пакетов. Среда выполнения JavaScript Dynatrace устойчива к определённым векторам атак, но вы можете случайно разрешить выполнение вредоносного кода. Убедитесь, что зависимости, на которые вы полагаетесь, зеркалируются в вашей внутренней инфраструктуре, и отслеживайте их последствия для безопасности с помощью [Dynatrace Application Security](/docs/secure/application-security "Доступ к функциональности Dynatrace Application Security.") или сторонних инструментов, таких как Snyk.

Настоятельно не рекомендуется возвращать какие-либо секретные данные в составе результата. Каждый результат доступен в разделе выполнений для всех, у кого есть доступ на чтение к рабочему процессу.

## Требования к действию Run JavaScript

* Совместимость среды выполнения JavaScript Dynatrace с Node и Web API описана в документации [JavaScript runtime](https://developer.dynatrace.com/reference/javascript-runtime/).
  Среда выполнения JavaScript имеет тайм-аут 120 секунд.
  Соответственно, любое действие Run JavaScript также имеет тайм-аут 120 секунд.
  Обратите внимание, что этот тайм-аут нельзя увеличить, установив более высокое значение в настройках задачи.
* Среда выполнения JavaScript предоставляет до 256 МБ оперативной памяти.
* Среда выполнения JavaScript и, соответственно, действия Run JavaScript не могут возвращать бинарный результат. В качестве обходного решения можно сериализовать данные в объект.
* Размер скрипта действия Run JavaScript ограничен примерно 5 МБ. Дополнительная контекстная информация, неявно отправляемая AutomationEngine при вызове действия, например идентификаторы выполнения рабочего процесса и действия, также учитывается в данном ограничении.
* Результат действия Run JavaScript ограничен 6 МБ.
* Существует ограничение на количество одновременных запросов к базовой инфраструктуре (Function executor), которая выполняет среду JavaScript. Если ваши задачи Run JavaScript сталкиваются с такой проблемой, вы можете использовать функцию повторных попыток в настройках задачи для её решения.

## Результат задачи

Ваши JavaScript-действия могут получать результат предыдущей задачи и использовать его для дальнейшей обработки.

### Пример использования SDK automation-utils для доступа к результату

```
// import of sdk modules



import { result } from '@dynatrace-sdk/automation-utils';



export default async function () {



// get the result of task 'my_task'. 'my_task' must be a predecessor.



var myResult = await result('my_task');



// log the result object



console.log('The whole result object: ', myResult);



console.log('only one variable: ', myResult.myVariable)



}
```

### Пример использования SDK client-automation для доступа к результату

```
// import of sdk modules



import { executionsClient } from '@dynatrace-sdk/client-automation';



export default async function ({ executionId }) {



// load the execution object using the current executionId



var config = {executionId, id: 'my_task'}



var myResult = await executionsClient.getTaskExecutionResult(config)



// log the result object



console.log('My task result: ', myResult)



console.log('only one variable: ', myResult.myVariable)



}
```

## Доступный контекст выполнения

Следующий контекст выполнения доступен из коробки и может быть использован для любых сценариев, которые в нём нуждаются.

```
export default async function ({ executionId, actionExecutionId }) {



//log available execution context ids



console.log('Workflow execution id: ', executionId);



console.log('Action execution id: ', actionExecutionId)



}
```

Для контекста элемента цикла см. раздел [Цикл задачи](#task-loop) ниже.
Различная контекстная информация рабочего процесса также доступна непосредственно в среде выполнения JavaScript Dynatrace.

## Цикл задачи

При использовании опции циклического выполнения задачи вам может потребоваться доступ к значению текущего элемента цикла. Для этого используйте параметр `loopItemValue`, чтобы получить значение элемента для текущей итерации.

### Пример использования `loopItemValue`

```
export default async function ({ loopItemValue }) {



// log the current value of the loop item



console.log(loopItemValue)



}
```

## Контекстная информация AutomationEngine

Пакет `@dynatrace-sdk/automation-utils`, доступный для задач Run JavaScript, предоставляет доступ к следующей информации:

* `workflowId` — идентификатор выполняемого рабочего процесса.
* `executionId` — идентификатор связанного выполнения рабочего процесса.
* `actionExecutionId` — идентификатор текущего выполнения действия.
* `taskName` — имя задачи в выполнении рабочего процесса, с которым связано выполнение действия.

```
// optional import of sdk modules



import { actionExecutionId, executionId, taskName, workflowId } from '@dynatrace-sdk/automation-utils';



export default async function () {



console.log(`Running action execution '${actionExecutionId}' for task '${taskName}' of workflow '${workflowId}' in workflow execution '${executionId}'`)



}
```

## Импорт сторонних библиотек

Если для вашего JavaScript-действия требуется определённая функциональность, предоставляемая сторонними библиотеками, вы можете загрузить библиотеку через импорт URL.

Применяются ограничения:

* JavaScript-модули должны быть допустимыми [модулями ECMAScript](https://tc39.es/ecma262/#sec-modules)
* Они выполняются в [контексте среды выполнения JavaScript Dynatrace](https://developer.dynatracelabs.com/reference/javascript-runtime/) с соответствующей совместимостью.
* Загружать можно только модули с URL из списка разрешённых. Их необходимо добавить в раздел **External requests**.

  External requests обеспечивают исходящие сетевые подключения из вашей среды Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с функциями приложений и функциями в Dashboards, Notebooks и Automations.

  1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
  2. Нажмите **New host pattern**.
  3. Добавьте доменные имена.
  4. Нажмите **Add**.

  Таким образом вы можете детально контролировать, к каким веб-сервисам могут подключаться ваши функции.
* Общий размер импортов не должен превышать 6 МБ.

### Пример — использование библиотеки XMLJSON для разбора XML-данных

Допустим, ваш бэкенд выдаёт устаревший XML-формат, но вам нужно обрабатывать данные как JSON. В таком случае вы можете использовать универсальную библиотеку XML2JSON для разбора содержимого вместо написания собственного кода.

1. Добавьте URL библиотеки XMLJSON в разрешённые **External requests**.

   External requests обеспечивают исходящие сетевые подключения из вашей среды Dynatrace к внешним сервисам. Они позволяют контролировать доступ к публичным конечным точкам из AppEngine с функциями приложений и функциями в Dashboards, Notebooks и Automations.

   1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **External requests**.
   2. Нажмите **New host pattern**.
   3. Добавьте доменные имена.
   4. Нажмите **Add**.

   Таким образом вы можете детально контролировать, к каким веб-сервисам могут подключаться ваши функции.
2. Добавьте фрагмент кода, подобный приведённому ниже, в ваше JavaScript-действие для разбора XML, преобразования его в JSON и использования в качестве входных данных для вашего действия.

```
// Load the XML parser from ESM



import xml2js from "https://esm.sh/xml2js@0.6.2";



export default async function() {



// Dummy XML, can be fetched from your back-end



const xml = "<root><list><item>Hello</item><item>World</item></list></root>";



const parser = new xml2js.Parser();



const json = await parser.parseStringPromise(xml);



return json;



}
```

CDN-площадки для пакетов, такие как [esm.sh](https://esm.sh), [unpkg](https://unpkg.com/), [JSR](https://jsr.io/), [JSDELIVER](https://www.jsdelivr.com/) или [Deno](https://deno.com/), предлагают совместимые пакеты.

Обратите внимание, что некоторые из этих библиотек зависят от внутренних компонентов Node.js или Deno, которые среда выполнения JavaScript Dynatrace не предоставляет. Совместимость с Node и Web API среды выполнения JavaScript Dynatrace описана в документации [JavaScript runtime](https://developer.dynatrace.com/reference/javascript-runtime/).

## Намеренный сбой задачи

Если вам нужно намеренно завершить задачу Run JavaScript с ошибкой, вы можете выбросить необработанное исключение.

Вот пример, который всегда завершает выполнение задачи с ошибкой.

```
export default async function() {



throw new Error()



}
```

## Доступ к полезным данным триггера события

Для рабочих процессов, запускаемых по событию, вам может потребоваться доступ к полезным данным события для реализации бизнес-логики.

Вот пример получения контекста события из выполнения рабочего процесса для рабочих процессов, запускаемых по событию.

```
import { execution } from '@dynatrace-sdk/automation-utils';



export default async function () {



const ex = await execution();



console.log( ex.params.event);



// your code goes here



}
```
