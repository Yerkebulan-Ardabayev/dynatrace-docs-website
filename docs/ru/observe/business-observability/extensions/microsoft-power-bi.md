---
title: Microsoft Power BI
source: https://www.dynatrace.com/docs/observe/business-observability/extensions/microsoft-power-bi
scraped: 2026-03-06T21:14:50.262778
---

* Latest Dynatrace
* 2-min read
* Preview

Preview

Расширение Microsoft Power BI передаёт данные из Grail непосредственно в ваши отчёты и дашборды Microsoft Power BI, предоставляя DQL-запросы.

Стоимость выполнения DQL-запросов в Microsoft Power BI эквивалентна пользовательскому интерфейсу Dynatrace.

## Ограничения

* Только режим импорта
* Максимальный результат для DQL-запросов: 1 000 000 строк
* Максимальный результат для стандартных таблиц (BizEvents, Events, Logs, Spans): 1 000 строк

## Настройка

Для выполнения запросов и просмотра определённых таблиц в Grail необходимы разрешения в Grail.

Пример оператора политики для чтения бизнес-событий:

```
ALLOW storage:buckets:read WHERE storage:table-name = "bizevents";


ALLOW storage:bizevents:read;
```

### Подключение к Dynatrace Grail из Microsoft Power BI Desktop

Чтобы подключиться к экземпляру Dynatrace из Power Query Desktop, выполните следующие шаги.

1. Выберите **Dynatrace Grail DQL** в интерфейсе **Get Data**. Дополнительные сведения см. в разделе [Where to get data | Power Query](https://dt-url.net/x203wmh).
2. Введите вашу среду Dynatrace. Эта среда должна быть последней версии Dynatrace с включённым Grail. DQL-запрос на данном этапе не является обязательным, но рекомендуется для более сложных запросов, выходящих за рамки встроенных запросов по умолчанию.
3. Войдите в свою среду для аутентификации ваших разрешений.
4. Введите свои учётные данные во всплывающем окне.
5. После аутентификации вы увидите сообщение о том, что вы вошли в систему. Нажмите **Connect**.
6. На странице **Navigator** отображаются типы записей, доступные для выбора из Dynatrace Grail.
7. Выберите один из них, например **Logs**, и выполните DQL-запрос для получения журналов с лимитом по умолчанию в 1 000 строк. Для успешного выполнения этого запроса необходимы разрешения в среде Dynatrace.
8. В **Advanced Editor** отображается M-код, используемый коннектором.
9. Теперь вы можете вернуться к опциональному DQL-запросу из шага 2 и ввести DQL-запрос.
10. Импортируйте результаты в Microsoft Power BI.

## Связанные темы

* [Microsoft Power BI extension](https://dt-url.net/go03wp3)
