---
title: Overview of Dynatrace IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-concepts
scraped: 2026-02-24T21:22:06.165616
---

# Overview of Dynatrace IAM

# Overview of Dynatrace IAM

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Jun 18, 2025

This guide outlines the key Identity and Access Management (IAM) components in Dynatrace, covering user and group management, access models, identity providers, access policies, and access tokens. These components ensure secure interactions, enable effective automation, and support seamless integration within the platform.

## Identity management

Manage user and group lifecycle operations and implement automated authentication with identity providers (IdPs).

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover the IAM user types, identity federation, and user repositories.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts "Understand the key identity concepts in Dynatrace IAM")[### Local users

Dynatrace serves as your identity store.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts#users "Understand the key identity concepts in Dynatrace IAM")[### Service users

Non-human identities interacting with services and resources.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts#service-users "Understand the key identity concepts in Dynatrace IAM")[### SAML federation

Delegate authentication through your IdP.](/docs/manage/identity-access-management/user-and-group-management/access-saml "SAML")[### SCIM

Keep your identity repositories in sync.](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM")

## Access management

Define granular user access in Dynatrace, controlling permissions to safeguard sensitive data and resources.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace manages groups and policies.](/docs/manage/identity-access-management/permission-management/access-concepts "Understand the key access concepts in Dynatrace IAM")[### Groups

Collectively manage your access configurations.](/docs/manage/identity-access-management/permission-management/access-concepts#groups "Understand the key access concepts in Dynatrace IAM")[### Policies

Define tailored permissions to access resources.](/docs/manage/identity-access-management/permission-management/access-concepts#policies "Understand the key access concepts in Dynatrace IAM")[### Policy boundaries

Scale, refine, and simplify access permissions.](/docs/manage/identity-access-management/permission-management/access-concepts#policy-boundaries "Understand the key access concepts in Dynatrace IAM")[### Policy templates

Reusable policies to regulate access control.](/docs/manage/identity-access-management/permission-management/access-concepts#policy-templates "Understand the key access concepts in Dynatrace IAM")[### Default policies

Get started with Dynatrace default policies.](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference")[### Default groups

Get started with Dynatrace default groups.](/docs/manage/identity-access-management/user-and-group-management/default-groups "Dynatrace default groups reference")

## Tokens and OAuth clients

Externalize and automate the access to Dynatrace using secure tokens.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace handles API tokens and access automation.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/token-concepts "Understand the key API access and automation in Dynatrace IAM")[### Platform tokens

Allow interactions with the Dynatrace platform.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.")[### OAuth tokens

Access Dynatrace through OAuth clients.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.")