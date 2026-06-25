---
title: Поддержка source map для анализа ошибок JavaScript
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/source-map-support-for-javascript-error-analysis
scraped: 2026-05-12T11:35:01.270188
---

# Поддержка source map для анализа ошибок JavaScript

# Поддержка source map для анализа ошибок JavaScript

* How-to guide
* 4-min read
* Updated on Nov 15, 2023

Сведения о файлах маппинга для Android и файлах символов для iOS или tvOS см. в разделе [Загрузка и управление файлами символов для мобильных приложений](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.").

Для повышения производительности JavaScript-код часто преобразуется перед развёртыванием в production-среду. Одним из распространённых преобразований является *минификация* — удаление ненужных и повторяющихся фрагментов кода без влияния на его обработку браузером. На следующем изображении показан минифицированный JavaScript-файл:

![Minified javascript](https://dt-cdn.net/images/javascript-minified-1062-cf8952873a.png)

Minified javascript

Хотя этот подход улучшает производительность, его недостаток заключается в том, что преобразованные JavaScript-исходники нечитаемы и сложны для отладки. Source map обеспечивают немедленный доступ ко всем деталям обнаруженных ошибок JavaScript, упрощая их анализ, воспроизведение и исправление.

![Mapping minified javascript](https://dt-cdn.net/images/mapping-minified-javascript-667-17697bfb68.png)

Mapping minified javascript

## Анализ ошибки JavaScript с использованием source map

1. Перейдите в **Web** и выберите приложение для анализа.
2. Выберите плитку **Errors** и прокрутите страницу вниз до раздела **Top errors**.
3. Перейдите на вкладку **JavaScript** и выберите **Analyze errors**.
4. В разделе **Detail analysis for selected timeframe** выберите ошибку JavaScript для анализа.
   В разделе **Error details** можно просмотреть соответствующий стек вызовов ошибки. Сведения об ошибке сгруппированы по типу браузера.
5. Выберите **Expand** ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") для открытия фрейма стека для анализа.

Если для ошибки найден source map, источник обнаруженного source map и расположение ошибки в исходном JavaScript-файле выделяются. Если source map не обнаружен, можно выбрать **Upload source map** и загрузить соответствующий source map вручную.

В большинстве случаев source map содержит исходный JavaScript-код, и можно видеть стек вызовов с выделенной строкой кода, вызвавшей ошибку. Пример показан на следующем изображении.

![Upload source files](https://dt-cdn.net/images/upload-source-files-1920-475c274471.png)

Upload source files

Если source map не содержит исходный JavaScript-код, выберите **Upload source files** для загрузки исходных JavaScript-файлов.

Для загрузки source map и файлов символов требуется [разрешение](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") **Change monitoring settings** на уровне среды.

После ручной загрузки JavaScript-файла для анализа конкретного фрейма стека другие связанные фреймы стека автоматически сопоставляются с тем же файлом. Это экономит время при навигации по фреймам стека. Если встречается ошибка без соответствующего source map, загрузите необходимые файлы.

## Автоматическая загрузка source map

Dynatrace пытается автоматически загружать все доступные файлы source map следующим образом:

* При каждом возникновении ошибки Dynatrace пытается загрузить ответственный JavaScript-файл.
* После загрузки файла Dynatrace проверяет, содержит ли он ссылку на source map, например `//# sourceMappingURL=http://example.com/path/to/your/sourcemap.map`. Dynatrace может отображать точный номер строки, вызвавшей ошибку, в успешно загруженном минифицированном файле.
* Если source map содержит ссылку на source map, Dynatrace автоматически загружает его.
* При успешной загрузке и минифицированного файла, и соответствующего source map Dynatrace может отображать читаемый JavaScript-код и точный номер строки, вызвавшей ошибку.

Для работы загрузок оба файла должны быть публично доступны.

Все запросы на загрузку от Dynatrace можно идентифицировать по строке `User-agent`, которая в обоих случаях имеет значение `ruxit server`.

Загрузите исходный файл, если также нужно читать комментарии разработчиков, которые обычно удаляются при минификации и обфускации.

## Загрузка source map

Для загрузки source map и файлов символов требуется [разрешение](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") **Change monitoring settings** на уровне среды.

Все доступные исходные файлы перечислены в **Settings** > **Web and mobile monitoring** > **Source maps and symbol files**.

Dynatrace автоматически пытается загружать все доступные source map и исходные JavaScript-файлы из публичных CDN. Кроме того, source map и исходные файлы можно загружать со страницы сведений об ошибке JavaScript.

Чтобы загрузить source map со страницы сведений об ошибке JavaScript:

1. Перейдите в **Web** и выберите приложение для настройки.
2. Выберите плитку **Errors** и прокрутите страницу вниз до раздела **Top errors**.
3. Перейдите на вкладку **JavaScript** и выберите нужную ошибку.
4. Прокрутите страницу вниз до раздела **Stack trace** и выберите **Expand** ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") для открытия фрейма стека.
5. Выберите **Upload source map**.

   Обратите внимание, что можно загружать файл символов размером до 100 МиБ в сжатом виде; несжатый файл не должен превышать 500 МиБ.

   ![Upload source map](https://dt-cdn.net/images/upload-stacktrace-954-61408e527f.png)

   Upload source map

## Управление source map

Для управления ранее загруженными source map можно использовать веб-интерфейс Dynatrace.

Чтобы просмотреть список загруженных source map и файлов символов для всех приложений:

1. Перейдите в **Settings**.
2. Выберите **Web and mobile monitoring** > **Source maps and symbol files**.

На странице отображается объём используемого хранилища и его лимит. При достижении лимита хранилища Dynatrace начинает удалять source map и файлы символов, начиная с наиболее старых.

Для Dynatrace Managed размер хранилища файлов символов и маппинга по умолчанию составляет 1 ГиБ. Размер хранилища можно изменить в соответствии с требованиями.

Для освобождения места можно вручную удалять файлы, которые больше не нужны. Выберите **Delete** ![Remove](https://dt-cdn.net/images/remove-icon-105c6a04c2.svg "Remove") в строке удаляемого файла.

Чтобы предотвратить автоматическое удаление файлов при достижении лимита хранилища, включите **Pinned** для source map и файлов символов, которые нужно сохранить.