---
title: Настройка XHR для старых версий Internet Explorer в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-xhr-for-older-versions-of-ie
---

# Настройка XHR для старых версий Internet Explorer в RUM Classic

# Настройка XHR для старых версий Internet Explorer в RUM Classic

* Практическое руководство
* Чтение 2 минуты
* Обновлено 03 апр. 2024 г.

Скрипт Dynatrace RUM JavaScript использует *слушатели свойств (property listeners)* для определения точного момента полной инициализации фреймворка (подробнее о слушателях свойств можно узнать на [сайте Mozilla﻿](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperty)). Эта техника позволяет Dynatrace автоматически инструментировать несколько функций, предоставляемых фреймворком, что необходимо для захвата и корреляции веб-запросов и действий пользователей. Однако слушатели свойств недоступны в Internet Explorer 8 и более старых версиях. Самым ранним событием автоматической инициализации будет окончание события "onload", когда, скорее всего, фреймворки уже завершили инициализацию. Для большинства случаев этого достаточно, но иногда компоненты фреймворка используются во время события onload. Чтобы захватить эти вызовы функций, нужно вручную вызвать начальную процедуру Dynatrace RUM JavaScript. Для большинства фреймворков достаточно добавить небольшой фрагмент JavaScript сразу после тега script фреймворка. Для AngularJS и Prototype требуются дополнительные усилия.

Начиная с версии RUM JavaScript 1.293 [прекращена поддержка Internet Explorer 11](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-javascript-version#rum-javascript-for-ie "Control the RUM JavaScript version used to monitor your applications").

Посмотрите на следующий общий пример, чтобы увидеть, где и как нужно добавить фрагмент кода. Значение-заполнитель `Framework` нужно заменить на фактические названия фреймворков.

**Пример расположения фрагмента**

```
<head>



<meta...></meta>



<script type="text/javascript" src="/ruxitagentjs_....."></script>



<script type="text/javascript" src="Framework.js"></script>



<script type="text/javascript">window.dT_&&dT_.initFramework&&dT_.initFramework();</script>



<script>/* other scripts */</script>



</head>
```

## Модули Ajax Detection, требующие фрагментов кода:

### AngularJS

Этот фреймворк поставляется вместе с jqLite, минимальной версией jQuery. Необходимо, чтобы агент инициализировался сразу после завершения инициализации jqLite. Для отладочной версии AngularJS фрагмент нужно вставить прямо перед `jqLite(document).ready`. На скриншоте ниже показано, куда его нужно вставить в минифицированной версии AngularJS `(angular.min.js)`.

**Фрагмент Angular**

`window.dT_&&dT_.initAngular&&dT_.initAngular();`

![Xhr confi 1](https://dt-cdn.net/images/xhr-confi-1-1234-051d10abfc.png)

Xhr confi 1

### Dojo

Вставить фрагмент после тега script `dojo.js`.

**Фрагмент Dojo**

`window.dT_&&dT_.initDojo&&dT_.initDojo();`

### ExtJS

Вставить фрагмент после тега script `ext-all.js`.

**Фрагмент ExtJS**

`window.dT_&&dT_.dtInitExtJS&&dT_.dtInitExtJS();`

### jQuery

Вставить фрагмент после тега script `jquery.js`.

**Фрагмент jQuery**

`window.dT_&&dT_.initJQuery&&dT_.initJQuery();`

### MooTools

Вставить фрагмент после тега script `mootools.core.js`.

**Фрагмент MooTools**

`window.dT_&&dT_.initMooTools&&dT_.initMooTools();`

### Prototype

Вставить фрагмент перед вызовом `Ajax.Updater` в файле `prototype.js`. Расположение в файле prototype показано на скриншоте.

**Фрагмент Prototype**

`window.dT_&&dT_.initPrototype&&dT_.initPrototype();`

![Xhr confi 2](https://dt-cdn.net/images/xhr-confi-2-676-9d1abd0f10.png)

Xhr confi 2