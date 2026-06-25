---
title: Видимость на уровне кода для PHP
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/php/code-level-visibility
scraped: 2026-05-12T12:03:47.392564
---

# Видимость на уровне кода для PHP

# Видимость на уровне кода для PHP

* Чтение: 2 мин
* Опубликовано: 12 июня 2019

Видимость на уровне кода даёт представление о том, где ваш PHP-код тратит больше всего времени и потребляет больше всего CPU.

Чтобы открыть представление уровня кода для PHP

1. Перейдите в **Services**.
2. Необязательно: отфильтруйте таблицу по `Technology: PHP`.
3. Выберите сервис PHP.
   Пример: запрос PHP

   ![Dynamic requests](https://dt-cdn.net/images/php1-1595-f396bf2d41.png)

   Dynamic requests
4. Выберите **View dynamic requests**, затем выберите запрос PHP.
5. Выберите **View response time hotspots**.  
   Если вы используете FPM, выберите сервис FPM, а затем выберите **View response time hotspots**, чтобы просмотреть весь сервис или отдельный запрос.
   Пример: время отклика

   ![Response time](https://dt-cdn.net/images/php2-1620-3b68309947.png)

   Response time
6. Чтобы увидеть разбивку временных показателей запроса на уровне кода, выберите **Analyze outliers** или откройте вкладку **Response time**.
7. Чтобы просмотреть горячие точки на уровне методов в вашем PHP-коде, на странице **Response time analysis** выберите **PHP execution**.
   Пример: PHP execution

   ![PHP execution](https://dt-cdn.net/images/php3-1673-ed6ceb7e1e.png)

   PHP execution
8. Чтобы изучить потребление CPU кодом на уровне методов, откройте вкладку **CPU**, а затем выберите **View method hotspots**, где можно отобразить диаграммы **Execution time** и **Top APIs**. Также можно проверить **Call hierarchy** и **Hotspots**, чтобы оценить общий вклад каждого вызванного файла или метода.
   Пример: просмотр горячих точек методов

   ![View method hotspots](https://dt-cdn.net/images/php4-1672-5c1658871f.png)

   View method hotspots