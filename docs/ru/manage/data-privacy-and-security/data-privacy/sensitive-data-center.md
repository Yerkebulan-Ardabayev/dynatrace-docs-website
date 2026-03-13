---
title: Центр конфиденциальных данных
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center
scraped: 2026-03-05T21:34:45.103522
---

# Центр конфиденциальных данных

# Центр конфиденциальных данных

* Последняя версия Dynatrace
* Приложение
* Чтение: 9 мин
* Обновлено 21 января 2026 г.

## Предварительные требования

### Разрешения

В следующей таблице описаны необходимые разрешения.

storage:logs:read

Позволяет приложению выполнять запросы к логам

storage:logs:write

Позволяет приложению записывать логи аудита конфиденциальности

storage:buckets:read

Позволяет приложению получать список бакетов Grail

state:app-states:read

Позволяет приложению читать данные запросов

state:app-states:write

Позволяет приложению сохранять данные запросов

state:app-states:delete

Позволяет приложению удалять политики запросов

state:user-app-states:read

Позволяет приложению читать пользовательскую конфигурацию

state:user-app-states:write

Позволяет приложению сохранять пользовательскую конфигурацию

iam:service-users:use

Позволяет приложению обрабатывать запросы с использованием сервисного пользователя

email:emails:send

Позволяет приложению отправлять обновления статуса запросов

## Перед началом работы

Перед использованием ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** необходимо выполнить некоторые одноразовые настройки.

