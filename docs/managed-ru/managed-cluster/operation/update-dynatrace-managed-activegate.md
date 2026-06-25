---
title: Обновление Cluster ActiveGate
source: https://docs.dynatrace.com/managed/managed-cluster/operation/update-dynatrace-managed-activegate
scraped: 2026-05-12T11:53:10.081085
---

# Обновление Cluster ActiveGate

# Обновление Cluster ActiveGate

* Published Jun 03, 2020

Для просмотра списка установленных ActiveGate перейдите в **Deployment Status** > **ActiveGates**. Для каждого ActiveGate в списке указана текущая **Version** и **Update status** (актуален, ожидает обновления или обновляется).

![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Жёлтый значок предупреждения указывает на то, что ваш ActiveGate отстаёт более чем на пять версий. Рекомендуется обновить эти ActiveGate как можно скорее.

ActiveGate в контейнерах развёртываются и загружаются с использованием облачных инструментов. Например, Kubernetes использует [пользовательские определения ресурсов](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

### Автоматическое обновление

Для управления функцией обновления конкретного ActiveGate в списке выберите ActiveGate, чтобы развернуть сведения.

* **Auto-update**  
  Для использования функции автоматического обновления убедитесь, что переключатель **Automatic updates** для данного ActiveGate включён. При появлении новой версии ActiveGate новый пакет установки будет загружен на соответствующий хост и установлена новая версия ActiveGate. Это настройка по умолчанию для новых сред. Для существующих сред настройка остаётся без изменений.  
  Проверка наличия обновлений выполняется с интервалом 30 минут.
* **One-click update**  
  Для немедленного выполнения обновления выберите **Update**. Эта функция доступна только в том случае, если переключатель **Automatic updates** для данного ActiveGate отключён.

### Загрузка и обновление вручную

Также можно загрузить ActiveGate вручную и обновить его. Удалять текущую версию ActiveGate не нужно — просто установите новую версию поверх старой, и конфигурация ActiveGate будет перенесена.

* [Установить Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").

В процессе обновления конфигурация ActiveGate сохраняется в файлах `custom.properties` и `launcheruserconfig.conf`. Эти два файла не будут перезаписаны в процессе обновления, однако рекомендуется создать их резервные копии перед обновлением ActiveGate.

* Свойства файла `custom.properties` см. в разделе [Настройка ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").
* Свойства `launcheruserconfig.conf` см. в разделе [Настройка лаунчера ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

## Статус обновления

Статус обновления ActiveGate, отображаемый на странице **Deployment Status**, может принимать следующие значения:

**Up to date**  
На соответствующем хосте установлена последняя доступная версия ActiveGate.

**Update available**  
Доступно обновление для данной версии ActiveGate.

**Update pending**  
Сразу после выбора **Update ActiveGate** статус изменяется на **Update pending** и остаётся таким до начала процесса обновления.
Статус также может отображаться как `pending` в следующих случаях:

* Кластер в настоящее время обновляется.
* Достигнуто максимальное количество одновременных загрузок обновлений, и ActiveGate ожидает возобновления загрузки.

**Update in progress**  
ActiveGate запросил и загрузил новый пакет установки с сервера и в настоящее время выполняет его установку или восстанавливает подключение к серверу.

**Update problem**  
В этом случае для ActiveGate отображается старый номер версии.  
Возможные причины:

* ActiveGate загрузил новый установщик, однако установка не была выполнена или завершилась неудачно; в результате ActiveGate по-прежнему работает на старой версии.
  Проверьте журналы автообновления и установщика ActiveGate для определения причины.
* ActiveGate загрузил новый установщик, но затем не смог восстановить подключение к серверу (был потерян).
  Проверьте журналы установщика ActiveGate для определения причины неудачи.
* Для ActiveGate недоступны установщики.
* Обновление приостановлено, поскольку в другой среде возникли проблемы с обновлением предложенной версии ActiveGate.

**Unknown**  
Подключение к данному ActiveGate прервано, и определить статус невозможно.  
Этот статус также может отображаться, если ActiveGate был успешно удалён: в таком случае **Deployment Status** продолжает отображать удалённый ActiveGate со статусом обновления `Unknown` в течение семи дней.