---
title: Overview of Dynatrace IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-concepts
scraped: 2026-03-06T21:31:44.586811
---

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

Discover the IAM user types, identity federation, and user repositories.](user-and-group-management/identity-concepts.md "Understand the key identity concepts in Dynatrace IAM")### Local users

Dynatrace serves as your identity store.### Service users

Non-human identities interacting with services and resources.### SAML federation

Delegate authentication through your IdP.### SCIM

Keep your identity repositories in sync.

## Access management

Define granular user access in Dynatrace, controlling permissions to safeguard sensitive data and resources.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace manages groups and policies.](permission-management/access-concepts.md "Understand the key access concepts in Dynatrace IAM")### Groups

Collectively manage your access configurations.### Policies

Define tailored permissions to access resources.### Policy boundaries

Scale, refine, and simplify access permissions.### Policy templates

Reusable policies to regulate access control.### Default policies

Get started with Dynatrace default policies.### Default groups

Get started with Dynatrace default groups.

## Tokens and OAuth clients

Externalize and automate the access to Dynatrace using secure tokens.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace handles API tokens and access automation.](access-tokens-and-oauth-clients/token-concepts.md "Understand the key API access and automation in Dynatrace IAM")### Platform tokens

Allow interactions with the Dynatrace platform.### OAuth tokens

Access Dynatrace through OAuth clients.