---
title: Настройка XHR для устаревших версий Internet Explorer
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie
scraped: 2026-05-12T11:34:45.977116
---

# Настройка XHR для устаревших версий Internet Explorer

# Настройка XHR для устаревших версий Internet Explorer

* How-to guide
* 2-min read
* Updated on Apr 03, 2024

Dynatrace RUM JavaScript использует *слушателей свойств* (property listeners) для определения момента полной инициализации фреймворка (подробнее о слушателях свойств см. на [сайте Mozilla](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)). Эта техника позволяет Dynatrace автоматически инструментировать ряд функций фреймворка, что необходимо для захвата и корреляции веб-запросов и пользовательских действий. Однако слушатели свойств недоступны в версиях Internet Explorer 8 и более ранних. Самым ранним автоматическим событием инициализации будет окончание события `onload`, к которому фреймворки, как правило, уже завершают инициализацию. В большинстве случаев этого достаточно, но иногда компоненты фреймворка используются в процессе события `onload`. Для захвата этих вызовов функций необходимо вручную вызвать начальную процедуру RUM JavaScript Dynatrace. Для большинства фреймворков достаточно добавить небольшой JavaScript-сниппет сразу после тега скрипта фреймворка. Для AngularJS и Prototype потребуются дополнительные действия.

Начиная с RUM JavaScript версии 1.293 [поддержка Internet Explorer 11 прекращена](/managed/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

Рассмотрите следующий общий пример, чтобы понять, где и как добавлять сниппет кода. Значение-заполнитель `Framework` необходимо заменить на реальные имена фреймворков.

**Пример размещения сниппета**

```
<head>



<meta...></meta>



<script type="text/javascript" src="/ruxitagentjs_....."></script>



<script type="text/javascript" src="Framework.js"></script>



<script type="text/javascript">window.dT_&&dT_.initFramework&&dT_.initFramework();</script>



<script>/* other scripts */</script>



</head>
```

## Модули обнаружения Ajax, требующие сниппетов:

### AngularJS

Этот фреймворк поставляется в комплекте с jqLite — минимальной версией jQuery. Необходимо, чтобы агент инициализировался сразу после завершения инициализации jqLite. Для отладочной версии AngularJS сниппет необходимо вставить непосредственно перед `jqLite(document).ready`. На скриншоте ниже показано место вставки в минифицированной версии AngularJS `(angular.min.js)`.

**Angular Snippet**

`window.dT_&&dT_.initAngular&&dT_.initAngular();`

![Xhr confi 1](https://dt-cdn.net/images/xhr-confi-1-1234-051d10abfc.png)

Xhr confi 1

### Dojo

Вставьте сниппет после тега скрипта `dojo.js`.

**Dojo Snippet**

`window.dT_&&dT_.initDojo&&dT_.initDojo();`

### ExtJS

Вставьте сниппет после тега скрипта `ext-all.js`.

**ExtJS Snippet**

`window.dT_&&dT_.dtInitExtJS&&dT_.dtInitExtJS();`

### jQuery

Вставьте сниппет после тега скрипта `jquery.js`.

**jQuery Snippet**

`window.dT_&&dT_.initJQuery&&dT_.initJQuery();`

### MooTools

Вставьте сниппет после тега скрипта `mootools.core.js`.

**MooTools Snippet**

`window.dT_&&dT_.initMooTools&&dT_.initMooTools();`

### Prototype

Вставьте сниппет перед вызовом `Ajax.Updater` в файле `prototype.js`. Расположение в файле prototype показано на скриншоте.

**Prototype Snippet**

`window.dT_&&dT_.initPrototype&&dT_.initPrototype();`

![Xhr confi 2](https://dt-cdn.net/images/xhr-confi-2-676-9d1abd0f10.png)

Xhr confi 2