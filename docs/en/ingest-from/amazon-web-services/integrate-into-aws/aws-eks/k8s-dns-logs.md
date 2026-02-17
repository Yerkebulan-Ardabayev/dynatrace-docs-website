---
title: Ingest Kubernetes DNS logs from AWS
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks/k8s-dns-logs
scraped: 2026-02-17T05:02:57.002334
---

# Ingest Kubernetes DNS logs from AWS

# Ingest Kubernetes DNS logs from AWS

* How-to guide
* 5-min read
* Published Mar 18, 2024

This page describes how to ingest Kubernetes-related DNS logs from AWS to Dynatrace with containers running in an Amazon Elastic Kubernetes Service (EKS) Cluster.

## Kubernetes and domain name resolution

In EKS, service discovery and domain name resolution are both done via the [CoreDNS add-onï»¿](https://dt-url.net/iu037ap), which is a flexible, extensible DNS server that can serve as the Kubernetes cluster DNS.

When you launch an Amazon EKS cluster with at least one node, two replicas of the CoreDNS image are deployed by default, regardless of the number of nodes deployed in your cluster.

Read more about [working with the CoreDNS Amazon EKS add-onï»¿](https://dt-url.net/dn837jp).

### CoreDNS

When a pod in an EKS cluster tries to resolve the domain name `www.dynatrace.com`, the request is first sent to the CoreDNS service. CoreDNS keeps a local registry of the registered services in the EKS cluster and a DNS cache, to provide faster responses to incoming DNS queries.

CoreDNS does not log DNS queries by default.

To enable DNS query logging in Kubernetes, you need to enable the [log pluginï»¿](https://dt-url.net/iu037ap) in the CoreDNS configuration.

1. Open your Kubernetes management console to view your existing CoreDNS `ConfigMap`, which includes the current `Corefile`. CoreDNS service is running under the `kube-system` namespace:

   ```
   kubectl describe configmaps --namespace kube-system coredns
   ```
2. Copy the `Corefile` from the response to the respective `coredns-config.yml` section. The default Kubernetes `ConfigMap` looks something like this:

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
3. To use the log plugin and start logging all the DNS queries to standard output, apply the following configuration:

   ```
   . {



   log



   }
   ```
4. To activate the log plugin, add the corresponding line to the default `Corefile` in your `coredns-config.yml` file. Output when using the default `ConfigMap` should be similar to this:

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
5. Apply the `coredns-config.yml` to your CoreDNS service in Kubernetes with the following command:

   ```
   kubectl apply -f coredns-config.yml
   ```

   As a result, the DNS query logs can now be seen in the CoreDNS pods' logs, which can now be either forwarded to Dynatrace or viewed in the AWS CloudShell environment with the command:

   ```
   kubectl logs --namespace kube-system -f deployment/coredns --follow
   ```

### Route53

If CoreDNS doesnât have an answer for `www.dynatrace.com` in the registry, the DNS query is forwarded to the DNS server of the cluster Node. Usually, this is the [AWS Route53 serviceï»¿](https://dt-url.net/c7237yw), which is the default recursive DNS server in AWS.

Like CoreDNS, Route53 does not log DNS queries by default.

To configure Route53 to log DNS queries

1. Open your AWS Management Console and go to the Route53 Dashboard page.
2. From the left menu, go to **Resolver** > **Query logging** and select **Configure query logging**.
3. Select **CloudWatch Logs log group** as your destination and choose a log group as the destination log group for your query logs.
4. Add the VPCs that you want the queries to be logged for (for example, the VPC where your EKS nodes reside).
5. Select **Configure query logging** to save your settings.

Read more about [configuring logging for DNS queriesï»¿](https://dt-url.net/qt437wq).

### DNS log content in EKS

Let's go through why you need both CoreDNS logs and Route53 logs with some log content.

* In **CoreDNS**, the query logs are stored in the following format by default:

  ```
  172.31.47.132:40395 - 23683 "A IN www.dynatrace.com. udp 35 false 512" NOERROR qr,rd,ra 278 0.002157881s
  ```

  The log record contains:

  + the source IP address and port
  + an ID of the request
  + request type and class
  + query itself
  + some other details about the response, such as the response code, flags, and the size of the response

  The fields can be configured to some extent.

  Read more about the [CoreDNS custom log formatï»¿](https://dt-url.net/iu037ap).
* **Route53** logs are stored in the following JSON structure:

  ```
  {



  "version":"1.100000","account_id":"<id>","region":"us-east-1","vpc_id":"vpc-<id>",



  "query_timestamp":"2023-11-20T21:20:29Z","query_name":"www.dynatrace.com.","query_type":"A",



  "query_class":"IN","rcode":"NOERROR","answers":[{"Rdata":"52.3.5.163","Type":"A","Class":"IN"}],



  "srcaddr":"172.31.73.143","srcport":"51217","transport":"UDP","srcids":{"instance":"i-<id>"}



  }
  ```

  From the example above, we can see that Route53 logs contain far more details about the DNS query, including detailed content of the response data, which is needed for threat hunting. Note that we donât have the pods' IP address in Route53 logs: we can only see that an EKS Node has tried to resolve this host. Therefore, if you want to pinpoint the exact pod that's creating malicious DNS traffic, Route53 logs would not be enough.

In CoreDNS logs we can find information about the request origin (pods' IP and source port), but the logs don't contain any information about the response payload.

To find an infected process that is getting its commands from an external server via DNS responses, threat hunting is required. To perform it precisely, we need to analyze both of those logs and correlate them as needed.

## Stream logs to Dynatrace

The easiest way to ingest logs into Dynatrace is via [Amazon Data Firehose integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.").

To configure it in AWS CloudShell, perform the following actions:

```
# setting the environment in CLI



TARGET_URL=<your_environment_URL>



TARGET_API_TOKEN=dt0c01.*****



STACK_NAME=dynatrace-log-delivery-stream



wget -O dynatrace-firehose-log-stream.yaml https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-log-stream.yaml



aws cloudformation deploy --capabilities CAPABILITY_NAMED_IAM --template-file ./dynatrace-firehose-log-stream.yaml --stack-name $STACK_NAME --parameter-overrides DtApiUrl=$DYNATRACE_API_URL DtApiToken=$DYNATRACE_API_KEY
```

To configure CloudWatch Logs log groups to be forwarded to Dynatrace, use the following command, both for the EKS clusters' CloudWatch Logs log group and for the log group youâre storing the Route53 logs.

```
wget -O dynatrace-firehose-logs.sh https://assets.cloud.dynatrace.com/awslogstreaming/dynatrace-firehose-logs.sh && chmod +x dynatrace-firehose-logs.sh



./dynatrace-firehose-logs.sh subscribe --log-groups <log-group-name> --stack-name $STACK_NAME
```

To see your CloudWatch Logs log group in Dynatrace, use the following DQL script in your tenant.

```
fetch logs



| filter aws.log_group == "<log-group-name>"
```