---
title: Настройка конечной точки маяков для веб-приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint
---

# Настройка конечной точки маяков для веб-приложений в RUM Classic

# Настройка конечной точки маяков для веб-приложений в RUM Classic

* Практическое руководство
* 6 минут на чтение
* Обновлено 21 ноября 2025 г.

RUM JavaScript отправляет RUM-маяки, чтобы передавать собранные данные в Dynatrace. По умолчанию конечная точка маяков зависит от метода внедрения, используемого для приложения.

* **Приложения с автоматическим внедрением:** когда [RUM JavaScript внедряется автоматически](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications"), маяки отправляются обратно на веб-сервер или сервер приложений с использованием относительного от корня URL, где последний сегмент пути имеет префикс `rb_` (например, `/rb_xxxxxxxxxx` или `/myapplication/rb_xxxxxxxxxx`). Конечную точку маяков предоставляет OneAgent, который перехватывает и пересылает RUM-маяки.
* **Приложения без агента:** если выбран [мониторинг без агента](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications."), данные отправляются на конечную точку маяков, которая является частью кластерного ActiveGate.

Обычно менять конечную точку маяков по умолчанию не нужно, но есть определённые сценарии, в которых может понадобиться альтернативная конфигурация конечной точки маяков. Например:

* Если инфраструктура блокирует маяки приложения с автоматическим внедрением из-за пути их URL по умолчанию.
* Если нужно, чтобы трафик мониторинга приложения с автоматическим внедрением обходил CDN.
* Если предпочтительнее, чтобы RUM-маяки не обрабатывались на веб-сервере или сервере приложений, на котором размещено приложение.

* Если кластерный ActiveGate недоступен публично.

В следующих разделах описаны альтернативные конфигурации конечной точки маяков, которые позволяют учесть эти и подобные ограничения.

Конфигурации конечной точки маяков, описанные на этой странице, не влияют на корреляцию между действиями пользователей и распределёнными трассировками. Однако стоит свериться с разделом [Поддержка технологий](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), чтобы узнать, поддерживается ли Real User Monitoring для используемой технологии.

## Приложение с автоматическим внедрением. Изменение URL конечной точки маяков

В зависимости от инфраструктуры и её конфигурации возможно, что маяки не могут пройти с автоматически выбранным путём URL и поэтому не могут обрабатываться OneAgent. Чтобы решить эту проблему, можно изменить часть URL конечной точки маяков, которая идёт перед префиксом `rb_`.

Чтобы изменить URL конечной точки маяков для приложения с автоматическим внедрением

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **General settings** > **Beacon endpoint**.
5. В раскрывающемся списке **Type** выбрать **OneAgent**.
6. В поле **URL** ввести относительный URL конечной точки маяков.

Обратите внимание, что нельзя удалить сегмент пути с префиксом `rb_`, поскольку он требуется OneAgent для идентификации RUM-маяков.

#### Примеры

В следующих примерах предполагается, что по умолчанию RUM-маяки отправляются на `/rb_bf12345abc`.

* **URL, относительный от корня:** если задать **URL** как `/custompath`, маяки будут отправляться на `/custompath/rb_bf12345abc`.
* **Относительный URL:** если задать **URL** как `./`, то URL, на который RUM JavaScript отправляет маяки, будет относительным от текущей страницы. Например:

  + Если текущая страница `/shop/index.html`, то маяки отправляются на `/shop/rb_bf12345abc`.
  + Если текущая страница `/account/dashboard/`, то маяки отправляются на `/account/dashboard/rb_bf12345abc`.

## Приложение с автоматическим внедрением. Отправка маяков в кластерный ActiveGate

Если нужно, чтобы RUM-маяки приложения с автоматическим внедрением обрабатывались кластерным ActiveGate вместо OneAgent, выполнить следующие шаги.

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно настроить.
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **General settings** > **Beacon endpoint**.
5. В раскрывающемся списке **Type** выбрать **Cluster ActiveGate**.

Для этой конфигурации Dynatrace применяет [список разрешённых источников маяков](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам приложения.

## Приложение с автоматическим внедрением. Отправка маяков на другой веб-сервер

По умолчанию RUM-маяки приложения с автоматическим внедрением обрабатываются одной из групп процессов, на которой размещено приложение. В качестве альтернативы маяки можно обрабатывать на любом другом инструментированном веб-сервере или сервере приложений технологии, перечисленной в разделе [Поддержка технологий - Real User Monitoring - веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Чтобы отправлять маяки приложения с автоматическим внедрением на другой инструментированный сервер

1. Во внедрённом RUM JavaScript найти `reportUrl` и скопировать последний сегмент пути URL, у которого есть префикс `rb_`.
2. Добавить это значение к URL инструментированного веб-сервера или сервера приложений.

   Например, если последний сегмент `reportUrl`, это `/rb_abcdefghi`, а URL сервера, это `http://www.my-server.com`, итоговый URL конечной точки маяков будет `http://www.my-server.com/rb_abcdefghi`.
3. Перейти в **Web**.
4. Выбрать приложение, которое нужно настроить.
5. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
6. В настройках приложения выбрать **General settings** > **Beacon endpoint**.
7. В раскрывающемся списке **Type** выбрать **OneAgent**.
8. В поле **URL** ввести конечную точку маяков, определённую на шаге 2.
9. Включить **Send beacon data via CORS**.

Для этой конфигурации Dynatrace применяет [список разрешённых источников маяков](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам приложения.

## Приложение без агента. Отправка маяков на веб-сервер

Вместо использования кластерного ActiveGate в качестве конечной точки маяков для приложения без агента можно использовать любой инструментированный веб-сервер или сервер приложений технологии, перечисленной в разделе [Поддержка технологий - Real User Monitoring - веб-серверы и приложения](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Чтобы отправлять маяки приложения без агента на инструментированный сервер

1. Перейти в **Web**.
2. Выбрать любое приложение **с автоматическим внедрением**, которое не использует ни одну из пользовательских конфигураций конечной точки маяков, описанных на этой странице.

   На этом шаге нужно выбрать не приложение без агента, которое настраивается, а другое приложение **с автоматическим внедрением**, у которого конфигурация конечной точки маяков задана по умолчанию. Если приложения с автоматическим внедрением нет, временно создать его, как описано в разделе [Определение приложений для Real User Monitoring | Подход с правилами обнаружения приложений](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). Затем это временное приложение можно [удалить](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/delete-application-web "Delete your web applications via the Dynatrace web UI or API.").
3. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
4. В настройках приложения выбрать **Injection** > **Manual insertion**.
5. В разделе **OneAgent JavaScript tag** найти `reportUrl` в предоставленном фрагменте кода и скопировать его значение.
6. Добавить значение `reportUrl` к URL инструментированного веб-сервера или сервера приложений.

   Например, если значение `reportUrl`, это `/rb_abcdefghi`, а URL сервера, это `http://www.my-server.com`, итоговый URL конечной точки маяков будет `http://www.my-server.com/rb_abcdefghi`.
7. Перейти в **Web**.
8. Выбрать приложение без агента, которое нужно настроить.
9. В верхнем правом углу страницы обзора приложения выбрать **More** (**…**) > **Edit**.
10. В настройках приложения выбрать **General settings** > **Beacon endpoint**.
11. В раскрывающемся списке **Type** выбрать **OneAgent**.
12. В поле **URL** ввести конечную точку маяков, определённую на шаге 6.
13. Включить **Send beacon data via CORS**.

Для этой конфигурации Dynatrace применяет [список разрешённых источников маяков](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.") к RUM-маякам приложения (то же самое делается для конфигурации конечной точки маяков по умолчанию для всех приложений без агента).