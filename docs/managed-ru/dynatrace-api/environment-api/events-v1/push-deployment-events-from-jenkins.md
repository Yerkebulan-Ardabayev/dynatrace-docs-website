---
title: Отправка событий развёртывания из Jenkins
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/events-v1/push-deployment-events-from-jenkins
scraped: 2026-05-12T12:13:37.847230
---

# Отправка событий развёртывания из Jenkins

# Отправка событий развёртывания из Jenkins

* Справочник
* Обновлено 13 июня 2022 г.

Чтобы настроить Jenkins для отправки событий развёртывания в Dynatrace.

1. Сгенерируйте новый [access-токен для Dynatrace API](/managed/dynatrace-api/basics/dynatrace-api-authentication "Узнайте, как пройти аутентификацию для использования Dynatrace API.").
2. Установите [HTTP Request Plugin](https://dt-url.net/3g23u1a) в вашу установку Jenkins.
3. В конфигурации сборки Jenkins нажмите **Add build step** и выберите **HTTP Request**.

![Jenkins, добавление HTTP Request как шага сборки](https://dt-cdn.net/images/jenkins-build-addbuildstep-httprequest-2-333-fec9e1de4a.png)

Jenkins, добавление HTTP Request как шага сборки

4. В поле **URL** введите URL вашего эндпоинта event API:

   * Dynatrace Managed https://{your-domain}/e/{your-environment-id}/api/v1/events/
   * Dynatrace SaaS https://{your-environment-id}.live.dynatrace.com/api/v1/events/
   * Environment ActiveGate https://{your-activegate-domain}/e/{your-environment-id}/api/v1/events
5. Выберите **POST** в качестве **HTTP mode**.
6. Нажмите **Advanced**, чтобы увидеть все поля конфигурации.

![Jenkins, конфигурация HTTP Request](https://dt-cdn.net/images/jenkins-httprequest-1433-c9422103f1.png)

Jenkins, конфигурация HTTP Request

7. В секции **Headers** выберите **APPLICATION\_JSON** в поле **Accept** .
8. Выберите **APPLICATION\_JSON** в поле **Content-type**.
9. Добавьте **Custom header**, введите **Authorization** в поле **Header** и **Api-Token {token}** в поле **Value**.

![Jenkins, конфигурация Headers](https://dt-cdn.net/images/jenkins-headers-1417-ef4687d080.png)

Jenkins, конфигурация Headers

10. Скопируйте и адаптируйте по необходимости следующий payload в поле **Request body**. Подробнее о полях payload смотрите в [POST events](/managed/dynatrace-api/environment-api/events-v1/post-event "Создание пользовательского события через Dynatrace API.").

```
{



"eventType": "CUSTOM_DEPLOYMENT",



"attachRules": {



"tagRule": {



"meTypes": "PROCESS_GROUP_INSTANCE",



"tags": "Dev"



}



},



"deploymentName": "${JOB_NAME}",



"deploymentVersion": "1.1",



"deploymentProject": "CustomBankingService",



"remediationAction": "http://revertMe",



"ciBackLink": "${BUILD_URL}",



"source": "Jenkins",



"customProperties": {



"Jenkins Build Number": "${BUILD_ID}",



"Git commit": "${GIT_COMMIT}"



}



}
```

`${JOB_NAME}`, `${BUILD_URL}`, `${BUILD_ID}`, `${GIT_COMMIT}` это [переменные окружения, задаваемые Jenkins](https://dt-url.net/x803uzw) во время выполнения задания.

11. Сохраните конфигурацию сборки. В следующий раз, когда вы соберёте свой проект, событие развёртывания будет отправлено наблюдаемым сущностям (например, хостам и сервисам), которые вы определили в `tagRule` тела запроса.