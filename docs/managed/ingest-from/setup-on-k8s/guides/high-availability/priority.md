---
title: Use priorityClass for critical Dynatrace components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/high-availability/priority
scraped: 2026-05-12T12:09:28.023605
---

# Use priorityClass for critical Dynatrace components

# Use priorityClass for critical Dynatrace components

* 1-min read
* Published Jul 28, 2023

Starting with Dynatrace Operator version 0.8.0+, a `priorityClass` object is created by default when installing the Dynatrace Operator. This priority class is initially set to a high value to ensure that the components that use it have a higher priority than other pods, and that critical components like the CSI driver are scheduled by Kubernetes. For details, see the [Kubernetes documentation on PriorityClassï»¿](https://kubernetes.io/docs/concepts/scheduling-eviction/pod-priority-preemption/#priorityclass).

You can change the default value of this parameter according to your environment and the individual use of priority classes within your cluster. Be aware that lowering the default value might impact the scheduling of the pods created by Dynatrace. `priorityClass` is used on the CSI driver pods by default, but it can also be used on OneAgent pods (see the `priorityClassName` parameter in [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.")).