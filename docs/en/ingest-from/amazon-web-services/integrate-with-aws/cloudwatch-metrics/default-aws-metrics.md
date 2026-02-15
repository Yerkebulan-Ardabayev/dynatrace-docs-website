---
title: Classic (formerly 'built-in') AWS metrics
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/default-aws-metrics
scraped: 2026-02-15T09:10:00.154569
---

# Classic (formerly 'built-in') AWS metrics

# Classic (formerly 'built-in') AWS metrics

* Reference
* 1-min read
* Updated on Jan 29, 2024

For information about differences between classic services and other services, see [Migrate from AWS classic (formerly 'built-in') services to cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Migrate AWS classic services to their new versions.").

The table below lists all AWS metrics that Dynatrace collects by default when you enable [AWS monitoring](/docs/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Monitor AWS with Dynatrace").

For all other metrics collected by Dynatrace per configurable AWS service, see the [cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") pages.

| Metric key | Name | Unit | Aggregations |
| --- | --- | --- | --- |
| builtin:cloud.aws.alb.connections.active | ALB number of active connections | Count | autoavgmaxmin |
| builtin:cloud.aws.alb.connections.new | ALB number of new connections | Count | autovalue |
| builtin:cloud.aws.alb.errors.alb.http4xx | ALB number of 4XX errors | Count | autovalue |
| builtin:cloud.aws.alb.errors.alb.http5xx | ALB number of 5XX errors | Count | autovalue |
| builtin:cloud.aws.alb.errors.target.http4xx | ALB number of 4XX target errors | Count | autovalue |
| builtin:cloud.aws.alb.errors.target.http5xx | ALB number of 5XX target errors | Count | autovalue |
| builtin:cloud.aws.alb.errors.rejCon | ALB number of rejected connections | Count | autovalue |
| builtin:cloud.aws.alb.errors.targConn | ALB number of target connection errors | Count | autovalue |
| builtin:cloud.aws.alb.errors.tlsNeg | ALB number of client TLS negotiation errors | Count | autovalue |
| builtin:cloud.aws.alb.bytes | ALB number of processed bytes | Count | autovalue |
| builtin:cloud.aws.alb.lcus | ALB number of consumed LCUs | Count | autovalue |
| builtin:cloud.aws.alb.requests | ALB number of requests | Count | autovalue |
| builtin:cloud.aws.alb.respTime | ALB target response time | Second | autoavgmaxmin |
| builtin:cloud.aws.asg.running | Number of running EC2 instances (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.asg.stopped | Number of stopped EC2 instances (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.asg.terminated | Number of terminated EC2 instances (ASG) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.running | Number of running EC2 instances (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.stopped | Number of stopped EC2 instances (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.az.terminated | Number of terminated EC2 instances (AZ) | Count | autoavgmaxmin |
| builtin:cloud.aws.dynamo.capacityUnits.consumed.read | DynamoDB read capacity units | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.consumed.write | DynamoDB write capacity units | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.provisioned.read | DynamoDB provisioned read capacity units | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.provisioned.write | DynamoDB provisioned write capacity units | Count | autovalue |
| builtin:cloud.aws.dynamo.capacityUnits.read | DynamoDB read capacity units % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.dynamo.capacityUnits.write | DynamoDB write capacity units % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.dynamo.errors.system | DynamoDB number of requests with HTTP 500 status code | Count | autovalue |
| builtin:cloud.aws.dynamo.errors.user | DynamoDB number of requests with HTTP 400 status code | Count | autovalue |
| builtin:cloud.aws.dynamo.requests.latency | DynamoDB number of successful request latency for operation | Millisecond | autoavgmaxmin |
| builtin:cloud.aws.dynamo.requests.returnedItems | DynamoDB number of items returned by operation | Count | autovalue |
| builtin:cloud.aws.dynamo.requests.throttled | DynamoDB number of throttled requests for operation | Count | autovalue |
| builtin:cloud.aws.dynamo.throttledEvents.read | DynamoDB number of read throttled events | Count | autovalue |
| builtin:cloud.aws.dynamo.throttledEvents.write | DynamoDB number of write throttled events | Count | autovalue |
| builtin:cloud.aws.dynamo.tables | Number of tables for AvailabilityZone | Count | autoavgmaxmin |
| builtin:cloud.aws.ebs.latency.read | EBS volume read latency | Second | autoavgmaxmin |
| builtin:cloud.aws.ebs.latency.write | EBS volume write latency | Second | autoavgmaxmin |
| builtin:cloud.aws.ebs.ops.consumed | EBS volume consumed OPS | Per second | autovalue |
| builtin:cloud.aws.ebs.ops.read | EBS volume read OPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.ops.write | EBS volume write OPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.percent | EBS volume throughput % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.read | EBS volume read throughput | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.throughput.write | EBS volume write throughput | Per second | autoavgmaxmin |
| builtin:cloud.aws.ebs.idleTime | EBS volume idle time % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ebs.queue | EBS volume queue length | Count | autoavgmaxmin |
| builtin:cloud.aws.ec2.cpu.usage | EC2 CPU usage % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.readOps | EC2 instance storage read IOPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.readRate | EC2 instance storage read rate | kB/s | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.writeOps | EC2 instance storage write IOPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.ec2.disk.writeRate | EC2 instance storage write rate | kB/s | autoavgmaxmin |
| builtin:cloud.aws.ec2.net.rx | EC2 network data received rate | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.ec2.net.tx | EC2 network data transmitted rate | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.elb.errors.backend.connection | CLB backend connection errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http2xx | CLB number of backend 2XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http3xx | CLB number of backend 3XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http4xx | CLB number of backend 4XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.backend.http5xx | CLB number of backend 5XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.elb.http4xx | CLB number of 4XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.elb.http5xx | CLB number of 5XX errors | Count | autovalue |
| builtin:cloud.aws.elb.errors.frontend | CLB frontend errors percentage | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.elb.hosts.healthy | CLB number of healthy hosts | Count | autoavgmaxmin |
| builtin:cloud.aws.elb.hosts.unhealthy | CLB number of unhealthy hosts | Count | autoavgmaxmin |
| builtin:cloud.aws.elb.latency | CLB latency | Second | autoavgmaxmin |
| builtin:cloud.aws.elb.reqCompl | CLB number of completed requests | Count | autovalue |
| builtin:cloud.aws.lambda.concExecutions | LambdaFunction concurrent executions count | Count | autoavgcountmaxminsum |
| builtin:cloud.aws.lambda.duration | LambdaFunction code execution time. | Millisecond | autoavgcountmaxminsum |
| builtin:cloud.aws.lambda.errors | LambdaFunction number of failed invocations with HTTP 4XX status code | Count | autovalue |
| builtin:cloud.aws.lambda.errorsRate | LambdaFunction rate of failed invocations to all invocations % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.lambda.invocations | LambdaFunction number of times a function is invoked | Count | autovalue |
| builtin:cloud.aws.lambda.provConcExecutions | LambdaFunction provisioned concurrent executions count | Count | autovalue |
| builtin:cloud.aws.lambda.provConcInvocations | LambdaFunction provisioned concurrency invocation count | Count | autovalue |
| builtin:cloud.aws.lambda.provConcSpilloverInvocations | LambdaFunction provisioned concurrency spillover invocation count | Count | autovalue |
| builtin:cloud.aws.lambda.throttlers | LambdaFunction throttled function invocation count | Count | autovalue |
| builtin:cloud.aws.nlb.flow.active | NLB number of active flows | Count | autoavgmaxmin |
| builtin:cloud.aws.nlb.flow.new | NLB number of new flows | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.client | NLB number of client resets | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.elb | NLB number of resets | Count | autovalue |
| builtin:cloud.aws.nlb.tcp.reset.target | NLB number of target resets | Count | autovalue |
| builtin:cloud.aws.nlb.bytes | NLB number of processed bytes | Count | autovalue |
| builtin:cloud.aws.nlb.lcus | NLB number of consumed LCUs | Count | autovalue |
| builtin:cloud.aws.rds.cpu.usage | RDS CPU usage % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.rds.latency.read | RDS read latency | Second | autoavgmaxmin |
| builtin:cloud.aws.rds.latency.write | RDS write latency | Second | autoavgmaxmin |
| builtin:cloud.aws.rds.memory.freeable | RDS freeable memory | Byte | autoavgmaxmin |
| builtin:cloud.aws.rds.memory.swap | RDS swap usage | Byte | autoavgmaxmin |
| builtin:cloud.aws.rds.net.rx | RDS network received throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.net.tx | RDS network transmitted throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.ops.read | RDS read IOPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.rds.ops.write | RDS write IOPS | Per second | autoavgmaxmin |
| builtin:cloud.aws.rds.throughput.read | RDS read throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.throughput.write | RDS write throughput | Byte/second | autoavgmaxmin |
| builtin:cloud.aws.rds.connections | RDS connections | Count | autoavgmaxmin |
| builtin:cloud.aws.rds.free | RDS free storage space % | Percent (%) | autoavgmaxmin |
| builtin:cloud.aws.rds.restarts | RDS restarts | Count | autovalue |