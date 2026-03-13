---
title: Create scheduled scan in Sensitive Data Center
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-scheduled-scan
scraped: 2026-03-04T21:28:24.209852
---

# Создание запланированного сканирования в Sensitive Data Center

# Создание запланированного сканирования в Sensitive Data Center

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 16, 2025
* Preview

Вы можете настроить запланированные сканирования в ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center** для непрерывного мониторинга вашей среды на наличие конфиденциальных данных. Вы можете выбрать конкретные бакеты или всю среду для мониторинга, выбрать типы конфиденциальных данных из встроенных правил и задать периодичность запуска сканирования.

## Настройка сканирований в Sensitive Data Scanner

Чтобы создать повторяющееся сканирование для непрерывного мониторинга

1. Перейдите в ![Sensitive Data Center](https://dt-cdn.net/images/privacy-rights-highresolution-1024-fa3477e788.png "Sensitive Data Center") **Sensitive Data Center**.
2. Перейдите на вкладку **Scanner** и нажмите **Create scan**.
3. Выберите один или несколько **типов конфиденциальных данных** из списка, например адреса электронной почты, номера кредитных карт или IP-адреса.
4. Задайте интервал сканирования, выбрав периодичность в соответствии с вашими требованиями к соответствию нормативным требованиям.
5. Выберите **область бакета журналов (Log bucket scope)**, указав конкретные бакеты из списка или всю среду.
6. Необязательно: применяйте политики сканирования для уточнения области сканирования — например, для исключения известных ложноположительных результатов. Подробнее см. в разделе [Create a policy in Sensitive Data Center](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/create-policy "Create a policy to enrich or filter request results with Sensitive Data Center.").
7. Введите понятное имя для сканирования.
8. Нажмите **Create scan** для сохранения конфигурации.

Сканирование запускается автоматически с заданной периодичностью и оповещает вас при обнаружении данных, соответствующих выбранным критериям.

## Просмотр результатов сканирования

Дашборд сканера обеспечивает чёткий обзор статусов сканирований и выделяет случаи обнаружения конфиденциальных данных. Отсюда вы можете перейти к конкретному сканированию, чтобы просмотреть подробные результаты и точно понять, что было обнаружено.

Вы можете просмотреть результаты и изучить поток данных от приёма до места хранения.

В средах с большим объёмом принимаемых журналов результаты сканирования могут быть выборочными. Выборка является адаптивной и помогает снизить затраты на обработку, сохраняя точность обнаружения. Частота выборки автоматически регулируется в зависимости от текущего объёма принимаемых журналов.

## Устранение потенциальных выявлений

На основе результатов сканирования вы можете предпринять немедленные действия:

* [Настроить или скорректировать правила маскирования](/docs/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), чтобы предотвратить приём аналогичных данных.
* Изменить права доступа к хранимым данным.
* Обновить [периоды хранения данных](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").
* Использовать [функцию очистки](/docs/manage/data-privacy-and-security/data-privacy/sensitive-data-center/cleanup-data "Clean up data with Sensitive Data Center cleanup requests.") для удаления конфиденциальных данных при необходимости.
