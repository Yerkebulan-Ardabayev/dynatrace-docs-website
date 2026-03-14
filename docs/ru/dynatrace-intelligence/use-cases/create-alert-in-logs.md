---
title: Создание оповещений по журналам для события журнала или сводки данных журнала
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/create-alert-in-logs
scraped: 2026-03-05T21:40:14.975184
---

# Создание оповещений журналов для события журнала или сводки данных журналов


* Latest Dynatrace
* Обучающее руководство
* Чтение: 5 мин
* Обновлено 28 января 2026 г.

Одно из применений ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** -- оповещение пользователей об аномальном поведении. Например, с помощью команды DQL `makeTimeseries` вы можете настроить пользовательское оповещение для анализа или оповещения по различным данным, таким как бизнес-события или журналы. В этом случае пользовательское оповещение запрашивает необработанные данные каждую минуту. Однако, если у вас редкие записи в журналах или если вас интересует конкретное событие журнала, вы можете использовать альтернативные решения, более эффективные по стоимости и времени.

В этом руководстве вы узнаете, как:

* Создать оповещение журнала для конкретного события журнала.
* Создать оповещение журнала для определенного периода времени.

## Предварительные требования

* Доступ к среде Dynatrace SaaS
* Установленное приложение ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**

Для сценария [Создание оповещения журнала на основе сводки данных журналов с помощью DQL](#create-log-custom-alert-with-dql) вам также потребуется:

* [Настроенные разрешения ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**](../anomaly-detection/anomaly-detection-app.md "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.")

## Создание оповещения журнала на основе конкретного события журнала

Если вы хотите отслеживать конкретное событие журнала и получать уведомления при его возникновении, вы можете создать оповещение на основе отфильтрованного запроса, чтобы избежать обработки всего необработанного журнала.

Предположим, вы хотите настроить оповещение, которое уведомляет вас каждый раз, когда в журналах NGINX фиксируется ошибка `Connection refused`. Кроме того, вы хотите извлечь из содержимого журнала следующую информацию для быстрого обзора события:

* Номер ошибки
* IP-адрес клиента
* Строка `http_request`, приводящая к ошибке.

Чтобы сэкономить время и усилия, вы можете настроить оповещение журнала вместо оповещения обнаружения аномалий. В этом случае вам не нужно создавать временной ряд. Вместо этого достаточно создать отфильтрованный запрос, который покажет только конкретное событие, например:

```
fetch logs


| filter matchesValue(process.technology, "nginx")


| filter matchesValue(loglevel, "ERROR")


| filter matchesPhrase(content, "Connection refused")


| fields timestamp,content, process.technology


| parse content, "LD '[error] ' INT:error_number '#' INT LD 'Connection refused' LD 'client:' SPACE? IPADDR:client_ip LD 'request:' SPACE? DQS:http_request"


| sort timestamp desc
```

Создание оповещения журнала не требует доступа к ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**. Вам нужно только **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events"). Подробнее о создании оповещений через **Logs** ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") см. в разделе [Настройка оповещения журнала](../../analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-events.md "Как создать и настроить проблемы и оповещения Davis на основе событий из журналов.").

## Создание оповещения журнала на основе сводки данных журналов за период времени

Если вы хотите получить обзор данных журналов за определенный период, например, если данные содержат редкие записи в журналах, вы можете использовать один из подходов:

* Создать выделенную метрику журнала.
* Использовать DQL для создания оповещения журнала на основе сводки данных журналов.

### Создание выделенной метрики журнала

Создание выделенной метрики журнала позволяет повторно использовать метрику журнала в приложениях, таких как **Dashboards** ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") и **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks"), а также создавать оповещения без дополнительных затрат.

Чтобы узнать, как создавать метрики журналов, см. [Метрики журналов](../../analyze-explore-automate/logs/lma-log-processing/lma-log-metrics.md "Создавайте метрики на основе данных журналов и используйте их в Dynatrace как любую другую метрику.").

Предположим, вы создали метрику журнала `log.conn_refused_count`, которая собирает каждую запись журнала с ошибкой `Connection refused`.

![Пример настроек анализа и оповещений для графика метрики журнала с выбранным обнаружением аномалий в приложении Notebooks.](https://dt-cdn.net/images/notebooks-log-metric-analyze-and-alert-1741-740d26f404.png)

Поскольку данные в метрике журнала содержат только необходимые журналы, вы можете создать оповещение с помощью обычной команды DQL `timeseries` и имени вашей метрики журнала в качестве параметра.

### Создание оповещения журнала на основе сводки данных журналов с помощью DQL

Использование DQL позволяет создавать сложные запросы и применять множество фильтров и условий сортировки. Этот подход дает вам больше контроля над тем, какие данные вы хотите захватить и какую информацию вы хотите видеть в своих оповещениях.

Создание оповещения журнала на основе сводки данных журналов

1. Откройте **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks").
2. Выберите **Notebook** > **New section** > **DQL**, чтобы создать новый раздел.
3. Заполните поле аналогично примеру ниже:

   ```
   fetch logs


   | filter dt.system.bucket == "{your bucket name}"


   | filter matchesPhrase(content, "Connection refused")


   | makeTimeseries count(), interval:1m
   ```
4. Необязательно: выберите **Run**, чтобы протестировать и убедиться, что ваша команда работает правильно.
5. Выберите **Options** и выберите **Analyze and alert**.
6. Включите анализатор данных Dynatrace Intelligence, если он не активен.
7. Выберите необходимый анализатор и настройте его. Подробности см. в разделе [Конфигурация обнаружения аномалий](../anomaly-detection/anomaly-detection-configuration.md "Как настроить оповещение для пропущенных измерений.").
8. Выберите **Run analysis**.
9. Когда вы будете удовлетворены результатом, выберите ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** и выберите **Anomaly Detection**.
   Это действие перенесет вас в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
10. Разверните **Create an event template** и настройте событие, вызываемое конфигурацией. Подробности см. в разделе [Шаблон события](../anomaly-detection/anomaly-detection-configuration.md#event-template "Как настроить оповещение для пропущенных измерений.").
11. Выберите **Create**.

![Пример настроек анализа и оповещений для графика метрики журнала бакета с выбранным обнаружением аномалий в приложении Notebooks.](https://dt-cdn.net/images/notebooks-bucket-log-metric-analyze-and-alert-1744-cef4fa6326.png)

Извлечение данных из бакета `default_logs` может повлечь дополнительные расходы. Если ваши журналы доступны в определенном бакете, мы рекомендуем использовать `filter dt.system.bucket == "{your bucket}"` для повышения эффективности.

Если у вас нет доступа к бакету вашей команды или отдела, вы можете создать приватный бакет, следуя документации по [назначению бакетов](../../analyze-explore-automate/logs/lma-bucket-assignment.md "Данные ваших журналов могут храниться в бакетах хранения данных на основе определенных сроков хранения.").

## Заключение

Помимо стандартных оповещений Anomaly Detection, Dynatrace предлагает другие решения, такие как:

* Создание оповещения журнала для конкретного события.
* Создание оповещения по данным журналов за определенный период времени.

Если вы выполнили эти шаги, теперь вы знаете, как создавать оповещения журналов для конкретных событий и сводки данных журналов за определенный период времени.

## Связанные темы

* [Приложение Anomaly Detection](../anomaly-detection/anomaly-detection-app.md "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.")
* [[Видео] Повышение безопасности с помощью Anomaly Detection](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Видео] Anomaly Detection и наблюдаемость данных](https://www.youtube.com/watch?v=HPQi63mQg3w)
