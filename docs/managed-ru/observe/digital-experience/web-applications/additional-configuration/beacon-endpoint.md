---
title: Настройка конечной точки маяка для веб-приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint
scraped: 2026-05-12T11:22:39.403812
---

# Настройка конечной точки маяка для веб-приложений

# Настройка конечной точки маяка для веб-приложений

* How-to guide
* 6-min read
* Updated on Nov 21, 2025

RUM JavaScript отправляет RUM-маяки (beacon) для передачи собранных данных в Dynatrace. По умолчанию конечная точка маяка зависит от метода инъекции, используемого для вашего приложения.

* **Приложения с автоматической инъекцией:** когда [RUM JavaScript инжектируется автоматически](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), маяки отправляются обратно на веб-сервер или сервер приложений через корневой относительный URL, где последний сегмент пути начинается с префикса `rb_` (например, `/rb_xxxxxxxxxx` или `/myapplication/rb_xxxxxxxxxx`). Конечная точка маяка предоставляется OneAgent, который перехватывает и пересылает RUM-маяки.
* **Безагентные приложения:** если выбран [безагентный мониторинг](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), данные отправляются на конечную точку маяка, которая является частью Cluster ActiveGate.

Как правило, изменять конечную точку маяка по умолчанию не требуется, однако существуют ситуации, когда может понадобиться альтернативная конфигурация конечной точки маяка. Например:

* Если ваша инфраструктура блокирует маяки автоматически инжектированного приложения из-за стандартного пути URL.
* Если необходимо, чтобы трафик мониторинга автоматически инжектированного приложения минуал CDN.
* Если нежелательно, чтобы RUM-маяки обрабатывались на веб-сервере или сервере приложений, на котором размещено приложение.
* Если ваш Cluster ActiveGate недоступен публично.

В следующих разделах описаны альтернативные конфигурации конечной точки маяка для учёта этих и подобных ограничений.

Конфигурации конечной точки маяка, описанные на этой странице, не влияют на корреляцию между пользовательскими действиями и распределёнными трассировками. Тем не менее проверьте в разделе [Technology support](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), поддерживается ли Real User Monitoring для вашей технологии.

## Приложение с автоматической инъекцией: изменение URL конечной точки маяка

В зависимости от конфигурации инфраструктуры возможна ситуация, когда маяки не могут пройти по автоматически выбранному URL-пути и поэтому не могут быть обработаны OneAgent. Для решения этой проблемы можно изменить часть URL конечной точки маяка, предшествующую префиксу `rb_`.

Чтобы изменить URL конечной точки маяка для приложения с автоматической инъекцией:

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Beacon endpoint**.
5. В раскрывающемся списке **Type** выберите **OneAgent**.
6. В поле **URL** введите относительный URL конечной точки маяка.

Обратите внимание, что нельзя удалить сегмент пути с префиксом `rb_`, поскольку он необходим OneAgent для идентификации RUM-маяков.

#### Примеры

В следующих примерах предполагается, что по умолчанию RUM-маяки отправляются на `/rb_bf12345abc`.

* **Корневой относительный URL:** если задать значение поля **URL** равным `/custompath`, маяки будут отправляться на `/custompath/rb_bf12345abc`.
* **Относительный URL:** если задать значение поля **URL** равным `./`, URL, по которому RUM JavaScript отправляет маяки, будет относительным по отношению к текущей странице. Например:

  + Если текущая страница — `/shop/index.html`, маяки будут отправляться на `/shop/rb_bf12345abc`.
  + Если текущая страница — `/account/dashboard/`, маяки будут отправляться на `/account/dashboard/rb_bf12345abc`.

## Приложение с автоматической инъекцией: отправка маяков в Cluster ActiveGate

Если необходимо, чтобы RUM-маяки приложения с автоматической инъекцией обрабатывались Cluster ActiveGate, а не OneAgent, выполните следующие шаги.

1. Перейдите в **Web**.
2. Выберите приложение, которое нужно настроить.
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **General settings** > **Beacon endpoint**.
5. В раскрывающемся списке **Type** выберите **Cluster ActiveGate**.

При такой конфигурации Dynatrace применяет [allowlist источников маяков](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам вашего приложения.

## Приложение с автоматической инъекцией: отправка маяков на другой веб-сервер

По умолчанию RUM-маяки приложения с автоматической инъекцией обрабатываются одной из групп процессов, на которых размещено приложение. В качестве альтернативы маяки могут обрабатываться на любом другом инструментированном веб-сервере или сервере приложений, технология которого указана в разделе [Technology support — Real User Monitoring — Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Чтобы отправлять маяки приложения с автоматической инъекцией на другой инструментированный сервер:

1. В инжектированном RUM JavaScript найдите `reportUrl` и скопируйте последний сегмент URL-пути, начинающийся с `rb_`.
2. Добавьте это значение к URL инструментированного веб-сервера или сервера приложений.

   Например, если последний сегмент `reportUrl` — `/rb_abcdefghi`, а URL сервера — `http://www.my-server.com`, итоговый URL конечной точки маяка будет `http://www.my-server.com/rb_abcdefghi`.
3. Перейдите в **Web**.
4. Выберите приложение, которое нужно настроить.
5. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
6. В настройках приложения выберите **General settings** > **Beacon endpoint**.
7. В раскрывающемся списке **Type** выберите **OneAgent**.
8. В поле **URL** введите URL конечной точки маяка, определённый на шаге 2.
9. Включите **Send beacon data via CORS**.

При такой конфигурации Dynatrace применяет [allowlist источников маяков](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам вашего приложения.

## Безагентное приложение: отправка маяков на веб-сервер

Вместо использования Cluster ActiveGate в качестве конечной точки маяка для безагентного приложения можно использовать любой инструментированный веб-сервер или сервер приложений, технология которого указана в разделе [Technology support — Real User Monitoring — Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Чтобы отправлять маяки безагентного приложения на инструментированный сервер:

1. Перейдите в **Web**.
2. Выберите любое **приложение с автоматической инъекцией**, которое не использует пользовательских конфигураций конечной точки маяка, описанных на этой странице.

   На этом шаге следует выбрать не настраиваемое безагентное приложение, а другое **приложение с автоматической инъекцией** со стандартной конфигурацией конечной точки маяка. Если такого приложения нет, временно создайте его, как описано в разделе [Определение приложений для Real User Monitoring | Подход на основе правил обнаружения приложений](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Впоследствии это временное приложение можно [удалить](/managed/observe/digital-experience/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.").
3. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
4. В настройках приложения выберите **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript tag** найдите `reportUrl` в предоставленном сниппете и скопируйте его значение.
6. Добавьте значение `reportUrl` к URL инструментированного веб-сервера или сервера приложений.

   Например, если значение `reportUrl` — `/rb_abcdefghi`, а URL сервера — `http://www.my-server.com`, итоговый URL конечной точки маяка будет `http://www.my-server.com/rb_abcdefghi`.
7. Перейдите в **Web**.
8. Выберите безагентное приложение, которое нужно настроить.
9. В правом верхнем углу страницы обзора приложения выберите **More** (**…**) > **Edit**.
10. В настройках приложения выберите **General settings** > **Beacon endpoint**.
11. В раскрывающемся списке **Type** выберите **OneAgent**.
12. В поле **URL** введите URL конечной точки маяка, определённый на шаге 6.
13. Включите **Send beacon data via CORS**.

При такой конфигурации Dynatrace применяет [allowlist источников маяков](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам вашего приложения (то же самое выполняется для стандартной конфигурации конечной точки маяка всех безагентных приложений).