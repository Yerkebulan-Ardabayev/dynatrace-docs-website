---
title: Ingest Kubernetes DNS logs from AWS
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks/k8s-dns-logs
scraped: 2026-03-02T21:29:46.309494
---

# Приём DNS-логов Kubernetes из AWS

# Приём DNS-логов Kubernetes из AWS

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 18 марта 2024 г.

На этой странице описывается, как принимать DNS-логи, связанные с Kubernetes, из AWS в Dynatrace для контейнеров, работающих в кластере Amazon Elastic Kubernetes Service (EKS).

## Kubernetes и разрешение доменных имён

В EKS обнаружение сервисов и разрешение доменных имён выполняются через [дополнение CoreDNS](https://dt-url.net/iu037ap), которое представляет собой гибкий, расширяемый DNS-сервер, способный выступать в качестве кластерного DNS для Kubernetes.

При запуске кластера Amazon EKS хотя бы с одним узлом по умолчанию развёртываются две реплики образа CoreDNS независимо от количества развёрнутых узлов в вашем кластере.

Подробнее о [работе с дополнением CoreDNS для Amazon EKS](https://dt-url.net/dn837jp).

### CoreDNS

Когда под в кластере EKS пытается разрешить доменное имя `www.dynatrace.com`, запрос сначала отправляется в сервис CoreDNS. CoreDNS ведёт локальный реестр зарегистрированных сервисов в кластере EKS и кэш DNS для более быстрого ответа на входящие DNS-запросы.

По умолчанию CoreDNS не ведёт журнал DNS-запросов.

Чтобы включить журналирование DNS-запросов в Kubernetes, необходимо включить [плагин log](https://dt-url.net/iu037ap) в конфигурации CoreDNS.

1. Откройте консоль управления Kubernetes для просмотра существующего `ConfigMap` CoreDNS, который включает текущий `Corefile`. Сервис CoreDNS работает в пространстве имён `kube-system`:

   ```
   kubectl describe configmaps --namespace kube-system coredns
   ```
2. Скопируйте `Corefile` из ответа в соответствующий раздел `coredns-config.yml`. По умолчанию `ConfigMap` Kubernetes выглядит примерно так:

   ```
   apiVersion: v1



   kind: ConfigMap



   metadata:



   name: coredns



   namespace: kube-system



   data:



   Corefile: |



   .:53 {



   errors



   health



   kubernetes cluster.local in-addr.arpa ip6.arpa {



   pods insecure



   fallthrough in-addr.arpa ip6.arpa



   }



   prometheus :9153



   forward . /etc/resolv.conf



   cache 30



   loop



   reload



   loadbalance



   }
   ```
3. Чтобы использовать плагин log и начать журналирование всех DNS-запросов в стандартный вывод, примените следующую конфигурацию:

   ```
   . {



   log



   }
   ```
4. Чтобы активировать плагин log, добавьте соответствующую строку в `Corefile` по умолчанию в вашем файле `coredns-config.yml`. Результат при использовании `ConfigMap` по умолчанию должен выглядеть примерно так:

   ```
   apiVersion: v1



   kind: ConfigMap



   metadata:



   name: coredns



   namespace: kube-system



   data:



   Corefile: |



   .:53 {



   log



   errors



   health



   kubernetes cluster.local in-addr.arpa ip6.arpa {



   pods insecure



   fallthrough in-addr.arpa ip6.arpa



   }



   prometheus :9153



   forward . /etc/resolv.conf



   cache 30



   loop



   reload



   loadbalance



   }
   ```
5. Примените `coredns-config.yml` к вашему сервису CoreDNS в Kubernetes с помощью следующей команды:

   ```
   kubectl apply -f coredns-config.yml
   ```

   В результате логи DNS-запросов теперь можно увидеть в логах подов CoreDNS, которые можно либо перенаправить в Dynatrace, либо просмотреть в среде AWS CloudShell с помощью команды:

   ```
   kubectl logs --namespace kube-system -f deployment/coredns --follow
   ```

### Route53

Если CoreDNS не имеет ответа для `www.dynatrace.com` в реестре, DNS-запрос перенаправляется на DNS-сервер узла кластера. Обычно это [сервис AWS Route53](https://dt-url.net/c7237yw), который является рекурсивным DNS-сервером по умолчанию в AWS.

Как и CoreDNS, Route53 по умолчанию не ведёт журнал DNS-запросов.

Чтобы настроить Route53 для журналирования DNS-запросов

1. Откройте консоль управления AWS и перейдите на страницу панели управления Route53.
2. В левом меню перейдите в **Resolver** > **Query logging** и выберите **Configure query logging**.
3. Выберите **CloudWatch Logs log group** в качестве назначения и выберите группу логов в качестве целевой группы логов для ваших журналов запросов.
4. Добавьте VPC, для которых вы хотите журналировать запросы (например, VPC, где расположены ваши узлы EKS).
5. Выберите **Configure query logging**, чтобы сохранить настройки.

Подробнее о [настройке журналирования DNS-запросов](https://dt-url.net/qt437wq).

### Содержимое DNS-логов в EKS

Давайте разберём, почему вам нужны и логи CoreDNS, и логи Route53, на примере содержимого логов.

* В **CoreDNS** логи запросов по умолчанию хранятся в следующем формате:

  ```
  172.31.47.132:40395 - 23683 "A IN www.dynatrace.com. udp 35 false 512" NOERROR qr,rd,ra 278 0.002157881s
  ```

  Запись лога содержит:

  + IP-адрес и порт источника
  + идентификатор запроса
  + тип и класс запроса
  + сам запрос
  + другие детали ответа, такие как код ответа, флаги и размер ответа

  Поля можно в некоторой степени настраивать.

  Подробнее о [пользовательском формате логов CoreDNS](https://dt-url.net/iu037ap).
* Логи **Route53** хранятся в следующей JSON-структуре:

  ```
  {



  "version":"1.100000","account_id":"<id>","region":"us-east-1","vpc_id":"vpc-<id>",



  "query_timestamp":"2023-11-20T21:20:29Z","query_name":"www.dynatrace.com.","query_type":"A",



  "query_class":"IN","rcode":"NOERROR","answers":[{"Rdata":"52.3.5.163","Type":"A","Class":"IN"}],



  "srcaddr":"172.31.73.143","srcport":"51217","transport":"UDP","srcids":{"instance":"i-<id>"}



  }
  ```

  Из приведённого примера видно, что логи Route53 содержат гораздо больше деталей о DNS-запросе, включая подробное содержимое данных ответа, которое необходимо для поиска угроз. Обратите внимание, что в логах Route53 нет IP-адреса подов: мы видим только то, что узел EKS пытался разрешить этот хост. Поэтому, если вы хотите точно определить под, создающий вредоносный DNS-трафик, логов Route53 будет недостаточно.

В логах CoreDNS можно найти информацию об источнике запроса (IP и порт источника пода), но логи не содержат информации о полезной нагрузке ответа.

Чтобы найти заражённый процесс, который получает команды от внешнего сервера через DNS-ответы, необходим поиск угроз. Для точного выполнения этого поиска необходимо анализировать оба типа логов и при необходимости коррелировать их.

## Потоковая передача логов в Dynatrace

Самый простой способ приёма логов в Dynatrace — через [интеграцию Amazon Data Firehose](../../integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет принимать облачные логи напрямую, без дополнительной инфраструктуры, с более высокой пропускной способностью.").

Чтобы настроить это в AWS CloudShell, выполните следующие действия:

```
# setting the environment in CLI



TARGET_URL=<your_environment_URL>



TARGET_API_TOKEN=dt0c01.*****



STACK_NAME=dynatrace-log-delivery-stream



wget -O dynatrace-firehose-log-stream.yaml https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-log-stream.yaml



aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-firehose-log-stream.yaml --stack-name $STACK_NAME --parameter-overrides DtApiUrl=$DYNATRACE_API_URL DtApiToken=$DYNATRACE_API_KEY
```

Чтобы настроить перенаправление групп логов CloudWatch Logs в Dynatrace, используйте следующую команду как для группы логов CloudWatch Logs кластера EKS, так и для группы логов, в которой хранятся логи Route53.

```
wget -O dynatrace-firehose-logs.sh https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-logs.sh && chmod +x dynatrace-firehose-logs.sh



./dynatrace-firehose-logs.sh subscribe --log-groups <log-group-name> --stack-name $STACK_NAME
```

Чтобы просмотреть вашу группу логов CloudWatch Logs в Dynatrace, используйте следующий DQL-скрипт в вашем тенанте.

```
fetch logs



| filter aws.log_group == "<log-group-name>"
```
