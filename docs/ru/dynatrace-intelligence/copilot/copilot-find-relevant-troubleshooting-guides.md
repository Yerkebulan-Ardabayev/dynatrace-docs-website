---
title: Discover relevant troubleshooting guides with Dynatrace Intelligence agentic and generative AI
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-find-relevant-troubleshooting-guides
scraped: 2026-03-06T21:09:55.153167
---

# Поиск релевантных руководств по устранению неполадок с помощью агентного и генеративного ИИ Dynatrace Intelligence

# Поиск релевантных руководств по устранению неполадок с помощью агентного и генеративного ИИ Dynatrace Intelligence

* Latest Dynatrace
* Руководство
* Обновлено 28 января 2026 г.

Агентный и генеративный ИИ Dynatrace Intelligence помогает быстрее решать проблемы, автоматически находя релевантные руководства по устранению неполадок, такие как блокноты (notebooks) или дашборды, созданные вашей командой.

Для сокращения среднего времени восстановления (MTTR) вы можете использовать предложения документов агентного и генеративного ИИ Dynatrace Intelligence в приложении ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, чтобы проверить, создала ли ваша команда руководства по устранению неполадок для проблем, аналогичных той, с которой вы столкнулись.

## Для кого это руководство

Данная статья предназначена для всех пользователей, которые хотят быстро и эффективно устранять активные проблемы в своей среде и выполнять их исправление.

## Чему вы научитесь

В этой статье вы узнаете, как агентный и генеративный ИИ Dynatrace Intelligence может предлагать релевантные руководства по устранению неполадок для помощи в исправлении проблем.

## Перед началом

Агентный и генеративный ИИ Dynatrace Intelligence периодически индексирует блокноты и дашборды, помеченные как руководства по устранению неполадок и предоставленные в общий доступ в среде.

* По умолчанию семантическая векторная индексация руководств происходит каждые 6 часов.
* Для того чтобы агентный и генеративный ИИ Dynatrace Intelligence проиндексировал и предложил ваш документ, необходимо предоставить к нему общий доступ для всех пользователей вашей среды. Агентный и генеративный ИИ Dynatrace Intelligence не будет индексировать или предлагать приватные документы или документы, доступные только определённым пользователям. Подробнее о предоставлении общего доступа к документам см. в разделе [Общий доступ к документам](../../discover-dynatrace/get-started/dynatrace-ui/share.md "Предоставление общего доступа к документам Dynatrace (дашборды, блокноты и лаунчпады) другим пользователям Dynatrace в вашей организации.").

### Необходимые знания

* [Обзор агентного и генеративного ИИ Dynatrace Intelligence](copilot-overview.md "Узнайте о безопасности данных и других аспектах агентного и генеративного ИИ Dynatrace Intelligence.")
* [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](copilot-getting-started.md "Узнайте, как настроить агентный и генеративный ИИ Dynatrace Intelligence.")
* [Приложение Problems](../davis-problems-app.md "Используйте приложение Problems для быстрого определения первопричины инцидентов в вашей среде.")

### Предварительные условия