### Создание сервисного пользователя

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** использует сервисного пользователя для продолжения обработки сканирований и запросов, пока вы не используете приложение. См. [Создание сервисных пользователей](../../identity-access-management/user-and-group-management/access-service-users.md#create-service-users "Service users"), чтобы узнать, как создать сервисного пользователя. Следуйте приведённым ниже инструкциям для настройки сервисного пользователя:

1. Назовите сервисного пользователя `sensitive-data-center`. Имя должно совпадать точно.
2. Создайте политику с приведённым ниже определением, чтобы предоставить сервисному пользователю необходимые разрешения.
3. Создайте группу для назначения политики (например, `sensitive-data-center-service-users`) и назначьте сервисного пользователя в эту группу. Подробнее см. [Создание политик на основе сервисного пользователя](../../identity-access-management/user-and-group-management/access-service-users.md#policy "Service users").
4. Этот пользователь также должен быть назначен в группу `sensitive-data-center-users`, определённую в следующем разделе.

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:records:delete, storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:system:read, storage:logs:read, storage:events:read, storage:bizevents:read, storage:metrics:read, storage:spans:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read, document:documents:write, document:direct-shares:write, document:documents:delete, document:trash.documents:delete;



ALLOW automation:workflows:read, automation:workflows:write;
```

Если вы ранее использовали **Privacy Rights**, переименуйте сервисного пользователя `privacy-rights` в `sensitive-data-center` вместо создания нового. Обратите внимание, что необходимые разрешения изменились, и вам также нужно их обновить. Переименование сервисного пользователя позволяет ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** автоматически очистить рабочий процесс, использовавшийся **Privacy Rights**. В качестве альтернативы администратор Workflows может удалить его вручную.

### Группа `sensitive-data-center-users`

Назначайте пользователей в эту группу, если хотите, чтобы они могли создавать запросы и сканирования. Для просмотра всех совпадающих данных для запросов и сканирований этим пользователям необходим неограниченный доступ к данным в [Grail](../../../platform/grail/dynatrace-grail.md "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."). Для корректной работы ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** имя группы должно совпадать точно, и группе должна быть назначена [политика](../../identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") со следующими разрешениями:

```
ALLOW app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW app-engine:functions:run;



ALLOW state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW state:user-app-states:read, state:user-app-states:write, state:user-app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



ALLOW iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";



ALLOW iam:users:read, iam:groups:read;



ALLOW storage:logs:write, storage:events:write;



ALLOW storage:fieldsets:read, storage:logs:read, storage:bizevents:read, storage:buckets:read;



ALLOW email:emails:send;



ALLOW document:documents:read;



ALLOW automation:workflows:read, automation:workflows:write;
```

Замените значение-заполнитель для `iam:service-user-email` на адрес электронной почты вашего сервисного пользователя `sensitive-data-center`. Чтобы найти адрес электронной почты сервисного пользователя:

1. В Dynatrace перейдите в [Управление учётной записью](../../account-management.md "Manage your Dynatrace license, accounts, platform adoption, and environment health.").
2. Выберите **Identity & access management** > **Service users**. Вы увидите обзорную таблицу со всеми вашими сервисными пользователями.
3. В столбце **Actions** выберите > **Edit**.
4. Адрес электронной почты сервисного пользователя отображается вверху.

Если вы ранее использовали **Privacy Rights**, эта группа эквивалентна группе `Privacy Rights request assignees`. Вы можете изменить имя группы и использовать ту же группу повторно, но обратите внимание, что необходимо добавить дополнительные разрешения в политику. Эти разрешения поддерживают функциональность Sensitive Data Scanner, которая в настоящее время доступна в рамках [программы предварительного доступа](../../../../common/whats-new/preview-releases.md "Learn about our Preview releases and how you can participate in them.") в ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.

### Группа `sensitive-data-center-admins`

Назначайте пользователей в эту группу, если хотите, чтобы они могли утверждать запросы и удалять данные из Grail. Все пользователи, назначенные в эту группу, также должны быть назначены в группу `sensitive-data-center-users`. Для корректной работы ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** имя группы должно совпадать точно, и группе должна быть назначена [политика](../../identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt.md "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.") со следующим разрешением:

```
ALLOW storage:records:delete;
```

Если вы ранее использовали **Privacy Rights**, эта группа эквивалентна группе `Privacy Rights request reviewers`. Вы можете изменить имя группы и использовать ту же группу повторно, но обратите внимание, что политика изменилась.

### Настройка журнала аудита

По умолчанию логи аудита сохраняются в бакет `default_logs`. Чтобы изменить это, вы можете создать бакет `privacy_audit` для назначения логов аудита. Имя должно совпадать точно. Вы можете настроить период хранения в соответствии с вашими потребностями и ограничить доступ к бакету с помощью политик IAM. Также необходимо [настроить назначение бакетов](../../../analyze-explore-automate/logs/lma-bucket-assignment.md "Your log data can be stored in data retention buckets based on specific retention periods."), чтобы логи, соответствующие `log.source == "Sensitive Data Center"`, назначались в бакет `privacy_audit`.

### Ограничение доступа

Поскольку конфиденциальные данные видны в ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, мы рекомендуем ограничить доступ для пользователей, которым не нужно создавать или рассматривать запросы и сканирования. Чтобы запретить пользователям доступ к ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, вы можете назначить их в группу со следующей политикой:

```
DENY app-engine:apps:run WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state:app-states:read, state:app-states:write, state:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY state-management:app-states:delete WHERE shared:app-id = 'dynatrace.sensitive.data.center';



DENY iam:service-users:use WHERE iam:service-user-email = "YOUR-SERVICE-USER-EMAIL-HERE";
```

Также следует запретить доступ на чтение логов аудита в бакетах `default_logs` или `privacy_audit` (в зависимости от выбранной конфигурации журнала аудита).

## Начало работы

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** позволяет вам обрабатывать и управлять запросами клиентов, связанными с правами субъектов данных в соответствии с применимыми законами о защите данных (например, GDPR и CCPA/CPRA).

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** помогает вам:

* [Экспортировать персональные данные](sensitive-data-center/export-personal-data.md "Export personal data with Sensitive Data Center export requests."): Просмотр и экспорт персональных данных, относящихся к конкретному конечному пользователю.
* [Удалить персональные данные](sensitive-data-center/delete-personal-data.md "Delete personal data with Sensitive Data Center deletion requests."): Просмотр и удаление персональных данных, относящихся к конкретному конечному пользователю.
* [Очистить данные](sensitive-data-center/cleanup-data.md "Clean up data with Sensitive Data Center cleanup requests."): Удаление ошибочно загруженных данных за определённый период времени.
* [Запланировать сканирования](sensitive-data-center/create-scheduled-scan.md "Create a scheduled scan to maintain personal data with Sensitive Data Center."): Создание сканирований для ошибочно загруженных конфиденциальных данных, таких как номера кредитных карт и IBAN, с использованием Sensitive Data Scanner. Эта функциональность доступна только в рамках [предварительного доступа](../../../../common/whats-new/preview-releases.md "Learn about our Preview releases and how you can participate in them.").

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** в настоящее время поддерживает экспорт, удаление и очистку логов Grail. Другие типы данных не поддерживаются.

![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** использует модель многостороннего контроля доступа для защиты ваших данных. Это требует настройки политик, групп и сервисного пользователя перед первым использованием приложения. Подробнее см. в разделе [Предварительные требования](#prerequisites).

Мы рекомендуем ограничить доступ к приложению, состоянию приложения, сервисному пользователю и логам аудита небольшой группой доверенных пользователей. Сервисный пользователь имеет обширные разрешения и может быть ошибочно или намеренно использован не по назначению, например, для удаления большого объёма данных. Пользователи с доступом к состоянию приложения могут изменять запросы, даже если у них нет доступа к пользовательскому интерфейсу приложения. Чтобы узнать, как ограничить доступ, см. [Предварительные требования](#prerequisites).

![Создание запроса для просмотра и экспорта персональных данных конкретного конечного пользователя. Обзор включает детали всех запросов, включая соответствующий идентификатор пользователя, исполнителей и рецензентов, текущий статус каждого запроса, а также установленный срок выполнения. Логи аудита и политики запросов можно просматривать и управлять ими с этой страницы.](https://cdn.hub.central.dynatrace.com/hub/hub1_DVwrUOD.png)![В форме запроса на экспорт вы указываете данные пользователя, такие как тип пользователя, идентификатор пользователя для поиска совпадающих данных в Grail, а также область поиска в Grail (временной период и бакеты логов).](https://cdn.hub.central.dynatrace.com/hub/hub3_qr80Yha.png)![Для каждого созданного запроса возвращаются данные, совпадающие с выполненным запросом, которые можно просмотреть по количеству записей логов, объёму, месту хранения данных, а также количеству систем. Рецензент может затем утвердить или отклонить экспорт этих данных.](https://cdn.hub.central.dynatrace.com/hub/hub4-final.png)

1 из 3 — Создание запроса для просмотра и экспорта персональных данных конкретного конечного пользователя. Обзор включает детали всех запросов, включая соответствующий идентификатор пользователя, исполнителей и рецензентов, текущий статус каждого запроса, а также установленный срок выполнения. Логи аудита и политики запросов можно просматривать и управлять ими с этой страницы.

## Сценарии использования

* Удобная фильтрация, запрос и просмотр данных, обработанных для конкретного конечного пользователя в Grail.
* Экспорт персональных данных конкретного конечного пользователя для ответа на запрос о доступе (например, право на доступ в GDPR).
* Удаление персональных данных конкретного конечного пользователя для выполнения запроса на удаление (например, право на удаление в GDPR).
* Очистка ошибочно загруженных данных за определённый период времени.

## Лучшие практики

Для ограничения области запросов:

* Используйте минимально возможный временной период и выбирайте только соответствующие бакеты.
* Убедитесь, что вы не экспортируете персональные данные других лиц или конфиденциальные данные.
* Используйте [политики](sensitive-data-center/create-policy.md "Create a policy to enrich or filter request results with Sensitive Data Center."), чтобы обеспечить соблюдение политик вашей организации в отношении конфиденциальных данных.
* Минимизируйте количество логов, которые вы экспортируете/удаляете, чтобы упростить проверку данных.

## Часто задаваемые вопросы

Я вижу баннер с сообщением о неправильной настройке разрешений, что мне делать?

Если вы видите баннер с сообщением о неправильной настройке разрешений, убедитесь, что:

1. Разрешения правильно настроены для сервисного пользователя. Подробнее см. [Предварительные требования](#prerequisites).
2. Простой рабочий процесс, используемый приложением, не был ошибочно удалён или отключён. Пользователи с разрешением `automation:workflows:admin` могут просматривать и редактировать рабочий процесс в **Workflows** после включения режима администратора. Рабочий процесс должен быть включён по расписанию и включать действие **Process deletion requests** приложения.

Я заметил, что запросы на удаление и очистку в состоянии «Утверждено» не переходят в состояние «Обработка», что мне делать?

Если вы заметили, что запросы на удаление и очистку в состоянии **Утверждено** не переходят в состояние **Обработка**, убедитесь, что:

1. Разрешения правильно настроены для сервисного пользователя. Подробнее см. [Предварительные требования](#prerequisites).
2. Простой рабочий процесс, используемый приложением, не был ошибочно удалён или отключён. Пользователи с разрешением `automation:workflows:admin` могут просматривать и редактировать рабочий процесс в **Workflows** после включения режима администратора. Рабочий процесс должен быть включён по расписанию и включать действие **Process deletion requests** приложения.

Мой запрос находится в состоянии «Ошибка», что мне делать?

Если произошла ошибка удаления, ваш запрос переходит в состояние **Ошибка**. В деталях запроса будет предоставлена дополнительная информация по каждой неудавшейся задаче. Запросы на удаление и очистку обрабатываются в одной или нескольких задачах, охватывающих определённые временные периоды. Можно считать, что удаление прошло успешно для всех временных периодов, не указанных в неудавшихся задачах. Существует четыре причины, по которым задача удаления может завершиться неудачей:

1. **Недопустимый запрос:** запрос не был принят, потому что он использует [DQL, не поддерживаемый для удаления](../../../platform/grail/organize-data/record-deletion-in-grail.md "Find out how to delete records in Grail via API."), или совпадает со слишком большим количеством записей. Данные не были удалены. Вы можете решить эту проблему, создав новый запрос с изменённым запросом и повторив попытку удаления для неудавшихся временных периодов.
2. **Тайм-аут запуска:** из-за временного сбоя не удалось запустить удаление, и задача истекла по тайм-ауту. Данные не были удалены. Мы рекомендуем подождать 12 часов или более, затем создать новый запрос для неудавшихся временных периодов и повторить попытку удаления.
3. **Тайм-аут обработки:** из-за временного сбоя во время удаления задача истекла по тайм-ауту. Данные могли быть удалены частично. Мы рекомендуем подождать 12 часов или более, затем создать новый запрос для неудавшихся временных периодов и повторить попытку удаления.
4. **Внутренняя ошибка:** во время удаления произошла внутренняя ошибка. В этом маловероятном случае данные могли быть частично удалены для указанного временного периода. Пожалуйста, обратитесь в службу поддержки, чтобы мы могли помочь вам решить проблему.

Почему я получаю ошибку при утверждении запроса?

Если вы видите ошибку, либо у вас отсутствуют разрешения, либо приложение ещё не полностью настроено. Для утверждения запроса вы должны быть участником группы `sensitive-data-center-admins`. Убедитесь, что вы входите в эту группу, что сервисный пользователь `sensitive-data-center` существует, и что как группа, так и сервисный пользователь настроены в соответствии с описанием в разделе [Предварительные требования](#prerequisites). Имена должны совпадать точно.

Почему я не вижу свои логи аудита на вкладке «Журнал аудита»?

Если логи аудита не отображаются в ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, проверьте, не настроено ли назначение бакетов неправильно.

Если бакет `privacy_audit` существует, назначение бакетов должно быть настроено для маршрутизации логов аудита ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** в него, поскольку ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** запрашивает только этот бакет.

Если бакет `privacy_audit` не существует, проверьте, не назначают ли другие правила назначения ошибочно логи аудита ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** в другой бакет, отличный от `default_logs`. Если это не так, то объём загрузки логов слишком велик для использования `default_logs`, и вам необходимо настроить пользовательский бакет `privacy_audit` (см. [Предварительные требования](#prerequisites)).

Я ранее использовал Privacy Rights. Что с ним произошло?

**Privacy Rights** был заменён на ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**, который предлагает ту же функциональность запросов на права конфиденциальности в сочетании с дополнительными функциями для управления конфиденциальными данными. Для поддержки этих функций требуются новые группы и политики IAM, поэтому необходима дополнительная одноразовая настройка. Для клиентов, которые ранее использовали **Privacy Rights**, данные запросов сохраняются в **Privacy Rights**, но запросы и политики больше не могут быть созданы.

Почему я вижу неудавшиеся сканирования?

Наиболее вероятная причина неудавшихся сканирований — неправильно настроенные разрешения для сервисного пользователя. Проверьте, что имя сервисного пользователя, две назначенные группы и политики, назначенные этим группам, точно соответствуют описанию в разделе [Предварительные требования](#prerequisites).

## Учебные модули

[01Создание политики в Sensitive Data Center

* Руководство
* Создание политики для обогащения или фильтрации результатов запросов с помощью Sensitive Data Center.](sensitive-data-center/create-policy.md)[02Экспорт персональных данных в Sensitive Data Center

* Руководство
* Экспорт персональных данных с помощью запросов на экспорт Sensitive Data Center.](sensitive-data-center/export-personal-data.md)[03Просмотр логов аудита в Sensitive Data Center

* Руководство
* Просмотр логов аудита Sensitive Data Center.](sensitive-data-center/review-audit-logs.md)[04Удаление персональных данных в Sensitive Data Center

* Руководство
* Удаление персональных данных с помощью запросов на удаление Sensitive Data Center.](sensitive-data-center/delete-personal-data.md)[05Очистка данных в Sensitive Data Center

* Руководство
* Очистка данных с помощью запросов на очистку Sensitive Data Center.](sensitive-data-center/cleanup-data.md)[06Создание запланированного сканирования в Sensitive Data Center

* Руководство
* Создание запланированного сканирования для поддержания персональных данных с помощью Sensitive Data Center.](sensitive-data-center/create-scheduled-scan.md)
