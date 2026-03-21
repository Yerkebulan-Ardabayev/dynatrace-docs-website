---
title: Связь пользовательских взаимодействий с функциями и UI-компонентами
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions/features-and-components
scraped: 2026-03-05T21:30:50.126179
---

* Последняя Dynatrace

Ранний доступ

Новый функционал RUM Experience позволяет связывать пользовательские взаимодействия с функциями и UI-компонентами путём добавления специальных атрибутов в ваш HTML. Этот всеобъемлющий контекст взаимодействия обеспечивает мощные запросы и углублённый анализ того, как пользователи взаимодействуют с UI и функциональностью вашего приложения.

## Связь пользовательских взаимодействий с функциями

Используйте атрибут `data-dt-features` для связи пользовательских взаимодействий на HTML-элементе с одной или несколькими конкретными функциями продукта. При пользовательских взаимодействиях захваченные функции доступны в поле `ui_element.features`; см. [Пользовательские взаимодействия](../../../../../../semantic-dictionary/model/rum/user-events/user-interactions.md). Элементы наследуют функции от своих предков, обеспечивая комплексное отслеживание функций.

### Сценарии использования

Атрибут `data-dt-features` позволяет:

* Отслеживать пользовательские взаимодействия по функциям — например, «поиск», «оформление заказа», «навигация».
* Группировать связанные UI-компоненты на странице.
* Анализировать поведение пользователей по функциональным областям.
* Создавать панели и отчёты на основе функций.

### Формат

Значение атрибута `data-dt-features` — это список имён функций через запятую, где функция может быть любой строкой. Функции чувствительны к регистру — например, «Search» и «search» — это разные функции.

Примеры

```
<!-- Single feature -->


<div data-dt-features="search">


<input type="text" placeholder="Search...">


<button>Search</button>


</div>


<!-- Multiple features -->


<nav data-dt-features="navigation,sidebar">


<a href="/home">Home</a>


<a href="/products">Products</a>


<a href="/about">About</a>


</nav>
```

### Наследование функций

Наследование функций работает путём сбора значений функций от всех элементов-предков в порядке сверху вниз. Все унаследованные функции объединяются в один массив, дубликаты удаляются с сохранением первого вхождения. Итоговый список отражает иерархию DOM, начиная с самого удалённого элемента-предка и заканчивая самим элементом.

Примеры

```
<div data-dt-features="shop,product-catalog">


<div data-dt-features="filters">


<button>Price</button>          <!-- ui_element.features: ["shop", "product-catalog", "filters"] -->


<button>Brand</button>          <!-- ui_element.features: ["shop", "product-catalog", "filters"] -->


</div>


<div data-dt-features="results">


<div>Product 1</div>            <!-- ui_element.features: ["shop", "product-catalog", "results"] -->


<div>Product 2</div>            <!-- ui_element.features: ["shop", "product-catalog", "results"] -->


</div>


</div>


<div data-dt-features="app,main">


<div data-dt-features="sidebar,navigation">


<div data-dt-features="menu,navigation">


<button>Click</button>  <!-- ui_element.features: ["app", "main", "sidebar", "navigation", "menu"] -->


</div>


</div>


</div>
```

### Пример DQL

Следующий DQL-запрос генерирует временной ряд, показывающий для каждой функции количество сессий, включающих хотя бы одно взаимодействие с этой функцией.

```
fetch user.events


| filter isNotNull(ui_element.features)


| expand ui_element.features


| makeTimeseries countDistinct(dt.rum.session.id), by: {ui_element.features}, interval: 1d
```

## Связь пользовательских взаимодействий с UI-компонентами

Используйте атрибут `data-dt-component` для связи пользовательских взаимодействий на HTML-элементе с одним или несколькими UI-компонентами, такими как выбор даты или календарь. Значения компонентов наследуются от всех элементов-предков и собираются в порядке сверху вниз, формируя путь через дерево компонентов. В захваченном пользовательском взаимодействии собранные компоненты доступны в поле `ui_element.components`; см. [Пользовательские взаимодействия](../../../../../../semantic-dictionary/model/rum/user-events/user-interactions.md).

### Сценарии использования

Атрибут `data-dt-component` позволяет:

* Определять, где происходят пользовательские взаимодействия в компонентных UI-фреймворках, таких как React, Vue и Angular.
* Понимать путь компонента от корня до элемента взаимодействия.
* Различать идентичные элементы в разных контекстах компонентов.
* Отлаживать и анализировать взаимодействия во вложенных структурах компонентов.

### Формат и наследование

Значение `data-dt-component` — это строка, представляющая компонент. Компоненты собираются сверху вниз от всех предков, формируя массив, представляющий путь через дерево компонентов. Пустые значения или значения из пробелов игнорируются.

Пример (React JSX)

```
<App data-dt-component="App">


<Container data-dt-component="Container">


<AuthProvider data-dt-component="AuthProvider">


<Dashboard data-dt-component="Dashboard">


<Container data-dt-component="Container">


<Card data-dt-component="Card">


<Button data-dt-component="Button">Save</Button>


{/* ui_element.components: ["App", "Container", "AuthProvider", "Dashboard", "Container", "Card", "Button"] */}


</Card>


</Container>


</Dashboard>


</AuthProvider>


</Container>


</App>
```

### Пример DQL

Следующий DQL-запрос генерирует временной ряд, показывающий, сколько разных пользователей взаимодействовали с компонентом `TimeframeSelector`. Результаты разбиваются по фронтендам.

```
fetch user.events


| expand ui_element.components


| filter ui_element.components == "TimeframeSelector"


| makeTimeseries countDistinct(dt.rum.instance.id), by: {frontend.name}, interval: 1d
```