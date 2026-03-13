---
title: Настройка захвата пользовательских взаимодействий для веб-фронтендов
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions
scraped: 2026-03-05T21:33:14.629107
---

# Настройка захвата пользовательских взаимодействий для веб-фронтендов

# Настройка захвата пользовательских взаимодействий для веб-фронтендов

* Последняя Dynatrace
* Практическое руководство
* Обновлено 26 февраля 2026 г.

Ранний доступ

Новый функционал RUM Experience позволяет захватывать [пользовательские взаимодействия](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-interactions "Ознакомьтесь с моделью данных в основе нового функционала RUM Experience."), такие как клики и прокрутки, и превращать их в полезные инсайты:

* Вы можете просматривать все пользовательские взаимодействия, произошедшие в рамках сессии пользователя, с помощью приложения [![Users & Sessions](https://dt-cdn.net/images/users-sessions-149-f84e0b9b20.png "Users & Sessions") **Users & Sessions**](/docs/observe/digital-experience/new-rum-experience/users-and-sessions#events "Приложение Users & Sessions предоставляет информацию о путях и паттернах поведения отдельных пользователей."). Это особенно полезно для команд поддержки клиентов и разработчиков при диагностике проблем клиентов или ошибок.
* Анализ пользовательских взаимодействий через DQL позволяет понять паттерны поведения для широкого спектра сценариев использования; см. [примеры DQL](/docs/observe/digital-experience/new-rum-experience/use-cases/dql-examples#behavioral-insights "Анализ и изучение данных RUM с помощью DQL.").

В период раннего доступа к пользовательским взаимодействиям дополнительная плата за приём пользовательских взаимодействий не взимается. Запросы пользовательских взаимодействий также включены без дополнительных затрат, поскольку запросы необработанных данных DEM в настоящее время находятся в раннем доступе; см. [Расчёт потребления мониторинга цифрового опыта (DEM) — Запросы](/docs/license/capabilities/digital-experience-monitoring-query-retain/queries-dem "Узнайте, как потребляются и тарифицируются DQL-запросы, связанные с DEM.").

## Активация захвата пользовательских взаимодействий

Чтобы захватывать пользовательские взаимодействия

1. Перейдите в ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Обзор**.
2. Выберите **Web** для просмотра всех веб-фронтендов.
3. Выберите фронтенд, который хотите настроить.
4. Перейдите на вкладку **Настройки**.
5. В разделе **Включение и контроль затрат** включите **Пользовательские взаимодействия**.

## Типы пользовательских взаимодействий

В следующей таблице приведён обзор доступных типов пользовательских взаимодействий. Подробную спецификацию см. в [Пользовательские взаимодействия](/docs/semantic-dictionary/model/rum/user-events/user-interactions) в Semantic Dictionary.

## Типы пользовательских взаимодействий с явным подключением

Большинство типов пользовательских взаимодействий захватываются автоматически после [активации захвата пользовательских взаимодействий](#activate-capturing). Однако для некоторых типов взаимодействий требуется явное подключение путём добавления специальных атрибутов к соответствующим HTML-элементам. Эти атрибуты включают захват событий, но не влияют на поведение элемента.

### Focus/Blur

Для захвата пользовательских взаимодействий focus и blur добавьте атрибуты `data-dt-focus` и `data-dt-blur` к соответствующим HTML-элементам. Атрибут может быть пустым или иметь значение; и `data-dt-focus`, и `data-dt-focus="true"` являются допустимыми.

Примеры

```
<!-- Track when users focus on search -->



<input data-dt-focus type="text" placeholder="Search products...">



<!-- Monitor form field interaction -->



<form>



<input data-dt-focus name="email" type="email" placeholder="Email">



<input data-dt-focus name="password" type="password" placeholder="Password">



<button type="submit">Login</button>



</form>



<!-- Track focus on custom components -->



<div data-dt-focus tabindex="0" role="button">Custom Button</div>



<!-- Track both focus and blur for complete interaction -->



<textarea data-dt-focus data-dt-blur placeholder="Your feedback..."></textarea>



<!-- Monitor search abandonment -->



<input data-dt-focus data-dt-blur type="search" placeholder="What are you looking for?">
```

### Mouseover

Для захвата пользовательских взаимодействий mouseover добавьте атрибут `data-dt-mouse-over="<миллисекунды>"` к соответствующему HTML-элементу. Значение атрибута указывает, сколько миллисекунд пользователь должен наводить курсор на элемент, прежде чем взаимодействие будет захвачено. При выборе подходящей задержки учитывайте следующие факторы:

* Если вы хотите измерить вовлечённость для CTA (элементов призыва к действию) или карточек товаров, сколько миллисекунд должен наводить пользователь, чтобы считать наведение намеренным?
* Если ваша цель — отслеживание взаимодействий с всплывающими подсказками, какую задержку использует ваше приложение перед отображением подсказок?

Примеры

```
<!-- Track hover after 300ms (shows intent) -->



<button data-dt-mouse-over="300">



Learn More



</button>



<!-- Monitor product card interest with 500ms threshold -->



<div class="product-card" data-dt-mouse-over="500">



<img src="product.jpg">



<h3>Premium Headphones</h3>



<p>$299.99</p>



</div>



<!-- Track tooltip hover with 1 second threshold -->



<span data-dt-mouse-over="1000">



<i class="info-icon">?</i>



<div class="tooltip">Detailed information appears here</div>



</span>



<!-- Possible different thresholds for different intents -->



<nav>



<div data-dt-mouse-over="200">Products</div>      <!-- Quick hover -->



<div data-dt-mouse-over="500">Solutions</div>     <!-- Medium intent -->



<div data-dt-mouse-over="1000">Documentation</div> <!-- Strong intent -->



</nav>
```

## Кастомизация

Для дополнительного контекста вы можете добавить атрибуты в ваш HTML, которые связывают захваченные пользовательские взаимодействия с функциями и UI-компонентами; см. [Связь пользовательских взаимодействий с функциями и UI-компонентами](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions/features-and-components "Узнайте, как связывать пользовательские взаимодействия для веб-фронтендов с функциями и UI-компонентами."). Эта кастомизация обеспечивает мощные запросы и углублённый анализ того, как пользователи взаимодействуют с UI и функциональностью вашего приложения.