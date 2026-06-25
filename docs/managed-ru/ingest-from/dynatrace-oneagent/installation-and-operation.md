---
title: Установка OneAgent на сервер
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation
scraped: 2026-05-12T11:06:38.497546
---

# Установка OneAgent на сервер

# Установка OneAgent на сервер

* 3-min read
* Updated on Jan 22, 2026

Следуйте этому руководству для первоначальной установки Dynatrace OneAgent.

После выполнения всех шагов OneAgent будет установлен на хост, и вы сможете использовать Dynatrace для мониторинга этого хоста и его процессов.

Информация на этой странице не зависит от платформы.

Для получения сведений об установке OneAgent и расширенных операциях, специфичных для конкретной ОС, выберите вашу операционную систему для получения подробных инструкций.

[Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Windows](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [AIX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Solaris](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [zOS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

## Предварительные требования

В данном руководстве предполагается, что у вас есть:

* Окружение Dynatrace.
* Права администратора на хосте Linux, Windows или AIX (на котором отсутствуют существующие установки OneAgent).
* Сеть, поддерживающая SSL-связь.

## Настройка OneAgent

Чтобы загрузить и установить OneAgent на хост:

1. Перейдите в **Deploy Dynatrace**.
2. Выберите **Start installation**. Затем выберите платформу, на которой необходимо установить OneAgent.

   ![Выбор платформы OneAgent](https://dt-cdn.net/images/download-dynatrace-oneagent-1213-68157f2673.png)

   Выбор платформы OneAgent
3. Вставьте PaaS-токен в поле **Download token** или выберите **Create token** для генерации нового токена Deployment API.

   Скопируйте токен и сохраните в безопасном месте, поскольку получить к нему доступ повторно не получится.
4. Введите или выберите соответствующие параметры:

   * **Architecture**

     Только для Linux: выберите один из доступных вариантов из списка.
   * **Monitoring mode**

     Варианты: **Full-Stack**, **Infrastructure** или **Discovery**. Если вы используете бесплатную пробную версию Dynatrace, выберите **Full-Stack** для просмотра всех возможностей наблюдения. Режим мониторинга всегда можно изменить после установки.
   * Для **Optional parameters** можно добавить **Custom host name** для удобной идентификации.

     Остальные параметры выходят за рамки данного руководства.

   ![Параметры развёртывания OneAgent](https://dt-cdn.net/images/oneagent-installation-1-668-edc694da5b.png)

   Параметры развёртывания OneAgent
5. Загрузите OneAgent. Используйте предоставленную команду CLI или выберите **Download**.
6. Проверьте подпись. Используйте предоставленную команду CLI. (Только для Linux и AIX.)
7. Установите OneAgent. Используйте предоставленную команду CLI или запустите исполняемый файл через GUI. Следуйте шагам, описанным в установщике.

   При установке через GUI добавьте следующие параметры на экране **Optional: advanced command-line settings**:
   `--set-monitoring-mode=fullstack --set-app-log-content-access=true`
8. Когда установщик отобразит сообщение **Congratulations! Dynatrace OneAgent was successfully installed!**, OneAgent установлен на хост. Выберите **Finish** для выхода из установщика.
9. Поскольку OneAgent не может внедриться в уже запущенные процессы, необходимо перезапустить все процессы, которые OneAgent должен мониторить.
10. Чтобы убедиться, что OneAgent мониторит ваш хост, откройте Dynatrace и перейдите в **Infrastructure & Operations** > **Host**. Если всё работает корректно, вы увидите имя вашего хоста в таблице **Hosts**.

OneAgent настроен и мониторит ваш хост. Смотрите [Начало работы](/managed/discover-dynatrace/get-started "Узнайте, как начать работу с Dynatrace Managed.") для продолжения первого знакомства с Dynatrace.

## Связанные темы

* [Функции OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управление функциями OneAgent глобально и для каждой группы процессов.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранный раздел недоступен в Dynatrace Managed.")
* [Настройки уровня хоста](/managed/observe/infrastructure-observability/hosts/configuration "Настройки уровня хоста")
* [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Подробнее о доступных режимах мониторинга при использовании OneAgent.")