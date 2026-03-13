---
title: Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto
scraped: 2026-03-03T21:30:58.689094
---

# Установка дополнения Dynatrace Operator для AWS Elastic Kubernetes Service (AWS EKS)

# Установка дополнения Dynatrace Operator для AWS Elastic Kubernetes Service (AWS EKS)

* Последняя версия Dynatrace
* Чтение: 3 минуты
* Опубликовано 16 января 2024 г.

Для использования дополнения Dynatrace Operator для AWS Elastic Kubernetes Service (AWS EKS) необходимо установить дополнение, а затем подключить EKS к вашей среде.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Установка дополнения Dynatrace Operator для EKS**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Подключение EKS к вашей среде**](#connect-eks)

## Шаг 1. Установка дополнения Dynatrace Operator для EKS

Дополнение Dynatrace Operator для AWS EKS можно установить через консоль AWS или через CLI.

### Установка через консоль AWS

Чтобы установить дополнение Dynatrace Operator для AWS EKS через консоль AWS

1. Перейдите к своему кластеру EKS.
2. В разделе **Дополнения** выберите **Получить дополнительные дополнения** > **Дополнения AWS Marketplace**.
3. Отфильтруйте по категории **Мониторинг** или выполните поиск по слову **Dynatrace**, чтобы найти дополнение Dynatrace Operator.
4. Установите флажок в правом верхнем углу карточки, затем нажмите **Далее**.
5. Необязательно: Выберите версию этого дополнения и роль IAM.
6. Нажмите **Далее** и проверьте конфигурацию перед применением.
7. Нажмите **Создать** и дождитесь завершения операции.

   * На странице обзора кластера отобразится баннер подтверждения.
   * Будет создано новое пространство имён `dynatrace`.
   * Несколько ресурсов будут автоматически развёрнуты путём рендеринга базового helm-чарта.

### Установка через CLI

Чтобы установить дополнение Dynatrace Operator для AWS EKS через CLI

1. Проверьте доступность дополнения и его версий.

   ```
   aws eks describe-addon-versions --addon-name dynatrace_dynatrace-operator
   ```
2. Разверните дополнение, указав версию при необходимости.

   ```
   aws eks create-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator --addon-version <version>
   ```
3. Проверьте успешность установки.

   ```
   aws eks describe-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator
   ```

## Шаг 2. Подключение EKS к вашей среде

1. Создайте секрет для токенов доступа.

   Создайте секрет с именем `dynakube` для токена Dynatrace Operator и токена приёма данных, полученных в разделе [Необходимые токены и разрешения](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
2. Примените пользовательский ресурс DynaKube.

   Мониторинг с `cloudNativeFullStack` или `appOnly` (с CSI-драйвером) поддерживается только для Dynatrace Operator версии 0.15.0+.

   Загрузите [образец пользовательского ресурса DynaKube для режима cloud-native full-stack с GitHub](https://dt-url.net/9n636jg). Кроме того, можно ознакомиться с [доступными параметрами](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") или [практическими руководствами](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases") и адаптировать пользовательский ресурс DynaKube согласно своим требованиям.

   Выполните приведённую ниже команду для применения пользовательского ресурса DynaKube, заменив `<your-DynaKube-CR>` на фактическое имя файла вашего пользовательского ресурса DynaKube. Веб-хук валидации предоставит полезные сообщения об ошибках в случае возникновения проблем.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
3. Необязательно: Проверка развёртывания.

   Убедитесь, что ваш DynaKube запущен и все Pod'ы в пространстве имён Dynatrace находятся в состоянии запуска и готовности.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   При стандартной конфигурации DynaKube должны отображаться следующие Pod'ы:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```
