---
title: VS Code
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode
---

# VS Code

# VS Code

* Объяснение
* 2 мин чтения
* Обновлено 07 июл 2026

![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions**, это расширение для Visual Studio Code, которое поддерживает все аспекты разработки Extensions на Dynatrace. Найти его можно в [VS Code extensions marketplace﻿](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions).

Оно открывает доступ к готовому специализированному набору инструментов и помогает в следующем:

1. Операционная эффективность
2. Создание контента
3. Проверка контента

Можно сразу перейти к инструкциям по [началу работы](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/guides/getting-started "Set up the Dynatrace Extensions add-on for Visual Studio Code and build your first extension ready for upload in five minutes.") или продолжить чтение, чтобы узнать о некоторых возможностях.

## Возможности

### Операционная эффективность

![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions** повышает операционную эффективность при разработке расширений. В него входят следующие возможности:

* Специальные представления для управления рабочими пространствами и средами в любом масштабе
* Обзор развёрнутых расширений в нескольких средах
* Все операции с расширениями доступны прямо в редакторе:

  + Создание, сборка, подпись, загрузка и активация расширений.
  + Создание и управление конфигурациями мониторинга.
  + Создание и управление учётными данными для подписи расширений.

### Создание контента

Разработку можно ускорить, автоматически генерируя значительную часть манифеста расширения и ресурсов. Возможности включают:

* Генерацию [unified analysis pages](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.") для сущностей.
* Автодополнение кода на основе данных из среды.

* Генерацию документации, дашбордов и оповещений.
* Выполнение запросов Windows Management Instrumentation (WMI) для автоматического извлечения метрик и измерений.
* Подключение к экспортёрам Prometheus для автоматического извлечения метрик, измерений и метаданных.
* Подключение к Java-процессам для автоматического извлечения JMX-метрик и измерений.

### Проверка контента

Ошибок становится меньше, если проверять контент расширения на ранних этапах. ![Dynatrace Extensions](https://dt-cdn.net/images/dynatrace-extensions-icon-1580-5032ebda6e.png "Dynatrace Extensions") **Dynatrace Extensions** предоставляет:

* Проверку манифеста расширения на соответствие различным версиям схемы
* Дополнительную диагностику, выходящую за рамки схем расширений

* Проверку metric и entity selector на соответствие данным среды

## Поддержка

Этот проект с открытым исходным кодом опирается на отзывы и вклад сообщества и не поддерживается официально компанией Dynatrace.

По любым проблемам, вопросам и предложениям можно обращаться на [страницу issues﻿](https://github.com/dynatrace-extensions/dynatrace-extensions-vscode/issues) репозитория GitHub, в котором размещён этот проект.