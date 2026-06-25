---
title: Cluster API v1
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1
scraped: 2026-05-12T12:04:47.499302
---

# Cluster API v1

# Cluster API v1

* Published Nov 18, 2020

Dynatrace Managed exposes cluster-wide functionality via REST endpoints. This interactive documentation also acts as a REST client you can use to interact with Dynatrace Managed clusters.

To access the Cluster API

1. Open the Cluster Management Console.
2. Open the User menu by selecting the User icon in the upper-right corner.
3. Select **Cluster API v1**.

### Cluster

* [Get cluster information about known cluster nodes](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-info-known-servers "Learn how to use the Dynatrace API to get cluster information about known nodes.")
* [Get cluster nodes configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration "Learn how to use the Dynatrace API to get cluster nodes configuration.")
* [Configure cluster nodes responsibilities](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities "Learn how to configure cluster nodes responsibilities.")
* [Get cluster nodes configuration current status](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-current-status "Learn how to use the Dynatrace API to get cluster nodes configuration current status.")
* [Get cluster nodes configuration request status](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration-request-status "Learn how to use the Dynatrace API to get the status of cluster node configuration requests.")
* [Get details about the current cluster maintenance state](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-maintenance "Learn how to use the Dynatrace API to get details about the current cluster maintenance state.")
* [Turn on the maintenance of the cluster](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-on "Learn how to turn on the maintenance of the cluster.")
* [Turn off the maintenance of the cluster](/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-off "Learn how to turn off the maintenance of the cluster.")

### Internet proxy

* [Get cluster proxy configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration "Learn how to use the Dynatrace API to get cluster proxy configuration.")
* [Set or update cluster proxy configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration "Learn how to use the Dynatrace API to set or update cluster proxy configuration.")
* [Delete cluster proxy configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration "Learn how to use the Dynatrace API to delete cluster proxy configuration.")
* [Test cluster proxy configuration](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration "Learn how to use the Dynatrace API to test cluster proxy configuration.")
* [HA - Get proxy configurations for all data centers](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha-all "Learn how to use the Dynatrace API to get proxy configurations for all data centers in premium high availability deployments.")
* [HA - Get proxy configuration for specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to get proxy configuration for specific data center in premium high availability deployments.")
* [HA - Set or update proxy configuration for specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to set or update proxy configuration in specific data center.")
* [HA - Delete proxy configuration in specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to delete proxy configuration in specific data center.")
* [HA - Test proxy configuration from specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to test proxy configuration from specific data center.")

#### High Availability deployments

[Get proxy configurations for all data centers](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha-all "Learn how to use the Dynatrace API to get proxy configurations for all data centers in premium high availability deployments.")

[Get proxy configuration for specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to get proxy configuration for specific data center in premium high availability deployments.")

[Set or update proxy configuration for specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to set or update proxy configuration in specific data center.")

[Delete proxy configuration in specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to delete proxy configuration in specific data center.")

[Test proxy configuration from specific data center](/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration-ha "Learn how to use the Dynatrace API to test proxy configuration from specific data center.")

### Password policy

* [Get cluster password policy](/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/get-cluster-password-policy "Learn how to use the Dynatrace API to get cluster password policy.")
* [Update cluster password policy](/managed/dynatrace-api/cluster-api/cluster-api-v1/password-policy-v1/put-cluster-password-policy "Learn how to use the Dynatrace API to update cluster password policy.")

### SSL certificates

* [Get cluster SSL certificate details](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-details "Learn how to use the Dynatrace API to get cluster SSL certificate details.")
* [Get cluster SSL certificate storage status](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-storage-status "Learn how to use the Dynatrace API to get cluster SSL certificate storage status.")
* [Store cluster SSL certificate](/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status "Learn how to use the Dynatrace API to store cluster SSL certificate.")

### Users

* [Get users](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-users "Learn how to use the Dynatrace API to get a list of cluster users.")
* [Update user](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/put-update-user "Learn how to use the Dynatrace API to update cluster user.")
* [Create user](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-user "Learn how to use the Dynatrace API to create cluster user.")
* [Get user](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-user "Learn how to use the Dynatrace API to get specific cluster user.")
* [Delete user](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/delete-user "Learn how to use the Dynatrace API to delete cluster user.")
* [Create cluster user accounts](/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-users "Learn how configure multiple cluster user accounts.")

### User groups

* [Get user groups](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-user-groups "Learn how to use the Dynatrace API to get specific cluster user groups.")
* [Update user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-user-groups "Learn how to use the Dynatrace API to update cluster user group.")
* [Create user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-user-group "Learn how to use the Dynatrace API to create cluster user group.")
* [Get user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group "Learn how to use the Dynatrace API to get specific cluster user.")
* [Delete user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/delete-group "Learn how to use the Dynatrace API to delete cluster user.")
* [Create user groups](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/post-create-users-groups "Learn how configure multiple cluster user groups.")
* [Get management zones for user groups](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-groups-mz "Learn how to use the Dynatrace API to get management zone permissions for all groups.")
* [Update management zones for user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-group-mz "Learn how to use the Dynatrace API to update management zones for a single user group.")
* [Get management zones for user group](/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-group-mz "Learn how to use the Dynatrace API to get management zone permissions for specific group.")