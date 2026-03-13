---
title: OneAgent SDK
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk
scraped: 2026-03-06T21:16:36.669068
---

# OneAgent SDK

# OneAgent SDK

* Latest Dynatrace
* 2-min read
* Published Mar 01, 2018

Dynatrace предоставляет широкие возможности мониторинга для практически всех популярных языков и технологий, включая Java, .NET, Node.js, PHP и Golang. Подробную информацию обо всех поддерживаемых технологиях см. на [странице поддерживаемых технологий](/docs/ingest-from/technology-support "Ознакомьтесь с техническими подробностями поддержки Dynatrace для конкретных платформ и фреймворков разработки.").

Dynatrace OneAgent SDK позволяет вам выполнять ручную инструментацию приложения для расширения сквозной видимости для фреймворков и технологий, для которых пока нет доступного модуля кода. С помощью SDK вы получаете полный доступ ко всем функциям анализа и мониторинга, включая автоматическое определение базовых показателей и анализ первопричин на основе ИИ.

Dynatrace OneAgent SDK доступен на GitHub. Отзывы и запросы на добавление функций можно подавать непосредственно на GitHub.

## Что можно делать с Dynatrace OneAgent SDK

С помощью Dynatrace OneAgent SDK вы можете:

* Трассировать входящие и исходящие удалённые вызовы
* Трассировать запросы к базам данных
* Трассировать входящие и исходящие веб-запросы
* Трассировать асинхронное выполнение внутри процесса
* Трассировать очереди и сообщения
* Захватывать атрибуты запросов

Со временем в OneAgent SDK будет добавлено больше функциональности. Наборы функций немного различаются для каждой языковой реализации.

## Что нельзя делать с Dynatrace OneAgent SDK

С помощью Dynatrace OneAgent SDK нельзя:

* Создавать пользовательские сессии и действия пользователей: эта функциональность предоставляется [Dynatrace OpenKit](/docs/ingest-from/extend-dynatrace/openkit "Узнайте, как инструментировать приложение с помощью OpenKit, как использовать методы Dynatrace OpenKit API и многое другое.")

## Как использовать Dynatrace OneAgent SDK

Поскольку OneAgent SDK работает в тандеме с Dynatrace OneAgent, дополнительная настройка не требуется.

Основные требования для использования OneAgent SDK:

* Доступ к исходному коду приложения (и готовность вносить изменения в код)
* Поскольку OneAgent SDK напрямую взаимодействует с OneAgent, OneAgent (минимальная требуемая версия OneAgent зависит от версии SDK) должен быть установлен и запущен на хосте, где выполняется приложение. Поддерживаются контейнерные среды.
* OneAgent в режиме мониторинга полного стека.

OneAgent автоматически определяет, что ваше приложение инструментировано с помощью OneAgent SDK, и немедленно начинает его мониторинг. После установки OneAgent на хосте требуется перезапуск приложения.

## OneAgent SDK на GitHub

Dynatrace OneAgent SDK публикуется непосредственно на GitHub вместе с технической документацией. Для получения подробного обзора текущих функций OneAgent SDK перейдите по следующим ссылкам:

* [Языко-независимая документация по API и концепциям SDK](https://github.com/Dynatrace/OneAgent-SDK)
* [OneAgent SDK для Java](https://github.com/Dynatrace/OneAgent-SDK-for-Java)
* [OneAgent SDK для C/C++](https://github.com/Dynatrace/OneAgent-SDK-for-C)
* [OneAgent SDK для Node.js](https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs)
* [OneAgent SDK для .NET](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet)
* [OneAgent SDK для Python](https://github.com/Dynatrace/OneAgent-SDK-for-Python)
* [OneAgent SDK для PHP](https://github.com/Dynatrace/OneAgent-SDK-for-PHP)

## Дополнительное чтение

* [Блог: расширение анализа первопричин на основе ИИ с помощью OneAgent SDK](https://www.dynatrace.com/news/blog/extend-ai-based-root-cause-analysis-with-oneagent-sdk)

## Связанные темы

* [Инструментация через OneAgent SDK для Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Узнайте, как расширить мониторинг пользовательского опыта мобильных приложений на Android с помощью OneAgent SDK.")
* [OneAgent SDK для iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Расширьте мониторинг пользовательского опыта мобильных приложений с помощью OneAgent SDK для iOS.")
* [OneAgent](/docs/platform/oneagent "Узнайте о возможностях мониторинга OneAgent.")
* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Изучите важные концепции, связанные с OneAgent, и узнайте, как установить и эксплуатировать OneAgent на различных платформах.")