* Среда Dynatrace SaaS.
* Вы выполнили настройку агентного и генеративного ИИ Dynatrace Intelligence, описанную в разделе [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](copilot-getting-started.md "Узнайте, как настроить агентный и генеративный ИИ Dynatrace Intelligence.").
* В вашей среде включены предложения документов. Включение индексации документов является частью руководства [Включение агентного и генеративного ИИ Dynatrace Intelligence в вашей среде](copilot-getting-started.md#enable-davis-copilot "Узнайте, как настроить агентный и генеративный ИИ Dynatrace Intelligence.").
* У вас есть разрешение `ALLOW davis-copilot:document-search:execute;`. Информацию о настройке разрешений см. в разделе [Разрешения в Grail](../../platform/grail/organize-data/assign-permissions-in-grail.md "Узнайте, как назначать разрешения для корзин и таблиц в Grail.").

## Получение предложений документов для исправления проблем

1. Перейдите в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems** и откройте проблему, которую необходимо решить.
2. На странице деталей проблемы выберите **Troubleshooting**. Вы сможете увидеть все руководства по устранению неполадок, созданные вами для данной проблемы, а также релевантные документы, предложенные агентным и генеративным ИИ Dynatrace Intelligence.

   Агентный и генеративный ИИ Dynatrace Intelligence индексирует только документы, распознанные как руководства по устранению неполадок. Дашборды и блокноты, созданные непосредственно из ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**, автоматически распознаются как руководства по устранению неполадок и не требуют префикса `[TSG]`.

   Если вы создаёте руководство по устранению неполадок непосредственно из ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** или ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, вам необходимо добавить к названию документа префикс `[TSG]`, чтобы указать, что это руководство по устранению неполадок.

   Независимо от способа создания документа, он должен быть предоставлен в общий доступ на уровне среды для индексации агентным и генеративным ИИ Dynatrace Intelligence.
3. Необязательно: укажите ключевые слова или часть ключевого слова в поле поиска **Name** для фильтрации предложенных документов по имени.
4. Необязательно: выберите **Type** (`Notebooks`, `Dashboards`) для фильтрации предложенных документов по типу. По умолчанию для предложений документов выбраны оба типа.
5. Нажмите **View ...** на документе, который хотите просмотреть. Это действие перенаправит вас к руководству по устранению неполадок для дальнейшего расследования.

## Прикрепление документов к проблеме

Когда вы создаёте документ со страницы деталей проблемы, он автоматически прикрепляется к этой конкретной проблеме. Прикреплённые документы не включаются в список предложенных документов. Вместо этого руководства TSG связываются с проблемой, из которой они были созданы. Это гарантирует, что документы, созданные в контексте проблемы, остаются привязанными, и предотвращает сценарии, когда ИИ может исключить их из списка предложений из-за недостаточного сходства.

Документы прикрепляются к проблемам путём установки поля `id` в хранилище документов. Шаблон, используемый для прикрепления к проблеме, состоит из:

* Строки `problem-TSG`.
* Дефиса `-`.
* Идентификатора проблемы (`event.id` в записи проблемы Grail).
* Дефиса `-`.
* Случайного UUID, представленного строкой.

Общий шаблон показан в примере ниже:

`problem-TSG-{problem_ID}-{random-UUID}`

Поскольку символ подчёркивания `_`, присутствующий в идентификаторе проблемы, не поддерживается идентификатором документа, его необходимо заменить дефисом `-`, как показано в примере ниже:

`problem-TSG-1589269324049748129-1747888020000V2-225b65bd-ab67-4efe-9d71-742de9b87387`

Случайный UUID, добавляемый в конце шаблона, обеспечивает уникальность каждого документа и позволяет прикреплять несколько документов к одной и той же проблеме без конфликтов.

Прикрепление документов к проблемам позволяет добавлять дополнительные результаты анализа и доменные знания непосредственно к обнаруженным проблемам. Вы можете прикрепить документ к проблеме через рабочие процессы (Workflows) или API для бесшовных внешних интеграций.

### Создание и прикрепление блокнота к обнаруженной проблеме через Workflows

С помощью действия JavaScript в рабочем процессе вы можете автоматически создавать и прикреплять документ (блокнот или дашборд) с результатами доменного анализа к обнаруженной проблеме.

1. Перейдите в **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") и нажмите кнопку создания нового рабочего процесса.
2. Выберите предпочитаемый тип триггера.
3. Нажмите **Add task**.
4. В разделе **Choose action** выберите **Run JavaScript**.
5. В разделе **Input** введите следующий скрипт:

   ```
   import { documentsClient } from "@dynatrace-sdk/client-document";



   import { credentialVaultClient } from '@dynatrace-sdk/client-classic-environment-v2';



   import { execution } from '@dynatrace-sdk/automation-utils';



   function generateGUID() {



   return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {



   const r = Math.random() * 16 | 0, v = c === 'x' ? r : (r & 0x3 | 0x8);



   return v.toString(16);



   });



   }



   export default async function () {



   const ex = await execution();



   const problem_event = ex.params.event;



   var problem_id = problem_event['event.id'];



   problem_id = problem_id.replace('_', '-'); // Replace the unsupported character



   // Create a new Notebook and pin it to the triggering problem



   try {



   const notebookContent = {



   defaultTimeframe: { from: "now()-2h", to: "now()" },



   defaultSegments: [],



   sections: [



   {"id":"19ebed94-69a9-4a6e-b392-7bb7b0deb330","type":"markdown","markdown":"# Domain Analysis Results\n\nHere goes the external, domain-specific analysis results"}



   ],



   };



   const generatedNotebook = await documentsClient.createDocument({



   body: {



   name: "[TSG] Domain Analysis Results",



   type: "notebook",



   description: "A notebook containing domain specific analysis results",



   id: "problem-TSG-" + problem_id + "-" + generateGUID(),



   content: new Blob([JSON.stringify(notebookContent)], { type: "application/json" }),



   },



   });



   // Make the document public



   const updated = await documentsClient.updateDocument({



   id: generatedNotebook.id,



   optimisticLockingVersion: generatedNotebook.version,



   body: {



   isPrivate: false,



   }



   })



   } catch (error) {



   console.error("Error creating notebook:", error);



   }



   return { };



   }
   ```

После того как созданный блокнот будет прикреплён к обнаруженной ИИ проблеме, вы сможете увидеть его в разделе устранения неполадок. Документ также будет предлагаться вам для аналогичных проблем в будущем.

![Пример результатов анализа в приложении Problems.](https://dt-cdn.net/images/problems-analysis-results-2147-303c6e5b9b.png)

## Связанные темы

* [Обзор агентного и генеративного ИИ Dynatrace Intelligence](copilot-overview.md "Узнайте о безопасности данных и других аспектах агентного и генеративного ИИ Dynatrace Intelligence.")
* [Начало работы с агентным и генеративным ИИ Dynatrace Intelligence](copilot-getting-started.md "Узнайте, как настроить агентный и генеративный ИИ Dynatrace Intelligence.")
* [Приложение Problems](../davis-problems-app.md "Используйте приложение Problems для быстрого определения первопричины инцидентов в вашей среде.")
